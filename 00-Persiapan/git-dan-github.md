# Git dan GitHub

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Mengatasi Masalah ➡️](mengatasi-masalah.md)

> Materi kuliah ini disimpan di GitHub dan akan diperbarui sepanjang semester. Halaman ini menjelaskan dua cara mengambil materi ke laptopmu, cara memperbaruinya, dan cara menyimpan latihanmu sendiri agar **tidak tertimpa** saat materi diperbarui.

## Daftar Isi

1. [Git dan GitHub dalam Satu Menit](#1-git-dan-github-dalam-satu-menit)
2. [Cara 1: Unduh ZIP (Tanpa Git)](#2-cara-1-unduh-zip-tanpa-git)
3. [Cara 2: git clone (Disarankan)](#3-cara-2-git-clone-disarankan)
4. [Memperbarui Materi dengan git pull](#4-memperbarui-materi-dengan-git-pull)
5. [Menyimpan Latihanmu Sendiri](#5-menyimpan-latihanmu-sendiri)
6. [Jika git pull Menolak Berjalan](#6-jika-git-pull-menolak-berjalan)

---

## 1. Git dan GitHub dalam Satu Menit

- **Git** adalah program yang mencatat riwayat perubahan sebuah folder. Bayangkan seperti fitur "riwayat versi" di dokumen daring, tetapi untuk seluruh folder kode.
- **GitHub** adalah situs tempat menyimpan folder ber-Git itu secara daring, sehingga bisa diunduh dan diperbarui oleh banyak orang.
- **Repositori** (*repository*, sering disingkat *repo*) adalah folder proyek yang riwayatnya dicatat oleh Git. Materi kuliah ini adalah sebuah repositori di alamat [github.com/antonprafanto/PBO2026](https://github.com/antonprafanto/PBO2026).

Kamu **tidak wajib** mahir Git untuk mengikuti mata kuliah ini. Namun, mengenalnya sejak sekarang akan sangat berguna, karena hampir semua tim pengembang perangkat lunak memakainya.

## 2. Cara 1: Unduh ZIP (Tanpa Git)

Cara paling mudah, cocok jika kamu belum memasang Git.

1. Buka [github.com/antonprafanto/PBO2026](https://github.com/antonprafanto/PBO2026).
2. Klik tombol hijau **Code**, lalu pilih **Download ZIP**.
3. Ekstrak file ZIP ke folder yang mudah ditemukan, misalnya `Documents`. Hasil ekstraknya biasanya bernama `PBO2026-main`.
4. Buka folder hasil ekstrak itu di VS Code atau terminal.

**Kekurangannya:** setiap kali materi diperbarui, kamu harus mengunduh ZIP yang baru. Jika kamu mengekstraknya ke folder yang sama, isi lama, **termasuk perubahan yang kamu buat**, bisa tertimpa.

> [!WARNING]
> Jangan menyimpan latihanmu di dalam folder hasil ekstrak ZIP. Simpan di folder terpisah (lihat [bagian 5](#5-menyimpan-latihanmu-sendiri)).

## 3. Cara 2: `git clone` (Disarankan)

### 3.1 Memasang Git

| Sistem | Cara memasang |
|---|---|
| Windows | Unduh **Git for Windows** dari [git-scm.com](https://git-scm.com/). Jalankan installernya. Pilihan bawaan di setiap langkah sudah aman untuk pemula. |
| macOS | Ketik `git --version` di Terminal. Jika Git belum ada, macOS akan menawarkan pemasangan *Command Line Tools* yang sudah berisi Git. Setujui tawarannya. |
| Linux | Ubuntu/Debian: `sudo apt install git`. Fedora: `sudo dnf install git`. |

Setelah terpasang, buka terminal **baru** dan periksa:

```bash
git --version
```

Jika muncul tulisan seperti `git version 2.x.y`, Git siap dipakai.

### 3.2 Mengambil materi

Masuk ke folder tempat kamu ingin menyimpan materi, lalu jalankan `git clone`:

```bash
cd Documents
git clone https://github.com/antonprafanto/PBO2026.git
cd PBO2026
```

Perintah `git clone` membuat folder `PBO2026` berisi seluruh materi, lengkap dengan catatan riwayatnya. Langkah ini cukup dilakukan **sekali**.

> [!TIP]
> Lebih suka tampilan grafis? **GitHub Desktop** ([desktop.github.com](https://desktop.github.com/)) bisa melakukan *clone* dan *pull* dengan beberapa klik, tanpa mengetik perintah.

## 4. Memperbarui Materi dengan `git pull`

Materi bisa bertambah atau diperbaiki sewaktu-waktu. Untuk mengambil versi terbaru, masuk ke folder `PBO2026`, lalu jalankan:

```bash
git pull
```

Git hanya mengunduh **bagian yang berubah**, jadi prosesnya cepat. Biasakan menjalankan `git pull` sebelum mulai belajar setiap minggu.

## 5. Menyimpan Latihanmu Sendiri

Ini aturan emas agar latihanmu aman: **jangan mengubah file materi secara langsung.** Salin dulu file yang ingin kamu ubah ke folder milikmu sendiri.

### Pilihan A: folder terpisah (paling sederhana)

Buat folder di **luar** folder materi, misalnya:

```text
Documents/
├── PBO2026/                  <- materi kuliah (hanya dibaca, diperbarui dengan git pull)
└── PBO-latihan-saya/         <- milikmu: latihan, tugas, dan percobaan
    ├── pertemuan-02/
    ├── pertemuan-03/
    └── proyek-akhir/
```

Saat ingin bereksperimen dengan sebuah contoh, salin filenya ke `PBO-latihan-saya`, lalu ubah sesukamu di sana. Materi asli tetap bersih, dan `git pull` tidak akan pernah bentrok dengan pekerjaanmu.

> [!TIP]
> Untuk jalur Java, pertahankan susunan **satu folder per pertemuan** di folder latihanmu juga. Alasannya sama seperti di [Editor VS Code](editor-vscode.md): kelas bernama sama dari pertemuan berbeda tidak boleh berada dalam satu proyek.

### Pilihan B: *fork* di GitHub (untuk yang ingin belajar Git lebih jauh)

*Fork* adalah salinan repositori di akun GitHub-mu sendiri.

1. Buat akun GitHub (gratis), lalu buka halaman repositori materi.
2. Klik tombol **Fork**. Kini kamu punya salinan di `github.com/nama-akunmu/PBO2026`.
3. Lakukan `git clone` dari alamat *fork*-mu, lalu simpan latihanmu di sana dengan `git add`, `git commit`, dan `git push`.
4. Saat materi asli diperbarui, klik **Sync fork** di halaman *fork*-mu, lalu jalankan `git pull` di laptop.

Pilihan B memberimu cadangan daring dan latihan Git sungguhan. Namun jika kamu baru mengenal Git, **Pilihan A sudah lebih dari cukup**.

## 6. Jika `git pull` Menolak Berjalan

Jika kamu terlanjur mengubah file materi, `git pull` bisa menolak berjalan dengan pesan seperti ini:

```text
error: Your local changes to the following files would be overwritten by merge:
	Pertemuan-02-Kelas-dan-Objek/python/contoh/contoh01_kelas_dan_objek.py
Please commit your changes or stash them before you merge.
Aborting
```

Artinya: "Ada file yang kamu ubah, dan versi barunya akan menimpa perubahanmu. Aku berhenti dulu agar perubahanmu tidak hilang."

Pilih salah satu jalan keluar berikut:

**Jalan 1: simpan sementara, perbarui, lalu kembalikan perubahanmu.**

```bash
git stash
git pull
git stash pop
```

`git stash` menyimpan perubahanmu ke "laci" sementara, `git pull` memperbarui materi, lalu `git stash pop` mengembalikan perubahanmu. Jika Git melaporkan konflik setelah `git stash pop`, mintalah bantuan asisten.

**Jalan 2: buang perubahanmu pada file materi.** Salin dulu perubahan yang ingin kamu simpan ke folder latihanmu, lalu jalankan:

```bash
git restore .
git pull
```

> [!CAUTION]
> `git restore .` **menghapus semua perubahan** pada file materi yang belum di-*commit*, dan tidak bisa dibatalkan. Pastikan semua yang penting sudah kamu salin ke tempat lain.

Setelah masalah ini selesai, gunakan **Pilihan A** di bagian 5 agar tidak terulang.

## 📝 Ringkasan

- Ambil materi dengan **Download ZIP**, atau lebih baik dengan `git clone https://github.com/antonprafanto/PBO2026.git`.
- Perbarui materi dengan `git pull` di dalam folder `PBO2026`.
- Simpan latihanmu di **folder terpisah** atau di *fork* milikmu, bukan di file materi.
- Jika `git pull` menolak karena ada perubahan lokal, gunakan `git stash` atau salin perubahanmu lalu `git restore .`.

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Mengatasi Masalah ➡️](mengatasi-masalah.md)
