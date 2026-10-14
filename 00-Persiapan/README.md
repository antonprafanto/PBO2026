# Persiapan Belajar

[🏠 Beranda](../README.md) · [Pertemuan 01 ➡️](../Pertemuan-01-Pengenalan-PBO/README.md)

> Sebelum masuk Pertemuan 01, kita siapkan dulu "dapur"-nya: bahasa pemrograman, materi kuliah di laptopmu, editor kode, dan cara menjalankan program. Bagian ini cukup dikerjakan **sekali**, kira-kira 1—2 jam. Setelah itu, kamu bisa fokus belajar tanpa terganggu urusan teknis.

## 🎯 Tujuan Pembelajaran

Setelah menyelesaikan bagian persiapan ini, kamu mampu:

1. Memasang Python dan/atau JDK (Java) dengan versi yang sesuai.
2. Mengunduh materi ke laptopmu dan memperbaruinya setiap minggu.
3. Memasang VS Code beserta ekstensi Python dan/atau Java.
4. Membuka folder materi dengan benar di VS Code.
5. Menjalankan program Python dan Java dari terminal maupun dari VS Code.

## Daftar Isi

1. [Pilih Jalurmu Dulu](#1-pilih-jalurmu-dulu)
2. [Daftar Panduan Persiapan](#2-daftar-panduan-persiapan)
3. [Alur Persiapan](#3-alur-persiapan)
4. [Uji Coba: Apakah Semuanya Sudah Siap?](#4-uji-coba-apakah-semuanya-sudah-siap)
5. [*Checklist* Siap Belajar](#5-checklist-siap-belajar)
6. [Kalau Ada Masalah](#6-kalau-ada-masalah)

---

## 1. Pilih Jalurmu Dulu

Mata kuliah ini punya dua jalur praktik: 🐍 **Python** dan ☕ **Java**. Konsepnya sama, yang berbeda hanya bahasanya. Pilihanmu menentukan apa yang wajib dipasang.

| Jalur | Wajib dipasang | Sangat disarankan |
|---|---|---|
| 🐍 Python | Python 3.10 ke atas (disarankan 3.12 atau lebih baru) | VS Code + ekstensi Python |
| ☕ Java | JDK 17 ke atas (disarankan JDK 25 atau 21, keduanya LTS) | VS Code + Extension Pack for Java |

> [!TIP]
> Jika laptopmu cukup lega, pasang **keduanya**. Kamu jadi bisa mencoba kode di jalur lain saat membaca halaman Jembatan Python ↔ Java. Namun, kalau waktumu terbatas, pasang yang sesuai jalurmu dulu.

Belum yakin memilih jalur yang mana? Baca bagian [Dua Jalur di Beranda](../README.md#2-dua-jalur-python-dan-java) atau [FAQ](../Lampiran/faq.md).

## 2. Daftar Panduan Persiapan

Ikuti panduan berikut secara berurutan. Lewati yang tidak kamu perlukan, misalnya panduan 2 jika kamu hanya memilih jalur Python.

| No | Panduan | Isinya | Untuk siapa |
|---|---|---|---|
| 1 | [Instalasi Python](instalasi-python.md) | memasang Python di Windows, macOS, dan Linux, lalu memeriksa versinya | jalur Python |
| 2 | [Instalasi Java (JDK)](instalasi-java.md) | bedanya JDK dan JRE, memasang JDK, mengatur `JAVA_HOME` dan `PATH` | jalur Java |
| 3 | [Git dan GitHub](git-dan-github.md) | mengunduh materi (ZIP atau `git clone`), mengenali folder utama materi, dan memperbaruinya | semua |
| 4 | [Editor VS Code](editor-vscode.md) | memasang VS Code dan ekstensinya, membuka folder yang benar, tombol ▷, terminal VS Code | semua |
| 5 | [Menjalankan Program](menjalankan-program.md) | dasar terminal, folder aktif, menjalankan Python dan Java satu *file* maupun banyak *file* | semua |
| 6 | [Mengatasi Masalah](mengatasi-masalah.md) | kumpulan masalah instalasi yang sering terjadi beserta solusinya | buka saat perlu |

> [!TIP]
> Cara membaca petunjuk di panduan-panduan ini:
>
> - Nama tombol, menu, dan pilihan yang perlu kamu klik ditulis **tebal**, persis seperti tulisan di layar, misalnya **Install** atau **Open Folder**.
> - Tanda → berarti "lalu pilih". Misalnya, **File → Open Folder** artinya klik menu **File**, lalu pilih **Open Folder**.
> - Kombinasi tombol seperti Ctrl+S berarti: tekan dan tahan Ctrl, lalu tekan S.
> - Teks `seperti ini` adalah perintah, kode, atau nama *file*, misalnya `python --version` atau `halo.py`. Jika perlu diketik, ketik persis apa adanya, termasuk huruf besar-kecil dan spasinya.

## 3. Alur Persiapan

```mermaid
flowchart TD
    A["Pilih jalur:<br/>Python, Java, atau keduanya"] --> B["Pasang Python<br/>dan/atau JDK"]
    B --> C["Periksa versi<br/>di terminal"]
    C --> D["Unduh materi<br/>ZIP atau git clone"]
    D --> E["Pasang VS Code<br/>dan ekstensinya"]
    E --> F["Jalankan program uji coba"]
    F --> G{"Berhasil?"}
    G -->|Ya| H["Siap ke Pertemuan 01"]
    G -->|Belum| I["Buka halaman<br/>Mengatasi Masalah"]
    I --> C
```

## 4. Uji Coba: Apakah Semuanya Sudah Siap?

Setelah semua terpasang dan materi sudah ada di laptopmu, lakukan uji coba berikut. Kita memakai studi kasus KedaiKita dari Pertemuan 02 karena programnya sudah tersedia di materi.

**Langkah 1: periksa versi di terminal.** Buka terminal: di Windows, klik **Start**, ketik `PowerShell`, lalu tekan Enter; di macOS/Linux, buka aplikasi **Terminal**. Ketik perintah yang sesuai jalurmu satu per satu, masing-masing diakhiri Enter:

```bash
python --version
java -version
javac -version
```

Di macOS dan Linux, ketik `python3 --version` sebagai ganti `python --version`. Pastikan Python minimal **3.10**, serta `java` dan `javac` minimal **17** dengan angka utama yang sama. Contoh hasil yang benar: `Python 3.15.0` dan `javac 21.0.5` (angkamu boleh berbeda).

**Langkah 2: jalankan dari VS Code.**

1. Buka VS Code, lalu pilih **File → Open Folder**.
2. Masuk ke **folder utama materi** (`PBO2026`, atau `PBO2026-master` jika kamu mengunduh ZIP), lalu pilih folder `Pertemuan-02-Kelas-dan-Objek/python` (jalur Python) atau `Pertemuan-02-Kelas-dan-Objek/java` (jalur Java). Jika VS Code bertanya **Do you trust the authors of the files in this folder?**, pilih **Yes, I trust the authors**.
3. Di panel **Explorer** (sisi kiri), buka folder `studi-kasus`, lalu klik *file* `kedaikita.py` (Python) atau `KedaiKita.java` (Java).
4. Jalur Python: klik tombol ▷ (**Run Python File**) di pojok kanan atas. Jalur Java: klik tulisan **Run** di atas baris `public static void main`.

Hasilnya muncul di panel **TERMINAL** di bagian bawah, setelah baris perintah panjang yang diketik VS Code secara otomatis. Jika semuanya beres, kedua program menampilkan hasil yang sama persis seperti ini:

```text
=== MENU KEDAIKITA ===
Kopi Susu Gula Aren - Rp18000
Es Teh Manis - Rp8000
Nasi Goreng Kampung - Rp25000

=== PESANAN BUDI ===
2 x Kopi Susu Gula Aren = Rp36000
1 x Nasi Goreng Kampung = Rp25000
Total bayar: Rp61000

=== HARGA ES TEH NAIK ===
Es Teh Manis - Rp10000
Kopi Susu Gula Aren - Rp18000
```

**Langkah 3: jalankan dari terminal.** Masih di VS Code, klik kanan folder `studi-kasus` di panel **Explorer**, lalu pilih **Open in Integrated Terminal**. Terminal baru terbuka **tepat di folder itu**, jadi kamu tidak perlu mengetik `cd`. Ketik perintah berikut, lalu tekan Enter.

Jalur 🐍 Python (di macOS/Linux, ketik `python3` sebagai ganti `python`):

```bash
python kedaikita.py
```

Jalur ☕ Java:

```bash
java KedaiKita.java
```

Hasilnya harus sama persis dengan hasil di langkah 2.

> [!NOTE]
> Ingin mencoba tanpa VS Code? Buka terminal di folder utama materi (caranya ada di [Menjalankan Program bagian 2](menjalankan-program.md#2-membuka-terminal)). Lalu masuk dulu ke folder studi kasus dengan `cd Pertemuan-02-Kelas-dan-Objek/python/studi-kasus` (Python) atau `cd Pertemuan-02-Kelas-dan-Objek/java/studi-kasus` (Java), baru jalankan perintah di atas. Pemisah folder di Windows sebenarnya `\`. PowerShell juga menerima `/`, tetapi jika perintah dengan `/` bermasalah di Command Prompt, ganti dengan `\`.

Selamat! Jika kamu melihat menu KedaiKita di layarmu, artinya "dapur"-mu sudah siap dipakai.

## 5. *Checklist* Siap Belajar

Periksa setiap butir berikut. Jika semuanya sudah terpenuhi, kamu siap belajar.

- [ ] Jalur utama sudah dipilih: Python atau Java.
- [ ] `python --version` (atau `python3 --version`) menampilkan Python 3.10 atau lebih baru (jalur Python).
- [ ] `java -version` dan `javac -version` sama-sama menampilkan versi 17 atau lebih baru (jalur Java).
- [ ] Materi sudah ada di laptopmu, kamu tahu letak **folder utama materi**, dan kamu tahu cara memperbaruinya.
- [ ] VS Code sudah terpasang beserta ekstensi **Python** dan/atau **Extension Pack for Java**.
- [ ] Kamu bisa membuka terminal tepat di sebuah folder (misalnya lewat **Open in Integrated Terminal**) dan berpindah folder dengan `cd`.
- [ ] Hasil uji coba di bagian 4 sudah muncul dengan benar, baik lewat VS Code maupun lewat terminal.
- [ ] Folder terpisah untuk menyimpan latihanmu sendiri sudah disiapkan.

## 6. Kalau Ada Masalah

Masalah instalasi itu wajar dan **sangat** sering terjadi, bahkan pada pemrogram berpengalaman. Jangan menyerah. Langkah yang disarankan:

1. Baca pesan *error*-nya pelan-pelan. Pesan *error* adalah petunjuk, bukan hukuman.
2. Cari gejalanya di halaman [Mengatasi Masalah](mengatasi-masalah.md).
3. Tutup **semua** terminal dan VS Code, lalu buka lagi. Banyak masalah `PATH` beres dengan cara ini.
4. Masih buntu? Tanyakan ke asisten atau dosen. Sertakan teks pesan *error*, sistem operasi, dan langkah yang sudah kamu coba.

## 📝 Ringkasan

- Jalur Python butuh Python 3.10+, jalur Java butuh JDK 17+. Keduanya boleh dipasang.
- Urutan persiapan: pasang Python/JDK → unduh materi → pasang VS Code → jalankan uji coba.
- VS Code dengan ekstensi Python dan Extension Pack for Java dipakai sebagai editor utama.
- Di VS Code, buka folder `python/` atau `java/` milik satu pertemuan. Untuk Java, jangan membuka seluruh folder materi.
- Perintah `cd` di halaman praktik ditulis dari **folder utama materi** (`PBO2026` atau `PBO2026-master`). Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.
- Uji coba yang berhasil: studi kasus Pertemuan 02 menampilkan menu KedaiKita.
- Simpan latihanmu sendiri di folder terpisah agar tidak tertimpa saat materi diperbarui.

## ➡️ Langkah Berikutnya

Semua siap? Mari mulai belajar di [Pertemuan 01: Pengenalan PBO](../Pertemuan-01-Pengenalan-PBO/README.md).

---

[🏠 Beranda](../README.md) · [Pertemuan 01 ➡️](../Pertemuan-01-Pengenalan-PBO/README.md)
