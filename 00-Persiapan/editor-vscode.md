# Editor VS Code

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Menjalankan Program ➡️](menjalankan-program.md)

> Kita memakai **Visual Studio Code** (VS Code) sebagai editor utama karena gratis, ringan, dan bisa dipakai untuk Python maupun Java. Halaman ini membahas cara memasangnya, ekstensi yang dibutuhkan, dan satu hal yang sangat penting: **membuka folder yang benar**.

## Daftar Isi

1. [Memasang VS Code](#1-memasang-vs-code)
2. [Memasang Ekstensi](#2-memasang-ekstensi)
3. [Membuka Folder yang Benar](#3-membuka-folder-yang-benar)
4. [Menjalankan Program dari VS Code](#4-menjalankan-program-dari-vs-code)
5. [Terminal Terintegrasi](#5-terminal-terintegrasi)
6. [Pengaturan Kecil yang Membantu](#6-pengaturan-kecil-yang-membantu)
7. [Alternatif Editor dan IDE](#7-alternatif-editor-dan-ide)

---

## 1. Memasang VS Code

Unduh VS Code dari situs resminya: [code.visualstudio.com](https://code.visualstudio.com/).

**Windows**

1. Unduh installer untuk Windows (pilihan bawaan, *User Installer*, sudah tepat).
2. Jalankan installer, setujui lisensi, lalu klik **Next**.
3. Di halaman **Select Additional Tasks**, centang:
   - **Add "Open with Code" action to Windows Explorer file context menu**
   - **Add "Open with Code" action to Windows Explorer directory context menu**
   - **Add to PATH** (biasanya sudah tercentang)
4. Klik **Next**, lalu **Install**.

Dua pilihan "Open with Code" membuatmu bisa klik kanan sebuah folder di File Explorer lalu langsung membukanya di VS Code. Sangat praktis.

**macOS**

1. Unduh file `.zip` untuk macOS, lalu buka hingga muncul aplikasi **Visual Studio Code**.
2. Seret aplikasi itu ke folder **Applications**.
3. (Opsional) Buka VS Code, tekan Cmd+Shift+P, ketik `shell command`, lalu pilih **Shell Command: Install 'code' command in PATH**. Setelah itu kamu bisa membuka folder dari Terminal dengan perintah `code .`.

**Linux**

Unduh paket `.deb` (Ubuntu/Debian) atau `.rpm` (Fedora) dari situs VS Code, lalu pasang seperti aplikasi biasa. Sebagian distribusi juga menyediakan VS Code lewat Snap.

## 2. Memasang Ekstensi

Ekstensi menambah kemampuan VS Code. Buka panel **Extensions** dengan menekan Ctrl+Shift+X (macOS: Cmd+Shift+X), lalu cari dan pasang ekstensi berikut:

| Jalur | Nama ekstensi | Penerbit | Gunanya |
|---|---|---|---|
| 🐍 Python | **Python** | Microsoft | menjalankan dan men-*debug* Python, pewarnaan kode, saran otomatis |
| ☕ Java | **Extension Pack for Java** | Microsoft | paket berisi beberapa ekstensi Java sekaligus: dukungan bahasa, *debugger*, pengelola proyek, dan lainnya |

> [!WARNING]
> Ada banyak ekstensi dengan nama mirip. Pastikan penerbitnya **Microsoft** dan jumlah unduhannya besar. Ekstensi Python resmi biasanya juga memasang beberapa ekstensi pendampingnya secara otomatis, seperti Pylance. Itu normal.

Setelah ekstensi terpasang:

- **Python:** buka sebuah file `.py`. Jika VS Code memintamu memilih *interpreter*, pilih Python yang tadi kamu pasang. Kamu juga bisa memilihnya kapan saja lewat Ctrl+Shift+P, lalu ketik **Python: Select Interpreter**.
- **Java:** buka sebuah file `.java`. VS Code biasanya menemukan JDK secara otomatis. Jika tidak, tekan Ctrl+Shift+P lalu jalankan **Java: Configure Java Runtime**. Jika JDK baru saja dipasang, tutup dan buka lagi VS Code.

> [!TIP]
> Untuk Windows dan macOS, Microsoft juga menyediakan **Coding Pack for Java**, yaitu satu installer yang memasang VS Code, JDK, dan ekstensi Java sekaligus. Ini pilihan praktis jika kamu memulai dari nol untuk jalur Java.

## 3. Membuka Folder yang Benar

Ini bagian **paling penting** di halaman ini. Bacalah pelan-pelan.

VS Code bekerja paling baik jika kamu membuka sebuah **folder**, bukan satu file saja. Caranya: **File → Open Folder...**, lalu pilih foldernya. Atau di Windows, klik kanan folder lalu pilih **Open with Code**.

| Jalur | Folder yang sebaiknya dibuka | Contoh |
|---|---|---|
| 🐍 Python | folder pertemuan, atau folder `python/` milik pertemuan itu | `Pertemuan-02-Kelas-dan-Objek/python` |
| ☕ Java | folder **`java/` milik satu pertemuan**, bukan seluruh repositori | `Pertemuan-02-Kelas-dan-Objek/java` |

### Kenapa Java tidak boleh membuka seluruh repositori?

Ekstensi Java menganggap semua file `.java` di dalam folder yang kamu buka sebagai **satu proyek**. Masalahnya, hampir setiap pertemuan punya kelas dengan nama yang sama, misalnya `Menu`, `Pesanan`, atau `Kedai`. Di dalam satu proyek Java, dua kelas tidak boleh bernama sama.

Akibatnya, jika kamu membuka seluruh folder `PBO2026`, VS Code akan memberi garis merah bergelombang di banyak file, dengan pesan seperti:

```text
The type Menu is already defined
```

Padahal kodenya tidak salah. Di dalam satu folder `java/` pertemuan, setiap nama kelas sudah dibuat unik, sehingga masalah ini tidak muncul.

> [!IMPORTANT]
> Untuk jalur Java: **satu pertemuan, satu jendela VS Code**. Saat pindah pertemuan, buka folder `java/` pertemuan berikutnya (**File → Open Folder...** atau **File → Open Recent**).

> [!TIP]
> Garis merah masih tersisa setelah kamu berpindah folder? Tekan Ctrl+Shift+P, lalu jalankan **Java: Clean Java Language Server Workspace**, dan pilih *Restart*.

### Kotak dialog "Do you trust the authors?"

Saat membuka folder baru, VS Code mungkin bertanya *Do you trust the authors of the files in this folder?*. Untuk folder materi ini, pilih **Yes, I trust the authors**. Jika kamu memilih tidak, VS Code masuk ke *Restricted Mode* dan sebagian fitur ekstensi, termasuk tombol *Run*, dimatikan.

## 4. Menjalankan Program dari VS Code

**Python**

1. Buka file `.py` yang ingin dijalankan.
2. Klik tombol ▷ di pojok kanan atas editor (**Run Python File**).
3. Hasilnya muncul di panel **TERMINAL** di bagian bawah.

**Java**

1. Buka file `.java` yang berisi method `main`.
2. Klik tulisan **Run** yang muncul tepat di atas baris `public static void main`, atau klik tombol ▷ di pojok kanan atas editor.
3. Hasilnya muncul di panel **TERMINAL** atau **DEBUG CONSOLE** di bagian bawah.

Untuk studi kasus Java mulai Pertemuan 05 yang terdiri atas banyak file, jalankan file `Main.java`. VS Code akan mengompilasi file-file lain yang dibutuhkan secara otomatis. Untuk proyek ber-*package* di Pertemuan 15, ikuti petunjuk di halaman praktik pertemuan itu.

> [!NOTE]
> Tombol *Run* sangat praktis, tetapi kamu tetap perlu bisa menjalankan program dari terminal. Saat ujian praktik atau saat ada masalah dengan editor, terminal adalah penyelamatmu. Pelajari caranya di [Menjalankan Program](menjalankan-program.md).

## 5. Terminal Terintegrasi

VS Code punya terminal di dalamnya, jadi kamu tidak perlu berpindah jendela. Bukalah dengan menu **View → Terminal** atau tombol Ctrl+\` (tombol *backtick*, di kiri angka 1).

- Terminal ini otomatis dibuka di folder yang sedang kamu buka di VS Code.
- Semua perintah di halaman [Menjalankan Program](menjalankan-program.md) bisa diketik di sini.
- Di Windows, terminal bawaannya adalah **PowerShell**. Jika kamu lebih suka Command Prompt, tekan Ctrl+Shift+P, jalankan **Terminal: Select Default Profile**, lalu pilih **Command Prompt**.

## 6. Pengaturan Kecil yang Membantu

| Pengaturan | Cara | Manfaat |
|---|---|---|
| Simpan otomatis | **File → Auto Save** | tidak ada lagi program yang dijalankan sebelum disimpan |
| Merapikan kode | Shift+Alt+F (macOS: Shift+Option+F) | indentasi dan spasi menjadi rapi |
| Memperbesar huruf | Ctrl+= dan Ctrl+- (macOS: Cmd+= dan Cmd+-) | nyaman dibaca, apalagi saat presentasi |
| Palet perintah | Ctrl+Shift+P (macOS: Cmd+Shift+P) | mencari perintah VS Code apa pun dengan mengetik namanya |

> [!WARNING]
> Jika "Auto Save" tidak aktif, perhatikan titik bulat di tab file. Titik itu berarti ada perubahan yang **belum disimpan**. Program yang dijalankan dari terminal selalu memakai versi yang **sudah disimpan**.

## 7. Alternatif Editor dan IDE

VS Code bukan satu-satunya pilihan. Jika kamu sudah nyaman dengan editor lain, silakan dipakai. Prinsipnya tetap sama: satu pertemuan, satu proyek.

| Alat | Bahasa | Catatan |
|---|---|---|
| **IntelliJ IDEA** (JetBrains) | Java | IDE Java yang sangat populer di industri. Gunakan edisi atau fitur gratisnya. |
| **PyCharm** (JetBrains) | Python | IDE khusus Python. Fitur intinya gratis; dulu dikenal sebagai *Community Edition*. |
| **Apache NetBeans** | Java | IDE gratis dan terbuka dari Apache. |
| **Thonny** | Python | editor sederhana untuk pemula, sudah membawa Python sendiri. |
| **BlueJ** | Java | dirancang untuk belajar PBO; kelas dan objek bisa dilihat dan dicoba secara visual. |

> [!NOTE]
> Cara membuka proyek dan menjalankan program di setiap IDE sedikit berbeda. Materi ini menulis petunjuk untuk terminal dan VS Code. Jika memakai IDE lain, sesuaikan sendiri, ya.

## 📝 Ringkasan

- Pasang VS Code, lalu ekstensi **Python** dan/atau **Extension Pack for Java** dari Microsoft.
- Selalu buka **folder**, bukan satu file saja.
- Jalur Java: buka folder `java/` milik **satu** pertemuan agar tidak muncul pesan *The type ... is already defined*.
- Pilih **Yes, I trust the authors** agar ekstensi berjalan penuh.
- Tombol ▷ menjalankan program, dan terminal terintegrasi dibuka dengan Ctrl+\`.

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Menjalankan Program ➡️](menjalankan-program.md)
