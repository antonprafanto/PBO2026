# ☕ Solusi Praktik Java Pertemuan 16: UAS

[⬅️ Pembahasan](../pembahasan.md) · [🐍 Solusi Python](../python/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)

> **Prasyarat:** sudah mencoba sendiri [soal praktik](../latihan-soal.md#bagian-c-soal-praktik) dan membaca [pembahasan desainnya](../pembahasan.md#bagian-c-soal-praktik). Halaman ini membedah kode solusinya bagian demi bagian. Semua kode ada di folder `solusi/` dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Solusi](#cara-menjalankan-solusi)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membandingkan Jawabanmu dengan Solusi](#cara-membandingkan-jawabanmu-dengan-solusi)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Soal C1: Sistem Pemesanan Tiket Bioskop](#1-soal-c1-sistem-pemesanan-tiket-bioskop)
2. [Soal C2: *Refactor* Kasir *Laundry*](#2-soal-c2-refactor-kasir-laundry)
3. [Membuktikan *Output* Tidak Berubah](#3-membuktikan-output-tidak-berubah)
4. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (17, 21, atau 25), VS Code dengan ekstensi **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Java pertemuan ini:

```text
java/
└── solusi/
    ├── SoalC1TiketBioskop.java   <- solusi Soal C1
    ├── SoalC2Sebelum.java        <- Soal C2: kode awal yang berantakan
    └── SoalC2Sesudah.java        <- Soal C2: hasil refactor
```

Setiap solusi adalah **program satu *file***: kelas `public` yang memiliki `main` dan kelas-kelas pembantunya (tanpa `public`) ditulis di dalam satu *file* `.java`. Di proyek sungguhan, setiap kelas sebaiknya punya *file* sendiri. Saat ujian, ikuti aturan pengumpulan dari dosen.

> [!IMPORTANT]
> Di setiap *file*, kelas `public` yang memiliki `main` ditulis **paling atas**, dan kelas pembantunya di bawahnya. Pada Java 11 sampai 21, urutan ini wajib agar perintah `java NamaFile.java` bisa berjalan. Java yang lebih baru sedikit lebih longgar, tetapi biasakan urutan ini agar programmu berjalan di semua versi.

### Cara Menjalankan Solusi

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-16-UAS/java`. Di panel **Explorer**, buka folder `solusi`, lalu klik *file* yang ingin dijalankan (misalnya `SoalC1TiketBioskop.java`). Klik tulisan **Run** yang muncul tepat di atas baris `public static void main` (bagian dari **Run | Debug**), atau tombol ▷ di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Jika tulisan **Run** belum muncul, tunggu beberapa detik sampai ekstensi Java selesai memuat folder itu.

Kenapa harus folder `java` milik pertemuan ini, bukan seluruh folder materi? Ekstensi Java menganggap semua *file* `.java` di dalam folder yang dibuka sebagai **satu proyek**, padahal hampir setiap pertemuan punya kelas bernama sama. Di dalam satu folder `java` pertemuan, setiap nama kelas sudah dibuat unik.

> [!NOTE]
> Keunikan nama itulah alasan kelas format uang di `SoalC2Sesudah.java` bernama `RupiahLaundry`, bukan `Rupiah`: `SoalC1TiketBioskop.java` sudah punya kelas `Rupiah`. Jika ada dua kelas bernama sama, VS Code protes `The type Rupiah is already defined` (lihat [Kesalahan 6](#kesalahan-6-dua-kelas-bernama-sama-dalam-satu-folder)).

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-16-UAS/java/solusi` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd solusi` |

Setelah itu, jalankan *file* yang ingin kamu lihat, satu perintah setiap kali:

```bash
java SoalC1TiketBioskop.java
java SoalC2Sebelum.java
java SoalC2Sesudah.java
```

Perintah ini (Java 11 ke atas) mengompilasi *file* di memori, lalu langsung menjalankannya. Cara klasik dua langkah juga bisa dipakai, misalnya `javac SoalC1TiketBioskop.java` lalu `java SoalC1TiketBioskop`. Baris pertama *output* Soal C1 adalah `=== JADWAL TAYANG BioskopKita ===`. Kedua program Soal C2 diawali garis `====================================` dan *output*-nya sama persis.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `solusi`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Perintah `java` sama di Windows, macOS, dan Linux.

### Tempat Menyimpan Kodemu Sendiri

Jawaban latihan UAS-mu jangan disimpan di folder materi, termasuk di folder `solusi/`. Simpan di folder milikmu sendiri **di luar** folder materi, misalnya `PBO-latihan-saya/uas`, agar pekerjaanmu tidak tertimpa saat materi diperbarui (lihat [aturan emas di Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri)). Untuk Java, pakai **satu subfolder untuk setiap soal**:

```text
Documents/
├── PBO2026/                      <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/             <- milikmu sendiri
    └── uas/
        ├── c1/
        │   └── JawabanC1.java    <- jawabanmu untuk Soal C1
        ├── c2/
        │   └── JawabanC2.java    <- jawabanmu untuk Soal C2
        ├── solusi/               <- salinan file solusi, untuk dibandingkan
        └── coba/                 <- tempat bereksperimen dengan salinan solusi
```

Alasannya sama dengan aturan "satu pertemuan, satu folder": jawaban C1, jawaban C2, dan *file* solusi kemungkinan besar punya kelas bernama sama (misalnya `Tiket` atau `Rupiah`). Saat mengerjakan, buka hanya folder `c1` atau `c2` di VS Code. Ingat juga, nama *file* harus sama dengan nama kelas `public` di dalamnya: `JawabanC1.java` berisi `public class JawabanC1`. Ingin bereksperimen dengan kode solusi, misalnya untuk "Coba sendiri" atau kesalahan di bagian 4? Salin dulu *file* solusinya ke folder `uas/coba`, lalu ubah salinannya.

### Cara Membandingkan Jawabanmu dengan Solusi

Targetnya, *output* programmu **sama persis** dengan *output* solusi. Biarkan komputer yang membandingkan karena mata mudah melewatkan satu spasi.

1. Salin *file* solusi yang ingin dibandingkan, misalnya `SoalC1TiketBioskop.java`, ke folder `PBO-latihan-saya/uas/solusi`.
2. Buka terminal **di folder `uas`** (bukan di `c1`). Caranya: buka folder `uas` di File Explorer, klik kanan area kosong, lalu pilih **Open in Terminal**. Jika terminal VS Code-mu sedang berada di folder `c1`, cukup ketik `cd ..`.
3. Simpan *output* kedua program ke *file* teks. Tanda `>` artinya "jangan tampilkan di layar, simpan ke *file* ini":

   ```bash
   java c1/JawabanC1.java > hasil_saya.txt
   java solusi/SoalC1TiketBioskop.java > hasil_solusi.txt
   ```

4. Bandingkan kedua *file* dengan perintah yang sesuai dengan terminalmu:

   | Terminal | Perintah | Jika kedua *file* sama |
   |---|---|---|
   | Windows: Command Prompt | `fc hasil_saya.txt hasil_solusi.txt` | muncul `FC: no differences encountered` |
   | Windows: PowerShell (terminal bawaan VS Code) | `fc.exe hasil_saya.txt hasil_solusi.txt` | sama seperti di atas |
   | macOS/Linux | `diff hasil_saya.txt hasil_solusi.txt` | tidak mencetak apa pun |

Di PowerShell, `fc` tanpa `.exe` adalah singkatan perintah lain, jadi selalu tulis `fc.exe`. Jika Command Prompt menolak garis miring `/` pada `c1/JawabanC1.java`, tulis `c1\JawabanC1.java`. VS Code juga bisa membandingkan dua *file* tanpa terminal: klik kanan *file* pertama di panel **Explorer**, pilih **Select for Compare**, lalu klik kanan *file* kedua dan pilih **Compare with Selected**. Untuk Soal C2, cara yang sama dipakai untuk membuktikan bahwa *refactor*-mu tidak mengubah perilaku (lihat [bagian 3](#3-membuktikan-output-tidak-berubah)).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal bagian 1 dan 2 menunjuk *file* solusinya. Klik untuk melihat isi lengkapnya.
- Blok kode sesudahnya adalah **potongan** penting dari *file* itu, disalin persis beserta komentarnya. Potongan dari dalam sebuah kelas tampil menjorok 4 spasi, dan potongan dari dalam *method* menjorok 8 spasi. Jangan menjalankan potongannya sendiri. Jalankan *file* lengkapnya dengan cara di atas.
- Tanda `// [1]`, `// [2]`, dan seterusnya di komentar kode dijelaskan di daftar **Penjelasan** di bawah blok kodenya. Nomornya dimulai lagi dari `[1]` untuk setiap *file*.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.

---

## 1. Soal C1: Sistem Pemesanan Tiket Bioskop

*File*: [`solusi/SoalC1TiketBioskop.java`](solusi/SoalC1TiketBioskop.java)

Saran urutan membaca: *exception* → `Tiket` dan kelas anaknya → `Jadwal` → `Bioskop` → `main`. Urutan ini sama dengan urutan saat kamu sebaiknya **menulis** kodenya: dari bagian yang tidak bergantung pada apa pun, menuju bagian yang memakai semuanya.

### 1.1 *Exception* Buatan Sendiri (*Checked*)

```java
/** Induk semua error BioskopKita. CHECKED: wajib ditangkap atau dideklarasikan. */
class BioskopException extends Exception {
    public BioskopException(String pesan) {
        super(pesan);
    }
}
```

```java
/** Dilempar saat kursi sudah dipesan orang lain. */
class KursiSudahTerjualException extends BioskopException {
    private final String kodeKursi;
    private final String judul;
    private final int sisaKursi; // [2] data tambahan untuk penangkap error

    public KursiSudahTerjualException(String kodeKursi, String judul, int sisaKursi) {
        super("Kursi " + kodeKursi + " untuk " + judul + " sudah terjual"); // [1]
        this.kodeKursi = kodeKursi;
        this.judul = judul;
        this.sisaKursi = sisaKursi;
    }

    public String getKodeKursi() {
        return kodeKursi;
    }

    public String getJudul() {
        return judul;
    }

    public int getSisaKursi() {
        return sisaKursi;
    }
}
```

Penjelasan:

- `BioskopException` mewarisi `Exception` (bukan `RuntimeException`) sehingga ia ***checked***. Setiap *method* yang bisa melemparnya harus menulis `throws`, dan setiap pemanggilnya harus menangkap atau ikut mendeklarasikannya. *Compiler* yang menjaga agar tidak ada yang lupa.
- **[1]** Pesan dikirim ke konstruktor induk lewat `super(...)`. Pesan inilah yang dikembalikan `e.getMessage()`.
- **[2]** *Exception* adalah objek biasa: *field*-nya `private final` dan dibaca lewat *getter*. Penangkap *error* memakai `e.getSisaKursi()` untuk memberi saran.

### 1.2 Kelas Abstrak Tiket dan Tiga Kelas Anaknya

```java
/** Kelas abstrak: kerangka untuk semua jenis tiket. */
abstract class Tiket {
    private final String kodeKursi;
    private final String pemesan;
    private final int hargaDasar;

    public Tiket(String kodeKursi, String pemesan, int hargaDasar) {
        this.kodeKursi = kodeKursi;
        this.pemesan = pemesan;
        this.hargaDasar = hargaDasar;
    }
```

```java
    /** Nama jenis tiket, misalnya "Reguler". */
    public abstract String jenis(); // [3] method abstrak: WAJIB diisi kelas anak

    /** Harga akhir tiket dalam rupiah (bilangan bulat). */
    public abstract int hitungHarga();

    @Override
    public String toString() { // [4] method konkret yang memanggil method abstrak
        String harga = Rupiah.format(hitungHarga());
        return String.format("%-4s%-9s%-16s%10s", kodeKursi, jenis(), pemesan, harga);
    }
}
```

Salah satu kelas anaknya:

```java
/** Kursi sofa + popcorn: harga dasar ditambah biaya tetap. */
class TiketVIP extends Tiket {
    static final int TAMBAHAN = 25000;

    public TiketVIP(String kodeKursi, String pemesan, int hargaDasar) {
        super(kodeKursi, pemesan, hargaDasar);
    }

    @Override
    public String jenis() {
        return "VIP";
    }

    @Override
    public int hitungHarga() {
        return getHargaDasar() + TAMBAHAN;
    }
}
```

Penjelasan:

- Kelas abstrak boleh punya *field* dan **konstruktor**. Konstruktor itu dipanggil kelas anak lewat `super(...)` di baris pertama konstruktornya.
- *Field* dibuat `private final`: tiket yang sudah terjual tidak bisa diubah dari luar, dan kelas anak membaca harga dasar lewat `getHargaDasar()`.
- **[3]** *Method* `abstract` tidak punya badan, diakhiri titik koma. Kelas anak yang tidak mengisinya ditolak *compiler*.
- **[4]** `toString()` ditulis sekali di kelas induk, tetapi memanggil `jenis()` dan `hitungHarga()` milik objek sebenarnya (pola *Template Method* sederhana).

Objek tiket dibuat oleh sebuah *Factory* sederhana supaya rantai `if` jenis tiket hanya ada di **satu** tempat:

```java
/** Factory sederhana: membuat objek Tiket dari pilihan berupa teks. */
class TiketFactory {
    static Tiket buat(String jenis, String kodeKursi, String pemesan, int hargaDasar) {
        // "VIP", "vip", dan "Vip" dianggap sama. Locale.ROOT membuat aturan huruf
        // kecilnya sama di semua komputer, apa pun bahasa sistem operasinya.
        String pilihan = jenis.toLowerCase(Locale.ROOT);
        if (pilihan.equals("reguler")) {
            return new TiketReguler(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("vip")) {
            return new TiketVIP(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("pelajar")) {
            return new TiketPelajar(kodeKursi, pemesan, hargaDasar);
        }
        throw new IllegalArgumentException("Jenis tiket '" + jenis + "' tidak dikenal");
    }
}
```

Teks dibandingkan dengan `.equals()`, bukan `==`. `IllegalArgumentException` adalah *unchecked* sehingga *method* `buat` tidak perlu menulis `throws`.

### 1.3 Jadwal: Map Kursi dan Polimorfisme

*Field* koleksi di kelas `Jadwal`:

```java
    private final List<String> semuaKursi = new ArrayList<>(); // A1..A5, B1..B5, C1..C5
    // [5] kode kursi -> Tiket. TreeMap selalu urut berdasarkan kunci (A1, A2, ...)
    private final Map<String, Tiket> terjual = new TreeMap<>();
```

Di konstruktornya, daftar kursi dibuat dengan dua perulangan:

```java
        for (char baris : BARIS.toCharArray()) {
            for (int nomor = 1; nomor <= KURSI_PER_BARIS; nomor++) {
                semuaKursi.add(baris + String.valueOf(nomor));
            }
        }
```

Lalu *method-method* utamanya:

```java
    /** Menyimpan tiket. Melempar exception jika kursi tidak ada/sudah terjual. */
    public void tambahTiket(Tiket tiket) throws KursiTidakAdaException,
            KursiSudahTerjualException {
        String kursi = tiket.getKodeKursi();
        if (!semuaKursi.contains(kursi)) {
            throw new KursiTidakAdaException(kursi, studio);
        }
        if (terjual.containsKey(kursi)) { // [6] cek kunci Map
            throw new KursiSudahTerjualException(kursi, judul, kursiKosong().size());
        }
        terjual.put(kursi, tiket);
    }

    public List<String> kursiKosong() {
        List<String> hasil = new ArrayList<>();
        for (String kursi : semuaKursi) {
            if (!terjual.containsKey(kursi)) {
                hasil.add(kursi);
            }
        }
        return hasil;
    }

    /** Tiket terjual, sudah urut kode kursi karena memakai TreeMap. */
    public List<Tiket> daftarTiket() {
        return new ArrayList<>(terjual.values());
    }

    public int jumlahTerjual() {
        return terjual.size();
    }

    public int pendapatan() {
        int total = 0;
        for (Tiket tiket : terjual.values()) {
            total += tiket.hitungHarga(); // [7] polimorfisme
        }
        return total;
    }
```

Penjelasan:

- Tipe *field* ditulis sebagai *interface* (`List`, `Map`), implementasinya dipilih di sebelah kanan (`ArrayList`, `TreeMap`).
- **[5]** `TreeMap` menyimpan kunci dalam keadaan **terurut**. Akibatnya, `daftarTiket()` cukup menyalin `terjual.values()` dan tiket otomatis urut kode kursi. Versi Python memakai dict biasa lalu `sorted()`.
- `baris + String.valueOf(nomor)` menghasilkan teks `"A1"`. Hati-hati: `baris + nomor` (tanpa `String.valueOf`) adalah penjumlahan **angka** karena `char` diperlakukan sebagai kode karakternya. `'A' + 1` menghasilkan `66`, bukan `"A1"`.
- `tambahTiket` mendeklarasikan **dua** *exception* yang bisa dilemparnya secara tepat sehingga pembaca langsung tahu kegagalan apa saja yang mungkin terjadi.
- **[6]** `containsKey` memeriksa kunci tanpa perulangan. Kunci `Map` selalu unik, jadi satu kursi mustahil tercatat untuk dua tiket.
- **[7]** `pendapatan()` tidak peduli jenis tiket; setiap objek menjawab `hitungHarga()` dengan caranya sendiri.

### 1.4 Bioskop: Pemesanan dan Laporan Terurut

```java
    /** Memesan satu tiket. Urutan pemeriksaan: jadwal, jenis, kursi. */
    public Tiket pesan(String kodeJadwal, String jenis, String kodeKursi, String pemesan)
            throws BioskopException { // mencakup ketiga turunannya
        Jadwal jadwal = cariJadwal(kodeJadwal);
        Tiket tiket = TiketFactory.buat(jenis, kodeKursi, pemesan, jadwal.getHargaDasar());
        jadwal.tambahTiket(tiket);
        return tiket;
    }
```

```java
    /** Pendapatan terbesar dulu; jika sama, judul A-Z. */
    public List<Jadwal> laporanPerFilm() {
        List<Jadwal> hasil = new ArrayList<>(daftarJadwal.values());
        hasil.sort(Comparator.comparing(Jadwal::pendapatan).reversed()
                .thenComparing(Jadwal::getJudul)); // [8]
        return hasil;
    }

    /** Jenis tiket -> banyak tiket terjual. TreeMap: urut nama jenis. */
    public Map<String, Integer> jumlahPerJenis() {
        Map<String, Integer> hasil = new TreeMap<>();
        for (Tiket tiket : semuaTiket()) {
            hasil.put(tiket.jenis(), hasil.getOrDefault(tiket.jenis(), 0) + 1);
        }
        return hasil;
    }
```

Penjelasan:

- `pesan` cukup menulis `throws BioskopException` karena ketiga *exception* bioskop adalah turunannya. *Method* ini tidak menangkap apa pun; kegagalan diteruskan ke `main`, yang lebih tahu cara menampilkannya.
- **[8]** `Comparator.comparing(Jadwal::pendapatan)` mengurutkan berdasarkan pendapatan (naik), `.reversed()` membaliknya (turun), lalu `.thenComparing(Jadwal::getJudul)` dipakai jika pendapatannya sama. Pakailah *method reference* (`Jadwal::pendapatan`) seperti ini; versi *lambda* tanpa tipe bisa membingungkan *compiler* (lihat [Kesalahan 5](#kesalahan-5-lambda-tanpa-tipe-sebelum-reversed)).
- `getOrDefault(kunci, 0) + 1` adalah pola menghitung frekuensi dengan `Map`. Karena `hasil` adalah `TreeMap`, kuncinya urut nama jenis (Pelajar, Reguler, VIP).

### 1.5 Program Utama: Menangkap *Exception* dengan Rapi

```java
    // main boleh melempar BioskopException karena cariJadwal("J02") di bawah
    // dipanggil di luar try (seperti versi Python). J02 pasti ada; jika tidak,
    // program berhenti dan Java menampilkan stack trace.
    public static void main(String[] args) throws BioskopException {
```

```java
        System.out.println("=== PEMESANAN TIKET ===");
        for (String[] permintaan : DAFTAR_PERMINTAAN) {
            String kodeJadwal = permintaan[0];
            try {
                Tiket tiket = bioskop.pesan(kodeJadwal, permintaan[1], permintaan[2],
                        permintaan[3]);
                // Java tidak punya "else" pada try: baris sukses ditulis di dalam try
                String harga = Rupiah.format(tiket.hitungHarga());
                System.out.println("[OK]    " + kodeJadwal + "/" + tiket.getKodeKursi() + " "
                        + tiket.jenis() + " untuk " + tiket.getPemesan() + ": " + harga);
            } catch (KursiSudahTerjualException e) { // [9] yang spesifik ditulis dulu
                System.out.println("[GAGAL] " + e.getMessage());
                System.out.println("        Saran: pilih kursi lain, masih ada "
                        + e.getSisaKursi() + " kursi kosong");
            } catch (BioskopException e) { // [10] semua error bioskop yang lain
                System.out.println("[GAGAL] " + e.getMessage());
            } catch (IllegalArgumentException e) { // jenis tiket tidak dikenal
                System.out.println("[GAGAL] " + e.getMessage());
            }
        }
        System.out.println();
```

Penjelasan:

- `main` menulis `throws BioskopException` karena di bagian laporan ada `bioskop.cariJadwal("J02")` di luar `try`. Tanpa `throws`, *compiler* menolak (lihat [Kesalahan 2](#kesalahan-2-checked-exception-tidak-ditangani)).
- **[9]** Blok `catch` untuk kelas anak **wajib** ditulis sebelum kelas induknya. Jika terbalik, Java menolaknya saat kompilasi.
- **[10]** Dua *exception* bioskop lainnya ditangani sama, cukup dengan satu blok milik induknya.
- `IllegalArgumentException` tidak berkerabat dengan `BioskopException` (yang satu *unchecked*, yang lain *checked*), jadi urutan kedua blok terakhir bebas.
- Data permintaan disimpan sebagai `String[][]` karena keempat isinya sama-sama teks.

Kelas `Rupiah` di *file* ini memformat uang dengan `Locale.US` agar hasilnya sama di semua komputer:

```java
/** Kelas utilitas format uang: 18000 -> "Rp18.000". */
class Rupiah {
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}
```

Cara menjalankan dari folder utama materi (cara lain ada di [Persiapan](#cara-menjalankan-solusi)):

```bash
cd Pertemuan-16-UAS/java/solusi
java SoalC1TiketBioskop.java
```

***Output:***

```text
=== JADWAL TAYANG BioskopKita ===
J01  13:00  Studio 1  Rindu di Tepian     Rp30.000
J02  16:00  Studio 2  Mahakam Biru        Rp40.000
J03  19:00  Studio 1  Detektif Kampus     Rp50.000

=== PEMESANAN TIKET ===
[OK]    J02/A1 Reguler untuk Budi Santoso: Rp40.000
[OK]    J02/A2 VIP untuk Siti Aminah: Rp65.000
[GAGAL] Kursi A1 untuk Mahakam Biru sudah terjual
        Saran: pilih kursi lain, masih ada 13 kursi kosong
[OK]    J02/A3 Pelajar untuk Rina Marlina: Rp32.000
[GAGAL] Kursi D1 tidak ada di Studio 1
[OK]    J03/C5 VIP untuk Andi Wijaya: Rp75.000
[GAGAL] Jadwal J05 tidak ditemukan
[GAGAL] Jenis tiket 'premium' tidak dikenal
[OK]    J01/B2 VIP untuk Dimas Pratama: Rp55.000
[OK]    J01/B3 Reguler untuk Ayu Lestari: Rp30.000
[OK]    J01/B4 Reguler untuk Bima Saputra: Rp30.000
[OK]    J03/C4 Pelajar untuk Citra Dewi: Rp40.000
[OK]    J02/B1 Reguler untuk Eko Prasetyo: Rp40.000

=== TIKET TERJUAL J02: Mahakam Biru ===
A1  Reguler  Budi Santoso      Rp40.000
A2  VIP      Siti Aminah       Rp65.000
A3  Pelajar  Rina Marlina      Rp32.000
B1  Reguler  Eko Prasetyo      Rp40.000
Kursi kosong (11): A4, A5, B2, B3, B4, B5, C1, C2, C3, C4, C5

=== LAPORAN PENDAPATAN PER FILM ===
1. Mahakam Biru       4 tiket   Rp177.000
2. Detektif Kampus    2 tiket   Rp115.000
3. Rindu di Tepian    3 tiket   Rp115.000
Total pendapatan: Rp407.000

=== REKAP PER JENIS TIKET ===
Pelajar   2 tiket    Rp72.000
Reguler   4 tiket   Rp140.000
VIP       3 tiket   Rp195.000
```

*Output* ini **identik** dengan versi Python.

> [!TIP]
> **Coba sendiri:** salin `solusi/SoalC1TiketBioskop.java` ke folder latihanmu (`PBO-latihan-saya/uas/coba`), lalu buka salinannya. Di kelas `Jadwal`, ubah `new TreeMap<>()` pada *field* `terjual` menjadi `new HashMap<>()`, dan tambahkan `import java.util.HashMap;` di bagian atas *file* (tanpa baris ini, Java protes `cannot find symbol`). Simpan, lalu jalankan `java SoalC1TiketBioskop.java` dari folder itu. Apakah daftar tiket J02 masih **pasti** urut A1, A2, A3, B1? Mengapa?

<details>
<summary>Lihat jawaban</summary>

Di komputer kami, *output*-nya ternyata tetap sama persis. Namun, itu kebetulan, bukan jaminan. `HashMap` tidak menjaga urutan apa pun; urutan yang terlihat bergantung pada nilai *hash* kuncinya. Bisa saja kebetulan terlihat urut pada data sekecil ini, dan justru itulah jebakannya. Jika tetap memakai `HashMap`, `daftarTiket()` harus mengurutkan sendiri, misalnya dengan `hasil.sort(Comparator.comparing(Tiket::getKodeKursi))`.

</details>

---

## 2. Soal C2: *Refactor* Kasir *Laundry*

*File*: [`solusi/SoalC2Sebelum.java`](solusi/SoalC2Sebelum.java) (kode awal) dan [`solusi/SoalC2Sesudah.java`](solusi/SoalC2Sesudah.java) (hasil *refactor*)

### 2.1 Membaca Kode Sebelum *Refactor*

Potongan inti *method* `terimaCucian()` di kode awal:

```java
        // hitung promo
        int potongan = 0;
        String namaPromo = "";
        if (promo.equals("member")) {
            potongan = subtotal * 10 / 100;
            namaPromo = "Member 10%";
        } else if (promo.equals("gratis1kg")) {
            if (berat >= 5) {
                potongan = tarif;
                namaPromo = "Gratis 1 kg";
            }
        }
        int total = subtotal - potongan;
```

```java
        // kirim WhatsApp
        System.out.println("[WA ke " + noHp + "] Halo " + nama + ", cucian " + kode
                + " sudah kami terima. Total " + teksTotal + ".");

        // simpan riwayat
        riwayat.add(new String[] {kode, nama, String.valueOf(berat), String.valueOf(total)});
```

Perhatikan komentar-komentar seperti `// hitung promo` dan `// kirim WhatsApp`. Setiap komentar yang menandai "babak" di dalam satu *method* adalah petunjuk bahwa *method* itu mengerjakan terlalu banyak hal. Perhatikan juga riwayat yang disimpan sebagai *array* `String`: berat dan total diubah menjadi teks, lalu di `cetakLaporan()` di-*parse* lagi dengan `Integer.parseInt`. Daftar lengkap masalahnya ada di [pembahasan](../pembahasan.md#soal-c2-refactor-kasir-laundry-yang-berantakan).

### 2.2 Katalog Layanan dan *Exception*

```java
/** Daftar layanan. Layanan baru cukup DIDAFTARKAN, tanpa mengubah kode (OCP). */
class KatalogLayanan {
    // [1] nama layanan -> Layanan. HashMap cukup karena katalog hanya dipakai
    //     untuk MENCARI, tidak pernah dicetak berurutan.
    private final Map<String, Layanan> daftar = new HashMap<>();

    public void tambah(Layanan layanan) {
        daftar.put(layanan.getNama(), layanan);
    }

    public Layanan cari(String nama) throws LayananTidakTersediaException {
        if (!daftar.containsKey(nama)) {
            throw new LayananTidakTersediaException(nama); // [2] bukan lagi print + return
        }
        return daftar.get(nama);
    }
}
```

Penjelasan:

- **[1]** Rantai `if (layanan.equals("cuci kering")) ...` berubah menjadi **data** di dalam `Map`. Di sini `HashMap` sudah cukup karena isinya tidak pernah dicetak berurutan. Seandainya kelak perlu menampilkan daftar layanan, gantilah dengan `LinkedHashMap`.
- **[2]** Kode awal mencetak `[DITOLAK] ...` lalu `return` sehingga pemanggil tidak tahu ada kegagalan. Kini katalog melempar `LayananTidakTersediaException` (*checked*), dan *compiler* memastikan pemanggilnya menangani kemungkinan itu.

### 2.3 *Strategy* untuk Promo

```java
/** Strategi promo. Promo baru = kelas baru; kelas lain tidak diubah (OCP). */
interface Promo {
    /** Besar potongan dalam rupiah. Tidak pernah negatif (LSP). */
    int hitungPotongan(PesananLaundry pesanan); // [3]

    /** Nama promo untuk dicetak di nota. */
    String keterangan();
}
```

```java
/** Cucian minimal 5 kg: gratis 1 kg (potongan = tarif 1 kg). */
class PromoGratisSatuKg implements Promo {
    static final int MINIMAL_BERAT = 5;

    @Override
    public int hitungPotongan(PesananLaundry pesanan) {
        if (pesanan.getBerat() < MINIMAL_BERAT) {
            return 0;
        }
        return pesanan.getLayanan().getTarifPerKg();
    }

    @Override
    public String keterangan() {
        return "Gratis 1 kg";
    }
}
```

Di kelas `PesananLaundry`:

```java
    public int subtotal() {
        return layanan.getTarifPerKg() * berat;
    }

    public int potongan() {
        return promo.hitungPotongan(this); // [4] diserahkan ke strategi
    }

    public int total() {
        return subtotal() - potongan();
    }
```

Penjelasan:

- **[3]** *Method* di dalam `interface` otomatis `public` dan abstrak, jadi tidak perlu menulis kedua kata itu. Kelas yang mengimplementasikannya wajib menulis `public` saat meng-*override*.
- Setiap promo menjadi satu kelas kecil. Rantai `if (promo.equals(...))` hilang, dan salah ketik nama promo kini ditolak *compiler* (`cannot find symbol`), bukan promo yang diam-diam tidak berlaku.
- **[4]** `PesananLaundry` tidak tahu promo apa yang dipakainya. Ia cukup **meminta** strategi menghitung potongan, sambil memberikan dirinya sendiri (`this`) sebagai data.

### 2.4 Kasir yang Bergantung pada Abstraksi

```java
/** Kontrak kecil: cukup satu method untuk mengirim pesan (ISP). */
interface Pengirim {
    void kirim(String noHp, String pesan);
}

/** Simulasi WhatsApp: pesan dicetak ke layar. */
class PengirimWhatsApp implements Pengirim {
    @Override
    public void kirim(String noHp, String pesan) {
        System.out.println("[WA ke " + noHp + "] " + pesan);
    }
}
```

```java
/** Mengatur alur kerja kasir dengan memakai kelas-kelas di atas. */
class KasirLaundry {
    private final KatalogLayanan katalog;
    private final Pengirim pengirim; // bergantung pada ABSTRAKSI (DIP)
    private final List<PesananLaundry> riwayat = new ArrayList<>();
    private int nomorTerakhir = 0;

    public KasirLaundry(KatalogLayanan katalog, Pengirim pengirim) { // [5]
        this.katalog = katalog;
        this.pengirim = pengirim;
    }

    /** Melempar LayananTidakTersediaException jika layanan tidak dikenal. */
    public PesananLaundry terimaCucian(Pelanggan pelanggan, String namaLayanan, int berat,
            Promo promo) throws LayananTidakTersediaException {
        Layanan layanan = katalog.cari(namaLayanan); // dicek SEBELUM nomor dibuat
        nomorTerakhir++;
        String kode = String.format("L%03d", nomorTerakhir);
        PesananLaundry pesanan = new PesananLaundry(kode, pelanggan, layanan, berat, promo);
        System.out.println(new NotaLaundry(pesanan).buatTeks());
        pengirim.kirim(pelanggan.getNoHp(), "Halo " + pelanggan.getNama() + ", cucian " + kode
                + " sudah kami terima. Total " + RupiahLaundry.format(pesanan.total()) + ".");
        riwayat.add(pesanan);
        return pesanan;
    }
```

Lapisan tampilan kecil dan program utamanya:

```java
    /** Lapisan tampilan: memanggil kasir dan menampilkan pesan bila ditolak. */
    static void terima(KasirLaundry kasir, Pelanggan pelanggan, String namaLayanan,
            int berat, Promo promo) {
        try {
            kasir.terimaCucian(pelanggan, namaLayanan, berat, promo);
        } catch (LayananTidakTersediaException e) {
            System.out.println("[DITOLAK] " + e.getMessage());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        KasirLaundry kasir = new KasirLaundry(siapkanKatalog(), new PengirimWhatsApp()); // [6]
        terima(kasir, new Pelanggan("Budi Santoso", "081234567890"), "cuci setrika", 4,
                new PromoMember());
```

Penjelasan:

- **[5]** `KasirLaundry` menerima katalog dan pengirim **dari luar** lewat konstruktor (*dependency injection*). Tipe *field*-nya `Pengirim` (*interface*), bukan `PengirimWhatsApp`.
- **[6]** Keputusan "pesan dikirim lewat WhatsApp" hanya ada di satu baris ini. Mengganti ke SMS cukup membuat `PengirimSMS implements Pengirim` dan mengubah baris ini; `KasirLaundry` tidak disentuh.
- Komentar `dicek SEBELUM nomor dibuat` menjaga detail perilaku kode awal: nomor order hanya bertambah jika layanannya valid. *Refactor* tidak boleh mengubah perilaku sekecil apa pun.
- `main` tidak perlu `throws` karena satu-satunya *checked exception* (`LayananTidakTersediaException`) sudah ditangkap di `terima()`.
- `riwayat()` mengembalikan **salinan** *list* (`new ArrayList<>(riwayat)`) sehingga isi riwayat tidak bisa dirusak dari luar.

Cara menjalankan dari folder utama materi (baris ketiga dan keempat dijalankan satu per satu):

```bash
cd Pertemuan-16-UAS/java/solusi
java SoalC2Sebelum.java
java SoalC2Sesudah.java
```

Kedua program menghasilkan *output* yang sama persis, dan sama pula dengan versi Python.

***Output:***

```text
====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L001
Pelanggan : Budi Santoso
Layanan   : cuci setrika
Berat     : 4 kg x Rp8.000
------------------------------------
Subtotal                    Rp32.000
Promo Member 10%            -Rp3.200
TOTAL                       Rp28.800
====================================
[WA ke 081234567890] Halo Budi Santoso, cucian L001 sudah kami terima. Total Rp28.800.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L002
Pelanggan : Siti Aminah
Layanan   : cuci kering
Berat     : 6 kg x Rp6.000
------------------------------------
Subtotal                    Rp36.000
Promo Gratis 1 kg           -Rp6.000
TOTAL                       Rp30.000
====================================
[WA ke 082198765432] Halo Siti Aminah, cucian L002 sudah kami terima. Total Rp30.000.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L003
Pelanggan : Rina Marlina
Layanan   : setrika saja
Berat     : 3 kg x Rp5.000
------------------------------------
Subtotal                    Rp15.000
TOTAL                       Rp15.000
====================================
[WA ke 085312345678] Halo Rina Marlina, cucian L003 sudah kami terima. Total Rp15.000.

[DITOLAK] Layanan 'dry clean' tidak tersedia

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L004
Pelanggan : Dimas Pratama
Layanan   : cuci setrika
Berat     : 5 kg x Rp8.000
------------------------------------
Subtotal                    Rp40.000
TOTAL                       Rp40.000
====================================
[WA ke 081355577799] Halo Dimas Pratama, cucian L004 sudah kami terima. Total Rp40.000.

=== LAPORAN HARIAN ===
L001  Budi Santoso      4 kg    Rp28.800
L002  Siti Aminah       6 kg    Rp30.000
L003  Rina Marlina      3 kg    Rp15.000
L004  Dimas Pratama     5 kg    Rp40.000
Jumlah order : 4
Total berat  : 18 kg
Pendapatan   : Rp113.800
```

---

## 3. Membuktikan *Output* Tidak Berubah

Untuk Soal C2, bandingkan *output* kode awal dengan *output* hasil *refactor*-mu memakai langkah di [Persiapan](#cara-membandingkan-jawabanmu-dengan-solusi). Ketik perintah berikut di terminal yang berada di folder `PBO-latihan-saya/uas` (salinan `SoalC2Sebelum.java` ada di subfolder `solusi`, jawabanmu di subfolder `c2`):

```bash
java solusi/SoalC2Sebelum.java > sebelum.txt
java c2/JawabanC2.java > sesudah.txt
diff sebelum.txt sesudah.txt
```

Baris ketiga untuk macOS/Linux. Di Windows, ganti dengan `fc sebelum.txt sesudah.txt` (Command Prompt) atau `fc.exe sebelum.txt sesudah.txt` (PowerShell). Jika kedua *file* identik, `diff` **tidak mencetak apa pun**, sedangkan `fc` menulis `FC: no differences encountered`. Ingin melihat solusi lulus pemeriksaan yang sama? Salin juga `SoalC2Sesudah.java` ke subfolder `solusi`, lalu ganti `c2/JawabanC2.java` di baris kedua dengan `solusi/SoalC2Sesudah.java`. Contoh membaca hasil `diff` yang **berbeda** ada di [Solusi Python](../python/README.md#3-membuktikan-output-tidak-berubah).

Ada satu detail khusus Java di Windows. `println` mengakhiri setiap baris dengan pemisah baris milik sistem operasi. Di Windows, pemisah itu terdiri atas dua karakter tak kasatmata, CR dan LF, sedangkan `"\n"` hanya LF. Jika jawabanmu menyusun teks nota dengan `String.join("\n", ...)` lalu mencetaknya dengan `println`, *file* hasilnya bercampur antara CR LF dan LF saja, dan alat pembanding bisa melaporkan perbedaan padahal tulisannya tampak sama. Karena itu, `NotaLaundry` dan `LaporanHarian` di `SoalC2Sesudah.java` menyambung baris dengan `System.lineSeparator()`, yaitu pemisah yang sama dengan milik `println`. Di macOS/Linux, keduanya sama-sama LF sehingga hasilnya tidak berubah.

> [!TIP]
> Jalankan `diff` setiap kali selesai memindahkan **satu** tanggung jawab ke kelas baru. Jika muncul perbedaan, kamu langsung tahu langkah mana penyebabnya.

---

## 4. Kesalahan Umum dan Cara Membaca Pesan *Error*

Sebagian besar kesalahan di bawah ini adalah ***error* kompilasi**: Java menolak menjalankan program sama sekali. Pesannya diawali nama *file* dan nomor baris, dan tanda `^` menunjuk posisi masalahnya. Karena program dijalankan dengan `java NamaFile.java`, pesannya diakhiri baris `error: compilation failed`. Jika memakai `javac`, yang muncul hanya pesan *error* dan `1 error`.

Ingin mencoba sendiri? Jangan mengubah *file* di folder materi. Salin dulu `solusi/SoalC1TiketBioskop.java` ke folder `PBO-latihan-saya/uas/coba`, buat kesalahannya di salinan itu, lalu jalankan `java SoalC1TiketBioskop.java` dari folder tersebut.

### Kesalahan 1: Urutan catch terbalik

Jika blok `catch (BioskopException e)` beserta isinya dipindah ke **atas** blok `catch (KursiSudahTerjualException e)`:

```text
SoalC1TiketBioskop.java:78: error: exception KursiSudahTerjualException has already been caught
            } catch (KursiSudahTerjualException e) { // [9] yang spesifik ditulis dulu
              ^
1 error
error: compilation failed
```

**Artinya:** setiap `KursiSudahTerjualException` juga merupakan `BioskopException`, jadi blok di atasnya sudah menangkapnya. Blok di bawah tidak akan pernah tercapai, dan Java menganggap itu kesalahan. (Python diam saja untuk kasus yang sama sehingga *bug*-nya lebih licin.) **Perbaikan:** tulis `catch` yang lebih spesifik lebih dulu.

### Kesalahan 2: *Checked exception* tidak ditangani

Jika `throws BioskopException` dihapus dari `main`:

```text
SoalC1TiketBioskop.java:88: error: unreported exception JadwalTidakDitemukanException; must be caught or declared to be thrown
        Jadwal jadwal = bioskop.cariJadwal("J02");
                                          ^
1 error
error: compilation failed
```

**Artinya:** `cariJadwal` bisa melempar *checked exception*, dan baris ini tidak berada di dalam `try`, sementara `main` juga tidak mendeklarasikannya. **Perbaikan:** bungkus dengan `try-catch`, atau tambahkan `throws` pada *method* yang memanggilnya. Pilih yang paling masuk akal: tangkap di tempat yang bisa **menangani** kegagalan dengan baik.

### Kesalahan 3: Lupa mengisi *method* abstrak

Jika *method* `hitungHarga()` di `TiketVIP` (beserta `@Override` di atasnya) dihapus:

```text
SoalC1TiketBioskop.java:249: error: TiketVIP is not abstract and does not override abstract method hitungHarga() in Tiket
class TiketVIP extends Tiket {
^
1 error
error: compilation failed
```

**Artinya:** kelas konkret wajib mengisi semua *method* abstrak induknya. Berbeda dengan Python yang baru protes saat objek dibuat, Java menolak sejak kompilasi. **Perbaikan:** tambahkan `hitungHarga()` lengkap dengan `@Override`.

### Kesalahan 4: Membuat objek dari kelas abstrak

Misalkan baris berikut ditambahkan sebagai baris pertama di dalam `main` (potongan kode untuk ditempel di salinan *file*, bukan program utuh):

```java
        Tiket coba = new Tiket("A1", "Budi Santoso", 40000);
```

Pesan *error*-nya:

```text
SoalC1TiketBioskop.java:59: error: Tiket is abstract; cannot be instantiated
        Tiket coba = new Tiket("A1", "Budi Santoso", 40000);
                     ^
1 error
error: compilation failed
```

**Artinya:** kelas abstrak hanya kerangka. **Perbaikan:** buat objek dari kelas anaknya, misalnya `Tiket coba = new TiketReguler("A1", "Budi Santoso", 40000);`. Variabelnya boleh tetap bertipe `Tiket` (*upcasting*).

### Kesalahan 5: *Lambda* tanpa tipe sebelum `reversed()`

Jika `Comparator.comparing(Jadwal::pendapatan)` diganti dengan *lambda* `Comparator.comparing(j -> j.pendapatan())`, bagian awal pesan *error*-nya:

```text
SoalC1TiketBioskop.java:458: error: cannot find symbol
        hasil.sort(Comparator.comparing(j -> j.pendapatan()).reversed()
                                              ^
  symbol:   method pendapatan()
  location: variable j of type Object
```

Setelah itu muncul pesan kedua yang panjang tentang `thenComparing`, lalu `2 errors` dan `error: compilation failed`.

**Artinya:** karena ada `.reversed()` yang menempel, *compiler* tidak bisa menebak tipe `j`, lalu menganggapnya `Object`, padahal `Object` tidak punya *method* `pendapatan()`. **Perbaikan:** pakai *method reference* `Jadwal::pendapatan`, atau tulis tipenya secara eksplisit: `(Jadwal j) -> j.pendapatan()`.

### Kesalahan 6: Dua kelas bernama sama dalam satu folder

Jika kelas `RupiahLaundry` di salinan `SoalC2Sesudah.java` dinamai `Rupiah` (termasuk semua pemanggilan `RupiahLaundry.format`), lalu kedua *file* dikompilasi bersama dengan `javac SoalC1TiketBioskop.java SoalC2Sesudah.java` di folder `coba`:

```text
SoalC2Sesudah.java:73: error: duplicate class: Rupiah
class Rupiah {
^
1 error
```

**Artinya:** dalam satu paket (di sini paket bawaan tanpa nama), nama kelas harus unik. VS Code menampilkan masalah yang sama sebagai `The type Rupiah is already defined`. **Perbaikan:** beri nama yang berbeda, atau letakkan kelas di *file*/paket sendiri seperti pada proyek berpaket di Pertemuan 15.

> [!NOTE]
> Pesan di halaman ini berasal dari JDK 21. Bunyinya bisa sedikit berbeda antarversi JDK; fokuslah pada kata kuncinya. Jika kamu mengompilasi dengan `javac -Xlint:all`, javac juga memberi peringatan `[serial] serializable class BioskopException has no definition of serialVersionUID`. Itu hanya **peringatan**, bukan *error*: kelas *exception* bisa diserialisasi, dan Java menyarankan nomor versi. Untuk latihan ini aman diabaikan; jika ingin menghilangkannya, tambahkan `private static final long serialVersionUID = 1L;` di kelas *exception*.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh dari solusi |
|---|---|---|
| Kelas abstrak | `abstract class Nama` + `public abstract Tipe method();` | `abstract class Tiket` |
| *Interface* | `interface Nama { Tipe method(...); }` + `implements` | `interface Promo` |
| *Checked exception* | `class X extends Exception` | `class BioskopException extends Exception` |
| Deklarasi lemparan | `Tipe method(...) throws X` | `Tiket pesan(...) throws BioskopException` |
| Menangkap berurutan | `catch (Anak e)` lalu `catch (Induk e)` | `catch (KursiSudahTerjualException e)` |
| Map terurut kunci | `Map<K, V> m = new TreeMap<>();` | `terjual`, `jumlahPerJenis()` |
| Map urutan masuk | `Map<K, V> m = new LinkedHashMap<>();` | `daftarJadwal` |
| Hitung frekuensi | `m.put(k, m.getOrDefault(k, 0) + 1)` | `jumlahPerJenis()` |
| Urut dua kriteria | `comparing(A::x).reversed().thenComparing(A::y)` | `laporanPerFilm()` |
| Huruf kecil tanpa jebakan *locale* | `teks.toLowerCase(Locale.ROOT)` | `TiketFactory.buat()` |
| *Dependency injection* | objek pendukung lewat konstruktor | `new KasirLaundry(katalog, new PengirimWhatsApp())` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Python: [🐍 Solusi Python](../python/README.md). *Output*-nya identik.
- Siapkan presentasi proyek akhir: [Presentasi Proyek Akhir](../README.md#8-presentasi-proyek-akhir).

---

[⬅️ Pembahasan](../pembahasan.md) · [🐍 Solusi Python](../python/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)
