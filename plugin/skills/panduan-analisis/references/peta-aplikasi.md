# Peta Aplikasi Analisis

Berkas ini hanya peta awal. Fitur, versi, lisensi, dan harga berubah. Sebelum menyebut sebuah fitur ada di versi tertentu, cek dokumentasi resmi pada sesi. Status verifikasi pembangunan plugin, keberadaan Taguette sebagai alat sumber terbuka untuk analisis kualitatif sudah dicek lewat pencarian web. Selebihnya adalah pengetahuan umum yang belum dicek per versi, jadi berlabel [PERLU VERIFIKASI] saat dipakai untuk menjelaskan fitur spesifik.

## Kuantitatif

| Aplikasi | Catatan umum | Cocok untuk |
|---|---|---|
| IBM SPSS Statistics | Berlisensi. Antarmuka menu dan sintaks | Deskriptif, uji beda, korelasi, regresi, reliabilitas, analisis faktor |
| JASP | Gratis, sumber terbuka, antarmuka menu dengan modul | Sama seperti di atas, sebagian modul lanjutan |
| jamovi | Gratis, sumber terbuka, modul tambahan | Sama seperti di atas |
| R dengan RStudio | Gratis, berbasis kode. Paket seperti psych, lavaan, seminr, car, irr | Hampir semua teknik, kurva belajar lebih curam |
| Python | Gratis, berbasis kode. Pustaka pandas, scipy, statsmodels, pingouin, semopy | Sama seperti R |
| Microsoft Excel | Berlisensi. Add-in Analysis ToolPak untuk sebagian uji dasar | Deskriptif, uji t, ANOVA dasar, korelasi, regresi sederhana |
| SmartPLS | Khusus PLS-SEM. Lisensi dan edisi bervariasi, cek situs resmi | PLS-SEM |
| IBM SPSS Amos | Khusus SEM berbasis kovarian. Berlisensi | CB-SEM, CFA |

## Kualitatif

| Aplikasi | Catatan umum |
|---|---|
| NVivo, ATLAS.ti, MAXQDA | Berlisensi. Koding, memo, kueri, visualisasi |
| Taguette | Gratis, sumber terbuka. Pemberian tag pada teks. Fitur lebih sederhana |
| Word dan Excel manual | Matriks koding dengan tabel. Cukup untuk data kecil bila disiplin |

## Cara menjaga mahasiswa tidak salah alat

1. Pilih teknik dari rancangan, baru pilih aplikasi. Bukan sebaliknya.
2. Bila mahasiswa tidak punya lisensi, tanyakan apakah kampus menyediakan lisensi, lalu tunjukkan pilihan gratis. Cek ketersediaan dan syarat lisensi di situs resmi pada sesi.
3. Satu penelitian sebaiknya memakai sesedikit mungkin aplikasi agar jejaknya mudah dilacak.

## Cara cek versi

R, `R.version.string` untuk versi R dan `packageVersion("nama_paket")` untuk paket. Python, `python --version` di terminal, lalu untuk pustaka, `import nama_pustaka` dan cetak `nama_pustaka.__version__`. Aplikasi berantarmuka grafis, biasanya di menu Help atau About, tetapi lokasi persisnya bergantung aplikasi dan versi, jadi minta mahasiswa mengirim tangkapan layar halaman About bila ia tidak menemukannya. Catat juga edisi dan sistem operasi.
