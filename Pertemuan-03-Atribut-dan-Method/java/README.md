# ☕ Praktik Java Pertemuan 03: Atribut dan *Method* Lebih Dalam

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 03](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Atribut Objek dan Atribut `static`](#1-atribut-objek-dan-atribut-static)
2. [Atribut `static` Selalu lewat Nama Kelas](#2-atribut-static-selalu-lewat-nama-kelas)
3. [*Method* `static` dan Konstruktor Alternatif](#3-method-static-dan-konstruktor-alternatif)
4. [*Overloading* Konstruktor dan `this(...)`](#4-overloading-konstruktor-dan-this)
5. [Representasi Teks dengan `toString()`](#5-representasi-teks-dengan-tostring)
6. [Referensi, *Aliasing*, dan `null`](#6-referensi-aliasing-dan-null)
7. [Objek sebagai Parameter](#7-objek-sebagai-parameter)
8. [Objek sebagai Nilai Kembalian](#8-objek-sebagai-nilai-kembalian)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (17, 21, atau 25), VS Code dengan **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 8 contoh, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 03
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap *file* `.java` di sini adalah **program satu *file***: kelas utama yang berisi `main` dan kelas-kelas pembantunya ada di *file* yang sama.

> [!IMPORTANT]
> Seperti di Pertemuan 02, kelas yang memiliki `main` ditulis **paling atas** di setiap *file*, lalu kelas-kelas pembantunya di bawahnya. Ini syarat perintah `java NamaFile.java`. Ikuti aturan yang sama saat menulis programmu sendiri.

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).**

1. Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-03-Atribut-dan-Method/java`.
2. Buka *file* contoh yang ingin dicoba, misalnya `contoh/Contoh01AtributKelas.java`.
3. Klik tulisan **Run** tepat di atas baris `public static void main` (bagian dari **Run | Debug**) atau tombol ▷ di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** (kadang **DEBUG CONSOLE**) di bagian bawah.

Mengapa yang dibuka hanya folder `java` ini, bukan seluruh folder materi? Banyak pertemuan memakai nama kelas yang sama, misalnya `Menu`. Jika semuanya terbuka sekaligus, VS Code memberi garis merah dengan pesan `The type Menu is already defined`. Di dalam folder `java` satu pertemuan, setiap nama kelas sudah dibuat unik.

**Cara 2: lewat terminal.** Buka terminal (di VS Code: menu **Terminal → New Terminal**), pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-03-Atribut-dan-Method/java/contoh` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
java Contoh01AtributKelas.java
```

Perintah `java NamaFile.java` (Java 11 ke atas) mengompilasi *file* itu di memori, lalu langsung menjalankannya. Yang tercetak di terminal sama persis dengan blok ***Output:*** di [bagian 1](#1-atribut-objek-dan-atribut-static). Untuk contoh lain, ganti nama *file*-nya. *File* di folder `studi-kasus` dan `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan nama folder itu. Cara klasik dua langkah juga tetap bisa dipakai: `javac Contoh01AtributKelas.java`, lalu `java Contoh01AtributKelas`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Penjelasan lengkap tentang terminal ada di [Menjalankan Program](../../00-Persiapan/menjalankan-program.md).

### Tempat Menyimpan Kodemu Sendiri

Simpan semua kode buatanmu (hasil mengetik ulang, percobaan "Coba sendiri", *file* coretan seperti `Coba.java`, dan jawaban latihan) di folder `PBO-latihan-saya/pertemuan-03/`, **di luar** folder materi; untuk Java, pakai satu subfolder untuk setiap pertemuan agar nama kelas tidak bentrok. Jika sebuah percobaan memintamu mengubah *file* contoh, salin dulu *file* itu ke folder tersebut tanpa mengganti namanya (nama *file* Java harus sama dengan nama kelas `public`-nya), lalu ubah dan jalankan salinannya. Untuk menjalankan salinan itu, buka folder `pertemuan-03` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**); terminal di jendela itu (**Terminal → New Terminal**) langsung berada di folder `pertemuan-03`. Alasan dan cara menyalinnya ada di [aturan emas 00-Persiapan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

```text
Documents/
├── PBO2026/                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/
    └── pertemuan-03/         <- salinan contoh, Coba.java, dan jawaban latihanmu
```

### Cara Membaca Kode di Halaman Ini

- Setiap bagian diawali baris ***File*:** atau **Potongan dari** yang menautkan *file* contohnya.
- ***File*:** berarti kode di bawahnya adalah isi lengkap *file* itu, hanya tanpa komentar pembuka, termasuk kelas yang memiliki `main`. Hasil ketik ulangnya bisa langsung dijalankan.
- **Potongan dari** berarti yang ditampilkan hanya sebagian, biasanya kelas pembantunya dulu, lalu isi *method* `main`. Potongan dari dalam `main` tampil menjorok 8 spasi karena aslinya berada di dalam kelas dan di dalam `main`. Jangan mengetik ulang potongannya saja; jalankan *file* lengkapnya dengan cara di atas.
- Tanda `// [1]`, `// [2]`, dan seterusnya di dalam kode dijelaskan satu per satu dalam daftar **Penjelasan** tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* materi itu dijalankan. Hasil percobaan "Coba sendiri" yang kamu kerjakan di folder `pertemuan-03` ada di balik tulisan **Lihat jawaban** atau **Lihat hasilnya**.

## 1. Atribut Objek dan Atribut `static`

*File*: [`contoh/Contoh01AtributKelas.java`](contoh/Contoh01AtributKelas.java)

Di Java, atribut kelas ditandai dengan kata kunci **`static`**. Atribut tanpa `static` adalah atribut objek, seperti yang kita pakai di Pertemuan 02.

```java
public class Contoh01AtributKelas {

    public static void main(String[] args) {
        System.out.println("=== SEBELUM ADA OBJEK ===");
        System.out.println("Kampus          : " + Mahasiswa.kampus); // [6] dibaca tanpa objek
        System.out.println("Jumlah mahasiswa: " + Mahasiswa.jumlah);

        Mahasiswa ayu = new Mahasiswa("2409106001", "Ayu Lestari");
        Mahasiswa bima = new Mahasiswa("2409106002", "Bima Saputra");
        Mahasiswa citra = new Mahasiswa("2409106003", "Citra Dewi");

        System.out.println();
        System.out.println("=== SETELAH TIGA OBJEK DIBUAT ===");
        ayu.perkenalan();
        bima.perkenalan();
        citra.perkenalan();
        System.out.println("Jumlah mahasiswa: " + Mahasiswa.jumlah);

        System.out.println();
        System.out.println("=== NAMA KAMPUS DITULIS LENGKAP ===");
        Mahasiswa.kampus = "Universitas Mulawarman"; // [7] berlaku untuk SEMUA objek
        ayu.perkenalan();
        bima.perkenalan();
        citra.perkenalan();
    }
}

/** Mahasiswa Informatika di Samarinda. */
class Mahasiswa {
    static String kampus = "Unmul"; // [1] atribut kelas: sama untuk semua mahasiswa
    static int jumlah = 0;          // [2] atribut kelas: penghitung objek yang sudah dibuat

    String nim;  // [3] atribut objek: milik masing-masing mahasiswa
    String nama;

    Mahasiswa(String nim, String nama) {
        this.nim = nim;
        this.nama = nama;
        Mahasiswa.jumlah += 1; // [4] mengubah atribut kelas lewat NAMA KELAS
    }

    void perkenalan() {
        System.out.println("Saya " + nama + " (" + nim + ") dari " + Mahasiswa.kampus); // [5]
    }
}
```

***Output:***

```text
=== SEBELUM ADA OBJEK ===
Kampus          : Unmul
Jumlah mahasiswa: 0

=== SETELAH TIGA OBJEK DIBUAT ===
Saya Ayu Lestari (2409106001) dari Unmul
Saya Bima Saputra (2409106002) dari Unmul
Saya Citra Dewi (2409106003) dari Unmul
Jumlah mahasiswa: 3

=== NAMA KAMPUS DITULIS LENGKAP ===
Saya Ayu Lestari (2409106001) dari Universitas Mulawarman
Saya Bima Saputra (2409106002) dari Universitas Mulawarman
Saya Citra Dewi (2409106003) dari Universitas Mulawarman
```

Penjelasan:

- **[1]** `static String kampus` adalah **atribut kelas** (sering disebut juga *static field* atau variabel kelas). Nilainya hanya satu dan dipakai bersama oleh semua objek `Mahasiswa`.
- **[2]** `static int jumlah` dipakai sebagai **penghitung** objek yang sudah dibuat, dimulai dari 0.
- **[3]** *Field* tanpa `static` adalah **atribut objek**: setiap mahasiswa punya `nim` dan `nama` sendiri.
- **[4]** Setiap kali konstruktor berjalan, penghitung bertambah satu. Kita menulisnya lewat **nama kelas**, `Mahasiswa.jumlah` agar jelas bahwa yang diubah adalah milik bersama.
- **[5]** *Method* objek boleh membaca atribut `static`.
- **[6]** Atribut `static` sudah ada **sebelum** objek mana pun dibuat. Karena itu, `Mahasiswa.jumlah` bisa dibaca dari `main`, dan hasilnya 0.
- **[7]** Mengubah atribut `static` **satu kali** langsung berlaku untuk **semua** objek.

```text
                  Mahasiswa.kampus, Mahasiswa.jumlah     <- hanya ada SATU, milik kelas
                         ^          ^          ^
                         |          |          |
                       [ayu]     [bima]     [citra]       <- masing-masing punya nim dan nama
```

> [!NOTE]
> Sama seperti *field* biasa, *field* `static` yang tidak diberi nilai awal otomatis berisi nilai bawaan: `0` untuk `int`, `false` untuk `boolean`, dan `null` untuk objek seperti `String`.

> [!TIP]
> **Coba sendiri:** salin `contoh/Contoh01AtributKelas.java` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di akhir *method* `main` (tepat sebelum kurung kurawal `}` penutupnya), tambahkan dua baris berikut, simpan, lalu jalankan salinan itu. Baris terakhir *output*-nya harus `Jumlah mahasiswa: 4` karena konstruktor menaikkan penghitung sekali lagi.
>
> ```java
> Mahasiswa dimas = new Mahasiswa("2409106004", "Dimas Pratama");
> System.out.println("Jumlah mahasiswa: " + Mahasiswa.jumlah);
> ```

## 2. Atribut `static` Selalu lewat Nama Kelas

*File*: [`contoh/Contoh02AksesStatic.java`](contoh/Contoh02AksesStatic.java)

Java mengizinkan kita menulis atribut `static` **lewat objek**, misalnya `ayu.total` atau `this.total`. Tulisan itu sah, tetapi menyesatkan. Contoh ini memakai skenario yang sama persis dengan contoh Python di pertemuan ini: perpustakaan kampus menghitung jumlah pengunjung.

```java
public class Contoh02AksesStatic {

    public static void main(String[] args) {
        Pengunjung ayu = new Pengunjung("Ayu");
        Pengunjung bima = new Pengunjung("Bima");

        System.out.println("=== LEWAT OBJEK: this.total += 1 ===");
        ayu.masukLewatObjek();
        bima.masukLewatObjek();
        System.out.println("Total menurut kelas : " + Pengunjung.total);
        System.out.println("Total menurut ayu   : " + ayu.total);  // [3] boleh, tetapi menyesatkan
        System.out.println("Total menurut bima  : " + bima.total);

        System.out.println();
        System.out.println("=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===");
        Pengunjung citra = new Pengunjung("Citra");
        Pengunjung dimas = new Pengunjung("Dimas");
        citra.masukLewatKelas();
        dimas.masukLewatKelas();
        System.out.println("Total menurut kelas : " + Pengunjung.total);
        System.out.println("Total menurut citra : " + citra.total);
        System.out.println("Total menurut dimas : " + dimas.total);
        System.out.println("Total menurut ayu   : " + ayu.total); // [4] tetap total bersama
    }
}

/** Pengunjung perpustakaan kampus. */
class Pengunjung {
    static int total = 0; // atribut kelas: jumlah seluruh pengunjung hari ini

    String nama;

    Pengunjung(String nama) {
        this.nama = nama;
    }

    void masukLewatObjek() {
        this.total += 1; // [1] boleh, tetapi menyesatkan: yang berubah tetap total BERSAMA
    }

    void masukLewatKelas() {
        Pengunjung.total += 1; // [2] cara yang jelas: lewat nama kelas
    }
}
```

***Output:***

```text
=== LEWAT OBJEK: this.total += 1 ===
Total menurut kelas : 2
Total menurut ayu   : 2
Total menurut bima  : 2

=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===
Total menurut kelas : 4
Total menurut citra : 4
Total menurut dimas : 4
Total menurut ayu   : 4
```

Penjelasan:

- **[1]** `this.total += 1` terlihat seperti mengubah milik objek ini saja. Kenyataannya, `total` adalah *field* `static`, jadi yang berubah adalah **satu-satunya** `total` milik kelas.
- **[2]** `Pengunjung.total += 1` melakukan hal yang **sama persis**, tetapi tulisannya jujur: jelas bahwa yang diubah milik bersama.
- **[3]** `ayu.total` hanyalah cara lain menulis `Pengunjung.total`. Jadi, `ayu.total`, `bima.total`, dan `Pengunjung.total` selalu bernilai sama.
- **[4]** Bahkan setelah Citra dan Dimas masuk, `ayu.total` ikut menjadi 4 karena memang tidak ada "total milik Ayu".

*Compiler* sebenarnya juga tidak menyukai cara pertama. Kamu bisa memintanya menampilkan semua peringatan dengan pilihan `-Xlint`. Salin dulu `contoh/Contoh02AksesStatic.java` ke folder `pertemuan-03` milikmu, lalu ketik perintah berikut di terminal yang berada di folder `pertemuan-03` itu:

```bash
javac -Xlint Contoh02AksesStatic.java
```

Java menampilkan enam peringatan, satu untuk setiap tempat yang memakai `total` lewat objek. Salah satunya seperti ini:

```text
Contoh02AksesStatic.java:54: warning: [static] static variable should be qualified by type name, Pengunjung, instead of by an expression
        this.total += 1; // [1] boleh, tetapi menyesatkan: yang berubah tetap total BERSAMA
            ^
```

Artinya: "variabel `static` sebaiknya ditulis dengan nama tipenya (`Pengunjung`), bukan lewat sebuah ekspresi seperti `this`". Ini hanya **peringatan** (*warning*), bukan *error*, jadi program tetap bisa dijalankan. Editor seperti VS Code biasanya juga memberi garis peringatan kuning di tempat yang sama.

Perintah `javac` tadi juga membuat *file* `Contoh02AksesStatic.class` dan `Pengunjung.class` di folder `pertemuan-03`. Keduanya boleh dihapus.

> [!IMPORTANT]
> Aturannya sederhana: **tulis atribut `static` selalu lewat nama kelasnya**, misalnya `Pengunjung.total` atau `Mahasiswa.jumlah`. Pembaca kodemu langsung tahu bahwa data itu milik bersama.

> [!NOTE]
> Program Python dengan skenario yang sama ([`contoh02_jebakan_atribut_kelas.py`](../python/contoh/contoh02_jebakan_atribut_kelas.py)) menghasilkan *output* yang **berbeda**. Di Python, `self.total += 1` diam-diam membuat atribut objek baru sehingga total milik kelas tetap 0. Perbandingannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md#1-atribut-kelas-dua-kejutan-yang-berlawanan).

## 3. *Method* `static` dan Konstruktor Alternatif

Potongan dari [`contoh/Contoh03MethodStatic.java`](contoh/Contoh03MethodStatic.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Method* juga bisa diberi kata kunci `static`. *Method* `static` adalah milik kelas: dipanggil lewat nama kelas dan **tidak punya `this`**.

Potongan pertama: kelas `Tanggal` (di dalam *file*, kelas ini ditulis di bawah kelas utama `Contoh03MethodStatic`).

```java
/** Tanggal sederhana: hari, bulan, dan tahun (semuanya bilangan bulat). */
class Tanggal {
    static final String[] NAMA_BULAN = {"Januari", "Februari", "Maret", "April", "Mei",
        "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"};

    int hari;
    int bulan;
    int tahun;

    Tanggal(int hari, int bulan, int tahun) {
        this.hari = hari;
        this.bulan = bulan;
        this.tahun = tahun;
    }

    String teks() { // [1] method objek: butuh data milik objek (this)
        return hari + " " + NAMA_BULAN[bulan - 1] + " " + tahun;
    }

    /** true jika tahun kabisat (bulan Februari punya 29 hari). */
    static boolean isKabisat(int tahun) { // [2] method static: tanpa this
        return (tahun % 4 == 0 && tahun % 100 != 0) || tahun % 400 == 0;
    }

    /** Konstruktor alternatif: membuat Tanggal dari teks "hari-bulan-tahun". */
    static Tanggal dariTeks(String teks) { // [3] method static yang mengembalikan objek
        String[] bagian = teks.split("-");
        int hari = Integer.parseInt(bagian[0]); // [4] Integer.parseInt juga method static
        int bulan = Integer.parseInt(bagian[1]);
        int tahun = Integer.parseInt(bagian[2]);
        return new Tanggal(hari, bulan, tahun);
    }
}
```

Potongan kedua: isi *method* `main` di kelas `Contoh03MethodStatic`.

```java
        System.out.println("=== METHOD OBJEK (butuh objek) ===");
        Tanggal proklamasi = new Tanggal(17, 8, 1945);
        System.out.println("Proklamasi kemerdekaan: " + proklamasi.teks());

        System.out.println();
        System.out.println("=== STATIC METHOD (tanpa objek) ===");
        int[] daftarTahun = {2024, 2026, 1900, 2000};
        for (int tahun : daftarTahun) {
            if (Tanggal.isKabisat(tahun)) { // [5] dipanggil lewat nama kelas
                System.out.println(tahun + ": tahun kabisat");
            } else {
                System.out.println(tahun + ": bukan tahun kabisat");
            }
        }

        System.out.println();
        System.out.println("=== KONSTRUKTOR ALTERNATIF (dari teks) ===");
        Tanggal sumpahPemuda = Tanggal.dariTeks("28-10-1928"); // [6] objek dibuat dari teks
        System.out.println("Sumpah Pemuda: " + sumpahPemuda.teks());
        Tanggal pertempuran = Tanggal.dariTeks("10-11-1945");
        System.out.println("Pertempuran Surabaya: " + pertempuran.teks());
```

***Output:***

```text
=== METHOD OBJEK (butuh objek) ===
Proklamasi kemerdekaan: 17 Agustus 1945

=== STATIC METHOD (tanpa objek) ===
2024: tahun kabisat
2026: bukan tahun kabisat
1900: bukan tahun kabisat
2000: tahun kabisat

=== KONSTRUKTOR ALTERNATIF (dari teks) ===
Sumpah Pemuda: 28 Oktober 1928
Pertempuran Surabaya: 10 November 1945
```

Penjelasan:

- **[1]** `teks()` adalah *method* objek biasa. Ia butuh data milik objek tertentu (hari, bulan, tahun). `NAMA_BULAN` adalah konstanta milik kelas: `static` karena dipakai bersama, `final` karena nilainya tidak boleh diganti. Nama konstanta ditulis dengan huruf kapital semua.
- **[2]** `static boolean isKabisat(int tahun)` adalah ***method* `static`**. Ia hanya butuh angka tahun dari parameternya, lalu mengembalikan `true` atau `false`. Awalan `is` adalah kebiasaan Java untuk *method boolean*.
- **[3]** `dariTeks()` adalah *method* `static` yang **mengembalikan objek baru** bertipe `Tanggal`. Inilah **konstruktor alternatif** (sering disebut *static factory method*). `teks.split("-")` memecah `"28-10-1928"` menjadi *array* `{"28", "10", "1928"}`.
- **[4]** `Integer.parseInt("28")` mengubah teks menjadi angka `int`. Perhatikan cara memanggilnya: lewat nama kelas `Integer`. Ya, `parseInt` juga *method* `static`!
- **[5]** *Method* `static` dipanggil lewat **nama kelas**, tanpa membuat objek.
- **[6]** Konstruktor alternatif juga dipanggil lewat nama kelas, dan hasilnya objek `Tanggal` yang siap dipakai.

### Mengapa `main` ditulis `static`?

Saat kamu menjalankan `java Contoh03MethodStatic.java`, belum ada objek apa pun. Java lalu memanggil `Contoh03MethodStatic.main(args)` **lewat nama kelasnya**. Karena `main` adalah *method* `static`, Java tidak perlu membuat objek dulu untuk menjalankannya. Itulah sebabnya bentuk baku `main` adalah `public static void main(String[] args)`, dan di Java 17 maupun 21 bentuk ini wajib.

Akibatnya, ada aturan penting: dari dalam `main` (yang `static`), kita **hanya bisa langsung** memanggil *method* `static` lain dan memakai *field* `static`. Untuk memanggil *method* objek, buat objeknya dulu dengan `new`. Melanggar aturan ini menghasilkan *error* yang sangat sering muncul, yaitu `non-static method ... cannot be referenced from a static context` (lihat [Kesalahan 1](#kesalahan-1-memanggil-method-objek-dari-main-tanpa-objek)).

> [!NOTE]
> Java 25 memperkenalkan bentuk `main` yang lebih ringkas, termasuk `main` tanpa `static` (Java akan membuat objeknya terlebih dahulu). Di mata kuliah ini kita tetap memakai bentuk klasik `public static void main(String[] args)` karena berlaku di semua versi Java yang kita pakai (17, 21, dan 25).

### Kelas utilitas

Kelas yang **hanya berisi *method* `static`** disebut **kelas utilitas**, misalnya `Math` bawaan Java dan `Rupiah` di studi kasus KedaiKita. Kita memakainya seperti kotak perkakas: tidak perlu membuat objeknya, cukup panggil *method*-nya lewat nama kelas. Beberapa contoh *method* `static` yang dipanggil lewat nama kelas:

| Kelas | Contoh pemanggilan | Hasil |
|---|---|---|
| `Math` (bawaan Java) | `Math.max(3, 7)` | `7` |
| `Integer` (bawaan Java) | `Integer.parseInt("28")` | `28` |
| `Rupiah` (studi kasus KedaiKita) | `Rupiah.format(18000)` | `"Rp18.000"` |

> [!TIP]
> **Coba sendiri:** salin `contoh/Contoh03MethodStatic.java` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di akhir *method* `main`, tambahkan tiga baris berikut, lalu ganti `"21-04-2006"` dengan tanggal lahirmu. Simpan, lalu jalankan salinan itu.
>
> ```java
> Tanggal lahir = Tanggal.dariTeks("21-04-2006");
> System.out.println("Tanggal lahirku: " + lahir.teks());
> System.out.println("Tahun kabisat? " + Tanggal.isKabisat(lahir.tahun));
> ```

<details>
<summary>Lihat hasil untuk contoh tanggal di atas</summary>

```text
Tanggal lahirku: 21 April 2006
Tahun kabisat? false
```

Tahun 2006 tidak habis dibagi 4, jadi bukan tahun kabisat. Perhatikan bahwa `dariTeks()` dan `isKabisat()` sama-sama dipanggil lewat nama kelas `Tanggal`, sedangkan `teks()` dipanggil lewat objek `lahir`.

</details>

## 4. *Overloading* Konstruktor dan `this(...)`

Potongan dari [`contoh/Contoh04OverloadingKonstruktor.java`](contoh/Contoh04OverloadingKonstruktor.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Java tidak mengenal nilai bawaan untuk parameter. Sebagai gantinya, kita boleh menulis **beberapa konstruktor** dalam satu kelas, asalkan daftar parameternya berbeda. Teknik ini disebut ***overloading***.

Potongan pertama: kelas `Laptop` (di dalam *file*, kelas ini ditulis di bawah kelas utama `Contoh04OverloadingKonstruktor`).

```java
/** Laptop dengan kapasitas RAM dan penyimpanan (dalam GB). */
class Laptop {
    String merek;
    int ram;
    int penyimpanan;

    Laptop(String merek, int ram, int penyimpanan) { // [1] konstruktor lengkap
        this.merek = merek;
        this.ram = ram;
        this.penyimpanan = penyimpanan;
    }

    Laptop(String merek, int ram) { // [2] overloading: daftar parameter berbeda
        this(merek, ram, 512);      // [3] teruskan ke konstruktor lengkap
    }

    Laptop(String merek) {
        this(merek, 8, 512);
    }

    void tambahRam() { // [4] overloading method: nama sama, parameter berbeda
        tambahRam(8);
    }

    void tambahRam(int tambahan) {
        ram = ram + tambahan;
    }

    String info() {
        return merek + ": RAM " + ram + " GB, SSD " + penyimpanan + " GB";
    }
}
```

Potongan kedua: isi *method* `main` di kelas `Contoh04OverloadingKonstruktor`.

```java
        System.out.println("=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===");
        Laptop laptopAyu = new Laptop("Asus");             // [5] konstruktor 1 parameter
        Laptop laptopBima = new Laptop("Lenovo", 16);      //     konstruktor 2 parameter
        Laptop laptopCitra = new Laptop("Acer", 16, 1024); //     konstruktor 3 parameter
        Laptop laptopDimas = new Laptop("HP", 8, 256);     // [6] semua nilai ditulis
        System.out.println(laptopAyu.info());
        System.out.println(laptopBima.info());
        System.out.println(laptopCitra.info());
        System.out.println(laptopDimas.info());

        System.out.println();
        System.out.println("=== MENAMBAH RAM ===");
        laptopAyu.tambahRam(); // [7] memakai versi tanpa parameter (tambah 8)
        laptopBima.tambahRam(16);
        System.out.println(laptopAyu.info());
        System.out.println(laptopBima.info());
```

***Output:***

```text
=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===
Asus: RAM 8 GB, SSD 512 GB
Lenovo: RAM 16 GB, SSD 512 GB
Acer: RAM 16 GB, SSD 1024 GB
HP: RAM 8 GB, SSD 256 GB

=== MENAMBAH RAM ===
Asus: RAM 16 GB, SSD 512 GB
Lenovo: RAM 32 GB, SSD 512 GB
```

Penjelasan:

- **[1]** Konstruktor **lengkap** dengan tiga parameter. Hanya konstruktor ini yang benar-benar mengisi *field*.
- **[2]** Konstruktor kedua bernama sama, tetapi parameternya hanya dua. Java memilih konstruktor berdasarkan **jumlah dan tipe argumen** yang dikirim.
- **[3]** `this(merek, ram, 512)` memanggil konstruktor lain **di kelas yang sama**, yaitu konstruktor lengkap, sambil mengisi `penyimpanan` dengan nilai bawaan 512. Dengan cara ini, kode pengisian *field* tidak perlu ditulis berulang.
- **[4]** *Overloading* juga berlaku untuk *method* biasa. `tambahRam()` tanpa parameter meneruskan ke `tambahRam(8)`. Topik ini akan dibahas lagi di Pertemuan 09 (Polimorfisme).
- **[5]** Tiga baris ini memanggil tiga konstruktor yang berbeda, sesuai jumlah argumennya.
- **[6]** Java tidak punya argumen bernama seperti Python (`penyimpanan=256`). Jika ingin mengubah `penyimpanan` saja, kita tetap menulis semua nilai: `new Laptop("HP", 8, 256)`.
- **[7]** Memanggil versi `tambahRam()` tanpa argumen sehingga RAM bertambah 8.

Alur pemanggilan `new Laptop("Asus")`:

```text
new Laptop("Asus")
   -> Laptop(String merek)                                memanggil this(merek, 8, 512)
      -> Laptop(String merek, int ram, int penyimpanan)   mengisi ketiga field
```

Aturan *overloading* yang perlu diingat:

- Konstruktor (atau *method*) yang bernama sama harus berbeda **daftar tipe parameternya**: jumlahnya, tipenya, atau urutan tipenya. **Nama** parameter tidak dihitung. Karena itu, `Laptop(String merek, int ram)` dan `Laptop(String merek, int penyimpanan)` **tidak boleh** ada bersamaan (lihat [Kesalahan 5](#kesalahan-5-dua-konstruktor-dengan-tipe-parameter-yang-sama)).
- `this(...)` harus ditulis sebagai **pernyataan pertama** di dalam konstruktor. Di Java 17 dan 21, menaruh perintah lain sebelum `this(...)` menghasilkan *error* `call to this must be first statement in constructor`.

> [!NOTE]
> Java 25 sedikit melonggarkan aturan "pernyataan pertama" untuk `this(...)`. Meski begitu, menulis `this(...)` di baris pertama tetap cara yang paling aman dan paling mudah dibaca, jadi biasakan seperti itu.

## 5. Representasi Teks dengan `toString()`

Potongan dari [`contoh/Contoh05ToString.java`](contoh/Contoh05ToString.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Setiap kelas Java otomatis punya *method* `toString()` bawaan. Sayangnya, hasil bawaannya tidak berguna bagi manusia. Bayangkan kelas `Motor` yang belum punya `toString()` sendiri. Jika objeknya dicetak dengan `System.out.println(motor)`, hasilnya kira-kira seperti ini:

```text
Motor@130f889
```

Teks itu berisi nama kelas, tanda `@`, dan sebuah kode angka yang bisa berbeda di komputermu. Kita ingin teks yang lebih bermakna, jadi kita **menimpa** `toString()` bawaan dengan versi sendiri.

Potongan pertama: kelas `Motor` (di dalam *file*, kelas ini ditulis di bawah kelas utama `Contoh05ToString`).

```java
/** Motor mahasiswa yang terdaftar di parkiran kampus. */
class Motor {
    String plat;
    String merek;
    String warna;

    Motor(String plat, String merek, String warna) {
        this.plat = plat;
        this.merek = merek;
        this.warna = warna;
    }

    @Override // [1] menandai bahwa kita menimpa toString() bawaan
    public String toString() { // [2] wajib public; mengembalikan teks, bukan mencetak
        return plat + " - " + merek + " (" + warna + ")";
    }
}
```

Potongan kedua: isi *method* `main` di kelas `Contoh05ToString`.

```java
        Motor motorBudi = new Motor("KT 1234 AB", "Honda Beat", "merah");
        Motor motorSiti = new Motor("KT 5678 CD", "Yamaha NMAX", "hitam");

        System.out.println("=== MENCETAK OBJEK LANGSUNG ===");
        System.out.println(motorBudi); // [3] println memanggil motorBudi.toString()
        System.out.println(motorSiti);

        System.out.println();
        System.out.println("=== DIPAKAI DI DALAM TEKS LAIN ===");
        System.out.println("Motor Budi: " + motorBudi); // [4] penggabungan teks juga memanggilnya
        String teks = motorSiti.toString();             // [5] boleh juga dipanggil langsung
        System.out.println("Teks motor Siti terdiri atas " + teks.length() + " karakter");

        System.out.println();
        System.out.println("=== SETELAH WARNA DIUBAH ===");
        motorBudi.warna = "biru";
        System.out.println(motorBudi); // [6] teks selalu mengikuti nilai atribut terbaru
```

***Output:***

```text
=== MENCETAK OBJEK LANGSUNG ===
KT 1234 AB - Honda Beat (merah)
KT 5678 CD - Yamaha NMAX (hitam)

=== DIPAKAI DI DALAM TEKS LAIN ===
Motor Budi: KT 1234 AB - Honda Beat (merah)
Teks motor Siti terdiri atas 32 karakter

=== SETELAH WARNA DIUBAH ===
KT 1234 AB - Honda Beat (biru)
```

Penjelasan:

- **[1]** `@Override` adalah **anotasi**: catatan untuk *compiler* bahwa *method* ini **menimpa** *method* bawaan. *Compiler* lalu memeriksa apakah memang ada *method* bawaan yang ditimpa. Jika kita salah ketik, misalnya `tostring()`, *compiler* langsung protes (lihat [Kesalahan 4](#kesalahan-4-salah-ketik-nama-method-yang-di-override)). Detail tentang *override* dibahas di Pertemuan 07.
- **[2]** `toString()` **wajib** ditulis `public` dan mengembalikan `String`, persis seperti versi bawaannya. Kata `public` di sini bukan pilihan: *method* yang menimpa tidak boleh punya hak akses yang lebih sempit (aturan hak akses dibahas di Pertemuan 04). Tugasnya **mengembalikan** teks, bukan mencetak.
- **[3]** `System.out.println(motorBudi)` otomatis memanggil `motorBudi.toString()`.
- **[4]** Menggabungkan objek dengan teks memakai `+` juga otomatis memanggil `toString()`.
- **[5]** `toString()` boleh juga dipanggil langsung. Hasilnya `String` biasa yang bisa diolah lagi, misalnya dihitung panjangnya dengan `length()`.
- **[6]** Karena `toString()` menyusun teks dari *field* **saat itu juga**, perubahan *field* langsung terlihat saat objek dicetak lagi.

> [!TIP]
> **Coba sendiri:** salin `contoh/Contoh05ToString.java` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di dalam `toString()`, ganti baris `return` menjadi `return merek + " " + warna + " (" + plat + ")";`, simpan, lalu jalankan salinan itu. Kamu tidak perlu mengubah satu baris pun di `main`. Tebak dulu: bagian mana saja dari *output* yang ikut berubah?

<details>
<summary>Lihat hasilnya</summary>

```text
=== MENCETAK OBJEK LANGSUNG ===
Honda Beat merah (KT 1234 AB)
Yamaha NMAX hitam (KT 5678 CD)

=== DIPAKAI DI DALAM TEKS LAIN ===
Motor Budi: Honda Beat merah (KT 1234 AB)
Teks motor Siti terdiri atas 30 karakter

=== SETELAH WARNA DIUBAH ===
Honda Beat biru (KT 1234 AB)
```

Semua tempat yang mencetak motor ikut berubah, termasuk panjang teks motor Siti (kini 30 karakter). Itulah enaknya `toString()`: aturan tampilannya cukup ditulis di **satu** tempat.

</details>

## 6. Referensi, *Aliasing*, dan `null`

Potongan dari [`contoh/Contoh06Referensi.java`](contoh/Contoh06Referensi.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Potongan pertama: isi *method* `main` di kelas `Contoh06Referensi`.

```java
        System.out.println("=== DUA VARIABEL, SATU OBJEK ===");
        Ponsel ponselBudi = new Ponsel("Budi", 80);
        Ponsel ponselDipinjam = ponselBudi; // [1] TIDAK membuat ponsel baru
        ponselDipinjam.pakai(30);           // [2] Siti memakai ponsel yang ia pinjam
        System.out.println("Baterai dilihat lewat variabel peminjam: "
                + ponselDipinjam.baterai + "%");
        System.out.println("Baterai dilihat lewat variabel pemilik : "
                + ponselBudi.baterai + "%"); // [3] ikut berubah!
        if (ponselBudi == ponselDipinjam) { // [4] == pada objek: apakah objeknya sama?
            System.out.println("Keduanya menunjuk objek yang SAMA");
        } else {
            System.out.println("Keduanya menunjuk objek yang berbeda");
        }

        System.out.println();
        System.out.println("=== DUA OBJEK DENGAN DATA KEMBAR ===");
        Ponsel ponselA = new Ponsel("Rina", 50);
        Ponsel ponselB = new Ponsel("Rina", 50); // [5] objek baru, walaupun datanya kembar
        if (ponselA == ponselB) {
            System.out.println("Ponsel A dan ponsel B menunjuk objek yang SAMA");
        } else {
            System.out.println("Ponsel A dan ponsel B menunjuk objek yang berbeda");
        }
        ponselA.pakai(10);
        System.out.println("Baterai ponsel A: " + ponselA.baterai + "%, ponsel B: "
                + ponselB.baterai + "%");

        System.out.println();
        System.out.println("=== VARIABEL TANPA OBJEK ===");
        Ponsel ponselDimas = null; // [6] Dimas belum punya ponsel
        if (ponselDimas == null) { // [7] cara memeriksa null
            System.out.println("Dimas belum punya ponsel");
        }
        ponselDipinjam = null; // [8] Siti mengembalikan ponsel: "label"-nya dilepas
        System.out.println("Ponsel Budi tetap ada, baterainya " + ponselBudi.baterai + "%");
```

Potongan kedua: kelas `Ponsel` yang dipakai (di dalam *file*, kelas ini ditulis di bawah kelas utama).

```java
/** Ponsel dengan persentase baterai. */
class Ponsel {
    String pemilik;
    int baterai;

    Ponsel(String pemilik, int baterai) {
        this.pemilik = pemilik;
        this.baterai = baterai;
    }

    void pakai(int persen) {
        baterai = baterai - persen;
    }
}
```

***Output:***

```text
=== DUA VARIABEL, SATU OBJEK ===
Baterai dilihat lewat variabel peminjam: 50%
Baterai dilihat lewat variabel pemilik : 50%
Keduanya menunjuk objek yang SAMA

=== DUA OBJEK DENGAN DATA KEMBAR ===
Ponsel A dan ponsel B menunjuk objek yang berbeda
Baterai ponsel A: 40%, ponsel B: 50%

=== VARIABEL TANPA OBJEK ===
Dimas belum punya ponsel
Ponsel Budi tetap ada, baterainya 50%
```

Penjelasan:

- **[1]** `ponselDipinjam = ponselBudi` **tidak** membuat ponsel baru karena tidak ada `new`. Yang disalin hanyalah referensinya sehingga kedua variabel menunjuk objek yang sama.
- **[2]** Siti memakai ponsel lewat variabel `ponselDipinjam`, dan baterai **objek itu** berkurang 30.
- **[3]** Dilihat lewat `ponselBudi`, baterainya juga 50%. Memang hanya ada satu ponsel.
- **[4]** Untuk objek, operator `==` menjawab pertanyaan "apakah dua variabel menunjuk **objek yang sama**?".
- **[5]** `new` dipanggil dua kali, jadi ada **dua objek berbeda** walaupun datanya kembar.
- **[6]** `null` berarti variabel **tidak menunjuk objek apa pun**.
- **[7]** `null` diperiksa dengan `==`.
- **[8]** Mengisi `ponselDipinjam` dengan `null` hanya **melepas label**. Objek ponselnya tetap ada karena masih ditunjuk oleh `ponselBudi`.

Keadaan memori setelah baris [2]:

```text
 ponselBudi --------+
                    v
                [Ponsel] pemilik = "Budi", baterai = 50
                    ^
 ponselDipinjam ----+          satu objek, dua nama (aliasing)
```

### `==` atau `.equals()`?

| Cara | Pertanyaan yang dijawab | Contoh |
|---|---|---|
| `a == b` | apakah `a` dan `b` menunjuk **objek yang sama**? | `ponselBudi == ponselDipinjam` |
| `a.equals(b)` | apakah **isinya** sama? | `kategori.equals("Minuman")` |

Untuk kelas buatan kita sendiri, `equals()` bawaan **masih** membandingkan apakah objeknya sama, persis seperti `==`. Jadi, `ponselA.equals(ponselB)` bernilai `false` walaupun datanya kembar. Cara mengatur `equals()` sendiri dibahas di Pertemuan 12.

Yang **sudah wajib** kamu biasakan sejak sekarang: **teks (`String`) dibandingkan dengan `.equals()`**, bukan dengan `==`. Teks yang isinya sama bisa saja tersimpan sebagai dua objek berbeda (lihat [Kesalahan 6](#kesalahan-6-membandingkan-string-dengan-)).

### Memanggil *method* lewat `null`

Jika `ponselDimas` masih `null` lalu kita menulis `ponselDimas.pakai(10);`, program berhenti dengan pesan berikut. Pesan ini diambil dari program kecil bernama `ContohNull.java` (tidak ada di folder `contoh/`):

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Ponsel.pakai(int)" because "<local1>" is null
	at ContohNull.main(ContohNull.java:4)
```

Artinya: tidak ada objek yang bisa menjalankan `pakai`. Bagian `ContohNull.java:4` menunjukkan *file* dan nomor baris tempat *error* terjadi. Nama variabel tertulis sebagai `<local1>`, bukan `ponselDimas` karena program dijalankan dari terminal (`java NamaFile.java` maupun `javac` lalu `java`) tanpa menyimpan nama variabel lokal. Jika dijalankan dengan tombol **Run** di VS Code, biasanya nama `ponselDimas` yang muncul. **Perbaikan:** pastikan variabel sudah berisi objek, atau periksa dulu dengan `if (ponselDimas != null)`.

> [!TIP]
> **Coba sendiri:** tebak dulu *output* kode berikut. Setelah itu, buktikan: salin `contoh/Contoh06Referensi.java` ke folder `pertemuan-03` milikmu, buka salinannya, tambahkan kelima baris ini di akhir *method* `main`, simpan, lalu jalankan salinan itu. Jawabannya ada di baris terakhir *output*.
>
> ```java
> Ponsel x = new Ponsel("Ayu", 90);
> Ponsel y = x;
> Ponsel z = new Ponsel("Ayu", 90);
> y.pakai(20);
> System.out.println(x.baterai + " " + z.baterai + " " + (x == y) + " " + (x == z));
> ```

<details>
<summary>Lihat jawaban</summary>

`70 90 true false`. `x` dan `y` menunjuk objek yang sama, jadi pemakaian lewat `y` ikut mengurangi baterai `x`. `z` adalah objek lain yang tidak tersentuh.

</details>

## 7. Objek sebagai Parameter

*File*: [`contoh/Contoh07ObjekParameter.java`](contoh/Contoh07ObjekParameter.java)

```java
public class Contoh07ObjekParameter {

    // Method static milik kelas utama: bisa dipanggil langsung dari main.
    static void tambahBonusAngka(int saldo) { // [4] menerima ANGKA (salinan nilainya)
        saldo = saldo + 5000; // hanya mengubah variabel milik method ini
        System.out.println("  (di dalam: Rp" + saldo + ")");
    }

    static void tambahBonusDompet(DompetDigital dompet) { // [5] menerima OBJEK
        dompet.saldo = dompet.saldo + 5000; // mengubah objek milik pemanggil
        System.out.println("  (di dalam: Rp" + dompet.saldo + ")");
    }

    public static void main(String[] args) {
        DompetDigital dompetBudi = new DompetDigital("Budi", 100000);
        DompetDigital dompetSiti = new DompetDigital("Siti", 20000);

        System.out.println("=== TRANSFER ANTARDOMPET ===");
        dompetBudi.transfer(dompetSiti, 30000); // [6] objek dompetSiti dikirim
        dompetSiti.transfer(dompetBudi, 75000);
        System.out.println("Saldo Budi: Rp" + dompetBudi.saldo);
        System.out.println("Saldo Siti: Rp" + dompetSiti.saldo);

        System.out.println();
        System.out.println("=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===");
        int saldoTunai = 10000;
        tambahBonusAngka(saldoTunai);
        System.out.println("Saldo tunai sesudahnya      : Rp" + saldoTunai); // [7] tidak berubah
        tambahBonusDompet(dompetSiti);
        System.out.println("Saldo dompet Siti sesudahnya: Rp" + dompetSiti.saldo); // [8] berubah
    }
}

/** Dompet digital (e-wallet) dengan saldo dalam rupiah. */
class DompetDigital {
    String pemilik;
    int saldo;

    DompetDigital(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    boolean saldoCukup(int jumlah) { // [1] method boolean: jawabannya ya atau tidak
        return saldo >= jumlah;
    }

    void transfer(DompetDigital tujuan, int jumlah) { // [2] tujuan berisi objek lain
        if (!saldoCukup(jumlah)) {
            System.out.println("Transfer gagal: saldo " + pemilik + " tidak cukup");
            return;
        }
        saldo = saldo - jumlah;
        tujuan.saldo = tujuan.saldo + jumlah; // [3] mengubah objek yang dikirim
        System.out.println(pemilik + " transfer Rp" + jumlah + " ke " + tujuan.pemilik);
    }
}
```

***Output:***

```text
=== TRANSFER ANTARDOMPET ===
Budi transfer Rp30000 ke Siti
Transfer gagal: saldo Siti tidak cukup
Saldo Budi: Rp70000
Saldo Siti: Rp50000

=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===
  (di dalam: Rp15000)
Saldo tunai sesudahnya      : Rp10000
  (di dalam: Rp55000)
Saldo dompet Siti sesudahnya: Rp55000
```

Penjelasan:

- **[1]** `saldoCukup()` adalah ***method boolean***. Namanya dibaca seperti pertanyaan ("saldonya cukup?"), dan hasilnya langsung dipakai di `if`.
- **[2]** Parameter `tujuan` bertipe `DompetDigital`, jadi ia menerima objek dompet lain.
- **[3]** *Method* mengubah saldo **objek yang dikirim**. Setelah *method* selesai, perubahan itu tetap ada karena `tujuan` dan `dompetSiti` menunjuk objek yang sama.
- **[4]** *Method* `static` ini menerima **angka**. Di dalamnya, `saldo` diubah menjadi 15000, tetapi itu hanya variabel milik *method*. *Method* ini `static` agar bisa dipanggil langsung dari `main` tanpa objek.
- **[5]** *Method* ini menerima **objek**, lalu mengubah *field* objek itu.
- **[6]** Objek `dompetSiti` dikirim sebagai argumen.
- **[7]** `saldoTunai` milik `main` tetap 10000.
- **[8]** Saldo dompet Siti benar-benar bertambah 5000 karena yang diubah adalah **isi objeknya**.

Secara teknis, Java **selalu menyalin nilai** argumen ke parameter. Untuk `int`, yang disalin adalah angkanya. Untuk objek, yang disalin adalah **referensinya** sehingga parameter dan variabel pemanggil menunjuk objek yang sama.

```text
tambahBonusAngka(saldoTunai)      ->  method menerima SALINAN angka 10000
tambahBonusDompet(dompetSiti)     ->  method menerima salinan referensi ke objek yang SAMA
```

> [!TIP]
> **Coba sendiri:** salin `contoh/Contoh07ObjekParameter.java` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Tambahkan *method* berikut di dalam kelas `Contoh07ObjekParameter`, tepat di bawah *method* `tambahBonusDompet`. Lalu, di akhir `main`, tambahkan dua baris `gantiDompet(dompetSiti);` dan `System.out.println(dompetSiti.saldo);`. Simpan, lalu jalankan salinan itu. Tebak dulu: apakah saldonya menjadi 0?
>
> ```java
> static void gantiDompet(DompetDigital dompet) {
>     dompet = new DompetDigital("Orang Lain", 0);
> }
> ```

<details>
<summary>Lihat jawaban</summary>

Tidak. Saldo Siti tetap 55000. Baris `dompet = new DompetDigital(...)` hanya mengarahkan **variabel parameter** `dompet` ke objek baru. Variabel `dompetSiti` milik `main` tetap menunjuk objek lama. *Method* bisa **mengubah isi** objek kiriman, tetapi tidak bisa **mengganti** objek yang dipegang variabel pemanggil.

</details>

## 8. Objek sebagai Nilai Kembalian

Potongan dari [`contoh/Contoh08ObjekKembalian.java`](contoh/Contoh08ObjekKembalian.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Potongan pertama: kelas `Durasi` (di dalam *file*, kelas ini ditulis di bawah kelas utama `Contoh08ObjekKembalian`).

```java
/** Lama waktu dalam jam dan menit (bilangan bulat). */
class Durasi {
    int jam;
    int menit;

    Durasi(int jam, int menit) {
        int total = jam * 60 + menit; // [1] dirapikan: 1 jam 75 menit -> 2 jam 15 menit
        this.jam = total / 60;
        this.menit = total % 60;
    }

    int totalMenit() {
        return jam * 60 + menit;
    }

    Durasi tambah(Durasi lain) { // [2] tipe kembaliannya Durasi: sebuah objek
        return new Durasi(0, totalMenit() + lain.totalMenit()); // [3] objek BARU
    }

    boolean lebihLamaDari(Durasi lain) { // [4] method boolean dengan parameter objek
        return totalMenit() > lain.totalMenit();
    }

    @Override
    public String toString() {
        return jam + " jam " + menit + " menit";
    }
}
```

Potongan kedua: isi *method* `main` di kelas `Contoh08ObjekKembalian`.

```java
        Durasi kuliah = new Durasi(2, 30);
        Durasi praktikum = new Durasi(1, 40);

        System.out.println("=== MENJUMLAHKAN DUA DURASI ===");
        Durasi total = kuliah.tambah(praktikum); // [5] hasilnya objek baru
        System.out.println("Kuliah    : " + kuliah);
        System.out.println("Praktikum : " + praktikum);
        System.out.println("Total     : " + total);
        System.out.println("Durasi aneh 1 jam 75 menit dirapikan menjadi " + new Durasi(1, 75));

        System.out.println();
        System.out.println("=== MEMANGGIL SECARA BERANTAI ===");
        Durasi istirahat = new Durasi(0, 45);
        Durasi sehari = kuliah.tambah(istirahat).tambah(praktikum); // [6] hasil dipakai lagi
        System.out.println("Kuliah + istirahat + praktikum = " + sehari);
        System.out.println("Kuliah tetap " + kuliah); // [7] objek lama tidak berubah

        System.out.println();
        System.out.println("=== MEMBANDINGKAN DUA DURASI ===");
        Durasi batas = new Durasi(4, 30);
        if (total.lebihLamaDari(batas)) {
            System.out.println(total + " lebih lama dari " + batas);
        } else {
            System.out.println(total + " tidak lebih lama dari " + batas);
        }
```

***Output:***

```text
=== MENJUMLAHKAN DUA DURASI ===
Kuliah    : 2 jam 30 menit
Praktikum : 1 jam 40 menit
Total     : 4 jam 10 menit
Durasi aneh 1 jam 75 menit dirapikan menjadi 2 jam 15 menit

=== MEMANGGIL SECARA BERANTAI ===
Kuliah + istirahat + praktikum = 4 jam 55 menit
Kuliah tetap 2 jam 30 menit

=== MEMBANDINGKAN DUA DURASI ===
4 jam 10 menit tidak lebih lama dari 4 jam 30 menit
```

Penjelasan:

- **[1]** Konstruktor mengubah semuanya menjadi total menit, lalu membaginya lagi menjadi jam dan menit (pembagian `int` membuang sisa, `%` mengambil sisanya). Jadi, `new Durasi(1, 75)` tersimpan rapi sebagai 2 jam 15 menit.
- **[2]** Tipe kembalian `tambah()` adalah `Durasi`, yaitu nama kelas. Artinya, *method* ini mengembalikan sebuah **objek** `Durasi`.
- **[3]** `tambah()` **tidak mengubah** objek ini maupun `lain`. Ia membuat objek **baru** dengan `new`, lalu mengembalikannya.
- **[4]** `lebihLamaDari()` menerima objek sebagai parameter dan mengembalikan `boolean`. Bagian akhir `main` memakainya untuk membandingkan `total` dengan batas 4 jam 30 menit.
- **[5]** Hasil `tambah()` disimpan ke variabel bertipe `Durasi`.
- **[6]** Karena `tambah()` mengembalikan objek `Durasi`, hasilnya bisa langsung dipanggil `tambah()` lagi. Ini disebut pemanggilan **berantai**.
- **[7]** Objek `kuliah` tetap 2 jam 30 menit. Penjumlahan tidak merusak objek asalnya.

> [!IMPORTANT]
> Ada dua gaya *method* yang sama-sama sah: *method* yang **mengubah objeknya sendiri** (misalnya `tambahRam()` atau `pakai()`), dan *method* yang **mengembalikan objek baru** (misalnya `tambah()` di sini). Pilih salah satu dengan sadar, lalu beri nama yang jujur agar pembaca tahu apakah objek asal akan berubah. Kelas `String` milik Java memakai gaya kedua: `teks.replace(',', '.')` tidak mengubah `teks`, melainkan mengembalikan `String` baru.

## 9. Studi Kasus KedaiKita

*File*: [`studi-kasus/KedaiKita.java`](studi-kasus/KedaiKita.java)

Saatnya mengembangkan KedaiKita dari Pertemuan 02. Rancangannya sudah kita bahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-menu-yang-lebih-lengkap).

**Apa yang berubah dibanding Pertemuan 02?**

- Kelas utilitas baru `Rupiah` dengan *method* `static` `format()` menampilkan uang dengan titik ribuan: `Rp18.000`, bukan lagi `Rp18000`.
- `Menu` kini punya lima *field*: `kode`, `nama`, `harga`, `kategori`, dan `stok`, serta **dua konstruktor**: dengan stok, atau tanpa stok (otomatis 0).
- *Field* `static` `jumlahMenu` menghitung banyaknya menu yang sudah dibuat.
- `tampilkanInfo()` dihapus dan diganti `toString()` sehingga menu cukup dicetak dengan `System.out.println(menu)`.
- *Method* baru: `hargaSetelahDiskon(persen)` dan `stokCukup(jumlah)`. *Method* `hitungTotal(jumlah)` tetap ada.
- Kelas baru `Pelanggan` dengan *field* `nama`, `noHp`, dan `poin` (selalu mulai dari 0), serta *method* `tambahPoin()`.

Perubahan terbesar ada pada cara menampilkan menu. Bandingkan potongan kode kelas `Menu` versi Pertemuan 02 dan versi sekarang (hanya untuk dibaca, bukan untuk dijalankan):

```java
// Pertemuan 02: method yang MENCETAK
void tampilkanInfo() {
    System.out.println(nama + " - Rp" + harga);
}

// Pertemuan 03: method yang MENGEMBALIKAN teks
@Override
public String toString() {
    return "[" + kode + "] " + nama + " (" + kategori + ") - "
            + Rupiah.format(harga) + " | stok " + stok;
}
```

Isi lengkap *file* `studi-kasus/KedaiKita.java` (tanpa komentar pembuka di baris paling atas):

```java
import java.util.Locale;

public class KedaiKita {

    public static void main(String[] args) {
        Menu kopi = new Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20);
        Menu esTeh = new Menu("M02", "Es Teh Manis", 8000, "Minuman", 30);
        Menu nasiGoreng = new Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15);
        Menu mieGoreng = new Menu("M04", "Mie Goreng Jawa", 23000, "Makanan"); // stok bawaan 0

        System.out.println("=== MENU KEDAIKITA ===");
        System.out.println(kopi);
        System.out.println(esTeh);
        System.out.println(nasiGoreng);
        System.out.println(mieGoreng);
        System.out.println("Jumlah menu terdaftar: " + Menu.jumlahMenu);

        System.out.println();
        System.out.println("=== CEK STOK ===");
        if (kopi.stokCukup(2)) {
            System.out.println("Pesan 2 " + kopi.nama + "? Bisa");
        } else {
            System.out.println("Pesan 2 " + kopi.nama + "? Stok tidak cukup");
        }
        if (mieGoreng.stokCukup(1)) {
            System.out.println("Pesan 1 " + mieGoreng.nama + "? Bisa");
        } else {
            System.out.println("Pesan 1 " + mieGoreng.nama + "? Stok tidak cukup");
        }

        System.out.println();
        System.out.println("=== PROMO HARI INI: DISKON 10% ===");
        Menu[] menuPromo = {kopi, nasiGoreng};
        for (Menu menu : menuPromo) {
            int hargaBaru = menu.hargaSetelahDiskon(10);
            System.out.println(menu.nama + ": " + Rupiah.format(menu.harga) + " -> "
                    + Rupiah.format(hargaBaru));
        }

        System.out.println();
        System.out.println("=== PELANGGAN ===");
        Pelanggan budi = new Pelanggan("Budi Santoso", "081234567890");
        System.out.println(budi);
        int belanja = kopi.hitungTotal(2) + esTeh.hitungTotal(1);
        int poinBaru = belanja / 10000; // 1 poin untuk setiap Rp10.000
        budi.tambahPoin(poinBaru);
        System.out.println("Budi belanja " + Rupiah.format(belanja) + ", dapat " + poinBaru
                + " poin");
        System.out.println(budi);
    }
}

/** Kelas utilitas untuk menampilkan uang. Isinya hanya method static. */
class Rupiah {

    /** Mengubah 18000 menjadi "Rp18.000". */
    static String format(int angka) {
        // Locale.US membuat pemisah ribuan selalu koma (18,000) di komputer mana
        // pun, apa pun pengaturan bahasanya. Setelah itu koma diganti titik.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Cetak biru untuk setiap menu di KedaiKita. */
class Menu {
    static int jumlahMenu = 0; // atribut KELAS: satu nilai untuk semua objek Menu

    String kode; // atribut OBJEK: tiap objek punya nilainya sendiri
    String nama;
    int harga;
    String kategori;
    int stok;

    Menu(String kode, String nama, int harga, String kategori, int stok) {
        this.kode = kode;
        this.nama = nama;
        this.harga = harga;
        this.kategori = kategori;
        this.stok = stok;
        Menu.jumlahMenu += 1; // setiap ada objek baru, penghitung bertambah
    }

    /** Konstruktor tanpa stok: stok bawaan 0 (padanan stok=0 di Python). */
    Menu(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0); // teruskan ke konstruktor lengkap
    }

    /** Teks yang muncul saat objek dicetak dengan System.out.println(). */
    @Override
    public String toString() {
        return "[" + kode + "] " + nama + " (" + kategori + ") - "
                + Rupiah.format(harga) + " | stok " + stok;
    }

    /** Total harga untuk sejumlah porsi. */
    int hitungTotal(int jumlah) {
        return harga * jumlah;
    }

    /** Harga setelah dipotong diskon sekian persen. */
    int hargaSetelahDiskon(int persen) {
        int potongan = harga * persen / 100;
        return harga - potongan;
    }

    /** true jika stok masih cukup untuk sejumlah porsi. */
    boolean stokCukup(int jumlah) {
        return stok >= jumlah;
    }
}

/** Data pelanggan KedaiKita beserta poin belanjanya. */
class Pelanggan {
    String nama;
    String noHp;
    int poin;

    Pelanggan(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = 0; // setiap pelanggan baru mulai dari 0 poin
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }

    void tambahPoin(int jumlah) {
        poin += jumlah;
    }
}
```

**Cara menjalankan.** Di VS Code, buka *file* `studi-kasus/KedaiKita.java`, lalu klik tulisan **Run** (bagian dari **Run | Debug**) di atas baris `public static void main`. Lewat terminal, ketik perintah berikut dari folder utama materi:

```bash
cd Pertemuan-03-Atribut-dan-Method/java/studi-kasus
java KedaiKita.java
```

Hasilnya harus sama persis dengan blok berikut.

***Output:***

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 0
Jumlah menu terdaftar: 4

=== CEK STOK ===
Pesan 2 Kopi Susu Gula Aren? Bisa
Pesan 1 Mie Goreng Jawa? Stok tidak cukup

=== PROMO HARI INI: DISKON 10% ===
Kopi Susu Gula Aren: Rp18.000 -> Rp16.200
Nasi Goreng Kampung: Rp25.000 -> Rp22.500

=== PELANGGAN ===
Budi Santoso (081234567890) - 0 poin
Budi belanja Rp44.000, dapat 4 poin
Budi Santoso (081234567890) - 4 poin
```

*Output* ini **sama persis** dengan *output* versi Python, sampai ke spasi terakhir.

Penjelasan per bagian:

- **`import java.util.Locale;`** ditulis di bagian paling atas *file*, sebelum kelas mana pun. Baris ini membuat kelas `Locale` dari pustaka standar Java bisa dipakai di *file* ini.
- **`Rupiah.format()`** memakai `String.format(Locale.US, "%,d", angka)`. Di dalam kode format `%,d`, huruf `d` berarti "tempat untuk bilangan bulat", dan tanda `,` berarti "sisipkan pemisah ribuan". Masalahnya, pemisah ribuan di Java mengikuti pengaturan bahasa (*locale*) komputer: di komputer berbahasa Indonesia hasilnya `18.000`, sedangkan di komputer berbahasa Inggris (AS) `18,000`. Agar hasilnya pasti, kita kunci ke `Locale.US` sehingga pemisahnya selalu koma (`18,000`). Setelah itu, `.replace(',', '.')` mengganti setiap koma dengan titik: `Rp18.000`. Hasilnya sama di komputer mana pun, dan langkahnya sama dengan versi Python (format dengan koma, lalu ganti dengan titik).
- **Dua konstruktor `Menu`**: konstruktor 4 parameter memanggil `this(kode, nama, harga, kategori, 0)`. Perhatikan bahwa `Menu.jumlahMenu += 1` hanya ada di konstruktor lengkap, jadi penghitung bertambah **tepat satu kali** untuk setiap menu, apa pun konstruktor yang dipakai. Itulah sebabnya hasilnya 4, bukan 5.
- **`toString()`** adalah satu-satunya *method* di `Menu` dan `Pelanggan` yang ditulis `public`. *Field* dan *method* lainnya sengaja belum diberi *access modifier*; topik itu dibahas di Pertemuan 04.
- **`hargaSetelahDiskon(10)`** menghitung potongan dengan `int`: `18000 * 10 / 100` = 1800 sehingga harga promonya 16200. Uang tidak pernah memakai bilangan desimal.
- **`stokCukup(jumlah)`** mengembalikan `boolean` dan langsung dipakai di `if`. Mie Goreng Jawa stoknya 0, jadi jawabannya "Stok tidak cukup".
- **`Menu[] menuPromo = {kopi, nasiGoreng};`** berisi referensi ke objek `kopi` dan `nasiGoreng` yang sama, bukan salinannya. Ini contoh *aliasing* yang bermanfaat.
- **`Pelanggan`** selalu mulai dengan `poin = 0`, nilai awal yang tidak berasal dari parameter. Belanja Budi Rp44.000 menghasilkan `44000 / 10000` = 4 poin.

Selamat! KedaiKita kini punya menu yang lengkap, penghitung menu, harga promo, dan pelanggan dengan poin belanja. Semua itu dibangun dengan konsep yang baru kamu pelajari hari ini.

> [!TIP]
> **Coba sendiri:** tambahkan menu kelima, M05 Pisang Goreng Keju seharga Rp15.000 (kategori Makanan), **tanpa** menyebut stok. Salin `studi-kasus/KedaiKita.java` ke folder `pertemuan-03` milikmu, buka salinannya, lalu di dalam `main`:
>
> 1. Tepat di bawah baris `Menu mieGoreng = ...`, tambahkan `Menu pisang = new Menu("M05", "Pisang Goreng Keju", 15000, "Makanan");`.
> 2. Tepat di bawah baris `System.out.println(mieGoreng);`, tambahkan `System.out.println(pisang);`.
>
> Simpan, jalankan salinan itu, lalu perhatikan bagian `=== MENU KEDAIKITA ===`. Apa yang tercetak?

<details>
<summary>Lihat jawaban</summary>

Bagian awal *output*-nya menjadi:

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 0
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 0
Jumlah menu terdaftar: 5
```

Konstruktor 4 parameter yang dipakai, lalu ia meneruskan ke konstruktor lengkap dengan stok 0. Penghitung bertambah tepat satu kali karena `Menu.jumlahMenu += 1` hanya ada di konstruktor lengkap. *File* studi kasus di folder materi tetap utuh karena yang kamu ubah hanya salinannya.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Sebagian besar kesalahan di pertemuan ini adalah ***error* saat kompilasi**: pesannya diawali nama *file* dan nomor baris, dan tanda `^` menunjuk posisi kesalahan. Jika kamu menjalankan dengan `java NamaFile.java`, pesan yang sama muncul dan diakhiri `error: compilation failed`.

Kode di bagian ini **sengaja dibuat salah** dan tidak ada di folder `contoh/`. Kesalahan 1 dan 2 berupa program utuh; sisanya hanya potongan. Pesan dan hasil yang ditampilkan diambil dari program kecil bernama `E1.java` sampai `E6.java`. Jika ingin mencobanya sendiri, kerjakan di folder `pertemuan-03` milikmu (lihat [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)). Program utuh disimpan sebagai `E1.java` atau `E2.java` (nama *file* harus sama dengan nama kelas `public`-nya), lalu dijalankan dengan `java E1.java`. Untuk potongan, salin *file* contoh yang disebut, lalu ubah salinannya. Nama *file* dan nomor baris di pesanmu bisa berbeda, tetapi isi *error*-nya sama.

### Kesalahan 1: Memanggil *method* objek dari `main` tanpa objek

```java
public class E1 {

    void sapa() {
        System.out.println("Halo!");
    }

    public static void main(String[] args) {
        sapa();
    }
}
```

```text
E1.java:8: error: non-static method sapa() cannot be referenced from a static context
        sapa();
        ^
1 error
```

**Artinya:** `main` adalah *method* `static` (tidak punya `this`), sedangkan `sapa()` adalah *method* objek yang butuh objek. Pesan yang sama muncul jika kamu memanggil *method* objek lewat nama kelas, misalnya `Tanggal.teks()`. **Perbaikan:** jadikan `sapa()` *method* `static` jika memang tidak butuh data objek, atau buat objeknya dulu: `new E1().sapa();`.

### Kesalahan 2: Memakai *field* objek dari `main`

```java
public class E2 {
    int jumlah = 0;

    public static void main(String[] args) {
        jumlah = 5;
        System.out.println(jumlah);
    }
}
```

```text
E2.java:5: error: non-static variable jumlah cannot be referenced from a static context
        jumlah = 5;
        ^
E2.java:6: error: non-static variable jumlah cannot be referenced from a static context
        System.out.println(jumlah);
                           ^
2 errors
```

**Artinya:** `jumlah` adalah *field* objek, jadi ia baru ada setelah objek `E2` dibuat. Dari `main` yang `static`, Java tidak tahu `jumlah` milik objek yang mana. **Perbaikan:** jika `jumlah` hanya dipakai di `main`, jadikan variabel lokal di dalam `main` (`int jumlah = 5;`). Jika memang milik bersama, tulis `static int jumlah = 0;`.

### Kesalahan 3: `toString()` tanpa `public`

Potongan dari kelas `Motor` (contoh 05) yang `toString()`-nya lupa diberi `public`:

```java
    @Override
    String toString() {
        return "Motor " + plat;
    }
```

```text
E3.java:15: error: toString() in Motor cannot override toString() in Object
    String toString() {
           ^
  attempting to assign weaker access privileges; was public
1 error
```

**Artinya:** `toString()` bawaan (milik kelas `Object`, "nenek moyang" semua kelas Java) bersifat `public`. *Method* yang menimpanya tidak boleh punya hak akses yang lebih sempit (*weaker access privileges*). **Perbaikan:** tulis `public String toString()`.

### Kesalahan 4: Salah ketik nama *method* yang di-*override*

Potongan dari kelas `Motor` yang sama, tetapi nama *method*-nya salah ketik:

```java
    @Override
    public String tostring() {   // huruf s seharusnya kapital
        return "Motor " + plat;
    }
```

```text
E4.java:14: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
```

**Artinya:** `@Override` berjanji bahwa *method* ini menimpa *method* bawaan, tetapi tidak ada *method* bawaan bernama `tostring` (yang ada `toString`). Inilah gunanya `@Override`: tanpa anotasi itu, kode tetap berjalan, tetapi diam-diam mencetak teks bawaan seperti `Motor@130f889`. **Perbaikan:** tulis tepat `toString`.

### Kesalahan 5: Dua konstruktor dengan tipe parameter yang sama

Potongan dari kelas `Laptop` (*field*-nya sama seperti contoh 04):

```java
    Laptop(String merek, int ram) {
        this.merek = merek;
        this.ram = ram;
    }

    Laptop(String merek, int penyimpanan) {
        this.merek = merek;
        this.penyimpanan = penyimpanan;
    }
```

```text
E5.java:17: error: constructor Laptop(String,int) is already defined in class Laptop
    Laptop(String merek, int penyimpanan) {
    ^
1 error
```

**Artinya:** bagi Java, kedua konstruktor sama-sama `Laptop(String,int)`. Nama parameter tidak dihitung, jadi Java tidak akan tahu konstruktor mana yang dimaksud oleh `new Laptop("Asus", 16)`. **Perbaikan:** bedakan jumlah atau tipe parameternya, atau gunakan konstruktor lengkap seperti di contoh 04.

### Kesalahan 6: Membandingkan `String` dengan `==`

Potongan isi *method* `main` (boleh ditempel di `main` salinan contoh mana pun):

```java
        String kategori = "M01;Minuman".split(";")[1];
        if (kategori == "Minuman") {
            System.out.println("== : kategori Minuman");
        } else {
            System.out.println("== : bukan Minuman?!");
        }
        if (kategori.equals("Minuman")) {
            System.out.println("equals: kategori Minuman");
        } else {
            System.out.println("equals: bukan Minuman");
        }
```

Tidak ada *error*, tetapi hasilnya:

```text
== : bukan Minuman?!
equals: kategori Minuman
```

**Artinya:** teks `"Minuman"` hasil `split()` adalah objek `String` baru, berbeda dengan objek `"Minuman"` yang ditulis langsung di kode. Operator `==` membandingkan **objeknya** sehingga hasilnya `false` walaupun isinya sama. Kesalahan ini licin karena kadang `==` kebetulan memberi hasil benar. **Perbaikan:** selalu bandingkan teks dengan `.equals()`.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Java. Fokuslah pada kata-kata kuncinya, misalnya `non-static`, `static context`, `override`, atau `already defined`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Atribut kelas | `static Tipe nama = nilai;` | `static int jumlahMenu = 0;` |
| Mengubah atribut kelas | `NamaKelas.field = ...;` | `Menu.jumlahMenu += 1;` |
| Konstanta milik kelas | `static final Tipe NAMA = nilai;` | `static final String[] NAMA_BULAN = {...};` |
| *Method* `static` | `static Tipe nama(...)` | `Tanggal.isKabisat(2024)` |
| Konstruktor alternatif | `static NamaKelas dariX(...)` | `Tanggal.dariTeks("17-08-1945")` |
| *Overloading* konstruktor | beberapa konstruktor, parameter berbeda | `Laptop(String)`, `Laptop(String, int)` |
| Memanggil konstruktor lain | `this(...);` (baris pertama) | `this(merek, 8, 512);` |
| Representasi teks | `@Override public String toString()` | `System.out.println(kopi);` |
| *Method boolean* | `boolean nama(...)` | `boolean stokCukup(int jumlah)` |
| Objek yang sama? | `a == b` | `ponselBudi == ponselDipinjam` |
| Isi teks sama? | `a.equals(b)` | `kategori.equals("Minuman")` |
| Tidak menunjuk objek | `null` | `if (ponsel == null)` |
| Objek sebagai parameter | `void f(NamaKelas lain)` | `dompetBudi.transfer(dompetSiti, 30000)` |
| Mengembalikan objek baru | `NamaKelas f(...) { return new NamaKelas(...); }` | `Durasi tambah(Durasi lain)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
