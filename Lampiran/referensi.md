# Referensi

[🏠 Beranda](../README.md) · [Lampiran](README.md) · [Glosarium](glosarium.md) · [*Cheat Sheet* Python ↔ Java](cheatsheet-python-java.md) · **Referensi** · [FAQ](faq.md)

> Daftar bacaan dan sumber belajar untuk memperdalam materi. Kamu **tidak** perlu membaca semuanya. Pilih satu atau dua sumber yang sesuai dengan jalurmu dan topik yang sedang kamu pelajari. Di bagian akhir ada daftar sumber semua gambar yang dipakai di materi ini.

## Daftar Isi

1. [Cara Memakai Daftar Ini](#1-cara-memakai-daftar-ini)
2. [Dokumentasi Resmi Python](#2-dokumentasi-resmi-python)
3. [Dokumentasi Resmi Java](#3-dokumentasi-resmi-java)
4. [Buku](#4-buku)
5. [Situs Belajar Daring](#5-situs-belajar-daring)
6. [Alat Bantu Diagram dan Visualisasi](#6-alat-bantu-diagram-dan-visualisasi)
7. [Gaya Penulisan Kode dan Pengujian](#7-gaya-penulisan-kode-dan-pengujian)
8. [Sumber Gambar](#8-sumber-gambar)

---

## 1. Cara Memakai Daftar Ini

Urutan yang disarankan saat kamu ingin memahami sesuatu lebih dalam:

1. **Materi pertemuan di repositori ini.** Semua istilah dan contoh disesuaikan dengan alur kuliah.
2. **Dokumentasi resmi.** Paling akurat dan selalu mengikuti versi terbaru bahasa.
3. **Buku.** Bagus untuk pemahaman yang runtut dan mendalam.
4. **Situs belajar dan video.** Bagus untuk sudut pandang lain, tetapi periksa tahun terbit dan versi bahasanya.

> [!TIP]
> Sebagian besar sumber di bawah ini berbahasa Inggris. Jangan takut. Bahasa Inggris teknis cenderung sederhana dan berulang, dan kemampuan membacanya akan sangat berguna sepanjang kariermu. Biasakan sedikit demi sedikit, misalnya dengan membaca dokumentasi resmi setiap kali menemukan istilah baru.

## 2. Dokumentasi Resmi Python

| Sumber | Isinya | Pertemuan terkait |
|---|---|---|
| [*The Python Tutorial: Classes*](https://docs.python.org/3/tutorial/classes.html) | bab resmi tentang kelas, objek, pewarisan, dan *iterator* | P02—P07 |
| [*The Python Tutorial: Errors and Exceptions*](https://docs.python.org/3/tutorial/errors.html) | `try`, `except`, `else`, `finally`, `raise`, dan *exception* buatan sendiri | P11 |
| [Modul `abc`](https://docs.python.org/3/library/abc.html) | `ABC` dan `@abstractmethod` untuk kelas abstrak | P10 |
| [Modul `typing`](https://docs.python.org/3/library/typing.html) | petunjuk tipe, `Protocol`, `Generic`, dan `TypeVar` | P05, P10, P12 |
| [Modul `unittest`](https://docs.python.org/3/library/unittest.html) | kerangka *unit test* bawaan Python | P15 |
| [Modul `csv`](https://docs.python.org/3/library/csv.html) dan [modul `pathlib`](https://docs.python.org/3/library/pathlib.html) | membaca dan menulis *file* CSV, serta mengelola alamat *file* | P15 |
| [*Using Python on Windows*](https://docs.python.org/3/using/windows.html) | panduan resmi memasang dan menjalankan Python di Windows, termasuk Python install manager yang kini dianjurkan python.org | Persiapan |

> [!NOTE]
> Alamat `docs.python.org/3/` selalu menampilkan dokumentasi Python versi terbaru (per Oktober 2026: Python 3.15). Perhatikan keterangan seperti *Added in version 3.11* di bawah sebuah fitur. Jika angkanya lebih besar daripada versi Python-mu, fitur itu belum bisa kamu pakai.

## 3. Dokumentasi Resmi Java

| Sumber | Isinya | Pertemuan terkait |
|---|---|---|
| [*Learn Java* (dev.java)](https://dev.java/learn/) | tutorial resmi Java terkini dari Oracle, mulai dari langkah pertama | semua |
| [dev.java: *Object Oriented Programming*](https://dev.java/learn/language/oop/) | kelas, objek, *interface*, dan pewarisan di Java | P02—P10 |
| [dev.java: *Annotations and Exceptions*](https://dev.java/learn/language/annotations-exceptions/) | penanganan *exception* di Java | P11 |
| [dev.java: *Collections and Streams*](https://dev.java/learn/api/collections-and-streams/) | `List`, `Set`, `Map`, dan *stream* | P12 |
| [*The Java Tutorials* (Oracle)](https://docs.oracle.com/javase/tutorial/) | tutorial klasik yang lengkap, misalnya [*Object-Oriented Programming Concepts*](https://docs.oracle.com/javase/tutorial/java/concepts/index.html) | P01—P12 |
| [Dokumentasi API Java SE 17](https://docs.oracle.com/en/java/javase/17/docs/api/index.html) | penjelasan resmi setiap kelas bawaan Java, misalnya `ArrayList` atau `String`; versi 17 sesuai batas minimal mata kuliah ini | semua |
| [*JEP 330: Launch Single-File Source-Code Programs*](https://openjdk.org/jeps/330) | latar belakang perintah `java NamaFile.java` (sejak Java 11) | P01, Persiapan |

> [!NOTE]
> *The Java Tutorials* dari Oracle ditulis untuk JDK 8 sehingga tidak memuat fitur Java yang lebih baru. Konsep PBO di dalamnya tetap berlaku. Untuk materi yang lebih mutakhir, gunakan dev.java.

## 4. Buku

Cek ketersediaan buku-buku ini di perpustakaan atau toko buku. Untuk buku yang punya beberapa edisi, utamakan edisi terbaru.

### Pemrograman dasar dan bahasa

| Judul | Penulis | Cocok untuk |
|---|---|---|
| *Head First Java* | Kathy Sierra, Bert Bates, dan Trisha Gee (edisi ke-3) | pemula jalur Java; gaya bahasanya santai dan penuh gambar |
| *Python Crash Course* | Eric Matthes | pemula jalur Python; ada bab khusus tentang kelas |
| *Think Python* | Allen B. Downey | pemula jalur Python; edisi ke-3 bisa [dibaca gratis secara daring](https://allendowney.github.io/ThinkPython/) |
| *Python Object-Oriented Programming* | Steven F. Lott dan Dusty Phillips | jalur Python yang ingin mendalami PBO |
| *Fluent Python* | Luciano Ramalho | tingkat lanjut: memahami cara kerja Python secara mendalam, termasuk *method* khusus seperti `__eq__` |
| *Effective Java* | Joshua Bloch | tingkat lanjut: praktik terbaik Java, misalnya `equals` dan `hashCode`, serta desain kelas dan *interface* |

### Analisis, desain, dan UML

| Judul | Penulis | Cocok untuk |
|---|---|---|
| *Head First Object-Oriented Analysis and Design* | Brett D. McLaughlin, Gary Pollice, dan David West | belajar cara berpikir dan merancang secara berorientasi objek |
| *UML Distilled* | Martin Fowler | pengantar UML yang ringkas, termasuk diagram kelas (P06) |

### Prinsip desain dan pola desain

| Judul | Penulis | Cocok untuk |
|---|---|---|
| *Design Patterns: Elements of Reusable Object-Oriented Software* | Erich Gamma, Richard Helm, Ralph Johnson, dan John Vlissides (dikenal sebagai *Gang of Four*) | rujukan asli 23 pola desain (P14) |
| *Head First Design Patterns* | Eric Freeman dan Elisabeth Robson | pengantar pola desain yang ramah pemula, dengan contoh Java (P14) |
| *Clean Code* | Robert C. Martin | menulis kode yang mudah dibaca dan dirawat (P13) |
| *Agile Software Development, Principles, Patterns, and Practices* | Robert C. Martin | sumber klasik yang membahas kelima prinsip SOLID secara lengkap (P13) |
| *Refactoring: Improving the Design of Existing Code* | Martin Fowler | katalog teknik *refactoring*; edisi ke-2 memakai contoh JavaScript (P13) |

> [!TIP]
> Untuk pemula, mulailah dari satu buku seri *Head First* atau buku pemrograman dasar sesuai jalurmu. Buku seperti *Design Patterns* dan *Effective Java* lebih nikmat dibaca setelah kamu menyelesaikan Pertemuan 10.

## 5. Situs Belajar Daring

| Situs | Isinya | Pertemuan terkait |
|---|---|---|
| [Real Python: *Object-Oriented Programming (OOP) in Python*](https://realpython.com/python3-object-oriented-programming/) | artikel panjang tentang PBO di Python, dengan banyak contoh | P02—P07 |
| [Real Python: *Inheritance and Composition: A Python OOP Guide*](https://realpython.com/inheritance-composition-python/) | kapan memakai pewarisan dan kapan memakai komposisi | P05, P07 |
| [Refactoring.Guru: *Design Patterns*](https://refactoring.guru/design-patterns) | penjelasan visual pola desain, lengkap dengan contoh kode Python dan Java | P14 |
| [Refactoring.Guru: *Refactoring*](https://refactoring.guru/refactoring) | katalog *code smell* dan teknik *refactoring* | P13 |
| [Martin Fowler: *Tell Don't Ask*](https://martinfowler.com/bliki/TellDontAsk.html) | artikel singkat tentang menyuruh objek bekerja, alih-alih menanyakan datanya | P04 |
| [*Pro Git*](https://git-scm.com/book/en/v2) | buku gratis tentang Git karya Scott Chacon dan Ben Straub, bisa dibaca daring | Persiapan |

## 6. Alat Bantu Diagram dan Visualisasi

| Alat | Kegunaan | Pertemuan terkait |
|---|---|---|
| [Mermaid: *Class diagrams*](https://mermaid.js.org/syntax/classDiagram.html) | dokumentasi resmi sintaks diagram kelas yang dipakai di materi ini | P06 |
| [Mermaid Live Editor](https://mermaid.live/) | mencoba kode Mermaid dan langsung melihat gambarnya | P06 |
| [GitHub Docs: *Creating diagrams*](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/creating-diagrams) | cara GitHub menampilkan diagram Mermaid di *file* Markdown | P06 |
| [draw.io / diagrams.net](https://www.drawio.com/) | menggambar diagram dengan *drag and drop*, gratis, bisa langsung di peramban | P06 |
| [PlantUML: *Class diagram*](https://plantuml.com/class-diagram) | membuat diagram UML dari teks | P06 |
| [Python Tutor](https://pythontutor.com/) | melihat langkah demi langkah apa yang terjadi di memori saat kode Python atau Java berjalan; sangat membantu memahami objek dan referensi | P02, P03 |
| [BlueJ](https://www.bluej.org/) | lingkungan Java untuk belajar PBO; objek bisa dibuat dan dicoba secara visual | P02—P07 |
| [Thonny](https://thonny.org/) | editor Python untuk pemula dengan tampilan variabel yang jelas; sudah membawa Python sendiri | P01—P04 |

## 7. Gaya Penulisan Kode dan Pengujian

| Sumber | Isinya | Pertemuan terkait |
|---|---|---|
| [*PEP 8: Style Guide for Python Code*](https://peps.python.org/pep-0008/) | panduan resmi gaya penulisan kode Python | semua |
| [*Google Java Style Guide*](https://google.github.io/styleguide/javaguide.html) | panduan gaya penulisan kode Java yang banyak dirujuk | semua |
| [pytest](https://docs.pytest.org/) | kerangka pengujian Python yang populer di industri (lanjutan dari `unittest`) | P15 |
| [JUnit](https://junit.org/) | kerangka pengujian standar di dunia Java; versi terbarunya, JUnit 6, membutuhkan Java 17 ke atas | P15 |

## 8. Sumber Gambar

### Tangkapan layar dari dokumentasi resmi

Tangkapan layar berikut diambil dari dokumentasi resmi yang boleh dipakai ulang asalkan sumber dan lisensinya dicantumkan. Keterangan sumber juga tertulis tepat di bawah setiap gambar.

| Gambar | Dipakai di | Sumber | Hak cipta dan lisensi | Perubahan |
|---|---|---|---|---|
| Tampilan utama VS Code | [Editor VS Code](../00-Persiapan/editor-vscode.md#mengenal-tampilan-vs-code) | [*User interface*](https://code.visualstudio.com/docs/editing/getting-started/userinterface) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| Hasil pencarian ekstensi Python | [Editor VS Code](../00-Persiapan/editor-vscode.md#2-memasang-ekstensi) | [*Extension Marketplace*](https://code.visualstudio.com/docs/configure/extensions/extension-marketplace) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | dipotong dan diperkecil |
| Kotak dialog *Workspace Trust* | [Editor VS Code](../00-Persiapan/editor-vscode.md#kotak-dialog-do-you-trust-the-authors) | [*Workspace Trust*](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| Tombol **Run Python File** | [Editor VS Code](../00-Persiapan/editor-vscode.md#4-menjalankan-program-dari-vs-code), [Praktik Python P01](../Pertemuan-01-Pengenalan-PBO/python/README.md#cara-menjalankan-contoh) | [*Getting Started with Python in VS Code*](https://code.visualstudio.com/docs/python/python-tutorial) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| *Output* program di panel **TERMINAL** | [Editor VS Code](../00-Persiapan/editor-vscode.md#4-menjalankan-program-dari-vs-code) | [*Getting Started with Python in VS Code*](https://code.visualstudio.com/docs/python/python-tutorial) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| Tulisan **Run \| Debug** di atas `main` | [Editor VS Code](../00-Persiapan/editor-vscode.md#4-menjalankan-program-dari-vs-code), [Praktik Java P01](../Pertemuan-01-Pengenalan-PBO/java/README.md#cara-menjalankan-contoh) | [*Running and debugging Java*](https://code.visualstudio.com/docs/java/java-debugging) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| Menu **Open in Integrated Terminal** | [Editor VS Code](../00-Persiapan/editor-vscode.md#5-terminal-terintegrasi) | [*Terminal Basics*](https://code.visualstudio.com/docs/terminal/basics) | © Microsoft Corporation, [CC BY 3.0 US](https://creativecommons.org/licenses/by/3.0/us/) | tidak ada |
| Menu **Download ZIP** di GitHub | [Git dan GitHub](../00-Persiapan/git-dan-github.md#2-cara-1-unduh-zip-tanpa-git) | GitHub Docs: [*Cloning a repository*](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository) | © GitHub, Inc., [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) | penanda kotak dipindahkan ke **Download ZIP**, diperkecil |
| *Installer* klasik Python di Windows | [Instalasi Python](../00-Persiapan/instalasi-python.md#32-cara-b-installer-klasik) | [*Using Python on Windows*](https://docs.python.org/3/using/windows.html) | Copyright © 2001 Python Software Foundation; All Rights Reserved, [PSF License Version 2](https://docs.python.org/3/license.html) | kotak merah ditambahkan |

> [!NOTE]
> Lisensi di atas mengizinkan gambar dipakai ulang, tetapi tidak memberikan hak atas merek dagang. Logo VS Code, GitHub, dan Python yang terlihat di gambar tetap milik pemiliknya masing-masing dan hanya muncul sebagai bagian dari tangkapan layar.

### Ilustrasi buatan sendiri

Ilustrasi berikut dibuat khusus untuk materi ini oleh penyusun materi.

| Ilustrasi | Dipakai di |
|---|---|
| Folder materi dan folder latihan (versi Python dan versi Java) | [Git dan GitHub](../00-Persiapan/git-dan-github.md#pilihan-a-folder-terpisah-paling-sederhana), [Praktik Python P01](../Pertemuan-01-Pengenalan-PBO/python/README.md#tempat-menyimpan-kodemu-sendiri), [Praktik Java P01](../Pertemuan-01-Pengenalan-PBO/java/README.md#tempat-menyimpan-kodemu-sendiri) |
| Tiga tempat mengetik: editor, terminal, dan mode interaktif | [Menjalankan Program](../00-Persiapan/menjalankan-program.md#1-apa-itu-terminal), [Praktik Python P01](../Pertemuan-01-Pengenalan-PBO/python/README.md#cek-instalasi-python), [Praktik Java P01](../Pertemuan-01-Pengenalan-PBO/java/README.md#cek-instalasi-java) |
| Satu cetakan (kelas), banyak kue (objek) | [Pertemuan 02](../Pertemuan-02-Kelas-dan-Objek/README.md#1-cerita-pembuka-satu-cetakan-banyak-kue) |
| Dua nama, satu yang ditunjuk (referensi) | [Pertemuan 03](../Pertemuan-03-Atribut-dan-Method/README.md#7-variabel-menyimpan-referensi-bukan-objek) |
| Enam garis relasi UML | [Pertemuan 06](../Pertemuan-06-UML-Class-Diagram/README.md#5-relasi-arti-setiap-garis) |
| "Adalah" berarti berada di dalam himpunan yang lebih umum | [Pertemuan 07](../Pertemuan-07-Pewarisan/README.md#3-relasi-adalah-is-a) |
| Label kardus: tipe variabel dan tipe objek | [Pertemuan 09](../Pertemuan-09-Polimorfisme/README.md#tipe-variabel-dan-tipe-objek) |
| Stopkontak dan alat-alatnya (abstraksi) | [Pertemuan 10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md#2-abstraksi-menonjolkan-yang-penting) |
| Arah membaca *traceback* dan *stack trace* | [Pertemuan 11](../Pertemuan-11-Exception-Handling/README.md#4-jika-tidak-ada-yang-menangkap-traceback-dan-stack-trace) |
| Rak bernomor dan kode *hash* | [Pertemuan 12](../Pertemuan-12-Koleksi-dan-Generics/README.md#mengapa-harus-berpasangan-dengan-hash) |

---

Semua tautan di halaman ini terakhir diperiksa pada Oktober 2026. Menemukan tautan yang rusak atau sumber bagus yang ingin kamu rekomendasikan ke teman-teman? Usulkan lewat [Issues GitHub](https://github.com/antonprafanto/PBO2026/issues) atau sampaikan ke dosen.

[🏠 Beranda](../README.md) · [Lampiran](README.md) · [Glosarium](glosarium.md) · [*Cheat Sheet* Python ↔ Java](cheatsheet-python-java.md) · **Referensi** · [FAQ](faq.md)
