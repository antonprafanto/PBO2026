# Instalasi Java (JDK)

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Git dan GitHub ➡️](git-dan-github.md)

> Halaman ini memandumu memasang **JDK** (*Java Development Kit*) agar kamu bisa menulis, mengompilasi, dan menjalankan program Java. Jika kamu memilih jalur Python saja, halaman ini boleh dilewati; lanjutkan ke [Git dan GitHub](git-dan-github.md).

## Daftar Isi

1. [JDK atau JRE?](#1-jdk-atau-jre)
2. [Versi yang Kita Butuhkan](#2-versi-yang-kita-butuhkan)
3. [Cek Dulu: Mungkin JDK Sudah Terpasang](#3-cek-dulu-mungkin-jdk-sudah-terpasang)
4. [Memilih Distribusi JDK](#4-memilih-distribusi-jdk)
5. [Windows](#5-windows)
6. [macOS](#6-macos)
7. [Linux](#7-linux)
8. [Memeriksa Hasil Instalasi](#8-memeriksa-hasil-instalasi)
9. [Jebakan: Lebih dari Satu Java Terpasang](#9-jebakan-lebih-dari-satu-java-terpasang)

---

## 1. JDK atau JRE?

Ada dua istilah yang sering membingungkan pemula:

| | JRE (*Java Runtime Environment*) | JDK (*Java Development Kit*) |
|---|---|---|
| Isinya | mesin untuk **menjalankan** program Java | JRE **ditambah** alat untuk **membuat** program Java |
| Punya perintah `java` | ya | ya |
| Punya perintah `javac` (*compiler*) | **tidak** | **ya** |
| Cocok untuk | pengguna aplikasi Java | pemrogram, termasuk kamu |

Analogi sederhananya: JRE itu seperti **pemutar video**, sedangkan JDK adalah **pemutar video sekaligus studio untuk membuat videonya**. Sebagai mahasiswa yang akan menulis program, kamu butuh **JDK**. Saat mengunduh, pastikan jenis paketnya **JDK**, bukan JRE.

> [!IMPORTANT]
> Jika `java -version` berjalan tetapi `javac -version` tidak dikenali, kemungkinan besar yang terpasang hanyalah JRE, atau folder JDK belum masuk `PATH`. Pasanglah JDK.

## 2. Versi yang Kita Butuhkan

| | Versi |
|---|---|
| **Disarankan** | JDK **25** (LTS terbaru) atau JDK **21** |
| **Minimal** | JDK **17** |

**LTS** (*Long-Term Support*) adalah versi yang didukung dalam jangka panjang sehingga lebih stabil untuk belajar dan bekerja. Contoh versi LTS adalah 17, 21, dan 25. Versi di antaranya, misalnya 22, 23, atau 24, hanya didukung sebentar (sekitar enam bulan).

Semua kode Java di materi ini diuji agar berjalan di Java 17. Jadi, JDK 17, 21, maupun 25 sama-sama aman dipakai. Jika baru akan memasang, pilih JDK 25.

## 3. Cek Dulu: Mungkin JDK Sudah Terpasang

Buka terminal: di Windows, klik **Start**, ketik `PowerShell`, lalu tekan Enter; di macOS, buka aplikasi **Terminal** (Cmd+Spasi, ketik `Terminal`); di Linux, tekan Ctrl+Alt+T. Lalu ketik dua perintah ini satu per satu, masing-masing diakhiri Enter. Folder aktif terminalnya tidak berpengaruh untuk perintah ini.

```bash
java -version
javac -version
```

Perhatikan bahwa keduanya memakai **satu** tanda minus: `-version`. Contoh hasilnya ada di [bagian 8](#8-memeriksa-hasil-instalasi).

- Jika **keduanya** menampilkan versi **17 atau lebih**, dengan angka utama yang **sama**, JDK-mu sudah siap. Lanjutkan ke [Git dan GitHub](git-dan-github.md) untuk mengunduh materi.
- Jika salah satunya tidak dikenali, versinya di bawah 17, atau angka keduanya berbeda, lanjutkan membaca.

## 4. Memilih Distribusi JDK

Java bersifat terbuka sehingga ada beberapa "distribusi" JDK dari berbagai penyedia. Untuk belajar, semuanya bekerja sama baiknya.

| Distribusi | Penyedia | Situs |
|---|---|---|
| **Eclipse Temurin** (disarankan) | Eclipse Adoptium | [adoptium.net](https://adoptium.net/) |
| Oracle JDK | Oracle | [oracle.com/java](https://www.oracle.com/java/technologies/downloads/) |

Kami menyarankan **Eclipse Temurin** karena gratis, terbuka, dan *installer*-nya di Windows bisa sekaligus mengatur `PATH` dan `JAVA_HOME`. Oracle JDK juga boleh dipakai.

> [!TIP]
> Cukup pasang **satu** JDK. Memasang banyak JDK sekaligus adalah sumber masalah yang paling sering muncul (lihat [bagian 9](#9-jebakan-lebih-dari-satu-java-terpasang)).

## 5. Windows

### 5.1 Eclipse Temurin (disarankan)

1. Buka [adoptium.net](https://adoptium.net/), lalu pilih unduhan **Temurin** versi **LTS** (disarankan 25; 21 juga boleh).
2. Pastikan pilihannya: sistem operasi **Windows**, arsitektur **x64** (cocok untuk hampir semua laptop Windows), jenis paket **JDK**, dan format **.msi**.
3. Jalankan *file* `.msi` yang sudah diunduh, klik **Next**, lalu setujui lisensinya dan klik **Next** lagi.
4. Di layar **Custom Setup**, kamu akan melihat beberapa pilihan fitur dalam bentuk daftar bertingkat:
   - **Add to PATH**: biasanya sudah aktif. Biarkan aktif.
   - **Set JAVA_HOME variable**: biasanya belum aktif (ikonnya bertanda silang merah). Klik ikon itu, lalu pilih **Will be installed on local hard drive**.
   - Pilihan lain boleh dibiarkan seperti bawaannya.
5. Klik **Next**, lalu **Install**. Jika Windows meminta izin, pilih **Yes**. Setelah selesai, klik **Finish**.
6. **Tutup semua terminal yang terbuka**, lalu buka terminal baru dan periksa hasilnya (lihat [bagian 8](#8-memeriksa-hasil-instalasi)).

> [!NOTE]
> `JAVA_HOME` adalah variabel lingkungan yang berisi alamat folder JDK. Perintah `java` dan `javac` sebenarnya cukup membutuhkan `PATH`, tetapi beberapa editor dan alat bantu Java mencari JDK lewat `JAVA_HOME`. Mengaktifkannya sekarang akan menghemat waktumu nanti.

### 5.2 Oracle JDK (alternatif)

1. Buka halaman unduhan [Oracle JDK](https://www.oracle.com/java/technologies/downloads/), lalu pilih versi **25** atau **21** dan tab **Windows**.
2. Unduh **x64 Installer** (`.exe`) atau **x64 MSI Installer**, lalu jalankan dan ikuti langkahnya.
3. *Installer* Oracle menyalin `java`, `javac`, `javaw`, dan `jshell` ke folder `C:\Program Files\Common Files\Oracle\Java\javapath`, dan folder itu sudah ada di `PATH`. Jadi, perintahnya langsung bisa dipakai di terminal baru.
4. `JAVA_HOME` tidak diatur otomatis. Jika dibutuhkan, atur secara manual seperti di bagian 5.3.

### 5.3 Mengatur `PATH` dan `JAVA_HOME` Secara Manual

Langkah ini hanya diperlukan jika `javac` tetap tidak dikenali setelah instalasi, atau jika kamu ingin mengatur `JAVA_HOME` sendiri.

1. Cari lokasi folder JDK-mu di File Explorer. Contohnya untuk Temurin: `C:\Program Files\Eclipse Adoptium\jdk-21.0.5.11-hotspot`, dan untuk Oracle: `C:\Program Files\Java\jdk-21`. Nama foldernya mengikuti versi yang kamu pasang. Salin alamatnya dari bilah alamat File Explorer.
2. Klik **Start**, ketik `environment variables`, lalu pilih **Edit environment variables for your account**. Jendela **Environment Variables** terbuka. Jika Windows-mu berbahasa Indonesia, nama menunya memakai kata "variabel lingkungan".
3. Di bagian **User variables**, klik **New...**. Isi **Variable name** dengan `JAVA_HOME` dan **Variable value** dengan alamat folder JDK dari langkah 1. Klik **OK**.
4. Masih di bagian **User variables**, pilih variabel **Path**, klik **Edit...**, lalu **New**, dan ketik `%JAVA_HOME%\bin`. Pindahkan ke paling atas dengan tombol **Move Up**.
5. Klik **OK** di semua jendela. Tutup semua terminal, buka terminal baru, lalu periksa lagi.

> [!WARNING]
> Isi `JAVA_HOME` adalah folder JDK-nya (misalnya `...\jdk-21`), **bukan** folder `bin` di dalamnya. Folder `bin` ditambahkan ke `Path`, bukan ke `JAVA_HOME`.

Langkah di atas cukup jika sebelumnya belum ada Java sama sekali. Jika masalahnya justru Java **lain** yang terpakai lebih dulu, baca [bagian 9](#9-jebakan-lebih-dari-satu-java-terpasang): Windows selalu membaca `Path` milik sistem (**System variables**) sebelum `Path` milik akunmu (**User variables**).

## 6. macOS

1. Cari tahu jenis prosesor Mac-mu: klik menu **Apple → About This Mac**. Jika tertulis **Apple M1, M2, M3**, atau sejenisnya, pilih arsitektur **aarch64**. Jika tertulis **Intel**, pilih **x64**.
2. Buka [adoptium.net](https://adoptium.net/), lalu unduh **Temurin** versi **LTS** (disarankan 25; 21 juga boleh) untuk **macOS** dengan arsitektur yang sesuai, dalam format **.pkg**.
3. Buka *file* `.pkg`, lalu ikuti langkahnya sampai selesai: **Continue**, setujui lisensi, lalu **Install**. Masukkan kata sandi Mac jika diminta. JDK-nya terpasang di folder `/Library/Java/JavaVirtualMachines/`.
4. Tutup Terminal sepenuhnya (Cmd+Q), buka lagi, lalu periksa hasilnya (lihat [bagian 8](#8-memeriksa-hasil-instalasi)).

Untuk melihat semua JDK yang terpasang di Mac, ketik perintah berikut di Terminal:

```bash
/usr/libexec/java_home -V
```

Jika kamu ingin mengatur `JAVA_HOME` (opsional), ketik perintah berikut **sekali saja** di Terminal. Perintah ini menambahkan satu baris ke *file* pengaturan `~/.zshrc`:

```bash
echo 'export JAVA_HOME=$(/usr/libexec/java_home -v 25)' >> ~/.zshrc
```

Ganti `25` dengan versi yang kamu pasang, lalu buka Terminal baru. Periksa hasilnya dengan `echo $JAVA_HOME`; yang muncul adalah alamat folder JDK-mu.

## 7. Linux

Di Ubuntu dan Debian, JDK bisa dipasang dari pengelola paket. Ketik di Terminal (`sudo` akan meminta kata sandi akunmu; hurufnya memang tidak terlihat saat diketik):

```bash
sudo apt update
sudo apt install openjdk-21-jdk
```

Jika distribusimu menyediakan paket yang lebih baru, misalnya `openjdk-25-jdk`, paket itu juga boleh dipakai. Jika `openjdk-21-jdk` tidak tersedia, gunakan `openjdk-17-jdk`. Perhatikan akhiran **`-jdk`**: paket berakhiran `-jre` tidak berisi `javac`.

Di Fedora, gunakan:

```bash
sudo dnf install java-21-openjdk-devel
```

Paket berakhiran **`-devel`** itulah yang berisi `javac`.

## 8. Memeriksa Hasil Instalasi

Buka terminal **baru** (PowerShell di Windows, Terminal di macOS/Linux), lalu ketik dua perintah ini satu per satu:

```bash
java -version
javac -version
```

Contoh hasil jika kamu memasang Temurin 21 (angka detailmu boleh berbeda; jika memasang JDK 25, angkanya diawali `25`):

```text
openjdk version "21.0.5" 2024-10-15 LTS
OpenJDK Runtime Environment Temurin-21.0.5+11 (build 21.0.5+11-LTS)
OpenJDK 64-Bit Server VM Temurin-21.0.5+11 (build 21.0.5+11-LTS, mixed mode, sharing)
```

```text
javac 21.0.5
```

Yang perlu kamu periksa:

1. Angka utamanya (di contoh ini `21`) **minimal 17**.
2. Angka utama `java` dan `javac` **sama**.

Selanjutnya, pastikan Java bisa menjalankan sebuah *file* program:

1. Buat folder untuk latihanmu sendiri, misalnya `PBO-latihan-saya` di dalam **Documents** (lihat [Git dan GitHub bagian 5](git-dan-github.md#5-menyimpan-latihanmu-sendiri)).
2. Di folder itu, buat *file* baru bernama **persis** `Halo.java` (huruf H besar), salin kode di bawah ini ke dalamnya, lalu simpan. Jika VS Code sudah terpasang, pakai VS Code. Jika belum, Notepad (Windows) atau TextEdit (macOS) juga bisa, asalkan *file*-nya tersimpan sebagai teks biasa dan namanya tidak menjadi `Halo.java.txt`.
3. Buka terminal di folder `PBO-latihan-saya` (caranya ada di [Menjalankan Program bagian 2](menjalankan-program.md#2-membuka-terminal)), lalu jalankan *file*-nya.

Isi *file* `Halo.java`:

```java
public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, KedaiKita!");
    }
}
```

Ketik perintah berikut di terminal yang berada di folder `PBO-latihan-saya`:

```bash
java Halo.java
```

Hasilnya:

```text
Halo, KedaiKita!
```

Perintah `java Halo.java` langsung mengompilasi dan menjalankan program satu *file* (fitur sejak Java 11). Cara lain, termasuk `javac`, dijelaskan di [Menjalankan Program](menjalankan-program.md).

> [!TIP]
> JDK juga punya mode interaktif bernama **jshell**. Ketik `jshell` di terminal, lalu coba `System.out.println("Halo")` atau `18000 * 2`. Ketik `/exit` untuk keluar. Fitur ini enak untuk mencoba potongan kode kecil.

## 9. Jebakan: Lebih dari Satu Java Terpasang

Banyak laptop sudah punya Java lama, misalnya Java 8 yang dipasang untuk aplikasi tertentu, atau JDK sisa praktikum sebelumnya. Akibatnya, perintah `java` bisa menjalankan **versi yang salah**.

**Gejalanya:**

- `java -version` dan `javac -version` menampilkan angka utama yang **berbeda**, misalnya `1.8.0_...` dan `21.0.5`.
- Muncul *error* `UnsupportedClassVersionError` saat menjalankan program.
- `java Halo.java` gagal dengan pesan `Could not find or load main class Halo.java`. Ini terjadi karena Java 8 belum mengenal cara menjalankan *file* `.java` secara langsung.

**Cara memeriksa** Java mana yang sebenarnya dipakai (ketik di terminal, dari folder mana saja):

| Sistem | Perintah | Keterangan |
|---|---|---|
| Windows (Command Prompt) | `where java` | menampilkan semua lokasi `java.exe`, sesuai urutan `PATH` |
| Windows (PowerShell) | `where.exe java` | di PowerShell, `where` tanpa `.exe` artinya perintah lain |
| macOS | `/usr/libexec/java_home -V` | menampilkan semua JDK yang terpasang |
| Linux | `which -a java` | menampilkan semua lokasi `java` |

Yang dipakai adalah lokasi yang muncul **paling atas**.

**Cara memperbaiki:**

- **Windows:** cara termudah adalah menghapus Java lama yang tidak diperlukan lewat **Settings → Apps**. Jika Java lama itu harus tetap ada, atur urutan `Path` milik **sistem** (butuh izin administrator):
  1. Klik **Start**, ketik `environment variables`, pilih **Edit the system environment variables**, lalu klik **Environment Variables...**.
  2. Di bagian **System variables**, pilih **Path**, lalu klik **Edit...**.
  3. Pindahkan folder `bin` JDK pilihanmu ke **paling atas** dengan tombol **Move Up**. Perhatikan juga folder `...\Oracle\Java\javapath` di daftar itu karena folder itu bisa mendahului JDK lain.
  4. Klik **OK** di semua jendela.

  Mengubah `Path` milik akunmu saja (bagian 5.3) tidak cukup karena Windows membaca `Path` milik sistem lebih dulu.
- **macOS:** atur `JAVA_HOME` ke versi pilihanmu seperti di [bagian 6](#6-macos).
- **Linux (Ubuntu/Debian):** ketik perintah berikut di Terminal, lalu pilih nomor JDK yang diinginkan sebagai versi bawaan:

```bash
sudo update-alternatives --config java
sudo update-alternatives --config javac
```

Setelah memperbaiki, selalu buka terminal baru lalu periksa ulang `java -version` dan `javac -version`.

## 📝 Ringkasan

- Pemrogram butuh **JDK**, bukan hanya JRE, karena hanya JDK yang punya `javac`.
- Gunakan JDK LTS **25** (terbaru) atau **21**, minimal **17**.
- Di Windows, *installer* Temurin bisa mengatur `PATH` dan `JAVA_HOME`. Aktifkan **Set JAVA_HOME variable**.
- Periksa dengan `java -version` dan `javac -version` di terminal baru. Angka utamanya harus sama.
- Jika versinya kacau, cari tahu Java mana yang dipakai dengan `where java`, `where.exe java`, atau `which -a java`.

Masih ada kendala? Lihat [Mengatasi Masalah](mengatasi-masalah.md). Jika JDK sudah siap, lanjutkan ke [Git dan GitHub](git-dan-github.md) untuk mengunduh materi.

---

[⬅️ Persiapan](README.md) · [🏠 Beranda](../README.md) · [Git dan GitHub ➡️](git-dan-github.md)
