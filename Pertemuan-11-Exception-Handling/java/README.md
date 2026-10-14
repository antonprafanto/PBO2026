# ☕ Praktik Java — Pertemuan 11: Exception Handling

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 11](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Exception Pertama: Pembagian dengan Nol](#1-exception-pertama-pembagian-dengan-nol)
2. [Mengubah Teks Menjadi Angka](#2-mengubah-teks-menjadi-angka)
3. [Indeks di Luar Batas dan Exception yang Merambat](#3-indeks-di-luar-batas-dan-exception-yang-merambat)
4. [Banyak `catch` dan Urutannya](#4-banyak-catch-dan-urutannya)
5. [`finally` dan Pengganti `else`](#5-finally-dan-pengganti-else)
6. [`throw`: Melempar dan Melempar Ulang](#6-throw-melempar-dan-melempar-ulang)
7. [Exception Buatan Sendiri dan Chaining](#7-exception-buatan-sendiri-dan-chaining)
8. [Checked dan Unchecked Exception](#8-checked-dan-unchecked-exception)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 8 contoh program satu file (contoh 08 khusus Java)
├── studi-kasus/     <- KedaiKita versi Pertemuan 11 (satu kelas per file, 4 kelas exception baru)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file, jadi bisa langsung dijalankan:

```bash
cd Pertemuan-11-Exception-Handling/java/contoh
java Contoh01PembagianNol.java
```

Studi kasus terdiri atas banyak file. Kompilasi semuanya dulu, lalu jalankan kelas `Main`:

```bash
cd Pertemuan-11-Exception-Handling/java/studi-kasus
javac *.java
java Main
```

> [!TIP]
> Di VS Code, buka folder `java/` **milik pertemuan ini** saja (File → Open Folder). Nama kelas di dalam satu folder harus unik, jadi contoh dan solusi memakai nama yang berbeda dari studi kasus, misalnya `SaldoTidakCukupException` di contoh 07. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

> [!NOTE]
> Halaman ini banyak menampilkan **pesan error asli** dari potongan kode yang sengaja dibuat salah. Bunyinya bisa sedikit berbeda antarversi JDK. Fokuslah pada **jenis** exception, **pesannya**, dan **nomor barisnya**.

## 1. Exception Pertama: Pembagian dengan Nol

File: [`contoh/Contoh01PembagianNol.java`](contoh/Contoh01PembagianNol.java)

### Tanpa penanganan: program berhenti mendadak

Kita mulai dari program patungan di [halaman konsep](../README.md#4-jika-tidak-ada-yang-menangkap-traceback-dan-stack-trace) yang **belum** menangani exception. Di file `Patungan.java`, method `hitungPatungan()` menghitung `total / jumlahOrang` di baris 3. Method itu dipanggil dari `main()` di baris 8 dengan jumlah orang 0, lalu hasilnya dicetak dengan awalan `Hasil: Rp`. Saat dijalankan dengan `java Patungan.java`, hasilnya:

```text
Menghitung patungan...
Exception in thread "main" java.lang.ArithmeticException: / by zero
	at Patungan.hitungPatungan(Patungan.java:3)
	at Patungan.main(Patungan.java:8)
```

Baca *stack trace* **dari atas ke bawah**:

- Baris pertama menyebut **jenis** exception (`java.lang.ArithmeticException`) dan **pesannya** (`/ by zero`).
- Baris `at` **paling atas** adalah tempat exception lahir: `hitungPatungan`, baris 3. Baris `at` di bawahnya menunjukkan pemanggilnya: `main`, baris 8.
- `Hasil: Rp...` tidak pernah tercetak. Begitu exception dilempar, sisa program tidak dijalankan.

### Dengan `try`/`catch`: program tetap berjalan

```java
    /** Membagi tagihan sama rata ke semua orang (sisa pembagian dibuang). */
    static int hitungPatungan(int total, int jumlahOrang) {
        return total / jumlahOrang; // [1] gagal jika jumlahOrang = 0
    }

    public static void main(String[] args) {
        System.out.println("=== PATUNGAN MAKAN DI WARUNG ===");
        int perOrang = hitungPatungan(120000, 4);
        System.out.println("Rp120000 dibagi 4 orang: Rp" + perOrang + " per orang");

        System.out.println();
        System.out.println("=== JIKA JUMLAH ORANG NOL ===");
        try { // [2] "coba jalankan blok ini"
            System.out.println("Menghitung patungan untuk 0 orang...");
            int hasil = hitungPatungan(120000, 0); // [3] exception dilempar di sini
            System.out.println("Hasil: Rp" + hasil + " per orang"); // [4] baris ini DILEWATI
        } catch (ArithmeticException e) { // [5] exception ditangkap di sini
            System.out.println("Gagal: jumlah orang tidak boleh nol");
        }
        System.out.println("Program tetap berjalan sampai baris terakhir"); // [6]
    }
```

**Output:**

```text
=== PATUNGAN MAKAN DI WARUNG ===
Rp120000 dibagi 4 orang: Rp30000 per orang

=== JIKA JUMLAH ORANG NOL ===
Menghitung patungan untuk 0 orang...
Gagal: jumlah orang tidak boleh nol
Program tetap berjalan sampai baris terakhir
```

Penjelasan:

- **[1]** Pembagian dua `int` dengan nol melempar `ArithmeticException`. Method ini tidak menangkapnya, jadi exception merambat ke pemanggil. (Untuk `double`, `10.0 / 0` justru menghasilkan `Infinity` tanpa exception. Itulah salah satu alasan uang selalu disimpan sebagai `int`.)
- **[2]** `try { ... }` membungkus kode yang **mungkin** gagal.
- **[3]** dan **[4]** Di baris [3] exception dilempar. Java langsung berhenti menjalankan blok `try`, jadi baris [4] **dilewati**.
- **[5]** `catch (ArithmeticException e)` hanya menangkap `ArithmeticException` (atau turunannya). Variabel `e` berisi objek exception-nya. Di sini kita tidak memakainya, tetapi Java tetap mewajibkan namanya ditulis.
- **[6]** Setelah blok `catch` selesai, program melanjutkan ke baris **setelah** struktur `try`, bukan kembali ke baris yang gagal.

> [!TIP]
> **Coba sendiri:** ganti `catch (ArithmeticException e)` menjadi `catch (IllegalArgumentException e)`, lalu jalankan. Tebak dulu: apakah exception-nya masih tertangkap?

<details>
<summary>Lihat jawaban</summary>

Tidak. Jenisnya tidak cocok, jadi exception lolos. Program berhenti dengan *stack trace* `java.lang.ArithmeticException: / by zero`, dan baris "Program tetap berjalan..." tidak pernah tercetak. Penangkap hanya bekerja untuk jenis yang **cocok**.

</details>

## 2. Mengubah Teks Menjadi Angka

File: [`contoh/Contoh02KonversiTeks.java`](contoh/Contoh02KonversiTeks.java)

Data dari formulir, file, atau jaringan selalu datang sebagai **teks**. Saat teks diubah dengan `Integer.parseInt()`, teks yang bukan bilangan bulat membuat Java melempar `NumberFormatException`.

```java
    public static void main(String[] args) {
        // [1] isian jumlah porsi dari formulir pesanan online (semuanya teks)
        String[] isianFormulir = {"3", "dua", "5", "2.5", "", "4"};
        int total = 0;
        int jumlahSalah = 0;

        System.out.println("=== REKAP JUMLAH PORSI ===");
        for (String teks : isianFormulir) {
            try {
                int porsi = Integer.parseInt(teks); // [2] bisa melempar NumberFormatException
                total += porsi; // [3] hanya dijalankan jika parseInt() berhasil
                System.out.println("'" + teks + "' -> " + porsi + " porsi");
            } catch (NumberFormatException e) { // [4] isian ini dilewati, perulangan lanjut
                jumlahSalah++;
                System.out.println("'" + teks + "' -> bukan bilangan bulat, dilewati");
            }
        }

        System.out.println();
        System.out.println("Total porsi     : " + total);
        System.out.println("Isian yang salah: " + jumlahSalah);
    }
```

**Output:**

```text
=== REKAP JUMLAH PORSI ===
'3' -> 3 porsi
'dua' -> bukan bilangan bulat, dilewati
'5' -> 5 porsi
'2.5' -> bukan bilangan bulat, dilewati
'' -> bukan bilangan bulat, dilewati
'4' -> 4 porsi

Total porsi     : 12
Isian yang salah: 3
```

Penjelasan:

- **[1]** dan **[2]** Data ditulis langsung di program (bukan dari `Scanner`), supaya hasilnya selalu sama. `Integer.parseInt("dua")`, `"2.5"`, dan `""` sama-sama melempar `NumberFormatException`.
- **[3]** Penjumlahan ada **setelah** `parseInt()` di dalam blok `try`. Jika `parseInt()` gagal, baris ini ikut dilewati, sehingga total tidak tercemar data yang salah.
- **[4]** Karena `try` berada **di dalam** perulangan, satu isian yang salah tidak menghentikan perulangan.

### Stack trace yang melewati kode bawaan Java

Jika `Integer.parseInt("dua")` dijalankan tanpa `try` (misalnya di file `Konversi.java`), *stack trace*-nya lebih panjang:

```text
Exception in thread "main" java.lang.NumberFormatException: For input string: "dua"
	at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
	at java.base/java.lang.Integer.parseInt(Integer.java:662)
	at java.base/java.lang.Integer.parseInt(Integer.java:778)
	at Konversi.main(Konversi.java:3)
```

Tiga baris `at java.base/...` adalah kode **milik Java sendiri**, bukan tempat kesalahanmu. Cari baris pertama yang menyebut **file milikmu**: `Konversi.main(Konversi.java:3)`. Di baris 3 itulah teks yang salah dikirim.

Pesan seperti `For input string: "dua"` bisa kamu ambil sendiri lewat `e.getMessage()` di dalam `catch`. Pesan bawaan ini berguna untuk programmer, tetapi kurang ramah untuk pengguna, jadi contoh 02 menulis pesannya sendiri.

> [!WARNING]
> `Integer.parseInt(" 7 ")` **gagal** karena ada spasi, padahal di Python `int(" 7 ")` berhasil. Jika data mungkin berisi spasi di tepinya, bersihkan dulu dengan `teks.trim()`.

## 3. Indeks di Luar Batas dan Exception yang Merambat

File: [`contoh/Contoh03IndeksDanMerambat.java`](contoh/Contoh03IndeksDanMerambat.java)

Meminta elemen `List` di posisi yang tidak ada membuat Java melempar `IndexOutOfBoundsException`. Contoh ini juga memperlihatkan **perjalanan** exception melewati beberapa method. `main()` menyimpan tiga kelompok di sebuah `ArrayList`, lalu memanggil `umumkan()`, yang memanggil `ambilKelompok()`:

```java
    /** Mengembalikan nama kelompok pada giliran tertentu (mulai dari 1). */
    static String ambilKelompok(List<String> jadwal, int giliran) {
        System.out.println("    [ambil kelompok] mencari giliran " + giliran);
        return jadwal.get(giliran - 1); // [1] IndexOutOfBoundsException jika terlalu besar
    }

    static void umumkan(List<String> jadwal, int giliran) {
        System.out.println("  [umumkan] giliran " + giliran);
        String kelompok = ambilKelompok(jadwal, giliran); // [2] tidak ada try di sini
        System.out.println("  Giliran " + giliran + ": " + kelompok); // [3] dilewati jika ada error
    }
```

Perulangan di `main()`:

```java
        int[] daftarGiliran = {1, 3, 5};
        for (int giliran : daftarGiliran) {
            try {
                umumkan(jadwal, giliran); // [4]
            } catch (IndexOutOfBoundsException e) { // [5] exception merambat sampai ke sini
                System.out.println("  -> Giliran " + giliran + " tidak ada. "
                        + "Hanya ada " + jadwal.size() + " kelompok.");
            }
        }
```

**Output:**

```text
=== JADWAL PRESENTASI ===
  [umumkan] giliran 1
    [ambil kelompok] mencari giliran 1
  Giliran 1: Kelompok Pesut
  [umumkan] giliran 3
    [ambil kelompok] mencari giliran 3
  Giliran 3: Kelompok Bekantan
  [umumkan] giliran 5
    [ambil kelompok] mencari giliran 5
  -> Giliran 5 tidak ada. Hanya ada 3 kelompok.
```

Penjelasan:

- **[1]** Giliran 5 berarti indeks 4, padahal list hanya punya indeks 0 sampai 2. Pesan exception-nya: `Index 4 out of bounds for length 3`.
- **[2]** dan **[3]** `umumkan()` tidak punya `try`, jadi exception **merambat** melewatinya, dan baris [3] tidak pernah dijalankan untuk giliran 5. Bandingkan dengan giliran 1 dan 3 di output.
- **[4]** dan **[5]** Exception baru tertangkap di `main()`, tempat yang tahu harus berkata apa kepada pengguna.

> [!NOTE]
> Untuk **array**, jenisnya `ArrayIndexOutOfBoundsException`, turunan dari `IndexOutOfBoundsException`. Indeks negatif juga ditolak: `jadwal.get(-1)` melempar exception berpesan `Index -1 out of bounds for length 3`. (Di Python, indeks -1 justru sah dan berarti elemen terakhir.)

## 4. Banyak `catch` dan Urutannya

File: [`contoh/Contoh04BanyakCatch.java`](contoh/Contoh04BanyakCatch.java)

Setiap baris data berformat `nama;total_nilai;jumlah_tugas`. Satu baris bisa gagal dengan beberapa cara, dan setiap cara ditangani berbeda.

```java
    /** Menghitung rata-rata nilai tugas dari satu baris data. */
    static int hitungRataRata(String baris) {
        String[] bagian = baris.split(";");
        int total = Integer.parseInt(bagian[1]); // [1] ArrayIndexOutOfBounds atau NumberFormat
        int jumlahTugas = Integer.parseInt(bagian[2]);
        return total / jumlahTugas; // [2] ArithmeticException jika belum ada tugas
    }
```

Array `data` di `main()` berisi enam baris: `"Ayu;255;3"`, `"Bima;sembilan puluh;1"` (nilai bukan angka), `"Citra;160"` (kolom jumlah tugas tidak ada), `"Dimas;0;0"` (belum ada tugas yang dinilai), `null` (data kosong dari sistem lama), dan `"Eka;176;2"`. Setiap baris diproses dengan banyak `catch`:

```java
        for (int nomor = 1; nomor <= data.length; nomor++) {
            String baris = data[nomor - 1];
            try {
                int rata = hitungRataRata(baris);
                String nama = baris.split(";")[0];
                System.out.println("Baris " + nomor + " (" + nama + "): rata-rata " + rata);
            } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) { // [3] dua jenis
                System.out.println("Baris " + nomor + ": format salah, dilewati");
            } catch (ArithmeticException e) { // [4]
                System.out.println("Baris " + nomor + ": belum ada tugas yang dinilai");
            } catch (Exception e) { // [5] jaring pengaman: PALING UMUM, PALING BAWAH
                System.out.println("Baris " + nomor + ": data tidak terbaca, dilewati");
            }
        }
    }
```

**Output:**

```text
=== RATA-RATA NILAI TUGAS ===
Baris 1 (Ayu): rata-rata 85
Baris 2: format salah, dilewati
Baris 3: format salah, dilewati
Baris 4: belum ada tugas yang dinilai
Baris 5: data tidak terbaca, dilewati
Baris 6 (Eka): rata-rata 88
```

Penjelasan:

- **[1]** `"Citra;160".split(";")` hanya menghasilkan array dua elemen, jadi `bagian[2]` melempar `ArrayIndexOutOfBoundsException`. `Integer.parseInt("sembilan puluh")` melempar `NumberFormatException`.
- **[2]** Dimas belum punya tugas yang dinilai, jadi `0 / 0` melempar `ArithmeticException`.
- **[3]** *Multi-catch*: tanda `|` berarti "tangkap salah satu dari keduanya". Cocok jika penanganannya sama.
- **[4]** Penangkap khusus untuk pembagian dengan nol, dengan pesan yang berbeda.
- **[5]** `Exception` menangkap hampir semua exception lain. Di sini ia menangkap baris 5: `split()` pada `null` melempar `NullPointerException`, jenis yang tidak kita duga. Karena paling umum, ia **wajib** ditulis paling bawah.

### Jika urutannya salah, kode tidak bisa dikompilasi

Bagaimana jika penangkap umum ditulis lebih dulu?

```java
        try {
            int hasil = 120000 / 0;
            System.out.println(hasil);
        } catch (Exception e) {
            System.out.println("Terjadi kesalahan umum");
        } catch (ArithmeticException e) {
            System.out.println("Gagal: jumlah orang tidak boleh nol");
        }
```

Pesan error-nya:

```text
Urutan.java:8: error: exception ArithmeticException has already been caught
        } catch (ArithmeticException e) {
          ^
1 error
```

**Artinya:** `ArithmeticException` adalah turunan `Exception`, jadi sudah "tertangkap" oleh penangkap pertama. Penangkap kedua tidak mungkin pernah dijalankan, dan Java menolaknya. Python justru menerima kode seperti ini tanpa protes.

Aturan serupa berlaku untuk *multi-catch*: jenis-jenisnya tidak boleh berhubungan induk-anak. `catch (NumberFormatException | IllegalArgumentException e)` ditolak dengan pesan `Alternatives in a multi-catch statement cannot be related by subclassing`, karena `NumberFormatException` adalah turunan `IllegalArgumentException`. Cukup tulis induknya saja.

## 5. `finally` dan Pengganti `else`

File: [`contoh/Contoh05Finally.java`](contoh/Contoh05Finally.java)

Proyektor di ruang kelas harus **selalu** dimatikan setelah presentasi, apa pun yang terjadi. Method `tampilkan()` milik kelas `Proyektor` bisa gagal dengan dua cara: melempar `IllegalArgumentException` jika file bukan PDF, atau `IllegalStateException` jika lampunya putus.

```java
    static void presentasi(Proyektor proyektor, String namaFile) {
        proyektor.nyalakan();
        try {
            proyektor.tampilkan(namaFile); // [1] bisa gagal
            System.out.println("  Presentasi lancar, terima kasih!"); // [3] hanya jika berhasil
        } catch (IllegalArgumentException e) { // [2] hanya menangani IllegalArgumentException
            System.out.println("  Gagal presentasi: " + e.getMessage());
        } finally { // [4] SELALU dijalankan
            proyektor.matikan();
        }
    }
```

`main()` memanggil `presentasi()` tiga kali: dengan file PDF, dengan file `.docx`, lalu sekali lagi setelah lampu dirusak:

```java
        proyektor.rusakkanLampu();
        try {
            presentasi(proyektor, "laporan-akhir.pdf"); // [5]
        } catch (IllegalStateException e) { // [6] ditangkap oleh pemanggil
            System.out.println("Ditangani di main: " + e.getMessage());
        }
```

**Output:**

```text
=== PRESENTASI 1: LANCAR ===
  Proyektor R301 menyala
  Menampilkan laporan-akhir.pdf
  Presentasi lancar, terima kasih!
  Proyektor R301 dimatikan

=== PRESENTASI 2: FILE SALAH ===
  Proyektor R301 menyala
  Gagal presentasi: file laporan-akhir.docx bukan PDF
  Proyektor R301 dimatikan

=== PRESENTASI 3: LAMPU PUTUS ===
  Proyektor R301 menyala
  Proyektor R301 dimatikan
Ditangani di main: lampu proyektor putus
```

Penjelasan:

- **[1]** Hanya baris yang **mungkin gagal** dan yang bergantung padanya yang ditaruh di blok `try`.
- **[2]** `catch (IllegalArgumentException e)` menangani file yang bukan PDF. `e.getMessage()` mengambil pesan dari `throw`.
- **[3]** Java tidak punya blok `else` seperti Python. Kode yang hanya boleh berjalan jika semuanya berhasil ditulis di **akhir** blok `try`. Baris ini hanya tercetak pada presentasi 1.
- **[4]** `finally` berjalan di **ketiga** presentasi. Proyektor tidak pernah lupa dimatikan.
- **[5]** dan **[6]** Pada presentasi 3, `IllegalStateException` tidak cocok dengan `catch` di `presentasi()`. Exception merambat ke `main()`, tetapi **sebelum** itu `finally` tetap mematikan proyektor. Perhatikan urutan di output: "dimatikan" muncul sebelum "Ditangani di main".

> [!NOTE]
> Ada beda halus antara "akhir blok `try`" (Java) dan `else` (Python). Kode di akhir blok `try` ikut "dijaga" oleh `catch`: jika baris **[3]** sendiri melempar `IllegalArgumentException`, `catch` di bawahnya ikut menangkapnya. Karena itu, jaga agar baris tambahan di akhir `try` tetap sederhana.

> [!NOTE]
> **Pratinjau Pertemuan 15:** untuk file, Java punya *try-with-resources*, misalnya `try (BufferedReader pembaca = Files.newBufferedReader(Path.of("data", "menu_awal.csv"))) { ... }`. Objek di dalam tanda kurung **pasti** ditutup saat blok selesai, walaupun terjadi exception, seperti `finally` yang ditulis untukmu.

## 6. `throw`: Melempar dan Melempar Ulang

File: [`contoh/Contoh06ThrowDanLemparUlang.java`](contoh/Contoh06ThrowDanLemparUlang.java)

Di Pertemuan 04 kita sudah memakai `throw new IllegalArgumentException(...)` untuk menolak data. Contoh ini mengulangnya, lalu menambah satu pola baru: **melempar ulang**. Kelas `AC` menyimpan suhu (awalnya 25) dan konstanta batas `SUHU_MIN = 16` serta `SUHU_MAKS = 30`. Method pengaturnya:

```java
    public void aturSuhu(int suhu) {
        if (suhu < SUHU_MIN || suhu > SUHU_MAKS) { // [1] periksa lebih dulu
            throw new IllegalArgumentException("Suhu " + suhu + " di luar batas "
                    + SUHU_MIN + "-" + SUHU_MAKS + " derajat"); // [2]
        }
        this.suhu = suhu; // [3] hanya dijalankan jika lolos pemeriksaan
    }
```

Method perantara di kelas utama:

```java
    /** Meneruskan perintah ke AC. Penolakan dicatat, lalu dilempar ulang. */
    static void tekanRemote(AC ac, int suhu) {
        try {
            ac.aturSuhu(suhu);
        } catch (IllegalArgumentException e) {
            System.out.println("  [log] perintah " + suhu + " derajat ditolak"); // [4] catat...
            throw e; // [5] ...lalu lempar ulang exception yang SAMA ke pemanggil
        }
    }
```

`main()` mengirim perintah 22, 10, 35, dan 18 derajat. Setiap perintah dibungkus `try`, dan penangkapnya mencetak `"Layar remote: " + e.getMessage()` **[6]**.

**Output:**

```text
=== REMOTE AC (suhu awal 25 derajat) ===
Suhu diatur ke 22 derajat
  [log] perintah 10 derajat ditolak
Layar remote: Suhu 10 di luar batas 16-30 derajat
  [log] perintah 35 derajat ditolak
Layar remote: Suhu 35 di luar batas 16-30 derajat
Suhu diatur ke 18 derajat
Suhu akhir: 18 derajat
```

Penjelasan:

- **[1]**, **[2]**, dan **[3]** Validasi lebih awal: data diperiksa **sebelum** field diubah. `throw new ...` membuat objek exception berisi pesan, lalu melemparnya, sehingga method langsung berhenti dan suhu lama tetap utuh.
- **[4]** `tekanRemote()` ingin mencatat setiap penolakan, tetapi tidak tahu harus menampilkan apa ke pengguna.
- **[5]** `throw e;` melempar ulang **objek yang sama**, lengkap dengan pesan dan *stack trace* aslinya. Tidak ada `new`, karena kita tidak membuat exception baru.
- **[6]** `main()` menerima exception yang sama. Perhatikan urutan di output: log dulu, baru "Layar remote".

> [!TIP]
> **Coba sendiri:** hapus baris `throw e;` di `tekanRemote()`, lalu jalankan. Apa yang salah dari output-nya?

<details>
<summary>Lihat jawaban</summary>

Program **berbohong**: tepat setelah baris `[log] perintah 10 derajat ditolak`, tercetak `Suhu diatur ke 10 derajat`, padahal AC menolaknya (hal yang sama terjadi untuk 35 derajat). Exception sudah "ditelan" oleh `tekanRemote()`, jadi `main()` mengira semuanya berhasil. Inilah bahayanya menangkap exception tanpa meneruskannya.

</details>

## 7. Exception Buatan Sendiri dan Chaining

File: [`contoh/Contoh07ExceptionBuatanSendiri.java`](contoh/Contoh07ExceptionBuatanSendiri.java)

Exception hanyalah **kelas**, jadi kita bisa membuat jenis baru dengan pewarisan. Contoh ini membuat hierarki kecil untuk rekening tabungan: `RekeningException` sebagai induk, dengan dua anak, `SaldoTidakCukupException` (membawa data saldo dan jumlah yang diminta) dan `TransferGagalException`.

```java
/** Induk semua error yang berhubungan dengan rekening. */
class RekeningException extends Exception { // [1] turunan Exception
    // Nomor versi untuk serialisasi; dianjurkan ada di setiap kelas exception.
    private static final long serialVersionUID = 1L;

    public RekeningException(String pesan) {
        super(pesan);
    }

    public RekeningException(String pesan, Throwable penyebab) {
        super(pesan, penyebab); // pesan + exception lama yang menjadi penyebab
    }
}

/** Dilempar saat saldo tidak cukup untuk penarikan. */
class SaldoTidakCukupException extends RekeningException { // [2] turunan RekeningException
    private static final long serialVersionUID = 1L;

    private int saldo; // [4] data tambahan untuk penangkap
    private int diminta;

    public SaldoTidakCukupException(int saldo, int diminta) {
        super("Saldo tidak cukup: saldo Rp" + saldo + ", diminta Rp" + diminta); // [3]
        this.saldo = saldo;
        this.diminta = diminta;
    }
```

Kelas ini juga punya *getter* `getSaldo()`, `getDiminta()`, dan `getKekurangan()` (selisih keduanya). `TransferGagalException` cukup punya konstruktor `(String pesan, Throwable penyebab)` yang meneruskan keduanya ke `super`. Method `tarik(int jumlah) throws SaldoTidakCukupException` milik kelas `Rekening` melempar `new SaldoTidakCukupException(saldo, jumlah)` **[5]** jika saldo kurang.

Method `transfer()` membungkusnya menjadi `TransferGagalException`:

```java
    static void transfer(Rekening asal, Rekening tujuan, int jumlah)
            throws TransferGagalException {
        try {
            asal.tarik(jumlah);
        } catch (SaldoTidakCukupException e) {
            String pesan = "Transfer " + asal.getPemilik() + " ke " + tujuan.getPemilik()
                    + " gagal";
            throw new TransferGagalException(pesan, e); // [6] simpan penyebab aslinya
        }
        tujuan.setor(jumlah);
        System.out.println("Transfer Rp" + jumlah + " dari " + asal.getPemilik()
                + " ke " + tujuan.getPemilik() + " berhasil");
    }
```

Program utamanya:

```java
        System.out.println("=== TARIK TUNAI ===");
        int[] daftarJumlah = {200000, 400000};
        for (int jumlah : daftarJumlah) {
            try {
                budi.tarik(jumlah);
                System.out.println("Tarik Rp" + jumlah + " berhasil, sisa saldo Rp"
                        + budi.getSaldo());
            } catch (SaldoTidakCukupException e) { // [7] tangkap yang spesifik
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Kurang Rp" + e.getKekurangan()
                        + ". Coba tarik paling banyak Rp" + e.getSaldo() + "."); // [8]
            }
        }

        System.out.println();
        System.out.println("=== TRANSFER ===");
        Rekening[] daftarAsal = {budi, siti};
        Rekening[] daftarTujuan = {siti, budi};
        int[] daftarNominal = {50000, 250000};
        for (int i = 0; i < daftarAsal.length; i++) {
            try {
                transfer(daftarAsal[i], daftarTujuan[i], daftarNominal[i]);
            } catch (RekeningException e) { // [9] tangkap induknya: semua error rekening
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Penyebab: " + e.getCause().getMessage()); // [10]
            }
        }
```

**Output:**

```text
=== TARIK TUNAI ===
Tarik Rp200000 berhasil, sisa saldo Rp300000
Gagal: Saldo tidak cukup: saldo Rp300000, diminta Rp400000
  Kurang Rp100000. Coba tarik paling banyak Rp300000.

=== TRANSFER ===
Transfer Rp50000 dari Budi ke Siti berhasil
Gagal: Transfer Siti ke Budi gagal
  Penyebab: Saldo tidak cukup: saldo Rp150000, diminta Rp250000

Saldo akhir: Budi Rp250000, Siti Rp150000
```

Penjelasan:

- **[1]** dan **[2]** Exception buatan sendiri mewarisi `Exception` (atau turunannya). `SaldoTidakCukupException` **adalah** `RekeningException`, dan juga **adalah** `Exception`. Karena tidak mewarisi `RuntimeException`, ketiganya termasuk ***checked exception*** (bagian 8).
- **[3]** dan **[4]** Pesan dikirim ke konstruktor induk dengan `super(...)`; pesan inilah yang dikembalikan `getMessage()`. Data tambahan disimpan di field biasa, lengkap dengan *getter*.
- **[5]** Karena checked, method yang bisa melemparnya **wajib** menulis `throws` di kepalanya, seperti `tarik()` dan `transfer()`.
- **[6]** `new TransferGagalException(pesan, e)` membuat exception baru dan menyimpan `e` sebagai penyebabnya (*exception chaining*). Yang menyimpannya adalah konstruktor induk `Exception(String, Throwable)`.
- **[7]** dan **[8]** Penangkap spesifik bisa memakai data tambahan (`getKekurangan()`, `getSaldo()`) untuk memberi saran.
- **[9]** dan **[10]** Penangkap induk `RekeningException` menangkap `TransferGagalException` karena relasi *is-a*. `e.getCause()` mengembalikan exception lama, jadi penyebab aslinya tidak hilang.

> [!NOTE]
> **Apa itu `serialVersionUID`?** Kelas `Exception` mendukung *serialisasi*, yaitu mengubah objek menjadi deretan byte agar bisa disimpan atau dikirim lewat jaringan. `serialVersionUID` adalah "nomor versi" kelas untuk keperluan itu. Kita belum memakai serialisasi, jadi kamu boleh mengabaikannya untuk sekarang. Baris itu ditulis agar kompilasi dengan `javac -Xlint:all` bersih dari peringatan `[serial] serializable class RekeningException has no definition of serialVersionUID`. Tanpa baris itu, program tetap bisa dikompilasi dan dijalankan.

### Jika exception bersambung tidak ditangkap

Tambahkan baris `transfer(siti, budi, 250000);` di akhir `main()`, di luar `try`. Java langsung menolak saat kompilasi dengan pesan `unreported exception TransferGagalException; must be caught or declared to be thrown` (aturan *checked exception*, bagian 8). Untuk sekadar melihat *stack trace*-nya, ubah juga kepala `main` menjadi `public static void main(String[] args) throws TransferGagalException`, lalu jalankan lagi:

```text
Exception in thread "main" TransferGagalException: Transfer Siti ke Budi gagal
	at Contoh07ExceptionBuatanSendiri.transfer(Contoh07ExceptionBuatanSendiri.java:34)
	at Contoh07ExceptionBuatanSendiri.main(Contoh07ExceptionBuatanSendiri.java:76)
Caused by: SaldoTidakCukupException: Saldo tidak cukup: saldo Rp150000, diminta Rp250000
	at Rekening.tarik(Contoh07ExceptionBuatanSendiri.java:149)
	at Contoh07ExceptionBuatanSendiri.transfer(Contoh07ExceptionBuatanSendiri.java:30)
	at Contoh07ExceptionBuatanSendiri.main(Contoh07ExceptionBuatanSendiri.java:76)
	at java.base/jdk.internal.reflect.DirectMethodHandleAccessor.invoke(DirectMethodHandleAccessor.java:103)
	at java.base/java.lang.reflect.Method.invoke(Method.java:580)
	at jdk.compiler/com.sun.tools.javac.launcher.Main.execute(Main.java:484)
	at jdk.compiler/com.sun.tools.javac.launcher.Main.run(Main.java:208)
	at jdk.compiler/com.sun.tools.javac.launcher.Main.main(Main.java:135)
```

Bagian atas adalah exception yang akhirnya lolos (transfer gagal). Bagian **`Caused by:`** adalah penyebabnya (saldo kurang), lengkap dengan lokasinya: `Rekening.tarik`, baris 149. Baris `java.base/...` dan `jdk.compiler/...` milik Java sendiri, yang menjalankan program satu file.

> [!WARNING]
> Menulis `throws` di kepala `main` hanya untuk percobaan. Di program sungguhan, `main` adalah tempat terakhir untuk menangkap exception dan memberi pesan yang ramah. Jika `main` ikut melempar, pengguna hanya melihat *stack trace*.

## 8. Checked dan Unchecked Exception

File: [`contoh/Contoh08CheckedUnchecked.java`](contoh/Contoh08CheckedUnchecked.java) (contoh ini **khusus Java**, lihat [Jembatan](../jembatan-python-java.md))

Di [halaman konsep](../README.md#9-checked-dan-unchecked-exception-khusus-java), kita sudah melihat dua kelompok exception di Java. Ringkasnya:

- **Checked:** turunan `Exception` yang **bukan** turunan `RuntimeException`, misalnya `IOException` dan `KedaiException`. *Compiler* memaksa kita memilih: **tangkap** dengan `try`/`catch`, atau **umumkan** dengan `throws` agar pemanggil yang mengurus.
- **Unchecked:** turunan `RuntimeException`, misalnya `ArithmeticException`, `IllegalArgumentException`, dan `NullPointerException`. Tidak ada paksaan.

Contoh ini memakai kelas kuliah yang bisa penuh saat pengisian KRS. Exception-nya dideklarasikan sebagai `class KelasPenuhException extends Exception` **[1]**, dengan konstruktor yang menyusun pesan seperti `Kelas PBO-A sudah penuh (kapasitas 2 orang)`. Method yang melemparnya:

```java
    public void daftar(String nama) throws KelasPenuhException { // [2] wajib diumumkan
        if (peserta.size() >= kapasitas) {
            throw new KelasPenuhException(kode, kapasitas);
        }
        peserta.add(nama);
    }
```

Konstruktor `KelasKuliah` juga menolak kapasitas 0 dengan `IllegalArgumentException`, **tanpa** menulis `throws`, karena exception itu unchecked. Di kelas utama, satu method meneruskan exception dengan `throws`, dan `main` menangkapnya:

```java
    /** Mendaftarkan beberapa mahasiswa sekaligus. Exception TIDAK ditangkap di sini. */
    static void daftarkanRombongan(KelasKuliah kelas, String[] daftarNama)
            throws KelasPenuhException { // [4] "saya tidak menangani, saya meneruskan"
        for (String nama : daftarNama) {
            kelas.daftar(nama);
            System.out.println(nama + " terdaftar di " + kelas.getKode());
        }
    }

    public static void main(String[] args) {
        System.out.println("=== KRS: CHECKED EXCEPTION WAJIB DITANGANI ===");
        KelasKuliah pboA = new KelasKuliah("PBO-A", 2);
        String[] pendaftar = {"Ayu", "Bima", "Citra"};
        for (String nama : pendaftar) {
            try { // [3] tanpa try/catch ini, program GAGAL DIKOMPILASI
                pboA.daftar(nama);
                System.out.println(nama + " terdaftar di " + pboA.getKode());
            } catch (KelasPenuhException e) {
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Saran: pilih kelas paralel lain");
            }
        }

        System.out.println();
        System.out.println("=== MENERUSKAN DENGAN THROWS ===");
        KelasKuliah pboB = new KelasKuliah("PBO-B", 1);
        String[] rombongan = {"Dimas", "Eka"};
        try {
            daftarkanRombongan(pboB, rombongan);
        } catch (KelasPenuhException e) { // [5] ditangkap di pemanggil paling atas
            System.out.println("Gagal: " + e.getMessage());
        }
```

Bagian terakhir `main` **[6]** mencoba membuat kelas berkapasitas 0 di dalam `try`/`catch (IllegalArgumentException e)`.

**Output:**

```text
=== KRS: CHECKED EXCEPTION WAJIB DITANGANI ===
Ayu terdaftar di PBO-A
Bima terdaftar di PBO-A
Gagal: Kelas PBO-A sudah penuh (kapasitas 2 orang)
  Saran: pilih kelas paralel lain

=== MENERUSKAN DENGAN THROWS ===
Dimas terdaftar di PBO-B
Gagal: Kelas PBO-B sudah penuh (kapasitas 1 orang)

=== UNCHECKED EXCEPTION ===
Gagal membuat kelas: Kapasitas harus lebih dari 0
```

Penjelasan:

- **[1]** `extends Exception` (bukan `RuntimeException`) menjadikan `KelasPenuhException` sebuah *checked exception*. Kelas penuh adalah situasi **wajar** yang harus dipikirkan setiap pemanggil.
- **[2]** Method yang bisa melempar *checked exception* **wajib** mengumumkannya dengan `throws`.
- **[3]** Setiap pemanggil `daftar()` wajib memilih: tangkap atau umumkan. Di sini kita menangkapnya.
- **[4]** `daftarkanRombongan()` memilih **mengumumkan**: ia tidak punya `try`, tetapi menulis `throws KelasPenuhException`. Saat Eka ditolak, perulangan berhenti dan exception merambat ke `main`.
- **[5]** `main` yang akhirnya menangkap. Perhatikan output: Dimas terdaftar, lalu langsung muncul pesan gagal, tanpa baris untuk Eka.
- **[6]** `IllegalArgumentException` boleh ditangkap, tetapi tidak wajib. Kapasitas 0 adalah kesalahan programmer, jadi biasanya cukup diperbaiki di kodenya.

### Jika lupa menangani checked exception

Jika `pboA.daftar("Ayu");` ditulis tanpa `try`/`catch` di method yang tidak punya `throws`, kompilasi gagal:

```text
LupaTangani.java:7: error: unreported exception KelasPenuhException; must be caught or declared to be thrown
        pboA.daftar("Ayu");
                   ^
1 error
```

**Artinya:** *"exception KelasPenuhException tidak dilaporkan; harus ditangkap atau diumumkan untuk dilempar"*. Pilih salah satu: bungkus dengan `try`/`catch`, atau tambahkan `throws KelasPenuhException` di kepala method pemanggilnya.

Kebalikannya juga dilarang: menangkap *checked exception* yang tidak mungkin dilempar oleh isi blok `try`. Misalnya `catch (java.io.IOException e)` di sekitar kode yang tidak membaca file ditolak dengan pesan `exception IOException is never thrown in body of corresponding try statement`.

> [!NOTE]
> Buat exception sendiri yang **checked** (`extends Exception`) untuk situasi wajar yang harus diantisipasi pemanggil, seperti kelas penuh atau stok habis. Pakai **unchecked** (`extends RuntimeException`, atau langsung `IllegalArgumentException`) untuk kesalahan pemrograman. Alasan lengkapnya ada di halaman konsep.

## 9. Studi Kasus KedaiKita

File: semua file di folder `studi-kasus/`, terutama empat file exception yang baru (misalnya [`studi-kasus/KedaiException.java`](studi-kasus/KedaiException.java)) dan [`studi-kasus/Main.java`](studi-kasus/Main.java).

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kesalahan-yang-jelas-dan-bisa-ditangkap).

**Apa yang berubah dibanding Pertemuan 10?**

- **Empat file baru:** `KedaiException.java`, `StokTidakCukupException.java`, `MenuTidakDitemukanException.java`, dan `PembayaranGagalException.java`.
- `Kedai.cariMenu()` melempar `MenuTidakDitemukanException`, tidak lagi mengembalikan `null`. `Menu.kurangiStok()` melempar `StokTidakCukupException` (sebelumnya `IllegalArgumentException` biasa).
- `Pembayaran.proses()` dan versi kelas anaknya bertipe `void` dan melempar `PembayaranGagalException`, tidak lagi mengembalikan `boolean`.
- `Pesanan.tambahItem()` dan `Pesanan.bayar()` menolak pesanan yang sudah LUNAS dengan `KedaiException`. `bayar()` kini bertipe `void`.
- `Main.java`: skenarionya baru, memakai `try`/`catch`/`finally`. Kelas lainnya **tidak berubah**.

### Exception khusus KedaiKita

`KedaiException.java`:

```java
/** Induk semua error khusus KedaiKita. */
public class KedaiException extends Exception {
    // serialVersionUID: "nomor versi" yang dianjurkan untuk setiap turunan
    // Exception (javac -Xlint memperingatkan jika tidak ada). Cukup diisi 1L.
    private static final long serialVersionUID = 1L;

    public KedaiException(String pesan) {
        super(pesan);
    }
}
```

Tiga turunannya disusun seperti `SaldoTidakCukupException` di contoh 07: konstruktor menyusun pesan lewat `super(...)`, lalu menyimpan data tambahan di field *private* dengan *getter*. `StokTidakCukupException` membawa `getNamaMenu()`, `getDiminta()`, dan `getTersedia()`. `MenuTidakDitemukanException` membawa `getKode()`. `PembayaranGagalException` membawa `getMetode()` dan `getAlasan()`.

> [!IMPORTANT]
> **Mengapa `KedaiException` dibuat checked?** Menu tidak ada, stok habis, dan pembayaran gagal adalah kejadian **wajar** di kasir, bukan kesalahan pemrograman. Setiap kode yang memesan atau membayar harus siap menghadapinya. Dengan *checked exception*, *compiler* menjamin tidak ada pemanggil yang lupa. Konsekuensinya, `throws` muncul di banyak method, dan `Main` wajib memakai `try`/`catch`.

### Rantai `throws`

Ikuti perjalanan exception stok. `Menu.kurangiStok()` mengumumkan jenis yang **tepat**, `throws StokTidakCukupException`. `Pesanan.tambahItem()` memanggilnya tanpa menangkap:

```java
    public void tambahItem(Menu menu, int jumlah) throws KedaiException {
        if (status.equals("LUNAS")) {
            throw new KedaiException("Pesanan " + nomor + " sudah lunas, tidak bisa diubah");
        }
        ItemPesanan item = new ItemPesanan(menu, jumlah); // objek item dibuat OLEH pesanan
        menu.kurangiStok(jumlah); // bisa melempar StokTidakCukupException
        daftarItem.add(item);
    }
```

- Karena tidak menangkap, `tambahItem()` wajib ikut mengumumkan. Ia menulis induknya, `throws KedaiException`, yang sudah mencakup `StokTidakCukupException` **dan** `KedaiException` yang ia lempar sendiri untuk pesanan LUNAS.
- Dengan pola yang sama, `Kedai.cariMenu()` menulis `throws MenuTidakDitemukanException`, dan `Pesanan.bayar()` menulis `throws KedaiException`.

Kelas abstrak `Pembayaran` mengumumkan exception di method abstraknya:

```java
    /** Memproses pembayaran. Melempar PembayaranGagalException jika gagal. */
    public abstract void proses(int total) throws PembayaranGagalException;
```

`PembayaranTunai` dan `PembayaranQRIS` melemparnya saat uang atau saldo kurang. `PembayaranKartu` justru menulis `proses()` **tanpa** `throws`:

```java
    // Tanpa "throws": di simulasi ini transaksi kartu selalu disetujui.
    // Method yang meng-override boleh melempar LEBIH SEDIKIT checked exception
    // daripada method induknya, tetapi tidak boleh lebih banyak.
    @Override
    public void proses(int total) {
```

Jika `PembayaranKartu` mencoba menulis `throws KedaiException` (lebih luas daripada induknya), kompilasi gagal dengan pesan `proses(int) in PembayaranKartu cannot override proses(int) in Pembayaran` dan keterangan `overridden method does not throw KedaiException`. Aturan ini masuk akal: kode yang memanggil `pembayaran.proses(...)` hanya bersiap menghadapi `PembayaranGagalException`. Kelas anak tidak boleh memberi "kejutan" exception lain.

### Program utama

Bagian pertama memproses lima permintaan Budi. Karena Java tidak punya `else`, baris `[OK]` ditulis di akhir blok `try`:

```java
        System.out.println("=== PESANAN BUDI: MENAMBAH ITEM ===");
        Pesanan pesananBudi = kedai.buatPesanan(budi);
        // Dua array sejajar: kode menu ke-i dipesan sebanyak jumlah ke-i.
        String[] kodePermintaan = {"M01", "M03", "M99", "M04", "M02"};
        int[] jumlahPermintaan = {2, 1, 1, 50, 0};
        for (int i = 0; i < kodePermintaan.length; i++) {
            String kode = kodePermintaan[i];
            int jumlah = jumlahPermintaan[i];
            try {
                Menu menu = kedai.cariMenu(kode);
                pesananBudi.tambahItem(menu, jumlah);
                // Baris ini hanya dijalankan jika dua baris di atasnya
                // berhasil (tidak ada exception yang dilempar).
                System.out.println("  [OK] " + jumlah + " x " + menu.getNama());
            } catch (MenuTidakDitemukanException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
            } catch (StokTidakCukupException e) {
                System.out.println("  [GAGAL] " + e.getMessage());
                System.out.println("          Saran: pesan paling banyak " + e.getTersedia()
                        + " porsi");
            } catch (KedaiException e) { // error kedai lain (misalnya pesanan sudah lunas)
                System.out.println("  [GAGAL] " + e.getMessage());
            } catch (IllegalArgumentException e) {
                System.out.println("  [GAGAL] " + kode + ": " + e.getMessage());
            }
        }
        System.out.println();
```

- Dua penangkap spesifik ditulis **di atas** induknya, `KedaiException`. Urutan sebaliknya tidak bisa dikompilasi.
- Penangkap `KedaiException` juga **wajib** ada, karena `tambahItem()` mengumumkan `throws KedaiException`.
- `IllegalArgumentException` menangkap permintaan 0 porsi yang ditolak `ItemPesanan`. Ia tidak berhubungan dengan `KedaiException`, jadi urutannya terhadap penangkap lain bebas.

Bagian kedua memperlihatkan **rencana cadangan** dan `finally`:

```java
        System.out.println("=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===");
        Pesanan pesananSiti = kedai.buatPesanan(siti);
        try {
            pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
            pesananSiti.tambahItem(kedai.cariMenu("M05"));
            pesananSiti.bayar(new PembayaranQRIS(20000));
        } catch (PembayaranGagalException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
            System.out.println("  Mencoba kartu kredit...");
            try {
                pesananSiti.bayar(new PembayaranKartu("BNI"));
            } catch (KedaiException e2) {
                System.out.println("  [GAGAL LAGI] " + e2.getMessage());
            }
        } catch (KedaiException e) {
            System.out.println("  [GAGAL] " + e.getMessage());
        } finally {
            System.out.println("  [log] proses pesanan Siti selesai");
        }
        System.out.println();
```

- Di dalam blok `catch` boleh ada `try` lagi. Variabelnya diberi nama `e2`, karena nama `e` masih dipakai oleh `catch` di luarnya.
- `bayar()` tidak menangkap `PembayaranGagalException` dari `proses()`. Exception itu merambat ke sini, dan baris `status = "LUNAS";` di `bayar()` ikut dilewati, sehingga status tetap BARU sampai kartu kredit berhasil.

Bagian ketiga (pesanan Rina) cukup memakai **satu** penangkap, `catch (KedaiException e)`, untuk semua jenis error kedai: kode M77 yang tidak ada, stok yang kurang, serta membayar ulang dan mengubah pesanan Budi yang sudah LUNAS.

Jalankan `javac *.java` lalu `java Main` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

**Output:**

```text
=== PESANAN BUDI: MENAMBAH ITEM ===
  [OK] 2 x Kopi Susu Gula Aren
  [OK] 1 x Nasi Goreng Kampung
  [GAGAL] Menu dengan kode M99 tidak ditemukan
  [GAGAL] Stok Mie Goreng Jawa tidak cukup: diminta 50, tersedia 10
          Saran: pesan paling banyak 10 porsi
  [GAGAL] M02: Jumlah harus lebih dari 0

Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

=== PESANAN SITI: BAYAR GAGAL, LALU COBA LAGI ===
Pembayaran pesanan P002 (Siti Aminah)
  Metode       : QRIS
  Total bayar  : Rp31.000
  [GAGAL] Pembayaran QRIS gagal: saldo e-wallet tidak cukup (saldo Rp20.000)
  Mencoba kartu kredit...
Pembayaran pesanan P002 (Siti Aminah)
  Metode       : Kartu Kredit BNI
  Biaya layanan: Rp620
  Total bayar  : Rp31.620
  Transaksi kartu BNI disetujui sebesar Rp31.620
  Status       : LUNAS (+3 poin)
  [log] proses pesanan Siti selesai

=== SATU PENANGKAP UNTUK SEMUA ERROR KEDAI ===
  Ditolak: Menu dengan kode M77 tidak ditemukan
  Ditolak: Stok Mie Goreng Jawa tidak cukup: diminta 99, tersedia 10
  Ditolak: Pesanan P001 sudah lunas
  Ditolak: Pesanan P001 sudah lunas, tidak bisa diubah

=== RINGKASAN ===
P001 (Budi Santoso): LUNAS
P002 (Siti Aminah): LUNAS
P003 (Rina Marlina): BARU, 0 item
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11 | pedas level 0
```

Output ini **sama persis** dengan versi Python. Pesanan Rina tetap kosong (0 item), dan stok Mie Goreng Jawa tetap 10, karena permintaan yang berlebihan ditolak sebelum stok diubah.

> [!TIP]
> **Coba sendiri:** tambahkan baris `kedai.cariMenu("M99");` tepat setelah `Kedai kedai = siapkanKedai();` di `main`, di luar `try` mana pun. Tebak dulu: kapan kesalahannya ketahuan?

<details>
<summary>Lihat jawaban</summary>

Kesalahannya ketahuan **sebelum** program berjalan. `javac *.java` menolak:

```text
Main.java:30: error: unreported exception MenuTidakDitemukanException; must be caught or declared to be thrown
        kedai.cariMenu("M99");
                      ^
1 error
```

Inilah keuntungan *checked exception*: lupa menangani menu yang tidak ada langsung ketahuan saat kompilasi. Versi Python dari kesalahan yang sama baru meledak saat program berjalan. Hapus lagi baris tadi setelah mencoba.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Dua kesalahan yang paling sering sudah kamu temui: **menelan exception diam-diam** dengan `catch` yang kosong ("Coba sendiri" bagian 6), dan **lupa menangani checked exception** (bagian 8). Untuk yang kedua, ingat dua pilihannya: **tangkap** jika method itu tahu harus berbuat apa, atau **umumkan** dengan `throws` jika keputusannya milik pemanggil. Berikut kesalahan lain yang sering muncul.

### Kesalahan 1: Lupa `new` saat melempar

```java
        throw IllegalArgumentException("Suhu di luar batas");
```

```text
LupaNew.java:3: error: cannot find symbol
        throw IllegalArgumentException("Suhu di luar batas");
              ^
  symbol:   method IllegalArgumentException(String)
  location: class LupaNew
1 error
```

**Artinya:** tanpa `new`, Java mengira `IllegalArgumentException(...)` adalah pemanggilan **method**, dan method itu tidak ada. **Perbaikan:** `throw new IllegalArgumentException("Suhu di luar batas");`.

> [!NOTE]
> Yang boleh dilempar hanyalah objek turunan `Throwable`. `throw "Stok habis";` ditolak dengan pesan `incompatible types: String cannot be converted to Throwable`.

### Kesalahan 2: Memakai variabel dari blok `try` di luar blok itu

```java
    static int bacaPorsi(String teks) {
        try {
            int porsi = Integer.parseInt(teks);
        } catch (NumberFormatException e) {
            System.out.println("'" + teks + "' bukan angka");
        }
        return porsi;
    }
```

```text
Lingkup.java:8: error: cannot find symbol
        return porsi;
               ^
  symbol:   variable porsi
  location: class Lingkup
1 error
```

**Artinya:** variabel yang dideklarasikan **di dalam** `{ }` blok `try` hanya hidup di blok itu. Jika deklarasinya dipindah ke atas `try` (`int porsi;`), Java tetap menolak dengan pesan `variable porsi might not have been initialized`, karena jika `parseInt()` gagal, `porsi` tidak pernah diisi. **Perbaikan:** kembalikan nilai cadangan di dalam `catch` (misalnya `return 0;`), atau lempar ulang exception-nya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Menangkap | `try { ... } catch (Jenis e) { ... }` | `catch (ArithmeticException e)` |
| Membaca pesan exception | `e.getMessage()` | `"Gagal: " + e.getMessage()` |
| Beberapa jenis, satu penanganan | `catch (A \| B e)` | `catch (NumberFormatException \| ArrayIndexOutOfBoundsException e)` |
| Selalu dijalankan | `finally { ... }` | `finally { proyektor.matikan(); }` |
| Pengganti `else` Python | tulis di akhir blok `try` | `System.out.println("[OK] ...");` |
| Melempar | `throw new Jenis("pesan");` | `throw new IllegalArgumentException("Suhu di luar batas");` |
| Melempar ulang | `throw e;` (di dalam `catch`) | `throw e;` |
| *Exception chaining* | `throw new Baru("pesan", e);` (konstruktornya memanggil `super(pesan, penyebab)`), lalu `e.getCause()` | `throw new TransferGagalException(pesan, e);` |
| Exception sendiri (checked) | `class NamaException extends Exception` | `class KedaiException extends Exception` |
| Exception sendiri (unchecked) | `class NamaException extends RuntimeException` | tidak wajib ditangkap |
| Mengumumkan exception | `... method(...) throws Jenis` | `void tarik(int jumlah) throws SaldoTidakCukupException` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
