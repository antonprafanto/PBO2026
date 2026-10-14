# ☕ Praktik Java Pertemuan 15: Proyek Terintegrasi

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 15](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Menulis dan Membaca *File* Teks](#1-menulis-dan-membaca-file-teks)
2. [*File* CSV dengan `split` dan `String.join`](#2-file-csv-dengan-split-dan-stringjoin)
3. [*Try-with-resources*: Menutup dengan Aman](#3-try-with-resources-menutup-dengan-aman)
4. [*Package*: Mengelompokkan Kelas](#4-package-mengelompokkan-kelas)
5. [*Unit Test*: *Runner* Mini dan JUnit](#5-unit-test-runner-mini-dan-junit)
6. [Validasi *Input* dan Akhir *Input*](#6-validasi-input-dan-akhir-input)
7. [Studi Kasus KedaiKita](#7-studi-kasus-kedaikita)
8. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#8-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** JDK 17 atau lebih baru (17, 21, atau 25), VS Code dengan ekstensi **Extension Pack for Java**, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

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

Setiap contoh dan setiap solusi adalah **program satu *file***: kelas yang memiliki `main` dan kelas pembantunya ditulis di dalam satu *file* `.java`.

> [!IMPORTANT]
> Di setiap *file* contoh, kelas yang memiliki *method* `main` ditulis **paling atas**, dan kelas pembantunya di bawahnya. Pada Java 11 sampai 21, urutan ini wajib agar perintah `java NamaFile.java` bisa berjalan.

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol Run di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-15-Proyek-Terintegrasi/java`. Di panel **Explorer**, buka folder `contoh`, lalu klik *file* yang ingin dicoba. Setelah *file* terbuka, klik tulisan **Run** yang muncul tepat di atas baris `public static void main` (bagian dari **Run | Debug**), atau tombol ▷ di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Jika tulisan **Run** belum muncul, tunggu beberapa detik sampai ekstensi Java selesai memuat folder itu.

Kenapa harus folder `java` milik pertemuan ini, bukan seluruh folder materi? Ekstensi Java menganggap semua *file* `.java` di dalam folder yang dibuka sebagai **satu proyek**. Padahal, hampir setiap pertemuan punya kelas bernama sama (misalnya `Menu`), dan VS Code akan protes dengan pesan *The type Menu is already defined*. Di dalam satu folder `java` pertemuan, setiap nama kelas sudah dibuat unik, termasuk kelas solusi latihan.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-15-Proyek-Terintegrasi/java/contoh` |
| folder `java` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
java Contoh01BacaTulisTeks.java
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di bagian 1. *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Perintah `java` sama di Windows, macOS, dan Linux. Semua contoh menulis *file* ke **folder sementara** lalu menghapusnya lagi, jadi tidak ada *file* sampah yang tertinggal.

### Cara Menjalankan Studi Kasus

Studi kasus pertemuan ini adalah **proyek ber-*package***: 39 *file* di folder `src/kedaikita/` yang harus dikompilasi bersama, lalu dijalankan dengan nama kelas lengkap `kedaikita.Main`. Agar kamu cukup mengetik satu perintah, disediakan skrip `jalankan` dan `uji`.

1. **Buka terminal di folder `studi-kasus`.** Cara tercepat: di panel **Explorer** VS Code, klik kanan folder `studi-kasus`, lalu pilih **Open in Integrated Terminal**. Dari folder utama materi, ketik `cd Pertemuan-15-Proyek-Terintegrasi/java/studi-kasus`.
2. **Ketik perintah yang sesuai dengan terminalmu.** Terminal bawaan VS Code di Windows adalah PowerShell.

| Tujuan | Windows (PowerShell) | Windows (Command Prompt) | macOS / Linux |
|---|---|---|---|
| Mode demo | `.\jalankan.bat --demo` | `jalankan.bat --demo` | `bash jalankan.sh --demo` |
| Mode interaktif | `.\jalankan.bat` | `jalankan.bat` | `bash jalankan.sh` |
| Menjalankan *unit test* | `.\uji.bat` | `uji.bat` | `bash uji.sh` |

Bentuk `.\jalankan.bat` juga berjalan di Command Prompt, jadi pengguna Windows cukup mengingat bentuk itu. Setiap kali dijalankan, skrip mengompilasi ulang semua *file* ke folder `out/` sehingga perubahan kodemu selalu ikut terpakai. Mode interaktif dijelaskan langkah demi langkah di bagian 7.8, dan arti hasil *unit test* di bagian 7.10.

**Bagaimana dengan tombol Run di VS Code?** Untuk `Main.java`, jangan pakai tombol itu. VS Code biasanya menjalankan program dari folder yang kamu buka (`java`), bukan dari `studi-kasus`, sehingga folder `data/` tidak ditemukan dan muncul pesan `Terjadi kesalahan: ...transaksi.csv` (lihat Kesalahan 3 di bagian 8). Tombol itu juga tidak bisa menambahkan `--demo`. Pakai skrip di terminal.

**Di mana data disimpan?** Semua *file* data ada di folder `studi-kasus/data/`, dan hasil kompilasi di folder `studi-kasus/out/`:

| *File* atau folder | Dibuat oleh | Keterangan |
|---|---|---|
| `data/menu_awal.csv` | sudah ada sejak awal | data menu awal; **jangan dihapus** |
| `data/menu.csv` | mode interaktif, saat keluar | stok terbaru; dibaca lagi saat aplikasi dibuka |
| `data/transaksi.csv` | mode interaktif, setiap pesanan LUNAS | riwayat transaksi |
| `data/demo-menu.csv`, `data/demo-transaksi.csv` | mode demo | ditulis ulang dari awal setiap kali mode demo dijalankan |
| `out/` | skrip `jalankan` dan `uji` | *file* `.class`; boleh dihapus kapan saja karena dibuat ulang oleh skrip |

**Ingin mulai lagi dari stok awal?** Tutup aplikasinya, lalu hapus `menu.csv` dan `transaksi.csv`, misalnya lewat klik kanan di panel **Explorer** VS Code lalu **Delete**. Lewat terminal di folder `studi-kasus`, ketik `del data\menu.csv` lalu `del data\transaksi.csv` (Windows), atau `rm data/menu.csv data/transaksi.csv` (macOS/Linux). Saat dibuka lagi, aplikasi kembali memuat `menu_awal.csv`. Folder `out/` dan semua *file* hasil aplikasi itu sudah diatur agar diabaikan Git sehingga tidak mengganggu `git pull`.

### Tempat Menyimpan Kodemu Sendiri

Anggap folder materi sebagai buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Simpan kode buatanmu sendiri (hasil mengetik ulang, percobaan "Coba sendiri", dan jawaban latihan) di folder lain **di luar** folder materi, satu folder untuk setiap pertemuan, misalnya:

```text
Documents/
├── PBO2026/                          <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/                 <- milikmu sendiri
    └── pertemuan-15/                 <- kode pertemuan ini
        ├── Contoh02Csv.java          <- salinan contoh yang ingin diubah
        └── studi-kasus/              <- salinan UTUH folder studi-kasus
```

Jika sebuah "Coba sendiri" memintamu mengubah *file* contoh, salin dulu *file* itu ke folder `pertemuan-15` (lewat File Explorer di Windows atau Finder di macOS), lalu ubah salinannya. Jangan ganti nama *file*-nya: nama *file* Java harus sama dengan nama kelas `public` di dalamnya. Untuk studi kasus, salin **seluruh** folder `studi-kasus` (folder `src/`, `data/`, dan keempat skripnya); skrip di salinan itu tetap berjalan karena selalu pindah ke foldernya sendiri. Buka folder `pertemuan-15` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**), atau arahkan terminal ke sana dengan `cd`. Alasannya ada di [Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Kode yang ditampilkan biasanya **potongan** *file* itu. Potongan dari dalam sebuah kelas tampil menjorok 4 spasi, dan potongan dari dalam *method* menjorok 8 spasi, karena begitulah letak aslinya. Untuk mencoba, jalankan *file*-nya, jangan hanya menyalin potongannya.
- Tanda `// [1]`, `// [2]`, dan seterusnya di dalam kode dijelaskan satu per satu di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan. Blok yang diperkenalkan dengan kata lain (misalnya "Hasilnya:") bisa sedikit berbeda di komputermu.

## 1. Menulis dan Membaca *File* Teks

*File*: [`contoh/Contoh01BacaTulisTeks.java`](contoh/Contoh01BacaTulisTeks.java)

Kelas `Files` (paket `java.nio.file`) menyediakan *method* siap pakai untuk membaca dan menulis *file*. Alamat *file* diwakili objek `Path`. Berikut potongan *method* `main` sampai langkah 4:

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

Langkah 5 menimpa isi *file* dengan `Files.writeString()` tanpa opsi tambahan. Langkah 6 membaca *file* yang tidak ada di dalam `try ... catch (NoSuchFileException e)` **[8]**, dan blok `finally { Files.deleteIfExists(path); Files.deleteIfExists(folder); }` **[9]** membersihkan folder sementara (lihat *file* lengkapnya).

***Output:***

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

- **[1]** Hampir semua *method* `Files` bisa melempar `IOException`, sebuah *checked exception* (Pertemuan 11). Di contoh ini `main` cukup meneruskannya dengan `throws IOException`.
- **[2]** `Files.createTempDirectory()` membuat folder sementara dengan nama acak di folder sementara sistem operasi.
- **[3]** `resolve()` menyambung folder dengan nama *file*. Pemisah `\` atau `/` diurus otomatis sesuai sistem operasi.
- **[4]** `Files.writeString()` membuat *file* baru atau **menimpa** isi lama, lalu langsung menutupnya.
- **[5]** Opsi `StandardOpenOption.APPEND` menambahkan teks di akhir *file*.
- **[6]** `Files.readString()` mengembalikan seluruh isi *file* sebagai satu `String`.
- **[7]** `Files.readAllLines()` mengembalikan `List<String>`, satu elemen per baris, **tanpa** karakter ganti baris.
- **[8]** Membaca *file* yang tidak ada melempar `NoSuchFileException`, turunan `IOException`. Tangkap jika memang bisa ditangani.
- **[9]** Blok `finally` menghapus *file* dan folder sementara apa pun yang terjadi sehingga tidak ada sisa *file*.

| Tujuan | *Method* |
|---|---|
| Menulis (menimpa) | `Files.writeString(path, teks, StandardCharsets.UTF_8)` |
| Menambah di akhir | `Files.writeString(path, teks, StandardCharsets.UTF_8, StandardOpenOption.APPEND)` |
| Membaca seluruh isi | `Files.readString(path, StandardCharsets.UTF_8)` |
| Membaca per baris | `Files.readAllLines(path, StandardCharsets.UTF_8)` |
| Memeriksa keberadaan | `Files.exists(path)` |

> [!NOTE]
> *Method* `Files` di atas memakai UTF-8 jika *charset* tidak disebut. Namun, kelas lama seperti `FileReader` dan `FileWriter` memakai *charset* bawaan sistem operasi (sebelum Java 18), yang di Windows sering bukan UTF-8. Kebiasaan aman: **selalu** tulis `StandardCharsets.UTF_8` secara eksplisit.

## 2. *File* CSV dengan `split` dan `String.join`

*File*: [`contoh/Contoh02Csv.java`](contoh/Contoh02Csv.java)

Java tidak punya modul CSV bawaan. Untuk CSV sederhana, cukup dua alat: `String.join()` untuk menulis dan `split()` untuk membaca. Contoh ini menyimpan tiga objek `Mahasiswa` (*field* `nim`, `nama`, `asal`, `sks`, `catatan`), lalu memuatnya kembali. Kolom `asal` sengaja berisi koma, dan catatan Bima sengaja kosong. Berikut potongan *method* `simpan()` dan `muat()`:

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

*Method* `Mahasiswa.dariKolom(kolom)` memeriksa bahwa ada tepat 5 kolom (jika tidak, melempar `IllegalArgumentException`), lalu membuat objek dengan `Integer.parseInt(kolom[3])` untuk `sks`.

***Output:***

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
- **[2]** Baris-baris digabung dengan `"\n"` secara eksplisit, **bukan** `System.lineSeparator()` (yang di Windows bernilai `"\r\n"`). Hasilnya, *file* yang sama persis di semua sistem operasi.
- **[3]** Indeks 0 adalah baris judul, jadi perulangan mulai dari 1. Nomor baris di *file* (`i + 1`) dipakai untuk pesan *error*.
- **[4]** `split(";", -1)`: angka **-1** menjaga kolom kosong di akhir baris. Tanpa -1, baris Bima (`...;18;`) hanya menghasilkan 4 kolom (lihat Kesalahan 4 di bagian 8).
- **[5]** `Integer.parseInt("dua puluh")` melempar `NumberFormatException`, yang ternyata **turunan** `IllegalArgumentException`. Satu `catch` menangkap keduanya: kolom kurang dan angka tidak valid.

> [!NOTE]
> Versi sederhana ini tidak mengenal tanda kutip ala CSV. Jika isi kolom mengandung titik koma, barisnya akan terpecah salah. Itulah sebabnya KedaiKita melarang titik koma di dalam nama menu. Untuk CSV yang rumit, pemrogram Java biasanya memakai pustaka khusus (misalnya OpenCSV atau Apache Commons CSV).

## 3. *Try-with-resources*: Menutup dengan Aman

*File*: [`contoh/Contoh03TryWithResources.java`](contoh/Contoh03TryWithResources.java)

Agar kita bisa **melihat** kapan sumber daya dibuka dan ditutup, contoh ini memakai kelas `SambunganPrinter` yang mencetak pesan di setiap langkah. Kelas ini ditulis di bagian bawah *file* (disalin utuh):

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

Program utamanya mencoba empat situasi. Berikut potongan situasi 2 dan situasi 4 dari *method* `main`:

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

***Output:***

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

- **[7]** Hanya objek yang mengimplementasikan *interface* `AutoCloseable` (*method* `close()`) yang boleh ditulis di dalam kurung `try ( ... )`.
- **[8]** `close()` dipanggil **otomatis** saat blok `try` selesai, baik normal maupun karena *exception*.
- **[3]** Setelah `cetak("")` melempar *exception*, sisa blok `try` tidak dijalankan.
- **[4]** Urutan *output* membuktikan: `close()` dijalankan **lebih dulu**, baru blok `catch`. Di situasi 3, dua sumber daya dipisahkan titik koma di dalam kurung `try` dan ditutup dengan urutan terbalik.
- **[5]** `BufferedWriter` dan `BufferedReader` adalah objek yang kita **pegang sendiri**, jadi wajib ditutup. *Try-with-resources* melakukannya untuk kita.
- **[6]** `readLine()` mengembalikan satu baris tanpa ganti baris, atau `null` jika *file* sudah habis.

> [!NOTE]
> Kapan *try-with-resources* dibutuhkan? Saat kamu memegang objek yang terbuka, seperti `BufferedReader`, `BufferedWriter`, atau `Scanner` untuk *file*. *Method* sekali jalan seperti `Files.readAllLines()` dan `Files.writeString()` membuka **dan** menutup *file* sendiri sehingga tidak perlu dibungkus. Itulah sebabnya kode *file* KedaiKita jarang memakainya. Satu-satunya *try-with-resources* di studi kasus ada di `UjiKedaiKita`, untuk `PrintStream` sementara.

## 4. *Package*: Mengelompokkan Kelas

*File*: [`contoh/Contoh04PaketMini.java`](contoh/Contoh04PaketMini.java)

Versi Python contoh ini memecah kelasnya ke dalam *package* `perpustakaan/` berisi beberapa *file*. Versi Java-nya sengaja tetap **satu *file*** (kelas `Buku`, `Katalog`, dan tiga *exception* ditulis di bawah kelas utama) karena `java NamaFile.java` hanya bisa menjalankan satu *file*. *Output*-nya sama persis dengan versi Python:

***Output:***

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

### *Package* sungguhan di KedaiKita

Studi kasus KedaiKita memakai *package* yang sebenarnya. Aturannya:

1. Setiap *file* diawali baris `package kedaikita;` (sebelum `import`).
2. *File* berada di folder yang namanya **sama** dengan nama *package*: `src/kedaikita/`.
3. Nama lengkap kelas kini memuat nama *package*: `kedaikita.Main`, `kedaikita.Menu`.
4. Kelas yang dipakai dari **luar** *package* harus `public`. Sesama *package* boleh saling memakai tanpa `import`.

Di balik layar, skrip `jalankan` mengompilasi dan menjalankannya dengan dua perintah berikut (diketik dari folder `studi-kasus`; di Command Prompt, ganti `/` dengan `\` jika perintah pertama gagal):

```bash
javac -d out src/kedaikita/*.java
java -cp out kedaikita.Main --demo
```

| Bagian | Artinya |
|---|---|
| `javac -d out` | simpan hasil kompilasi (`.class`) di folder `out/`, dengan subfolder sesuai nama *package* |
| `src/kedaikita/*.java` | kompilasi **semua** *file* di *package* sekaligus karena mereka saling membutuhkan |
| `java -cp out` | *classpath*: cari *file* `.class` di folder `out/` |
| `kedaikita.Main` | nama **lengkap** kelas yang punya `main` |
| `--demo` | argumen untuk program, diterima `main` sebagai `args` |

Setelah kompilasi, folder `out/kedaikita/` berisi satu *file* `.class` untuk setiap kelas dan *interface*: `AplikasiKasir.class`, `DapatDicetak.class`, dan seterusnya. Struktur folder `out/` mengikuti nama *package*.

> [!TIP]
> **Coba sendiri:** buat *package* Java sungguhan versimu sendiri. Di folder `pertemuan-15` milikmu, buat subfolder baru `paket-perpustakaan`, lalu di dalamnya buat folder `perpustakaan`. Salin kode di bawah ke dua *file* baru, `perpustakaan/Buku.java` dan `AplikasiPerpustakaan.java`. Buka terminal di folder `paket-perpustakaan`, lalu kompilasi dan jalankan. Setelah berhasil, hapus kata `public` di depan `class Buku`, lalu kompilasi lagi. Apa yang terjadi?

<details>
<summary>Lihat kode, perintah, dan hasilnya</summary>

Susunan foldernya:

```text
paket-perpustakaan/
├── AplikasiPerpustakaan.java
└── perpustakaan/
    └── Buku.java
```

*File* `perpustakaan/Buku.java`:

```java
package perpustakaan;

public class Buku {
    private String judul;

    public Buku(String judul) {
        this.judul = judul;
    }

    public String getJudul() {
        return judul;
    }
}
```

*File* `AplikasiPerpustakaan.java`:

```java
import perpustakaan.Buku;

public class AplikasiPerpustakaan {
    public static void main(String[] args) {
        Buku buku = new Buku("Laskar Pelangi");
        System.out.println("Judul      : " + buku.getJudul());
        System.out.println("Nama kelas : " + buku.getClass().getName());
    }
}
```

Dari folder `paket-perpustakaan`, ketik (di Command Prompt, ganti `/` dengan `\`):

```bash
javac -d out perpustakaan/*.java AplikasiPerpustakaan.java
java -cp out AplikasiPerpustakaan
```

Hasilnya:

```text
Judul      : Laskar Pelangi
Nama kelas : perpustakaan.Buku
```

Di dalam `out/` kini ada `AplikasiPerpustakaan.class` dan `perpustakaan/Buku.class`: struktur folder `out/` mengikuti nama *package*. Jika kata `public` di depan `class Buku` dihapus, kompilasi gagal dengan pesan `error: Buku is not public in perpustakaan; cannot be accessed from outside package` karena kelas tanpa `public` hanya bisa dipakai dari dalam *package*-nya sendiri.

</details>

## 5. *Unit Test*: *Runner* Mini dan JUnit

*File*: [`contoh/Contoh05UnitTestMini.java`](contoh/Contoh05UnitTestMini.java)

Kelas yang diuji adalah `KeranjangBelanja`: gratis ongkir jika belanja **minimal** Rp100.000, selain itu ongkir Rp10.000. `KeranjangBerbug` adalah turunannya yang sengaja diberi *bug*: *method* `ongkir()`-nya memakai `subtotal() > BATAS_GRATIS_ONGKIR`, padahal seharusnya `>=`.

Di industri, pemrogram Java memakai pustaka **JUnit** untuk *unit test*. JUnit tidak ikut di dalam JDK, jadi di sini kita membuat *runner* mini sendiri, yaitu program kecil yang menjalankan uji satu per satu lalu melaporkan hasilnya. Dua di antara lima kasus ujinya (potongan):

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

Alat bantu ujinya (potongan dari *file* yang sama):

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

***Output:***

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

- **[2]** `KeranjangBelanja::new` adalah *method reference* ke konstruktor (Pertemuan 12). Ia disimpan di *field* `pembuatKeranjang` bertipe `Supplier<KeranjangBelanja>`: sebuah "resep" yang membuat objek baru setiap kali `get()` dipanggil.
- **[3]** Setiap uji meminta keranjang **baru** sehingga uji tidak saling memengaruhi. Inilah pengganti `setUp()` milik `unittest` Python.
- **[4]** `samakan(hasil, harapan)` meniru `assertEqual`. `harusMelempar(jenis, kode)` meniru `assertRaises`: uji lulus jika *lambda* `kode` melempar *exception* jenis tersebut.
- **[5]** Kegagalan pemeriksaan ditandai dengan `AssertionError`. *Runner* menangkapnya, mencetak `[GAGAL]`, lalu **melanjutkan** uji berikutnya.
- **[6]** Pesannya `10000 != 0`: ongkirnya 10000, padahal seharusnya 0. Hanya uji **batas** (tepat Rp100.000) yang menangkap *bug* `>` versus `>=`.

> [!WARNING]
> Java punya kata kunci `assert`, tetapi pemeriksaannya **mati secara bawaan** dan baru aktif jika program dijalankan dengan opsi `-ea`. Jangan mengandalkannya untuk pengujian. Lempar `AssertionError` sendiri seperti di atas, atau pakai JUnit.

### Sekilas JUnit 5

Kamu **tidak wajib** memasang JUnit untuk mata kuliah ini. Namun, ada baiknya mengenal bentuknya karena JUnit adalah standar industri. *Test* yang sama dengan `TestPesanan` versi Python, jika ditulis dengan JUnit 5, kira-kira seperti ini (hanya untuk dibaca; kode ini tidak bisa dijalankan tanpa memasang JUnit):

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

- `@Test` menandai *method test*; JUnit menemukannya sendiri.
- `assertEquals` di JUnit menulis **harapan dulu**, baru hasil. Urutan ini kebalikan dari kebiasaan kita di *runner* mini, jadi hati-hati saat membaca pesan gagalnya.
- JUnit biasanya dijalankan lewat alat bantu *build* (Maven atau Gradle) atau tombol **Run Test** di editor seperti VS Code dan IntelliJ IDEA.

## 6. Validasi *Input* dan Akhir *Input*

*File*: [`contoh/Contoh06ValidasiInput.java`](contoh/Contoh06ValidasiInput.java)

Program interaktif membaca ketikan dengan `Scanner.nextLine()`. Agar hasilnya selalu sama, contoh ini memakai kelas `MasukanPalsu` yang mengambil jawaban dari daftar yang sudah disiapkan. *Method* `baca(pertanyaan)`-nya mencetak pertanyaan beserta jawabannya (jawaban kosong ditampilkan sebagai `<Enter>`), dan melempar `NoSuchElementException("No line found")` jika jawabannya sudah habis **[1]**.

*Method* validasinya bertanya terus sampai jawabannya benar (potongan):

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

***Output:***

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

- **[1]** Saat *input* habis, `Scanner.nextLine()` melempar `NoSuchElementException` dengan pesan `No line found`. `MasukanPalsu` menirunya.
- **[2]** `while (true)` baru berhenti lewat `return` saat jawabannya valid. Jawaban yang salah dibalas pesan yang jelas, lalu pertanyaan diulang.
- **[3]** `Integer.parseInt()` melempar `NumberFormatException` untuk teks seperti `dua`. Perhatikan `trim()` sebelumnya: `parseInt(" 2 ")` akan gagal karena spasi.
- **[4]** Angka yang bentuknya benar tetap diperiksa batasnya.
- **[5]** `Locale.ROOT` membuat perubahan huruf besar tidak bergantung pada pengaturan bahasa komputer.
- **[6]** Akhir *input* ditangani dengan tertib, bukan dibiarkan menjadi *stack trace*.

Pilihan kategori disimpan di `LinkedHashMap`, bukan `Map.of()` karena urutannya **dicetak** (`U, M`), sedangkan `Map.of()` tidak menjamin urutan (Pertemuan 12).

> [!NOTE]
> Di program interaktif sungguhan, akhir *input* terjadi saat pengguna menekan Ctrl+D (macOS/Linux) atau Ctrl+Z lalu Enter (Windows), atau saat masukan diambil dari *file* dan isinya sudah habis.

## 7. Studi Kasus KedaiKita

Rancangan dan arsitekturnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini). Sekarang kita bedah kodenya. Semua perintah di bagian ini diketik dari folder `studi-kasus` (lihat [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)).

### 7.1 Apa yang Berubah dibanding Pertemuan 14

- Semua *file* pindah ke `src/kedaikita/` dan diawali baris `package kedaikita;`. Isi kelas lama **tidak berubah**, kecuali `Makanan` yang mendapat konstruktor *overload* 4 parameter (tanpa level pedas, dipakai oleh *test*).
- *Exception* baru: `FormatDataException` (turunan `KedaiException`, jadi *checked*).
- Kelas baru per lapisan: `RepositoriMenuCSV` dan `PencatatTransaksiCSV` (penyimpanan), `LayananKasir` (layanan), `AplikasiKasir` (tampilan). `Main` kini hanya memilih mode.
- Menu dibaca dari `data/menu_awal.csv`. Ada skrip `jalankan`/`uji` dan kelas pengujian `UjiKedaiKita` berisi 16 pemeriksaan.

### 7.2 Skrip `jalankan` dan `uji`

*File*: [`studi-kasus/jalankan.sh`](studi-kasus/jalankan.sh) dan [`studi-kasus/jalankan.bat`](studi-kasus/jalankan.bat)

Berikut tiga baris perintah di `jalankan.sh` (tanpa komentar pembukanya):

```bash
cd "$(dirname "$0")" || exit 1
javac -d out src/kedaikita/*.java || exit 1
java -cp out kedaikita.Main "$@"
```

- Baris pertama pindah ke folder milik skrip itu sendiri sehingga folder `data/` pasti ditemukan.
- Baris kedua mengompilasi seluruh *package*. Jika gagal, skrip berhenti (`|| exit 1`).
- `"$@"` meneruskan semua argumen, jadi `bash jalankan.sh --demo` menjadi `java -cp out kedaikita.Main --demo`.

Versi Windows (`jalankan.bat`) melakukan hal yang sama dengan `cd /d "%~dp0"` dan `%*`. Skrip `uji.sh`/`uji.bat` identik, hanya kelas yang dijalankan adalah `kedaikita.UjiKedaiKita`.

> [!NOTE]
> Di macOS/Linux, `bash jalankan.sh` selalu berhasil. Bentuk `./jalankan.sh` juga bisa, asalkan *file* skripnya punya izin eksekusi (`chmod +x jalankan.sh`). Di PowerShell, ketik `.\jalankan.bat`; tanpa awalan `.\`, PowerShell tidak mau menjalankannya (lihat Kesalahan 7 di bagian 8).

### 7.3 `Main`: Pintu Masuk

*File*: [`studi-kasus/src/kedaikita/Main.java`](studi-kasus/src/kedaikita/Main.java)

Berikut isi kelasnya, tanpa komentar pembuka dan baris `import`:

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

- `Path.of("data")` adalah *path* **relatif**: dihitung dari folder kerja (*working directory*), yaitu folder aktif terminal saat `java` dijalankan. Karena itu, jalankan dari folder `studi-kasus` (skrip sudah mengurusnya).
- `List.of(args).contains("--demo")` memeriksa apakah argumen `--demo` diberikan.
- *Multi-catch* `KedaiException | IOException | UncheckedIOException` adalah jaring pengaman terakhir. *File* rusak atau masalah disk ditampilkan dengan sopan, lalu `System.exit(1)` menandakan program gagal.

### 7.4 `RepositoriMenuCSV`: Memuat dan Menyimpan Menu

*File*: [`studi-kasus/src/kedaikita/RepositoriMenuCSV.java`](studi-kasus/src/kedaikita/RepositoriMenuCSV.java)

Berikut potongan *method* `muat()`:

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

- `throws IOException, FormatDataException` mengumumkan dua *checked exception*: masalah membaca *file* dan isi *file* yang rusak.
- `kodeTerpakai` adalah `HashSet` (Pertemuan 12) untuk mendeteksi kode ganda. Urutannya tidak penting karena set ini tidak pernah dicetak.
- *Method* `buatMenu()` (lihat *file* lengkapnya) adalah *factory* kecil: memeriksa jumlah kolom dan jenis, mengubah teks menjadi angka dengan `Integer.parseInt()`, lalu membuat `Makanan` atau `Minuman`. `NumberFormatException` dan `IllegalArgumentException` dari validasi `Menu` diterjemahkan menjadi `FormatDataException` bernomor baris.
- `simpan()` menyusun semua baris, lalu menulisnya sekaligus dengan `Files.writeString(path, String.join("\n", semuaBaris) + "\n", StandardCharsets.UTF_8)`.

### 7.5 `PencatatTransaksiCSV` dan `UncheckedIOException`

*File*: [`studi-kasus/src/kedaikita/PencatatTransaksiCSV.java`](studi-kasus/src/kedaikita/PencatatTransaksiCSV.java)

Berikut potongan *method* `perbarui()`:

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

- Kelas ini `implements PengamatPesanan`, *interface* *Observer* dari Pertemuan 14. `Pesanan` memanggil `perbarui()` setiap kali statusnya berubah; hanya status LUNAS yang dicatat.
- Opsi `CREATE` dan `APPEND`: buat *file* jika belum ada, lalu tambahkan satu baris di akhir.
- **Mengapa `UncheckedIOException`?** *Method* yang meng-*override* tidak boleh menambah *checked exception* baru di luar yang dideklarasikan *method* aslinya. `perbarui()` di *interface* tidak punya `throws IOException` sehingga `IOException` tidak boleh lolos begitu saja. Solusinya: bungkus menjadi `UncheckedIOException` (turunan `RuntimeException`) dengan *exception* asal sebagai penyebabnya (*exception chaining*, Pertemuan 11). `Main` menangkapnya di lapisan terluar.

### 7.6 `LayananKasir` dan `AplikasiKasir`

*File*: [`studi-kasus/src/kedaikita/LayananKasir.java`](studi-kasus/src/kedaikita/LayananKasir.java) dan [`studi-kasus/src/kedaikita/AplikasiKasir.java`](studi-kasus/src/kedaikita/AplikasiKasir.java)

`LayananKasir` berisi alur kerja tanpa satu pun `Scanner`: `pelanggan(nama, noHp)`, `buatPesanan(pelanggan)` (sekaligus memasang semua pengamat yang disuntikkan lewat konstruktor), `tambahItem(pesanan, kode, jumlah)`, `bayar(pesanan, jenis, nominal, bank)` yang memakai `PembayaranFactory`, dan `laporan()`. Karena semuanya menerima data yang sudah jadi, kelas ini mudah dipakai tampilan apa pun dan mudah diuji.

`AplikasiKasir` memakai **satu** `Scanner` untuk semua *input*, dan dua *method* bantu di bagian akhir *file*-nya (potongan):

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

Perulangan menu utama di `jalankan()` dibungkus `try ... catch (NoSuchElementException e)`, dan stok **selalu** disimpan setelahnya (potongan):

```java
        } catch (NoSuchElementException e) { // input habis (misalnya saat input dari file)
            System.out.println();
            System.out.println("Input berakhir.");
        }
        new RepositoriMenuCSV(fileMenu).simpan(layanan.getKedai().semuaMenu());
```

Pilihan diskon memakai `Map` berisi "resep" pembuat objek (potongan dari awal kelas):

```java
    private static final Map<String, Supplier<Diskon>> PILIHAN_DISKON = Map.of(
            "1", TanpaDiskon::new,
            "2", DiskonMember::new,
            "3", DiskonHappyHour::new);
```

`PILIHAN_DISKON.get("3").get()` membuat objek `DiskonHappyHour` **baru**. Di sini `Map.of()` aman dipakai karena isinya hanya dicari, tidak pernah dicetak berurutan.

### 7.7 Menjalankan Mode Demo

Dari folder `studi-kasus`, ketik perintah sesuai terminalmu.

**Windows (PowerShell atau terminal VS Code):**

```powershell
.\jalankan.bat --demo
```

**macOS/Linux:**

```bash
bash jalankan.sh --demo
```

Di Command Prompt, `jalankan.bat --demo` juga bisa. Skrip lebih dulu mengompilasi semua *file*; jika tidak ada pesan *error* kompilasi, program langsung berjalan.

*Output* diawali `Memuat menu dari data/menu_awal.csv: 6 menu` dan daftar keenam menu, lalu transaksi 1 dan 2 dengan proses pembayaran dan struk lengkap seperti di Pertemuan 14. Berikut cuplikan bagian selanjutnya: *input* keliru, laporan, dan riwayat yang dibaca dari *file*.

***Output:***

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

*Output* versi Java **sama persis** dengan versi Python, baris demi baris. Riwayat itu ditulis oleh `PencatatTransaksiCSV` lalu dibaca kembali dengan `bacaSemua()`. *Output* diakhiri isi `demo-menu.csv` dengan stok terbaru.

### 7.8 Memakai Mode Interaktif

Dari folder `studi-kasus`, jalankan `.\jalankan.bat` (PowerShell), `jalankan.bat` (Command Prompt), atau `bash jalankan.sh` (macOS/Linux). Kini kamu menjadi kasirnya. Setiap pertanyaan diakhiri titik dua: ketik jawabanmu di terminal, lalu tekan Enter.

| Pertanyaan | Yang kamu ketik |
|---|---|
| `Pilihan:` (menu utama) | `1` lihat menu, `2` buat pesanan, `3` laporan sesi ini, `4` riwayat dari *file*, `0` simpan dan keluar |
| `Nama pelanggan:` dan `No. HP:` | nama dan nomor HP pelanggan |
| `Kode menu:` | kode seperti `M01` (huruf kecil boleh). Jika semua item sudah dimasukkan, **langsung tekan Enter** tanpa mengetik apa pun. |
| `Jumlah:` | angka bulat, misalnya `2` |
| `Pilihan diskon:` | `1` tanpa diskon, `2` member (baru berlaku jika pelanggan sudah punya minimal 10 poin), `3` *happy hour* (20% untuk minuman) |
| `Pilihan pembayaran:` | `1` tunai (lalu uang diterima), `2` QRIS (lalu saldo *e-wallet*), `3` kartu kredit (lalu nama bank; biaya layanan 2%) |

Pertanyaan pembayaran diulang sampai pesanan LUNAS. Jika uangnya kurang, pilih lagi lalu masukkan nominal yang cukup, atau pilih `3` karena pembayaran kartu kredit di simulasi ini selalu disetujui.

Berikut **ilustrasi** satu sesi. Teks setelah tanda titik dua pada baris pertanyaan adalah **ketikan kasir**; `<Enter>` berarti kasir langsung menekan Enter. Menu utama dan struk disingkat agar ringkas. Sesi yang sama di versi Python menghasilkan tampilan yang persis sama.

```text
Memuat menu dari data/menu_awal.csv: 6 menu
Selamat datang di Kasir KedaiKita!

=========== MENU UTAMA ===========
1. Lihat daftar menu
(... pilihan 2, 3, 4 ...)
0. Simpan dan keluar
Pilihan: 2
Nama pelanggan: Dewi Lestari
No. HP: 081255501234
Masukkan kode menu satu per satu (kosongkan untuk selesai).
  Kode menu: m01
  Jumlah: dua
  Harap isi dengan angka bulat, misalnya 2 atau 50000.
  Jumlah: 2
  -> 2 x Kopi Susu Gula Aren ditambahkan
  Kode menu: M05
  Jumlah: 1
  -> 1 x Pisang Goreng Keju ditambahkan
  Kode menu: <Enter>
Diskon: 1. Tanpa diskon  2. Member  3. Happy Hour
Pilihan diskon: 5
Pilihan tidak dikenal, coba lagi.
Pilihan diskon: 1
(struk dicetak: Status BARU, TOTAL Rp56.100)
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 50000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp56.100
[GAGAL] Pembayaran Tunai gagal: uang kurang Rp6.100
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 100000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp56.100
  Uang diterima Rp100.000, kembalian Rp43.900
  Status       : LUNAS (+5 poin)
(struk dicetak lagi: Status LUNAS)
(menu utama)
Pilihan: 4
P001 | Dewi Lestari | 081255501234 | 3 | 56100
(menu utama)
Pilihan: 0
Stok terbaru disimpan ke data/menu.csv. Sampai jumpa!
```

Setelah sesi ini, folder `data/` berisi `menu.csv` (stok kopi tinggal 18, pisang goreng 11) dan `transaksi.csv` (satu baris P001). Saat aplikasi dibuka lagi, baris pertamanya menjadi `Memuat menu dari data/menu.csv: 6 menu`. Stok berlanjut dari sesi sebelumnya!

**Cara keluar yang benar:**

- Pilih `0` di menu utama. Stok disimpan ke `data/menu.csv`, lalu aplikasi pamit.
- Jika *input* berakhir di tengah sesi (kamu menekan Ctrl+D di macOS/Linux, atau Ctrl+Z lalu Enter di Windows), aplikasi mencetak `Input berakhir.`, tetap menyimpan stok ke `data/menu.csv`, lalu pamit.
- **Jangan** keluar dengan Ctrl+C. Program langsung dihentikan sebelum sempat menyimpan stok, padahal pesanan yang sudah LUNAS tetap tercatat di `transaksi.csv`.

> [!WARNING]
> Buat pesanan lagi di sesi kedua, lalu lihat riwayatnya (pilihan 4). Nomornya kembali **P001** karena penghitung nomor pesanan (*field* `static`) mulai dari nol setiap kali aplikasi dibuka. Memperbaikinya adalah [Latihan 3](../latihan.md).

### 7.9 Saat *File* Data Rusak

Percobaan ini dikerjakan di **salinan**. Salin seluruh folder `studi-kasus` ke folder `pertemuan-15` milikmu (lihat Persiapan). Di salinan itu, buat *file* baru `data/menu.csv` (di VS Code: klik kanan folder `data`, pilih **New File**) berisi tiga baris berikut. Harga Es Teh Manis sengaja ditulis `8rb`:

```text
jenis;kode;nama;harga;stok;ekstra
Minuman;M01;Kopi Susu Gula Aren;18000;20;dingin
Minuman;M02;Es Teh Manis;8rb;30;dingin
```

Simpan, lalu jalankan mode interaktif dari folder `studi-kasus` salinan itu (`.\jalankan.bat` atau `bash jalankan.sh`). Hasilnya:

```text
Terjadi kesalahan: Baris 3: harga, stok, dan level pedas harus berupa angka
```

Pesannya sama persis dengan versi Python. Pesan untuk kerusakan lain ada di [tabel halaman konsep](../README.md#46-jangan-percaya-isi-file). Setelah selesai, hapus `data/menu.csv` di salinan itu agar aplikasi kembali memuat `menu_awal.csv`.

### 7.10 *Unit Test* `UjiKedaiKita`

*File*: [`studi-kasus/src/kedaikita/UjiKedaiKita.java`](studi-kasus/src/kedaikita/UjiKedaiKita.java)

`UjiKedaiKita` adalah *runner* mini yang lebih lengkap: setiap uji adalah *method* yang mengembalikan `true` (lulus) atau `false` (gagal). Berikut potongannya:

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

Uji untuk `RepositoriMenuCSV` menulis *file* ke folder dari `Files.createTempDirectory()` lalu menghapusnya di blok `finally` sehingga folder `data/` tidak pernah tersentuh. Dari folder `studi-kasus`, jalankan `.\uji.bat` (PowerShell), `uji.bat` (Command Prompt), atau `bash uji.sh` (macOS/Linux). Di balik layar, skrip menjalankan `java -cp out kedaikita.UjiKedaiKita`.

***Output:***

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

Keenam belas uji ini sama dengan 16 *test* versi Python. Cara membaca hasilnya:

| Baris | Artinya |
|---|---|
| `[LULUS] nama uji` | semua pemeriksaan di uji itu benar |
| `[GAGAL] nama uji` | uji selesai, tetapi hasil kodenya berbeda dari harapan (padanan `FAIL` di Python) |
| `[GAGAL] nama uji (exception tak terduga: ...)` | uji berhenti di tengah jalan karena *exception* yang tidak diduga (padanan `ERROR` di Python); teks di dalam kurung menyebut jenis dan pesannya |
| `Hasil: 16 lulus, 0 gagal` | ringkasan; target kita **0 gagal** |

Contoh baris *exception* tak terduga, jika stok kopi di `siapkanPesanan()` hanya 1 padahal uji memesan 2:

```text
[GAGAL] Pesanan: subtotal (exception tak terduga: kedaikita.StokTidakCukupException: Stok Kopi Susu Gula Aren tidak cukup: diminta 2, tersedia 1)
```

Jika ada yang gagal, program keluar dengan kode 1 sehingga alat otomatis (misalnya layanan CI di GitHub) bisa mendeteksinya.

> [!TIP]
> **Coba sendiri:** kerjakan di salinan folder `studi-kasus` di folder `pertemuan-15` milikmu. Buka `src/kedaikita/PengaturanKedai.java` di salinan itu, ubah baris `this.pajakPersen = 10;` menjadi `this.pajakPersen = 11;`, simpan, lalu jalankan skrip `uji` dari folder salinan itu. Uji mana yang gagal?

<details>
<summary>Lihat jawaban</summary>

`Pesanan: total sudah termasuk pajak 10 persen` dan `Pesanan: struk memuat total` menjadi `[GAGAL]` karena totalnya kini Rp67.710, bukan Rp67.100. Uji lain tetap lulus karena tidak bergantung pada pajak. Baris terakhirnya menjadi `Hasil: 14 lulus, 2 gagal`. Skrip mengompilasi ulang sebelum menguji, jadi perubahanmu langsung terpakai.

</details>

### 7.11 Batasan yang Perlu Kamu Ketahui

KedaiKita sengaja dibuat sederhana. Batasan berikut nyata dan bisa kamu temui saat mencobanya. Tuliskan batasan seperti ini dengan jujur di README proyek akhirmu juga.

| Batasan | Akibatnya | Lihat |
|---|---|---|
| Nomor pesanan mulai dari P001 lagi setiap kali aplikasi dibuka | `transaksi.csv` bisa berisi nomor ganda | [Latihan 3](../latihan.md) |
| Total pesanan selalu dihitung ulang dari harga menu dan poin pelanggan **saat ini** | struk yang dicetak ulang, laporan, dan bahkan `transaksi.csv` bisa berbeda dari jumlah yang benar-benar dibayar (contoh di bawah) | catatan desain di solusi [Latihan 5](../latihan.md) |
| *File* CSV yang tidak tersimpan sebagai UTF-8 | aplikasi berhenti dengan pesan yang kurang jelas, `Terjadi kesalahan: Input length = 1` | Kesalahan 6 di bagian 8 |
| Isi kolom tidak boleh memuat titik koma atau tanda petik ganda | baris CSV terpecah salah | [halaman konsep bagian 4.4](../README.md#44-mengapa-titik-koma-bukan-koma) |
| *Input* berakhir saat pesanan belum dibayar | stok item yang sudah dimasukkan tetap berkurang dan ikut tersimpan, padahal pesanannya tidak tercatat | bagian 7.8 |

Contoh batasan kedua: pelanggan baru memesan 4 Nasi Goreng Kampung dengan diskon Member. Saat membayar, poinnya masih 0 sehingga diskon belum berlaku, dan ia membayar Rp110.000. Setelah lunas, ia mendapat 11 poin. Struk yang dicetak sesudah pembayaran, laporan sesi, dan `transaksi.csv` lalu menghitung ulang dengan poin baru itu sehingga mencatat Rp99.000. Perbaikannya adalah menyimpan total **saat pembayaran terjadi**, persis seperti struk kertas yang tidak berubah lagi setelah dicetak.

## 8. Kesalahan Umum dan Cara Membaca Pesan *Error*

### Kesalahan 1: Menjalankan kelas tanpa nama *package*

Dari folder `studi-kasus`, setelah kompilasi, perintah berikut **salah**:

```bash
java -cp out Main
```

Pesan *error*-nya:

```text
Error: Could not find or load main class Main
Caused by: java.lang.ClassNotFoundException: Main
```

**Artinya:** kelasnya bernama lengkap `kedaikita.Main` dan tersimpan di `out/kedaikita/Main.class`. Tidak ada kelas `Main` tanpa *package*. **Perbaikan:** `java -cp out kedaikita.Main`.

### Kesalahan 2: Hanya mengompilasi satu *file*

Dari folder `studi-kasus`, perintah berikut **salah**:

```bash
javac -d out src/kedaikita/Main.java
```

Awal pesan *error*-nya:

```text
src/kedaikita/Main.java:36: error: cannot find symbol
        AplikasiKasir aplikasi = new AplikasiKasir(FOLDER_DATA);
        ^
  symbol:   class AplikasiKasir
  location: class Main
```

Pesan ini diikuti beberapa *error* serupa untuk kelas lain.

**Artinya:** `javac` tidak menemukan *file* kelas-kelas lain yang dipakai `Main`. **Perbaikan:** kompilasi seluruh *package* sekaligus: `javac -d out src/kedaikita/*.java`, atau cukup pakai skrip `jalankan`.

### Kesalahan 3: Menjalankan dari folder yang salah

Dari folder `java/` (satu tingkat di atas `studi-kasus`), perintah berikut **salah**:

```bash
java -cp studi-kasus/out kedaikita.Main --demo
```

Hasilnya:

```text
=== MODE DEMO KASIR KEDAIKITA ===
Terjadi kesalahan: data/demo-transaksi.csv
```

**Artinya:** `Path.of("data")` dihitung dari folder kerja, dan folder `java/` tidak punya subfolder `data/`. Pesan `NoSuchFileException` hanya berisi *path file* yang gagal dibuka. Di Windows, pemisah foldernya tertulis `\`, misalnya `data\demo-transaksi.csv`. Mode interaktif yang dijalankan dari folder yang salah, termasuk lewat tombol **Run** di VS Code, gagal dengan pesan serupa: `Terjadi kesalahan: data/transaksi.csv`. **Perbaikan:** jalankan dari folder `studi-kasus`, atau pakai skrip (skrip selalu pindah ke foldernya sendiri).

### Kesalahan 4: `split` tanpa `-1`

Perhatikan potongan kode berikut. Untuk mencobanya, tempel ketiga baris ini ke dalam `main` sebuah *file* latihan di folder `pertemuan-15` milikmu.

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

**Artinya:** tanpa `-1`, `split()` membuang *string* kosong di **akhir** hasilnya. Kolom `ekstra` yang kosong hilang, dan `RepositoriMenuCSV` akan menolak baris itu dengan `Baris 2: harus ada 6 kolom`. **Perbaikan:** selalu tulis `split(PEMISAH, -1)` untuk data CSV. (Di Python, `"a;b;".split(";")` tetap menghasilkan 3 elemen.)

### Kesalahan 5: `Scanner` tanpa penanganan akhir *input*

Coba sendiri di folder `pertemuan-15` milikmu: buat *file* baru bernama `BacaNama.java`, salin kode berikut, lalu jalankan `java BacaNama.java`.

```java
import java.util.Scanner;

public class BacaNama {
    public static void main(String[] args) {
        Scanner masukan = new Scanner(System.in);
        System.out.print("Nama pelanggan: ");
        String nama = masukan.nextLine();
        System.out.println("Halo " + nama);
    }
}
```

Saat ditanya nama, jangan mengetik nama. Tekan Ctrl+D (macOS/Linux) atau Ctrl+Z lalu Enter (Windows) untuk mengakhiri *input*. Pesan *error*-nya:

```text
Nama pelanggan: Exception in thread "main" java.util.NoSuchElementException: No line found
	at java.base/java.util.Scanner.nextLine(Scanner.java:1660)
	at BacaNama.main(BacaNama.java:7)
```

**Artinya:** `nextLine()` tidak punya lagi yang bisa dibaca. `NoSuchElementException` adalah *unchecked exception*, jadi *compiler* tidak mengingatkanmu. **Perbaikan:** bungkus perulangan utama dengan `try ... catch (NoSuchElementException e)`, seperti `AplikasiKasir.jalankan()`.

### Kesalahan 6: *File* CSV tidak tersimpan sebagai UTF-8

*File* `menu.csv` diedit lalu disimpan Excel dengan pilihan **CSV (Comma delimited)**, dan ada huruf `é` pada `Café Latte`. Saat aplikasi dibuka, muncul pesan berikut:

```text
Terjadi kesalahan: Input length = 1
```

**Artinya:** pilihan itu menyimpan `é` sebagai satu *byte* `0xE9` (*encoding* Windows-1252), padahal dalam UTF-8 *byte* itu tidak sah. `Files.readAllLines(..., UTF_8)` lalu melempar `MalformedInputException` (turunan `IOException`), yang pesannya kurang jelas. Inilah salah satu batasan KedaiKita (bagian 7.11). **Perbaikan:** simpan ulang lewat **File → Save As**, lalu pilih jenis **CSV UTF-8 (Comma delimited)**, atau hindari huruf beraksen. Pilihan itu menambahkan penanda kecil (BOM) di awal *file*, tetapi KedaiKita tetap bisa membacanya karena baris pertama (judul kolom) dilewati. Tantangan: tangkap `MalformedInputException` di `muat()` dan ubah menjadi `FormatDataException` dengan pesan yang ramah.

### Kesalahan 7: PowerShell tidak mau menjalankan `jalankan.bat`

Di PowerShell (termasuk terminal VS Code di Windows), perintah `jalankan.bat --demo` tanpa awalan `.\` ditolak. Pesannya kira-kira seperti ini (Windows PowerShell 5.1, dipendekkan):

```text
jalankan.bat : The term 'jalankan.bat' is not recognized as the name of a cmdlet, function, script file, or operable program.
...
Suggestion [3,General]: The command jalankan.bat was not found, but does exist in the current location. Windows PowerShell does not load commands from the current location by default. If you trust this command, instead type: ".\jalankan.bat".
```

**Artinya:** demi keamanan, PowerShell tidak menjalankan *file* dari folder aktif kecuali kamu menyebut letaknya dengan jelas. **Perbaikan:** ketik `.\jalankan.bat --demo`, persis seperti saran di baris terakhir pesan itu. Jika pesannya berbunyi sama tetapi tanpa baris *Suggestion*, kemungkinan besar kamu belum berada di folder `studi-kasus`.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Java, misalnya nomor baris di dalam `Scanner.java`. Fokuslah pada jenis *error*-nya (`ClassNotFoundException`, `cannot find symbol`, `NoSuchElementException`) dan kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Alamat *file* (`Path`) | `Path.of(...)`, `folder.resolve("nama")` | `Path.of("data").resolve("menu.csv")` |
| Menulis / menambah *file* | `Files.writeString(path, teks, UTF_8[, APPEND])` | `StandardOpenOption.APPEND` |
| Membaca *file* | `Files.readString(path, UTF_8)`, `Files.readAllLines(path, UTF_8)` | `List<String> semuaBaris = ...` |
| CSV: menulis / membaca | `String.join(";", kolom)` / `baris.split(";", -1)` | `"a;b;".split(";", -1)` → 3 kolom |
| Menutup otomatis | `try (Tipe x = ...) { ... }` | `try (BufferedReader r = Files.newBufferedReader(p, UTF_8))` |
| Sumber daya sendiri | `implements AutoCloseable` + `close()` | `class SambunganPrinter implements AutoCloseable` |
| Folder sementara | `Files.createTempDirectory("awalan")` | hapus di `finally` dengan `Files.deleteIfExists` |
| *Package* | `package nama;` di baris pertama | `package kedaikita;` |
| Kompilasi dan jalankan | `javac -d out ...` lalu `java -cp out paket.Kelas` | `java -cp out kedaikita.Main --demo` |
| Membungkus *checked exception* | `throw new UncheckedIOException(pesan, e);` | di `PencatatTransaksiCSV.perbarui()` |
| *Input* dan akhir *input* | `scanner.nextLine()` + `catch (NoSuchElementException e)` | `AplikasiKasir.tanya()` |
| Pemeriksaan uji | `throw new AssertionError(hasil + " != " + harapan);` | *runner* mini |
| JUnit 5 (wawasan) | `@Test`, `@BeforeEach`, `assertEquals`, `assertThrows` | `assertEquals(36000, pesanan.hitungSubtotal())` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).
- Mulai rencanakan [Proyek Akhir](../proyek-akhir.md)-mu.

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
