# Rencana Pembelajaran Semester — Pemrograman Berorientasi Objek 2026

[🏠 Beranda](README.md) · [Persiapan ➡️](00-Persiapan/README.md)

> Dokumen ini merangkum arah mata kuliah selama satu semester: kemampuan apa yang akan kamu kuasai, urutan materinya, cara belajarnya, dan cara penilaiannya. Bacalah sekali di awal semester, lalu buka lagi setiap kali kamu ingin melihat "peta besarnya".

## Daftar Isi

1. [Identitas Mata Kuliah](#1-identitas-mata-kuliah)
2. [Deskripsi Mata Kuliah](#2-deskripsi-mata-kuliah)
3. [Capaian Pembelajaran Mata Kuliah (CPMK)](#3-capaian-pembelajaran-mata-kuliah-cpmk)
4. [Sub-CPMK per Pertemuan](#4-sub-cpmk-per-pertemuan)
5. [Rencana 16 Pertemuan](#5-rencana-16-pertemuan)
6. [Metode Pembelajaran](#6-metode-pembelajaran)
7. [Ritme dan Beban Belajar](#7-ritme-dan-beban-belajar)
8. [Penilaian](#8-penilaian)
9. [Proyek Akhir](#9-proyek-akhir)
10. [Kejujuran Akademik dan Penggunaan AI](#10-kejujuran-akademik-dan-penggunaan-ai)
11. [Referensi](#11-referensi)

---

## 1. Identitas Mata Kuliah

| | |
|---|---|
| Mata kuliah | Pemrograman Berorientasi Objek (PBO) |
| Program studi | Informatika |
| Perguruan tinggi | Universitas Mulawarman, Samarinda, Kalimantan Timur |
| Tahun | 2026 |
| Jumlah pertemuan | 16: 14 pertemuan materi, Ujian Tengah Semester (Pertemuan 08), dan Ujian Akhir Semester (Pertemuan 16) |
| Bahasa pemrograman | Python dan Java, dengan dua jalur praktik (mahasiswa memilih satu jalur utama) |
| Versi perangkat lunak | Python 3.10 ke atas (disarankan 3.12 atau lebih baru); Java 17 ke atas (disarankan JDK LTS 21 atau 25) |
| Kemampuan awal yang diharapkan | dasar pemrograman: variabel, tipe data, percabangan, perulangan, fungsi, dan list/array |
| Bahasa pengantar materi | Bahasa Indonesia |

> [!NOTE]
> Informasi administratif seperti bobot SKS, semester, jadwal kelas, dan nama dosen pengampu mengikuti ketentuan program studi dan diumumkan oleh dosen di kelas.

## 2. Deskripsi Mata Kuliah

Mata kuliah ini memperkenalkan **paradigma pemrograman berorientasi objek** (PBO): cara membangun program sebagai kumpulan objek yang menyimpan data dan perilakunya sendiri, lalu saling bekerja sama.

Mahasiswa mempelajari kelas dan objek, enkapsulasi, relasi antarkelas, diagram kelas UML, pewarisan, polimorfisme, kelas abstrak dan *interface*, penanganan *exception*, koleksi dan *generics*, prinsip desain SOLID, serta *design pattern* dasar. Semua konsep itu akhirnya dipadukan menjadi sebuah aplikasi utuh yang berlapis, menyimpan data ke file, dan diuji secara otomatis.

Setiap konsep diajarkan **tanpa terikat bahasa** lebih dulu, kemudian dipraktikkan dalam **Python** dan **Java**. Sepanjang semester, mahasiswa membangun satu studi kasus yang terus berkembang, yaitu aplikasi kasir kafe **KedaiKita**, sehingga terlihat jelas bagaimana setiap konsep memperbaiki program yang nyata.

## 3. Capaian Pembelajaran Mata Kuliah (CPMK)

Setelah menyelesaikan mata kuliah ini, mahasiswa mampu:

| Kode | Rumusan capaian |
|---|---|
| CPMK-1 | Menjelaskan konsep dasar PBO (kelas, objek, atribut, method, dan empat pilar PBO) serta membandingkannya dengan paradigma prosedural. |
| CPMK-2 | Menerapkan kelas, objek, enkapsulasi, dan relasi antarkelas untuk memodelkan masalah sederhana dalam Python atau Java. |
| CPMK-3 | Membaca dan merancang diagram kelas UML, lalu menerjemahkannya menjadi kode dan sebaliknya. |
| CPMK-4 | Menerapkan pewarisan, polimorfisme, kelas abstrak, dan *interface* untuk membangun program yang mudah dikembangkan. |
| CPMK-5 | Membangun program yang tangguh dengan penanganan *exception* serta pemilihan koleksi dan *generics* yang tepat. |
| CPMK-6 | Menganalisis dan memperbaiki desain program menggunakan prinsip SOLID dan *design pattern* dasar. |
| CPMK-7 | Mengembangkan, menguji, dan mempresentasikan aplikasi berorientasi objek yang terintegrasi secara jujur dan bertanggung jawab. |

## 4. Sub-CPMK per Pertemuan

Sub-CPMK adalah kemampuan akhir yang diharapkan pada setiap pertemuan. Kodenya mengikuti nomor pertemuan. Pertemuan 08 dan 16 tidak punya Sub-CPMK baru karena keduanya adalah pekan evaluasi.

Kolom **Level** memakai taksonomi Bloom yang direvisi: C2 memahami, C3 menerapkan, C4 menganalisis, C5 mengevaluasi, C6 mencipta.

| Kode | Kemampuan akhir yang diharapkan | CPMK | Level |
|---|---|---|---|
| Sub-CPMK 01 | Menjelaskan perbedaan paradigma prosedural dan berorientasi objek, serta mengenali calon kelas, atribut, dan method dari sebuah masalah sederhana. | CPMK-1 | C2 |
| Sub-CPMK 02 | Membuat kelas dengan konstruktor, atribut, dan method, lalu membuat beberapa objek yang mandiri dari kelas tersebut. | CPMK-1, CPMK-2 | C3 |
| Sub-CPMK 03 | Membedakan atribut dan method milik objek dengan milik kelas, membuat representasi teks objek, serta menjelaskan referensi dan *aliasing*. | CPMK-2 | C3 |
| Sub-CPMK 04 | Menerapkan enkapsulasi (*access modifier*, *getter*/*setter* atau `@property`, dan validasi) agar data objek selalu valid. | CPMK-2 | C3 |
| Sub-CPMK 05 | Menerapkan relasi dependensi, asosiasi, agregasi, dan komposisi dalam program yang terdiri atas beberapa file. | CPMK-2 | C3 |
| Sub-CPMK 06 | Membaca dan membuat diagram kelas UML, serta menerjemahkan diagram menjadi kode dan kode menjadi diagram. | CPMK-3 | C4 |
| Sub-CPMK 07 | Menerapkan pewarisan, *override*, dan `super`, serta menentukan kapan memakai pewarisan (*is-a*) atau komposisi (*has-a*). | CPMK-4 | C4 |
| Sub-CPMK 09 | Menerapkan polimorfisme melalui *override* dan koleksi polimorfik, serta membedakannya dengan *overloading*. | CPMK-4 | C3 |
| Sub-CPMK 10 | Merancang kelas abstrak dan *interface* yang tepat untuk sebuah kebutuhan. | CPMK-4 | C4 |
| Sub-CPMK 11 | Menangani kesalahan dengan *exception*, termasuk membuat dan melempar *exception* buatan sendiri. | CPMK-5 | C3 |
| Sub-CPMK 12 | Memilih koleksi yang tepat, memakai *generics*, mengurutkan objek, dan mendefinisikan kesamaan objek. | CPMK-5 | C4 |
| Sub-CPMK 13 | Menganalisis pelanggaran prinsip SOLID dan melakukan *refactoring* tanpa mengubah perilaku program. | CPMK-6 | C5 |
| Sub-CPMK 14 | Menerapkan pola Singleton, Factory, Strategy, dan Observer pada masalah yang sesuai. | CPMK-6 | C4 |
| Sub-CPMK 15 | Membangun aplikasi berorientasi objek berlapis yang menyimpan data ke file dan diuji dengan *unit test*. | CPMK-7 | C6 |

## 5. Rencana 16 Pertemuan

Kode aktivitas: **K** = kuliah konsep, **P** = praktikum Python/Java, **J** = jembatan Python ↔ Java, **L** = latihan dan tugas mandiri, **Q** = kuis.

| Pertemuan | Kemampuan akhir | Materi pokok | Studi kasus KedaiKita | Aktivitas |
|---|---|---|---|---|
| [01](Pertemuan-01-Pengenalan-PBO/README.md) | Sub-CPMK 01 | paradigma pemrograman, masalah program prosedural, cara pandang objek, empat pilar sekilas, pemanasan dasar Python/Java | versi prosedural (data tertukar) vs kilasan versi objek | K, P, J, L, Q |
| [02](Pertemuan-02-Kelas-dan-Objek/README.md) | Sub-CPMK 02 | kelas, objek, instansiasi, konstruktor, `self`/`this`, method, diagram kelas sederhana | kelas `Menu` pertama | K, P, J, L, Q |
| [03](Pertemuan-03-Atribut-dan-Method/README.md) | Sub-CPMK 03 | atribut objek vs atribut kelas, method kelas dan *static*, konstruktor lanjutan, `__str__`/`toString()`, referensi dan `None`/`null` | `Menu` lengkap, format Rupiah, `Pelanggan` dan poin | K, P, J, L, Q |
| [04](Pertemuan-04-Enkapsulasi/README.md) | Sub-CPMK 04 | *information hiding*, *access modifier*, *getter*/*setter*, `@property`, validasi, atribut *read-only* | harga tervalidasi, stok dan poin lewat method resmi | K, P, J, L, Q |
| [05](Pertemuan-05-Relasi-Antar-Kelas/README.md) | Sub-CPMK 05 | dependensi, asosiasi, agregasi, komposisi, multiplisitas, program multi-file, `ArrayList` dasar | `ItemPesanan`, `Pesanan`, `Kedai` | K, P, J, L, Q |
| [06](Pertemuan-06-UML-Class-Diagram/README.md) | Sub-CPMK 06 | notasi kelas UML, visibilitas, relasi dan multiplisitas, *forward* dan *reverse engineering*, Mermaid | diagram kelas lengkap KedaiKita | K, P, J, L, Q |
| [07](Pertemuan-07-Pewarisan/README.md) | Sub-CPMK 07 | generalisasi, kelas induk dan anak, `super`, *override*, `protected`, pewarisan bertingkat, *is-a* vs *has-a* | `Makanan` dan `Minuman` | K, P, J, L, Q |
| [08](Pertemuan-08-UTS/README.md) | Sub-CPMK 01–07 | Ujian Tengah Semester: teori dan praktik | (kasus ujian baru) | ulasan, latihan soal, ujian |
| [09](Pertemuan-09-Polimorfisme/README.md) | Sub-CPMK 09 | *override* dan *dynamic dispatch*, *upcasting* dan *downcasting*, *overloading*, *duck typing*, koleksi polimorfik | tiga metode pembayaran | K, P, J, L, Q |
| [10](Pertemuan-10-Abstract-Class-dan-Interface/README.md) | Sub-CPMK 10 | abstraksi, kelas abstrak, *interface*, *default method*, `Protocol`, kelas abstrak vs *interface* | `Pembayaran` abstrak, `DapatDicetak` | K, P, J, L, Q |
| [11](Pertemuan-11-Exception-Handling/README.md) | Sub-CPMK 11 | jenis kesalahan, `try`/`except`/`catch`/`finally`, `raise`/`throw`, hierarki *exception*, *checked* vs *unchecked*, *exception* buatan sendiri | `KedaiError` dan turunannya | K, P, J, L, Q |
| [12](Pertemuan-12-Koleksi-dan-Generics/README.md) | Sub-CPMK 12 | list, set, dict vs `List`, `Set`, `Map`; *generics*; pengurutan dengan *key*/`Comparator`; `equals`/`hashCode` | menu per kode, `Pasangan`, `LaporanPenjualan` | K, P, J, L, Q |
| [13](Pertemuan-13-Prinsip-SOLID/README.md) | Sub-CPMK 13 | *code smell*, SRP, OCP, LSP, ISP, DIP, *refactoring*, DRY, KISS, YAGNI | `KasirSerbaBisa` sebelum dan sesudah *refactoring* | K, P, J, L, Q |
| [14](Pertemuan-14-Design-Pattern/README.md) | Sub-CPMK 14 | Singleton, Factory, Strategy, Observer, wawasan pola lain | pajak, `PembayaranFactory`, diskon *happy hour*, notifikasi | K, P, J, L, Q |
| [15](Pertemuan-15-Proyek-Terintegrasi/README.md) | Sub-CPMK 15 | arsitektur berlapis, package, file CSV, validasi input, *unit test*, peta konsep P02–P14 | aplikasi kasir lengkap + mode demo | K, P, J, L, Q, mulai proyek akhir |
| [16](Pertemuan-16-UAS/README.md) | Sub-CPMK 09–15 | Ujian Akhir Semester: teori dan praktik; presentasi proyek akhir; refleksi | (kasus ujian baru) | ulasan, latihan soal, ujian, presentasi |

## 6. Metode Pembelajaran

| Metode | Bentuknya di mata kuliah ini |
|---|---|
| Kuliah interaktif | Dosen membuka setiap topik dengan masalah nyata dan analogi, lalu berdiskusi bersama mahasiswa (bagian **Konsep**). |
| Praktikum terbimbing | Mahasiswa menjalankan, mengubah, dan menjelaskan kode contoh di jalur pilihannya (bagian **Praktik**). |
| Pembelajaran berbasis kasus | Studi kasus KedaiKita tumbuh setiap minggu sehingga setiap konsep terlihat manfaatnya. |
| Perbandingan dua bahasa | Halaman **Jembatan** melatih kemampuan membaca konsep yang sama dalam dua bahasa. |
| Latihan bertingkat | Soal bertingkat Dasar, Menengah, dan Tantangan, lengkap dengan petunjuk dan solusi. |
| Asesmen formatif | Kuis 10 soal di setiap pertemuan untuk mengukur pemahaman sendiri. |
| Pembelajaran berbasis proyek | Proyek akhir yang memadukan semua konsep, dikerjakan bertahap di akhir semester. |
| Diskusi dan tinjauan sejawat | Mahasiswa saling membaca kode, memberi masukan, dan menjelaskan solusinya. |

## 7. Ritme dan Beban Belajar

Untuk setiap pertemuan materi, alokasikan waktu kira-kira seperti berikut:

| Kegiatan | Perkiraan waktu |
|---|---|
| Membaca konsep | 40 menit |
| Praktik di jalur pilihan | 90 menit |
| Membaca jembatan Python ↔ Java | 15 menit |
| Mengerjakan latihan | 60 menit |
| Mengerjakan kuis | 15 menit |
| **Total** | **sekitar 3,5 jam**, belum termasuk tugas mandiri |

> [!TIP]
> Belajar 30–45 menit setiap hari jauh lebih efektif daripada belajar 4 jam sekaligus sehari sebelum ujian. Materi PBO saling bertumpuk: Pertemuan 09 sulit dipahami jika Pertemuan 07 belum dikuasai.

## 8. Penilaian

### Komponen penilaian

| Komponen | Bentuk | CPMK yang diukur |
|---|---|---|
| Latihan dan tugas mandiri | tugas mandiri di akhir setiap `latihan.md`, dikumpulkan sesuai arahan dosen | CPMK-1 sampai CPMK-6 |
| Kuis | kuis di kelas atau daring, dengan bentuk serupa kuis setiap pertemuan | CPMK-1 sampai CPMK-6 |
| UTS | teori dan praktik, cakupan Pertemuan 01–07 | CPMK-1 sampai CPMK-4 |
| Proyek akhir | aplikasi, dokumen desain, dan presentasi | CPMK-2 sampai CPMK-7 |
| UAS | teori dan praktik, cakupan Pertemuan 09–15 (beserta dasar-dasar sebelumnya) | CPMK-4 sampai CPMK-7 |

### Bobot penilaian

> [!IMPORTANT]
> Tabel berikut adalah **komposisi yang disarankan, dapat disesuaikan oleh dosen pengampu**. Bobot yang berlaku di kelasmu adalah bobot yang diumumkan dosen.

| Komponen | Bobot yang disarankan |
|---|---|
| Latihan dan tugas mandiri | 15% |
| Kuis | 10% |
| UTS | 20% |
| Proyek akhir | 30% |
| UAS | 25% |
| **Total** | **100%** |

Catatan penting:

- Latihan, kuis, dan latihan soal UTS/UAS di repositori ini bersifat **publik** dan dilengkapi kunci jawaban. Fungsinya untuk berlatih. Kuis, tugas, dan ujian yang **dinilai** diberikan terpisah oleh dosen.
- Konversi nilai angka menjadi nilai huruf mengikuti ketentuan yang berlaku di Universitas Mulawarman.

## 9. Proyek Akhir

Proyek akhir adalah kesempatanmu membuktikan bahwa kamu bisa merancang dan membangun aplikasi berorientasi objek **sendiri**, bukan sekadar mengikuti contoh. Spesifikasi lengkapnya ada di [Spesifikasi Proyek Akhir](Pertemuan-15-Proyek-Terintegrasi/proyek-akhir.md) (bagian dari [Pertemuan 15](Pertemuan-15-Proyek-Terintegrasi/README.md)).

Ringkasannya:

- **Tema bebas, asalkan bukan kafe.** Contohnya perpustakaan, rental kendaraan, bengkel, apotek, bioskop, kos-kosan, *laundry*, klinik hewan, *event* kampus, atau bank sampah.
- **Bahasa:** Python **atau** Java.
- **Kebutuhan minimum:** paling sedikit 6 kelas; enkapsulasi; minimal satu hierarki pewarisan; polimorfisme; minimal satu kelas abstrak atau *interface*; *exception* buatan sendiri; koleksi; simpan dan muat data ke file; minimal satu *design pattern*; minimal 5 *unit test*; diagram kelas UML; serta README berisi cara menjalankan program.
- **Tahapan:** analisis kebutuhan → rancangan diagram kelas → implementasi bertahap → pengujian → presentasi dan demo di akhir semester.
- **Yang dinilai:** kebenaran program, kualitas desain berorientasi objek, kerapian kode, pengujian, dokumentasi, dan kemampuanmu menjelaskan kode sendiri saat presentasi.

> [!TIP]
> Jadikan KedaiKita sebagai "contoh berjalan". Saat bingung bagaimana menerapkan sebuah konsep di proyekmu, lihat bagaimana KedaiKita menerapkannya, lalu sesuaikan dengan temamu.

## 10. Kejujuran Akademik dan Penggunaan AI

Tujuan mata kuliah ini adalah **kemampuanmu sendiri**. Nilai yang bagus tanpa kemampuan tidak akan menolongmu di mata kuliah berikutnya maupun di dunia kerja.

### Aturan kejujuran akademik

- Tugas individu dikerjakan **sendiri**. Berdiskusi tentang konsep itu baik, tetapi tulislah kodemu sendiri.
- Menyalin kode teman, kakak tingkat, atau internet lalu mengakuinya sebagai karya sendiri adalah **plagiarisme**.
- Jika kamu memakai potongan kode dari sumber lain, **cantumkan sumbernya** di komentar atau laporan.
- Pada proyek kelompok (jika diizinkan dosen), setiap anggota harus bisa menjelaskan **seluruh** bagian proyek, bukan hanya bagiannya sendiri.

### Memakai AI secara bertanggung jawab

Asisten AI (misalnya chatbot atau fitur pelengkap kode di editor) bisa menjadi teman belajar yang sangat membantu jika dipakai dengan benar.

| Boleh dan dianjurkan | Tidak boleh |
|---|---|
| Meminta penjelasan konsep dengan bahasa yang lebih sederhana atau dengan contoh lain | Menyerahkan kode buatan AI yang tidak kamu pahami sebagai tugasmu |
| Meminta bantuan memahami pesan error, lalu memperbaikinya sendiri | Memakai AI saat kuis atau ujian, kecuali dosen mengizinkannya secara tertulis |
| Meminta soal latihan tambahan atau umpan balik atas kode yang sudah kamu tulis | Menyembunyikan bantuan AI yang kamu pakai |
| Membandingkan solusimu dengan saran AI, lalu menilai mana yang lebih baik dan mengapa | Mempercayai jawaban AI tanpa menjalankan dan memeriksa kodenya |

Prinsip praktisnya:

1. **Coba sendiri dulu.** Pakai AI setelah kamu benar-benar berusaha, bukan sebagai langkah pertama.
2. **Pahami setiap baris.** Jika kamu tidak bisa menjelaskan sebuah baris kode, jangan kumpulkan baris itu.
3. **Cantumkan bantuan yang dipakai**, misalnya: "Bagian validasi input dibuat dengan bantuan AI, lalu saya ubah agar sesuai kebutuhan." Kejujuran seperti ini dihargai.
4. **Siap diuji lisan.** Dosen dapat meminta kamu menjelaskan atau mengubah kodemu secara langsung.

> [!WARNING]
> AI bisa salah dengan sangat meyakinkan, misalnya memakai sintaks yang tidak ada atau versi bahasa yang berbeda. Selalu jalankan dan uji kodenya. Kebijakan penggunaan AI yang berlaku di kelasmu mengikuti ketentuan dosen pengampu.

## 11. Referensi

Referensi utama mata kuliah ini:

1. Materi di repositori ini (konsep, praktik, jembatan, latihan, dan kuis setiap pertemuan).
2. Dokumentasi resmi Python: *The Python Tutorial*, terutama bab tentang kelas.
3. Dokumentasi resmi Java: Learn Java di dev.java dan *The Java Tutorials* dari Oracle.
4. Erich Gamma, Richard Helm, Ralph Johnson, dan John Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*.
5. Martin Fowler, *UML Distilled*.

Daftar lengkap buku, dokumentasi, dan situs belajar ada di [Lampiran: Referensi](Lampiran/referensi.md).

---

[🏠 Beranda](README.md) · [Persiapan ➡️](00-Persiapan/README.md)
