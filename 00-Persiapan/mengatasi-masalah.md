# Mengatasi Masalah

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Pertemuan 01 ➡️](../Pertemuan-01-Pengenalan-PBO/README.md)

> Kumpulan masalah yang paling sering muncul saat menyiapkan dan menjalankan program, lengkap dengan **gejala**, **penyebab**, dan **solusinya**. Kamu tidak perlu membaca semuanya. Cari saja pesan error yang mirip dengan yang kamu lihat (tekan Ctrl+F di peramban, lalu ketik sebagian pesannya).

> [!NOTE]
> Pesan error ditampilkan dalam bahasa Inggris, sama seperti yang akan kamu lihat di layar. Bunyinya bisa sedikit berbeda antarversi Python, Java, atau sistem operasi. Fokuslah pada kata-kata kuncinya.

## Daftar Isi

**Langkah umum**

- [Lima Langkah yang Menyelesaikan Banyak Masalah](#lima-langkah-yang-menyelesaikan-banyak-masalah)

**A. Python**

- [A1. `python` tidak dikenali di Windows](#a1-python-tidak-dikenali-di-windows)
- [A2. `python` membuka Microsoft Store](#a2-python-membuka-microsoft-store)
- [A3. `command not found: python` di macOS atau Linux](#a3-command-not-found-python-di-macos-atau-linux)
- [A4. Versi Python terlalu lama](#a4-versi-python-terlalu-lama)
- [A5. `can't open file ... No such file or directory`](#a5-cant-open-file--no-such-file-or-directory)
- [A6. `ModuleNotFoundError: No module named ...`](#a6-modulenotfounderror-no-module-named-)
- [A7. Nama file sama dengan modul bawaan Python](#a7-nama-file-sama-dengan-modul-bawaan-python)
- [A8. `SyntaxError: invalid syntax` saat mengetik perintah terminal](#a8-syntaxerror-invalid-syntax-saat-mengetik-perintah-terminal)
- [A9. `UnicodeEncodeError` atau karakter aneh di konsol](#a9-unicodeencodeerror-atau-karakter-aneh-di-konsol)

**B. Java**

- [B1. `javac` tidak dikenali](#b1-javac-tidak-dikenali)
- [B2. Versi `java` dan `javac` berbeda](#b2-versi-java-dan-javac-berbeda)
- [B3. `UnsupportedClassVersionError`](#b3-unsupportedclassversionerror)
- [B4. `Could not find or load main class`](#b4-could-not-find-or-load-main-class)
- [B5. `can't find main(String[]) method in class`](#b5-cant-find-mainstring-method-in-class)
- [B6. `class X is public, should be declared in a file named X.java`](#b6-class-x-is-public-should-be-declared-in-a-file-named-xjava)
- [B7. `error: file not found`](#b7-error-file-not-found)
- [B8. Perubahan kode tidak berpengaruh](#b8-perubahan-kode-tidak-berpengaruh)
- [B9. `class found on application class path`](#b9-class-found-on-application-class-path)
- [B10. Karakter aneh pada output Java](#b10-karakter-aneh-pada-output-java)

**C. VS Code**

- [C1. Garis merah `The type Menu is already defined`](#c1-garis-merah-the-type-menu-is-already-defined)
- [C2. Tombol *Run* tidak muncul](#c2-tombol-run-tidak-muncul)
- [C3. Garis bergelombang di baris `import` padahal program berjalan](#c3-garis-bergelombang-di-baris-import-padahal-program-berjalan)
- [C4. VS Code tidak menemukan Python atau JDK yang baru dipasang](#c4-vs-code-tidak-menemukan-python-atau-jdk-yang-baru-dipasang)

**D. Terminal, Skrip, dan Git**

- [D1. PowerShell tidak mengenali `jalankan.bat`](#d1-powershell-tidak-mengenali-jalankanbat)
- [D2. `permission denied` saat menjalankan skrip `.sh`](#d2-permission-denied-saat-menjalankan-skrip-sh)
- [D3. Nama folder mengandung spasi](#d3-nama-folder-mengandung-spasi)
- [D4. `git` tidak dikenali](#d4-git-tidak-dikenali)
- [D5. `git pull` menolak berjalan](#d5-git-pull-menolak-berjalan)

**Penutup**

- [Masih Buntu? Cara Meminta Bantuan](#masih-buntu-cara-meminta-bantuan)

---

## Lima Langkah yang Menyelesaikan Banyak Masalah

Sebelum mencari ke daftar di bawah, coba lima langkah ini. Sebagian besar masalah pemula selesai di sini.

1. **Tutup semua terminal dan VS Code, lalu buka lagi.** Perubahan `PATH` setelah instalasi hanya terbaca oleh terminal yang dibuka **setelahnya**.
2. **Periksa versi.** `python --version` (atau `python3 --version`), `java -version`, dan `javac -version`.
3. **Periksa folder aktif.** Ketik `dir` (Windows) atau `ls` (macOS/Linux). Apakah file yang ingin kamu jalankan ada di daftar?
4. **Periksa ejaan dan huruf besar-kecil.** `KedaiKita.java` tidak sama dengan `kedaikita.java`.
5. **Baca baris terpenting pesan error.** Di Python, baris paling bawah. Di Java, baris yang mengandung `error:` atau `Exception`.

---

## A. Python

### A1. `python` tidak dikenali di Windows

**Gejala.** Di Command Prompt muncul:

```text
'python' is not recognized as an internal or external command,
operable program or batch file.
```

Di PowerShell, pesannya memuat kalimat `The term 'python' is not recognized as the name of a cmdlet, ...`.

**Penyebab.** Python belum terpasang, atau sudah terpasang tetapi foldernya belum masuk `PATH`. Penyebab paling umum: lupa mencentang **Add python.exe to PATH** saat instalasi.

**Solusi.**

1. Coba `py --version`. Jika berhasil, kamu bisa memakai `py` sebagai ganti `python` (misalnya `py kedaikita.py`).
2. Untuk memperbaiki `python`, jalankan lagi installer Python, pilih **Modify**, lalu centang **Add Python to environment variables**. Cara lain: hapus Python, lalu pasang ulang dengan mencentang **Add python.exe to PATH**. Lihat [Instalasi Python](instalasi-python.md).
3. Tutup terminal, buka yang baru, lalu coba lagi.

### A2. `python` membuka Microsoft Store

**Gejala.** Mengetik `python` membuka Microsoft Store, atau muncul pesan:

```text
Python was not found; run without arguments to install from the Microsoft Store, or disable this shortcut from Settings > Manage App Execution Aliases.
```

**Penyebab.** Windows punya jalan pintas (*app execution alias*) bernama `python.exe` yang mengarah ke Microsoft Store. Jalan pintas itu terpakai karena Windows tidak menemukan Python sungguhan di `PATH`.

**Solusi.** Pastikan Python sudah terpasang dan masuk `PATH` (lihat [A1](#a1-python-tidak-dikenali-di-windows)). Lalu klik **Start**, ketik `alias`, buka **Manage app execution aliases**, dan:

- jika memasang Python dengan installer klasik, **matikan** alias **App Installer python.exe** dan **App Installer python3.exe**;
- jika memakai **Python install manager**, pastikan alias **Python (default)** **menyala**.

Penjelasan lengkapnya ada di [Instalasi Python](instalasi-python.md).

### A3. `command not found: python` di macOS atau Linux

**Gejala.**

```text
zsh: command not found: python
```

Di Linux, pesannya bisa berbunyi `Command 'python' not found` disertai saran memakai `python3`.

**Penyebab.** Di macOS dan banyak distribusi Linux, perintah Python 3 bernama `python3`, bukan `python`.

**Solusi.** Ketik `python3` setiap kali materi menulis `python`, misalnya `python3 main.py`. Di Ubuntu, kamu juga bisa memasang paket `python-is-python3`.

### A4. Versi Python terlalu lama

**Gejala.** Program studi kasus Pertemuan 05 ke atas gagal dengan pesan seperti ini:

```text
    def cari_menu(self, kode: str) -> Menu | None:
TypeError: unsupported operand type(s) for |: 'type' and 'NoneType'
```

**Penyebab.** Penulisan `Menu | None` baru didukung sejak **Python 3.10**. Pesan di atas muncul jika kamu memakai Python 3.9 atau lebih lama. Ini sering terjadi di macOS yang memakai `python3` bawaan Apple.

**Solusi.** Periksa dengan `python --version` atau `python3 --version`. Pasang Python 3.12 atau lebih baru dari python.org (lihat [Instalasi Python](instalasi-python.md)), lalu buka terminal baru.

### A5. `can't open file ... No such file or directory`

**Gejala.**

```text
python3: can't open file '/home/budi/PBO2026/halo.py': [Errno 2] No such file or directory
```

**Penyebab.** File yang kamu sebutkan tidak ada di **folder aktif**. Biasanya kamu belum masuk ke folder yang benar, atau nama filenya salah ketik.

**Solusi.** Lihat isi folder dengan `dir` atau `ls`. Pindah ke folder yang benar dengan `cd`, lalu jalankan lagi. Gunakan tombol Tab agar nama file terisi otomatis tanpa salah ketik.

### A6. `ModuleNotFoundError: No module named ...`

**Gejala.**

```text
ModuleNotFoundError: No module named 'kedaikita'
```

atau `No module named 'kedai'`, `No module named 'menu'`, dan sejenisnya.

**Penyebab.** Python tidak menemukan file yang di-`import`. Penyebab yang paling sering:

- Kamu menyalin `main.py` saja ke folder lain, tanpa file-file pendampingnya (`menu.py`, `kedai.py`, dan lainnya).
- Kamu menjalankan file **di dalam** *package* secara langsung, misalnya `python kedaikita/aplikasi.py` di Pertemuan 15.
- Kamu menjalankan `python -m unittest discover -s tests` dari luar folder `studi-kasus`.

**Solusi.** Masuk ke folder `studi-kasus` pertemuan itu, lalu jalankan program utamanya dari sana:

```bash
cd Pertemuan-15-Proyek-Terintegrasi/python/studi-kasus
python main.py --demo
python -m unittest discover -s tests -v
```

Untuk Pertemuan 05–14, cukup `python main.py` dari folder `studi-kasus`. Jika menyalin studi kasus ke folder latihanmu, salin **semua** file `.py` di folder itu.

### A7. Nama file sama dengan modul bawaan Python

**Gejala.** Program yang memakai modul bawaan tiba-tiba gagal. Misalnya kamu membuat file bernama `csv.py` untuk berlatih membaca file CSV. Di Python 3.13 muncul pesan yang cukup jelas:

```text
AttributeError: module 'csv' has no attribute 'writer' (consider renaming '.../csv.py' since it has the same name as the standard library module named 'csv' and prevents importing that standard library module)
```

Di versi yang lebih lama, pesannya kurang jelas, misalnya `AttributeError: partially initialized module 'csv' has no attribute 'writer' (most likely due to a circular import)`.

**Penyebab.** Python mencari modul di folder tempat programmu berada lebih dulu, baru kemudian di pustaka bawaannya. File `csv.py` milikmu "menutupi" modul `csv` bawaan Python.

**Solusi.** Ganti nama filemu, misalnya menjadi `latihan_csv.py`. Hindari nama file yang sama dengan modul bawaan, seperti `csv.py`, `random.py`, `string.py`, atau `unittest.py`. Hapus juga folder `__pycache__` jika ada.

### A8. `SyntaxError: invalid syntax` saat mengetik perintah terminal

**Gejala.**

```text
>>> python halo.py
  File "<stdin>", line 1
    python halo.py
           ^^^^
SyntaxError: invalid syntax
```

**Penyebab.** Kamu sedang berada di dalam **mode interaktif Python** (ditandai `>>>`), lalu mengetik perintah terminal. Python tidak mengerti perintah terminal.

**Solusi.** Ketik `exit()` untuk keluar dari mode interaktif, lalu ketik ulang perintahnya di terminal biasa.

### A9. `UnicodeEncodeError` atau karakter aneh di konsol

**Gejala.** Program yang mencetak simbol khusus (emoji, panah `→`, huruf beraksen) gagal di Windows dengan pesan seperti:

```text
UnicodeEncodeError: 'charmap' codec can't encode character '\u2192' in position 10: character maps to <undefined>
```

Atau programnya berjalan, tetapi simbol tampil sebagai `?` atau huruf-huruf aneh.

**Penyebab.** Konsol Windows tidak selalu memakai pengodean UTF-8. Masalah ini paling sering muncul saat output dialihkan ke file atau saat program dijalankan dari terminal atau alat tertentu.

**Solusi.**

- Semua program di materi ini sengaja hanya mencetak karakter **ASCII** (huruf, angka, dan tanda baca biasa) agar aman di semua komputer. Ikuti kebiasaan yang sama di latihanmu: tulis `->` sebagai ganti `→`, dan hindari emoji di output.
- Jika memang perlu mencetak karakter khusus, jalankan program dengan mode UTF-8 Python, misalnya `python -X utf8 nama_file.py`.
- Memakai **Windows Terminal** dan Python versi terbaru juga mengurangi masalah ini.

---

## B. Java

### B1. `javac` tidak dikenali

**Gejala.**

```text
'javac' is not recognized as an internal or external command,
operable program or batch file.
```

Di macOS/Linux, pesannya bisa berbunyi `command not found: javac` atau `Unable to locate a Java Runtime`.

**Penyebab.** Yang terpasang hanya JRE (tanpa *compiler*), atau JDK sudah terpasang tetapi folder `bin`-nya belum masuk `PATH`.

**Solusi.** Pasang **JDK** (bukan JRE), misalnya Eclipse Temurin, dan pastikan pilihan **Add to PATH** aktif. Jika masih gagal, atur `PATH` dan `JAVA_HOME` secara manual. Langkahnya ada di [Instalasi Java](instalasi-java.md). Setelah itu, buka terminal baru.

### B2. Versi `java` dan `javac` berbeda

**Gejala.** `java -version` menampilkan `1.8.0_...` atau `17.0...`, sedangkan `javac -version` menampilkan `21.0...`. Atau versinya tidak sesuai dengan JDK yang baru kamu pasang.

**Penyebab.** Ada lebih dari satu Java di komputermu, dan `PATH` menemukan Java yang lain lebih dulu. Contohnya, Java lama yang pernah dipasang untuk aplikasi tertentu, atau folder `...\Oracle\Java\javapath` yang berada di urutan atas `PATH`.

**Solusi.** Cari tahu Java mana yang dipakai dengan `where java` (Command Prompt), `where.exe java` (PowerShell), atau `which -a java` (macOS/Linux). Lokasi paling atas itulah yang dipakai. Hapus Java yang tidak diperlukan, atau atur urutan `PATH` agar JDK pilihanmu berada paling atas. Panduannya ada di bagian "Lebih dari Satu Java Terpasang" pada [Instalasi Java](instalasi-java.md).

### B3. `UnsupportedClassVersionError`

**Gejala.** Program berhasil dikompilasi, tetapi gagal dijalankan dengan pesan yang memuat:

```text
java.lang.UnsupportedClassVersionError: Halo has been compiled by a more recent version of the Java Runtime (class file version 65.0), this version of the Java Runtime only recognizes class file versions up to 52.0
```

**Penyebab.** File `.class` dibuat oleh `javac` versi baru, tetapi dijalankan oleh `java` versi lama. Angka *class file version* menunjukkan versinya:

| Class file version | Versi Java |
|---|---|
| 52 | Java 8 |
| 55 | Java 11 |
| 61 | Java 17 |
| 65 | Java 21 |
| 69 | Java 25 |

Pada contoh di atas, kode dikompilasi dengan Java 21 (65) tetapi dijalankan dengan Java 8 (52).

**Solusi.** Samakan versi `java` dan `javac`. Lihat [B2](#b2-versi-java-dan-javac-berbeda).

### B4. `Could not find or load main class`

**Gejala.**

```text
Error: Could not find or load main class Halo.class
Caused by: java.lang.ClassNotFoundException: Halo.class
```

**Penyebab dan solusi.** Pesan ini punya beberapa kemungkinan penyebab:

| Penyebab | Solusi |
|---|---|
| Menulis akhiran `.class`, misalnya `java Halo.class` | tulis nama kelasnya saja: `java Halo` |
| Belum menjalankan `javac`, atau berada di folder yang salah | jalankan `javac` dulu di folder yang benar, lalu `java NamaKelas` |
| Huruf besar-kecil salah, misalnya `java halo` | tulis persis seperti nama kelasnya: `java Halo` |
| Menulis `java Halo.java` padahal `java` yang terpakai adalah Java 8 | pasang dan pakai JDK 17 atau lebih baru (lihat [B2](#b2-versi-java-dan-javac-berbeda)) |
| Kelas berada di dalam *package* (Pertemuan 15) | gunakan nama lengkap dan *class path*, atau cukup jalankan skrip `jalankan.bat`/`jalankan.sh` |

### B5. `can't find main(String[]) method in class`

**Gejala.** Saat menjalankan `java NamaFile.java`:

```text
error: can't find main(String[]) method in class: Kucing
```

**Penyebab.** Saat memakai `java NamaFile.java`, Java 11 sampai 21 menjalankan **kelas pertama** di dalam file. Di contoh ini, kelas pertamanya adalah `Kucing`, yang tidak punya method `main`.

**Solusi.** Pindahkan kelas `public` yang berisi `main` ke **paling atas** file, lalu letakkan kelas-kelas pembantu di bawahnya. Semua contoh di materi ini sudah memakai susunan tersebut.

### B6. `class X is public, should be declared in a file named X.java`

**Gejala.**

```text
Salah.java:1: error: class KedaiKita is public, should be declared in a file named KedaiKita.java
public class KedaiKita {
       ^
1 error
```

**Penyebab.** Di Java, kelas `public` harus disimpan di file yang namanya **sama persis** dengan nama kelasnya, termasuk huruf besar-kecilnya.

**Solusi.** Ganti nama file menjadi `KedaiKita.java`, atau ganti nama kelasnya agar sama dengan nama file.

### B7. `error: file not found`

**Gejala.**

```text
error: file not found: *.java
Usage: javac <options> <source files>
use --help for a list of possible options
```

Pesan yang sama muncul untuk nama file tertentu, misalnya `error: file not found: KedaiKita.java`.

**Penyebab.** Kamu menjalankan `javac` di folder yang tidak berisi file tersebut. Pada contoh di atas, folder aktifnya tidak berisi satu pun file `.java`.

**Solusi.** Periksa isi folder dengan `dir` atau `ls`, lalu pindah ke folder yang benar, misalnya `java/studi-kasus` milik pertemuan yang sedang kamu pelajari.

### B8. Perubahan kode tidak berpengaruh

**Gejala.** Kamu sudah mengubah kode, tetapi output program masih sama seperti sebelumnya.

**Penyebab.** Ada dua kemungkinan. Pertama, file belum disimpan. Kedua, kamu memakai cara dua langkah (`javac` lalu `java`) dan lupa menjalankan `javac` lagi, sehingga `java` masih menjalankan file `.class` versi lama.

**Solusi.** Simpan file (Ctrl+S), lalu jalankan `javac` lagi sebelum `java`. Untuk program satu file, kamu bisa memakai `java NamaFile.java` yang selalu mengompilasi ulang. Aktifkan juga **File → Auto Save** di VS Code.

### B9. `class found on application class path`

**Gejala.** Saat menjalankan `java NamaFile.java`:

```text
error: class found on application class path: NamaFile
```

**Penyebab.** Pesan ini muncul di **Java 11** jika di folder yang sama terdapat file `NamaFile.class` hasil `javac` sebelumnya. Java 17 ke atas tidak lagi bermasalah dengan hal ini.

**Solusi.** Hapus file-file `.class` di folder itu (`del *.class` di Windows, `rm *.class` di macOS/Linux), lalu jalankan lagi. Solusi yang lebih baik: pasang JDK 17 atau lebih baru, sesuai syarat mata kuliah ini.

### B10. Karakter aneh pada output Java

**Gejala.** Huruf beraksen atau simbol khusus di program Java-mu tampil sebagai `?` atau sebagai huruf-huruf aneh seperti `Ã©`.

**Penyebab.** Ada dua kemungkinan. Konsol Windows tidak memakai pengodean UTF-8, atau (pada JDK 17 di Windows) `javac` membaca file sumber dengan pengodean bawaan Windows, bukan UTF-8.

**Solusi.**

- Seperti di materi ini, cetak hanya karakter **ASCII** di output program.
- Jika memakai JDK 17 di Windows dan kode sumbermu berisi karakter khusus, kompilasi dengan `javac -encoding UTF-8 NamaFile.java`. Mulai JDK 18, `javac` sudah memakai UTF-8 secara bawaan.
- Di Command Prompt, perintah `chcp 65001` sebelum menjalankan program biasanya membantu konsol menampilkan karakter UTF-8.

---

## C. VS Code

### C1. Garis merah `The type Menu is already defined`

**Gejala.** Banyak file Java diberi garis merah bergelombang, dengan pesan seperti `The type Menu is already defined`, padahal programnya benar.

**Penyebab.** Kamu membuka **seluruh repositori** (atau beberapa pertemuan sekaligus) di VS Code. Ekstensi Java menganggap semua file `.java` sebagai satu proyek, sedangkan kelas `Menu` ada di banyak pertemuan.

**Solusi.** Tutup folder itu, lalu buka folder `java/` milik **satu** pertemuan saja (**File → Open Folder...**). Jika garis merah masih tersisa, tekan Ctrl+Shift+P lalu jalankan **Java: Clean Java Language Server Workspace**. Lihat [Editor VS Code](editor-vscode.md).

### C2. Tombol *Run* tidak muncul

**Gejala.** Tombol ▷ atau tulisan **Run** di atas `main` tidak muncul.

**Penyebab dan solusi.**

- **Ekstensi belum terpasang.** Pasang **Python** dan/atau **Extension Pack for Java** dari Microsoft.
- **VS Code dalam *Restricted Mode*.** Klik tulisan *Restricted Mode* di bilah status bawah (atau tombol *Manage* pada pemberitahuannya), lalu pilih **Trust**.
- **Kamu membuka satu file saja, bukan folder.** Buka foldernya dengan **File → Open Folder...**.
- **Ekstensi Java masih memuat proyek.** Tunggu beberapa detik sampai proses di bilah status bawah selesai.

### C3. Garis bergelombang di baris `import` padahal program berjalan

**Gejala.** Jika VS Code memberi garis bergelombang di baris seperti `from menu import Menu`, dengan pesan `Import "menu" could not be resolved`, tetapi program berjalan normal dari terminal.

**Penyebab.** Folder yang kamu buka di VS Code berbeda dengan folder tempat file-file itu berada, sehingga editor gagal "melihat" file `menu.py`.

**Solusi.** Program yang berjalan normal dari terminal itu tidak salah. Agar garisnya hilang, buka folder `studi-kasus` pertemuan itu secara langsung di VS Code.

### C4. VS Code tidak menemukan Python atau JDK yang baru dipasang

**Gejala.** VS Code meminta kamu memasang Python atau Java, padahal sudah terpasang.

**Penyebab.** VS Code sudah terbuka sebelum instalasi selesai, sehingga belum membaca `PATH` yang baru.

**Solusi.** Tutup **semua** jendela VS Code, lalu buka lagi. Untuk Python, pilih *interpreter* lewat Ctrl+Shift+P → **Python: Select Interpreter**. Untuk Java, gunakan Ctrl+Shift+P → **Java: Configure Java Runtime**.

---

## D. Terminal, Skrip, dan Git

### D1. PowerShell tidak mengenali `jalankan.bat`

**Gejala.** Di PowerShell, mengetik `jalankan.bat` memunculkan pesan panjang yang memuat:

```text
The term 'jalankan.bat' is not recognized as the name of a cmdlet, function, script file, or operable program.
```

**Penyebab.** Demi keamanan, PowerShell tidak menjalankan file dari folder aktif tanpa awalan `.\`.

**Solusi.** Ketik `.\jalankan.bat` (atau `.\jalankan.bat --demo`). Di Command Prompt, `jalankan.bat` tanpa awalan tetap bisa dipakai.

### D2. `permission denied` saat menjalankan skrip `.sh`

**Gejala.** Di macOS atau Linux:

```text
zsh: permission denied: ./jalankan.sh
```

**Penyebab.** File skrip belum punya izin untuk dieksekusi. Ini sering terjadi jika materi diunduh sebagai ZIP.

**Solusi.** Jalankan skrip lewat `bash`, yang tidak butuh izin eksekusi:

```bash
bash jalankan.sh --demo
```

Cara lain: beri izin sekali dengan `chmod +x jalankan.sh`, lalu jalankan `./jalankan.sh --demo`.

### D3. Nama folder mengandung spasi

**Gejala.** `cd` gagal atau masuk ke folder yang salah, misalnya saat mengetik `cd Tugas Kuliah`.

**Penyebab.** Terminal menganggap spasi sebagai pemisah, sehingga `Tugas` dan `Kuliah` dibaca sebagai dua hal berbeda.

**Solusi.** Apit nama folder dengan tanda kutip: `cd "Tugas Kuliah"`. Lebih baik lagi, hindari spasi saat memberi nama folder kerjamu, misalnya `Tugas-Kuliah`.

### D4. `git` tidak dikenali

**Gejala.**

```text
'git' is not recognized as an internal or external command,
operable program or batch file.
```

**Penyebab.** Git belum terpasang, atau terminal dibuka sebelum Git selesai dipasang.

**Solusi.** Pasang Git (lihat [Git dan GitHub](git-dan-github.md)), lalu buka terminal baru. Jika belum ingin memakai Git, kamu tetap bisa mengunduh materi sebagai ZIP.

### D5. `git pull` menolak berjalan

**Gejala.** Muncul pesan `Your local changes to the following files would be overwritten by merge`.

**Penyebab.** Kamu mengubah file materi secara langsung, dan versi barunya akan menimpa perubahanmu.

**Solusi.** Gunakan `git stash`, `git pull`, lalu `git stash pop`, atau salin perubahanmu ke tempat lain lalu buang perubahan itu. Langkah lengkapnya ada di [Git dan GitHub](git-dan-github.md). Ke depannya, simpan latihanmu di folder terpisah.

---

## Masih Buntu? Cara Meminta Bantuan

Tidak apa-apa meminta bantuan. Agar asisten atau dosen bisa membantu dengan cepat, sertakan informasi berikut:

```text
Sistem operasi : Windows 11 / macOS / Ubuntu 24.04 / ...
Versi          : (hasil python --version, java -version, javac -version)
Perintah       : (perintah yang kamu ketik, persis)
Folder aktif   : (hasil pwd atau cd tanpa argumen)
Pesan error    : (salin TEKSNYA, jangan hanya tangkapan layar)
Sudah dicoba   : (langkah apa saja yang sudah kamu lakukan)
```

Pertanyaan yang lengkap biasanya terjawab dalam satu kali balasan. Jika kamu menemukan kesalahan pada materi, laporkan lewat [Issues GitHub](https://github.com/antonprafanto/PBO2026/issues).

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Pertemuan 01 ➡️](../Pertemuan-01-Pengenalan-PBO/README.md)
