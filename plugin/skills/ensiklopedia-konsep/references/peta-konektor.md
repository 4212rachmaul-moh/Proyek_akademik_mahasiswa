# Peta Konektor dan Jalur Pencarian

Muat tool yang tertunda lewat ToolSearch sebelum dipakai. Pakai sesuai kebutuhan, jangan memanggil semuanya sekaligus.

| Kebutuhan | Urutan utama | Cadangan |
|---|---|---|
| Artikel ilmiah lintas bidang, ringkasan temuan | Consensus (search) | Scholar Gateway (semanticSearch), Elicit (search_papers), Undermind (search_papers, find_papers_by_author, launch_deep_search, bila tersambung di sesi), You.com (you-search, terutama literatur berbahasa Indonesia atau topik niche yang tidak terindeks Consensus/Scholar Gateway) |
| Full text dan definisi dalam artikel | Scholar Gateway | web search ke DOAJ, Garuda, SINTA |
| Kesehatan, psikologi, pendidikan kedokteran | PubMed | Consensus |
| Preprint biologi dan kesehatan | bioRxiv | PubMed |
| Web umum, regulasi, panduan hibah, author guidelines | WebSearch lalu WebFetch | exa, You.com |
| Verifikasi sitasi, DOI, retraksi | Scholar Sidekick (verifyCitation, checkRetraction, resolveIdentifier) bila tersambung di komputer pengguna | skrip `literatur-valid/scripts/verifikasi_referensi.py` (Crossref dan OpenAlex) |
| Kuartil dan indeksasi jurnal | WebFetch ke scimagojr.com dan mjl.clarivate.com | WebSearch "nama jurnal scimago" |
| Akreditasi SINTA | WebFetch ke sinta.kemdiktisaintek.go.id | WebSearch nama jurnal + SINTA |
| Kamus dan istilah | KBBI daring, Merriam-Webster, Cambridge, Almaany | korpus atau literatur bidang |
| Naskah mahasiswa yang dievaluasi | Google Drive, folder yang disambungkan | minta unggah langsung |

Catatan Undermind: bila tersambung, panggil `get_orientation` lalu `list_workspaces` lebih dulu sebelum tool pencarian lain, sesuai instruksi konektornya sendiri. Hasil dari Undermind maupun You.com tunduk pada tiga status sumber literatur-valid (Terverifikasi, Kandidat, Ditolak) yang sama seperti hasil Consensus atau Scholar Gateway, tidak ada pengecualian.


## Kriteria sumber kredibel
Terima: artikel jurnal bereputasi atau terakreditasi, buku akademik penerbit dikenal, prosiding bereputasi, dokumen resmi lembaga (peraturan, panduan hibah, statistik resmi), kamus resmi.
Tolak sebagai dasar tunggal: blog anonim, situs agregator SEO, forum, jawaban AI lain, Wikipedia (boleh sebagai pintu ke sumber primer), jurnal yang terindikasi predator atau sudah dikeluarkan dari indeks.

## Kejujuran saat jalur terbatas
Bila konektor gagal atau jaringan terbatas, nyatakan cakupan verifikasi yang sebenarnya, beri label [PERLU VERIFIKASI], dan jangan menaikkan tingkat kepastian klaim.
