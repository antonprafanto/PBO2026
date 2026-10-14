# ☕ Praktik Java Pertemuan 04: Enkapsulasi

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 04](../README.md). Kode contoh di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan. Potongan kode lain diberi keterangan cara mencobanya.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Masalah: Data yang Bisa Diubah Sembarangan](#1-masalah-data-yang-bisa-diubah-sembarangan)
2. [`private` dan *Getter*](#2-private-dan-getter)
3. [*Getter* dan *Setter* dengan Validasi](#3-getter-dan-setter-dengan-validasi)
4. [Validasi di Konstruktor](#4-validasi-di-konstruktor)
5. [Atribut *Read-Only* dan `final`](#5-atribut-read-only-dan-final)
6. [*Method* Penjaga Aturan](#6-method-penjaga-aturan)
7. [*Field* `static` yang Dilindungi](#7-field-static-yang-dilindungi)
8. [Anatomi Kelas Java yang Terenkapsulasi](#8-anatomi-kelas-java-yang-terenkapsulasi)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (misalnya 17, 21, atau 25), VS Code dengan **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh kecil, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 04
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap *file* contoh adalah **program satu *file***. Sejak Java 11, program seperti ini bisa langsung dijalankan dengan perintah `java NamaFile.java`, tanpa langkah kompilasi terpisah.

> [!IMPORTANT]
> Di setiap *file* contoh, kelas yang memiliki *method* `main` ditulis **paling atas**, dan kelas-kelas pembantunya ditulis di bawahnya. Pada Java 11 sampai 21, perintah `java NamaFile.java` mewajibkan kelas pertama di dalam *file* punya `main`. Agar aman di semua versi, ikuti urutan yang sama saat kamu membuat *file* sendiri.

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-04-Enkapsulasi/java`. Buka **hanya** folder `java` milik pertemuan ini, bukan seluruh repositori. Alasannya, setiap pertemuan punya kelas dengan nama yang sama (misalnya `Menu`), dan VS Code akan protes jika dua kelas bernama sama berada dalam satu proyek. Setelah itu, buka *file* contoh yang ingin dicoba, misalnya `contoh/Contoh01DataBocor.java`, lalu klik **Run** pada tulisan **Run | Debug** yang muncul tepat di atas baris `public static void main` (atau tombol ▷ di pojok kanan atas). Hasilnya muncul di panel **TERMINAL** (kadang **DEBUG CONSOLE**) di bagian bawah.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-04-Enkapsulasi/java/contoh` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu, jalankan:

```bash
java Contoh01DataBocor.java
```

Jika berhasil, *output* yang muncul sama persis dengan *output* yang ditampilkan di [bagian 1](#1-masalah-data-yang-bisa-diubah-sembarangan).

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Perintah `java` sama di Windows, macOS, dan Linux. Cara klasik dua langkah (`javac Contoh01DataBocor.java`, lalu `java Contoh01DataBocor`) juga tetap bisa dipakai. Penjelasannya ada di [Menjalankan Program](../../00-Persiapan/menjalankan-program.md).

### Tempat Menyimpan Kodemu Sendiri

Simpan semua kode buatanmu (hasil mengetik ulang, percobaan "Coba sendiri", *file* coretan, dan jawaban latihan) di folder `PBO-latihan-saya/pertemuan-04/`, **di luar** folder materi; untuk Java, pakai satu subfolder untuk setiap pertemuan agar nama kelas tidak bentrok. Jika sebuah percobaan memintamu mengubah *file* contoh atau studi kasus, salin dulu *file* itu ke folder tersebut tanpa mengganti namanya (nama *file* Java harus sama dengan nama kelas `public`-nya), lalu ubah dan jalankan salinannya. Untuk menjalankan salinan itu, buka folder tersebut di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**) atau arahkan terminal ke sana dengan `cd`. Alasan dan cara menyalinnya ada di [aturan emas 00-Persiapan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Setiap bagian diawali baris ***File*:** atau **Potongan dari** yang menautkan *file* contohnya.
- ***File*:** berarti kode di bawahnya adalah isi lengkap *file* itu, hanya tanpa komentar pembuka, termasuk kelas yang memiliki `main`. Hasil ketik ulangnya bisa langsung dijalankan.
- **Potongan dari** berarti yang ditampilkan hanya sebagian. Potongan dari dalam *method* `main` tampil menjorok 8 spasi karena aslinya berada di dalam kelas dan di dalam `main`. Jangan mengetik ulang potongannya saja; jalankan *file* lengkapnya dengan cara di atas.
- Tanda `// [1]`, `// [2]`, dan seterusnya di dalam kode dijelaskan satu per satu tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.

Saran belajar: **ketik ulang** contoh yang ditampilkan lengkap ke folder latihanmu, jangan hanya menyalin. Jari yang mengetik membantu otak mengingat.

## 1. Masalah: Data yang Bisa Diubah Sembarangan

*File*: [`contoh/Contoh01DataBocor.java`](contoh/Contoh01DataBocor.java)

Kita mulai dengan membandingkan dua kelas tabungan. Yang pertama "bocor", yang kedua menjaga saldonya sendiri. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```java
public class Contoh01DataBocor {

    public static void main(String[] args) {
        System.out.println("=== TABUNGAN BOCOR ===");
        TabunganBocor bocor = new TabunganBocor("Budi", 500000);
        System.out.println("Saldo awal Budi: Rp" + bocor.saldo);
        bocor.saldo = bocor.saldo - 2000000; // [5] tarik melebihi saldo, tidak dicegah
        System.out.println("Setelah ditarik Rp2000000: Rp" + bocor.saldo);
        bocor.saldo = 999999999; // [6] saldo "disulap" langsung dari luar kelas
        System.out.println("Setelah disulap: Rp" + bocor.saldo);

        System.out.println();
        System.out.println("=== TABUNGAN AMAN ===");
        TabunganAman aman = new TabunganAman("Siti", 500000);
        aman.cekSaldo();
        aman.tarik(2000000); // [7] semua perubahan lewat method, aturan selalu dicek
        aman.setor(-100000);
        aman.setor(250000);
        aman.tarik(100000);
        aman.cekSaldo();
    }
}

/** Tabungan tanpa perlindungan: field saldo bisa diubah siapa saja. */
class TabunganBocor {
    String pemilik;
    int saldo; // [1] tanpa access modifier: kelas lain di paket yang sama bebas mengubahnya

    TabunganBocor(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }
}

/** Tabungan yang menjaga saldonya sendiri. */
class TabunganAman {
    private String pemilik;
    private int saldo; // [2] private: hanya kode di dalam kelas ini yang boleh menyentuhnya

    public TabunganAman(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    public void setor(int jumlah) { // [3] pintu resmi untuk menambah saldo
        if (jumlah <= 0) {
            System.out.println("Setor Rp" + jumlah + " ditolak: jumlah harus lebih dari 0");
        } else {
            saldo += jumlah;
            System.out.println("Setor Rp" + jumlah + " berhasil");
        }
    }

    public void tarik(int jumlah) { // [4] pintu resmi untuk mengurangi saldo
        if (jumlah <= 0) {
            System.out.println("Tarik Rp" + jumlah + " ditolak: jumlah harus lebih dari 0");
        } else if (jumlah > saldo) {
            System.out.println("Tarik Rp" + jumlah + " ditolak: saldo tidak cukup");
        } else {
            saldo -= jumlah;
            System.out.println("Tarik Rp" + jumlah + " berhasil");
        }
    }

    public void cekSaldo() {
        System.out.println("  Saldo " + pemilik + ": Rp" + saldo);
    }
}
```

***Output:***

```text
=== TABUNGAN BOCOR ===
Saldo awal Budi: Rp500000
Setelah ditarik Rp2000000: Rp-1500000
Setelah disulap: Rp999999999

=== TABUNGAN AMAN ===
  Saldo Siti: Rp500000
Tarik Rp2000000 ditolak: saldo tidak cukup
Setor Rp-100000 ditolak: jumlah harus lebih dari 0
Setor Rp250000 berhasil
Tarik Rp100000 berhasil
  Saldo Siti: Rp650000
```

Penjelasan:

- **[1]** *Field* `saldo` tidak diberi *access modifier*, persis seperti yang kita tulis di Pertemuan 02 dan 03. Artinya, semua kelas di paket yang sama, termasuk kelas `Contoh01DataBocor` yang berisi `main`, bebas mengubahnya.
- **[2]** Kata kunci `private` membuat *field* `saldo` hanya bisa disentuh oleh kode **di dalam** kelas `TabunganAman`.
- **[3]** *Method* `setor()` diberi `public` sehingga boleh dipanggil dari mana saja. *Method* ini menjadi satu-satunya pintu resmi untuk menambah saldo, dan selalu memeriksa aturannya dulu.
- **[4]** *Method* `tarik()` menolak jumlah yang tidak masuk akal dan penarikan yang melebihi saldo.
- **[5]** Pada tabungan bocor, saldo bisa langsung dikurangi melebihi isinya. Hasilnya minus, dan tidak ada yang mencegah.
- **[6]** Lebih parah lagi, saldo bisa "disulap" menjadi angka berapa pun.
- **[7]** Pada tabungan aman, `main` tidak pernah menyentuh `saldo`. Semua perubahan lewat *method* sehingga aturan selalu diperiksa. Seandainya `main` menulis `aman.saldo = 999999999;`, Java menolaknya saat kompilasi (lihat bagian 2).

Di contoh ini, penolakan masih berupa `System.out.println`. Cara itu punya kelemahan: kode pemanggil tidak tahu bahwa perintahnya gagal. Mulai bagian 3, kita memakai cara yang lebih tegas, yaitu *exception*.

> [!TIP]
> **Coba sendiri:** salin `Contoh01DataBocor.java` ke folder `PBO-latihan-saya/pertemuan-04/` tanpa mengganti namanya. Di salinan itu, tambahkan dua baris berikut di akhir *method* `main`, tepat di bawah baris `aman.cekSaldo();` yang terakhir. Simpan, jalankan salinan itu, lalu bandingkan dengan jawaban di bawah. Apakah saldo awal yang negatif ditolak?
>
> ```java
>         TabunganAman rina = new TabunganAman("Rina", -100000);
>         rina.cekSaldo();
> ```

<details>
<summary>Lihat jawaban</summary>

Tidak ditolak. Di baris paling bawah *output* muncul `Saldo Rina: Rp-100000`. *Method* `setor()` dan `tarik()` memang sudah menjaga aturan, tetapi **konstruktor** masih menyimpan saldo awal tanpa memeriksanya. Celah ini kita tutup di bagian 4.

</details>

## 2. `private` dan *Getter*

*File*: [`contoh/Contoh02PrivateDanGetter.java`](contoh/Contoh02PrivateDanGetter.java)

> [!NOTE]
> Di jalur Python, contoh nomor 02 membahas *name mangling*, fitur yang **khusus Python** (lihat [Jembatan](../jembatan-python-java.md)). Padanannya di Java adalah contoh berikut: *field* `private` yang benar-benar dijaga oleh *compiler*, plus *getter* sebagai pintu bacanya.

Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```java
public class Contoh02PrivateDanGetter {

    public static void main(String[] args) {
        Brankas brankas = new Brankas("Budi", "246810");

        System.out.println("=== MEMAKAI BRANKAS LEWAT METHOD ===");
        brankas.buka("123456");
        brankas.buka("246810");

        System.out.println();
        System.out.println("=== MEMBACA DATA LEWAT GETTER ===");
        System.out.println("Pemilik brankas: " + brankas.getPemilik()); // [5]
        // System.out.println(brankas.pin); // [6] jika tanda // dihapus: error kompilasi
        System.out.println("PIN tidak punya getter, jadi tidak bisa dibaca dari luar kelas");
    }
}

/** Brankas sederhana: punya pemilik dan PIN. */
class Brankas {
    private String pemilik; // [1] private: hanya kode di dalam kelas Brankas yang boleh menyentuh
    private String pin;

    public Brankas(String pemilik, String pin) { // [2] public: boleh dipanggil dari mana saja
        this.pemilik = pemilik;
        this.pin = pin;
    }

    public String getPemilik() { // [3] getter: "pintu baca" untuk field pemilik
        return pemilik;
    }

    public void buka(String pin) {
        if (pin.equals(this.pin)) { // [4] di DALAM kelas, field private bebas dipakai
            System.out.println("PIN benar. Brankas milik " + pemilik + " terbuka.");
        } else {
            System.out.println("PIN salah. Brankas tetap terkunci.");
        }
    }
}
```

***Output:***

```text
=== MEMAKAI BRANKAS LEWAT METHOD ===
PIN salah. Brankas tetap terkunci.
PIN benar. Brankas milik Budi terbuka.

=== MEMBACA DATA LEWAT GETTER ===
Pemilik brankas: Budi
PIN tidak punya getter, jadi tidak bisa dibaca dari luar kelas
```

Penjelasan:

- **[1]** Kedua *field* diberi `private`. Kelas `Contoh02PrivateDanGetter` (tempat `main` berada) adalah kelas **lain**, jadi ia tidak boleh menyentuh `pemilik` maupun `pin` meskipun keduanya ditulis di *file* yang sama.
- **[2]** Konstruktor diberi `public` sehingga objek `Brankas` boleh dibuat dari kelas mana pun.
- **[3]** ***Getter*** adalah *method* `public` yang mengembalikan nilai *field* `private`. Namanya mengikuti kesepakatan Java: `get` + nama *field* dengan huruf awal kapital, yaitu `getPemilik()`.
- **[4]** Di dalam kelas `Brankas`, *field* `private` bebas dipakai. `this.pin` adalah *field*, sedangkan `pin` adalah parameter. Perhatikan juga bahwa teks dibandingkan dengan `.equals()`, bukan `==`.
- **[5]** Dari luar kelas, nama pemilik dibaca lewat *getter*.
- **[6]** *Field* `pin` sengaja **tidak** diberi *getter*. Coba salin `Contoh02PrivateDanGetter.java` ke folder `PBO-latihan-saya/pertemuan-04/`, hapus tanda `//` di awal baris 29 pada salinan itu, simpan, lalu jalankan. Program bahkan tidak bisa dikompilasi:

```text
Contoh02PrivateDanGetter.java:29: error: pin has private access in Brankas
        System.out.println(brankas.pin); // [6] jika tanda // dihapus: error kompilasi
                                  ^
1 error
error: compilation failed
```

Pesan *pin has private access in Brankas* berarti "*field* `pin` bersifat privat milik kelas `Brankas`". Tanda `^` menunjuk bagian yang bermasalah. Baris terakhir, `error: compilation failed`, muncul jika program dijalankan dengan `java NamaFile.java`. Jika memakai `javac`, baris itu tidak ada.

Inilah perbedaan besar dengan Python: di Java, larangan `private` **dijaga oleh *compiler***. Kode yang melanggar tidak akan pernah sempat berjalan.

### Empat tingkat akses di Java

Tabel jangkauan `public`, `protected`, *default*, dan `private` sudah dibahas di [halaman konsep](../README.md#4-access-modifier-siapa-boleh-masuk). Untuk sekarang, pegang pola yang paling umum:

- ***field*** dibuat `private`
- **konstruktor dan *method* untuk umum** dibuat `public`
- ***method* pembantu internal** juga dibuat `private`

Paket bernama baru dipakai di Pertemuan 15, sedangkan `protected` dibahas bersama pewarisan di Pertemuan 07.

> [!NOTE]
> Kelas pembantu seperti `Brankas` sendiri tidak diberi `public` karena dalam satu *file* Java hanya boleh ada **satu** kelas `public` (yang namanya sama dengan nama *file*). Di depan kelas tingkat atas, `private` juga tidak diizinkan (lihat [Kesalahan 5](#kesalahan-5-memberi-private-pada-kelas)).

## 3. *Getter* dan *Setter* dengan Validasi

Potongan dari [`contoh/Contoh03GetterSetter.java`](contoh/Contoh03GetterSetter.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Getter* adalah pintu baca. Sekarang kita tambahkan ***setter***, pintu ubah yang memeriksa data sebelum menyimpannya. Potongan pertama, kelas `Televisi`:

```java
/** Televisi dengan volume 0 sampai 100. */
class Televisi {
    private String merek;
    private int volume;

    public Televisi(String merek) {
        this.merek = merek;
        this.volume = 10; // volume awal setiap TV baru
    }

    public String getMerek() { // [1] getter: mengembalikan nilai field private
        return merek;
    }

    public int getVolume() {
        return volume;
    }

    public void setVolume(int volume) { // [2] setter: menerima nilai baru lewat parameter
        if (volume < 0 || volume > 100) {
            throw new IllegalArgumentException("Volume harus 0-100, bukan " + volume); // [3]
        }
        this.volume = volume; // [4] baru disimpan setelah lolos pemeriksaan
    }
}
```

Potongan kedua, isi *method* `main`:

```java
        Televisi tv = new Televisi("Polytron");
        System.out.println("=== TV BARU DINYALAKAN ===");
        System.out.println("Merek : " + tv.getMerek()); // [5] membaca lewat getter
        System.out.println("Volume: " + tv.getVolume());

        System.out.println();
        System.out.println("=== MENGATUR VOLUME ===");
        tv.setVolume(25); // [6] mengubah lewat setter
        System.out.println("Volume diatur ke 25, sekarang " + tv.getVolume());
        tv.setVolume(tv.getVolume() + 10); // [7] baca dulu (25), lalu simpan 35
        System.out.println("Volume dinaikkan 10, sekarang " + tv.getVolume());

        System.out.println();
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try { // [8] intip sekilas: "coba jalankan; jika ditolak, tangkap"
            tv.setVolume(150);
            System.out.println("Baris ini tidak pernah tercetak");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Volume tetap " + tv.getVolume());
```

***Output:***

```text
=== TV BARU DINYALAKAN ===
Merek : Polytron
Volume: 10

=== MENGATUR VOLUME ===
Volume diatur ke 25, sekarang 25
Volume dinaikkan 10, sekarang 35

=== DATA TIDAK VALID DITOLAK ===
Ditolak: Volume harus 0-100, bukan 150
Volume tetap 35
```

Penjelasan:

- **[1]** *Getter* `getMerek()` bertipe kembalian `String`, sama dengan tipe *field*-nya. Karena `merek` tidak punya *setter*, *field* ini bersifat *read-only* dari luar.
- **[2]** *Setter* `setVolume(int volume)` bertipe `void` dan menerima nilai baru lewat parameter. Nama parameter sengaja dibuat sama dengan nama *field* sehingga `this.volume` berarti *field* dan `volume` berarti nilai baru (ingat Pertemuan 02).
- **[3]** `throw new IllegalArgumentException("...")` **melempar** *exception*. *Method* langsung berhenti di baris ini. `IllegalArgumentException` adalah kelas *exception* bawaan Java yang artinya "argumen yang dikirim tidak sah".
- **[4]** Baris penyimpanan hanya tercapai jika pemeriksaan lolos. Jika nilainya ditolak, *field* `volume` tidak tersentuh.
- **[5]** Dari luar kelas, *field* dibaca lewat *getter*, lengkap dengan tanda kurung: `tv.getMerek()`.
- **[6]** *Field* diubah lewat *setter*: `tv.setVolume(25)`.
- **[7]** Untuk menaikkan volume, nilai lama dibaca dulu dengan *getter*, ditambah 10, lalu dikirim ke *setter*. *Setter* tetap memeriksa nilai 35 itu.
- **[8]** `try`/`catch` kita intip sekilas. Java **mencoba** menjalankan blok `try`. Saat *setter* melempar *exception*, sisa blok `try` dilewati (baris "tidak pernah tercetak" memang tidak tercetak), lalu blok `catch` dijalankan. `e.getMessage()` mengambil pesan yang ditulis saat *exception* dilempar.

```text
tv.setVolume(150)
      |
      v
setVolume(volume=150) --> 150 > 100 --> throw new IllegalArgumentException(...)
      |
      v   (sisa blok try dilewati)
catch (IllegalArgumentException e)  -->  println("Ditolak: " + e.getMessage())
```

> [!NOTE]
> Hari ini kita hanya **mengintip** `try`/`catch` agar program tetap berjalan setelah data ditolak. Bahasan lengkapnya ada di Pertemuan 11.

### Kesepakatan nama *getter* dan *setter*

| Jenis | Pola nama | Contoh |
|---|---|---|
| *Getter* | `get` + NamaField | `getVolume()`, `getMerek()` |
| *Getter* untuk `boolean` | `is` + NamaField | `isPenuh()`, `isLulus()` |
| *Setter* | `set` + NamaField | `setVolume(int volume)` |

Kesepakatan ini diikuti hampir semua pemrogram Java, dan banyak alat bantu (misalnya fitur **Generate Getters and Setters** di VS Code) mengandalkannya. Namun, ingat pesan di halaman konsep: jangan membuat *getter* dan *setter* untuk **semua** *field* secara otomatis.

## 4. Validasi di Konstruktor

Potongan dari [`contoh/Contoh04ValidasiKonstruktor.java`](contoh/Contoh04ValidasiKonstruktor.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Setter* sudah rajin memeriksa. Namun, data juga masuk lewat **konstruktor**. Contoh ini menunjukkan apa yang terjadi jika pintu yang satu itu lupa dijaga. Potongan pertama, awal kelas `MahasiswaBercelah`:

```java
/** Setter-nya memeriksa data, tetapi konstruktornya tidak. */
class MahasiswaBercelah {
    private String nama;
    private int semester;

    public MahasiswaBercelah(String nama, int semester) {
        this.nama = nama;
        this.semester = semester; // [1] celah: disimpan langsung tanpa diperiksa
    }
```

Sisa kelas `MahasiswaBercelah` (*method* `getNama()`, `getSemester()`, dan `setSemester()`) sama persis dengan milik kelas `Mahasiswa` berikut. Perbedaan pentingnya ada di konstruktor. Selain itu, `Mahasiswa` juga punya *setter* `setNama()`. Potongan kedua, kelas `Mahasiswa` selengkapnya:

```java
/** Konstruktor memakai setter, jadi data diperiksa sejak objek lahir. */
class Mahasiswa {
    private String nama;
    private int semester;

    public Mahasiswa(String nama, int semester) {
        setNama(nama); // [2] lewat setter: aturan nama ikut diperiksa
        setSemester(semester); // [3] lewat setter: aturan semester ikut diperiksa
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        if (nama.isBlank()) { // [4] isBlank(): kosong atau hanya berisi spasi
            throw new IllegalArgumentException("Nama tidak boleh kosong");
        }
        this.nama = nama;
    }

    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        if (semester < 1 || semester > 14) {
            throw new IllegalArgumentException("Semester harus 1-14, bukan " + semester);
        }
        this.semester = semester;
    }
}
```

Potongan ketiga, isi *method* `main`:

```java
        System.out.println("=== VERSI BERCELAH ===");
        MahasiswaBercelah ayu = new MahasiswaBercelah("Ayu", 20); // [5] semester 20 lolos!
        System.out.println(ayu.getNama() + " tercatat di semester " + ayu.getSemester());
        try {
            ayu.setSemester(21);
        } catch (IllegalArgumentException e) {
            System.out.println("Mengubah lewat setter ditolak: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== VERSI AMAN ===");
        Mahasiswa bima = new Mahasiswa("Bima", 3);
        System.out.println(bima.getNama() + " tercatat di semester " + bima.getSemester());
        try {
            Mahasiswa citra = new Mahasiswa("Citra", 20); // [6] ditolak sejak lahir
            System.out.println(citra.getNama() + " berhasil dibuat"); // tidak pernah dijalankan
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat mahasiswa: " + e.getMessage());
        }
        try {
            new Mahasiswa("   ", 2); // nama berisi spasi saja
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat mahasiswa: " + e.getMessage());
        }
```

***Output:***

```text
=== VERSI BERCELAH ===
Ayu tercatat di semester 20
Mengubah lewat setter ditolak: Semester harus 1-14, bukan 21

=== VERSI AMAN ===
Bima tercatat di semester 3
Gagal membuat mahasiswa: Semester harus 1-14, bukan 20
Gagal membuat mahasiswa: Nama tidak boleh kosong
```

Penjelasan:

- **[1]** Konstruktor `MahasiswaBercelah` mengisi *field* secara langsung. *Setter*-nya tidak pernah dipanggil sehingga nilai apa pun lolos.
- **[2]** Konstruktor `Mahasiswa` memanggil `setNama(nama)`. *Method* milik objek yang sama boleh dipanggil langsung dari konstruktor. (Mulai Pertemuan 05, *setter* yang dipanggil konstruktor KedaiKita akan diberi `final` agar lebih aman. Alasannya baru terasa setelah belajar pewarisan di Pertemuan 07.)
- **[3]** Begitu juga `setSemester(semester)`. Aturan semester cukup ditulis **sekali** di *setter*, lalu dipakai oleh konstruktor dan oleh siapa pun yang mengubah semester kelak.
- **[4]** `isBlank()` (Java 11 ke atas) bernilai `true` jika teks kosong atau hanya berisi spasi.
- **[5]** Lihat keanehannya: semester 20 lolos saat objek dibuat, tetapi semester 21 ditolak saat diubah lewat *setter*. Data objek ini tidak konsisten.
- **[6]** Pada versi aman, objek dengan semester 20 **tidak pernah tercipta**. *Exception* dilempar dari dalam konstruktor sehingga `new` gagal dan baris `println` di bawahnya dilewati.

> [!IMPORTANT]
> Di dalam konstruktor, isi *field* yang punya aturan **lewat *setter*-nya**, misalnya `setHarga(harga);`. Dengan begitu, konstruktor ikut melewati pemeriksaan yang sama.

> [!NOTE]
> Batas semester 1—14 hanyalah aturan contoh di program ini. Di dunia nyata, aturan seperti ini mengikuti ketentuan kampus masing-masing.

## 5. Atribut *Read-Only* dan `final`

Potongan dari [`contoh/Contoh05ReadOnly.java`](contoh/Contoh05ReadOnly.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

*Field* yang hanya punya *getter*, tanpa *setter*, bersifat *read-only* dari luar. Kita pakai contoh data KTP: NIK tidak pernah berubah, tetapi alamat boleh berubah. Potongan pertama, kelas `Penduduk`:

```java
/** Data kependudukan sederhana. */
class Penduduk {
    private final String nik; // [6] final: hanya boleh diisi satu kali, di konstruktor
    private final String nama;
    private String alamat;

    public Penduduk(String nik, String nama, String alamat) {
        if (nik.length() != 16) { // [1] satu-satunya kesempatan memeriksa NIK
            throw new IllegalArgumentException("NIK harus 16 digit");
        }
        this.nik = nik;
        this.nama = nama;
        setAlamat(alamat); // lewat setter alamat
    }

    public String getNik() { // [2] hanya getter, TANPA setter -> read-only
        return nik;
    }

    public String getNama() {
        return nama;
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) { // [3] alamat boleh berubah, asal tidak kosong
        if (alamat.isBlank()) {
            throw new IllegalArgumentException("Alamat tidak boleh kosong");
        }
        this.alamat = alamat;
    }
}
```

Potongan kedua, isi *method* `main`:

```java
        Penduduk warga = new Penduduk("1234567890123456", "Rina Wulandari",
                "Jl. Pramuka, Samarinda");
        System.out.println("=== DATA AWAL ===");
        System.out.println("NIK   : " + warga.getNik());
        System.out.println("Nama  : " + warga.getNama());
        System.out.println("Alamat: " + warga.getAlamat());

        System.out.println();
        System.out.println("=== PINDAH RUMAH ===");
        warga.setAlamat("Jl. Juanda, Samarinda"); // [4] diizinkan: alamat punya setter
        System.out.println("Alamat baru: " + warga.getAlamat());
        // warga.setNik("9999999999999999"); // [5] hapus tanda // untuk melihat error-nya

        System.out.println();
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            warga.setAlamat("");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            new Penduduk("12345", "Doni Saputra", "Jl. Merdeka, Samarinda");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Alamat " + warga.getNama() + " tetap: " + warga.getAlamat());
```

***Output:***

```text
=== DATA AWAL ===
NIK   : 1234567890123456
Nama  : Rina Wulandari
Alamat: Jl. Pramuka, Samarinda

=== PINDAH RUMAH ===
Alamat baru: Jl. Juanda, Samarinda

=== DATA TIDAK VALID DITOLAK ===
Ditolak: Alamat tidak boleh kosong
Ditolak: NIK harus 16 digit
Alamat Rina Wulandari tetap: Jl. Juanda, Samarinda
```

Penjelasan:

- **[1]** Karena `nik` tidak punya *setter*, pemeriksaannya ditulis langsung di konstruktor. Inilah satu-satunya kesempatan untuk memeriksa NIK.
- **[2]** `nik` dan `nama` hanya punya *getter*. Dari luar, keduanya bisa dibaca, tetapi tidak bisa diubah.
- **[3]** `alamat` punya *getter* dan *setter*, jadi boleh diubah asal tidak kosong.
- **[4]** Mengubah alamat diizinkan dan tetap diperiksa oleh *setter*.
- **[5]** Baris ini sengaja diberi tanda `//` di awalnya agar tidak ikut dikompilasi. Coba salin `Contoh05ReadOnly.java` ke folder `PBO-latihan-saya/pertemuan-04/`, hapus tanda `//` pertama di baris 32 pada salinan itu, simpan, lalu jalankan. *Compiler* menolak karena *method* `setNik` memang tidak pernah dibuat:

```text
Contoh05ReadOnly.java:32: error: cannot find symbol
        warga.setNik("9999999999999999"); // [5] hapus tanda // untuk melihat error-nya
             ^
  symbol:   method setNik(String)
  location: variable warga of type Penduduk
1 error
error: compilation failed
```

- **[6]** Kata kunci `final` menambah satu lapis pengaman. *Field* `final` hanya boleh diisi **satu kali**, biasanya di konstruktor. Setelah itu, kode **di dalam** kelas pun tidak bisa mengubahnya lagi.

Apa bedanya "tanpa *setter*" dengan `final`?

| | Tanpa *setter* saja | Tanpa *setter* + `final` |
|---|---|---|
| Kode di luar kelas bisa mengubah? | Tidak | Tidak |
| Kode di dalam kelas bisa mengubah? | Bisa (misalnya oleh *method* lain) | Tidak, ditolak *compiler* |

Misalnya, seseorang menambahkan *method* `setNik` ke kelas `Penduduk`. Kamu bisa mencobanya di salinan `Contoh05ReadOnly.java` yang sama: tambahkan tiga baris berikut tepat di bawah *method* `getNik()` (sisakan satu baris kosong di antaranya), simpan, lalu jalankan.

```java
    public void setNik(String nik) {
        this.nik = nik;
    }
```

*Compiler* langsung menolaknya:

```text
Contoh05ReadOnly.java:70: error: cannot assign a value to final variable nik
        this.nik = nik;
            ^
1 error
error: compilation failed
```

Pesan *cannot assign a value to final variable nik* berarti "tidak bisa mengisi ulang variabel `final` bernama `nik`". Baris 32 yang tadi kamu aktifkan kini tidak lagi bermasalah karena `setNik` sudah ada, jadi yang tersisa hanya *error* ini.

> [!TIP]
> `final` cocok untuk data yang memang tidak pernah berubah sepanjang hidup objek, seperti NIK atau kode menu. Jangan pakai `final` untuk *field* yang diubah oleh *method*, seperti stok atau saldo.

## 6. *Method* Penjaga Aturan

Potongan dari [`contoh/Contoh06MethodPenjagaAturan.java`](contoh/Contoh06MethodPenjagaAturan.java). Untuk melihat hasilnya, jalankan *file* lengkapnya.

Jumlah motor di parkiran tidak diberi *setter*. Jumlah itu hanya berubah lewat dua pintu resmi, yaitu `masuk()` dan `keluar()`. Masing-masing menjaga aturannya sendiri. Potongan pertama, awal kelas `Parkiran`:

```java
/** Parkiran motor dengan kapasitas terbatas. */
class Parkiran {
    private String nama;
    private int kapasitas;
    private int terisi; // [1] tanpa setter: hanya berubah lewat masuk()/keluar()

    public Parkiran(String nama, int kapasitas) {
        if (kapasitas <= 0) {
            throw new IllegalArgumentException("Kapasitas harus lebih dari 0");
        }
        this.nama = nama;
        this.kapasitas = kapasitas;
        this.terisi = 0;
    }
```

*Getter* `getNama()`, `getKapasitas()`, dan `getTerisi()` hanya berisi `return` biasa. Bagian yang menarik ada setelahnya (potongan kedua, sisa kelas `Parkiran`):

```java
    public int getSisa() { // [2] dihitung saat diminta, tidak disimpan di field
        return kapasitas - terisi;
    }

    public boolean isPenuh() { // [3] getter boolean memakai awalan is, bukan get
        return terisi == kapasitas;
    }

    public void masuk(int jumlah) { // [4] pintu resmi untuk menambah jumlah motor
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah motor harus lebih dari 0");
        }
        if (jumlah > getSisa()) {
            throw new IllegalArgumentException("Tempat tidak cukup untuk " + jumlah
                    + " motor (sisa " + getSisa() + ")");
        }
        terisi += jumlah;
    }

    public void keluar(int jumlah) { // [5] pintu resmi untuk mengurangi jumlah motor
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah motor harus lebih dari 0");
        }
        if (jumlah > terisi) {
            throw new IllegalArgumentException("Hanya ada " + terisi + " motor di parkiran");
        }
        terisi -= jumlah;
    }
}
```

Potongan ketiga, isi *method* `main`. *Method* `tampilkan()` yang dipanggil di sini mencetak satu baris status parkiran, dan `yaTidak()` mengubah `true`/`false` menjadi "ya"/"tidak" (lihat *file* lengkapnya):

```java
        Parkiran parkiran = new Parkiran("Parkiran Gedung C", 5);

        System.out.println("=== PAGI: MOTOR BERDATANGAN ===");
        tampilkan(parkiran);
        parkiran.masuk(3); // [6] "tell": suruh parkiran mencatat motor yang masuk
        System.out.println("3 motor masuk");
        parkiran.masuk(2);
        System.out.println("2 motor masuk");
        tampilkan(parkiran);
        try {
            parkiran.masuk(1);
            System.out.println("1 motor masuk");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== SORE: MOTOR PULANG ===");
        parkiran.keluar(4);
        System.out.println("4 motor keluar");
        tampilkan(parkiran);
        try {
            parkiran.keluar(2);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            parkiran.masuk(-2); // [7] trik curang: "masuk" dengan angka negatif
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
```

***Output:***

```text
=== PAGI: MOTOR BERDATANGAN ===
  Parkiran Gedung C: terisi 0/5, sisa 5, penuh: tidak
3 motor masuk
2 motor masuk
  Parkiran Gedung C: terisi 5/5, sisa 0, penuh: ya
Ditolak: Tempat tidak cukup untuk 1 motor (sisa 0)

=== SORE: MOTOR PULANG ===
4 motor keluar
  Parkiran Gedung C: terisi 1/5, sisa 4, penuh: tidak
Ditolak: Hanya ada 1 motor di parkiran
Ditolak: Jumlah motor harus lebih dari 0
```

Penjelasan:

- **[1]** *Field* `terisi` hanya punya *getter*. Tidak ada `setTerisi()`, jadi tidak ada cara resmi untuk menulis "terisi menjadi 100".
- **[2]** `getSisa()` tidak membaca *field* mana pun yang bernama `sisa`. Nilainya **dihitung** setiap kali diminta sehingga selalu cocok dengan `kapasitas` dan `terisi`.
- **[3]** *Getter* yang mengembalikan `boolean` memakai awalan `is`: `isPenuh()`, bukan `getPenuh()`. Nilai `true`/`false` lalu dicetak sebagai "ya"/"tidak" agar *output*-nya sama dengan versi Python.
- **[4]** `masuk()` menolak jumlah nol atau negatif, juga jumlah yang melebihi sisa tempat.
- **[5]** `keluar()` menolak jumlah yang melebihi motor yang ada sehingga `terisi` tidak pernah minus.
- **[6]** Kode di luar kelas cukup **menyuruh**: "parkiran, catat 3 motor masuk". Parkiran sendiri yang memeriksa aturannya.
- **[7]** Tanpa pemeriksaan `jumlah <= 0`, perintah `masuk(-2)` diam-diam akan **mengurangi** jumlah motor dan melewati aturan di `keluar()`. Selalu periksa tanda bilangan pada *method* penjaga aturan.

Bandingkan dengan gaya "bertanya", yaitu mengambil datanya lalu mengubahnya sendiri dari luar kelas (potongan ilustrasi, tidak untuk dijalankan sendiri):

```java
// Gaya "bertanya" (hindari): aturan ditulis di luar kelas
if (parkiran.getTerisi() + 3 <= parkiran.getKapasitas()) {
    parkiran.setTerisi(parkiran.getTerisi() + 3); // error kompilasi: setTerisi tidak ada
}

// Gaya "menyuruh" (tell, don't ask): aturan dijaga di dalam kelas
parkiran.masuk(3);
```

Desain kelas `Parkiran` **memaksa** kita memakai gaya menyuruh karena `setTerisi()` memang tidak pernah dibuat.

## 7. *Field* `static` yang Dilindungi

*File*: [`contoh/Contoh07AtributKelasPrivat.java`](contoh/Contoh07AtributKelasPrivat.java)

*Field* `static` (milik kelas) juga perlu dilindungi. Contoh ini membuat tiket antrean bernomor otomatis yang tidak boleh kembar. Berikut isi lengkap *file*-nya, tanpa komentar pembuka:

```java
public class Contoh07AtributKelasPrivat {

    public static void main(String[] args) {
        System.out.println("=== PENGAMBILAN TIKET ===");
        TiketAntrean budi = new TiketAntrean("Budi");
        System.out.println(budi.getNomor() + " - " + budi.getNama());
        TiketAntrean siti = new TiketAntrean("Siti");
        System.out.println(siti.getNomor() + " - " + siti.getNama());
        try {
            new TiketAntrean(""); // [5] ditolak sebelum penghitung dinaikkan
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        TiketAntrean rina = new TiketAntrean("Rina");
        System.out.println(rina.getNomor() + " - " + rina.getNama()); // tetap A003

        System.out.println();
        System.out.println("Jumlah tiket tercetak: " + TiketAntrean.getJumlahTiket()); // [6]
        // TiketAntrean.nomorTerakhir = 0; // [7] jika tanda // dihapus: error kompilasi
    }
}

/** Tiket antrean loket. Nomornya dibuat otomatis dan tidak boleh kembar. */
class TiketAntrean {
    private static int nomorTerakhir = 0; // [1] milik kelas, private: tak bisa diubah dari luar

    private int nomor;
    private String nama;

    public TiketAntrean(String nama) {
        if (nama.isBlank()) {
            throw new IllegalArgumentException("Nama tidak boleh kosong");
        }
        TiketAntrean.nomorTerakhir += 1; // [2] naik HANYA jika data sudah valid
        this.nomor = TiketAntrean.nomorTerakhir;
        this.nama = nama;
    }

    public static int getJumlahTiket() { // [3] getter static: dipanggil lewat nama kelas
        return nomorTerakhir;
    }

    public String getNomor() { // [4] getter boleh menyajikan data dalam format yang rapi
        return String.format("A%03d", nomor);
    }

    public String getNama() {
        return nama;
    }
}
```

***Output:***

```text
=== PENGAMBILAN TIKET ===
A001 - Budi
A002 - Siti
Ditolak: Nama tidak boleh kosong
A003 - Rina

Jumlah tiket tercetak: 3
```

Penjelasan:

- **[1]** `nomorTerakhir` adalah *field* `static` (ingat Pertemuan 03): satu nilai yang dipakai bersama oleh semua tiket. Karena `private`, kelas lain tidak bisa mengubahnya.
- **[2]** Penghitung dinaikkan **setelah** pemeriksaan nama lolos. Jika nama kosong, *exception* sudah dilempar lebih dulu sehingga penghitung tidak berubah.
- **[3]** *Getter* untuk *field* `static` juga dibuat `static`, lalu dipanggil lewat nama kelas: `TiketAntrean.getJumlahTiket()`.
- **[4]** *Getter* `getNomor()` tidak mengembalikan angka mentah, tetapi teks rapi seperti `A001`. Format `%03d` artinya "bilangan bulat, minimal 3 digit, diawali nol".
- **[5]** Tiket dengan nama kosong ditolak, dan tidak ada nomor yang "hangus".
- **[6]** Dari luar, jumlah tiket dibaca lewat *getter* `static`.
- **[7]** Coba salin `Contoh07AtributKelasPrivat.java` ke folder `PBO-latihan-saya/pertemuan-04/`, hapus tanda `//` di awal baris 34 pada salinan itu, simpan, lalu jalankan. *Compiler* menolak:

```text
Contoh07AtributKelasPrivat.java:34: error: nomorTerakhir has private access in TiketAntrean
        TiketAntrean.nomorTerakhir = 0; // [7] jika tanda // dihapus: error kompilasi
                    ^
1 error
error: compilation failed
```

Pesan itu berarti "*field* `nomorTerakhir` bersifat privat milik kelas `TiketAntrean`". Di Python, baris serupa (`TiketAntrean._nomor_terakhir = 0`) tetap berjalan dan membuat nomor tiket kembar. Java mencegahnya sejak awal.

## 8. Anatomi Kelas Java yang Terenkapsulasi

Berikut rangkuman bagian-bagian kelas Java yang menjaga datanya sendiri. Ini hanya gambaran ringkas, bukan *file* yang bisa dijalankan. Tanda `<-` menunjuk keterangan untuk baris di sebelah kirinya. Simpan gambar ini di kepala.

```text
class Menu {
    private static int jumlahMenu = 0;          <- field static, private

    private final String kode;                  <- private + final: tak pernah berubah
    private int harga;                          <- private: hanya untuk kode di kelas ini

    public Menu(String kode, int harga) {       <- konstruktor public
        this.kode = kode;
        setHarga(harga);                        <- lewat setter: ikut diperiksa
        Menu.jumlahMenu += 1;                   <- paling akhir, setelah semua lolos
    }

    public static int getJumlahMenu() {         <- getter static (milik kelas)
        return jumlahMenu;
    }

    public String getKode() {                   <- getter saja = read-only
        return kode;
    }

    public int getHarga() {                     <- getter
        return harga;
    }

    public void setHarga(int harga) {           <- setter
        if (harga <= 0) {
            throw new IllegalArgumentException("...");   <- tolak data tidak valid
        }
        this.harga = harga;
    }

    private void bantuHitung() { ... }          <- method internal juga boleh private
}
```

## 9. Studi Kasus KedaiKita

Potongan dari [`studi-kasus/KedaiKita.java`](studi-kasus/KedaiKita.java). Untuk melihat hasilnya, jalankan *file* lengkapnya (caranya ada di akhir bagian ini).

Saatnya KedaiKita menjaga datanya sendiri. Rancangan dan daftar aturannya sudah dibahas di [halaman konsep](../README.md#11-studi-kasus-kedaikita-menu-yang-menjaga-dirinya).

**Apa yang berubah dibanding Pertemuan 03?**

| Bagian | Pertemuan 03 | Pertemuan 04 |
|---|---|---|
| *Field* `Menu` dan `Pelanggan` | tanpa *access modifier* | `private` |
| Konstruktor dan *method* | tanpa *access modifier* | `public` |
| Membaca data | `kopi.harga` | `kopi.getHarga()` |
| Mengubah harga | `kopi.harga = 20000;` tanpa pemeriksaan | `kopi.setHarga(20000);` dengan pemeriksaan |
| Kode, nama, kategori | bisa diubah | *read-only* (hanya *getter*) |
| Stok | `kopi.stok = 15;` | hanya lewat `tambahStok()` dan `kurangiStok()` |
| Penghitung menu | *field* `static` yang bisa diubah dari luar | `private static` + `Menu.getJumlahMenu()` |
| Poin pelanggan | bisa diubah langsung | hanya lewat `tambahPoin()` dan `tukarPoin()` |
| Data tidak valid | diterima begitu saja | ditolak dengan `throw new IllegalArgumentException(...)` |

Kelas `Rupiah` tetap sama, hanya *method* `format()`-nya kini diberi `public`. Berikut bagian-bagian yang baru. Pertama, *field*, konstruktor, dan *getter* milik kelas:

```java
/** Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method. */
class Menu {
    private static int jumlahMenu = 0; // atribut kelas, dibaca lewat Menu.getJumlahMenu()

    private String kode;
    private String nama;
    private int harga;
    private String kategori;
    private int stok;

    public Menu(String kode, String nama, int harga, String kategori, int stok) {
        if (stok < 0) {
            throw new IllegalArgumentException("Stok tidak boleh negatif");
        }
        this.kode = kode;
        this.nama = nama;
        this.kategori = kategori;
        this.stok = stok;
        setHarga(harga); // lewat setter, jadi ikut divalidasi
        Menu.jumlahMenu += 1; // dihitung hanya jika objek berhasil dibuat
    }

    /** Konstruktor tanpa stok: stok awal 0 (padanan stok=0 di versi Python). */
    public Menu(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0);
    }

    /** Banyaknya objek Menu yang berhasil dibuat. */
    public static int getJumlahMenu() {
        return jumlahMenu;
    }
```

- Semua *field* kini `private`. Kelas lain, termasuk `KedaiKita` yang berisi `main`, tidak bisa menyentuhnya secara langsung.
- Stok awal diperiksa paling awal. Stok negatif langsung ditolak.
- Harga disimpan **lewat *setter*** (`setHarga(harga)`) sehingga menu berharga 0 ditolak sejak dibuat.
- Penghitung naik di baris paling akhir. Menu yang gagal dibuat tidak ikut terhitung.
- Konstruktor 4 parameter masih memanggil konstruktor 5 parameter lewat `this(...)`, seperti di Pertemuan 03. Karena itu, pemeriksaan harga juga berlaku untuk konstruktor 4 parameter.

Kedua, *getter* dan *setter*. *Field* `kode`, `nama`, `kategori`, dan `stok` hanya punya *getter* (`getKode()`, `getNama()`, `getKategori()`, `getStok()`) sehingga keempatnya ***read-only*** dari luar. Hanya `harga` yang punya *setter*:

```java
    // ----- getter + setter dengan validasi -----
    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = harga;
    }
```

- *Setter* menolak harga nol atau negatif. Karena konstruktor memakai *setter* ini, aturan yang sama berlaku sejak menu dibuat.

Ketiga, *method* penjaga aturan untuk stok:

```java
    // ----- method pengubah stok -----
    public void tambahStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        stok += jumlah;
    }

    public void kurangiStok(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        if (jumlah > stok) {
            throw new IllegalArgumentException("Stok " + nama + " tidak cukup (sisa " + stok + ")");
        }
        stok -= jumlah;
    }
```

- Stok **tidak** punya *setter*. Restok memakai `tambahStok()`, penjualan memakai `kurangiStok()`.
- `kurangiStok()` menolak penjualan yang melebihi stok sehingga stok tidak pernah minus.
- *Method* `hitungTotal()`, `hargaSetelahDiskon()`, `stokCukup()`, dan `toString()` sama seperti Pertemuan 03. Bedanya, tiga *method* pertama kini diberi `public`. `toString()` memang sudah `public` sejak Pertemuan 03.

Keempat, kelas `Pelanggan`. *Field* `nama`, `noHp`, dan `poin` kini `private` dan hanya punya *getter* (*read-only*). Poinnya hanya berubah lewat dua *method* berikut:

```java
    public void tambahPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditambahkan harus lebih dari 0");
        }
        poin += jumlah;
    }

    /** Menukar poin menjadi potongan harga. 1 poin = Rp1.000. */
    public int tukarPoin(int jumlah) {
        if (jumlah > poin) {
            throw new IllegalArgumentException("Poin tidak cukup (sisa " + poin + ")");
        }
        poin -= jumlah;
        return jumlah * 1000;
    }
```

- `tambahPoin()` menolak jumlah nol atau negatif sehingga poin tidak bisa "dikurangi diam-diam" lewat pintu tambah.
- `tukarPoin()` adalah *method* penjaga aturan yang juga **mengembalikan nilai** `int`, yaitu besar potongan harga dalam rupiah.

Terakhir, cara `main` menangani data yang ditolak (potongan dari *method* `main`):

```java
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            new Menu("M09", "Menu Gratis", 0, "Minuman");
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat menu: " + e.getMessage());
        }
        System.out.println("Jumlah menu terdaftar tetap: " + Menu.getJumlahMenu());
```

`new Menu(...)` boleh ditulis tanpa disimpan ke variabel karena di sini kita hanya ingin melihat apakah objeknya berhasil dibuat. Pola `try`/`catch` yang sama dipakai untuk `setHarga()`, `kurangiStok()`, dan `tukarPoin()`. Kode lengkapnya ada di *file* studi kasus.

Cara menjalankan: buka *file* `studi-kasus/KedaiKita.java` di VS Code, lalu klik **Run** pada tulisan **Run | Debug** di atas baris `public static void main`. Bisa juga lewat terminal. Dari folder utama materi, ketik:

```bash
cd Pertemuan-04-Enkapsulasi/java/studi-kasus
java KedaiKita.java
```

***Output:***

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
Jumlah menu terdaftar: 3

=== DATA TIDAK VALID DITOLAK ===
Gagal membuat menu: Harga harus lebih dari 0
Jumlah menu terdaftar tetap: 3

=== MENGUBAH HARGA LEWAT SETTER ===
Harga Es Teh Manis naik menjadi Rp10.000
Gagal mengubah harga: Harga harus lebih dari 0
Harga Es Teh Manis tetap Rp10.000

=== MENGELOLA STOK ===
Stok awal Kopi Susu Gula Aren: 20
Terjual 5, stok sekarang 15
Restok 10, stok sekarang 25
Gagal menjual: Stok Kopi Susu Gula Aren tidak cukup (sisa 25)

=== POIN PELANGGAN ===
Budi Santoso (081234567890) - 0 poin
Budi Santoso (081234567890) - 12 poin
Tukar 10 poin -> potongan Rp10.000
Budi Santoso (081234567890) - 2 poin
Gagal menukar poin: Poin tidak cukup (sisa 2)
```

Perhatikan bahwa setiap penolakan meninggalkan data dalam keadaan **utuh**: jumlah menu tetap 3, harga es teh tetap Rp10.000, stok kopi tetap 25, dan poin Budi tetap 2. *Output* ini sama persis dengan versi Python.

> [!NOTE]
> Di *file* ini, kelas `Rupiah`, `Menu`, dan `Pelanggan` tidak diberi `public` karena dalam satu *file* Java hanya boleh ada satu kelas `public`, yaitu `KedaiKita`. Isi kelas-kelas itu (*field*, konstruktor, dan *method*) tetap diberi `public` atau `private` sesuai perannya. Mulai Pertemuan 05, setiap kelas punya *file* sendiri.

> [!TIP]
> **Coba sendiri:** salin `studi-kasus/KedaiKita.java` ke folder `PBO-latihan-saya/pertemuan-04/`. Di salinan itu, cari kelas `Menu` (mulai baris 102). Simpan dan jalankan salinan itu setelah setiap langkah.
>
> 1. Tambahkan `final` pada *field* `kode`, `nama`, dan `kategori`. Contohnya, ubah `private String kode;` menjadi `private final String kode;`. Apakah program masih berjalan?
> 2. Sekarang tambahkan `final` juga pada *field* `stok` (`private final int stok;`). Apa yang terjadi, dan mengapa?

<details>
<summary>Lihat jawaban</summary>

1. Program tetap berjalan dengan *output* yang sama. Ketiga *field* itu hanya diisi sekali di konstruktor dan tidak pernah diubah lagi, jadi cocok diberi `final`.
2. Kompilasi gagal dengan dua *error* `cannot assign a value to final variable stok`, yaitu di baris `stok += jumlah;` dan `stok -= jumlah;`. Stok **memang harus** berubah lewat `tambahStok()` dan `kurangiStok()`, jadi stok tidak boleh `final`. Hal yang sama berlaku untuk `harga` karena harga diubah oleh `setHarga()`.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Java punya dua jenis kesalahan:

- ***Error* saat kompilasi** (*compile error*): ditemukan sebelum program berjalan. Pesannya diawali nama *file* dan nomor baris, misalnya `KedaiKita.java:31: error: ...`. Tanda `^` menunjuk posisi kesalahannya. Jika program dijalankan dengan `java NamaFile.java`, di akhir pesan muncul juga baris `error: compilation failed`.
- ***Error* saat program berjalan** (*runtime error*): program sempat berjalan lalu berhenti. Pesannya diawali `Exception in thread "main"`.

Setiap kesalahan di bawah ini ditampilkan dalam dua blok: potongan kode yang salah (jangan ditiru) dan pesan yang muncul. Ingin mencobanya sendiri? Kerjakan di folder latihanmu, jangan di folder materi, dan coba satu kesalahan dalam satu waktu:

1. Salin `studi-kasus/KedaiKita.java` ke folder `PBO-latihan-saya/pertemuan-04/`. Untuk setiap kesalahan, mulailah dari salinan yang masih asli (salin ulang dan timpa salinan lama) agar nomor barisnya cocok dengan pesan di bawah.
2. Untuk kesalahan 1 sampai 4, cari baris `Menu nasiGoreng = new Menu(...);` (baris 30) di *method* `main` salinan itu. Tambahkan baris kesalahannya **tepat di bawahnya** sehingga baris itu menjadi baris 31. Kesalahan 5 dijelaskan langsung di bagiannya.
3. Simpan, lalu jalankan dari terminal yang sedang berada di folder latihan itu dengan perintah `java KedaiKita.java`.

Pesan-pesan di bawah ini adalah yang muncul di terminal. Jika kamu menjalankannya lewat tulisan **Run | Debug** di VS Code, kesalahan kompilasi biasanya tampil dengan cara lain: garis merah bergelombang di editor dan daftar pesan di panel **PROBLEMS**. Isi pesannya tetap sama.

### Kesalahan 1: Mengakses *field* `private` dari luar kelas

```java
        kopi.harga = -18000;
```

Pesan *error*-nya:

```text
KedaiKita.java:31: error: harga has private access in Menu
        kopi.harga = -18000;
            ^
1 error
error: compilation failed
```

**Artinya:** *field* `harga` adalah milik privat kelas `Menu`, sedangkan baris ini berada di kelas `KedaiKita`. **Perbaikan:** pakai pintu resminya, `kopi.setHarga(20000);`. *Setter* itu juga akan menolak nilai negatif.

### Kesalahan 2: Memanggil *setter* yang tidak ada

```java
        kopi.setKode("M10");
```

Pesan *error*-nya:

```text
KedaiKita.java:31: error: cannot find symbol
        kopi.setKode("M10");
            ^
  symbol:   method setKode(String)
  location: variable kopi of type Menu
1 error
error: compilation failed
```

**Artinya:** *compiler* mencari *method* `setKode(String)` di kelas `Menu` (*location: variable kopi of type Menu*), tetapi tidak menemukannya (*cannot find symbol*). Kode menu memang dirancang *read-only*. **Perbaikan:** jika kode memang tidak boleh berubah, hapus baris itu. Jika aturan bisnisnya berubah, tambahkan *setter* lengkap dengan validasinya.

### Kesalahan 3: Lupa tanda kurung pada *getter*

```java
        System.out.println(kopi.getHarga);
```

Pesan *error*-nya:

```text
KedaiKita.java:31: error: cannot find symbol
        System.out.println(kopi.getHarga);
                               ^
  symbol:   variable getHarga
  location: variable kopi of type Menu
1 error
error: compilation failed
```

**Artinya:** tanpa tanda kurung, Java mengira `getHarga` adalah nama ***field*** (*symbol: variable getHarga*), dan *field* seperti itu tidak ada. Kesalahan ini sering terjadi pada pemrogram yang terbiasa dengan *property* Python. **Perbaikan:** `kopi.getHarga()`.

### Kesalahan 4: *Exception* yang tidak ditangkap

```java
        new Menu("M09", "Menu Gratis", 0, "Minuman");
```

Kali ini kompilasi berhasil, tetapi program berhenti saat berjalan dengan pesan berikut:

```text
Exception in thread "main" java.lang.IllegalArgumentException: Harga harus lebih dari 0
	at Menu.setHarga(KedaiKita.java:158)
	at Menu.<init>(KedaiKita.java:120)
	at Menu.<init>(KedaiKita.java:126)
	at KedaiKita.main(KedaiKita.java:31)
```

**Artinya:** ini bukan *bug* pada kelas `Menu`. Justru validasinya **bekerja**: menu berharga 0 ditolak. Karena tidak ada `try`/`catch`, program berhenti. Pesan ini disebut *stack trace* dan dibaca dari atas ke bawah:

- Baris pertama: jenis *exception* (`IllegalArgumentException`) dan pesannya.
- `at Menu.setHarga(...)`: tempat *exception* dilempar, yaitu di dalam *setter*.
- `at Menu.<init>(...)`: `<init>` adalah cara Java menyebut **konstruktor**. Ada dua baris karena konstruktor 4 parameter memanggil konstruktor 5 parameter lewat `this(...)`.
- `at KedaiKita.main(KedaiKita.java:31)`: baris di program kita yang memulai semuanya.

**Perbaikan:** jangan mengirim data yang tidak valid, atau bungkus perintahnya dengan `try`/`catch` jika data berasal dari luar (misalnya *input* pengguna).

### Kesalahan 5: Memberi `private` pada kelas

Karena semangat "semua harus privat", seseorang mengubah baris 102, `class Menu {`, menjadi `private class Menu {`. Kamu bisa mencobanya di salinan `KedaiKita.java` yang masih asli. Pesan *error*-nya:

```text
KedaiKita.java:102: error: modifier private not allowed here
private class Menu {
        ^
1 error
error: compilation failed
```

**Artinya:** kelas tingkat atas (yang tidak berada di dalam kelas lain) hanya boleh `public` atau tanpa *access modifier*. **Perbaikan:** kembalikan menjadi `class Menu {`. Yang dibuat `private` adalah ***field*** di dalamnya, bukan kelasnya.

### Kesalahan 6: Mengubah *field* `final`

Lihat kembali bagian 5. Mengisi ulang *field* `final` di luar konstruktor ditolak dengan pesan `cannot assign a value to final variable nik`. **Perbaikan:** jika data itu memang perlu berubah, hapus `final` dan buat *setter* yang memeriksanya. Jika tidak perlu berubah, hapus kode yang mencoba mengubahnya.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi JDK. Fokuslah pada kata-kata kuncinya, seperti *has private access*, *cannot find symbol*, dan nama *exception*-nya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| *Field* privat | `private Tipe nama;` | `private int harga;` |
| *Field* yang tidak pernah berubah | `private final Tipe nama;` | `private final String nik;` |
| Konstruktor dan *method* publik | `public ...` | `public void setHarga(int harga)` |
| *Getter* | `public Tipe getNama() { return nama; }` | `kopi.getHarga()` |
| *Getter* `boolean` | `public boolean isNama() { ... }` | `parkiran.isPenuh()` |
| *Setter* | `public void setNama(Tipe nama) { ... }` | `kopi.setHarga(20000)` |
| *Read-only* | *getter* **tanpa** *setter* | `kopi.getKode()` |
| Menolak data | `throw new IllegalArgumentException("pesan");` | `throw new IllegalArgumentException("Harga harus lebih dari 0");` |
| Menangkap (intip) | `try { ... } catch (IllegalArgumentException e) { ... }` | `e.getMessage()` |
| Validasi di konstruktor | panggil *setter* di konstruktor | `setHarga(harga);` |
| *Field* `static` privat | `private static Tipe nama;` | `private static int jumlahMenu = 0;` |
| *Getter* `static` | `public static Tipe getNama()` | `Menu.getJumlahMenu()` |
| *Method* internal | `private Tipe nama(...)` | `private void periksaPassword(String password)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
