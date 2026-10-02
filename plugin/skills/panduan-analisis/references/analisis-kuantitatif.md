# Keluarga Analisis Kuantitatif (Pengetahuan Pembimbing)

Berkas ini untuk menuntun mahasiswa. Tidak dipakai untuk mengolah data mahasiswa. Rujukan yang disebut adalah rujukan lazim dan wajib dicek lewat `literatur-valid` sebelum dikutip mahasiswa. Ambang angka adalah kebiasaan, bukan hukum.

Setiap bagian punya enam butir. Tujuan, bahan yang dibutuhkan, pemeriksaan sebelum uji, langkah umum yang tidak bergantung aplikasi, keluaran yang dibaca, dan salah kaprah. Unsur laporan ada di `templat-tutorial.md`.

## 1. Pengolahan skor angket

Tujuan. Mengubah jawaban menjadi skor yang siap dianalisis.
Bahan. Data tabular dari belangko tabulasi, kamus variabel, arah tiap butir.
Pemeriksaan. Kode jawaban konsisten, tidak ada nilai di luar rentang skala, data hilang tercatat.
Langkah. Tetapkan kode skala sebelum pengumpulan data. Balik skor butir bernada negatif dengan rumus nilai maksimum ditambah nilai minimum dikurangi nilai jawaban. Hitung skor total atau rerata per variabel sesuai rencana. Putuskan perlakuan data hilang dan catat alasannya.
Dibaca. Rentang, rerata, simpangan baku, dan sebaran per butir.
Salah kaprah. Skala Likert diperlakukan sebagai interval itu praktik umum yang diperdebatkan. Mahasiswa perlu membaca argumennya dan menyatakan sikapnya di naskah. Kategori tinggi, sedang, rendah dengan batas dari rerata dan simpangan baku adalah pilihan penulis dan butuh pembenaran.

## 2. Validitas isi oleh ahli

Tujuan. Menilai kesesuaian butir dengan konstruk menurut penilaian ahli.
Bahan. Lembar validasi ahli terisi, jumlah penilai, kategori skala.
Langkah. Tiap ahli menilai tiap butir. Koefisien V Aiken dihitung per butir dengan rumus V sama dengan jumlah S dibagi n dikali c dikurangi 1. S adalah skor penilaian dikurangi skor terendah, n jumlah penilai, c jumlah kategori. Penetapan butir layak memakai tabel kritis dari sumber, bukan angka tebakan. Rujukan, Aiken (1985), Educational and Psychological Measurement.
Dibaca. Nilai V per butir dan keputusan butir mana yang direvisi.
Salah kaprah. Jumlah ahli sedikit membuat ambang yang lazim bisa menyesatkan. Cek tabel kritis untuk n dan c yang dipakai.

## 3. Validitas butir empiris

Tujuan. Melihat apakah butir bergerak searah dengan skor total konstruknya.
Bahan. Data uji coba, cukup besar menurut dasar yang dikutip.
Langkah umum. Hitung korelasi butir dengan skor total yang sudah mengeluarkan butir itu sendiri (corrected item-total). Korelasi tanpa koreksi cenderung terlalu tinggi. Bandingkan dengan ambang yang dikutip dari sumber, atau lihat nilai p.
Dibaca. Kolom korelasi butir-total terkoreksi, bukan hanya nilai p.
Salah kaprah. Menggugurkan butir hanya berdasarkan satu angka tanpa menimbang isi butir. Untuk bukti struktur konstruk, analisis faktor lebih tepat daripada korelasi butir-total.

## 4. Reliabilitas

Tujuan. Konsistensi pengukuran.
Langkah umum. Alpha Cronbach untuk skala berbutir banyak skor, KR-20 untuk butir dikotomi. Alternatif seperti omega ada dan sering dipakai karena asumsi alpha ketat. Kappa Cohen untuk kesepakatan dua penilai pada kategori. ICC untuk penilaian kontinu.
Dibaca. Koefisien keseluruhan, nilai bila butir dihapus, dan korelasi butir-total.
Salah kaprah. Alpha tinggi tidak membuktikan validitas. Alpha dihitung per dimensi atau skala, bukan semua butir dari konstruk berbeda digabung. Ambang 0,70 yang sering dikutip bersumber dari literatur psikometri tertentu, cek sumbernya.

## 5. Analisis butir tes

Tujuan. Menilai mutu butir tes hasil belajar.
Langkah umum. Tingkat kesukaran P sama dengan B dibagi JS, B jumlah penjawab benar dan JS jumlah peserta. Daya beda D sama dengan PA dikurangi PB, proporsi benar kelompok atas dikurangi kelompok bawah. Kategori kesukaran dan daya beda mengikuti sumber yang dikutip mahasiswa.
Dibaca. P dan D per butir dan keputusan butir.
Salah kaprah. Teori tes klasik bergantung sampel. Butir mudah belum tentu buruk bila tujuannya penguasaan dasar.

## 6. Pemeriksaan asumsi

Normalitas. Shapiro-Wilk dan Kolmogorov-Smirnov dengan koreksi Lilliefors, plus Q-Q plot. Untuk model berbasis residual, periksa residual, bukan hanya data mentah. Pada sampel besar uji formal terlalu sensitif, jadi lihat grafik. Pada sampel kecil uji formal lemah.
Homogenitas varians. Uji Levene. Bila varians tidak homogen, pakai Welch.
Regresi. Linearitas lewat plot residual, multikolinearitas lewat VIF atau tolerance, heteroskedastisitas lewat plot residual dan uji formal, autokorelasi lewat Durbin-Watson pada data berurutan waktu.
Salah kaprah. Menguji normalitas pada data mentah untuk semua uji tanpa tahu apa yang dituntut uji itu. Memilih uji nonparametrik hanya karena p kecil pada uji normalitas tanpa melihat grafik.

## 7. Uji beda dua kelompok

Pohon keputusan. Dua kelompok independen atau berpasangan. Data interval atau ordinal. Asumsi terpenuhi atau tidak. Independen dan asumsi terpenuhi, uji t independen. Independen dengan varians tidak homogen, uji t Welch. Berpasangan dan beda berdistribusi mendekati normal, uji t berpasangan. Ordinal atau asumsi sangat dilanggar, Mann-Whitney untuk independen dan Wilcoxon signed-rank untuk berpasangan.
Dibaca. Statistik kelompok, hasil uji kesamaan varians, baris yang sesuai hasil itu, nilai uji, derajat bebas, p, selisih rerata, selang kepercayaan, dan ukuran efek.
Salah kaprah. Menyebut kelompok "berbeda signifikan" tanpa menyebut besar perbedaan. Memakai uji t independen untuk data pretest-posttest dari kelompok yang sama.

## 8. Uji beda lebih dari dua kelompok

Pohon keputusan. ANOVA satu arah bila asumsi terpenuhi. Welch ANOVA bila varians tidak homogen. Kruskal-Wallis untuk ordinal atau asumsi dilanggar. Uji lanjut hanya bila uji omnibus bermakna, dengan jenis yang sesuai kondisi varians, misalnya Tukey atau Games-Howell, atau koreksi Bonferroni.
Dibaca. Tabel ANOVA, F, derajat bebas, p, ukuran efek seperti eta kuadrat, lalu tabel uji lanjut.
Salah kaprah. Menjalankan banyak uji t berpasangan tanpa koreksi.

## 9. Pretest dan posttest

Bahan. Skor sebelum dan sesudah, kelompok perlakuan dan pembanding bila ada.
Arah. Pilihan analisis bergantung desain. Perbandingan pasangan dalam satu kelompok, perbandingan skor akhir antarkelompok, ANCOVA dengan pretest sebagai kovariat, atau perbandingan skor gain. Tiap pilihan punya asumsi dan kelemahan. Diskusikan dengan pembimbing sebelum memilih, dan minta mahasiswa membela pilihannya dengan rujukan.
N-gain. Rumus g sama dengan skor posttest dikurangi skor pretest, dibagi skor maksimum dikurangi skor pretest. Kategori yang lazim dikutip mengikuti Hake (1998), American Journal of Physics, dengan batas 0,3 dan 0,7. Cek sumber sebelum dikutip. N-gain adalah deskriptor peningkatan, bukan uji hipotesis. Perhatikan pembagian dengan nol bila pretest sudah maksimum.

## 10. Korelasi dan asosiasi

Pilihan. Pearson untuk dua variabel kontinu dengan hubungan linear, Spearman atau Kendall untuk ordinal atau pelanggaran asumsi, point-biserial untuk satu variabel dikotomi, chi-kuadrat untuk dua variabel kategorik dengan ukuran asosiasi seperti Cramer V, dan Fisher exact bila frekuensi harapan kecil.
Dibaca. Koefisien beserta tandanya, p, jumlah data, dan sebaran data pada diagram pencar.
Salah kaprah. Korelasi dibaca sebagai sebab akibat. Hubungan nonlinear terlewat karena tidak melihat diagram pencar. Nilai r kecil tetapi p kecil pada sampel besar dianggap hubungan kuat.

## 11. Regresi linear

Dibaca. R kuadrat dan R kuadrat terkoreksi, uji F model, koefisien tak terstandar B dan standar error, koefisien terstandar bila dipakai, t, p, selang kepercayaan, dan diagnostik asumsi.
Salah kaprah. Menyebut variabel sebagai penyebab dari data observasional. Memasukkan variabel yang kolinear. Menafsirkan koefisien tanpa satuan variabel.

## 12. Analisis faktor eksploratori

Pemeriksaan. Kecukupan sampel dan matriks korelasi, lazimnya KMO dan uji Bartlett. Pilih metode ekstraksi dan rotasi dengan alasan berdasar teori. Jumlah faktor tidak ditentukan hanya oleh eigenvalue lebih dari satu karena kriteria itu dikritik. Pertimbangkan scree plot dan analisis paralel.
Dibaca. KMO, Bartlett, komunalitas, varians terjelaskan, matriks pola, dan butir yang memuat silang.
Salah kaprah. Menamai faktor tanpa kembali ke teori. Menyalahgunakan EFA sebagai pembuktian akhir tanpa uji konfirmatori.

## 13. CFA, SEM berbasis kovarian, dan PLS-SEM

Gambaran. CFA menguji model pengukuran yang sudah dispesifikasikan oleh teori. SEM berbasis kovarian menguji model struktural dan pengukuran dengan indeks kecocokan. PLS-SEM berbasis varians, lazim dipakai untuk model kompleks atau sampel terbatas, dan punya kelemahan serta perdebatan. Pemilihan harus berdasar tujuan dan rujukan, bukan karena aplikasinya mudah.
CB-SEM dibaca. Statistik chi-kuadrat, RMSEA, CFI, TLI, SRMR, beban faktor, dan jalur. Batas yang lazim dikutip berasal dari Hu dan Bentler (1999) dan diperdebatkan.
PLS-SEM dibaca. Model pengukuran, yaitu beban indikator, reliabilitas komposit, AVE, dan validitas diskriminan dengan HTMT atau Fornell-Larcker. Model struktural, yaitu kolinearitas, koefisien jalur dengan bootstrap, R kuadrat, f kuadrat, dan Q kuadrat. Rujukan HTMT, Henseler, Ringle, dan Sarstedt (2015), Journal of the Academy of Marketing Science, 43(1), 115-135, keberadaannya sudah dicek lewat pencarian web. Nilai ambang dan jumlah sampel bootstrap harus dicek ke sumber terbaru.
Salah kaprah. Memodifikasi model hanya demi indeks bagus. Mengklaim sebab akibat dari model yang datanya observasional.

## 14. Analisis deskriptif untuk survei dan evaluasi program

Dibaca. Frekuensi, persentase, rerata per butir dan per dimensi, dan kategori. Kriteria keberhasilan harus ditetapkan sebelum data dianalisis, dengan sumbernya.
Salah kaprah. Menetapkan kriteria setelah melihat hasil.
