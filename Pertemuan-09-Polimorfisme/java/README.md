# ☕ Praktik Java — Pertemuan 09: Polimorfisme

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 09](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Satu Perintah, Banyak Bentuk](#1-satu-perintah-banyak-bentuk)
2. [Koleksi Polimorfik dan Jenis Baru](#2-koleksi-polimorfik-dan-jenis-baru)
3. [Upcasting, Downcasting, dan `instanceof`](#3-upcasting-downcasting-dan-instanceof)
4. [Polimorfisme dari Dalam Kelas](#4-polimorfisme-dari-dalam-kelas)
5. [Tanpa Duck Typing: Java Butuh Tipe Bersama](#5-tanpa-duck-typing-java-butuh-tipe-bersama)
6. [Overloading Method dan Konstruktor](#6-overloading-method-dan-konstruktor)
7. [Overload Dipilih saat Kompilasi, Override saat Berjalan](#7-overload-dipilih-saat-kompilasi-override-saat-berjalan)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan Error](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh program satu file
├── studi-kasus/     <- KedaiKita versi Pertemuan 09 (satu kelas per file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file, jadi bisa langsung dijalankan:

```bash
cd Pertemuan-09-Polimorfisme/java/contoh
java Contoh01SatuPerintahBanyakBentuk.java
```

Studi kasus terdiri atas banyak file. Kompilasi semuanya dulu, lalu jalankan kelas `Main`:

```bash
cd Pertemuan-09-Polimorfisme/java/studi-kasus
javac *.java
java Main
```

> [!TIP]
> Di VS Code, buka folder `java/` **milik pertemuan ini** saja (File → Open Folder). Nama kelas di dalam satu folder harus unik. Itulah sebabnya setiap contoh memakai nama kelas yang berbeda-beda, dan solusi latihan KedaiKita memakai nama seperti `PembayaranKedai`. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

> [!NOTE]
> Contoh 03 memakai bentuk `instanceof` yang tersedia sejak **Java 16**. Mata kuliah ini memakai JDK 17 ke atas, jadi semua contoh bisa dijalankan.

## 1. Satu Perintah, Banyak Bentuk

File: [`contoh/Contoh01SatuPerintahBanyakBentuk.java`](contoh/Contoh01SatuPerintahBanyakBentuk.java)

Kita mulai dari contoh klasik: hewan-hewan yang bersuara. Ini kelas yang memiliki `main`:

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

**Output:**

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
- **[2]** `Kucing`, `Anjing`, dan `Bebek` meng-*override* `bersuara()`. Anotasi `@Override` meminta *compiler* memastikan method ini benar-benar menimpa method induk.
- **[3]** Parameter bertipe `Hewan` mau menerima objek `Kucing`, `Anjing`, `Bebek`, atau `Ikan`, karena semuanya **adalah** `Hewan`.
- **[4]** Inilah inti polimorfisme. `suruhBersuara` tidak tahu jenis hewannya, tetapi `hewan.bersuara()` selalu menjalankan versi milik **objek** yang sebenarnya.
- **[5]** **Tipe variabel** `hewan` adalah `Hewan`, sedangkan **tipe objeknya** `Kucing`. Menyimpan objek anak di variabel bertipe induk disebut ***upcasting***, dan Java melakukannya otomatis. Baris `System.out.println(hewan.bersuara())` ditulis sama dua kali, tetapi hasilnya berbeda.
- **[6]** `List<Hewan>` berisi empat objek dari empat kelas berbeda. `Ikan` tidak meng-*override*, jadi Java naik ke kelas induk dan memakai `(diam saja)`.

Aturan emasnya:

| Pertanyaan | Ditentukan oleh |
|---|---|
| Method apa saja yang **boleh dipanggil**? | **Tipe variabel** (diperiksa *compiler*) |
| Versi method mana yang **dijalankan**? | **Tipe objek** (dipilih saat program berjalan) |

> [!TIP]
> **Coba sendiri:** tambahkan kelas `Sapi extends Hewan` yang bersuara `"Mooo!"` (jangan lupa konstruktor dengan `super(nama)`), lalu masukkan `new Sapi("Belang")` ke `kebun`. Apakah `suruhBersuara` perlu diubah?

<details>
<summary>Lihat jawaban</summary>

Tidak perlu. Muncul baris baru `Belang si Sapi: Mooo!` tanpa menyentuh `suruhBersuara` sedikit pun. Inilah keuntungan utama polimorfisme yang dibahas di bagian berikutnya.

</details>

## 2. Koleksi Polimorfik dan Jenis Baru

File: [`contoh/Contoh02KoleksiPolimorfik.java`](contoh/Contoh02KoleksiPolimorfik.java)

Sekarang kita buktikan bahwa jenis baru bisa ditambahkan tanpa mengubah kode pemanggil. Berikut kelas induknya:

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

Kelas anak `Persegi`, `PersegiPanjang`, dan `Segitiga` masing-masing meng-*override* `nama()` dan `luas()` dengan `@Override`. Misalnya, `luas()` milik `Segitiga` mengembalikan `alas * tinggi / 2`. Kelas baru `Trapesium` (ditandai `// [2] cukup menulis kelas baru`) ditulis di bagian paling bawah file dengan pola yang sama. Lalu method laporan di kelas utama:

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

**Output:**

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

- **[1]** Versi induk mengembalikan 0, karena bangun datar "umum" tidak punya rumus luas.
- **[2]** Menambah jenis baru cukup dengan **menulis kelas baru**. Tidak ada kode lama yang diubah.
- **[3]** Parameter `List<BangunDatar>` berarti "daftar berisi bangun datar jenis apa pun". Isi method ini tidak menyebut `Persegi`, `Segitiga`, atau `Trapesium` sama sekali.
- **[4]** Setiap putaran memanggil `luas()` dan `nama()` milik objek yang sedang diproses.
- **[5]** `List<BangunDatar>` boleh diisi objek kelas anak mana pun. Inilah **koleksi polimorfik**.
- **[6]** `Trapesium` ikut dihitung dengan benar, walaupun `cetakLaporan` ditulis sebelum kelas itu ada.

> [!NOTE]
> Baris `Bangun datar ... luas 0` terasa janggal. Objek `new BangunDatar()` memang tidak seharusnya bisa dibuat. Di Pertemuan 10, kita membuat kelas seperti ini menjadi **kelas abstrak**, sehingga *compiler* menolak pembuatan objeknya.

## 3. Upcasting, Downcasting, dan `instanceof`

File: [`contoh/Contoh03UpcastingDowncasting.java`](contoh/Contoh03UpcastingDowncasting.java)

Kadang sebuah kelas anak punya method **khusus** yang tidak dimiliki saudaranya. Di contoh ini, hanya `Mahasiswa` yang punya `isiKrs()`, dan hanya `Dosen` yang punya `inputNilai()`. Keduanya sama-sama meng-*override* `peran()` dan `menuUtama()` milik `Pengguna`. Berikut method khusus di kelas `Mahasiswa`:

```java
    public String isiKrs(int sks) { // method KHUSUS mahasiswa
        return getNama() + " (" + nim + ") mengisi KRS " + sks + " SKS";
    }
```

Kelas `Dosen` serupa, dengan method khusus `inputNilai(String mataKuliah, String nilai)`. Program utamanya:

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

**Output:**

```text
=== SEMUA PENGGUNA LOGIN ===
Ayu Lestari [Mahasiswa] menu: Profil, KRS, KHS
Rahmat Hidayat [Dosen] menu: Profil, Input Nilai, Jadwal Mengajar
Bima Saputra [Mahasiswa] menu: Profil, KRS, KHS

=== FITUR KHUSUS: CEK JENIS DULU ===
Ayu Lestari (2409106001) mengisi KRS 21 SKS
Rahmat Hidayat menginput nilai PBO: A
Bima Saputra (2409106002) mengisi KRS 21 SKS

=== CEK JENIS IKUT MENGENAL INDUK ===
Ayu termasuk Mahasiswa? ya
Ayu termasuk Pengguna?  ya
Ayu termasuk Dosen?     tidak
```

Penjelasan:

- **[1]** **Upcasting**: objek `Mahasiswa` dan `Dosen` dimasukkan ke `List<Pengguna>`. Java melakukannya otomatis, karena setiap mahasiswa dan dosen **adalah** pengguna.
- **[2]** Lewat variabel bertipe `Pengguna`, kita hanya boleh memanggil method milik `Pengguna`. Hasilnya tetap polimorfik.
- **[3]** `instanceof` memeriksa apakah objek yang ditunjuk `pengguna` adalah `Mahasiswa` (atau anak dari `Mahasiswa`).
- **[4]** **Downcasting** dengan cara klasik: `(Mahasiswa) pengguna` meminta *compiler* memandang objek itu sebagai `Mahasiswa`, lalu hasilnya disimpan ke variabel `mhs`. Setelah itu, `isiKrs()` boleh dipanggil.
- **[5]** Bentuk modern sejak Java 16 (disebut *pattern matching for instanceof*). `pengguna instanceof Dosen dosen` memeriksa jenis **sekaligus** membuat variabel `dosen` bertipe `Dosen`. Variabel itu hanya berlaku di dalam cabang yang pemeriksaannya bernilai benar. Lebih ringkas, dan kita tidak mungkin lupa memeriksa sebelum *cast*.
- **[6]** `instanceof` juga menjawab "ya" untuk kelas induk, karena setiap mahasiswa **adalah** pengguna.

Mengapa *cast* dibutuhkan? Karena *compiler* hanya melihat **tipe variabel**. Baginya, `pengguna` hanyalah `Pengguna`, dan kelas `Pengguna` tidak punya `isiKrs()`. Jika kita langsung menulis `pengguna.isiKrs(21)`, kompilasi gagal (lihat [Kesalahan 1](#kesalahan-1-memanggil-method-khusus-lewat-variabel-bertipe-induk)).

| Arah | Contoh | Perlu ditulis? | Aman? |
|---|---|---|---|
| *Upcasting* | `Pengguna p = new Mahasiswa(...);` | Tidak, otomatis | Selalu |
| *Downcasting* | `Mahasiswa m = (Mahasiswa) p;` | Ya, wajib *cast* | Hanya jika objeknya memang `Mahasiswa` |

Jika *cast* lupa ditulis (`Mahasiswa m = p;`), kompilasi gagal dengan pesan `incompatible types: Pengguna cannot be converted to Mahasiswa`. *Compiler* tidak bisa menjamin setiap `Pengguna` adalah `Mahasiswa`, jadi kita wajib menyatakannya secara eksplisit.

### Jika downcasting salah tebak: `ClassCastException`

*Cast* bukan sihir. *Cast* tidak mengubah objek, melainkan hanya cara kita memandangnya. Jika objeknya ternyata **bukan** kelas yang kita tebak, Java menghentikan program saat berjalan:

```java
        Pengguna p = new Dosen("Rahmat");
        Mahasiswa m = (Mahasiswa) p;
        System.out.println(m.isiKrs(21));
```

Kode ini lolos kompilasi, karena secara teori sebuah `Pengguna` *mungkin saja* seorang `Mahasiswa`. Namun saat dijalankan:

```text
Exception in thread "main" java.lang.ClassCastException: class Dosen cannot be cast to class Mahasiswa (Dosen and Mahasiswa are in unnamed module of loader 'app')
	at E3.main(E3.java:4)
```

**Artinya:** objek yang ditunjuk `p` adalah `Dosen`, dan seorang dosen tidak bisa dipandang sebagai mahasiswa. Bagian dalam kurung hanya keterangan teknis tentang lokasi kelas. Jika file dijalankan dengan `java NamaFile.java`, bagian itu menyebut `MemoryClassLoader` beserta sebuah kode acak, tetapi intinya sama. **Perbaikan:** selalu periksa dengan `instanceof` sebelum *downcasting*, atau pakai bentuk `instanceof Mahasiswa m` yang memeriksa sekaligus melakukan *cast*.

> [!NOTE]
> *Compiler* Java cukup cerdas untuk menolak *cast* yang **mustahil**. Jika variabelnya sudah bertipe `Mahasiswa`, menulis `(Dosen) ayu` langsung gagal dikompilasi dengan pesan `incompatible types: Mahasiswa cannot be converted to Dosen`, karena seorang `Mahasiswa` tidak mungkin sekaligus `Dosen`. `ClassCastException` hanya bisa terjadi jika tipe variabelnya induk, sehingga *compiler* belum bisa memastikan.

> [!WARNING]
> Gunakan `instanceof` dan *cast* hanya untuk method yang benar-benar **khusus**. Untuk perilaku yang dimiliki semua jenis, cukup *override* lalu panggil langsung seperti di **[2]**. Kode yang penuh `if (x instanceof A) ... else if (x instanceof B) ...` adalah tanda rancangan belum memanfaatkan polimorfisme.

## 4. Polimorfisme dari Dalam Kelas

File: [`contoh/Contoh04PolimorfismeDariDalamKelas.java`](contoh/Contoh04PolimorfismeDariDalamKelas.java)

Method `tulis()` hanya ditulis sekali, di kelas induk. Namun hasilnya berbeda untuk setiap jenis kartu.

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

**Output:**

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
- **[2]** Di dalam method, `salam()` sama artinya dengan `this.salam()`. Saat objek `KartuWisuda` menjalankan `tulis()`, `this` adalah objek kartu wisuda itu, jadi versi `KartuWisuda` yang dipanggil.
- **[3]** (di `KartuUlangTahun`) Hanya `isi()` yang di-*override*. Salamnya tetap versi induk (`Halo, Rina!`).
- **[4]** `KartuWisuda` meng-*override* keduanya. Field `penerima` bersifat `private` di induk, jadi kelas anak membacanya lewat `getPenerima()`.
- **[5]** Gaya "memperluas" dari Pertemuan 07: menambahkan kalimat, lalu memakai versi induk lewat `super.isi()`.
- **[6]** (di `main`) Program utama hanya memanggil `tulis()`. Ia tidak tahu bahwa di dalamnya terjadi polimorfisme.

Jejak eksekusi untuk kartu ketiga:

```text
kartu.tulis()          -> tulis() milik KartuUcapan (KartuWisuda tidak punya tulis)
  salam()              -> this adalah KartuWisuda -> "Selamat, Dimas, S.Kom.!"
  isi()                -> this adalah KartuWisuda -> isi() milik KartuWisuda
    super.isi()        -> isi() milik KartuUcapan -> "Semoga harimu menyenangkan."
```

## 5. Tanpa Duck Typing: Java Butuh Tipe Bersama

File: [`contoh/Contoh05TipeBersama.java`](contoh/Contoh05TipeBersama.java)

Di Python, objek-objek yang **tidak bersaudara** tetap bisa diproses bersama, asalkan sama-sama punya method yang dipanggil. Gaya ini disebut ***duck typing*** (lihat [halaman konsep](../README.md#7-duck-typing-yang-penting-bisa-bukan-siapa)). Bagaimana di Java? Coba simpan objek `AyamJago` (tanpa induk khusus) di variabel bertipe `Object`, kelas akar semua kelas:

```java
        Object benda = new AyamJago();
        System.out.println(benda.bunyikan());
```

```text
E6.java:4: error: cannot find symbol
        System.out.println(benda.bunyikan());
                                ^
  symbol:   method bunyikan()
  location: variable benda of type Object
1 error
```

*Compiler* hanya melihat tipe variabel `Object`, dan kelas `Object` tidak punya `bunyikan()`. Java tidak mau "berharap" objeknya punya method itu. Solusinya: beri semua kelas **tipe bersama** yang punya `bunyikan()`.

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

`AlarmPonsel`, `Kentongan`, dan `BelSekolah` juga `extends SumberBunyi`. Di kelas utama, `main` memanggil method berikut dengan `List.of(new AyamJago(), new AlarmPonsel("05.00"), new Kentongan())`, lalu dengan daftar kedua:

```java
    static void bangunkanSemua(List<SumberBunyi> daftar) { // [3] tipe bersama wajib disebut
        for (SumberBunyi benda : daftar) {
            String nama = benda.getClass().getSimpleName();
            System.out.println(String.format("%-12s: %s", nama, benda.bunyikan())); // [4]
        }
    }
```

**Output:**

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
- **[3]** Parameter method wajib menyebut tipe bersama itu.
- **[4]** Pemanggilan `bunyikan()` tetap polimorfik, sama seperti contoh-contoh sebelumnya.

Output-nya sama persis dengan versi *duck typing* di Python. Bedanya, Java memastikan **sebelum program berjalan** bahwa setiap objek pasti punya `bunyikan()`. Di Python, objek tanpa `bunyikan()` baru ketahuan saat program berjalan (`AttributeError`).

> [!NOTE]
> Kalimat "ayam jago **adalah** sumber bunyi" terdengar dipaksakan, bukan? Ayam jago, alarm, dan kentongan tidak benar-benar bersaudara. Mereka hanya punya **kemampuan** yang sama: bisa berbunyi. Untuk kebutuhan seperti ini, Java punya alat yang lebih tepat, yaitu ***interface***, yang kita pelajari di Pertemuan 10.

## 6. Overloading Method dan Konstruktor

File: [`contoh/Contoh06Overloading.java`](contoh/Contoh06Overloading.java)

Di Pertemuan 03, kamu sudah membuat beberapa konstruktor dengan daftar parameter berbeda. Teknik ***overloading*** ini juga berlaku untuk method biasa. Contohnya, perpustakaan sederhana. Kelas `Buku` menyimpan judul, penulis, dan tahun. Bagian pentingnya ada di kelas `Perpustakaan`:

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

**Output:**

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
- **[3]** **Varargs**: `Buku...` (tiga titik) membuat method menerima argumen bertipe `Buku` **berapa pun jumlahnya**, termasuk nol. Di dalam method, `daftarBuku` berupa array. Varargs harus menjadi parameter **terakhir**. Ini padanan `*args` di Python.
- **[4]** Versi pertama `cari` menerima satu `String`. Ia tidak menulis ulang rumus pencarian, melainkan memanggil versi terlengkap **[6]**.
- **[5]** Versi kedua juga punya satu parameter, tetapi **tipenya** `int`. Bagi Java, `cari(String)` dan `cari(int)` adalah dua method yang berbeda.
- **[6]** Versi ketiga punya **dua** parameter. Rumus pencarian hanya ditulis di sini.
- **[7]** (di `main`) `new Perpustakaan()` memilih konstruktor tanpa parameter.
- **[8]** *Compiler* memilih versi `cari` berdasarkan argumen yang tertulis: `"Pe"` adalah `String`, `1980` adalah `int`, dan `("a", 2006)` adalah `String, int`. Pemilihan ini terjadi **saat kompilasi**, sebelum program berjalan.

Aturan *overloading*:

| Dua method bernama sama dengan... | Sah? |
|---|---|
| Jumlah parameter berbeda: `cari(String)` dan `cari(String, int)` | ya |
| Tipe parameter berbeda: `cari(String)` dan `cari(int)` | ya |
| Urutan tipe berbeda: `f(String, int)` dan `f(int, String)` | ya (tetapi membingungkan, hindari) |
| Hanya nama parameter yang berbeda: `cari(String judul)` dan `cari(String penulis)` | tidak |
| Hanya tipe kembalian yang berbeda: `int hitung(int)` dan `String hitung(int)` | tidak (lihat [Kesalahan 3](#kesalahan-3-overload-yang-hanya-berbeda-tipe-kembalian)) |

> [!TIP]
> Kamu sudah memakai overloading sejak Pertemuan 01. `System.out.println` punya banyak versi: `println(String)`, `println(int)`, `println(boolean)`, `println(Object)`, dan lainnya. Itu sebabnya satu nama method bisa mencetak data jenis apa pun.

## 7. Overload Dipilih saat Kompilasi, Override saat Berjalan

File: [`contoh/Contoh07OverloadVsOverride.java`](contoh/Contoh07OverloadVsOverride.java)

> [!NOTE]
> Contoh ini **khusus Java**. Python tidak punya overloading, jadi tidak ada padanannya. Ringkasannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

Apa yang terjadi jika *overloading* dan *overriding* bertemu? Contoh ini sering muncul sebagai soal ujian.

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

`Tamu` punya method `fasilitas()` yang mengembalikan `"kamar standar"`, dan `TamuVip` meng-*override*-nya menjadi `"kamar suite dan sarapan"`. Kelas `Resepsionis` punya dua versi `sambut`:

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

**Output:**

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
- **[2]** Perhatikan baris ketiga output: `sambut(Tamu)` yang dipakai untuk Rina, padahal Rina tamu VIP! *Compiler* memilih versi *overload* saat kompilasi, dan saat itu ia hanya tahu **tipe variabel** `rina`, yaitu `Tamu`.
- **[3]** Sebaliknya, `rina.fasilitas()` menghasilkan versi VIP. *Override* dipilih saat program berjalan berdasarkan **objek** yang sebenarnya.
- **[4]** dan **[5]** Dua method bernama `sambut` dengan tipe parameter berbeda: ini *overloading*, bukan *overriding*.

> [!IMPORTANT]
> **Overload** dipilih *compiler* berdasarkan **tipe variabel argumen**, saat kompilasi. **Override** dipilih saat program berjalan berdasarkan **tipe objek** yang menerima panggilan. Karena itu, polimorfisme yang sesungguhnya (yang mengikuti objek) datang dari *override*. Jika ingin perilaku VIP mengikuti objeknya, taruh perilaku itu sebagai method yang di-*override* di kelas `TamuVip`, bukan sebagai versi *overload* di kelas lain.

## 8. Studi Kasus KedaiKita

File: [`studi-kasus/Pembayaran.java`](studi-kasus/Pembayaran.java), [`PembayaranTunai.java`](studi-kasus/PembayaranTunai.java), [`PembayaranQRIS.java`](studi-kasus/PembayaranQRIS.java), [`PembayaranKartu.java`](studi-kasus/PembayaranKartu.java), [`Pesanan.java`](studi-kasus/Pesanan.java), dan [`Main.java`](studi-kasus/Main.java)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-banyak-cara-bayar).

**Apa yang berubah dibanding Pertemuan 07?**

- **Empat file baru:** kelas induk `Pembayaran` dan tiga kelas anak, `PembayaranTunai`, `PembayaranQRIS`, dan `PembayaranKartu`.
- **`Pesanan.java`**: field `status` (`"BARU"` lalu `"LUNAS"`) dengan *getter*-nya, method baru `bayar(Pembayaran)`, dan versi *overload* `tambahItem(Menu)`. Struk ikut menampilkan status.
- **`Main.java`**: menambah bagian "SATU PANGGILAN, BANYAK BENTUK", pembayaran Budi dan Siti, serta "MEMERIKSA JENIS PEMBAYARAN".
- `Menu`, `Makanan`, `Minuman`, `ItemPesanan`, `Kedai`, `Pelanggan`, dan `Rupiah` **tidak berubah**.

Berikut kelas induknya, `Pembayaran.java`:

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

Ketiga kelas anak meng-*override* `namaMetode()` dan `proses()` dengan cara masing-masing: tunai menghitung kembalian, QRIS memotong saldo e-wallet, dan kartu mencetak persetujuan bank. Hanya `PembayaranKartu` yang juga meng-*override* biaya layanan (konstanta `PERSEN_BIAYA` bernilai 2):

```java
    @Override
    public int hitungBiayaLayanan(int total) {
        return total * PERSEN_BIAYA / 100;
    }
```

- **`Pembayaran`** menetapkan tiga method yang dimiliki **semua** jenis pembayaran. `hitungBiayaLayanan` bawaannya 0, jadi hanya kelas yang punya biaya tambahan yang perlu meng-*override*-nya.
- **Tunai dan QRIS tidak menulis `hitungBiayaLayanan`**, jadi biayanya 0 (warisan induk). Setiap `@Override` diperiksa *compiler*.
- **`getKembalian()` hanya ada di `PembayaranTunai`.** Method khusus ini nanti hanya bisa dipanggil setelah *downcasting*.
- **Kelas `Pembayaran` "umum" terasa janggal.** Tidak ada pelanggan yang membayar dengan "Pembayaran umum", tetapi `new Pembayaran()` tetap bisa ditulis. Di Pertemuan 10, kelas ini dijadikan `abstract class`.

Di `Pesanan.java`, inilah bagian yang baru. Pertama, versi *overload* `tambahItem`:

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

Lalu method `bayar`:

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
- **Parameter `bayar` bertipe `Pembayaran`**, sehingga mau menerima objek kelas anak mana pun (*upcasting* otomatis).
- **`bayar()` tidak punya satu pun `instanceof`.** Tiga baris bertanda `// polimorfisme` menjalankan method milik objek pembayaran yang sebenarnya.
- **Poin dihitung dari total pesanan** (sebelum biaya layanan): 1 poin per Rp10.000.

Di `Main.java`, bagian "SATU PANGGILAN, BANYAK BENTUK" memproses `List<Pembayaran>` berisi tiga jenis pembayaran dengan satu perulangan. Bagian baru yang paling menarik adalah pemeriksaan jenis:

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

Jalankan `javac *.java` lalu `java Main` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

Daftar menu di awal output sama persis dengan Pertemuan 07. Sesudahnya:

**Output:**

```text
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

Output ini **identik** dengan versi Python. Perhatikan pembayaran Siti: method `bayar()` yang **sama** dipanggil dua kali pada pesanan yang **sama**. Yang berbeda hanya objek pembayarannya, dan itulah yang menentukan seluruh perilakunya.

> [!TIP]
> **Coba sendiri:**
> 1. Ubah saldo QRIS Siti dari `20000` menjadi `50000`. Apa yang tercetak pada pembayaran Siti?
> 2. Di bagian "SATU PANGGILAN, BANYAK BENTUK", tambahkan `new Pembayaran()` ke `List.of(...)`. Baris apa yang muncul, dan mengapa terasa janggal?

<details>
<summary>Lihat jawaban</summary>

1. Pembayaran QRIS langsung berhasil. Tercetak `Saldo e-wallet terpotong Rp31.000, sisa Rp19.000` lalu `Status       : LUNAS (+3 poin)`, sehingga percobaan kartu kredit tidak dijalankan.

2. Muncul baris `Pembayaran umum      biaya layanan untuk Rp100.000: Rp0`. Janggal, karena "pembayaran umum" bukan metode bayar sungguhan. Objek seperti ini seharusnya tidak bisa dibuat. Pertemuan 10 akan memperbaikinya dengan `abstract class`.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan Error

Ingat dua jenis kesalahan di Java: **error kompilasi** (diawali nama file dan nomor baris, ada tanda `^`) dan **error saat berjalan** (diawali `Exception in thread "main"`). Tiga kesalahan lain sudah dibahas sebelumnya: *downcasting* tanpa *cast* dan `ClassCastException` di [bagian 3](#3-upcasting-downcasting-dan-instanceof), serta memanggil method lewat tipe yang tidak punya method itu di [bagian 5](#5-tanpa-duck-typing-java-butuh-tipe-bersama).

### Kesalahan 1: Memanggil method khusus lewat variabel bertipe induk

```java
        Pengguna p = new Mahasiswa("Ayu");
        System.out.println(p.isiKrs(21));
```

```text
E1.java:4: error: cannot find symbol
        System.out.println(p.isiKrs(21));
                            ^
  symbol:   method isiKrs(int)
  location: variable p of type Pengguna
1 error
```

**Artinya:** objeknya memang mahasiswa, tetapi *compiler* hanya melihat **tipe variabel** `p`, yaitu `Pengguna` (`variable p of type Pengguna`). Kelas `Pengguna` tidak punya `isiKrs`. **Perbaikan:** periksa dengan `instanceof`, lalu *downcast*: `if (p instanceof Mahasiswa m) { m.isiKrs(21); }`.

### Kesalahan 2: *Override* yang tanpa sengaja menjadi *overload*

`Segitiga` ingin meng-*override* `luas()`, tetapi menambahkan parameter:

```java
class Segitiga extends BangunDatar {
    // ... field dan konstruktor ...

    @Override
    public int luas(int skala) {
        return alas * tinggi / 2 * skala;
    }
}
```

```text
E5.java:23: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
```

**Artinya:** `BangunDatar` hanya punya `luas()` tanpa parameter. `luas(int skala)` punya daftar parameter berbeda, jadi ini **bukan** *override*, melainkan *overload*. Untungnya `@Override` membuat *compiler* protes. Tanpa `@Override`, kode ini lolos kompilasi, dan `bangun.luas()` pada objek segitiga diam-diam memakai versi induk, sehingga tercetak `0`. Kesalahan senyap seperti ini sulit dicari. **Perbaikan:** samakan daftar parameternya dengan versi induk, dan **selalu** tulis `@Override`.

### Kesalahan 3: *Overload* yang hanya berbeda tipe kembalian

```java
class Kalkulator {
    int hitung(int x) {
        return x * 2;
    }

    String hitung(int x) {
        return "Hasil: " + (x * 2);
    }
}
```

```text
E4.java:12: error: method hitung(int) is already defined in class Kalkulator
    String hitung(int x) {
           ^
1 error
```

**Artinya:** kedua method punya nama dan daftar parameter yang sama, `hitung(int)`. Tipe kembalian tidak ikut dihitung, karena saat memanggil `hitung(5)`, *compiler* tidak bisa menebak versi mana yang dimaksud. **Perbaikan:** beri nama berbeda, misalnya `hitung` dan `hitungTeks`, atau bedakan daftar parameternya.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK. Fokuslah pada kata kuncinya, seperti `cannot find symbol`, `incompatible types`, `does not override`, `is already defined`, dan `ClassCastException`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Override (dasar polimorfisme) | `@Override` + tanda tangan sama | `@Override public String bersuara()` |
| *Upcasting* (otomatis) | `Induk var = new Anak(...);` | `Hewan hewan = new Kucing("Oyen");` |
| Koleksi polimorfik | `List<Induk>` berisi objek anak | `List<BangunDatar> daftar = new ArrayList<>();` |
| Memeriksa jenis objek | `objek instanceof Kelas` | `pengguna instanceof Mahasiswa` |
| *Downcasting* (klasik) | `(Anak) var` | `Mahasiswa mhs = (Mahasiswa) pengguna;` |
| Cek + *cast* sekaligus (Java 16+) | `objek instanceof Kelas nama` | `if (pengguna instanceof Dosen dosen)` |
| Polimorfisme dari dalam kelas | panggil method lain di method induk | `System.out.println(isi());` |
| *Overload* method | nama sama, parameter berbeda | `cari(String)`, `cari(int)` |
| *Overload* konstruktor | `this(...)` ke konstruktor lain | `this("Perpustakaan Kampus");` |
| *Varargs* | `Tipe... nama` (parameter terakhir) | `void tambahBuku(Buku... daftarBuku)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
