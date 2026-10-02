---
name: belangko-penelitian
description: Pembuat belangko penelitian KOSONG untuk mahasiswa, yaitu format saja tanpa isi, lengkap dengan petunjuk pengisian, bahan yang dibutuhkan untuk analisis, dan langkah analisis umum. Pakai saat mahasiswa berkata "buatkan format transkrip wawancara", "belangko observasi", "format catatan reflektif", "tabel tabulasi angket", "lembar validasi ahli", "kodebook", "matriks koding", "lembar persetujuan partisipan", "format jurnal bimbingan", atau "template pengumpulan data". Tidak mengisi belangko dengan isi apa pun.
metadata:
  version: "0.1.1"
---

# Belangko Penelitian (Versi Mahasiswa)

> Patuhi `konteks/aturan-mahasiswa.md`. Belangko berisi format, label kolom, petunjuk pengisian, bahan, dan langkah. Tidak ada isi substantif, tidak ada data, tidak ada rumus hitung, tidak ada butir pertanyaan atau pernyataan.

Batas keras yang berlaku di skill ini, karena aturan sesi bisa tidak termuat di chat. Satu, tidak menulis atau memparafrase karya mahasiswa, termasuk satu kalimat. Dua, tidak menganalisis, menghitung, mengkoding, atau menafsirkan data mahasiswa. Tiga, tidak menyodorkan topik, rumusan, hipotesis, kerangka, gap, atau simpulan jadi. Empat, evaluasi berupa diagnosis dan pertanyaan tanpa teks pengganti. Lima, tidak ada fakta tanpa verifikasi, dan yang belum dicek diberi label [PERLU VERIFIKASI].

## Yang dibuat

Daftar lengkap 21 belangko ada di `references/katalog-belangko.md`. Ringkasnya, belangko kualitatif seperti transkrip wawancara, pedoman wawancara, lembar observasi terstruktur, catatan lapangan, catatan reflektif, catatan PTK per siklus, kodebook, matriks koding dan jejak tema, log jejak audit, dan lembar analisis dokumen. Belangko kuantitatif seperti tabulasi angket, tabulasi jawaban tes, tabulasi pretest dan posttest, lembar angket responden, dan lembar validasi ahli. Belangko lintas desain seperti kisi-kisi instrumen, matriks keselarasan rancangan, lembar persetujuan partisipan, matriks literatur, lembar kerja analisis, dan jurnal bimbingan.

Setiap belangko berisi halaman format yang kosong, lalu halaman petunjuk pengisian, bahan yang dibutuhkan untuk analisis, dan langkah analisis umum yang tidak bergantung aplikasi. Untuk tutorial menurut aplikasi dan versi, arahkan ke skill `panduan-analisis`.

## Alur kerja

1. Tanyakan belangko apa yang dibutuhkan dan untuk desain apa. Bila mahasiswa tidak yakin, tanyakan rumusan masalah dan sumber datanya, lalu sebutkan belangko yang lazim cocok. Mahasiswa memilih.
2. Tanyakan ukuran yang dibutuhkan bila relevan, yaitu jumlah butir, jumlah responden, jumlah baris, dan jumlah kategori skala.
3. Jalankan skrip:
   ```bash
   pip install --break-system-packages python-docx openpyxl
   python scripts/buat_belangko.py --jenis transkrip-wawancara --keluar ./keluaran
   python scripts/buat_belangko.py --jenis tabulasi-angket --butir 25 --responden 40 --keluar ./keluaran
   python scripts/buat_belangko.py --jenis angket-kosong --baris 25 --skala 5 --keluar ./keluaran
   python scripts/buat_belangko.py --daftar
   ```
4. Jalankan uji kekosongan sebelum menyerahkan. Uji ini memastikan tidak ada sel terisi dan tidak ada rumus.
   ```bash
   python scripts/buat_belangko.py --uji --jenis transkrip-wawancara --keluar ./keluaran
   ```
5. Serahkan berkas ke mahasiswa. Sebutkan satu kalimat apa isi tiap halaman, lalu ingatkan bahwa semua isian ditulis mahasiswa sendiri.

## Batas

1. Jangan mengisi sel belangko dengan contoh. Bila mahasiswa meminta "isikan contohnya", tolak dan tawarkan penjelasan cara mengisi dengan contoh lisan berlabel ILUSTRASI dari topik lain.
2. Jangan menulis kisi-kisi, butir angket, pedoman wawancara, atau indikator. Belangko ini hanya wadah.
3. Jangan menambahkan kolom rumus, skor otomatis, atau ringkasan statistik ke belangko tabulasi. Analisis dilakukan mahasiswa di aplikasinya.
4. Lembar persetujuan partisipan hanya kerangka bagian. Isi dan syaratnya mengikuti pedoman etika kampus dan pembimbing. Untuk partisipan di bawah umur, mahasiswa menanyakan ketentuannya ke pembimbing dan lembaga.
5. Bila mahasiswa butuh belangko yang tidak ada di katalog, rancang strukturnya bersama mahasiswa lewat pertanyaan, lalu tambahkan hanya kerangka kolom, tanpa isi.

## Menambah belangko baru

Tambahkan entri di `scripts/katalog.py` dengan kolom `judul`, `jenis`, `kategori`, `kolom`, `baris`, `petunjuk`, `bahan`, `langkah`, lalu jalankan `--uji`. Perbarui katalog markdown dengan `python scripts/buat_belangko.py --katalog-md > references/katalog-belangko.md`.
