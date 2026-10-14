# Latihan — Pertemuan 12: Koleksi dan Generics

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Setiap kali mencetak isi set atau map berbasis hash, **urutkan dulu**. Tanpa itu, output-mu bisa berbeda urutan dengan contoh, padahal programmu sudah benar.

---

## Latihan 1 — Daftar Hadir Unik (⭐ Dasar)

**Tujuan:** memakai set untuk membuang data kembar dan menerapkan operasi himpunan.

**Soal:** Kelas PBO berisi delapan mahasiswa: Ayu, Bima, Citra, Dimas, Eka, Fajar, Gita, dan Hadi. Kehadiran dicatat lewat scan QR, dan beberapa mahasiswa memindai dua kali.

- Scan pertemuan 1: Ayu, Bima, Citra, Ayu, Eka, Gita, Bima
- Scan pertemuan 2: Bima, Citra, Dimas, Gita, Citra

Tampilkan jumlah scan dan jumlah mahasiswa unik per pertemuan, lalu siapa yang hadir di kedua pertemuan, siapa yang hadir sekali saja, dan siapa yang belum pernah hadir. Semua daftar nama diurutkan abjad.

**Contoh output yang diharapkan:**

```text
=== REKAP DAFTAR HADIR KELAS PBO ===
Pertemuan 1: 7 kali scan, 5 mahasiswa
Pertemuan 2: 5 kali scan, 4 mahasiswa
Hadir di kedua pertemuan: Bima, Citra, Gita
Hadir sekali saja       : Ayu, Dimas, Eka
Belum pernah hadir      : Fajar, Hadi
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `set(scan_p1)`, lalu operator `&` (irisan), `^` (hanya di salah satu), `|` (gabungan), dan `-` (selisih). Cetak dengan `", ".join(sorted(...))`.
- Java: `new HashSet<>(scanP1)`, lalu `retainAll`, `addAll`, `removeAll` pada **salinan**. "Hadir sekali saja" = gabungan dikurangi irisan. Cetak lewat `new TreeSet<>(...)` agar urut.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_daftar_hadir.py) · [☕ Java](java/solusi/Latihan01DaftarHadir.java)

---

## Latihan 2 — Inventaris Sekretariat Himpunan (⭐ Dasar)

**Tujuan:** memakai dict/Map sebagai pencatat jumlah, lengkap dengan exception saat gagal.

**Soal:** Buat kelas `Inventaris` yang menyimpan stok dalam bentuk *nama barang → jumlah*, dengan method:

- `tambah(nama, jumlah)`: barang yang belum ada otomatis terdaftar.
- `ambil(nama, jumlah)`: melempar `ValueError` (Python) / `IllegalArgumentException` (Java) berpesan `barang tidak terdaftar` atau `stok hanya N`.
- `cek(nama)` (0 jika tidak ada), `jumlah_jenis()`, `barang_habis()`, dan `tampilkan()` (urut sesuai urutan barang pertama kali didaftarkan).

Daftarkan spidol 12, kertas HVS (rim) 5, dan lakban 3. Lalu: tambah spidol 6, ambil lakban 3, ambil kertas HVS (rim) 10, ambil stapler 1, dan tambah stapler 2. Tangkap exception-nya dan laporkan hasil setiap transaksi.

**Contoh output yang diharapkan:**

```text
=== INVENTARIS AWAL ===
  spidol              12
  kertas HVS (rim)     5
  lakban               3

=== TRANSAKSI ===
Tambah spidol 6 -> stok 18
Ambil lakban 3 -> sisa 0
Ambil kertas HVS (rim) 10 -> gagal: stok hanya 5
Ambil stapler 1 -> gagal: barang tidak terdaftar
Tambah stapler 2 -> stok 2

=== INVENTARIS AKHIR ===
  spidol              18
  kertas HVS (rim)     5
  lakban               0
  stapler              2
Jumlah jenis barang: 4
Barang habis       : lakban
```

<details>
<summary>💡 Petunjuk</summary>

- Pola tambah: `stok[nama] = stok.get(nama, 0) + jumlah` / `stok.put(nama, stok.getOrDefault(nama, 0) + jumlah)`.
- Java: pakai `LinkedHashMap` agar urutan tampil sesuai urutan didaftarkan.
- Format baris: `f"  {nama:<18}{jumlah:>4}"` / `String.format("  %-18s%4d", nama, jumlah)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_inventaris.py) · [☕ Java](java/solusi/Latihan02Inventaris.java)

---

## Latihan 3 — Frekuensi Kata (⭐⭐ Menengah)

**Tujuan:** menghitung kemunculan dengan map, lalu mengurutkan dengan dua kriteria.

**Soal:** Hitung frekuensi kata pada teks berikut (abaikan huruf besar/kecil, buang titik dan koma):

> Kopi susu gula aren enak. Kopi hitam juga enak, tapi kopi susu paling laris di kedai.

Tampilkan jumlah kata, jumlah kata unik, tiga kata terbanyak (jika seri, urut abjad), dan kata-kata yang muncul sekali (urut abjad).

**Contoh output yang diharapkan:**

```text
=== FREKUENSI KATA ===
Jumlah kata     : 16
Jumlah kata unik: 12
3 kata terbanyak:
  1. kopi (3 kali)
  2. enak (2 kali)
  3. susu (2 kali)
Muncul sekali   : aren, di, gula, hitam, juga, kedai, laris, paling, tapi
```

<details>
<summary>💡 Petunjuk</summary>

- Bersihkan teks: `teks.lower().replace(".", "").replace(",", "")`, lalu `split()` / `split(" ")`.
- Python: `sorted(frekuensi.items(), key=lambda p: (-p[1], p[0]))`.
- Java: salin `entrySet()` ke `ArrayList`, lalu urutkan dengan lambda: `Integer.compare(b.getValue(), a.getValue())`, dan jika hasilnya 0, bandingkan kuncinya.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_frekuensi_kata.py) · [☕ Java](java/solusi/Latihan03FrekuensiKata.java)

---

## Latihan 4 — Ranking Nilai Mahasiswa (⭐⭐ Menengah)

**Tujuan:** membedakan urutan alami dan urutan khusus tiga kriteria.

**Soal:** Buat kelas `NilaiMahasiswa` (NIM, nama, nilai akhir, nilai UAS) yang **urutan alaminya** berdasarkan NIM. Tampilkan daftar urut NIM, lalu ranking kelas: nilai akhir tertinggi dulu; jika seri, nilai UAS tertinggi; jika masih seri, nama A-Z. Terakhir, hitung yang lulus (nilai akhir ≥ 70) dan tampilkan peringkat 1.

| NIM | Nama | Nilai akhir | UAS |
|---|---|---|---|
| 2409106003 | Citra Dewi | 88 | 90 |
| 2409106001 | Ayu Lestari | 88 | 85 |
| 2409106005 | Eka Putri | 75 | 80 |
| 2409106002 | Bima Saputra | 75 | 80 |
| 2409106004 | Dimas Pratama | 64 | 60 |

**Contoh output yang diharapkan:**

```text
=== URUT NIM (urutan alami) ===
2409106001 Ayu Lestari
2409106002 Bima Saputra
2409106003 Citra Dewi
2409106004 Dimas Pratama
2409106005 Eka Putri

=== RANKING KELAS ===
1. Citra Dewi      88 (UAS 90)
2. Ayu Lestari     88 (UAS 85)
3. Bima Saputra    75 (UAS 80)
4. Eka Putri       75 (UAS 80)
5. Dimas Pratama   64 (UAS 60)

Lulus (nilai akhir >= 70): 4 orang
Peringkat 1: Citra Dewi
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `__lt__` membandingkan NIM; ranking memakai `key=lambda m: (-m.nilai_akhir, -m.nilai_uas, m.nama)`.
- Java: `implements Comparable<NilaiMahasiswa>`; ranking memakai `Comparator.comparing(NilaiMahasiswa::getNilaiAkhir).reversed()`, lalu `.thenComparing(NilaiMahasiswa::getNilaiUas, Comparator.reverseOrder())`, lalu `.thenComparing(NilaiMahasiswa::getNama)`. Hati-hati: `.reversed()` di **akhir** rantai membalik semua kriteria, termasuk nama.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_ranking_nilai.py) · [☕ Java](java/solusi/Latihan04RankingNilai.java)

---

## Latihan 5 — KedaiKita: Menu Tak Laku dan Rata-rata Porsi (⭐⭐ Menengah)

**Tujuan:** mengembangkan laporan studi kasus KedaiKita dengan dict/Map dan set.

**Soal:** Pemilik KedaiKita menambah dua menu baru, M06 Teh Tarik dan M07 Roti Bakar Cokelat, lalu ingin tahu menu mana yang **tidak laku** dan berapa **rata-rata porsi** per pesanan. Pakai empat pesanan lunas dari studi kasus:

| Pesanan | Isi |
|---|---|
| P001 (Budi) | M01 x 2, M03 x 1 |
| P002 (Siti) | M02 x 2, M05 x 1 |
| P003 (Rina) | M01 x 1, M04 x 1 |
| P004 (Budi) | M01 x 1, M02 x 2 |

Buat kelas `ItemBeli` (kode, jumlah) dan `AnalisisPenjualan` yang menerima daftar menu (kode → nama) dan daftar pesanan lunas, dengan method `porsi_per_menu()` (semua menu tampil, termasuk yang 0), `menu_tak_laku()`, `total_porsi()`, dan `rata_rata_porsi_x100()`.

**Contoh output yang diharapkan:**

```text
=== PORSI TERJUAL PER MENU ===
M01 Kopi Susu Gula Aren       4
M02 Es Teh Manis              4
M03 Nasi Goreng Kampung       1
M04 Mie Goreng Jawa           1
M05 Pisang Goreng Keju        1
M06 Teh Tarik                 0
M07 Roti Bakar Cokelat        0

=== RINGKASAN ===
Pesanan lunas  : 4
Total porsi    : 11
Rata-rata porsi: 2.75 porsi per pesanan
Menu tak laku  : Teh Tarik, Roti Bakar Cokelat
```

<details>
<summary>💡 Petunjuk</summary>

- Isi semua kode dengan 0 dulu: `{kode: 0 for kode in daftar_menu}` / perulangan `put(kode, 0)`, baru tambahkan porsinya.
- Menu tak laku = himpunan semua kode **dikurangi** himpunan kode yang pernah terjual.
- Rata-rata tanpa float: hitung `total * 100 // jumlah_pesanan` (275), lalu cetak sebagai `2` titik `75`.
- Pengguna Java: jangan beri nama kelas `ItemPesanan` atau `LaporanPenjualan`, karena nama itu sudah dipakai studi kasus di folder `java/` yang sama.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_menu_tak_laku.py) · [☕ Java](java/solusi/Latihan05MenuTakLaku.java)

---

## Latihan 6 — Pengelompok Generik (⭐⭐⭐ Tantangan)

**Tujuan:** menulis fungsi/method generik yang menerima lambda.

**Soal:** Tulis fungsi generik `kelompokkan(daftar, kunci)` yang menerima list berisi tipe **apa pun** (`T`) dan sebuah fungsi `kunci` yang mengubah setiap isi menjadi kunci bertipe **apa pun** (`K`). Hasilnya map *kunci → list isi*, dengan kunci sesuai urutan kemunculan pertama. Uji dengan tiga kasus: buah (apel, anggur, belimbing, ceri, bisbul, alpukat) per huruf awal, buah per panjang nama, dan anggota UKM per angkatan (Bima 2023, Ayu 2024, Eka 2023, Citra 2024, Dimas 2025).

**Contoh output yang diharapkan:**

```text
=== BUAH PER HURUF AWAL ===
a: apel, anggur, alpukat
b: belimbing, bisbul
c: ceri

=== BUAH PER PANJANG NAMA ===
4 huruf: apel, ceri
6 huruf: anggur, bisbul
9 huruf: belimbing
7 huruf: alpukat

=== ANGGOTA UKM PER ANGKATAN ===
2023: Bima, Eka (2 orang)
2024: Ayu, Citra (2 orang)
2025: Dimas (1 orang)
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `T = TypeVar("T")`, `K = TypeVar("K")`, dan tipe fungsi kuncinya `Callable[[T], K]` (dari `typing`). Kuncinya bisa `lambda kata: kata[0]`, fungsi bawaan `len`, atau `lambda a: a.angkatan`.
- Java: `static <T, K> Map<K, List<T>> kelompokkan(List<T> daftar, Function<T, K> kunci)`. `Function` ada di `java.util.function`; panggil dengan `kunci.apply(isi)`. Kuncinya bisa `kata -> kata.substring(0, 1)`, `String::length`, atau `Anggota::getAngkatan`.
- Jika kunci belum ada di map, simpan dulu list kosong untuk kunci itu, baru tambahkan isinya.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_pengelompok_generik.py) · [☕ Java](java/solusi/Latihan06PengelompokGenerik.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Klasemen Turnamen Futsal Antarprodi

Himpunan mahasiswa mengadakan turnamen futsal antarprodi dan butuh program klasemen.

**Kebutuhan:**

1. Kelas `Tim` dengan nama tim. Dua tim dianggap sama jika namanya sama (`__eq__` + `__hash__` / `equals` + `hashCode`).
2. Kelas generik `Skor[A, B]` / `Skor<A, B>` (atau sejenisnya) untuk menyimpan pasangan gol tim kandang dan tim tamu.
3. Kelas `Klasemen` yang menyimpan statistik setiap tim di dalam dict/Map (`Tim` → statistik): main, menang, seri, kalah, gol memasukkan, gol kemasukan, dan poin (menang 3, seri 1, kalah 0).
4. Klasemen diurutkan dengan urutan khusus: poin terbanyak → selisih gol terbesar → gol memasukkan terbanyak → nama A-Z.
5. Tampilkan klasemen dalam bentuk tabel rapi, lalu daftar tim yang **belum pernah menang** (pakai set, cetak urut abjad).
6. Minimal 4 tim dan 6 pertandingan. Data ditulis langsung di program (tanpa input dari keyboard).

**Ketentuan pengumpulan:** satu program (Python atau Java) beserta tangkapan layar output-nya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kelas `Tim` dengan aturan kesamaan dan hash yang benar | 20% |
| Pemakaian dict/Map dan set yang tepat | 25% |
| Pengurutan empat kriteria benar, termasuk saat ada poin yang seri | 30% |
| Kelas generik dipakai dengan benar | 10% |
| Kerapian kode dan output (nama jelas, tabel rapi, output deterministik) | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
