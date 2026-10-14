# ☕ Praktik Java Pertemuan 09: Polimorfisme

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 09](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Satu Perintah, Banyak Bentuk](#1-satu-perintah-banyak-bentuk)
2. [Koleksi Polimorfik dan Jenis Baru](#2-koleksi-polimorfik-dan-jenis-baru)
3. [*Upcasting*, *Downcasting*, dan `instanceof`](#3-upcasting-downcasting-dan-instanceof)
4. [Polimorfisme dari dalam Kelas](#4-polimorfisme-dari-dalam-kelas)
5. [Tanpa *Duck Typing*: Java Butuh Tipe Bersama](#5-tanpa-duck-typing-java-butuh-tipe-bersama)
6. [*Overloading Method* dan Konstruktor](#6-overloading-method-dan-konstruktor)
7. [*Overload* Dipilih saat Kompilasi, *Override* saat Berjalan](#7-overload-dipilih-saat-kompilasi-override-saat-berjalan)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (17, 21, atau 25), VS Code dengan **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md). Contoh 03 memakai bentuk `instanceof` yang baru ada sejak **Java 16**, jadi JDK yang lebih lama tidak cukup.

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh program satu file
├── studi-kasus/     <- KedaiKita versi Pertemuan 09 (satu kelas per file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara Menjalankan Contoh

Setiap contoh adalah **program satu *file***: kelas yang memiliki `main` ditulis paling atas, lalu kelas-kelas pembantunya di bawahnya. Pilih salah satu cara berikut. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-09-Polimorfisme/java`. Buka folder ini saja, bukan seluruh materi. VS Code menganggap semua *file* `.java` di folder yang dibuka sebagai satu proyek, padahal pertemuan lain punya kelas bernama sama, misalnya `Menu` atau `Pesanan`. Di panel **Explorer**, buka folder `contoh`, klik *file* yang ingin dicoba (misalnya `Contoh01SatuPerintahBanyakBentuk.java`), lalu klik tulisan **Run** di atas baris `public static void main` (bagian dari **Run | Debug**) atau tombol ▷ di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** (kadang **DEBUG CONSOLE**) di bagian bawah. Jika tulisan **Run** belum muncul, tunggu beberapa detik sampai ekstensi Java selesai memuat folder itu.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-09-Polimorfisme/java/contoh` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
java Contoh01SatuPerintahBanyakBentuk.java
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di [bagian 1](#1-satu-perintah-banyak-bentuk). Untuk contoh lain, ganti nama *file*-nya, misalnya `java Contoh02KoleksiPolimorfik.java`. *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!IMPORTANT]
> Di dalam satu folder `java/`, setiap nama kelas harus unik. Itulah sebabnya setiap contoh memakai nama kelas yang berbeda-beda, dan solusi Latihan 5 memakai nama seperti `PembayaranKedai` agar tidak bentrok dengan kelas `Pembayaran` milik studi kasus.

### Cara Menjalankan Studi Kasus

Studi kasus terdiri atas banyak *file*, satu kelas per *file*. Program utamanya ada di `Main.java`.

- **Cara 1:** di VS Code, buka `studi-kasus/Main.java`, lalu klik **Run**. VS Code mengompilasi *file* lain yang dibutuhkan secara otomatis.
- **Cara 2:** masuk dulu ke folder `studi-kasus`, kompilasi semua *file*, lalu jalankan kelas `Main`.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi | `cd Pertemuan-09-Polimorfisme/java/studi-kasus` |
| folder `java` pertemuan ini | `cd studi-kasus` |

Setelah itu jalankan dua perintah ini:

```bash
javac *.java
java Main
```

`javac *.java` mengompilasi **semua** *file* `.java` di folder itu sekaligus. Jika berhasil, perintah ini tidak menampilkan apa-apa. `java Main` ditulis **tanpa** akhiran `.java`. Baris pertama yang muncul adalah `=== MENU KedaiKita ===`, dan *output* lengkapnya ada di [bagian 8](#8-studi-kasus-kedaikita). Setiap kali kode studi kasus diubah, jalankan `javac *.java` lagi sebelum `java Main`.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Perintah `java` dan `javac` sama di Windows, macOS, dan Linux.

### Tempat Menyimpan Kodemu Sendiri

Anggap folder materi sebagai buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Semua percobaan di halaman ini ("Coba sendiri" dan percobaan pesan *error*) dikerjakan di folder milikmu sendiri **di luar** folder materi, satu folder untuk setiap pertemuan. Alasannya ada di aturan emas [Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

```text
Documents/
├── PBO2026/                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/
    └── pertemuan-09/         <- salinan contoh, Coba.java, dan jawaban latihanmu
```

Polanya selalu sama: salin *file* contoh ke folder `pertemuan-09` (lewat File Explorer di Windows atau Finder di macOS), buka salinannya, ubah, simpan, jalankan, lalu bandingkan hasilnya dengan yang diharapkan. Jangan ganti nama *file*-nya: nama *file* Java harus sama dengan nama kelas `public` di dalamnya. Buka folder `pertemuan-09` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**). Terminal di jendela itu (**Terminal → New Terminal**) langsung berada di folder `pertemuan-09`, jadi kamu cukup mengetik `java NamaFile.java`.

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Kode yang ditampilkan bisa berupa satu kelas utuh dari *file* itu atau **potongan**. Potongan dari dalam *method* `main` tampil menjorok 8 spasi karena aslinya berada di dalam kelas dan di dalam `main`. Untuk mencoba, jalankan *file* lengkapnya, jangan mengetik ulang potongannya.
- Tanda `// [1]`, `// [2]`, dan seterusnya di komentar kode dijelaskan di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* materi itu dijalankan. Blok berlabel **Hasilnya:** adalah hasil percobaan yang kamu buat sendiri di folder `pertemuan-09`.

## 1. Satu Perintah, Banyak Bentuk

*File*: [`contoh/Contoh01SatuPerintahBanyakBentuk.java`](contoh/Contoh01SatuPerintahBanyakBentuk.java)

Kita mulai dari contoh klasik: hewan-hewan yang bersuara. Berikut potongan *file*-nya, dimulai dari kelas yang memiliki `main` (kelas ini ditulis utuh):

```java
public class Contoh01SatuPerintahBanyakBentuk {

    static void suruhBersuara(Hewan hewan) { // [3] parameter bertipe kelas induk
        String jenis = hewan.getClass().getSimpleName();
        System.out.println(hewan.getNama() + " si " + jenis + ": " + hewan.bersuara()); // [4]
    }

    public static void main(String[] args) {
        System.out.println("=== SATU VARIABEL, BERGANTI OBJEK ===");
        Hewan hewan = new Kucing("Oyen"); // [5] tipe variabel Hewan, objeknya Kucing
        System.out.println(hewan.bersuara());
        hewan = new Anjing("Bruno"); // sekarang menunjuk objek Anjing
        System.out.println(hewan.bersuara()); // baris yang sama persis, hasilnya berbeda

        System.out.println();
        System.out.println("=== SATU PERINTAH UNTUK SEMUA HEWAN ===");
        List<Hewan> kebun = List.of(new Kucing("Oyen"), new Anjing("Bruno"),
                new Bebek("Kuning"), new Ikan("Koki")); // [6]
        for (Hewan satwa : kebun) {
            suruhBersuara(satwa);
        }
    }
}
```

Kelas-kelas hewannya ditulis di bawahnya. `Anjing` dan `Bebek` ditulis dengan pola yang sama seperti `Kucing`, sedangkan `Ikan` hanya berisi konstruktor, tanpa `bersuara()`.

```java
/** Kelas induk semua hewan. */
class Hewan {
    private String nama;

    public Hewan(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String bersuara() {
        return "(diam saja)"; // [1] versi umum milik induk
    }
}

class Kucing extends Hewan {
    public Kucing(String nama) {
        super(nama);
    }

    @Override // [2] override: versi khusus kucing
    public String bersuara() {
        return "Meong!";
    }
}
```

***Output:***

```text
=== SATU VARIABEL, BERGANTI OBJEK ===
Meong!
Guk guk!

=== SATU PERINTAH UNTUK SEMUA HEWAN ===
Oyen si Kucing: Meong!
Bruno si Anjing: Guk guk!
Kuning si Bebek: Kwek kwek!
Koki si Ikan: (diam saja)
```

Penjelasan:

- **[1]** `Hewan` menyediakan versi **umum** dari `bersuara()`. Versi ini dipakai oleh kelas anak yang tidak menulis versinya sendiri.
- **[2]** `Kucing`, `Anjing`, dan `Bebek` meng-*override* `bersuara()`. Anotasi `@Override` meminta *compiler* memastikan *method* ini benar-benar menimpa *method* induk.
- **[3]** Parameter bertipe `Hewan` mau menerima objek `Kucing`, `Anjing`, `Bebek`, atau `Ikan` karena semuanya **adalah** `Hewan`.
- **[4]** Inilah inti polimorfisme. `suruhBersuara` tidak tahu jenis hewannya, tetapi `hewan.bersuara()` selalu menjalankan versi milik **objek** yang sebenarnya.
- **[5]** **Tipe variabel** `hewan` adalah `Hewan`, sedangkan **tipe objeknya** `Kucing`. Menyimpan objek anak di variabel bertipe induk disebut ***upcasting***, dan Java melakukannya otomatis. Baris `System.out.println(hewan.bersuara())` ditulis sama dua kali, tetapi hasilnya berbeda.
- **[6]** `List<Hewan>` berisi empat objek dari empat kelas berbeda. `Ikan` tidak meng-*override*, jadi Java naik ke kelas induk dan memakai `(diam saja)`.

Aturan emasnya:

| Pertanyaan | Ditentukan oleh |
|---|---|
| *Method* apa saja yang **boleh dipanggil**? | **Tipe variabel** (diperiksa *compiler*) |
| Versi *method* mana yang **dijalankan**? | **Tipe objek** (dipilih saat program berjalan) |

> [!TIP]
> **Coba sendiri:** salin `contoh/Contoh01SatuPerintahBanyakBentuk.java` ke folder `pertemuan-09` milikmu, lalu buka salinannya. Di bagian paling bawah *file*, tambahkan kelas `Sapi extends Hewan` dengan konstruktor yang memanggil `super(nama)` dan *method* `bersuara()` yang mengembalikan `"Mooo!"`. Lalu tambahkan `new Sapi("Belang")` di akhir `List.of(...)` milik `kebun`. Simpan, jalankan, dan perhatikan: apakah `suruhBersuara` perlu diubah?

<details>
<summary>Lihat jawaban</summary>

Tidak perlu. Di akhir *output* muncul baris baru `Belang si Sapi: Mooo!` tanpa menyentuh `suruhBersuara` sedikit pun. Kelas tambahannya cukup seperti ini:

```java
class Sapi extends Hewan {
    public Sapi(String nama) {
        super(nama);
    }

    @Override
    public String bersuara() {
        return "Mooo!";
    }
}
```

Inilah keuntungan utama polimorfisme yang dibahas di bagian berikutnya.

</details>

## 2. Koleksi Polimorfik dan Jenis Baru

*File*: [`contoh/Contoh02KoleksiPolimorfik.java`](contoh/Contoh02KoleksiPolimorfik.java)

Sekarang kita buktikan bahwa jenis baru bisa ditambahkan tanpa mengubah kode pemanggil. Berikut potongan *file*-nya, dimulai dari kelas induk:

```java
/** Kelas induk semua bangun datar. */
class BangunDatar {

    public String nama() {
        return "Bangun datar";
    }

    public int luas() {
        return 0; // [1] bangun datar "umum" tidak punya rumus luas
    }
}
```

Kelas anak `Persegi`, `PersegiPanjang`, dan `Segitiga` masing-masing meng-*override* `nama()` dan `luas()` dengan `@Override`. Misalnya, `luas()` milik `Segitiga` mengembalikan `alas * tinggi / 2`. Kelas baru `Trapesium` (ditandai `// [2] cukup menulis kelas baru`) ditulis di bagian paling bawah *file* dengan pola yang sama. Lalu *method* laporan di kelas utama:

```java
    static void cetakLaporan(List<BangunDatar> daftar) { // [3] tidak kenal kelas anak mana pun
        int total = 0;
        for (BangunDatar bangun : daftar) {
            int luas = bangun.luas(); // [4] versi luas() milik objek yang sebenarnya
            System.out.println(String.format("%-30s luas %4d cm2", bangun.nama(), luas));
            total += luas;
        }
        System.out.println("Total luas: " + total + " cm2");
    }
```

Di `main`, `daftar` bertipe `List<BangunDatar>` dan mula-mula diisi `Persegi`, `PersegiPanjang`, dan `Segitiga` (ditandai `// [5]`). Setelah laporan pertama, dua objek lagi ditambahkan:

```java
        daftar.add(new Trapesium(6, 10, 4)); // [6] cetakLaporan() tidak diubah
        daftar.add(new BangunDatar());
        cetakLaporan(daftar);
```

***Output:***

```text
=== LAPORAN AWAL: TIGA JENIS ===
Persegi 10x10                  luas  100 cm2
Persegi panjang 12x5           luas   60 cm2
Segitiga alas 8 tinggi 6       luas   24 cm2
Total luas: 184 cm2

=== SETELAH ADA JENIS BARU ===
Persegi 10x10                  luas  100 cm2
Persegi panjang 12x5           luas   60 cm2
Segitiga alas 8 tinggi 6       luas   24 cm2
Trapesium 6/10 tinggi 4        luas   32 cm2
Bangun datar                   luas    0 cm2
Total luas: 216 cm2
```

Penjelasan:

- **[1]** Versi induk mengembalikan 0 karena bangun datar "umum" tidak punya rumus luas.
- **[2]** Menambah jenis baru cukup dengan **menulis kelas baru**. Tidak ada kode lama yang diubah.
- **[3]** Parameter `List<BangunDatar>` berarti "daftar berisi bangun datar jenis apa pun". Isi *method* ini tidak menyebut `Persegi`, `Segitiga`, atau `Trapesium` sama sekali.
- **[4]** Setiap putaran memanggil `luas()` dan `nama()` milik objek yang sedang diproses.
- **[5]** `List<BangunDatar>` boleh diisi objek kelas anak mana pun. Inilah **koleksi polimorfik**.
- **[6]** `Trapesium` ikut dihitung dengan benar walaupun `cetakLaporan` ditulis sebelum kelas itu ada.

> [!NOTE]
> Baris `Bangun datar ... luas 0` terasa janggal. Objek `new BangunDatar()` memang tidak seharusnya bisa dibuat. Di Pertemuan 10, kita membuat kelas seperti ini menjadi **kelas abstrak** sehingga *compiler* menolak pembuatan objeknya.

## 3. *Upcasting*, *Downcasting*, dan `instanceof`

*File*: [`contoh/Contoh03UpcastingDowncasting.java`](contoh/Contoh03UpcastingDowncasting.java)

Kadang sebuah kelas anak punya *method* **khusus** yang tidak dimiliki saudaranya. Di contoh ini, hanya `Mahasiswa` yang punya `isiKrs()`, dan hanya `Dosen` yang punya `inputNilai()`. Keduanya sama-sama meng-*override* `peran()` dan `menuUtama()` milik `Pengguna`. Berikut potongan *file*-nya, yaitu *method* khusus di kelas `Mahasiswa`:

```java
    public String isiKrs(int sks) { // method KHUSUS mahasiswa
        return getNama() + " (" + nim + ") mengisi KRS " + sks + " SKS";
    }
```

Kelas `Dosen` serupa, dengan *method* khusus `inputNilai(String mataKuliah, String nilai)`. Potongan berikutnya adalah bagian awal *method* `main`:

```java
    public static void main(String[] args) {
        List<Pengguna> daftar = List.of(
                new Mahasiswa("Ayu Lestari", "2409106001"), // [1] upcasting otomatis
                new Dosen("Rahmat Hidayat", "198003152005011002"),
                new Mahasiswa("Bima Saputra", "2409106002"));

        System.out.println("=== SEMUA PENGGUNA LOGIN ===");
        for (Pengguna pengguna : daftar) { // [2] method bersama: aman untuk semua pengguna
            System.out.println(pengguna.getNama() + " [" + pengguna.peran() + "] menu: "
                    + pengguna.menuUtama());
        }

        System.out.println();
        System.out.println("=== FITUR KHUSUS: CEK JENIS DULU ===");
        for (Pengguna pengguna : daftar) {
            if (pengguna instanceof Mahasiswa) { // [3] pastikan dulu jenisnya
                Mahasiswa mhs = (Mahasiswa) pengguna; // [4] downcasting (cara klasik)
                System.out.println(mhs.isiKrs(21));
            } else if (pengguna instanceof Dosen dosen) { // [5] cek + cast sekaligus (Java 16+)
                System.out.println(dosen.inputNilai("PBO", "A"));
            }
        }
```

Bagian terakhir `main` memeriksa objek Ayu dengan `instanceof Mahasiswa`, `instanceof Pengguna` (ditandai `// [6]`), dan `instanceof Dosen`.

***Output:***

```text
=== SEMUA PENGGUNA LOGIN ===
Ayu Lestari [Mahasiswa] menu: Profil, KRS, KHS
Rahmat Hidayat [Dosen] menu: Profil, Input Nilai, Jadwal Mengajar
Bima Saputra [Mahasiswa] menu: Profil, KRS, KHS

=== FITUR KHUSUS: CEK JENIS DULU ===
Ayu Lestari (2409106001) mengisi KRS 21 SKS
Rahmat Hidayat memasukkan nilai PBO: A
Bima Saputra (2409106002) mengisi KRS 21 SKS

=== CEK JENIS IKUT MENGENAL INDUK ===
Ayu termasuk Mahasiswa? ya
Ayu termasuk Pengguna?  ya
Ayu termasuk Dosen?     tidak
```

Penjelasan:

- **[1]** ***Upcasting***: objek `Mahasiswa` dan `Dosen` dimasukkan ke `List<Pengguna>`. Java melakukannya otomatis karena setiap mahasiswa dan dosen **adalah** pengguna.
- **[2]** Lewat variabel bertipe `Pengguna`, kita hanya boleh memanggil *method* milik `Pengguna`. Hasilnya tetap polimorfik.
- **[3]** `instanceof` memeriksa apakah objek yang ditunjuk `pengguna` adalah `Mahasiswa` (atau anak dari `Mahasiswa`).
- **[4]** ***Downcasting*** dengan cara klasik: *cast* `(Mahasiswa) pengguna` meminta *compiler* memandang objek itu sebagai `Mahasiswa`, lalu hasilnya disimpan ke variabel `mhs`. Setelah itu, `isiKrs()` boleh dipanggil. Saat program berjalan, Java tetap memeriksa apakah objeknya memang `Mahasiswa`. Jika bukan, program berhenti dengan `ClassCastException` (lihat di bawah).
- **[5]** Bentuk modern sejak Java 16 (disebut *pattern matching for instanceof*). `pengguna instanceof Dosen dosen` memeriksa jenis **sekaligus** membuat variabel `dosen` bertipe `Dosen`. Variabel itu hanya berlaku di dalam cabang yang pemeriksaannya bernilai benar. Lebih ringkas, dan kita tidak mungkin lupa memeriksa sebelum *cast*.
- **[6]** `instanceof` juga menjawab "ya" untuk kelas induk karena setiap mahasiswa **adalah** pengguna.

Mengapa *cast* dibutuhkan? Karena *compiler* hanya melihat **tipe variabel**. Baginya, `pengguna` hanyalah `Pengguna`, dan kelas `Pengguna` tidak punya `isiKrs()`. Jika kita langsung menulis `pengguna.isiKrs(21)`, kompilasi gagal (lihat [Kesalahan 1](#kesalahan-1-memanggil-method-khusus-lewat-variabel-bertipe-induk)).

| Arah | Contoh | Perlu ditulis? | Aman? |
|---|---|---|---|
| *Upcasting* | `Pengguna p = new Mahasiswa(...);` | Tidak, otomatis | Selalu |
| *Downcasting* | `Mahasiswa m = (Mahasiswa) p;` | Ya, wajib *cast* | Hanya jika objeknya memang `Mahasiswa` |

Jika *cast* lupa ditulis (`Mahasiswa m = p;`), kompilasi gagal dengan pesan `incompatible types: Pengguna cannot be converted to Mahasiswa`. *Compiler* tidak bisa menjamin setiap `Pengguna` adalah `Mahasiswa`, jadi kita wajib menyatakannya secara eksplisit.

### Jika *downcasting* salah tebak: `ClassCastException`

*Cast* bukan sihir. *Cast* tidak mengubah objek, melainkan hanya cara kita memandangnya. Jika objeknya ternyata **bukan** kelas yang kita tebak, Java menghentikan program saat berjalan.

Buktikan sendiri. Salin `contoh/Contoh03UpcastingDowncasting.java` ke folder `pertemuan-09` milikmu, lalu buka salinannya. Di akhir *method* `main`, tepat setelah baris yang mencetak `Ayu termasuk Dosen?`, tambahkan tiga baris berikut:

```java
        Pengguna p = new Dosen("Rahmat Hidayat", "198003152005011002");
        Mahasiswa m = (Mahasiswa) p;
        System.out.println(m.isiKrs(21));
```

Kode ini lolos kompilasi karena secara teori sebuah `Pengguna` *mungkin saja* seorang `Mahasiswa`. Simpan, lalu jalankan dengan `java Contoh03UpcastingDowncasting.java`. Semua baris *output* biasa tercetak dulu, lalu program berhenti. Hasilnya (bagian akhir):

```text
Ayu termasuk Dosen?     tidak
Exception in thread "main" java.lang.ClassCastException: class Dosen cannot be cast to class Mahasiswa (Dosen and Mahasiswa are in unnamed module of loader com.sun.tools.javac.launcher.Main$MemoryClassLoader @35ef1869)
	at Contoh03UpcastingDowncasting.main(Contoh03UpcastingDowncasting.java:55)
```

**Artinya:** objek yang ditunjuk `p` adalah `Dosen`, dan seorang dosen tidak bisa dipandang sebagai mahasiswa. Baris `at ...` menunjukkan lokasinya: *method* `main`, baris 55, yaitu baris *cast*. Bagian di dalam kurung hanya keterangan teknis tentang pemuat kelas. Isinya bisa berbeda di komputermu: kode setelah `@` berubah setiap kali program dijalankan, dan jika program dijalankan lewat tombol **Run** VS Code, bagian itu berbunyi `loader 'app'`. **Perbaikan:** selalu periksa dengan `instanceof` sebelum *downcasting*, atau pakai bentuk `instanceof Mahasiswa m` yang memeriksa sekaligus melakukan *cast*.

> [!NOTE]
> *Compiler* Java cukup cerdas untuk menolak *cast* yang **mustahil**. Jika variabelnya sudah bertipe `Mahasiswa`, misalnya `Mahasiswa mhsAyu = new Mahasiswa("Ayu Lestari", "2409106001");`, maka menulis `(Dosen) mhsAyu` langsung gagal dikompilasi dengan pesan `incompatible types: Mahasiswa cannot be converted to Dosen`. Alasannya, seorang `Mahasiswa` tidak mungkin sekaligus `Dosen`. Secara sederhana, `ClassCastException` terjadi ketika tipe variabelnya induk sehingga *compiler* belum bisa memastikan isinya.

> [!WARNING]
> Gunakan `instanceof` dan *cast* hanya untuk *method* yang benar-benar **khusus**. Untuk perilaku yang dimiliki semua jenis, cukup *override* lalu panggil langsung seperti di **[2]**. Kode yang penuh `if (x instanceof A) ... else if (x instanceof B) ...` adalah tanda rancangan belum memanfaatkan polimorfisme.

## 4. Polimorfisme dari dalam Kelas

*File*: [`contoh/Contoh04PolimorfismeDariDalamKelas.java`](contoh/Contoh04PolimorfismeDariDalamKelas.java)

*Method* `tulis()` hanya ditulis sekali, di kelas induk. Namun, hasilnya berbeda untuk setiap jenis kartu. Berikut potongan *file*-nya, dimulai dari kelas induk:

```java
/** Kartu ucapan umum. Kerangka tulis() sama untuk semua jenis kartu. */
class KartuUcapan {
    private String penerima;
    private String pengirim;

    public KartuUcapan(String penerima, String pengirim) {
        this.penerima = penerima;
        this.pengirim = pengirim;
    }

    public String getPenerima() {
        return penerima;
    }

    public String salam() {
        return "Halo, " + penerima + "!";
    }

    public String isi() {
        return "Semoga harimu menyenangkan.";
    }

    public void tulis() { // [1] method induk yang memanggil method lain milik objek ini
        System.out.println("-".repeat(40));
        System.out.println(salam()); // [2] artinya this.salam(): versi siapa? tergantung objeknya
        System.out.println(isi());
        System.out.println("Salam hangat, " + pengirim);
        System.out.println("-".repeat(40));
    }
}
```

`KartuUlangTahun` menyimpan `umur` dan hanya meng-*override* `isi()` (ditandai `// [3]`). Kelas ketiga:

```java
class KartuWisuda extends KartuUcapan {
    public KartuWisuda(String penerima, String pengirim) {
        super(penerima, pengirim);
    }

    @Override // [4] salam() dan isi() sama-sama di-override
    public String salam() {
        return "Selamat, " + getPenerima() + ", S.Kom.!";
    }

    @Override
    public String isi() {
        return "Perjuanganmu terbayar lunas. " + super.isi(); // [5]
    }
}
```

Program utamanya membuat tiga kartu (umum, ulang tahun, dan wisuda) di dalam `List<KartuUcapan>`, lalu memanggil `kartu.tulis()` untuk masing-masing.

***Output:***

```text
=== Kartu 1: KartuUcapan ===
----------------------------------------
Halo, Siti!
Semoga harimu menyenangkan.
Salam hangat, Budi
----------------------------------------

=== Kartu 2: KartuUlangTahun ===
----------------------------------------
Halo, Rina!
Selamat ulang tahun yang ke-20!
Salam hangat, Ayu
----------------------------------------

=== Kartu 3: KartuWisuda ===
----------------------------------------
Selamat, Dimas, S.Kom.!
Perjuanganmu terbayar lunas. Semoga harimu menyenangkan.
Salam hangat, Keluarga di Samarinda
----------------------------------------
```

Penjelasan:

- **[1]** `tulis()` adalah **kerangka** yang sama untuk semua kartu: garis, salam, isi, pengirim, garis. `"-".repeat(40)` membuat teks berisi 40 tanda minus.
- **[2]** Di dalam *method*, `salam()` sama artinya dengan `this.salam()`. Saat objek `KartuWisuda` menjalankan `tulis()`, `this` adalah objek kartu wisuda itu, jadi versi `KartuWisuda` yang dipanggil.
- **[3]** (di `KartuUlangTahun`) Hanya `isi()` yang di-*override*. Salamnya tetap versi induk (`Halo, Rina!`).
- **[4]** `KartuWisuda` meng-*override* keduanya. *Field* `penerima` bersifat `private` di induk, jadi kelas anak membacanya lewat `getPenerima()`.
- **[5]** Gaya "memperluas" dari Pertemuan 07: menambahkan kalimat, lalu memakai versi induk lewat `super.isi()`.
- **[6]** (di `main`) Program utama hanya memanggil `tulis()`. Ia tidak tahu bahwa di dalamnya terjadi polimorfisme.

Jejak eksekusi untuk kartu ketiga:

```text
kartu.tulis()          -> tulis() milik KartuUcapan (KartuWisuda tidak menulis versinya sendiri)
  salam()              -> this adalah KartuWisuda -> "Selamat, Dimas, S.Kom.!"
  isi()                -> this adalah KartuWisuda -> isi() milik KartuWisuda
    super.isi()        -> isi() milik KartuUcapan -> "Semoga harimu menyenangkan."
```

## 5. Tanpa *Duck Typing*: Java Butuh Tipe Bersama

*File*: [`contoh/Contoh05TipeBersama.java`](contoh/Contoh05TipeBersama.java)

Di Python, objek-objek yang **tidak bersaudara** tetap bisa diproses bersama, asalkan sama-sama punya *method* yang dipanggil. Gaya ini disebut ***duck typing*** (lihat [halaman konsep](../README.md#7-duck-typing-yang-penting-bisa-bukan-siapa)). Bagaimana di Java? Tanpa induk bersama, satu-satunya tipe yang bisa menampung ayam jago, alarm, dan kentongan sekaligus adalah `Object`, kelas akar semua kelas. Kita coba simpan objek `AyamJago` di variabel bertipe `Object`, lalu suruh berbunyi.

Salin `contoh/Contoh05TipeBersama.java` ke folder `pertemuan-09` milikmu, lalu buka salinannya. Tambahkan dua baris berikut di awal *method* `main`, tepat di atas baris yang mencetak `=== PAGI DI ASRAMA ===`:

```java
        Object benda = new AyamJago();
        System.out.println(benda.bunyikan());
```

Simpan, lalu jalankan dengan `java Contoh05TipeBersama.java`. Hasilnya:

```text
Contoh05TipeBersama.java:33: error: cannot find symbol
        System.out.println(benda.bunyikan());
                                ^
  symbol:   method bunyikan()
  location: variable benda of type Object
1 error
error: compilation failed
```

**Artinya:** `cannot find symbol` berarti "nama ini tidak ditemukan". *Compiler* tidak menemukan *method* `bunyikan()` (`symbol`) pada variabel `benda` yang bertipe `Object` (`location`). Padahal, di *file* itu `AyamJago` sebenarnya punya `bunyikan()`. *Compiler* hanya melihat tipe variabel `Object`, dan kelas `Object` tidak punya `bunyikan()`. Java tidak mau "berharap" objeknya punya *method* itu. Baris terakhir, `error: compilation failed`, muncul karena kita memakai `java NamaFile.java`. Solusinya: beri semua kelas **tipe bersama** yang punya `bunyikan()`, seperti di *file* contoh 05 berikut (potongan):

```java
/** Tipe bersama: "tiket masuk" agar objek-objek berbeda bisa diperlakukan sama. */
class SumberBunyi { // [1]
    public String bunyikan() {
        return "...";
    }
}

class AyamJago extends SumberBunyi { // [2] wajib menyebut induk bersamanya
    @Override
    public String bunyikan() {
        return "Kukuruyuuuk!";
    }
}
```

`AlarmPonsel`, `Kentongan`, dan `BelSekolah` juga `extends SumberBunyi`. Di kelas utama, `main` memanggil *method* berikut dengan `List.of(new AyamJago(), new AlarmPonsel("05.00"), new Kentongan())`, lalu dengan daftar kedua:

```java
    static void bangunkanSemua(List<SumberBunyi> daftar) { // [3] tipe bersama wajib disebut
        for (SumberBunyi benda : daftar) {
            String nama = benda.getClass().getSimpleName();
            System.out.println(String.format("%-12s: %s", nama, benda.bunyikan())); // [4]
        }
    }
```

***Output:***

```text
=== PAGI DI ASRAMA ===
AyamJago    : Kukuruyuuuk!
AlarmPonsel : Kriiing! Sudah pukul 05.00
Kentongan   : Tung tung tung!

=== PAGI DI SEKOLAH ===
BelSekolah  : Teeet! Waktunya masuk kelas
AlarmPonsel : Kriiing! Sudah pukul 06.45
```

Penjelasan:

- **[1]** `SumberBunyi` adalah tipe bersama. Isinya hanya versi umum `bunyikan()`.
- **[2]** Setiap kelas wajib menyatakan dirinya anak `SumberBunyi`. Tanpa itu, objeknya tidak bisa masuk `List<SumberBunyi>`.
- **[3]** Parameter *method* wajib menyebut tipe bersama itu.
- **[4]** Pemanggilan `bunyikan()` tetap polimorfik, sama seperti contoh-contoh sebelumnya.

*Output*-nya sama persis dengan versi *duck typing* di Python. Bedanya, Java memastikan **sebelum program berjalan** bahwa setiap objek pasti punya `bunyikan()`. Di Python, objek tanpa `bunyikan()` baru ketahuan saat program berjalan (`AttributeError`).

> [!NOTE]
> Kalimat "ayam jago **adalah** sumber bunyi" terdengar dipaksakan, bukan? Ayam jago, alarm, dan kentongan tidak benar-benar bersaudara. Mereka hanya punya **kemampuan** yang sama: bisa berbunyi. Untuk kebutuhan seperti ini, Java punya alat yang lebih tepat, yaitu ***interface***. Kita mempelajarinya di Pertemuan 10.

## 6. *Overloading Method* dan Konstruktor

*File*: [`contoh/Contoh06Overloading.java`](contoh/Contoh06Overloading.java)

Di Pertemuan 03, kamu sudah membuat beberapa konstruktor dengan daftar parameter berbeda. Teknik ***overloading*** ini juga berlaku untuk *method* biasa. Contohnya, perpustakaan sederhana. Kelas `Buku` menyimpan judul, penulis, dan tahun. Bagian pentingnya ada di kelas `Perpustakaan`. Berikut potongan *file*-nya:

```java
/** Perpustakaan sederhana yang bisa menyimpan dan mencari buku. */
class Perpustakaan {
    private String nama;
    private List<Buku> koleksi;

    public Perpustakaan() { // [1] konstruktor tanpa parameter
        this("Perpustakaan Kampus"); // memanggil konstruktor lain di kelas ini
    }

    public Perpustakaan(String nama) { // [2] overload konstruktor
        this.nama = nama;
        this.koleksi = new ArrayList<>();
        System.out.println(nama + " dibuka");
    }

    public void tambahBuku(Buku... daftarBuku) { // [3] varargs: berapa pun jumlahnya
        for (Buku buku : daftarBuku) { // daftarBuku berupa array berisi semua argumen
            koleksi.add(buku);
        }
        System.out.println(nama + ": " + daftarBuku.length + " buku ditambahkan");
    }

    public List<Buku> cari(String kataKunci) { // [4] cari berdasarkan judul
        return cari(kataKunci, 0);
    }

    public List<Buku> cari(int tahun) { // [5] nama sama, TIPE parameter berbeda
        return cari("", tahun);
    }

    public List<Buku> cari(String kataKunci, int tahun) { // [6] JUMLAH parameter berbeda
        List<Buku> hasil = new ArrayList<>();
        for (Buku buku : koleksi) {
            boolean cocokJudul = buku.getJudul().contains(kataKunci); // "" selalu cocok
            boolean cocokTahun = tahun == 0 || buku.getTahun() == tahun; // 0 = tahun bebas
            if (cocokJudul && cocokTahun) {
                hasil.add(buku);
            }
        }
        return hasil;
    }
}
```

Di `main`, objek dibuat dengan `new Perpustakaan()` (ditandai `// [7]`) dan `new Perpustakaan("Pojok Baca Informatika")`. Lalu `tambahBuku` dipanggil dengan satu buku, tiga buku sekaligus, dan tanpa buku. Bagian terakhir `main` memanggil ketiga versi `cari`:

```java
        System.out.println("=== SATU NAMA METHOD, BANYAK CARA CARI ===");
        tampilkan("Judul memuat 'Pe'", pusat.cari("Pe")); // [8] cocok dengan cari(String)
        tampilkan("Tahun 1980", pusat.cari(1980)); // cocok dengan cari(int)
        tampilkan("Judul memuat 'a', tahun 2006", pusat.cari("a", 2006)); // cari(String, int)
        tampilkan("Judul memuat 'Kancil'", pusat.cari("Kancil"));
```

***Output:***

```text
=== KONSTRUKTOR DENGAN NILAI BAWAAN ===
Perpustakaan Kampus dibuka
Pojok Baca Informatika dibuka

=== SATU METHOD, JUMLAH ARGUMEN BEBAS ===
Perpustakaan Kampus: 1 buku ditambahkan
Perpustakaan Kampus: 3 buku ditambahkan
Pojok Baca Informatika: 0 buku ditambahkan

=== SATU NAMA METHOD, BANYAK CARA CARI ===
Judul memuat 'Pe'           : Laskar Pelangi (2005), Sang Pemimpi (2006)
Tahun 1980                  : Bumi Manusia (1980)
Judul memuat 'a', tahun 2006: Sang Pemimpi (2006)
Judul memuat 'Kancil'       : (tidak ada)
```

Penjelasan:

- **[1]** Konstruktor tanpa parameter meneruskan pekerjaannya ke konstruktor lain dengan `this(...)`, seperti di Pertemuan 03. Hasilnya mirip nilai bawaan di Python.
- **[2]** Dua konstruktor bernama sama (`Perpustakaan`) dengan daftar parameter berbeda: *overloading* konstruktor.
- **[3]** ***Varargs*** (*variable arguments*): `Buku...` (tiga titik) membuat *method* menerima argumen bertipe `Buku` **berapa pun jumlahnya**, termasuk nol. Di dalam *method*, `daftarBuku` berupa *array*. *Varargs* harus menjadi parameter **terakhir**. Ini padanan `*args` di Python.
- **[4]** Versi pertama `cari` menerima satu `String`. Ia tidak menulis ulang rumus pencarian, melainkan memanggil versi terlengkap **[6]**.
- **[5]** Versi kedua juga punya satu parameter, tetapi **tipenya** `int`. Bagi Java, `cari(String)` dan `cari(int)` adalah dua *method* yang berbeda.
- **[6]** Versi ketiga punya **dua** parameter. Rumus pencarian hanya ditulis di sini.
- **[7]** (di `main`) `new Perpustakaan()` memilih konstruktor tanpa parameter.
- **[8]** *Compiler* memilih versi `cari` berdasarkan argumen yang tertulis: `"Pe"` adalah `String`, `1980` adalah `int`, dan `("a", 2006)` adalah `String, int`. Pemilihan ini terjadi **saat kompilasi**, sebelum program berjalan.

Aturan *overloading*:

| Dua *method* bernama sama dengan... | Sah? |
|---|---|
| Jumlah parameter berbeda: `cari(String)` dan `cari(String, int)` | ya |
| Tipe parameter berbeda: `cari(String)` dan `cari(int)` | ya |
| Urutan tipe berbeda: `f(String, int)` dan `f(int, String)` | ya (tetapi membingungkan, hindari) |
| Hanya nama parameter yang berbeda: `cari(String judul)` dan `cari(String penulis)` | tidak |
| Hanya tipe kembalian yang berbeda: `int hitung(int)` dan `String hitung(int)` | tidak (lihat [Kesalahan 3](#kesalahan-3-overload-yang-hanya-berbeda-tipe-kembalian)) |

> [!TIP]
> Kamu sudah memakai *overloading* sejak Pertemuan 01. `System.out.println` punya banyak versi: `println(String)`, `println(int)`, `println(boolean)`, `println(Object)`, dan lainnya. Itu sebabnya satu nama *method* bisa mencetak data jenis apa pun.

## 7. *Overload* Dipilih saat Kompilasi, *Override* saat Berjalan

*File*: [`contoh/Contoh07OverloadVsOverride.java`](contoh/Contoh07OverloadVsOverride.java)

> [!NOTE]
> Contoh ini **khusus Java**. Python tidak punya *overloading*, jadi tidak ada padanannya. Ringkasannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

Apa yang terjadi jika *overloading* dan *overriding* bertemu? Contoh ini sering muncul sebagai soal ujian. Berikut potongan *file*-nya, dimulai dari kelas yang memiliki `main` (kelas ini ditulis utuh):

```java
public class Contoh07OverloadVsOverride {

    public static void main(String[] args) {
        Resepsionis resepsionis = new Resepsionis();
        Tamu budi = new Tamu("Budi");
        TamuVip siti = new TamuVip("Siti");
        Tamu rina = new TamuVip("Rina"); // [1] tipe variabel Tamu, objeknya TamuVip

        System.out.println("=== OVERLOAD: DIPILIH SAAT KOMPILASI ===");
        System.out.println(resepsionis.sambut(budi));
        System.out.println(resepsionis.sambut(siti));
        System.out.println(resepsionis.sambut(rina)); // [2] melihat tipe VARIABEL rina

        System.out.println();
        System.out.println("=== OVERRIDE: DIPILIH SAAT BERJALAN ===");
        System.out.println(budi.getNama() + ": " + budi.fasilitas());
        System.out.println(siti.getNama() + ": " + siti.fasilitas());
        System.out.println(rina.getNama() + ": " + rina.fasilitas()); // [3] melihat OBJEK rina
    }
}
```

`Tamu` punya *method* `fasilitas()` yang mengembalikan `"kamar standar"`, dan `TamuVip` meng-*override*-nya menjadi `"kamar suite dan sarapan"`. Kelas `Resepsionis` punya dua versi `sambut`:

```java
/** Resepsionis punya dua method sambut(): ini OVERLOADING. */
class Resepsionis {
    public String sambut(Tamu tamu) { // [4] versi untuk tipe Tamu
        return "sambut(Tamu)    dipakai untuk " + tamu.getNama();
    }

    public String sambut(TamuVip tamu) { // [5] versi untuk tipe TamuVip
        return "sambut(TamuVip) dipakai untuk " + tamu.getNama();
    }
}
```

***Output:***

```text
=== OVERLOAD: DIPILIH SAAT KOMPILASI ===
sambut(Tamu)    dipakai untuk Budi
sambut(TamuVip) dipakai untuk Siti
sambut(Tamu)    dipakai untuk Rina

=== OVERRIDE: DIPILIH SAAT BERJALAN ===
Budi: kamar standar
Siti: kamar suite dan sarapan
Rina: kamar suite dan sarapan
```

Penjelasan:

- **[1]** Variabel `rina` bertipe `Tamu`, tetapi objeknya `TamuVip`.
- **[2]** Perhatikan baris ketiga *output*: `sambut(Tamu)` yang dipakai untuk Rina, padahal Rina tamu VIP! *Compiler* memilih versi *overload* saat kompilasi, dan saat itu ia hanya tahu **tipe variabel** `rina`, yaitu `Tamu`.
- **[3]** Sebaliknya, `rina.fasilitas()` menghasilkan versi VIP. *Override* dipilih saat program berjalan berdasarkan **objek** yang sebenarnya.
- **[4]** dan **[5]** Dua *method* bernama `sambut` dengan tipe parameter berbeda: ini *overloading*, bukan *overriding*.

> [!IMPORTANT]
> ***Overload*** dipilih *compiler* berdasarkan **tipe variabel argumen**, saat kompilasi. ***Override*** dipilih saat program berjalan berdasarkan **tipe objek** yang menerima panggilan. Karena itu, polimorfisme yang sesungguhnya (yang mengikuti objek) datang dari *override*. Jika ingin perilaku VIP mengikuti objeknya, taruh perilaku itu sebagai *method* yang di-*override* di kelas `TamuVip`, bukan sebagai versi *overload* di kelas lain.

## 8. Studi Kasus KedaiKita

*File*: [`studi-kasus/Pembayaran.java`](studi-kasus/Pembayaran.java), [`PembayaranTunai.java`](studi-kasus/PembayaranTunai.java), [`PembayaranQRIS.java`](studi-kasus/PembayaranQRIS.java), [`PembayaranKartu.java`](studi-kasus/PembayaranKartu.java), [`Pesanan.java`](studi-kasus/Pesanan.java), dan [`Main.java`](studi-kasus/Main.java)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-banyak-cara-bayar).

**Apa yang berubah dibanding Pertemuan 07?**

- **Empat *file* baru:** kelas induk `Pembayaran` dan tiga kelas anak, `PembayaranTunai`, `PembayaranQRIS`, dan `PembayaranKartu`.
- **`Pesanan.java`**: *field* `status` (`"BARU"` lalu `"LUNAS"`) dengan *getter*-nya, *method* baru `bayar(Pembayaran)`, dan versi *overload* `tambahItem(Menu)`. Struk ikut menampilkan status.
- **`Main.java`**: skenarionya diganti agar fokus ke pembayaran. Kini ada bagian "SATU PANGGILAN, BANYAK BENTUK", pembayaran Budi dan Siti, serta "MEMERIKSA JENIS PEMBAYARAN". Bagian cek pewarisan dan menu tambahan dari Pertemuan 07 tidak dipakai lagi.
- `Menu`, `Makanan`, `Minuman`, `ItemPesanan`, `Kedai`, `Pelanggan`, dan `Rupiah` **tidak berubah**.

Berikut kelas induknya, `Pembayaran.java` (isi lengkap tanpa komentar pembuka):

```java
/** Kelas induk semua metode pembayaran. */
public class Pembayaran {

    public String namaMetode() {
        return "Pembayaran umum";
    }

    /** Biaya tambahan yang dibebankan ke pelanggan. Bawaannya 0. */
    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    /** Memproses pembayaran. Mengembalikan true jika berhasil. */
    public boolean proses(int total) {
        System.out.println("  Memproses pembayaran " + Rupiah.format(total));
        return true;
    }
}
```

Ketiga kelas anak meng-*override* `namaMetode()` dan `proses()` dengan cara masing-masing: tunai menghitung kembalian, QRIS memotong saldo *e-wallet*, dan kartu mencetak persetujuan bank. Berikut isi lengkap `PembayaranTunai.java`:

```java
/** Bayar dengan uang tunai. Bisa menghasilkan kembalian. */
public class PembayaranTunai extends Pembayaran {
    private int uangDiterima;
    private int kembalian;

    public PembayaranTunai(int uangDiterima) {
        this.uangDiterima = uangDiterima;
        this.kembalian = 0;
    }

    public int getKembalian() {
        return kembalian;
    }

    @Override
    public String namaMetode() {
        return "Tunai";
    }

    @Override
    public boolean proses(int total) {
        if (uangDiterima < total) {
            int kurang = total - uangDiterima;
            System.out.println("  Uang kurang " + Rupiah.format(kurang));
            return false;
        }
        kembalian = uangDiterima - total;
        System.out.println("  Uang diterima " + Rupiah.format(uangDiterima)
                + ", kembalian " + Rupiah.format(kembalian));
        return true;
    }
}
```

`PembayaranQRIS` ditulis dengan pola yang sama, tetapi menyimpan `saldo` *e-wallet* dan memotongnya di `proses()`. Hanya `PembayaranKartu` yang juga meng-*override* biaya layanan. Potongan `PembayaranKartu.java` (konstanta `PERSEN_BIAYA` bernilai 2):

```java
    @Override
    public int hitungBiayaLayanan(int total) {
        return total * PERSEN_BIAYA / 100;
    }
```

- **`Pembayaran`** menetapkan tiga *method* yang dimiliki **semua** jenis pembayaran. `hitungBiayaLayanan` bawaannya 0, jadi hanya kelas yang punya biaya tambahan yang perlu meng-*override*-nya.
- **Tunai dan QRIS tidak menulis `hitungBiayaLayanan`**, jadi biayanya 0 (warisan induk). Setiap `@Override` diperiksa *compiler*.
- **`getKembalian()` hanya ada di `PembayaranTunai`.** Lewat variabel bertipe `PembayaranTunai`, *method* ini bisa langsung dipanggil. Namun, lewat variabel atau `List` bertipe `Pembayaran`, *method* khusus ini baru bisa dipanggil setelah *downcasting*.
- **Kelas `Pembayaran` "umum" terasa janggal.** Tidak ada pelanggan yang membayar dengan "Pembayaran umum", tetapi `new Pembayaran()` tetap bisa ditulis. Di Pertemuan 10, kelas ini dijadikan `abstract class`.

Di `Pesanan.java`, inilah potongan bagian yang baru. Pertama, versi *overload* `tambahItem`:

```java
    public void tambahItem(Menu menu, int jumlah) {
        ItemPesanan item = new ItemPesanan(menu, jumlah); // objek item dibuat OLEH pesanan
        menu.kurangiStok(jumlah); // gagal (IllegalArgumentException) jika stok kurang
        daftarItem.add(item);
    }

    /** Versi overload: tanpa parameter jumlah berarti memesan 1 porsi. */
    public void tambahItem(Menu menu) {
        tambahItem(menu, 1);
    }
```

Lalu *method* `bayar`:

```java
    /** Membayar pesanan dengan metode pembayaran apa pun. */
    public boolean bayar(Pembayaran pembayaran) {
        int total = hitungTotal();
        int biaya = pembayaran.hitungBiayaLayanan(total); // polimorfisme
        int totalBayar = total + biaya;
        System.out.println("Pembayaran pesanan " + nomor + " (" + pelanggan.getNama() + ")");
        System.out.println("  Metode       : " + pembayaran.namaMetode()); // polimorfisme
        if (biaya > 0) {
            System.out.println("  Biaya layanan: " + Rupiah.format(biaya));
        }
        System.out.println("  Total bayar  : " + Rupiah.format(totalBayar));
        boolean berhasil = pembayaran.proses(totalBayar); // polimorfisme
        if (berhasil) {
            status = "LUNAS";
            int poin = total / 10000;
            if (poin > 0) {
                pelanggan.tambahPoin(poin);
            }
            System.out.println("  Status       : LUNAS (+" + poin + " poin)");
        } else {
            System.out.println("  Status       : GAGAL, silakan pilih metode lain");
        }
        return berhasil;
    }
```

- **`tambahItem(Menu)`** adalah *overloading*: Java tidak punya nilai bawaan untuk parameter, jadi dibuat versi pendek yang meneruskan ke versi lengkap dengan jumlah 1. Versi Python cukup memakai `jumlah: int = 1`.
- **Parameter `bayar` bertipe `Pembayaran`** sehingga mau menerima objek kelas anak mana pun (*upcasting* otomatis).
- **`bayar()` tidak punya satu pun `instanceof`.** Tiga baris bertanda `// polimorfisme` menjalankan *method* milik objek pembayaran yang sebenarnya.
- **Poin dihitung dari total pesanan** (sebelum biaya layanan): 1 poin per Rp10.000.

Di `Main.java`, bagian "SATU PANGGILAN, BANYAK BENTUK" memproses `List<Pembayaran>` berisi tiga jenis pembayaran dengan satu perulangan. Bagian baru yang paling menarik adalah pemeriksaan jenis. Berikut potongannya:

```java
        System.out.println("=== MEMERIKSA JENIS PEMBAYARAN ===");
        List<Pembayaran> daftarPembayaran = List.of(pembayaranBudi,
                new PembayaranKartu("Mandiri"));
        for (Pembayaran pembayaran : daftarPembayaran) {
            if (pembayaran instanceof PembayaranTunai) {
                // Casting: pembayaran "dipandang" sebagai PembayaranTunai
                // agar getKembalian() (yang hanya ada di kelas itu) bisa dipanggil.
                PembayaranTunai tunai = (PembayaranTunai) pembayaran;
                String kembalian = Rupiah.format(tunai.getKembalian());
                System.out.println(pembayaran.namaMetode() + ": kembalian " + kembalian);
            } else {
                System.out.println(pembayaran.namaMetode() + ": tidak ada kembalian");
            }
        }
        System.out.println();
```

- **`instanceof` + *cast* dipakai hanya untuk fitur khusus**, yaitu kembalian. Dengan Java 16 ke atas, bagian itu bisa juga ditulis `if (pembayaran instanceof PembayaranTunai tunai)`.
- Sebelum bagian ini, Siti mencoba membayar dengan QRIS (saldo Rp20.000). Karena `bayar()` mengembalikan `false`, program mencoba lagi dengan `new PembayaranKartu("BNI")`.

Jalankan `javac *.java` lalu `java Main` dari dalam folder `studi-kasus` (lihat [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)). Daftar menu di awal *output* sama persis dengan Pertemuan 07.

***Output:***

```text
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 12 | pedas level 0

=== SATU PANGGILAN, BANYAK BENTUK ===
Tunai                biaya layanan untuk Rp100.000: Rp0
QRIS                 biaya layanan untuk Rp100.000: Rp0
Kartu Kredit BNI     biaya layanan untuk Rp100.000: Rp2.000

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
Status      : BARU
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
Status      : BARU
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================
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

=== MEMERIKSA JENIS PEMBAYARAN ===
Tunai: kembalian Rp39.000
Kartu Kredit Mandiri: tidak ada kembalian

=== STATUS AKHIR ===
P001: LUNAS
P002: LUNAS
Budi Santoso (081234567890) - 6 poin
Siti Aminah (082198765432) - 3 poin
```

*Output* ini **identik** dengan versi Python. Perhatikan pembayaran Siti: *method* `bayar()` yang **sama** dipanggil dua kali pada pesanan yang **sama**. Yang berbeda hanya objek pembayarannya, dan itulah yang menentukan seluruh perilakunya.

> [!TIP]
> **Coba sendiri:** salin **seluruh folder** `studi-kasus` ke folder `pertemuan-09` milikmu. Seluruh folder perlu disalin karena `Main.java` membutuhkan semua kelas lain di folder itu. Lalu, di salinan `Main.java`:
> 1. Ubah `new PembayaranQRIS(20000)` di bagian pesanan Siti menjadi `new PembayaranQRIS(50000)`. Simpan, lalu jalankan: klik **Run** di atas `main`, atau ketik `javac *.java` lalu `java Main` di terminal yang berada di salinan folder `studi-kasus` (klik kanan folder itu di **Explorer**, lalu pilih **Open in Integrated Terminal**). Apa yang tercetak pada pembayaran Siti?
> 2. Di bagian "SATU PANGGILAN, BANYAK BENTUK", tambahkan `new Pembayaran()` di akhir `List.of(...)` milik `daftarMetode`. Simpan dan jalankan lagi. Baris apa yang muncul, dan mengapa terasa janggal?

<details>
<summary>Lihat jawaban</summary>

1. Pembayaran QRIS langsung berhasil. Tercetak `Saldo e-wallet terpotong Rp31.000, sisa Rp19.000`, lalu `Status       : LUNAS (+3 poin)`. Percobaan kartu kredit tidak dijalankan karena `bayar()` sudah mengembalikan `true`.

2. Muncul baris `Pembayaran umum      biaya layanan untuk Rp100.000: Rp0`. Janggal karena "pembayaran umum" bukan metode bayar sungguhan. Objek seperti ini seharusnya tidak bisa dibuat. Pertemuan 10 akan memperbaikinya dengan `abstract class`.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan *Error*

Ingat dua jenis kesalahan di Java: ***error* kompilasi** (diawali nama *file* dan nomor baris, ada tanda `^`) dan ***error* saat berjalan** (diawali `Exception in thread "main"`). Tiga kesalahan lain sudah dibahas sebelumnya: *downcasting* tanpa *cast* dan `ClassCastException` di [bagian 3](#3-upcasting-downcasting-dan-instanceof), serta memanggil *method* lewat tipe yang tidak punya *method* itu di [bagian 5](#5-tanpa-duck-typing-java-butuh-tipe-bersama).

**Cara mencobanya sendiri.** Kerjakan di folder `pertemuan-09` milikmu. Kesalahan 1 dan 2 memakai salinan *file* contoh yang disebut (jangan ganti nama *file*-nya, dan mulailah dari salinan baru tanpa tambahan percobaan sebelumnya). Kesalahan 3 memakai *file* baru bernama `Coba.java`. Jalankan dengan `java NamaFile.java` dari terminal yang berada di folder itu. Ketiganya adalah *error* kompilasi, jadi setiap pesan diakhiri baris `error: compilation failed`. Baris itu muncul karena kita memakai `java NamaFile.java`; jika memakai `javac`, baris itu tidak ada.

### Kesalahan 1: Memanggil *method* khusus lewat variabel bertipe induk

Di salinan `contoh/Contoh03UpcastingDowncasting.java`, tambahkan dua baris berikut di akhir *method* `main`, tepat setelah baris yang mencetak `Ayu termasuk Dosen?`:

```java
        Pengguna p = new Mahasiswa("Ayu Lestari", "2409106001");
        System.out.println(p.isiKrs(21));
```

Simpan, lalu jalankan dengan `java Contoh03UpcastingDowncasting.java`. Hasilnya:

```text
Contoh03UpcastingDowncasting.java:55: error: cannot find symbol
        System.out.println(p.isiKrs(21));
                            ^
  symbol:   method isiKrs(int)
  location: variable p of type Pengguna
1 error
error: compilation failed
```

**Artinya:** objeknya memang mahasiswa, tetapi *compiler* hanya melihat **tipe variabel** `p`, yaitu `Pengguna` (`variable p of type Pengguna`). Kelas `Pengguna` tidak punya `isiKrs`, jadi *method* itu "tidak ditemukan" (`cannot find symbol`). **Perbaikan:** periksa dengan `instanceof`, lalu *downcast*: `if (p instanceof Mahasiswa m) { System.out.println(m.isiKrs(21)); }`.

### Kesalahan 2: *Override* yang tanpa sengaja menjadi *overload*

Di salinan `contoh/Contoh02KoleksiPolimorfik.java`, cari kelas `Segitiga`. Ubah *method* `luas()`-nya sehingga menerima parameter `skala`, lalu simpan:

```java
    @Override
    public int luas(int skala) {
        return alas * tinggi / 2 * skala;
    }
```

Jalankan dengan `java Contoh02KoleksiPolimorfik.java`. Hasilnya:

```text
Contoh02KoleksiPolimorfik.java:110: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
error: compilation failed
```

**Artinya:** "*method* ini tidak menimpa *method* apa pun milik induknya". `BangunDatar` hanya punya `luas()` tanpa parameter. `luas(int skala)` punya daftar parameter berbeda, jadi ini **bukan** *override*, melainkan *overload*. Untungnya `@Override` membuat *compiler* protes.

Sekarang hapus baris `@Override` di atas `luas(int skala)`, simpan, lalu jalankan lagi. Kompilasi berhasil, tetapi baris segitiga di kedua laporan berubah menjadi seperti di bawah, dan total luasnya ikut berkurang 24:

```text
Segitiga alas 8 tinggi 6       luas    0 cm2
```

Tanpa `@Override`, `bangun.luas()` pada objek segitiga diam-diam memakai versi induk sehingga luasnya 0. Kesalahan senyap seperti ini sulit dicari. **Perbaikan:** samakan daftar parameternya dengan versi induk, dan **selalu** tulis `@Override`.

### Kesalahan 3: *Overload* yang hanya berbeda tipe kembalian

Buat *file* baru bernama `Coba.java` di folder `pertemuan-09` milikmu, salin kode berikut, simpan, lalu jalankan dengan `java Coba.java`.

```java
public class Coba {
    public static void main(String[] args) {
        System.out.println(new Kalkulator().hitung(5));
    }
}

class Kalkulator {
    int hitung(int x) {
        return x * 2;
    }

    String hitung(int x) {
        return "Hasil: " + (x * 2);
    }
}
```

Hasilnya:

```text
Coba.java:12: error: method hitung(int) is already defined in class Kalkulator
    String hitung(int x) {
           ^
1 error
error: compilation failed
```

**Artinya:** "*method* `hitung(int)` sudah ada di kelas `Kalkulator`". Kedua *method* punya nama dan daftar parameter yang sama, `hitung(int)`. Tipe kembalian tidak ikut dihitung karena saat memanggil `hitung(5)`, *compiler* tidak bisa menebak versi mana yang dimaksud. **Perbaikan:** beri nama berbeda, misalnya `hitung` dan `hitungTeks`, atau bedakan daftar parameternya.

> [!NOTE]
> Contoh pesan di atas berasal dari JDK 21. Bunyi pesan *error* bisa sedikit berbeda antarversi JDK, dan nomor barisnya bisa bergeser jika letak tambahanmu berbeda. Fokuslah pada kata kuncinya, seperti `cannot find symbol`, `incompatible types`, `does not override`, `is already defined`, dan `ClassCastException`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| *Override* (dasar polimorfisme) | `@Override` + nama dan parameter sama | `@Override public String bersuara()` |
| *Upcasting* (otomatis) | `Induk var = new Anak(...);` | `Hewan hewan = new Kucing("Oyen");` |
| Koleksi polimorfik | `List<Induk>` berisi objek anak | `List<BangunDatar> daftar = new ArrayList<>();` |
| Memeriksa jenis objek | `objek instanceof Kelas` | `pengguna instanceof Mahasiswa` |
| *Downcasting* (klasik) | `(Anak) var` | `Mahasiswa mhs = (Mahasiswa) pengguna;` |
| Cek + *cast* sekaligus (Java 16+) | `objek instanceof Kelas nama` | `if (pengguna instanceof Dosen dosen)` |
| Polimorfisme dari dalam kelas | panggil *method* lain di *method* induk | `System.out.println(isi());` |
| *Overload* *method* | nama sama, parameter berbeda | `cari(String)`, `cari(int)` |
| *Overload* konstruktor | `this(...)` ke konstruktor lain | `this("Perpustakaan Kampus");` |
| *Varargs* | `Tipe... nama` (parameter terakhir) | `void tambahBuku(Buku... daftarBuku)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
