# 🐍 Praktik Python Pertemuan 14: *Design Pattern* Dasar

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 14](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [*Singleton* dengan `get_instance()`](#1-singleton-dengan-get_instance)
2. [Variasi *Singleton* ala Python: Modul dan `__new__`](#2-variasi-singleton-ala-python-modul-dan-__new__)
3. [Sisi Gelap *Singleton*: *State* Global](#3-sisi-gelap-singleton-state-global)
4. [*Simple Factory*: Membuat Objek dari Teks](#4-simple-factory-membuat-objek-dari-teks)
5. [*Factory Method*: *Subclass* yang Memilih](#5-factory-method-subclass-yang-memilih)
6. [*Strategy*: Menukar Cara Menghitung](#6-strategy-menukar-cara-menghitung)
7. [*Observer*: Berlangganan Kabar](#7-observer-berlangganan-kabar)
8. [Studi Kasus KedaiKita](#8-studi-kasus-kedaikita)
9. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#9-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 7 contoh, satu atau dua per pola
├── studi-kasus/     <- KedaiKita versi Pertemuan 14 (18 file .py)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Semua contoh memakai materi yang sudah kamu kenal: atribut kelas, `@classmethod`, dan `@staticmethod` (Pertemuan 03), atribut bergaris bawah dan `@property` (Pertemuan 04), kelas abstrak `ABC` (Pertemuan 10), serta *list* dan *dict* (Pertemuan 12). Yang baru hanyalah **cara menyusunnya**.

### Cara Menjalankan Contoh

Setiap *file* di folder `contoh/` dan `solusi/` adalah program satu *file*. Pilih salah satu cara berikut. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-14-Design-Pattern/python`. Di panel **Explorer**, buka folder `contoh`, klik *file* yang ingin dicoba (misalnya `contoh01_singleton_konfigurasi.py`), lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-14-Design-Pattern/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_singleton_konfigurasi.py
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di bagian 1. Untuk contoh lain, ganti nama *file*-nya, misalnya `python contoh02_variasi_singleton.py`. *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

### Cara Menjalankan Studi Kasus

Studi kasus terdiri atas 18 *file* yang saling memakai lewat `import`. Yang dijalankan selalu `main.py`. *File* lain, seperti `pengaturan.py` atau `pesanan.py`, hanya berisi kelas sehingga tidak menampilkan apa-apa jika dijalankan sendiri.

- **Cara 1:** di jendela VS Code yang sama (folder `python` pertemuan ini), buka `studi-kasus/main.py`, lalu klik tombol ▷.
- **Cara 2:** masuk dulu ke folder `studi-kasus`, lalu jalankan `main.py`.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi | `cd Pertemuan-14-Design-Pattern/python/studi-kasus` |
| folder `python` pertemuan ini | `cd studi-kasus` |

Setelah itu jalankan:

```bash
python main.py
```

Hasilnya berupa empat bagian, satu bagian per pola, lalu diakhiri sebuah struk. *Output* setiap bagian dibahas di [bagian 8](#8-studi-kasus-kedaikita).

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.

### Tempat Menyimpan Kodemu Sendiri

Folder materi ibarat buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Semua percobaan di halaman ini ("Coba sendiri" dan Kesalahan Umum) kamu kerjakan di folder milikmu sendiri **di luar** folder materi, sesuai [aturan emas di halaman Git dan GitHub](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri):

```text
Documents/
├── PBO2026/                                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/
    └── pertemuan-14/                         <- kodemu untuk pertemuan ini
        ├── contoh01_singleton_konfigurasi.py <- salinan untuk dicoba
        └── studi-kasus/                      <- salinan SELURUH folder studi-kasus
```

Salin dulu *file* contoh yang ingin kamu ubah ke folder `pertemuan-14` (lewat File Explorer di Windows atau Finder di macOS). Untuk studi kasus, salin **seluruh folder** `studi-kasus` karena `main.py` membutuhkan 17 *file* lainnya. Lalu buka folder `pertemuan-14` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**). Terminal VS Code di jendela itu langsung berada di folder `pertemuan-14`, jadi salinanmu bisa dijalankan dengan ▷ atau dengan `python nama_file.py`.

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Blok kode sesudahnya adalah **potongan** penting dari *file* itu, disalin persis. Bagian yang dilewati diceritakan dengan kalimat di antara potongan. Untuk mencoba, jalankan *file* lengkapnya; jangan hanya mengetik ulang potongannya.
- Tanda `# [1]`, `# [2]`, dan seterusnya di komentar kode dijelaskan satu per satu di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* lengkapnya dijalankan. Di bagian 8, setiap blok ***Output:*** hanya memuat bagian *output* `main.py` yang sedang dibahas.
- Kode di "Coba sendiri" dan di bagian Kesalahan Umum adalah percobaan. Kerjakan di folder milikmu, bukan di folder materi.

## 1. *Singleton* dengan `get_instance()`

*File*: [`contoh/contoh01_singleton_konfigurasi.py`](contoh/contoh01_singleton_konfigurasi.py)

Kita mulai dari *Singleton* paling klasik: kelas `Konfigurasi` yang menyimpan bahasa dan tema aplikasi. Berikut potongan *file*-nya, bagian kelasnya:

```python
class Konfigurasi:
    """Pengaturan aplikasi yang harus SAMA di semua bagian program."""

    _instance = None  # [1] atribut kelas: tempat satu-satunya objek

    def __init__(self):
        if Konfigurasi._instance is not None:  # [2] penjaga objek kedua
            raise RuntimeError("Konfigurasi adalah Singleton. "
                               "Gunakan Konfigurasi.get_instance()")
        print("  (objek Konfigurasi dibuat)")
        self._data = {"bahasa": "Indonesia", "tema": "terang"}

    @classmethod
    def get_instance(cls) -> "Konfigurasi":  # [3] satu-satunya pintu masuk
        if cls._instance is None:  # [4] dibuat hanya saat pertama diminta
            cls._instance = cls()
        return cls._instance
```

Di bawahnya ada *method* `ambil(kunci)` dan `ubah(kunci, nilai)` untuk membaca dan mengubah `_data`. Potongan berikutnya berisi fungsi-fungsi "halaman" dan awal `main()`:

```python
def halaman_beranda():
    konfigurasi = Konfigurasi.get_instance()  # [5] tanpa parameter tambahan
    print(f"Beranda: bahasa {konfigurasi.ambil('bahasa')}, "
          f"tema {konfigurasi.ambil('tema')}")


def halaman_pengaturan():
    print("Pengguna memilih tema gelap di halaman Pengaturan")
    Konfigurasi.get_instance().ubah("tema", "gelap")  # [6]


def main():
    print("=== MEMINTA KONFIGURASI DUA KALI ===")
    print("Permintaan pertama:")
    a = Konfigurasi.get_instance()
    print("Permintaan kedua:")
    b = Konfigurasi.get_instance()
    sama = "ya" if a is b else "tidak"  # [7] is: objek yang sama?
    print(f"a dan b objek yang sama? {sama}")
```

`halaman_profil()` ditulis sama seperti `halaman_beranda()`. Sisa `main()` memanggil Beranda dan Profil, lalu Pengaturan, lalu Beranda dan Profil sekali lagi.

***Output:***

```text
=== MEMINTA KONFIGURASI DUA KALI ===
Permintaan pertama:
  (objek Konfigurasi dibuat)
Permintaan kedua:
a dan b objek yang sama? ya

=== SEMUA HALAMAN MEMBACA PENGATURAN YANG SAMA ===
Beranda: bahasa Indonesia, tema terang
Profil : bahasa Indonesia, tema terang

=== DIUBAH DI SATU TEMPAT, TERLIHAT DI SEMUA TEMPAT ===
Pengguna memilih tema gelap di halaman Pengaturan
Beranda: bahasa Indonesia, tema gelap
Profil : bahasa Indonesia, tema gelap
```

Penjelasan:

- **[1]** `_instance` adalah **atribut kelas** (Pertemuan 03): hanya ada satu untuk seluruh kelas, bukan satu per objek. Awalnya `None`, artinya objek belum pernah dibuat.
- **[2]** Penjaga. Jika objek resmi sudah ada, pembuatan objek baru lewat `Konfigurasi()` ditolak dengan `RuntimeError`.
- **[3]** `@classmethod` (Pertemuan 03) membuat *method* ini milik kelas. Kita memanggilnya lewat nama kelas, `Konfigurasi.get_instance()`, tanpa perlu punya objek lebih dulu. Parameter `cls` berisi kelas `Konfigurasi` itu sendiri. Tipe kembaliannya ditulis sebagai teks `"Konfigurasi"` karena kelasnya belum selesai didefinisikan saat baris itu dibaca.
- **[4]** Inilah sifat ***lazy***: objek baru dibuat saat **pertama kali** diminta. Pesan `(objek Konfigurasi dibuat)` hanya muncul sekali walaupun `get_instance()` dipanggil berkali-kali.
- **[5]** Setiap halaman mengambil objek sendiri lewat `get_instance()`, tanpa perlu menerimanya sebagai parameter. Praktis, tetapi ingat sisi gelapnya di bagian 3.
- **[6]** Halaman Pengaturan mengubah tema. Karena objeknya satu, perubahan itu langsung terlihat di Beranda dan Profil.
- **[7]** `is` memeriksa apakah dua variabel menunjuk ke **objek yang sama** (Pertemuan 02). Hasilnya `ya`.

> [!WARNING]
> Penjaga di `__init__` punya celah: ia hanya bekerja **setelah** objek resmi ada. Jika seseorang memanggil `Konfigurasi()` sebelum `get_instance()` pernah dipanggil, objek "liar" tetap tercipta tanpa *error*, dan `get_instance()` nanti membuat objek kedua (dibahas lagi di Kesalahan 1). Python memang tidak punya konstruktor privat sungguhan, sama seperti tidak punya atribut privat sungguhan (Pertemuan 04). Kesepakatannya: **selalu** ambil objek lewat `get_instance()`.

> [!TIP]
> **Coba sendiri:** salin `contoh01_singleton_konfigurasi.py` ke folder `pertemuan-14` milikmu, lalu buka salinannya. Di `main()`, ganti baris `b = Konfigurasi.get_instance()` menjadi `b = Konfigurasi()`. Simpan, tebak dulu apa yang akan terjadi, lalu jalankan.

<details>
<summary>Lihat jawaban</summary>

Program sempat mencetak empat baris pertama (sampai `Permintaan kedua:`), lalu berhenti dengan *traceback* yang baris terakhirnya:

```text
RuntimeError: Konfigurasi adalah Singleton. Gunakan Konfigurasi.get_instance()
```

Saat baris `b = Konfigurasi()` dijalankan, `_instance` sudah berisi objek dari permintaan pertama sehingga penjaga di `__init__` menolaknya. Kembalikan barisnya menjadi `b = Konfigurasi.get_instance()` agar program berjalan normal lagi.

</details>

## 2. Variasi *Singleton* ala Python: Modul dan `__new__`

*File*: [`contoh/contoh02_variasi_singleton.py`](contoh/contoh02_variasi_singleton.py)

Cara `get_instance()` di atas lazim di banyak bahasa. Python punya dua cara lain yang sering kamu temui di kode orang lain. `PencatatLog` di contoh ini adalah kelas biasa dengan *method* `catat(sumber, pesan)` dan `jumlah()`. Keistimewaannya ada pada cara objeknya dibuat. Berikut potongan *file*-nya, tepat di bawah kelas `PencatatLog`:

```python
# [1] Variasi 1: objek tingkat modul, dibuat SEKALI saat file ini dimuat
pencatat = PencatatLog()


class Tema:
    """Variasi 2: Singleton lewat __new__."""

    _instance = None
    _sudah_diisi = False

    def __new__(cls):  # [2] __new__ MEMBUAT objek, dipanggil sebelum __init__
        if cls._instance is None:
            print("  (objek Tema dibuat)")
            cls._instance = super().__new__(cls)
        return cls._instance  # [3] selalu mengembalikan objek yang sama

    def __init__(self):
        if Tema._sudah_diisi:  # [4] __init__ tetap terpanggil di SETIAP Tema()
            return
        Tema._sudah_diisi = True
        self._warna = "terang"
```

Kelas `Tema` juga punya *property* `warna` beserta *setter*-nya. Program utamanya:

```python
def modul_kasir():
    pencatat.catat("kasir", "transaksi dibuka")  # [5] memakai objek modul


def main():
    print("=== VARIASI 1: OBJEK DISIAPKAN DI AWAL (EAGER) ===")
    modul_kasir()
    modul_laporan()
    print(f"Jumlah catatan: {pencatat.jumlah()}")

    print()
    print("=== VARIASI 2: DIBUAT SAAT PERTAMA DIMINTA (LAZY) ===")
    print("Permintaan pertama:")
    t1 = Tema()  # [6] terlihat seperti membuat objek baru...
    print("Permintaan kedua:")
    t2 = Tema()  # ...padahal hasilnya objek yang sama
    print(f"t1 dan t2 objek yang sama? {'ya' if t1 is t2 else 'tidak'}")
    t1.warna = "gelap"
    print("Warna diubah lewat t1 menjadi gelap")
    print(f"Warna dibaca lewat t2: {t2.warna}")
```

***Output:***

```text
=== VARIASI 1: OBJEK DISIAPKAN DI AWAL (EAGER) ===
[LOG 1] kasir: transaksi dibuka
[LOG 2] laporan: laporan harian dibuat
Jumlah catatan: 2

=== VARIASI 2: DIBUAT SAAT PERTAMA DIMINTA (LAZY) ===
Permintaan pertama:
  (objek Tema dibuat)
Permintaan kedua:
t1 dan t2 objek yang sama? ya
Warna diubah lewat t1 menjadi gelap
Warna dibaca lewat t2: gelap
```

Penjelasan:

- **[1]** Variasi 1, **objek tingkat modul**. Sebuah modul (*file* `.py`) hanya dijalankan sekali walaupun di-*import* berkali-kali; Python menyimpan modul yang sudah dimuat dan memakainya lagi. Jadi objek `pencatat` hanya dibuat sekali, **di awal** (*eager*). Di proyek sungguhan, objek ini biasanya ditaruh di *file* sendiri, misalnya `log.py`, lalu dipakai dengan `from log import pencatat`.
- **[2]** Variasi 2, **`__new__`**. Ingat catatan di Pertemuan 02: objek sudah dibuat sesaat sebelum `__init__` berjalan. Yang membuatnya adalah *method* `__new__`, lalu `__init__` mengisinya. Di sini kita meng-*override* `__new__`. `super().__new__(cls)` memanggil versi asli milik kelas induk (`object`) untuk benar-benar membuat objek.
- **[3]** Pada pemanggilan berikutnya, `__new__` tidak membuat apa-apa, hanya mengembalikan objek yang tersimpan.
- **[4]** Jebakan penting! Setiap kali kamu menulis `Tema()`, Python tetap memanggil `__init__` pada objek yang dikembalikan `__new__`. Tanpa penjaga `_sudah_diisi`, `__init__` akan mengisi ulang `self._warna = "terang"`. Akibatnya, jika `Tema()` dipanggil lagi setelah `t1.warna = "gelap"`, warnanya diam-diam kembali menjadi `terang`. Tidak ada *error* sama sekali, jadi *bug* ini sulit dilacak.
- **[5]** Fungsi mana pun cukup memakai nama `pencatat`, tanpa `get_instance()` sama sekali. `modul_laporan()` ditulis serupa `modul_kasir()`.
- **[6]** Bagi pemanggil, `Tema()` terlihat seperti membuat objek baru, padahal tidak. Ini kelebihan sekaligus kekurangannya: praktis, tetapi bisa mengejutkan pembaca kode.

| Variasi | Kapan objek dibuat | Mencegah objek kedua? | Catatan |
|---|---|---|---|
| `get_instance()` (contoh 01) | saat pertama diminta | sebagian: penjaga di `__init__` baru bekerja setelah objek resmi ada | paling mirip versi Java |
| Objek tingkat modul | saat modul dimuat | tidak, hanya kesepakatan | paling sederhana dan paling *Pythonic* (sesuai gaya khas Python) |
| `__new__` | saat pertama diminta | ya, `Tema()` selalu objek yang sama | waspadai `__init__` yang terpanggil ulang |

> [!NOTE]
> *Output* contoh ini sengaja dibuat **sama persis** dengan versi Java. Bedanya hanya di mekanismenya: Java memakai *field* `static final` (*eager*) dan `synchronized` (*lazy* yang aman untuk banyak *thread*). Perbandingannya ada di [Jembatan Python ↔ Java](../jembatan-python-java.md).

## 3. Sisi Gelap *Singleton*: *State* Global

*File*: [`contoh/contoh03_bahaya_state_global.py`](contoh/contoh03_bahaya_state_global.py)

Di halaman konsep disebutkan bahwa *Singleton* sulit diuji. Contoh ini membuktikannya. `PengaturanPajak` adalah *Singleton* yang ditulis persis seperti contoh 01, dengan *property* `persen` (awalnya 10). Lalu ada dua "uji" kecil, yaitu fungsi yang memeriksa hasil hitungan dan mengembalikan `LULUS` atau `GAGAL`. `uji_harga_normal()` memeriksa bahwa Rp10.000 ditambah pajak 10% menjadi Rp11.000. Berikut potongan *file*-nya: fungsi `harga_akhir()`, uji kedua, dan kelas solusinya.

```python
def harga_akhir(harga: int) -> int:
    # [1] ketergantungan tersembunyi: tidak terlihat dari parameternya
    persen = PengaturanPajak.get_instance().persen
    return harga + harga * persen // 100


def uji_acara_bebas_pajak() -> str:
    """Saat acara bebas pajak, Rp10000 harus tetap Rp10000."""
    PengaturanPajak.get_instance().persen = 0  # [2] mengubah state global...
    hasil = harga_akhir(10000)  # ...dan lupa mengembalikannya
    return "LULUS" if hasil == 10000 else f"GAGAL (dapat Rp{hasil})"


class KalkulatorHarga:
    """[3] Solusi: persen pajak DIKIRIM lewat konstruktor (dependency injection)."""

    def __init__(self, persen_pajak: int):
        self._persen_pajak = persen_pajak

    def harga_akhir(self, harga: int) -> int:
        return harga + harga * self._persen_pajak // 100
```

Program utamanya:

```python
def main():
    print("=== PUTARAN 1: DUA UJI DIJALANKAN ===")
    print(f"Uji harga normal      : {uji_harga_normal()}")
    print(f"Uji acara bebas pajak : {uji_acara_bebas_pajak()}")

    print()
    print("=== PUTARAN 2: UJI YANG SAMA DIULANG ===")
    print(f"Uji harga normal      : {uji_harga_normal()}")  # [4] kini gagal!
    print(f"Pajak sekarang {PengaturanPajak.get_instance().persen}%, "
          "sisa perubahan uji sebelumnya")

    print()
    print("=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===")
    normal = KalkulatorHarga(10)  # [5] setiap uji punya objeknya sendiri
    bebas_pajak = KalkulatorHarga(0)
    print(f"Pajak 10%: Rp10000 -> Rp{normal.harga_akhir(10000)}")
    print(f"Pajak 0% : Rp10000 -> Rp{bebas_pajak.harga_akhir(10000)}")
    print(f"Diulang  : Rp10000 -> Rp{normal.harga_akhir(10000)} (tetap benar)")
```

***Output:***

```text
=== PUTARAN 1: DUA UJI DIJALANKAN ===
Uji harga normal      : LULUS
Uji acara bebas pajak : LULUS

=== PUTARAN 2: UJI YANG SAMA DIULANG ===
Uji harga normal      : GAGAL (dapat Rp10000)
Pajak sekarang 0%, sisa perubahan uji sebelumnya

=== SOLUSI: KIRIM NILAINYA LEWAT KONSTRUKTOR ===
Pajak 10%: Rp10000 -> Rp11000
Pajak 0% : Rp10000 -> Rp10000
Diulang  : Rp10000 -> Rp11000 (tetap benar)
```

Penjelasan:

- **[1]** Dari luar, `harga_akhir(harga)` terlihat hanya butuh `harga`. Padahal diam-diam ia juga bergantung pada *Singleton*. Inilah **ketergantungan tersembunyi**.
- **[2]** Uji kedua mengubah pajak menjadi 0 dan lupa mengembalikannya. Karena objeknya satu untuk seluruh program, perubahan itu **menetap**.
- **[3]** Solusinya adalah *dependency injection* dari Pertemuan 13: kebutuhan dikirim lewat konstruktor sehingga terlihat jelas dan mudah diganti.
- **[4]** Uji yang **sama persis**, yang tadi LULUS, kini GAGAL. Hasil uji bergantung pada urutan dan riwayat pemanggilan sebelumnya. Bayangkan mencari penyebabnya di program berisi ratusan uji!
- **[5]** Setiap `KalkulatorHarga` membawa nilainya sendiri. Membuat objek berpajak 0% tidak mengganggu objek berpajak 10%.

> [!TIP]
> *Singleton* dan *dependency injection* bisa berdampingan. Di bagian paling luar program (misalnya `main()`), ambil nilainya dari *Singleton* lalu **kirimkan**: `KalkulatorHarga(PengaturanPajak.get_instance().persen)`. Kelas-kelas di dalam tetap mudah diuji karena tidak meraih *Singleton* sendiri.

## 4. *Simple Factory*: Membuat Objek dari Teks

*File*: [`contoh/contoh04_simple_factory.py`](contoh/contoh04_simple_factory.py)

Aplikasi ojek *online* menerima pilihan kendaraan berupa teks. Kelas abstrak `Kendaraan` punya *method* abstrak `nama()`, `kapasitas()`, dan `tarif_per_km()`, serta *method* biasa `hitung_ongkos(jarak_km)`. Tiga kelas anaknya mengisi *method* abstrak itu: `Motor` (1 penumpang, Rp2.500/km), `Mobil` (4 penumpang, Rp4.000/km), dan `MobilBesar` (6 penumpang, Rp5.500/km). Berikut potongan *file*-nya, bagian *factory* dan pemakainya:

```python
class KendaraanFactory:
    """Simple Factory: SATU tempat yang memutuskan kelas mana yang dibuat."""

    @staticmethod
    def buat(jenis: str) -> Kendaraan:  # [1] tipe kembalian: kelas abstrak
        pilihan = jenis.lower()  # [2] "MOBIL" dan "mobil" dianggap sama
        if pilihan == "motor":
            return Motor()
        if pilihan == "mobil":
            return Mobil()
        if pilihan == "mobil besar":
            return MobilBesar()
        raise ValueError(f"Jenis kendaraan tidak dikenal: {jenis}")  # [3]


def main():
    print("=== PESANAN DARI APLIKASI (JARAK 8 KM) ===")
    for pilihan in ["motor", "Mobil", "MOBIL BESAR"]:
        kendaraan = KendaraanFactory.buat(pilihan)  # [4] cukup kirim teks
        ongkos = kendaraan.hitung_ongkos(8)
        print(f"{pilihan:<12} -> {kendaraan.nama():<12} "
              f"maks {kendaraan.kapasitas()} penumpang, Rp{ongkos}")
```

Setelah itu, `main()` mencoba `KendaraanFactory.buat("helikopter")` di dalam `try` dan menangkapnya dengan `except ValueError as e:  # [5]`.

***Output:***

```text
=== PESANAN DARI APLIKASI (JARAK 8 KM) ===
motor        -> Motor        maks 1 penumpang, Rp20000
Mobil        -> Mobil        maks 4 penumpang, Rp32000
MOBIL BESAR  -> Mobil Besar  maks 6 penumpang, Rp44000

=== PILIHAN TIDAK DIKENAL ===
Ditolak: Jenis kendaraan tidak dikenal: helikopter
```

Penjelasan:

- **[1]** `@staticmethod` (Pertemuan 03): *method* milik kelas yang tidak butuh `self` maupun `cls`. Petunjuk tipenya `-> Kendaraan`, yaitu kelas **abstrak**. Pemanggil hanya dijanjikan "sebuah kendaraan", bukan kelas tertentu.
- **[2]** `.lower()` membuat pilihan tidak peka huruf besar/kecil. Pengguna boleh mengetik `MOBIL BESAR`.
- **[3]** Pilihan yang tidak dikenal ditolak di **satu tempat** dengan `ValueError` (Pertemuan 11).
- **[4]** Pemanggil tidak pernah menulis `Motor()` atau `Mobil()`. Ia cukup mengirim teks, lalu memakai objek hasilnya lewat *method* milik `Kendaraan`. Ini polimorfisme (Pertemuan 09) yang bekerja sama dengan *factory*.
- **[5]** Kesalahan *input* ditangkap dengan `try`/`except` seperti biasa.

> [!TIP]
> **Coba sendiri:** salin `contoh04_simple_factory.py` ke folder `pertemuan-14` milikmu, lalu buka salinannya.
>
> 1. Tambahkan kelas `Bajaj(Kendaraan)` di atas `KendaraanFactory`. Tiru kelas `Motor`: `nama()` mengembalikan `"Bajaj"`, `kapasitas()` mengembalikan 2, dan `tarif_per_km()` mengembalikan 3000.
> 2. Di `KendaraanFactory.buat()`, tepat sebelum baris `raise`, tambahkan cabang baru yang mengembalikan `Bajaj()` jika `pilihan == "bajaj"`.
> 3. Agar hasilnya terlihat, tambahkan teks `"bajaj"` ke daftar pilihan di perulangan `for` dalam `main()`.
>
> Simpan, lalu jalankan. Perhatikan: logika pembuatan objek hanya berubah di **satu** tempat, yaitu *factory*.

<details>
<summary>Lihat kode dan hasil yang diharapkan</summary>

Cabang baru di *factory*:

```python
        if pilihan == "bajaj":
            return Bajaj()
```

Bagian pertama *output* kini punya satu baris tambahan:

```text
bajaj        -> Bajaj        maks 2 penumpang, Rp24000
```

Ongkosnya 8 km × Rp3.000 = Rp24.000. Kode pemakai di `main()` tetap memanggil `KendaraanFactory.buat(pilihan)` tanpa pernah menyebut nama kelas `Bajaj`.

</details>

## 5. *Factory Method*: *Subclass* yang Memilih

*File*: [`contoh/contoh05_factory_method.py`](contoh/contoh05_factory_method.py)

Sekarang versi GoF. Tidak ada lagi `if`: setiap kelas anak memutuskan sendiri produk yang dibuatnya. Berikut potongan *file*-nya. Di *file* aslinya, kelas `Truk` dan `KapalSungai` berada di antara `Angkutan` dan `Ekspedisi`; keduanya dilewati di sini.

```python
class Angkutan(ABC):
    """Produk: sesuatu yang bisa mengantar paket."""

    @abstractmethod
    def antar(self, tujuan: str) -> str:
        """Keterangan perjalanan menuju tujuan."""


class Ekspedisi(ABC):
    """Langkah kerja tetap, tetapi produk angkutannya diserahkan ke subclass."""

    @abstractmethod
    def nama(self) -> str:
        """Nama layanan ekspedisi."""

    @abstractmethod
    def buat_angkutan(self) -> Angkutan:  # [1] inilah FACTORY METHOD
        """Subclass memutuskan angkutan apa yang dibuat."""

    def kirim_paket(self, tujuan: str):  # [2] memakai produk tanpa tahu kelasnya
        print(f"[{self.nama()}] Paket ke {tujuan} dikemas")
        angkutan = self.buat_angkutan()
        print(f"  {angkutan.antar(tujuan)}")
        print(f"  Paket tiba di {tujuan}")


class EkspedisiDarat(Ekspedisi):
    def nama(self) -> str:
        return "Ekspedisi Darat"

    def buat_angkutan(self) -> Angkutan:  # [3] subclass memilih produknya
        return Truk()
```

Produk konkretnya, `Truk` dan `KapalSungai`, hanya mengembalikan teks perjalanan. `EkspedisiSungai` ditulis serupa `EkspedisiDarat`, dengan `buat_angkutan()` yang mengembalikan `KapalSungai()`. Program utamanya:

```python
def main():
    print("=== FACTORY METHOD: SUBCLASS MEMILIH ANGKUTANNYA ===")
    darat: Ekspedisi = EkspedisiDarat()
    sungai: Ekspedisi = EkspedisiSungai()
    darat.kirim_paket("Balikpapan")  # [4] method sama, angkutan berbeda
    sungai.kirim_paket("Tenggarong")
```

***Output:***

```text
=== FACTORY METHOD: SUBCLASS MEMILIH ANGKUTANNYA ===
[Ekspedisi Darat] Paket ke Balikpapan dikemas
  Truk melaju lewat jalan darat menuju Balikpapan
  Paket tiba di Balikpapan
[Ekspedisi Sungai] Paket ke Tenggarong dikemas
  Kapal menyusuri Sungai Mahakam menuju Tenggarong
  Paket tiba di Tenggarong
```

Penjelasan:

- **[1]** `buat_angkutan()` adalah *factory method*: *method* abstrak yang tugasnya **membuat** produk. Kelas induk tidak tahu produknya apa.
- **[2]** `kirim_paket()` adalah langkah kerja tetap: kemas, buat angkutan, antar, tiba. Ia memanggil `buat_angkutan()` dan memakai hasilnya sebagai `Angkutan`. Pola "kerangka di induk, langkah tertentu di anak" ini juga punya nama sendiri: *Template Method*.
- **[3]** Kelas anak meng-*override* *factory method* dan memilih produknya. Inilah bedanya dengan *Simple Factory*: keputusan diambil lewat *overriding*, bukan lewat `if`.
- **[4]** Variabel diberi petunjuk tipe `Ekspedisi`. *Method* yang dipanggil sama, tetapi angkutan yang dipakai berbeda.

> [!TIP]
> **Coba sendiri:** salin `contoh05_factory_method.py` ke folder `pertemuan-14` milikmu, lalu buka salinannya.
>
> 1. Di atas `main()`, tambahkan kelas `Pesawat(Angkutan)` yang `antar()`-nya mengembalikan `f"Pesawat terbang menuju {tujuan}"`.
> 2. Tambahkan kelas `EkspedisiUdara(Ekspedisi)`: `nama()` mengembalikan `"Ekspedisi Udara"`, dan `buat_angkutan()` mengembalikan `Pesawat()`.
> 3. Di akhir `main()`, tambahkan `udara: Ekspedisi = EkspedisiUdara()` lalu `udara.kirim_paket("Berau")`.
>
> Simpan, lalu jalankan. Kamu hanya **menambah** kelas baru; tidak ada satu baris pun kode lama yang diubah. Bandingkan dengan *Simple Factory*, yang harus ditambah cabang `if`.

<details>
<summary>Lihat hasil yang diharapkan</summary>

Di bawah *output* lama muncul tiga baris baru:

```text
[Ekspedisi Udara] Paket ke Berau dikemas
  Pesawat terbang menuju Berau
  Paket tiba di Berau
```

</details>

## 6. *Strategy*: Menukar Cara Menghitung

*File*: [`contoh/contoh06_strategy_ongkir.py`](contoh/contoh06_strategy_ongkir.py)

Kelas abstrak `StrategiOngkir` punya dua *method* abstrak: `nama()` dan `hitung(berat_kg)`. Tiga strategi mengisinya dengan rumus berbeda:

| Strategi | `nama()` | Rumus `hitung(berat_kg)` |
|---|---|---|
| `OngkirReguler` | Reguler (3 hari) | `8000 * berat_kg` |
| `OngkirKilat` | Kilat (besok tiba) | `15000 * berat_kg + 5000` |
| `OngkirHemat` | Hemat (5 hari) | `5000 * max(berat_kg, 3)` (minimal dihitung 3 kg) |

Yang memakai strategi adalah `Pengiriman` (*context*). Berikut potongan *file*-nya: kelas `Pengiriman` dan `main()`. Kelas `OngkirAmbilSendiri` yang berada di antara keduanya dibahas di penjelasan [5].

```python
class Pengiriman:
    """Context: memakai strategi ongkir tanpa tahu rumus di dalamnya."""

    def __init__(self, berat_kg: int, strategi: StrategiOngkir):
        self._berat_kg = berat_kg
        self._strategi = strategi  # [1] strategi disimpan sebagai atribut

    def atur_strategi(self, strategi: StrategiOngkir):  # [2] bisa ditukar
        self._strategi = strategi

    def ongkir(self) -> int:
        return self._strategi.hitung(self._berat_kg)  # [3] didelegasikan

    def ringkasan(self) -> str:
        return f"{self._strategi.nama():<20} Rp{self.ongkir()}"


def main():
    paket = Pengiriman(2, OngkirReguler())
    print("=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===")
    for strategi in [OngkirReguler(), OngkirKilat(), OngkirHemat()]:
        paket.atur_strategi(strategi)  # [4] tukar saat program berjalan
        print(paket.ringkasan())

    print()
    print("=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===")
    paket.atur_strategi(OngkirAmbilSendiri())  # [5]
    print(paket.ringkasan())
```

***Output:***

```text
=== PAKET 2 KG DARI SAMARINDA KE BONTANG ===
Reguler (3 hari)     Rp16000
Kilat (besok tiba)   Rp35000
Hemat (5 hari)       Rp15000

=== STRATEGI BARU, KELAS Pengiriman TIDAK DIUBAH ===
Ambil di gerai       Rp0
```

Penjelasan:

- **[1]** *Context* **menyimpan** objek strategi sebagai atribut. Ini hubungan "punya" (agregasi, Pertemuan 05).
- **[2]** `atur_strategi()` menukar strategi kapan saja, bahkan setelah objek `Pengiriman` dibuat.
- **[3]** `Pengiriman` tidak menghitung apa pun sendiri. Ia **mendelegasikan** pekerjaan ke strategi, lalu memakai hasilnya.
- **[4]** Satu objek `paket` yang sama dihitung dengan tiga strategi bergantian. Tidak ada `if` sama sekali.
- **[5]** `OngkirAmbilSendiri` (nama "Ambil di gerai", ongkir selalu 0) sengaja ditulis **setelah** `Pengiriman` di *file*, seolah-olah ditambahkan belakangan. `Pengiriman` tidak diubah sedikit pun: OCP terpenuhi.

> [!TIP]
> **Coba sendiri:** salin `contoh06_strategy_ongkir.py` ke folder `pertemuan-14` milikmu, lalu buka salinannya. Di atas `main()`, tambahkan kelas `OngkirSameDay(StrategiOngkir)` dengan `nama()` yang mengembalikan `"Same Day (hari ini)"` dan `hitung()` yang mengembalikan `25000 * berat_kg`. Lalu tambahkan `OngkirSameDay()` ke daftar strategi di perulangan `for` dalam `main()`. Simpan, lalu jalankan.

<details>
<summary>Lihat hasil yang diharapkan</summary>

Bagian pertama *output* kini punya baris keempat:

```text
Same Day (hari ini)  Rp50000
```

Berat 2 kg × Rp25.000 = Rp50.000. Kelas `Pengiriman` lagi-lagi tidak perlu diubah.

</details>

## 7. *Observer*: Berlangganan Kabar

*File*: [`contoh/contoh07_observer_kanal_video.py`](contoh/contoh07_observer_kanal_video.py)

Kelas abstrak `PengamatKanal` hanya punya satu *method* abstrak: `perbarui(nama_kanal, judul)`. Ada dua pengamat konkret: `Penonton` mencetak notifikasi ke "HP"-nya, sedangkan `PencatatStatistik` menghitung jumlah video. *Subject*-nya adalah `KanalVideo`. Berikut potongan *file*-nya, bagian kelas `KanalVideo`:

```python
class KanalVideo:
    """Subject: menyimpan daftar pengamat dan memberi kabar ke semuanya."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_pengamat: list[PengamatKanal] = []  # [1]

    def langganan(self, pengamat: PengamatKanal):  # [2]
        self._daftar_pengamat.append(pengamat)

    def berhenti_langganan(self, pengamat: PengamatKanal):
        self._daftar_pengamat.remove(pengamat)

    def unggah_video(self, judul: str):
        print(f"{self._nama} mengunggah: {judul}")
        self._beri_kabar(judul)  # [3] kejadian -> semua pengamat diberi tahu

    def _beri_kabar(self, judul: str):
        for pengamat in self._daftar_pengamat:  # [4] tidak peduli jenisnya
            pengamat.perbarui(self._nama, judul)
```

Di `main()`, kanal "Belajar PBO" mendapat tiga pengamat: penonton Ayu, penonton Bima, dan sebuah `PencatatStatistik`. Setelah video pertama diunggah, Bima berhenti berlangganan dengan `kanal.berhenti_langganan(bima)  # [5]`, lalu video kedua diunggah.

***Output:***

```text
=== VIDEO PERTAMA (3 PENGAMAT) ===
Belajar PBO mengunggah: Kelas dan Objek
  [HP Ayu] Video baru dari Belajar PBO: Kelas dan Objek
  [HP Bima] Video baru dari Belajar PBO: Kelas dan Objek
  [STATISTIK] Belajar PBO sudah mengunggah 1 video

=== BIMA BERHENTI BERLANGGANAN ===
Belajar PBO mengunggah: Design Pattern Dasar
  [HP Ayu] Video baru dari Belajar PBO: Design Pattern Dasar
  [STATISTIK] Belajar PBO sudah mengunggah 2 video
```

Penjelasan:

- **[1]** *Subject* menyimpan pengamat dalam *list* bertipe abstraksi `PengamatKanal`, bukan `Penonton`.
- **[2]** `langganan()` dan `berhenti_langganan()` adalah pintu untuk mendaftar dan keluar.
- **[3]** Setiap kejadian (video baru) langsung diikuti pemberian kabar.
- **[4]** `KanalVideo` memanggil `perbarui()` milik setiap pengamat tanpa tahu apakah itu penonton atau pencatat statistik. Data kejadian dikirim sebagai argumen: inilah gaya ***push***.
- **[5]** Setelah Bima berhenti berlangganan, ia tidak lagi menerima kabar video kedua.

> [!WARNING]
> `list.remove()` melempar `ValueError` jika objek yang dihapus tidak ada di *list*. Jika program bisa saja memanggil `berhenti_langganan()` untuk pengamat yang belum terdaftar, periksa dulu dengan `if pengamat in self._daftar_pengamat:`.

## 8. Studi Kasus KedaiKita

*File* baru: [`studi-kasus/pengaturan.py`](studi-kasus/pengaturan.py), [`studi-kasus/pengamat.py`](studi-kasus/pengamat.py), [`studi-kasus/notifikasi.py`](studi-kasus/notifikasi.py). *File* yang berubah: [`pembayaran.py`](studi-kasus/pembayaran.py), [`diskon.py`](studi-kasus/diskon.py), [`pesanan.py`](studi-kasus/pesanan.py), [`struk.py`](studi-kasus/struk.py), [`laporan.py`](studi-kasus/laporan.py), dan [`main.py`](studi-kasus/main.py).

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini).

**Apa yang berubah dibanding Pertemuan 13?**

- **Baru** `pengaturan.py`: *Singleton* `PengaturanKedai` (nama kedai, alamat, pajak 10%).
- **Baru** `pengamat.py` (kontrak `PengamatPesanan`) dan `notifikasi.py` (`LayarDapur`, `NotifikasiPelanggan`).
- `pembayaran.py`: ditambah kelas `PembayaranFactory`.
- `diskon.py`: ditambah strategi `DiskonHappyHour`.
- `pesanan.py`: ada `hitung_pajak()`, total kini memuat pajak, ada daftar pengamat, `tambah_pengamat()`, `ubah_status()`, dan `bayar()` mengubah status lewat `ubah_status("LUNAS")`.
- `struk.py`: kepala struk memakai nama dan alamat dari `PengaturanKedai`, dan ada baris pajak.
- `laporan.py`: hanya teks label menjadi "(sebelum diskon & pajak)".
- `main.py` ditulis ulang: empat bagian, satu bagian per pola.
- *File* lain (`menu.py`, `pelanggan.py`, `item_pesanan.py`, `kedai.py`, `penyimpanan.py`, `pengecualian.py`, `pasangan.py`, `dapat_dicetak.py`, `utilitas.py`) **tidak berubah**.

Cara menjalankannya ada di [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus). Singkatnya, dari folder utama materi:

```bash
cd Pertemuan-14-Design-Pattern/python/studi-kasus
python main.py
```

*Output*-nya panjang, jadi kita bahas per bagian. Setiap blok ***Output:*** di bawah adalah sepotong dari *output* `main.py` itu.

### 8.1 *Singleton*: `pengaturan.py`

*File*: [`studi-kasus/pengaturan.py`](studi-kasus/pengaturan.py)

Berikut potongan *file*-nya, tanpa komentar pembuka:

```python
class PengaturanKedai:
    """Pengaturan global KedaiKita (Singleton)."""

    _instance = None  # tempat menyimpan satu-satunya objek

    def __init__(self):
        if PengaturanKedai._instance is not None:
            raise RuntimeError("PengaturanKedai adalah Singleton. "
                               "Gunakan PengaturanKedai.get_instance()")
        self._nama_kedai = "KedaiKita"
        self._alamat = "Jl. Pramuka No. 10, Samarinda"
        self._pajak_persen = 10  # Pajak Barang dan Jasa Tertentu (PBJT) 10%

    @classmethod
    def get_instance(cls) -> "PengaturanKedai":
        """Mengembalikan satu-satunya objek; dibuat saat pertama kali diminta."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
```

Di bawahnya ada *property* `nama_kedai`, `alamat`, dan `pajak_persen`. Hanya `pajak_persen` yang punya *setter*, dengan validasi 0 sampai 100. Struktur *Singleton*-nya sama persis dengan contoh 01. Pajak 10% di sini adalah nilai simulasi untuk latihan.

Bagian pertama `main()` meminta pengaturan dua kali (`pengaturan_a` dan `pengaturan_b`), membandingkannya dengan `is`, lalu mencetak isinya:

***Output:***

```text
=== 1. SINGLETON: PENGATURAN KEDAI ===
Objek yang sama? ya
Nama   : KedaiKita
Alamat : Jl. Pramuka No. 10, Samarinda
Pajak  : 10%
```

### 8.2 *Factory*: `PembayaranFactory` di `pembayaran.py`

*File*: [`studi-kasus/pembayaran.py`](studi-kasus/pembayaran.py)

Kelas `PembayaranFactory` berada di bagian paling bawah *file* itu:

```python
class PembayaranFactory:
    """Factory: membuat objek Pembayaran berdasarkan pilihan (teks)."""

    @staticmethod
    def buat(jenis: str, nominal: int = 0, bank: str = "") -> Pembayaran:
        """nominal = uang diterima (tunai) atau saldo e-wallet (qris)."""
        pilihan = jenis.lower()
        if pilihan == "tunai":
            return PembayaranTunai(nominal)
        if pilihan == "qris":
            return PembayaranQRIS(nominal)
        if pilihan == "kartu":
            return PembayaranKartu(bank)
        raise ValueError(f"Metode pembayaran tidak dikenal: {jenis}")
```

- *Factory* ditaruh di *file* yang sama dengan kelas-kelas `Pembayaran` karena ia perlu mengenal ketiganya.
- `nominal` dan `bank` punya nilai bawaan (`0` dan `""`), jadi pemanggil boleh hanya mengisi yang relevan.
- Kode di luar *file* ini tidak perlu meng-*import* `PembayaranTunai`, `PembayaranQRIS`, atau `PembayaranKartu`. Cukup `PembayaranFactory`.

Bagian kedua `main()` memanggil `PembayaranFactory.buat(pilihan, 100000, "BNI")` untuk pilihan `"tunai"`, `"QRIS"`, dan `"kartu"`, lalu mencoba `"bitcoin"` di dalam `try`/`except ValueError`:

***Output:***

```text
=== 2. FACTORY: MEMBUAT PEMBAYARAN DARI PILIHAN ===
Pilihan 'tunai' -> Tunai (biaya layanan Rp0)
Pilihan 'QRIS' -> QRIS (biaya layanan Rp0)
Pilihan 'kartu' -> Kartu Kredit BNI (biaya layanan Rp2.000)
Ditolak: Metode pembayaran tidak dikenal: bitcoin
```

Pilihan `'QRIS'` ditulis kapital, tetapi tetap dikenali berkat `.lower()`. Biaya layanan kartu Rp2.000 adalah 2% dari Rp100.000 (aturan sejak Pertemuan 09).

### 8.3 *Strategy*: `DiskonHappyHour` di `diskon.py`

*File*: [`studi-kasus/diskon.py`](studi-kasus/diskon.py) dan [`studi-kasus/pesanan.py`](studi-kasus/pesanan.py)

Strategi baru ini hanya menambah satu kelas di bagian paling bawah `diskon.py`. `Diskon`, `TanpaDiskon`, `DiskonPersen`, dan `DiskonMember` tidak berubah.

```python
class DiskonHappyHour(Diskon):
    """Happy hour: diskon 20% khusus untuk item minuman."""

    PERSEN = 20

    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        total_minuman = 0
        for item in daftar_item:
            if item.menu.kategori == "Minuman":
                total_minuman += item.hitung_subtotal()
        return total_minuman * DiskonHappyHour.PERSEN // 100

    def keterangan(self) -> str:
        return "Happy Hour (minuman)"
```

Total pesanan kini memuat pajak. Berikut potongan dari kelas `Pesanan` di `pesanan.py` (menjorok karena berada di dalam kelas):

```python
    def hitung_pajak(self) -> int:
        """Pajak dihitung dari subtotal setelah dipotong diskon."""
        persen = PengaturanKedai.get_instance().pajak_persen
        return (self.hitung_subtotal() - self.hitung_potongan()) * persen // 100

    def hitung_total(self) -> int:
        return self.hitung_subtotal() - self.hitung_potongan() + self.hitung_pajak()
```

Bagian ketiga `main()` memasang `TanpaDiskon()`, `DiskonPersen(15)`, dan `DiskonHappyHour()` secara bergantian pada pesanan Rina lewat `pesanan_rina.atur_diskon(strategi)`, lalu mencetak potongan dan totalnya:

***Output:***

```text
=== 3. STRATEGY: MENUKAR ATURAN DISKON ===
Subtotal pesanan Rina: Rp59.000
Tanpa diskon           potongan      Rp0, total Rp64.900
Promo 15%              potongan  Rp8.850, total Rp55.165
Happy Hour (minuman)   potongan  Rp7.200, total Rp56.980
```

- `atur_diskon()` adalah cara menukar strategi, persis seperti `atur_strategi()` di contoh 06. *Method* ini sudah ada sejak Pertemuan 13. Hari ini kita sekadar mengenali namanya: ***Strategy***.
- *Happy Hour* hanya memotong minuman: 20% dari Rp36.000 (2 kopi) = Rp7.200. Mie goreng tidak ikut dipotong.
- Persentase pajak (10%) dibaca dari *Singleton* `PengaturanKedai`, lalu pajaknya dihitung dari subtotal setelah diskon. Contoh untuk Promo 15%: pajak = (Rp59.000 − Rp8.850) × 10% = Rp5.015 sehingga total = Rp59.000 − Rp8.850 + Rp5.015 = Rp55.165.

### 8.4 *Observer*: `pengamat.py`, `notifikasi.py`, dan `pesanan.py`

*File*: [`studi-kasus/pengamat.py`](studi-kasus/pengamat.py), [`studi-kasus/notifikasi.py`](studi-kasus/notifikasi.py), dan [`studi-kasus/pesanan.py`](studi-kasus/pesanan.py)

Kontrak pengamatnya ada di `pengamat.py` (potongan, tanpa komentar pembuka dan baris `import`):

```python
class PengamatPesanan(ABC):
    """Kontrak untuk objek yang ingin diberi tahu perubahan status pesanan."""

    @abstractmethod
    def perbarui(self, pesanan):
        """Dipanggil oleh Pesanan setiap kali statusnya berubah.

        Parameter pesanan sengaja tidak diberi type hint, agar modul ini
        tidak perlu meng-import pesanan.py (mencegah circular import).
        """
```

Mengapa parameter `pesanan` **tidak** diberi petunjuk tipe `Pesanan`? Karena untuk menulis `pesanan: Pesanan`, *file* ini harus meng-*import* `pesanan.py`. Padahal `pesanan.py` sendiri sudah meng-*import* `pengamat.py`. Dua *file* yang saling meng-*import* disebut **impor melingkar** (*circular import*), dan dalam kasus ini Python gagal memuatnya (lihat Kesalahan 3). Masalah serupa pernah kita temui di Pertemuan 13, saat `ItemPesanan` dipindah ke *file* sendiri.

Arah `import` di antara ketiga *file* itu (panah dibaca "meng-*import*"):

```text
pesanan.py    --import-->  pengamat.py                  (aman)
pengamat.py   --import-->  pesanan.py                   (jika ditambahkan: melingkar, GAGAL)
notifikasi.py --import-->  pengamat.py dan pesanan.py   (aman, tidak ada yang balik)
```

Ada teknik lanjutan untuk tetap menulis petunjuk tipe tanpa impor melingkar (`typing.TYPE_CHECKING`), tetapi itu di luar cakupan kita. Menghilangkan petunjuk tipe di satu parameter adalah pilihan paling sederhana.

Dua pengamat konkretnya ada di `notifikasi.py`. *File* ini **boleh** meng-*import* `pesanan.py` karena `pesanan.py` tidak meng-*import* balik `notifikasi.py`. Berikut isi `notifikasi.py` tanpa komentar pembuka dan baris `import`:

```python
class LayarDapur(PengamatPesanan):
    """Layar di dapur yang menampilkan pesanan masuk."""

    def perbarui(self, pesanan: Pesanan):
        if pesanan.status == "LUNAS":
            daftar = ", ".join(str(item) for item in pesanan.daftar_item)
            print(f"  [DAPUR] Pesanan baru {pesanan.nomor}: {daftar}")
        else:
            print(f"  [DAPUR] {pesanan.nomor} -> {pesanan.status}")


class NotifikasiPelanggan(PengamatPesanan):
    """Mengirim kabar status pesanan ke nomor HP pelanggan (simulasi)."""

    def perbarui(self, pesanan: Pesanan):
        pelanggan = pesanan.pelanggan
        print(f"  [SMS ke {pelanggan.no_hp}] Halo {pelanggan.nama}, "
              f"status pesanan {pesanan.nomor}: {pesanan.status}")
```

*Subject*-nya adalah `Pesanan`. Di konstruktornya ada `self._daftar_pengamat: list[PengamatPesanan] = []`. Berikut potongan kelas `Pesanan` yang mengurus pengamat:

```python
    # ----- pola Observer -----
    def tambah_pengamat(self, pengamat: PengamatPesanan):
        self._daftar_pengamat.append(pengamat)

    def ubah_status(self, status_baru: str):
        """Mengubah status lalu memberi tahu SEMUA pengamat."""
        if status_baru not in STATUS_VALID:
            raise ValueError(f"Status tidak dikenal: {status_baru}")
        self._status = status_baru
        for pengamat in self._daftar_pengamat:
            pengamat.perbarui(self)
```

- `STATUS_VALID` adalah *tuple* berisi `"BARU"`, `"LUNAS"`, `"DIPROSES"`, `"SIAP"`, dan `"SELESAI"`. Status lain ditolak.
- `pengamat.perbarui(self)` mengirim **objek pesanan itu sendiri**. Inilah gaya ***pull***: `LayarDapur` menarik nomor dan item, `NotifikasiPelanggan` menarik data pelanggan.
- Di `bayar()`, baris `self._status = "LUNAS"` versi Pertemuan 13 kini diganti `self.ubah_status("LUNAS")` di akhir *method* sehingga pengamat ikut tahu saat pesanan dibayar.

Bagian keempat `main()` membuat pesanan Budi (2 Kopi Susu Gula Aren, 1 Nasi Goreng Kampung), mendaftarkan `LayarDapur()` dan `NotifikasiPelanggan()` lewat `tambah_pengamat()`, membayar dengan `PembayaranFactory.buat("tunai", 100000, "")`, lalu memanggil `ubah_status()` untuk `DIPROSES`, `SIAP`, dan `SELESAI`:

***Output:***

```text
=== 4. OBSERVER: NOTIFIKASI STATUS PESANAN ===
Pembayaran pesanan P002 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp67.100
  Uang diterima Rp100.000, kembalian Rp32.900
  Status       : LUNAS (+6 poin)
  [DAPUR] Pesanan baru P002: 2 x Kopi Susu Gula Aren, 1 x Nasi Goreng Kampung
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: LUNAS
Status diubah menjadi DIPROSES:
  [DAPUR] P002 -> DIPROSES
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: DIPROSES
Status diubah menjadi SIAP:
  [DAPUR] P002 -> SIAP
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: SIAP
Status diubah menjadi SELESAI:
  [DAPUR] P002 -> SELESAI
  [SMS ke 081234567890] Halo Budi Santoso, status pesanan P002: SELESAI
```

- Empat perubahan status × dua pengamat = delapan kabar. `Pesanan` tidak pernah menyebut nama `LayarDapur` atau `NotifikasiPelanggan`.
- Pembayaran pun memakai *factory*: `PembayaranFactory.buat("tunai", 100000, "")`.

### 8.5 Struk Baru: `struk.py`

*File*: [`studi-kasus/struk.py`](studi-kasus/struk.py)

Di awal `buat_teks()`, struk mengambil `pengaturan = PengaturanKedai.get_instance()`, lalu memakai `pengaturan.nama_kedai` dan `pengaturan.alamat` sebagai kepala struk. Di bagian akhir ada baris pajak (potongan dari `buat_teks()`):

```python
        pajak = f"Pajak {pengaturan.pajak_persen}%"
        baris.append(self._baris_rapi(pajak, format_rupiah(p.hitung_pajak())))
        baris.append(self._baris_rapi("TOTAL", format_rupiah(p.hitung_total())))
```

Label `Pajak 10%` dan hitungan pajaknya sama-sama berasal dari `PengaturanKedai`. Jika pajak diubah lewat *setter*, label dan angkanya pasti berubah bersamaan.

***Output:***

```text
========================================
KedaiKita
Jl. Pramuka No. 10, Samarinda
========================================
No. Pesanan : P002
Pelanggan   : Budi Santoso
Status      : SELESAI
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
Subtotal                        Rp61.000
Pajak 10%                        Rp6.100
TOTAL                           Rp67.100
========================================
```

> [!TIP]
> **Coba sendiri:** salin **seluruh folder** `studi-kasus` ke folder `pertemuan-14` milikmu, lalu buka `main.py` di salinan itu. Tepat di bawah baris `def main():`, tambahkan baris baru `PengaturanKedai.get_instance().pajak_persen = 11`, menjorok 4 spasi seperti baris-baris di bawahnya. Simpan, lalu jalankan `python main.py` dari folder salinan itu. Berapa total pesanan Budi sekarang, dan apa tulisan di struk?

<details>
<summary>Lihat jawaban</summary>

Pajak menjadi 11% × Rp61.000 = Rp6.710 sehingga total pesanan Budi menjadi **Rp67.710**, dan struk menampilkan baris berikut:

```text
Pajak 11%                        Rp6.710
TOTAL                           Rp67.710
```

Bagian lain juga ikut berubah: bagian *Singleton* mencetak `Pajak  : 11%`, total di bagian *Strategy* menjadi Rp65.490, Rp55.666, dan Rp57.498, dan kembalian Budi menjadi Rp32.290. Satu baris mengubah seluruh program: inilah kekuatan sekaligus bahaya *state* global.

</details>

## 9. Kesalahan Umum dan Cara Membaca Pesan *Error*

Ketiga kesalahan berikut memakai kelas-kelas studi kasus, jadi cobalah di **salinan** folder `studi-kasus` milikmu (lihat [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)). Jalankan dari terminal yang berada di folder salinan itu. Jika sudah selesai, hapus *file* coba-cobanya atau salin ulang folder `studi-kasus` dari materi.

### Kesalahan 1: Membuat objek *Singleton* secara langsung

Buat *file* baru bernama `coba1.py` di salinan folder `studi-kasus` (sejajar dengan `pengaturan.py`), isi dengan kode berikut, lalu jalankan `python coba1.py`:

```python
from pengaturan import PengaturanKedai

pengaturan = PengaturanKedai.get_instance()
pengaturan_lain = PengaturanKedai()
```

Pesan *error*-nya (Python 3.13):

```text
Traceback (most recent call last):
  File "coba1.py", line 4, in <module>
    pengaturan_lain = PengaturanKedai()
  File "pengaturan.py", line 20, in __init__
    raise RuntimeError("PengaturanKedai adalah Singleton. "
                       "Gunakan PengaturanKedai.get_instance()")
RuntimeError: PengaturanKedai adalah Singleton. Gunakan PengaturanKedai.get_instance()
```

**Artinya:** penjaga di `__init__` menolak objek kedua. Baca *traceback* dari bawah: jenis *error*-nya `RuntimeError`, dan pesannya sudah memberi tahu solusinya. **Perbaikan:** ganti `PengaturanKedai()` dengan `PengaturanKedai.get_instance()`.

Hati-hati dengan urutan sebaliknya. Jika `liar = PengaturanKedai()` dijalankan **sebelum** `get_instance()` pertama, tidak ada *error* sama sekali, tetapi `liar is PengaturanKedai.get_instance()` bernilai `False`. Dua objek tercipta! Karena itu, jangan pernah memanggil konstruktor *Singleton* secara langsung.

### Kesalahan 2: Pengamat lupa menulis `perbarui()`

Buat *file* baru bernama `coba2.py` di salinan folder `studi-kasus`, isi dengan kode berikut, lalu jalankan `python coba2.py`:

```python
from pengamat import PengamatPesanan


class LayarAntrean(PengamatPesanan):
    def tampilkan(self, pesanan):
        print(f"Nomor {pesanan.nomor} silakan ambil pesanan")


layar = LayarAntrean()
```

Pesan *error*-nya (Python 3.13):

```text
Traceback (most recent call last):
  File "coba2.py", line 9, in <module>
    layar = LayarAntrean()
TypeError: Can't instantiate abstract class LayarAntrean without an implementation for abstract method 'perbarui'
```

**Artinya:** `PengamatPesanan` mewajibkan *method* `perbarui()` (Pertemuan 10). Kelas `LayarAntrean` menamai *method*-nya `tampilkan` sehingga ia masih abstrak dan tidak bisa dibuat objeknya. Untung Python sudah menolaknya saat objek dibuat. Jika tidak, masalahnya baru ketahuan belakangan karena `Pesanan` pasti memanggil `perbarui()`, bukan `tampilkan()`. **Perbaikan:** ganti nama *method* menjadi `perbarui`. Di Python 3.10 dan 3.11, bunyinya sedikit berbeda: `Can't instantiate abstract class LayarAntrean with abstract method perbarui`.

### Kesalahan 3: Impor melingkar

Misalkan kamu ingin "merapikan" `pengamat.py` dengan memberi petunjuk tipe. Di salinan folder `studi-kasus`, buka `pengamat.py`, tambahkan baris `from pesanan import Pesanan` tepat di bawah baris `from abc import ABC, abstractmethod`, lalu ubah `def perbarui(self, pesanan):` menjadi `def perbarui(self, pesanan: Pesanan):`. Simpan, lalu jalankan `python main.py`. Di Python 3.10 sampai 3.12, hasilnya:

```text
Traceback (most recent call last):
  File "main.py", line 16, in <module>
    from kedai import Kedai
  File "kedai.py", line 15, in <module>
    from penyimpanan import PenyimpananPesanan
  File "penyimpanan.py", line 15, in <module>
    from pesanan import Pesanan
  File "pesanan.py", line 22, in <module>
    from pengamat import PengamatPesanan
  File "pengamat.py", line 12, in <module>
    from pesanan import Pesanan
ImportError: cannot import name 'Pesanan' from partially initialized module 'pesanan' (most likely due to a circular import) (pesanan.py)
```

**Artinya:** baca rantainya dari atas. `pesanan.py` mulai dimuat, di tengah jalan ia meng-*import* `pengamat.py`, lalu `pengamat.py` meminta `Pesanan` dari `pesanan.py` yang **belum selesai** dimuat (*partially initialized*). Kelas `Pesanan` belum ada, maka gagal. **Perbaikan:** hapus impor itu dan biarkan parameter `pesanan` tanpa petunjuk tipe, seperti aslinya.

Mulai Python 3.13 (termasuk 3.14 dan 3.15), baris terakhirnya berbeda, dan sayangnya kurang membantu:

```text
ImportError: cannot import name 'Pesanan' from 'pesanan' (consider renaming 'pesanan.py' if it has the same name as a library you intended to import)
```

Pesan itu menyarankan mengganti nama *file*. Jika kamu melihatnya padahal tidak ada pustaka bernama `pesanan`, curigai impor melingkar dan periksa rantai `import` di atasnya.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Python, seperti terlihat di Kesalahan 2 dan 3. Di Python 3.11 dan 3.12, *traceback* juga bisa memuat baris berisi tanda `^^^^` yang menunjuk bagian kode penyebab *error*. Fokuslah pada **jenis *error*** (`RuntimeError`, `TypeError`, `ImportError`) dan kata-kata kunci di dalamnya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| *Singleton*: tempat objek | atribut kelas | `_instance = None` |
| *Singleton*: pintu masuk | `@classmethod` | `def get_instance(cls): ...` |
| *Singleton*: penjaga | `raise` di `__init__` | `if Kelas._instance is not None: raise RuntimeError(...)` |
| *Singleton* ala modul | objek tingkat modul | `pencatat = PencatatLog()` |
| *Singleton* lewat `__new__` | *override* `__new__` | `cls._instance = super().__new__(cls)` |
| *Simple Factory* | `@staticmethod` + `if` | `KendaraanFactory.buat("motor")` |
| *Factory Method* | *method* abstrak pembuat produk | `def buat_angkutan(self) -> Angkutan:` |
| *Strategy*: kontrak | kelas `ABC` | `class StrategiOngkir(ABC):` |
| *Strategy*: tukar | simpan di atribut | `paket.atur_strategi(OngkirKilat())` |
| *Observer*: daftar pengamat | *list* | `self._daftar_pengamat.append(pengamat)` |
| *Observer*: beri kabar | perulangan memanggil *method* | `for p in self._daftar_pengamat: p.perbarui(self)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
