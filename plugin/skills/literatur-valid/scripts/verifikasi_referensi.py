#!/usr/bin/env python3
"""Verifikasi referensi ke Crossref dan OpenAlex (tanpa kunci API).

Masukan: berkas teks berisi satu referensi per baris (DOI, URL doi.org, atau
string referensi lengkap), atau DOI langsung lewat --doi.

    python verifikasi_referensi.py daftar_pustaka.txt -o hasil.md
    python verifikasi_referensi.py --doi 10.3389/fpsyg.2019.03087

Untuk tiap referensi dilaporkan:
  - status: COCOK, PERLU CEK (metadata beda), TIDAK DITEMUKAN, GAGAL AKSES
  - metadata resmi (judul, penulis pertama, tahun, jurnal, DOI)
  - tanda retraksi dari OpenAlex (is_retracted)
Status TIDAK DITEMUKAN tidak otomatis berarti fiktif (buku lokal, jurnal
non-DOI, dan Garuda sering tidak terindeks). Tindak lanjuti dengan web search.
Skrip tidak pernah mengisi metadata dari tebakan.
"""
import argparse
import difflib
import json
import re
import sys
import time
import urllib.parse
import urllib.request

UA = "akademik-terpadu-plugin/0.1 (verifikasi referensi; mailto:anonymous@example.org)"
RE_DOI = re.compile(r"10\.\d{4,9}/[^\s\"<>]+", re.I)


def ambil_json(url, jeda=0.2):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            data = json.loads(r.read().decode("utf-8"))
        time.sleep(jeda)
        return data, None
    except urllib.error.HTTPError as e:
        return None, f"HTTP {e.code}"
    except Exception as e:  # jaringan diblokir, timeout, dll.
        return None, type(e).__name__


def norm(s):
    return re.sub(r"[^a-z0-9؀-ۿ ]", "", (s or "").lower()).strip()


def mirip(a, b):
    return difflib.SequenceMatcher(None, norm(a), norm(b)).ratio()


def dari_crossref_item(it):
    penulis = it.get("author") or []
    return {
        "judul": (it.get("title") or [""])[0],
        "penulis_pertama": (penulis[0].get("family") or penulis[0].get("name", "")) if penulis else "",
        "tahun": ((it.get("issued") or {}).get("date-parts") or [[None]])[0][0],
        "wadah": (it.get("container-title") or [""])[0],
        "doi": it.get("DOI", ""),
        "jenis": it.get("type", ""),
    }


def cek_openalex(doi):
    data, err = ambil_json("https://api.openalex.org/works/doi:" + urllib.parse.quote(doi)
                           + "?select=id,display_name,publication_year,is_retracted,primary_location")
    if not data:
        return {"openalex": err or "tidak ditemukan"}
    sumber = ((data.get("primary_location") or {}).get("source") or {})
    return {"openalex_id": data.get("id"), "retraksi": bool(data.get("is_retracted")),
            "openalex_sumber": sumber.get("display_name")}


def verifikasi_doi(doi):
    doi = doi.rstrip(".,;)")
    data, err = ambil_json("https://api.crossref.org/works/" + urllib.parse.quote(doi))
    if err and err.startswith("HTTP 404"):
        oa = cek_openalex(doi)
        if "openalex_id" in oa:
            return {"status": "PERLU CEK", "catatan": "DOI tidak ada di Crossref tetapi ada di OpenAlex", **oa}
        return {"status": "TIDAK DITEMUKAN", "catatan": "DOI tidak terdaftar di Crossref maupun OpenAlex"}
    if not data:
        return {"status": "GAGAL AKSES", "catatan": err}
    meta = dari_crossref_item(data["message"])
    return {"status": "COCOK", **meta, **cek_openalex(meta["doi"])}


def verifikasi_teks(ref):
    q = urllib.parse.quote(ref[:300])
    data, err = ambil_json(f"https://api.crossref.org/works?query.bibliographic={q}&rows=3")
    if not data:
        return {"status": "GAGAL AKSES", "catatan": err}
    kandidat = [dari_crossref_item(it) for it in data["message"].get("items", [])]
    if not kandidat:
        return {"status": "TIDAK DITEMUKAN", "catatan": "tidak ada kandidat di Crossref"}
    terbaik = max(kandidat, key=lambda k: mirip(k["judul"], ref) + (0.3 if norm(k["penulis_pertama"]) in norm(ref) else 0))
    skor_judul = max(mirip(terbaik["judul"], potong) for potong in re.split(r"[.?]\s", ref) if potong) if ref else 0
    tahun_ok = str(terbaik["tahun"]) in ref if terbaik["tahun"] else False
    penulis_ok = bool(terbaik["penulis_pertama"]) and norm(terbaik["penulis_pertama"]) in norm(ref)
    if skor_judul >= 0.85 and tahun_ok and penulis_ok:
        status = "COCOK"
    elif skor_judul >= 0.6:
        status = "PERLU CEK"
    else:
        status = "TIDAK DITEMUKAN"
    if status == "TIDAK DITEMUKAN":
        return {"status": status, "catatan": f"kandidat terdekat tidak cocok (skor judul {round(skor_judul, 2)})"}
    hasil = {"status": status, "skor_judul": round(skor_judul, 2), "tahun_cocok": tahun_ok,
             "penulis_cocok": penulis_ok, **terbaik}
    if status != "TIDAK DITEMUKAN" and terbaik["doi"]:
        hasil.update(cek_openalex(terbaik["doi"]))
    return hasil


def proses(baris):
    m = RE_DOI.search(baris)
    if not m:
        return verifikasi_teks(baris)
    h = verifikasi_doi(m.group(0))
    sisa = RE_DOI.sub("", baris).replace("https://doi.org/", "").strip()
    # bila baris juga memuat teks referensi, pastikan DOI memang milik referensi itu
    if h["status"] == "COCOK" and len(sisa) > 40:
        skor = max(mirip(h["judul"], p) for p in re.split(r"[.?]\s", sisa) if p)
        tahun_ok = bool(h.get("tahun")) and str(h["tahun"]) in sisa
        if skor < 0.85 or not tahun_ok:
            h["status"] = "PERLU CEK"
            h["catatan"] = f"DOI valid tetapi metadata tidak cocok dengan teks referensi (skor judul {round(skor, 2)}, tahun {'ya' if tahun_ok else 'tidak'})"
    return h


def ke_markdown(hasil):
    out = ["# Hasil Verifikasi Referensi", "",
           "| No | Status | Retraksi | Referensi masukan | Metadata resmi | Catatan |", "|---|---|---|---|---|---|"]
    for i, (ref, h) in enumerate(hasil, 1):
        meta = ""
        if h.get("judul"):
            meta = f"{h.get('penulis_pertama','')} ({h.get('tahun','')}). {h.get('judul','')}. {h.get('wadah','')}. doi:{h.get('doi','')}"
        catatan = h.get("catatan", "")
        if "skor_judul" in h:
            catatan += f" skor judul {h['skor_judul']}, tahun {'ya' if h['tahun_cocok'] else 'tidak'}, penulis {'ya' if h['penulis_cocok'] else 'tidak'}"
        out.append(f"| {i} | {h['status']} | {'YA' if h.get('retraksi') else '-'} | {ref[:120].replace('|','/')} | {meta.replace('|','/')} | {catatan.strip()} |")
    ringkas = {}
    for _, h in hasil:
        ringkas[h["status"]] = ringkas.get(h["status"], 0) + 1
    out += ["", "Ringkasan: " + ", ".join(f"{k} {v}" for k, v in ringkas.items())]
    if any(h["status"] == "GAGAL AKSES" for _, h in hasil):
        out.append("Catatan: sebagian gagal diakses (jaringan dibatasi). Verifikasi ulang lewat konektor riset atau web search.")
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("berkas", nargs="?")
    ap.add_argument("--doi", action="append", default=[])
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-o", "--output")
    a = ap.parse_args()
    refs = list(a.doi)
    if a.berkas:
        with open(a.berkas, encoding="utf-8") as f:
            refs += [b.strip() for b in f if len(b.strip()) > 8]
    if not refs:
        sys.exit("Tidak ada referensi. Beri berkas atau --doi.")
    hasil = [(r, proses(r)) for r in refs]
    keluaran = json.dumps([{"referensi": r, **h} for r, h in hasil], ensure_ascii=False, indent=2) if a.json else ke_markdown(hasil)
    if a.output:
        open(a.output, "w", encoding="utf-8").write(keluaran)
        print(f"Hasil ditulis ke {a.output}")
    else:
        print(keluaran)


if __name__ == "__main__":
    main()
