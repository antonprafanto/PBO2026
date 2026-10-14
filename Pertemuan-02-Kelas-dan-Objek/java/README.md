# ☕ Praktik Java Pertemuan 02: Kelas dan Objek

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 02](../README.md). Semua contoh dan studi kasus di halaman ini ada di folder `contoh/` dan `studi-kasus/`. Semuanya bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Kelas dan Objek Pertamamu](#1-kelas-dan-objek-pertamamu)
2. [Konstruktor](#2-konstruktor)
3. [*Method*: Memberi Objek Kemampuan](#3-method-memberi-objek-kemampuan)
4. [Parameter dan Nilai Kembalian](#4-parameter-dan-nilai-kembalian)
5. [Memahami `this`](#5-memahami-this)
6. [Setiap Objek Menyimpan Datanya Sendiri](#6-setiap-objek-menyimpan-datanya-sendiri)
7. [Banyak Objek dalam *Array*](#7-banyak-objek-dalam-array)
8. [Anatomi Kelas Java](#8-anatomi-kelas-java)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (17, 21, atau 25), VS Code dengan ekstensi **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh kecil, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 02
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah **program satu *file***: kelas yang memiliki `main` dan kelas pembantunya (misalnya `Kucing`) ditulis di dalam satu *file* `.java`.

> [!IMPORTANT]
> Di setiap *file* contoh, kelas yang memiliki *method* `main` ditulis **paling atas**, dan kelas pembantunya di bawahnya. Pada Java 11 sampai 21, urutan ini wajib agar perintah `java NamaFile.java` bisa berjalan. Java yang lebih baru sedikit lebih longgar, tetapi biasakan urutan ini agar programmu berjalan di semua versi.

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-02-Kelas-dan-Objek/java`. Di panel **Explorer** sebelah kiri, klik folder `contoh`, lalu klik *file* contoh yang ingin dicoba. Setelah *file* terbuka, klik **Run** pada tulisan **Run | Debug** yang muncul tepat di atas baris `public static void main` (atau tombol ▷ di pojok kanan atas). Hasilnya muncul di panel **TERMINAL** di bagian bawah. Baris pertama di panel itu berisi perintah panjang yang diketik VS Code secara otomatis; *output* programmu muncul di bawahnya. Jika tulisan **Run | Debug** belum muncul, tunggu beberapa detik sampai ekstensi Java selesai memuat folder itu.

Kenapa harus folder `java` milik pertemuan ini, bukan seluruh folder materi? Ekstensi Java menganggap semua *file* `.java` di dalam folder yang dibuka sebagai **satu proyek**. Padahal, hampir setiap pertemuan punya kelas bernama sama (misalnya `Menu`), dan dua kelas bernama sama tidak boleh berada dalam satu proyek. Jika seluruh materi dibuka, VS Code akan protes dengan pesan *The type Menu is already defined*. Di dalam satu folder `java` pertemuan, setiap nama kelas sudah dibuat unik.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-02-Kelas-dan-Objek/java/contoh` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
java Contoh01KelasDanObjek.java
```

Perintah ini (Java 11 ke atas) mengompilasi *file* di memori, lalu langsung menjalankannya, jadi tidak ada *file* `.class` yang tertinggal. Belum yakin sudah berada di folder yang benar? Ketik `dir` (Windows) atau `ls` (macOS/Linux). Jika nama *file* yang ingin dijalankan muncul di daftar, kamu sudah di tempat yang tepat. *File* di folder `studi-kasus` dan `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan nama folder itu.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Perintah `java` sama di Windows, macOS, dan Linux. Cara klasik dua langkah (`javac Contoh01KelasDanObjek.java` lalu `java Contoh01KelasDanObjek`) juga tetap bisa dipakai; penjelasannya ada di [Menjalankan Program](../../00-Persiapan/menjalankan-program.md).

### Tempat Menyimpan Kodemu Sendiri

Simpan semua kode buatanmu (hasil mengetik ulang, percobaan "Coba sendiri", *file* coretan seperti `Coba.java`, dan jawaban latihan) di folder `PBO-latihan-saya/pertemuan-02/`, **di luar** folder materi; untuk Java, pakai satu subfolder untuk setiap pertemuan agar nama kelas tidak bentrok. Jika sebuah percobaan memintamu mengubah *file* contoh, salin dulu *file* itu ke folder tersebut tanpa mengganti namanya (nama *file* Java harus sama dengan nama kelas `public`-nya), lalu ubah dan jalankan salinannya. Untuk menjalankan salinan itu, buka folder tersebut di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**) atau arahkan terminal ke sana dengan `cd`. Alasan dan cara menyalinnya ada di [aturan emas 00-Persiapan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Setiap bagian diawali baris ***File*:** atau **Potongan dari** yang menautkan *file* contohnya.
- ***File*:** berarti kode di bawahnya adalah isi lengkap *file* itu, hanya tanpa komentar pembuka, termasuk kelas yang memiliki `main`. Hasil ketik ulangnya bisa langsung dijalankan.
- **Potongan dari** berarti yang ditampilkan hanya sebagian. Potongan dari dalam *method* `main` tampil menjorok 8 spasi karena aslinya berada di dalam kelas dan di dalam `main`. Jangan mengetik ulang potongannya saja; jalankan *file* lengkapnya dengan cara di atas.
- Tanda `// [1]`, `// [2]`, dan seterusnya di dalam kode dijelaskan satu per satu tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.

## 1. Kelas dan Objek Pertamamu

*File*: [`contoh/Contoh01KelasDanObjek.java`](contoh/Contoh01KelasDanObjek.java)

Kita mulai dari kelas yang paling sederhana: kelas `Kucing`. Berikut isi lengkap *file*-nya, hanya tanpa komentar pembuka:

```java
public class Contoh01KelasDanObjek {

    public static void main(String[] args) {
        Kucing oyen = new Kucing(); // [2] membuat objek pertama dari kelas Kucing
        oyen.nama = "Oyen";         // [3] mengisi atribut milik objek oyen
        oyen.warna = "oranye";

        Kucing belang = new Kucing(); // objek kedua dari kelas yang SAMA
        belang.nama = "Belang";
        belang.warna = "hitam putih";

        System.out.println("=== DUA OBJEK DARI SATU KELAS ===");
        System.out.println("Kucing pertama: " + oyen.nama + ", warnanya " + oyen.warna); // [4]
        System.out.println("Kucing kedua  : " + belang.nama + ", warnanya " + belang.warna);
        System.out.println("oyen dibuat dari kelas  : " + oyen.getClass().getSimpleName()); // [5]
        System.out.println("belang dibuat dari kelas: " + belang.getClass().getSimpleName());
        if (oyen == belang) { // [6] apakah keduanya objek yang sama?
            System.out.println("oyen dan belang adalah objek yang sama");
        } else {
            System.out.println("oyen dan belang adalah dua objek yang berbeda");
        }
    }
}

/** Cetak biru untuk semua kucing. */
class Kucing { // [1] mendefinisikan kelas bernama Kucing
    String nama;  // atribut (field) dideklarasikan lengkap dengan tipenya
    String warna;
}
```

***Output:***

```text
=== DUA OBJEK DARI SATU KELAS ===
Kucing pertama: Oyen, warnanya oranye
Kucing kedua  : Belang, warnanya hitam putih
oyen dibuat dari kelas  : Kucing
belang dibuat dari kelas: Kucing
oyen dan belang adalah dua objek yang berbeda
```

Penjelasan:

- **[1]** Kata kunci `class` diikuti nama kelas dan badan kelas di dalam kurung kurawal `{ }`. Di Java, atribut (disebut juga ***field***) **wajib dideklarasikan** di badan kelas, lengkap dengan tipenya (`String nama;`).
- **[2]** `new Kucing()` **membuat objek baru**. Kata kunci `new` wajib ditulis. Tipe variabelnya adalah nama kelas itu sendiri: `Kucing oyen`.
- **[3]** Notasi titik `oyen.nama = "Oyen"` mengisi *field* `nama` **milik objek oyen**.
- **[4]** `oyen.nama` membaca *field* milik oyen. Ucapkan dalam hati: "nama milik oyen".
- **[5]** `getClass().getSimpleName()` memberi tahu nama kelas asal objek.
- **[6]** Operator `==` pada objek memeriksa apakah dua variabel menunjuk ke **objek yang sama**. Hasilnya tidak karena `new` dipanggil dua kali sehingga tercipta dua objek berbeda.
- Kelas `Contoh01KelasDanObjek` hanyalah wadah untuk *method* `main`, pintu masuk program, seperti di Pertemuan 01. Kelas yang sedang kita pelajari adalah `Kucing`.

> [!NOTE]
> *Field* yang belum diisi otomatis mendapat **nilai bawaan**: `null` untuk objek seperti `String`, `0` untuk `int`, dan `false` untuk `boolean`.

> [!TIP]
> **Coba sendiri:** salin `Contoh01KelasDanObjek.java` ke folder `PBO-latihan-saya/pertemuan-02/`. Di salinan itu, hapus baris `belang.warna = "hitam putih";`, simpan, lalu jalankan. Apa yang berubah? Bandingkan dengan hasil di bawah.

<details>
<summary>Lihat hasilnya</summary>

Program tetap berjalan sampai selesai, tetapi baris ketiga *output*-nya menjadi:

```text
Kucing kedua  : Belang, warnanya null
```

*Field* `warna` milik `belang` tidak pernah diisi, jadi berisi nilai bawaan `null`. Inilah masalah "objek setengah jadi" yang dibahas di halaman konsep. Konstruktor di bagian berikutnya mencegah masalah ini.

</details>

## 2. Konstruktor

Potongan dari [`contoh/Contoh02Konstruktor.java`](contoh/Contoh02Konstruktor.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Konstruktor di Java punya dua ciri khas: **namanya sama persis dengan nama kelas** dan **tidak punya tipe kembalian** (bahkan tidak `void`). Konstruktor dipanggil otomatis setiap kali objek dibuat dengan `new`. Bentuknya memang mirip *method*, tetapi secara resmi Java tidak menggolongkannya sebagai *method*.

Potongan pertama: kelas `Mobil` dari bagian bawah *file*.

```java
/** Cetak biru mobil: setiap mobil punya merek, warna, dan tahun. */
class Mobil {
    String merek;
    String warna;
    int tahun;

    Mobil(String merek, String warna, int tahun) { // [1] konstruktor
        System.out.println("  (konstruktor dipanggil untuk mobil " + merek + ")"); // [2]
        this.merek = merek; // [3] simpan parameter ke atribut objek
        this.warna = warna;
        this.tahun = tahun;
    }
}
```

Potongan kedua: awal *method* `main` di *file* yang sama. Sisanya mencetak data setiap mobil.

```java
        System.out.println("=== MEMBUAT TIGA OBJEK MOBIL ===");
        Mobil mobilBudi = new Mobil("Avanza", "hitam", 2019); // [4] argumen dikirim ke konstruktor
        Mobil mobilSiti = new Mobil("Brio", "merah", 2022);
        Mobil mobilRina = new Mobil("Xpander", "putih", 2021);
```

***Output:***

```text
=== MEMBUAT TIGA OBJEK MOBIL ===
  (konstruktor dipanggil untuk mobil Avanza)
  (konstruktor dipanggil untuk mobil Brio)
  (konstruktor dipanggil untuk mobil Xpander)

=== DATA SETIAP MOBIL ===
Mobil Budi: Avanza hitam (2019)
Mobil Siti: Brio merah (2022)
Mobil Rina: Xpander putih (2021)
```

Penjelasan:

- **[1]** Konstruktor `Mobil(...)` menerima tiga parameter. Perhatikan: tidak ada `void` atau tipe apa pun di depannya.
- **[2]** Baris ini sengaja ditambahkan untuk **membuktikan** bahwa konstruktor berjalan sendiri setiap kali `new Mobil(...)` dieksekusi.
- **[3]** `this.merek = merek` berarti: "*field* `merek` milik objek ini diisi dengan nilai parameter `merek`". Karena nama parameter dan nama *field* sama, `this.` wajib ditulis untuk membedakan keduanya.
- **[4]** `new Mobil("Avanza", "hitam", 2019)` membuat objek baru, lalu menjalankan konstruktor dengan argumen tersebut. Urutan dan tipe argumen harus cocok dengan parameter: `String`, `String`, `int`.

Urutan pengiriman argumen ke parameter terlihat seperti ini. Argumen pertama masuk ke parameter pertama, argumen kedua ke parameter kedua, dan seterusnya:

```text
new Mobil(      "Avanza",     "hitam",     2019)
                   |             |          |
                   v             v          v
    Mobil(String merek, String warna, int tahun)
```

Spasi tambahan setelah `new Mobil(` hanya agar panahnya lurus. Di kode sungguhan, tulis saja `new Mobil("Avanza", "hitam", 2019)`.

> [!NOTE]
> Jika sebuah kelas tidak menulis konstruktor sama sekali (seperti `Kucing` di contoh 01), Java otomatis menyediakan **konstruktor bawaan** tanpa parameter. Begitu kita menulis konstruktor sendiri, konstruktor bawaan itu tidak lagi disediakan.

## 3. *Method*: Memberi Objek Kemampuan

Potongan dari [`contoh/Contoh03Method.java`](contoh/Contoh03Method.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Method* ditulis di dalam kelas dengan format: **tipe kembalian, nama *method*, lalu parameter**. *Method* yang tidak mengembalikan nilai memakai tipe `void`.

Potongan pertama: kelas `Lampu` dari bagian bawah *file*.

```java
/** Lampu yang bisa dinyalakan dan dimatikan. */
class Lampu {
    String ruangan;
    boolean menyala;

    Lampu(String ruangan) {
        this.ruangan = ruangan;
        this.menyala = false; // [1] nilai awal tidak harus dari parameter
    }

    void nyalakan() { // [2] method yang mengubah atribut
        menyala = true;
        System.out.println("Lampu " + ruangan + " dinyalakan");
    }

    void matikan() {
        menyala = false;
        System.out.println("Lampu " + ruangan + " dimatikan");
    }

    void tampilkanStatus() { // [3] method yang hanya membaca atribut
        if (menyala) {
            System.out.println("Status lampu " + ruangan + ": MENYALA");
        } else {
            System.out.println("Status lampu " + ruangan + ": PADAM");
        }
    }
}
```

Potongan kedua: isi *method* `main` di *file* yang sama.

```java
        Lampu lampuKamar = new Lampu("kamar");
        Lampu lampuDapur = new Lampu("dapur");

        System.out.println("=== KONDISI AWAL ===");
        lampuKamar.tampilkanStatus(); // [4] memanggil method
        lampuDapur.tampilkanStatus();

        System.out.println();
        System.out.println("=== SETELAH DIOPERASIKAN ===");
        lampuKamar.nyalakan();
        lampuKamar.tampilkanStatus();
        lampuDapur.tampilkanStatus(); // lampu dapur tidak terpengaruh
        lampuKamar.matikan();
        lampuKamar.tampilkanStatus();
```

***Output:***

```text
=== KONDISI AWAL ===
Status lampu kamar: PADAM
Status lampu dapur: PADAM

=== SETELAH DIOPERASIKAN ===
Lampu kamar dinyalakan
Status lampu kamar: MENYALA
Status lampu dapur: PADAM
Lampu kamar dimatikan
Status lampu kamar: PADAM
```

Penjelasan:

- **[1]** Tidak semua *field* harus berasal dari parameter. Setiap lampu baru otomatis dalam keadaan padam.
- **[2]** *Method* `nyalakan()` **mengubah keadaan** (*state*) objek. Di dalam *method*, kita boleh langsung menulis `menyala` tanpa `this.` karena tidak ada parameter bernama sama. Java otomatis mengartikannya sebagai `this.menyala`.
- **[3]** *Method* `tampilkanStatus()` hanya **membaca** *field*.
- **[4]** *Method* dipanggil dengan notasi titik. Objek di sebelah kiri titik menjadi `this` di dalam *method*.

> [!NOTE]
> Nama *method* di Java memakai gaya ***camelCase***: kata pertama huruf kecil, kata berikutnya diawali huruf kapital (`tampilkanStatus`, `hitungLuas`). Nama kelas memakai ***PascalCase*** (`Lampu`, `PersegiPanjang`).

> [!TIP]
> **Coba sendiri:** salin `Contoh03Method.java` ke folder `PBO-latihan-saya/pertemuan-02/`. Di salinan itu, tambahkan *method* `saklar()` di dalam kelas `Lampu` yang membalik keadaan lampu (menyala menjadi padam, padam menjadi menyala). Petunjuk: `menyala = !menyala;`. Lalu, di akhir `main`, panggil `lampuDapur.saklar();` dan `lampuDapur.tampilkanStatus();`. Simpan, jalankan, lalu bandingkan baris terakhir *output*-nya dengan jawaban di bawah.

<details>
<summary>Lihat jawaban</summary>

Tambahkan *method* ini di dalam kelas `Lampu`, sejajar dengan `matikan()`:

```java
    void saklar() {
        menyala = !menyala;
    }
```

Lalu tambahkan dua baris ini di akhir `main`:

```java
        lampuDapur.saklar();
        lampuDapur.tampilkanStatus();
```

Baris terakhir *output*-nya menjadi `Status lampu dapur: MENYALA` karena lampu dapur yang tadinya padam kini dibalik menjadi menyala.

</details>

## 4. Parameter dan Nilai Kembalian

Potongan dari [`contoh/Contoh04ParameterDanReturn.java`](contoh/Contoh04ParameterDanReturn.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Method* bisa menerima parameter dan bisa **mengembalikan** hasil dengan `return`. Potongan pertama: kelas `PersegiPanjang` dari bagian bawah *file*.

```java
/** Bangun datar persegi panjang dengan panjang dan lebar (cm). */
class PersegiPanjang {
    int panjang;
    int lebar;

    PersegiPanjang(int panjang, int lebar) {
        this.panjang = panjang;
        this.lebar = lebar;
    }

    int hitungLuas() { // [1] tipe kembalian int
        return panjang * lebar;
    }

    int hitungKeliling() {
        return 2 * (panjang + lebar);
    }

    void perbesar(int faktor) { // [2] menerima parameter dan mengubah atribut
        panjang = panjang * faktor;
        lebar = lebar * faktor;
    }
}
```

Potongan kedua: isi *method* `main` di *file* yang sama.

```java
        PersegiPanjang meja = new PersegiPanjang(120, 60);
        int luas = meja.hitungLuas(); // [3] hasil return disimpan ke variabel
        System.out.println("=== MEJA BELAJAR ===");
        System.out.println("Ukuran   : " + meja.panjang + " x " + meja.lebar + " cm");
        System.out.println("Luas     : " + luas + " cm2");
        System.out.println("Keliling : " + meja.hitungKeliling() + " cm"); // [4] langsung dipakai

        System.out.println();
        meja.perbesar(2); // [5] mengirim argumen ke parameter faktor
        System.out.println("=== SETELAH DIPERBESAR 2 KALI ===");
        System.out.println("Ukuran   : " + meja.panjang + " x " + meja.lebar + " cm");
        System.out.println("Luas     : " + meja.hitungLuas() + " cm2");
        System.out.println("Luas naik " + (meja.hitungLuas() / luas) + " kali lipat");
```

***Output:***

```text
=== MEJA BELAJAR ===
Ukuran   : 120 x 60 cm
Luas     : 7200 cm2
Keliling : 360 cm

=== SETELAH DIPERBESAR 2 KALI ===
Ukuran   : 240 x 120 cm
Luas     : 28800 cm2
Luas naik 4 kali lipat
```

Penjelasan:

- **[1]** `int` di depan nama *method* adalah **tipe kembalian**. Java memeriksa bahwa nilai yang di-`return` memang bertipe `int`.
- **[2]** Parameter ditulis lengkap dengan tipenya: `int faktor`. *Method* ini bertipe `void` karena tidak mengembalikan apa pun.
- **[3]** Nilai kembalian disimpan ke variabel `luas`. Tipe variabel itu harus cocok dengan tipe kembaliannya (`int`).
- **[4]** Nilai kembalian juga bisa langsung dipakai dalam ekspresi.
- **[5]** Argumen `2` dikirim ke parameter `faktor`.

> [!IMPORTANT]
> Bedakan **mencetak** (`System.out.println`) dengan **mengembalikan** (`return`). *Method* yang mengembalikan nilai lebih fleksibel: hasilnya bisa dicetak, dijumlahkan, dibandingkan, atau disimpan.

> [!WARNING]
> Hati-hati saat menggabungkan teks dengan **penjumlahan**. `"Total: Rp" + 36000 + 25000` menghasilkan `Total: Rp3600025000` karena Java menggabungkan dari kiri ke kanan: teks + angka menjadi teks, lalu ditambah angka lagi menjadi teks lagi. Bungkus penjumlahannya dengan kurung: `"Total: Rp" + (36000 + 25000)`. Perkalian dan pembagian tidak bermasalah karena selalu dikerjakan lebih dulu, tetapi menambahkan kurung tetap membuat kode lebih mudah dibaca.

## 5. Memahami `this`

Potongan dari [`contoh/Contoh05This.java`](contoh/Contoh05This.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Contoh ini menunjukkan tiga peran `this` sekaligus. Potongan pertama: kelas `Akun` dari bagian bawah *file*.

```java
/** Akun aplikasi dengan username dan email. */
class Akun {
    String username;
    String email;

    Akun(String username, String email) {
        this.username = username;
        this.email = email;
    }

    void gantiEmail(String email) {
        // [1] this.email = atribut milik objek, email = parameter yang baru diterima
        System.out.println(username + ": email " + this.email + " diganti ke " + email);
        this.email = email;
    }

    String sapa() {
        return "Halo, " + username + "!";
    }

    void tampilkanProfil() {
        System.out.println(this.sapa()); // [2] memanggil method lain milik objek yang sama
        System.out.println("  Email terdaftar: " + email);
    }
}
```

Potongan kedua: isi *method* `main` di *file* yang sama.

```java
        Akun akunBudi = new Akun("budi_s", "budi@contoh.id");
        Akun akunSiti = new Akun("siti_a", "siti@contoh.id");

        System.out.println("=== PROFIL AWAL ===");
        akunBudi.tampilkanProfil(); // [3] di dalam method, this = akunBudi
        akunSiti.tampilkanProfil(); //     di dalam method, this = akunSiti

        System.out.println();
        System.out.println("=== BUDI MENGGANTI EMAIL ===");
        akunBudi.gantiEmail("budi.santoso@contoh.id");
        akunBudi.tampilkanProfil();
        akunSiti.tampilkanProfil(); // email Siti tidak ikut berubah
```

***Output:***

```text
=== PROFIL AWAL ===
Halo, budi_s!
  Email terdaftar: budi@contoh.id
Halo, siti_a!
  Email terdaftar: siti@contoh.id

=== BUDI MENGGANTI EMAIL ===
budi_s: email budi@contoh.id diganti ke budi.santoso@contoh.id
Halo, budi_s!
  Email terdaftar: budi.santoso@contoh.id
Halo, siti_a!
  Email terdaftar: siti@contoh.id
```

Penjelasan:

- **[1]** Di dalam `gantiEmail`, nama `email` merujuk ke **parameter** (*email* baru) karena parameter "menutupi" *field* yang bernama sama. Peristiwa ini disebut *shadowing*. Untuk menyebut *field*-nya, kita wajib menulis `this.email`.
- **[2]** *Method* boleh memanggil *method* lain milik objek yang sama. `this.sapa()` dan `sapa()` sama artinya.
- **[3]** *Method* `tampilkanProfil` ditulis sekali, tetapi dijalankan dengan `this` yang berbeda sehingga hasilnya berbeda.

| Kapan `this.` wajib? | Contoh |
|---|---|
| Nama parameter sama dengan nama *field* | `this.email = email;` |
| Tidak ada nama yang bentrok | boleh ditulis atau tidak: `this.sapa()` sama dengan `sapa()` |

## 6. Setiap Objek Menyimpan Datanya Sendiri

Potongan dari [`contoh/Contoh06ObjekMandiri.java`](contoh/Contoh06ObjekMandiri.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Kali ini potongan yang ditampilkan hanya kelas `RekeningBank` dari bagian bawah *file*:

```java
/** Rekening tabungan sederhana. */
class RekeningBank {
    String pemilik;
    int saldo;

    RekeningBank(String pemilik, int saldoAwal) {
        this.pemilik = pemilik;
        this.saldo = saldoAwal;
    }

    void setor(int jumlah) {
        saldo = saldo + jumlah;
        System.out.println(pemilik + " setor Rp" + jumlah);
    }

    void tarik(int jumlah) {
        if (jumlah > saldo) {
            System.out.println(pemilik + " gagal tarik Rp" + jumlah + ": saldo tidak cukup");
        } else {
            saldo = saldo - jumlah;
            System.out.println(pemilik + " tarik Rp" + jumlah);
        }
    }

    void cekSaldo() {
        System.out.println("  Saldo " + pemilik + ": Rp" + saldo);
    }
}
```

*Method* `main` di *file* yang sama membuat rekening Budi (saldo awal Rp500.000) dan Siti (saldo awal Rp750.000), lalu melakukan beberapa transaksi.

***Output:***

```text
=== SALDO AWAL ===
  Saldo Budi: Rp500000
  Saldo Siti: Rp750000

=== TRANSAKSI ===
Budi setor Rp200000
Budi gagal tarik Rp1000000: saldo tidak cukup
Siti tarik Rp250000

=== SALDO AKHIR ===
  Saldo Budi: Rp700000
  Saldo Siti: Rp500000
```

Transaksi pada rekening Budi tidak menyentuh saldo Siti sama sekali. *Method* `tarik` juga **menjaga** agar saldo tidak menjadi negatif. Menjaga data agar tetap masuk akal adalah tugas penting sebuah kelas. Di Pertemuan 04 (Enkapsulasi), kita akan belajar cara menjaga data dengan lebih ketat.

## 7. Banyak Objek dalam *Array*

Potongan dari [`contoh/Contoh07DaftarObjek.java`](contoh/Contoh07DaftarObjek.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Objek bisa disimpan di dalam *array*. Tipe *array*-nya adalah nama kelas diikuti `[]`.

Potongan pertama: kelas `Lagu` dari bagian bawah *file*.

```java
/** Satu lagu di playlist. */
class Lagu {
    String judul;
    String penyanyi;
    int durasiDetik;

    Lagu(String judul, String penyanyi, int durasiDetik) {
        this.judul = judul;
        this.penyanyi = penyanyi;
        this.durasiDetik = durasiDetik;
    }

    String durasiTeks() {
        int menit = durasiDetik / 60;
        int detik = durasiDetik % 60;
        return menit + ":" + String.format("%02d", detik);
    }

    void tampilkan() {
        System.out.println("- " + judul + " (" + penyanyi + ") " + durasiTeks());
    }
}
```

Potongan kedua: isi *method* `main` di *file* yang sama.

```java
        Lagu[] playlist = { // [1] array berisi tiga objek Lagu
            new Lagu("Indonesia Pusaka", "Ismail Marzuki", 215),
            new Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132),
            new Lagu("Bengawan Solo", "Gesang", 187)
        };

        System.out.println("=== PLAYLIST BELAJAR ===");
        int total = 0;
        for (Lagu lagu : playlist) { // [2] variabel lagu bergantian menunjuk tiap objek
            lagu.tampilkan();
            total = total + lagu.durasiDetik;
        }
        System.out.println("Jumlah lagu : " + playlist.length);
        System.out.println("Total durasi: " + (total / 60) + " menit " + (total % 60) + " detik");
```

***Output:***

```text
=== PLAYLIST BELAJAR ===
- Indonesia Pusaka (Ismail Marzuki) 3:35
- Ampar-Ampar Pisang (Lagu Daerah Kalimantan Selatan) 2:12
- Bengawan Solo (Gesang) 3:07
Jumlah lagu : 3
Total durasi: 8 menit 54 detik
```

Penjelasan:

- **[1]** `Lagu[]` adalah *array* yang setiap elemennya bertipe `Lagu`. Objek dibuat langsung di dalam kurung kurawal.
- **[2]** Perulangan *for-each* (`for (Lagu lagu : playlist)`) membaca elemen satu per satu. *Method* yang sama dipanggil untuk setiap objek.
- Kelas `Lagu` menyimpan durasi dalam detik. *Method* `durasiTeks()` mengubahnya menjadi teks berformat menit:detik. Di sana, `/` pada dua `int` adalah pembagian bulat dan `%` adalah sisa bagi. `String.format("%02d", detik)` berarti "tulis `detik` dua digit, tambahkan nol di depan bila perlu". Karena itu, 187 detik tercetak `3:07`, bukan `3:7`.

> [!NOTE]
> Ukuran *array* tetap (tidak bisa ditambah setelah dibuat). Wadah yang ukurannya bisa bertambah, yaitu `ArrayList`, kita pakai mulai Pertemuan 05.

## 8. Anatomi Kelas Java

Berikut rangkuman bagian-bagian sebuah kelas Java. Ini gambaran ringkas, bukan *file* untuk dijalankan; dalam program sungguhan, dua baris terakhir ditulis di dalam *method* `main`. Simpan gambar ini di kepala.

```text
class Menu {                           <- kata kunci class + nama kelas (PascalCase)
    String nama;                       <- field: tipe + nama, wajib dideklarasikan
    int harga;

    Menu(String nama, int harga) {     <- konstruktor: nama = nama kelas, tanpa tipe kembalian
        this.nama = nama;              <- this.field = parameter
        this.harga = harga;
    }

    int hitungTotal(int jumlah) {      <- method: tipe kembalian + nama (camelCase) + parameter
        return harga * jumlah;
    }
}

Menu kopi = new Menu("Kopi", 18000);   <- membuat objek dengan new
int total = kopi.hitungTotal(2);       <- memanggil method dengan notasi titik
```

## 9. Studi Kasus KedaiKita

*File*: [`studi-kasus/KedaiKita.java`](studi-kasus/KedaiKita.java)

Saatnya membangun KedaiKita versi pertama yang memakai kelas. Rancangannya sudah kita bahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-kelas-menu-pertama).

**Apa yang berubah dibanding Pertemuan 01?**

- Data menu tidak lagi disimpan di tiga *array* terpisah, tetapi di dalam objek `Menu`.
- Perhitungan total tidak lagi memakai *method* `static` yang lepas, tetapi *method* `hitungTotal()` milik setiap menu.

Berikut isi lengkap *file*-nya, hanya tanpa komentar pembuka:

```java
public class KedaiKita {

    public static void main(String[] args) {
        System.out.println("=== MENU KEDAIKITA ===");
        Menu kopi = new Menu("Kopi Susu Gula Aren", 18000); // [5] membuat objek
        Menu esTeh = new Menu("Es Teh Manis", 8000);
        Menu nasiGoreng = new Menu("Nasi Goreng Kampung", 25000);

        kopi.tampilkanInfo(); // [6] memanggil method milik objek
        esTeh.tampilkanInfo();
        nasiGoreng.tampilkanInfo();

        System.out.println();
        System.out.println("=== PESANAN BUDI ===");
        int totalKopi = kopi.hitungTotal(2);
        int totalNasi = nasiGoreng.hitungTotal(1);
        System.out.println("2 x " + kopi.nama + " = Rp" + totalKopi); // [7] membaca atribut objek
        System.out.println("1 x " + nasiGoreng.nama + " = Rp" + totalNasi);
        System.out.println("Total bayar: Rp" + (totalKopi + totalNasi));

        System.out.println();
        System.out.println("=== HARGA ES TEH NAIK ===");
        esTeh.harga = 10000; // [8] mengubah atribut satu objek
        esTeh.tampilkanInfo();
        kopi.tampilkanInfo(); // objek lain tidak ikut berubah
    }
}

/** Cetak biru untuk setiap menu di KedaiKita. */
class Menu {
    String nama; // [2] atribut (field) milik objek
    int harga;

    Menu(String nama, int harga) { // [1] konstruktor: dipanggil saat objek dibuat
        this.nama = nama;
        this.harga = harga;
    }

    void tampilkanInfo() { // [3] method: perilaku objek
        System.out.println(nama + " - Rp" + harga);
    }

    int hitungTotal(int jumlah) { // [4] method yang mengembalikan nilai
        return harga * jumlah;
    }
}
```

Cara menjalankan: buka *file* `studi-kasus/KedaiKita.java` di VS Code, lalu klik **Run** pada tulisan **Run | Debug** di atas baris `public static void main`. Lewat terminal, ketik perintah berikut dari folder utama materi:

```bash
cd Pertemuan-02-Kelas-dan-Objek/java/studi-kasus
java KedaiKita.java
```

***Output:***

```text
=== MENU KEDAIKITA ===
Kopi Susu Gula Aren - Rp18000
Es Teh Manis - Rp8000
Nasi Goreng Kampung - Rp25000

=== PESANAN BUDI ===
2 x Kopi Susu Gula Aren = Rp36000
1 x Nasi Goreng Kampung = Rp25000
Total bayar: Rp61000

=== HARGA ES TEH NAIK ===
Es Teh Manis - Rp10000
Kopi Susu Gula Aren - Rp18000
```

Penjelasan:

- **[1]** Konstruktor menerima `nama` dan `harga` sehingga tidak ada menu yang lahir tanpa nama atau harga.
- **[2]** *Field* `nama` dan `harga` dideklarasikan di badan kelas beserta tipenya.
- **[3]** `tampilkanInfo()` bertipe `void`: ia mencetak, tetapi tidak mengembalikan apa pun.
- **[4]** `hitungTotal(int jumlah)` bertipe `int`: hasilnya bisa dijumlahkan di program utama.
- **[5]** Tiga objek dibuat dari satu kelas dengan `new`.
- **[6]** *Method* yang sama menghasilkan teks berbeda karena `this`-nya berbeda.
- **[7]** *Field* `nama` dibaca langsung dengan notasi titik.
- **[8]** Hanya harga es teh yang berubah. Objek kopi tidak terpengaruh.

> [!NOTE]
> Di *file* ini, kelas `KedaiKita` ditulis lebih dulu karena memiliki `main`, lalu kelas `Menu` di bawahnya. Kelas `Menu` tidak diberi kata `public` karena dalam satu *file* Java hanya boleh ada **satu** kelas `public`, dan namanya harus sama dengan nama *file*. Mulai Pertemuan 05, setiap kelas akan punya *file* sendiri.

> [!TIP]
> **Coba sendiri:** salin `studi-kasus/KedaiKita.java` ke folder `PBO-latihan-saya/pertemuan-02/`. Di akhir *method* `main` salinan itu, buat menu keempat, `Mie Goreng Jawa` seharga `23000`, lalu hitung dan cetak total pesanan Siti: 1 mie goreng dan 2 es teh (dengan harga es teh yang sudah naik). Simpan, lalu jalankan. Berapa total yang harus Siti bayar? Bandingkan dengan jawaban di bawah.

<details>
<summary>Lihat jawaban</summary>

Totalnya 1 x 23.000 + 2 x 10.000 = Rp43.000. Salah satu cara menulisnya, ditambahkan di akhir `main`:

```java
        Menu mieGoreng = new Menu("Mie Goreng Jawa", 23000);
        int totalSiti = mieGoreng.hitungTotal(1) + esTeh.hitungTotal(2);
        System.out.println("Total bayar Siti: Rp" + totalSiti);
```

Baris terakhir yang tercetak: `Total bayar Siti: Rp43000`. Perhatikan bahwa penjumlahannya dihitung dulu di baris kedua, jadi tidak terkena jebakan penggabungan teks di bagian 4.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Java punya dua jenis kesalahan:

- ***Error* saat kompilasi** (*compile error*): ditemukan sebelum program berjalan. Pesannya diawali nama *file* dan nomor baris, misalnya `E1.java:3: error: ...`. Tanda `^` menunjuk posisi kesalahannya.
- ***Error* saat program berjalan** (*runtime error*): program sempat berjalan lalu berhenti. Pesannya diawali `Exception in thread "main"`.

Setiap kesalahan di bawah ini ditampilkan dalam dua blok: potongan kode yang salah (jangan ditiru) dan pesan yang muncul. Pesan-pesan itu didapat dari *file* uji kecil bernama `E1.java`, `E2.java`, dan seterusnya, yang dijalankan dengan `java E1.java`. Ingin mencobanya sendiri? Salin *file* contoh atau studi kasus yang relevan ke folder `PBO-latihan-saya/pertemuan-02/` (jangan mengubah *file* di folder materi), buat kesalahan yang sama di salinannya, lalu jalankan. Nama *file* dan nomor baris di pesanmu akan berbeda, tetapi bentuk pesannya sama. Jika memakai `javac`, baris terakhir `error: compilation failed` tidak muncul.

### Kesalahan 1: Lupa menulis `new`

Potongan kode yang salah:

```java
        Kucing oyen = Kucing();
```

Pesan *error*-nya:

```text
E1.java:3: error: cannot find symbol
        Kucing oyen = Kucing();
                      ^
  symbol:   method Kucing()
  location: class E1
1 error
error: compilation failed
```

**Artinya:** tanpa `new`, Java mengira `Kucing()` adalah pemanggilan ***method*** bernama `Kucing`, dan *method* itu tidak ada (*cannot find symbol*). **Perbaikan:** `Kucing oyen = new Kucing();`.

### Kesalahan 2: Memberi tipe kembalian pada konstruktor

Potongan kode yang salah:

```java
class Mobil {
    // ...
    void Mobil(String merek, String warna, int tahun) { // salah: ada void
        // ...
    }
}
```

Pesan *error*-nya:

```text
E2.java:3: error: constructor Mobil in class Mobil cannot be applied to given types;
        Mobil mobilBudi = new Mobil("Avanza", "hitam", 2019);
                          ^
  required: no arguments
  found:    String,String,int
  reason: actual and formal argument lists differ in length
1 error
error: compilation failed
```

**Artinya:** karena ada `void`, `Mobil(...)` dianggap *method* biasa, bukan konstruktor. Java lalu memakai konstruktor bawaan yang tidak menerima argumen (*required: no arguments*). Perhatikan bahwa pesannya menunjuk baris yang membuat objek (`new Mobil(...)`), bukan baris `void Mobil`. Jadi, saat pesan seperti ini muncul, periksa juga konstruktornya. **Perbaikan:** hapus kata `void`.

### Kesalahan 3: Lupa `this.` saat nama parameter sama dengan *field*

Potongan konstruktor yang salah:

```java
    Menu(String nama, int harga) {
        nama = nama;
        harga = harga;
    }
```

Tidak ada *error*, tetapi `kopi.tampilkanInfo()` mencetak:

```text
null - Rp0
```

**Artinya:** `nama = nama` mengisi parameter dengan dirinya sendiri. *Field*-nya tidak tersentuh sehingga tetap bernilai bawaan (`null` dan `0`). Ini *bug* yang licin karena tidak ada pesan *error*. **Perbaikan:** `this.nama = nama;`.

### Kesalahan 4: Memanggil *method* pada variabel yang belum berisi objek

Potongan kode yang salah:

```java
        Menu kopi = null;
        kopi.tampilkanInfo();
```

Pesan *error*-nya:

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Menu.tampilkanInfo()" because "<local1>" is null
	at E4.main(E4.java:4)
```

**Artinya:** variabel `kopi` tidak menunjuk ke objek apa pun (`null`), jadi tidak ada yang bisa menjalankan *method*. Bagian `at E4.main(E4.java:4)` menunjukkan lokasinya: baris 4. Nama variabel kadang tertulis sebagai `<local1>`, kadang sebagai `kopi`, tergantung cara program dikompilasi. **Perbaikan:** pastikan variabel sudah diisi dengan `new Menu(...)`.

### Kesalahan 5: Jumlah argumen tidak sesuai konstruktor

Potongan kode yang salah:

```java
        Menu kopi = new Menu("Kopi Susu Gula Aren");
```

Pesan *error*-nya:

```text
E5.java:3: error: constructor Menu in class Menu cannot be applied to given types;
        Menu kopi = new Menu("Kopi Susu Gula Aren");
                    ^
  required: String,int
  found:    String
  reason: actual and formal argument lists differ in length
1 error
error: compilation failed
```

**Artinya:** konstruktor membutuhkan `String, int` (*required*), tetapi kita hanya mengirim `String` (*found*). **Perbaikan:** `new Menu("Kopi Susu Gula Aren", 18000)`.

### Kesalahan 6: Nama kelas `public` berbeda dengan nama *file*

Jika *file* `Salah.java` berisi `public class KedaiKita`, perintah `javac Salah.java` menolak:

```text
Salah.java:1: error: class KedaiKita is public, should be declared in a file named KedaiKita.java
public class KedaiKita {
       ^
1 error
```

VS Code juga memberi garis merah dengan pesan *The public type KedaiKita must be defined in its own file*. Anehnya, perintah cepat `java Salah.java` biasanya tetap bisa menjalankannya karena cara itu tidak memeriksa aturan nama *file*. Jangan terkecoh: kode seperti ini tetap dianggap salah. **Perbaikan:** samakan nama *file* dengan nama kelas `public`-nya. Ingat, huruf besar dan kecil juga harus sama persis.

> [!NOTE]
> Pesan di atas diambil dari JDK 21. Bunyinya bisa sedikit berbeda antarversi Java. Fokuslah pada kata-kata kuncinya, misalnya `cannot find symbol`, `cannot be applied to given types`, atau `NullPointerException`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Mendefinisikan kelas | `class NamaKelas { ... }` | `class Menu { ... }` |
| *Field* (atribut) | `Tipe nama;` | `int harga;` |
| Konstruktor | `NamaKelas(parameter) { ... }` | `Menu(String nama, int harga) { ... }` |
| Mengisi *field* di konstruktor | `this.field = parameter;` | `this.harga = harga;` |
| *Method* tanpa nilai kembalian | `void nama(parameter) { ... }` | `void tampilkanInfo() { ... }` |
| *Method* dengan nilai kembalian | `Tipe nama(parameter) { return ...; }` | `int hitungTotal(int jumlah)` |
| Membuat objek | `NamaKelas var = new NamaKelas(argumen);` | `Menu kopi = new Menu("Kopi", 18000);` |
| Membaca *field* | `objek.field` | `kopi.harga` |
| Memanggil *method* | `objek.method(argumen)` | `kopi.hitungTotal(2)` |
| *Array* objek | `NamaKelas[] var = { ... };` | `Lagu[] playlist = { new Lagu(...) };` |
| Cek objek yang sama | `a == b` | `oyen == belang` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
