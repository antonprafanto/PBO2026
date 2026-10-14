# Latihan — Pertemuan 14: Design Pattern Dasar

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Sebelum menulis kode, sebutkan dulu **peran** setiap kelas: mana Singleton-nya, mana factory dan produknya, mana *context* dan strateginya, mana *subject* dan pengamatnya. Jika perannya sudah jelas, kodenya biasanya mengalir dengan sendirinya.

---

## Latihan 1 — Mesin Antrean (⭐ Dasar)

**Tujuan:** menerapkan pola Singleton.

**Soal:** Sebuah kantor pelayanan punya dua pintu masuk, Pintu Utara dan Pintu Selatan. Di setiap pintu ada tombol pengambil nomor, tetapi semua tombol harus terhubung ke **satu** mesin antrean agar nomornya tidak pernah kembar.

- Buat kelas Singleton `MesinAntrean` dengan method `ambil_nomor()` / `ambilNomor()` yang mengembalikan nomor berformat `A001`, `A002`, dan seterusnya, serta `jumlah_dibagikan()` / `jumlahDibagikan()`.
- Buat kelas `TombolAntrean(lokasi)` dengan method `tekan()` yang meminta nomor dari mesin lewat `get_instance()` / `getInstance()` lalu mencetaknya.
- Tekan tombol berurutan: Utara, Utara, Selatan, Utara, Selatan. Lalu buktikan bahwa mesinnya objek yang sama.

**Contoh output yang diharapkan:**

```text
=== PENGUNJUNG MENGAMBIL NOMOR ===
Pintu Utara   : nomor A001
Pintu Utara   : nomor A002
Pintu Selatan : nomor A003
Pintu Utara   : nomor A004
Pintu Selatan : nomor A005

=== RINGKASAN ===
Mesin yang sama? ya
Total nomor dibagikan: 5
```

<details>
<summary>💡 Petunjuk</summary>

- Tiru struktur `Konfigurasi` di contoh 01: atribut kelas/field `static` untuk objeknya, penjaga di `__init__` (Python) atau konstruktor `private` (Java).
- Format nomor: `f"A{n:03d}"` di Python, `String.format("A%03d", n)` di Java.
- Lokasi dirapikan 14 kolom: `f"{lokasi:<14}"` atau `String.format("%-14s", lokasi)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_mesin_antrean.py) · [☕ Java](java/solusi/Latihan01MesinAntrean.java)

---

## Latihan 2 — Factory Bangun Datar (⭐ Dasar)

**Tujuan:** menerapkan Simple Factory dengan produk abstrak.

**Soal:** Buat kelas abstrak `Bentuk` dengan method abstrak `nama()` dan `luas()` (bilangan bulat), lalu tiga kelas konkret: `Persegi(sisi)`, `PersegiPanjang(panjang, lebar)`, dan `Segitiga(alas, tinggi)`. Buat `BentukFactory.buat(jenis, a, b)` yang tidak peka huruf besar/kecil dan menolak jenis yang tidak dikenal. Program utama membuat bentuk dari daftar pesanan berikut, melewati yang ditolak, lalu menjumlahkan luasnya.

| Jenis (teks) | a | b |
|---|---|---|
| `persegi` | 5 | 0 |
| `Persegi Panjang` | 8 | 3 |
| `SEGITIGA` | 6 | 4 |
| `lingkaran` | 7 | 0 |

**Contoh output yang diharapkan:**

```text
=== MEMBUAT BENTUK DARI PILIHAN TEKS ===
Persegi sisi 5                 luas 25
Persegi panjang 8 x 3          luas 24
Segitiga alas 6 tinggi 4       luas 12
Ditolak: Bentuk tidak dikenal: lingkaran

Total luas bentuk yang berhasil dibuat: 61
```

<details>
<summary>💡 Petunjuk</summary>

- Luas segitiga dengan bilangan bulat: `alas * tinggi // 2` (Python) atau `alas * tinggi / 2` (Java).
- Tangkap penolakan di dalam perulangan, cetak pesannya, lalu lanjut ke pesanan berikutnya (`continue`).
- Nama bentuk dirapikan 30 kolom: `f"{bentuk.nama():<30} luas {bentuk.luas()}"`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_factory_bentuk.py) · [☕ Java](java/solusi/Latihan02FactoryBentuk.java)

---

## Latihan 3 — Strategy Pengurutan Mahasiswa (⭐⭐ Menengah)

**Tujuan:** menukar algoritma pengurutan saat program berjalan.

**Soal:** Buat kelas `Mahasiswa(nim, nama, nilai)` dan kontrak `StrategiUrut` dengan method `nama()` serta `urutkan(daftar)` yang mengembalikan list **baru**. Buat tiga strategi: `UrutNim`, `UrutNama` (A–Z), dan `UrutNilai` (nilai tertinggi dulu; jika sama, nama A–Z). Kelas *context* `DaftarPeringkat` menyimpan satu strategi, bisa ditukar lewat `atur_strategi()` / `aturStrategi()`, dan punya method `tampilkan()`. Data:

| NIM | Nama | Nilai |
|---|---|---|
| 2409106004 | Ayu Lestari | 85 |
| 2409106002 | Bima Saputra | 92 |
| 2409106001 | Citra Dewi | 85 |
| 2409106003 | Dimas Pratama | 78 |

**Contoh output yang diharapkan:**

```text
=== URUT: NIM TERKECIL ===
1. 2409106001 Citra Dewi       85
2. 2409106002 Bima Saputra     92
3. 2409106003 Dimas Pratama    78
4. 2409106004 Ayu Lestari      85

=== URUT: NAMA A-Z ===
1. 2409106004 Ayu Lestari      85
2. 2409106002 Bima Saputra     92
3. 2409106001 Citra Dewi       85
4. 2409106003 Dimas Pratama    78

=== URUT: NILAI TERTINGGI ===
1. 2409106002 Bima Saputra     92
2. 2409106004 Ayu Lestari      85
3. 2409106001 Citra Dewi       85
4. 2409106003 Dimas Pratama    78
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `sorted(daftar, key=lambda m: (-m.nilai, m.nama))` untuk nilai tertinggi lalu nama.
- Java: salin dulu ke `new ArrayList<>(daftar)`, lalu `sort(Comparator.comparing(Mahasiswa::getNilai).reversed().thenComparing(Mahasiswa::getNama))`.
- Baris mahasiswa: `f"{nim} {nama:<15}{nilai:>4}"` atau `String.format("%s %-15s%4d", nim, nama, nilai)`.
- Renungkan: `key=` dan `Comparator` dari Pertemuan 12 sebenarnya juga "strategi kecil".

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_strategy_urutan.py) · [☕ Java](java/solusi/Latihan03StrategyUrutan.java)

---

## Latihan 4 — Observer Stok Gudang (⭐⭐ Menengah)

**Tujuan:** menerapkan Observer dengan gaya *push*.

**Soal:** Sebuah gudang sembako ingin pemasok dan admin langsung tahu saat stok menipis.

- Kontrak `PengamatGudang` punya satu method: `stok_menipis(nama_barang, sisa)` / `stokMenipis(namaBarang, sisa)`.
- Dua pengamat: `Pemasok(nama)` dan `AdminGudang` (menghitung jumlah peringatan).
- *Subject* `Gudang` menyimpan stok (dict/`LinkedHashMap`) dan daftar pengamat. Method `ambil(nama_barang, jumlah)` mengurangi stok, mencetak sisa, lalu memberi kabar ke semua pengamat **jika sisa di bawah 10**.
- Stok awal: Beras 50, Gula 20, Minyak 15. Lalu ambil Beras 30, Gula 12, Minyak 3, Gula 5.

**Contoh output yang diharapkan:**

```text
=== TRANSAKSI GUDANG (BATAS MINIMUM 10) ===
Ambil 30 Beras, sisa 20
Ambil 12 Gula, sisa 8
  [Pemasok Pak Rahman] Siap mengirim Gula tambahan
  [Admin] Catat: stok Gula tinggal 8
Ambil 3 Minyak, sisa 12
Ambil 5 Gula, sisa 3
  [Pemasok Pak Rahman] Siap mengirim Gula tambahan
  [Admin] Catat: stok Gula tinggal 3

=== RINGKASAN ===
Peringatan yang dicatat admin: 2
```

<details>
<summary>💡 Petunjuk</summary>

- Batas minimum cocok dijadikan konstanta kelas: `BATAS_MINIMUM = 10`.
- Pisahkan pemberian kabar ke method tersendiri, misalnya `_beri_kabar()` / `beriKabar()`, seperti `KanalVideo` di contoh 07.
- Gudang tidak boleh tahu kelas `Pemasok` atau `AdminGudang`; ia hanya mengenal `PengamatGudang`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_observer_gudang.py) · [☕ Java](java/solusi/Latihan04ObserverGudang.java)

---

## Latihan 5 — KedaiKita: Diskon Pelajar (⭐⭐ Menengah)

**Tujuan:** menambah strategi baru di KedaiKita tanpa mengubah kelas pesanan.

**Soal:** KedaiKita ingin memberi potongan untuk pelajar: **10% dari subtotal, paling banyak Rp5.000**. Buat strategi `DiskonPelajar` dengan keterangan `Pelajar 10%`. Di salinan studi kasusmu sendiri, cukup tambahkan kelas itu ke `diskon.py` (Java: file `DiskonPelajar.java` yang meng-*implements* `Diskon`), lalu bandingkan dengan `TanpaDiskon` dan `DiskonHappyHour` pada dua pesanan: (1) 2 Es Teh Manis + 1 Pisang Goreng Keju, (2) 2 Kopi Susu Gula Aren + 1 Mie Goreng Jawa. Pajak 10% dihitung dari subtotal setelah diskon.

**Contoh output yang diharapkan:**

```text
=== 2 ES TEH MANIS + 1 PISANG GORENG KEJU ===
Subtotal: Rp31.000
Tanpa diskon           potongan      Rp0, total Rp34.100
Happy Hour (minuman)   potongan  Rp3.200, total Rp30.580
Pelajar 10%            potongan  Rp3.100, total Rp30.690

=== 2 KOPI SUSU GULA AREN + 1 MIE GORENG JAWA ===
Subtotal: Rp59.000
Tanpa diskon           potongan      Rp0, total Rp64.900
Happy Hour (minuman)   potongan  Rp7.200, total Rp56.980
Pelajar 10%            potongan  Rp5.000, total Rp59.400
```

Perhatikan pesanan kedua: 10% dari Rp59.000 adalah Rp5.900, tetapi potongannya dibatasi Rp5.000.

<details>
<summary>💡 Petunjuk</summary>

- Inti strateginya dua baris: hitung `subtotal * 10 // 100`, lalu ambil yang lebih kecil antara hasil itu dan 5000 (`min()` / `Math.min()`).
- Kelas pesanan **tidak boleh** diubah. Jika kamu tergoda menambah `if` di dalamnya, berarti strateginya belum lengkap.
- Solusi di bawah memakai versi **mini** studi kasus agar bisa dijalankan sendiri, dengan nama kelas berbeda (`MenuKedai`, `ItemKeranjang`, `AturanDiskon`, `Keranjang`). Pengguna Java: nama `Menu`, `Diskon`, dan `Pesanan` sudah dipakai studi kasus di folder `java/` yang sama.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_diskon_pelajar.py) · [☕ Java](java/solusi/Latihan05DiskonPelajar.java)

---

## Latihan 6 — KedaiKita: Pengamat Stok (⭐⭐⭐ Tantangan)

**Tujuan:** menambah pengamat baru bergaya *pull* tanpa mengubah *subject*.

**Soal:** Dapur KedaiKita sering kehabisan bahan tanpa sadar. Buat pengamat `PengamatStok(batas)` yang hanya bereaksi saat status pesanan menjadi `LUNAS`. Saat itu, ia **menarik** daftar item dari pesanan dan memeriksa stok setiap menunya. Jika stok kurang dari atau sama dengan `batas`, cetak `[STOK] Peringatan: <nama menu> tinggal <n> porsi`. Status lain diabaikan.

Skenario (batas 5): stok awal Kopi Susu Gula Aren 20, Nasi Goreng Kampung 6, Pisang Goreng Keju 5. Pesanan P001 berisi 2 kopi dan 3 nasi goreng, lalu berstatus `LUNAS` dan `DIPROSES`. Pesanan P002 berisi 1 kopi dan 1 pisang goreng, lalu `LUNAS`. Setiap pesanan juga diamati sebuah layar yang mencetak setiap perubahan status.

**Contoh output yang diharapkan:**

```text
=== PESANAN P001 ===
Isi: 2 x Kopi Susu Gula Aren, 3 x Nasi Goreng Kampung
  [LAYAR] P001 -> LUNAS
  [STOK] Peringatan: Nasi Goreng Kampung tinggal 3 porsi
  [LAYAR] P001 -> DIPROSES

=== PESANAN P002 ===
Isi: 1 x Kopi Susu Gula Aren, 1 x Pisang Goreng Keju
  [LAYAR] P002 -> LUNAS
  [STOK] Peringatan: Pisang Goreng Keju tinggal 4 porsi

=== SISA STOK ===
Kopi Susu Gula Aren  17 porsi
Nasi Goreng Kampung   3 porsi
Pisang Goreng Keju    4 porsi
```

<details>
<summary>💡 Petunjuk</summary>

- Ingat urutan di studi kasus: stok berkurang saat item **ditambahkan** ke pesanan, bukan saat dibayar.
- Langkah pertama `perbarui()`: jika status bukan `LUNAS`, langsung `return`.
- Satu objek `PengamatStok` boleh didaftarkan ke banyak pesanan sekaligus.
- Solusi memakai versi **mini** studi kasus dengan nama `MenuStok`, `BarisPesanan`, `PesananKedai`, `PengamatStatus`, dan `LayarPesanan`, agar bisa dijalankan sendiri dan tidak bentrok dengan kelas studi kasus di folder Java.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_pengamat_stok.py) · [☕ Java](java/solusi/Latihan06PengamatStok.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Aplikasi Pemesanan Lapangan Futsal

GOR futsal di dekat kampus ingin aplikasi pemesanan lapangan sederhana. Rancang dan buat programnya dengan menerapkan **minimal tiga** dari empat pola yang dipelajari hari ini.

**Kebutuhan:**

1. **Singleton** `PengaturanGor`: nama GOR, alamat, jam buka, dan jam tutup. Semua bagian program membaca pengaturan dari objek yang sama.
2. **Factory** `LapanganFactory.buat(jenis)`: membuat `LapanganVinyl` atau `LapanganSintetis` dari teks, masing-masing dengan tarif dasar per jam yang berbeda. Jenis yang tidak dikenal harus ditolak dengan *exception*.
3. **Strategy** tarif: minimal tiga aturan, misalnya `TarifSiang`, `TarifMalam` (lebih mahal), dan `TarifMember` (potongan). Aturan tarif sebuah pemesanan bisa ditukar sebelum dibayar.
4. **Observer**: `Pemesanan` (subject) punya status `BARU`, `DIKONFIRMASI`, `SELESAI`, atau `DIBATALKAN`. Setiap perubahan status memberi kabar ke minimal dua pengamat, misalnya `NotifikasiPemesan` dan `PapanJadwal`.
5. Program utama menjalankan skenario demo minimal **tiga** pemesanan, tanpa `input()`/`Scanner`. Uang memakai bilangan bulat.
6. Sertakan **diagram kelas** (boleh Mermaid atau gambar tangan yang difoto) yang menandai peran setiap kelas dalam pola.

**Ketentuan pengumpulan:** kode program (Python atau Java), tangkapan layar output, diagram kelas, dan satu paragraf penjelasan: pola mana yang dipakai, di kelas mana, dan mengapa.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Penerapan pola benar (peran kelas sesuai pola, bukan sekadar nama kelas) | 40% |
| Program berjalan, skenario demo lengkap, output rapi | 20% |
| Diagram kelas sesuai dengan kode | 15% |
| Penjelasan alasan memilih pola (termasuk pola yang **tidak** dipakai) | 15% |
| Kerapian kode: nama jelas, enkapsulasi, komentar secukupnya | 10% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
