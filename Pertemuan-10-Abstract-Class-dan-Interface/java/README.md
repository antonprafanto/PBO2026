# ☕ Praktik Java — Pertemuan 10: Abstract Class dan Interface

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 10](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Masalah: Kelas Induk yang Terlalu Umum](#1-masalah-kelas-induk-yang-terlalu-umum)
2. [`abstract class` dan Method `abstract`](#2-abstract-class-dan-method-abstract)
3. [Konstruktor, Field, dan Method Konkret di Kelas Abstrak](#3-konstruktor-field-dan-method-konkret-di-kelas-abstrak)
4. [Template Method dan `final`](#4-template-method-dan-final)
5. [`interface` dan `implements`](#5-interface-dan-implements)
6. [Satu Kelas, Banyak Interface](#6-satu-kelas-banyak-interface)
7. [`default` Method dan Konstanta di Interface](#7-default-method-dan-konstanta-di-interface)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan Error](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh program satu file
├── studi-kasus/     <- KedaiKita versi Pertemuan 10 (14 file .java)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file, jadi bisa langsung dijalankan (Java 11 ke atas):

```bash
cd Pertemuan-10-Abstract-Class-dan-Interface/java/contoh
java Contoh01MasalahIndukUmum.java
```

> [!TIP]
> Jika memakai VS Code, buka folder `java/` **milik pertemuan ini** (File → Open Folder), bukan seluruh repositori, agar kelas bernama sama dari pertemuan lain tidak bentrok. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

Contoh 08 (*default method*) khusus Java. Tidak ada contoh 07 di folder ini, karena contoh 07 khusus Python (`typing.Protocol`). Penjelasannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 1. Masalah: Kelas Induk yang Terlalu Umum

File: [`contoh/Contoh01MasalahIndukUmum.java`](contoh/Contoh01MasalahIndukUmum.java)

Sebelum belajar cara baru, kita rasakan dulu masalahnya. Kelas induk `BangunDatar` di bawah ini masih kelas biasa, sama seperti `Pembayaran` di Pertemuan 09.

```java
/** Kelas induk biasa (BELUM abstrak) untuk semua bangun datar. */
class BangunDatar {
    private String nama;

    public BangunDatar(String nama) {
        this.nama = nama;
    }

    public int luas() {
        return 0; // [1] luas "bangun datar umum"? Tidak ada jawaban yang masuk akal
    }

    public String info() {
        return nama + ": luas " + luas() + " cm2";
    }
}
```

Kelas `Persegi` meng-*override* `luas()` dengan benar (`sisi * sisi`). Berikut kelas `Segitiga`:

```java
/** Segitiga dengan alas dan tinggi. */
class Segitiga extends BangunDatar {
    private int alas;
    private int tinggi;

    public Segitiga(int alas, int tinggi) {
        super("Segitiga");
        this.alas = alas;
        this.tinggi = tinggi;
    }

    // [2] Programmer LUPA menulis method luas() di sini!
}
```

Program utamanya:

```java
        System.out.println("=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===");
        BangunDatar misterius = new BangunDatar("Bangun datar misterius"); // [3] tidak dilarang
        System.out.println(misterius.info());

        System.out.println();
        System.out.println("=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===");
        List<BangunDatar> daftar = List.of(new Persegi(5), new Segitiga(6, 4));
        for (BangunDatar bangun : daftar) {
            System.out.println(bangun.info()); // [4] Segitiga memakai luas() milik induk
        }
        System.out.println("Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!");
```

**Output:**

```text
=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===
Bangun datar misterius: luas 0 cm2

=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===
Persegi: luas 25 cm2
Segitiga: luas 0 cm2
Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!
```

Penjelasan:

- **[1]** Kelas induk terpaksa memberi isi "pura-pura" untuk `luas()`. Angka 0 dipilih asal-asalan, karena luas "bangun datar umum" memang tidak ada.
- **[2]** Kelas `Segitiga` tidak menulis `luas()`. Mungkin programmernya lupa, mungkin terburu-buru.
- **[3]** Java mengizinkan `new BangunDatar(...)`. Hasilnya objek yang tidak bermakna.
- **[4]** `Segitiga` diam-diam mewarisi `luas()` milik induk, sehingga luasnya tercetak 0. Kompilasi tetap berhasil.

> [!WARNING]
> `@Override` tidak bisa menolong di sini. Anotasi itu hanya memeriksa method yang **ditulis** (misalnya salah ketik nama, Pertemuan 07). Method yang **tidak ditulis sama sekali** tidak diperiksa siapa pun. Di KedaiKita Pertemuan 09, kesalahan serupa pada `proses()` bisa membuat pesanan tercatat LUNAS tanpa uang masuk.

## 2. `abstract class` dan Method `abstract`

File: [`contoh/Contoh02KelasAbstrak.java`](contoh/Contoh02KelasAbstrak.java)

Java punya kata kunci khusus: `abstract`. Kata ini dipakai di dua tempat: di depan `class` dan di depan method.

```java
/** Kelas abstrak: konsep umum semua bangun datar. */
abstract class Bentuk { // [1] kata kunci abstract -> kelas abstrak

    /** Menghitung luas (cm2). */
    public abstract int luas(); // [2] method abstrak: tanpa isi, diakhiri titik koma

    /** Menghitung keliling (cm). */
    public abstract int keliling();
}
```

Kelas konkret pertama, `PersegiPanjang`, menyimpan `panjang` dan `lebar`, lalu mengisi kedua method abstrak. Salah satunya:

```java
    @Override
    public int luas() { // [3] mengisi (meng-override) method abstrak
        return panjang * lebar;
    }
```

Method `keliling()`-nya mengembalikan `2 * (panjang + lebar)`. Kelas `SegitigaSiku` ditulis dengan pola yang sama: luasnya `alas * tinggi / 2`, kelilingnya `alas + tinggi + miring`. Program utamanya:

```java
        // Bentuk bentukUmum = new Bentuk(); // [4] hapus // di awal baris ini -> error kompilasi

        PersegiPanjang kartu = new PersegiPanjang(8, 5);
        SegitigaSiku penggaris = new SegitigaSiku(6, 8, 10);
        List<Bentuk> daftar = List.of(kartu, penggaris); // [5] list bertipe kelas abstrak

        System.out.println("=== DAFTAR BENTUK ===");
        for (Bentuk bentuk : daftar) {
            String nama = bentuk.getClass().getSimpleName();
            System.out.println(nama + ": luas " + bentuk.luas() + " cm2, keliling "
                    + bentuk.keliling() + " cm");
        }

        System.out.println();
        System.out.println("=== CEK JENIS ===");
        System.out.println("kartu dibuat dari kelas: " + kartu.getClass().getSimpleName());
        boolean termasukBentuk = kartu instanceof Bentuk; // [6]
        System.out.println("Apakah kartu termasuk Bentuk? " + yaTidak(termasukBentuk));
```

**Output:**

```text
=== DAFTAR BENTUK ===
PersegiPanjang: luas 40 cm2, keliling 26 cm
SegitigaSiku: luas 24 cm2, keliling 24 cm

=== CEK JENIS ===
kartu dibuat dari kelas: PersegiPanjang
Apakah kartu termasuk Bentuk? ya
```

Penjelasan:

- **[1]** `abstract class Bentuk` menandai `Bentuk` sebagai kelas abstrak.
- **[2]** Method abstrak ditulis dengan kata `abstract`, **tanpa** kurung kurawal, dan diakhiri titik koma. Ia hanya "kepala" method.
- **[3]** `PersegiPanjang` meng-*override* **kedua** method abstrak, sehingga ia menjadi kelas konkret. Tetap tulis `@Override`.
- **[4]** Baris ini sengaja dijadikan komentar. Kalau `//`-nya dihapus, program gagal dikompilasi (lihat di bawah).
- **[5]** `List<Bentuk>` adalah list bertipe kelas abstrak. Isinya objek-objek kelas konkret. Inilah polimorfisme dari Pertemuan 09.
- **[6]** `kartu instanceof Bentuk` bernilai benar: objek kelas anak tetap "adalah" kelas induknya, walaupun induknya abstrak.

### Mencoba membuat objek kelas abstrak

Hapus `//` di awal baris **[4]**, lalu jalankan lagi:

```text
Contoh02KelasAbstrak.java:22: error: Bentuk is abstract; cannot be instantiated
        Bentuk bentukUmum = new Bentuk(); // [4] hapus // di awal baris ini -> error kompilasi
                            ^
1 error
error: compilation failed
```

**Artinya:** "`Bentuk` adalah kelas abstrak, jadi tidak bisa dibuat objeknya (*instantiated*)." Tanda `^` menunjuk ke `new Bentuk()`. Perhatikan bahwa **tidak ada satu baris output pun** yang tercetak, karena Java menolak program ini sebelum dijalankan. Bandingkan dengan Python, yang baru protes ketika baris itu dijalankan.

> [!NOTE]
> Baris terakhir `error: compilation failed` muncul karena kita memakai cara satu file (`java NamaFile.java`). Jika memakai `javac`, yang muncul hanya pesan error dan `1 error`.

> [!TIP]
> **Coba sendiri:** kembalikan `//` pada baris **[4]**. Lalu hapus method `keliling()` beserta `@Override`-nya dari kelas `SegitigaSiku`. Apa kata *compiler*?

<details>
<summary>Lihat jawaban</summary>

```text
Contoh02KelasAbstrak.java:75: error: SegitigaSiku is not abstract and does not override abstract method keliling() in Bentuk
class SegitigaSiku extends Bentuk {
^
1 error
error: compilation failed
```

Artinya: "`SegitigaSiku` bukan kelas abstrak, tetapi belum meng-*override* method abstrak `keliling()` milik `Bentuk`." Bandingkan dengan contoh 01: dulu lupa menulis method tidak diprotes, sekarang program bahkan tidak bisa dikompilasi. (Nomor baris di pesanmu bisa berbeda.)

</details>

## 3. Konstruktor, Field, dan Method Konkret di Kelas Abstrak

File: [`contoh/Contoh03IsiKelasAbstrak.java`](contoh/Contoh03IsiKelasAbstrak.java)

Kelas abstrak bukan kelas kosong. Ia boleh punya konstruktor, *field*, dan method yang sudah berisi.

```java
/** Kelas abstrak: data dan perilaku bersama semua kendaraan. */
abstract class Kendaraan {
    private String plat; // [2] field bersama
    private int bensin;

    protected Kendaraan(String plat, int bensinLiter) { // [1] konstruktor
        System.out.println("  (konstruktor Kendaraan dijalankan untuk " + plat + ")");
        this.plat = plat;
        this.bensin = bensinLiter;
    }

    public String getPlat() {
        return plat;
    }

    public void isiBensin(int liter) { // [3] method konkret: langsung diwarisi
        bensin += liter;
        System.out.println(plat + " mengisi bensin " + liter + " liter");
    }

    public int jarakTempuh() { // [4] method konkret yang memakai method abstrak
        return bensin * kmPerLiter();
    }

    public String info() {
        return getClass().getSimpleName() + " " + plat + ": bensin " + bensin
                + " liter, bisa menempuh " + jarakTempuh() + " km";
    }

    /** Jarak (km) yang bisa ditempuh dengan 1 liter bensin. */
    public abstract int kmPerLiter(); // [5] berbeda untuk setiap jenis kendaraan
}

/** Motor: tetap wajib menulis konstruktor yang meneruskan data ke super(...). */
class Motor extends Kendaraan {

    public Motor(String plat, int bensinLiter) {
        super(plat, bensinLiter);
    }

    @Override
    public int kmPerLiter() {
        return 40;
    }
}
```

Kelas `Mobil` punya *field* tambahan `jumlahKursi`. Konstruktornya:

```java
    public Mobil(String plat, int bensinLiter, int jumlahKursi) {
        super(plat, bensinLiter); // [6] memanggil konstruktor kelas abstrak
        this.jumlahKursi = jumlahKursi;
    }
```

`Mobil` juga meng-*override* `info()` untuk menambahkan jumlah kursi. Program utamanya membuat `new Motor("KT 1234 AB", 3)` dan `new Mobil("KT 5678 CD", 20, 7)`, menampilkan info keduanya, mengisi bensin, lalu menampilkan info lagi.

**Output:**

```text
=== MEMBUAT KENDARAAN ===
  (konstruktor Kendaraan dijalankan untuk KT 1234 AB)
  (konstruktor Kendaraan dijalankan untuk KT 5678 CD)

=== INFO AWAL ===
Motor KT 1234 AB: bensin 3 liter, bisa menempuh 120 km
Mobil KT 5678 CD: bensin 20 liter, bisa menempuh 240 km, 7 kursi

=== ISI BENSIN (method konkret milik Kendaraan) ===
KT 1234 AB mengisi bensin 2 liter
KT 5678 CD mengisi bensin 10 liter
Motor KT 1234 AB: bensin 5 liter, bisa menempuh 200 km
Mobil KT 5678 CD: bensin 30 liter, bisa menempuh 360 km, 7 kursi
```

Penjelasan:

- **[1]** Kelas abstrak boleh punya konstruktor. Baris `println` di dalamnya membuktikan bahwa konstruktor ini **benar-benar berjalan** dua kali, yaitu saat objek `Motor` dan objek `Mobil` dibuat. Konstruktornya diberi akses `protected`, karena yang memanggilnya hanya kelas anak (lewat `super(...)`). Akses `public` pun tetap sah.
- **[2]** *Field* `plat` dan `bensin` dimiliki semua kendaraan, jadi cukup ditulis sekali. Keduanya `private`, sehingga kelas anak memakainya lewat method warisan.
- **[3]** `isiBensin()` adalah method konkret. `Motor` dan `Mobil` langsung memakainya tanpa menulis ulang.
- **[4]** Method konkret boleh memanggil method abstrak. Saat `jarakTempuh()` dijalankan oleh objek `Motor`, `kmPerLiter()` yang terpanggil adalah versi milik `Motor` (40).
- **[5]** Hanya bagian yang benar-benar berbeda yang dijadikan abstrak.
- **[6]** `super(plat, bensinLiter)` memanggil konstruktor kelas abstrak dan wajib ditulis di baris pertama konstruktor, sama seperti di Pertemuan 07.

> [!IMPORTANT]
> Perhatikan kelas `Motor`: walaupun tidak punya *field* tambahan, ia **tetap wajib** menulis konstruktor yang meneruskan data ke `super(...)`. Konstruktor tidak diwariskan di Java, dan `Kendaraan` tidak punya konstruktor tanpa parameter. Di Python, kelas `Motor` yang sama tidak perlu menulis `__init__` sama sekali.

## 4. Template Method dan `final`

File: [`contoh/Contoh04TemplateMethod.java`](contoh/Contoh04TemplateMethod.java)

Sekarang kita pakai method konkret yang memanggil method abstrak untuk membuat **kerangka tetap**.

```java
/** Kelas abstrak untuk semua jenis laporan. */
abstract class Laporan {
    private static final int LEBAR = 40;

    /** Template method. final: kelas anak tidak boleh mengubah kerangkanya. */
    public final void tampilkan() { // [1] urutan langkahnya selalu sama
        System.out.println("=".repeat(LEBAR));
        System.out.println(judul()); // [2] langkah yang diisi kelas anak
        System.out.println("-".repeat(LEBAR));
        for (String baris : isi()) { // [2]
            System.out.println(baris);
        }
        System.out.println("-".repeat(LEBAR));
        System.out.println(penutup()); // [3] hook: sudah punya isi, boleh di-override
        System.out.println("=".repeat(LEBAR));
    }

    /** Judul laporan. */
    public abstract String judul();

    /** Baris-baris isi laporan. */
    public abstract List<String> isi();

    public String penutup() {
        return "Dicetak oleh Sistem Informasi Akademik";
    }
}
```

Dua kelas anaknya, `LaporanKehadiran` dan `LaporanPerpustakaan`, sama-sama mengisi `judul()` dan `isi()`. Hanya `LaporanPerpustakaan` yang juga mengganti penutupnya:

```java
    @Override
    public String penutup() { // [4] meng-override hook
        return "Disahkan oleh Kepala Perpustakaan";
    }
```

Program utamanya menyimpan kedua laporan dalam `List<Laporan>`, lalu:

```java
        for (Laporan laporan : daftar) {
            System.out.println();
            laporan.tampilkan(); // [5] satu panggilan, kerangka sama, isi berbeda
        }
```

**Output:**

```text
=== MENCETAK 2 LAPORAN ===

========================================
LAPORAN KEHADIRAN PBO
----------------------------------------
Mahasiswa  : Ayu Lestari
Hadir      : 14 dari 16 pertemuan
Persentase : 87%
----------------------------------------
Dicetak oleh Sistem Informasi Akademik
========================================

========================================
LAPORAN PERPUSTAKAAN BULAN OKTOBER
----------------------------------------
Buku dipinjam      : 120
Sudah dikembalikan : 112
Belum dikembalikan : 8
----------------------------------------
Disahkan oleh Kepala Perpustakaan
========================================
```

Penjelasan:

- **[1]** `tampilkan()` adalah **template method**: method konkret yang menetapkan urutan langkah. Kata `final` di depannya berarti method ini **tidak boleh** di-*override* kelas anak. Kerangka laporan pun terjamin seragam.
- **[2]** Dua langkah yang berbeda untuk setiap laporan diserahkan ke method abstrak `judul()` dan `isi()`. Tipe `List<String>` dipakai agar isi laporan bisa berapa baris pun.
- **[3]** `penutup()` adalah *hook*: sudah punya isi bawaan, tetapi boleh diganti.
- **[4]** `LaporanPerpustakaan` meng-*override* *hook* itu, sedangkan `LaporanKehadiran` memakai versi bawaan. Bandingkan baris penutup kedua laporan di output.
- **[5]** Program utama cukup memanggil `tampilkan()`.

> [!NOTE]
> Method abstrak tidak boleh `final`, karena method abstrak justru **harus** di-*override*. Sebaliknya, template method sering dibuat `final` agar urutannya tidak diubah. Python tidak punya cara langsung untuk melarang *override*, jadi versi Python contoh ini hanya mengandalkan kesepakatan.

## 5. `interface` dan `implements`

File: [`contoh/Contoh05Interface.java`](contoh/Contoh05Interface.java)

Java punya kata kunci khusus untuk kontrak kemampuan: `interface`. Kelas yang memenuhinya menulis `implements`.

```java
/** Kontrak: benda ini bisa dinyalakan dan dimatikan. */
interface BisaDinyalakan { // [1] interface: daftar kemampuan tanpa isi
    void nyalakan();

    void matikan();

    boolean sedangMenyala();
}

/** Lampu di sebuah ruangan. */
class Lampu implements BisaDinyalakan { // [2] memenuhi kontrak dengan implements
```

`Lampu` lalu mengisi ketiga method itu satu per satu. Misalnya `nyalakan()`:

```java
    @Override
    public void nyalakan() {
        menyala = true;
        System.out.println("Lampu " + ruangan + " menyala");
    }
```

`KomporGas` dan `Televisi` meng-*implements* interface yang sama dengan isi masing-masing. Ketiga kelas itu tidak punya kelas induk bersama selain kontrak `BisaDinyalakan`. Method yang memakai kontraknya:

```java
    /** Mematikan semua benda yang masih menyala, apa pun jenisnya. */
    public static void matikanSemua(List<BisaDinyalakan> daftar) { // [3] tipe: interface
        System.out.println("Memeriksa " + daftar.size() + " benda...");
        for (BisaDinyalakan benda : daftar) {
            if (benda.sedangMenyala()) { // [4] yang dipakai hanya method dari kontrak
                benda.matikan();
            }
        }
        System.out.println("Semua sudah padam. Aman!");
    }
```

Program utamanya menyalakan lampu, kompor, dan TV, mematikan TV, lalu memanggil `matikanSemua(List.of(lampu, kompor, tv))`.

**Output:**

```text
=== PAGI HARI ===
Lampu teras menyala
Kompor gas: klik... api biru menyala
TV menyala di saluran 5
TV dimatikan

=== SEBELUM BERANGKAT KULIAH ===
Memeriksa 3 benda...
Lampu teras padam
Kompor gas: api dimatikan, katup gas ditutup
Semua sudah padam. Aman!
```

Penjelasan:

- **[1]** Interface berisi daftar method **tanpa isi**. Kita tidak perlu menulis `public abstract`, karena method di dalam interface otomatis `public` dan `abstract`.
- **[2]** `implements BisaDinyalakan` adalah janji: "kelas `Lampu` menyediakan semua method di kontrak itu". Setiap method yang mengisinya wajib `public` (lihat [Kesalahan 4](#kesalahan-4-lupa-public-saat-mengisi-method-interface)) dan sebaiknya diberi `@Override`.
- **[3]** Parameter bertipe interface: `List<BisaDinyalakan>` berarti "daftar apa saja yang bisa dinyalakan".
- **[4]** Di dalam method, kita hanya memanggil method yang dijanjikan kontrak. TV yang sudah dimatikan dilewati.

> [!IMPORTANT]
> Interface tidak bisa dibuat objeknya (`new BisaDinyalakan()` ditolak), tetapi **boleh** dipakai sebagai tipe variabel, parameter, dan isi list: `BisaDinyalakan benda = new Lampu("teras");`.

> [!TIP]
> **Coba sendiri:** tambahkan kelas `KipasAngin implements BisaDinyalakan` yang hanya menulis `nyalakan()` dan `matikan()`. *Compiler* akan menolak dengan pesan `KipasAngin is not abstract and does not override abstract method sedangMenyala() in BisaDinyalakan`.

## 6. Satu Kelas, Banyak Interface

File: [`contoh/Contoh06BanyakInterface.java`](contoh/Contoh06BanyakInterface.java)

Di Pertemuan 07 kamu belajar bahwa sebuah kelas Java hanya boleh `extends` **satu** kelas. Interface adalah jalan keluarnya: sebuah kelas boleh `implements` **banyak** interface sekaligus.

Kelas abstrak `Hewan` menyimpan `nama` dan punya method abstrak `bersuara()`. Dua interface kemampuannya, lalu kelas `Bebek`:

```java
/** Kontrak kemampuan terbang. */
interface BisaTerbang {
    String terbang();
}

/** Kontrak kemampuan berenang. */
interface BisaBerenang {
    String berenang();
}

/** Bebek: hewan yang bisa terbang dan berenang. */
class Bebek extends Hewan implements BisaTerbang, BisaBerenang { // [1] satu induk + dua interface
```

Di dalam badannya, `Bebek` meng-*override* `bersuara()` dari `Hewan`, serta `terbang()` dan `berenang()` dari kedua interface.

Kelas `Ikan extends Hewan implements BisaBerenang` hanya bisa berenang. Lalu ada kelas yang sama sekali bukan hewan:

```java
/** Pesawat: benda mati yang bisa terbang. */
class Pesawat implements BisaTerbang { // [2] bukan Hewan, tetapi BisaTerbang
```

Potongan program utamanya:

```java
        List<BisaTerbang> penerbang = List.of(bebek, pesawat); // [3] dikelompokkan per kontrak
        for (BisaTerbang benda : penerbang) {
            System.out.println(benda.terbang());
        }
```

dan bagian pemeriksaan kemampuan:

```java
        List<Object> semuaBenda = List.of(bebek, ikan, pesawat);
        for (Object benda : semuaBenda) {
            String nama = benda.getClass().getSimpleName();
            String hewan = yaTidak(benda instanceof Hewan); // [4]
            String terbang = yaTidak(benda instanceof BisaTerbang);
            String berenang = yaTidak(benda instanceof BisaBerenang);
            System.out.println(String.format("%-8s | %-5s | %-7s | %s",
                    nama, hewan, terbang, berenang));
        }
```

**Output:**

```text
=== SEMUA HEWAN BERSUARA ===
Bebek Kuning: Kwek kwek!
Ikan Patin: (diam saja)

=== YANG BISA TERBANG ===
Bebek Kuning terbang rendah di atas sawah
Pesawat Rajawali 01 terbang di atas awan

=== YANG BISA BERENANG ===
Bebek Kuning mengapung sambil mengayuh kaki
Ikan Patin berenang di Sungai Mahakam

=== CEK KEMAMPUAN ===
Kelas    | Hewan | Terbang | Berenang
Bebek    | ya    | ya      | ya
Ikan     | ya    | tidak   | ya
Pesawat  | tidak | ya      | tidak
```

Penjelasan:

- **[1]** Urutannya selalu: `extends` (paling banyak satu kelas) lebih dulu, lalu `implements` (boleh banyak interface, dipisah koma).
- **[2]** `Pesawat` tidak punya hubungan dengan `Hewan`. Ia hanya meng-*implements* `BisaTerbang`.
- **[3]** `bebek` dan `pesawat` bisa berada di `List<BisaTerbang>` yang sama, karena keduanya `BisaTerbang`.
- **[4]** `instanceof` juga bisa memeriksa interface. Pertanyaannya bukan lagi "kamu kelas apa?", tetapi "kamu **bisa** apa?". Daftarnya bertipe `List<Object>` karena isinya campuran yang tidak punya tipe bersama selain `Object`.

## 7. `default` Method dan Konstanta di Interface

File: [`contoh/Contoh08DefaultMethod.java`](contoh/Contoh08DefaultMethod.java) (contoh ini khusus Java, lihat [Jembatan](../jembatan-python-java.md))

Sejak Java 8, interface boleh punya method **berisi** yang diberi kata kunci `default`. Interface juga boleh menyimpan konstanta.

```java
/** Kontrak: sesuatu yang bisa diberi bintang oleh pengguna aplikasi. */
interface BisaDinilai {
    int BINTANG_MAKS = 5; // [1] konstanta: otomatis public static final

    String nama(); // [2] method abstrak: otomatis public abstract

    int totalBintang();

    int jumlahUlasan();

    default int rataRata() { // [3] default method: punya isi
        if (jumlahUlasan() == 0) {
            return 0;
        }
        return totalBintang() / jumlahUlasan();
    }

    default String ringkasan() { // [3]
        return nama() + ": " + rataRata() + "/" + BINTANG_MAKS + " bintang dari "
                + jumlahUlasan() + " ulasan";
    }
}
```

Kelas `WarungMakan` hanya mengisi tiga method abstrak. Kelas `DriverOjek` juga mengisi ketiganya, lalu mengganti `ringkasan()` dengan versinya sendiri:

```java
    @Override
    public String ringkasan() { // [4] default method boleh di-override
        String predikat = "perlu pembinaan";
        if (rataRata() >= 4) {
            predikat = "driver teladan";
        }
        return "Driver " + nama + ": " + rataRata() + "/" + BINTANG_MAKS + " (" + predikat + ")";
    }
```

Program utamanya menyimpan dua `WarungMakan` dan satu `DriverOjek` dalam `List<BisaDinilai>`, lalu:

```java
        for (BisaDinilai yangDinilai : daftar) {
            System.out.println(yangDinilai.ringkasan()); // [5] versi default atau versi override
        }
```

Di bagian akhir, konstantanya dibaca dengan:

```java
        System.out.println("Bintang maksimal: " + BisaDinilai.BINTANG_MAKS); // [6]
```

**Output:**

```text
=== RINGKASAN PENILAIAN ===
Warung Nasi Kuning Bu Ani: 4/5 bintang dari 10 ulasan
Driver Pak Rahman: 4/5 (driver teladan)
Warung Pecel Baru: 0/5 bintang dari 0 ulasan

=== KONSTANTA INTERFACE ===
Bintang maksimal: 5
```

Penjelasan:

- **[1]** *Field* di dalam interface otomatis `public static final`, yaitu **konstanta** milik interface. Interface tidak bisa menyimpan data objek biasa.
- **[2]** Method tanpa isi tetap otomatis `public abstract`.
- **[3]** `default` method punya isi dan boleh memanggil method abstrak (`totalBintang()`, `jumlahUlasan()`). Ini mirip template method, tetapi berada di interface.
- **[4]** `WarungMakan` tidak menulis `rataRata()` maupun `ringkasan()`, tetapi tetap memilikinya. `DriverOjek` memilih meng-*override* `ringkasan()`.
- **[5]** Setiap objek menjawab `ringkasan()` dengan versinya: dua warung memakai versi `default`, sang driver memakai versinya sendiri. Perhatikan juga penjaga `jumlahUlasan() == 0` untuk warung baru, agar tidak terjadi pembagian dengan nol.
- **[6]** Konstanta dibaca lewat nama interface: `BisaDinilai.BINTANG_MAKS`.

Mengapa Java menambahkan *default method*? Bayangkan sebuah interface sudah dipakai oleh ratusan kelas. Jika kita menambah satu method **abstrak** baru, ratusan kelas itu langsung gagal dikompilasi. Dengan method `default`, method baru bisa ditambahkan **tanpa** merusak kelas-kelas lama.

> [!NOTE]
> Sejak Java 8, interface juga boleh punya method `static`, misalnya `static int hitung(...)`. Kita akan memakainya di Pertemuan 13. Padanan *default method* di Python adalah method biasa (berisi) di dalam kelas `ABC`.

## 8. Studi Kasus KedaiKita

File: [`studi-kasus/Pembayaran.java`](studi-kasus/Pembayaran.java), [`studi-kasus/DapatDicetak.java`](studi-kasus/DapatDicetak.java), [`studi-kasus/Pesanan.java`](studi-kasus/Pesanan.java), [`studi-kasus/Kedai.java`](studi-kasus/Kedai.java), dan [`studi-kasus/Main.java`](studi-kasus/Main.java)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#11-studi-kasus-kedaikita-pembayaran-abstrak-dan-kontrak-dapatdicetak).

**Apa yang berubah dibanding Pertemuan 09?**

- `Pembayaran.java`: `public abstract class Pembayaran`. `namaMetode()` dan `proses()` menjadi method abstrak, sehingga isi lamanya (`"Pembayaran umum"` dan `"Memproses pembayaran ..."`) dihapus. Ada method konkret baru, `deskripsi(int total)`. `PembayaranTunai`, `PembayaranQRIS`, dan `PembayaranKartu` **tidak berubah**.
- `DapatDicetak.java` (**file baru**): `public interface DapatDicetak` dengan satu method, `void cetak()`.
- `Pesanan.java`: `public class Pesanan implements DapatDicetak`. Method `cetakStruk()` **berganti nama** menjadi `cetak()`. Isinya tidak berubah.
- `Kedai.java`: `public class Kedai implements DapatDicetak`. Method `tampilkanMenu()` **berganti nama** menjadi `cetak()`. Isinya tidak berubah.
- `Main.java`: ada method baru `cetakSemua()` dan bagian baru "MENGENAL METODE PEMBAYARAN". Struk kini dicetak di akhir lewat `cetakSemua()`, setelah pembayaran, sehingga statusnya sudah LUNAS.
- `Menu`, `Makanan`, `Minuman`, `Pelanggan`, `ItemPesanan`, dan `Rupiah` **tidak berubah sama sekali**.

### Kelas abstrak `Pembayaran`

```java
/** Kelas abstrak: kerangka untuk semua metode pembayaran. */
public abstract class Pembayaran {

    /** Nama metode pembayaran, misalnya "Tunai". */
    public abstract String namaMetode();

    /** Memproses pembayaran. Mengembalikan true jika berhasil. */
    public abstract boolean proses(int total);

    /** Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override). */
    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    /** Method konkret yang memanggil method abstrak. */
    public String deskripsi(int total) {
        String biaya = Rupiah.format(hitungBiayaLayanan(total));
        return namaMetode() + " (biaya layanan " + biaya + ")";
    }
}
```

- `namaMetode()` dan `proses()` kini **wajib** di-*override* setiap jenis pembayaran. Masalah "lupa menulis `proses()` lalu pesanan tercatat LUNAS" tidak mungkin terjadi lagi, karena kelas seperti itu tidak bisa dikompilasi.
- `hitungBiayaLayanan()` adalah *hook*: bawaannya 0, dan hanya `PembayaranKartu` yang meng-*override*-nya (2%).
- `deskripsi()` adalah template method kecil. Ia ditulis sekali, tetapi hasilnya berbeda untuk setiap jenis pembayaran.

### Interface `DapatDicetak`

```java
/** Kontrak: objek ini bisa dicetak ke layar. */
public interface DapatDicetak {

    /** Mencetak isi objek ke layar. */
    void cetak();
}
```

### `Kedai` dan `Pesanan` memenuhi kontrak

Perubahan di dua kelas ini sangat kecil:

```text
Pertemuan 09                               Pertemuan 10
public class Pesanan {                ->   public class Pesanan implements DapatDicetak {
    public void cetakStruk() {        ->       @Override
                                               public void cetak() {

public class Kedai {                  ->   public class Kedai implements DapatDicetak {
    public void tampilkanMenu() {     ->       @Override
                                               public void cetak() {
```

**Mengapa namanya harus diganti?** Interface `DapatDicetak` menuntut method bernama persis `cetak()`. Seandainya `Pesanan` sudah menulis `implements DapatDicetak` tetapi method-nya masih bernama `cetakStruk()`, *compiler* menolak:

```text
Pesanan.java:20: error: Pesanan is not abstract and does not override abstract method cetak() in DapatDicetak
public class Pesanan implements DapatDicetak {
       ^
1 error
```

Nama yang seragam inilah kuncinya. Karena kedai dan pesanan sama-sama punya `cetak()`, keduanya bisa dicetak oleh satu perulangan.

### `Main.java`: mencetak apa saja yang `DapatDicetak`

```java
    /** Mencetak objek apa pun, asalkan ia memenuhi kontrak DapatDicetak. */
    public static void cetakSemua(List<DapatDicetak> daftarDokumen) {
        int jumlah = daftarDokumen.size();
        for (int nomor = 1; nomor <= jumlah; nomor++) {
            DapatDicetak dokumen = daftarDokumen.get(nomor - 1);
            System.out.println("--- Dokumen " + nomor + " dari " + jumlah + " ---");
            dokumen.cetak();
            System.out.println();
        }
    }
```

Di dalam `main()`, bagian baru yang pertama memakai `deskripsi()`:

```java
        System.out.println("=== MENGENAL METODE PEMBAYARAN ===");
        List<Pembayaran> daftarMetode = List.of(new PembayaranTunai(100000),
                new PembayaranQRIS(50000), new PembayaranKartu("BNI"));
        for (Pembayaran metode : daftarMetode) {
            System.out.println(metode.deskripsi(100000));
        }
        System.out.println();
```

Bagian transaksi Budi dan Siti sama seperti Pertemuan 09, hanya saja pemanggilan `cetakStruk()` tidak ada lagi di sana. Struk dan daftar menu kini dicetak bersama di akhir:

```java
        System.out.println("=== CETAK SEMUA DOKUMEN ===");
        cetakSemua(List.of(kedai, pesananBudi, pesananSiti));
```

Cara menjalankan (kompilasi semua file, lalu jalankan kelas `Main`):

```bash
cd Pertemuan-10-Abstract-Class-dan-Interface/java/studi-kasus
javac *.java
java Main
```

**Output:**

```text
=== MENGENAL METODE PEMBAYARAN ===
Tunai (biaya layanan Rp0)
QRIS (biaya layanan Rp0)
Kartu Kredit BNI (biaya layanan Rp2.000)

=== TRANSAKSI ===
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

Pembayaran pesanan P002 (Siti Aminah)
  Metode       : QRIS
  Total bayar  : Rp31.000
  Saldo e-wallet tidak cukup (saldo Rp20.000)
  Status       : GAGAL, silakan pilih metode lain

Pembayaran pesanan P002 (Siti Aminah)
  Metode       : Kartu Kredit BNI
  Biaya layanan: Rp620
  Total bayar  : Rp31.620
  Transaksi kartu BNI disetujui sebesar Rp31.620
  Status       : LUNAS (+3 poin)

=== CETAK SEMUA DOKUMEN ===
--- Dokumen 1 dari 3 ---
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11 | pedas level 0

--- Dokumen 2 dari 3 ---
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
Status      : LUNAS
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================

--- Dokumen 3 dari 3 ---
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
Status      : LUNAS
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================

=== POIN PELANGGAN ===
Budi Santoso (081234567890) - 6 poin
Siti Aminah (082198765432) - 3 poin
```

Hal-hal yang perlu diperhatikan:

- Bagian "MENGENAL METODE PEMBAYARAN" dihasilkan oleh **satu** method `deskripsi()` milik kelas abstrak. Teksnya berbeda karena `namaMetode()` dan `hitungBiayaLayanan()` dijawab oleh kelas anak masing-masing.
- `List<Pembayaran> daftarMetode` adalah list bertipe kelas abstrak, dan `List<DapatDicetak>` di `cetakSemua()` adalah list bertipe interface. Keduanya sah, walaupun `Pembayaran` maupun `DapatDicetak` tidak bisa dibuat objeknya.
- `List.of(kedai, pesananBudi, pesananSiti)` berisi satu objek `Kedai` dan dua objek `Pesanan`. Java menerimanya sebagai `List<DapatDicetak>` karena ketiganya meng-*implements* `DapatDicetak`.

> [!TIP]
> **Coba sendiri:** di folder `studi-kasus`, buat file `PembayaranEWallet.java` berisi `public class PembayaranEWallet extends Pembayaran` yang **hanya** meng-*override* `namaMetode()`. Lalu jalankan `javac *.java`. Apa yang terjadi? Bandingkan dengan Pertemuan 09.

<details>
<summary>Lihat jawaban</summary>

```text
PembayaranEWallet.java:1: error: PembayaranEWallet is not abstract and does not override abstract method proses(int) in Pembayaran
public class PembayaranEWallet extends Pembayaran {
       ^
1 error
```

Di Pertemuan 09, kelas yang sama akan diterima begitu saja dan memakai `proses()` milik induk yang selalu berhasil. Kini kesalahan itu tertangkap saat kompilasi, sebelum program sempat berjalan. Hapus file itu lagi setelah mencoba.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan Error

Semua kesalahan berikut adalah **error kompilasi**: Java menolaknya sebelum program berjalan. Pesannya diawali nama file dan nomor baris, dan tanda `^` menunjuk posisi kesalahan. Kesalahan paling umum, yaitu kelas anak yang belum mengisi semua method abstrak (*is not abstract and does not override abstract method ...*), sudah kita temui di bagian 2 dan bagian 8. Perbaikannya: tulis method yang disebut dalam pesan, atau tandai kelas itu `abstract` jika memang sengaja dibiarkan setengah jadi.

### Kesalahan 1: Memakai `new` pada kelas abstrak atau interface

```java
        DapatDicetak dokumen = new DapatDicetak();
```

```text
E9.java:3: error: DapatDicetak is abstract; cannot be instantiated
        DapatDicetak dokumen = new DapatDicetak();
                               ^
1 error
```

**Artinya:** interface dan kelas abstrak tidak bisa dibuat objeknya. **Perbaikan:** buat objek dari kelas konkret yang meng-*implements* atau meng-*extends*-nya, misalnya `DapatDicetak dokumen = new Kedai("KedaiKita");`.

### Kesalahan 2: Memberi isi pada method abstrak

```java
abstract class Bentuk {
    public abstract int luas() {
        return 0;
    }
}
```

```text
E3.java:2: error: abstract methods cannot have a body
    public abstract int luas() {
                        ^
1 error
```

**Artinya:** method `abstract` tidak boleh punya badan `{ ... }`. **Perbaikan:** pilih salah satu. Jika ingin abstrak, tulis `public abstract int luas();` (diakhiri titik koma). Jika ingin punya isi bawaan, hapus kata `abstract`.

### Kesalahan 3: Method abstrak di kelas yang tidak `abstract`

```java
class Bentuk {
    public abstract int luas();
}
```

```text
E4.java:1: error: Bentuk is not abstract and does not override abstract method luas() in Bentuk
class Bentuk {
^
1 error
```

**Artinya:** kelas yang punya method abstrak wajib ditandai `abstract`. Pesannya terdengar aneh (`Bentuk` "tidak meng-*override*" method miliknya sendiri), tetapi maksudnya: kelas konkret tidak boleh menyimpan method tanpa isi. **Perbaikan:** `abstract class Bentuk`.

### Kesalahan 4: Lupa `public` saat mengisi method interface

```java
class Kedai implements DapatDicetak {
    @Override
    void cetak() {
        System.out.println("=== MENU ===");
    }
}
```

```text
E5.java:7: error: cetak() in Kedai cannot implement cetak() in DapatDicetak
    void cetak() {
         ^
  attempting to assign weaker access privileges; was public
1 error
```

**Artinya:** method di interface otomatis `public`. Tanpa kata `public`, method `cetak()` di `Kedai` hanya punya akses *package*, yang lebih sempit (*weaker access privileges*). Aturan "tidak boleh memperkecil akses saat *override*" dari Pertemuan 07 berlaku juga di sini. **Perbaikan:** `public void cetak()`.

### Kesalahan 5: Tertukar `extends` dan `implements`

```java
class Bebek extends BisaTerbang {   // BisaTerbang adalah interface
```

```text
E6.java:5: error: no interface expected here
class Bebek extends BisaTerbang {
                    ^
1 error
```

Kebalikannya, `class Bebek implements Hewan` (padahal `Hewan` adalah kelas abstrak), ditolak dengan pesan `error: interface expected here`.

**Artinya:** `extends` untuk kelas, `implements` untuk interface. **Perbaikan:** `class Bebek extends Hewan implements BisaTerbang`.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK. Fokuslah pada kata-kata kuncinya, misalnya *is abstract; cannot be instantiated* atau *does not override abstract method*.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Kelas abstrak | `abstract class Nama { ... }` | `public abstract class Pembayaran` |
| Method abstrak | `public abstract Tipe nama(...);` | `public abstract boolean proses(int total);` |
| Kelas anak konkret | `extends` + `@Override` semua method abstrak | `class PersegiPanjang extends Bentuk` |
| Konstruktor kelas abstrak | `protected Nama(...) { ... }` | `protected Kendaraan(String plat, int bensinLiter)` |
| Template method tak bisa diubah | `public final void nama()` | `public final void tampilkan()` |
| Interface | `interface Nama { Tipe method(); }` | `public interface DapatDicetak { void cetak(); }` |
| Memenuhi interface | `class X implements A, B` | `class Kedai implements DapatDicetak` |
| Satu induk + banyak interface | `class X extends Induk implements A, B` | `class Bebek extends Hewan implements BisaTerbang, BisaBerenang` |
| *Default method* | `default Tipe nama() { ... }` | `default int rataRata() { ... }` |
| Konstanta interface | `Tipe NAMA = nilai;` | `int BINTANG_MAKS = 5;` |
| Memeriksa kemampuan | `objek instanceof Interface` | `benda instanceof BisaTerbang` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
