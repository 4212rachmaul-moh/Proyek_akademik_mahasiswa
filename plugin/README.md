# Akademik Terpadu Versi Mahasiswa

Plugin pembimbing akademik berbahasa Indonesia untuk mahasiswa. Dibangun dari fondasi plugin akademik-terpadu (Aturan Emas, konektor riset, skrip verifikasi referensi, audit paragraf), tetapi seluruh kemampuan menulis dan menganalisis dibuang.

## Yang tidak dilakukan

Tidak menulis atau memparafrase proposal, skripsi, tesis, disertasi, artikel, makalah, esai, bab, paragraf, atau kalimat pengganti. Tidak menyodorkan topik, rumusan masalah, hipotesis, kerangka teori, atau simpulan jadi. Tidak menganalisis, menghitung, mengkoding, atau menafsirkan data mahasiswa.

## Yang dilakukan

| Skill | Fungsi |
|---|---|
| pusat-bimbingan | Pengatur rute dan penegak batas |
| bimbingan-riset | Bimbingan tahap 0 sampai 9 lewat pertanyaan, tugas mandiri, dan gerbang lulus |
| penjelas-konsep | Penjelasan konsep dengan contoh dari topik lain dan uji teach back |
| ensiklopedia-konsep | Kartu konsep, istilah, teori, atribusi, diverifikasi ke literatur internasional bereputasi, SINTA hanya wawasan |
| literatur-valid | Strategi pencarian, kandidat sumber terverifikasi, verifikasi referensi, DOI, retraksi, atribusi |
| penantang-argumen | Uji argumen dan simulasi penguji, diagnosis tanpa teks pengganti |
| audit-metodologi | Audit rancangan dan keselarasan, tanpa menghitung ulang |
| periksa-paragraf | Diagnosis paragraf TS SS SD C, tanda baca, pola generik, tanpa menyunting |
| panduan-analisis | Tanya aplikasi dan versi, tutorial langkah demi langkah, tuntunan membaca hasil |
| belangko-penelitian | 21 belangko kosong dengan petunjuk, bahan, dan langkah analisis umum |
| review-kelayakan | Verdik formatif kelayakan naskah |

Skill berjumlah 11. Lima agen pendukung, yaitu verifikator-sumber, penantang-argumen, penguji-metodologi, auditor-gaya, dan reviewer-kelayakan, semuanya hanya mengevaluasi.

## Dibuang dari plugin dosen

naskah-tugas-akhir, artikel-jurnal, buku-dari-ide, buku-dari-riset, hibah-penelitian, naskah-akademik-kebijakan, proofread-terjemah, tinjauan-sistematis, bagan-kerangka, mentor-riset (karena menghasilkan dokumen dan menjalankan skrip analisis), serta seluruh skrip analisis statistik dan SEM. Yang tidak ada tidak bisa dipanggil.

## Hierarki sumber

Rujukan utama verifikasi konsep adalah literatur internasional bereputasi. Sumber SINTA hanya menambah wawasan. Rincian di `skills/ensiklopedia-konsep/references/hierarki-sumber.md`.

## Perubahan v0.1.1

Skill ensiklopedia-konsep, hierarki sumber, batas keras dimuat di tiap skill karena hook tidak dimuat di chat, dan peta konektor serta hierarki sumber disalin ke dalam folder skill yang memakainya.

## Pemasangan

Jangan memasang plugin ini bersamaan dengan plugin akademik-terpadu di akun yang sama. Hook sesi keduanya akan tumpang tindih dan skill pembuat naskah dari plugin dosen tetap bisa dipanggil. Konektor di `.mcp.json` mungkin meminta login pada pemakaian pertama.

## Verifikasi saat pembangunan

Skrip belangko diuji otomatis, yaitu `python skills/belangko-penelitian/scripts/buat_belangko.py --uji --keluar ./keluaran`. Uji memastikan semua belangko kosong dan tanpa rumus, dan uji negatif terbukti mendeteksi sel yang terisi. Keberadaan rujukan Henseler dkk. (2015), Hake (1998), Aiken (1985), dan Taguette dicek lewat pencarian web. Ambang angka statistik dan jalur menu aplikasi belum diverifikasi per versi, dan skill diperintah memverifikasinya pada sesi dan memberi label bila belum.

## Keterbatasan yang jujur

1. Batas dijaga lewat instruksi, bukan penghalang teknis mutlak. Mahasiswa bisa memakai alat lain.
2. Verifikasi paragraf memeriksa mutu argumen dan keterlacakan sumber, bukan membuktikan penulisnya manusia. Tidak ada jaminan lolos detektor AI atau cek kemiripan.
3. Tutorial aplikasi bergantung versi. Menu yang belum dicek ke dokumentasi resmi berlabel [PERLU VERIFIKASI MENU].
4. Rubrik FITK UINSSC diadaptasi dari skill milik pengampu. Cocokkan dengan pedoman fakultas terbaru.
5. Kampus belum memiliki kebijakan resmi tentang penggunaan AI (keterangan pengguna). Bila kebijakan terbit, cocokkan isinya.

## Lisensi

Referensi stop-slop di skill periksa-paragraf berlisensi MIT (Hardik Pandya), berkas lisensi disertakan.
