# ☕ Solusi Praktik Java — Pertemuan 08: UTS

[⬅️ Informasi UTS](../README.md) · [🐍 Solusi Python](../python/README.md) · [Pembahasan ➡️](../pembahasan.md)

> **Prasyarat:** sudah mencoba sendiri [Soal C1 dan C2](../latihan-soal.md#bagian-c-soal-praktik). Halaman ini menjelaskan cara menjalankan solusi Java dan bagian-bagian terpenting kodenya. Alasan pemilihan kelas dan relasi dibahas di [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).

## Daftar Isi

- [Persiapan](#persiapan)
1. [Soal C1: Peminjaman Alat Laboratorium](#1-soal-c1-peminjaman-alat-laboratorium)
2. [Soal C2: Toko Buku Daring](#2-soal-c2-toko-buku-daring)
3. [Membandingkan Output-mu dengan Solusi](#3-membandingkan-output-mu-dengan-solusi)
4. [Kesalahan Umum dan Cara Membaca Pesan Error](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
└── solusi/
    ├── SoalC1PeminjamanAlat.java   <- solusi Soal C1
    └── SoalC2TokoBuku.java         <- solusi Soal C2
```

Setiap solusi adalah **program satu file**: kelas `public` yang memiliki `main` ditulis paling atas, lalu kelas-kelas pembantunya di bawahnya tanpa kata `public`. Cara menjalankannya (Java 11 ke atas):

```bash
cd Pertemuan-08-UTS/java/solusi
java SoalC1PeminjamanAlat.java
java SoalC2TokoBuku.java
```

Cara klasik dua langkah juga bisa dipakai:

```bash
javac SoalC1PeminjamanAlat.java
java SoalC1PeminjamanAlat
```

> [!NOTE]
> Perintah `javac` menghasilkan **satu file `.class` untuk setiap kelas** (`Alat.class`, `Mahasiswa.class`, dan seterusnya) di folder yang sama. Ini salah satu alasan nama kelas di dalam satu folder harus unik. Jika dua solusi sama-sama punya kelas `Rupiah`, file `Rupiah.class` milik solusi yang satu akan tertimpa oleh solusi yang lain.

Karena alasan itu, pemformat uang di solusi C1 bernama `RupiahLab` dan di solusi C2 bernama `RupiahToko`. Isinya sama dengan kelas `Rupiah` di KedaiKita:

```java
/** Kelas utilitas: mengubah 30000 menjadi "Rp30.000". */
class RupiahLab {
    public static String format(int angka) {
        // Locale.US agar pemisah ribuan selalu koma, lalu diganti titik.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}
```

> [!TIP]
> Jika memakai VS Code, buka folder `java/` **milik pertemuan ini** (*File → Open Folder*), bukan seluruh repositori. Dengan begitu, kelas-kelas dari pertemuan lain tidak bentrok nama. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

## 1. Soal C1: Peminjaman Alat Laboratorium

File: [`solusi/SoalC1PeminjamanAlat.java`](solusi/SoalC1PeminjamanAlat.java)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Mahasiswa` | Menyimpan data peminjam secara *read-only* | Field `private` + getter tanpa setter (P04), `toString()` (P03) |
| `Alat` | Menyimpan data dan status alat; meminjamkan, menerima kembali, menghitung denda | Enkapsulasi, method penjaga aturan (P04) |
| `AlatElektronik`, `KitPraktikum` | Menambah field, menentukan denda per hari, meng-*override* `toString()` | `extends`, `super(...)`, `@Override` (P07) |
| `Peminjaman` | Nomor otomatis, daftar alat, pengembalian dan denda, bukti peminjaman | Field `static` (P03), agregasi dan asosiasi (P05) |
| `Laboratorium` | Daftar alat, pencarian alat, catatan peminjaman | Agregasi, `null` (P05) |

### Kelas induk `Alat` dan kelas anaknya

Bagian awal kelas `Alat`:

```java
/** Kelas induk: data dan perilaku yang dimiliki SEMUA alat lab. */
class Alat {
    private String kode;
    private String nama;
    private int dendaPerHari;
    private boolean tersedia;

    public Alat(String kode, String nama, int dendaPerHari) {
        if (dendaPerHari <= 0) {
            throw new IllegalArgumentException("Denda per hari harus lebih dari 0");
        }
        this.kode = kode;
        this.nama = nama;
        this.dendaPerHari = dendaPerHari;
        this.tersedia = true; // [1] alat baru selalu tersedia
    }
```

Setelah deretan getter, kelas `Alat` punya method-method berikut:

```java
    /** Pintu resmi untuk mengubah status menjadi dipinjam. */
    public void pinjamkan() {
        if (!tersedia) {
            throw new IllegalArgumentException(nama + " sedang dipinjam"); // [2]
        }
        tersedia = false;
    }

    public void terimaKembali() {
        tersedia = true;
    }

    public int hitungDenda(int hariTerlambat) {
        return dendaPerHari * hariTerlambat;
    }

    @Override
    public String toString() {
        String status = tersedia ? "tersedia" : "dipinjam";
        return "[" + kode + "] " + nama + " - " + status;
    }
}
```

Salah satu kelas anaknya:

```java
/** Alat yang memakai listrik. Tambahan: daya dalam watt. */
class AlatElektronik extends Alat {
    private static final int DENDA_PER_HARI = 10000; // Rupiah

    private int dayaWatt;

    public AlatElektronik(String kode, String nama, int dayaWatt) {
        super(kode, nama, DENDA_PER_HARI); // [3] konstruktor induk, WAJIB baris pertama
        if (dayaWatt <= 0) {
            throw new IllegalArgumentException("Daya harus lebih dari 0 watt");
        }
        this.dayaWatt = dayaWatt;
    }

    public int getDayaWatt() {
        return dayaWatt;
    }

    @Override
    public String toString() {
        // [4] override: pakai teks dari induk, lalu tambahkan info daya
        return super.toString() + " | " + dayaWatt + " watt";
    }
}
```

Penjelasan:

- **[1]** Status awal tidak diambil dari parameter. Setiap alat baru otomatis tersedia. Field ini hanya dibaca lewat `isTersedia()` (getter boolean memakai awalan `is`) dan **tidak punya setter**.
- **[2]** `pinjamkan()` adalah satu-satunya pintu untuk mengubah status menjadi dipinjam. Jika alat sedang dipinjam, method menolak **sebelum** mengubah apa pun. Ekspresi `kondisi ? a : b` di `toString()` adalah bentuk singkat dari `if`/`else` yang menghasilkan nilai.
- **[3]** `super(...)` menjalankan konstruktor `Alat` dan mengirim denda per hari yang tetap. Di Java 17, panggilan ini **wajib** menjadi pernyataan pertama di konstruktor. Karena itu, pemeriksaan `dayaWatt` ditulis setelahnya.
- **[4]** `@Override` meminta *compiler* memastikan bahwa method ini benar-benar menimpa `toString()` milik induk. `super.toString()` memakai teks buatan induk. Kelas `KitPraktikum` ditulis dengan pola yang sama.

> [!NOTE]
> Field `kode` dan `nama` bersifat `private` di `Alat`, sehingga kelas anak **tidak bisa** membacanya langsung (lihat [Kesalahan 2](#kesalahan-2-mengakses-field-private-milik-induk)). Itulah sebabnya `AlatElektronik` memakai `super.toString()`, dan kelas lain memakai getter seperti `getKode()`.

### Kelas `Peminjaman`

```java
/** Satu transaksi: siapa meminjam, alat apa saja, dan berapa lama. */
class Peminjaman {
    private static final int MAKS_HARI_PINJAM = 7;
    private static final int LEBAR_BUKTI = 40;
    private static int nomorTerakhir = 0; // [5] milik kelas: penghitung nomor otomatis

    private String nomor;
    private Mahasiswa peminjam;
    private int lamaHari;
    private List<Alat> daftarAlat;
    private boolean selesai;

    public Peminjaman(Mahasiswa peminjam, int lamaHari) {
        if (lamaHari < 1 || lamaHari > MAKS_HARI_PINJAM) {
            throw new IllegalArgumentException(
                    "Lama pinjam harus 1 sampai " + MAKS_HARI_PINJAM + " hari");
        }
        nomorTerakhir++; // [6] bertambah HANYA jika data valid
        this.nomor = String.format("PJ%03d", nomorTerakhir); // PJ001, PJ002, ...
        this.peminjam = peminjam; // [7] asosiasi: menyimpan referensi Mahasiswa
        this.lamaHari = lamaHari;
        this.daftarAlat = new ArrayList<>(); // [8] agregasi: alat dibuat di luar
        this.selesai = false;
    }
```

Dua method terpentingnya:

```java
    public void tambahAlat(Alat alat) {
        if (selesai) {
            throw new IllegalArgumentException("Peminjaman " + nomor + " sudah selesai");
        }
        alat.pinjamkan(); // [9] gagal (exception) jika alat sedang dipinjam
        daftarAlat.add(alat);
    }

    /** Menerima kembali semua alat lalu MENGEMBALIKAN total denda. */
    public int kembalikan(int hariTerlambat) {
        if (selesai) {
            throw new IllegalArgumentException("Peminjaman " + nomor + " sudah selesai");
        }
        if (hariTerlambat < 0) {
            throw new IllegalArgumentException("Hari terlambat tidak boleh negatif");
        }
        int totalDenda = 0;
        for (Alat alat : daftarAlat) { // [10] mengirim pesan ke setiap alat
            alat.terimaKembali();
            totalDenda += alat.hitungDenda(hariTerlambat);
        }
        selesai = true;
        return totalDenda;
    }
```

Penjelasan:

- **[5]** `nomorTerakhir` bersifat `static`: hanya ada satu penghitung untuk semua objek `Peminjaman` (Pertemuan 03). Konstanta seperti `MAKS_HARI_PINJAM` memakai `static final`.
- **[6]** Penghitung baru bertambah setelah `lamaHari` lolos pemeriksaan, sehingga peminjaman 10 hari yang ditolak tidak "menghabiskan" nomor. `String.format("PJ%03d", ...)` menghasilkan tiga digit dengan nol di depan.
- **[7]** Peminjaman hanya **menyimpan referensi** ke objek `Mahasiswa` yang sudah ada (asosiasi).
- **[8]** List alat berisi objek yang dibuat di luar, yaitu yang didaftarkan ke lab (agregasi). Getter `getDaftarAlat()` mengembalikan `new ArrayList<>(daftarAlat)`, yaitu salinannya.
- **[9]** `pinjamkan()` dipanggil **sebelum** `add`. Jika alat sedang dipinjam, *exception* dilempar dan baris `add` tidak pernah dijalankan.
- **[10]** Peminjaman "mengirim pesan" ke setiap alat. Total denda **dikembalikan** dengan `return`, bukan dicetak.

Cara menjalankan:

```bash
cd Pertemuan-08-UTS/java/solusi
java SoalC1PeminjamanAlat.java
```

<details>
<summary>Lihat output lengkap Soal C1</summary>

**Output:**

```text
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - tersedia | 200 watt
[A02] Laptop Cadangan - tersedia | 65 watt
[K01] Kit Mikrokontroler - tersedia | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen

=== DATA TIDAK VALID DITOLAK ===
Gagal menambah alat: Daya harus lebih dari 0 watt
Gagal membuat peminjaman: Lama pinjam harus 1 sampai 7 hari
Cari X99: alat tidak ditemukan

=== PEMINJAMAN ===
========================================
BUKTI PEMINJAMAN PJ001
========================================
Peminjam : Ayu Lestari (2409106001)
Lama     : 3 hari
----------------------------------------
Alat                          Denda/hari
[A01] Proyektor Portabel        Rp10.000
[K01] Kit Mikrokontroler         Rp5.000
----------------------------------------
Jumlah alat: 2
========================================
Gagal meminjam: Proyektor Portabel sedang dipinjam
========================================
BUKTI PEMINJAMAN PJ002
========================================
Peminjam : Bima Saputra (2409106002)
Lama     : 2 hari
----------------------------------------
Alat                          Denda/hari
[A02] Laptop Cadangan           Rp10.000
----------------------------------------
Jumlah alat: 1
========================================

=== SETELAH PEMINJAMAN ===
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - dipinjam | 200 watt
[A02] Laptop Cadangan - dipinjam | 65 watt
[K01] Kit Mikrokontroler - dipinjam | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen
Alat tersedia: 1 dari 4

=== PENGEMBALIAN ===
PJ001 kembali terlambat 2 hari, denda Rp30.000
PJ002 kembali tepat waktu, denda Rp0
Gagal mengembalikan: Peminjaman PJ001 sudah selesai

=== STATUS AKHIR ===
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - tersedia | 200 watt
[A02] Laptop Cadangan - tersedia | 65 watt
[K01] Kit Mikrokontroler - tersedia | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen
Alat tersedia: 4 dari 4
Peminjaman tercatat: 2
```

</details>

> [!TIP]
> **Coba sendiri:** di `main`, ubah `prosesPengembalian(pinjamBima, 0);` menjadi `prosesPengembalian(pinjamBima, 3);`. Tebak dulu: berapa denda Bima?

<details>
<summary>Lihat jawaban</summary>

Bima hanya meminjam satu alat elektronik (Laptop Cadangan, denda Rp10.000 per hari). Terlambat 3 hari berarti 3 × 10.000, sehingga tercetak `PJ002 kembali terlambat 3 hari, denda Rp30.000`.

</details>

## 2. Soal C2: Toko Buku Daring

File: [`solusi/SoalC2TokoBuku.java`](solusi/SoalC2TokoBuku.java)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Pelanggan` | Menyimpan data pemesan secara *read-only* | Getter tanpa setter, `toString()` |
| `Produk` | Data produk; harga tervalidasi; stok hanya berkurang lewat method | Setter dengan validasi, method penjaga aturan (P04) |
| `Buku`, `AlatTulis` | Menambah field dan meng-*override* `toString()` | `extends`, `super(...)` (P07) |
| `ItemPesanan` | Satu baris pesanan: produk, jumlah, subtotal, berat | Asosiasi ke `Produk` (P05) |
| `Pesanan` | Nomor otomatis, daftar item, subtotal, ongkir, total, invoice | Komposisi (P05), field `static` (P03) |
| `TokoBuku` | Katalog produk, pencarian, catatan pesanan, total penjualan | Agregasi, `null` (P05) |

### Harga dijaga oleh setter

Konstruktor `Produk` mengisi harga **lewat setter**:

```java
    public Produk(String kode, String nama, int harga, int stok, int beratGram) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        if (beratGram <= 0) {
            throw new IllegalArgumentException("Berat harus lebih dari 0 gram");
        }
        this.kode = kode;
        this.nama = nama;
        this.stok = stok;
        this.beratGram = beratGram;
        setHarga(harga); // [1] lewat setter, jadi ikut divalidasi
    }
```

Setter harganya:

```java
    public void setHarga(int nilai) {
        if (nilai <= 0) {
            // [2] ditolak SEBELUM field diubah, jadi harga lama tetap aman
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = nilai;
    }
```

Kelas anak `Buku`:

```java
/** Produk berupa buku. Tambahan: penulis. */
class Buku extends Produk {
    private String penulis;

    public Buku(String kode, String judul, int harga, int stok, int beratGram,
            String penulis) {
        super(kode, judul, harga, stok, beratGram); // [3]
        this.penulis = penulis;
    }

    public String getPenulis() {
        return penulis;
    }

    @Override
    public String toString() {
        // [4] override: pakai teks dari induk, lalu tambahkan nama penulis
        return super.toString() + " | penulis " + penulis;
    }
}
```

Penjelasan:

- **[1]** Konstruktor memanggil `setHarga(harga)` alih-alih menulis `this.harga = harga`. Aturan "harga harus lebih dari 0" hanya ditulis sekali, tetapi berlaku saat produk dibuat maupun saat harganya diubah.
- **[2]** Setter memeriksa dulu, baru menyimpan. Itu sebabnya harga Bumi Manusia tetap Rp120.000 setelah percobaan `setHarga(-5000)`.
- **[3]** Judul buku dikirim ke induk sebagai `nama`. Semua field umum disiapkan oleh konstruktor `Produk`.
- **[4]** Pola *override* yang sama dengan Soal C1. Kelas `AlatTulis` menambahkan ` | warna ...` dengan cara yang sama.

### Kelas `Pesanan`: komposisi dan perhitungan

```java
    public void tambahItem(Produk produk, int jumlah) {
        ItemPesanan item = new ItemPesanan(produk, jumlah); // [5] item dibuat OLEH pesanan
        produk.kurangiStok(jumlah); // [6] gagal (exception) jika stok kurang
        daftarItem.add(item); // [7] hanya disimpan jika semua lolos
    }

    public int hitungSubtotal() {
        int subtotal = 0;
        for (ItemPesanan item : daftarItem) {
            subtotal += item.hitungSubtotal();
        }
        return subtotal;
    }

    /** Total berat dalam kg, DIBULATKAN KE ATAS (1080 gram -> 2 kg). */
    public int hitungBeratKg() {
        int beratGram = 0;
        for (ItemPesanan item : daftarItem) {
            beratGram += item.hitungBerat();
        }
        return (beratGram + 999) / 1000; // [8] pembulatan ke atas tanpa double
    }

    public int hitungOngkir() {
        if (hitungSubtotal() >= BATAS_GRATIS_ONGKIR) {
            return 0;
        }
        return hitungBeratKg() * ONGKIR_PER_KG;
    }
```

Penjelasan:

- **[5]** Objek `ItemPesanan` dibuat **di dalam** pesanan dengan `new`, sehingga hubungannya komposisi. Konstruktor `ItemPesanan` sekaligus memeriksa jumlah, jadi jumlah 0 sudah ditolak sebelum stok tersentuh.
- **[6]** Stok hanya berkurang lewat `kurangiStok()`, yang menolak permintaan melebihi stok.
- **[7]** Item baru disimpan setelah kedua pemeriksaan lolos. Jika salah satu gagal, *exception* menghentikan method sebelum baris ini.
- **[8]** Pembagian dua `int` di Java membuang angka di belakang koma. Dengan menambahkan 999 lebih dulu, hasilnya menjadi pembulatan ke atas: 720 menjadi 1, 1080 menjadi 2, dan 1000 tetap 1.

Cara menjalankan:

```bash
cd Pertemuan-08-UTS/java/solusi
java SoalC2TokoBuku.java
```

<details>
<summary>Lihat output lengkap Soal C2</summary>

**Output:**

```text
=== KATALOG PustakaKita ===
[B01] Laskar Pelangi - Rp95.000 | stok 5 | penulis Andrea Hirata
[B02] Bumi Manusia - Rp120.000 | stok 3 | penulis Pramoedya Ananta Toer
[B03] Negeri 5 Menara - Rp89.000 | stok 2 | penulis Ahmad Fuadi
[T01] Pulpen Gel - Rp8.000 | stok 50 | warna hitam
[T02] Map Plastik - Rp5.000 | stok 40 | warna biru

=== DATA TIDAK VALID DITOLAK ===
Gagal menambah produk: Harga harus lebih dari 0
Gagal mengubah harga: Harga harus lebih dari 0
Harga Bumi Manusia tetap Rp120.000
Cari B99: produk tidak ditemukan

=== PESANAN ===
========================================
INVOICE INV001
========================================
Pelanggan : Siti Aminah (siti@contoh.id)
----------------------------------------
2 x Laskar Pelangi             Rp190.000
2 x Pulpen Gel                  Rp16.000
----------------------------------------
Subtotal                       Rp206.000
Ongkir (1 kg)                     GRATIS
TOTAL                          Rp206.000
========================================
Gagal menambah item: Stok Negeri 5 Menara tidak cukup (sisa 2)
Gagal menambah item: Jumlah harus lebih dari 0
========================================
INVOICE INV002
========================================
Pelanggan : Budi Santoso (budi@contoh.id)
----------------------------------------
2 x Negeri 5 Menara            Rp178.000
3 x Map Plastik                 Rp15.000
----------------------------------------
Subtotal                       Rp193.000
Ongkir (2 kg)                   Rp20.000
TOTAL                          Rp213.000
========================================

=== RINGKASAN ===
=== KATALOG PustakaKita ===
[B01] Laskar Pelangi - Rp95.000 | stok 3 | penulis Andrea Hirata
[B02] Bumi Manusia - Rp120.000 | stok 3 | penulis Pramoedya Ananta Toer
[B03] Negeri 5 Menara - Rp89.000 | stok 0 | penulis Ahmad Fuadi
[T01] Pulpen Gel - Rp8.000 | stok 48 | warna hitam
[T02] Map Plastik - Rp5.000 | stok 37 | warna biru
Jumlah pesanan : 2
Total penjualan: Rp419.000
```

</details>

> [!TIP]
> **Coba sendiri:** di kelas `Pesanan`, ubah konstanta `BATAS_GRATIS_ONGKIR` menjadi `150000`. Tebak dulu: apa yang berubah pada invoice Budi dan pada total penjualan?

<details>
<summary>Lihat jawaban</summary>

Subtotal Budi Rp193.000 kini sudah mencapai batas, sehingga ongkirnya menjadi `GRATIS` dan totalnya Rp193.000. Total penjualan menjadi Rp206.000 + Rp193.000 = **Rp399.000**. Cukup satu angka yang diubah, karena aturan itu disimpan sebagai konstanta.

</details>

## 3. Membandingkan Output-mu dengan Solusi

Targetnya, output programmu **sama persis** dengan contoh output di soal. Simpan output kedua program ke file teks, lalu biarkan komputer yang membandingkan:

```bash
java Jawabanku.java > hasil_saya.txt
java SoalC1PeminjamanAlat.java > hasil_solusi.txt
```

Lalu bandingkan:

- **Command Prompt (Windows):** `fc hasil_saya.txt hasil_solusi.txt`
- **PowerShell (Windows):** `fc.exe hasil_saya.txt hasil_solusi.txt` (di PowerShell, `fc` tanpa `.exe` berarti perintah lain)
- **macOS/Linux:** `diff hasil_saya.txt hasil_solusi.txt`. Jika tidak ada yang tercetak, berarti kedua file sama.
- **VS Code:** klik kanan file pertama, pilih *Select for Compare*, lalu klik kanan file kedua dan pilih *Compare with Selected*.

> [!TIP]
> Perbedaan yang paling sering ditemukan adalah spasi di akhir baris, huruf besar/kecil pada pesan error, dan lebar kolom pada `String.format`. Salin teks pesan langsung dari soal agar tidak salah ketik.

## 4. Kesalahan Umum dan Cara Membaca Pesan Error

Sebagian besar kesalahan pewarisan di Java tertangkap saat **kompilasi**, sebelum program sempat berjalan. Pesannya diawali nama file dan nomor baris, dan tanda `^` menunjuk posisi masalahnya.

### Kesalahan 1: Lupa memanggil `super(...)`

```java
    public AlatElektronik(String kode, String nama, int dayaWatt) {
        this.dayaWatt = dayaWatt; // lupa super(kode, nama);
    }
```

Pesan error-nya:

```text
E1.java:21: error: constructor Alat in class Alat cannot be applied to given types;
    public AlatElektronik(String kode, String nama, int dayaWatt) {
                                                                  ^
  required: String,String
  found:    no arguments
  reason: actual and formal argument lists differ in length
1 error
```

**Artinya:** jika kita tidak menulis `super(...)`, Java diam-diam memanggil `super()` **tanpa argumen**. Padahal `Alat` hanya punya konstruktor dengan dua parameter (*required: String,String*). **Perbaikan:** tulis `super(kode, nama);` di baris pertama konstruktor anak.

### Kesalahan 2: Mengakses field `private` milik induk

```java
    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " | " + dayaWatt + " watt";
    }
```

Pesan error-nya:

```text
E2.java:27: error: kode has private access in Alat
        return "[" + kode + "] " + nama + " | " + dayaWatt + " watt";
                     ^
E2.java:27: error: nama has private access in Alat
        return "[" + kode + "] " + nama + " | " + dayaWatt + " watt";
                                   ^
2 errors
```

**Artinya:** field `private` hanya bisa diakses dari dalam kelas `Alat` sendiri, termasuk tidak bisa diakses oleh kelas anaknya. **Perbaikan:** pakai `super.toString()` atau getter (`getKode()`). Cara lain adalah membuat field-nya `protected`, tetapi ingat bahwa `protected` di Java juga terbuka untuk kelas lain dalam paket yang sama.

### Kesalahan 3: Salah ketik nama method yang di-*override*

```java
    @Override
    public String tostring() {
        return "Buku: " + judul;
    }
```

Pesan error-nya:

```text
E3.java:14: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
```

**Artinya:** `tostring` (huruf s kecil) tidak sama dengan `toString`, jadi method ini bukan *override*, melainkan method baru. Tanpa `@Override`, kesalahan ini lolos kompilasi dan objek tetap tercetak seperti `Buku@1b6d3586`. **Perbaikan:** perbaiki namanya menjadi `toString`. Inilah alasan `@Override` selalu ditulis.

### Kesalahan 4: Memperkecil hak akses saat *override*

```java
    @Override
    String toString() {
        return "Buku: " + judul;
    }
```

Pesan error-nya:

```text
E4.java:15: error: toString() in Buku cannot override toString() in Object
    String toString() {
           ^
  attempting to assign weaker access privileges; was public
1 error
```

**Artinya:** `toString()` milik `Object` bersifat `public`, sedangkan versi kita tanpa *modifier* (lebih sempit). Aturan *override* di Java melarang memperkecil hak akses. **Perbaikan:** tulis `public String toString()`.

### Kesalahan 5: `super(...)` bukan di baris pertama

```java
    public AlatElektronik(String kode, String nama, int dayaWatt) {
        this.dayaWatt = dayaWatt;
        super(kode, nama);
    }
```

Pesan error-nya (dicoba dengan JDK 21 dan `javac --release 17`):

```text
E7.java:22: error: call to super must be first statement in constructor
        super(kode, nama);
             ^
1 error
```

**Artinya:** di Java 17, konstruktor induk harus dipanggil paling awal. **Perbaikan:** pindahkan `super(kode, nama);` ke baris pertama.

> [!NOTE]
> Java 25 melonggarkan aturan ini: beberapa pernyataan tertentu boleh ditulis sebelum `super(...)`, sehingga JDK yang lebih baru bisa menampilkan pesan yang berbeda atau bahkan menerima kode di atas. Namun, mata kuliah ini berpatokan pada Java 17, dan kebiasaan menulis `super(...)` di baris pertama tetap aman di semua versi.

### Kesalahan 6: Memakai hasil pencarian yang ternyata `null`

```java
        Alat alat = lab.cariAlat("A09");
        alat.pinjamkan();
```

Pesan error-nya (saat program berjalan):

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Alat.pinjamkan()" because "<local2>" is null
	at E6.main(E6.java:8)
```

**Artinya:** alat berkode A09 tidak ada, sehingga `cariAlat` mengembalikan `null`. Memanggil method pada `null` menghasilkan `NullPointerException`. Nama variabel kadang tertulis sebagai `<local2>` alih-alih `alat`, tergantung cara program dikompilasi. **Perbaikan:** periksa dulu dengan `if (alat == null)` sebelum memakai hasil pencarian.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK. Fokuslah pada nomor baris dan kata-kata kuncinya, seperti `cannot be applied`, `private access`, atau `does not override`.

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Python: [🐍 Solusi Python](../python/README.md). Kelas, urutan langkah, dan output-nya sama persis.
- Baca pembahasan rancangannya: [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).
- Kembali ke [Informasi UTS](../README.md) untuk mengecek checklist kesiapanmu.

---

[⬅️ Informasi UTS](../README.md) · [🐍 Solusi Python](../python/README.md) · [Pembahasan ➡️](../pembahasan.md)
