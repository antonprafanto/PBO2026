# Git dan GitHub: Mengunduh Materi

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Editor VS Code ➡️](editor-vscode.md)

> Sebelum menjalankan program apa pun, materi kuliah harus ada dulu di laptopmu. Materi ini disimpan di GitHub dan akan diperbarui sepanjang semester. Halaman ini menjelaskan dua cara mengambil materi, cara memperbaruinya, dan cara menyimpan latihanmu sendiri agar **tidak tertimpa** saat materi diperbarui.

## Daftar Isi

1. [Git dan GitHub dalam Satu Menit](#1-git-dan-github-dalam-satu-menit)
2. [Cara 1: Unduh ZIP (Tanpa Git)](#2-cara-1-unduh-zip-tanpa-git)
3. [Cara 2: `git clone` (Disarankan)](#3-cara-2-git-clone-disarankan)
4. [Memperbarui Materi dengan `git pull`](#4-memperbarui-materi-dengan-git-pull)
5. [Menyimpan Latihanmu Sendiri](#5-menyimpan-latihanmu-sendiri)
6. [Jika `git pull` Menolak Berjalan](#6-jika-git-pull-menolak-berjalan)

---

## 1. Git dan GitHub dalam Satu Menit

- **Git** adalah program yang mencatat riwayat perubahan sebuah folder. Bayangkan seperti fitur "riwayat versi" di dokumen daring, tetapi untuk seluruh folder kode.
- **GitHub** adalah situs tempat menyimpan folder ber-Git itu secara daring sehingga bisa diunduh dan diperbarui oleh banyak orang.
- **Repositori** (*repository*, sering disingkat *repo*) adalah folder proyek yang riwayatnya dicatat oleh Git. Materi kuliah ini adalah sebuah repositori di alamat [github.com/antonprafanto/PBO2026](https://github.com/antonprafanto/PBO2026).

Kamu **tidak wajib** mahir Git untuk mengikuti mata kuliah ini. Namun, mengenalnya sejak sekarang akan sangat berguna, karena hampir semua tim pengembang perangkat lunak memakainya.

Ada dua cara mengambil materi. Pilih **salah satu** saja:

| | Cara 1: Unduh ZIP | Cara 2: `git clone` |
|---|---|---|
| Perlu memasang Git | tidak | ya |
| Nama folder hasilnya | `PBO2026-master` | `PBO2026` |
| Cara memperbarui materi | unduh ZIP baru, lalu ganti folder lama | cukup ketik `git pull` |
| Cocok untuk | yang ingin cepat mulai | yang ingin mudah memperbarui materi setiap minggu |

Folder hasil kedua cara itu kita sebut **folder utama materi**. Di dalamnya langsung terdapat folder `00-Persiapan`, folder-folder `Pertemuan-...`, dan *file* `README.md`. Semua perintah di halaman praktik ditulis dengan folder ini sebagai titik awal.

## 2. Cara 1: Unduh ZIP (Tanpa Git)

Cara paling mudah, cocok jika kamu belum memasang Git. Yang kamu butuhkan hanya peramban (Chrome, Edge, Firefox, atau Safari).

1. Buka [github.com/antonprafanto/PBO2026](https://github.com/antonprafanto/PBO2026) di peramban.
2. Klik tombol hijau **Code** di atas daftar *file*, lalu pilih **Download ZIP**. *File* ZIP-nya (biasanya `PBO2026-master.zip`) tersimpan di folder **Downloads**.
3. Ekstrak *file* ZIP itu ke folder yang mudah ditemukan, misalnya **Documents**:
   - **Windows:** buka folder **Downloads** di File Explorer, klik kanan *file* ZIP-nya, lalu pilih **Extract All...**. Klik **Browse...**, pilih folder **Documents**, lalu klik **Extract**.
   - **macOS:** klik dua kali *file* ZIP-nya di Finder (Safari sering sudah mengekstraknya otomatis), lalu pindahkan folder hasilnya ke **Documents**.
   - **Linux:** klik kanan *file* ZIP-nya di pengelola *file*, pilih **Extract Here** (namanya bisa sedikit berbeda), lalu pindahkan folder hasilnya ke **Documents**.
4. Buka folder hasil ekstrak, biasanya bernama `PBO2026-master`. Jika di dalamnya langsung terlihat folder `00-Persiapan` dan folder-folder `Pertemuan-...`, itulah **folder utama materi**. Ingat letaknya karena di panduan berikutnya kamu akan membukanya di VS Code.

> [!WARNING]
> Di Windows, **Extract All...** kadang menghasilkan folder ganda: `PBO2026-master\PBO2026-master\`. Folder utama materi adalah folder **yang di dalam**, yaitu yang langsung berisi `00-Persiapan`. Pindahkan folder dalam itu ke **Documents**, lalu hapus folder luarnya yang sudah kosong.

**Memperbarui materi (cara ZIP).** Setiap kali materi diperbarui, kamu harus mengunduh ZIP yang baru:

1. Pastikan tidak ada latihanmu yang tersimpan di folder materi (lihat [bagian 5](#5-menyimpan-latihanmu-sendiri)).
2. Hapus folder materi yang lama, atau ganti namanya, misalnya menjadi `PBO2026-lama`.
3. Ulangi langkah 1—4 di atas.

> [!CAUTION]
> Jangan mengekstrak ZIP baru **di atas** folder lama. *File* yang sudah dihapus atau diganti namanya di versi baru akan tetap tertinggal dan bercampur dengan yang baru. Perubahan yang kamu buat di folder itu juga bisa tertimpa.

## 3. Cara 2: `git clone` (Disarankan)

### 3.1 Memasang Git

| Sistem | Cara memasang |
|---|---|
| Windows | Unduh **Git for Windows** dari [git-scm.com](https://git-scm.com/), lalu jalankan *installer*-nya. Pilihan bawaan di setiap langkah sudah aman untuk pemula: cukup klik **Next** sampai **Install**. |
| macOS | Buka Terminal, lalu ketik `git --version`. Jika Git belum ada, macOS menawarkan pemasangan **Command Line Tools** yang sudah berisi Git. Klik **Install**, lalu tunggu sampai selesai. |
| Linux | Di Terminal, ketik `sudo apt install git` (Ubuntu/Debian) atau `sudo dnf install git` (Fedora). |

Setelah terpasang, buka terminal **baru** (Windows: PowerShell; macOS/Linux: Terminal), lalu ketik:

```bash
git --version
```

Jika muncul tulisan seperti `git version 2.x.y`, Git siap dipakai. Jika muncul pesan "tidak dikenali" (*not recognized*), tutup terminal lalu buka yang baru, kemudian coba lagi.

### 3.2 Mengambil materi

Langkah ini cukup dilakukan **sekali**. Kita akan menyimpan materi di folder **Documents**.

1. Buka terminal **tepat di folder Documents**:
   - **Windows:** buka File Explorer, masuk ke folder **Documents**, klik kanan di area kosong, lalu pilih **Open in Terminal**. Di Windows 10, tahan Shift sambil klik kanan, lalu pilih **Open PowerShell window here**.
   - **macOS/Linux:** buka Terminal, lalu ketik `cd Documents` dan tekan Enter. Di Linux berbahasa Indonesia, nama foldernya mungkin `Dokumen`.
2. Ketik perintah berikut, lalu tekan Enter:

   ```bash
   git clone https://github.com/antonprafanto/PBO2026.git
   ```

   Tunggu sampai selesai. Hasilnya kira-kira seperti ini (angkanya bisa berbeda):

   ```text
   Cloning into 'PBO2026'...
   ...
   Resolving deltas: 100% (...), done.
   ```

3. Kini di dalam **Documents** ada folder baru bernama `PBO2026`. Folder inilah **folder utama materi**, lengkap dengan catatan riwayatnya. Masuk ke dalamnya dengan `cd PBO2026` jika ingin langsung memakainya dari terminal. Ingat letaknya karena di panduan berikutnya kamu akan membukanya di VS Code.

> [!TIP]
> Lebih suka tampilan grafis? **GitHub Desktop** ([desktop.github.com](https://desktop.github.com/)) bisa melakukan *clone* dan *pull* dengan beberapa klik, tanpa mengetik perintah.

## 4. Memperbarui Materi dengan `git pull`

Materi bisa bertambah atau diperbaiki sewaktu-waktu. Untuk mengambil versi terbaru:

1. Buka terminal di folder utama materi `PBO2026` (misalnya lewat **Open in Terminal** seperti di bagian 3.2). Terminal VS Code juga bisa dipakai karena `git pull` boleh diketik dari folder `PBO2026` maupun dari subfolder mana pun di dalamnya.
2. Ketik perintah berikut, lalu tekan Enter:

```bash
git pull
```

Jika tidak ada yang baru, Git menjawab `Already up to date.` Jika ada pembaruan, Git menampilkan daftar *file* yang berubah. Git hanya mengunduh **bagian yang berubah**, jadi prosesnya cepat. Biasakan menjalankan `git pull` sebelum mulai belajar setiap minggu.

## 5. Menyimpan Latihanmu Sendiri

Ini aturan emas agar latihanmu aman: **jangan mengubah *file* materi secara langsung.** Salin dulu *file* yang ingin kamu ubah ke folder milikmu sendiri.

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

Saat ingin bereksperimen dengan sebuah contoh, salin *file*-nya ke `PBO-latihan-saya` lewat File Explorer atau Finder: pilih *file*-nya, tekan Ctrl+C (macOS: Cmd+C), buka folder tujuan, lalu tekan Ctrl+V (macOS: Cmd+V). Setelah itu, buka folder latihan tersebut di VS Code (**File → Open Folder**) dan ubah *file*-nya sesukamu di sana. Materi asli tetap bersih, dan `git pull` tidak akan pernah bentrok dengan pekerjaanmu.

> [!TIP]
> Untuk jalur Java, pertahankan susunan **satu folder per pertemuan** di folder latihanmu juga. Alasannya sama seperti di [Editor VS Code](editor-vscode.md): kelas bernama sama dari pertemuan berbeda tidak boleh berada dalam satu proyek.

### Pilihan B: *fork* di GitHub (untuk yang ingin belajar Git lebih jauh)

*Fork* adalah salinan repositori di akun GitHub-mu sendiri.

1. Buat akun GitHub (gratis), lalu buka halaman repositori materi.
2. Klik tombol **Fork**. Kini kamu punya salinan di `github.com/nama-akunmu/PBO2026`.
3. Lakukan `git clone` dari alamat *fork*-mu, lalu simpan latihanmu di sana dengan `git add`, `git commit`, dan `git push`.
4. Saat materi asli diperbarui, buka halaman *fork*-mu di GitHub, klik **Sync fork**, lalu **Update branch**. Setelah itu, jalankan `git pull` di laptop.

Pilihan B memberimu cadangan daring dan latihan Git sungguhan. Namun, jika kamu baru mengenal Git, **Pilihan A sudah lebih dari cukup**.

## 6. Jika `git pull` Menolak Berjalan

Jika kamu telanjur mengubah *file* materi, `git pull` bisa menolak berjalan dengan pesan seperti ini:

```text
error: Your local changes to the following files would be overwritten by merge:
	Pertemuan-02-Kelas-dan-Objek/python/contoh/contoh01_kelas_dan_objek.py
Please commit your changes or stash them before you merge.
Aborting
```

Artinya: "Ada *file* yang kamu ubah, dan versi barunya akan menimpa perubahanmu. Aku berhenti dulu agar perubahanmu tidak hilang."

Pilih salah satu jalan keluar berikut. Semua perintahnya diketik di terminal yang berada di folder materi, sama seperti saat menjalankan `git pull`.

**Jalan 1: simpan sementara, perbarui, lalu kembalikan perubahanmu.**

```bash
git stash
git pull
git stash pop
```

`git stash` menyimpan perubahanmu ke "laci" sementara, `git pull` memperbarui materi, lalu `git stash pop` mengembalikan perubahanmu. Jika Git melaporkan konflik setelah `git stash pop`, mintalah bantuan asisten.

**Jalan 2: buang perubahanmu pada *file* materi.** Salin dulu perubahan yang ingin kamu simpan ke folder latihanmu, lalu jalankan:

```bash
git restore .
git pull
```

> [!CAUTION]
> `git restore .` **menghapus semua perubahan** pada *file* materi yang belum di-*commit*, dan tidak bisa dibatalkan. Pastikan semua yang penting sudah kamu salin ke tempat lain.

Setelah masalah ini selesai, gunakan **Pilihan A** di bagian 5 agar tidak terulang.

**Kasus khusus: `fatal: refusing to merge unrelated histories`.** Pesan ini muncul jika riwayat materi di GitHub ditulis ulang oleh pengelolanya sehingga riwayat di laptopmu tidak lagi tersambung dengan riwayat di GitHub. Jalan keluarnya:

1. Salin dulu latihanmu yang masih tertinggal di folder materi ke folder latihanmu.
2. Ganti nama folder materi yang lama, misalnya menjadi `PBO2026-lama`.
3. Ambil ulang materinya dengan `git clone` seperti di [bagian 3.2](#32-mengambil-materi).

## 📝 Ringkasan

- Ambil materi dengan **Download ZIP**, atau lebih baik dengan `git clone https://github.com/antonprafanto/PBO2026.git`.
- Folder hasilnya (`PBO2026` atau `PBO2026-master`) disebut **folder utama materi**. Di dalamnya langsung ada `00-Persiapan` dan folder-folder `Pertemuan-...`.
- Perbarui materi dengan `git pull` di dalam folder `PBO2026`. Pengguna ZIP mengunduh ZIP baru dan mengganti folder lama.
- Simpan latihanmu di **folder terpisah** atau di *fork* milikmu, bukan di *file* materi.
- Jika `git pull` menolak karena ada perubahan lokal, gunakan `git stash` atau salin perubahanmu lalu `git restore .`.

Materi sudah ada di laptopmu? Langkah berikutnya: pasang dan siapkan [Editor VS Code](editor-vscode.md).

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Editor VS Code ➡️](editor-vscode.md)
