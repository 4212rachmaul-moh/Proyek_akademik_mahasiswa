# -*- coding: utf-8 -*-
"""Katalog belangko penelitian. Semua belangko berisi format saja, tanpa isi.
Setiap entri memuat: judul, jenis (docx atau xlsx), kolom tabel, jumlah baris,
petunjuk pengisian, bahan yang dibutuhkan untuk analisis, dan langkah analisis umum.
Teks di sini adalah panduan netral. Tidak ada isi substantif penelitian."""

ETIKA_DATA = ("Gunakan kode partisipan, bukan nama asli. Simpan data mentah terpisah dari data kerja. "
              "Pastikan persetujuan partisipan sudah ada sebelum data dicatat.")

FORMS = {
 "transkrip-wawancara": {
  "judul": "Belangko Transkrip Wawancara", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Kode Partisipan", "Peran Partisipan", "Tanggal", "Waktu Mulai", "Waktu Selesai", "Tempat", "Pewawancara", "Nomor Berkas Rekaman", "Status Persetujuan Partisipan"],
  "kolom": ["No Baris", "Pembicara", "Isi Ujaran", "Penanda Nonverbal dan Jeda", "Catatan Pewawancara"],
  "baris": 25,
  "petunjuk": [
   "Tetapkan konvensi transkripsi sebelum mulai, misalnya verbatim atau dirapikan, cara menulis jeda, tumpang tindih, dan tawa, lalu pakai konvensi yang sama untuk semua partisipan.",
   "Tulis ujaran sesuai rekaman. Jangan memperbaiki atau menafsirkan saat transkripsi.",
   "Beri nomor baris berurutan agar kutipan bisa ditelusuri.",
   "Ganti nama orang dan lembaga dengan kode.",
   "Dengarkan ulang rekaman sambil membaca transkrip untuk memeriksa kesalahan."],
  "bahan": ["Rekaman audio atau video", "Bukti persetujuan partisipan", "Kode partisipan", "Konvensi transkripsi yang tertulis", "Pedoman wawancara", "Kodebook (dibuat peneliti)", "Aplikasi pengelola data kualitatif, atau tabel Word atau Excel"],
  "langkah": [
   "Transkripsikan rekaman dengan konvensi yang sama untuk semua partisipan.",
   "Periksa transkrip dengan mendengar ulang rekaman.",
   "Anonimkan identitas.",
   "Baca seluruh transkrip beberapa kali dan catat kesan awal di jurnal reflektif, sebagai asumsi peneliti.",
   "Beri kode pada unit makna dan catat di matriks koding.",
   "Kelompokkan kode menjadi kategori dan tema. Setiap tema harus bisa ditelusuri ke kutipan dengan kode partisipan dan nomor baris.",
   "Cari data yang menentang tema dan bahas.",
   "Lakukan strategi keterpercayaan yang kamu rencanakan, misalnya triangulasi dan member checking.",
   "Catat setiap keputusan analisis di log jejak audit."]},
 "pedoman-wawancara": {
  "judul": "Belangko Pedoman Wawancara", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Fokus Penelitian", "Kelompok Partisipan", "Jenis Wawancara", "Perkiraan Durasi"],
  "kolom": ["No", "Fokus atau Indikator dari Kisi-kisi", "Pertanyaan Utama", "Pertanyaan Penelusuran", "Catatan"],
  "baris": 12,
  "petunjuk": [
   "Isi kolom fokus dari kisi-kisi atau rumusan masalah milikmu, lalu tulis pertanyaan dengan kata-katamu sendiri.",
   "Setiap pertanyaan harus punya alasan keterkaitan dengan fokus.",
   "Bedakan pertanyaan utama dan pertanyaan penelusuran.",
   "Uji coba pedoman pada satu orang di luar partisipan, lalu catat revisinya di kolom catatan."],
  "bahan": ["Rumusan masalah", "Kisi-kisi atau fokus penelitian", "Landasan teori bersumber", "Daftar partisipan dan alasan pemilihan"],
  "langkah": [
   "Turunkan fokus wawancara dari rumusan masalah.",
   "Tulis pertanyaan utama dan penelusuran untuk tiap fokus.",
   "Mintalah pembimbing atau ahli menilai kesesuaian pertanyaan dengan fokus.",
   "Uji coba, revisi, lalu gunakan.",
   "Catat bila pedoman berubah selama pengumpulan data, beserta alasannya, di log jejak audit."]},
 "lembar-observasi-terstruktur": {
  "judul": "Belangko Lembar Observasi Terstruktur", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif atau Kuantitatif",
  "identitas": ["Tanggal", "Waktu", "Lokasi", "Subjek atau Kelompok yang Diamati", "Kegiatan yang Diamati", "Pengamat", "Pertemuan atau Siklus Ke-"],
  "kolom": ["No", "Indikator", "Deskripsi Perilaku yang Teramati", "Muncul", "Frekuensi atau Skor", "Catatan"],
  "baris": 15,
  "petunjuk": [
   "Isi indikator dari kisi-kisi observasi yang kamu rancang sendiri. Tetapkan sebelum observasi.",
   "Tulis perilaku yang benar-benar terlihat, bukan tafsiran.",
   "Tentukan di awal arti kolom muncul dan cara mengisi frekuensi atau skor.",
   "Bila ada lebih dari satu pengamat, tiap pengamat mengisi lembarnya sendiri."],
  "bahan": ["Kisi-kisi observasi", "Definisi tiap indikator", "Jadwal dan lokasi observasi", "Izin lembaga", "Lembar yang diisi lebih dari satu pengamat bila ingin menghitung kesepakatan"],
  "langkah": [
   "Latih pengamat memakai definisi indikator yang sama.",
   "Lakukan observasi dan isi lembar saat atau segera setelah kegiatan.",
   "Rekap data per indikator dan per pertemuan di tabel terpisah.",
   "Bila ada dua pengamat, hitung kesepakatan antar pengamat dengan cara yang kamu kutip dari sumber.",
   "Bandingkan temuan observasi dengan sumber data lain untuk triangulasi.",
   "Catat keterbatasan observasi, misalnya kehadiran pengamat memengaruhi perilaku."]},
 "catatan-lapangan": {
  "judul": "Belangko Catatan Lapangan", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Tanggal", "Waktu", "Lokasi", "Kegiatan", "Pihak yang Terlibat", "Peneliti"],
  "kolom": ["Waktu", "Catatan Deskriptif", "Catatan Reflektif"],
  "baris": 12,
  "petunjuk": [
   "Kolom deskriptif berisi apa yang terjadi, apa adanya, tanpa penilaian.",
   "Kolom reflektif berisi tafsiran, perasaan, dan pertanyaan peneliti. Pisahkan jelas dari deskripsi.",
   "Tulis catatan secepat mungkin setelah kegiatan agar ingatan masih utuh.",
   "Gunakan kode untuk orang dan lembaga."],
  "bahan": ["Kode partisipan dan lokasi", "Izin penelitian", "Fokus pengamatan", "Daftar kode awal bila ada"],
  "langkah": [
   "Baca catatan secara berkala dan tandai kejadian penting.",
   "Perlakukan catatan sebagai data teks, lalu beri kode dengan prosedur yang sama seperti transkrip.",
   "Gunakan kolom reflektif untuk menelusuri bias dan asumsi peneliti.",
   "Cocokkan dengan transkrip dan dokumen untuk triangulasi.",
   "Catat keputusan analisis di log jejak audit."]},
 "jurnal-reflektif": {
  "judul": "Belangko Catatan Reflektif", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif, PTK, Praktik Reflektif",
  "identitas": ["Tanggal", "Kegiatan", "Pertemuan atau Siklus Ke-"],
  "kolom": ["Apa yang terjadi", "Apa yang saya rasakan dan pikirkan", "Mengapa itu terjadi", "Apa yang saya pelajari", "Apa yang akan saya lakukan berikutnya"],
  "baris": 8,
  "petunjuk": [
   "Tulis dengan kata-katamu sendiri. Isi kolom adalah milikmu, bukan milik alat bantu.",
   "Nyatakan di awal penelitian apakah catatan reflektif berstatus data atau hanya jejak refleksivitas peneliti.",
   "Jujur pada hal yang tidak berjalan sesuai rencana. Itu data yang berharga."],
  "bahan": ["Jadwal kegiatan", "Fokus refleksi", "Keputusan status data refleksi dari rancangan penelitian"],
  "langkah": [
   "Isi segera setelah kegiatan.",
   "Baca seluruh catatan setelah beberapa pertemuan dan cari pola yang berulang.",
   "Bila berstatus data, beri kode seperti teks lain. Bila hanya jejak refleksivitas, gunakan untuk memeriksa asumsi dan bias.",
   "Hubungkan temuan refleksi dengan data lain dan catat di log jejak audit."]},
 "catatan-ptk-per-siklus": {
  "judul": "Belangko Catatan Penelitian Tindakan Kelas per Siklus", "jenis": "docx", "landscape": True,
  "kategori": "PTK",
  "identitas": ["Siklus Ke-", "Pertemuan Ke-", "Tanggal", "Kelas dan Jumlah Siswa", "Peneliti", "Kolaborator atau Pengamat"],
  "kolom": ["Tahap", "Uraian Rencana atau Kejadian", "Data yang Dikumpulkan", "Catatan"],
  "baris": 4,
  "petunjuk": [
   "Gunakan satu lembar untuk satu siklus atau satu pertemuan.",
   "Baris tahap diisi perencanaan, tindakan, observasi, dan refleksi, sesuai model siklus yang kamu pilih dan kutip.",
   "Tulis indikator keberhasilan yang kamu tetapkan sebelum tindakan. Jangan mengubahnya setelah melihat hasil."],
  "bahan": ["Indikator keberhasilan beserta sumbernya", "Rencana tindakan", "Instrumen pengumpul data", "Data siklus sebelumnya"],
  "langkah": [
   "Rencanakan tindakan dari hasil refleksi siklus sebelumnya.",
   "Kumpulkan data sesuai instrumen.",
   "Olah data tiap siklus dengan teknik yang sama agar bisa dibandingkan.",
   "Bandingkan hasil antar siklus terhadap indikator keberhasilan yang sudah tetap.",
   "Tulis refleksi dan keputusan lanjut atau berhenti, dengan alasannya."]},
 "kisi-kisi-instrumen": {
  "judul": "Belangko Kisi-kisi Instrumen", "jenis": "docx", "landscape": True,
  "kategori": "Kuantitatif dan Kualitatif",
  "identitas": ["Nama Instrumen", "Variabel atau Fokus yang Diukur", "Jenis Instrumen", "Sasaran Responden"],
  "kolom": ["Variabel atau Fokus", "Dimensi", "Indikator", "Nomor Butir", "Jumlah Butir", "Sumber Teori"],
  "baris": 12,
  "petunjuk": [
   "Seluruh isi diturunkan dari teori yang kamu baca dan kamu sitasi di kolom sumber teori. Isi dengan kata-katamu sendiri.",
   "Setiap indikator harus bisa diamati atau diukur.",
   "Setiap butir harus terhubung ke satu indikator."],
  "bahan": ["Definisi operasional bersumber", "Landasan teori", "Skala yang dipilih beserta alasannya", "Daftar ahli penilai"],
  "langkah": [
   "Turunkan dimensi dan indikator dari teori.",
   "Tulis butir di instrumen terpisah dan catat nomornya di kisi-kisi.",
   "Validasi isi oleh ahli dengan lembar validasi.",
   "Uji coba, lalu tangani butir yang lemah dengan memeriksa isi butir dan hasil analisis di aplikasi.",
   "Revisi dan finalkan, simpan semua versi."]},
 "matriks-keselarasan": {
  "judul": "Belangko Matriks Keselarasan Rancangan Penelitian", "jenis": "docx", "landscape": True,
  "kategori": "Semua desain",
  "identitas": ["Jenis dan Desain Penelitian", "Jenjang dan Program Studi"],
  "kolom": ["Rumusan Masalah", "Tujuan", "Sumber Data", "Instrumen", "Teknik Analisis", "Bentuk Temuan yang Diharapkan"],
  "baris": 6,
  "petunjuk": [
   "Satu baris untuk satu rumusan masalah.",
   "Setiap sel harus nyambung dengan sel di sebelah kirinya.",
   "Bila ada sel yang tidak bisa kamu isi, itu tanda rancangan perlu diperbaiki."],
  "bahan": ["Rumusan masalah", "Rancangan metode", "Instrumen yang direncanakan", "Teknik analisis yang dipilih beserta alasannya"],
  "langkah": [
   "Isi matriks dari rancanganmu sendiri.",
   "Cek keselarasan dari kiri ke kanan.",
   "Bawa matriks ke pembimbing atau minta diaudit lewat skill audit-metodologi.",
   "Perbarui matriks bila rancangan berubah."]},
 "kodebook-kualitatif": {
  "judul": "Belangko Kodebook Kualitatif", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Pendekatan Koding", "Penyusun", "Tanggal Pembaruan", "Versi"],
  "kolom": ["Kode", "Definisi", "Kriteria Pemakaian", "Kriteria Tidak Dipakai", "Contoh Kutipan dan Lokasi", "Catatan Revisi"],
  "baris": 15,
  "petunjuk": [
   "Tulis definisi kode dengan kata-katamu sendiri.",
   "Kriteria pemakaian dan tidak dipakai membantu konsistensi, terlebih bila ada lebih dari satu pengkoding.",
   "Setiap revisi kode dicatat bersama alasannya."],
  "bahan": ["Transkrip dan catatan lapangan", "Kerangka teori bila koding deduktif", "Memo analisis"],
  "langkah": [
   "Mulai dari kode awal dari data atau teori.",
   "Pakai kode pada beberapa transkrip, lalu revisi definisi bila ada ketidakkonsistenan.",
   "Bila ada dua pengkoding, hitung kesepakatan dengan cara yang kamu kutip dan bahas perbedaan.",
   "Kelompokkan kode menjadi kategori dan tema di matriks koding."]},
 "matriks-koding-tema": {
  "judul": "Belangko Matriks Koding dan Jejak Tema", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Sumber Data", "Peneliti", "Tanggal"],
  "kolom": ["Kutipan", "Kode Partisipan dan Nomor Baris", "Kode", "Kategori", "Tema", "Memo"],
  "baris": 20,
  "petunjuk": [
   "Satu baris untuk satu kutipan bermakna.",
   "Kutipan dicatat apa adanya, jangan dipotong sehingga maknanya berubah.",
   "Jejak dari kutipan ke tema harus terbaca dari kiri ke kanan."],
  "bahan": ["Transkrip bernomor baris", "Kodebook", "Memo analisis"],
  "langkah": [
   "Pindahkan kutipan bermakna ke matriks.",
   "Beri kode, lalu kelompokkan menjadi kategori dan tema.",
   "Periksa setiap tema terhadap beragam partisipan dan data yang menentang.",
   "Tinjau tema terhadap seluruh data, bukan hanya matriks.",
   "Gunakan matriks sebagai jejak audit untuk pembimbing."]},
 "log-jejak-audit": {
  "judul": "Belangko Log Jejak Audit Analisis", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif, Semua desain",
  "identitas": ["Penelitian", "Peneliti"],
  "kolom": ["Tanggal", "Keputusan Analisis", "Alasan", "Dampak pada Kodebook, Tema, atau Hasil", "Pengambil Keputusan"],
  "baris": 15,
  "petunjuk": [
   "Catat setiap keputusan penting selama analisis, bukan hanya hasil akhir.",
   "Alasan harus tertulis saat keputusan dibuat, bukan diingat belakangan.",
   "Bila keputusan diubah, catat perubahan sebagai baris baru."],
  "bahan": ["Catatan harian analisis", "Versi kodebook", "Hasil keluaran aplikasi"],
  "langkah": [
   "Isi log setiap kali ada keputusan analisis.",
   "Simpan berkas keluaran aplikasi bertanggal.",
   "Bawa log ke pembimbing sebagai bukti keterlacakan.",
   "Rujuk log saat menulis bagian keterpercayaan."]},
 "persetujuan-partisipan": {
  "judul": "Belangko Lembar Persetujuan Partisipan", "jenis": "docx", "landscape": False,
  "kategori": "Etika penelitian",
  "identitas": [],
  "kolom": ["Bagian", "Isi yang Diisi Peneliti"],
  "baris": 0,
  "bagian": ["Judul Penelitian", "Nama dan Institusi Peneliti", "Tujuan Penelitian", "Prosedur yang Dialami Partisipan", "Perkiraan Waktu Keterlibatan", "Risiko dan Ketidaknyamanan", "Manfaat", "Kerahasiaan dan Penyimpanan Data", "Hak Berhenti Kapan Saja", "Kontak Peneliti dan Pembimbing", "Pernyataan Persetujuan Partisipan", "Nama Partisipan atau Wali", "Tanda Tangan dan Tanggal", "Nama Peneliti, Tanda Tangan, dan Tanggal"],
  "petunjuk": [
   "Isi tiap bagian dengan kata-katamu sendiri, dalam bahasa yang mudah dipahami partisipan.",
   "Untuk partisipan di bawah umur, tanyakan ke pembimbing dan lembaga siapa yang harus memberi persetujuan, dan apakah perlu persetujuan wali serta persetujuan anak.",
   "Susunan dan syarat lembar persetujuan bergantung pada kampus dan komite etik. Cocokkan dengan pedomannya."],
  "bahan": ["Rancangan penelitian", "Pedoman etika kampus", "Izin lembaga tempat penelitian"],
  "langkah": [
   "Isi semua bagian dan konsultasikan ke pembimbing.",
   "Jelaskan isi lembar ke calon partisipan secara lisan.",
   "Minta tanda tangan sebelum pengumpulan data dimulai.",
   "Simpan lembar yang sudah ditandatangani terpisah dari data."]},
 "dokumentasi-analisis-dokumen": {
  "judul": "Belangko Lembar Analisis Dokumen", "jenis": "docx", "landscape": True,
  "kategori": "Kualitatif",
  "identitas": ["Fokus Analisis Dokumen", "Peneliti", "Tanggal"],
  "kolom": ["Kode Dokumen", "Jenis dan Asal Dokumen", "Tahun", "Alasan Pemilihan", "Bagian atau Halaman Penting", "Catatan Konteks"],
  "baris": 10,
  "petunjuk": [
   "Tetapkan kriteria seleksi dokumen sebelum mengumpulkan.",
   "Catat asal dan konteks pembuatan dokumen karena memengaruhi cara membacanya.",
   "Simpan salinan dokumen asli."],
  "bahan": ["Kriteria seleksi dokumen", "Salinan dokumen", "Kodebook"],
  "langkah": [
   "Seleksi dokumen sesuai kriteria dan catat alasannya.",
   "Baca dan beri kode seperti pada transkrip.",
   "Hubungkan dengan sumber data lain untuk triangulasi.",
   "Catat keterbatasan dokumen, misalnya sudut pandang pembuatnya."]},
 "jurnal-bimbingan": {
  "judul": "Belangko Jurnal Bimbingan", "jenis": "docx", "landscape": True,
  "kategori": "Administrasi bimbingan",
  "identitas": ["Nama Mahasiswa", "Pembimbing", "Judul Sementara"],
  "kolom": ["Tanggal", "Topik yang Dibahas", "Masukan Pembimbing", "Tindak Lanjut Mahasiswa", "Tenggat", "Paraf"],
  "baris": 12,
  "petunjuk": [
   "Isi segera setelah bimbingan.",
   "Tulis masukan dengan kata-kata pembimbing sebisanya.",
   "Tindak lanjut dikerjakan sendiri dan dilaporkan di pertemuan berikutnya."],
  "bahan": ["Catatan bimbingan", "Jadwal bimbingan"],
  "langkah": [
   "Periksa tindak lanjut sebelum tiap pertemuan.",
   "Bawa jurnal ke pertemuan berikutnya.",
   "Gunakan jurnal untuk menelusuri perubahan keputusan penelitian."]},
 "lembar-validasi-ahli": {
  "judul": "Belangko Lembar Validasi Ahli", "jenis": "docx", "landscape": True,
  "kategori": "Kuantitatif, R&D",
  "identitas": ["Nama Validator", "Bidang Keahlian", "Institusi", "Tanggal Penilaian", "Instrumen atau Produk yang Divalidasi"],
  "kolom": ["No", "Butir atau Aspek yang Dinilai", "Skor Penilaian", "Komentar dan Saran Perbaikan"],
  "baris": 15,
  "petunjuk": [
   "Tetapkan skala penilaian dan arti tiap angka di bagian petunjuk lembar yang kamu berikan ke ahli.",
   "Isi kolom butir dari instrumen atau produkmu. Kolom skor dan komentar diisi oleh ahli.",
   "Sediakan ruang kesimpulan umum dan kategori kesimpulan yang kamu rancang."],
  "bahan": ["Instrumen atau produk yang divalidasi", "Kisi-kisi", "Skala penilaian dan kategori kelayakan beserta sumbernya", "Daftar ahli dan alasan pemilihan"],
  "langkah": [
   "Kirim lembar bersama instrumen dan kisi-kisi ke ahli.",
   "Rekap skor semua ahli di tabulasi, satu baris per butir dan satu kolom per ahli.",
   "Hitung koefisien validitas isi di aplikasi dengan cara yang kamu kutip, misalnya V Aiken, mengikuti tutorial dari skill panduan-analisis.",
   "Putuskan butir yang direvisi dengan mempertimbangkan komentar tertulis, bukan hanya angka.",
   "Catat seluruh revisi dan alasannya."]},
 "angket-kosong": {
  "judul": "Belangko Lembar Angket Responden", "jenis": "docx", "landscape": True,
  "kategori": "Kuantitatif",
  "identitas": ["Kode Responden", "Tanggal Pengisian"],
  "kolom": ["No", "Pernyataan", "1", "2", "3", "4", "5"],
  "baris": 20,
  "petunjuk": [
   "Tulis pernyataan dari kisi-kisi milikmu sendiri. Jumlah dan label skala ditetapkan olehmu, sesuaikan kolom bila skalamu berbeda.",
   "Tulis keterangan arti angka skala di bagian petunjuk lembar yang kamu berikan ke responden.",
   "Satu pernyataan hanya memuat satu gagasan."],
  "bahan": ["Kisi-kisi instrumen", "Hasil validasi ahli", "Hasil uji coba", "Persetujuan responden"],
  "langkah": [
   "Cetak atau digitalkan lembar angket final.",
   "Catat jawaban ke belangko tabulasi angket apa adanya.",
   "Balik skor butir negatif di aplikasi atau lembar kerja terpisah dan catat hal itu.",
   "Lanjutkan ke tutorial analisis di skill panduan-analisis."]},
 "lembar-kerja-analisis": {
  "judul": "Belangko Lembar Kerja Analisis", "jenis": "docx", "landscape": False,
  "kategori": "Semua analisis",
  "identitas": ["Nama Peneliti", "Tanggal"],
  "kolom": ["Bagian", "Isian Peneliti"],
  "baris": 0,
  "bagian": ["Rumusan masalah yang dijawab", "Jenis data dan skalanya", "Teknik analisis yang dipilih", "Alasan memilih teknik, dengan rujukan", "Aplikasi dan versi", "Asumsi yang diperiksa dan hasil pemeriksaannya", "Langkah yang dijalankan di aplikasi", "Berkas keluaran dan lokasi penyimpanannya", "Hasil, dinyatakan dengan kata sendiri", "Batas klaim yang boleh dibuat", "Pertanyaan untuk pembimbing"],
  "petunjuk": [
   "Isi sebelum, selama, dan sesudah analisis, bukan sekaligus di akhir.",
   "Simpan lembar ini bersama berkas keluaran sebagai jejak analisis.",
   "Bagian hasil diisi dengan kata-katamu sendiri setelah membaca keluaran."],
  "bahan": ["Data yang sudah dicatat sesuai belangko", "Rancangan analisis", "Aplikasi analisis terpasang"],
  "langkah": [
   "Isi bagian rencana sebelum menjalankan analisis.",
   "Jalankan analisis mengikuti tutorial dari skill panduan-analisis.",
   "Isi bagian hasil dan batas klaim, lalu bawa ke pembimbing."]},
 "tabulasi-angket": {
  "judul": "Belangko Tabulasi Data Angket", "jenis": "xlsx",
  "kategori": "Kuantitatif", "parameter": ["butir", "responden"],
  "petunjuk": [
   "Isi lembar Kamus Variabel lebih dulu sebelum memasukkan data.",
   "Masukkan jawaban apa adanya sesuai lembar responden. Jangan membalik skor di lembar Data.",
   "Data hilang dikosongkan, bukan diisi nol.",
   "Satu baris untuk satu responden dan satu kolom untuk satu butir.",
   "Simpan salinan data mentah yang tidak diubah."],
  "bahan": ["Lembar angket terisi", "Kisi-kisi dan kamus variabel", "Skala dan arah butir", "Aplikasi analisis dan versinya"],
  "langkah": [
   "Isi kamus variabel, termasuk arah butir positif atau negatif.",
   "Masukkan data dan periksa rentang nilai.",
   "Impor ke aplikasi dan pastikan tipe variabel benar.",
   "Balik skor butir negatif sesuai kamus variabel di aplikasi atau lembar kerja terpisah, dan catat.",
   "Lanjutkan ke tutorial validitas, reliabilitas, atau uji yang sesuai di skill panduan-analisis."]},
 "tabulasi-tes": {
  "judul": "Belangko Tabulasi Jawaban Tes", "jenis": "xlsx",
  "kategori": "Kuantitatif", "parameter": ["butir", "responden"],
  "petunjuk": [
   "Isi kunci jawaban di lembar Kunci setelah soal final.",
   "Masukkan jawaban peserta apa adanya di lembar Data Jawaban.",
   "Jangan menskor di lembar Data Jawaban. Skoring dilakukan setelah data bersih."],
  "bahan": ["Lembar jawaban peserta", "Kunci jawaban", "Kisi-kisi soal", "Aplikasi analisis dan versinya"],
  "langkah": [
   "Isi kunci dan indikator tiap soal.",
   "Masukkan jawaban peserta.",
   "Skoring di aplikasi atau lembar kerja terpisah dan catat aturannya.",
   "Lakukan analisis butir dan reliabilitas mengikuti tutorial di skill panduan-analisis.",
   "Tentukan keputusan butir berdasarkan isi soal dan hasil analisis."]},
 "tabulasi-pretest-posttest": {
  "judul": "Belangko Tabulasi Pretest dan Posttest", "jenis": "xlsx",
  "kategori": "Kuantitatif", "parameter": ["responden"],
  "petunjuk": [
   "Satu baris untuk satu peserta. Kode peserta sama untuk pretest dan posttest.",
   "Isi skor apa adanya. Skor maksimum dicatat di lembar Parameter.",
   "Catat bila ada peserta yang tidak mengikuti salah satu tes."],
  "bahan": ["Skor pretest dan posttest", "Skor maksimum tes", "Kelompok peserta", "Rancangan analisis"],
  "langkah": [
   "Pilih teknik analisis berdasarkan desain bersama pembimbing.",
   "Periksa kelengkapan pasangan data.",
   "Jalankan analisis di aplikasi mengikuti tutorial dari skill panduan-analisis.",
   "Bila memakai N-gain, ketahui batas dan rujukannya, dan pastikan tidak ada pretest yang sudah maksimum."]},
 "matriks-literatur": {
  "judul": "Belangko Matriks Literatur", "jenis": "xlsx",
  "kategori": "Studi pustaka", "parameter": ["baris"],
  "petunjuk": [
   "Isi hanya dari sumber yang sudah kamu buka dan baca sendiri.",
   "Tulis ringkasan dengan kata-katamu sendiri, bukan salinan abstrak.",
   "Kolom status verifikasi diisi setelah kamu mengecek metadata dan isi sumber."],
  "bahan": ["Sumber yang sudah dibaca", "Kata kunci dan basis data yang dipakai", "Jejak pencarian"],
  "langkah": [
   "Kumpulkan sumber relevan lewat pencarian yang tercatat.",
   "Baca dan isi satu baris per sumber.",
   "Bandingkan konteks, metode, dan temuan antar baris untuk menemukan pola dan celah.",
   "Tulis sendiri celah dan kebaruanmu dalam satu kalimat, lalu uji dengan skill penantang-argumen."]},
}

XLSX_KOLOM = {
 "kamus": ["Kode Butir", "Pernyataan", "Variabel", "Dimensi", "Indikator", "Arah Butir", "Skala"],
 "kunci": ["No Soal", "Kunci Jawaban", "Indikator", "Catatan"],
 "prepost": ["No", "Kode Peserta", "Kelompok", "Pretest", "Posttest", "Catatan"],
 "literatur": ["No", "Penulis dan Tahun", "Judul", "Wadah Publikasi", "DOI atau URL", "Konteks dan Sampel", "Metode", "Temuan Inti", "Keterbatasan", "Relevansi dengan Penelitianku", "Status Verifikasi"],
}
