# ☕ Praktik Java — Pertemuan 02: Kelas dan Objek

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 02](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Kelas dan Objek Pertamamu](#1-kelas-dan-objek-pertamamu)
2. [Konstruktor](#2-konstruktor)
3. [Method: Memberi Objek Kemampuan](#3-method-memberi-objek-kemampuan)
4. [Parameter dan Nilai Kembalian](#4-parameter-dan-nilai-kembalian)
5. [Memahami `this`](#5-memahami-this)
6. [Setiap Objek Menyimpan Datanya Sendiri](#6-setiap-objek-menyimpan-datanya-sendiri)
7. [Banyak Objek dalam Array](#7-banyak-objek-dalam-array)
8. [Anatomi Kelas Java](#8-anatomi-kelas-java)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh kecil, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 02
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah **program satu file**. Sejak Java 11, program satu file bisa langsung dijalankan tanpa langkah kompilasi terpisah:

```bash
cd Pertemuan-02-Kelas-dan-Objek/java/contoh
java Contoh01KelasDanObjek.java
```

Cara klasik dua langkah (kompilasi dulu, lalu jalankan) juga tetap bisa dipakai:

```bash
javac Contoh01KelasDanObjek.java
java Contoh01KelasDanObjek
```

> [!IMPORTANT]
> Di setiap file contoh, kelas yang memiliki method `main` ditulis **paling atas**, dan kelas-kelas pembantunya (misalnya `Kucing`) ditulis di bawahnya. Urutan ini adalah syarat perintah `java NamaFile.java`: kelas pertama di dalam file harus punya `main`.

> [!TIP]
> Jika memakai VS Code, buka folder `java/` **milik pertemuan ini** (File → Open Folder), bukan seluruh repositori. Alasannya, setiap pertemuan punya kelas dengan nama yang sama (misalnya `Menu`), dan VS Code akan protes jika dua kelas bernama sama berada dalam satu proyek. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

Saran belajar: **ketik ulang** kodenya, jangan hanya menyalin. Jari yang mengetik membantu otak mengingat.

## 1. Kelas dan Objek Pertamamu

File: [`contoh/Contoh01KelasDanObjek.java`](contoh/Contoh01KelasDanObjek.java)

Kita mulai dari kelas yang paling sederhana: kelas `Kucing`.

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

**Output:**

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
- **[3]** Notasi titik `oyen.nama = "Oyen"` mengisi field `nama` **milik objek oyen**.
- **[4]** `oyen.nama` membaca field milik oyen. Ucapkan dalam hati: "nama milik oyen".
- **[5]** `getClass().getSimpleName()` memberi tahu nama kelas asal objek.
- **[6]** Operator `==` pada objek memeriksa apakah dua variabel menunjuk ke **objek yang sama**. Hasilnya tidak, karena `new` dipanggil dua kali sehingga tercipta dua objek berbeda.

> [!NOTE]
> Field yang belum diisi otomatis mendapat **nilai bawaan**: `null` untuk objek seperti `String`, `0` untuk `int`, dan `false` untuk `boolean`.

> [!TIP]
> **Coba sendiri:** hapus baris `belang.warna = "hitam putih";`, lalu jalankan lagi. Program tetap berjalan, tetapi tercetak `warnanya null`. Inilah masalah "objek setengah jadi" yang dibahas di halaman konsep. Konstruktor akan mencegahnya.

## 2. Konstruktor

File: [`contoh/Contoh02Konstruktor.java`](contoh/Contoh02Konstruktor.java)

Konstruktor di Java punya dua ciri khas: **namanya sama persis dengan nama kelas** dan **tidak punya tipe kembalian** (bahkan tidak `void`). Konstruktor dipanggil otomatis setiap kali objek dibuat dengan `new`.

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

Program utamanya:

```java
        System.out.println("=== MEMBUAT TIGA OBJEK MOBIL ===");
        Mobil mobilBudi = new Mobil("Avanza", "hitam", 2019); // [4] argumen dikirim ke konstruktor
        Mobil mobilSiti = new Mobil("Brio", "merah", 2022);
        Mobil mobilRina = new Mobil("Xpander", "putih", 2021);
```

**Output:**

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
- **[3]** `this.merek = merek` berarti: "field `merek` milik objek ini diisi dengan nilai parameter `merek`". Karena nama parameter dan nama field sama, `this.` wajib ditulis untuk membedakan keduanya.
- **[4]** `new Mobil("Avanza", "hitam", 2019)` membuat objek baru, lalu menjalankan konstruktor dengan argumen tersebut. Urutan dan tipe argumen harus cocok dengan parameter: `String`, `String`, `int`.

```text
new Mobil(  "Avanza",       "hitam",       2019  )
               |               |             |
               v               v             v
    Mobil(String merek,  String warna,  int tahun)
```

> [!NOTE]
> Jika sebuah kelas tidak menulis konstruktor sama sekali (seperti `Kucing` di contoh 01), Java otomatis menyediakan **konstruktor bawaan** tanpa parameter. Begitu kita menulis konstruktor sendiri, konstruktor bawaan itu tidak lagi disediakan.

## 3. Method: Memberi Objek Kemampuan

File: [`contoh/Contoh03Method.java`](contoh/Contoh03Method.java)

Method ditulis di dalam kelas dengan format: **tipe kembalian, nama method, lalu parameter**. Method yang tidak mengembalikan nilai memakai tipe `void`.

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

Program utamanya:

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

**Output:**

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

- **[1]** Tidak semua field harus berasal dari parameter. Setiap lampu baru otomatis dalam keadaan padam.
- **[2]** Method `nyalakan()` **mengubah keadaan** (*state*) objek. Di dalam method, kita boleh langsung menulis `menyala` tanpa `this.`, karena tidak ada parameter bernama sama. Java otomatis mengartikannya sebagai `this.menyala`.
- **[3]** Method `tampilkanStatus()` hanya **membaca** field.
- **[4]** Method dipanggil dengan notasi titik. Objek di sebelah kiri titik menjadi `this` di dalam method.

> [!NOTE]
> Nama method di Java memakai gaya **camelCase**: kata pertama huruf kecil, kata berikutnya diawali huruf kapital (`tampilkanStatus`, `hitungLuas`). Nama kelas memakai **PascalCase** (`Lampu`, `PersegiPanjang`).

> [!TIP]
> **Coba sendiri:** tambahkan method `saklar()` yang membalik keadaan lampu. Petunjuk: `menyala = !menyala;`.

## 4. Parameter dan Nilai Kembalian

File: [`contoh/Contoh04ParameterDanReturn.java`](contoh/Contoh04ParameterDanReturn.java)

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

Program utamanya:

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

**Output:**

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

- **[1]** `int` di depan nama method adalah **tipe kembalian**. Java memeriksa bahwa nilai yang di-`return` memang bertipe `int`.
- **[2]** Parameter ditulis lengkap dengan tipenya: `int faktor`. Method ini bertipe `void` karena tidak mengembalikan apa pun.
- **[3]** Nilai kembalian disimpan ke variabel `luas`, yang tipenya harus cocok (`int`).
- **[4]** Nilai kembalian juga bisa langsung dipakai dalam ekspresi.
- **[5]** Argumen `2` dikirim ke parameter `faktor`.

> [!IMPORTANT]
> Bedakan **mencetak** (`System.out.println`) dengan **mengembalikan** (`return`). Method yang mengembalikan nilai lebih fleksibel: hasilnya bisa dicetak, dijumlahkan, dibandingkan, atau disimpan.

> [!WARNING]
> Hati-hati saat menggabungkan teks dengan **penjumlahan**. `"Total: Rp" + 36000 + 25000` menghasilkan `Total: Rp3600025000`, karena Java menggabungkan dari kiri ke kanan: teks + angka menjadi teks, lalu ditambah angka lagi menjadi teks lagi. Bungkus penjumlahannya dengan kurung: `"Total: Rp" + (36000 + 25000)`. Perkalian dan pembagian tidak bermasalah karena selalu dikerjakan lebih dulu, tetapi menambahkan kurung tetap membuat kode lebih mudah dibaca.

## 5. Memahami `this`

File: [`contoh/Contoh05This.java`](contoh/Contoh05This.java)

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

Program utamanya:

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

**Output:**

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

- **[1]** Di dalam `gantiEmail`, nama `email` merujuk ke **parameter** (email baru), karena parameter "menutupi" field yang bernama sama. Untuk menyebut field-nya, kita wajib menulis `this.email`.
- **[2]** Method boleh memanggil method lain milik objek yang sama. `this.sapa()` dan `sapa()` sama artinya.
- **[3]** Method `tampilkanProfil` ditulis sekali, tetapi dijalankan dengan `this` yang berbeda, sehingga hasilnya berbeda.

| Kapan `this.` wajib? | Contoh |
|---|---|
| Nama parameter sama dengan nama field | `this.email = email;` |
| Tidak ada nama yang bentrok | boleh ditulis atau tidak: `this.sapa()` sama dengan `sapa()` |

## 6. Setiap Objek Menyimpan Datanya Sendiri

File: [`contoh/Contoh06ObjekMandiri.java`](contoh/Contoh06ObjekMandiri.java)

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

Program utamanya membuat rekening Budi (saldo awal 500000) dan Siti (saldo awal 750000), lalu melakukan beberapa transaksi.

**Output:**

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

Transaksi pada rekening Budi tidak menyentuh saldo Siti sama sekali. Method `tarik` juga **menjaga** agar saldo tidak menjadi negatif. Menjaga data agar tetap masuk akal adalah tugas penting sebuah kelas. Di Pertemuan 04 (Enkapsulasi), kita belajar cara menjaga data dengan lebih ketat.

## 7. Banyak Objek dalam Array

File: [`contoh/Contoh07DaftarObjek.java`](contoh/Contoh07DaftarObjek.java)

Objek bisa disimpan di dalam array. Tipe array-nya adalah nama kelas diikuti `[]`.

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

**Output:**

```text
=== PLAYLIST BELAJAR ===
- Indonesia Pusaka (Ismail Marzuki) 3:35
- Ampar-Ampar Pisang (Lagu Daerah Kalimantan Selatan) 2:12
- Bengawan Solo (Gesang) 3:07
Jumlah lagu : 3
Total durasi: 8 menit 54 detik
```

Penjelasan:

- **[1]** `Lagu[]` adalah array yang setiap elemennya bertipe `Lagu`. Objek dibuat langsung di dalam kurung kurawal.
- **[2]** Perulangan *for-each* (`for (Lagu lagu : playlist)`) membaca elemen satu per satu. Method yang sama dipanggil untuk setiap objek.

> [!NOTE]
> Ukuran array tetap (tidak bisa ditambah setelah dibuat). Wadah yang ukurannya bisa bertambah, yaitu `ArrayList`, kita pakai mulai Pertemuan 05.

## 8. Anatomi Kelas Java

Berikut rangkuman bagian-bagian sebuah kelas Java. Simpan gambar ini di kepala.

```text
class Menu {                                   <- kata kunci class + Nama kelas (PascalCase)
    String nama;                               <- field: tipe + nama, wajib dideklarasikan
    int harga;

    Menu(String nama, int harga) {             <- konstruktor: nama = nama kelas, tanpa tipe kembalian
        this.nama = nama;                      <- this.field = parameter
        this.harga = harga;
    }

    int hitungTotal(int jumlah) {              <- method: tipe kembalian + nama (camelCase) + parameter
        return harga * jumlah;
    }
}

Menu kopi = new Menu("Kopi Susu Gula Aren", 18000);   <- membuat objek dengan new
int total = kopi.hitungTotal(2);                      <- memanggil method dengan notasi titik
```

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/KedaiKita.java`](studi-kasus/KedaiKita.java)

Saatnya membangun KedaiKita versi pertama yang memakai kelas. Rancangannya sudah kita bahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-kelas-menu-pertama).

**Apa yang berubah dibanding Pertemuan 01?**

- Data menu tidak lagi disimpan di tiga array terpisah, tetapi di dalam objek `Menu`.
- Perhitungan total tidak lagi memakai method `static` yang lepas, tetapi method `hitungTotal()` milik setiap menu.

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

Cara menjalankan:

```bash
cd Pertemuan-02-Kelas-dan-Objek/java/studi-kasus
java KedaiKita.java
```

**Output:**

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

- **[1]** Konstruktor menerima `nama` dan `harga`, sehingga tidak ada menu yang lahir tanpa nama atau harga.
- **[2]** Field `nama` dan `harga` dideklarasikan di badan kelas beserta tipenya.
- **[3]** `tampilkanInfo()` bertipe `void`: ia mencetak, tetapi tidak mengembalikan apa pun.
- **[4]** `hitungTotal(int jumlah)` bertipe `int`: hasilnya bisa dijumlahkan di program utama.
- **[5]** Tiga objek dibuat dari satu kelas dengan `new`.
- **[6]** Method yang sama menghasilkan teks berbeda, karena `this`-nya berbeda.
- **[7]** Field `nama` dibaca langsung dengan notasi titik.
- **[8]** Hanya harga es teh yang berubah. Objek kopi tidak terpengaruh.

> [!NOTE]
> Di file ini, kelas `KedaiKita` ditulis lebih dulu karena memiliki `main`, lalu kelas `Menu` di bawahnya. Kelas `Menu` tidak diberi kata `public`, karena dalam satu file Java hanya boleh ada **satu** kelas `public`, dan namanya harus sama dengan nama file. Mulai Pertemuan 05, setiap kelas akan punya file sendiri.

> [!TIP]
> **Coba sendiri:** tambahkan menu keempat, `Mie Goreng Jawa` seharga 23000, lalu hitung pesanan Siti: 1 mie goreng dan 2 es teh (dengan harga es teh yang sudah naik). Berapa total yang harus Siti bayar?

<details>
<summary>Lihat jawaban</summary>

1 x 23000 + 2 x 10000 = **Rp43000**.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Java punya dua jenis kesalahan:

- **Error saat kompilasi** (*compile error*): ditemukan sebelum program berjalan. Pesannya diawali nama file dan nomor baris, misalnya `E1.java:3: error: ...`. Tanda `^` menunjuk posisi kesalahannya.
- **Error saat program berjalan** (*runtime error*): program sempat berjalan lalu berhenti. Pesannya diawali `Exception in thread "main"`.

### Kesalahan 1: Lupa menulis `new`

```java
Kucing oyen = Kucing();
```

```text
E1.java:3: error: cannot find symbol
        Kucing oyen = Kucing();
                      ^
  symbol:   method Kucing()
  location: class E1
1 error
```

**Artinya:** tanpa `new`, Java mengira `Kucing()` adalah pemanggilan **method** bernama `Kucing`, dan method itu tidak ada. **Perbaikan:** `Kucing oyen = new Kucing();`.

### Kesalahan 2: Memberi tipe kembalian pada konstruktor

```java
class Mobil {
    // ...
    void Mobil(String merek, String warna, int tahun) { // salah: ada void
        // ...
    }
}
```

```text
E2.java:3: error: constructor Mobil in class Mobil cannot be applied to given types;
        Mobil mobilBudi = new Mobil("Avanza", "hitam", 2019);
                          ^
  required: no arguments
  found:    String,String,int
  reason: actual and formal argument lists differ in length
1 error
```

**Artinya:** karena ada `void`, `Mobil(...)` dianggap method biasa, bukan konstruktor. Java lalu memakai konstruktor bawaan yang tidak menerima argumen (*required: no arguments*). **Perbaikan:** hapus kata `void`.

### Kesalahan 3: Lupa `this.` saat nama parameter sama dengan field

```java
    Menu(String nama, int harga) {
        nama = nama;
        harga = harga;
    }
```

Tidak ada error, tetapi outputnya:

```text
null - Rp0
```

**Artinya:** `nama = nama` mengisi parameter dengan dirinya sendiri. Field-nya tidak tersentuh, sehingga tetap bernilai bawaan (`null` dan `0`). Ini *bug* yang licin karena tidak ada pesan error. **Perbaikan:** `this.nama = nama;`.

### Kesalahan 4: Memanggil method pada variabel yang belum berisi objek

```java
        Menu kopi = null;
        kopi.tampilkanInfo();
```

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Menu.tampilkanInfo()" because "<local1>" is null
	at E4.main(E4.java:4)
```

**Artinya:** variabel `kopi` tidak menunjuk ke objek apa pun (`null`), jadi tidak ada yang bisa menjalankan method. Bagian `at E4.main(E4.java:4)` menunjukkan lokasinya: baris 4. Nama variabel kadang tertulis sebagai `<local1>`, kadang sebagai `kopi`, tergantung cara program dikompilasi. **Perbaikan:** pastikan variabel sudah diisi dengan `new Menu(...)`.

### Kesalahan 5: Jumlah argumen tidak sesuai konstruktor

```java
        Menu kopi = new Menu("Kopi Susu Gula Aren");
```

```text
E5.java:3: error: constructor Menu in class Menu cannot be applied to given types;
        Menu kopi = new Menu("Kopi Susu Gula Aren");
                    ^
  required: String,int
  found:    String
  reason: actual and formal argument lists differ in length
1 error
```

**Artinya:** konstruktor membutuhkan `String, int` (*required*), tetapi kita hanya mengirim `String` (*found*). **Perbaikan:** `new Menu("Kopi Susu Gula Aren", 18000)`.

### Kesalahan 6: Nama kelas `public` berbeda dengan nama file

Jika file `Salah.java` berisi `public class KedaiKita`, perintah `javac Salah.java` menolak:

```text
Salah.java:1: error: class KedaiKita is public, should be declared in a file named KedaiKita.java
```

**Perbaikan:** samakan nama file dengan nama kelas `public`-nya. Ingat, huruf besar dan kecil juga harus sama persis.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Mendefinisikan kelas | `class NamaKelas { ... }` | `class Menu { ... }` |
| Field (atribut) | `Tipe nama;` | `int harga;` |
| Konstruktor | `NamaKelas(parameter) { ... }` | `Menu(String nama, int harga) { ... }` |
| Mengisi field di konstruktor | `this.field = parameter;` | `this.harga = harga;` |
| Method tanpa nilai kembalian | `void nama(parameter) { ... }` | `void tampilkanInfo() { ... }` |
| Method dengan nilai kembalian | `Tipe nama(parameter) { return ...; }` | `int hitungTotal(int jumlah)` |
| Membuat objek | `NamaKelas var = new NamaKelas(argumen);` | `Menu kopi = new Menu("Kopi", 18000);` |
| Membaca field | `objek.field` | `kopi.harga` |
| Memanggil method | `objek.method(argumen)` | `kopi.hitungTotal(2)` |
| Array objek | `NamaKelas[] var = { ... };` | `Lagu[] playlist = { new Lagu(...) };` |
| Cek objek yang sama | `a == b` | `oyen == belang` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
