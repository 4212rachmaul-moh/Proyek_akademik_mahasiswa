# Rubrik Proposal dan Skripsi FITK UIN Siber Syekh Nurjati Cirebon (Versi Mahasiswa)

Diadaptasi dari skill review-proposal-skripsi-pjj milik pengguna. Berlaku untuk program reguler maupun PJJ. Cocokkan dengan pedoman fakultas terbaru bila diunggah.

Rubrik ini dipakai untuk penilaian formatif yang membangun, kritis, dan mendidik. Tujuannya bukan menulis ulang karya mahasiswa. Temuan dilaporkan dalam tabel dan catatan, dengan lokasi yang jelas, tanpa kalimat pengganti.

## Alur Kerja

1. Identifikasi format file dan jenis dokumen (proposal atau skripsi), judul, dan jurusan. Jurusan menentukan apakah ketentuan abstrak Arab dan 20 sumber Arab berlaku, yang khusus Pendidikan Bahasa Arab.
2. Analisis per aspek sesuai enam kompetensi di bawah. Baca paragraf demi paragraf, terutama BAB I sampai III.
3. Susun laporan sesuai format di bagian akhir.
4. Tawarkan asistensi lanjutan berupa pertanyaan pemandu dan arah. Mahasiswa yang menulis ulang.

## Kompetensi Penilaian

### 1. Struktur Paragraf Akademik
Untuk setiap paragraf penting (terutama BAB I-III), cek:
- **TS (Topic Sentence):** ide utama, lazimnya di awal paragraf, tepat satu.
- **SS (Supporting Sentence):** penjelas logika dari TS, boleh lebih dari satu.
- **SD (Supporting Detail/Data):** sintesis literatur (jurnal atau buku) atau data bersitasi, boleh lebih dari satu.
- **C (Concluding Sentence):** simpulan kecil atau transisi, tepat satu.
Pola sah: TS SS SD C, TS SS SD1 SD2 C, TS SS1 SD SS2 SD C. Diagnosis pelanggaran memakai kode P1 sampai P9 di skill `periksa-paragraf` (`references/struktur-paragraf.md`). Jalankan `scripts/audit_gaya.py` untuk peta cepat.

Saat menemukan paragraf bermasalah, catat dalam tabel temuan dengan format:
```
Kekuatan: [sebutkan]
Kelemahan: [sebutkan]
Arah: [pertanyaan atau langkah untuk mahasiswa, bukan kalimat pengganti]
```

### 2. Alur Logika
Periksa koherensi:
- Latar belakang → identifikasi masalah → rumusan masalah (logis?)
- Teori → indikator → kerangka pemikiran → hipotesis/fokus (koheren?)
- Metode → indikator → instrumen → analisis data (konsisten?)
- Hasil → pembahasan → simpulan (selaras, khusus skripsi)

Untuk setiap bab, beri nilai Sangat Baik/Baik/Cukup/Kurang dengan penjelasan singkat dan rekomendasi perbaikan.

### 3. Gramatika
- **Bahasa Arab** (jika ada abstrak/kutipan Arab): i'rab (إعراب), susunan jumlah ismiyyah & fi'liyyah, penggunaan adawat (أدوات), tashrif kata kerja/benda
- **Bahasa Indonesia:** struktur SPO/SPOK, kata baku (sesuai KBBI), ejaan EYD V (huruf kapital, kata depan, tanda baca), kalimat efektif (tidak ambigu, tidak bertele-tele)

Beri skor masing-masing dari 10, dengan daftar kesalahan utama beserta perbaikannya.

### 4. Terminologi Akademik
Cek konsistensi istilah pendidikan/penelitian dalam tiga bahasa:

| Indonesia | Arab | Transliterasi |
|---|---|---|
| pendidikan/pengajaran | تعليم | ta'līm |
| pendidikan (formatif) | تربية | tarbiyah |
| pengajaran | تدريس | tadrīs |
| metode | طريقة | ṭarīqah |
| kurikulum/program | منهج | manhaj |
| pendekatan/gaya | أسلوب | uslūb |
| keterampilan | مهارة | mahārah |
| penelitian | بحث | baḥṡ |
| studi/kajian | دراسة | dirāsah |
| analisis | تحليل | taḥlīl |

Checklist:
- Konsistensi transliterasi (mis. selalu "ta'līm", bukan campur "ta'lim"/"ta'līm")
- Istilah Arab ditulis miring (italic) saat pertama kali muncul
- Padanan Indonesia-Arab-Inggris konsisten di seluruh dokumen
- Tidak ada istilah asing yang tidak perlu/berlebihan

### 5. Verifikasi Sumber/Daftar Pustaka
Catatan. Rubrik ini menilai komposisi sumber menurut pedoman fakultas. Untuk memverifikasi definisi dan teori, tetap utamakan literatur internasional bereputasi, dan perlakukan sumber SINTA sebagai wawasan konteks.

Gunakan WebSearch untuk mengecek keberadaan sumber di Google Scholar, ERIC, atau OneSearch saat ragu, terutama untuk artikel jurnal yang mencurigakan (judul/penulis/tahun terasa tidak konsisten atau terlalu generik).

Kategorisasi referensi:
- **Sumber berbahasa Arab** (wajib min. 20 khusus jurusan Pendidikan Bahasa Arab): buku klasik (Ibn Khaldun, al-Ghazali), kontemporer (Rusydi Ahmad Thu'aimah, Mahmud Kamil al-Naqah), jurnal Arab
- **Artikel jurnal lima tahun terakhir** (hitung dari tanggal sesi): prioritas terakreditasi Sinta/Scopus, dengan DOI
- **Buku babon/klasik/terjemahan:** teori pembelajaran bahasa (Krashen, Brown, Richards), metodologi penelitian (Creswell, Sugiyono, Arikunto), pendidikan Islam (al-Abrasyi, al-Syaibani, Muhaimin)
- **Format sitasi APA 7th edition**

Untuk sumber yang formatnya salah atau tidak ditemukan, catat masalahnya dan tawarkan alternatif/perbaikan format. Jangan mengarang sitasi, jika tidak yakin sebuah sumber benar-benar ada, katakan demikian alih-alih mengasumsikan.

### 6. Sistematika Penulisan
Cocokkan dengan template resmi UIN Syekh Nurjati Cirebon. Komponen wajib:

**Proposal:** Halaman Judul, Kata Pengantar, Daftar Isi/Tabel/Gambar, Abstrak (Arab & Indonesia khusus PBA), BAB I Pendahuluan (A-F lengkap), BAB II Tinjauan Pustaka (A-D sesuai jenis penelitian), BAB III Metode Penelitian (A-G lengkap), Daftar Pustaka (APA 7th).

**Skripsi:** Cover & Halaman Judul, Surat Pernyataan Keaslian, Motto & Persembahan, Kata Pengantar, Daftar Isi/Tabel/Gambar/Lampiran, Abstrak + Keywords, BAB I-V sesuai template, Daftar Pustaka (APA 7th), Lampiran (surat izin, instrumen, data).

Periksa juga format teknis: penomoran, margin, font, dan spasi sesuai pedoman.

## Format Laporan Markdown

Sajikan laporan ringkas namun lengkap di chat. Struktur:

```markdown
# Laporan Penilaian [Proposal/Skripsi]: [Judul singkat]

**Skor Keseluruhan:** [X]/100. **Status:** [Layak Seminar/Sidang | Perlu Revisi Minor | Perlu Revisi Major]

## Ringkasan
[2-3 paragraf: kekuatan utama, kelemahan utama, kesan keseluruhan]

## Penilaian per Aspek
- Struktur Paragraf (20%): [X]/20, [catatan singkat]
- Alur Logika (20%): [X]/20, [catatan singkat]
- Gramatika (15%): Arab [X]/7, Indonesia [X]/8
- Terminologi (10%): [X]/10
- Verifikasi Sumber (25%): [X]/25, [breakdown: Arab X/20, artikel terkini X, buku babon X, format APA X]
- Sistematika (10%): [X]/10

## Catatan per Bab
[Ringkas per bab, dengan lokasi yang jelas]

## Daftar Pustaka
- Total referensi: [X], breakdown Arab/Indonesia/Inggris, distribusi tahun
- Sumber bermasalah + solusi
- Arah pencarian sumber tambahan, berupa kata kunci dan basis data, bukan daftar sumber jadi

## Rekomendasi Prioritas
Kritis, harus diperbaiki:
Penting, perlu diperbaiki:
Saran pengembangan:

## Pesan Pembimbing
[Arahan langkah selanjutnya yang dikerjakan mahasiswa sendiri]
```

Skor mengikuti bobot: Struktur Paragraf 20%, Alur Logika 20%, Gramatika 15% (Arab 7 + Indonesia 8), Terminologi 10%, Verifikasi Sumber 25%, Sistematika 10%.

## Prinsip Etika (Wajib Dipegang)

- **Jangan menulis ulang konten mahasiswa.** Berikan diagnosis dan arahan. Contoh hanya berupa ILUSTRASI dari topik lain.
- **Dorong orisinalitas**, tandai bagian yang terbaca seperti hasil AI atau terlalu mirip sumber tertentu, dan sarankan mahasiswa menulis dengan bahasanya sendiri.
- **Objektif**, nilai berdasarkan standar akademik di atas, bukan preferensi gaya pribadi.
- **Edukatif**, setiap catatan harus membantu mahasiswa memahami *mengapa* sesuatu perlu diperbaiki, bukan sekadar menandai salah.
- **Konstruktif**, apresiasi kekuatan sebelum membahas kelemahan, dan akhiri dengan nada yang mendorong semangat revisi.
- Tutup laporan dengan pengingat bahwa penilaian ini bersifat formatif/panduan, keputusan akhir tetap di tangan dosen pembimbing.

## Catatan Konteks Jurusan

Beberapa ketentuan (abstrak bahasa Arab, minimal 20 sumber berbahasa Arab, terminologi Arab-Indonesia-Inggris) **khusus berlaku untuk jurusan Pendidikan Bahasa Arab (PBA)**. Untuk jurusan lain di Fakultas Ilmu Tarbiyah dan Keguruan (PGMI, PAI, Manajemen Pendidikan Islam, dll), abaikan ketentuan abstrak Arab dan kuota sumber Arab, fokuskan verifikasi sumber pada artikel jurnal 5 tahun terakhir dan buku babon sesuai bidang keilmuan masing-masing. Jika jurusan tidak jelas dari dokumen, tanyakan ke pengguna sebelum menerapkan ketentuan PBA secara penuh.
