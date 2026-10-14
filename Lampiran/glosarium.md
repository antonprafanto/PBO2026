# Glosarium PBO

[🏠 Beranda](../README.md) · [Lampiran](README.md) · **Glosarium** · [*Cheat Sheet* Python ↔ Java](cheatsheet-python-java.md) · [Referensi](referensi.md) · [FAQ](faq.md)

> Kamus kecil berisi istilah-istilah yang muncul sepanjang mata kuliah, diurutkan dari A sampai Z. Ada 161 istilah. Kolom **Dibahas di** menunjukkan pertemuan yang memperkenalkan istilah itu dan pertemuan yang membahasnya secara lengkap.

Cara membaca tabel:

- Istilah ditulis dalam bahasa Indonesia jika padanannya lazim dipakai. Istilah yang tetap dipakai dalam bahasa Inggris ditulis *miring*, sama seperti di materi.
- Penulisan yang berupa kode, seperti `self` atau `super`, ditulis dengan huruf kode.
- Nama diri, seperti Git, dan singkatan, seperti OOP, tidak dimiringkan.
- Kode pertemuan: **P02** berarti Pertemuan 02. **Persiapan** berarti folder 00-Persiapan. Klik kodenya untuk membuka halaman konsep pertemuan itu.

> [!TIP]
> Mencari istilah tertentu? Tekan Ctrl+F (macOS: Cmd+F) di peramban, lalu ketik istilahnya dalam bahasa Indonesia atau Inggris.

**Lompat ke huruf:** [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Y](#y)

---

## A

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Abstraksi | *abstraction* | Menonjolkan hal yang penting dan menyembunyikan detail yang tidak perlu diketahui pemakai | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| *Access modifier* (pengatur hak akses) | *access modifier* | Penanda yang mengatur siapa yang boleh mengakses atribut atau *method*. Java punya `public`, `protected`, tanpa penanda (*default*), dan `private`; Python hanya memakai konvensi nama, misalnya `_harga` | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| *Adapter* | *adapter* | Pola desain yang menjembatani dua kelas yang antarmukanya tidak cocok | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| Agregasi | *aggregation* | Relasi "punya" yang bagiannya tetap bisa hidup sendiri, misalnya kedai dan menu-menunya | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| *Aliasing* | *aliasing* | Dua variabel menunjuk objek yang sama sehingga perubahan lewat satu variabel terlihat dari variabel lain | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Argumen | *argument* | Nilai yang dikirim saat memanggil fungsi, *method*, atau konstruktor | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Arsitektur berlapis | *layered architecture* | Susunan aplikasi dalam lapisan (tampilan, layanan, model, penyimpanan) yang masing-masing punya tugas jelas | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Asosiasi | *association* | Relasi "mengenal": sebuah objek menyimpan referensi ke objek lain | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| *Assertion* | *assertion* | Pernyataan di dalam *unit test* yang memeriksa hasil, misalnya "nilai ini seharusnya 36000"; jika tidak sesuai, *test* dinyatakan gagal | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Atribut | *attribute*, *field* | Data atau ciri yang dimiliki objek; di Java disebut juga *field* | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Atribut kelas | *class attribute*, *static field* | Atribut milik kelas yang nilainya dipakai bersama oleh semua objek | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Atribut objek | *instance attribute* | Atribut yang nilainya bisa berbeda untuk setiap objek | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Atribut *read-only* | *read-only attribute* | Atribut yang bisa dibaca dari luar tetapi tidak bisa diubah langsung | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| *Autoboxing* | *autoboxing* | Konversi otomatis Java antara tipe primitif (`int`) dan kelas pembungkusnya (`Integer`) | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |

---

## B

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Bytecode* | *bytecode* | Hasil kompilasi Java (*file* `.class`) yang dijalankan oleh JVM | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |

---

## C

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Casting* / *cast* | *casting*, *cast* | Menuliskan nama kelas tujuan di dalam kurung, misalnya `(PembayaranKartu) p` di Java. Pada objek, *casting* hanya mengubah cara memandang objek, bukan objeknya; lihat *upcasting* dan *downcasting* | [P09](../Pertemuan-09-Polimorfisme/README.md) |
| *Checked exception* | *checked exception* | *Exception* Java yang wajib ditangkap atau dideklarasikan dengan `throws` | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| *Code smell* | *code smell* | Tanda-tanda kode yang berpotensi bermasalah, misalnya kelas yang terlalu besar atau `if` yang sangat panjang | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| `Comparable` | *Comparable* | *Interface* Java untuk urutan alami objek lewat *method* `compareTo()`; padanan Python: `__lt__` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| `Comparator` | *Comparator* | Objek Java yang menentukan cara membandingkan dua objek saat mengurutkan; padanan Python: argumen `key` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *Compiler* | *compiler* | Program yang menerjemahkan kode sumber sebelum program dijalankan; di Java, `javac` menerjemahkannya menjadi *bytecode* | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| CSV | *comma-separated values* | Format *file* teks berisi data berbentuk tabel, satu baris per data, kolom dipisah tanda tertentu | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |

---

## D

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Decorator* (pola desain) | *decorator pattern* | Pola desain yang menambah perilaku objek dengan membungkusnya, tanpa mengubah kelas aslinya | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| *Default method* | *default method* | *Method* di *interface* Java yang sudah punya isi (sejak Java 8) | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| *Dependency injection* (injeksi dependensi) | *dependency injection* | Memberikan objek yang dibutuhkan sebuah kelas dari luar, biasanya lewat konstruktor; salah satu cara mewujudkan DIP | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| Dependensi | *dependency* | Relasi "memakai sementara", misalnya objek lain hanya diterima sebagai parameter. Di P13, dependensi berarti objek lain yang dibutuhkan sebuah kelas untuk bekerja | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md), [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Design pattern* (pola desain) | *design pattern* | Solusi teruji untuk masalah desain yang sering berulang | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| Diagram kelas | *class diagram* | Gambar UML yang menampilkan kelas, atribut, *method*, dan relasinya | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| DIP | *Dependency Inversion Principle* | Prinsip SOLID: kelas pengatur alur kerja tidak bergantung pada kelas detail teknis; keduanya bergantung pada abstraksi, bukan pada kelas konkret | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Docstring* | *docstring* | Teks penjelasan dalam tanda kutip tiga (`"""`) di awal *file*, kelas, fungsi, atau *method* Python | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| *Downcasting* | *downcasting* | Memandang kembali objek bertipe induk sebagai kelas anak tertentu. Di Java ditulis eksplisit, misalnya `(PembayaranKartu) p`, sebaiknya setelah diperiksa dengan `instanceof`; jika kelasnya salah, muncul `ClassCastException` | [P09](../Pertemuan-09-Polimorfisme/README.md) |
| DRY | *Don't Repeat Yourself* | Prinsip "jangan menulis logika yang sama berulang-ulang" | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Duck typing* | *duck typing* | Gaya Python: objek boleh dipakai selama punya *method* yang dibutuhkan, apa pun kelasnya | [P09](../Pertemuan-09-Polimorfisme/README.md) |
| *Dynamic dispatch* | *dynamic dispatch*, *late binding* | Pemilihan versi *method* berdasarkan objek sebenarnya saat program berjalan | [P09](../Pertemuan-09-Polimorfisme/README.md) |

---

## E

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Encoding* (pengodean) | *encoding* | Aturan mengubah huruf menjadi *byte*, misalnya UTF-8. *File* teks harus dibaca dengan *encoding* yang sama seperti saat ditulis | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Enkapsulasi | *encapsulation* | Membungkus data dan *method* dalam satu kelas serta membatasi akses langsung ke datanya | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| *Exception* (pengecualian) | *exception* | Objek yang mewakili kesalahan atau keadaan luar biasa saat program berjalan | [P04](../Pertemuan-04-Enkapsulasi/README.md), [P11](../Pertemuan-11-Exception-Handling/README.md) |
| *Exception* buatan sendiri | *custom exception* | Kelas *exception* baru yang dibuat dengan mewarisi kelas *exception* bawaan | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| *Exception chaining* | *exception chaining* | Melempar *exception* baru sambil menyertakan *exception* penyebabnya | [P11](../Pertemuan-11-Exception-Handling/README.md) |

---

## F

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Factory* | *factory* | Pola desain yang memusatkan pembuatan objek. *Simple Factory* memilih kelas lewat `if` di satu *method* (idiom populer, bukan pola GoF); *Factory Method* (pola GoF) menyerahkan pilihan ke kelas anak yang meng-*override* *method* pembuat milik kelas induk | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| *Field* | *field* | Sebutan Java untuk atribut; lihat Atribut | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| `final` | *final* | Kata kunci Java: atribut atau variabel hanya boleh diisi satu kali (misalnya konstanta `static final`), *method* tidak bisa di-*override*, kelas tidak bisa diwarisi | [P03](../Pertemuan-03-Atribut-dan-Method/README.md), [P04](../Pertemuan-04-Enkapsulasi/README.md), [P07](../Pertemuan-07-Pewarisan/README.md) |
| `finally` | *finally* | Blok yang selalu dijalankan setelah `try`, terjadi *exception* maupun tidak | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| Folder aktif | *working directory* | Folder tempat terminal sedang berada; perintah seperti `python main.py` mencari *file* di folder ini | [Persiapan: Menjalankan Program](../00-Persiapan/menjalankan-program.md), [P05](../Pertemuan-05-Relasi-Antarkelas/README.md) |

---

## G

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Generalisasi | *generalization* | Mengumpulkan kesamaan beberapa kelas ke dalam satu kelas induk | [P06](../Pertemuan-06-UML-Class-Diagram/README.md), [P07](../Pertemuan-07-Pewarisan/README.md) |
| *Generics* | *generics* | Kelas atau *method* yang tipe isinya ditentukan saat dipakai, misalnya `List<Menu>` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *Getter* | *getter* | *Method* untuk membaca nilai atribut yang disembunyikan | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| Git | Git | Program pencatat riwayat perubahan folder kode, dipakai untuk mengunduh dan memperbarui materi | [Persiapan: Git](../00-Persiapan/git-dan-github.md) |
| GoF | *Gang of Four* | Sebutan untuk empat penulis buku *Design Patterns* (1994) yang memuat 23 pola desain | [P14](../Pertemuan-14-Design-Pattern/README.md) |

---

## H

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Hierarki pewarisan | *inheritance hierarchy* | Susunan kelas induk dan kelas anak secara bertingkat | [P07](../Pertemuan-07-Pewarisan/README.md) |
| *Hook* | *hook method* | *Method* di kelas induk yang sudah punya isi bawaan dan boleh di-*override* kelas anak bila perlu | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |

---

## I

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| IDE | *integrated development environment* | Aplikasi lengkap untuk menulis, menjalankan, dan men-*debug* kode | [Persiapan: VS Code](../00-Persiapan/editor-vscode.md) |
| *Immutable* (tidak bisa diubah) | *immutable* | Sifat objek atau koleksi yang isinya tidak bisa diubah setelah dibuat, misalnya *tuple* di Python dan `List.of(...)` di Java | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *Information hiding* (penyembunyian informasi) | *information hiding* | Menyembunyikan detail internal kelas dari kode di luar kelas | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| Instansiasi | *instantiation* | Proses membuat objek dari sebuah kelas | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| *Interface* (antarmuka) | *interface* | Kontrak berisi daftar kemampuan yang wajib disediakan oleh kelas yang mengimplementasikannya | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| *Interpreter* | *interpreter* | Program yang menjalankan kode sumber secara langsung; program Python dijalankan oleh *interpreter* | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| *Is-a* dan *has-a* | *is-a*, *has-a* | Uji sederhana: "adalah" cocok untuk pewarisan, "punya" cocok untuk komposisi atau agregasi | [P07](../Pertemuan-07-Pewarisan/README.md) |
| ISP | *Interface Segregation Principle* | Prinsip SOLID: jangan memaksa kelas bergantung pada *method* yang tidak ia butuhkan; lebih baik beberapa *interface* kecil yang fokus | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |

---

## J

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Jaminan hasil | *postcondition* | Janji tentang hasil dan akibat *method* setelah dipanggil, misalnya "potongan tidak pernah negatif"; kelas anak tidak boleh memperlemahnya (LSP) | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| JDK | *Java Development Kit* | Paket untuk mengembangkan program Java, berisi *compiler* `javac` | [Persiapan: Java](../00-Persiapan/instalasi-java.md) |
| JRE | *Java Runtime Environment* | Paket untuk menjalankan program Java saja, tanpa *compiler* | [Persiapan: Java](../00-Persiapan/instalasi-java.md) |
| JVM | *Java Virtual Machine* | Mesin yang menjalankan *bytecode* Java | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |

---

## K

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Keadaan objek | *state* | Nilai-nilai atribut sebuah objek pada suatu saat; *method* bisa mengubahnya | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Kelas | *class* | Cetak biru yang mendefinisikan atribut dan *method* sebuah jenis objek | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Kelas abstrak | *abstract class* | Kelas yang tidak bisa dibuat objeknya dan boleh berisi *method* abstrak | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| Kelas akar | *root class* | Kelas paling atas yang menjadi induk semua kelas: `object` di Python, `Object` di Java | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Kelas anak | *subclass* | Kelas yang mewarisi kelas lain | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Kelas generik | *generic class* | Kelas dengan parameter tipe, misalnya `Pasangan<A, B>` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Kelas induk | *superclass* | Kelas yang diwarisi oleh kelas lain | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Kelas konkret | *concrete class* | Kelas biasa yang bisa dibuat objeknya, lawan dari kelas abstrak | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| Kelas pembungkus | *wrapper class* | Kelas Java yang membungkus tipe primitif, misalnya `Integer` untuk `int`; dibutuhkan saat menyimpan angka di dalam koleksi | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Kelas serba bisa | *god class* | Kelas yang mengerjakan terlalu banyak hal sekaligus; termasuk *code smell* | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| Kelas utilitas | *utility class* | Kelas yang hanya berisi *method* milik kelas sebagai pembantu, misalnya `Rupiah` di KedaiKita versi Java | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Kesamaan objek | *equality* | Dua objek dianggap sama isinya: `__eq__` di Python, `equals()` di Java | [P03](../Pertemuan-03-Atribut-dan-Method/README.md), [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| KISS | *Keep It Simple, Stupid* | Prinsip "buat sesederhana mungkin" | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| Kode *hash* | *hash code* | Angka "sidik jari" objek yang dipakai set dan dict/`Map` untuk mencari dengan cepat | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Koleksi | *collection* | Wadah berisi banyak objek, seperti *list*, set, dan dict/`Map` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Koleksi polimorfik | *polymorphic collection* | *List* atau *array* bertipe induk yang berisi objek dari berbagai kelas anak | [P09](../Pertemuan-09-Polimorfisme/README.md) |
| Kompilasi | *compilation* | Proses menerjemahkan kode sumber oleh *compiler* sebelum program dijalankan | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| Komposisi | *composition* | Relasi "punya" yang erat: bagian hanya milik satu pemilik dan ikut berakhir bersamanya, misalnya pesanan dan item pesanannya | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| Konstruktor | *constructor* | Bagian khusus kelas, mirip *method*, yang dijalankan otomatis saat objek dibuat untuk mengisi nilai awal atributnya. Di Java, konstruktor bernama sama dengan kelasnya dan bukan *method*; di Python, konstruktor ditulis sebagai *method* khusus `__init__` | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Konstruktor alternatif | *alternative constructor* | *Method* milik kelas yang membuat objek dari bentuk data lain, misalnya dari teks `"M02;Es Teh Manis;8000;Minuman"` | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |

---

## L

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Lambda* | *lambda* | Fungsi kecil tanpa nama, sering dipakai sebagai aturan pengurutan | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *List* | *list* | Koleksi berurutan yang boleh berisi data ganda; di Java: `List`/`ArrayList` | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| LSP | *Liskov Substitution Principle* | Prinsip SOLID: objek kelas anak harus bisa menggantikan objek kelas induk tanpa mengubah kebenaran program; kelas anak menepati semua janji induknya (lihat prasyarat dan jaminan hasil) | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |

---

## M

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Map / dict | *map*, *dictionary* | Koleksi pasangan kunci dan nilai, misalnya kode menu menuju objek `Menu` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Melempar *exception* | *throw*, *raise* | Memunculkan *exception* dengan sengaja: `raise` di Python, `throw` di Java; alur normal langsung berhenti | [P04](../Pertemuan-04-Enkapsulasi/README.md), [P11](../Pertemuan-11-Exception-Handling/README.md) |
| Melempar ulang | *re-raise*, *rethrow* | Meneruskan *exception* yang sedang ditangani ke pemanggil: `raise` saja di Python, `throw e;` di Java | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| Menangkap *exception* | *catch*, *except* | Menangani *exception* di blok `except` (Python) atau `catch` (Java) agar program tidak berhenti mendadak | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| Mengirim pesan | *message passing* | Meminta objek melakukan sesuatu; di kode berwujud pemanggilan *method*, misalnya `kopi.hitung_total(2)` | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Merambat | *propagate* | Perjalanan *exception* yang tidak ditangkap: naik dari *method* ke pemanggilnya, terus sampai ada yang menangkap | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| *Method* | *method* | Perilaku atau aksi yang bisa dilakukan objek | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| *Method* abstrak | *abstract method* | *Method* tanpa isi yang wajib diisi (di-*override*) oleh kelas anak yang konkret | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| *Method* milik kelas | *class method*, *static method* | *Method* yang dipanggil lewat nama kelas, bukan lewat objek: `@classmethod` atau `@staticmethod` di Python, `static` di Java | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| *Method reference* | *method reference* | Singkatan *lambda* di Java, misalnya `Menu::getHarga` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Modul | *module* | *File* Python berisi kode yang bisa di-`import` oleh *file* lain | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| MRO | *Method Resolution Order* | Urutan Python mencari *method* saat sebuah kelas mewarisi beberapa kelas | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Multiplisitas | *multiplicity* | Jumlah objek yang terlibat dalam sebuah relasi, misalnya `1`, `0..1`, `*` | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |

---

## N

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Name mangling* | *name mangling* | Python mengganti nama atribut `__nama` menjadi `_Kelas__nama`; ini bukan fitur keamanan | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| Nilai bawaan | *default value* | Nilai yang otomatis dipakai parameter jika argumennya tidak dikirim, misalnya `stok=0` di Python. Java tidak mengenalnya dan memakai *overloading* sebagai gantinya | [P03](../Pertemuan-03-Atribut-dan-Method/README.md), [P09](../Pertemuan-09-Polimorfisme/README.md) |
| Nilai kembalian | *return value* | Nilai yang dikirim balik oleh fungsi atau *method* dengan `return` | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| `None` / `null` | *None*, *null* | Nilai khusus yang berarti "tidak menunjuk objek apa pun" | [P03](../Pertemuan-03-Atribut-dan-Method/README.md), [P05](../Pertemuan-05-Relasi-Antarkelas/README.md) |
| Notasi titik | *dot notation* | Cara mengakses atribut dan *method*: `objek.atribut`, `objek.method()` | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |

---

## O

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Objek | *object*, *instance* | Wujud nyata yang dibuat dari kelas dan menyimpan datanya sendiri; disebut juga *instance* | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| *Observer* | *observer* | Pola desain: para pengamat (*observer*) otomatis diberi tahu setiap kali objek yang diamati (*subject*) berubah | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| OCP | *Open/Closed Principle* | Prinsip SOLID: terbuka untuk ditambah, tertutup untuk diubah | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Overloading* | *overloading* | Beberapa *method* atau konstruktor bernama sama dengan parameter berbeda (Java) | [P03](../Pertemuan-03-Atribut-dan-Method/README.md), [P09](../Pertemuan-09-Polimorfisme/README.md) |
| *Override* | *override* | Kelas anak menulis ulang *method* yang diwarisi dari kelas induk; di Java ditandai anotasi `@Override` | [P07](../Pertemuan-07-Pewarisan/README.md) |

---

## P

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Package* (paket) | *package* | Pengelompokan kelas atau modul dalam folder bernama | [P04](../Pertemuan-04-Enkapsulasi/README.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Paradigma pemrograman | *programming paradigm* | Cara pandang dalam menyusun program, misalnya prosedural atau berorientasi objek | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| Parameter | *parameter* | Variabel di definisi fungsi atau *method* yang menerima nilai saat fungsi atau *method* itu dipanggil | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| `PATH` | *PATH environment variable* | Daftar folder tempat sistem operasi mencari perintah seperti `python`, `java`, dan `javac` | [Persiapan: Python](../00-Persiapan/instalasi-python.md), [Java](../00-Persiapan/instalasi-java.md) |
| Pemeriksa tipe | *type checker* | Alat yang memeriksa kecocokan tipe sebelum program dijalankan, misalnya mypy atau Pylance di VS Code. Pemeriksaan Pylance mati secara bawaan; nyalakan lewat pengaturan **Python › Analysis: Type Checking Mode** | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md), [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| Pemrograman berorientasi objek (PBO) | *object-oriented programming* (OOP) | Paradigma yang menyusun program sebagai kumpulan objek yang membawa data dan perilakunya sendiri, lalu saling bekerja sama | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| Pemrograman prosedural | *procedural programming* | Paradigma yang menyusun program sebagai urutan langkah dan fungsi; datanya terpisah dari fungsi-fungsi yang mengolahnya | [P01](../Pertemuan-01-Pengenalan-PBO/README.md) |
| Persistensi | *persistence* | Kemampuan menyimpan data, misalnya ke *file* CSV, agar tetap ada setelah program ditutup | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Pewarisan | *inheritance* | Kelas anak mewarisi atribut dan *method* dari kelas induk | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P07](../Pertemuan-07-Pewarisan/README.md) |
| Pewarisan bertingkat | *multilevel inheritance* | Rantai pewarisan lebih dari satu tingkat: induk, anak, cucu, dan seterusnya | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Pewarisan ganda | *multiple inheritance* | Satu kelas mewarisi lebih dari satu kelas induk; Python mengizinkan, Java tidak | [P07](../Pertemuan-07-Pewarisan/README.md) |
| Pintu masuk program | *entry point* | Bagian yang dijalankan pertama kali: blok `if __name__ == "__main__":` (misalnya di `main.py`) di Python, *method* `main` (misalnya di kelas `Main`) di Java | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P05](../Pertemuan-05-Relasi-Antarkelas/README.md) |
| Polimorfisme | *polymorphism* | Satu perintah yang sama menghasilkan perilaku berbeda sesuai objek penerimanya | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P09](../Pertemuan-09-Polimorfisme/README.md) |
| Prasyarat | *precondition* | Syarat yang harus dipenuhi pemanggil sebelum memanggil *method*, misalnya "jumlah porsi minimal 1"; kelas anak tidak boleh memperketatnya (LSP) | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Property* | *property* | Fitur Python `@property` untuk membuat *getter* dan *setter* yang diakses seperti atribut biasa | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| `protected` | *protected* | *Access modifier* Java: bisa diakses kelas anak dan kelas lain dalam *package* yang sama | [P04](../Pertemuan-04-Enkapsulasi/README.md), [P07](../Pertemuan-07-Pewarisan/README.md) |
| `Protocol` | *protocol*, *structural typing* | Kontrak struktural Python (`typing.Protocol`): kelas cukup punya *method* yang sama, tanpa mewarisi. Kecocokannya diperiksa pemeriksa tipe, bukan oleh Python saat program berjalan | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |

---

## R

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Realisasi | *realization* | Relasi UML antara *interface* dan kelas yang mengimplementasikannya | [P06](../Pertemuan-06-UML-Class-Diagram/README.md), [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| *Refactoring* | *refactoring* | Mengubah struktur kode tanpa mengubah perilakunya | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| Referensi | *reference* | Penunjuk yang disimpan variabel untuk menuju sebuah objek di memori | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Relasi antarkelas | *class relationship* | Hubungan yang membuat objek dari satu kelas bisa memakai, mengenal, atau memiliki objek kelas lain: dependensi, asosiasi, agregasi, dan komposisi | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md) |
| Repositori | *repository* | (1) Folder proyek yang riwayat perubahannya dicatat oleh Git. (2) Di P15: kelas yang menjembatani objek dengan tempat penyimpanan, misalnya `RepositoriMenuCSV` | [Persiapan: Git](../00-Persiapan/git-dan-github.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Representasi teks objek | *string representation* | Teks yang muncul saat objek dicetak: `__str__` di Python, `toString()` di Java | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |

---

## S

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| `self` / `this` | *self*, *this* | Kata ganti untuk objek yang sedang menjalankan *method* | [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| Set | *set* | Koleksi tanpa data ganda; di Java: `Set`, `HashSet`, `TreeSet` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *Setter* | *setter* | *Method* untuk mengubah nilai atribut yang disembunyikan, biasanya sambil memvalidasi | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| *Singleton* | *singleton* | Pola desain yang menjamin sebuah kelas hanya punya satu objek | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| SOLID | *SOLID principles* | Lima prinsip desain berorientasi objek: SRP, OCP, LSP, ISP, dan DIP | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| SRP | *Single Responsibility Principle* | Prinsip SOLID: satu kelas sebaiknya hanya punya satu alasan untuk berubah | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| *Stack trace* / *traceback* | *stack trace*, *traceback* | Laporan jejak pemanggilan *method* saat terjadi *error* | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| `static` | *static* | Kata kunci Java untuk anggota milik kelas, bukan milik objek; padanannya di Python: atribut kelas, `@classmethod`, dan `@staticmethod` | [P03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| Stereotip | *stereotype* | Penanda jenis kelas di diagram UML, misalnya `<<interface>>` atau `<<utility>>` | [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| *Strategy* | *strategy* | Pola desain: aturan atau algoritma dibungkus dalam objek sehingga bisa ditukar saat program berjalan | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| `super` | *super* | Cara merujuk ke kelas induk dari dalam kelas anak, misalnya untuk memanggil konstruktor atau *method*-nya. Di Python, `super()` dipanggil seperti fungsi; di Java, `super` adalah kata kunci | [P07](../Pertemuan-07-Pewarisan/README.md) |

---

## T

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| *Tell, don't ask* | *tell, don't ask* | Prinsip "suruh objek mengerjakan tugasnya", alih-alih mengambil datanya lalu mengolahnya di luar objek | [P04](../Pertemuan-04-Enkapsulasi/README.md) |
| *Template method* | *template method* | *Method* di kelas induk yang menyusun langkah-langkah, sebagian langkahnya diisi kelas anak | [P10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md), [P14](../Pertemuan-14-Design-Pattern/README.md) |
| Terminal | *terminal*, *command line* | Jendela untuk memberi perintah ke komputer dengan mengetik | [Persiapan: Menjalankan Program](../00-Persiapan/menjalankan-program.md) |
| *Thread-safe* | *thread-safe* | Tetap benar walaupun dipakai beberapa *thread* (alur kerja) sekaligus; *Singleton* versi *lazy* yang sederhana belum *thread-safe* | [P14](../Pertemuan-14-Design-Pattern/README.md) |
| `throws` | *throws clause* | Klausa Java di kepala *method* yang mengumumkan *exception* yang mungkin dilempar *method* itu. Jangan tertukar dengan `throw`, yang benar-benar melempar | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| Tipe dinamis dan tipe statis | *dynamic typing*, *static typing* | Python memeriksa tipe saat program berjalan; Java memeriksanya saat kompilasi | [P01](../Pertemuan-01-Pengenalan-PBO/README.md), [P02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| *Try-with-resources* | *try-with-resources* | Bentuk `try` di Java yang otomatis menutup sumber daya seperti *file* | [P11](../Pertemuan-11-Exception-Handling/README.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| *Tuple* | *tuple* | Koleksi berurutan di Python yang isinya tidak bisa diubah, misalnya `("M01", 18000)` | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| *Type hint* (petunjuk tipe) | *type hint* | Keterangan tipe di Python, misalnya `harga: int`, yang tidak diperiksa saat program berjalan | [P05](../Pertemuan-05-Relasi-Antarkelas/README.md), [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |

---

## U

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| UML | *Unified Modeling Language* | Bahasa pemodelan visual standar untuk merancang perangkat lunak | [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |
| *Unchecked exception* | *unchecked exception* | *Exception* Java turunan `RuntimeException` yang tidak wajib ditangkap atau diumumkan dengan `throws`. Aturan yang sama berlaku untuk turunan `Error` | [P11](../Pertemuan-11-Exception-Handling/README.md) |
| *Unit test* (pengujian unit) | *unit test* | Kode kecil yang memeriksa sebagian program secara otomatis | [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| *Upcasting* | *upcasting* | Memperlakukan objek kelas anak sebagai tipe induknya; terjadi otomatis | [P09](../Pertemuan-09-Polimorfisme/README.md) |
| Urutan alami | *natural ordering* | Aturan urutan baku yang ditulis di dalam kelas: `__lt__` di Python, `compareTo()` dari `Comparable` di Java | [P12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |

---

## V

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| Validasi | *validation* | Pemeriksaan agar data yang masuk ke objek masuk akal, misalnya harga harus lebih dari 0 | [P04](../Pertemuan-04-Enkapsulasi/README.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |
| Visibilitas | *visibility* | Simbol hak akses di UML: `+` publik, `-` privat, `#` *protected*, `~` *package* | [P06](../Pertemuan-06-UML-Class-Diagram/README.md) |

---

## W

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| `with` | *with statement*, *context manager* | Pernyataan Python yang otomatis menutup sumber daya seperti *file* setelah selesai dipakai | [P11](../Pertemuan-11-Exception-Handling/README.md), [P15](../Pertemuan-15-Proyek-Terintegrasi/README.md) |

---

## Y

| Istilah | Inggris | Arti singkat | Dibahas di |
|---|---|---|---|
| YAGNI | *You Aren't Gonna Need It* | Prinsip "jangan membuat fitur yang belum dibutuhkan" | [P13](../Pertemuan-13-Prinsip-SOLID/README.md) |

---

Ada istilah yang membingungkan tetapi belum tercantum? Usulkan lewat [Issues GitHub](https://github.com/antonprafanto/PBO2026/issues) atau sampaikan ke dosen.

[🏠 Beranda](../README.md) · [Lampiran](README.md) · **Glosarium** · [*Cheat Sheet* Python ↔ Java](cheatsheet-python-java.md) · [Referensi](referensi.md) · [FAQ](faq.md)
