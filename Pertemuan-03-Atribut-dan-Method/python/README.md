# 🐍 Praktik Python Pertemuan 03: Atribut dan *Method* Lebih Dalam

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 03](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Atribut Objek dan Atribut Kelas](#1-atribut-objek-dan-atribut-kelas)
2. [Jebakan: Mengubah Atribut Kelas lewat Objek](#2-jebakan-mengubah-atribut-kelas-lewat-objek)
3. [*Static Method*, *Class Method*, dan Fungsi Biasa](#3-static-method-class-method-dan-fungsi-biasa)
4. [Parameter dengan Nilai Bawaan](#4-parameter-dengan-nilai-bawaan)
5. [Representasi Teks dengan `__str__`](#5-representasi-teks-dengan-__str__)
6. [Referensi, *Aliasing*, dan `None`](#6-referensi-aliasing-dan-none)
7. [Objek sebagai Parameter](#7-objek-sebagai-parameter)
8. [Objek sebagai Nilai Kembalian](#8-objek-sebagai-nilai-kembalian)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 8 contoh, dari yang paling sederhana
├── studi-kasus/     <- KedaiKita versi Pertemuan 03
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara Menjalankan Contoh

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-03-Atribut-dan-Method/python`. Buka *file* contoh yang ingin dicoba, lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah.

**Cara 2: lewat terminal.** Buka terminal (di VS Code: menu **Terminal → New Terminal**), pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-03-Atribut-dan-Method/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_atribut_kelas.py
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di [bagian 1](#1-atribut-objek-dan-atribut-kelas). Untuk contoh lain, ganti nama *file*-nya. *File* di folder `studi-kasus` dan `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan nama folder itu.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Penjelasan lengkap tentang terminal ada di [Menjalankan Program](../../00-Persiapan/menjalankan-program.md).

### Tempat Menyimpan Kodemu Sendiri

Simpan semua kode buatanmu (hasil mengetik ulang, percobaan "Coba sendiri", *file* coretan seperti `coba.py`, dan jawaban latihan) di folder `PBO-latihan-saya/pertemuan-03/`, **di luar** folder materi. Jika sebuah percobaan memintamu mengubah *file* contoh, salin dulu *file* itu ke folder tersebut (lewat File Explorer di Windows atau Finder di macOS), lalu ubah dan jalankan salinannya. Untuk menjalankan salinan itu, buka folder `pertemuan-03` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**); terminal di jendela itu (**Terminal → New Terminal**) langsung berada di folder `pertemuan-03`. Alasan dan cara menyalinnya ada di [aturan emas 00-Persiapan](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

```text
Documents/
├── PBO2026/                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/
    └── pertemuan-03/         <- salinan contoh, coba.py, dan jawaban latihanmu
```

### Cara Membaca Kode di Halaman Ini

- Setiap bagian diawali baris ***File*:** atau **Potongan dari** yang menautkan *file* contohnya.
- ***File*:** berarti kode di bawahnya adalah isi lengkap *file* itu, hanya tanpa komentar pembuka (*docstring*), termasuk dua baris penutup `if __name__ == "__main__":` dan `main()`. Hasil ketik ulangnya bisa langsung dijalankan.
- **Potongan dari** berarti yang ditampilkan hanya sebagian. Jangan mengetik ulang potongannya saja; jalankan *file* lengkapnya dengan cara di atas.
- Tanda `# [1]`, `# [2]`, dan seterusnya di dalam kode dijelaskan satu per satu dalam daftar **Penjelasan** tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* materi itu dijalankan. Hasil percobaan "Coba sendiri" yang kamu kerjakan di folder `pertemuan-03` ada di balik tulisan **Lihat jawaban** atau **Lihat hasilnya**.

## 1. Atribut Objek dan Atribut Kelas

*File*: [`contoh/contoh01_atribut_kelas.py`](contoh/contoh01_atribut_kelas.py)

Atribut kelas ditulis **langsung di badan kelas**, di luar *method* dan tanpa `self.`. Atribut objek tetap ditulis seperti di Pertemuan 02, yaitu `self.atribut = nilai` di dalam `__init__`.

```python
class Mahasiswa:
    """Mahasiswa Informatika di Samarinda."""

    kampus = "Unmul"  # [1] atribut kelas: sama untuk semua mahasiswa
    jumlah = 0  # [2] atribut kelas: penghitung objek yang sudah dibuat

    def __init__(self, nim, nama):
        self.nim = nim  # [3] atribut objek: milik masing-masing mahasiswa
        self.nama = nama
        Mahasiswa.jumlah += 1  # [4] mengubah atribut kelas lewat NAMA KELAS

    def perkenalan(self):
        print(f"Saya {self.nama} ({self.nim}) dari {Mahasiswa.kampus}")  # [5]


def main():
    print("=== SEBELUM ADA OBJEK ===")
    print(f"Kampus          : {Mahasiswa.kampus}")  # [6] dibaca tanpa objek
    print(f"Jumlah mahasiswa: {Mahasiswa.jumlah}")

    ayu = Mahasiswa("2409106001", "Ayu Lestari")
    bima = Mahasiswa("2409106002", "Bima Saputra")
    citra = Mahasiswa("2409106003", "Citra Dewi")

    print()
    print("=== SETELAH TIGA OBJEK DIBUAT ===")
    ayu.perkenalan()
    bima.perkenalan()
    citra.perkenalan()
    print(f"Jumlah mahasiswa: {Mahasiswa.jumlah}")

    print()
    print("=== NAMA KAMPUS DITULIS LENGKAP ===")
    Mahasiswa.kampus = "Universitas Mulawarman"  # [7] berlaku untuk SEMUA objek
    ayu.perkenalan()
    bima.perkenalan()
    citra.perkenalan()


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== SEBELUM ADA OBJEK ===
Kampus          : Unmul
Jumlah mahasiswa: 0

=== SETELAH TIGA OBJEK DIBUAT ===
Saya Ayu Lestari (2409106001) dari Unmul
Saya Bima Saputra (2409106002) dari Unmul
Saya Citra Dewi (2409106003) dari Unmul
Jumlah mahasiswa: 3

=== NAMA KAMPUS DITULIS LENGKAP ===
Saya Ayu Lestari (2409106001) dari Universitas Mulawarman
Saya Bima Saputra (2409106002) dari Universitas Mulawarman
Saya Citra Dewi (2409106003) dari Universitas Mulawarman
```

Penjelasan:

- **[1]** `kampus` ditulis di badan kelas, jadi ia adalah **atribut kelas**. Nilainya hanya satu dan dipakai bersama oleh semua objek `Mahasiswa`.
- **[2]** `jumlah` juga atribut kelas. Ia dipakai sebagai **penghitung** objek yang sudah dibuat, dimulai dari 0.
- **[3]** `self.nim` dan `self.nama` adalah **atribut objek**: setiap mahasiswa punya nilainya sendiri.
- **[4]** Setiap kali konstruktor berjalan, penghitung bertambah satu. Perhatikan cara menulisnya: lewat **nama kelas** (`Mahasiswa.jumlah`), bukan lewat `self`. Alasannya dibahas di bagian 2.
- **[5]** *Method* objek boleh membaca atribut kelas. Lagi-lagi kita menulisnya lewat nama kelas agar jelas bahwa `kampus` milik bersama.
- **[6]** Atribut kelas sudah ada **sebelum** objek mana pun dibuat. Karena itu, `Mahasiswa.jumlah` bisa dibaca dan hasilnya 0.
- **[7]** Mengubah atribut kelas **satu kali** langsung berlaku untuk **semua** objek. Ketiga mahasiswa kini memperkenalkan nama kampus yang lengkap.

### Membaca atribut kelas lewat objek

Python juga mengizinkan kita **membaca** atribut kelas lewat objek, misalnya `ayu.kampus`. Saat membaca atribut lewat objek, Python mencari dengan urutan seperti ini (nilai di sebelah kanan adalah keadaan di akhir program):

```text
ayu.nama   : 1. cari di objek ayu        -> ketemu    -> "Ayu Lestari"

ayu.kampus : 1. cari di objek ayu        -> tidak ada
             2. cari di kelas Mahasiswa  -> ketemu    -> "Universitas Mulawarman"
```

Membaca seperti ini aman. Masalah baru muncul saat kita **mengisi** atribut lewat objek. Itulah jebakan di bagian berikutnya.

> [!TIP]
> **Coba sendiri:** salin `contoh/contoh01_atribut_kelas.py` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di akhir fungsi `main()`, tambahkan empat baris berikut (menjorok 4 spasi, sejajar dengan baris di atasnya), simpan, lalu jalankan salinan itu. Tebak dulu tiga baris terakhir *output*-nya.
>
> ```python
>     dimas = Mahasiswa("2409106004", "Dimas Pratama")
>     print(Mahasiswa.jumlah)
>     print(ayu.kampus)
>     print(ayu.jumlah)
> ```

<details>
<summary>Lihat jawaban</summary>

Tiga baris terakhirnya `4`, `Universitas Mulawarman`, lalu `4`. Membuat objek `dimas` menaikkan penghitung menjadi 4. Objek `ayu` tidak punya atribut `kampus` maupun `jumlah` sendiri, jadi Python membacanya dari kelas `Mahasiswa`, persis seperti urutan pencarian di atas.

</details>

## 2. Jebakan: Mengubah Atribut Kelas lewat Objek

*File*: [`contoh/contoh02_jebakan_atribut_kelas.py`](contoh/contoh02_jebakan_atribut_kelas.py)

Contoh ini memperlihatkan kesalahan yang **sangat sering** terjadi. Perpustakaan kampus ingin menghitung jumlah pengunjung hari ini. Kita bandingkan dua cara menambah penghitung.

```python
class Pengunjung:
    """Pengunjung perpustakaan kampus."""

    total = 0  # atribut kelas: jumlah seluruh pengunjung hari ini

    def __init__(self, nama):
        self.nama = nama

    def masuk_lewat_objek(self):
        self.total += 1  # [1] JEBAKAN: membuat atribut OBJEK baru bernama total

    def masuk_lewat_kelas(self):
        Pengunjung.total += 1  # [2] BENAR: mengubah atribut kelas milik bersama


def main():
    ayu = Pengunjung("Ayu")
    bima = Pengunjung("Bima")

    print("=== LEWAT OBJEK: self.total += 1 ===")
    ayu.masuk_lewat_objek()
    bima.masuk_lewat_objek()
    print(f"Total menurut kelas : {Pengunjung.total}")  # [3] tetap 0!
    print(f"Total menurut ayu   : {ayu.total}")
    print(f"Total menurut bima  : {bima.total}")

    print()
    print("=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===")
    citra = Pengunjung("Citra")
    dimas = Pengunjung("Dimas")
    citra.masuk_lewat_kelas()
    dimas.masuk_lewat_kelas()
    print(f"Total menurut kelas : {Pengunjung.total}")
    print(f"Total menurut citra : {citra.total}")  # [4] dibaca dari kelas
    print(f"Total menurut dimas : {dimas.total}")
    print(f"Total menurut ayu   : {ayu.total}")  # [5] ayu membaca "bayangannya" sendiri

    print()
    print("=== ISI MASING-MASING OBJEK ===")
    print(f"ayu   : {vars(ayu)}")  # [6] vars() menampilkan atribut milik objek
    print(f"citra : {vars(citra)}")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== LEWAT OBJEK: self.total += 1 ===
Total menurut kelas : 0
Total menurut ayu   : 1
Total menurut bima  : 1

=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===
Total menurut kelas : 2
Total menurut citra : 2
Total menurut dimas : 2
Total menurut ayu   : 1

=== ISI MASING-MASING OBJEK ===
ayu   : {'nama': 'Ayu', 'total': 1}
citra : {'nama': 'Citra'}
```

Penjelasan:

- **[1]** `self.total += 1` sama artinya dengan `self.total = self.total + 1`. Bagian kanan **membaca** `self.total`. Karena `ayu` belum punya atribut `total`, yang terbaca adalah milik kelas (0). Bagian kiri lalu **mengisi** `self.total`, dan pengisian lewat objek **selalu** menyimpan atribut di objek itu sendiri. Lahirlah atribut objek baru bernama `total` dengan nilai 1.
- **[2]** `Pengunjung.total += 1` mengubah atribut kelas yang sesungguhnya. Inilah cara yang benar.
- **[3]** Setelah Ayu dan Bima masuk dengan cara pertama, total milik kelas **tetap 0**. Penghitung yang sebenarnya tidak pernah bertambah!
- **[4]** `citra` tidak punya atribut `total` sendiri, jadi `citra.total` membaca milik kelas, yaitu 2.
- **[5]** `ayu` sudah telanjur punya atribut `total` sendiri (nilainya 1). Atribut objek itu "membayangi" atribut kelas sehingga `ayu.total` tidak pernah lagi membaca nilai bersama.
- **[6]** Fungsi bawaan `vars()` menampilkan semua atribut **milik objek** sebagai pasangan `'nama': nilai` (bentuk ini disebut *dictionary*, dibahas di Pertemuan 12). Terlihat jelas: objek `ayu` diam-diam punya `total`, sedangkan `citra` tidak.

Gambarannya:

```text
 Sebelum ayu.masuk_lewat_objek()        Sesudahnya

 kelas Pengunjung: total = 0            kelas Pengunjung: total = 0   <- tidak berubah!
 objek ayu       : nama = "Ayu"         objek ayu       : nama = "Ayu"
                                                          total = 1   <- atribut BARU (bayangan)
```

> [!IMPORTANT]
> Aturannya sederhana: **ubah atribut kelas selalu lewat nama kelasnya**, misalnya `Pengunjung.total += 1` atau `Mahasiswa.jumlah += 1`. Membaca lewat objek boleh, tetapi mengisi lewat objek hampir selalu berarti *bug*.

> [!NOTE]
> Java punya perilaku yang **berbeda** untuk kode yang mirip. Di Java, `this.total += 1` tetap mengubah nilai bersama. Program Java untuk skenario yang sama sengaja dibuat ([`Contoh02AksesStatic.java`](../java/contoh/Contoh02AksesStatic.java)), dan hasilnya memang berbeda. Perbandingannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md#1-atribut-kelas-dua-kejutan-yang-berlawanan).

## 3. *Static Method*, *Class Method*, dan Fungsi Biasa

*File*: [`contoh/contoh03_static_dan_class_method.py`](contoh/contoh03_static_dan_class_method.py)

Selain *method* objek, kelas Python bisa punya dua jenis *method* lain yang ditandai dengan **dekorator** (*decorator*). Dekorator adalah tanda `@...` yang ditulis tepat di atas `def` untuk mengubah cara *method* itu bekerja.

```python
class Tanggal:
    """Tanggal sederhana: hari, bulan, dan tahun (semuanya bilangan bulat)."""

    NAMA_BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                  "Agustus", "September", "Oktober", "November", "Desember"]

    def __init__(self, hari, bulan, tahun):
        self.hari = hari
        self.bulan = bulan
        self.tahun = tahun

    def teks(self):  # [1] method objek: butuh data milik objek (self)
        return f"{self.hari} {Tanggal.NAMA_BULAN[self.bulan - 1]} {self.tahun}"

    @staticmethod
    def kabisat(tahun):  # [2] static method: tanpa self, cukup data dari parameter
        """True jika tahun kabisat (bulan Februari punya 29 hari)."""
        return (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0

    @classmethod
    def dari_teks(cls, teks):  # [3] class method: cls berisi kelas Tanggal
        """Konstruktor alternatif: membuat Tanggal dari teks 'hari-bulan-tahun'."""
        hari, bulan, tahun = teks.split("-")
        return cls(int(hari), int(bulan), int(tahun))  # [4] sama dengan Tanggal(...)


def main():
    print("=== METHOD OBJEK (butuh objek) ===")
    proklamasi = Tanggal(17, 8, 1945)
    print(f"Proklamasi kemerdekaan: {proklamasi.teks()}")

    print()
    print("=== STATIC METHOD (tanpa objek) ===")
    for tahun in [2024, 2026, 1900, 2000]:
        if Tanggal.kabisat(tahun):  # [5] dipanggil lewat nama kelas
            print(f"{tahun}: tahun kabisat")
        else:
            print(f"{tahun}: bukan tahun kabisat")

    print()
    print("=== KONSTRUKTOR ALTERNATIF (dari teks) ===")
    sumpah_pemuda = Tanggal.dari_teks("28-10-1928")  # [6] objek dibuat dari teks
    print(f"Sumpah Pemuda: {sumpah_pemuda.teks()}")
    pertempuran = Tanggal.dari_teks("10-11-1945")
    print(f"Pertempuran Surabaya: {pertempuran.teks()}")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== METHOD OBJEK (butuh objek) ===
Proklamasi kemerdekaan: 17 Agustus 1945

=== STATIC METHOD (tanpa objek) ===
2024: tahun kabisat
2026: bukan tahun kabisat
1900: bukan tahun kabisat
2000: tahun kabisat

=== KONSTRUKTOR ALTERNATIF (dari teks) ===
Sumpah Pemuda: 28 Oktober 1928
Pertempuran Surabaya: 10 November 1945
```

Penjelasan:

- **[1]** `teks()` adalah *method* objek biasa. Ia butuh `self` karena harus membaca hari, bulan, dan tahun milik objek tertentu. `NAMA_BULAN` adalah atribut kelas yang berisi daftar nama bulan; huruf kapital semua menandakan bahwa nilainya tidak untuk diubah (konstanta).
- **[2]** `@staticmethod` membuat `kabisat()` menjadi ***static method***: tidak ada `self`, tidak ada `cls`. Ia hanya butuh angka tahun dari parameternya, lalu mengembalikan `True` atau `False`. *Method* ini kita letakkan di kelas `Tanggal` karena isinya masih berhubungan dengan tanggal.
- **[3]** `@classmethod` membuat `dari_teks()` menjadi ***class method***. Parameter pertamanya `cls`, dan Python mengisinya otomatis dengan **kelas** `Tanggal` (bukan objek). Baris `teks.split("-")` memecah `"28-10-1928"` menjadi *list* `["28", "10", "1928"]`, lalu ketiga isinya langsung dimasukkan ke tiga variabel sekaligus.
- **[4]** `cls(...)` sama artinya dengan `Tanggal(...)`: membuat objek baru, menjalankan `__init__`, lalu objeknya dikembalikan. Inilah **konstruktor alternatif**: cara lain membuat objek, kali ini dari teks.
- **[5]** *Static method* dipanggil lewat **nama kelas** tanpa membuat objek apa pun.
- **[6]** *Class method* juga dipanggil lewat nama kelas. Hasilnya objek `Tanggal` yang siap dipakai.

| Jenis | Ditandai | Parameter pertama | Dipanggil dengan | Cocok untuk |
|---|---|---|---|---|
| *Method* objek | (tanpa tanda) | `self` (objeknya) | `objek.method()` | perilaku yang memakai data objek |
| *Static method* | `@staticmethod` | (tidak ada) | `Kelas.method()` | fungsi bantu yang berhubungan dengan kelas |
| *Class method* | `@classmethod` | `cls` (kelasnya) | `Kelas.method()` | konstruktor alternatif, mengolah atribut kelas |

> [!NOTE]
> Mengapa menulis `cls(...)`, bukan langsung `Tanggal(...)`? Di program ini, hasilnya sama. Bedanya baru terasa setelah kamu mengenal pewarisan (*inheritance*) di Pertemuan 07. Jika kelas lain mewarisi `Tanggal` lalu memanggil `dari_teks()`, `cls` berisi kelas pewaris itu sehingga objek yang dibuat pun bertipe kelas pewaris. `Tanggal(...)` akan selalu membuat objek `Tanggal`.

### Fungsi biasa di luar kelas

Python punya pilihan ketiga yang tidak tersedia di Java: **fungsi biasa** yang ditulis di luar kelas mana pun. Studi kasus KedaiKita memakai cara ini untuk `format_rupiah()`. Potongan dari *file* [`studi-kasus/kedaikita.py`](studi-kasus/kedaikita.py) (dibahas lengkap di bagian 9):

```python
def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")
```

Lalu kapan memakai yang mana? Pegangan sederhananya:

| Kebutuhan | Pilihan di Python |
|---|---|
| Butuh data milik objek | *method* objek (`self`) |
| Membuat objek dengan cara lain, atau mengolah atribut kelas | `@classmethod` (`cls`) |
| Tidak butuh objek, tetapi isinya sangat terkait dengan satu kelas | `@staticmethod` |
| Tidak butuh objek dan bersifat umum (dipakai banyak kelas) | fungsi biasa di luar kelas |

`format_rupiah()` dipakai oleh banyak bagian program dan tidak terkait khusus dengan `Menu` maupun `Pelanggan`. Karena itu, fungsi biasa sudah tepat. Di Java, pilihan ini tidak ada sehingga Java memakai **kelas utilitas** `Rupiah`, yaitu kelas yang hanya berisi *method* milik kelas. Alasannya dibahas di [Jembatan](../jembatan-python-java.md#3-format_rupiah-atau-rupiahformat).

> [!TIP]
> **Coba sendiri:** salin `contoh/contoh03_static_dan_class_method.py` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di akhir fungsi `main()`, tambahkan tiga baris berikut (menjorok 4 spasi), lalu ganti `"21-04-2006"` dengan tanggal lahirmu. Simpan, lalu jalankan salinan itu.
>
> ```python
>     lahir = Tanggal.dari_teks("21-04-2006")
>     print(f"Tanggal lahirku: {lahir.teks()}")
>     print(f"Tahun kabisat? {Tanggal.kabisat(lahir.tahun)}")
> ```

<details>
<summary>Lihat hasil untuk contoh tanggal di atas</summary>

```text
Tanggal lahirku: 21 April 2006
Tahun kabisat? False
```

Tahun 2006 tidak habis dibagi 4, jadi bukan tahun kabisat. Perhatikan bahwa `dari_teks()` dan `kabisat()` sama-sama dipanggil lewat nama kelas `Tanggal`, sedangkan `teks()` dipanggil lewat objek `lahir`.

</details>

## 4. Parameter dengan Nilai Bawaan

*File*: [`contoh/contoh04_nilai_bawaan.py`](contoh/contoh04_nilai_bawaan.py)

Parameter boleh diberi **nilai bawaan** dengan menulis `nama=nilai` di daftar parameter. Jika argumennya tidak dikirim, nilai bawaan itulah yang dipakai.

```python
class Laptop:
    """Laptop dengan kapasitas RAM dan penyimpanan (dalam GB)."""

    def __init__(self, merek, ram=8, penyimpanan=512):  # [1] punya nilai bawaan
        self.merek = merek
        self.ram = ram
        self.penyimpanan = penyimpanan

    def tambah_ram(self, tambahan=8):  # [2] method biasa juga boleh punya nilai bawaan
        self.ram = self.ram + tambahan

    def info(self):
        return f"{self.merek}: RAM {self.ram} GB, SSD {self.penyimpanan} GB"


def main():
    print("=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===")
    laptop_ayu = Laptop("Asus")  # [3] ram dan penyimpanan memakai nilai bawaan
    laptop_bima = Laptop("Lenovo", 16)  # [4] penyimpanan memakai nilai bawaan
    laptop_citra = Laptop("Acer", 16, 1024)  # [5] semua argumen dikirim
    laptop_dimas = Laptop("HP", penyimpanan=256)  # [6] argumen bernama (keyword)
    print(laptop_ayu.info())
    print(laptop_bima.info())
    print(laptop_citra.info())
    print(laptop_dimas.info())

    print()
    print("=== MENAMBAH RAM ===")
    laptop_ayu.tambah_ram()  # [7] tambahan memakai nilai bawaan 8
    laptop_bima.tambah_ram(16)
    print(laptop_ayu.info())
    print(laptop_bima.info())


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===
Asus: RAM 8 GB, SSD 512 GB
Lenovo: RAM 16 GB, SSD 512 GB
Acer: RAM 16 GB, SSD 1024 GB
HP: RAM 8 GB, SSD 256 GB

=== MENAMBAH RAM ===
Asus: RAM 16 GB, SSD 512 GB
Lenovo: RAM 32 GB, SSD 512 GB
```

Penjelasan:

- **[1]** `ram=8` dan `penyimpanan=512` adalah nilai bawaan. Akibatnya, konstruktor ini bisa dipanggil dengan 1, 2, atau 3 argumen.
- **[2]** *Method* biasa juga boleh punya nilai bawaan.
- **[3]** Hanya `merek` yang dikirim, jadi `ram` = 8 dan `penyimpanan` = 512.
- **[4]** Argumen dicocokkan **berdasarkan urutan**: `"Lenovo"` masuk ke `merek`, `16` masuk ke `ram`. `penyimpanan` memakai nilai bawaan.
- **[5]** Semua argumen dikirim, jadi tidak ada nilai bawaan yang terpakai.
- **[6]** **Argumen bernama** (*keyword argument*): `penyimpanan=256` langsung menyebut nama parameternya. Kita bisa melompati `ram` (tetap 8) dan hanya mengubah `penyimpanan`.
- **[7]** `tambah_ram()` tanpa argumen memakai nilai bawaan `tambahan=8`.

Pencocokan argumen dengan parameter pada `Laptop("Lenovo", 16)`:

```text
Laptop(        "Lenovo",   16 )
                  |         |
                  v         v
__init__(self,  merek,     ram=8,   penyimpanan=512)
          ^                              ^
          |                              +-- tidak dikirim: memakai nilai bawaan 512
          +-- diisi otomatis oleh Python (objek yang sedang dibuat)
```

Ingat dari Pertemuan 02: kita tidak pernah mengirim argumen untuk `self`. Argumen pertama yang kita tulis (`"Lenovo"`) masuk ke parameter **setelah** `self`, yaitu `merek`.

> [!IMPORTANT]
> Parameter yang punya nilai bawaan harus ditulis **setelah** parameter yang tidak punya nilai bawaan. `def __init__(self, ram=8, merek):` akan ditolak Python dengan `SyntaxError`.

Python **tidak** mengenal *overloading* seperti Java. Jika kamu menulis dua `def __init__` di satu kelas, yang kedua akan **menimpa** yang pertama. Nilai bawaan dan argumen bernama adalah cara Python untuk mendapatkan keluwesan yang sama. Perbandingannya ada di [Jembatan](../jembatan-python-java.md#4-nilai-bawaan-atau-overloading).

### Jebakan: *list* sebagai nilai bawaan

> [!WARNING]
> Jangan memakai ***list*** (atau objek lain yang bisa diubah) sebagai nilai bawaan. Nilai bawaan dibuat **satu kali** saja, yaitu saat Python menjalankan baris `def`, lalu dipakai bersama oleh setiap pemanggilan. Akibatnya, mirip atribut kelas: *list* itu ikut dimiliki semua objek.

Kamu bisa membuktikannya sendiri. Buat *file* baru bernama `coba.py` di folder `pertemuan-03` milikmu, salin kode berikut, simpan, lalu jalankan dengan `python coba.py`.

```python
class Mahasiswa:
    def __init__(self, nama, hobi=[]):  # berbahaya!
        self.nama = nama
        self.hobi = hobi


ayu = Mahasiswa("Ayu")
bima = Mahasiswa("Bima")
ayu.hobi.append("membaca")
print(bima.hobi)  # tercetak ['membaca']: hobi Ayu "bocor" ke Bima
```

Hasilnya `['membaca']`, padahal kita hanya menambah hobi Ayu. Cara yang aman: jadikan `None` sebagai nilai bawaan, lalu buat *list* baru di dalam konstruktor dengan `if hobi is None: hobi = []`.

## 5. Representasi Teks dengan `__str__`

*File*: [`contoh/contoh05_str.py`](contoh/contoh05_str.py)

Tanpa persiapan apa pun, mencetak objek menghasilkan teks yang kurang berguna. Bayangkan kelas `Motor` sederhana yang hanya punya `__init__(self, plat)`, tanpa `__str__`. Jika objeknya dicetak dengan `print(Motor("KT 1234 AB"))`, hasilnya kira-kira seperti ini:

```text
<__main__.Motor object at 0x7f2b6b2decf0>
```

Teks itu berisi nama modul (`__main__`), nama kelas, dan alamat objek di memori. Angka alamatnya akan berbeda di komputermu. Kita ingin teks yang lebih bermakna, dan caranya adalah *method* khusus `__str__`. Begini isi *file* contoh 05:

```python
class Motor:
    """Motor mahasiswa yang terdaftar di parkiran kampus."""

    def __init__(self, plat, merek, warna):
        self.plat = plat
        self.merek = merek
        self.warna = warna

    def __str__(self):  # [1] dipanggil otomatis oleh print(), str(), dan f-string
        return f"{self.plat} - {self.merek} ({self.warna})"  # [2] return, bukan print


def main():
    motor_budi = Motor("KT 1234 AB", "Honda Beat", "merah")
    motor_siti = Motor("KT 5678 CD", "Yamaha NMAX", "hitam")

    print("=== MENCETAK OBJEK LANGSUNG ===")
    print(motor_budi)  # [3] print() memanggil motor_budi.__str__()
    print(motor_siti)

    print()
    print("=== DIPAKAI DI DALAM TEKS LAIN ===")
    print(f"Motor Budi: {motor_budi}")  # [4] f-string juga memanggil __str__
    teks = str(motor_siti)  # [5] str() menghasilkan teksnya untuk disimpan
    print(f"Teks motor Siti terdiri atas {len(teks)} karakter")

    print()
    print("=== SETELAH WARNA DIUBAH ===")
    motor_budi.warna = "biru"
    print(motor_budi)  # [6] teks selalu mengikuti nilai atribut terbaru


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== MENCETAK OBJEK LANGSUNG ===
KT 1234 AB - Honda Beat (merah)
KT 5678 CD - Yamaha NMAX (hitam)

=== DIPAKAI DI DALAM TEKS LAIN ===
Motor Budi: KT 1234 AB - Honda Beat (merah)
Teks motor Siti terdiri atas 32 karakter

=== SETELAH WARNA DIUBAH ===
KT 1234 AB - Honda Beat (biru)
```

Penjelasan:

- **[1]** `__str__` (dua garis bawah di depan dan di belakang, sama seperti `__init__`) adalah *method* khusus. Kita tidak perlu memanggilnya sendiri; Python yang memanggilnya setiap kali objek perlu diubah menjadi teks.
- **[2]** `__str__` wajib **mengembalikan** teks dengan `return`. Ia tidak boleh mencetak sendiri (lihat [Kesalahan 3](#kesalahan-3-__str__-mencetak-bukan-mengembalikan-teks)).
- **[3]** `print(motor_budi)` otomatis memanggil `motor_budi.__str__()`.
- **[4]** *f-string* juga memanggil `__str__` saat objek ditaruh di dalam `{ }`.
- **[5]** `str(objek)` menghasilkan teksnya sehingga bisa disimpan ke variabel dan diolah lagi, misalnya dihitung panjangnya.
- **[6]** Karena `__str__` menyusun teks dari atribut **saat itu juga**, perubahan atribut langsung terlihat saat objek dicetak lagi.

> [!NOTE]
> Python punya *method* khusus lain yang mirip, yaitu `__repr__`. Bedanya: `__str__` ditujukan untuk **pengguna** (teks yang rapi), sedangkan `__repr__` untuk **pemrogram** (teks yang jelas saat mencari *bug*). Salah satu tempat `__repr__` dipakai adalah saat sebuah ***list* berisi objek** dicetak. Tanpa `__repr__`, `print(daftar_motor)` menghasilkan `[<__main__.Motor object at 0x7f6414936cf0>, <__main__.Motor object at 0x7f6414814cd0>]` walaupun `__str__` sudah ada. Untuk sekarang, cukup biasakan membuat `__str__`.

> [!TIP]
> **Coba sendiri:** salin `contoh/contoh05_str.py` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Di dalam `__str__`, ganti baris `return` menjadi `return f"{self.merek} {self.warna} ({self.plat})"`, simpan, lalu jalankan salinan itu. Kamu tidak perlu mengubah satu baris pun di `main()`. Tebak dulu: bagian mana saja dari *output* yang ikut berubah?

<details>
<summary>Lihat hasilnya</summary>

```text
=== MENCETAK OBJEK LANGSUNG ===
Honda Beat merah (KT 1234 AB)
Yamaha NMAX hitam (KT 5678 CD)

=== DIPAKAI DI DALAM TEKS LAIN ===
Motor Budi: Honda Beat merah (KT 1234 AB)
Teks motor Siti terdiri atas 30 karakter

=== SETELAH WARNA DIUBAH ===
Honda Beat biru (KT 1234 AB)
```

Semua tempat yang mencetak motor ikut berubah, termasuk panjang teks motor Siti (kini 30 karakter). Itulah enaknya `__str__`: aturan tampilannya cukup ditulis di **satu** tempat.

</details>

## 6. Referensi, *Aliasing*, dan `None`

*File*: [`contoh/contoh06_referensi.py`](contoh/contoh06_referensi.py)

```python
class Ponsel:
    """Ponsel dengan persentase baterai."""

    def __init__(self, pemilik, baterai):
        self.pemilik = pemilik
        self.baterai = baterai

    def pakai(self, persen):
        self.baterai = self.baterai - persen


def main():
    print("=== DUA VARIABEL, SATU OBJEK ===")
    ponsel_budi = Ponsel("Budi", 80)
    ponsel_dipinjam = ponsel_budi  # [1] TIDAK membuat ponsel baru
    ponsel_dipinjam.pakai(30)  # [2] Siti memakai ponsel yang ia pinjam
    print(f"Baterai dilihat lewat variabel peminjam: {ponsel_dipinjam.baterai}%")
    print(f"Baterai dilihat lewat variabel pemilik : {ponsel_budi.baterai}%")  # [3]
    if ponsel_budi is ponsel_dipinjam:  # [4] apakah objeknya sama?
        print("Keduanya menunjuk objek yang SAMA")
    else:
        print("Keduanya menunjuk objek yang berbeda")

    print()
    print("=== DUA OBJEK DENGAN DATA KEMBAR ===")
    ponsel_a = Ponsel("Rina", 50)
    ponsel_b = Ponsel("Rina", 50)  # [5] objek baru, walaupun datanya kembar
    if ponsel_a is ponsel_b:
        print("Ponsel A dan ponsel B menunjuk objek yang SAMA")
    else:
        print("Ponsel A dan ponsel B menunjuk objek yang berbeda")
    ponsel_a.pakai(10)
    print(f"Baterai ponsel A: {ponsel_a.baterai}%, ponsel B: {ponsel_b.baterai}%")

    print()
    print("=== VARIABEL TANPA OBJEK ===")
    ponsel_dimas = None  # [6] Dimas belum punya ponsel
    if ponsel_dimas is None:  # [7] cara memeriksa None
        print("Dimas belum punya ponsel")
    ponsel_dipinjam = None  # [8] Siti mengembalikan ponsel: "label"-nya dilepas
    print(f"Ponsel Budi tetap ada, baterainya {ponsel_budi.baterai}%")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== DUA VARIABEL, SATU OBJEK ===
Baterai dilihat lewat variabel peminjam: 50%
Baterai dilihat lewat variabel pemilik : 50%
Keduanya menunjuk objek yang SAMA

=== DUA OBJEK DENGAN DATA KEMBAR ===
Ponsel A dan ponsel B menunjuk objek yang berbeda
Baterai ponsel A: 40%, ponsel B: 50%

=== VARIABEL TANPA OBJEK ===
Dimas belum punya ponsel
Ponsel Budi tetap ada, baterainya 50%
```

Penjelasan:

- **[1]** `ponsel_dipinjam = ponsel_budi` **tidak** membuat ponsel baru. Yang disalin hanyalah referensinya sehingga kedua variabel menunjuk objek yang sama.
- **[2]** Siti memakai ponsel lewat variabel `ponsel_dipinjam`, dan baterai **objek itu** berkurang 30.
- **[3]** Dilihat lewat `ponsel_budi`, baterainya juga 50%. Tidak ada yang "menyalin ulang" data; memang hanya ada satu ponsel.
- **[4]** Operator `is` menjawab pertanyaan "apakah dua variabel menunjuk **objek yang sama**?".
- **[5]** Memanggil `Ponsel(...)` dua kali menghasilkan **dua objek berbeda** walaupun datanya kembar. Mengubah ponsel A tidak mengubah ponsel B.
- **[6]** `None` berarti variabel **tidak menunjuk objek apa pun**.
- **[7]** Cara yang dianjurkan untuk memeriksa `None` adalah dengan `is None` (bukan `== None`).
- **[8]** Mengisi `ponsel_dipinjam` dengan `None` hanya **melepas label**. Objek ponselnya tetap ada karena masih ditunjuk oleh `ponsel_budi`.

Keadaan memori setelah baris [2]:

```text
 ponsel_budi -------+
                    v
                [Ponsel] pemilik = "Budi", baterai = 50
                    ^
 ponsel_dipinjam ---+          satu objek, dua nama (aliasing)
```

### `is` atau `==`?

| Operator | Pertanyaan yang dijawab | Contoh |
|---|---|---|
| `a is b` | apakah `a` dan `b` menunjuk **objek yang sama**? | `ponsel_budi is ponsel_dipinjam` |
| `a == b` | apakah **isinya** sama? | `"kopi" == "kopi"` |

Untuk teks dan angka, `==` membandingkan isinya. Untuk objek dari kelas buatan kita sendiri, `==` secara bawaan **masih** membandingkan apakah objeknya sama, persis seperti `is`. Jadi, `ponsel_a == ponsel_b` bernilai `False` walaupun datanya kembar. Cara mengajari Python membandingkan isi objek dibahas di Pertemuan 12.

> [!TIP]
> **Coba sendiri:** tebak dulu *output* kode berikut. Setelah itu, buktikan: salin `contoh/contoh06_referensi.py` ke folder `pertemuan-03` milikmu, buka salinannya, tambahkan kelima baris ini di akhir fungsi `main()` (menjorok 4 spasi), simpan, lalu jalankan salinan itu. Jawabannya ada di baris terakhir *output*.
>
> ```python
>     x = Ponsel("Ayu", 90)
>     y = x
>     z = Ponsel("Ayu", 90)
>     y.pakai(20)
>     print(x.baterai, z.baterai, x is y, x is z)
> ```

<details>
<summary>Lihat jawaban</summary>

`70 90 True False`. `x` dan `y` menunjuk objek yang sama, jadi pemakaian lewat `y` ikut mengurangi baterai `x`. `z` adalah objek lain yang tidak tersentuh.

</details>

## 7. Objek sebagai Parameter

*File*: [`contoh/contoh07_objek_sebagai_parameter.py`](contoh/contoh07_objek_sebagai_parameter.py)

```python
class DompetDigital:
    """Dompet digital (e-wallet) dengan saldo dalam rupiah."""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def saldo_cukup(self, jumlah):  # [1] method boolean: jawabannya ya atau tidak
        return self.saldo >= jumlah

    def transfer(self, tujuan, jumlah):  # [2] tujuan berisi objek DompetDigital lain
        if not self.saldo_cukup(jumlah):
            print(f"Transfer gagal: saldo {self.pemilik} tidak cukup")
            return
        self.saldo = self.saldo - jumlah
        tujuan.saldo = tujuan.saldo + jumlah  # [3] mengubah objek yang dikirim
        print(f"{self.pemilik} transfer Rp{jumlah} ke {tujuan.pemilik}")


def tambah_bonus_angka(saldo):  # [4] menerima ANGKA
    saldo = saldo + 5000  # hanya mengubah variabel milik fungsi ini
    print(f"  (di dalam: Rp{saldo})")


def tambah_bonus_dompet(dompet):  # [5] menerima OBJEK
    dompet.saldo = dompet.saldo + 5000  # mengubah objek milik pemanggil
    print(f"  (di dalam: Rp{dompet.saldo})")


def main():
    dompet_budi = DompetDigital("Budi", 100000)
    dompet_siti = DompetDigital("Siti", 20000)

    print("=== TRANSFER ANTARDOMPET ===")
    dompet_budi.transfer(dompet_siti, 30000)  # [6] objek dompet_siti dikirim
    dompet_siti.transfer(dompet_budi, 75000)
    print(f"Saldo Budi: Rp{dompet_budi.saldo}")
    print(f"Saldo Siti: Rp{dompet_siti.saldo}")

    print()
    print("=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===")
    saldo_tunai = 10000
    tambah_bonus_angka(saldo_tunai)
    print(f"Saldo tunai sesudahnya      : Rp{saldo_tunai}")  # [7] tidak berubah
    tambah_bonus_dompet(dompet_siti)
    print(f"Saldo dompet Siti sesudahnya: Rp{dompet_siti.saldo}")  # [8] berubah


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== TRANSFER ANTARDOMPET ===
Budi transfer Rp30000 ke Siti
Transfer gagal: saldo Siti tidak cukup
Saldo Budi: Rp70000
Saldo Siti: Rp50000

=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===
  (di dalam: Rp15000)
Saldo tunai sesudahnya      : Rp10000
  (di dalam: Rp55000)
Saldo dompet Siti sesudahnya: Rp55000
```

Penjelasan:

- **[1]** `saldo_cukup()` adalah ***method boolean***. Namanya dibaca seperti pertanyaan ("saldonya cukup?"), dan hasilnya langsung dipakai di `if`.
- **[2]** Parameter `tujuan` menerima objek `DompetDigital` lain. Di Python, tipe parameter tidak wajib ditulis (di pertemuan ini memang belum kita tulis), jadi nama parameter yang jelas sangat membantu.
- **[3]** *Method* mengubah saldo **objek yang dikirim**. Setelah *method* selesai, perubahan itu tetap ada karena `tujuan` dan `dompet_siti` menunjuk objek yang sama.
- **[4]** Fungsi ini menerima **angka**. Di dalamnya, `saldo` diubah menjadi 15000, tetapi itu hanya variabel milik fungsi.
- **[5]** Fungsi ini menerima **objek**, lalu mengubah atribut objek itu.
- **[6]** Objek `dompet_siti` dikirim sebagai argumen, persis seperti mengirim angka atau teks.
- **[7]** `saldo_tunai` milik `main()` tetap 10000. Mengubah variabel parameter tidak memengaruhi pemanggil.
- **[8]** Saldo dompet Siti benar-benar bertambah 5000 karena yang diubah adalah **isi objeknya**.

```text
tambah_bonus_angka(saldo_tunai)      ->  fungsi menerima angka 10000 (secara sederhana: salinannya)
tambah_bonus_dompet(dompet_siti)     ->  fungsi menerima referensi ke objek yang SAMA
```

> [!NOTE]
> Secara teknis, Python selalu mengirim referensi, termasuk untuk angka. Namun, angka tidak bisa diubah isinya. Baris `saldo = saldo + 5000` membuat angka **baru**, lalu mengarahkan variabel `saldo` milik fungsi ke angka baru itu. Variabel `saldo_tunai` milik `main()` tetap menunjuk angka lama sehingga hasilnya sama seperti menyalin angka.

> [!TIP]
> **Coba sendiri:** salin `contoh/contoh07_objek_sebagai_parameter.py` ke folder `pertemuan-03` milikmu, lalu buka salinannya. Tambahkan fungsi berikut di bawah fungsi `tambah_bonus_dompet()` (tanpa menjorok, sejajar dengan `def` lainnya). Lalu, di akhir `main()`, tambahkan dua baris `ganti_dompet(dompet_siti)` dan `print(dompet_siti.saldo)`. Simpan, lalu jalankan salinan itu. Tebak dulu: apakah saldonya menjadi 0?
>
> ```python
> def ganti_dompet(dompet):
>     dompet = DompetDigital("Orang Lain", 0)
> ```

<details>
<summary>Lihat jawaban</summary>

Tidak. Saldo Siti tetap 55000. Baris `dompet = DompetDigital(...)` hanya mengarahkan **variabel parameter** `dompet` ke objek baru. Variabel `dompet_siti` milik `main()` tetap menunjuk objek lama. *Method* bisa **mengubah isi** objek kiriman, tetapi tidak bisa **mengganti** objek yang dipegang variabel pemanggil.

</details>

## 8. Objek sebagai Nilai Kembalian

*File*: [`contoh/contoh08_objek_sebagai_kembalian.py`](contoh/contoh08_objek_sebagai_kembalian.py)

```python
class Durasi:
    """Lama waktu dalam jam dan menit (bilangan bulat)."""

    def __init__(self, jam, menit):
        total = jam * 60 + menit  # [1] dirapikan: 1 jam 75 menit -> 2 jam 15 menit
        self.jam = total // 60
        self.menit = total % 60

    def total_menit(self):
        return self.jam * 60 + self.menit

    def tambah(self, lain):  # [2] menerima objek Durasi lain ...
        return Durasi(0, self.total_menit() + lain.total_menit())  # [3] ... objek BARU

    def lebih_lama_dari(self, lain):  # [4] method boolean dengan parameter objek
        return self.total_menit() > lain.total_menit()

    def __str__(self):
        return f"{self.jam} jam {self.menit} menit"


def main():
    kuliah = Durasi(2, 30)
    praktikum = Durasi(1, 40)

    print("=== MENJUMLAHKAN DUA DURASI ===")
    total = kuliah.tambah(praktikum)  # [5] hasilnya objek baru
    print(f"Kuliah    : {kuliah}")
    print(f"Praktikum : {praktikum}")
    print(f"Total     : {total}")
    print(f"Durasi aneh 1 jam 75 menit dirapikan menjadi {Durasi(1, 75)}")

    print()
    print("=== MEMANGGIL SECARA BERANTAI ===")
    istirahat = Durasi(0, 45)
    sehari = kuliah.tambah(istirahat).tambah(praktikum)  # [6] hasil dipakai lagi
    print(f"Kuliah + istirahat + praktikum = {sehari}")
    print(f"Kuliah tetap {kuliah}")  # [7] objek lama tidak berubah

    print()
    print("=== MEMBANDINGKAN DUA DURASI ===")
    batas = Durasi(4, 30)
    if total.lebih_lama_dari(batas):
        print(f"{total} lebih lama dari {batas}")
    else:
        print(f"{total} tidak lebih lama dari {batas}")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== MENJUMLAHKAN DUA DURASI ===
Kuliah    : 2 jam 30 menit
Praktikum : 1 jam 40 menit
Total     : 4 jam 10 menit
Durasi aneh 1 jam 75 menit dirapikan menjadi 2 jam 15 menit

=== MEMANGGIL SECARA BERANTAI ===
Kuliah + istirahat + praktikum = 4 jam 55 menit
Kuliah tetap 2 jam 30 menit

=== MEMBANDINGKAN DUA DURASI ===
4 jam 10 menit tidak lebih lama dari 4 jam 30 menit
```

Penjelasan:

- **[1]** Konstruktor tidak sekadar menyimpan parameter. Ia mengubah semuanya menjadi total menit, lalu membaginya lagi menjadi jam dan menit (`//` mengambil hasil bagi bulat, `%` mengambil sisanya). Jadi, `Durasi(1, 75)` tersimpan rapi sebagai 2 jam 15 menit.
- **[2]** `tambah()` menerima objek `Durasi` lain sebagai parameter.
- **[3]** `tambah()` **tidak mengubah** `self` maupun `lain`. Ia membuat objek `Durasi` **baru**, lalu mengembalikannya dengan `return`. Konstruktor di [1] yang merapikan hasilnya.
- **[4]** `lebih_lama_dari()` menggabungkan dua hal: menerima objek sebagai parameter dan mengembalikan *boolean*.
- **[5]** Hasil `tambah()` disimpan ke variabel `total`, seperti menyimpan hasil `2 + 3`.
- **[6]** Karena `tambah()` mengembalikan objek `Durasi`, hasilnya bisa langsung dipanggil `tambah()` lagi. Ini disebut pemanggilan **berantai**.
- **[7]** Objek `kuliah` tetap 2 jam 30 menit. Penjumlahan tidak merusak objek asalnya.

> [!IMPORTANT]
> Ada dua gaya *method* yang sama-sama sah: *method* yang **mengubah objeknya sendiri** (misalnya `tambah_ram()` atau `pakai()`), dan *method* yang **mengembalikan objek baru** (misalnya `tambah()` di sini). Pilih salah satu dengan sadar, lalu beri nama yang jujur agar pembaca tahu apakah objek asal akan berubah.

## 9. Studi Kasus KedaiKita

*File*: [`studi-kasus/kedaikita.py`](studi-kasus/kedaikita.py)

Saatnya mengembangkan KedaiKita dari Pertemuan 02. Rancangannya sudah kita bahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-menu-yang-lebih-lengkap).

**Apa yang berubah dibanding Pertemuan 02?**

- Fungsi baru `format_rupiah()` menampilkan uang dengan titik ribuan: `Rp18.000`, bukan lagi `Rp18000`.
- `Menu` kini punya lima atribut objek: `kode`, `nama`, `harga`, `kategori`, dan `stok`. Parameter `stok` punya nilai bawaan 0.
- Atribut kelas `jumlah_menu` menghitung banyaknya menu yang sudah dibuat.
- `tampilkan_info()` dihapus dan diganti `__str__` sehingga menu cukup dicetak dengan `print(menu)`.
- *Method* baru: `harga_setelah_diskon(persen)` dan `stok_cukup(jumlah)`. *Method* `hitung_total(jumlah)` tetap ada.
- Kelas baru `Pelanggan` dengan atribut `nama`, `no_hp`, dan `poin` (selalu mulai dari 0), serta *method* `tambah_poin()`.

Perubahan terbesar ada pada cara menampilkan menu. Bandingkan potongan kode kelas `Menu` versi Pertemuan 02 dan versi sekarang (hanya untuk dibaca, bukan untuk dijalankan):

```python
# Pertemuan 02: method yang MENCETAK
def tampilkan_info(self):
    print(f"{self.nama} - Rp{self.harga}")

# Pertemuan 03: method yang MENGEMBALIKAN teks
def __str__(self):
    return (f"[{self.kode}] {self.nama} ({self.kategori}) - "
            f"{format_rupiah(self.harga)} | stok {self.stok}")
```

Isi lengkap *file* `studi-kasus/kedaikita.py` (tanpa komentar pembuka di baris paling atas):

```python
def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Cetak biru untuk setiap menu di KedaiKita."""

    jumlah_menu = 0  # atribut KELAS: satu nilai untuk semua objek Menu

    def __init__(self, kode, nama, harga, kategori, stok=0):
        self.kode = kode  # atribut OBJEK: tiap objek punya nilainya sendiri
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.stok = stok
        Menu.jumlah_menu += 1  # setiap ada objek baru, penghitung bertambah

    def __str__(self):
        """Teks yang muncul saat objek dicetak dengan print()."""
        return (f"[{self.kode}] {self.nama} ({self.kategori}) - "
                f"{format_rupiah(self.harga)} | stok {self.stok}")

    def hitung_total(self, jumlah):
        """Total harga untuk sejumlah porsi."""
        return self.harga * jumlah

    def harga_setelah_diskon(self, persen):
        """Harga setelah dipotong diskon sekian persen."""
        potongan = self.harga * persen // 100
        return self.harga - potongan

    def stok_cukup(self, jumlah):
        """True jika stok masih cukup untuk sejumlah porsi."""
        return self.stok >= jumlah


class Pelanggan:
    """Data pelanggan KedaiKita beserta poin belanjanya."""

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.poin = 0  # setiap pelanggan baru mulai dari 0 poin

    def __str__(self):
        return f"{self.nama} ({self.no_hp}) - {self.poin} poin"

    def tambah_poin(self, jumlah):
        self.poin += jumlah


def main():
    kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
    es_teh = Menu("M02", "Es Teh Manis", 8000, "Minuman", 30)
    nasi_goreng = Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15)
    mie_goreng = Menu("M04", "Mie Goreng Jawa", 23000, "Makanan")  # stok bawaan 0

    print("=== MENU KEDAIKITA ===")
    print(kopi)
    print(es_teh)
    print(nasi_goreng)
    print(mie_goreng)
    print(f"Jumlah menu terdaftar: {Menu.jumlah_menu}")

    print()
    print("=== CEK STOK ===")
    if kopi.stok_cukup(2):
        print(f"Pesan 2 {kopi.nama}? Bisa")
    else:
        print(f"Pesan 2 {kopi.nama}? Stok tidak cukup")
    if mie_goreng.stok_cukup(1):
        print(f"Pesan 1 {mie_goreng.nama}? Bisa")
    else:
        print(f"Pesan 1 {mie_goreng.nama}? Stok tidak cukup")

    print()
    print("=== PROMO HARI INI: DISKON 10% ===")
    for menu in [kopi, nasi_goreng]:
        harga_baru = menu.harga_setelah_diskon(10)
        print(f"{menu.nama}: {format_rupiah(menu.harga)} -> "
              f"{format_rupiah(harga_baru)}")

    print()
    print("=== PELANGGAN ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    print(budi)
    belanja = kopi.hitung_total(2) + es_teh.hitung_total(1)
    poin_baru = belanja // 10000  # 1 poin untuk setiap Rp10.000
    budi.tambah_poin(poin_baru)
    print(f"Budi belanja {format_rupiah(belanja)}, dapat {poin_baru} poin")
    print(budi)


if __name__ == "__main__":
    main()
```

**Cara menjalankan.** Di VS Code, buka *file* `studi-kasus/kedaikita.py`, lalu klik tombol ▷ (**Run Python File**). Lewat terminal, ketik perintah berikut dari folder utama materi (di macOS/Linux, ganti `python` dengan `python3`):

```bash
cd Pertemuan-03-Atribut-dan-Method/python/studi-kasus
python kedaikita.py
```

Hasilnya harus sama persis dengan blok berikut.

***Output:***

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 0
Jumlah menu terdaftar: 4

=== CEK STOK ===
Pesan 2 Kopi Susu Gula Aren? Bisa
Pesan 1 Mie Goreng Jawa? Stok tidak cukup

=== PROMO HARI INI: DISKON 10% ===
Kopi Susu Gula Aren: Rp18.000 -> Rp16.200
Nasi Goreng Kampung: Rp25.000 -> Rp22.500

=== PELANGGAN ===
Budi Santoso (081234567890) - 0 poin
Budi belanja Rp44.000, dapat 4 poin
Budi Santoso (081234567890) - 4 poin
```

Penjelasan per bagian:

- **`format_rupiah()`** adalah fungsi biasa di luar kelas. Di dalam *f-string*, bagian setelah titik dua pada `{angka:,}` adalah aturan format. Tanda `,` berarti "sisipkan pemisah ribuan", dan Python **selalu** memakai koma untuk itu (`18,000`), apa pun pengaturan bahasa komputermu. Setelah itu, `.replace(",", ".")` mengganti setiap koma dengan titik sesuai kebiasaan Indonesia: `Rp18.000`.
- **`jumlah_menu = 0`** ditulis di badan kelas, jadi ia atribut kelas. Konstruktor menambahnya lewat nama kelas (`Menu.jumlah_menu += 1`), sesuai aturan di bagian 2. Karena empat menu dibuat, hasilnya 4.
- **`stok=0`** adalah nilai bawaan. Mie Goreng Jawa dibuat dengan empat argumen sehingga stoknya 0.
- **`__str__`** memanggil `format_rupiah()`, jadi fungsi biasa pun boleh dipakai dari dalam *method*.
- **`harga_setelah_diskon(10)`** menghitung potongan dengan bilangan bulat: `18000 * 10 // 100` = 1800 sehingga harga promonya 16200. Uang tidak pernah memakai bilangan desimal.
- **`stok_cukup(jumlah)`** mengembalikan `True`/`False` dan langsung dipakai di `if`. Mie Goreng Jawa stoknya 0, jadi jawabannya "Stok tidak cukup".
- **`for menu in [kopi, nasi_goreng]`** menunjukkan *aliasing* yang bermanfaat: variabel `menu` bergantian menunjuk objek `kopi` dan `nasi_goreng` yang sama, bukan salinannya.
- **`Pelanggan`** selalu mulai dengan `poin = 0`. Nilai awal ini tidak berasal dari parameter. Belanja Budi Rp44.000 menghasilkan `44000 // 10000` = 4 poin, lalu `tambah_poin(4)` mengubah atribut objek `budi`.

Selamat! KedaiKita kini punya menu yang lengkap, penghitung menu, harga promo, dan pelanggan dengan poin belanja. Semua itu dibangun dengan konsep yang baru kamu pelajari hari ini.

> [!TIP]
> **Coba sendiri:** tambahkan menu kelima, M05 Pisang Goreng Keju seharga Rp15.000 (kategori Makanan), **tanpa** menyebut stok. Salin `studi-kasus/kedaikita.py` ke folder `pertemuan-03` milikmu, buka salinannya, lalu di dalam `main()`:
>
> 1. Tepat di bawah baris `mie_goreng = ...`, tambahkan `pisang = Menu("M05", "Pisang Goreng Keju", 15000, "Makanan")`.
> 2. Tepat di bawah baris `print(mie_goreng)`, tambahkan `print(pisang)`.
>
> Simpan, jalankan salinan itu, lalu perhatikan bagian `=== MENU KEDAIKITA ===`. Apa yang tercetak?

<details>
<summary>Lihat jawaban</summary>

Bagian awal *output*-nya menjadi:

```text
=== MENU KEDAIKITA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 0
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 0
Jumlah menu terdaftar: 5
```

Stoknya 0 karena memakai nilai bawaan, dan penghitung bertambah karena konstruktor dijalankan sekali lagi. *File* studi kasus di folder materi tetap utuh karena yang kamu ubah hanya salinannya.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Seperti biasa, pesan *error* Python dibaca **dari bawah ke atas**. Baris paling bawah menyebutkan jenis *error* dan penyebabnya, sedangkan baris di atasnya menunjukkan lokasinya.

Potongan kode di bagian ini **sengaja dibuat salah** dan tidak ada di folder `contoh/`. Pesan *error*-nya diambil dari program kecil bernama `coba.py`. Jika ingin mencobanya sendiri, kerjakan di folder `pertemuan-03` milikmu (lihat [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)): salin *file* contoh yang disebut di setiap kesalahan, ubah salinannya sesuai potongan, lalu jalankan. Nama *file* dan nomor baris di pesanmu bisa berbeda, tetapi jenis dan isi *error*-nya sama.

### Kesalahan 1: Memanggil *method* objek lewat nama kelas

Memakai kelas `Tanggal` dari contoh 03:

```python
print(Tanggal.teks())
```

```text
Traceback (most recent call last):
  File "coba.py", line 11, in <module>
    print(Tanggal.teks())
TypeError: Tanggal.teks() missing 1 required positional argument: 'self'
```

**Artinya:** `teks()` adalah *method* objek, jadi ia butuh `self`. Saat dipanggil lewat nama kelas, tidak ada objek yang bisa dijadikan `self`. **Perbaikan:** buat objeknya dulu, misalnya `Tanggal(17, 8, 1945).teks()`. Jika *method* itu memang tidak butuh data objek, jadikan *static method*.

### Kesalahan 2: Lupa menulis `@staticmethod`

```python
class Tanggal:
    # ... (konstruktor sama seperti contoh 03)

    def kabisat(tahun):  # lupa @staticmethod
        return (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0


hari_ini = Tanggal(14, 10, 2026)
print(hari_ini.kabisat(2026))
```

```text
Traceback (most recent call last):
  File "coba.py", line 13, in <module>
    print(hari_ini.kabisat(2026))
TypeError: Tanggal.kabisat() takes 1 positional argument but 2 were given
```

**Artinya:** tanpa `@staticmethod`, Python menganggap `kabisat` sebagai *method* objek dan mengirim `hari_ini` sebagai argumen pertama. Ditambah `2026`, jumlahnya menjadi 2, padahal *method* hanya menerima 1. Anehnya, `Tanggal.kabisat(2024)` (lewat nama kelas) tetap berjalan sehingga kesalahan ini sering lolos. **Perbaikan:** tambahkan `@staticmethod` di atas `def kabisat`.

### Kesalahan 3: `__str__` mencetak, bukan mengembalikan teks

Potongan dari kelas `Motor` yang `__str__`-nya ditulis keliru, lalu objeknya dicetak dengan `print(motor)`:

```python
    def __str__(self):
        print(f"Motor {self.plat}")  # salah: mencetak, tidak ada return
```

```text
Motor KT 1234 AB
Traceback (most recent call last):
  File "coba.py", line 10, in <module>
    print(motor)
TypeError: __str__ returned non-string (type NoneType)
```

**Artinya:** `print` di dalam `__str__` sempat berjalan (baris pertama *output*), tetapi `__str__` tidak mengembalikan apa pun sehingga hasilnya `None`. Python mewajibkan `__str__` mengembalikan teks (*string*). **Perbaikan:** `return f"Motor {self.plat}"`.

### Kesalahan 4: Salah menulis nama `__str__`

Potongan dari kelas `Motor` yang sama, tetapi nama *method*-nya salah ketik:

```python
    def _str_(self):  # salah: garis bawahnya hanya satu
        return f"Motor {self.plat}"
```

Tidak ada *error*, tetapi hasilnya:

```text
<__main__.Motor object at 0x7ffabf2decf0>
```

**Artinya:** bagi Python, `_str_` hanyalah *method* biasa yang kebetulan bernama aneh, bukan *method* khusus. Kesalahan yang sama terjadi pada `__str` atau `__Str__`. **Perbaikan:** tulis tepat `__str__`, dengan **dua** garis bawah di depan dan di belakang.

### Kesalahan 5: Memanggil *method* lewat variabel berisi `None`

Memakai kelas `Ponsel` dari contoh 06:

```python
ponsel_dimas = None
ponsel_dimas.pakai(10)
```

```text
Traceback (most recent call last):
  File "coba.py", line 11, in <module>
    ponsel_dimas.pakai(10)
AttributeError: 'NoneType' object has no attribute 'pakai'
```

**Artinya:** `ponsel_dimas` tidak menunjuk objek `Ponsel` apa pun. `NoneType` adalah "jenis" dari nilai `None`, dan tentu saja ia tidak punya *method* `pakai`. **Perbaikan:** pastikan variabel sudah berisi objek, atau periksa dulu dengan `if ponsel_dimas is not None:`.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Python. Mulai Python 3.11, *traceback* juga bisa menampilkan tanda seperti `^^^^` atau `~~~~^^^^` di bawah bagian kode yang bermasalah. Fokuslah pada **jenis *error*** (misalnya `TypeError`, `AttributeError`) dan kata-kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Atribut kelas | ditulis di badan kelas | `jumlah_menu = 0` |
| Mengubah atribut kelas | `NamaKelas.atribut = ...` | `Menu.jumlah_menu += 1` |
| *Static method* | `@staticmethod` + `def f(...)` | `Tanggal.kabisat(2024)` |
| *Class method* | `@classmethod` + `def f(cls, ...)` | `Tanggal.dari_teks("17-08-1945")` |
| Membuat objek di *class method* | `cls(...)` | `return cls(hari, bulan, tahun)` |
| Nilai bawaan | `parameter=nilai` | `def __init__(self, ..., stok=0):` |
| Argumen bernama | `fungsi(nama=nilai)` | `Laptop("HP", penyimpanan=256)` |
| Representasi teks | `def __str__(self): return ...` | `print(kopi)` |
| *Method boolean* | `return` ekspresi perbandingan | `return self.stok >= jumlah` |
| Objek yang sama? | `a is b` | `ponsel_budi is ponsel_dipinjam` |
| Tidak menunjuk objek | `None` | `if ponsel is None:` |
| Objek sebagai parameter | `def f(self, lain):` | `dompet_budi.transfer(dompet_siti, 30000)` |
| Mengembalikan objek baru | `return NamaKelas(...)` | `return Durasi(0, total)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
