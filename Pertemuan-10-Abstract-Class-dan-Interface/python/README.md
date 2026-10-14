# 🐍 Praktik Python Pertemuan 10: *Abstract Class* dan *Interface*

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 10](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Masalah: Kelas Induk yang Terlalu Umum](#1-masalah-kelas-induk-yang-terlalu-umum)
2. [Kelas Abstrak dengan `ABC` dan `@abstractmethod`](#2-kelas-abstrak-dengan-abc-dan-abstractmethod)
3. [Konstruktor, Atribut, dan *Method* Konkret di Kelas Abstrak](#3-konstruktor-atribut-dan-method-konkret-di-kelas-abstrak)
4. [*Template Method*](#4-template-method)
5. ["*Interface*" di Python: ABC yang Isinya Abstrak Semua](#5-interface-di-python-abc-yang-isinya-abstrak-semua)
6. [Satu Kelas, Banyak Kemampuan](#6-satu-kelas-banyak-kemampuan)
7. [`typing.Protocol`: *Duck Typing* yang Diresmikan](#7-typingprotocol-duck-typing-yang-diresmikan)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md). Modul `abc` dan `typing` yang kita pakai hari ini adalah bagian dari pustaka standar Python, jadi tidak perlu memasang apa pun.

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 7 contoh, dari masalahnya sampai typing.Protocol
├── studi-kasus/     <- KedaiKita versi Pertemuan 10 (8 file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Contoh di folder ini bernomor 01 sampai 07. Contoh 07 (`typing.Protocol`) khusus Python. Contoh 08 hanya ada di folder Java karena membahas fitur khusus Java (*default method*); padanannya di Python dibahas di [Jembatan Python ↔ Java](../jembatan-python-java.md).

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-10-Abstract-Class-dan-Interface/python`. Di panel **Explorer** sebelah kiri, buka folder `contoh`, lalu klik *file* yang ingin dicoba, misalnya `contoh01_masalah_induk_umum.py`. Setelah *file* terbuka, klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Baris pertama di panel itu berisi perintah panjang yang diketik VS Code secara otomatis; *output* programmu muncul di bawahnya.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-10-Abstract-Class-dan-Interface/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_masalah_induk_umum.py
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di bagian 1. Untuk contoh lain, ganti nama *file*-nya, misalnya `python contoh02_kelas_abstrak.py`. *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

### Cara Menjalankan Studi Kasus

Studi kasus terdiri atas delapan *file* yang saling memakai lewat `import`. Yang dijalankan selalu `main.py`. *File* lain, seperti `pembayaran.py` atau `dapat_dicetak.py`, hanya berisi kelas atau fungsi bantu sehingga jika dijalankan sendiri tidak menampilkan apa-apa.

- **Cara 1:** di VS Code, buka `studi-kasus/main.py`, lalu klik tombol ▷.
- **Cara 2:** masuk dulu ke folder `studi-kasus`, lalu jalankan `main.py`.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi | `cd Pertemuan-10-Abstract-Class-dan-Interface/python/studi-kasus` |
| folder `python` pertemuan ini | `cd studi-kasus` |

Setelah itu jalankan:

```bash
python main.py
```

Baris pertama yang muncul adalah `=== MENGENAL METODE PEMBAYARAN ===`. *Output* lengkapnya ada di [bagian 8](#8-studi-kasus-kedaikita).

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.

### Tempat Menyimpan Kodemu Sendiri

Anggap folder materi sebagai buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Semua percobaan di halaman ini (bagian **Coba sendiri** dan percobaan pesan *error*) dikerjakan pada **salinan** di folder milikmu sendiri, di luar folder materi:

```text
Documents/
├── PBO2026/                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/         <- milikmu sendiri
    └── pertemuan-10/         <- salinan contoh, percobaan, dan jawaban latihan
```

Polanya selalu sama: salin *file* contoh ke folder `pertemuan-10` (lewat File Explorer di Windows atau Finder di macOS), buka salinannya, ubah, simpan, jalankan, lalu bandingkan hasilnya dengan yang tertulis di halaman ini. Untuk menjalankan salinan, buka folder `pertemuan-10` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**), lalu klik ▷. Lewat terminal, masuk dulu ke folder itu dengan `cd Documents\PBO-latihan-saya\pertemuan-10` (Windows) atau `cd ~/Documents/PBO-latihan-saya/pertemuan-10` (macOS/Linux). Alasannya dijelaskan di [aturan emas menyimpan latihan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Blok kode sesudahnya adalah **potongan** penting dari *file* itu, disalin persis. Komentar pembuka dan dua baris penutup (`if __name__ == "__main__":` lalu `main()`) tidak ditulis ulang. Jangan menjalankan potongannya sendiri; jalankan *file* lengkapnya dengan cara di atas.
- Potongan yang menjorok (diawali spasi) berasal dari dalam sebuah kelas atau dari dalam fungsi `main()`.
- Tanda `# [1]`, `# [2]`, dan seterusnya di komentar kode dijelaskan di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan. Pesan *error* hasil percobaan diberi pengantar lain, misalnya "Pesan *error*-nya:".
- Pesan *error* lengkap di halaman ini diambil dari Python 3.13. Di versi lain, bunyinya bisa sedikit berbeda; perbedaan pentingnya disebutkan di tempat.

## 1. Masalah: Kelas Induk yang Terlalu Umum

*File*: [`contoh/contoh01_masalah_induk_umum.py`](contoh/contoh01_masalah_induk_umum.py)

Sebelum belajar cara baru, kita rasakan dulu masalahnya. Kelas induk `BangunDatar` di *file* ini masih kelas biasa, sama seperti `Pembayaran` di Pertemuan 09. Berikut potongan *file*-nya:

```python
class BangunDatar:
    """Kelas induk biasa (BELUM abstrak) untuk semua bangun datar."""

    def __init__(self, nama: str):
        self.nama = nama

    def luas(self) -> int:
        return 0  # [1] luas "bangun datar umum"? Tidak ada jawaban yang masuk akal

    def info(self) -> str:
        return f"{self.nama}: luas {self.luas()} cm2"
```

Kelas `Persegi` meng-*override* `luas()` dengan benar (`sisi * sisi`). Berikut kelas `Segitiga` dan program utamanya:

```python
class Segitiga(BangunDatar):
    """Segitiga dengan alas dan tinggi."""

    def __init__(self, alas: int, tinggi: int):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi

    # [2] Pemrogram LUPA menulis method luas() di sini!


def main():
    print("=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===")
    misterius = BangunDatar("Bangun datar misterius")  # [3] tidak ada yang melarang
    print(misterius.info())

    print()
    print("=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===")
    daftar = [Persegi(5), Segitiga(6, 4)]
    for bangun in daftar:
        print(bangun.info())  # [4] Segitiga memakai luas() milik induk
    print("Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!")
```

***Output:***

```text
=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===
Bangun datar misterius: luas 0 cm2

=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===
Persegi: luas 25 cm2
Segitiga: luas 0 cm2
Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!
```

Penjelasan:

- **[1]** Kelas induk terpaksa memberi isi "pura-pura" untuk `luas()`. Angka 0 dipilih asal-asalan karena luas "bangun datar umum" memang tidak ada.
- **[2]** Kelas `Segitiga` tidak menulis `luas()`. Mungkin pemrogramnya lupa, mungkin terburu-buru.
- **[3]** Python mengizinkan objek `BangunDatar` dibuat. Hasilnya adalah objek yang tidak bermakna.
- **[4]** `Segitiga` diam-diam mewarisi `luas()` milik induk sehingga luasnya tercetak 0.

> [!WARNING]
> Bagian paling berbahaya adalah **[4]**: Python tidak memberi *error* apa pun. *Bug* seperti ini baru ketahuan kalau ada orang yang teliti memeriksa hasilnya. Di KedaiKita Pertemuan 09, kesalahan serupa pada `proses()` bisa membuat pesanan tercatat LUNAS tanpa uang masuk.

## 2. Kelas Abstrak dengan `ABC` dan `@abstractmethod`

*File*: [`contoh/contoh02_kelas_abstrak.py`](contoh/contoh02_kelas_abstrak.py)

Python tidak punya kata kunci `abstract`. Sebagai gantinya, pustaka standar menyediakan modul `abc` (singkatan dari *Abstract Base Classes*). Ada dua bahan yang kita butuhkan:

- kelas `ABC` yang diwarisi oleh kelas abstrak kita
- dekorator `@abstractmethod` yang ditulis tepat di atas setiap *method* abstrak

Berikut potongan awal *file*-nya:

```python
from abc import ABC, abstractmethod


class Bentuk(ABC):  # [1] mewarisi ABC -> kelas ini boleh punya method abstrak
    """Kelas abstrak: konsep umum semua bangun datar."""

    @abstractmethod  # [2] method abstrak: tanpa isi, wajib diisi kelas anak
    def luas(self) -> int:
        """Menghitung luas (cm2)."""

    @abstractmethod
    def keliling(self) -> int:
        """Menghitung keliling (cm)."""


class PersegiPanjang(Bentuk):
    """Persegi panjang dengan panjang dan lebar."""

    def __init__(self, panjang: int, lebar: int):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> int:  # [3] mengisi (meng-override) method abstrak
        return self.panjang * self.lebar

    def keliling(self) -> int:
        return 2 * (self.panjang + self.lebar)
```

Kelas `SegitigaSiku` ditulis dengan pola yang sama: luasnya `alas * tinggi // 2`, kelilingnya `alas + tinggi + miring`. Program utamanya:

```python
def main():
    # bentuk_umum = Bentuk()  # [4] hapus tanda # di awal baris ini -> TypeError

    kartu = PersegiPanjang(8, 5)
    penggaris = SegitigaSiku(6, 8, 10)
    daftar: list[Bentuk] = [kartu, penggaris]  # [5] list bertipe kelas abstrak

    print("=== DAFTAR BENTUK ===")
    for bentuk in daftar:
        nama = type(bentuk).__name__
        print(f"{nama}: luas {bentuk.luas()} cm2, keliling {bentuk.keliling()} cm")

    print()
    print("=== CEK JENIS ===")
    print(f"kartu dibuat dari kelas: {type(kartu).__name__}")
    print(f"Apakah kartu termasuk Bentuk? {ya_tidak(isinstance(kartu, Bentuk))}")  # [6]
```

***Output:***

```text
=== DAFTAR BENTUK ===
PersegiPanjang: luas 40 cm2, keliling 26 cm
SegitigaSiku: luas 24 cm2, keliling 24 cm

=== CEK JENIS ===
kartu dibuat dari kelas: PersegiPanjang
Apakah kartu termasuk Bentuk? ya
```

Penjelasan:

- **[1]** `class Bentuk(ABC)` berarti `Bentuk` mewarisi `ABC`. Pewarisan inilah yang "menyalakan" pemeriksaan *method* abstrak. Ingat, Python baru menolak membuat objek jika kelas itu **masih punya** *method* abstrak. Kelas `ABC` tanpa satu pun `@abstractmethod` tetap bisa dibuat objeknya (bandingkan dengan Java di [Jembatan](../jembatan-python-java.md)).
- **[2]** `@abstractmethod` adalah **dekorator**, yaitu penanda yang ditulis dengan `@` di atas `def`. Ia menandai `luas()` sebagai *method* abstrak. Isinya cukup *docstring* (boleh juga `pass` atau `...`) karena isi sungguhan menjadi tugas kelas anak.
- **[3]** `PersegiPanjang` mengisi **kedua** *method* abstrak sehingga ia menjadi kelas konkret dan objeknya boleh dibuat.
- **[4]** Baris ini sengaja dijadikan komentar. Kalau tanda `#`-nya dihapus, program berhenti dengan `TypeError`. Kita coba di salinan sebentar lagi.
- **[5]** *Type hint* `list[Bentuk]` berarti "*list* berisi objek-objek `Bentuk`". Isinya tentu objek kelas konkret. Inilah polimorfisme dari Pertemuan 09.
- **[6]** `isinstance(kartu, Bentuk)` bernilai benar: objek kelas anak tetap "adalah" kelas induknya walaupun induknya abstrak.

### Mencoba membuat objek kelas abstrak

Kita buktikan bahwa objek `Bentuk` memang tidak bisa dibuat. Kerjakan di salinan, bukan di *file* materi:

1. Salin `contoh/contoh02_kelas_abstrak.py` ke folder `PBO-latihan-saya/pertemuan-10`, lalu buka salinannya di VS Code.
2. Cari baris **[4]**, yaitu baris pertama fungsi `main()`. Letakkan kursor di baris itu, lalu tekan Ctrl+/ (macOS: Cmd+/) untuk membuang tanda komentarnya. Jika menghapus manual, hapus tanda `#` **beserta satu spasi** sesudahnya agar baris itu tetap menjorok 4 spasi, sejajar dengan baris di bawahnya.
3. Simpan (Ctrl+S), lalu jalankan salinan itu.

Pesan *error*-nya di Python 3.13 ke atas:

```text
Traceback (most recent call last):
  File "contoh02_kelas_abstrak.py", line 81, in <module>
    main()
    ~~~~^^
  File "contoh02_kelas_abstrak.py", line 63, in main
    bentuk_umum = Bentuk()  # [4] hapus tanda # di awal baris ini -> TypeError
TypeError: Can't instantiate abstract class Bentuk without an implementation for abstract methods 'keliling', 'luas'
```

Di Python 3.12, baris terakhirnya sama; hanya letak penanda `^` yang berbeda (di bawah `Bentuk()`, bukan di bawah `main()`). Di Python 3.10 dan 3.11, baris terakhirnya sedikit berbeda:

```text
TypeError: Can't instantiate abstract class Bentuk with abstract methods keliling, luas
```

**Artinya:** "Tidak bisa membuat objek (*instantiate*) dari kelas abstrak `Bentuk` karena masih ada *method* abstrak yang belum punya isi: `keliling` dan `luas`." Perhatikan bahwa *error* ini muncul saat **program berjalan**, tepat ketika baris itu dijalankan. Python tidak memeriksanya lebih awal. Karena baris itu berada di awal `main()`, belum ada *output* lain yang sempat tercetak.

**Perbaikan:** jangan membuat objek dari kelas abstrak. Buat objek dari kelas konkret, misalnya `PersegiPanjang(8, 5)`. Setelah selesai mencoba, kembalikan baris **[4]** menjadi komentar (tekan Ctrl+/ lagi).

> [!NOTE]
> Baris berisi `~~~~^^` atau `^^^^` hanyalah penunjuk letak kesalahan, dan bentuknya berbeda antarversi Python. Fokuslah pada baris terakhir: jenis *error* (`TypeError`) dan kata kunci *Can't instantiate abstract class*.

> [!TIP]
> **Coba sendiri:** masih di salinan yang sama, pastikan baris **[4]** sudah menjadi komentar lagi. Lalu hapus seluruh *method* `keliling()` (baris `def keliling(self) -> int:` dan baris `return` di bawahnya) dari kelas `SegitigaSiku`. Simpan, lalu jalankan lagi. Baris mana yang sekarang *error*, dan apa bunyi pesannya?

<details>
<summary>Lihat jawaban</summary>

*Error* muncul di baris `penggaris = SegitigaSiku(6, 8, 10)` karena `SegitigaSiku` belum mengisi semua *method* abstrak sehingga ia masih abstrak. Baris terakhir pesannya di Python 3.12 ke atas:

```text
TypeError: Can't instantiate abstract class SegitigaSiku without an implementation for abstract method 'keliling'
```

Di Python 3.10 dan 3.11: `TypeError: Can't instantiate abstract class SegitigaSiku with abstract method keliling`. Objek `kartu` di baris sebelumnya tetap berhasil dibuat karena `PersegiPanjang` sudah lengkap.

Bandingkan dengan contoh 01: dulu lupa menulis *method* tidak diprotes, sekarang Python langsung menolak.

</details>

## 3. Konstruktor, Atribut, dan *Method* Konkret di Kelas Abstrak

*File*: [`contoh/contoh03_isi_kelas_abstrak.py`](contoh/contoh03_isi_kelas_abstrak.py)

Kelas abstrak bukan kelas kosong. Ia boleh punya konstruktor, atribut, dan *method* yang sudah berisi. Berikut potongan *file*-nya, mulai dari kelas abstrak `Kendaraan`:

```python
class Kendaraan(ABC):
    """Kelas abstrak: data dan perilaku bersama semua kendaraan."""

    def __init__(self, plat: str, bensin_liter: int):  # [1] konstruktor
        print(f"  (konstruktor Kendaraan dijalankan untuk {plat})")
        self._plat = plat  # [2] atribut bersama
        self._bensin = bensin_liter

    @property
    def plat(self) -> str:
        return self._plat

    def isi_bensin(self, liter: int):  # [3] method konkret: langsung diwarisi
        self._bensin += liter
        print(f"{self._plat} mengisi bensin {liter} liter")

    def jarak_tempuh(self) -> int:  # [4] method konkret yang memakai method abstrak
        return self._bensin * self.km_per_liter()

    def info(self) -> str:
        return (f"{type(self).__name__} {self._plat}: bensin {self._bensin} liter, "
                f"bisa menempuh {self.jarak_tempuh()} km")

    @abstractmethod
    def km_per_liter(self) -> int:  # [5] berbeda untuk setiap jenis kendaraan
        """Jarak (km) yang bisa ditempuh dengan 1 liter bensin."""


class Motor(Kendaraan):
    """Motor: tidak menulis __init__, jadi memakai konstruktor Kendaraan."""

    def km_per_liter(self) -> int:
        return 40


class Mobil(Kendaraan):
    """Mobil: punya atribut tambahan jumlah kursi."""

    def __init__(self, plat: str, bensin_liter: int, jumlah_kursi: int):
        super().__init__(plat, bensin_liter)  # [6] konstruktor kelas abstrak
        self._jumlah_kursi = jumlah_kursi

    def km_per_liter(self) -> int:
        return 12

    def info(self) -> str:  # method konkret milik induk juga boleh di-override
        return f"{super().info()}, {self._jumlah_kursi} kursi"
```

Program utamanya membuat `Motor("KT 1234 AB", 3)` dan `Mobil("KT 5678 CD", 20, 7)`, menampilkan info keduanya, mengisi bensin, lalu menampilkan info lagi.

***Output:***

```text
=== MEMBUAT KENDARAAN ===
  (konstruktor Kendaraan dijalankan untuk KT 1234 AB)
  (konstruktor Kendaraan dijalankan untuk KT 5678 CD)

=== INFO AWAL ===
Motor KT 1234 AB: bensin 3 liter, bisa menempuh 120 km
Mobil KT 5678 CD: bensin 20 liter, bisa menempuh 240 km, 7 kursi

=== ISI BENSIN (method konkret milik Kendaraan) ===
KT 1234 AB mengisi bensin 2 liter
KT 5678 CD mengisi bensin 10 liter
Motor KT 1234 AB: bensin 5 liter, bisa menempuh 200 km
Mobil KT 5678 CD: bensin 30 liter, bisa menempuh 360 km, 7 kursi
```

Penjelasan:

- **[1]** Kelas abstrak boleh punya konstruktor. Baris `print` membuktikan bahwa konstruktor ini **benar-benar berjalan** dua kali, yaitu saat objek `Motor` dan objek `Mobil` dibuat.
- **[2]** Atribut `_plat` dan `_bensin` dimiliki semua kendaraan, jadi cukup ditulis sekali di kelas abstrak.
- **[3]** `isi_bensin()` adalah *method* konkret. `Motor` dan `Mobil` langsung memakainya tanpa menulis ulang.
- **[4]** *Method* konkret boleh memanggil *method* abstrak. Saat `jarak_tempuh()` dijalankan oleh objek `Motor`, `self.km_per_liter()` memanggil versi milik `Motor` (40). Ini polimorfisme dari dalam kelas.
- **[5]** Hanya bagian yang benar-benar berbeda yang dijadikan abstrak.
- **[6]** `Mobil` punya atribut tambahan, jadi ia menulis `__init__` sendiri dan memanggil konstruktor kelas abstrak lewat `super().__init__(...)`. `Motor` tidak menulis `__init__` sehingga konstruktor `Kendaraan` dipakai apa adanya.

Plat `KT` pada contoh ini adalah kode plat nomor kendaraan Kalimantan Timur. Yang lebih penting, perhatikan betapa sedikitnya kode di kelas `Motor`: semua yang sama sudah diurus kelas abstrak.

## 4. *Template Method*

*File*: [`contoh/contoh04_template_method.py`](contoh/contoh04_template_method.py)

Sekarang kita pakai *method* konkret yang memanggil *method* abstrak untuk membuat **kerangka tetap**. Potongan pertama *file*-nya:

```python
LEBAR = 40


class Laporan(ABC):
    """Kelas abstrak untuk semua jenis laporan."""

    def tampilkan(self):  # [1] template method: urutan langkahnya selalu sama
        print("=" * LEBAR)
        print(self.judul())  # [2] langkah yang diisi kelas anak
        print("-" * LEBAR)
        for baris in self.isi():  # [2]
            print(baris)
        print("-" * LEBAR)
        print(self.penutup())  # [3] hook: sudah punya isi, boleh di-override
        print("=" * LEBAR)

    @abstractmethod
    def judul(self) -> str:
        """Judul laporan."""

    @abstractmethod
    def isi(self) -> list[str]:
        """Baris-baris isi laporan."""

    def penutup(self) -> str:
        return "Dicetak oleh Sistem Informasi Akademik"
```

Dua kelas anaknya, `LaporanKehadiran` dan `LaporanPerpustakaan`, sama-sama mengisi `judul()` dan `isi()`. Hanya `LaporanPerpustakaan` yang juga mengganti penutupnya:

```python
    def penutup(self) -> str:  # [4] meng-override hook
        return "Disahkan oleh Kepala Perpustakaan"
```

Program utamanya menyimpan kedua laporan dalam `list[Laporan]`, lalu:

```python
    for laporan in daftar:
        print()
        laporan.tampilkan()  # [5] satu panggilan, kerangka sama, isi berbeda
```

***Output:***

```text
=== MENCETAK 2 LAPORAN ===

========================================
LAPORAN KEHADIRAN PBO
----------------------------------------
Mahasiswa  : Ayu Lestari
Hadir      : 14 dari 16 pertemuan
Persentase : 87%
----------------------------------------
Dicetak oleh Sistem Informasi Akademik
========================================

========================================
LAPORAN PERPUSTAKAAN BULAN OKTOBER
----------------------------------------
Buku dipinjam      : 120
Sudah dikembalikan : 112
Belum dikembalikan : 8
----------------------------------------
Disahkan oleh Kepala Perpustakaan
========================================
```

Penjelasan:

- **[1]** `tampilkan()` adalah ***template method***. Ia adalah *method* konkret yang menetapkan urutan: garis, judul, garis, isi, garis, penutup, garis. Kelas anak tidak perlu (dan sebaiknya tidak) menulis ulang urutan ini.
- **[2]** Dua langkah yang berbeda untuk setiap laporan diserahkan ke *method* abstrak `judul()` dan `isi()`.
- **[3]** `penutup()` adalah *hook*: sudah punya isi bawaan, tetapi boleh diganti.
- **[4]** `LaporanPerpustakaan` meng-*override* *hook* itu, sedangkan `LaporanKehadiran` memakai versi bawaan. Bandingkan baris penutup kedua laporan di *output*.
- **[5]** Program utama cukup memanggil `tampilkan()`. Bentuk laporannya selalu rapi dan seragam.

Alur pemanggilannya saat `laporan.tampilkan()` dijalankan oleh objek `LaporanPerpustakaan`:

```text
Laporan.tampilkan()                      <- ditulis SEKALI di kelas abstrak
   |-- self.judul()   -> LaporanPerpustakaan.judul()     (wajib diisi anak)
   |-- self.isi()     -> LaporanPerpustakaan.isi()       (wajib diisi anak)
   '-- self.penutup() -> LaporanPerpustakaan.penutup()   (hook yang di-override)
```

## 5. "*Interface*" di Python: ABC yang Isinya Abstrak Semua

*File*: [`contoh/contoh05_interface.py`](contoh/contoh05_interface.py)

Python tidak punya kata kunci `interface`. Cara yang lazim adalah membuat kelas `ABC` yang **semua** *method*-nya abstrak dan **tidak** menyimpan data. Kelas seperti itu murni berisi daftar kemampuan. Potongan pertama *file*-nya:

```python
class BisaDinyalakan(ABC):  # [1] "interface": semua method-nya abstrak
    """Kontrak: benda ini bisa dinyalakan dan dimatikan."""

    @abstractmethod
    def nyalakan(self):
        """Menyalakan benda."""

    @abstractmethod
    def matikan(self):
        """Mematikan benda."""

    @abstractmethod
    def sedang_menyala(self) -> bool:
        """True jika benda sedang menyala."""


class Lampu(BisaDinyalakan):  # [2] memenuhi kontrak dengan mewarisinya
    """Lampu di sebuah ruangan."""
```

`Lampu` lalu menulis ketiga *method* itu dengan isinya sendiri, misalnya `nyalakan()` mencetak `Lampu teras menyala`. `KomporGas` dan `Televisi` melakukan hal yang sama dengan caranya masing-masing. Ketiga kelas itu tidak punya kelas induk bersama selain `BisaDinyalakan`. Fungsi yang memakai kontraknya:

```python
def matikan_semua(daftar: list[BisaDinyalakan]):  # [3] parameter bertipe kontrak
    """Mematikan semua benda yang masih menyala, apa pun jenisnya."""
    print(f"Memeriksa {len(daftar)} benda...")
    for benda in daftar:
        if benda.sedang_menyala():  # [4] yang dipakai hanya method dari kontrak
            benda.matikan()
    print("Semua sudah padam. Aman!")
```

Program utamanya menyalakan lampu, kompor, dan TV, mematikan TV, lalu memanggil `matikan_semua([lampu, kompor, tv])`.

***Output:***

```text
=== PAGI HARI ===
Lampu teras menyala
Kompor gas: klik... api biru menyala
TV menyala di saluran 5
TV dimatikan

=== SEBELUM BERANGKAT KULIAH ===
Memeriksa 3 benda...
Lampu teras padam
Kompor gas: api dimatikan, katup gas ditutup
Semua sudah padam. Aman!
```

Penjelasan:

- **[1]** Secara teknis, `BisaDinyalakan` hanyalah kelas abstrak. Yang membuatnya berperan sebagai *interface* adalah **cara kita memakainya**: semua *method* abstrak, tanpa atribut, dan namanya menggambarkan kemampuan.
- **[2]** `Lampu` memenuhi kontrak dengan **mewarisinya** secara tertulis. Kalau satu *method* saja lupa ditulis, objek `Lampu` tidak bisa dibuat.
- **[3]** *Type hint* `list[BisaDinyalakan]` memberi tahu pembaca kode: "fungsi ini menerima apa saja yang bisa dinyalakan".
- **[4]** Di dalam fungsi, kita hanya memanggil *method* yang dijanjikan kontrak. TV yang sudah dimatikan dilewati karena `sedang_menyala()`-nya bernilai salah.

> [!NOTE]
> Di Python, kelas `ABC` yang berperan sebagai *interface* sebenarnya **boleh** punya *method* berisi. *Method* seperti itu mirip *default method* di Java. Namun, agar perannya jelas, biasakan *interface* berisi *method* abstrak saja. Kalau butuh data dan kode bersama, gunakan kelas abstrak biasa.

> [!TIP]
> **Coba sendiri:** apa yang terjadi jika sebuah kelas mewarisi kontrak `BisaDinyalakan`, tetapi lupa menulis satu *method*? Salin `contoh/contoh05_interface.py` ke folder `pertemuan-10`-mu, lalu ikuti dua langkah di bawah.

1. Di salinan itu, tambahkan kelas berikut tepat di atas fungsi `matikan_semua()`:

   ```python
   class KipasAngin(BisaDinyalakan):
       """Kipas angin yang lupa menulis sedang_menyala()."""

       def nyalakan(self):
           print("Kipas angin berputar")

       def matikan(self):
           print("Kipas angin berhenti")
   ```

2. Di dalam `main()`, tambahkan baris `kipas = KipasAngin()` tepat di bawah baris `tv = Televisi(5)`, dengan indentasi yang sama. Simpan, lalu jalankan salinannya.

<details>
<summary>Lihat hasilnya</summary>

Program berhenti sebelum mencetak apa pun. Baris terakhir pesan *error*-nya (Python 3.12 ke atas):

```text
TypeError: Can't instantiate abstract class KipasAngin without an implementation for abstract method 'sedang_menyala'
```

Artinya: `KipasAngin` baru mengisi dua dari tiga *method* kontrak, jadi ia masih abstrak dan objeknya tidak bisa dibuat. Perbaikannya: tambahkan *method* `sedang_menyala()` di kelas `KipasAngin`. Perhatikan juga bahwa Python baru protes saat **objeknya dibuat**. Tanpa baris `kipas = KipasAngin()`, program berjalan seperti biasa.

</details>

## 6. Satu Kelas, Banyak Kemampuan

*File*: [`contoh/contoh06_banyak_interface.py`](contoh/contoh06_banyak_interface.py)

Satu kelas boleh mewarisi satu kelas abstrak **dan** memenuhi beberapa kontrak sekaligus.

Kelas abstrak `Hewan` di *file* ini menyimpan `nama` dan punya *method* abstrak `bersuara()`. Berikut potongan *file*-nya: dua kontrak kemampuan, lalu kelas `Bebek`.

```python
class BisaTerbang(ABC):
    """Kontrak kemampuan terbang."""

    @abstractmethod
    def terbang(self) -> str:
        """Menjelaskan cara terbang."""


class BisaBerenang(ABC):
    """Kontrak kemampuan berenang."""

    @abstractmethod
    def berenang(self) -> str:
        """Menjelaskan cara berenang."""


class Bebek(Hewan, BisaTerbang, BisaBerenang):  # [1] satu induk + dua kemampuan
    """Bebek: hewan yang bisa terbang dan berenang."""

    def bersuara(self) -> str:
        return "Kwek kwek!"

    def terbang(self) -> str:
        return f"{self.nama} terbang rendah di atas sawah"

    def berenang(self) -> str:
        return f"{self.nama} mengapung sambil mengayuh kaki"
```

Kelas `Ikan(Hewan, BisaBerenang)` hanya bisa berenang. Lalu ada kelas yang sama sekali bukan hewan:

```python
class Pesawat(BisaTerbang):  # [2] bukan Hewan, tetapi BisaTerbang
    """Pesawat: benda mati yang bisa terbang."""
```

Potongan program utamanya:

```python
    print("=== YANG BISA TERBANG ===")
    penerbang: list[BisaTerbang] = [bebek, pesawat]  # [3] dikelompokkan per kontrak
    for benda in penerbang:
        print(benda.terbang())
```

dan bagian pemeriksaan kemampuan:

```python
    for benda in [bebek, ikan, pesawat]:
        nama = type(benda).__name__
        hewan = ya_tidak(isinstance(benda, Hewan))  # [4]
        terbang = ya_tidak(isinstance(benda, BisaTerbang))
        berenang = ya_tidak(isinstance(benda, BisaBerenang))
        print(f"{nama:<8} | {hewan:<5} | {terbang:<7} | {berenang}")
```

***Output:***

```text
=== SEMUA HEWAN BERSUARA ===
Bebek Kuning: Kwek kwek!
Ikan Patin: (diam saja)

=== YANG BISA TERBANG ===
Bebek Kuning terbang rendah di atas sawah
Pesawat Rajawali 01 terbang di atas awan

=== YANG BISA BERENANG ===
Bebek Kuning mengapung sambil mengayuh kaki
Ikan Patin berenang di Sungai Mahakam

=== CEK KEMAMPUAN ===
Kelas    | Hewan | Terbang | Berenang
Bebek    | ya    | ya      | ya
Ikan     | ya    | tidak   | ya
Pesawat  | tidak | ya      | tidak
```

Penjelasan:

- **[1]** Di dalam kurung, tulis kelas induk "jenis" lebih dulu (`Hewan`), lalu kontrak-kontrak kemampuannya. Ini memakai pewarisan ganda (*multiple inheritance*) yang sudah kamu kenal di Pertemuan 07, tetapi perannya jelas: satu jenis, beberapa kemampuan.
- **[2]** `Pesawat` tidak punya hubungan dengan `Hewan`. Ia hanya memenuhi kontrak `BisaTerbang`.
- **[3]** `bebek` dan `pesawat` bisa berada di *list* yang sama karena keduanya `BisaTerbang`.
- **[4]** `isinstance()` juga bisa memeriksa kontrak. Pertanyaannya bukan lagi "kamu kelas apa?", tetapi "kamu **bisa** apa?".

## 7. `typing.Protocol`: *Duck Typing* yang Diresmikan

*File*: [`contoh/contoh07_protocol.py`](contoh/contoh07_protocol.py) (contoh ini khusus Python, lihat [Jembatan](../jembatan-python-java.md))

Dengan `ABC`, sebuah kelas harus **mewarisi** kontraknya secara tertulis. Python punya cara kedua: `typing.Protocol`. Kelas tidak perlu mewarisi apa pun. Asal punya *method* dengan nama dan bentuk yang cocok, kelas itu dianggap memenuhi kontrak. Ini persis *duck typing* dari Pertemuan 09, hanya saja kini kontraknya **tertulis**. Potongan pertama *file*-nya:

```python
from typing import Protocol, runtime_checkable


@runtime_checkable  # [3] agar Protocol ini boleh dipakai di isinstance()
class BisaBersuara(Protocol):  # [1] kontrak struktural
    """Apa saja yang punya method bersuara() -> str."""

    def bersuara(self) -> str:
        ...


class Kucing:  # [2] TIDAK mewarisi BisaBersuara
    """Kucing peliharaan."""

    def bersuara(self) -> str:
        return "Meong!"
```

Kelas `Kentongan` dan `AlarmPonsel` juga punya `bersuara()`, sedangkan kelas `Batu` tidak. Berikut fungsi dan program utamanya (dua potongan berikutnya dari *file* yang sama):

```python
def bunyikan_semua(daftar: list[BisaBersuara]):  # [4] menerima apa saja yang cocok
    for benda in daftar:
        print(f"{type(benda).__name__:<11}: {benda.bersuara()}")
```

```python
def main():
    print("=== BUNYIKAN SEMUA ===")
    bunyikan_semua([Kucing(), Kentongan(), AlarmPonsel("07.00")])

    print()
    print("=== CEK DENGAN isinstance() ===")
    for benda in [Kucing(), Kentongan(), Batu()]:
        cocok = ya_tidak(isinstance(benda, BisaBersuara))  # [5]
        print(f"{type(benda).__name__} cocok dengan BisaBersuara? {cocok}")
```

***Output:***

```text
=== BUNYIKAN SEMUA ===
Kucing     : Meong!
Kentongan  : Tung tung tung!
AlarmPonsel: Kring! Sudah jam 07.00, ayo berangkat kuliah!

=== CEK DENGAN isinstance() ===
Kucing cocok dengan BisaBersuara? ya
Kentongan cocok dengan BisaBersuara? ya
Batu cocok dengan BisaBersuara? tidak
```

Penjelasan:

- **[1]** Kelas yang mewarisi `Protocol` adalah kontrak **struktural**: yang dilihat adalah "bentuk" kelas (*method* apa saja yang dimiliki), bukan silsilahnya. Isi *method* di dalam `Protocol` cukup `...`.
- **[2]** `Kucing`, `Kentongan`, dan `AlarmPonsel` tidak menyebut `BisaBersuara` sama sekali, tetapi tetap cocok.
- **[3]** `@runtime_checkable` membuat `Protocol` boleh dipakai di `isinstance()`. Tanpa dekorator ini, `isinstance()` dengan `Protocol` berhenti dengan `TypeError: Instance and class checks can only be used with @runtime_checkable protocols`.
- **[4]** *Type hint* `list[BisaBersuara]` mendokumentasikan syarat fungsi: semua isinya harus bisa bersuara.
- **[5]** `isinstance()` dengan `Protocol` hanya memeriksa **ada atau tidaknya** *method* bernama `bersuara`. Ia tidak memeriksa parameter atau tipe nilai kembaliannya.

### Siapa yang memeriksa `Protocol`?

Python sendiri **tidak** memeriksa `Protocol` saat program berjalan. Buktikan di salinan:

1. Salin `contoh/contoh07_protocol.py` ke folder `pertemuan-10`-mu, lalu buka salinannya.
2. Di dalam `main()`, tambahkan baris berikut tepat di bawah pemanggilan `bunyikan_semua(...)` yang pertama, dengan indentasi yang sama:

   ```python
       bunyikan_semua([Batu()])
   ```

3. Simpan, lalu jalankan salinannya.

Judul `=== BUNYIKAN SEMUA ===` dan tiga baris di bawahnya tetap tercetak. Program baru berhenti ketika `bersuara()` dipanggil pada objek `Batu`. Pesan *error*-nya (Python 3.13):

```text
Traceback (most recent call last):
  File "contoh07_protocol.py", line 79, in <module>
    main()
    ~~~~^^
  File "contoh07_protocol.py", line 69, in main
    bunyikan_semua([Batu()])
    ~~~~~~~~~~~~~~^^^^^^^^^^
  File "contoh07_protocol.py", line 59, in bunyikan_semua
    print(f"{type(benda).__name__:<11}: {benda.bersuara()}")
                                         ^^^^^^^^^^^^^^
AttributeError: 'Batu' object has no attribute 'bersuara'
```

**Artinya:** objek `Batu` tidak punya *method* `bersuara`. *Type hint* `list[BisaBersuara]` tidak menghentikan Python karena *type hint* hanyalah keterangan untuk pembaca dan alat bantu. Baca *traceback* dari bawah: baris terakhir menyebut jenis *error*-nya, dan baris di atasnya menunjukkan bahwa *error* terjadi di dalam `bunyikan_semua()`, yang dipanggil dari baris tambahanmu di `main()`.

Pemeriksa `Protocol` yang sesungguhnya adalah **alat pemeriksa tipe** (*type checker*), misalnya Pylance (pemeriksa yang ikut terpasang bersama ekstensi Python di VS Code) atau mypy (harus dipasang terpisah). Alat itu membaca *type hint* dan bisa memberi garis merah pada `bunyikan_semua([Batu()])` **sebelum** program dijalankan.

> [!NOTE]
> Pemeriksaan tipe Pylance **mati** secara bawaan, jadi garis merah itu belum muncul. Untuk menyalakannya, tekan Ctrl+, (macOS: Cmd+,) untuk membuka **Settings**, ketik `type checking` di kotak pencarian, lalu ubah **Python › Analysis: Type Checking Mode** dari **off** menjadi **standard**. Setelah itu, baris tambahanmu diberi garis merah, dan di panel **PROBLEMS** muncul pesan yang diawali *Argument of type "list[Batu]" cannot be assigned to parameter "daftar"*. Pengaturan ini juga memunculkan pengingat di tempat lain, misalnya bahwa `cari_menu()` di `studi-kasus/main.py` bisa mengembalikan `None` (ingat Pertemuan 05). Programnya tetap berjalan normal. Jika garis merah itu terasa mengganggu, kembalikan pengaturannya ke **off**.

| | `ABC` + `@abstractmethod` | `typing.Protocol` |
|---|---|---|
| Kelas harus mewarisi kontrak? | ya, ditulis di dalam kurung | tidak |
| Kapan ketahuan jika tidak cocok? | saat objek dibuat (`TypeError`) | saat diperiksa alat seperti Pylance atau mypy; saat berjalan, baru *error* ketika *method*-nya dipanggil |
| Cocok untuk | kelas-kelas buatan sendiri yang memang dirancang memenuhi kontrak | menerima objek dari kode lain yang tidak bisa kamu ubah |
| Dipakai di KedaiKita | ya (`Pembayaran`, `DapatDicetak`) | tidak |

## 8. Studi Kasus KedaiKita

*File*: [`studi-kasus/pembayaran.py`](studi-kasus/pembayaran.py), [`studi-kasus/dapat_dicetak.py`](studi-kasus/dapat_dicetak.py), [`studi-kasus/pesanan.py`](studi-kasus/pesanan.py), [`studi-kasus/kedai.py`](studi-kasus/kedai.py), dan [`studi-kasus/main.py`](studi-kasus/main.py)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#11-studi-kasus-kedaikita-pembayaran-abstrak-dan-kontrak-dapatdicetak).

**Apa yang berubah dibanding Pertemuan 09?**

- `pembayaran.py`: `Pembayaran` kini mewarisi `ABC`. `nama_metode()` dan `proses()` menjadi *method* abstrak sehingga isi lamanya (`"Pembayaran umum"` dan `"Memproses pembayaran ..."`) dihapus. Ada *method* konkret baru, `deskripsi(total)`. Ketiga kelas anaknya **tidak berubah**.
- `dapat_dicetak.py` (***file* baru**): "*interface*" `DapatDicetak` dengan satu *method* abstrak, `cetak()`.
- `pesanan.py`: `class Pesanan(DapatDicetak)`. *Method* `cetak_struk()` **berganti nama** menjadi `cetak()`. Isinya tidak berubah.
- `kedai.py`: `class Kedai(DapatDicetak)`. *Method* `tampilkan_menu()` **berganti nama** menjadi `cetak()`. Isinya tidak berubah.
- `main.py`: ada fungsi baru `cetak_semua()`. Bagian "SATU PANGGILAN, BANYAK BENTUK" diganti bagian baru "MENGENAL METODE PEMBAYARAN", dan bagian "MEMERIKSA JENIS PEMBAYARAN" tidak dipakai lagi. Daftar menu dan struk kini dicetak bersama di akhir lewat `cetak_semua()`, setelah pembayaran, sehingga status struknya sudah LUNAS.
- `menu.py`, `pelanggan.py`, dan `utilitas.py` **tidak berubah sama sekali**.

### Kelas abstrak `Pembayaran`

Potongan dari `pembayaran.py` (kelas `Pembayaran` saja; tiga kelas anaknya tidak berubah):

```python
from abc import ABC, abstractmethod

from utilitas import format_rupiah


class Pembayaran(ABC):
    """Kelas abstrak: kerangka untuk semua metode pembayaran."""

    @abstractmethod
    def nama_metode(self) -> str:
        """Nama metode pembayaran, misalnya 'Tunai'."""

    @abstractmethod
    def proses(self, total: int) -> bool:
        """Memproses pembayaran. Mengembalikan True jika berhasil."""

    def hitung_biaya_layanan(self, total: int) -> int:
        """Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override)."""
        return 0

    def deskripsi(self, total: int) -> str:
        """Method konkret yang memanggil method abstrak."""
        biaya = format_rupiah(self.hitung_biaya_layanan(total))
        return f"{self.nama_metode()} (biaya layanan {biaya})"
```

- `nama_metode()` dan `proses()` kini **wajib** diisi setiap jenis pembayaran. Masalah "lupa menulis `proses()` lalu pesanan tercatat LUNAS" tidak mungkin terjadi lagi.
- `hitung_biaya_layanan()` adalah *hook*: bawaannya 0, dan hanya `PembayaranKartu` yang meng-*override*-nya (2%).
- `deskripsi()` adalah *template method* kecil. Ia ditulis sekali, tetapi hasilnya berbeda untuk setiap jenis pembayaran.

### "*Interface*" `DapatDicetak`

Isi lengkap `dapat_dicetak.py`, tanpa komentar pembuka:

```python
from abc import ABC, abstractmethod


class DapatDicetak(ABC):
    """Kontrak: objek ini bisa dicetak ke layar."""

    @abstractmethod
    def cetak(self):
        """Mencetak isi objek ke layar."""
```

### `Kedai` dan `Pesanan` memenuhi kontrak

Perubahan di dua kelas ini sangat kecil. Ringkasannya (bukan kode lengkap):

```text
Pertemuan 09                          Pertemuan 10
class Pesanan:                   ->   class Pesanan(DapatDicetak):
    def cetak_struk(self):       ->       def cetak(self):

class Kedai:                     ->   class Kedai(DapatDicetak):
    def tampilkan_menu(self):    ->       def cetak(self):
```

Contohnya, *method* `cetak()` milik `Kedai` (potongan dari `kedai.py`):

```python
    def cetak(self):
        """Mencetak daftar menu (memenuhi kontrak DapatDicetak)."""
        print(f"=== MENU {self._nama} ===")
        for menu in self._daftar_menu:
            print(menu)
```

**Mengapa namanya harus diganti?** Kontrak `DapatDicetak` menuntut *method* bernama persis `cetak()`. Seandainya `Pesanan` sudah mewarisi `DapatDicetak` tetapi *method*-nya masih bernama `cetak_struk()`, kontraknya tidak terpenuhi. Python lalu menolak membuat objek `Pesanan`. Baris terakhir pesan *error*-nya (Python 3.12 ke atas):

```text
TypeError: Can't instantiate abstract class Pesanan without an implementation for abstract method 'cetak'
```

(Di Python 3.10 dan 3.11: `TypeError: Can't instantiate abstract class Pesanan with abstract method cetak`.)

Nama yang seragam inilah kuncinya. Karena kedai dan pesanan sama-sama punya `cetak()`, keduanya bisa dicetak oleh satu perulangan.

### `main.py`: mencetak apa saja yang `DapatDicetak`

Potongan dari `main.py`, dimulai dari fungsi barunya:

```python
def cetak_semua(daftar_dokumen: list[DapatDicetak]):
    """Mencetak objek apa pun, asalkan ia memenuhi kontrak DapatDicetak."""
    jumlah = len(daftar_dokumen)
    for nomor, dokumen in enumerate(daftar_dokumen, start=1):
        print(f"--- Dokumen {nomor} dari {jumlah} ---")
        dokumen.cetak()
        print()
```

Di dalam `main()`, bagian baru yang pertama memakai `deskripsi()`:

```python
    print("=== MENGENAL METODE PEMBAYARAN ===")
    daftar_metode = [PembayaranTunai(100000), PembayaranQRIS(50000),
                     PembayaranKartu("BNI")]
    for metode in daftar_metode:
        print(metode.deskripsi(100000))
    print()
```

Bagian transaksi Budi dan Siti sama seperti Pertemuan 09, hanya saja pemanggilan `cetak_struk()` tidak ada lagi di sana. Struk dan daftar menu kini dicetak bersama di akhir:

```python
    print("=== CETAK SEMUA DOKUMEN ===")
    cetak_semua([kedai, pesanan_budi, pesanan_siti])
```

Cara menjalankannya sudah dibahas di [Persiapan](#cara-menjalankan-studi-kasus): di VS Code, buka `studi-kasus/main.py` lalu klik ▷, atau lewat terminal. Dari folder utama materi:

```bash
cd Pertemuan-10-Abstract-Class-dan-Interface/python/studi-kasus
python main.py
```

***Output:***

```text
=== MENGENAL METODE PEMBAYARAN ===
Tunai (biaya layanan Rp0)
QRIS (biaya layanan Rp0)
Kartu Kredit BNI (biaya layanan Rp2.000)

=== TRANSAKSI ===
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)

Pembayaran pesanan P002 (Siti Aminah)
  Metode       : QRIS
  Total bayar  : Rp31.000
  Saldo e-wallet tidak cukup (saldo Rp20.000)
  Status       : GAGAL, silakan pilih metode lain

Pembayaran pesanan P002 (Siti Aminah)
  Metode       : Kartu Kredit BNI
  Biaya layanan: Rp620
  Total bayar  : Rp31.620
  Transaksi kartu BNI disetujui sebesar Rp31.620
  Status       : LUNAS (+3 poin)

=== CETAK SEMUA DOKUMEN ===
--- Dokumen 1 dari 3 ---
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 28 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 11 | pedas level 0

--- Dokumen 2 dari 3 ---
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
Status      : LUNAS
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================

--- Dokumen 3 dari 3 ---
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
Status      : LUNAS
----------------------------------------
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
----------------------------------------
TOTAL                           Rp31.000
========================================

=== POIN PELANGGAN ===
Budi Santoso (081234567890) - 6 poin
Siti Aminah (082198765432) - 3 poin
```

Hal-hal yang perlu diperhatikan:

- Bagian "MENGENAL METODE PEMBAYARAN" dihasilkan oleh **satu** *method* `deskripsi()` milik kelas abstrak. Teksnya berbeda karena `nama_metode()` dan `hitung_biaya_layanan()` dijawab oleh kelas anak masing-masing.
- Di "CETAK SEMUA DOKUMEN", dokumen 1 adalah objek `Kedai`, sedangkan dokumen 2 dan 3 adalah objek `Pesanan`. Fungsi `cetak_semua()` tidak tahu dan tidak perlu tahu. Ia hanya memanggil `dokumen.cetak()`.
- *Type hint* `list[DapatDicetak]` membuat syarat fungsi itu jelas bagi siapa pun yang membaca kodenya.
- Stok menu di daftar menu sudah berkurang (misalnya M01 tinggal 18) karena daftar menu dicetak setelah transaksi.

> [!TIP]
> **Coba sendiri:** buktikan bahwa lupa menulis `proses()` kini langsung ketahuan. Salin **seluruh folder** `studi-kasus` ke folder `pertemuan-10`-mu sehingga terbentuk `PBO-latihan-saya/pertemuan-10/studi-kasus`. Di dalam salinan itu, buat *file* baru bernama `coba_ewallet.py` berisi kode di bawah. *File* itu harus berada satu folder dengan `pembayaran.py` dan `utilitas.py` agar `import`-nya berhasil.

Isi `coba_ewallet.py` (program kecil buatanmu sendiri):

```python
from pembayaran import Pembayaran


class PembayaranEWallet(Pembayaran):
    """Metode pembayaran baru yang LUPA menulis proses()."""

    def nama_metode(self) -> str:
        return "E-Wallet"


bayar = PembayaranEWallet()
print(bayar.deskripsi(50000))
```

Simpan, lalu jalankan *file* itu dengan tombol ▷, atau dari terminal yang berada di folder salinan `studi-kasus` dengan `python coba_ewallet.py`. Apa yang terjadi? Bandingkan dengan Pertemuan 09.

<details>
<summary>Lihat jawaban</summary>

Python menolak membuat objeknya. Pesan *error*-nya (Python 3.13):

```text
Traceback (most recent call last):
  File "coba_ewallet.py", line 11, in <module>
    bayar = PembayaranEWallet()
TypeError: Can't instantiate abstract class PembayaranEWallet without an implementation for abstract method 'proses'
```

Di Python 3.10 dan 3.11, baris terakhirnya berbunyi `... with abstract method proses`.

Di Pertemuan 09, kelas yang sama akan diterima begitu saja dan memakai `proses()` milik induk yang selalu berhasil. Kini kesalahan itu tertangkap seketika, sebelum ada satu pun pesanan yang dibayar. Untuk memperbaikinya, tambahkan *method* `proses(self, total: int) -> bool` di kelas `PembayaranEWallet`.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan *Error*

Ingat, pesan *error* Python dibaca **dari bawah ke atas**. Baris terakhir menyebutkan jenis *error* dan penyebabnya. Jika ingin meniru kesalahan-kesalahan berikut, kerjakan di folder `pertemuan-10`-mu, bukan di *file* materi.

### Kesalahan 1: Membuat objek dari kelas abstrak atau "*interface*"

Misalnya, di salinan `main.py` milik studi kasus (lihat **Coba sendiri** di bagian 8), baris berikut ditambahkan di dalam `main()`:

```python
    dokumen = DapatDicetak()
```

Baris terakhir pesan *error*-nya:

```text
TypeError: Can't instantiate abstract class DapatDicetak without an implementation for abstract method 'cetak'
```

**Artinya:** `DapatDicetak` masih punya *method* abstrak, jadi objeknya tidak bisa dibuat. **Perbaikan:** buat objek dari kelas **konkret** yang memenuhi kontraknya, misalnya `Kedai("KedaiKita")`.

### Kesalahan 2: Lupa mewarisi `ABC`

Buat *file* baru bernama `coba_lupa_abc.py` di folder `pertemuan-10`-mu, isi dengan kode berikut, lalu jalankan:

```python
from abc import abstractmethod


class Bentuk:  # lupa mewarisi ABC
    @abstractmethod
    def luas(self) -> int:
        """Menghitung luas."""


bentuk = Bentuk()
print("Objek Bentuk berhasil dibuat!")
print(f"Luasnya: {bentuk.luas()}")
```

Tidak ada *error* sama sekali. Hasilnya:

```text
Objek Bentuk berhasil dibuat!
Luasnya: None
```

**Artinya:** `@abstractmethod` hanya bekerja jika kelasnya mewarisi `ABC`. Tanpa `ABC`, dekorator itu diam saja, dan `luas()` yang isinya hanya *docstring* mengembalikan `None`. Ini *bug* licin karena Python tidak protes. **Perbaikan:** `class Bentuk(ABC):` dan jangan lupa `from abc import ABC, abstractmethod`.

### Kesalahan 3: Kelas anak lupa mengisi salah satu *method* abstrak

Misalnya, `SegitigaSiku` hanya menulis `luas()`, seperti pada **Coba sendiri** di bagian 2, lalu objeknya dibuat dengan `SegitigaSiku(6, 8, 10)`. Baris terakhir pesan *error*-nya:

```text
TypeError: Can't instantiate abstract class SegitigaSiku without an implementation for abstract method 'keliling'
```

**Artinya:** `SegitigaSiku` baru mengisi `luas()`. Karena `keliling()` belum diisi, `SegitigaSiku` masih dianggap abstrak. **Perbaikan:** tambahkan *method* `keliling()`. Perhatikan juga ejaannya. Salah ketik seperti `kelilling()` dianggap *method* baru sehingga `keliling()` tetap belum terisi dan *error* yang sama muncul.

### Kesalahan 4: Mengira `Protocol` diperiksa saat program berjalan

Sudah dibahas di [bagian 7](#7-typingprotocol-duck-typing-yang-diresmikan): mengirim `Batu()` ke fungsi yang mengharapkan `BisaBersuara` baru *error* ketika `bersuara()` dipanggil (`AttributeError`). **Perbaikan:** nyalakan pemeriksaan tipe Pylance (caranya ada di catatan bagian 7) agar kesalahan seperti ini ketahuan sebelum program dijalankan, atau pakai `ABC` jika kamu ingin Python sendiri yang menolak.

> [!NOTE]
> Di Python 3.10 dan 3.11, bunyi pesan `TypeError` di atas sedikit berbeda: `... with abstract method keliling` (tanpa tanda kutip dan tanpa kata *without an implementation for*). Maknanya sama persis.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Mengimpor alat kelas abstrak | `from abc import ABC, abstractmethod` | ditulis di bagian atas *file* |
| Kelas abstrak | `class Nama(ABC):` | `class Bentuk(ABC):` |
| *Method* abstrak | `@abstractmethod` di atas `def` | `@abstractmethod`<br>`def luas(self) -> int:` |
| Kelas anak konkret | mewarisi lalu mengisi semua *method* abstrak | `class PersegiPanjang(Bentuk):` |
| Memanggil konstruktor kelas abstrak | `super().__init__(...)` | `super().__init__(plat, bensin_liter)` |
| "*Interface*" | kelas `ABC` berisi *method* abstrak saja | `class DapatDicetak(ABC):` |
| Satu induk + banyak kontrak | `class Anak(Induk, KontrakA, KontrakB):` | `class Bebek(Hewan, BisaTerbang, BisaBerenang):` |
| Memeriksa kontrak | `isinstance(objek, Kontrak)` | `isinstance(bebek, BisaTerbang)` |
| Kontrak struktural | `class Nama(Protocol):` | `class BisaBersuara(Protocol):` |
| Protocol untuk `isinstance()` | `@runtime_checkable` | `@runtime_checkable`<br>`class BisaBersuara(Protocol):` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
