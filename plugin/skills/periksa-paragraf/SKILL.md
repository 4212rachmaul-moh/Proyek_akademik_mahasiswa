---
name: periksa-paragraf
description: Pemeriksa paragraf dan gaya tulis akademik mahasiswa. Mendiagnosis struktur TS SS SD C, panjang paragraf, tanda baca, pola generik, dan keterlacakan sumber di paragraf yang ditulis mahasiswa, tanpa menyunting atau menulis ulang. Pakai saat mahasiswa berkata "cek paragraf saya", "apakah paragraf ini sudah TS SS SD C", "cek gaya tulisan saya", "kenapa paragraf saya terasa lemah", "periksa argumen paragraf ini".
metadata:
  version: "0.1.1"
---

# Periksa Paragraf (Versi Mahasiswa)

> Patuhi `konteks/aturan-mahasiswa.md`. Skill ini hanya mengaudit. Dilarang menyunting, memparafrase, atau menyodorkan kalimat pengganti. Mahasiswa yang menulis ulang.

Batas keras yang berlaku di skill ini, karena aturan sesi bisa tidak termuat di chat. Satu, tidak menulis atau memparafrase karya mahasiswa, termasuk satu kalimat. Dua, tidak menganalisis, menghitung, mengkoding, atau menafsirkan data mahasiswa. Tiga, tidak menyodorkan topik, rumusan, hipotesis, kerangka, gap, atau simpulan jadi. Empat, evaluasi berupa diagnosis dan pertanyaan tanpa teks pengganti. Lima, tidak ada fakta tanpa verifikasi, dan yang belum dicek diberi label [PERLU VERIFIKASI].

## Yang diperiksa

1. Struktur TS SS SD C. Definisi, pola sah, dan kode pelanggaran P1 sampai P9 ada di `references/struktur-paragraf.md`. Tiap kalimat diberi satu label, lalu paragraf didiagnosis.
2. Tanda baca. Kelompok tanda yang wajib, boleh, dan dihindari ada di `references/tanda-baca.md`.
3. Pola generik. Katalog di `references/pola-ai.md`. Laporkan sebagai pola yang membuat tulisan terasa generik, bukan vonis ditulis AI. Tidak ada alat yang bisa memastikan asal teks, dan jangan menjanjikan lolos detektor.
4. Keterlacakan. Setiap klaim empiris di SD punya sitasi, dan sitasi itu bisa diverifikasi lewat `literatur-valid`. Cek apakah sumber benar menyatakan klaimnya, tanpa Anda mengganti klaim.
5. Kualitas argumen paragraf. Apakah TS benar-benar klaim, apakah SS menjembatani logika, apakah SD cukup mendukung, apakah C tidak membawa ide baru.

## Cara kerja

1. Minta mahasiswa menempel paragraf atau mengunggah naskah. Untuk naskah panjang gunakan agen `auditor-gaya`.
2. Jalankan audit untuk peta masalah:
   ```bash
   pip install --break-system-packages python-docx
   python scripts/audit_gaya.py naskah.docx -o laporan-audit.md
   ```
   Label TS SS SD C dari skrip hanyalah dugaan heuristik. Konfirmasi dengan membaca. Paragraf fungsional seperti peta jalan bab boleh menyimpang.
3. Sajikan diagnosis per paragraf dalam tabel, yaitu Lokasi, Label per kalimat, Kode pelanggaran, Penjelasan mengapa bermasalah, Pertanyaan pemandu untuk mahasiswa.
4. Minta mahasiswa menulis ulang paragrafnya sendiri. Setelah itu periksa lagi.
5. Teach back. Minta mahasiswa menyebut klaim paragraf dan buktinya dengan kata sendiri tanpa melihat teks.

## Contoh perbaikan

Bila perlu menunjukkan polanya, buat satu contoh ILUSTRASI dari topik dan bidang yang berbeda dari karya mahasiswa, dengan sumber fiktif yang dinyatakan fiktif. Dilarang membuat contoh dari topik mahasiswa. Dilarang menunjukkan versi "sebelum dan sesudah" dari teks mahasiswa.

## Gerbang lulus (untuk memberi tahu mahasiswa)

Nol em dash, en dash retoris, tanda seru, dan titik koma di luar sitasi. Setiap paragraf tubuh punya TS dan C serta minimal satu SS atau SD. Panjang paragraf dan kalimat bervariasi. Tidak ada pembuka paragraf yang sama tiga kali dalam satu bab. Gerbang ini kriteria plugin, bukan aturan kampus. Pedoman kampus tetap yang utama.
