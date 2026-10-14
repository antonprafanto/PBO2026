# 🐍 Praktik Python Pertemuan 15: Proyek Terintegrasi

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 15](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Menulis dan Membaca *File* Teks](#1-menulis-dan-membaca-file-teks)
2. [*File* CSV dengan Modul `csv`](#2-file-csv-dengan-modul-csv)
3. [`with`: Membuka dan Menutup dengan Aman](#3-with-membuka-dan-menutup-dengan-aman)
4. [*Package* dan Impor Absolut](#4-package-dan-impor-absolut)
5. [*Unit Test* dengan `unittest`](#5-unit-test-dengan-unittest)
6. [Validasi *Input* dan Akhir *Input*](#6-validasi-input-dan-akhir-input)
7. [Studi Kasus KedaiKita](#7-studi-kasus-kedaikita)
8. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#8-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/                  <- 6 contoh kecil
│   └── perpustakaan/        <- package mini untuk contoh 04
├── studi-kasus/             <- aplikasi kasir KedaiKita
│   ├── main.py              <- pintu masuk aplikasi
│   ├── kedaikita/           <- package berisi semua kelas (21 file)
│   ├── data/menu_awal.csv   <- data menu awal
│   └── tests/               <- unit test
└── solusi/                  <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara Menjalankan Contoh

Contoh 01 sampai 06, juga setiap *file* di folder `solusi/`, dijalankan sebagai satu *file*. Pilih salah satu cara berikut. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-15-Proyek-Terintegrasi/python`. Di panel **Explorer**, buka folder `contoh`, klik *file* yang ingin dicoba (misalnya `contoh01_baca_tulis_teks.py`), lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-15-Proyek-Terintegrasi/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_baca_tulis_teks.py
```

Yang tercetak di terminal sama persis dengan blok ***Output:*** di bagian 1. *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Semua contoh menulis *file* ke **folder sementara** yang dihapus otomatis, jadi tidak ada *file* sampah yang tertinggal. Folder `__pycache__` yang muncul setelah program dijalankan boleh diabaikan; Git sudah diatur untuk mengabaikannya.

### Cara Menjalankan Studi Kasus

Studi kasus pertemuan ini adalah **proyek ber-*package***: banyak *file* yang bekerja sama. Ingat tiga hal berikut.

1. **Pintu masuknya selalu `main.py`.** *File* di dalam folder `kedaikita/` dan `tests/` tidak dijalankan sendiri.
2. **Semua perintah diketik dari folder `studi-kasus`.** Cara tercepat: di panel **Explorer** VS Code, klik kanan folder `studi-kasus`, lalu pilih **Open in Integrated Terminal**. Dari folder utama materi, ketik `cd Pertemuan-15-Proyek-Terintegrasi/python/studi-kasus`.
3. **Pilih perintah sesuai tujuanmu** (di macOS/Linux, ganti `python` dengan `python3`):

| Tujuan | Ketik | Yang terjadi |
|---|---|---|
| Mode demo | `python main.py --demo` | berjalan sendiri tanpa perlu mengetik apa pun; hasilnya selalu sama |
| Mode interaktif | `python main.py` | kamu menjadi kasir; pilih `0` untuk menyimpan dan keluar (panduannya di bagian 7.8) |
| Menjalankan *unit test* | `python -m unittest discover -s tests -v` | 16 *test* dijalankan; baris terakhir `OK` berarti semua lulus (bagian 7.10) |

**Bagaimana dengan tombol ▷?** Jika yang sedang terbuka adalah `main.py`, tombol ▷ (**Run Python File**) menjalankan **mode interaktif**, dan kamu mengetik jawaban di panel **TERMINAL**. Tombol itu tidak bisa menambahkan `--demo`, jadi mode demo dan *unit test* dijalankan lewat terminal. Jangan menekan ▷ saat yang terbuka adalah *file* di dalam `kedaikita/` atau `tests/`: biasanya muncul `ModuleNotFoundError` (lihat Kesalahan 1 di bagian 8).

**Di mana data disimpan?** Semua *file* data ada di folder `studi-kasus/data/`:

| *File* | Dibuat oleh | Keterangan |
|---|---|---|
| `menu_awal.csv` | sudah ada sejak awal | data menu awal; **jangan dihapus** |
| `menu.csv` | mode interaktif, saat keluar | stok terbaru; dibaca lagi saat aplikasi dibuka |
| `transaksi.csv` | mode interaktif, setiap pesanan LUNAS | riwayat transaksi |
| `demo-menu.csv`, `demo-transaksi.csv` | mode demo | ditulis ulang dari awal setiap kali mode demo dijalankan |

**Ingin mulai lagi dari stok awal?** Tutup aplikasinya, lalu hapus `menu.csv` dan `transaksi.csv`, misalnya lewat klik kanan di panel **Explorer** VS Code lalu **Delete**. Lewat terminal di folder `studi-kasus`, ketik `del data\menu.csv` lalu `del data\transaksi.csv` (Windows), atau `rm data/menu.csv data/transaksi.csv` (macOS/Linux). Saat dibuka lagi, aplikasi kembali memuat `menu_awal.csv`. Semua *file* hasil aplikasi itu sudah diatur agar diabaikan Git sehingga tidak mengganggu `git pull`.

### Tempat Menyimpan Kodemu Sendiri

Anggap folder materi sebagai buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Simpan kode buatanmu sendiri (hasil mengetik ulang, percobaan "Coba sendiri", dan jawaban latihan) di folder lain **di luar** folder materi, misalnya:

```text
Documents/
├── PBO2026/                          <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/                 <- milikmu sendiri
    └── pertemuan-15/                 <- kode pertemuan ini
        ├── contoh02_csv.py           <- salinan contoh yang ingin diubah
        └── studi-kasus/              <- salinan UTUH folder studi-kasus
```

Jika sebuah "Coba sendiri" memintamu mengubah *file* contoh, salin dulu *file* itu ke folder `pertemuan-15` (lewat File Explorer di Windows atau Finder di macOS), lalu ubah salinannya. Untuk studi kasus, salin **seluruh** folder `studi-kasus`, bukan satu *file* saja, karena `main.py`, `kedaikita/`, `data/`, dan `tests/` saling membutuhkan. Buka folder `pertemuan-15` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**), atau arahkan terminal ke sana dengan `cd`. Alasannya ada di [Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Kode yang ditampilkan biasanya **potongan** *file* itu: komentar pembuka, baris `import`, dan dua baris penutup (`if __name__ == "__main__":` lalu `main()`) tidak ditulis ulang. Untuk mencoba, jalankan *file*-nya, jangan hanya menyalin potongannya.
- Tanda `# [1]`, `# [2]`, dan seterusnya di dalam kode dijelaskan satu per satu di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan. Blok yang diperkenalkan dengan kata lain (misalnya "Hasilnya kira-kira seperti berikut") bisa sedikit berbeda di komputermu.

## 1. Menulis dan Membaca *File* Teks

*File*: [`contoh/contoh01_baca_tulis_teks.py`](contoh/contoh01_baca_tulis_teks.py)

Fungsi bawaan `open()` membuka *file* dan mengembalikan objek *file*. Argumen keduanya, **mode**, menentukan apa yang boleh dilakukan. Berikut potongan *file*-nya, yaitu fungsi `main()` sampai langkah 4:

```python
def main():
    with tempfile.TemporaryDirectory() as folder:  # [1] folder sementara
        path = Path(folder) / "jadwal-piket.txt"  # [2] menyusun path dengan /

        print("=== 1. MENULIS FILE BARU ===")
        with open(path, "w", encoding="utf-8") as berkas:  # [3]
            berkas.write("Senin: Ayu\n")  # [4] write tidak menambah baris baru
            berkas.write("Selasa: Bima\n")
        print(f"File {path.name} sudah ada? {'ya' if path.exists() else 'tidak'}")

        print()
        print("=== 2. MENAMBAH DI AKHIR FILE ===")
        with open(path, "a", encoding="utf-8") as berkas:
            berkas.write("Rabu: Citra\n")
        print("Satu baris ditambahkan di akhir file")

        print()
        print("=== 3. MEMBACA SELURUH ISI ===")
        with open(path, encoding="utf-8") as berkas:
            isi = berkas.read()  # [5] seluruh isi file sebagai satu str
        print(isi, end="")  # isi sudah diakhiri "\n", jadi print tidak menambah lagi

        print()
        print("=== 4. MEMBACA BARIS DEMI BARIS ===")
        with open(path, encoding="utf-8") as berkas:
            for nomor, baris in enumerate(berkas, start=1):  # [6]
                hari, nama = baris.strip().split(": ")  # [7] buang "\n" dulu
                print(f"{nomor}. {nama} piket hari {hari}")
```

Langkah 5 dan 6 (lihat *file* lengkapnya) menimpa isi *file* dengan mode `"w"` lalu mencoba membuka *file* yang tidak ada.

***Output:***

```text
=== 1. MENULIS FILE BARU ===
File jadwal-piket.txt sudah ada? ya

=== 2. MENAMBAH DI AKHIR FILE ===
Satu baris ditambahkan di akhir file

=== 3. MEMBACA SELURUH ISI ===
Senin: Ayu
Selasa: Bima
Rabu: Citra

=== 4. MEMBACA BARIS DEMI BARIS ===
1. Ayu piket hari Senin
2. Bima piket hari Selasa
3. Citra piket hari Rabu

=== 5. MENIMPA ISI FILE ===
Kamis: Dimas

=== 6. MEMBACA FILE YANG TIDAK ADA ===
File jadwal-lama.txt tidak ditemukan, lanjut dengan data kosong

Folder sementara sudah dihapus? ya
```

Penjelasan:

- **[1]** `tempfile.TemporaryDirectory()` membuat folder sementara, lalu **menghapusnya beserta isinya** begitu blok `with` selesai. Cocok untuk contoh dan *unit test*.
- **[2]** `Path` dari modul `pathlib` mewakili alamat *file*. Operator `/` menyambung folder dan nama *file* dengan pemisah yang benar di Windows maupun macOS/Linux.
- **[3]** `open(path, "w", encoding="utf-8")` membuka *file* untuk ditulis. Blok `with` menutupnya otomatis (bagian 3).
- **[4]** `write()` menulis teks apa adanya, tanpa ganti baris otomatis. Karena itu, kita menulis `"\n"` sendiri.
- **[5]** `read()` mengembalikan **seluruh** isi *file* sebagai satu `str`.
- **[6]** Objek *file* bisa langsung di-*loop*: setiap putaran menghasilkan satu baris **lengkap dengan** `"\n"`-nya.
- **[7]** `strip()` membuang `"\n"` di ujung baris sebelum dipecah dengan `split(": ")`.
- **[8]** (langkah 5) `path.read_text(encoding="utf-8")` membuka, membaca semua, lalu menutup *file* dalam satu langkah.
- **[9]** (langkah 6) Membaca *file* yang tidak ada melempar `FileNotFoundError` (turunan `OSError`). Tangkap jika memang bisa ditangani, misalnya dengan memakai data kosong.
- **[10]** Setelah blok `with tempfile...` selesai, folder sementara sudah hilang.

| Mode | Arti | Jika *file* belum ada | Jika *file* sudah ada |
|---|---|---|---|
| `"r"` (bawaan) | membaca | `FileNotFoundError` | dibaca dari awal |
| `"w"` | menulis | dibuat baru | **isi lama dihapus**, lalu ditulis ulang |
| `"a"` | menambah (*append*) | dibuat baru | tulisan ditambahkan di akhir |

> [!WARNING]
> Selalu tulis `encoding="utf-8"`. Tanpa itu, Python 3.14 ke bawah memakai *encoding* bawaan sistem operasi. Di banyak komputer Windows, *encoding* bawaannya `cp1252` sehingga teks UTF-8 `Café` terbaca sebagai `CafÃ©`, atau malah memunculkan `UnicodeDecodeError`. Mulai Python 3.15, bawaannya sudah UTF-8, tetapi tetap tulis `encoding="utf-8"` agar programmu benar di semua versi.

> [!TIP]
> **Coba sendiri:** salin `contoh01_baca_tulis_teks.py` ke folder `pertemuan-15` milikmu (lihat Persiapan). Di salinannya, ubah baris `with open(path, "a", encoding="utf-8") as berkas:` di langkah 2 menjadi `with open(path, "w", encoding="utf-8") as berkas:`. Simpan, jalankan, lalu perhatikan apa yang tercetak di langkah 3.

<details>
<summary>Lihat jawaban</summary>

Hanya `Rabu: Citra`. Mode `"w"` menghapus isi lama (Senin dan Selasa) sebelum menulis sehingga langkah 4 pun hanya mencetak `1. Citra piket hari Rabu`.

</details>

## 2. *File* CSV dengan Modul `csv`

*File*: [`contoh/contoh02_csv.py`](contoh/contoh02_csv.py)

Contoh ini menyimpan tiga objek `Mahasiswa(nim, nama, asal, sks, catatan)` ke *file* CSV, lalu memuatnya kembali. Kolom `asal` sengaja berisi koma (`Samarinda, Kaltim`), dan catatan Bima sengaja kosong. Pemisah kolomnya `PEMISAH = ";"`. Berikut potongan *file*-nya (dua *method* kelas `Mahasiswa`, lalu fungsi `simpan()` dan `muat()`):

```python
    def ke_kolom(self) -> list[str]:  # [1] objek -> list teks (satu baris)
        return [self.nim, self.nama, self.asal, str(self.sks), self.catatan]

    @staticmethod
    def dari_kolom(kolom: list[str]) -> "Mahasiswa":  # [2] list teks -> objek
        nim, nama, asal, teks_sks, catatan = kolom
        return Mahasiswa(nim, nama, asal, int(teks_sks), catatan)


def simpan(path: Path, daftar: list[Mahasiswa]):
    with open(path, "w", encoding="utf-8", newline="") as berkas:
        penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")  # [3]
        penulis.writerow(JUDUL_KOLOM)  # baris pertama: judul kolom
        for mhs in daftar:
            penulis.writerow(mhs.ke_kolom())


def muat(path: Path) -> list[Mahasiswa]:
    hasil = []
    with open(path, encoding="utf-8", newline="") as berkas:
        pembaca = csv.reader(berkas, delimiter=PEMISAH)  # [4]
        next(pembaca)  # [5] lewati baris judul kolom
        for nomor_baris, kolom in enumerate(pembaca, start=2):
            try:
                hasil.append(Mahasiswa.dari_kolom(kolom))
            except ValueError:  # [6] jumlah kolom salah atau sks bukan angka
                print(f"  Baris {nomor_baris} dilewati: data tidak valid")
    return hasil
```

***Output:***

```text
=== 1. MENYIMPAN 3 OBJEK KE CSV ===
Tersimpan di mahasiswa.csv

=== 2. ISI FILE APA ADANYA ===
nim;nama;asal;sks;catatan
2409106001;Ayu Lestari;Samarinda, Kaltim;20;ketua kelas
2409106002;Bima Saputra;Balikpapan, Kaltim;18;
2409106003;Citra Dewi;Tenggarong, Kukar;22;asisten lab

=== 3. MEMUAT KEMBALI MENJADI OBJEK ===
Ayu Lestari   Samarinda, Kaltim    20 sks  (ketua kelas)
Bima Saputra  Balikpapan, Kaltim   18 sks  (-)
Citra Dewi    Tenggarong, Kukar    22 sks  (asisten lab)
Total 3 mahasiswa, 60 sks

=== 4. FILE DENGAN BARIS RUSAK ===
  Baris 5 dilewati: data tidak valid
  Baris 6 dilewati: data tidak valid
Berhasil dimuat: 3 mahasiswa
```

Penjelasan:

- **[1]** `ke_kolom()` menerjemahkan objek menjadi daftar teks. *File* hanya menyimpan teks, jadi `sks` diubah dengan `str()`.
- **[2]** `dari_kolom()` adalah kebalikannya. Ia dibuat `@staticmethod` karena tugasnya **membuat** objek baru (ingat "konstruktor alternatif" di Pertemuan 03).
- **[3]** `csv.writer` mengubah *list* menjadi satu baris CSV. `delimiter` adalah pemisah kolom, dan `lineterminator="\n"` membuat isi *file* sama persis di semua sistem operasi.
- **[4]** `csv.reader` menghasilkan ***list* teks** untuk setiap baris *file*.
- **[5]** `next(pembaca)` mengambil satu baris (judul kolom) tanpa memakainya.
- **[6]** Langkah 4 menambahkan dua baris rusak: `sks` berisi `dua puluh` (`int()` melempar `ValueError`) dan baris yang kolomnya kurang (pembongkaran `nim, nama, ... = kolom` juga melempar `ValueError`). Program tidak berhenti; baris rusak dilewati dengan pesan bernomor baris.

> [!NOTE]
> Dokumentasi modul `csv` menganjurkan `newline=""` saat membuka *file* CSV agar ganti baris tidak diterjemahkan dua kali (di Windows hal itu memunculkan baris kosong tambahan). Kolom kosong milik Bima tertulis `18;` di *file* dan terbaca kembali sebagai teks kosong `""`.

> [!TIP]
> **Coba sendiri:** salin `contoh02_csv.py` ke folder `pertemuan-15` milikmu. Di salinannya, ubah baris `PEMISAH = ";"` menjadi `PEMISAH = ","`, simpan, lalu jalankan. Lihat langkah 2: bagaimana asal `Samarinda, Kaltim` disimpan?

<details>
<summary>Lihat jawaban</summary>

Baris Ayu menjadi `2409106001,Ayu Lestari,"Samarinda, Kaltim",20,ketua kelas`. Modul `csv` membungkus isi kolom yang mengandung pemisah dengan tanda kutip, lalu membuangnya lagi saat membaca. Namun, program lain (misalnya versi Java KedaiKita yang memakai `split`) belum tentu sepintar itu. Karena itu, KedaiKita tetap memakai titik koma.

</details>

## 3. `with`: Membuka dan Menutup dengan Aman

*File*: [`contoh/contoh03_with_aman.py`](contoh/contoh03_with_aman.py)

Agar kita bisa **melihat** kapan sumber daya dibuka dan ditutup, contoh ini memakai kelas buatan sendiri yang mencetak pesan di setiap langkah. Berikut kelasnya, disalin utuh dari *file* itu:

```python
class SambunganPrinter:
    """Sumber daya pura-pura: setelah dibuka, wajib ditutup lagi."""

    def __init__(self, nama: str):
        self._nama = nama

    def __enter__(self) -> "SambunganPrinter":  # [1] saat masuk blok with
        print(f"  [{self._nama}] sambungan dibuka")
        return self  # objek inilah yang diterima variabel setelah "as"

    def __exit__(self, jenis_error, error, jejak) -> bool:  # [2] SELALU dipanggil
        print(f"  [{self._nama}] sambungan ditutup")
        return False  # [3] False: error (jika ada) tetap diteruskan ke luar

    def cetak(self, halaman: str):
        if halaman == "":
            raise ValueError("Halaman kosong tidak bisa dicetak")
        print(f"  [{self._nama}] mencetak {halaman}")
```

Program utamanya mencoba empat situasi. Situasi terpenting adalah *error* di tengah blok (potongan dari fungsi `main()`):

```python
    try:
        with SambunganPrinter("Printer Lab") as printer:
            printer.cetak("Halaman 1")
            printer.cetak("")  # [4] melempar ValueError
            printer.cetak("Halaman 3")  # tidak pernah dijalankan
    except ValueError as e:
        print(f"Error ditangkap: {e}")  # [5] sambungan SUDAH ditutup di sini
```

***Output:***

```text
=== 1. BLOK SELESAI TANPA ERROR ===
  [Printer Lab] sambungan dibuka
  [Printer Lab] mencetak Laporan Praktikum
  [Printer Lab] sambungan ditutup
Setelah blok selesai

=== 2. ERROR DI TENGAH BLOK ===
  [Printer Lab] sambungan dibuka
  [Printer Lab] mencetak Halaman 1
  [Printer Lab] sambungan ditutup
Error ditangkap: Halaman kosong tidak bisa dicetak

=== 3. DUA SUMBER DAYA SEKALIGUS ===
  [Printer A] sambungan dibuka
  [Printer B] sambungan dibuka
  [Printer A] mencetak Sampul
  [Printer B] mencetak Isi
  [Printer B] sambungan ditutup
  [Printer A] sambungan ditutup
Ditutup dengan urutan terbalik: yang terakhir dibuka, pertama ditutup

=== 4. MENULIS DAN MEMBACA FILE ===
Hadir: Ayu
Hadir: Bima
Hadir: Citra
```

Penjelasan:

- **[1]** Objek yang bisa dipakai dengan `with` disebut ***context manager***. `__enter__()` dijalankan saat masuk blok, dan nilai kembaliannya diterima variabel setelah `as`.
- **[2]** `__exit__()` dijalankan **selalu** saat keluar dari blok, baik normal maupun karena *exception*. Tiga parameternya berisi informasi *exception* (semuanya `None` jika tidak ada *error*).
- **[3]** `return False` berarti "sumber daya sudah kubereskan, tetapi *error*-nya jangan ditelan".
- **[4]** Setelah `cetak("")` melempar `ValueError`, sisa blok **tidak** dijalankan.
- **[5]** Urutan *output* membuktikan bahwa sambungan **sudah ditutup** sebelum `except` berjalan. Situasi 3 (`with A as a, B as b:`) menunjukkan bahwa beberapa sumber daya ditutup dengan urutan terbalik.

Objek *file* dari `open()` juga *context manager*: `__exit__()`-nya menutup *file*. Jadi `with open(path, encoding="utf-8") as berkas:` setara dengan `berkas = open(...)` lalu `try: ... finally: berkas.close()`, hanya jauh lebih ringkas dan tidak mungkin lupa menutup.

> [!TIP]
> **Coba sendiri:** salin `contoh03_with_aman.py` ke folder `pertemuan-15` milikmu. Di salinannya, ubah `return False` di dalam `__exit__()` menjadi `return True`, simpan, lalu jalankan. Apa yang berubah pada situasi 2?

<details>
<summary>Lihat jawaban</summary>

Baris `Error ditangkap: ...` hilang. Jika `__exit__()` mengembalikan `True`, *exception* dianggap sudah ditangani dan **ditelan diam-diam**. Karena itu, `__exit__()` pada umumnya mengembalikan `False`: menelan *error* diam-diam adalah kebiasaan buruk (Pertemuan 11).

</details>

## 4. *Package* dan Impor Absolut

*File*: [`contoh/contoh04_paket_mini.py`](contoh/contoh04_paket_mini.py) dan folder [`contoh/perpustakaan/`](contoh/perpustakaan/__init__.py)

Kelas-kelas contoh ini tidak ditulis di *file* yang dijalankan, tetapi di dalam *package* `perpustakaan`:

```text
contoh/
├── contoh04_paket_mini.py     <- file yang dijalankan
└── perpustakaan/              <- PACKAGE (folder berisi __init__.py)
    ├── __init__.py            <- penanda package (isinya cukup docstring)
    ├── pengecualian.py        <- PerpustakaanError dan turunannya
    ├── buku.py                <- kelas Buku
    └── katalog.py             <- kelas Katalog
```

Modul `perpustakaan/katalog.py` meng-*import* modul lain di *package* yang sama. Berikut potongan awal *file* itu:

```python
from perpustakaan.buku import Buku  # impor absolut: diawali nama package
from perpustakaan.pengecualian import BukuTidakDitemukanError


class Katalog:
    """Daftar buku perpustakaan, dicari berdasarkan kode."""

    def __init__(self):
        self._daftar: dict[str, Buku] = {}  # kode -> Buku

    def tambah(self, buku: Buku):
        self._daftar[buku.kode] = buku
```

*Method* `cari(kode)` di bawahnya melempar `BukuTidakDitemukanError` jika kodenya tidak terdaftar.

*File* yang dijalankan cukup meng-*import* apa yang dibutuhkan, misalnya `from perpustakaan.katalog import Katalog` **[1]**, lalu memakainya (potongan dari `contoh04_paket_mini.py`):

```python
    for kode in ["B02", "B02", "B09"]:  # [2] pinjam B02 dua kali, lalu kode asal
        try:
            buku = katalog.cari(kode)
            buku.pinjam()
            print(f"{kode}: berhasil dipinjam")
        except PerpustakaanError as e:  # [3] menangkap semua error milik package
            print(f"{kode}: gagal, {e}")
```

***Output:***

```text
=== KATALOG PERPUSTAKAAN MINI ===
[B01] Laskar Pelangi - Andrea Hirata (tersedia)
[B02] Bumi Manusia - Pramoedya Ananta Toer (tersedia)
[B03] Negeri 5 Menara - Ahmad Fuadi (tersedia)

=== MEMINJAM BUKU ===
B02: berhasil dipinjam
B02: gagal, buku 'Bumi Manusia' sedang dipinjam
B09: gagal, buku dengan kode B09 tidak ditemukan

=== KATALOG SETELAH PEMINJAMAN ===
[B01] Laskar Pelangi - Andrea Hirata (tersedia)
[B02] Bumi Manusia - Pramoedya Ananta Toer (dipinjam)
[B03] Negeri 5 Menara - Ahmad Fuadi (tersedia)
```

Penjelasan:

- **[1]** `from package.modul import Kelas` disebut **impor absolut**: alamatnya ditulis lengkap mulai dari nama *package*.
- **[2]** Peminjaman kedua B02 gagal karena bukunya sedang dipinjam, sedangkan B09 tidak terdaftar.
- **[3]** Kedua *error* adalah turunan `PerpustakaanError`, jadi cukup ditangkap sekali. KedaiKita memakai pola yang sama dengan `KedaiError`.

**Bagaimana Python menemukan `perpustakaan`?** Saat kamu menjalankan `python contoh04_paket_mini.py`, Python menambahkan **folder milik *file* yang dijalankan** ke daftar tempat pencarian modul (`sys.path`). Folder `perpustakaan/` ada di sana, jadi langsung ditemukan. Itulah sebabnya `main.py` KedaiKita diletakkan **di luar** folder `kedaikita/`, bersebelahan dengannya.

> [!NOTE]
> `__init__.py` menandai folder sebagai *package* biasa (*regular package*). Kodenya dijalankan sekali saat *package* pertama kali di-*import*; di sini isinya cukup *docstring*. Sejak Python 3.3, folder tanpa `__init__.py` pun masih bisa di-*import* (*namespace package*), tetapi tetap tuliskan `__init__.py` agar maksudmu jelas. Python juga mengenal impor relatif (`from .buku import Buku`); materi ini memakai impor absolut karena alamatnya lebih jelas.

> [!TIP]
> **Coba sendiri:** salin `contoh04_paket_mini.py` **beserta** folder `perpustakaan/` ke folder `pertemuan-15` milikmu (tanpa folder itu, `import`-nya gagal). Di salinan `contoh04_paket_mini.py`, tambahkan baris `print(Buku.__module__)` sebagai baris pertama di dalam `main()`, simpan, lalu jalankan. Apa yang tercetak paling atas?

<details>
<summary>Lihat jawaban</summary>

`perpustakaan.buku`, yaitu nama lengkap modul tempat kelas `Buku` ditulis.

</details>

## 5. *Unit Test* dengan `unittest`

*File*: [`contoh/contoh05_unit_test_mini.py`](contoh/contoh05_unit_test_mini.py)

Kelas yang diuji adalah `KeranjangBelanja`: gratis ongkir jika belanja **minimal** Rp100.000, selain itu ongkir Rp10.000. Ada juga `KeranjangBerbug` yang sengaja diberi *bug*: *method* `ongkir()`-nya memakai `self.subtotal() > BATAS_GRATIS_ONGKIR`, padahal seharusnya `>=`. Berikut potongan kelas ujinya:

```python
class UjiKeranjang(unittest.TestCase):
    """Kumpulan test untuk KeranjangBelanja."""

    def setUp(self):  # [1] dijalankan ulang sebelum SETIAP test
        self.keranjang = KeranjangBelanja()

    def test_jumlah_nol_ditolak(self):
        """Jumlah barang 0 ditolak"""
        with self.assertRaises(ValueError):  # [2] lulus jika ValueError dilempar
            self.keranjang.tambah("Buku tulis", 5000, 0)

    def test_ongkir_di_bawah_batas(self):
        """Belanja Rp99.000 kena ongkir Rp10.000"""
        self.keranjang.tambah("Kaos", 99000, 1)
        self.assertEqual(self.keranjang.ongkir(), 10000)  # [3] hasil, harapan

    def test_ongkir_gratis_tepat_di_batas(self):
        """Belanja tepat Rp100.000 gratis ongkir"""
        self.keranjang.tambah("Sepatu", 100000, 1)
        self.assertEqual(self.keranjang.ongkir(), 0)
```

Dua *test* lainnya (`test_subtotal_dua_barang` dan `test_total_termasuk_ongkir`) ditulis dengan pola yang sama. Lalu, untuk menguji versi berbug **tanpa menulis ulang *test***, kita memakai pewarisan:

```python
class UjiKeranjangBerbug(UjiKeranjang):
    """Test yang SAMA (diwarisi), tetapi dijalankan pada KeranjangBerbug."""

    def setUp(self):  # [4] hanya cara membuat objeknya yang diganti
        self.keranjang = KeranjangBerbug()
```

Biasanya *test* dijalankan dari terminal (lihat bagian 7.10). Di contoh ini, *test* dijalankan dari dalam program dengan pencatat hasil buatan sendiri agar *output*-nya tidak memuat catatan waktu:

```python
class HasilRingkas(unittest.TestResult):
    """Pencatat hasil buatan sendiri: satu baris per test, tanpa waktu."""

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"[LULUS] {test.shortDescription()}")  # [5] baris pertama docstring

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"[GAGAL] {test.shortDescription()}")
        print(f"        -> {err[1]}")  # [6] pesan dari assertEqual
```

Fungsi `jalankan_uji(kelas_uji)` lalu mengumpulkan *test* dengan `unittest.defaultTestLoader.loadTestsFromTestCase(kelas_uji)` **[7]**, menjalankannya dengan pencatat di atas, dan mencetak jumlah yang lulus dan gagal.

***Output:***

```text
=== UJI 1: KeranjangBelanja ===
[LULUS] Jumlah barang 0 ditolak
[LULUS] Belanja Rp99.000 kena ongkir Rp10.000
[LULUS] Belanja tepat Rp100.000 gratis ongkir
[LULUS] Subtotal dua barang dijumlahkan
[LULUS] Total = subtotal + ongkir
Hasil: 5 lulus, 0 gagal

=== UJI 2: KeranjangBerbug (sengaja diberi bug) ===
[LULUS] Jumlah barang 0 ditolak
[LULUS] Belanja Rp99.000 kena ongkir Rp10.000
[GAGAL] Belanja tepat Rp100.000 gratis ongkir
        -> 10000 != 0
[LULUS] Subtotal dua barang dijumlahkan
[LULUS] Total = subtotal + ongkir
Hasil: 4 lulus, 1 gagal
```

Penjelasan:

- **[1]** `setUp()` dijalankan ulang **sebelum setiap** *test* sehingga setiap *test* mendapat keranjang baru yang kosong dan tidak saling memengaruhi.
- **[2]** `with self.assertRaises(ValueError):` lulus jika kode di dalamnya melempar `ValueError`. Jika tidak ada yang dilempar, *test* gagal dengan pesan `ValueError not raised`.
- **[3]** `assertEqual(a, b)` lulus jika `a == b`. Di materi ini kita menulis **hasil** dulu, lalu **harapan**.
- **[4]** `UjiKeranjangBerbug` mewarisi kelima *test* (Pertemuan 07) dan hanya mengganti `setUp()`.
- **[5]** `shortDescription()` mengambil baris pertama *docstring* *test* sebagai nama yang mudah dibaca.
- **[6]** Saat `assertEqual` gagal, pesannya berbentuk `hasil != harapan`: ongkirnya `10000`, padahal seharusnya `0`. (*Method* `addError()` untuk *exception* tak terduga ditulis dengan pola yang sama.)
- **[7]** `loadTestsFromTestCase()` mengumpulkan semua *method* berawalan `test_`, **diurutkan menurut abjad**.

Hanya *test* **batas** (tepat Rp100.000) yang menangkap *bug* `>` versus `>=`. *Test* dengan Rp99.000 atau Rp150.000 tidak akan pernah menemukannya. Selain `assertEqual` dan `assertRaises`, yang sering dipakai adalah `assertNotEqual(a, b)`, `assertTrue(x)`, `assertFalse(x)`, dan `assertIn(a, b)` (lulus jika `a` ada di dalam `b`).

> [!TIP]
> **Coba sendiri:** salin `contoh05_unit_test_mini.py` ke folder `pertemuan-15` milikmu. Di salinannya, perbaiki *bug* di `KeranjangBerbug`: ubah `if self.subtotal() > BATAS_GRATIS_ONGKIR:` menjadi `if self.subtotal() >= BATAS_GRATIS_ONGKIR:`, simpan, lalu jalankan. Hasil UJI 2 seharusnya menjadi `Hasil: 5 lulus, 0 gagal`.

## 6. Validasi *Input* dan Akhir *Input*

*File*: [`contoh/contoh06_validasi_input.py`](contoh/contoh06_validasi_input.py)

Program yang menunggu ketikan sulit dijadikan contoh yang hasilnya selalu sama. Karena itu, `input()` di contoh ini **digantikan** objek `MasukanPalsu` yang mengambil jawaban dari daftar yang sudah disiapkan, lalu menampilkannya seolah-olah diketik pengguna. Berikut potongan *file*-nya:

```python
class MasukanPalsu:
    """Pengganti input(): jawaban diambil dari daftar yang sudah disiapkan."""

    def __init__(self, daftar_jawaban: list[str]):
        self._sisa = list(daftar_jawaban)

    def baca(self, pertanyaan: str) -> str:
        if not self._sisa:  # [1] jawaban habis = input berakhir
            print(f"{pertanyaan}(input habis)")
            raise EOFError("EOF when reading a line")  # sama seperti input() asli
        jawaban = self._sisa.pop(0)
        # Tampilkan pertanyaan + jawaban seolah-olah diketik pengguna.
        # Jawaban kosong ditampilkan sebagai <Enter> agar terlihat.
        print(f"{pertanyaan}{jawaban if jawaban else '<Enter>'}")
        return jawaban


def tanya_angka(masukan: MasukanPalsu, pertanyaan: str, minimum: int,
                maksimum: int) -> int:
    """Bertanya terus sampai jawabannya angka bulat dari minimum..maksimum."""
    while True:  # [2] ulangi sampai jawabannya valid
        teks = masukan.baca(pertanyaan).strip()
        if teks == "":
            print("  Jawaban tidak boleh kosong.")
            continue
        try:
            angka = int(teks)  # [3] melempar ValueError jika bukan angka
        except ValueError:
            print(f"  '{teks}' bukan angka bulat.")
            continue
        if angka < minimum or angka > maksimum:  # [4] periksa batas
            print(f"  Harus di antara {minimum} dan {maksimum}.")
            continue
        return angka
```

Fungsi `tanya_pilihan()` bekerja dengan cara yang sama untuk pilihan huruf `U`/`M`, setelah jawaban diubah ke huruf besar **[5]**. Program utamanya menjalankan dua skenario: `MasukanPalsu(["", "dua", "9", "2", "x", "m"])` untuk pengguna yang salah ketik beberapa kali, dan `MasukanPalsu(["abc"])` yang jawabannya habis di tengah jalan, dibungkus `try ... except EOFError:` **[6]**.

***Output:***

```text
=== SKENARIO 1: PENGGUNA SALAH KETIK BEBERAPA KALI ===
Jumlah tiket (1-5): <Enter>
  Jawaban tidak boleh kosong.
Jumlah tiket (1-5): dua
  'dua' bukan angka bulat.
Jumlah tiket (1-5): 9
  Harus di antara 1 dan 5.
Jumlah tiket (1-5): 2
Kategori (U=Umum, M=Mahasiswa): x
  Pilihan tersedia: U, M.
Kategori (U=Umum, M=Mahasiswa): m
Pendaftaran berhasil: 2 tiket Mahasiswa, total Rp50000

=== SKENARIO 2: INPUT BERAKHIR DI TENGAH JALAN ===
Jumlah tiket (1-5): abc
  'abc' bukan angka bulat.
Jumlah tiket (1-5): (input habis)
Input berakhir. Pendaftaran dibatalkan.
```

Penjelasan:

- **[1]** Saat jawaban habis, `MasukanPalsu` melempar `EOFError`, persis seperti `input()` asli ketika *input* berakhir.
- **[2]** `while True` baru berhenti lewat `return` saat jawabannya valid. Setiap jawaban salah dibalas pesan yang **menjelaskan masalahnya**, lalu pertanyaan diulang.
- **[3]** `int()` melempar `ValueError` untuk teks seperti `dua`. Kita menggantinya dengan pesan ramah.
- **[4]** Angka yang bentuknya benar tetap diperiksa batasnya: `9` ditolak karena maksimal 5 tiket.
- **[5]** Jawaban `m` diterima sebagai `M`. Pengguna tidak perlu "dihukum" karena huruf kecil.
- **[6]** Akhir *input* bukan kesalahan pengguna. Program menutup urusannya dengan tertib, bukan menampilkan *traceback*.

> [!NOTE]
> Di program interaktif sungguhan, akhir *input* terjadi saat pengguna menekan Ctrl+D (macOS/Linux) atau Ctrl+Z lalu Enter (Windows), atau saat masukan diambil dari *file* dan isinya sudah habis dibaca. Contohnya `python main.py < masukan.txt` di Command Prompt, macOS, atau Linux. PowerShell tidak mengenal tanda `<` ini; di sana, pakai `Get-Content masukan.txt | python main.py`.

## 7. Studi Kasus KedaiKita

Rancangan dan arsitekturnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini). Sekarang kita bedah kodenya. Semua perintah di bagian ini diketik dari folder `studi-kasus` (lihat [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)).

### 7.1 Apa yang Berubah dibanding Pertemuan 14

- Semua modul pindah ke *package* `kedaikita/` (ditambah `__init__.py`). Impor berubah dari `from menu import Menu` menjadi `from kedaikita.menu import Menu`. Selain baris impor itu, kelas-kelas lama **tidak berubah**.
- `pengecualian.py` mendapat *exception* baru, `FormatDataError` (turunan `KedaiError`).
- Tiga modul baru, satu per lapisan: `repositori.py` (penyimpanan: `RepositoriMenuCSV`, `PencatatTransaksiCSV`), `layanan.py` (layanan: `LayananKasir`), dan `aplikasi.py` (tampilan: `AplikasiKasir`).
- Menu dibaca dari `data/menu_awal.csv`. `main.py` kini hanya memilih mode demo atau interaktif.
- Folder `tests/` berisi 16 *unit test*.

### 7.2 `main.py`: Pintu Masuk

*File*: [`studi-kasus/main.py`](studi-kasus/main.py)

Berikut potongan *file*-nya (tanpa komentar pembuka dan baris `import`):

```python
# Folder data dicari relatif terhadap lokasi file ini, sehingga program tetap
# berjalan walaupun dijalankan dari folder lain.
FOLDER_DATA = Path(__file__).resolve().parent / "data"


def main():
    aplikasi = AplikasiKasir(FOLDER_DATA)
    try:
        if "--demo" in sys.argv:
            aplikasi.jalankan_demo()
        else:
            aplikasi.jalankan()
    except (KedaiError, OSError) as e:
        # Lapisan terluar: error tak terduga ditampilkan dengan sopan
        print(f"Terjadi kesalahan: {e}")
        sys.exit(1)
```

- `__file__` berisi alamat *file* `main.py` itu sendiri. `resolve()` menjadikannya alamat lengkap, `parent` mengambil foldernya, lalu `/ "data"` menunjuk folder data di sebelahnya. Jadi `python studi-kasus/main.py --demo` yang diketik dari folder lain pun tetap menemukan datanya.
- `sys.argv` adalah *list* argumen dari terminal: `python main.py --demo` menghasilkan `["main.py", "--demo"]`.
- `except (KedaiError, OSError)` adalah jaring pengaman terakhir. *File* rusak (`FormatDataError`) atau masalah disk (`OSError`) ditampilkan dengan sopan, lalu program keluar dengan kode 1 (tanda gagal).

### 7.3 `RepositoriMenuCSV`: Memuat dan Menyimpan Menu

*File*: [`studi-kasus/kedaikita/repositori.py`](studi-kasus/kedaikita/repositori.py)

*Method* `muat()` membuka *file* dengan `with open(..., encoding="utf-8", newline="")`, melewati baris judul dengan `next(pembaca, None)` (nilai bawaan `None` mencegah *error* jika *file* benar-benar kosong), lalu menyerahkan setiap baris ke `_buat_menu()` beserta nomor barisnya. Kode yang sudah pernah muncul dicatat di sebuah `set` (Pertemuan 12); kode ganda ditolak dengan `FormatDataError("Baris 3: kode M01 sudah dipakai")`. Inti validasinya ada di `_buat_menu()` (potongan):

```python
    @staticmethod
    def _buat_menu(kolom: list[str], nomor_baris: int) -> Menu:
        """Factory kecil: mengubah satu baris CSV menjadi Makanan/Minuman."""
        if len(kolom) != len(KOLOM_MENU):
            raise FormatDataError(f"Baris {nomor_baris}: harus ada "
                                  f"{len(KOLOM_MENU)} kolom")
        jenis, kode, nama, teks_harga, teks_stok, ekstra = kolom
        if jenis not in ("Makanan", "Minuman"):
            raise FormatDataError(f"Baris {nomor_baris}: jenis '{jenis}' tidak dikenal")
        level_pedas = 0  # hanya dipakai oleh Makanan
        try:
            harga = int(teks_harga)
            stok = int(teks_stok)
            if jenis == "Makanan":
                level_pedas = int(ekstra)
        except ValueError:
            raise FormatDataError(f"Baris {nomor_baris}: harga, stok, dan level "
                                  f"pedas harus berupa angka") from None
        try:
            if jenis == "Makanan":
                return Makanan(kode, nama, harga, stok, level_pedas)
            return Minuman(kode, nama, harga, stok, ekstra == "dingin")
        except ValueError as e:  # ditolak validasi Menu, misalnya harga 0
            raise FormatDataError(f"Baris {nomor_baris}: {e}") from None
```

- `_buat_menu()` adalah *factory* kecil: kolom `jenis` menentukan objek `Makanan` atau `Minuman` yang dibuat.
- Semua kegagalan diterjemahkan menjadi `FormatDataError` bernomor baris. `from None` menyembunyikan *exception* asalnya (`ValueError`) agar pesan untuk pengguna tetap bersih (*exception chaining*, Pertemuan 11).
- Aturan harga dan level pedas **tidak** ditulis ulang di sini. Konstruktor `Makanan`/`Minuman` yang menolaknya; repositori hanya menambahkan nomor baris.

Kebalikannya, `simpan()` menulis ulang seluruh *file* dengan `csv.writer`, dan `_ke_kolom()` memakai `isinstance()` untuk mengisi kolom `ekstra`: level pedas untuk `Makanan`, `dingin`/`panas` untuk `Minuman`.

### 7.4 `PencatatTransaksiCSV`: *Observer* yang Menulis *File*

*File*: [`studi-kasus/kedaikita/repositori.py`](studi-kasus/kedaikita/repositori.py) (kelas kedua di *file* itu)

Berikut potongannya, tanpa *method* `baca_semua()`:

```python
class PencatatTransaksiCSV(PengamatPesanan):
    """Observer: mencatat setiap pesanan LUNAS ke file CSV."""

    def __init__(self, path: Path, mulai_baru: bool = False):
        self._path = path
        if mulai_baru or not path.exists():
            with open(path, "w", encoding="utf-8", newline="") as berkas:
                penulis = csv.writer(berkas, delimiter=PEMISAH,
                                     lineterminator="\n")
                penulis.writerow(KOLOM_TRANSAKSI)

    def perbarui(self, pesanan: Pesanan):
        if pesanan.status != "LUNAS":
            return
        porsi = 0
        for item in pesanan.daftar_item:
            porsi += item.jumlah
        baris = [pesanan.nomor, pesanan.pelanggan.nama, pesanan.pelanggan.no_hp,
                 str(porsi), str(pesanan.hitung_total())]
        with open(self._path, "a", encoding="utf-8", newline="") as berkas:
            penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")
            penulis.writerow(baris)
```

- Kelas ini mewarisi `PengamatPesanan`, *interface* *Observer* dari Pertemuan 14, dan mengisi *method* kontraknya, `perbarui()`.
- Konstruktor menulis baris judul jika *file* belum ada, atau jika diminta mulai baru (`mulai_baru=True`, dipakai mode demo).
- `perbarui()` membuka *file* dengan mode `"a"`: setiap pesanan LUNAS **ditambahkan** di akhir tanpa menghapus riwayat lama. *Method* `baca_semua()` membaca riwayat itu kembali.

### 7.5 `LayananKasir`: Otak Alur Kerja

*File*: [`studi-kasus/kedaikita/layanan.py`](studi-kasus/kedaikita/layanan.py)

Berikut tiga *method* intinya (potongan):

```python
    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = self._kedai.buat_pesanan(pelanggan)
        for pengamat in self._daftar_pengamat:
            pesanan.tambah_pengamat(pengamat)
        return pesanan

    def tambah_item(self, pesanan: Pesanan, kode: str, jumlah: int) -> Menu:
        """Menambah item berdasarkan kode menu. Mengembalikan menu tersebut."""
        menu = self._kedai.cari_menu(kode)
        pesanan.tambah_item(menu, jumlah)
        return menu

    def bayar(self, pesanan: Pesanan, jenis: str, nominal: int, bank: str):
        """Membayar memakai PembayaranFactory (pola Factory)."""
        pembayaran = PembayaranFactory.buat(jenis, nominal, bank)
        pesanan.bayar(pembayaran)
```

- Tidak ada satu pun `input()` di sini. Semua *method* menerima data yang **sudah jadi** sehingga bisa dipakai tampilan apa pun dan mudah diuji.
- Daftar pengamat **disuntikkan** lewat konstruktor (DIP, Pertemuan 13), lalu dipasang ke setiap pesanan baru. *Method* `pelanggan(nama, no_hp)` memakai `dict` (no HP → `Pelanggan`) agar pelanggan lama tidak didaftarkan dua kali.
- `bayar()` menerima pilihan berupa teks (`"tunai"`, `"qris"`, `"kartu"`) dan menyerahkan pembuatan objeknya ke `PembayaranFactory`.

### 7.6 `AplikasiKasir`: Mode Demo dan Mode Interaktif

*File*: [`studi-kasus/kedaikita/aplikasi.py`](studi-kasus/kedaikita/aplikasi.py)

Kedua mode memakai persiapan yang sama, yaitu *method* `_siapkan()`: membuat `Kedai`, mengisinya dengan menu hasil `RepositoriMenuCSV(file_menu).muat()`, lalu membuat `LayananKasir(kedai, [pencatat])`. Di sinilah semua lapisan dirakit.

Mode interaktif (`jalankan()`) memuat `data/menu.csv` jika sudah ada (hasil sesi sebelumnya), atau `data/menu_awal.csv` jika belum. Perulangan menu utamanya dibungkus `try ... except EOFError`, dan bagian akhirnya selalu menyimpan stok:

```python
        except EOFError:  # input habis (misalnya saat input dari file)
            print()
            print("Input berakhir.")
        RepositoriMenuCSV(file_menu).simpan(layanan.kedai.semua_menu())
        print(f"Stok terbaru disimpan ke data/{file_menu.name}. Sampai jumpa!")
```

Semua pertanyaan memakai dua *method* bantu di akhir *file* yang sama. `_tanya_angka()` adalah versi sungguhan dari `tanya_angka()` di contoh 06:

```python
    @staticmethod
    def _tanya(pertanyaan: str) -> str:
        return input(pertanyaan).strip()

    def _tanya_angka(self, pertanyaan: str) -> int:
        while True:
            teks = self._tanya(pertanyaan)
            try:
                return int(teks)
            except ValueError:
                print("  Harap isi dengan angka bulat, misalnya 2 atau 50000.")
```

Alur pesanan (`_alur_pesanan`), pilihan diskon (`_pilih_diskon`), dan pembayaran (`_alur_bayar`) memakai pola yang sama: tanya, validasi, ulangi jika salah. Kesalahan dari model (`KedaiError`) ditangkap lalu ditampilkan sebagai `[GAGAL] ...`, dan kasir boleh mencoba lagi.

### 7.7 Menjalankan Mode Demo

Dari folder `studi-kasus`, ketik (macOS/Linux: `python3 main.py --demo`):

```bash
python main.py --demo
```

*Output* diawali `Memuat menu dari data/menu_awal.csv: 6 menu` dan daftar keenam menu, lalu transaksi 1 dan 2 dengan proses pembayaran dan struk lengkap seperti di Pertemuan 14. Berikut cuplikan bagian selanjutnya: *input* keliru, laporan, dan riwayat yang dibaca dari *file*.

***Output:***

```text
--- Transaksi 3: input keliru ditangani dengan rapi ---
  [GAGAL] Menu dengan kode M99 tidak ditemukan
  [GAGAL] Stok Mie Goreng Jawa tidak cukup: diminta 100, tersedia 10
  -> 2 x Kopi Tubruk ditambahkan
Pembayaran pesanan P003 (Rina Marlina)
  Metode       : QRIS
  Total bayar  : Rp26.400
  Saldo e-wallet terpotong Rp26.400, sisa Rp73.600
  Status       : LUNAS (+2 poin)

=== LAPORAN SESI INI ===
========================================
LAPORAN PENJUALAN KEDAIKITA
========================================
Pesanan lunas                          3
Total pendapatan               Rp124.080
----------------------------------------
Menu terlaris:
1. Es Teh Manis (2 porsi)
2. Kopi Susu Gula Aren (2 porsi)
3. Kopi Tubruk (2 porsi)
----------------------------------------
Penjualan per kategori (sebelum diskon & pajak):
Makanan                         Rp40.000
Minuman                         Rp76.000
========================================

=== RIWAYAT DARI FILE data/demo-transaksi.csv ===
P001 | Budi Santoso | 081234567890 | 3 | 67100
P002 | Siti Aminah | 082198765432 | 3 | 30580
P003 | Rina Marlina | 085312345678 | 2 | 26400
```

Tiga baris riwayat itu ditulis oleh `PencatatTransaksiCSV` setiap kali pesanan menjadi LUNAS, lalu dibaca kembali dari *file*. *Output* diakhiri isi `demo-menu.csv` dengan stok terbaru (lihat [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini)). Jalankan sendiri untuk melihat *output* lengkapnya.

### 7.8 Memakai Mode Interaktif

Dari folder `studi-kasus`, jalankan `python main.py` (macOS/Linux: `python3 main.py`), atau buka `main.py` di VS Code lalu klik ▷. Kini kamu menjadi kasirnya. Setiap pertanyaan diakhiri titik dua: ketik jawabanmu di terminal, lalu tekan Enter.

| Pertanyaan | Yang kamu ketik |
|---|---|
| `Pilihan:` (menu utama) | `1` lihat menu, `2` buat pesanan, `3` laporan sesi ini, `4` riwayat dari *file*, `0` simpan dan keluar |
| `Nama pelanggan:` dan `No. HP:` | nama dan nomor HP pelanggan |
| `Kode menu:` | kode seperti `M01` (huruf kecil boleh). Jika semua item sudah dimasukkan, **langsung tekan Enter** tanpa mengetik apa pun. |
| `Jumlah:` | angka bulat, misalnya `2` |
| `Pilihan diskon:` | `1` tanpa diskon, `2` member (baru berlaku jika pelanggan sudah punya minimal 10 poin), `3` *happy hour* (20% untuk minuman) |
| `Pilihan pembayaran:` | `1` tunai (lalu uang diterima), `2` QRIS (lalu saldo *e-wallet*), `3` kartu kredit (lalu nama bank; biaya layanan 2%) |

Pertanyaan pembayaran diulang sampai pesanan LUNAS. Jika uangnya kurang, pilih lagi lalu masukkan nominal yang cukup, atau pilih `3` karena pembayaran kartu kredit di simulasi ini selalu disetujui.

Berikut **ilustrasi** satu sesi. Teks setelah tanda titik dua pada baris pertanyaan adalah **ketikan kasir**; `<Enter>` berarti kasir langsung menekan Enter. Menu utama dan struk disingkat agar ringkas.

```text
Memuat menu dari data/menu_awal.csv: 6 menu
Selamat datang di Kasir KedaiKita!

=========== MENU UTAMA ===========
1. Lihat daftar menu
(... pilihan 2, 3, 4 ...)
0. Simpan dan keluar
Pilihan: 2
Nama pelanggan: Dewi Lestari
No. HP: 081255501234
Masukkan kode menu satu per satu (kosongkan untuk selesai).
  Kode menu: m01
  Jumlah: dua
  Harap isi dengan angka bulat, misalnya 2 atau 50000.
  Jumlah: 2
  -> 2 x Kopi Susu Gula Aren ditambahkan
  Kode menu: M05
  Jumlah: 1
  -> 1 x Pisang Goreng Keju ditambahkan
  Kode menu: <Enter>
Diskon: 1. Tanpa diskon  2. Member  3. Happy Hour
Pilihan diskon: 5
Pilihan tidak dikenal, coba lagi.
Pilihan diskon: 1
(struk dicetak: Status BARU, TOTAL Rp56.100)
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 50000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp56.100
[GAGAL] Pembayaran Tunai gagal: uang kurang Rp6.100
Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit
Pilihan pembayaran: 1
Uang diterima: 100000
Pembayaran pesanan P001 (Dewi Lestari)
  Metode       : Tunai
  Total bayar  : Rp56.100
  Uang diterima Rp100.000, kembalian Rp43.900
  Status       : LUNAS (+5 poin)
(struk dicetak lagi: Status LUNAS)
(menu utama)
Pilihan: 4
P001 | Dewi Lestari | 081255501234 | 3 | 56100
(menu utama)
Pilihan: 0
Stok terbaru disimpan ke data/menu.csv. Sampai jumpa!
```

Setelah sesi ini, folder `data/` berisi `menu.csv` (stok kopi tinggal 18, pisang goreng 11) dan `transaksi.csv` (satu baris P001). Jalankan `python main.py` lagi, dan baris pertamanya menjadi `Memuat menu dari data/menu.csv: 6 menu`. Stok berlanjut dari sesi sebelumnya!

**Cara keluar yang benar:**

- Pilih `0` di menu utama. Stok disimpan ke `data/menu.csv`, lalu aplikasi pamit.
- Jika *input* berakhir di tengah sesi (kamu menekan Ctrl+D di macOS/Linux, atau Ctrl+Z lalu Enter di Windows), aplikasi mencetak `Input berakhir.`, tetap menyimpan stok ke `data/menu.csv`, lalu pamit.
- **Jangan** keluar dengan Ctrl+C. Program berhenti paksa dengan *traceback* `KeyboardInterrupt` sebelum sempat menyimpan stok, padahal pesanan yang sudah LUNAS tetap tercatat di `transaksi.csv`.

> [!WARNING]
> Buat satu pesanan lagi di sesi kedua, lalu lihat riwayatnya (pilihan 4). Nomornya kembali **P001** karena penghitung nomor pesanan mulai dari nol setiap kali aplikasi dibuka. Memperbaikinya adalah [Latihan 3](../latihan.md).

### 7.9 Saat *File* Data Rusak

Percobaan ini dikerjakan di **salinan**. Salin seluruh folder `studi-kasus` ke folder `pertemuan-15` milikmu (lihat Persiapan). Di salinan itu, buat *file* baru `data/menu.csv` (di VS Code: klik kanan folder `data`, pilih **New File**) berisi tiga baris berikut. Harga Es Teh Manis sengaja ditulis `8rb`:

```text
jenis;kode;nama;harga;stok;ekstra
Minuman;M01;Kopi Susu Gula Aren;18000;20;dingin
Minuman;M02;Es Teh Manis;8rb;30;dingin
```

Simpan, lalu jalankan `python main.py` dari folder `studi-kasus` salinan itu. Hasilnya:

```text
Terjadi kesalahan: Baris 3: harga, stok, dan level pedas harus berupa angka
```

Aplikasi berhenti dengan sopan dan menunjuk baris yang rusak, tanpa *traceback* panjang yang membingungkan kasir. Pesan untuk kerusakan lain (kolom kurang, jenis tidak dikenal, kode ganda, harga 0) ada di [tabel halaman konsep](../README.md#46-jangan-percaya-isi-file). Setelah selesai, hapus `data/menu.csv` di salinan itu agar aplikasi kembali memuat `menu_awal.csv`.

### 7.10 *Unit Test* KedaiKita

*File*: [`studi-kasus/tests/test_kedaikita.py`](studi-kasus/tests/test_kedaikita.py)

Berikut potongan kelas `TestPesanan`:

```python
class TestPesanan(unittest.TestCase):
    def setUp(self):
        """Dijalankan ulang sebelum SETIAP test, agar tiap test mulai dari nol."""
        self.kopi = Minuman("M01", "Kopi Susu Gula Aren", 18000, 10)
        self.nasi = Makanan("M03", "Nasi Goreng Kampung", 25000, 10, 2)
        self.pelanggan = Pelanggan("Uji Coba", "080000000000")
        self.pesanan = Pesanan(self.pelanggan)
        self.pesanan.tambah_item(self.kopi, 2)
        self.pesanan.tambah_item(self.nasi, 1)

    def test_subtotal(self):
        self.assertEqual(self.pesanan.hitung_subtotal(), 61000)

    def test_total_sudah_termasuk_pajak_10_persen(self):
        self.assertEqual(self.pesanan.hitung_total(), 67100)
```

*Test* untuk `RepositoriMenuCSV` memakai `tempfile.TemporaryDirectory()` sehingga tidak pernah menyentuh folder `data/` milik aplikasi. Contohnya, `test_file_rusak_ditolak` menulis *file* berisi harga `mahal`, lalu memeriksa bahwa `muat()` melempar `FormatDataError`.

Jalankan semua *test* dari folder `studi-kasus` (macOS/Linux: `python3`):

```bash
python -m unittest discover -s tests -v
```

Hasilnya kira-kira seperti berikut. Catatan waktunya pasti berbeda, dan format nama *test* sedikit berbeda antarversi Python (Python 3.10 hanya menulis `(test_kedaikita.TestMenu)`):

```text
test_harga_harus_positif (test_kedaikita.TestMenu.test_harga_harus_positif) ... ok
test_level_pedas_maksimal_lima (test_kedaikita.TestMenu.test_level_pedas_maksimal_lima) ... ok
test_stok_tidak_berubah_jika_gagal (test_kedaikita.TestMenu.test_stok_tidak_berubah_jika_gagal) ... ok
(13 baris lain untuk test PembayaranFactory, Pesanan, dan RepositoriMenuCSV)

----------------------------------------------------------------------
Ran 16 tests in 0.003s

OK
```

- `discover` mencari *file* berpola `test*.py` di folder yang disebut `-s` (*start directory*), lalu menjalankan setiap *method* berawalan `test_`.
- `-v` (*verbose*) menampilkan satu baris per *test*, diurutkan menurut nama kelas lalu nama *method*.
- Kata di ujung setiap baris adalah hasil *test* itu. Tanpa `-v`, hasilnya ditandai satu karakter saja.

| Hasil (`-v`) | Tanpa `-v` | Artinya |
|---|---|---|
| `ok` | `.` | lulus: semua *assertion* terpenuhi |
| `FAIL` | `F` | gagal: sebuah *assertion* tidak terpenuhi, jadi hasil kodenya berbeda dari harapan |
| `ERROR` | `E` | *test* berhenti karena *exception* lain yang tidak diduga, misalnya salah ketik nama *method* sehingga muncul `AttributeError`; pemeriksaannya belum sempat dilakukan |

- Baris terakhir merangkum semuanya. `OK` berarti semua lulus. Jika tidak, tertulis misalnya `FAILED (failures=2)` atau `FAILED (errors=1)`, dan di atasnya ada laporan untuk setiap *test* yang bermasalah: nama *test*, baris kodenya, dan pesan *error*-nya. Contohnya ada di jawaban "Coba sendiri" di bawah.
- *Test* `test_bayar_gagal_status_tetap_baru` memakai `contextlib.redirect_stdout()` untuk "membisukan" `print()` milik `bayar()` agar hasil pengujian tetap bersih.

> [!TIP]
> **Coba sendiri:** kerjakan di salinan folder `studi-kasus` di folder `pertemuan-15` milikmu. Buka `kedaikita/pengaturan.py` di salinan itu, ubah baris `self._pajak_persen = 10` menjadi `self._pajak_persen = 11`, simpan, lalu jalankan *test* dari folder salinan itu. *Test* mana yang gagal, dan mengapa?

<details>
<summary>Lihat jawaban</summary>

`test_total_sudah_termasuk_pajak_10_persen` gagal dengan pesan `67710 != 67100`, dan `test_struk_memuat_total` gagal karena teks `Rp67.100` tidak ada di struk. Empat belas *test* lain tetap lulus karena tidak bergantung pada pajak. Inilah gunanya *test*: dampak sebuah perubahan langsung ketahuan. Cuplikan hasilnya (dipendekkan):

```text
test_struk_memuat_total (test_kedaikita.TestPesanan.test_struk_memuat_total) ... FAIL
test_subtotal (test_kedaikita.TestPesanan.test_subtotal) ... ok
test_total_sudah_termasuk_pajak_10_persen (test_kedaikita.TestPesanan.test_total_sudah_termasuk_pajak_10_persen) ... FAIL
...
======================================================================
FAIL: test_total_sudah_termasuk_pajak_10_persen (test_kedaikita.TestPesanan.test_total_sudah_termasuk_pajak_10_persen)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "tests/test_kedaikita.py", line 58, in test_total_sudah_termasuk_pajak_10_persen
    self.assertEqual(self.pesanan.hitung_total(), 67100)
AssertionError: 67710 != 67100

----------------------------------------------------------------------
Ran 16 tests in 0.005s

FAILED (failures=2)
```

Baca dari bawah: `failures=2` berarti dua *test* gagal. Laporan `FAIL:` menunjuk baris 58 di *file test*, dan pesan `67710 != 67100` berarti hasil kodenya 67710, padahal *test* mengharapkan 67100.

</details>

### 7.11 Batasan yang Perlu Kamu Ketahui

KedaiKita sengaja dibuat sederhana. Batasan berikut nyata dan bisa kamu temui saat mencobanya. Tuliskan batasan seperti ini dengan jujur di README proyek akhirmu juga.

| Batasan | Akibatnya | Lihat |
|---|---|---|
| Nomor pesanan mulai dari P001 lagi setiap kali aplikasi dibuka | `transaksi.csv` bisa berisi nomor ganda | [Latihan 3](../latihan.md) |
| Total pesanan selalu dihitung ulang dari harga menu dan poin pelanggan **saat ini** | struk yang dicetak ulang, laporan, dan bahkan `transaksi.csv` bisa berbeda dari jumlah yang benar-benar dibayar (contoh di bawah) | catatan desain di solusi [Latihan 5](../latihan.md) |
| *File* CSV yang tidak tersimpan sebagai UTF-8 | aplikasi berhenti dengan *traceback* `UnicodeDecodeError` | Kesalahan 3 di bagian 8 |
| Isi kolom tidak boleh memuat titik koma atau tanda petik ganda | *file* tidak terbaca dengan benar oleh versi Java | [halaman konsep bagian 4.4](../README.md#44-mengapa-titik-koma-bukan-koma) |
| *Input* berakhir saat pesanan belum dibayar | stok item yang sudah dimasukkan tetap berkurang dan ikut tersimpan, padahal pesanannya tidak tercatat | bagian 7.8 |

Contoh batasan kedua: pelanggan baru memesan 4 Nasi Goreng Kampung dengan diskon Member. Saat membayar, poinnya masih 0 sehingga diskon belum berlaku, dan ia membayar Rp110.000. Setelah lunas, ia mendapat 11 poin. Struk yang dicetak sesudah pembayaran, laporan sesi, dan `transaksi.csv` lalu menghitung ulang dengan poin baru itu sehingga mencatat Rp99.000. Perbaikannya adalah menyimpan total **saat pembayaran terjadi**, persis seperti struk kertas yang tidak berubah lagi setelah dicetak.

## 8. Kesalahan Umum dan Cara Membaca Pesan *Error*

### Kesalahan 1: Menjalankan modul di dalam *package* secara langsung

Dari folder `studi-kasus`, perintah berikut **salah**:

```bash
python kedaikita/aplikasi.py
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "aplikasi.py", line 13, in <module>
    from kedaikita.diskon import (Diskon, DiskonHappyHour, DiskonMember,
                                  TanpaDiskon)
ModuleNotFoundError: No module named 'kedaikita'
```

**Artinya:** saat `aplikasi.py` dijalankan langsung, Python mencari modul di folder milik `aplikasi.py` (di dalam `kedaikita/`), dan di sana tidak ada *package* bernama `kedaikita`. Pesan yang sama muncul jika kamu menekan ▷ saat yang terbuka adalah `aplikasi.py` atau `tests/test_kedaikita.py`. **Perbaikan:** jalankan pintu masuknya, `python main.py`, dari folder `studi-kasus`. Untuk *test*, pakai perintah di bagian 7.10.

### Kesalahan 2: *Test* tidak ditemukan atau gagal di-*import*

Perintah `python -m unittest` (tanpa `discover -s tests`) di folder `studi-kasus` hanya melaporkan `Ran 0 tests in 0.000s` lalu `NO TESTS RAN`.

**Artinya:** tanpa `discover -s tests`, `unittest` hanya mencari di folder aktif dan subfolder yang berupa *package* biasa. Folder `tests/` tidak punya `__init__.py` sehingga dilewati. **Perbaikan:** `python -m unittest discover -s tests -v`. Pastikan nama *file test* diawali `test` dan nama *method*-nya diawali `test_`.

Kasus serupa: perintah yang benar diketik dari folder yang salah, misalnya dari folder `python` dengan `-s studi-kasus/tests`. Hasilnya satu baris `ERROR` berisi `ImportError: Failed to import test module: test_kedaikita` dan `ModuleNotFoundError: No module named 'kedaikita'`, lalu `FAILED (errors=1)`. Penyebabnya sama dengan Kesalahan 1. **Perbaikan:** masuk dulu ke folder `studi-kasus`, lalu ketik perintahnya persis seperti di bagian 7.10.

### Kesalahan 3: *File* CSV tidak tersimpan sebagai UTF-8

*File* `menu.csv` diedit lalu disimpan Excel dengan pilihan **CSV (Comma delimited)**, dan ada huruf `é` pada `Café Latte`. Saat aplikasi dibuka, muncul pesan berikut:

```text
Traceback (most recent call last):
  ...
  File "repositori.py", line 45, in muat
    if next(pembaca, None) is None:
  File "<frozen codecs>", line 325, in decode
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xe9 in position 99: invalid continuation byte
```

**Artinya:** *byte* `0xe9` adalah huruf `é` dalam *encoding* Windows-1252 (bawaan Excel untuk pilihan itu), dan *byte* itu tidak sah dalam UTF-8. Angka `position 99` adalah letak *byte* itu di dalam *file*, jadi di komputermu angkanya bisa lain. *Exception* ini tidak ditangkap `main.py` karena `UnicodeDecodeError` bukan `KedaiError` maupun `OSError`. Inilah salah satu batasan KedaiKita (bagian 7.11). **Perbaikan:** simpan ulang lewat **File → Save As**, lalu pilih jenis **CSV UTF-8 (Comma delimited)**, atau hindari huruf beraksen. Pilihan itu menambahkan penanda kecil (BOM) di awal *file*, tetapi KedaiKita tetap bisa membacanya karena baris pertama (judul kolom) dilewati. Tantangan: tangkap `UnicodeDecodeError` di `muat()` lalu ubah menjadi `FormatDataError` agar pesannya ramah.

### Kesalahan 4: `input()` tanpa penanganan akhir *input*

Coba sendiri di folder `pertemuan-15` milikmu: buat *file* baru bernama `eof.py`, salin dua baris berikut ke dalamnya, lalu jalankan `python eof.py`.

```python
nama = input("Nama pelanggan: ")
print("Halo", nama)
```

Saat ditanya nama, jangan mengetik nama. Tekan Ctrl+D (macOS/Linux) atau Ctrl+Z lalu Enter (Windows) untuk mengakhiri *input*. Pesan *error*-nya:

```text
Nama pelanggan: Traceback (most recent call last):
  File "eof.py", line 1, in <module>
    nama = input("Nama pelanggan: ")
EOFError: EOF when reading a line
```

**Artinya:** `input()` tidak punya lagi yang bisa dibaca. **Perbaikan:** bungkus perulangan utama dengan `try ... except EOFError:` lalu tutup aplikasi dengan rapi, seperti `AplikasiKasir.jalankan()`.

### Kesalahan 5: *Path* relatif yang bergantung pada folder aktif

Kode `open("data/menu_awal.csv", encoding="utf-8")` yang dijalankan dari folder tanpa subfolder `data/` gagal dengan `FileNotFoundError: [Errno 2] No such file or directory: 'data/menu_awal.csv'`.

**Artinya:** *path* relatif dihitung dari **folder aktif terminal**, bukan dari folder *file* `.py`-nya. **Perbaikan:** jalankan dari folder yang benar, atau susun *path* dari lokasi *file* seperti di `main.py`: `Path(__file__).resolve().parent / "data"`.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Python. Python 3.11 ke atas, misalnya, menambahkan tanda `~~~^^^` di bawah bagian kode yang bermasalah. Alamat lengkap (*path*) pada *traceback* di atas sudah dipendekkan menjadi nama *file* saja.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Menyusun *path* | `Path(folder) / "nama"` | `Path(__file__).resolve().parent / "data"` |
| Menulis / menambah *file* | `open(p, "w")` / `open(p, "a")` + `encoding="utf-8"` | `berkas.write("Senin: Ayu\n")` |
| Membaca *file* | `berkas.read()`, `for baris in berkas:` | `p.read_text(encoding="utf-8")` |
| Menulis CSV | `csv.writer(f, delimiter=";", lineterminator="\n")` | `penulis.writerow(["M01", "Kopi"])` |
| Membaca CSV | `csv.reader(f, delimiter=";")` | `next(pembaca)` untuk melewati judul |
| Menutup otomatis | `with ... as nama:` | `with open(p, encoding="utf-8") as f:` |
| *Context manager* sendiri | `__enter__()` dan `__exit__()` | `with SambunganPrinter("Lab") as p:` |
| Folder sementara | `tempfile.TemporaryDirectory()` | `with tempfile.TemporaryDirectory() as folder:` |
| *Package* dan impor | folder + `__init__.py` | `from kedaikita.menu import Menu` |
| Argumen terminal | `sys.argv` | `if "--demo" in sys.argv:` |
| Akhir *input* | `except EOFError:` | membungkus perulangan menu utama |
| Kelas *test* | `class UjiX(unittest.TestCase):` | `def setUp(self):`, `def test_...(self):` |
| *Assertion* | `self.assertEqual(hasil, harapan)` | `with self.assertRaises(ValueError):` |
| Menjalankan *test* | `python -m unittest discover -s tests -v` | dari folder `studi-kasus` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).
- Mulai rencanakan [Proyek Akhir](../proyek-akhir.md)-mu.

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
