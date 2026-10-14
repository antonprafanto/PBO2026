# Kuis — Pertemuan 14: Design Pattern Dasar

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 15 ➡️](../Pertemuan-15-Proyek-Terintegrasi/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Pernyataan yang paling tepat tentang *design pattern* adalah ...

- A. Pustaka kode siap pakai yang tinggal di-*import* ke dalam program
- B. Solusi umum yang sudah teruji untuk masalah desain yang berulang, dan perlu disesuaikan dengan program masing-masing
- C. Aturan wajib yang harus dipakai di setiap program berorientasi objek
- D. Fitur khusus bahasa Java yang tidak tersedia di Python

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: pola adalah gambaran susunan kelas dan objek, bukan kode jadi (A salah). Pola juga tidak wajib; memaksakan pola pada program kecil malah membuatnya rumit (C salah). Keempat pola hari ini bisa ditulis di Python maupun Java, hanya caranya yang berbeda (D salah).

</details>

### Soal 2

Buku *Design Patterns* karya Gang of Four (1994) memuat ...

- A. 23 pola yang dibagi menjadi 3 kategori: *creational*, *structural*, dan *behavioral*
- B. 4 pola, yaitu Singleton, Factory, Strategy, dan Observer, sesuai jumlah penulisnya
- C. 16 pola yang dibagi menurut bahasa pemrogramannya
- D. 5 prinsip SOLID beserta contoh kodenya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: buku GoF berisi 23 pola dalam tiga kategori: pembuatan objek (*creational*), struktur (*structural*), dan perilaku (*behavioral*). Julukan "Gang of Four" berasal dari jumlah penulisnya, bukan jumlah pola (B salah). Pola-polanya tidak terikat bahasa tertentu (C salah), dan SOLID adalah prinsip yang berbeda dari design pattern (D salah).

</details>

### Soal 3

Perhatikan kode berikut. `PengaturanKedai` adalah Singleton dari studi kasus, dengan pajak awal 10.

**Python:**

```python
a = PengaturanKedai.get_instance()
b = PengaturanKedai.get_instance()
a.pajak_persen = 11
print(b.pajak_persen)
```

**Java:**

```java
PengaturanKedai a = PengaturanKedai.getInstance();
PengaturanKedai b = PengaturanKedai.getInstance();
a.setPajakPersen(11);
System.out.println(b.getPajakPersen());
```

Apa yang tercetak?

- A. `10`
- B. Error, karena permintaan kedua ditolak oleh Singleton
- C. `11`
- D. `0`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `a` dan `b` menunjuk ke **objek yang sama**, jadi perubahan lewat `a` terbaca lewat `b`. Pilihan A adalah miskonsepsi "setiap variabel punya objek sendiri". Pilihan B salah karena `get_instance()`/`getInstance()` boleh dipanggil berkali-kali; yang ditolak adalah pembuatan objek **langsung** lewat konstruktor.

</details>

### Soal 4

Apa kekurangan utama pola Singleton?

- A. Program menjadi lambat karena objeknya dibuat ulang setiap kali diminta
- B. Objek Singleton tidak boleh punya method
- C. Singleton tidak bisa ditulis di Python
- D. Isinya menjadi *state* global: perubahan dari satu bagian program diam-diam memengaruhi bagian lain, dan pengujian bisa saling mengganggu

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: di contoh 03, uji yang tadinya LULUS menjadi GAGAL hanya karena uji lain mengubah pengaturan dan lupa mengembalikannya. Pilihan A terbalik: objek Singleton justru hanya dibuat **sekali**. Pilihan B dan C jelas salah; `PengaturanKedai` punya banyak method dan ditulis di kedua bahasa.

</details>

### Soal 5

Apa manfaat utama `PembayaranFactory` di KedaiKita?

- A. Pembayaran diproses lebih cepat
- B. Kode pemanggil cukup mengirim teks pilihan, lalu menerima objek bertipe `Pembayaran` tanpa perlu mengenal kelas konkretnya
- C. Kelas `PembayaranTunai`, `PembayaranQRIS`, dan `PembayaranKartu` tidak diperlukan lagi
- D. Factory menjamin hanya ada satu objek pembayaran di seluruh program

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: factory memusatkan keputusan "kelas mana yang dibuat" di satu tempat, termasuk validasi pilihan yang tidak dikenal. Kelas-kelas konkret tetap dibutuhkan, karena factory-lah yang membuatnya (C salah). Menjamin satu objek adalah tugas Singleton, bukan Factory (D salah). Kecepatan tidak berubah (A salah).

</details>

### Soal 6

Apa perbedaan *Simple Factory* dan *Factory Method* versi GoF?

- A. *Simple Factory* termasuk 23 pola GoF, sedangkan *Factory Method* tidak
- B. *Factory Method* selalu berupa method *static* berisi `if`/`elif`
- C. Pada *Factory Method*, kelas anak meng-*override* method pembuat produk, sehingga pemilihan produk terjadi lewat *overriding*, bukan lewat `if`
- D. Keduanya sama persis, hanya namanya yang berbeda

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: di contoh 05, `EkspedisiDarat` dan `EkspedisiSungai` masing-masing meng-*override* `buat_angkutan()`/`buatAngkutan()`. Pilihan A terbalik: *Factory Method* ada di buku GoF, *Simple Factory* adalah idiom populer. Pilihan B justru menggambarkan *Simple Factory*.

</details>

### Soal 7

Es Teh Manis berharga Rp8.000 (kategori Minuman) dan Nasi Goreng Kampung Rp25.000 (kategori Makanan). Pajak dari `PengaturanKedai` adalah 10%.

**Python:**

```python
pesanan.tambah_item(es_teh, 2)
pesanan.tambah_item(nasi_goreng, 1)
pesanan.atur_diskon(DiskonHappyHour())
print(pesanan.hitung_total())
```

**Java:**

```java
pesanan.tambahItem(esTeh, 2);
pesanan.tambahItem(nasiGoreng, 1);
pesanan.aturDiskon(new DiskonHappyHour());
System.out.println(pesanan.hitungTotal());
```

Apa yang tercetak?

- A. `41580`
- B. `37800`
- C. `41000`
- D. `45100`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: subtotal = 2 × 8.000 + 25.000 = 41.000. Happy Hour hanya memotong minuman: 20% × 16.000 = 3.200. Pajak dihitung **setelah** diskon: (41.000 − 3.200) × 10% = 3.780. Total = 41.000 − 3.200 + 3.780 = **41.580**. Pilihan B lupa pajak, C mengabaikan diskon dan pajak, sedangkan D menambah pajak tanpa diskon.

</details>

### Soal 8

Mengapa menambah `DiskonHappyHour` sama sekali tidak mengubah kelas `Pesanan`?

- A. Karena `DiskonHappyHour` mewarisi kelas `Pesanan`
- B. Karena Python dan Java otomatis membaca semua kelas diskon yang ada di folder
- C. Karena `Pesanan` memakai `if`/`elif` untuk setiap jenis diskon
- D. Karena `Pesanan` hanya bergantung pada abstraksi `Diskon` dan mendelegasikan hitungan ke objek strategi yang sedang dipasang

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: inilah pola Strategy yang sekaligus mewujudkan OCP. `Pesanan` (*context*) menyimpan satu objek `Diskon` dan memanggil `hitung_potongan()`/`hitungPotongan()` miliknya. `DiskonHappyHour` mewarisi/mengimplementasikan `Diskon`, bukan `Pesanan` (A salah). Pilihan C adalah kondisi **sebelum** refactor di Pertemuan 13.

</details>

### Soal 9

Di KedaiKita, `Pesanan` memanggil `pengamat.perbarui(self)` / `pengamat.perbarui(this)`. Gaya Observer apa ini, dan mengapa?

- A. *Push*, karena pesanan "mendorong" kabar ke semua pengamat
- B. *Push*, karena status pesanan dikirim sebagai teks
- C. *Pull*, karena subject mengirim dirinya sendiri, lalu setiap pengamat mengambil data yang ia butuhkan
- D. *Pull*, karena setiap pengamat memeriksa status pesanan berulang-ulang setiap detik

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `LayarDapur` menarik nomor dan daftar item, sedangkan `NotifikasiPelanggan` menarik nama dan nomor HP pelanggan, dari objek pesanan yang sama. Pada gaya *push* (contoh 07), yang dikirim adalah data kejadiannya, misalnya judul video. Pilihan D menggambarkan *polling*, bukan Observer: pada Observer, pengamat justru **menunggu dikabari**.

</details>

### Soal 10

Perhatikan kode berikut. Pesanan baru saja dibuat dan belum punya pengamat.

**Python:**

```python
pesanan.tambah_pengamat(LayarDapur())
pesanan.tambah_pengamat(NotifikasiPelanggan())
pesanan.tambah_pengamat(LayarDapur())
pesanan.ubah_status("DIPROSES")
pesanan.ubah_status("SIAP")
```

**Java:**

```java
pesanan.tambahPengamat(new LayarDapur());
pesanan.tambahPengamat(new NotifikasiPelanggan());
pesanan.tambahPengamat(new LayarDapur());
pesanan.ubahStatus("DIPROSES");
pesanan.ubahStatus("SIAP");
```

Berapa kali method `perbarui()` dipanggil secara total?

- A. 2
- B. 6
- C. 3
- D. 4

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: daftar pengamat berisi **tiga** objek (dua di antaranya sama-sama `LayarDapur`, tetapi tetap dua objek berbeda). Setiap `ubah_status()`/`ubahStatus()` memanggil `perbarui()` milik ketiganya, jadi 3 × 2 = 6. Pilihan A hanya menghitung jumlah perubahan status, sedangkan D lupa bahwa `LayarDapur` didaftarkan dua kali.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Keempat pola sudah kamu kuasai | Lanjut ke [Pertemuan 15](../Pertemuan-15-Proyek-Terintegrasi/README.md), tempat semua materi dirangkai menjadi satu proyek |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian konsep untuk pola yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 4 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan ketujuh contoh di halaman praktik, dan cocokkan setiap output dengan penjelasannya |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 15 ➡️](../Pertemuan-15-Proyek-Terintegrasi/README.md)
