# Menjalankan Program

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Git dan GitHub ➡️](git-dan-github.md)

> Tombol *Run* di editor memang praktis, tetapi programmer sejati juga akrab dengan **terminal**. Di halaman ini kamu belajar dasar terminal, lalu cara menjalankan program Python dan Java dalam berbagai bentuk yang akan kamu temui sepanjang semester.

## Daftar Isi

1. [Apa Itu Terminal?](#1-apa-itu-terminal)
2. [Membuka Terminal](#2-membuka-terminal)
3. [Perintah Dasar Terminal](#3-perintah-dasar-terminal)
4. [Berpindah ke Folder Materi](#4-berpindah-ke-folder-materi)
5. [Menjalankan Program Python](#5-menjalankan-program-python)
6. [Menjalankan Program Java](#6-menjalankan-program-java)
7. [Ke Mana Perginya File .class?](#7-ke-mana-perginya-file-class)
8. [Membaca Hasil dan Pesan Error](#8-membaca-hasil-dan-pesan-error)

---

## 1. Apa Itu Terminal?

**Terminal** adalah jendela tempat kita memberi perintah ke komputer dengan **mengetik**, bukan dengan mengklik. Bayangkan kamu memesan di kedai: alih-alih menunjuk gambar menu, kamu langsung menyebutkan pesananmu ke kasir dengan kalimat yang jelas.

Di terminal, kamu selalu "berdiri" di sebuah folder yang disebut **folder aktif**. Perintah seperti `python kedaikita.py` mencari file `kedaikita.py` **di folder aktif itu**. Karena itu, kemampuan paling penting di terminal adalah **berpindah ke folder yang benar**.

## 2. Membuka Terminal

| Sistem | Cara membuka |
|---|---|
| Windows | Klik **Start**, ketik `PowerShell` atau `Terminal`, lalu tekan Enter. Command Prompt (`cmd`) juga bisa dipakai. |
| Windows, langsung di sebuah folder | Buka folder di File Explorer, klik kanan di area kosong, lalu pilih **Open in Terminal** (Windows 11). Cara lain: klik bilah alamat File Explorer, ketik `powershell`, lalu tekan Enter. |
| macOS | Tekan Cmd+Spasi, ketik `Terminal`, lalu tekan Enter. |
| Linux | Biasanya Ctrl+Alt+T, atau cari aplikasi **Terminal**. |
| VS Code | Menu **View → Terminal** atau Ctrl+\`. Terminal langsung terbuka di folder yang sedang dibuka VS Code. |

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

> [!TIP]
> Di macOS, ketik `cd ` (dengan spasi), lalu **seret folder** dari Finder ke jendela Terminal. Alamat lengkap folder itu akan terisi otomatis. Tekan Enter, dan kamu sudah berada di folder tersebut.

## 4. Berpindah ke Folder Materi

Misalkan materi kamu simpan di folder `Documents`. Untuk masuk ke folder contoh Python Pertemuan 02:

**Windows:**

```bash
cd Documents\PBO2026\Pertemuan-02-Kelas-dan-Objek\python\contoh
```

**macOS / Linux:**

```bash
cd ~/Documents/PBO2026/Pertemuan-02-Kelas-dan-Objek/python/contoh
```

Lalu periksa isinya dengan `dir` (Windows) atau `ls` (macOS/Linux). Jika nama file yang ingin dijalankan terlihat di daftar, kamu sudah berada di tempat yang benar.

> [!NOTE]
> Di Windows, pemisah folder yang asli adalah `\`. PowerShell juga menerima `/`, sehingga perintah seperti `cd Pertemuan-02-Kelas-dan-Objek/python/contoh` di halaman praktik tetap berjalan. Jika di Command Prompt perintah dengan `/` bermasalah, ganti dengan `\`. Jika kamu mengunduh materi sebagai ZIP, nama foldernya biasanya `PBO2026-main`.

## 5. Menjalankan Program Python

### 5.1 Program satu file

Semua file di folder `contoh/` dan `solusi/`, serta studi kasus Pertemuan 01–04, adalah program satu file:

```bash
python nama_file.py
```

Di macOS/Linux, ketik `python3 nama_file.py`. Di Windows, `py nama_file.py` juga bisa dipakai.

### 5.2 Program banyak file (mulai Pertemuan 05)

Mulai Pertemuan 05, studi kasus KedaiKita terdiri atas beberapa file yang saling memakai lewat `import`. Masuk dulu ke folder `studi-kasus`, lalu jalankan `main.py`:

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/python/studi-kasus
python main.py
```

> [!IMPORTANT]
> Jalankan `main.py`, bukan file lain seperti `menu.py` atau `pesanan.py`. File-file itu hanya berisi kelas yang dipakai oleh `main.py`, sehingga jika dijalankan sendiri biasanya tidak menampilkan apa-apa.

### 5.3 Proyek ber-*package* (Pertemuan 15)

Di Pertemuan 15, semua kelas KedaiKita berada di dalam *package* `kedaikita/`. Jalankan dari folder `studi-kasus`:

```bash
python main.py --demo
python main.py
python -m unittest discover -s tests -v
```

| Perintah | Artinya |
|---|---|
| `python main.py --demo` | mode demo: berjalan sendiri tanpa perlu mengetik apa pun |
| `python main.py` | mode interaktif: kamu menjadi kasir dan mengetik pilihan menu |
| `python -m unittest discover -s tests -v` | menjalankan semua *unit test* di folder `tests/` |

## 6. Menjalankan Program Java

Program Java harus **dikompilasi** dulu menjadi *bytecode* (file `.class`), baru kemudian **dijalankan** oleh JVM (*Java Virtual Machine*). Ada beberapa cara melakukannya.

### 6.1 Satu file, cara cepat: `java NamaFile.java`

Sejak Java 11, program satu file bisa langsung dijalankan. Java mengompilasinya di memori, lalu langsung menjalankannya:

```bash
java NamaFile.java
```

Cara ini dipakai untuk semua file di folder `contoh/` dan `solusi/`, serta studi kasus Pertemuan 01–04.

> [!IMPORTANT]
> Dengan cara ini, kelas yang memiliki method `main` harus ditulis **paling atas** di dalam file. Pada Java 11 sampai 21, kelas pertama di dalam file **wajib** punya `main`. Java versi lebih baru sedikit lebih longgar, tetapi agar aman di semua versi, selalu taruh kelas ber-`main` paling atas, seperti semua contoh di materi ini.

Jika aturan itu dilanggar (Java 11 sampai 21), pesan error-nya kira-kira seperti ini, dengan `Kucing` sebagai kelas pertama di file:

```text
error: can't find main(String[]) method in class: Kucing
```

### 6.2 Satu file, cara klasik: `javac` lalu `java`

Cara klasik terdiri atas dua langkah: kompilasi dengan `javac`, lalu jalankan dengan `java`.

```bash
javac KedaiKita.java
java KedaiKita
```

- Langkah pertama menghasilkan file `.class` untuk **setiap kelas** di dalam file. Misalnya, `KedaiKita.java` di Pertemuan 02 menghasilkan `KedaiKita.class` dan `Menu.class`.
- Langkah kedua ditulis **tanpa** akhiran `.java` maupun `.class`. Yang ditulis adalah **nama kelas** yang punya `main`.

> [!WARNING]
> Setiap kali kodenya diubah, kamu harus menjalankan `javac` **lagi**. Jika lupa, `java` akan menjalankan file `.class` versi lama, dan kamu akan bingung kenapa perubahanmu "tidak berpengaruh".

### 6.3 Banyak file (mulai Pertemuan 05): `javac *.java` lalu `java Main`

Mulai Pertemuan 05, setiap kelas KedaiKita punya file sendiri (`Menu.java`, `Pesanan.java`, `Kedai.java`, dan seterusnya), dan program utamanya ada di `Main.java`. Masuk ke folder `studi-kasus`, lalu:

```bash
cd Pertemuan-05-Relasi-Antar-Kelas/java/studi-kasus
javac *.java
java Main
```

Tanda `*` berarti "semua". Jadi `javac *.java` mengompilasi **semua** file berakhiran `.java` di folder itu sekaligus. Perintah ini berjalan di Command Prompt, PowerShell, macOS, maupun Linux.

> [!TIP]
> Ingin folder tetap bersih dari file `.class`? Simpan hasil kompilasi di folder terpisah bernama `out`:
>
> ```bash
> javac -d out *.java
> java -cp out Main
> ```
>
> Opsi `-d out` artinya "simpan hasil kompilasi di folder `out`", dan `-cp out` artinya "cari kelas di folder `out`".

> [!NOTE]
> Sejak Java 22, perintah `java Main.java` juga bisa menjalankan program yang terdiri atas banyak file. Namun materi ini memakai `javac *.java` lalu `java Main` karena cara itu berlaku di semua versi yang kita pakai (17, 21, dan 25).

### 6.4 Proyek ber-*package* (Pertemuan 15)

Di Pertemuan 15, kode Java berada di dalam *package* `kedaikita` (folder `src/kedaikita/`). Perintahnya lebih panjang, jadi disediakan skrip agar kamu cukup mengetik satu perintah dari folder `studi-kasus`:

| Tujuan | Windows (Command Prompt) | Windows (PowerShell) | macOS / Linux |
|---|---|---|---|
| Mode demo | `jalankan.bat --demo` | `.\jalankan.bat --demo` | `bash jalankan.sh --demo` |
| Mode interaktif | `jalankan.bat` | `.\jalankan.bat` | `bash jalankan.sh` |
| Menjalankan pengujian | `uji.bat` | `.\uji.bat` | `bash uji.sh` |

Di balik layar, skrip itu kira-kira menjalankan dua perintah berikut:

```bash
javac -d out src/kedaikita/*.java
java -cp out kedaikita.Main --demo
```

Perhatikan nama kelasnya kini ditulis lengkap dengan nama *package*: `kedaikita.Main`. Penjelasan lengkapnya ada di halaman praktik Java Pertemuan 15.

> [!NOTE]
> PowerShell tidak menjalankan file dari folder aktif tanpa awalan `.\`. Itu sebabnya di PowerShell kamu harus mengetik `.\jalankan.bat`, bukan `jalankan.bat`.

## 7. Ke Mana Perginya File .class?

| Cara menjalankan | File `.class` yang dihasilkan |
|---|---|
| `java NamaFile.java` | **tidak ada**; kompilasi terjadi di memori |
| `javac NamaFile.java` | di folder yang sama dengan file `.java`, satu file per kelas |
| `javac *.java` | di folder yang sama, satu file per kelas |
| `javac -d out ...` | di dalam folder `out/` |
| Tombol *Run* di VS Code | disimpan oleh VS Code di lokasinya sendiri; kamu tidak perlu mengurusnya |

File `.class` boleh dihapus kapan saja, karena bisa dibuat ulang dengan `javac`. Repositori ini juga sudah mengatur agar file `.class` dan folder `out/` tidak ikut tersimpan ke Git.

> [!NOTE]
> Jika kamu masih memakai JDK lama (Java 11), perintah `java NamaFile.java` bisa gagal dengan pesan `error: class found on application class path: NamaFile` ketika di folder yang sama ada file `NamaFile.class` hasil `javac`. Solusinya, hapus file-file `.class` di folder itu. Solusi yang lebih baik: pasang JDK 17 atau lebih baru, karena versi itu tidak lagi bermasalah dengan file `.class` lama.

## 8. Membaca Hasil dan Pesan Error

Saat program dijalankan, ada tiga kemungkinan:

| Yang terjadi | Artinya | Yang perlu dilakukan |
|---|---|---|
| Output muncul sesuai harapan | program benar | lanjutkan belajar |
| Output muncul tetapi hasilnya keliru | ada kesalahan **logika** | periksa alur dan perhitungan programmu |
| Muncul pesan error | ada kesalahan **sintaks** atau kesalahan saat **berjalan** | baca pesan error-nya |

Cara membaca pesan error:

- **Python** menampilkan *traceback*. Baca dari **bawah ke atas**: baris paling bawah menyebutkan jenis error (misalnya `NameError`), dan baris di atasnya menunjukkan nama file serta nomor barisnya.
- **Java** punya dua jenis error. Error **kompilasi** muncul saat `javac` atau sebelum program berjalan, diawali nama file dan nomor baris (misalnya `Menu.java:12: error: ...`). Error saat **berjalan** diawali `Exception in thread "main"`.

Pesan error yang sering muncul saat persiapan beserta solusinya dikumpulkan di [Mengatasi Masalah](mengatasi-masalah.md).

## 📝 Ringkasan

| Situasi | 🐍 Python | ☕ Java |
|---|---|---|
| Satu file | `python nama_file.py` | `java NamaFile.java` |
| Satu file, cara klasik | (tidak perlu kompilasi) | `javac NamaFile.java` lalu `java NamaFile` |
| Banyak file (P05–P14) | masuk ke `studi-kasus`, lalu `python main.py` | masuk ke `studi-kasus`, lalu `javac *.java` dan `java Main` |
| Proyek ber-*package* (P15) | `python main.py --demo` | `jalankan.bat --demo` atau `bash jalankan.sh --demo` |
| Pengujian (P15) | `python -m unittest discover -s tests -v` | `uji.bat` atau `bash uji.sh` |

Ingat juga: selalu periksa **folder aktif**, di macOS/Linux gunakan `python3`, dan kompilasi ulang dengan `javac` setiap kali kode Java berubah.

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Git dan GitHub ➡️](git-dan-github.md)
