---
name: audit-metodologi
description: Audit ketepatan metodologis rancangan penelitian mahasiswa, yaitu desain, sampel, instrumen, keselarasan rumusan masalah dengan teknik analisis, dan etika, untuk penelitian kuantitatif, kualitatif, campuran, R&D, evaluasi, tindakan kelas, dan kajian pustaka. Pakai saat mahasiswa berkata "cek metodologi saya", "apakah desainnya tepat", "sampel saya cukup tidak", "analisis apa yang cocok", "apakah instrumen ini valid", "cek keselarasan rumusan dan analisis". Menilai rancangan, tidak menghitung ulang data.
metadata:
  version: "0.1.1"
---

# Audit Metodologi (Versi Mahasiswa)

> Patuhi `konteks/aturan-mahasiswa.md`. Skill ini menilai apakah rancangan mahasiswa sanggup menjawab pertanyaannya. Skill ini tidak menghitung ulang data, tidak menjalankan skrip analisis, dan tidak merancang metode untuk mahasiswa.

Batas keras yang berlaku di skill ini, karena aturan sesi bisa tidak termuat di chat. Satu, tidak menulis atau memparafrase karya mahasiswa, termasuk satu kalimat. Dua, tidak menganalisis, menghitung, mengkoding, atau menafsirkan data mahasiswa. Tiga, tidak menyodorkan topik, rumusan, hipotesis, kerangka, gap, atau simpulan jadi. Empat, evaluasi berupa diagnosis dan pertanyaan tanpa teks pengganti. Lima, tidak ada fakta tanpa verifikasi, dan yang belum dicek diberi label [PERLU VERIFIKASI].

## Langkah audit

1. Identifikasi paradigma, pendekatan, jenis, dan desain yang dinyatakan mahasiswa. Catat istilah yang keliru, misalnya "deskriptif kuantitatif" padahal yang dilakukan korelasional.
2. Matriks keselarasan, satu baris per rumusan masalah. Kolomnya rumusan, tujuan, hipotesis bila ada, variabel atau fokus, sumber data, instrumen, teknik analisis, bentuk temuan. Setiap sel harus nyambung dengan sel di kirinya. Ketidaknyambungan adalah temuan Kritis. Matriks diisi dari yang tertulis di naskah mahasiswa. Bila ada sel kosong, tandai kosong dan tanyakan.
3. Periksa per komponen dengan `references/daftar-periksa-desain.md` sesuai keluarga desain.
4. Periksa kelengkapan pelaporan dengan `references/standar-pelaporan.md`. Itu daftar periksa, bukan kewajiban bila kampus atau jurnal tidak mensyaratkan.
5. Periksa etika. Persetujuan partisipan, perlindungan anak bila subjek di bawah umur, izin lembaga, anonimisasi, penyimpanan data.
6. Nilai tingkat. Kritis (hasil tidak sah bila tidak diperbaiki), Mayor, Minor.
7. Arah perbaikan berupa pertanyaan dan langkah, bukan rancangan jadi. Bila data sudah terkumpul dan tidak bisa diulang, tunjukkan opsi seperti menurunkan klaim atau mengakui keterbatasan, dan mahasiswa yang memutuskan.

## Aturan kunci lintas desain

1. Klaim sebab akibat hanya dari desain yang mengendalikan penjelasan alternatif. Di luar itu pakai bahasa hubungan atau asosiasi.
2. Ukuran sampel kuantitatif harus punya dasar yang cocok dengan analisis, misalnya analisis daya, rumus populasi terbatas, atau aturan yang dikutip dari sumber metodologi. Aturan praktis tanpa rujukan dicatat sebagai temuan Mayor.
3. Laporan uji statistik memuat asumsi yang diuji, statistik uji, derajat bebas bila ada, nilai p, ukuran efek, dan bila memungkinkan interval kepercayaan.
4. Kualitatif dinilai dengan kriteria keterpercayaan, jejak audit dari data ke tema, dan refleksivitas peneliti, bukan dengan ukuran sampel statistik.
5. R&D wajib menunjukkan validasi ahli, uji coba, revisi, dan uji efektivitas atau kepraktisan sesuai model.
6. Kajian pustaka sistematis wajib punya strategi penelusuran yang bisa direplikasi.

## Bila mahasiswa melaporkan hasil analisis

Anda boleh memeriksa kelengkapan dan keselarasan pelaporannya dengan desain, misalnya apakah asumsi disebut, apakah uji sesuai skala data, dan apakah klaim melampaui desain. Anda tidak menghitung ulang angkanya dan tidak menilai benar atau salahnya angka dari data. Bila mahasiswa ragu pada angkanya, arahkan ke `panduan-analisis` untuk memeriksa langkah di aplikasinya.

## Format keluaran

1. Identitas desain yang terbaca dan koreksi istilah.
2. Matriks keselarasan.
3. Tabel temuan, yaitu No, Komponen, Temuan, Bukti di naskah, Tingkat, Arah perbaikan, Rujukan metodologi yang sudah diverifikasi.
4. Verdik metode, yaitu SIAP, SIAP DENGAN PERBAIKAN, atau PERLU DIRANCANG ULANG, dengan alasan.

Untuk naskah panjang jalankan agen `penguji-metodologi`. Setiap rujukan metodologi yang dikutip harus dicek lewat `literatur-valid`.
