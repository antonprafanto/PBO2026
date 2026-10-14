# ☕ Praktik Java — Pertemuan 15: Proyek Terintegrasi

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 15](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Menulis dan Membaca File Teks](#1-menulis-dan-membaca-file-teks)
2. [File CSV dengan `split` dan `String.join`](#2-file-csv-dengan-split-dan-stringjoin)
3. [Try-with-resources: Menutup dengan Aman](#3-try-with-resources-menutup-dengan-aman)
4. [Package: Mengelompokkan Kelas](#4-package-mengelompokkan-kelas)
5. [Unit Test: Runner Mini dan JUnit](#5-unit-test-runner-mini-dan-junit)
6. [Validasi Input dan Akhir Input](#6-validasi-input-dan-akhir-input)
7. [Studi Kasus KedaiKita](#7-studi-kasus-kedaikita)
8. [Kesalahan Umum dan Cara Membaca Pesan Error](#8-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/                       <- 6 contoh kecil (masing-masing satu file)
├── studi-kasus/                  <- aplikasi kasir KedaiKita
│   ├── src/kedaikita/*.java      <- package kedaikita (39 file)
│   ├── data/menu_awal.csv        <- data menu awal
│   ├── jalankan.bat, jalankan.sh <- skrip kompilasi + menjalankan aplikasi
│   └── uji.bat, uji.sh           <- skrip kompilasi + menjalankan unit test
└── solusi/                       <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file:

```bash
cd Pertemuan-15-Proyek-Terintegrasi/java/contoh
java Contoh01BacaTulisTeks.java
```

Studi kasus dijalankan lewat skrip dari folder `studi-kasus`:

| Tujuan | Windows (Command Prompt) | Windows (PowerShell) | macOS / Linux |
|---|---|---|---|
| Mode demo | `jalankan.bat --demo` | `.\jalankan.bat --demo` | `bash jalankan.sh --demo` |
| Mode interaktif | `jalankan.bat` | `.\jalankan.bat` | `bash jalankan.sh` |
| Menjalankan unit test | `uji.bat` | `.\uji.bat` | `bash uji.sh` |

> [!TIP]
> Buka folder `java/` **milik pertemuan ini** di VS Code (File → Open Folder), bukan seluruh repositori. Semua nama kelas di folder ini sudah dibuat unik, termasuk kelas solusi latihan, agar VS Code tidak protes "The type ... is already defined". Folder `out/` dan file data hasil aplikasi diabaikan oleh Git.

## 1. Menulis dan Membaca File Teks

File: [`contoh/Contoh01BacaTulisTeks.java`](contoh/Contoh01BacaTulisTeks.java)

Kelas `Files` (paket `java.nio.file`) menyediakan method siap pakai untuk membaca dan menulis file. Alamat file diwakili objek `Path`.

```java
    public static void main(String[] args) throws IOException { // [1]
        Path folder = Files.createTempDirectory("contoh01"); // [2] folder sementara
        Path path = folder.resolve("jadwal-piket.txt"); // [3] folder + nama file
        try {
            System.out.println("=== 1. MENULIS FILE BARU ===");
            Files.writeString(path, "Senin: Ayu\nSelasa: Bima\n", StandardCharsets.UTF_8); // [4]
            System.out.println("File " + path.getFileName() + " sudah ada? "
                    + (Files.exists(path) ? "ya" : "tidak"));

            System.out.println();
            System.out.println("=== 2. MENAMBAH DI AKHIR FILE ===");
            Files.writeString(path, "Rabu: Citra\n", StandardCharsets.UTF_8,
                    StandardOpenOption.APPEND); // [5]
            System.out.println("Satu baris ditambahkan di akhir file");

            System.out.println();
            System.out.println("=== 3. MEMBACA SELURUH ISI ===");
            String isi = Files.readString(path, StandardCharsets.UTF_8); // [6]
            System.out.print(isi); // isi sudah diakhiri "\n", jadi pakai print

            System.out.println();
            System.out.println("=== 4. MEMBACA BARIS DEMI BARIS ===");
            List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8); // [7]
            for (int i = 0; i < semuaBaris.size(); i++) {
                String[] bagian = semuaBaris.get(i).split(": "); // "\n" sudah dibuang
                System.out.println((i + 1) + ". " + bagian[1] + " piket hari " + bagian[0]);
            }
```

Langkah 5 menimpa isi file dengan `Files.writeString()` tanpa opsi tambahan. Langkah 6 membaca file yang tidak ada di dalam `try ... catch (NoSuchFileException e)` **[8]**, dan blok `finally { Files.deleteIfExists(path); Files.deleteIfExists(folder); }` **[9]** membersihkan folder sementara (lihat file lengkapnya).

**Output:**

```text
=== 1. MENULIS FILE BARU ===
File jadwal-piket.txt sudah ada? ya

=== 2. MENAMBAH DI AKHIR FILE ===
Satu baris ditambahkan di akhir file

=== 3. MEMBACA SELURUH ISI ===
Senin: Ayu
Selasa: Bima
Rabu: Citra

=== 4. MEMBACA BARIS DEMI BARIS ===
1. Ayu piket hari Senin
2. Bima piket hari Selasa
3. Citra piket hari Rabu

=== 5. MENIMPA ISI FILE ===
Kamis: Dimas

=== 6. MEMBACA FILE YANG TIDAK ADA ===
File jadwal-lama.txt tidak ditemukan, lanjut dengan data kosong

Folder sementara sudah dihapus? ya
```

Penjelasan:

- **[1]** Hampir semua method `Files` bisa melempar `IOException`, sebuah *checked exception* (Pertemuan 11). Di contoh ini `main` cukup meneruskannya dengan `throws IOException`.
- **[2]** `Files.createTempDirectory()` membuat folder sementara dengan nama acak di folder sementara sistem operasi.
- **[3]** `resolve()` menyambung folder dengan nama file. Pemisah `\` atau `/` diurus otomatis sesuai sistem operasi.
- **[4]** `Files.writeString()` membuat file baru atau **menimpa** isi lama, lalu langsung menutupnya.
- **[5]** Opsi `StandardOpenOption.APPEND` menambahkan teks di akhir file.
- **[6]** `Files.readString()` mengembalikan seluruh isi file sebagai satu `String`.
- **[7]** `Files.readAllLines()` mengembalikan `List<String>`, satu elemen per baris, **tanpa** karakter ganti baris.
- **[8]** Membaca file yang tidak ada melempar `NoSuchFileException`, turunan `IOException`. Tangkap jika memang bisa ditangani.
- **[9]** Blok `finally` menghapus file dan folder sementara apa pun yang terjadi, sehingga tidak ada sisa file.

| Tujuan | Method |
|---|---|
| Menulis (menimpa) | `Files.writeString(path, teks, StandardCharsets.UTF_8)` |
| Menambah di akhir | `Files.writeString(path, teks, StandardCharsets.UTF_8, StandardOpenOption.APPEND)` |
| Membaca seluruh isi | `Files.readString(path, StandardCharsets.UTF_8)` |
| Membaca per baris | `Files.readAllLines(path, StandardCharsets.UTF_8)` |
| Memeriksa keberadaan | `Files.exists(path)` |

> [!NOTE]
> Method `Files` di atas memakai UTF-8 jika *charset* tidak disebut. Namun kelas lama seperti `FileReader` dan `FileWriter` memakai *charset* bawaan sistem operasi (sebelum Java 18), yang di Windows sering bukan UTF-8. Kebiasaan aman: **selalu** tulis `StandardCharsets.UTF_8` secara eksplisit.

## 2. File CSV dengan `split` dan `String.join`

File: [`contoh/Contoh02Csv.java`](contoh/Contoh02Csv.java)

Java tidak punya modul CSV bawaan. Untuk CSV sederhana, cukup dua alat: `String.join()` untuk menulis dan `split()` untuk membaca. Contoh ini menyimpan tiga objek `Mahasiswa` (field `nim`, `nama`, `asal`, `sks`, `catatan`), lalu memuatnya kembali. Kolom `asal` sengaja berisi koma, dan catatan Bima sengaja kosong.

```java
    static void simpan(Path path, List<Mahasiswa> daftar) throws IOException {
        List<String> semuaBaris = new ArrayList<>();
        semuaBaris.add(String.join(PEMISAH, JUDUL_KOLOM)); // baris pertama: judul kolom
        for (Mahasiswa mhs : daftar) {
            semuaBaris.add(String.join(PEMISAH, mhs.keKolom())); // [1]
        }
        // [2] Setiap baris diakhiri "\n" agar isi file sama di Windows, macOS, dan Linux.
        Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8);
    }

    static List<Mahasiswa> muat(Path path) throws IOException {
        List<Mahasiswa> hasil = new ArrayList<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        for (int i = 1; i < semuaBaris.size(); i++) { // [3] mulai dari 1: lewati judul kolom
            int nomorBaris = i + 1;
            String[] kolom = semuaBaris.get(i).split(PEMISAH, -1); // [4]
            try {
                hasil.add(Mahasiswa.dariKolom(kolom));
            } catch (IllegalArgumentException e) { // [5] termasuk NumberFormatException
                System.out.println("  Baris " + nomorBaris + " dilewati: data tidak valid");
            }
        }
        return hasil;
    }
```

Method `Mahasiswa.dariKolom(kolom)` memeriksa bahwa ada tepat 5 kolom (jika tidak, melempar `IllegalArgumentException`), lalu membuat objek dengan `Integer.parseInt(kolom[3])` untuk `sks`.

**Output:**

```text
=== 1. MENYIMPAN 3 OBJEK KE CSV ===
Tersimpan di mahasiswa.csv

=== 2. ISI FILE APA ADANYA ===
nim;nama;asal;sks;catatan
2409106001;Ayu Lestari;Samarinda, Kaltim;20;ketua kelas
2409106002;Bima Saputra;Balikpapan, Kaltim;18;
2409106003;Citra Dewi;Tenggarong, Kukar;22;asisten lab

=== 3. MEMUAT KEMBALI MENJADI OBJEK ===
Ayu Lestari   Samarinda, Kaltim    20 sks  (ketua kelas)
Bima Saputra  Balikpapan, Kaltim   18 sks  (-)
Citra Dewi    Tenggarong, Kukar    22 sks  (asisten lab)
Total 3 mahasiswa, 60 sks

=== 4. FILE DENGAN BARIS RUSAK ===
  Baris 5 dilewati: data tidak valid
  Baris 6 dilewati: data tidak valid
Berhasil dimuat: 3 mahasiswa
```

Penjelasan:

- **[1]** `keKolom()` mengembalikan `List<String>` berisi isi setiap kolom, lalu `String.join(";", ...)` merangkainya menjadi satu baris.
- **[2]** Baris-baris digabung dengan `"\n"` secara eksplisit, **bukan** `System.lineSeparator()` (yang di Windows bernilai `"\r\n"`). Hasilnya, file yang sama persis di semua sistem operasi.
- **[3]** Indeks 0 adalah baris judul, jadi perulangan mulai dari 1. Nomor baris di file (`i + 1`) dipakai untuk pesan error.
- **[4]** `split(";", -1)`: angka **-1** menjaga kolom kosong di akhir baris. Tanpa -1, baris Bima (`...;18;`) hanya menghasilkan 4 kolom (lihat Kesalahan 4 di bagian 8).
- **[5]** `Integer.parseInt("dua puluh")` melempar `NumberFormatException`, yang ternyata **turunan** `IllegalArgumentException`. Satu `catch` menangkap keduanya: kolom kurang dan angka tidak valid.

> [!NOTE]
> Versi sederhana ini tidak mengenal tanda kutip ala CSV. Jika isi kolom mengandung titik koma, barisnya akan terpecah salah. Itulah sebabnya KedaiKita melarang titik koma di dalam nama menu. Untuk CSV yang rumit, programmer Java biasanya memakai pustaka khusus (misalnya OpenCSV atau Apache Commons CSV).

## 3. Try-with-resources: Menutup dengan Aman

File: [`contoh/Contoh03TryWithResources.java`](contoh/Contoh03TryWithResources.java)

Agar kita bisa **melihat** kapan sumber daya dibuka dan ditutup, contoh ini memakai kelas `SambunganPrinter` yang mencetak pesan di setiap langkah:

```java
/** Sumber daya pura-pura: setelah dibuka, wajib ditutup lagi. */
class SambunganPrinter implements AutoCloseable { // [7]
    private String nama;

    SambunganPrinter(String nama) {
        this.nama = nama;
        System.out.println("  [" + nama + "] sambungan dibuka");
    }

    void cetak(String halaman) {
        if (halaman.isEmpty()) {
            throw new IllegalArgumentException("Halaman kosong tidak bisa dicetak");
        }
        System.out.println("  [" + nama + "] mencetak " + halaman);
    }

    @Override
    public void close() { // [8] SELALU dipanggil saat keluar dari blok try
        System.out.println("  [" + nama + "] sambungan ditutup");
    }
}
```

Program utamanya mencoba empat situasi. Situasi 2 dan 4:

```java
        try (SambunganPrinter printer = new SambunganPrinter("Printer Lab")) {
            printer.cetak("Halaman 1");
            printer.cetak(""); // [3] melempar IllegalArgumentException
            printer.cetak("Halaman 3"); // tidak pernah dijalankan
        } catch (IllegalArgumentException e) {
            System.out.println("Error ditangkap: " + e.getMessage()); // [4] sudah ditutup
        }
```

```java
            try (BufferedWriter penulis = Files.newBufferedWriter(path, StandardCharsets.UTF_8)) { // [5]
                for (String nama : List.of("Ayu", "Bima", "Citra")) {
                    penulis.write(nama + "\n");
                }
            }
            try (BufferedReader pembaca = Files.newBufferedReader(path, StandardCharsets.UTF_8)) {
                String baris = pembaca.readLine();
                while (baris != null) { // [6] readLine() mengembalikan null di akhir file
                    System.out.println("Hadir: " + baris);
                    baris = pembaca.readLine();
                }
            }
```

**Output:**

```text
=== 1. BLOK SELESAI TANPA ERROR ===
  [Printer Lab] sambungan dibuka
  [Printer Lab] mencetak Laporan Praktikum
  [Printer Lab] sambungan ditutup
Setelah blok selesai

=== 2. ERROR DI TENGAH BLOK ===
  [Printer Lab] sambungan dibuka
  [Printer Lab] mencetak Halaman 1
  [Printer Lab] sambungan ditutup
Error ditangkap: Halaman kosong tidak bisa dicetak

=== 3. DUA SUMBER DAYA SEKALIGUS ===
  [Printer A] sambungan dibuka
  [Printer B] sambungan dibuka
  [Printer A] mencetak Sampul
  [Printer B] mencetak Isi
  [Printer B] sambungan ditutup
  [Printer A] sambungan ditutup
Ditutup dengan urutan terbalik: yang terakhir dibuka, pertama ditutup

=== 4. MENULIS DAN MEMBACA FILE ===
Hadir: Ayu
Hadir: Bima
Hadir: Citra
```

Penjelasan:

- **[7]** Hanya objek yang mengimplementasikan *interface* `AutoCloseable` (method `close()`) yang boleh ditulis di dalam kurung `try ( ... )`.
- **[8]** `close()` dipanggil **otomatis** saat blok `try` selesai, baik normal maupun karena *exception*.
- **[3]** Setelah `cetak("")` melempar *exception*, sisa blok `try` tidak dijalankan.
- **[4]** Urutan output membuktikan: `close()` dijalankan **lebih dulu**, baru blok `catch`. Di situasi 3, dua sumber daya dipisahkan titik koma di dalam kurung `try` dan ditutup dengan urutan terbalik.
- **[5]** `BufferedWriter` dan `BufferedReader` adalah objek yang kita **pegang sendiri**, jadi wajib ditutup. Try-with-resources melakukannya untuk kita.
- **[6]** `readLine()` mengembalikan satu baris tanpa ganti baris, atau `null` jika file sudah habis.

> [!NOTE]
> Kapan try-with-resources dibutuhkan? Saat kamu memegang objek yang terbuka, seperti `BufferedReader`, `BufferedWriter`, atau `Scanner` untuk file. Method sekali jalan seperti `Files.readAllLines()` dan `Files.writeString()` membuka **dan** menutup file sendiri, sehingga tidak perlu dibungkus. Itulah sebabnya kode file KedaiKita jarang memakainya. Satu-satunya try-with-resources di studi kasus ada di `UjiKedaiKita`, untuk `PrintStream` sementara.

## 4. Package: Mengelompokkan Kelas

File: [`contoh/Contoh04PaketMini.java`](contoh/Contoh04PaketMini.java)

Versi Python contoh ini memecah kelasnya ke dalam *package* `perpustakaan/` berisi beberapa file. Versi Java-nya sengaja tetap **satu file** (kelas `Buku`, `Katalog`, dan tiga *exception* ditulis di bawah kelas utama), karena `java NamaFile.java` hanya bisa menjalankan satu file. Output-nya sama persis dengan versi Python:

**Output:**

```text
=== KATALOG PERPUSTAKAAN MINI ===
[B01] Laskar Pelangi - Andrea Hirata (tersedia)
[B02] Bumi Manusia - Pramoedya Ananta Toer (tersedia)
[B03] Negeri 5 Menara - Ahmad Fuadi (tersedia)

=== MEMINJAM BUKU ===
B02: berhasil dipinjam
B02: gagal, buku 'Bumi Manusia' sedang dipinjam
B09: gagal, buku dengan kode B09 tidak ditemukan

=== KATALOG SETELAH PEMINJAMAN ===
[B01] Laskar Pelangi - Andrea Hirata (tersedia)
[B02] Bumi Manusia - Pramoedya Ananta Toer (dipinjam)
[B03] Negeri 5 Menara - Ahmad Fuadi (tersedia)
```

Kedua *exception* turunan `PerpustakaanException` ditangkap sekaligus dengan `catch (PerpustakaanException e)`, persis seperti `catch (KedaiException e)` di KedaiKita.

### Package sungguhan di KedaiKita

Studi kasus KedaiKita memakai *package* yang sebenarnya. Aturannya:

1. Setiap file diawali baris `package kedaikita;` (sebelum `import`).
2. File berada di folder yang namanya **sama** dengan nama *package*: `src/kedaikita/`.
3. Nama lengkap kelas kini memuat nama *package*: `kedaikita.Main`, `kedaikita.Menu`.
4. Kelas yang dipakai dari **luar** *package* harus `public`. Sesama *package* boleh saling memakai tanpa `import`.

Kompilasi dan menjalankannya dari folder `studi-kasus`:

```bash
javac -d out src/kedaikita/*.java
java -cp out kedaikita.Main --demo
```

| Bagian | Artinya |
|---|---|
| `javac -d out` | simpan hasil kompilasi (`.class`) di folder `out/`, dengan subfolder sesuai nama *package* |
| `src/kedaikita/*.java` | kompilasi **semua** file di *package* sekaligus, karena mereka saling membutuhkan |
| `java -cp out` | *classpath*: cari file `.class` di folder `out/` |
| `kedaikita.Main` | nama **lengkap** kelas yang punya `main` |
| `--demo` | argumen untuk program, diterima `main` sebagai `args` |

Setelah kompilasi, folder `out/kedaikita/` berisi satu file `.class` untuk setiap kelas dan *interface*: `AplikasiKasir.class`, `DapatDicetak.class`, dan seterusnya. Struktur folder `out/` mengikuti nama *package*.

> [!TIP]
> **Coba sendiri:** jadikan contoh 04 *package* sungguhan. Buat folder `perpustakaan/` berisi `Buku.java` yang diawali `package perpustakaan;` dan berisi `public class Buku`. Di folder induknya, buat `AplikasiPerpustakaan.java` dengan `import perpustakaan.Buku;`. Kompilasi dengan `javac -d out perpustakaan/*.java AplikasiPerpustakaan.java`, lalu jalankan `java -cp out AplikasiPerpustakaan`. Di dalam `out/` akan muncul `AplikasiPerpustakaan.class` dan `perpustakaan/Buku.class`, dan `buku.getClass().getName()` mencetak `perpustakaan.Buku`.

## 5. Unit Test: Runner Mini dan JUnit

File: [`contoh/Contoh05UnitTestMini.java`](contoh/Contoh05UnitTestMini.java)

Kelas yang diuji adalah `KeranjangBelanja`: gratis ongkir jika belanja **minimal** Rp100.000, selain itu ongkir Rp10.000. `KeranjangBerbug` adalah turunannya yang sengaja diberi *bug*: method `ongkir()`-nya memakai `subtotal() > BATAS_GRATIS_ONGKIR`, padahal seharusnya `>=`.

Di industri, programmer Java memakai **JUnit** untuk unit test. JUnit tidak ikut di dalam JDK, jadi di sini kita membuat "runner mini" sendiri. Dua di antara lima kasus ujinya:

```java
    static void ujiJumlahNolDitolak() {
        KeranjangBelanja keranjang = pembuatKeranjang.get(); // [3] objek baru setiap uji
        harusMelempar(IllegalArgumentException.class, () -> keranjang.tambah("Buku tulis", 5000, 0));
    }

    static void ujiOngkirDiBawahBatas() {
        KeranjangBelanja keranjang = pembuatKeranjang.get();
        keranjang.tambah("Kaos", 99000, 1);
        samakan(keranjang.ongkir(), 10000); // [4] hasil, harapan
    }
```

Alat bantu ujinya:

```java
    static void uji(String nama, KasusUji kasus) {
        try {
            kasus.jalankan();
            jumlahLulus++;
            System.out.println("[LULUS] " + nama);
        } catch (AssertionError e) { // [5] pemeriksaan tidak terpenuhi
            jumlahGagal++;
            System.out.println("[GAGAL] " + nama);
            System.out.println("        -> " + e.getMessage());
        } catch (RuntimeException e) { // exception yang tidak diduga
            jumlahGagal++;
            System.out.println("[ERROR] " + nama);
            System.out.println("        -> " + e);
        }
    }

    /** Seperti assertEqual: gagal jika hasil tidak sama dengan harapan. */
    static void samakan(int hasil, int harapan) {
        if (hasil != harapan) {
            throw new AssertionError(hasil + " != " + harapan); // [6]
        }
    }
```

Kelima uji dijalankan dua kali: `jalankanSemuaUji(KeranjangBelanja::new)` **[2]**, lalu `jalankanSemuaUji(KeranjangBerbug::new)`.

**Output:**

```text
=== UJI 1: KeranjangBelanja ===
[LULUS] Jumlah barang 0 ditolak
[LULUS] Belanja Rp99.000 kena ongkir Rp10.000
[LULUS] Belanja tepat Rp100.000 gratis ongkir
[LULUS] Subtotal dua barang dijumlahkan
[LULUS] Total = subtotal + ongkir
Hasil: 5 lulus, 0 gagal

=== UJI 2: KeranjangBerbug (sengaja diberi bug) ===
[LULUS] Jumlah barang 0 ditolak
[LULUS] Belanja Rp99.000 kena ongkir Rp10.000
[GAGAL] Belanja tepat Rp100.000 gratis ongkir
        -> 10000 != 0
[LULUS] Subtotal dua barang dijumlahkan
[LULUS] Total = subtotal + ongkir
Hasil: 4 lulus, 1 gagal
```

Penjelasan:

- **[2]** `KeranjangBelanja::new` adalah *method reference* ke konstruktor (Pertemuan 12). Ia disimpan di field `pembuatKeranjang` bertipe `Supplier<KeranjangBelanja>`: sebuah "resep" yang membuat objek baru setiap kali `get()` dipanggil.
- **[3]** Setiap uji meminta keranjang **baru**, sehingga uji tidak saling memengaruhi. Inilah pengganti `setUp()` milik `unittest` Python.
- **[4]** `samakan(hasil, harapan)` meniru `assertEqual`. `harusMelempar(jenis, kode)` meniru `assertRaises`: uji lulus jika *lambda* `kode` melempar *exception* jenis tersebut.
- **[5]** Kegagalan pemeriksaan ditandai dengan `AssertionError`. Runner menangkapnya, mencetak `[GAGAL]`, lalu **melanjutkan** uji berikutnya.
- **[6]** Pesannya `10000 != 0`: ongkirnya 10000, padahal seharusnya 0. Hanya uji **batas** (tepat Rp100.000) yang menangkap *bug* `>` versus `>=`.

> [!WARNING]
> Java punya kata kunci `assert`, tetapi pemeriksaannya **mati secara bawaan** dan baru aktif jika program dijalankan dengan opsi `-ea`. Jangan mengandalkannya untuk pengujian. Lempar `AssertionError` sendiri seperti di atas, atau pakai JUnit.

### Sekilas JUnit 5

Kamu **tidak wajib** memasang JUnit untuk mata kuliah ini. Namun ada baiknya mengenal bentuknya, karena JUnit adalah standar industri. Test yang sama dengan `TestPesanan` versi Python, jika ditulis dengan JUnit 5, kira-kira seperti ini:

```java
package kedaikita;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertThrows;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

class PesananTest {
    private Minuman kopi;
    private Pesanan pesanan;

    @BeforeEach // dijalankan sebelum SETIAP test, seperti setUp()
    void siapkan() throws KedaiException {
        kopi = new Minuman("M01", "Kopi Susu Gula Aren", 18000, 10);
        pesanan = new Pesanan(new Pelanggan("Uji Coba", "080000000000"));
        pesanan.tambahItem(kopi, 2);
    }

    @Test
    void subtotal() {
        assertEquals(36000, pesanan.hitungSubtotal()); // JUnit: (harapan, hasil)
    }

    @Test
    void stokTidakCukupDitolak() {
        assertThrows(StokTidakCukupException.class, () -> kopi.kurangiStok(100));
    }
}
```

- `@Test` menandai method test; JUnit menemukannya sendiri.
- `assertEquals` di JUnit menulis **harapan dulu**, baru hasil. Urutan ini kebalikan dari kebiasaan kita di runner mini, jadi hati-hati saat membaca pesan gagalnya.
- JUnit biasanya dijalankan lewat alat bantu *build* (Maven atau Gradle) atau tombol *Run Test* di editor seperti VS Code dan IntelliJ IDEA.

## 6. Validasi Input dan Akhir Input

File: [`contoh/Contoh06ValidasiInput.java`](contoh/Contoh06ValidasiInput.java)

Program interaktif membaca ketikan dengan `Scanner.nextLine()`. Agar hasilnya selalu sama, contoh ini memakai kelas `MasukanPalsu` yang mengambil jawaban dari daftar yang sudah disiapkan. Method `baca(pertanyaan)`-nya mencetak pertanyaan beserta jawabannya (jawaban kosong ditampilkan sebagai `<Enter>`), dan melempar `NoSuchElementException("No line found")` jika jawabannya sudah habis **[1]**.

Fungsi validasinya bertanya terus sampai jawabannya benar:

```java
    static int tanyaAngka(MasukanPalsu masukan, String pertanyaan, int minimum, int maksimum) {
        while (true) { // [2] ulangi sampai jawabannya valid
            String teks = masukan.baca(pertanyaan).trim();
            if (teks.isEmpty()) {
                System.out.println("  Jawaban tidak boleh kosong.");
                continue;
            }
            int angka;
            try {
                angka = Integer.parseInt(teks); // [3] melempar NumberFormatException
            } catch (NumberFormatException e) {
                System.out.println("  '" + teks + "' bukan angka bulat.");
                continue;
            }
            if (angka < minimum || angka > maksimum) { // [4] periksa batas
                System.out.println("  Harus di antara " + minimum + " dan " + maksimum + ".");
                continue;
            }
            return angka;
        }
    }
```

`tanyaPilihan()` bekerja dengan cara yang sama untuk huruf `U`/`M`, setelah jawaban diubah dengan `toUpperCase(Locale.ROOT)` **[5]**. Skenario kedua dibungkus `try ... catch (NoSuchElementException e)` **[6]**.

**Output:**

```text
=== SKENARIO 1: PENGGUNA SALAH KETIK BEBERAPA KALI ===
Jumlah tiket (1-5): <Enter>
  Jawaban tidak boleh kosong.
Jumlah tiket (1-5): dua
  'dua' bukan angka bulat.
Jumlah tiket (1-5): 9
  Harus di antara 1 dan 5.
Jumlah tiket (1-5): 2
Kategori (U=Umum, M=Mahasiswa): x
  Pilihan tersedia: U, M.
Kategori (U=Umum, M=Mahasiswa): m
Pendaftaran berhasil: 2 tiket Mahasiswa, total Rp50000

=== SKENARIO 2: INPUT BERAKHIR DI TENGAH JALAN ===
Jumlah tiket (1-5): abc
  'abc' bukan angka bulat.
Jumlah tiket (1-5): (input habis)
Input berakhir. Pendaftaran dibatalkan.
```

Penjelasan:

- **[1]** Saat input habis, `Scanner.nextLine()` melempar `NoSuchElementException` dengan pesan `No line found`. `MasukanPalsu` menirunya.
- **[2]** `while (true)` baru berhenti lewat `return` saat jawabannya valid. Jawaban yang salah dibalas pesan yang jelas, lalu pertanyaan diulang.
- **[3]** `Integer.parseInt()` melempar `NumberFormatException` untuk teks seperti `dua`. Perhatikan `trim()` sebelumnya: `parseInt(" 2 ")` akan gagal karena spasi.
- **[4]** Angka yang bentuknya benar tetap diperiksa batasnya.
- **[5]** `Locale.ROOT` membuat perubahan huruf besar tidak bergantung pada pengaturan bahasa komputer.
- **[6]** Akhir input ditangani dengan tertib, bukan dibiarkan menjadi *stack trace*.

Pilihan kategori disimpan di `LinkedHashMap`, bukan `Map.of()`, karena urutannya **dicetak** (`U, M`), sedangkan `Map.of()` tidak menjamin urutan (Pertemuan 12).

> [!NOTE]
> Di program interaktif sungguhan, akhir input terjadi saat pengguna menekan `Ctrl+D` (macOS/Linux) atau `Ctrl+Z` lalu Enter (Windows), atau saat masukan diambil dari file dan isinya sudah habis.

## 7. Studi Kasus KedaiKita

Rancangan dan arsitekturnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini). Sekarang kita bedah kodenya.

### 7.1 Apa yang Berubah dibanding Pertemuan 14

- Semua file pindah ke `src/kedaikita/` dan diawali baris `package kedaikita;`. Isi kelas lama **tidak berubah**, kecuali `Makanan` yang mendapat konstruktor *overload* 4 parameter (tanpa level pedas, dipakai oleh test).
- *Exception* baru: `FormatDataException` (turunan `KedaiException`, jadi *checked*).
- Kelas baru per lapisan: `RepositoriMenuCSV` dan `PencatatTransaksiCSV` (penyimpanan), `LayananKasir` (layanan), `AplikasiKasir` (tampilan). `Main` kini hanya memilih mode.
- Menu dibaca dari `data/menu_awal.csv`. Ada skrip `jalankan`/`uji` dan kelas pengujian `UjiKedaiKita` berisi 16 pemeriksaan.

### 7.2 Skrip `jalankan` dan `uji`

File: [`studi-kasus/jalankan.sh`](studi-kasus/jalankan.sh) dan [`studi-kasus/jalankan.bat`](studi-kasus/jalankan.bat)

```bash
cd "$(dirname "$0")" || exit 1
javac -d out src/kedaikita/*.java || exit 1
java -cp out kedaikita.Main "$@"
```

- Baris pertama pindah ke folder milik skrip itu sendiri, sehingga folder `data/` pasti ditemukan.
- Baris kedua mengompilasi seluruh *package*. Jika gagal, skrip berhenti (`|| exit 1`).
- `"$@"` meneruskan semua argumen, jadi `bash jalankan.sh --demo` menjadi `java -cp out kedaikita.Main --demo`.

Versi Windows (`jalankan.bat`) melakukan hal yang sama dengan `cd /d "%~dp0"` dan `%*`. Skrip `uji.sh`/`uji.bat` identik, hanya kelas yang dijalankan adalah `kedaikita.UjiKedaiKita`.

> [!NOTE]
> Di macOS/Linux, `bash jalankan.sh` selalu berhasil. Bentuk `./jalankan.sh` juga bisa, asalkan file skripnya punya izin eksekusi (`chmod +x jalankan.sh`). Di PowerShell, ketik `.\jalankan.bat`.

### 7.3 `Main`: Pintu Masuk

File: [`studi-kasus/src/kedaikita/Main.java`](studi-kasus/src/kedaikita/Main.java)

```java
public class Main {
    // Folder data dicari relatif terhadap folder kerja (working directory).
    // Skrip jalankan.bat/jalankan.sh selalu pindah dulu ke folder studi-kasus,
    // sehingga folder data/ pasti ditemukan.
    private static final Path FOLDER_DATA = Path.of("data");

    public static void main(String[] args) {
        AplikasiKasir aplikasi = new AplikasiKasir(FOLDER_DATA);
        try {
            if (List.of(args).contains("--demo")) {
                aplikasi.jalankanDemo();
            } else {
                aplikasi.jalankan();
            }
        } catch (KedaiException | IOException | UncheckedIOException e) {
            // Lapisan terluar: error tak terduga ditampilkan dengan sopan.
            // (UncheckedIOException = IOException yang dibungkus oleh
            // PencatatTransaksiCSV, lihat penjelasan di file itu.)
            System.out.println("Terjadi kesalahan: " + e.getMessage());
            System.exit(1);
        }
    }
}
```

- `Path.of("data")` adalah path **relatif**: dihitung dari folder kerja saat `java` dijalankan. Karena itu jalankan dari folder `studi-kasus` (skrip sudah mengurusnya).
- `List.of(args).contains("--demo")` memeriksa apakah argumen `--demo` diberikan.
- *Multi-catch* `KedaiException | IOException | UncheckedIOException` adalah jaring pengaman terakhir. File rusak atau masalah disk ditampilkan dengan sopan, lalu `System.exit(1)` menandakan program gagal.

### 7.4 `RepositoriMenuCSV`: Memuat dan Menyimpan Menu

File: [`studi-kasus/src/kedaikita/RepositoriMenuCSV.java`](studi-kasus/src/kedaikita/RepositoriMenuCSV.java)

```java
    public List<Menu> muat() throws IOException, FormatDataException {
        List<Menu> hasil = new ArrayList<>();
        Set<String> kodeTerpakai = new HashSet<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        if (semuaBaris.isEmpty()) {
            return hasil; // file kosong: belum ada menu
        }
        for (int i = 1; i < semuaBaris.size(); i++) { // mulai dari 1: lewati baris judul kolom
            int nomorBaris = i + 1; // nomor baris di file dihitung mulai dari 1
            String baris = semuaBaris.get(i);
            if (baris.isEmpty()) { // lewati baris kosong
                continue;
            }
            Menu menu = buatMenu(baris.split(PEMISAH, -1), nomorBaris);
            if (kodeTerpakai.contains(menu.getKode())) {
                throw new FormatDataException("Baris " + nomorBaris + ": kode "
                        + menu.getKode() + " sudah dipakai");
            }
            kodeTerpakai.add(menu.getKode());
            hasil.add(menu);
        }
        return hasil;
    }
```

- `throws IOException, FormatDataException` mengumumkan dua *checked exception*: masalah membaca file dan isi file yang rusak.
- `kodeTerpakai` adalah `HashSet` (Pertemuan 12) untuk mendeteksi kode ganda. Urutannya tidak penting, karena set ini tidak pernah dicetak.
- Method `buatMenu()` (lihat file lengkapnya) adalah *factory* kecil: memeriksa jumlah kolom dan jenis, mengubah teks menjadi angka dengan `Integer.parseInt()`, lalu membuat `Makanan` atau `Minuman`. `NumberFormatException` dan `IllegalArgumentException` dari validasi `Menu` diterjemahkan menjadi `FormatDataException` bernomor baris.
- `simpan()` menyusun semua baris, lalu menulisnya sekaligus dengan `Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8)`.

### 7.5 `PencatatTransaksiCSV` dan `UncheckedIOException`

File: [`studi-kasus/src/kedaikita/PencatatTransaksiCSV.java`](studi-kasus/src/kedaikita/PencatatTransaksiCSV.java)

```java
    @Override
    public void perbarui(Pesanan pesanan) {
        if (!pesanan.getStatus().equals("LUNAS")) {
            return;
        }
        int porsi = 0;
        for (ItemPesanan item : pesanan.getDaftarItem()) {
            porsi += item.getJumlah();
        }
        List<String> baris = List.of(pesanan.getNomor(), pesanan.getPelanggan().getNama(),
                pesanan.getPelanggan().getNoHp(), String.valueOf(porsi),
                String.valueOf(pesanan.hitungTotal()));
        try {
            Files.writeString(path, String.join(PEMISAH, baris) + "\n", StandardCharsets.UTF_8,
                    StandardOpenOption.CREATE, StandardOpenOption.APPEND);
        } catch (IOException e) {
            // perbarui() berasal dari interface PengamatPesanan yang tidak punya
            // "throws IOException". Karena itu IOException (checked) dibungkus
            // menjadi UncheckedIOException (unchecked) lalu dilempar lagi.
            throw new UncheckedIOException(e.getMessage(), e);
        }
    }
```

- Kelas ini `implements PengamatPesanan`, *interface* Observer dari Pertemuan 14. `Pesanan` memanggil `perbarui()` setiap kali statusnya berubah; hanya status LUNAS yang dicatat.
- Opsi `CREATE` dan `APPEND`: buat file jika belum ada, lalu tambahkan satu baris di akhir.
- **Mengapa `UncheckedIOException`?** Method yang meng-*override* tidak boleh menambah *checked exception* baru di luar yang dideklarasikan method aslinya. `perbarui()` di *interface* tidak punya `throws IOException`, sehingga `IOException` tidak boleh lolos begitu saja. Solusinya: bungkus menjadi `UncheckedIOException` (turunan `RuntimeException`) dengan *exception* asal sebagai penyebabnya (*exception chaining*, Pertemuan 11). `Main` menangkapnya di lapisan terluar.

### 7.6 `LayananKasir` dan `AplikasiKasir`

`LayananKasir` berisi alur kerja tanpa satu pun `Scanner`: `pelanggan(nama, noHp)`, `buatPesanan(pelanggan)` (sekaligus memasang semua pengamat yang disuntikkan lewat konstruktor), `tambahItem(pesanan, kode, jumlah)`, `bayar(pesanan, jenis, nominal, bank)` yang memakai `PembayaranFactory`, dan `laporan()`. Karena semuanya menerima data yang sudah jadi, kelas ini mudah dipakai tampilan apa pun dan mudah diuji.

`AplikasiKasir` memakai **satu** `Scanner` untuk semua input, dan dua method bantu:

```java
    // nextLine() melempar NoSuchElementException jika input sudah habis;
    // exception itu ditangkap di jalankan().
    private String tanya(String pertanyaan) {
        System.out.print(pertanyaan);
        return masukan.nextLine().trim();
    }

    private int tanyaAngka(String pertanyaan) {
        while (true) {
            String teks = tanya(pertanyaan);
            try {
                return Integer.parseInt(teks);
            } catch (NumberFormatException e) {
                System.out.println("  Harap isi dengan angka bulat, misalnya 2 atau 50000.");
            }
        }
    }
```

Perulangan menu utama di `jalankan()` dibungkus `try ... catch (NoSuchElementException e)`, dan stok **selalu** disimpan setelahnya:

```java
        } catch (NoSuchElementException e) { // input habis (misalnya saat input dari file)
            System.out.println();
            System.out.println("Input berakhir.");
        }
        new RepositoriMenuCSV(fileMenu).simpan(layanan.getKedai().semuaMenu());
```

Pilihan diskon memakai `Map` berisi "resep" pembuat objek:

```java
    private static final Map<String, Supplier<Diskon>> PILIHAN_DISKON = Map.of(
            "1", TanpaDiskon::new,
            "2", DiskonMember::new,
            "3", DiskonHappyHour::new);
```

`PILIHAN_DISKON.get("3").get()` membuat objek `DiskonHappyHour` **baru**. Di sini `Map.of()` aman dipakai karena isinya hanya dicari, tidak pernah dicetak berurutan.

### 7.7 Menjalankan Mode Demo

```bash
bash jalankan.sh --demo        # macOS/Linux; di Windows: jalankan.bat --demo
```

Output diawali `Memuat menu dari data/menu_awal.csv: 6 menu` dan daftar keenam menu, lalu transaksi 1 dan 2 dengan proses pembayaran dan struk lengkap seperti di Pertemuan 14. Berikut cuplikan bagian selanjutnya: input keliru, laporan, dan riwayat yang dibaca dari file.

**Output:**

```text
--- Transaksi 3: input keliru ditangani dengan rapi ---
  [GAGAL] Menu dengan kode M99 tidak ditemukan
  [GAGAL] Stok Mie Goreng Jawa tidak cukup: diminta 100, tersedia 10
  -> 2 x Kopi Tubruk ditambahkan
Pembayaran pesanan P003 (Rina Marlina)
  Metode       : QRIS
  Total bayar  : Rp26.400
  Saldo e-wallet terpotong Rp26.400, sisa Rp73.600
  Status       : LUNAS (+2 poin)

=== LAPORAN SESI INI ===
========================================
LAPORAN PENJUALAN KEDAIKITA
========================================
Pesanan lunas                          3
Total pendapatan               Rp124.080
----------------------------------------
Menu terlaris:
1. Es Teh Manis (2 porsi)
2. Kopi Susu Gula Aren (2 porsi)
3. Kopi Tubruk (2 porsi)
----------------------------------------
Penjualan per kategori (sebelum diskon & pajak):
Makanan                         Rp40.000
Minuman                         Rp76.000
========================================

=== RIWAYAT DARI FILE data/demo-transaksi.csv ===
P001 | Budi Santoso | 081234567890 | 3 | 67100
P002 | Siti Aminah | 082198765432 | 3 | 30580
P003 | Rina Marlina | 085312345678 | 2 | 26400
```

Output versi Java **sama persis** dengan versi Python, baris demi baris. Riwayat itu ditulis oleh `PencatatTransaksiCSV` lalu dibaca kembali dengan `bacaSemua()`. Output diakhiri isi `demo-menu.csv` dengan stok terbaru.

### 7.8 Contoh Sesi Interaktif

Jalankan `bash jalankan.sh` (atau `jalankan.bat`), dan kamu menjadi kasirnya. Berikut **ilustrasi** cuplikan sesi. Teks setelah tanda titik dua pada baris pertanyaan adalah **ketikan kasir**; `<Enter>` berarti kasir langsung menekan Enter.

```text
Pilihan: 2
Nama pelanggan: Dewi Lestari
No. HP: 081255501234
Masukkan kode menu satu per satu (kosongkan untuk selesai).
  Kode menu: m01
  Jumlah: dua
  Harap isi dengan angka bulat, misalnya 2 atau 50000.
  Jumlah: 2
  -> 2 x Kopi Susu Gula Aren ditambahkan
  Kode menu: <Enter>
Diskon: 1. Tanpa diskon  2. Member  3. Happy Hour
Pilihan diskon: 5
Pilihan tidak dikenal, coba lagi.
Pilihan diskon: 1
(struk dicetak: Status BARU)
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 20000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp39.600
[GAGAL] Pembayaran Tunai gagal: uang kurang Rp19.600
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 50000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp39.600
  Uang diterima Rp50.000, kembalian Rp10.400
  Status       : LUNAS (+3 poin)
(struk dicetak lagi: Status LUNAS)
```

Pilih `0` di menu utama untuk keluar: stok disimpan ke `data/menu.csv` dan pesanan tercatat di `data/transaksi.csv`. Saat aplikasi dibuka lagi, baris pertamanya menjadi `Memuat menu dari data/menu.csv: 6 menu`. Jika input berakhir di tengah sesi (misalnya kamu menekan `Ctrl+D`), aplikasi mencetak `Input berakhir.`, tetap menyimpan stok, lalu pamit.

> [!WARNING]
> Buat pesanan lagi di sesi kedua, lalu lihat riwayatnya (pilihan 4). Nomornya kembali **P001**, karena penghitung nomor pesanan (field `static`) mulai dari nol setiap kali aplikasi dibuka. Memperbaikinya adalah [Latihan 3](../latihan.md).

### 7.9 Saat File Data Rusak

Salin folder `studi-kasus` ke tempat lain, lalu buat `data/menu.csv` berisi baris yang sengaja dirusak (harga Es Teh Manis ditulis `8rb`):

```text
jenis;kode;nama;harga;stok;ekstra
Minuman;M01;Kopi Susu Gula Aren;18000;20;dingin
Minuman;M02;Es Teh Manis;8rb;30;dingin
```

Jalankan mode interaktif. Hasilnya:

```text
Terjadi kesalahan: Baris 3: harga, stok, dan level pedas harus berupa angka
```

Pesannya sama persis dengan versi Python. Pesan untuk kerusakan lain ada di [tabel halaman konsep](../README.md#46-jangan-percaya-isi-file).

### 7.10 Unit Test `UjiKedaiKita`

File: [`studi-kasus/src/kedaikita/UjiKedaiKita.java`](studi-kasus/src/kedaikita/UjiKedaiKita.java)

`UjiKedaiKita` adalah runner mini yang lebih lengkap: setiap uji adalah method yang mengembalikan `true` (lulus) atau `false` (gagal).

```java
    /** Dijalankan ulang sebelum SETIAP uji Pesanan, agar tiap uji mulai dari nol. */
    private static void siapkanPesanan() throws KedaiException {
        kopi = new Minuman("M01", "Kopi Susu Gula Aren", 18000, 10);
        nasi = new Makanan("M03", "Nasi Goreng Kampung", 25000, 10, 2);
        pelanggan = new Pelanggan("Uji Coba", "080000000000");
        pesanan = new Pesanan(pelanggan);
        pesanan.tambahItem(kopi, 2);
        pesanan.tambahItem(nasi, 1);
    }

    private static boolean ujiSubtotal() throws KedaiException {
        siapkanPesanan();
        return pesanan.hitungSubtotal() == 61000;
    }
```

Uji untuk `RepositoriMenuCSV` menulis file ke folder dari `Files.createTempDirectory()` lalu menghapusnya di blok `finally`, sehingga folder `data/` tidak pernah tersentuh. Jalankan dengan `bash uji.sh` atau `uji.bat` (di balik layar: `java -cp out kedaikita.UjiKedaiKita`).

**Output:**

```text
=== UNIT TEST KEDAIKITA ===
[LULUS] Menu: harga harus positif
[LULUS] Menu: level pedas maksimal lima
[LULUS] Menu: stok tidak berubah jika gagal
[LULUS] Pesanan: subtotal
[LULUS] Pesanan: total sudah termasuk pajak 10 persen
[LULUS] Pesanan: stok berkurang setelah dipesan
[LULUS] Pesanan: diskon persen
[LULUS] Pesanan: happy hour hanya untuk minuman
[LULUS] Pesanan: diskon member butuh 10 poin
[LULUS] Pesanan: bayar gagal, status tetap BARU
[LULUS] Pesanan: struk memuat total
[LULUS] PembayaranFactory: jenis tidak dikenal
[LULUS] PembayaranFactory: huruf besar/kecil tidak masalah
[LULUS] RepositoriMenuCSV: simpan lalu muat kembali
[LULUS] RepositoriMenuCSV: file rusak ditolak
[LULUS] RepositoriMenuCSV: kode ganda ditolak

Hasil: 16 lulus, 0 gagal
```

Keenam belas uji ini sama dengan 16 test versi Python. Jika ada yang gagal, program keluar dengan kode 1, sehingga alat otomatis (misalnya layanan CI di GitHub) bisa mendeteksinya.

> [!TIP]
> **Coba sendiri:** di `PengaturanKedai.java`, ubah pajak dari `10` menjadi `11`, lalu jalankan `uji` lagi. Uji mana yang gagal? Jangan lupa kembalikan nilainya.

<details>
<summary>Lihat jawaban</summary>

`Pesanan: total sudah termasuk pajak 10 persen` dan `Pesanan: struk memuat total` menjadi `[GAGAL]` karena totalnya kini Rp67.710, bukan Rp67.100. Uji lain tetap lulus karena tidak bergantung pada pajak.

</details>

## 8. Kesalahan Umum dan Cara Membaca Pesan Error

### Kesalahan 1: Menjalankan kelas tanpa nama package

```bash
java -cp out Main
```

```text
Error: Could not find or load main class Main
Caused by: java.lang.ClassNotFoundException: Main
```

**Artinya:** kelasnya bernama lengkap `kedaikita.Main` dan tersimpan di `out/kedaikita/Main.class`. Tidak ada kelas `Main` tanpa *package*. **Perbaikan:** `java -cp out kedaikita.Main`.

### Kesalahan 2: Hanya mengompilasi satu file

```bash
javac -d out src/kedaikita/Main.java
```

```text
src/kedaikita/Main.java:36: error: cannot find symbol
        AplikasiKasir aplikasi = new AplikasiKasir(FOLDER_DATA);
        ^
  symbol:   class AplikasiKasir
  location: class Main
```

Pesan ini diikuti beberapa error serupa untuk kelas lain.

**Artinya:** `javac` tidak menemukan file kelas-kelas lain yang dipakai `Main`. **Perbaikan:** kompilasi seluruh *package* sekaligus: `javac -d out src/kedaikita/*.java`, atau cukup pakai skrip `jalankan`.

### Kesalahan 3: Menjalankan dari folder yang salah

Dari folder `java/` (satu tingkat di atas `studi-kasus`):

```bash
java -cp studi-kasus/out kedaikita.Main --demo
```

```text
=== MODE DEMO KASIR KEDAIKITA ===
Terjadi kesalahan: data/demo-transaksi.csv
```

**Artinya:** `Path.of("data")` dihitung dari folder kerja, dan folder `java/` tidak punya subfolder `data/`. Pesan `NoSuchFileException` hanya berisi path file yang gagal dibuka. **Perbaikan:** jalankan dari folder `studi-kasus`, atau pakai skrip (skrip selalu pindah ke foldernya sendiri).

### Kesalahan 4: `split` tanpa `-1`

```java
String baris = "Minuman;M07;Air Mineral;5000;10;";
System.out.println(baris.split(";").length);
System.out.println(baris.split(";", -1).length);
```

Hasilnya:

```text
5
6
```

**Artinya:** tanpa `-1`, `split()` membuang string kosong di **akhir** hasilnya. Kolom `ekstra` yang kosong hilang, dan `RepositoriMenuCSV` akan menolak baris itu dengan `Baris 2: harus ada 6 kolom`. **Perbaikan:** selalu tulis `split(PEMISAH, -1)` untuk data CSV. (Di Python, `"a;b;".split(";")` tetap menghasilkan 3 elemen.)

### Kesalahan 5: `Scanner` tanpa penanganan akhir input

```java
Scanner masukan = new Scanner(System.in);
System.out.print("Nama pelanggan: ");
String nama = masukan.nextLine();
```

Jika input habis (pengguna menekan `Ctrl+D`, atau masukan diambil dari file kosong):

```text
Nama pelanggan: Exception in thread "main" java.util.NoSuchElementException: No line found
	at java.base/java.util.Scanner.nextLine(Scanner.java:1660)
	at BacaNama.main(BacaNama.java:7)
```

**Artinya:** `nextLine()` tidak punya lagi yang bisa dibaca. `NoSuchElementException` adalah *unchecked exception*, jadi compiler tidak mengingatkanmu. **Perbaikan:** bungkus perulangan utama dengan `try ... catch (NoSuchElementException e)`, seperti `AplikasiKasir.jalankan()`.

### Kesalahan 6: File CSV tidak tersimpan sebagai UTF-8

File `menu.csv` diedit lalu disimpan Excel dengan pilihan "CSV (Comma delimited)", dan ada huruf `é` pada `Café Latte`. Aplikasi menampilkan:

```text
Terjadi kesalahan: Input length = 1
```

**Artinya:** `Files.readAllLines(..., UTF_8)` menemukan byte yang tidak sah dalam UTF-8 dan melempar `MalformedInputException` (turunan `IOException`), yang pesannya kurang jelas. **Perbaikan:** simpan file sebagai **CSV UTF-8**, atau hindari huruf beraksen. Tantangan: tangkap `MalformedInputException` di `muat()` dan ubah menjadi `FormatDataException` dengan pesan yang ramah.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Java, misalnya nomor baris di dalam `Scanner.java`. Fokuslah pada jenis error-nya (`ClassNotFoundException`, `cannot find symbol`, `NoSuchElementException`) dan kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Path | `Path.of(...)`, `folder.resolve("nama")` | `Path.of("data").resolve("menu.csv")` |
| Menulis / menambah file | `Files.writeString(path, teks, UTF_8[, APPEND])` | `StandardOpenOption.APPEND` |
| Membaca file | `Files.readString(path, UTF_8)`, `Files.readAllLines(path, UTF_8)` | `List<String> semuaBaris = ...` |
| CSV: menulis / membaca | `String.join(";", kolom)` / `baris.split(";", -1)` | `"a;b;".split(";", -1)` → 3 kolom |
| Menutup otomatis | `try (Tipe x = ...) { ... }` | `try (BufferedReader r = Files.newBufferedReader(p, UTF_8))` |
| Sumber daya sendiri | `implements AutoCloseable` + `close()` | `class SambunganPrinter implements AutoCloseable` |
| Folder sementara | `Files.createTempDirectory("awalan")` | hapus di `finally` dengan `Files.deleteIfExists` |
| *Package* | `package nama;` di baris pertama | `package kedaikita;` |
| Kompilasi dan jalankan | `javac -d out ...` lalu `java -cp out paket.Kelas` | `java -cp out kedaikita.Main --demo` |
| Membungkus *checked exception* | `throw new UncheckedIOException(pesan, e);` | di `PencatatTransaksiCSV.perbarui()` |
| Input dan akhir input | `scanner.nextLine()` + `catch (NoSuchElementException e)` | `AplikasiKasir.tanya()` |
| Pemeriksaan uji | `throw new AssertionError(hasil + " != " + harapan);` | runner mini |
| JUnit 5 (wawasan) | `@Test`, `@BeforeEach`, `assertEquals`, `assertThrows` | `assertEquals(36000, pesanan.hitungSubtotal())` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).
- Mulai rencanakan [Proyek Akhir](../proyek-akhir.md)-mu.

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
