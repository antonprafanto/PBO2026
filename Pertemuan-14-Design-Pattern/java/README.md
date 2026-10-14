# ☕ Praktik Java — Pertemuan 14: Design Pattern Dasar

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 14](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Singleton dengan `getInstance()`](#1-singleton-dengan-getinstance)
2. [Variasi Singleton: Eager dan Thread-Safe](#2-variasi-singleton-eager-dan-thread-safe)
3. [Sisi Gelap Singleton: State Global](#3-sisi-gelap-singleton-state-global)
4. [Simple Factory: Membuat Objek dari Teks](#4-simple-factory-membuat-objek-dari-teks)
5. [Factory Method: Subclass yang Memilih](#5-factory-method-subclass-yang-memilih)
6. [Strategy: Menukar Cara Menghitung](#6-strategy-menukar-cara-menghitung)
7. [Observer: Berlangganan Kabar](#7-observer-berlangganan-kabar)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan Error](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh, satu atau dua per pola
├── studi-kasus/     <- KedaiKita versi Pertemuan 14 (33 file .java)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah **program satu file**, jadi bisa langsung dijalankan (Java 11 ke atas):

```bash
cd Pertemuan-14-Design-Pattern/java/contoh
java Contoh01SingletonKonfigurasi.java
```

Studi kasus terdiri atas satu kelas per file. Kompilasi semuanya sekaligus, lalu jalankan kelas `Main`, dari **dalam** folder `studi-kasus`:

```bash
cd Pertemuan-14-Design-Pattern/java/studi-kasus
javac *.java
java Main
```

> [!IMPORTANT]
> Di setiap file contoh, kelas `public` yang memiliki method `main` ditulis **paling atas**, dan kelas atau *interface* pembantunya ditulis di bawahnya tanpa kata `public`. Urutan ini syarat perintah `java NamaFile.java`.

> [!TIP]
> Jika memakai VS Code, buka folder `java/` **milik pertemuan ini** (File → Open Folder), bukan seluruh repositori. Semua nama kelas di dalam folder ini sudah dibuat unik, jadi editor tidak akan protes. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

Semua contoh memakai materi yang sudah kamu kenal: `static` (Pertemuan 03), `private` (Pertemuan 04), kelas abstrak dan *interface* (Pertemuan 10), serta `List` dan `Map` (Pertemuan 12). Yang baru hanyalah **cara menyusunnya**.

## 1. Singleton dengan `getInstance()`

File: [`contoh/Contoh01SingletonKonfigurasi.java`](contoh/Contoh01SingletonKonfigurasi.java)

Kita mulai dari Singleton paling klasik: kelas `Konfigurasi` yang menyimpan bahasa dan tema aplikasi.

```java
/** Pengaturan aplikasi yang harus SAMA di semua bagian program. */
class Konfigurasi {
    private static Konfigurasi instance = null; // [1] field static: satu-satunya objek

    private Map<String, String> data = new LinkedHashMap<>();

    private Konfigurasi() { // [2] private: new Konfigurasi() ditolak di luar kelas ini
        System.out.println("  (objek Konfigurasi dibuat)");
        data.put("bahasa", "Indonesia");
        data.put("tema", "terang");
    }

    public static Konfigurasi getInstance() { // [3] satu-satunya pintu masuk
        if (instance == null) { // [4] dibuat hanya saat pertama diminta
            instance = new Konfigurasi();
        }
        return instance;
    }
```

Di bawahnya ada method `ambil(kunci)` dan `ubah(kunci, nilai)` untuk membaca dan mengubah isi `data`. Di kelas utama, `halamanBeranda()` dan `halamanProfil()` masing-masing mengambil konfigurasinya sendiri dengan `Konfigurasi konfigurasi = Konfigurasi.getInstance(); // [5]`, lalu mencetak bahasa dan temanya. Halaman Pengaturan dan awal `main()`:

```java
    static void halamanPengaturan() {
        System.out.println("Pengguna memilih tema gelap di halaman Pengaturan");
        Konfigurasi.getInstance().ubah("tema", "gelap"); // [6]
    }

    public static void main(String[] args) {
        System.out.println("=== MEMINTA KONFIGURASI DUA KALI ===");
        System.out.println("Permintaan pertama:");
        Konfigurasi a = Konfigurasi.getInstance();
        System.out.println("Permintaan kedua:");
        Konfigurasi b = Konfigurasi.getInstance();
        String sama = (a == b) ? "ya" : "tidak"; // [7] ==: objek yang sama?
        System.out.println("a dan b objek yang sama? " + sama);
```

Sisa `main()` memanggil Beranda dan Profil, lalu Pengaturan, lalu Beranda dan Profil sekali lagi.

**Output:**

```text
=== MEMINTA KONFIGURASI DUA KALI ===
Permintaan pertama:
  (objek Konfigurasi dibuat)
Permintaan kedua:
a dan b objek yang sama? ya

=== SEMUA HALAMAN MEMBACA PENGATURAN YANG SAMA ===
Beranda: bahasa Indonesia, tema terang
Profil : bahasa Indonesia, tema terang

=== DIUBAH DI SATU TEMPAT, TERLIHAT DI SEMUA TEMPAT ===
Pengguna memilih tema gelap di halaman Pengaturan
Beranda: bahasa Indonesia, tema gelap
Profil : bahasa Indonesia, tema gelap
```

Penjelasan:

- **[1]** Field `static` (Pertemuan 03) hanya ada satu untuk seluruh kelas. Ia menyimpan satu-satunya objek, awalnya `null`.
- **[2]** Konstruktor `private` (Pertemuan 04) hanya bisa dipanggil dari dalam kelas `Konfigurasi`. Menulis `new Konfigurasi()` di kelas lain langsung ditolak oleh *compiler*. Inilah penjaga terkuat Singleton di Java.
- **[3]** Method `static` dipanggil lewat nama kelas: `Konfigurasi.getInstance()`. Kita tidak butuh objek untuk memanggilnya, dan memang tidak bisa, karena objeknya justru belum ada.
- **[4]** Sifat ***lazy***: objek baru dibuat saat **pertama kali** diminta. Pesan `(objek Konfigurasi dibuat)` hanya muncul sekali.
- **[5]** Setiap halaman mengambil objek lewat `getInstance()`, tanpa menerimanya sebagai parameter. Praktis, tetapi ingat sisi gelapnya di bagian 3.
- **[6]** Halaman Pengaturan mengubah tema. Karena objeknya satu, perubahan langsung terlihat di Beranda dan Profil.
- **[7]** `==` pada objek memeriksa apakah dua variabel menunjuk ke **objek yang sama** (Pertemuan 02). Hasilnya `ya`.

> [!TIP]
> **Coba sendiri:** tambahkan baris `Konfigurasi c = new Konfigurasi();` di dalam `main()`, lalu jalankan. Program bahkan tidak sempat berjalan, karena *compiler* menolaknya. Pesan lengkapnya dibahas di Kesalahan 1.

## 2. Variasi Singleton: Eager dan Thread-Safe

File: [`contoh/Contoh02VariasiSingleton.java`](contoh/Contoh02VariasiSingleton.java)

Contoh 01 memakai cara *lazy*. Ada dua variasi lain yang sering kamu temui di kode Java.

**Variasi 1, *eager*:**

```java
/** Variasi 1: Singleton EAGER (objek disiapkan di awal). */
class PencatatLog {
    private static final PencatatLog INSTANCE = new PencatatLog(); // [1] dibuat sekali

    private List<String> catatan = new ArrayList<>();

    private PencatatLog() {
    }

    public static PencatatLog getInstance() {
        return INSTANCE; // [2] tidak perlu if: objeknya pasti sudah ada
    }
```

Di bawahnya ada method `catat(sumber, pesan)` dan `jumlah()`. Program utama memakainya lewat baris seperti `PencatatLog.getInstance().catat("kasir", "transaksi dibuka"); // [5]`.

**Variasi 2, *lazy* yang aman untuk banyak *thread*:**

```java
/** Variasi 2: Singleton LAZY yang aman untuk banyak thread. */
class Tema {
    private static Tema instance = null;

    private String warna = "terang";

    private Tema() {
        System.out.println("  (objek Tema dibuat)");
    }

    public static synchronized Tema getInstance() { // [3] thread masuk bergantian
        if (instance == null) { // [4] tetap lazy: dibuat saat pertama diminta
            instance = new Tema();
        }
        return instance;
    }
```

`Tema` juga punya *getter* dan *setter* untuk `warna`. Di `main()`, objeknya diminta dua kali: `Tema t1 = Tema.getInstance(); // [6]` lalu `Tema t2 = Tema.getInstance();`, kemudian keduanya dibandingkan dengan `==`.

**Output:**

```text
=== VARIASI 1: OBJEK DISIAPKAN DI AWAL (EAGER) ===
[LOG 1] kasir: transaksi dibuka
[LOG 2] laporan: laporan harian dibuat
Jumlah catatan: 2

=== VARIASI 2: DIBUAT SAAT PERTAMA DIMINTA (LAZY) ===
Permintaan pertama:
  (objek Tema dibuat)
Permintaan kedua:
t1 dan t2 objek yang sama? ya
Warna diubah lewat t1 menjadi gelap
Warna dibaca lewat t2: gelap
```

Penjelasan:

- **[1]** Objek dibuat langsung saat field `static final` diisi. Java melakukannya sekali saja, ketika kelas `PencatatLog` mulai dipakai. `final` menjamin field itu tidak bisa diganti objek lain. Nama konstanta ditulis UPPER_SNAKE: `INSTANCE`.
- **[2]** Karena objeknya pasti sudah ada, `getInstance()` cukup mengembalikannya. Proses pengisian field `static` dijamin Java hanya terjadi sekali, sehingga versi ini otomatis aman untuk banyak *thread*.
- **[3]** `synchronized` membuat thread masuk ke method ini **bergantian**. Jika dua thread memanggil `getInstance()` pada saat bersamaan, thread kedua menunggu sampai thread pertama selesai, sehingga tidak mungkin tercipta dua objek.
- **[4]** Pemeriksaan `null` tetap ada, jadi objek tetap dibuat saat pertama diminta.
- **[5]** Kelas lain cukup memanggil `PencatatLog.getInstance()`. `modulLaporan()` ditulis serupa.
- **[6]** Permintaan pertama membuat objek; permintaan kedua mengembalikan objek yang sama.

| Variasi | Kapan objek dibuat | Aman untuk banyak thread? | Catatan |
|---|---|---|---|
| *Lazy* biasa (contoh 01) | saat pertama diminta | tidak | cukup untuk program satu alur seperti milik kita |
| *Eager* (`static final`) | saat kelas mulai dipakai | ya | paling sederhana |
| *Lazy* + `synchronized` | saat pertama diminta | ya | ada sedikit biaya menunggu di setiap pemanggilan |

> [!NOTE]
> Output contoh ini sengaja dibuat **sama persis** dengan versi Python, walaupun mekanismenya berbeda. Python memakai objek tingkat modul dan method `__new__`. Perbandingannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 3. Sisi Gelap Singleton: State Global

File: [`contoh/Contoh03BahayaStateGlobal.java`](contoh/Contoh03BahayaStateGlobal.java)

Di halaman konsep disebutkan bahwa Singleton sulit diuji. Contoh ini membuktikannya. `PengaturanPajak` adalah Singleton seperti contoh 01, dengan *getter* `getPersen()` dan *setter* `setPersen()` (awalnya 10). Harga akhir dihitung dengan membaca Singleton itu:

```java
    static int hargaAkhir(int harga) {
        // [1] ketergantungan tersembunyi: tidak terlihat dari parameternya
        int persen = PengaturanPajak.getInstance().getPersen();
        return harga + harga * persen / 100;
    }
```

`ujiHargaNormal()` memeriksa bahwa Rp10000 ditambah pajak menjadi Rp11000. Uji kedua dan program utamanya:

```java
    static String ujiAcaraBebasPajak() {
        PengaturanPajak.getInstance().setPersen(0); // [2] mengubah state global...
        int hasil = hargaAkhir(10000);              // ...dan lupa mengembalikannya
        return hasil == 10000 ? "LULUS" : "GAGAL (dapat Rp" + hasil + ")";
    }

    public static void main(String[] args) {
        System.out.println("=== PUTARAN 1: DUA UJI DIJALANKAN ===");
        System.out.println("Uji harga normal      : " + ujiHargaNormal());
        System.out.println("Uji acara bebas pajak : " + ujiAcaraBebasPajak());

        System.out.println();
        System.out.println("=== PUTARAN 2: UJI YANG SAMA DIULANG ===");
        System.out.println("Uji harga normal      : " + ujiHargaNormal()); // [4] kini gagal!
        System.out.println("Pajak sekarang " + PengaturanPajak.getInstance().getPersen()
                + "%, sisa perubahan uji sebelumnya");

        System.out.println();
        System.out.println("=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===");
        KalkulatorHarga normal = new KalkulatorHarga(10); // [5] setiap uji punya objeknya sendiri
        KalkulatorHarga bebasPajak = new KalkulatorHarga(0);
```

Solusinya ada di kelas `KalkulatorHarga` (bertanda `[3]` di file). Ia menerima `persenPajak` lewat konstruktor, menyimpannya di field `private`, lalu memakainya di method `hargaAkhir(int harga)`.

**Output:**

```text
=== PUTARAN 1: DUA UJI DIJALANKAN ===
Uji harga normal      : LULUS
Uji acara bebas pajak : LULUS

=== PUTARAN 2: UJI YANG SAMA DIULANG ===
Uji harga normal      : GAGAL (dapat Rp10000)
Pajak sekarang 0%, sisa perubahan uji sebelumnya

=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===
Pajak 10%: Rp10000 -> Rp11000
Pajak 0% : Rp10000 -> Rp10000
Diulang  : Rp10000 -> Rp11000 (tetap benar)
```

Penjelasan:

- **[1]** Dari luar, `hargaAkhir(int harga)` terlihat hanya butuh `harga`. Padahal diam-diam ia juga bergantung pada Singleton. Inilah **ketergantungan tersembunyi**.
- **[2]** Uji kedua mengubah pajak menjadi 0 dan lupa mengembalikannya. Karena objeknya satu untuk seluruh program, perubahan itu **menetap**.
- **[3]** Solusinya adalah DIP dari Pertemuan 13: kebutuhan dikirim lewat konstruktor, sehingga terlihat jelas dan mudah diganti.
- **[4]** Uji yang **sama persis**, yang tadi LULUS, kini GAGAL. Hasil uji bergantung pada urutan dan sejarah.
- **[5]** Setiap `KalkulatorHarga` membawa nilainya sendiri, jadi objek berpajak 0% tidak mengganggu objek berpajak 10%.

> [!TIP]
> Singleton dan *dependency injection* bisa berdampingan. Di bagian paling luar program (misalnya `main()`), ambil nilainya dari Singleton lalu **kirimkan**: `new KalkulatorHarga(PengaturanPajak.getInstance().getPersen())`. Kelas-kelas di dalam tetap mudah diuji karena tidak meraih Singleton sendiri.

## 4. Simple Factory: Membuat Objek dari Teks

File: [`contoh/Contoh04SimpleFactory.java`](contoh/Contoh04SimpleFactory.java)

Aplikasi ojek online menerima pilihan kendaraan berupa teks. Kelas abstrak `Kendaraan` punya method abstrak `nama()`, `kapasitas()`, dan `tarifPerKm()`, serta method biasa `hitungOngkos(jarakKm)`. Tiga kelas anaknya mengisi method abstrak itu: `Motor` (1 penumpang, Rp2500/km), `Mobil` (4 penumpang, Rp4000/km), dan `MobilBesar` (6 penumpang, Rp5500/km). Bagian utamanya adalah factory:

```java
/** Simple Factory: SATU tempat yang memutuskan kelas mana yang dibuat. */
class KendaraanFactory {

    public static Kendaraan buat(String jenis) { // [1] tipe kembalian: kelas abstrak
        if (jenis.equalsIgnoreCase("motor")) { // [2] "MOBIL" dan "mobil" dianggap sama
            return new Motor();
        }
        if (jenis.equalsIgnoreCase("mobil")) {
            return new Mobil();
        }
        if (jenis.equalsIgnoreCase("mobil besar")) {
            return new MobilBesar();
        }
        throw new IllegalArgumentException("Jenis kendaraan tidak dikenal: " + jenis); // [3]
    }
}
```

Pemakainya di `main()`:

```java
        System.out.println("=== PESANAN DARI APLIKASI (JARAK 8 KM) ===");
        for (String pilihan : List.of("motor", "Mobil", "MOBIL BESAR")) {
            Kendaraan kendaraan = KendaraanFactory.buat(pilihan); // [4] cukup kirim teks
            int ongkos = kendaraan.hitungOngkos(8);
            System.out.println(String.format("%-12s -> %-12s ", pilihan, kendaraan.nama())
                    + "maks " + kendaraan.kapasitas() + " penumpang, Rp" + ongkos);
        }
```

Setelah itu, `main()` mencoba `KendaraanFactory.buat("helikopter")` di dalam `try` dan menangkapnya dengan `catch (IllegalArgumentException e) { // [5]`.

**Output:**

```text
=== PESANAN DARI APLIKASI (JARAK 8 KM) ===
motor        -> Motor        maks 1 penumpang, Rp20000
Mobil        -> Mobil        maks 4 penumpang, Rp32000
MOBIL BESAR  -> Mobil Besar  maks 6 penumpang, Rp44000

=== PILIHAN TIDAK DIKENAL ===
Ditolak: Jenis kendaraan tidak dikenal: helikopter
```

Penjelasan:

- **[1]** Method `static` milik kelas factory. Tipe kembaliannya `Kendaraan`, kelas **abstrak**. Pemanggil hanya dijanjikan "sebuah kendaraan", bukan kelas tertentu.
- **[2]** `equalsIgnoreCase()` membandingkan teks tanpa memedulikan huruf besar/kecil. Ingat, teks di Java dibandingkan dengan method, bukan `==`.
- **[3]** Pilihan yang tidak dikenal ditolak di **satu tempat**. `IllegalArgumentException` adalah *unchecked exception* (Pertemuan 11), jadi method ini tidak perlu menulis `throws`.
- **[4]** Pemanggil tidak pernah menulis `new Motor()`. Ia cukup mengirim teks, lalu memakai objek hasilnya lewat method milik `Kendaraan`. Polimorfisme (Pertemuan 09) bekerja sama dengan factory.
- **[5]** Kesalahan input ditangkap dengan `try`/`catch` seperti biasa.

> [!TIP]
> **Coba sendiri:** tambahkan kelas `Bajaj extends Kendaraan` (kapasitas 2, tarif Rp3000/km) dan daftarkan di factory dengan pilihan `"bajaj"`. Yang perlu diubah hanya kelas baru itu dan **satu** cabang `if` di factory. Bagian `main()` tidak berubah sama sekali.

## 5. Factory Method: Subclass yang Memilih

File: [`contoh/Contoh05FactoryMethod.java`](contoh/Contoh05FactoryMethod.java)

Sekarang versi GoF. Tidak ada lagi `if`: setiap kelas anak memutuskan sendiri produk yang dibuatnya. Produknya adalah *interface* `Angkutan` dengan satu method, `String antar(String tujuan)`, yang diimplementasikan oleh `Truk` dan `KapalSungai`.

```java
/** Langkah kerja tetap, tetapi produk angkutannya diserahkan ke subclass. */
abstract class Ekspedisi {
    public abstract String nama();

    public abstract Angkutan buatAngkutan(); // [1] inilah FACTORY METHOD

    public void kirimPaket(String tujuan) { // [2] memakai produk tanpa tahu kelasnya
        System.out.println("[" + nama() + "] Paket ke " + tujuan + " dikemas");
        Angkutan angkutan = buatAngkutan();
        System.out.println("  " + angkutan.antar(tujuan));
        System.out.println("  Paket tiba di " + tujuan);
    }
}

class EkspedisiDarat extends Ekspedisi {
    @Override
    public String nama() {
        return "Ekspedisi Darat";
    }

    @Override
    public Angkutan buatAngkutan() { // [3] subclass memilih produknya
        return new Truk();
    }
}
```

`EkspedisiSungai` ditulis serupa, dengan `buatAngkutan()` yang mengembalikan `new KapalSungai()`. Program utamanya:

```java
        Ekspedisi darat = new EkspedisiDarat();
        Ekspedisi sungai = new EkspedisiSungai();
        darat.kirimPaket("Balikpapan"); // [4] method sama, angkutan berbeda
        sungai.kirimPaket("Tenggarong");
```

**Output:**

```text
=== FACTORY METHOD: SUBCLASS MEMILIH ANGKUTANNYA ===
[Ekspedisi Darat] Paket ke Balikpapan dikemas
  Truk melaju lewat jalan darat menuju Balikpapan
  Paket tiba di Balikpapan
[Ekspedisi Sungai] Paket ke Tenggarong dikemas
  Kapal menyusuri Sungai Mahakam menuju Tenggarong
  Paket tiba di Tenggarong
```

Penjelasan:

- **[1]** `buatAngkutan()` adalah *factory method*: method abstrak yang tugasnya **membuat** produk. Kelas induk tidak tahu produknya apa.
- **[2]** `kirimPaket()` adalah langkah kerja tetap: kemas, buat angkutan, antar, tiba. Ia memakai hasil `buatAngkutan()` sebagai `Angkutan`. Pola "kerangka di induk, langkah tertentu di anak" ini juga punya nama sendiri: *Template Method*.
- **[3]** Kelas anak meng-*override* factory method dan memilih produknya. Inilah bedanya dengan Simple Factory: keputusan diambil lewat *overriding*, bukan lewat `if`.
- **[4]** Tipe variabelnya `Ekspedisi`. Method yang dipanggil sama, tetapi angkutan yang dipakai berbeda.

Mengapa `Ekspedisi` berupa kelas abstrak, sedangkan `Angkutan` berupa *interface*? `Ekspedisi` punya method konkret (`kirimPaket`) yang diwariskan, sedangkan `Angkutan` hanya berisi kontrak. Aturan memilihnya sama dengan Pertemuan 10.

> [!TIP]
> **Coba sendiri:** buat `EkspedisiUdara` dengan produk `Pesawat`. Kamu hanya **menambah** dua kelas. Tidak ada satu baris pun kode lama yang diubah.

## 6. Strategy: Menukar Cara Menghitung

File: [`contoh/Contoh06StrategyOngkir.java`](contoh/Contoh06StrategyOngkir.java)

Kontraknya berupa *interface* `StrategiOngkir` dengan dua method: `String nama();` dan `int hitung(int beratKg);`. Tiga kelas mengimplementasikannya dengan rumus berbeda:

| Strategi | `nama()` | Rumus `hitung(beratKg)` |
|---|---|---|
| `OngkirReguler` | Reguler (3 hari) | `8000 * beratKg` |
| `OngkirKilat` | Kilat (besok tiba) | `15000 * beratKg + 5000` |
| `OngkirHemat` | Hemat (5 hari) | `5000 * Math.max(beratKg, 3)` (minimal dihitung 3 kg) |

Yang memakai strategi adalah `Pengiriman` (*context*):

```java
/** Context: memakai strategi ongkir tanpa tahu rumus di dalamnya. */
class Pengiriman {
    private int beratKg;
    private StrategiOngkir strategi; // [1] strategi disimpan sebagai field

    Pengiriman(int beratKg, StrategiOngkir strategi) {
        this.beratKg = beratKg;
        this.strategi = strategi;
    }

    public void aturStrategi(StrategiOngkir strategi) { // [2] bisa ditukar
        this.strategi = strategi;
    }

    public int ongkir() {
        return strategi.hitung(beratKg); // [3] didelegasikan
    }

    public String ringkasan() {
        return String.format("%-20s Rp", strategi.nama()) + ongkir();
    }
}
```

Program utamanya:

```java
        Pengiriman paket = new Pengiriman(2, new OngkirReguler());
        System.out.println("=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===");
        List<StrategiOngkir> daftarStrategi = List.of(new OngkirReguler(),
                new OngkirKilat(), new OngkirHemat());
        for (StrategiOngkir strategi : daftarStrategi) {
            paket.aturStrategi(strategi); // [4] tukar saat program berjalan
            System.out.println(paket.ringkasan());
        }

        System.out.println();
        System.out.println("=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===");
        paket.aturStrategi(new OngkirAmbilSendiri()); // [5]
        System.out.println(paket.ringkasan());
```

**Output:**

```text
=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===
Reguler (3 hari)     Rp16000
Kilat (besok tiba)   Rp35000
Hemat (5 hari)       Rp15000

=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===
Ambil di gerai       Rp0
```

Penjelasan:

- **[1]** *Context* **menyimpan** objek strategi sebagai field bertipe *interface*. Ini hubungan "punya" (agregasi, Pertemuan 05).
- **[2]** `aturStrategi()` menukar strategi kapan saja, bahkan setelah objek `Pengiriman` dibuat.
- **[3]** `Pengiriman` tidak menghitung apa pun sendiri. Ia **mendelegasikan** pekerjaan ke strategi.
- **[4]** Satu objek `paket` yang sama dihitung dengan tiga strategi bergantian. Tidak ada `if` sama sekali.
- **[5]** `OngkirAmbilSendiri` (nama "Ambil di gerai", ongkir selalu 0) sengaja ditulis **paling bawah** di file, seolah-olah ditambahkan belakangan. `Pengiriman` tidak diubah sedikit pun: OCP terpenuhi.

> [!TIP]
> **Coba sendiri:** buat kelas `OngkirSameDay implements StrategiOngkir` (Rp25000 per kg) lalu tambahkan ke `List.of(...)` di `main()`. Berat 2 kg seharusnya menghasilkan Rp50000.

## 7. Observer: Berlangganan Kabar

File: [`contoh/Contoh07ObserverKanalVideo.java`](contoh/Contoh07ObserverKanalVideo.java)

Kontrak pengamatnya adalah *interface* `PengamatKanal` dengan satu method: `void perbarui(String namaKanal, String judul);`. Ada dua pengamat konkret: `Penonton` mencetak notifikasi ke "HP"-nya, sedangkan `PencatatStatistik` menghitung jumlah video. Subject-nya adalah `KanalVideo`:

```java
/** Subject: menyimpan daftar pengamat dan memberi kabar ke semuanya. */
class KanalVideo {
    private String nama;
    private List<PengamatKanal> daftarPengamat = new ArrayList<>(); // [1]

    KanalVideo(String nama) {
        this.nama = nama;
    }

    public void langganan(PengamatKanal pengamat) { // [2]
        daftarPengamat.add(pengamat);
    }

    public void berhentiLangganan(PengamatKanal pengamat) {
        daftarPengamat.remove(pengamat);
    }

    public void unggahVideo(String judul) {
        System.out.println(nama + " mengunggah: " + judul);
        beriKabar(judul); // [3] kejadian -> semua pengamat diberi tahu
    }

    private void beriKabar(String judul) {
        for (PengamatKanal pengamat : daftarPengamat) { // [4] tidak peduli jenisnya
            pengamat.perbarui(nama, judul);
        }
    }
}
```

Di `main()`, kanal "Belajar PBO" mendapat tiga pengamat: penonton Ayu, penonton Bima, dan sebuah `PencatatStatistik`. Setelah video pertama diunggah, Bima berhenti berlangganan dengan `kanal.berhentiLangganan(bima); // [5]`, lalu video kedua diunggah.

**Output:**

```text
=== VIDEO PERTAMA (3 PENGAMAT) ===
Belajar PBO mengunggah: Kelas dan Objek
  [HP Ayu] Video baru dari Belajar PBO: Kelas dan Objek
  [HP Bima] Video baru dari Belajar PBO: Kelas dan Objek
  [STATISTIK] Belajar PBO sudah mengunggah 1 video

=== BIMA BERHENTI BERLANGGANAN ===
Belajar PBO mengunggah: Design Pattern Dasar
  [HP Ayu] Video baru dari Belajar PBO: Design Pattern Dasar
  [STATISTIK] Belajar PBO sudah mengunggah 2 video
```

Penjelasan:

- **[1]** Subject menyimpan pengamat dalam `List<PengamatKanal>`, bertipe *interface*, bukan `Penonton`.
- **[2]** `langganan()` dan `berhentiLangganan()` adalah pintu untuk mendaftar dan keluar.
- **[3]** Setiap kejadian (video baru) langsung diikuti pemberian kabar. `beriKabar()` dibuat `private` karena hanya urusan internal kanal.
- **[4]** `KanalVideo` memanggil `perbarui()` milik setiap pengamat tanpa tahu apakah itu penonton atau pencatat statistik. Data kejadian dikirim sebagai argumen: inilah gaya **push**.
- **[5]** Setelah Bima berhenti berlangganan, ia tidak lagi menerima kabar video kedua.

> [!NOTE]
> `daftarPengamat.remove(pengamat)` memanggil versi `remove(Object)`, yang menghapus objek tersebut dari list. Jika objeknya tidak ada di list, method ini hanya mengembalikan `false` tanpa error.

## 8. Studi Kasus KedaiKita

File baru: [`PengaturanKedai.java`](studi-kasus/PengaturanKedai.java), [`PembayaranFactory.java`](studi-kasus/PembayaranFactory.java), [`DiskonHappyHour.java`](studi-kasus/DiskonHappyHour.java), [`PengamatPesanan.java`](studi-kasus/PengamatPesanan.java), [`LayarDapur.java`](studi-kasus/LayarDapur.java), [`NotifikasiPelanggan.java`](studi-kasus/NotifikasiPelanggan.java). File yang berubah: [`Pesanan.java`](studi-kasus/Pesanan.java), [`StrukPesanan.java`](studi-kasus/StrukPesanan.java), [`LaporanPenjualan.java`](studi-kasus/LaporanPenjualan.java), dan [`Main.java`](studi-kasus/Main.java).

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini).

**Apa yang berubah dibanding Pertemuan 13?**

- **Baru** `PengaturanKedai` (Singleton: nama kedai, alamat, pajak 10%) dan `PembayaranFactory`.
- **Baru** strategi `DiskonHappyHour`.
- **Baru** *interface* `PengamatPesanan` beserta dua implementasinya, `LayarDapur` dan `NotifikasiPelanggan`.
- `Pesanan`: ada `hitungPajak()`, total kini memuat pajak, ada daftar pengamat, `tambahPengamat()`, `ubahStatus()`, dan `bayar()` mengubah status lewat `ubahStatus("LUNAS")`.
- `StrukPesanan`: kepala struk memakai nama dan alamat dari `PengaturanKedai`, dan ada baris pajak.
- `LaporanPenjualan`: hanya teks label menjadi "(sebelum diskon & pajak)". `Diskon` dan `Pembayaran` hanya berubah di komentar kepalanya.
- `Main` ditulis ulang: empat bagian, satu bagian per pola.
- Kelas lain **tidak berubah**.

Jalankan dari dalam folder `studi-kasus`:

```bash
cd Pertemuan-14-Design-Pattern/java/studi-kasus
javac *.java
java Main
```

### 8.1 Singleton: `PengaturanKedai`

Kelas ini punya field `private static PengaturanKedai instance = null;` serta field `namaKedai`, `alamat`, dan `pajakPersen`. Bagian intinya:

```java
    // Konstruktor PRIVATE: kode di luar kelas ini tidak bisa menulis
    // new PengaturanKedai(). Satu-satunya jalan adalah getInstance().
    private PengaturanKedai() {
        this.namaKedai = "KedaiKita";
        this.alamat = "Jl. Pramuka No. 10, Samarinda";
        this.pajakPersen = 10; // Pajak Barang dan Jasa Tertentu (PBJT) 10%
    }

    /** Mengembalikan satu-satunya objek; dibuat saat pertama kali diminta. */
    public static PengaturanKedai getInstance() {
        if (instance == null) {
            instance = new PengaturanKedai();
        }
        return instance;
    }
```

Di bawahnya ada *getter* `getNamaKedai()`, `getAlamat()`, `getPajakPersen()`, dan satu *setter* `setPajakPersen()` yang memvalidasi nilai 0 sampai 100. Struktur Singleton-nya sama persis dengan contoh 01. Pajak 10% di sini adalah nilai simulasi untuk latihan.

Bagian pertama `main()` meminta pengaturan dua kali (`pengaturanA` dan `pengaturanB`), membandingkannya dengan `==`, lalu mencetak isinya:

**Output:**

```text
=== 1. SINGLETON: PENGATURAN KEDAI ===
Objek yang sama? ya
Nama   : KedaiKita
Alamat : Jl. Pramuka No. 10, Samarinda
Pajak  : 10%
```

### 8.2 Factory: `PembayaranFactory`

```java
/** Factory: membuat objek Pembayaran berdasarkan pilihan (teks). */
public class PembayaranFactory {

    /** nominal = uang diterima (tunai) atau saldo e-wallet (qris). */
    public static Pembayaran buat(String jenis, int nominal, String bank) {
        // equalsIgnoreCase: huruf besar/kecil dianggap sama ("QRIS" = "qris").
        if (jenis.equalsIgnoreCase("tunai")) {
            return new PembayaranTunai(nominal);
        }
        if (jenis.equalsIgnoreCase("qris")) {
            return new PembayaranQRIS(nominal);
        }
        if (jenis.equalsIgnoreCase("kartu")) {
            return new PembayaranKartu(bank);
        }
        throw new IllegalArgumentException("Metode pembayaran tidak dikenal: " + jenis);
    }
}
```

- Tipe kembaliannya `Pembayaran`, kelas abstrak dari Pertemuan 10. Kelas lain tidak perlu menyebut `PembayaranTunai`, `PembayaranQRIS`, atau `PembayaranKartu`.
- Java tidak punya nilai bawaan parameter seperti Python, jadi pemanggil selalu mengirim ketiga argumen, misalnya `PembayaranFactory.buat("tunai", 100000, "")`.

Bagian kedua `main()` memanggil `PembayaranFactory.buat(pilihan, 100000, "BNI")` untuk pilihan `"tunai"`, `"QRIS"`, dan `"kartu"`, lalu mencoba `"bitcoin"` di dalam `try`/`catch (IllegalArgumentException e)`:

**Output:**

```text
=== 2. FACTORY: MEMBUAT PEMBAYARAN DARI PILIHAN ===
Pilihan 'tunai' -> Tunai (biaya layanan Rp0)
Pilihan 'QRIS' -> QRIS (biaya layanan Rp0)
Pilihan 'kartu' -> Kartu Kredit BNI (biaya layanan Rp2.000)
Ditolak: Metode pembayaran tidak dikenal: bitcoin
```

Pilihan `'QRIS'` ditulis kapital, tetapi tetap dikenali berkat `equalsIgnoreCase()`. Biaya layanan kartu Rp2.000 adalah 2% dari Rp100.000 (aturan sejak Pertemuan 09).

### 8.3 Strategy: `DiskonHappyHour`

Strategi baru ini cukup satu file baru. `Diskon`, `TanpaDiskon`, `DiskonPersen`, dan `DiskonMember` tidak berubah.

```java
/** Happy hour: diskon 20% khusus untuk item minuman. */
public class DiskonHappyHour implements Diskon {
    private static final int PERSEN = 20;

    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        int totalMinuman = 0;
        for (ItemPesanan item : daftarItem) {
            if (item.getMenu().getKategori().equals("Minuman")) {
                totalMinuman += item.hitungSubtotal();
            }
        }
        return totalMinuman * PERSEN / 100;
    }

    @Override
    public String keterangan() {
        return "Happy Hour (minuman)";
    }
}
```

Total pesanan kini memuat pajak. Di `Pesanan.java`:

```java
    /** Pajak dihitung dari subtotal setelah dipotong diskon. */
    public int hitungPajak() {
        int persen = PengaturanKedai.getInstance().getPajakPersen();
        return (hitungSubtotal() - hitungPotongan()) * persen / 100;
    }

    public int hitungTotal() {
        return hitungSubtotal() - hitungPotongan() + hitungPajak();
    }
```

Bagian ketiga `main()` memasang `new TanpaDiskon()`, `new DiskonPersen(15)`, dan `new DiskonHappyHour()` secara bergantian pada pesanan Rina lewat `pesananRina.aturDiskon(strategi)`, lalu mencetak potongan dan totalnya:

**Output:**

```text
=== 3. STRATEGY: MENUKAR ATURAN DISKON ===
Subtotal pesanan Rina: Rp59.000
Tanpa diskon           potongan      Rp0, total Rp64.900
Promo 15%              potongan  Rp8.850, total Rp55.165
Happy Hour (minuman)   potongan  Rp7.200, total Rp56.980
```

- `aturDiskon()` adalah cara menukar strategi, persis seperti `aturStrategi()` di contoh 06. Method ini sudah ada sejak Pertemuan 13. Hari ini kita sekadar mengenali namanya: **Strategy**.
- Happy Hour hanya memotong minuman: 20% dari Rp36.000 (2 kopi) = Rp7.200. Mie goreng tidak ikut dipotong.
- Pajak dibaca dari Singleton, lalu dihitung dari subtotal setelah diskon. Contoh Promo 15%: (59.000 − 8.850) × 10% = Rp5.015, sehingga total Rp55.165.
- `aturDiskon()` dideklarasikan `throws KedaiException` (pesanan lunas tidak boleh diubah), dan `main()` meneruskannya dengan `throws KedaiException`. Komentar di `Main.java` menjelaskan alasannya: di skenario demo ini datanya dijamin valid.

### 8.4 Observer: `PengamatPesanan`, `LayarDapur`, `NotifikasiPelanggan`

```java
/** Kontrak untuk objek yang ingin diberi tahu perubahan status pesanan. */
public interface PengamatPesanan {

    /**
     * Dipanggil oleh Pesanan setiap kali statusnya berubah.
     *
     * Parameternya langsung bertipe Pesanan, walaupun Pesanan sendiri juga
     * memakai PengamatPesanan. Di Java hal ini aman: tidak ada masalah
     * "circular import" seperti di Python.
     */
    void perbarui(Pesanan pesanan);
}
```

`Pesanan` memakai `PengamatPesanan`, dan `PengamatPesanan` memakai `Pesanan`. Di Java hal ini tidak masalah, karena `javac *.java` mengompilasi semua file **bersama-sama** dan mengenali semua kelas sekaligus. Versi Python terpaksa menghilangkan petunjuk tipe di parameter ini (lihat Jembatan).

Ada dua implementasinya. `LayarDapur` mencetak isi pesanan (semua item digabung dengan `String.join(", ", ...)`) saat statusnya `LUNAS`, dan hanya nomor serta status untuk perubahan lainnya. `NotifikasiPelanggan` menarik data pelanggan dari pesanan:

```java
    @Override
    public void perbarui(Pesanan pesanan) {
        Pelanggan pelanggan = pesanan.getPelanggan();
        System.out.println("  [SMS ke " + pelanggan.getNoHp() + "] Halo " + pelanggan.getNama()
                + ", status pesanan " + pesanan.getNomor() + ": " + pesanan.getStatus());
    }
```

Subject-nya adalah `Pesanan`, yang kini punya field `private List<PengamatPesanan> daftarPengamat` dan dua method baru:

```java
    // ----- pola Observer -----
    public void tambahPengamat(PengamatPesanan pengamat) {
        daftarPengamat.add(pengamat);
    }

    /** Mengubah status lalu memberi tahu SEMUA pengamat. */
    public void ubahStatus(String statusBaru) {
        if (!STATUS_VALID.contains(statusBaru)) {
            throw new IllegalArgumentException("Status tidak dikenal: " + statusBaru);
        }
        status = statusBaru;
        for (PengamatPesanan pengamat : daftarPengamat) {
            pengamat.perbarui(this);
        }
    }
```

- `STATUS_VALID` adalah `List.of("BARU", "LUNAS", "DIPROSES", "SIAP", "SELESAI")`. Status lain ditolak.
- `pengamat.perbarui(this)` mengirim **objek pesanan itu sendiri**. Inilah gaya **pull**: `LayarDapur` menarik nomor dan item, `NotifikasiPelanggan` menarik data pelanggan.
- Di `bayar()`, baris `status = "LUNAS";` versi Pertemuan 13 kini diganti `ubahStatus("LUNAS");` di akhir method, sehingga pengamat ikut tahu saat pesanan dibayar.

Bagian keempat `main()` membuat pesanan Budi (2 Kopi Susu Gula Aren, 1 Nasi Goreng Kampung), mendaftarkan `new LayarDapur()` dan `new NotifikasiPelanggan()` lewat `tambahPengamat()`, membayar dengan `PembayaranFactory.buat("tunai", 100000, "")`, lalu memanggil `ubahStatus()` untuk `DIPROSES`, `SIAP`, dan `SELESAI`:

**Output:**

```text
=== 4. OBSERVER: NOTIFIKASI STATUS PESANAN ===
Pembayaran pesanan P002 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp67.100
  Uang diterima Rp100.000, kembalian Rp32.900
  Status       : LUNAS (+6 poin)
  [DAPUR] Pesanan baru P002: 2 x Kopi Susu Gula Aren, 1 x Nasi Goreng Kampung
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: LUNAS
Status diubah menjadi DIPROSES:
  [DAPUR] P002 -> DIPROSES
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: DIPROSES
Status diubah menjadi SIAP:
  [DAPUR] P002 -> SIAP
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: SIAP
Status diubah menjadi SELESAI:
  [DAPUR] P002 -> SELESAI
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: SELESAI
```

Empat perubahan status × dua pengamat = delapan kabar, padahal `Pesanan` tidak pernah menyebut nama `LayarDapur` atau `NotifikasiPelanggan`.

### 8.5 Struk Baru: `StrukPesanan`

Di awal `buatTeks()`, struk mengambil `PengaturanKedai pengaturan = PengaturanKedai.getInstance();`, lalu memakai `pengaturan.getNamaKedai()` dan `pengaturan.getAlamat()` sebagai kepala struk. Di bagian akhir ada baris pajak:

```java
        String pajak = "Pajak " + pengaturan.getPajakPersen() + "%";
        baris.add(barisRapi(pajak, Rupiah.format(p.hitungPajak())));
        baris.add(barisRapi("TOTAL", Rupiah.format(p.hitungTotal())));
```

Label `Pajak 10%` dan hitungan pajaknya sama-sama berasal dari `PengaturanKedai`. Jika pajak diubah lewat *setter*, label dan angkanya pasti berubah bersamaan.

**Output:**

```text
========================================
KedaiKita
Jl. Pramuka No. 10, Samarinda
========================================
No. Pesanan : P002
Pelanggan   : Budi Santoso
Status      : SELESAI
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
Subtotal                        Rp61.000
Pajak 10%                        Rp6.100
TOTAL                           Rp67.100
========================================
```

> [!TIP]
> **Coba sendiri:** di awal `main()`, tambahkan `PengaturanKedai.getInstance().setPajakPersen(11);`. Kompilasi dan jalankan lagi. Berapa total pesanan Budi sekarang, dan apa tulisan di struk?

<details>
<summary>Lihat jawaban</summary>

Pajak menjadi 11% × Rp61.000 = Rp6.710, sehingga total menjadi **Rp67.710**, dan struk menampilkan `Pajak 11%`. Total di bagian Strategy juga ikut berubah. Satu baris mengubah seluruh program: inilah kekuatan sekaligus bahaya state global.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan Error

Semua kesalahan di bawah ini adalah **error kompilasi**: `javac` menolak kodenya sebelum program sempat berjalan. Pesannya diawali nama file dan nomor baris, dan tanda `^` menunjuk posisi kesalahannya.

### Kesalahan 1: Membuat objek Singleton dengan `new`

File `Coba1.java` di folder studi kasus berisi:

```java
        PengaturanKedai pengaturan = new PengaturanKedai();
```

```text
Coba1.java:3: error: PengaturanKedai() has private access in PengaturanKedai
        PengaturanKedai pengaturan = new PengaturanKedai();
                                     ^
1 error
```

**Artinya:** konstruktor `PengaturanKedai()` bersifat `private`, jadi hanya kelas itu sendiri yang boleh memanggilnya. Inilah perlindungan Singleton yang bekerja. **Perbaikan:** `PengaturanKedai.getInstance()`.

### Kesalahan 2: Lupa `static` pada `getInstance()`

Di file `Coba2.java`, kelas `Konfigurasi` ditulis seperti contoh 01, tetapi kata `static` terlupa:

```java
    public Konfigurasi getInstance() {
```

Lalu `main()` memanggilnya seperti biasa:

```java
        Konfigurasi konfigurasi = Konfigurasi.getInstance();
```

```text
Coba2.java:3: error: non-static method getInstance() cannot be referenced from a static context
        Konfigurasi konfigurasi = Konfigurasi.getInstance();
                                             ^
1 error
```

**Artinya:** tanpa `static`, `getInstance()` adalah method milik **objek**, sehingga harus dipanggil lewat sebuah objek. Padahal objek baru bisa didapat dari `getInstance()` itu sendiri, dan konstruktornya `private`. Lingkaran setan! **Perbaikan:** `public static Konfigurasi getInstance()`.

### Kesalahan 3: Pengamat lupa mengimplementasikan `perbarui()`

```java
public class LayarAntrean implements PengamatPesanan {

    public void tampilkan(Pesanan pesanan) {
        System.out.println("Nomor " + pesanan.getNomor() + " silakan ambil pesanan");
    }
}
```

```text
LayarAntrean.java:1: error: LayarAntrean is not abstract and does not override abstract method perbarui(Pesanan) in PengamatPesanan
public class LayarAntrean implements PengamatPesanan {
       ^
1 error
```

**Artinya:** siapa pun yang meng-*implements* `PengamatPesanan` wajib menyediakan `perbarui(Pesanan)` (Pertemuan 10). `tampilkan()` tidak dihitung, karena `Pesanan` hanya pernah memanggil `perbarui()`. **Perbaikan:** ganti nama method menjadi `perbarui` dan beri `@Override`. Dengan `@Override`, salah ketik nama method pun langsung ketahuan.

### Kesalahan 4: Memanggil method khusus subclass pada hasil factory

```java
        Pembayaran pembayaran = PembayaranFactory.buat("tunai", 100000, "");
        System.out.println(pembayaran.getKembalian());
```

```text
Coba4.java:4: error: cannot find symbol
        System.out.println(pembayaran.getKembalian());
                                     ^
  symbol:   method getKembalian()
  location: variable pembayaran of type Pembayaran
1 error
```

**Artinya:** factory mengembalikan tipe `Pembayaran`. Walaupun objek aslinya `PembayaranTunai`, *compiler* hanya melihat tipe variabelnya, dan `Pembayaran` tidak punya `getKembalian()` (bagian `location` menyebutkannya dengan jelas). **Perbaikan:** jika kamu memang butuh fitur khusus tunai, periksa dan *cast* dulu: `if (pembayaran instanceof PembayaranTunai) { ... ((PembayaranTunai) pembayaran).getKembalian() ... }`. Atau, jika jenisnya sudah pasti tunai, buat langsung dengan `new PembayaranTunai(100000)`. Factory paling berguna ketika pemanggil cukup memakai method milik abstraksi.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK, tetapi kata kuncinya (*has private access*, *non-static method*, *does not override abstract method*, *cannot find symbol*) tetap sama.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Singleton: tempat objek | field `private static` | `private static Konfigurasi instance = null;` |
| Singleton: tutup konstruktor | konstruktor `private` | `private Konfigurasi() { ... }` |
| Singleton: pintu masuk | method `public static` | `Konfigurasi.getInstance()` |
| Singleton eager | `static final` | `private static final PencatatLog INSTANCE = new PencatatLog();` |
| Singleton thread-safe | `synchronized` | `public static synchronized Tema getInstance()` |
| Simple Factory | method `static` + `if` | `KendaraanFactory.buat("motor")` |
| Factory Method | method abstrak pembuat produk | `public abstract Angkutan buatAngkutan();` |
| Strategy: kontrak | `interface` | `interface StrategiOngkir { int hitung(int beratKg); }` |
| Strategy: tukar | simpan di field | `paket.aturStrategi(new OngkirKilat());` |
| Observer: daftar pengamat | `List` bertipe interface | `List<PengamatKanal> daftarPengamat = new ArrayList<>();` |
| Observer: beri kabar | *for-each* memanggil method | `for (PengamatPesanan p : daftarPengamat) { p.perbarui(this); }` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
