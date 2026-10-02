# Protokol Verifikasi Istilah, Konsep, dan Teori

Rujukan Tahap 4. Tujuan: tidak ada saran istilah, konsep, teori, atau atribusi yang keluar tanpa dicek ke sumber kredibel terlebih dahulu.

## Apa yang Wajib Diverifikasi

1. **Istilah teknis** yang penulis pakai atau yang akan disarankan sebagai pengganti (mis. "washback effect", "الكفاية اللغوية", "penilaian autentik").
2. **Padanan antarbahasa**: apakah terjemahan istilah lazim di literatur bidangnya, bukan terjemahan harfiah buatan sendiri.
3. **Konsep dan teori**: definisi yang penulis tulis sesuai dengan sumber aslinya atau konsensus literatur.
4. **Atribusi**: "teori X dikemukakan Y (tahun)" harus benar tokoh dan tahunnya.
5. **Klaim empiris di SD**: bila penulis mengutip angka/temuan tanpa sumber, atau sumbernya diragukan.

Yang TIDAK perlu diverifikasi: kosakata umum, gaya bahasa, dan istilah yang sudah terverifikasi di sesi yang sama (catat dalam ingatan sesi agar tidak mengecek dua kali).

## Urutan Pemakaian Tool

Gunakan tool_search terlebih dahulu untuk memuat tool yang belum aktif. Urutan prioritas menurut jenis pertanyaan:

| Kebutuhan | Tool utama | Cadangan |
|---|---|---|
| Apakah istilah dipakai di literatur ilmiah + bagaimana pemakaiannya | Consensus:search | Scholar Gateway:semanticSearch |
| Definisi/penggunaan dalam artikel full-text | Scholar Gateway:semanticSearch | web_search ke jurnal terbuka (DOAJ, SINTA) |
| Bidang kesehatan/psikologi eksperimen | PubMed:search_articles | Consensus |
| Kamus otoritatif Indonesia | web_search "KBBI [kata]" lalu web_fetch kbbi.kemdikbud.go.id | Tesaurus Kemdikbud |
| Kamus/penggunaan bahasa Inggris | web_search Merriam-Webster / Cambridge | corpus (COCA) via web |
| Kamus dan i'rab bahasa Arab | web_search Almaany / المعاني، معجم الوسيط | web_fetch kamus daring lain |
| Atribusi teori dan tahun | Consensus/Scholar Gateway (artikel yang mengutip sumber primer) | web_search sumber primer |
| Istilah teknologi/AI terkini | web_search + web_fetch dokumentasi/paper primer | Context7 (bila terkait pustaka perangkat lunak) |

Prinsip hemat: satu istilah cukup satu-dua panggilan tool bila hasil pertama sudah tegas. Naskah dengan banyak istilah: kelompokkan, verifikasi hanya yang berisiko (asing, jarang, atau dicurigai salah pakai).

## Kriteria Sumber Kredibel

Terima: artikel jurnal bereputasi/terindeks, buku akademik penerbit dikenal, kamus resmi (KBBI, Merriam-Webster, معجم الوسيط), glosarium lembaga (ACTFL, CEFR, Kemdikbud), sumber primer teori.
Tolak sebagai dasar tunggal: blog anonim, konten agregator SEO, forum, jawaban AI lain, Wikipedia (boleh sebagai pintu masuk ke sumber primernya).

## Format Pelaporan

Setiap istilah yang diperiksa masuk tabel verifikasi:

| Istilah di naskah | Konteks kalimat | Status | Temuan | Sumber | Rekomendasi |
|---|---|---|---|---|---|

Status hanya tiga:
- **Terverifikasi**: istilah dan penggunaannya benar; cantumkan minimal satu sumber.
- **Perlu konfirmasi penulis**: literatur memakai istilah itu dalam makna berbeda-beda, atau ada dua padanan yang sama kuat; sajikan pilihannya dan biarkan penulis memutuskan.
- **Tidak ditemukan / diragukan**: istilah tidak muncul di literatur kredibel dengan makna tersebut; tawarkan padanan terverifikasi beserta sumbernya.

## Contoh Kasus

**Kasus 1.** Penulis: "penilaian formatif otomatis meningkatkan *washback* positif". Verifikasi via Consensus: istilah "washback" mapan dalam language testing (Alderson & Wall, 1993). Status: Terverifikasi; catat atribusi bila penulis ingin menambah sitasi.

**Kasus 2.** Penulis memakai "kesahihan muka" untuk face validity. Cek KBBI + literatur metodologi Indonesia: yang lazim "validitas muka/tampang". Status: Perlu konfirmasi; sarankan "validitas muka" dengan alasan frekuensi pemakaian di literatur.

**Kasus 3.** Penulis: "teori pemerolehan bahasa kedua Chomsky (1985)". Cek sumber: hipotesis pemerolehan-pembelajaran adalah Krashen (1982); Chomsky terkait Universal Grammar. Status: Diragukan; rekomendasikan koreksi atribusi dengan sumber primer.

## Kejujuran Saat Tool Gagal

Bila tool literatur tidak tersedia atau tidak menghasilkan apa pun, katakan apa adanya di laporan ("verifikasi terbatas pada kamus otoritatif; basis data ilmiah tidak dapat diakses saat sesi ini") dan turunkan klaim kepastian. Jangan pernah mengarang sumber atau tahun.
