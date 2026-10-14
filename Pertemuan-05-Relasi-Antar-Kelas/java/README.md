# ☕ Praktik Java — Pertemuan 05: Relasi Antar Kelas

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 05](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Dependensi: Objek sebagai Parameter](#1-dependensi-objek-sebagai-parameter)
2. [Asosiasi: Field Berisi Objek Lain](#2-asosiasi-field-berisi-objek-lain)
3. [Agregasi dan ArrayList](#3-agregasi-dan-arraylist)
4. [Komposisi: Bagian Dibuat di Dalam](#4-komposisi-bagian-dibuat-di-dalam)
5. [Multiplisitas dan Pencarian yang Bisa Gagal](#5-multiplisitas-dan-pencarian-yang-bisa-gagal)
6. [Mengembalikan Salinan List](#6-mengembalikan-salinan-list)
7. [Objek Saling Mengirim Pesan](#7-objek-saling-mengirim-pesan)
8. [Program Multi-File: Satu Kelas, Satu File](#8-program-multi-file-satu-kelas-satu-file)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh, masing-masing satu file
├── studi-kasus/     <- KedaiKita versi Pertemuan 05 (7 file, satu kelas per file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah **program satu file**, jadi bisa langsung dijalankan seperti biasa:

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/java/contoh
java Contoh01Dependensi.java
```

Cara klasik dua langkah juga tetap bisa dipakai: `javac Contoh01Dependensi.java`, lalu `java Contoh01Dependensi`.

> [!IMPORTANT]
> Studi kasus pertemuan ini **bukan** program satu file. Perintah `java Main.java` tidak bisa dipakai untuknya di JDK 17 dan 21. Cara menjalankannya dibahas di bagian 8.

> [!TIP]
> Jika memakai VS Code, buka folder `java/` **milik pertemuan ini** (File → Open Folder), bukan seluruh repositori. Alasannya, setiap pertemuan punya kelas dengan nama yang sama (misalnya `Menu`), dan VS Code akan protes jika dua kelas bernama sama berada dalam satu proyek. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

> [!NOTE]
> Versi Python pertemuan ini punya contoh 08, yaitu program kecil yang terdiri atas beberapa file. Di Java, program multi-file langsung kita pelajari lewat studi kasus di bagian 8. Perbedaannya dibahas di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 1. Dependensi: Objek sebagai Parameter

File: [`contoh/Contoh01Dependensi.java`](contoh/Contoh01Dependensi.java)

Kita mulai dari hubungan paling longgar. Kelas `Ojek` menyimpan nama pengemudi, plat nomor, dan tarif per km. Method `antar(tujuan, jarakKm)` mencetak siapa yang mengantar, lalu mengembalikan ongkosnya. Yang menarik adalah kelas `Penumpang`:

```java
/** Penumpang yang memesan ojek. Ia TIDAK menyimpan objek Ojek. */
class Penumpang {
    private String nama;
    private int jumlahPerjalanan; // [1] yang diingat hanya angka-angka ini
    private int totalOngkos;
```

Setelah konstruktor dan dua getter (`getJumlahPerjalanan()` dan `getTotalOngkos()`), ada method utamanya:

```java
    public void pesanOjek(Ojek ojek, String tujuan, int jarakKm) { // [2]
        System.out.println(nama + " memesan ojek, jarak " + jarakKm + " km");
        int ongkos = ojek.antar(tujuan, jarakKm); // [3] memakai objek Ojek
        jumlahPerjalanan++;
        totalOngkos += ongkos;
        System.out.println("  Ongkos: Rp" + ongkos);
        // [4] method selesai: parameter ojek dilepas, tidak disimpan di field
    }
```

Program utamanya membuat penumpang Ayu dan dua objek ojek, `ojekRudi` dan `ojekDedi`, lalu:

```java
        System.out.println("=== PERJALANAN 1 ===");
        ayu.pesanOjek(ojekRudi, "Kampus Gunung Kelua", 4); // [5]

        System.out.println();
        System.out.println("=== PERJALANAN 2 ===");
        ayu.pesanOjek(ojekDedi, "Tepian Mahakam", 6); // ojek lain pun bisa
```

**Output:**

```text
=== PERJALANAN 1 ===
Ayu memesan ojek, jarak 4 km
  Pak Rudi (KT 4521 AB) mengantar ke Kampus Gunung Kelua
  Ongkos: Rp10000

=== PERJALANAN 2 ===
Ayu memesan ojek, jarak 6 km
  Bang Dedi (KT 3317 CD) mengantar ke Tepian Mahakam
  Ongkos: Rp15000

=== RINGKASAN ===
Ayu sudah 2 kali naik ojek
Total ongkos: Rp25000
```

Penjelasan:

- **[1]** Field milik `Penumpang` hanya nama, jumlah perjalanan, dan total ongkos. **Tidak ada** field bertipe `Ojek`.
- **[2]** Tipe parameter boleh berupa nama kelas buatan kita sendiri. `Ojek ojek` berarti "parameter bernama `ojek` yang isinya objek kelas `Ojek`".
- **[3]** Di sinilah objek penumpang **mengirim pesan** ke objek ojek: "antar aku, lalu beri tahu ongkosnya".
- **[4]** Begitu method selesai, parameter `ojek` ikut hilang. Penumpang tidak lagi memegang ojek mana pun. Inilah ciri khas **dependensi**.
- **[5]** Setiap perjalanan boleh memakai ojek yang berbeda. Objek ojek bahkan boleh dibuat langsung di dalam pemanggilan, misalnya `ayu.pesanOjek(new Ojek("Mas Eko", "KT 7788 EF", 3000), "Bandara APT Pranoto", 20);`. Objek seperti itu tidak dipegang siapa pun setelah method selesai.

## 2. Asosiasi: Field Berisi Objek Lain

File: [`contoh/Contoh02Asosiasi.java`](contoh/Contoh02Asosiasi.java)

Kelas `DosenWali` di file ini sederhana: field `nama` dan `ruangan`, getter-nya, dan method `pindahRuangan()`. Yang menarik adalah kelas `Mahasiswa`, karena salah satu field-nya bertipe **kelas lain**.

```java
/** Mahasiswa yang mengenal dosen walinya. */
class Mahasiswa {
    private String nama;
    private DosenWali dosenWali; // [1] field bertipe kelas lain

    public Mahasiswa(String nama) {
        this.nama = nama;
        this.dosenWali = null; // awalnya belum ada
    }

    public void aturDosenWali(DosenWali dosen) {
        this.dosenWali = dosen; // [2] menyimpan REFERENSI, bukan salinan
    }

    public String infoPerwalian() {
        if (dosenWali == null) { // [3] periksa dulu sebelum dipakai
            return nama + ": belum punya dosen wali";
        }
        return nama + ": dosen wali " + dosenWali.getNama()
                + ", ruang " + dosenWali.getRuangan(); // [4]
    }
}
```

Program utamanya membuat objek `buRina` (ruang C-201) serta tiga mahasiswa: Ayu, Bima, dan Citra. Hanya Ayu dan Bima yang diberi dosen wali:

```java
        ayu.aturDosenWali(buRina); // [5] dua mahasiswa mengenal objek yang SAMA
        bima.aturDosenWali(buRina);
```

Setelah info perwalian ketiganya dicetak, Bu Rina pindah ruangan:

```java
        buRina.pindahRuangan("D-105"); // [6] diubah di satu tempat saja
        System.out.println(ayu.infoPerwalian());
        System.out.println(bima.infoPerwalian());
```

**Output:**

```text
=== SEBELUM PERWALIAN ===
Ayu: belum punya dosen wali

=== SETELAH PERWALIAN ===
Ayu: dosen wali Bu Rina, ruang C-201
Bima: dosen wali Bu Rina, ruang C-201
Citra: belum punya dosen wali

=== BU RINA PINDAH RUANGAN ===
Ayu: dosen wali Bu Rina, ruang D-105
Bima: dosen wali Bu Rina, ruang D-105
```

Penjelasan:

- **[1]** Tipe field-nya adalah kelas `DosenWali`. Field bertipe kelas yang belum diisi bernilai `null`, artinya "belum menunjuk objek apa pun". Di sini `null` diisi secara tertulis di konstruktor agar maksudnya jelas: multiplisitas `0..1`.
- **[2]** Yang disimpan adalah **referensi** ke objek dosen, bukan salinan datanya. Inilah ciri **asosiasi**.
- **[3]** Sebelum memakai field yang boleh kosong, periksa dulu dengan `== null`. Tanpa pemeriksaan ini, `dosenWali.getNama()` untuk Citra akan menghasilkan `NullPointerException`.
- **[4]** Mahasiswa "berjalan" ke objek dosen untuk membaca nama dan ruangannya. Arahnya satu: mahasiswa tahu dosennya, tetapi dosen tidak menyimpan daftar mahasiswa.
- **[5]** Ayu dan Bima memegang referensi ke objek `buRina` yang **sama**.
- **[6]** Karena objeknya sama, pindah ruangan cukup dilakukan sekali. Ayu dan Bima langsung melihat ruangan yang baru, sedangkan field `dosenWali` milik Citra tetap `null`.

> [!TIP]
> **Coba sendiri:** di akhir `main`, tambahkan `citra.aturDosenWali(new DosenWali("Bu Rina", "D-105"));`, lalu `buRina.pindahRuangan("E-301");`, lalu cetak `ayu.infoPerwalian()` dan `citra.infoPerwalian()`. Apakah ruangan dosen wali Citra ikut berubah?

<details>
<summary>Lihat jawaban</summary>

Tidak. Ayu melihat `ruang E-301`, tetapi Citra tetap `ruang D-105`. Citra dihubungkan ke objek `DosenWali` **baru** yang kebetulan bernama sama. Dua objek dengan data sama tetaplah dua objek berbeda.

</details>

## 3. Agregasi dan ArrayList

File: [`contoh/Contoh03Agregasi.java`](contoh/Contoh03Agregasi.java)

Tim futsal menyimpan **banyak** pemain, dan jumlahnya bisa bertambah. Array biasa tidak cocok, karena ukurannya tetap sejak dibuat. Java menyediakan `ArrayList`, yaitu list yang ukurannya bisa bertambah dan berkurang, mirip `list` di Python.

Untuk memakainya, tulis dua baris `import` di bagian paling atas file:

```java
import java.util.ArrayList;
import java.util.List;
```

Kelas `Pemain` berisi `nama`, `posisi`, getter `getNama()`, dan `toString()`. Kelas `Tim` mengumpulkan pemain-pemain itu:

```java
/** Tim futsal yang mengumpulkan pemain-pemain yang sudah ada. */
class Tim {
    private String nama;
    private List<Pemain> daftarPemain; // [1] "list berisi Pemain"

    public Tim(String nama) {
        this.nama = nama;
        this.daftarPemain = new ArrayList<>(); // list kosong: 0 pemain
    }

    public void rekrut(Pemain pemain) { // [2] menerima OBJEK yang sudah jadi
        daftarPemain.add(pemain);
        System.out.println(pemain.getNama() + " bergabung dengan " + nama);
    }

    public int jumlahPemain() {
        return daftarPemain.size();
    }

    public void tampilkan() {
        System.out.println(nama + " (" + jumlahPemain() + " pemain):");
        for (int i = 0; i < daftarPemain.size(); i++) { // [3] indeks mulai dari 0
            Pemain pemain = daftarPemain.get(i);
            System.out.println("  " + (i + 1) + ". " + pemain);
        }
    }
}
```

Potongan program utamanya:

```java
        Pemain andi = new Pemain("Andi", "kiper"); // [4] pemain lahir lebih dulu, tanpa tim
        Pemain bayu = new Pemain("Bayu", "anchor");
        Pemain candra = new Pemain("Candra", "pivot");
        Tim timKelas = new Tim("Tim Kelas TI-A");
        Tim timFakultas = new Tim("Tim Fakultas");

        System.out.println("=== MEMBENTUK TIM ===");
        timKelas.rekrut(andi);
        timKelas.rekrut(bayu);
        timKelas.rekrut(candra);
        timFakultas.rekrut(bayu); // [5] satu pemain boleh ikut dua tim
```

Setelah kedua tim ditampilkan, tim kelas dibubarkan:

```java
        timKelas = null; // [6] objek tim dilepas, pemain tidak ikut hilang
        System.out.println("Pemain tetap ada: " + andi + ", " + bayu + ", " + candra);
        timFakultas.tampilkan();
```

**Output:**

```text
=== MEMBENTUK TIM ===
Andi bergabung dengan Tim Kelas TI-A
Bayu bergabung dengan Tim Kelas TI-A
Candra bergabung dengan Tim Kelas TI-A
Bayu bergabung dengan Tim Fakultas

Tim Kelas TI-A (3 pemain):
  1. Andi (kiper)
  2. Bayu (anchor)
  3. Candra (pivot)
Tim Fakultas (1 pemain):
  1. Bayu (anchor)

=== TIM KELAS DIBUBARKAN ===
Pemain tetap ada: Andi (kiper), Bayu (anchor), Candra (pivot)
Tim Fakultas (1 pemain):
  1. Bayu (anchor)
```

Penjelasan:

- **[1]** `List<Pemain>` dibaca "list berisi `Pemain`". Tanda `<Pemain>` memberi tahu Java bahwa list ini hanya boleh berisi objek `Pemain`. Objeknya dibuat dengan `new ArrayList<>()`. Tanda `<>` yang kosong boleh dibiarkan kosong, karena Java mengisinya sendiri dari tipe field. Penjelasan lengkap tentang tanda `< >` (*generics*) ada di Pertemuan 12.
- **[2]** Method `rekrut()` menerima **objek** `Pemain` yang sudah jadi, lalu menyimpannya dengan `add()`. Inilah ciri **agregasi**.
- **[3]** `size()` memberi jumlah isi list, dan `get(i)` mengambil isi pada indeks `i`. Seperti array, indeksnya mulai dari 0, jadi nomor urut yang dicetak adalah `i + 1`.
- **[4]** Ketiga pemain sudah ada **sebelum** tim mana pun dibentuk.
- **[5]** Objek `bayu` yang sama tersimpan di dua list sekaligus. Hal ini wajar pada agregasi.
- **[6]** Variabel `timKelas` tidak lagi menunjuk objek tim, dan objek yang tidak dipegang siapa pun akan dibersihkan otomatis oleh Java (*garbage collector*). Para pemain tetap ada, karena masih dipegang variabel `andi`, `bayu`, `candra`, dan list milik `timFakultas`.

Method `ArrayList` yang paling sering dipakai:

| Kebutuhan | Kode | Padanan Python |
|---|---|---|
| Membuat list kosong | `List<Pemain> daftar = new ArrayList<>();` | `daftar = []` |
| Menambah di akhir | `daftar.add(pemain)` | `daftar.append(pemain)` |
| Jumlah isi | `daftar.size()` | `len(daftar)` |
| Mengambil isi ke-`i` | `daftar.get(i)` | `daftar[i]` |
| Membuang objek tertentu | `daftar.remove(pemain)` | `daftar.remove(pemain)` |
| Membaca satu per satu | `for (Pemain p : daftar) { ... }` | `for p in daftar:` |
| Membuat salinan | `new ArrayList<>(daftar)` | `list(daftar)` |

> [!NOTE]
> Tipe field ditulis `List<Pemain>`, sedangkan objeknya `new ArrayList<>()`. `List` adalah "jenis wadah" yang umum, dan `ArrayList` adalah salah satu wujud nyatanya. Untuk sekarang, cukup ikuti pola ini. Alasannya dibahas di Pertemuan 10 dan 12.

## 4. Komposisi: Bagian Dibuat di Dalam

File: [`contoh/Contoh04Komposisi.java`](contoh/Contoh04Komposisi.java)

Kelas `Ruangan` menyimpan nama, panjang, dan lebar, serta punya method `luas()`. Perhatikan **siapa** yang membuat objek `Ruangan`:

```java
/** Rumah yang membuat dan memiliki ruangan-ruangannya sendiri. */
class Rumah {
    private String pemilik;
    private List<Ruangan> daftarRuangan;

    public Rumah(String pemilik) {
        this.pemilik = pemilik;
        this.daftarRuangan = new ArrayList<>();
    }

    public void bangunRuangan(String nama, int panjang, int lebar) { // [1]
        Ruangan ruangan = new Ruangan(nama, panjang, lebar); // [2] dibuat DI DALAM rumah
        daftarRuangan.add(ruangan);
    }

    public int luasTotal() {
        int total = 0;
        for (Ruangan ruangan : daftarRuangan) {
            total += ruangan.luas(); // [3] rumah bertanya ke setiap ruangan
        }
        return total;
    }
```

Program utamanya:

```java
        System.out.println("=== MEMBANGUN RUMAH ===");
        Rumah rumah = new Rumah("Pak Hasan");
        rumah.bangunRuangan("Ruang tamu", 4, 3); // [4] hanya mengirim data
        rumah.bangunRuangan("Kamar tidur", 3, 3);
        rumah.bangunRuangan("Dapur", 3, 2);
        rumah.tampilkan();

        System.out.println();
        System.out.println("=== RUMAH DIROBOHKAN ===");
        rumah = null; // [5] satu-satunya pemegang ruangan dilepas
```

**Output:**

```text
=== MEMBANGUN RUMAH ===
Rumah Pak Hasan:
- Ruang tamu 4x3 m = 12 m2
- Kamar tidur 3x3 m = 9 m2
- Dapur 3x2 m = 6 m2
Luas total: 27 m2

=== RUMAH DIROBOHKAN ===
Rumah dirobohkan. Tidak ada variabel lain yang memegang ruangannya,
jadi ruangan-ruangan itu ikut hilang bersama rumahnya.
```

Penjelasan:

- **[1]** Method `bangunRuangan()` menerima **data** (nama dan ukuran), bukan objek `Ruangan`.
- **[2]** Objek `Ruangan` dibuat dengan `new` **di dalam** method milik rumah, dan hanya rumah yang memegang referensinya. Inilah ciri **komposisi**.
- **[3]** Rumah menghitung luas totalnya dengan bertanya ke setiap ruangan lewat perulangan *for-each*.
- **[4]** Di `main`, tidak ada satu baris pun yang menulis `new Ruangan(...)`. Kode luar tidak pernah memegang objek ruangan.
- **[5]** Begitu rumah dilepas, ruangannya pun tidak dipegang siapa-siapa lagi, sehingga ikut dibersihkan bersama rumahnya.

Bandingkan dengan contoh 03: `timKelas.rekrut(andi)` menerima **objek jadi** yang dibuat di luar (agregasi), sedangkan `rumah.bangunRuangan("Dapur", 3, 2)` menerima **data** dan membuat objeknya sendiri (komposisi).

> [!TIP]
> **Coba sendiri:** mengapa kelas `Rumah` sengaja **tidak** punya method `tambahRuangan(Ruangan ruangan)`? Pikirkan apa yang bisa terjadi jika method itu ada.

<details>
<summary>Lihat jawaban</summary>

Jika ada method yang menerima objek `Ruangan` jadi, kode luar bisa membuat satu ruangan lalu memasukkannya ke **dua** rumah sekaligus. Satu dapur dimiliki dua rumah? Itu melanggar makna komposisi. Dengan hanya menerima data, rumah memastikan setiap ruangannya dibuat sendiri dan tidak dibagi.

</details>

## 5. Multiplisitas dan Pencarian yang Bisa Gagal

File: [`contoh/Contoh05Multiplisitas.java`](contoh/Contoh05Multiplisitas.java)

Sebuah grup belajar punya aturan: **tepat satu** ketua (multiplisitas `1`) dan **minimal satu** anggota (multiplisitas `1..*`). Kelas `Peserta` berisi `nim` dan `nama`. Kelas `GrupBelajar` yang menjaga aturannya:

```java
    public GrupBelajar(String nama, Peserta ketua) {
        if (ketua == null) { // [1] multiplisitas 1: ketua wajib ada
            throw new IllegalArgumentException("Grup wajib punya ketua");
        }
        this.nama = nama;
        this.ketua = ketua;
        this.daftarAnggota = new ArrayList<>();
        this.daftarAnggota.add(ketua); // [2] 1..*: sudah 1 anggota
    }

    public void tambahAnggota(Peserta peserta) {
        daftarAnggota.add(peserta);
    }

    public Peserta cariAnggota(String nim) { // [3]
        for (Peserta peserta : daftarAnggota) {
            if (peserta.getNim().equals(nim)) {
                return peserta;
            }
        }
        return null; // [4] sudah diperiksa semua, tidak ketemu
    }

    public void keluarkan(String nim) {
        Peserta peserta = cariAnggota(nim);
        if (peserta == null) { // [5] periksa null sebelum memakai hasilnya
            System.out.println("Gagal: NIM " + nim + " bukan anggota " + nama);
        } else if (peserta == ketua) { // [6] ketua tidak boleh keluar
            System.out.println("Gagal: " + peserta.getNama()
                    + " adalah ketua, tidak bisa dikeluarkan");
        } else {
            daftarAnggota.remove(peserta);
            System.out.println(peserta.getNama() + " keluar dari " + nama);
        }
    }
```

Program utamanya membuat grup dengan Ayu sebagai ketua, mencoba membuat grup tanpa ketua (`new GrupBelajar("Grup Hantu", null)` di dalam `try`/`catch`), menambah Bima dan Citra, mencari dua NIM, lalu mencoba mengeluarkan tiga orang.

**Output:**

```text
=== GRUP BARU ===
Grup PBO - ketua: Ayu
Anggota (1 orang):
- Ayu (2409106001)

=== GRUP TANPA KETUA ===
Gagal membuat grup: Grup wajib punya ketua

=== MENAMBAH ANGGOTA ===
Grup PBO - ketua: Ayu
Anggota (3 orang):
- Ayu (2409106001)
- Bima (2409106002)
- Citra (2409106003)

=== MENCARI ANGGOTA ===
Cari 2409106002: Bima (2409106002)
Cari 2409106099: tidak ditemukan

=== MENGELUARKAN ANGGOTA ===
Gagal: NIM 2409106099 bukan anggota Grup PBO
Gagal: Ayu adalah ketua, tidak bisa dikeluarkan
Citra keluar dari Grup PBO
Grup PBO - ketua: Ayu
Anggota (2 orang):
- Ayu (2409106001)
- Bima (2409106002)
```

Penjelasan:

- **[1]** Parameter bertipe kelas selalu boleh diisi `null`, dan compiler tidak melarangnya. Karena itu, konstruktor memeriksanya sendiri dan menolak dengan `IllegalArgumentException`, seperti validasi di Pertemuan 04.
- **[2]** List anggota langsung diisi ketua. Sejak lahir, grup sudah punya satu anggota, sehingga aturan `1..*` terpenuhi.
- **[3]** Tipe kembaliannya `Peserta`, tetapi method ini boleh mengembalikan `null`. Komentar dokumentasi atau nama method seperti `cari...` sebaiknya memberi tahu pemanggil tentang kemungkinan itu.
- **[4]** `return null` baru dijalankan setelah perulangan selesai tanpa menemukan NIM yang dicari. Teks dibandingkan dengan `.equals()`, bukan `==`.
- **[5]** Hasil pencarian **selalu** diperiksa dulu dengan `== null` sebelum dipakai.
- **[6]** Pada objek, operator `==` memeriksa apakah dua variabel menunjuk objek yang **sama** (materi Pertemuan 03). Karena ketua tidak boleh keluar, list anggota tidak akan pernah kosong. Method `remove(peserta)` membuang objek itu dari list.

## 6. Mengembalikan Salinan List

File: [`contoh/Contoh06SalinanList.java`](contoh/Contoh06SalinanList.java)

Kelas `GarasiBocor` dan `GarasiAman` hampir identik. Konstruktor, method `parkir()` yang menolak motor saat garasi penuh, dan method `tampilkan()` keduanya sama persis. Bedanya hanya pada getter `getDaftarMotor()`.

Di kelas `GarasiBocor`:

```java
    public List<Motor> getDaftarMotor() {
        return daftarMotor; // [1] list ASLI diserahkan ke luar
    }
```

Di kelas `GarasiAman`:

```java
    public List<Motor> getDaftarMotor() {
        return new ArrayList<>(daftarMotor); // [2] yang diserahkan hanya SALINAN
    }
```

Di `main`, setiap garasi berkapasitas 2 dicoba diisi tiga motor, dan motor ketiga ditolak. Lalu kode luar mencoba menyelinapkan motor ketiga lewat list yang didapat dari getter. Untuk garasi bocor:

```java
        List<Motor> daftar = bocor.getDaftarMotor(); // [3] kode luar memegang list ASLI
        daftar.add(new Motor("KT 3333 CC")); // [4] menyelinap, kapasitas dilewati
```

Untuk garasi aman, caranya sama persis:

```java
        daftar = aman.getDaftarMotor(); // [5] kode luar hanya memegang salinan
        daftar.add(new Motor("KT 3333 CC")); // yang bertambah hanya salinannya
```

**Output:**

```text
=== GARASI BOCOR ===
KT 1111 AA masuk garasi
KT 2222 BB masuk garasi
Ditolak: garasi penuh, KT 3333 CC tidak bisa masuk
Isi garasi (3/2):
- KT 1111 AA
- KT 2222 BB
- KT 3333 CC

=== GARASI AMAN ===
KT 1111 AA masuk garasi
KT 2222 BB masuk garasi
Ditolak: garasi penuh, KT 3333 CC tidak bisa masuk
Isi garasi (2/2):
- KT 1111 AA
- KT 2222 BB
Isi salinan di luar: 3 motor
```

Penjelasan:

- **[1]** Getter ini mengembalikan list yang **sama** dengan yang dipakai garasi di dalam. Field-nya memang `private`, tetapi referensinya diserahkan begitu saja.
- **[2]** `new ArrayList<>(daftarMotor)` membuat **list baru** yang isinya sama. Garasi menyerahkan "fotokopi", bukan aslinya.
- **[3]** Variabel `daftar` kini menunjuk list asli milik garasi bocor.
- **[4]** Menambah ke list itu berarti menambah ke garasi **tanpa lewat** `parkir()`. Hasilnya `3/2`: aturan kapasitas jebol.
- **[5]** Pada garasi aman, yang bertambah hanya salinannya (3 motor). Isi garasi tetap `2/2`.

> [!IMPORTANT]
> `private` saja tidak cukup untuk melindungi list. `private` hanya mencegah kode luar menulis `garasi.daftarMotor`. Jika getter menyerahkan referensi list aslinya, kode luar tetap bisa mengubah isinya. Yang disalin pun hanya **list-nya**: objek `Motor` di dalam salinan tetap objek yang sama.

## 7. Objek Saling Mengirim Pesan

File: [`contoh/Contoh07KirimPesan.java`](contoh/Contoh07KirimPesan.java)

Tiga objek bekerja sama saat Ayu menarik uang tunai. Kelas `Rekening` menyimpan saldo, dan method `tarik(jumlah)`-nya mengembalikan `true` jika berhasil atau `false` jika saldo tidak cukup. Dua kelas lainnya:

```java
/** Kartu ATM yang MENGENAL rekeningnya (asosiasi). */
class KartuAtm {
    private String pin;
    private Rekening rekening; // [1] kartu menyimpan referensi rekening

    public KartuAtm(String pin, Rekening rekening) {
        this.pin = pin;
        this.rekening = rekening;
    }

    public boolean otorisasi(String pin, int jumlah) {
        if (!pin.equals(this.pin)) {
            System.out.println("  [KartuAtm] PIN salah");
            return false;
        }
        System.out.println("  [KartuAtm] PIN cocok, teruskan ke rekening");
        return rekening.tarik(jumlah); // [2] pesan diteruskan ke Rekening
    }
}
```

```java
    public void tarikTunai(KartuAtm kartu, String pin, int jumlah) { // [3]
        System.out.println("[MesinAtm] permintaan tarik Rp" + jumlah);
        if (jumlah > uangTersedia) {
            System.out.println("[MesinAtm] uang di mesin tidak cukup");
            return;
        }
        if (kartu.otorisasi(pin, jumlah)) { // [4] pesan dikirim ke KartuAtm
            uangTersedia -= jumlah;
            System.out.println("[MesinAtm] silakan ambil uang Rp" + jumlah);
        } else {
            System.out.println("[MesinAtm] transaksi dibatalkan");
        }
    }
```

Program utamanya membuat rekening Ayu (saldo 500000), kartunya dengan PIN `"123456"`, dan mesin berisi uang 1000000, lalu mencoba tiga transaksi. Transaksi pertama:

```java
        mesin.tarikTunai(kartuAyu, "123456", 200000); // [5]
```

**Output:**

```text
=== TRANSAKSI 1: BERHASIL ===
[MesinAtm] permintaan tarik Rp200000
  [KartuAtm] PIN cocok, teruskan ke rekening
    [Rekening] saldo Ayu kini Rp300000
[MesinAtm] silakan ambil uang Rp200000

=== TRANSAKSI 2: PIN SALAH ===
[MesinAtm] permintaan tarik Rp100000
  [KartuAtm] PIN salah
[MesinAtm] transaksi dibatalkan

=== TRANSAKSI 3: SALDO TIDAK CUKUP ===
[MesinAtm] permintaan tarik Rp400000
  [KartuAtm] PIN cocok, teruskan ke rekening
    [Rekening] saldo tidak cukup (sisa Rp300000)
[MesinAtm] transaksi dibatalkan

=== SETELAH TRANSAKSI ===
Saldo rekening Ayu: Rp300000
Uang di mesin     : Rp800000
```

Penjelasan:

- **[1]** Kartu menyimpan referensi rekeningnya sebagai field: **asosiasi** dari `KartuAtm` ke `Rekening`.
- **[2]** Kartu tidak mengubah saldo sendiri. Ia **meneruskan pesan** ke rekening, dan rekening yang memutuskan berhasil atau tidak. Perhatikan juga `pin.equals(this.pin)`: `pin` adalah parameter, sedangkan `this.pin` adalah field.
- **[3]** Mesin hanya memakai kartu selama transaksi dan tidak menyimpannya: **dependensi** dari `MesinAtm` ke `KartuAtm`.
- **[4]** Mesin hanya peduli jawaban akhirnya (`true` atau `false`). Ia tidak perlu tahu bagaimana kartu dan rekening bekerja di dalamnya.
- **[5]** Satu pemanggilan dari `main` memicu pesan berantai: mesin ke kartu, lalu kartu ke rekening. Jawabannya kembali dengan urutan terbalik. Indentasi pada output menunjukkan kedalaman rantai itu.

## 8. Program Multi-File: Satu Kelas, Satu File

Sejak Pertemuan 01, program Java kita selalu satu file: kelas `public` yang punya `main` di paling atas, lalu kelas-kelas pembantu tanpa `public` di bawahnya. Studi kasus pertemuan ini dipecah menjadi **tujuh file**:

```text
studi-kasus/
├── Rupiah.java        public class Rupiah       (format uang)
├── Menu.java          public class Menu
├── Pelanggan.java     public class Pelanggan
├── ItemPesanan.java   public class ItemPesanan
├── Pesanan.java       public class Pesanan
├── Kedai.java         public class Kedai
└── Main.java          public class Main         (punya method main)
```

Aturannya sederhana:

1. Setiap kelas `public` berada di file **sendiri**, dan nama filenya **sama persis** dengan nama kelasnya, termasuk huruf besar-kecilnya.
2. File-file di **folder yang sama** tergolong satu paket (*package*), yaitu paket tanpa nama yang kita pakai sejak awal. Kelas-kelas di paket yang sama bisa saling memakai **tanpa `import`**. Itu sebabnya `Main.java` bisa langsung menulis `new Kedai(...)`.
3. `import` tetap dibutuhkan untuk kelas dari pustaka Java di luar `java.lang`, misalnya `java.util.List` dan `java.util.ArrayList`.

Cara menjalankan: masuk ke folder `studi-kasus`, kompilasi semua file, lalu jalankan kelas `Main`.

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/java/studi-kasus
javac *.java
java Main
```

Apa yang terjadi di balik layar?

- `javac *.java` mengompilasi **semua** file `.java` di folder aktif. Tanda `*` berarti "semua". Hasilnya, satu file `.class` untuk setiap kelas, di folder yang sama: `Kedai.class`, `Main.class`, `Menu.class`, dan seterusnya.
- `java Main` menjalankan method `main` milik kelas `Main`. Perhatikan bahwa yang ditulis adalah **nama kelas**, tanpa `.java` dan tanpa `.class`. Kelas lain dimuat otomatis saat dibutuhkan.

> [!IMPORTANT]
> Setiap kali ada file `.java` yang kamu ubah, jalankan `javac *.java` **lagi** sebelum `java Main`. Jika lupa, Java menjalankan file `.class` versi lama, dan perubahanmu seolah-olah tidak berpengaruh.

> [!NOTE]
> File `.class` boleh dihapus kapan saja, karena bisa dibuat ulang dengan `javac`. Repositori ini juga sudah mengatur agar file `.class` tidak ikut tersimpan ke Git. Penjelasan lebih lengkap tentang perintah-perintah ini ada di [panduan menjalankan program](../../00-Persiapan/menjalankan-program.md).

## 9. Studi Kasus KedaiKita

Folder: `studi-kasus/`, berisi [`Rupiah.java`](studi-kasus/Rupiah.java), [`Menu.java`](studi-kasus/Menu.java), [`Pelanggan.java`](studi-kasus/Pelanggan.java), [`ItemPesanan.java`](studi-kasus/ItemPesanan.java), [`Pesanan.java`](studi-kasus/Pesanan.java), [`Kedai.java`](studi-kasus/Kedai.java), dan [`Main.java`](studi-kasus/Main.java).

Saatnya KedaiKita mencatat siapa memesan apa. Rancangan dan alasan pemilihan setiap relasi sudah dibahas di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kedai-pesanan-dan-item).

**Apa yang berubah dibanding Pertemuan 04?**

| Bagian | Pertemuan 04 | Pertemuan 05 |
|---|---|---|
| Susunan file | satu file `KedaiKita.java` (`java KedaiKita.java`) | tujuh file (`javac *.java`, lalu `java Main`) |
| Kelas `Rupiah`, `Menu`, `Pelanggan` | kelas pembantu tanpa `public` | masing-masing `public class` di file sendiri, isinya hampir sama |
| Penghitung menu | `private static int jumlahMenu` + `Menu.getJumlahMenu()` | dihapus; diganti `kedai.jumlahMenu()` |
| Konstruktor `Menu` tanpa stok | ada (memakai `this(..., 0)`) | dihapus, karena tidak dipakai lagi |
| `setHarga()` | `public void setHarga(int harga)` | `public final void setHarga(int harga)` |
| Pesanan | belum ada | kelas baru `ItemPesanan` dan `Pesanan` |
| Daftar menu | variabel lepas di `main` | disimpan dan dikelola objek `Kedai` |

**Kenapa `setHarga()` diberi `final`?** Kata kunci `final` pada method berarti method itu **tidak boleh di-*override*** (ditimpa) oleh kelas anak. Konstruktor `Menu` memanggil `setHarga()`, jadi method itu harus dijamin selalu bekerja seperti yang kita tulis. Tanpa `final`, JDK 21 ke atas yang dijalankan dengan `javac -Xlint` memperingatkan `possible 'this' escape before subclass is fully initialized`. Detailnya di Pertemuan 07, saat kita belajar pewarisan.

**Kelas `ItemPesanan`** mewakili satu baris pesanan:

```java
/** Satu baris pesanan: menu apa dan berapa porsi. */
public class ItemPesanan {
    private Menu menu;
    private int jumlah;

    public ItemPesanan(Menu menu, int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah harus lebih dari 0");
        }
        this.menu = menu; // menyimpan REFERENSI ke objek Menu
        this.jumlah = jumlah;
    }
```

- Field `menu` menyimpan **referensi** ke objek `Menu`: asosiasi dari `ItemPesanan` ke `Menu`.
- Selain getter, ada `hitungSubtotal()` yang mengembalikan `menu.getHarga() * jumlah`. Harga ditanyakan ke menunya **saat itu juga**, bukan disalin. Ada juga `toString()` yang menghasilkan teks seperti `2 x Kopi Susu Gula Aren`.

**Kelas `Pesanan`** memegang pelanggan pemiliknya dan daftar item:

```java
/** Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan. */
public class Pesanan {
    private static final int LEBAR_STRUK = 40;
    private static int nomorTerakhir = 0; // atribut static untuk membuat nomor otomatis

    private String nomor;
    private Pelanggan pelanggan;
    private List<ItemPesanan> daftarItem;

    public Pesanan(Pelanggan pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir); // P001, P002, ...
        this.pelanggan = pelanggan;
        this.daftarItem = new ArrayList<>();
    }
```

Setelah getter `getNomor()` dan `getPelanggan()`, ada tiga method penting:

```java
    /** Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<ItemPesanan> getDaftarItem() {
        return new ArrayList<>(daftarItem);
    }

    public void tambahItem(Menu menu, int jumlah) {
        ItemPesanan item = new ItemPesanan(menu, jumlah); // objek item dibuat OLEH pesanan
        menu.kurangiStok(jumlah); // gagal (IllegalArgumentException) jika stok kurang
        daftarItem.add(item);
    }

    public int hitungTotal() {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }
```

- `LEBAR_STRUK` adalah **konstanta**: `static` (milik kelas) dan `final` (tidak bisa diubah). Penamaannya memakai huruf besar semua.
- `String.format("P%03d", nomorTerakhir)` menulis angka selebar 3 digit dengan nol di depan: `P001`, `P002`, dan seterusnya.
- Field `pelanggan` menyimpan referensi pelanggan: asosiasi dengan multiplisitas `1`, karena pelanggan wajib diberikan saat pesanan dibuat.
- `getDaftarItem()` mengembalikan **salinan**, persis seperti garasi aman di contoh 06.
- `tambahItem()` menerima menu dan jumlah, lalu membuat objek `ItemPesanan` sendiri dengan `new`: **komposisi**. Urutannya penting: item dibuat dulu (jumlah divalidasi), lalu stok dikurangi, baru item dimasukkan ke list. Jika `kurangiStok()` melempar exception, baris `add` tidak pernah dijalankan, sehingga item yang gagal tidak masuk ke pesanan.
- `hitungTotal()` bertanya ke setiap item, dan setiap item bertanya ke menunya: `Pesanan -> ItemPesanan -> Menu`.

Method `cetakStruk()` membuat garis dengan `"=".repeat(LEBAR_STRUK)` (tersedia sejak Java 11), lalu mencetak setiap item dengan `String.format("%-30s%10s", item.toString(), subtotal)`. Format `%-30s` berarti "teks rata kiri selebar 30 karakter", dan `%10s` berarti "teks rata kanan selebar 10 karakter", sehingga kolom subtotal selalu lurus.

**Kelas `Kedai`** punya tiga field: `nama`, `List<Menu> daftarMenu`, dan `List<Pesanan> daftarPesanan`. Konstruktornya mengisi kedua list dengan `new ArrayList<>()`. Method-method utamanya:

```java
    public void tambahMenu(Menu menu) {
        daftarMenu.add(menu);
    }

    /** Mengembalikan objek Menu dengan kode tertentu, atau null jika tidak ada. */
    public Menu cariMenu(String kode) {
        for (Menu menu : daftarMenu) {
            if (menu.getKode().equals(kode)) {
                return menu;
            }
        }
        return null;
    }

    public int jumlahMenu() {
        return daftarMenu.size();
    }

    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = new Pesanan(pelanggan);
        daftarPesanan.add(pesanan);
        return pesanan;
    }
```

- `tambahMenu(menu)` menerima objek menu yang dibuat di luar: **agregasi**.
- `cariMenu()` mengembalikan objek `Menu` atau `null`, sama polanya dengan `cariAnggota()` di contoh 05. Kode menu dibandingkan dengan `.equals()`.
- `jumlahMenu()` menggantikan penghitung `static` milik kelas `Menu` dari Pertemuan 04.
- `buatPesanan()` membuat pesanan, mencatatnya, lalu **mengembalikannya** ke pemanggil agar bisa diisi. Parameter `pelanggan` hanya diteruskan, tidak disimpan oleh kedai: **dependensi**.
- Sisanya, `jumlahPesanan()` dan `tampilkanMenu()`, bentuknya sederhana.

**Kelas `Main`** berisi method `static` bernama `siapkanKedai()` yang membuat kedai beserta lima menunya, lalu method `main`. Berikut potongan pesanan Siti, termasuk item yang gagal:

```java
        Pesanan pesananSiti = kedai.buatPesanan(siti);
        pesananSiti.tambahItem(kedai.cariMenu("M02"), 2);
        pesananSiti.tambahItem(kedai.cariMenu("M05"), 1);
        try {
            pesananSiti.tambahItem(kedai.cariMenu("M04"), 20);
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal menambah item: " + e.getMessage());
        }
        pesananSiti.cetakStruk();
```

- Exception yang dilempar `kurangiStok()` di kelas `Menu` "naik" melewati `tambahItem()` di kelas `Pesanan`, lalu ditangkap oleh `catch` di `main`.
- Hasil `cariMenu("M02")` di sini langsung dipakai, karena kode `M01` sampai `M05` pasti ada. Untuk kode yang datang dari luar program, selalu periksa `null` dulu, seperti di bagian `=== MENCARI MENU ===` pada file yang sama.
- Bagian pencarian itu membaca kode-kode dari `List.of("M02", "M99")`, yaitu list kecil berisi data tetap yang tidak bisa diubah, cocok untuk daftar yang hanya dibaca.

Cara menjalankan (masuk dulu ke folder `studi-kasus`):

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/java/studi-kasus
javac *.java
java Main
```

Bagian awal output, yaitu daftar menu dan struk Budi, sama persis dengan yang tercantum di [halaman konsep](../README.md#12-studi-kasus-kedaikita-kedai-pesanan-dan-item). Lanjutannya:

**Output:**

```text
Gagal menambah item: Stok Mie Goreng Jawa tidak cukup (sisa 10)
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================

=== MENCARI MENU ===
Cari M02: [M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28
Cari M99: tidak ditemukan

=== SETELAH TRANSAKSI ===
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11
Jumlah pesanan tercatat: 2
```

Stok di menu milik kedai ikut berkurang, karena objek `Menu` yang dikurangi stoknya oleh `tambahItem()` adalah objek yang **sama** dengan yang tersimpan di daftar menu kedai. `cariMenu()` mengembalikan referensinya, bukan salinannya.

> [!TIP]
> **Coba sendiri:** tepat setelah `pesananBudi.cetakStruk();`, tambahkan tiga baris ini: `System.out.println(pesananBudi.getDaftarItem().size());`, lalu `pesananBudi.getDaftarItem().clear();`, lalu baris `println` yang sama sekali lagi. Kompilasi ulang dan jalankan. Angka berapa saja yang tercetak, dan mengapa?

<details>
<summary>Lihat jawaban</summary>

Tercetak `2`, lalu `2` lagi. Setiap kali `getDaftarItem()` dipanggil, method itu membuat **salinan baru**. Perintah `clear()` hanya mengosongkan salinan yang langsung dibuang, sedangkan list asli di dalam pesanan tetap berisi dua item.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Ingat dua jenis kesalahan di Java: **error saat kompilasi** (diawali nama file dan nomor baris, dengan tanda `^` di bawah posisi kesalahan) dan **error saat program berjalan** (diawali `Exception in thread "main"`). Pertemuan ini menambah jenis ketiga: kesalahan saat **menjalankan perintah** di folder yang salah.

### Kesalahan 1: Menjalankan studi kasus dengan `java Main.java`

Karena terbiasa dengan program satu file, kamu mengetik `java Main.java` di folder `studi-kasus`. Di JDK 17 dan 21, hasilnya:

```text
Main.java:24: error: cannot find symbol
    public static Kedai siapkanKedai() {
                  ^
  symbol:   class Kedai
  location: class Main
Main.java:25: error: cannot find symbol
        Kedai kedai = new Kedai("KedaiKita");
        ^
  symbol:   class Kedai
  location: class Main
...
16 errors
error: compilation failed
```

**Artinya:** perintah `java NamaFile.java` hanya mengompilasi **satu** file itu. Kelas `Kedai`, `Menu`, dan lainnya yang berada di file lain tidak ikut dikompilasi, sehingga tidak dikenal (*cannot find symbol*). **Perbaikan:** pakai `javac *.java`, lalu `java Main`. Sejak JDK 22, perintah `java Main.java` sebenarnya bisa mencari file lain di folder yang sama. Namun, cara `javac` berlaku di semua versi yang kita pakai.

### Kesalahan 2: Menjalankan dari folder yang salah

Misalkan terminalmu masih berada di folder `java/`, bukan di `java/studi-kasus/`. Perintah `javac *.java` gagal karena di folder itu tidak ada file `.java`:

```text
error: file not found: *.java
Usage: javac <options> <source files>
use --help for a list of possible options
```

Jika kamu sudah mengompilasi di folder `studi-kasus`, lalu pindah folder dan mengetik `java Main`, hasilnya:

```text
Error: Could not find or load main class Main
Caused by: java.lang.ClassNotFoundException: Main
```

**Artinya:** `java Main` mencari file `Main.class` di folder aktif, dan file itu tidak ada di sana. **Perbaikan:** masuk ke folder yang benar dengan `cd studi-kasus`, lalu ulangi kedua perintahnya. Pesan yang sama muncul jika kamu mengetik `java Main.class`, yaitu `Could not find or load main class Main.class`. Ingat, `java` menerima **nama kelas**, bukan nama file `.class`.

### Kesalahan 3: Lupa `import` untuk `List` atau `ArrayList`

Misalkan file `Rak.java` hanya berisi `import java.util.ArrayList;`, padahal field-nya bertipe `List<String>`:

```text
Rak.java:4: error: cannot find symbol
    private List<String> daftarBuku = new ArrayList<>();
            ^
  symbol:   class List
  location: class Rak
1 error
```

**Artinya:** compiler tidak mengenal kelas `List` (*symbol: class List*), karena kelas itu berada di paket `java.util` dan belum di-import. **Perbaikan:** tambahkan `import java.util.List;` di bagian atas file. Kelas di paket `java.lang`, seperti `String` dan `System`, tidak perlu di-import.

### Kesalahan 4: Memperlakukan `List` seperti array

Programmer yang terbiasa dengan array (atau dengan Python) sering menulis `daftarBuku[0]`:

```text
Rak.java:8: error: array required, but List<String> found
        return daftarBuku[0];
                         ^
1 error
```

**Artinya:** kurung siku `[ ]` hanya untuk array, sedangkan `daftarBuku` adalah `List`. Hal serupa terjadi pada `daftarBuku.length`, yang ditolak dengan `cannot find symbol` (*symbol: variable length*). **Perbaikan:** pakai `daftarBuku.get(0)` dan `daftarBuku.size()`.

Satu lagi: isi `< >` harus berupa **kelas**, bukan tipe primitif. Menulis `List<int>` ditolak dengan `error: unexpected type`, `required: reference`, `found: int`. Untuk menyimpan angka di list, Java memakai kelas pembungkus `Integer`, misalnya `List<Integer>`. Detailnya di Pertemuan 12.

### Kesalahan 5: Memakai hasil pencarian tanpa memeriksa `null`

Buat file `Coba.java` di folder `studi-kasus` berisi kode berikut, lalu jalankan `javac *.java` dan `java Coba`:

```java
public class Coba {
    public static void main(String[] args) {
        Kedai kedai = Main.siapkanKedai();
        Pesanan pesanan = kedai.buatPesanan(new Pelanggan("Budi Santoso", "081234567890"));
        pesanan.tambahItem(kedai.cariMenu("M10"), 1);
    }
}
```

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "Menu.kurangiStok(int)" because "<parameter1>" is null
	at Pesanan.tambahItem(Pesanan.java:46)
	at Coba.main(Coba.java:5)
```

**Artinya:** menu `M10` tidak ada, sehingga `cariMenu()` mengembalikan `null`, dan `null` itu dikirim ke `tambahItem()`. Di baris 46 `Pesanan.java`, Java mencoba menjalankan `kurangiStok()` milik `null`. Bagian `"<parameter1>"` adalah parameter pertama method itu, yaitu `menu`. Java menuliskannya seperti itu karena nama parameter tidak ikut disimpan saat kompilasi biasa. Baca baris `at ...` dari atas: error terjadi di `Pesanan.tambahItem`, yang dipanggil dari `Coba.main` baris 5. **Perbaikan:** simpan dulu hasil pencarian ke variabel, periksa dengan `if (menu == null)`, lalu panggil `tambahItem()` hanya jika menunya ada. Hapus lagi `Coba.java` dan file `.class`-nya setelah selesai.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK dan antarsistem operasi, terutama pesan `javac *.java` di Windows. Fokuslah pada kata kuncinya: `cannot find symbol`, `Could not find or load main class`, `array required`, dan `NullPointerException`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Dependensi | objek sebagai parameter, tidak disimpan | `public void pesanOjek(Ojek ojek, ...)` |
| Asosiasi | field bertipe kelas lain | `private DosenWali dosenWali;` |
| Field boleh kosong (`0..1`) | awalnya `null` | `this.dosenWali = null;` |
| Import list | `import java.util.ArrayList;` dan `import java.util.List;` | di baris paling atas file |
| Field list | `private List<Tipe> nama;` | `private List<Pemain> daftarPemain;` |
| Membuat list kosong | `new ArrayList<>()` | `daftarPemain = new ArrayList<>();` |
| Agregasi | `add` objek dari luar | `daftarPemain.add(pemain);` |
| Komposisi | objek bagian dibuat dengan `new` di dalam | `new Ruangan(nama, panjang, lebar)` |
| Jumlah dan isi ke-`i` | `size()` dan `get(i)` | `daftarPemain.get(0)` |
| Pencarian yang bisa gagal | `return null;` | `public Menu cariMenu(String kode)` |
| Memeriksa hasil kosong | `== null` / `!= null` | `if (menu == null)` |
| Objek yang sama? | `a == b` | `peserta == ketua` |
| Teks yang sama? | `a.equals(b)` | `menu.getKode().equals(kode)` |
| Salinan list | `new ArrayList<>(lama)` | `return new ArrayList<>(daftarItem);` |
| Konstanta | `static final` | `private static final int LEBAR_STRUK = 40;` |
| Method tidak bisa di-override | `final` | `public final void setHarga(int harga)` |
| Menjalankan program multi-file | `javac *.java`, lalu `java NamaKelas` | `javac *.java` lalu `java Main` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
