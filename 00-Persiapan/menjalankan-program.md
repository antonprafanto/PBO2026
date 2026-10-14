# Menjalankan Program

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Mengatasi Masalah ➡️](mengatasi-masalah.md)

> Tombol ▷ di editor memang praktis, tetapi pemrogram sejati juga akrab dengan **terminal**. Di halaman ini kamu belajar dasar terminal, lalu cara menjalankan program Python dan Java dalam berbagai bentuk yang akan kamu temui sepanjang semester. Pastikan materi sudah ada di laptopmu ([Git dan GitHub](git-dan-github.md)) agar semua contoh bisa langsung dicoba.

## Daftar Isi

1. [Apa Itu Terminal?](#1-apa-itu-terminal)
2. [Membuka Terminal](#2-membuka-terminal)
3. [Perintah Dasar Terminal](#3-perintah-dasar-terminal)
4. [Berpindah ke Folder Materi](#4-berpindah-ke-folder-materi)
5. [Menjalankan Program Python](#5-menjalankan-program-python)
6. [Menjalankan Program Java](#6-menjalankan-program-java)
7. [Ke Mana Perginya *File* `.class`?](#7-ke-mana-perginya-file-class)
8. [Membaca Hasil dan Pesan *Error*](#8-membaca-hasil-dan-pesan-error)

---

## 1. Apa Itu Terminal?

**Terminal** adalah jendela tempat kita memberi perintah ke komputer dengan **mengetik**, bukan dengan mengklik. Bayangkan kamu memesan di kedai: alih-alih menunjuk gambar menu, kamu langsung menyebutkan pesananmu ke kasir dengan kalimat yang jelas.

Di terminal, kamu selalu "berdiri" di sebuah folder yang disebut **folder aktif**. Perintah seperti `python kedaikita.py` mencari *file* `kedaikita.py` **di folder aktif itu**. Karena itu, kemampuan paling penting di terminal adalah **berpindah ke folder yang benar**.

Aplikasi terminal yang dipakai di materi ini: **PowerShell** atau **Command Prompt** di Windows, aplikasi **Terminal** di macOS dan Linux, atau **terminal di dalam VS Code**. Semua perintah di halaman praktik bisa diketik di salah satunya, **bukan** di dalam *file* kode.

## 2. Membuka Terminal

| Sistem | Cara membuka terminal |
|---|---|
| Windows | Klik **Start**, ketik `PowerShell` atau `Terminal`, lalu tekan Enter. Command Prompt (`cmd`) juga bisa dipakai. |
| macOS | Tekan Cmd+Spasi, ketik `Terminal`, lalu tekan Enter. |
| Linux | Biasanya Ctrl+Alt+T, atau cari aplikasi **Terminal**. |
| VS Code | Menu **Terminal → New Terminal** atau Ctrl+\`. |

Terminal yang dibuka dengan cara di atas dimulai di folder tertentu (lihat [bagian 4.2](#42-di-mana-terminal-mulai-berada)). Agar tidak perlu berpindah folder jauh-jauh, kamu bisa langsung membuka terminal **di folder yang dituju**:

- **VS Code:** di panel **Explorer**, klik kanan folder tujuan, lalu pilih **Open in Integrated Terminal**.
- **Windows 11:** buka folder itu di File Explorer, klik kanan di area kosong, lalu pilih **Open in Terminal**.
- **Windows 10:** buka folder itu di File Explorer, tahan Shift sambil klik kanan di area kosong, lalu pilih **Open PowerShell window here**. Cara lain (juga berlaku di Windows 11): klik bilah alamat File Explorer, ketik `powershell`, lalu tekan Enter.
- **macOS:** di Terminal, ketik `cd` diikuti satu spasi, **seret folder** dari Finder ke jendela Terminal, lalu tekan Enter. Alamat lengkap folder itu terisi otomatis.
- **Linux:** di pengelola *file*, klik kanan di dalam folder itu, lalu pilih **Open in Terminal** (namanya bisa sedikit berbeda).

## 3. Perintah Dasar Terminal

| Tujuan | Windows (PowerShell) | Windows (Command Prompt) | macOS / Linux |
|---|---|---|---|
| Melihat folder aktif | `pwd` | `cd` | `pwd` |
| Melihat isi folder | `dir` atau `ls` | `dir` | `ls` |
| Masuk ke subfolder | `cd nama_folder` | `cd nama_folder` | `cd nama_folder` |
| Naik satu folder | `cd ..` | `cd ..` | `cd ..` |
| Membersihkan layar | `cls` atau `clear` | `cls` | `clear` |
| Menghentikan program yang macet | Ctrl+C | Ctrl+C | Ctrl+C |

Tiga trik yang akan sangat menghemat waktumu:

1. **Tombol Tab untuk melengkapi nama.** Ketik `cd Pert`, lalu tekan Tab. Terminal melengkapi nama foldernya. Tekan Tab berkali-kali untuk melihat pilihan lain.
2. **Panah atas untuk mengulang perintah.** Tidak perlu mengetik ulang `python main.py`. Cukup tekan panah atas, lalu Enter.
3. **Tanda kutip untuk nama yang mengandung spasi.** Contohnya `cd "Tugas Kuliah"`. Tanpa tanda kutip, terminal menganggap `Tugas` dan `Kuliah` sebagai dua hal berbeda.

## 4. Berpindah ke Folder Materi

Perintah `python kedaikita.py` hanya berhasil jika terminal sedang berada di folder tempat *file* itu disimpan. Jadi, sebelum menjalankan program, pastikan dua hal: kamu tahu letak **folder utama materi**, dan kamu tahu **di mana terminalmu sedang berada**.

### 4.1 Folder utama materi

**Folder utama materi** adalah folder hasil unduhan di [Git dan GitHub](git-dan-github.md): `PBO2026` jika kamu memakai `git clone`, atau `PBO2026-master` jika mengunduh ZIP. Cirinya, folder itu **langsung** berisi folder `00-Persiapan`, folder-folder `Pertemuan-...`, dan *file* `README.md`:

```text
Documents/
└── PBO2026/                            <- folder utama materi
    ├── 00-Persiapan/
    ├── Pertemuan-01-Pengenalan-PBO/
    ├── Pertemuan-02-Kelas-dan-Objek/
    │   ├── python/
    │   │   ├── contoh/
    │   │   ├── studi-kasus/
    │   │   └── solusi/
    │   └── java/
    ├── ...
    └── README.md
```

Jika nama foldermu sedikit berbeda, tidak apa-apa. Yang penting, isinya seperti di atas.

### 4.2 Di mana terminal mulai berada?

| Cara membuka terminal | Folder aktif saat terminal terbuka |
|---|---|
| Dari menu **Start**, Spotlight, atau Ctrl+Alt+T | folder pribadimu (*home*), misalnya `C:\Users\Budi`, `/Users/budi`, atau `/home/budi` |
| **Open in Terminal** dari File Explorer atau pengelola *file* | folder yang sedang kamu buka di sana |
| Terminal VS Code (**Terminal → New Terminal**) | folder yang dibuka di VS Code, misalnya `Pertemuan-02-Kelas-dan-Objek/python` |
| **Open in Integrated Terminal** di panel **Explorer** VS Code | folder yang kamu klik kanan |

Untuk memeriksa folder aktif kapan saja, ketik `pwd` (PowerShell, macOS, Linux) atau `cd` (Command Prompt), lalu tekan Enter. Di PowerShell dan Command Prompt, alamat folder aktif juga terlihat di depan kursor, misalnya `PS C:\Users\Budi>`.

### 4.3 Membaca perintah `cd` di halaman praktik

Semua perintah `cd` di halaman praktik ditulis **dari folder utama materi**. Contohnya, untuk menjalankan contoh pertama Python Pertemuan 02:

```bash
cd Pertemuan-02-Kelas-dan-Objek/python/contoh
python contoh01_kelas_dan_objek.py
```

Sesuaikan baris `cd`-nya dengan posisi terminalmu:

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-02-Kelas-dan-Objek/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah membuka folder itu) | `cd contoh` |
| folder `contoh` itu sendiri (misalnya lewat **Open in Integrated Terminal**) | tidak perlu `cd`; lewati baris `cd`-nya |
| folder pribadimu (*home*) | lihat [bagian 4.4](#44-dari-folder-pribadi-ke-folder-materi) |

Setelah itu, ketik baris kedua (di macOS/Linux: `python3 contoh01_kelas_dan_objek.py`). Jika berhasil, baris pertama yang muncul adalah `=== DUA OBJEK DARI SATU KELAS ===`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder tujuan (misalnya `contoh`), lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

### 4.4 Dari folder pribadi ke folder materi

Terminal yang dibuka dari menu **Start**, Spotlight, atau Ctrl+Alt+T dimulai di folder pribadimu. Jika materi kamu simpan di **Documents**, masuk ke folder contoh Python Pertemuan 02 dengan perintah berikut.

**Windows (PowerShell atau Command Prompt):**

```bash
cd Documents\PBO2026\Pertemuan-02-Kelas-dan-Objek\python\contoh
```

**macOS / Linux (Terminal):**

```bash
cd ~/Documents/PBO2026/Pertemuan-02-Kelas-dan-Objek/python/contoh
```

Ganti `PBO2026` dengan `PBO2026-master` jika kamu mengunduh ZIP. Lalu periksa isinya dengan `dir` (Windows) atau `ls` (macOS/Linux). Jika nama *file* yang ingin dijalankan terlihat di daftar, kamu sudah berada di tempat yang benar.

> [!NOTE]
> Di Windows, pemisah folder yang asli adalah `\`. PowerShell juga menerima `/` sehingga perintah seperti `cd Pertemuan-02-Kelas-dan-Objek/python/contoh` di halaman praktik tetap berjalan. Jika di Command Prompt perintah dengan `/` bermasalah, ganti dengan `\`. Jika `cd Documents` gagal di Windows, buka saja folder materi di File Explorer, lalu pakai **Open in Terminal** (bagian 2).

## 5. Menjalankan Program Python

### 5.1 Program satu *file*

Semua *file* di folder `contoh/` dan `solusi/`, serta studi kasus Pertemuan 01—04, adalah program satu *file*. Dari folder tempat *file* itu berada, ketik:

```bash
python nama_file.py
```

Di macOS/Linux, ketik `python3 nama_file.py`. Di Windows, `py nama_file.py` juga bisa dipakai. Contoh lengkapnya ada di [bagian 4.3](#43-membaca-perintah-cd-di-halaman-praktik).

### 5.2 Program banyak *file* (mulai Pertemuan 05)

Mulai Pertemuan 05, studi kasus KedaiKita terdiri atas beberapa *file* yang saling memakai lewat `import`. Masuk dulu ke folder `studi-kasus`, lalu jalankan `main.py`. Dari folder utama materi:

```bash
cd Pertemuan-05-Relasi-Antarkelas/python/studi-kasus
python main.py
```

Jika berhasil, baris pertama yang muncul adalah `=== MENU KedaiKita ===`.

> [!IMPORTANT]
> Jalankan `main.py`, bukan *file* lain seperti `menu.py` atau `pesanan.py`. *File-file* itu hanya berisi kelas yang dipakai oleh `main.py` sehingga jika dijalankan sendiri biasanya tidak menampilkan apa-apa.

### 5.3 Proyek ber-*package* (Pertemuan 15)

Di Pertemuan 15, semua kelas KedaiKita berada di dalam *package* `kedaikita/`. Dari folder utama materi, masuk dulu ke folder `studi-kasus`:

```bash
cd Pertemuan-15-Proyek-Terintegrasi/python/studi-kasus
```

Lalu pilih salah satu perintah berikut:

| Perintah | Artinya |
|---|---|
| `python main.py --demo` | mode demo: berjalan sendiri tanpa perlu mengetik apa pun |
| `python main.py` | mode interaktif: kamu menjadi kasir dan mengetik pilihan menu; pilih `0` untuk menyimpan dan keluar |
| `python -m unittest discover -s tests -v` | menjalankan semua *unit test* di folder `tests/` |

## 6. Menjalankan Program Java

Program Java harus **dikompilasi** dulu menjadi *bytecode* (*file* `.class`), baru kemudian **dijalankan** oleh JVM (*Java Virtual Machine*). Ada beberapa cara melakukannya.

### 6.1 Satu *file*, cara cepat: `java NamaFile.java`

Sejak Java 11, program satu *file* bisa langsung dijalankan. Java mengompilasinya di memori, lalu langsung menjalankannya. Dari folder tempat *file* itu berada (misalnya `Pertemuan-02-Kelas-dan-Objek/java/contoh`), ketik:

```bash
java NamaFile.java
```

Cara ini dipakai untuk semua *file* di folder `contoh/` dan `solusi/`, serta studi kasus Pertemuan 01—04. Misalnya, `java Contoh01KelasDanObjek.java` di folder `contoh` Pertemuan 02 menampilkan baris pertama `=== DUA OBJEK DARI SATU KELAS ===`.

> [!IMPORTANT]
> Dengan cara ini, kelas yang memiliki *method* `main` harus ditulis **paling atas** di dalam *file*. Pada Java 11 sampai 21, kelas pertama di dalam *file* **wajib** punya `main`. Mulai Java 22, kelas ber-`main` boleh berada di bawah asalkan namanya sama dengan nama *file*. Agar aman di semua versi, selalu taruh kelas ber-`main` paling atas, seperti semua contoh di materi ini.

Jika aturan itu dilanggar (Java 11 sampai 21), pesan *error*-nya kira-kira seperti ini, dengan `Kucing` sebagai kelas pertama di *file*:

```text
error: can't find main(String[]) method in class: Kucing
```

### 6.2 Satu *file*, cara klasik: `javac` lalu `java`

Cara klasik terdiri atas dua langkah: kompilasi dengan `javac`, lalu jalankan dengan `java`. Contohnya, dari folder `Pertemuan-02-Kelas-dan-Objek/java/studi-kasus`:

```bash
javac KedaiKita.java
java KedaiKita
```

Perintah pertama tidak menampilkan apa-apa jika kodenya benar. Perintah kedua menampilkan menu KedaiKita, diawali baris `=== MENU KEDAIKITA ===`.

- Langkah pertama menghasilkan *file* `.class` untuk **setiap kelas** di dalam *file*. Misalnya, `KedaiKita.java` di Pertemuan 02 menghasilkan `KedaiKita.class` dan `Menu.class`.
- Langkah kedua ditulis **tanpa** akhiran `.java` maupun `.class`. Yang ditulis adalah **nama kelas** yang punya `main`.

> [!WARNING]
> Setiap kali kodenya diubah, kamu harus menjalankan `javac` **lagi**. Jika lupa, `java` akan menjalankan *file* `.class` versi lama, dan kamu akan bingung kenapa perubahanmu "tidak berpengaruh".

### 6.3 Banyak *file* (mulai Pertemuan 05): `javac *.java` lalu `java Main`

Mulai Pertemuan 05, setiap kelas KedaiKita punya *file* sendiri (`Menu.java`, `Pesanan.java`, `Kedai.java`, dan seterusnya), dan program utamanya ada di `Main.java`. Masuk ke folder `studi-kasus`, lalu kompilasi dan jalankan. Dari folder utama materi:

```bash
cd Pertemuan-05-Relasi-Antarkelas/java/studi-kasus
javac *.java
java Main
```

Jika berhasil, baris pertama yang muncul adalah `=== MENU KedaiKita ===`, sama persis dengan versi Python. Tanda `*` berarti "semua". Jadi, `javac *.java` mengompilasi **semua** *file* berakhiran `.java` di folder itu sekaligus. Perintah ini berjalan di Command Prompt, PowerShell, macOS, maupun Linux.

> [!TIP]
> Ingin folder tetap bersih dari *file* `.class`? Simpan hasil kompilasi di folder terpisah bernama `out`:
>
> ```bash
> javac -d out *.java
> java -cp out Main
> ```
>
> Opsi `-d out` artinya "simpan hasil kompilasi di folder `out`", dan `-cp out` artinya "cari kelas di folder `out`".

> [!NOTE]
> Sejak Java 22, perintah `java Main.java` juga bisa menjalankan program yang terdiri atas banyak *file*. Namun, materi ini memakai `javac *.java` lalu `java Main` karena cara itu berlaku di semua versi yang kita pakai (17, 21, dan 25).

### 6.4 Proyek ber-*package* (Pertemuan 15)

Di Pertemuan 15, kode Java berada di dalam *package* `kedaikita` (folder `src/kedaikita/`). Perintahnya lebih panjang, jadi disediakan skrip agar kamu cukup mengetik satu perintah. Dari folder utama materi, masuk dulu ke folder `studi-kasus`:

```bash
cd Pertemuan-15-Proyek-Terintegrasi/java/studi-kasus
```

Lalu ketik perintah yang sesuai dengan terminalmu:

| Tujuan | Windows (Command Prompt) | Windows (PowerShell) | macOS / Linux |
|---|---|---|---|
| Mode demo | `jalankan.bat --demo` | `.\jalankan.bat --demo` | `bash jalankan.sh --demo` |
| Mode interaktif | `jalankan.bat` | `.\jalankan.bat` | `bash jalankan.sh` |
| Menjalankan pengujian | `uji.bat` | `.\uji.bat` | `bash uji.sh` |

PowerShell tidak menjalankan *file* dari folder aktif tanpa awalan `.\`. Itu sebabnya di PowerShell kamu harus mengetik `.\jalankan.bat`, bukan `jalankan.bat`. Bentuk `.\jalankan.bat` juga berjalan di Command Prompt sehingga pengguna Windows cukup mengingat bentuk itu.

Di balik layar, skrip itu kira-kira menjalankan dua perintah berikut:

```bash
javac -d out src/kedaikita/*.java
java -cp out kedaikita.Main --demo
```

Perhatikan nama kelasnya kini ditulis lengkap dengan nama *package*: `kedaikita.Main`. Penjelasan lengkapnya ada di halaman praktik Java Pertemuan 15.

## 7. Ke Mana Perginya *File* `.class`?

| Cara menjalankan | *File* `.class` yang dihasilkan |
|---|---|
| `java NamaFile.java` | **tidak ada**; kompilasi terjadi di memori |
| `javac NamaFile.java` | di folder yang sama dengan *file* `.java`, satu *file* per kelas |
| `javac *.java` | di folder yang sama, satu *file* per kelas |
| `javac -d out ...` | di dalam folder `out/` |
| Tombol ▷/**Run** di VS Code | disimpan oleh VS Code di lokasinya sendiri; kamu tidak perlu mengurusnya |

*File* `.class` boleh dihapus kapan saja karena bisa dibuat ulang dengan `javac`. Caranya, dari folder tempat *file-file* itu berada, ketik `del *.class` (Windows) atau `rm *.class` (macOS/Linux). Repositori ini juga sudah mengatur agar *file* `.class` dan folder `out/` tidak ikut tersimpan ke Git.

> [!NOTE]
> Jika kamu masih memakai JDK lama (Java 11), perintah `java NamaFile.java` bisa gagal dengan pesan `error: class found on application class path: NamaFile` ketika di folder yang sama ada *file* `NamaFile.class` hasil `javac`. Solusinya, hapus *file-file* `.class` di folder itu. Solusi yang lebih baik: pasang JDK 17 atau lebih baru karena versi itu tidak lagi bermasalah dengan *file* `.class` lama.

## 8. Membaca Hasil dan Pesan *Error*

Saat program dijalankan, ada tiga kemungkinan:

| Yang terjadi | Artinya | Yang perlu dilakukan |
|---|---|---|
| *Output* muncul sesuai harapan | program benar | lanjutkan belajar |
| *Output* muncul tetapi hasilnya keliru | ada kesalahan **logika** | periksa alur dan perhitungan programmu |
| Muncul pesan *error* | ada kesalahan **sintaks** atau kesalahan saat **berjalan** | baca pesan *error*-nya |

Cara membaca pesan *error*:

- **Python** menampilkan *traceback*. Baca dari **bawah ke atas**: baris paling bawah menyebutkan jenis *error* (misalnya `NameError`), dan baris di atasnya menunjukkan nama *file* serta nomor barisnya.
- **Java** punya dua jenis *error*. *Error* **kompilasi** muncul saat `javac` atau sebelum program berjalan, diawali nama *file* dan nomor baris (misalnya `Menu.java:12: error: ...`). *Error* saat **berjalan** diawali `Exception in thread "main"`.

Pesan *error* yang sering muncul saat persiapan beserta solusinya dikumpulkan di [Mengatasi Masalah](mengatasi-masalah.md).

## 📝 Ringkasan

| Situasi | 🐍 Python | ☕ Java |
|---|---|---|
| Satu *file* | `python nama_file.py` | `java NamaFile.java` |
| Satu *file*, cara klasik | (tidak perlu kompilasi) | `javac NamaFile.java` lalu `java NamaFile` |
| Banyak *file* (P05—P14) | masuk ke `studi-kasus`, lalu `python main.py` | masuk ke `studi-kasus`, lalu `javac *.java` dan `java Main` |
| Proyek ber-*package* (P15) | `python main.py --demo` | `.\jalankan.bat --demo` (Windows) atau `bash jalankan.sh --demo` |
| Pengujian (P15) | `python -m unittest discover -s tests -v` | `.\uji.bat` (Windows) atau `bash uji.sh` |

Ingat juga:

- Perintah diketik di **terminal**, dari folder tempat programnya berada. Selalu periksa **folder aktif**.
- Semua perintah `cd` di halaman praktik ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.
- Di macOS/Linux, gunakan `python3` sebagai ganti `python`.
- Kompilasi ulang dengan `javac` setiap kali kode Java berubah (kecuali memakai `java NamaFile.java`).

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Mengatasi Masalah ➡️](mengatasi-masalah.md)
