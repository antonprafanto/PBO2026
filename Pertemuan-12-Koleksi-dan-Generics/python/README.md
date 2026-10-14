# 🐍 Praktik Python Pertemuan 12: Koleksi dan *Generics*

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 12](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Contoh](#cara-menjalankan-contoh)
  - [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [*List* dan *Tuple*](#1-list-dan-tuple)
2. [Set: Kumpulan Tanpa Data Kembar](#2-set-kumpulan-tanpa-data-kembar)
3. [Dict: Mencari Lewat Kunci](#3-dict-mencari-lewat-kunci)
4. [Menjelajahi Dict dan Menjaga Urutan](#4-menjelajahi-dict-dan-menjaga-urutan)
5. [Mengurutkan dengan `key` dan *Lambda*](#5-mengurutkan-dengan-key-dan-lambda)
6. [Urutan Alami dengan `__lt__`](#6-urutan-alami-dengan-__lt__)
7. [Kesamaan Objek: `__eq__` dan `__hash__`](#7-kesamaan-objek-__eq__-dan-__hash__)
8. [Kelas Generik dan Petunjuk Tipe](#8-kelas-generik-dan-petunjuk-tipe)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 8 contoh, dari list sederhana sampai kelas generik
├── studi-kasus/     <- KedaiKita versi Pertemuan 12 (11 file, pintu masuknya main.py)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

### Cara Menjalankan Contoh

Setiap *file* di folder `contoh/` dan `solusi/` adalah program satu *file*. Pilih salah satu cara berikut. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-12-Koleksi-dan-Generics/python`. Di panel **Explorer** sebelah kiri, buka folder `contoh`, klik *file* yang ingin dicoba (misalnya `contoh01_list_dan_tuple.py`), lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Baris pertama di panel itu berisi perintah panjang yang diketik VS Code secara otomatis; *output* programmu muncul di bawahnya.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-12-Koleksi-dan-Generics/python/contoh` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd contoh` |

Setelah itu jalankan:

```bash
python contoh01_list_dan_tuple.py
```

Jika berhasil, baris pertama yang muncul adalah `=== LIST: DAFTAR BELANJA ANAK KOS ===`, dan seluruh hasilnya sama persis dengan blok ***Output:*** di [bagian 1](#1-list-dan-tuple). *File* di folder `solusi` dijalankan dengan cara yang sama; ganti saja `contoh` dengan `solusi`.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `contoh`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.

### Cara Menjalankan Studi Kasus

Studi kasus KedaiKita terdiri atas **11 *file*** yang saling meng-*import*. Pintu masuknya selalu `main.py`. *File* lain, seperti `menu.py` atau `laporan.py`, hanya berisi kelas sehingga tidak menampilkan apa-apa jika dijalankan sendiri.

- **Lewat VS Code:** buka `studi-kasus/main.py`, lalu klik ▷ (**Run Python File**). Cara ini selalu berhasil karena Python mencari *file* lain di folder milik `main.py`.
- **Lewat terminal:** masuk dulu ke folder `studi-kasus`, baru jalankan `main.py`.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-12-Koleksi-dan-Generics/python/studi-kasus` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd studi-kasus` |

Setelah itu jalankan:

```bash
python main.py
```

Jika berhasil, baris pertama yang muncul adalah `=== MENU KedaiKita ===`. Penjelasan kodenya ada di [bagian 9](#9-studi-kasus-kedaikita).

### Tempat Menyimpan Kodemu Sendiri

Anggap folder materi sebagai buku pegangan: dibaca dan dijalankan, tetapi tidak dicoret-coret. Simpan kode buatanmu sendiri (hasil mengetik ulang, percobaan "Coba sendiri", dan jawaban latihan) di folder lain **di luar** folder materi, misalnya:

```text
Documents/
├── PBO2026/                  <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/         <- milikmu sendiri
    └── pertemuan-12/         <- kode pertemuan ini
```

Jika sebuah "Coba sendiri" memintamu mengubah *file* contoh, salin dulu *file* itu ke folder `pertemuan-12` (lewat File Explorer di Windows atau Finder di macOS), lalu ubah salinannya. Untuk percobaan pada studi kasus, salin **seluruh folder** `studi-kasus` karena *file-file*-nya saling membutuhkan. Jalankan salinan itu dengan membuka folder `pertemuan-12` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**), atau arahkan terminal ke folder itu dengan `cd`. Alasan lengkapnya ada di [Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal setiap bagian menunjuk *file* contohnya. Klik untuk melihat isi lengkapnya.
- Blok kode yang diawali keterangan "isi lengkap *file*" boleh kamu ketik ulang di folder latihanmu (komentar pembuka di bagian atas *file* tidak ditulis ulang). Blok yang diawali kata "potongan" hanya berisi sebagian *file*, disalin persis. Untuk mencoba potongan, jalankan *file* lengkapnya, jangan menjalankan potongannya sendiri.
- Tanda `# [1]`, `# [2]`, dan seterusnya di dalam kode dijelaskan satu per satu di daftar **Penjelasan** tepat di bawah blok kode.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan. Hasil dari kode yang sengaja dibuat salah diawali kata lain, misalnya "Pesan *error*-nya:".

## 1. *List* dan *Tuple*

*File*: [`contoh/contoh01_list_dan_tuple.py`](contoh/contoh01_list_dan_tuple.py)

*List* sudah kamu kenal. Kali ini kita lihat kemampuannya lebih lengkap, lalu membandingkannya dengan saudaranya yang "keras kepala", yaitu *tuple*. Berikut isi lengkap *file*-nya (tanpa komentar pembuka):

```python
def main():
    belanja: list[str] = ["beras", "telur", "minyak"]  # [1] list berisi teks
    print("=== LIST: DAFTAR BELANJA ANAK KOS ===")
    print(f"Isi awal      : {', '.join(belanja)}")

    belanja.append("gula")  # [2] tambah di akhir
    belanja.insert(0, "kopi")  # sisipkan di indeks 0 (paling depan)
    belanja.remove("minyak")  # [3] hapus berdasarkan ISI, bukan indeks
    belanja.append("telur")  # data kembar boleh
    print(f"Setelah diubah: {', '.join(belanja)}")
    print(f"Jumlah item   : {len(belanja)}")
    print(f"Item pertama  : {belanja[0]}")  # [4] akses lewat indeks
    print(f"Item terakhir : {belanja[-1]}")
    if "gula" in belanja:  # [5] cek keanggotaan
        print(f"Posisi gula   : indeks {belanja.index('gula')}")
    print(f"Telur dicatat : {belanja.count('telur')} kali")

    print()
    print("=== DATA TETAP: HARI KULIAH PBO ===")
    hari_kuliah: tuple[str, ...] = ("Senin", "Rabu")  # [6] tuple memakai ( )
    print(f"Hari kuliah   : {', '.join(hari_kuliah)}")
    try:
        hari_kuliah[0] = "Selasa"  # [7] mencoba mengubah isi tuple
    except TypeError:
        print("Gagal mengubah: isinya tetap (immutable)")

    print()
    print("=== MEMBUAT LIST BARU DARI LIST LAMA ===")
    huruf_besar = [barang.upper() for barang in belanja]  # [8] list comprehension
    pendek = [barang for barang in belanja if len(barang) <= 4]  # [9] dengan syarat
    print(f"Huruf besar   : {', '.join(huruf_besar)}")
    print(f"Nama pendek   : {', '.join(pendek)}")
    print(f"List asli     : {', '.join(belanja)}")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== LIST: DAFTAR BELANJA ANAK KOS ===
Isi awal      : beras, telur, minyak
Setelah diubah: kopi, beras, telur, gula, telur
Jumlah item   : 5
Item pertama  : kopi
Item terakhir : telur
Posisi gula   : indeks 3
Telur dicatat : 2 kali

=== DATA TETAP: HARI KULIAH PBO ===
Hari kuliah   : Senin, Rabu
Gagal mengubah: isinya tetap (immutable)

=== MEMBUAT LIST BARU DARI LIST LAMA ===
Huruf besar   : KOPI, BERAS, TELUR, GULA, TELUR
Nama pendek   : kopi, gula
List asli     : kopi, beras, telur, gula, telur
```

Penjelasan:

- **[1]** `list[str]` adalah petunjuk tipe yang dibaca "*list* berisi teks". Untuk mencetak *list* dengan rapi (tanpa tanda kutip dan kurung siku), kita memakai `", ".join(...)`.
- **[2]** `append()` menambah di akhir, sedangkan `insert(indeks, isi)` menyisipkan di posisi tertentu.
- **[3]** `remove()` menghapus isi **pertama** yang cocok. Jika isinya tidak ada, Python melempar `ValueError`.
- **[4]** Indeks dimulai dari 0. Indeks negatif dihitung dari belakang: `belanja[-1]` adalah item terakhir.
- **[5]** Operator `in` memeriksa keanggotaan. Pada *list*, Python memeriksa isi satu per satu dari depan. Ada juga `index()` (posisi pertama) dan `count()` (jumlah kemunculan).
- **[6]** *Tuple* ditulis dengan kurung biasa. Petunjuk tipe `tuple[str, ...]` dibaca "*tuple* berisi teks, berapa pun panjangnya".
- **[7]** Mengubah isi *tuple* memunculkan `TypeError`, yang kita tangkap dengan `try`/`except` seperti di Pertemuan 11.
- **[8]** *List comprehension* membuat *list* baru dalam satu baris. Bacalah: "`barang.upper()` untuk setiap `barang` di `belanja`". Hasilnya sama dengan perulangan `for` yang memanggil `append()` satu per satu, tetapi lebih ringkas.
- **[9]** Bagian `if` di akhir menyaring isi. *List* aslinya tidak berubah.

## 2. Set: Kumpulan Tanpa Data Kembar

*File*: [`contoh/contoh02_set_himpunan.py`](contoh/contoh02_set_himpunan.py)

Pendaftaran *workshop* sering kacau karena ada yang mengisi formulir dua kali. Set membereskannya secara otomatis. Berikut isi lengkap *file*-nya (tanpa komentar pembuka):

```python
def cetak(judul: str, isi: set[str]):
    """Mencetak isi set dalam urutan abjad agar hasilnya selalu sama."""
    print(f"{judul:<14}: {', '.join(sorted(isi))}")  # [5] urutkan dulu!


def main():
    pendaftar = ["Ayu", "Bima", "Citra", "Ayu", "Dimas", "Bima"]  # [1] ada yang 2 kali
    peserta_python: set[str] = set(pendaftar)  # [2] list -> set: duplikat hilang
    peserta_java = {"Citra", "Eka", "Ayu", "Fajar"}  # [3] set ditulis dengan { }

    print("=== PENDAFTARAN WORKSHOP PYTHON ===")
    print(f"Formulir masuk: {len(pendaftar)}")
    print(f"Peserta unik  : {len(peserta_python)}")
    cetak("Peserta Python", peserta_python)
    peserta_python.add("Eka")  # [4] tambah anggota baru
    peserta_python.add("Ayu")  # sudah ada: diabaikan, tanpa error
    print(f"Setelah tambah Eka dan Ayu: {len(peserta_python)} peserta")

    print()
    print("=== OPERASI HIMPUNAN ===")
    cetak("Peserta Java", peserta_java)
    cetak("Ikut keduanya", peserta_python & peserta_java)  # [6] irisan
    cetak("Semua peserta", peserta_python | peserta_java)  # gabungan
    cetak("Hanya Python", peserta_python - peserta_java)  # selisih
    if "Fajar" not in peserta_python:  # [7] cek keanggotaan
        print("Fajar belum ikut workshop Python")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== PENDAFTARAN WORKSHOP PYTHON ===
Formulir masuk: 6
Peserta unik  : 4
Peserta Python: Ayu, Bima, Citra, Dimas
Setelah tambah Eka dan Ayu: 5 peserta

=== OPERASI HIMPUNAN ===
Peserta Java  : Ayu, Citra, Eka, Fajar
Ikut keduanya : Ayu, Citra, Eka
Semua peserta : Ayu, Bima, Citra, Dimas, Eka, Fajar
Hanya Python  : Bima, Dimas
Fajar belum ikut workshop Python
```

Penjelasan:

- **[1]** *List* boleh berisi data kembar: Ayu dan Bima masing-masing muncul dua kali.
- **[2]** `set(pendaftar)` membuat set dari *list*. Data kembar otomatis dibuang sehingga 6 formulir menjadi 4 peserta.
- **[3]** Set juga bisa ditulis langsung dengan kurung kurawal.
- **[4]** `add()` menambah anggota. Menambah anggota yang sudah ada hanya diabaikan, tanpa *error*.
- **[5]** Urutan isi set **tidak dijamin**, bahkan bisa berubah setiap kali program dijalankan (lihat [halaman konsep](../README.md#4-urutan-isi-jangan-mengandalkan-kebetulan)). Karena itu, kita selalu memakai `sorted()`, yang mengembalikan ***list*** baru yang sudah urut.
- **[6]** Operator himpunan dari matematika diskrit: `&` irisan, `|` gabungan, `-` selisih.
- **[7]** Pemeriksaan `in`/`not in` pada set sangat cepat karena set langsung menuju "rak" lewat kode *hash*.

| Operasi | Operator | *Method* | Hasil untuk `{1, 2, 3}` dan `{2, 3, 4}` |
|---|---|---|---|
| Irisan | `a & b` | `a.intersection(b)` | `{2, 3}` |
| Gabungan | `a \| b` | `a.union(b)` | `{1, 2, 3, 4}` |
| Selisih | `a - b` | `a.difference(b)` | `{1}` |
| Selisih simetris | `a ^ b` | `a.symmetric_difference(b)` | `{1, 4}` |

> [!WARNING]
> `{}` membuat **dict** kosong, bukan set kosong. Untuk set kosong, tulis `set()`. Jika keliru, `peserta.add("Ayu")` akan gagal dengan `AttributeError: 'dict' object has no attribute 'add'`.

## 3. Dict: Mencari Lewat Kunci

*File*: [`contoh/contoh03_dict_pencarian.py`](contoh/contoh03_dict_pencarian.py)

*File* ini berisi kelas `Mahasiswa` sederhana dan fungsi `cari_di_list()` yang mencari dengan cara lama: memeriksa *list* satu per satu sambil menghitung langkahnya. Kita bandingkan dengan dict. Berikut potongan isi `main()`, setelah empat objek `Mahasiswa` disimpan di *list* `daftar`:

```python
    data: dict[str, Mahasiswa] = {}  # [1] dict kosong: NIM -> Mahasiswa
    for mhs in daftar:
        data[mhs.nim] = mhs  # [2] simpan dengan kunci NIM

    print("=== CARI MAHASISWA BERDASARKAN NIM ===")
    print(f"Lewat list : {cari_di_list(daftar, '2409106004')}")
    print(f"Lewat kunci: {data['2409106004']}")  # [3] langsung lewat kunci
    nim_asing = "2409106099"
    if nim_asing in data:  # [4] cek dulu apakah kuncinya ada
        print(data[nim_asing])
    else:
        print(f"NIM {nim_asing} tidak terdaftar")
    if data.get(nim_asing) is None:  # [5] get(): None jika kunci tidak ada
        print("get() untuk NIM asing: tidak ada hasil")

    print()
    print("=== MENGUBAH, MENGHAPUS, DAN NILAI CADANGAN ===")
    print(f"Jumlah data: {len(data)}")
    bima_baru = Mahasiswa("2409106002", "Bima Saputra", "Sistem Informasi")
    data["2409106002"] = bima_baru  # [6] kunci sudah ada: nilai lama DITIMPA
    print(f"Bima pindah prodi: {data['2409106002']}")
    print(f"Jumlah data: {len(data)}")  # tetap 4: kunci tidak bisa kembar
    del data["2409106001"]  # [7] hapus berdasarkan kunci
    print(f"Setelah 2409106001 dihapus: {len(data)} data")
    pinjaman: dict[str, int] = {"2409106003": 2}  # NIM -> jumlah buku dipinjam
    print(f"Buku dipinjam Citra: {pinjaman.get('2409106003', 0)}")  # [8] nilai cadangan
    print(f"Buku dipinjam Dimas: {pinjaman.get('2409106004', 0)}")
```

***Output:***

```text
=== CARI MAHASISWA BERDASARKAN NIM ===
  (list memeriksa 4 data sampai ditemukan)
Lewat list : 2409106004 Dimas Pratama (Informatika)
Lewat kunci: 2409106004 Dimas Pratama (Informatika)
NIM 2409106099 tidak terdaftar
get() untuk NIM asing: tidak ada hasil

=== MENGUBAH, MENGHAPUS, DAN NILAI CADANGAN ===
Jumlah data: 4
Bima pindah prodi: 2409106002 Bima Saputra (Sistem Informasi)
Jumlah data: 4
Setelah 2409106001 dihapus: 3 data
Buku dipinjam Citra: 2
Buku dipinjam Dimas: 0
```

Penjelasan:

- **[1]** `{}` membuat dict kosong. Petunjuk tipe `dict[str, Mahasiswa]` dibaca "dict dengan kunci teks dan nilai `Mahasiswa`".
- **[2]** `data[kunci] = nilai` menyimpan pasangan baru.
- **[3]** `data[kunci]` langsung mengambil nilainya, sedangkan *list* harus memeriksa 4 data dulu. Dengan ribuan mahasiswa, bedanya sangat terasa.
- **[4]** `in` pada dict memeriksa **kunci**, bukan nilai.
- **[5]** `get(kunci)` mengembalikan `None` jika kunci tidak ada. Sebaliknya, `data[kunci]` untuk kunci yang tidak ada memunculkan `KeyError`.
- **[6]** Menyimpan dengan kunci yang **sudah ada** menimpa nilai lama. Jumlah data tetap 4.
- **[7]** `del data[kunci]` menghapus pasangan berdasarkan kuncinya.
- **[8]** `get(kunci, cadangan)` mengembalikan nilai cadangan jika kunci tidak ada. Dimas belum meminjam buku, jadi hasilnya 0.

> [!IMPORTANT]
> Kunci dict harus *hashable*, yaitu punya kode *hash* yang tidak berubah. Teks, angka, dan *tuple* (yang isinya teks atau angka) boleh menjadi kunci, tetapi *list* tidak. Objek buatanmu sendiri boleh menjadi kunci asalkan aturan kesamaannya benar (bagian 7).

## 4. Menjelajahi Dict dan Menjaga Urutan

*File*: [`contoh/contoh04_iterasi_dict.py`](contoh/contoh04_iterasi_dict.py)

Pola paling terkenal dari dict adalah **menghitung kemunculan**, misalnya menghitung suara pemilihan ketua himpunan. Berikut isi lengkap *file*-nya (tanpa komentar pembuka):

```python
def main():
    suara = ["Bima", "Ayu", "Bima", "Citra", "Ayu", "Bima"]  # [1] isi kotak suara
    hitung: dict[str, int] = {}
    for nama in suara:
        hitung[nama] = hitung.get(nama, 0) + 1  # [2] belum ada -> mulai dari 0

    print("=== HASIL PEMILIHAN KETUA HIMPUNAN ===")
    print(f"Kandidat   : {', '.join(hitung.keys())}")  # [3] kunci saja
    total = sum(hitung.values())  # [4] nilai saja
    print(f"Total suara: {total}")
    for nama, jumlah in hitung.items():  # [5] pasangan kunci-nilai
        print(f"{nama}: {jumlah} suara")

    print()
    print("=== URUT NAMA KANDIDAT (A-Z) ===")
    for nama, jumlah in sorted(hitung.items()):  # [6] urutkan berdasarkan kunci
        print(f"{nama}: {jumlah} suara")

    print()
    print("=== PERSENTASE (dibulatkan ke bawah) ===")
    persen = {nama: jumlah * 100 // total for nama, jumlah in hitung.items()}  # [7]
    for nama, nilai in persen.items():
        print(f"{nama}: {nilai}%")


if __name__ == "__main__":
    main()
```

***Output:***

```text
=== HASIL PEMILIHAN KETUA HIMPUNAN ===
Kandidat   : Bima, Ayu, Citra
Total suara: 6
Bima: 3 suara
Ayu: 2 suara
Citra: 1 suara

=== URUT NAMA KANDIDAT (A-Z) ===
Ayu: 2 suara
Bima: 3 suara
Citra: 1 suara

=== PERSENTASE (dibulatkan ke bawah) ===
Bima: 50%
Ayu: 33%
Citra: 16%
```

Penjelasan:

- **[1]** Setiap isi *list* adalah satu suara.
- **[2]** Pola hitung: ambil jumlah lama (0 jika nama belum ada), tambah 1, lalu simpan lagi. Pola ini juga dipakai di `LaporanPenjualan`.
- **[3]** `keys()` berisi kunci saja. Urutannya sesuai urutan kunci **pertama kali** dimasukkan: Bima dulu karena suara pertama untuk Bima. Sejak Python 3.7, urutan ini **dijamin**.
- **[4]** `values()` berisi nilai saja, cocok untuk dijumlahkan dengan `sum()`.
- **[5]** `items()` berisi pasangan `(kunci, nilai)` yang bisa langsung dipecah menjadi dua variabel.
- **[6]** `sorted(hitung.items())` mengurutkan pasangan berdasarkan kuncinya (nama A-Z). Hasilnya *list* baru; dict aslinya tetap.
- **[7]** *Dict comprehension*: mirip *list comprehension*, tetapi menghasilkan pasangan `kunci: nilai`. Hitungan `jumlah * 100 // total` memakai pembagian bulat sehingga 1 dari 6 suara menjadi 16%, bukan 16,67%.

> [!WARNING]
> Jangan menambah atau menghapus kunci dict **sambil** menjelajahinya dengan `for`. Python akan berhenti dengan `RuntimeError: dictionary changed size during iteration`. Jelajahi salinan kuncinya (`for nama in list(hitung):`), atau bentuk dict baru dengan *dict comprehension*.

## 5. Mengurutkan dengan `key` dan *Lambda*

*File*: [`contoh/contoh05_sorting_key.py`](contoh/contoh05_sorting_key.py)

Toko daring selalu punya tombol "Termurah", "Terlaris", dan "Rating". Datanya sama, aturan urutnya berbeda. Inilah **urutan khusus**. *File* ini berisi kelas `Produk` (`nama`, `harga`, `rating`, `terjual`) dan fungsi `tampilkan()` yang mencetak judul lalu setiap produk. Berikut potongan *file*-nya, mulai dari fungsi `ambil_harga()`:

```python
def ambil_harga(produk: Produk) -> int:  # [1] fungsi biasa sebagai kunci
    return produk.harga


def main():
    daftar = [
        Produk("Flashdisk 64GB", 85000, 5, 120),
        Produk("Mouse Wireless", 75000, 4, 340),
        Produk("Kabel Data USB-C", 25000, 4, 520),
        Produk("Headset Gaming", 150000, 5, 95),
        Produk("Powerbank 10000mAh", 125000, 4, 210),
    ]
    tampilkan("URUTAN ASLI", daftar)
    tampilkan("TERMURAH", sorted(daftar, key=ambil_harga))  # [2] tanpa tanda ()
    terlaris = sorted(daftar, key=lambda p: p.terjual, reverse=True)  # [3] lambda
    tampilkan("TERLARIS", terlaris)
    rating = sorted(daftar, key=lambda p: (-p.rating, p.harga))  # [4] dua kriteria
    tampilkan("RATING TERTINGGI, LALU TERMURAH", rating)

    print("=== LAIN-LAIN ===")
    urut_nama = sorted(daftar, key=lambda p: p.nama)  # [5]
    print(f"Nama A-Z      : {', '.join([p.nama for p in urut_nama])}")
    print(f"Paling murah  : {min(daftar, key=lambda p: p.harga).nama}")  # [6]
    print(f"Paling mahal  : {max(daftar, key=lambda p: p.harga).nama}")
    print(f"Urutan asli tetap, pertama: {daftar[0].nama}")  # [7]
    rating_5 = [p.nama for p in daftar if p.rating == 5]  # [8] bonus
    print(f"Rating 5      : {', '.join(rating_5)}")
```

Bagian URUTAN ASLI mencetak kelima produk persis sesuai urutan di *list*. Bagian berikutnya:

***Output:***

```text
=== TERMURAH ===
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210
Headset Gaming        Rp150.000  rating 5  terjual 95

=== TERLARIS ===
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Headset Gaming        Rp150.000  rating 5  terjual 95

=== RATING TERTINGGI, LALU TERMURAH ===
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Headset Gaming        Rp150.000  rating 5  terjual 95
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210

=== LAIN-LAIN ===
Nama A-Z      : Flashdisk 64GB, Headset Gaming, Kabel Data USB-C, Mouse Wireless, Powerbank 10000mAh
Paling murah  : Kabel Data USB-C
Paling mahal  : Headset Gaming
Urutan asli tetap, pertama: Flashdisk 64GB
Rating 5      : Flashdisk 64GB, Headset Gaming
```

Penjelasan:

- **[1]** `key` membutuhkan sebuah **fungsi** yang menerima satu isi *list* dan mengembalikan nilai pembanding.
- **[2]** Fungsinya dikirim **tanpa** tanda kurung: `key=ambil_harga`. Kita menyerahkan fungsinya, bukan hasil memanggilnya. `sorted()` lalu memanggilnya untuk setiap produk.
- **[3]** Menulis fungsi kecil seperti `ambil_harga` setiap kali terasa repot. ***Lambda*** adalah fungsi tanpa nama yang ditulis langsung di tempat. `reverse=True` membalik urutan menjadi terbesar dulu.
- **[4]** Jika `key` mengembalikan ***tuple***, Python membandingkan isi pertama dulu, lalu isi kedua jika seri. Tanda minus pada `-p.rating` membuat rating terbesar di depan, sementara harga tetap dari yang termurah.
- **[5]** Kunci berupa teks diurutkan menurut abjad.
- **[6]** `min()` dan `max()` juga menerima `key`.
- **[7]** `sorted()` selalu membuat *list* **baru**. *List* `daftar` tetap pada urutan aslinya.
- **[8]** Bonus: *list comprehension* dengan syarat sekaligus mengambil nama.

Anatomi sebuah *lambda* (bukan program, hanya sketsa untuk dibaca):

```text
lambda p: p.terjual      <- kata kunci lambda, parameter p, lalu nilai yang dikembalikan
def tanpa_nama(p):       <- fungsi biasa yang artinya sama persis
    return p.terjual
```

> [!IMPORTANT]
> Bedakan `sorted(daftar)` dengan `daftar.sort()`. `sorted()` mengembalikan *list* **baru**. `daftar.sort()` mengurutkan *list* **itu sendiri** dan mengembalikan `None`. Kesalahan klasik: `hasil = daftar.sort()` lalu heran mengapa `hasil` berisi `None`.

## 6. Urutan Alami dengan `__lt__`

*File*: [`contoh/contoh06_urutan_alami.py`](contoh/contoh06_urutan_alami.py)

Untuk peserta lomba lari, urutan yang paling wajar selalu sama: yang tercepat di depan. Aturan baku seperti ini sebaiknya ditulis **di dalam kelas** `Pelari` sebagai urutan alami. Kelas `Pelari` menyimpan nomor dada, nama, dan waktu tempuh dalam detik. Berikut potongan kelas itu, yaitu *method* `__lt__`:

```python
    def __lt__(self, lain: "Pelari") -> bool:  # [1] dipakai untuk a < b
        if self._waktu_detik != lain._waktu_detik:
            return self._waktu_detik < lain._waktu_detik
        return self._nomor < lain._nomor  # [2] waktu sama: nomor dada kecil dulu
```

Potongan `main()` berikutnya, setelah lima objek `Pelari` disimpan di *list* `hasil` dan dicetak sebagai catatan panitia:

```python
    print("=== PERINGKAT (urutan alami: tercepat dulu) ===")
    for nomor, pelari in enumerate(sorted(hasil), start=1):  # [3] tanpa key
        print(f"{nomor}. {pelari}")
    print(f"Juara 1: {min(hasil).nama}")  # [4] min() juga memakai __lt__
    rudi = hasil[0]
    joko = hasil[2]
    print(f"Joko lebih cepat dari Rudi? {'ya' if joko < rudi else 'tidak'}")  # [5]

    print()
    print("=== DARI YANG TERLAMBAT ===")
    for pelari in sorted(hasil, reverse=True):  # [6] urutan alami dibalik
        print(pelari)

    print()
    print("=== ABSENSI (urutan khusus: nama A-Z) ===")
    absensi = sorted(hasil, key=lambda p: p.nama)  # [7] key mengalahkan urutan alami
    print(", ".join([p.nama for p in absensi]))
```

***Output:***

```text
=== CATATAN PANITIA (urutan tiba di meja) ===
#105 Rudi  21:30
#112 Maya  18:45
#101 Joko  19:58
#108 Lina  25:10
#103 Fikri 19:58

=== PERINGKAT (urutan alami: tercepat dulu) ===
1. #112 Maya  18:45
2. #101 Joko  19:58
3. #103 Fikri 19:58
4. #105 Rudi  21:30
5. #108 Lina  25:10
Juara 1: Maya
Joko lebih cepat dari Rudi? ya

=== DARI YANG TERLAMBAT ===
#108 Lina  25:10
#105 Rudi  21:30
#103 Fikri 19:58
#101 Joko  19:58
#112 Maya  18:45

=== ABSENSI (urutan khusus: nama A-Z) ===
Fikri, Joko, Lina, Maya, Rudi
```

Penjelasan:

- **[1]** `__lt__` (*less than*) dipanggil Python setiap kali menemui `a < b`. Kembalikan `True` jika `self` harus berada **sebelum** `lain`. Di sini "lebih kecil" berarti "waktunya lebih singkat".
- **[2]** Joko dan Fikri sama-sama 19:58. Kriteria kedua "nomor dada kecil dulu" membuat hasilnya selalu pasti.
- **[3]** `sorted(hasil)` tanpa `key` langsung memakai `__lt__`. `enumerate(..., start=1)` memberi nomor peringkat mulai dari 1.
- **[4]** `min()` mencari isi "terkecil", artinya yang tercepat.
- **[5]** Operator `<` kini bermakna untuk objek `Pelari`: `joko < rudi` memanggil `joko.__lt__(rudi)`.
- **[6]** `reverse=True` membalik urutan alami.
- **[7]** Urutan alami tidak mengunci kita. `key` tetap bisa memberi urutan khusus kapan saja.

## 7. Kesamaan Objek: `__eq__` dan `__hash__`

*File*: [`contoh/contoh07_kesamaan_objek.py`](contoh/contoh07_kesamaan_objek.py)

Kita bandingkan dua kelas. `PemilihPolos` tidak punya aturan kesamaan, sedangkan `Pemilih` (dengan *property* `nik` dan `nama`) menganggap dua pemilih sama jika NIK-nya sama. Berikut potongan kelas `Pemilih`:

```python
    def __eq__(self, lain) -> bool:  # [1] aturan kesamaan: bandingkan NIK
        if not isinstance(lain, Pemilih):
            return NotImplemented
        return self._nik == lain._nik

    def __hash__(self) -> int:  # [2] hash dari data yang SAMA dengan __eq__
        return hash(self._nik)
```

Program utamanya mula-mula membuat dua `PemilihPolos` dengan data identik (`a1` dan `a2`), mencetak `ya_tidak(a1 == a2)` (penanda **[3]**), lalu jumlah isi set `{a1, a2}`. Fungsi kecil `ya_tidak()` mengubah `True`/`False` menjadi teks "ya"/"tidak". Setelah itu, potongan `main()` untuk versi B:

```python
    print("=== VERSI B: SAMA JIKA NIK SAMA ===")
    b1 = Pemilih("6472010000000001", "Budi Santoso")
    b2 = Pemilih("6472010000000001", "Budi Santosa")  # salah ketik nama, NIK sama
    b3 = Pemilih("6472010000000002", "Siti Aminah")
    print(f"Dianggap sama     : {ya_tidak(b1 == b2)}")  # [4] memanggil __eq__
    print(f"Objek sama persis : {ya_tidak(b1 is b2)}")
    print(f"Kode hash sama    : {ya_tidak(hash(b1) == hash(b2))}")
    dpt: set[Pemilih] = set()  # DPT = daftar pemilih tetap
    dpt.add(b1)
    dpt.add(b2)  # [5] NIK sudah ada: diabaikan
    dpt.add(b3)
    print(f"Isi set           : {len(dpt)} pemilih")
    for pemilih in sorted(dpt, key=lambda p: p.nik):  # urutkan dulu sebelum dicetak
        print(f"  {pemilih.nik} {pemilih.nama}")

    print()
    print("=== MENCARI DENGAN OBJEK LAIN YANG NIK-NYA SAMA ===")
    tps: dict[Pemilih, str] = {b1: "TPS 05", b3: "TPS 12"}  # [6] objek sebagai kunci
    pencari = Pemilih("6472010000000002", "Siti A.")  # objek baru, NIK milik Siti
    print(f"Terdaftar di DPT  : {ya_tidak(pencari in dpt)}")  # [7]
    print(f"Lokasi TPS        : {tps[pencari]}")
```

***Output:***

```text
=== VERSI A: TANPA ATURAN KESAMAAN ===
Dianggap sama     : tidak
Isi set           : 2 pemilih

=== VERSI B: SAMA JIKA NIK SAMA ===
Dianggap sama     : ya
Objek sama persis : tidak
Kode hash sama    : ya
Isi set           : 2 pemilih
  6472010000000001 Budi Santoso
  6472010000000002 Siti Aminah

=== MENCARI DENGAN OBJEK LAIN YANG NIK-NYA SAMA ===
Terdaftar di DPT  : ya
Lokasi TPS        : TPS 12
```

Penjelasan:

- **[1]** `__eq__` dipanggil saat kita menulis `a == b`. Jika `lain` bukan `Pemilih`, kita mengembalikan nilai khusus `NotImplemented` ("aku tidak tahu cara membandingkannya"). Secara sederhana, Python lalu memakai aturan bawaannya sehingga hasilnya tidak sama.
- **[2]** `__hash__` dihitung dari **data yang sama** dengan `__eq__`, yaitu NIK. Cara termudah: pinjam kode *hash* milik teks NIK dengan `hash(self._nik)`. Nilai kode *hash* teks diacak setiap kali program berjalan, jadi kita hanya mencetak apakah keduanya **sama**.
- **[3]** Tanpa `__eq__`, `==` hanya bernilai benar untuk objek yang sama persis. Set berisi dua "Budi".
- **[4]** Kini `b1 == b2` bernilai benar walaupun keduanya **dua objek berbeda** (`b1 is b2` tetap salah).
- **[5]** Saat `b2` ditambahkan, set menemukan `b1` di rak yang sama dan menganggapnya sudah ada. Yang tersimpan tetap `b1` ("Budi Santoso"), objek yang masuk lebih dulu.
- **[6]** Objek `Pemilih` boleh menjadi kunci dict karena punya `__hash__`.
- **[7]** `pencari` adalah objek **baru**, tetapi NIK-nya milik Siti. Pencarian di set dan dict tetap berhasil.

## 8. Kelas Generik dan Petunjuk Tipe

*File*: [`contoh/contoh08_kelas_generik.py`](contoh/contoh08_kelas_generik.py)

Potongan bagian atas *file* ini (tepat setelah komentar pembuka):

```python
from typing import Generic, TypeVar

T = TypeVar("T")  # [1] variabel tipe bernama T


class Kotak(Generic[T]):  # [2] kelas generik dengan satu parameter tipe
    """Kotak yang berisi satu barang bertipe T."""

    def __init__(self, isi: T):
        self._isi = isi

    @property
    def isi(self) -> T:  # [3] tipe kembalian mengikuti T
        return self._isi

    def ganti(self, isi_baru: T):
        self._isi = isi_baru

    def __str__(self) -> str:
        return f"Kotak berisi {self._isi}"
```

Di bawahnya ada kelas `KotakLama` tanpa petunjuk tipe sama sekali (hanya menyimpan `self.isi = isi`). Potongan berikutnya berisi fungsi generik dan program utama:

```python
def pertama(daftar: list[T]) -> T:  # [4] fungsi generik
    """Mengembalikan isi pertama sebuah list, apa pun tipe isinya."""
    return daftar[0]


def main():
    kotak_angka: Kotak[int] = Kotak(42)  # [5] di sini T = int
    kotak_teks: Kotak[str] = Kotak("bekal nasi kuning")  # di sini T = str
    print("=== KOTAK GENERIK ===")
    print(kotak_angka)
    print(kotak_teks)
    print(f"Isi kotak angka + 8   : {kotak_angka.isi + 8}")
    print(f"Isi kotak teks kapital: {kotak_teks.isi.upper()}")
    kotak_angka.ganti(100)
    print(f"Setelah diganti       : {kotak_angka}")

    print()
    print("=== FUNGSI/METHOD GENERIK ===")
    print(f"Hari pertama : {pertama(['Senin', 'Rabu', 'Jumat'])}")
    print(f"Angka pertama: {pertama([10, 20, 30])}")

    print()
    print("=== KOTAK TANPA TIPE ===")
    kotak_lama = KotakLama("pulpen")
    print(f"Isi kotak lama: {kotak_lama.isi.upper()}")  # [6]
```

***Output:***

```text
=== KOTAK GENERIK ===
Kotak berisi 42
Kotak berisi bekal nasi kuning
Isi kotak angka + 8   : 50
Isi kotak teks kapital: BEKAL NASI KUNING
Setelah diganti       : Kotak berisi 100

=== FUNGSI/METHOD GENERIK ===
Hari pertama : Senin
Angka pertama: 10

=== KOTAK TANPA TIPE ===
Isi kotak lama: PULPEN
```

Penjelasan:

- **[1]** `TypeVar("T")` membuat **variabel tipe**. Seperti variabel biasa yang mewakili sebuah nilai, `T` mewakili sebuah **tipe** yang belum ditentukan.
- **[2]** `Generic[T]` menandai `Kotak` sebagai kelas generik dengan satu parameter tipe.
- **[3]** Setiap kali `T` ditulis di dalam kelas, artinya "tipe yang sama dengan isi kotak ini".
- **[4]** Fungsi juga bisa generik. `list[T] -> T` berarti "diberi *list* berisi teks, hasilnya teks; diberi *list* berisi angka, hasilnya angka".
- **[5]** `Kotak[int]` mengisi `T` dengan `int`. VS Code kini tahu bahwa `kotak_angka.isi` adalah angka dan menawarkan saran yang sesuai.
- **[6]** `KotakLama` tanpa petunjuk tipe ternyata bekerja sama baiknya. Inilah poin pentingnya: **petunjuk tipe tidak mengubah cara program berjalan**.

| Petunjuk tipe | Dibaca |
|---|---|
| `list[Menu]` | *list* berisi `Menu` |
| `tuple[str, ...]` | *tuple* berisi teks, berapa pun panjangnya |
| `set[str]` | set berisi teks |
| `dict[str, int]` | dict dengan kunci teks dan nilai angka |
| `Menu \| None` | sebuah `Menu`, atau `None` |
| `Pasangan[str, int]` | kelas generik buatan sendiri dengan dua parameter tipe |

### Python tidak memeriksa petunjuk tipe saat berjalan

Mau membuktikannya? Buat *file* baru bernama `cek_tipe.py` di folder latihanmu, `PBO-latihan-saya/pertemuan-12/`, lalu ketik isi berikut. Isinya versi ringkas kelas `Kotak`, lalu dua baris terakhir yang **sengaja** mengisi `Kotak[int]` dengan teks:

```python
from typing import Generic, TypeVar

T = TypeVar("T")


class Kotak(Generic[T]):
    def __init__(self, isi: T):
        self._isi = isi

    def __str__(self) -> str:
        return f"Kotak berisi {self._isi}"


kotak_angka: Kotak[int] = Kotak("bukan angka")
print(kotak_angka)
```

Jalankan dari folder itu dengan `python cek_tipe.py`. Program tetap berjalan tanpa protes:

```text
Kotak berisi bukan angka
```

Kesalahan ini hanya tertangkap oleh **alat pemeriksa tipe** (*type checker*), yaitu program terpisah yang membaca kodemu tanpa menjalankannya. Ada dua pilihan, dan keduanya opsional:

- **VS Code (ekstensi Pylance)** memberi garis bawah merah pada `Kotak("bukan angka")`, lengkap dengan pesannya di panel **PROBLEMS**. Jika garis merah itu belum muncul, nyalakan dulu pemeriksaannya: tekan Ctrl+, (macOS: Cmd+,) untuk membuka **Settings**, ketik `type checking mode` di kotak pencarian, lalu ubah **Python › Analysis: Type Checking Mode** dari `off` menjadi `standard`.
- **mypy** adalah alat pemeriksa tipe yang dipasang terpisah (bukan bawaan Python). Di terminal yang berada di folder `pertemuan-12`, pasang sekali dengan `python -m pip install mypy`, lalu jalankan `python -m mypy cek_tipe.py` (macOS/Linux: `python3 -m ...`). Hasilnya:

```text
cek_tipe.py:14: error: Argument 1 to "Kotak" has incompatible type "str"; expected "int"  [arg-type]
Found 1 error in 1 file (checked 1 source file)
```

**Artinya:** di baris 14, argumen pertama untuk `Kotak` bertipe `str` (teks), padahal yang diharapkan `int` karena variabelnya diberi label `Kotak[int]`. Perhatikan bahwa programnya sendiri tetap bisa berjalan. Alat pemeriksa tipe hanya **memperingatkan**, tidak menghentikan program.

> [!NOTE]
> Contoh 09 (jebakan kelas pembungkus `Integer`) **khusus Java** karena Python tidak punya tipe primitif seperti `int` di Java. Penjelasannya ada di [Jembatan Python ↔ Java bagian 6](../jembatan-python-java.md#6-generics-petunjuk-atau-aturan).

## 9. Studi Kasus KedaiKita

*File*: [`studi-kasus/kedai.py`](studi-kasus/kedai.py), [`studi-kasus/menu.py`](studi-kasus/menu.py), [`studi-kasus/pasangan.py`](studi-kasus/pasangan.py), [`studi-kasus/laporan.py`](studi-kasus/laporan.py), dan [`studi-kasus/main.py`](studi-kasus/main.py)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini).

**Apa yang berubah dibanding Pertemuan 11?**

- `kedai.py`: menu disimpan di **dict** (kode → `Menu`), kode ganda ditolak dengan `ValueError`, `cari_menu()` mencari langsung lewat kunci, dan ada empat *method* baru.
- `menu.py`: kelas `Menu` mendapat `__eq__`, `__hash__`, dan `__lt__`.
- *File* baru `pasangan.py` (kelas generik `Pasangan[A, B]`) dan `laporan.py` (kelas `LaporanPenjualan`).
- `main.py` ditulis ulang untuk memamerkan filter, pengurutan, kesamaan objek, transaksi, dan laporan.
- `pesanan.py`, `pembayaran.py`, `pengecualian.py`, `pelanggan.py`, `utilitas.py`, dan `dapat_dicetak.py` **tidak berubah**.

### `kedai.py`: menu kini di dalam dict

Di konstruktor, atributnya kini `self._daftar_menu: dict[str, Menu] = {}` (kode → objek `Menu`). Berikut potongan *method* yang berubah dan yang baru:

```python
    def tambah_menu(self, menu: Menu):
        if menu.kode in self._daftar_menu:
            raise ValueError(f"Kode {menu.kode} sudah dipakai")
        self._daftar_menu[menu.kode] = menu

    def cari_menu(self, kode: str) -> Menu:
        """Mengembalikan Menu berdasarkan kode.

        Melempar MenuTidakDitemukanError jika kode tidak terdaftar.
        """
        if kode not in self._daftar_menu:
            raise MenuTidakDitemukanError(kode)
        return self._daftar_menu[kode]

    def semua_menu(self) -> list[Menu]:
        """Salinan daftar menu, urut sesuai urutan saat ditambahkan."""
        return list(self._daftar_menu.values())

    def menu_berdasarkan_kategori(self, kategori: str) -> list[Menu]:
        return [menu for menu in self._daftar_menu.values()
                if menu.kategori == kategori]

    def daftar_kategori(self) -> list[str]:
        """Kategori unik (tanpa duplikat), diurutkan abjad."""
        kategori_unik: set[str] = set()
        for menu in self._daftar_menu.values():
            kategori_unik.add(menu.kategori)
        return sorted(kategori_unik)
```

- **`tambah_menu()`** memeriksa kunci dulu. Tanpa pemeriksaan ini, menu baru berkode sama akan **menimpa** menu lama secara diam-diam (ingat contoh 03).
- **`cari_menu()`** tidak lagi memakai `for`. Kontraknya tetap sama dengan Pertemuan 11: jika kode tidak ada, ia melempar `MenuTidakDitemukanError`.
- **`semua_menu()`** mengembalikan **salinan** berupa *list* sehingga pemanggil bebas mengurutkannya tanpa merusak isi kedai (prinsip dari Pertemuan 05).
- **`menu_berdasarkan_kategori()`** memakai *list comprehension* dengan syarat. **`daftar_kategori()`** mengumpulkan kategori ke dalam set agar unik, lalu `sorted()` mengubahnya menjadi *list* yang urut abjad.
- *Method* lain menyesuaikan: `cetak()` menjelajahi `self._daftar_menu.values()`, dan `riwayat_pesanan()` mengembalikan salinan *list* pesanan.

### `menu.py` dan `pasangan.py`

Potongan kelas `Menu` di `menu.py`, yaitu tiga *method* barunya:

```python
    def __eq__(self, lain) -> bool:
        if not isinstance(lain, Menu):
            return NotImplemented
        return self._kode == lain._kode

    def __hash__(self) -> int:
        return hash(self._kode)

    def __lt__(self, lain: "Menu") -> bool:
        """Urutan alami: harga termurah dulu; jika harga sama, urut kode."""
        if self._harga != lain._harga:
            return self._harga < lain._harga
        return self._kode < lain._kode
```

Dua menu dianggap sama jika **kodenya** sama. Kode adalah pilihan tepat karena kode hanya bisa dibaca (tanpa *setter*) sejak Pertemuan 04. Akibatnya, kode *hash*-nya tidak pernah berubah. Ketiga *method* ini diwarisi oleh `Makanan` dan `Minuman`.

`pasangan.py` berisi kelas `Pasangan(Generic[A, B])` dengan dua `TypeVar`, dua *property* (`pertama` dan `kedua`), dan `__str__`. Polanya sama dengan `Kotak[T]` di contoh 08, hanya saja parameter tipenya **dua** dan boleh berbeda.

### `laporan.py`: koleksi bekerja bersama

Konstruktornya hanya menyimpan pesanan **lunas**: `[p for p in daftar_pesanan if p.status == "LUNAS"]`. *Method* `jumlah_terjual()` memakai pola hitung dari contoh 04 (nama menu → total porsi), lalu dipakai oleh *method* berikut (potongan dari `laporan.py`):

```python
    def menu_terlaris(self, n: int = 3) -> list[Pasangan[str, int]]:
        """n menu dengan porsi terbanyak. Jika seri, urut nama A-Z."""
        daftar = [Pasangan(nama, jumlah)
                  for nama, jumlah in self.jumlah_terjual().items()]
        daftar.sort(key=lambda p: (-p.kedua, p.pertama))
        return daftar[:n]
```

- **`menu_terlaris()`** mengubah setiap pasangan dict menjadi objek `Pasangan[str, int]`, lalu mengurutkannya dengan `key` berupa *tuple*: porsi terbanyak dulu; jika seri, nama A-Z. Potongan `daftar[:n]` mengambil `n` teratas.
- **`pendapatan_per_kategori()`** menjumlahkan subtotal per kategori dengan pola yang sama, lalu mengembalikan `dict(sorted(hasil.items()))`. Karena dict menjaga urutan masuk, hasilnya urut abjad kategori.

### `main.py`: memakai semuanya

Potongan dari `main.py`, yaitu fungsi pembantu `transaksi()`:

```python
def transaksi(kedai: Kedai, pelanggan: Pelanggan,
              daftar_beli: list[Pasangan[str, int]],
              pembayaran: Pembayaran) -> Pesanan:
    """Membuat pesanan, mengisi item (kode, jumlah), lalu membayarnya."""
    pesanan = kedai.buat_pesanan(pelanggan)
    try:
        for beli in daftar_beli:
            pesanan.tambah_item(kedai.cari_menu(beli.pertama), beli.kedua)
        pesanan.bayar(pembayaran)
    except KedaiError as e:
        print(f"  [GAGAL] {e}")
    return pesanan
```

Fungsi ini menerima daftar belanja berupa `list[Pasangan[str, int]]`, misalnya `[Pasangan("M01", 2), Pasangan("M03", 1)]`. Semua *error* kedai ditangkap sekaligus lewat induknya, `KedaiError` (Pertemuan 11). Di `main()`, urut harga ditulis `sorted(kedai.semua_menu())` (urutan alami, memakai `__lt__`), sedangkan urut nama ditulis `sorted(kedai.semua_menu(), key=lambda m: m.nama)`.

Jalankan studi kasusnya seperti di [Cara Menjalankan Studi Kasus](#cara-menjalankan-studi-kasus): `python main.py` dari dalam folder `studi-kasus`. Program dimulai dengan mencetak lima menu lewat `kedai.cetak()`. Bagian berikutnya:

***Output:***

```text
=== KATEGORI UNIK ===
Makanan, Minuman

=== FILTER: MINUMAN SAJA ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin

=== URUT HARGA TERMURAH (urutan alami) ===
   Rp8.000  Es Teh Manis
  Rp15.000  Pisang Goreng Keju
  Rp18.000  Kopi Susu Gula Aren
  Rp23.000  Mie Goreng Jawa
  Rp25.000  Nasi Goreng Kampung

=== URUT NAMA A-Z (kunci pengurutan) ===
M02  Es Teh Manis
M01  Kopi Susu Gula Aren
M04  Mie Goreng Jawa
M03  Nasi Goreng Kampung
M05  Pisang Goreng Keju

=== KODE GANDA DITOLAK ===
Ditolak: Kode M01 sudah dipakai
Jumlah menu tetap 5

=== KESAMAAN OBJEK ===
Sama isinya (kode sama)? ya
Objek yang sama persis? tidak
```

Setelah itu tercetak lima transaksi. Empat berhasil, sedangkan pesanan P005 milik Andi gagal karena saldo QRIS-nya kurang. Bagian penutupnya:

***Output:***

```text
Pembayaran pesanan P005 (Andi Wijaya)
  Metode       : QRIS
  Total bayar  : Rp25.000
  [GAGAL] Pembayaran QRIS gagal: saldo e-wallet tidak cukup (saldo Rp10.000)

Pesanan tercatat: 5
========================================
LAPORAN PENJUALAN KEDAIKITA
========================================
Pesanan lunas                          4
Total pendapatan               Rp167.000
----------------------------------------
Menu terlaris:
1. Es Teh Manis (4 porsi)
2. Kopi Susu Gula Aren (4 porsi)
3. Mie Goreng Jawa (1 porsi)
----------------------------------------
Pendapatan per kategori:
Makanan                         Rp63.000
Minuman                        Rp104.000
========================================
```

- **Kesamaan objek**: `kopi_b` adalah objek baru, tetapi kodenya M01 sehingga `==` menjawab "ya", sedangkan `is` menjawab "tidak".
- **Pesanan P005** tetap berstatus BARU. Pesanan itu tercatat di riwayat (5 pesanan), tetapi tidak ikut dihitung di laporan (4 pesanan lunas).
- **Total pendapatan** Rp167.000 adalah Rp61.000 + Rp31.000 + Rp41.000 + Rp34.000 (pesanan P001 sampai P004). Biaya layanan kartu (Rp620) tidak ikut karena `hitung_total()` hanya menjumlahkan harga item.

> [!TIP]
> **Coba sendiri:** salin seluruh folder `studi-kasus` ke folder latihanmu, `PBO-latihan-saya/pertemuan-12/`. Di salinan itu, buka `main.py` dan cari baris `print(f"Objek yang sama persis? {ya_tidak(kopi_a is kopi_b)}")`. Tepat di bawahnya, tambahkan baris `print(len({kopi_a, kopi_b}))` dengan indentasi yang sama (4 spasi). Simpan, lalu jalankan `python main.py` dari folder `studi-kasus` salinanmu. Angka berapa yang muncul di bawah baris "Objek yang sama persis? tidak", dan mengapa?

<details>
<summary>Lihat jawaban</summary>

Angka yang muncul adalah `1`. Set `{kopi_a, kopi_b}` hanya berisi satu menu karena keduanya punya kode yang sama: `__hash__` mengantar keduanya ke rak yang sama, lalu `__eq__` menyatakan keduanya sama sehingga `kopi_b` diabaikan.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan *Error*

Ingat, pesan *error* Python dibaca **dari bawah ke atas**. Baris paling bawah menyebut jenis *error* dan penyebabnya.

Kode di bagian ini **sengaja dibuat salah**. Jika ingin mencobanya, buat *file*-nya di folder latihanmu (`PBO-latihan-saya/pertemuan-12/`) dengan nama seperti di pesan *error* (`salah1.py`, `salah2.py`, `salah3.py`), salin kodenya, lalu jalankan dari folder itu. Jangan menaruhnya di folder materi.

### Kesalahan 1: Membaca kunci yang tidak ada

```python
data = {"2409106001": "Ayu Lestari"}
print(data["2409106099"])
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "salah1.py", line 2, in <module>
    print(data["2409106099"])
          ~~~~^^^^^^^^^^^^^^
KeyError: '2409106099'
```

**Artinya:** dict tidak punya kunci `'2409106099'`. **Perbaikan:** periksa dulu dengan `if nim in data:`, atau pakai `data.get(nim)` / `data.get(nim, cadangan)`.

### Kesalahan 2: Mengurutkan objek tanpa aturan urutan

```python
class Pelari:
    def __init__(self, nama, waktu):
        self.nama = nama
        self.waktu = waktu


hasil = [Pelari("Rudi", 1290), Pelari("Maya", 1125)]
print(sorted(hasil))
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "salah2.py", line 8, in <module>
    print(sorted(hasil))
          ~~~~~~^^^^^^^
TypeError: '<' not supported between instances of 'Pelari' and 'Pelari'
```

**Artinya:** `sorted()` perlu membandingkan dua `Pelari` dengan `<`, tetapi kelasnya tidak punya `__lt__`. **Perbaikan:** tambahkan `__lt__` (urutan alami), atau berikan `key=lambda p: p.waktu` (urutan khusus).

### Kesalahan 3: Menulis `__eq__` tanpa `__hash__`

```python
class Pemilih:
    def __init__(self, nik):
        self.nik = nik

    def __eq__(self, lain):
        return self.nik == lain.nik


dpt = set()
dpt.add(Pemilih("6472010000000001"))
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "salah3.py", line 10, in <module>
    dpt.add(Pemilih("6472010000000001"))
    ~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: unhashable type: 'Pemilih'
```

Di Python 3.14 ke atas, baris terakhirnya lebih panjang, tetapi intinya sama:

```text
TypeError: cannot use 'Pemilih' as a set element (unhashable type: 'Pemilih')
```

**Artinya:** begitu `__eq__` ditulis, Python mencabut kode *hash* bawaan kelas itu. Ini perlindungan agar aturan "sama berarti *hash* sama" tidak dilanggar diam-diam. **Perbaikan:** tambahkan `__hash__` dari data yang sama: `return hash(self.nik)`. Pesan serupa (`unhashable type: 'list'`) muncul jika kamu memakai *list* sebagai kunci dict.

> [!NOTE]
> Bunyi pesan *error* bisa sedikit berbeda antarversi Python. Pesan di atas berasal dari Python 3.13. Tanda `~~~^^^` hanya muncul di Python 3.11 ke atas. Fokuslah pada **jenis *error*** (`KeyError`, `TypeError`) dan kata kuncinya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| *List* / *tuple* | `[a, b]` / `(a, b)` | `hari = ("Senin", "Rabu")` |
| Set / set kosong | `{a, b}` / `set()` | `peserta = set(pendaftar)` |
| Dict / dict kosong | `{k: v}` / `{}` | `data[nim] = mhs` |
| Ambil dengan cadangan | `d.get(k, cadangan)` | `hitung.get(nama, 0)` |
| Jelajah dict | `for k, v in d.items():` | `for nama, jumlah in hitung.items():` |
| *List comprehension* | `[ekspresi for x in xs if syarat]` | `[p.nama for p in daftar if p.rating == 5]` |
| *Dict comprehension* | `{k: v for k, v in d.items()}` | `{n: j * 100 // total for n, j in hitung.items()}` |
| Urutkan (*list* baru) | `sorted(xs, key=..., reverse=...)` | `sorted(daftar, key=lambda p: p.harga)` |
| Urutkan *list* itu sendiri | `xs.sort(key=...)` | `daftar.sort(key=lambda p: (-p.kedua, p.pertama))` |
| *Lambda* | `lambda parameter: nilai` | `lambda m: m.nama` |
| Urutan alami | `def __lt__(self, lain) -> bool:` | `return self._harga < lain._harga` |
| Kesamaan + *hash* | `__eq__` + `__hash__` | `return hash(self._kode)` |
| Kelas generik | `class K(Generic[T]):` | `class Pasangan(Generic[A, B]):` |
| Petunjuk tipe koleksi | `list[T]`, `dict[K, V]`, `set[T]` | `dict[str, Menu]` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
