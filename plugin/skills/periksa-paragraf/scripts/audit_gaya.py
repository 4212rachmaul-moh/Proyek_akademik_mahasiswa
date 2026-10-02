#!/usr/bin/env python3
"""Audit gaya tulisan akademik: tanda baca, pola penanda AI, dan struktur paragraf TS SS SD C.

Pemakaian:
    python audit_gaya.py naskah.docx            # laporan markdown ke stdout
    python audit_gaya.py naskah.md --json       # keluaran JSON
    python audit_gaya.py naskah.txt -o laporan.md

Skrip ini hanya MENDETEKSI. Perbaikan dilakukan Claude secara kontekstual,
karena pengganti tanda baca bergantung pada fungsi kalimat.
Label TS SS SD C bersifat heuristik (berbasis posisi dan keberadaan sitasi/data)
dan harus dikonfirmasi dengan membaca paragrafnya.
"""
import argparse
import json
import re
import statistics
import sys
from pathlib import Path

# ---------------------------------------------------------------- pembacaan

def baca_paragraf(path: Path):
    """Kembalikan daftar (nomor, teks) paragraf tubuh. Judul, tabel, dan baris pendek dilewati."""
    hasil = []
    if path.suffix.lower() == ".docx":
        try:
            import docx  # python-docx
        except ImportError:
            sys.exit("python-docx belum terpasang: pip install --break-system-packages python-docx")
        d = docx.Document(str(path))
        for i, p in enumerate(d.paragraphs, 1):
            gaya = (p.style.name or "").lower() if p.style is not None else ""
            teks = p.text.strip()
            if not teks:
                continue
            if any(k in gaya for k in ("heading", "title", "caption", "toc", "judul", "list")):
                continue
            hasil.append((i, teks))
    else:
        teks = path.read_text(encoding="utf-8", errors="ignore")
        blok = re.split(r"\n\s*\n", teks)
        for i, b in enumerate(blok, 1):
            b = b.strip()
            if not b or b.startswith(("#", "|", "```", ">", "- ", "* ")) or re.match(r"^\d+\.\s", b):
                continue
            hasil.append((i, " ".join(b.split())))
    # buang baris yang jelas bukan paragraf (judul tanpa titik)
    return [(n, t) for n, t in hasil if len(t.split()) >= 8 or t.endswith((".", "?"))]


SINGKATAN = [
    "dkk.", "dll.", "dsb.", "dst.", "mis.", "hlm.", "tt.", "et al.", "No.", "Vol.", "Dr.", "Prof.",
    "S.Pd.", "M.Pd.", "S.Ag.", "M.Ag.", "Ph.D.", "e.g.", "i.e.", "vs.", "cf.", "pp.", "p.", "ed.", "eds.",
    "Jl.", "H.", "K.H.", "St.", "Gr.",
]


def pecah_kalimat(teks: str):
    t = teks
    for s in SINGKATAN:
        t = t.replace(s, s.replace(".", "\u2024"))
    t = re.sub(r"(\d)\.(\d)", "\\1\u2024\\2", t)
    bagian = re.split(r"(?<=[.?!])\s+(?=[\"'\u201c(\[A-Z\u0600-\u06FF0-9])", t)
    return [b.replace("\u2024", ".").strip() for b in bagian if b.strip()]


# ---------------------------------------------------------------- pola

RE_SITASI = re.compile(
    r"\([^()]*?(?:19|20)\d{2}[a-z]?[^()]*?\)"      # (Nama, 2020) atau (2020)
    r"|\b[A-Z][A-Za-z\u00C0-\u017F'\-]+(?: (?:et al\.|dkk\.|& [A-Z][\w\-]+|dan [A-Z][\w\-]+))? \((?:19|20)\d{2}"  # Nama (2020
    r"|\[\d+(?:[,\u2013\-]\s*\d+)*\]"                 # [12] gaya IEEE/Vancouver
)
RE_DATA = re.compile(r"\d+(?:[.,]\d+)?\s?%|\b[pnrtFM]\s?[=<>]\s?[-\d.]|\bN\s?=\s?\d|\bSD\s?=|\balpha\b|\u03b1\s?=")

POLA_AI_ID = [
    "di era digital", "era globalisasi", "di era modern", "dewasa ini", "tak dapat dipungkiri",
    "tidak dapat dipungkiri", "tidak dapat disangkal", "sangat krusial", "sangat penting untuk dicatat",
    "perlu dicatat bahwa", "penting untuk dicatat", "memainkan peran penting", "memegang peranan penting",
    "memainkan peran krusial", "lanskap", "menavigasi", "secara holistik", "sinergi", "komprehensif dan",
    "dengan demikian, sudah sepatutnya", "sudah menjadi rahasia umum", "seiring dengan perkembangan zaman",
    "bukan hanya", "tidak hanya", "lebih dari sekadar", "dalam dunia yang", "mari kita", "pada akhirnya,",
    "secara keseluruhan,", "menggarisbawahi", "menyoroti pentingnya", "membuka jalan bagi",
    "berperan sebagai katalisator", "revolusioner", "transformatif", "paradigma baru",
]
POLA_AI_EN = [
    "delve", "pivotal", "crucial", "tapestry", "landscape", "foster", "leverage", "underscore",
    "it is important to note", "it is worth noting", "in today's", "ever-evolving", "fast-paced",
    "not only", "plays a vital role", "plays a crucial role", "a testament to", "navigate the",
    "in the realm of", "seamless", "holistic", "multifaceted", "shed light", "paving the way",
    "in conclusion,", "overall,", "moreover,", "furthermore,", "additionally,",
]


def cek_tanda_baca(teks: str):
    temuan = []
    tanpa_url = re.sub(r"https?://\S+|www\.\S+|doi\.org/\S+|10\.\d{4,}/\S+", " ", teks)
    # isi tanda kurung (sitasi) dihapus sementara untuk uji titik koma dan titik dua
    tanpa_kurung = re.sub(r"\([^()]*\)", " ", tanpa_url)
    if "\u2014" in teks:
        temuan.append(("em dash", teks.count("\u2014"), "DILARANG"))
    en_retoris = [m for m in re.finditer("\u2013", tanpa_url)
                  if not (m.start() > 0 and tanpa_url[m.start() - 1].isdigit()
                          and m.end() < len(tanpa_url) and tanpa_url[m.end()].isdigit())]
    if en_retoris:
        temuan.append(("en dash retoris", len(en_retoris), "DILARANG"))
    if re.search(r"\s-\s", tanpa_url):
        temuan.append(("tanda hubung berspasi sebagai pengganti dash", len(re.findall(r"\s-\s", tanpa_url)), "DILARANG"))
    if "!" in tanpa_url:
        temuan.append(("tanda seru", tanpa_url.count("!"), "DILARANG"))
    if ";" in tanpa_kurung:
        temuan.append(("titik koma di luar sitasi", tanpa_kurung.count(";"), "DILARANG"))
    elips = len(re.findall(r"\.\.\.|\u2026", tanpa_url))
    if elips:
        temuan.append(("elipsis", elips, "hindari kecuali kutipan terpotong"))
    miring = re.findall(r"(?<![\d/])\b[A-Za-z\u00C0-\u017F]+/[A-Za-z\u00C0-\u017F]+\b", tanpa_url)
    if miring:
        temuan.append(("garis miring antar kata", len(miring), "ganti dengan 'atau' / 'dan'"))
    titik_dua = re.findall(r"(?<!\d):(?!\d)", tanpa_kurung)
    if titik_dua:
        temuan.append(("titik dua dalam kalimat", len(titik_dua), "boleh hanya untuk rincian formal"))
    kurung_non_sitasi = [k for k in re.findall(r"\(([^()]*)\)", tanpa_url)
                         if not re.search(r"(?:19|20)\d{2}|hlm|p\.|pp\.|n\.d\.|t\.t\.", k)
                         and not re.fullmatch(r"[A-Z0-9\-]{2,12}", k.strip())]
    if kurung_non_sitasi:
        temuan.append(("kurung non-sitasi (sisipan)", len(kurung_non_sitasi), "pertimbangkan koma sepasang"))
    return temuan


def cek_pola_ai(teks: str):
    rendah = teks.lower()
    hasil = []
    for p in POLA_AI_ID + POLA_AI_EN:
        n = len(re.findall(r"(?<!\w)" + re.escape(p) + r"(?!\w)", rendah))
        if n:
            hasil.append((p, n))
    return hasil


def label_kalimat(kalimat):
    label = []
    n = len(kalimat)
    for i, k in enumerate(kalimat):
        ada_bukti = bool(RE_SITASI.search(k) or RE_DATA.search(k))
        if i == 0:
            label.append("TS")
        elif i == n - 1 and n >= 3:
            label.append("C")
        else:
            label.append("SD" if ada_bukti else "SS")
    return label


def diagnosis(kalimat, label):
    catatan = []
    n = len(kalimat)
    bukti = [bool(RE_SITASI.search(k) or RE_DATA.search(k)) for k in kalimat]
    if n == 1:
        catatan.append("P8 paragraf satu kalimat")
    elif n == 2:
        catatan.append("paragraf dua kalimat, komponen TS SS SD C tidak lengkap")
    if n > 8:
        catatan.append("P9 paragraf balon (>8 kalimat), cek apakah memuat dua ide")
    if bukti and bukti[0]:
        catatan.append("P1/P3 kalimat pertama berupa sitasi atau data, TS mungkin hilang atau terkubur")
    if n >= 3 and bukti[-1]:
        catatan.append("P7 kalimat penutup memuat sitasi atau data baru")
    if n >= 3 and not any(bukti[1:-1]):
        catatan.append("P5 tidak ada SD bersitasi di tengah paragraf (abaikan bila paragraf fungsional)")
    beruntun = 0
    for b in bukti[1:-1]:
        beruntun = beruntun + 1 if b else 0
        if beruntun >= 3:
            catatan.append("P4 data dumping, tiga SD berturut tanpa SS sintesis")
            break
    return catatan


def cv(nilai):
    if len(nilai) < 2 or statistics.mean(nilai) == 0:
        return 0.0
    return statistics.pstdev(nilai) / statistics.mean(nilai)


# ---------------------------------------------------------------- utama

def audit(path: Path):
    paragraf = baca_paragraf(path)
    rinci = []
    total_tb = {}
    total_ai = {}
    panjang_par, panjang_kal = [], []
    pembuka = {}
    for no, teks in paragraf:
        kal = pecah_kalimat(teks)
        lab = label_kalimat(kal)
        tb = cek_tanda_baca(teks)
        ai = cek_pola_ai(teks)
        for nama, n, _ in tb:
            total_tb[nama] = total_tb.get(nama, 0) + n
        for nama, n in ai:
            total_ai[nama] = total_ai.get(nama, 0) + n
        panjang_par.append(len(teks.split()))
        panjang_kal.extend(len(k.split()) for k in kal)
        kunci = " ".join(teks.lower().split()[:2])
        pembuka[kunci] = pembuka.get(kunci, 0) + 1
        rinci.append({
            "paragraf": no,
            "cuplikan": teks[:90] + ("..." if len(teks) > 90 else ""),
            "jumlah_kalimat": len(kal),
            "jumlah_kata": len(teks.split()),
            "pola": " ".join(lab),
            "diagnosis": diagnosis(kal, lab),
            "tanda_baca": [f"{a} ({b}x): {c}" for a, b, c in tb],
            "pola_ai": [f"{a} ({b}x)" for a, b in ai],
        })
    ringkas = {
        "berkas": str(path),
        "jumlah_paragraf": len(paragraf),
        "rerata_kata_per_paragraf": round(statistics.mean(panjang_par), 1) if panjang_par else 0,
        "cv_panjang_paragraf": round(cv(panjang_par), 2),
        "cv_panjang_kalimat": round(cv(panjang_kal), 2),
        "tanda_baca_bermasalah": total_tb,
        "pola_ai": dict(sorted(total_ai.items(), key=lambda x: -x[1])),
        "pembuka_berulang": {k: v for k, v in pembuka.items() if v >= 3},
        "peringatan_variasi": [],
    }
    if len(panjang_par) >= 5 and ringkas["cv_panjang_paragraf"] < 0.20:
        ringkas["peringatan_variasi"].append("Panjang paragraf terlalu seragam (CV < 0,20). Variasikan.")
    if len(panjang_kal) >= 10 and ringkas["cv_panjang_kalimat"] < 0.30:
        ringkas["peringatan_variasi"].append("Panjang kalimat terlalu seragam (CV < 0,30). Selingi kalimat pendek dan panjang.")
    lulus = (not any(k in total_tb for k in ("em dash", "en dash retoris", "tanda seru", "titik koma di luar sitasi",
                                              "tanda hubung berspasi sebagai pengganti dash"))
             and not ringkas["peringatan_variasi"])
    ringkas["lulus_gerbang_wajib"] = lulus
    return ringkas, rinci


def ke_markdown(ringkas, rinci):
    b = [f"# Laporan Audit Gaya: {Path(ringkas['berkas']).name}", ""]
    b.append(f"Status gerbang wajib: **{'LULUS' if ringkas['lulus_gerbang_wajib'] else 'BELUM LULUS'}**")
    b.append("")
    b.append(f"Paragraf dianalisis {ringkas['jumlah_paragraf']}, rerata {ringkas['rerata_kata_per_paragraf']} kata per paragraf, "
             f"CV panjang paragraf {ringkas['cv_panjang_paragraf']}, CV panjang kalimat {ringkas['cv_panjang_kalimat']}.")
    b.append("")
    b.append("## Tanda baca bermasalah")
    b += [f"- {k}: {v}" for k, v in ringkas["tanda_baca_bermasalah"].items()] or ["- tidak ada"]
    b.append("")
    b.append("## Pola penanda AI")
    b += [f"- {k}: {v}" for k, v in ringkas["pola_ai"].items()] or ["- tidak ada"]
    b.append("")
    b.append("## Variasi dan pembuka paragraf")
    b += [f"- {w}" for w in ringkas["peringatan_variasi"]] or ["- variasi panjang memadai"]
    b += [f"- pembuka berulang '{k}': {v} kali" for k, v in ringkas["pembuka_berulang"].items()]
    b.append("")
    b.append("## Rincian per paragraf (label heuristik, konfirmasi dengan membaca)")
    b.append("")
    b.append("| No | Kalimat | Kata | Pola | Diagnosis | Tanda baca | Pola AI |")
    b.append("|---|---|---|---|---|---|---|")
    for r in rinci:
        b.append(f"| {r['paragraf']} | {r['jumlah_kalimat']} | {r['jumlah_kata']} | {r['pola']} | "
                 f"{'; '.join(r['diagnosis']) or 'sehat'} | {'; '.join(r['tanda_baca']) or '-'} | {'; '.join(r['pola_ai']) or '-'} |")
    return "\n".join(b)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("berkas")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("-o", "--output")
    a = ap.parse_args()
    ringkas, rinci = audit(Path(a.berkas))
    keluaran = json.dumps({"ringkasan": ringkas, "rincian": rinci}, ensure_ascii=False, indent=2) if a.json \
        else ke_markdown(ringkas, rinci)
    if a.output:
        Path(a.output).write_text(keluaran, encoding="utf-8")
        print(f"Laporan ditulis ke {a.output}")
    else:
        print(keluaran)
    sys.exit(0 if ringkas["lulus_gerbang_wajib"] else 1)


if __name__ == "__main__":
    main()
