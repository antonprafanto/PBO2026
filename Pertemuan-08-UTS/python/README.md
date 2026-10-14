# 🐍 Solusi Praktik Python — Pertemuan 08: UTS

[⬅️ Informasi UTS](../README.md) · [☕ Solusi Java](../java/README.md) · [Pembahasan ➡️](../pembahasan.md)

> **Prasyarat:** sudah mencoba sendiri [Soal C1 dan C2](../latihan-soal.md#bagian-c-soal-praktik). Halaman ini menjelaskan cara menjalankan solusi Python dan bagian-bagian terpenting kodenya. Alasan pemilihan kelas dan relasi dibahas di [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).

## Daftar Isi

- [Persiapan](#persiapan)
1. [Soal C1: Peminjaman Alat Laboratorium](#1-soal-c1-peminjaman-alat-laboratorium)
2. [Soal C2: Toko Buku Daring](#2-soal-c2-toko-buku-daring)
3. [Membandingkan Output-mu dengan Solusi](#3-membandingkan-output-mu-dengan-solusi)
4. [Kesalahan Umum dan Cara Membaca Pesan Error](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
└── solusi/
    ├── soal_c1_peminjaman_alat.py   <- solusi Soal C1
    └── soal_c2_toko_buku.py         <- solusi Soal C2
```

Cara menjalankan dari terminal (Command Prompt, PowerShell, atau terminal VS Code):

```bash
cd Pertemuan-08-UTS/python/solusi
python soal_c1_peminjaman_alat.py
python soal_c2_toko_buku.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Solusi ini membutuhkan Python 3.10 atau lebih baru, karena memakai petunjuk tipe seperti `Alat | None`. Panduan instalasi ada di [00-Persiapan](../../00-Persiapan/README.md).

Setiap solusi ditulis dalam **satu file** agar mudah dibaca dan dikumpulkan. Di proyek sungguhan, kelas-kelasnya bisa dipecah ke beberapa file seperti KedaiKita sejak Pertemuan 05. Saat ujian, ikuti aturan pengumpulan dari dosen.

## 1. Soal C1: Peminjaman Alat Laboratorium

File: [`solusi/soal_c1_peminjaman_alat.py`](solusi/soal_c1_peminjaman_alat.py)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Mahasiswa` | Menyimpan data peminjam secara *read-only* | `@property` tanpa setter (P04), `__str__` (P03) |
| `Alat` | Menyimpan data dan status alat; meminjamkan, menerima kembali, menghitung denda | Enkapsulasi, method penjaga aturan (P04) |
| `AlatElektronik`, `KitPraktikum` | Menambah atribut, menentukan denda per hari, meng-*override* `__str__` | Pewarisan, `super()` (P07) |
| `Peminjaman` | Nomor otomatis, daftar alat, pengembalian dan denda, bukti peminjaman | Atribut kelas (P03), agregasi dan asosiasi (P05) |
| `Laboratorium` | Daftar alat, pencarian alat, catatan peminjaman | Agregasi, `None` (P05) |

### Kelas induk `Alat` dan kelas anaknya

Bagian awal kelas `Alat`:

```python
class Alat:
    """Kelas induk: data dan perilaku yang dimiliki SEMUA alat lab."""

    def __init__(self, kode: str, nama: str, denda_per_hari: int):
        if denda_per_hari <= 0:
            raise ValueError("Denda per hari harus lebih dari 0")
        self._kode = kode
        self._nama = nama
        self._denda_per_hari = denda_per_hari
        self._tersedia = True  # [1] alat baru selalu tersedia
```

Setelah deretan `@property`, kelas `Alat` punya method-method berikut:

```python
    def pinjamkan(self):
        """Pintu resmi untuk mengubah status menjadi dipinjam."""
        if not self._tersedia:
            raise ValueError(f"{self._nama} sedang dipinjam")  # [2]
        self._tersedia = False

    def terima_kembali(self):
        self._tersedia = True

    def hitung_denda(self, hari_terlambat: int) -> int:
        return self._denda_per_hari * hari_terlambat

    def __str__(self) -> str:
        status = "tersedia" if self._tersedia else "dipinjam"
        return f"[{self._kode}] {self._nama} - {status}"
```

Salah satu kelas anaknya:

```python
class AlatElektronik(Alat):
    """Alat yang memakai listrik. Tambahan: daya dalam watt."""

    def __init__(self, kode: str, nama: str, daya_watt: int):
        super().__init__(kode, nama, DENDA_ELEKTRONIK)  # [3] konstruktor induk
        if daya_watt <= 0:
            raise ValueError("Daya harus lebih dari 0 watt")
        self._daya_watt = daya_watt

    @property
    def daya_watt(self) -> int:
        return self._daya_watt

    def __str__(self) -> str:
        # [4] override: pakai teks dari induk, lalu tambahkan info daya
        return f"{super().__str__()} | {self._daya_watt} watt"
```

Penjelasan:

- **[1]** Status awal tidak diambil dari parameter. Setiap alat baru otomatis tersedia. Atribut ini hanya dibaca lewat `@property tersedia` dan **tidak punya setter**.
- **[2]** `pinjamkan()` adalah satu-satunya pintu untuk mengubah status menjadi dipinjam. Jika alat sedang dipinjam, method menolak **sebelum** mengubah apa pun.
- **[3]** Kelas anak memanggil konstruktor induk dan mengirim denda per hari yang tetap (`DENDA_ELEKTRONIK = 10000`). Karena itu, `hitung_denda()` cukup ditulis sekali di `Alat`. Pemeriksaan `daya_watt` dilakukan setelahnya, sama seperti urutan di versi Java.
- **[4]** *Override* `__str__` memakai teks buatan induk lewat `super().__str__()`, lalu menambahkan informasi daya. Kelas `KitPraktikum` ditulis dengan pola yang sama.

### Kelas `Peminjaman`

```python
class Peminjaman:
    """Satu transaksi: siapa meminjam, alat apa saja, dan berapa lama."""

    _nomor_terakhir = 0  # [5] atribut kelas: penghitung nomor otomatis

    def __init__(self, peminjam: Mahasiswa, lama_hari: int):
        if lama_hari < 1 or lama_hari > MAKS_HARI_PINJAM:
            raise ValueError(f"Lama pinjam harus 1 sampai {MAKS_HARI_PINJAM} hari")
        Peminjaman._nomor_terakhir += 1  # [6] bertambah HANYA jika data valid
        self._nomor = f"PJ{Peminjaman._nomor_terakhir:03d}"  # PJ001, PJ002, ...
        self._peminjam = peminjam  # [7] asosiasi: menyimpan referensi Mahasiswa
        self._lama_hari = lama_hari
        self._daftar_alat: list[Alat] = []  # [8] agregasi: alat dibuat di luar
        self._selesai = False
```

Dua method terpentingnya:

```python
    def tambah_alat(self, alat: Alat):
        if self._selesai:
            raise ValueError(f"Peminjaman {self._nomor} sudah selesai")
        alat.pinjamkan()  # [9] gagal (ValueError) jika alat sedang dipinjam
        self._daftar_alat.append(alat)

    def kembalikan(self, hari_terlambat: int) -> int:
        """Menerima kembali semua alat lalu MENGEMBALIKAN total denda."""
        if self._selesai:
            raise ValueError(f"Peminjaman {self._nomor} sudah selesai")
        if hari_terlambat < 0:
            raise ValueError("Hari terlambat tidak boleh negatif")
        total_denda = 0
        for alat in self._daftar_alat:  # [10] mengirim pesan ke setiap alat
            alat.terima_kembali()
            total_denda += alat.hitung_denda(hari_terlambat)
        self._selesai = True
        return total_denda
```

Penjelasan:

- **[5]** `_nomor_terakhir` adalah atribut **kelas** (Pertemuan 03): satu penghitung untuk semua objek `Peminjaman`.
- **[6]** Penghitung diubah lewat **nama kelas** (`Peminjaman._nomor_terakhir`), bukan lewat `self`, agar tidak terjadi jebakan atribut bayangan. Penghitung juga baru bertambah setelah `lama_hari` lolos pemeriksaan, sehingga peminjaman 10 hari yang ditolak tidak "menghabiskan" nomor.
- **[7]** Peminjaman hanya **menyimpan referensi** ke objek `Mahasiswa` yang sudah ada (asosiasi).
- **[8]** List alat berisi objek-objek yang dibuat di luar, yaitu yang didaftarkan ke lab (agregasi). Getter `daftar_alat` mengembalikan `list(self._daftar_alat)`, yaitu salinannya.
- **[9]** `pinjamkan()` dipanggil **sebelum** `append`. Jika alat sedang dipinjam, `ValueError` dilempar dan baris `append` tidak pernah dijalankan.
- **[10]** Peminjaman "mengirim pesan" ke setiap alat: terima kembali, lalu hitung dendamu. Total denda **dikembalikan** dengan `return`, bukan dicetak.

Cara menjalankan:

```bash
cd Pertemuan-08-UTS/python/solusi
python soal_c1_peminjaman_alat.py
```

<details>
<summary>Lihat output lengkap Soal C1</summary>

**Output:**

```text
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - tersedia | 200 watt
[A02] Laptop Cadangan - tersedia | 65 watt
[K01] Kit Mikrokontroler - tersedia | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen

=== DATA TIDAK VALID DITOLAK ===
Gagal menambah alat: Daya harus lebih dari 0 watt
Gagal membuat peminjaman: Lama pinjam harus 1 sampai 7 hari
Cari X99: alat tidak ditemukan

=== PEMINJAMAN ===
========================================
BUKTI PEMINJAMAN PJ001
========================================
Peminjam : Ayu Lestari (2409106001)
Lama     : 3 hari
----------------------------------------
Alat                          Denda/hari
[A01] Proyektor Portabel        Rp10.000
[K01] Kit Mikrokontroler         Rp5.000
----------------------------------------
Jumlah alat: 2
========================================
Gagal meminjam: Proyektor Portabel sedang dipinjam
========================================
BUKTI PEMINJAMAN PJ002
========================================
Peminjam : Bima Saputra (2409106002)
Lama     : 2 hari
----------------------------------------
Alat                          Denda/hari
[A02] Laptop Cadangan           Rp10.000
----------------------------------------
Jumlah alat: 1
========================================

=== SETELAH PEMINJAMAN ===
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - dipinjam | 200 watt
[A02] Laptop Cadangan - dipinjam | 65 watt
[K01] Kit Mikrokontroler - dipinjam | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen
Alat tersedia: 1 dari 4

=== PENGEMBALIAN ===
PJ001 kembali terlambat 2 hari, denda Rp30.000
PJ002 kembali tepat waktu, denda Rp0
Gagal mengembalikan: Peminjaman PJ001 sudah selesai

=== STATUS AKHIR ===
=== ALAT Lab Pemrograman ===
[A01] Proyektor Portabel - tersedia | 200 watt
[A02] Laptop Cadangan - tersedia | 65 watt
[K01] Kit Mikrokontroler - tersedia | 30 komponen
[K02] Kit Sensor IoT - tersedia | 12 komponen
Alat tersedia: 4 dari 4
Peminjaman tercatat: 2
```

</details>

> [!TIP]
> **Coba sendiri:** di fungsi `main()`, ubah `proses_pengembalian(pinjam_bima, 0)` menjadi `proses_pengembalian(pinjam_bima, 3)`. Tebak dulu: berapa denda Bima?

<details>
<summary>Lihat jawaban</summary>

Bima hanya meminjam satu alat elektronik (Laptop Cadangan, denda Rp10.000 per hari). Terlambat 3 hari berarti 3 × 10.000, sehingga tercetak `PJ002 kembali terlambat 3 hari, denda Rp30.000`.

</details>

## 2. Soal C2: Toko Buku Daring

File: [`solusi/soal_c2_toko_buku.py`](solusi/soal_c2_toko_buku.py)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Pelanggan` | Menyimpan data pemesan secara *read-only* | `@property`, `__str__` |
| `Produk` | Data produk; harga tervalidasi; stok hanya berkurang lewat method | Setter dengan validasi, method penjaga aturan (P04) |
| `Buku`, `AlatTulis` | Menambah atribut dan meng-*override* `__str__` | Pewarisan (P07) |
| `ItemPesanan` | Satu baris pesanan: produk, jumlah, subtotal, berat | Asosiasi ke `Produk` (P05) |
| `Pesanan` | Nomor otomatis, daftar item, subtotal, ongkir, total, invoice | Komposisi (P05), atribut kelas (P03) |
| `TokoBuku` | Katalog produk, pencarian, catatan pesanan, total penjualan | Agregasi, `None` (P05) |

### Harga dijaga oleh setter

Konstruktor `Produk` mengisi harga **lewat setter**:

```python
    def __init__(self, kode: str, nama: str, harga: int, stok: int,
                 berat_gram: int):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        if berat_gram <= 0:
            raise ValueError("Berat harus lebih dari 0 gram")
        self._kode = kode
        self._nama = nama
        self._stok = stok
        self._berat_gram = berat_gram
        self.harga = harga  # [1] lewat setter, jadi ikut divalidasi
```

Getter dan setter harganya:

```python
    @property
    def harga(self) -> int:
        return self._harga

    @harga.setter
    def harga(self, nilai: int):
        if nilai <= 0:
            # [2] ditolak SEBELUM atribut diubah, jadi harga lama tetap aman
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai
```

Kelas anak `Buku`:

```python
class Buku(Produk):
    """Produk berupa buku. Tambahan: penulis."""

    def __init__(self, kode: str, judul: str, harga: int, stok: int,
                 berat_gram: int, penulis: str):
        super().__init__(kode, judul, harga, stok, berat_gram)  # [3]
        self._penulis = penulis

    @property
    def penulis(self) -> str:
        return self._penulis

    def __str__(self) -> str:
        # [4] override: pakai teks dari induk, lalu tambahkan nama penulis
        return f"{super().__str__()} | penulis {self._penulis}"
```

Penjelasan:

- **[1]** `self.harga = harga` (tanpa garis bawah) **memanggil setter**. Aturan "harga harus lebih dari 0" hanya ditulis sekali, tetapi berlaku saat produk dibuat maupun saat harganya diubah.
- **[2]** Setter memeriksa dulu, baru menyimpan. Itu sebabnya harga Bumi Manusia tetap Rp120.000 setelah percobaan mengisi -5000.
- **[3]** Judul buku dikirim ke induk sebagai `nama`. Semua atribut umum disiapkan oleh konstruktor `Produk`.
- **[4]** Pola *override* yang sama dengan Soal C1 dan dengan `Makanan` di KedaiKita. Kelas `AlatTulis` menambahkan ` | warna ...` dengan cara yang sama.

### Kelas `Pesanan`: komposisi dan perhitungan

```python
    def tambah_item(self, produk: Produk, jumlah: int):
        item = ItemPesanan(produk, jumlah)  # [5] item dibuat OLEH pesanan
        produk.kurangi_stok(jumlah)  # [6] gagal (ValueError) jika stok kurang
        self._daftar_item.append(item)  # [7] hanya disimpan jika semua lolos

    def hitung_subtotal(self) -> int:
        subtotal = 0
        for item in self._daftar_item:
            subtotal += item.hitung_subtotal()
        return subtotal

    def hitung_berat_kg(self) -> int:
        """Total berat dalam kg, DIBULATKAN KE ATAS (1080 gram -> 2 kg)."""
        berat_gram = 0
        for item in self._daftar_item:
            berat_gram += item.hitung_berat()
        return (berat_gram + 999) // 1000  # [8] pembulatan ke atas tanpa float

    def hitung_ongkir(self) -> int:
        if self.hitung_subtotal() >= BATAS_GRATIS_ONGKIR:
            return 0
        return self.hitung_berat_kg() * ONGKIR_PER_KG
```

Penjelasan:

- **[5]** Objek `ItemPesanan` dibuat **di dalam** pesanan, sehingga hubungannya komposisi. Konstruktor `ItemPesanan` sekaligus memeriksa jumlah, jadi jumlah 0 sudah ditolak di langkah ini, sebelum stok tersentuh.
- **[6]** Stok hanya berkurang lewat `kurangi_stok()`, yang menolak permintaan melebihi stok.
- **[7]** Item baru disimpan setelah kedua pemeriksaan lolos. Jika salah satu gagal, `ValueError` menghentikan method sebelum baris ini.
- **[8]** `(berat_gram + 999) // 1000` membulatkan ke atas tanpa bilangan pecahan: 720 menjadi 1, 1080 menjadi 2, dan 1000 tetap 1.

Cara menjalankan:

```bash
cd Pertemuan-08-UTS/python/solusi
python soal_c2_toko_buku.py
```

<details>
<summary>Lihat output lengkap Soal C2</summary>

**Output:**

```text
=== KATALOG PustakaKita ===
[B01] Laskar Pelangi - Rp95.000 | stok 5 | penulis Andrea Hirata
[B02] Bumi Manusia - Rp120.000 | stok 3 | penulis Pramoedya Ananta Toer
[B03] Negeri 5 Menara - Rp89.000 | stok 2 | penulis Ahmad Fuadi
[T01] Pulpen Gel - Rp8.000 | stok 50 | warna hitam
[T02] Map Plastik - Rp5.000 | stok 40 | warna biru

=== DATA TIDAK VALID DITOLAK ===
Gagal menambah produk: Harga harus lebih dari 0
Gagal mengubah harga: Harga harus lebih dari 0
Harga Bumi Manusia tetap Rp120.000
Cari B99: produk tidak ditemukan

=== PESANAN ===
========================================
INVOICE INV001
========================================
Pelanggan : Siti Aminah (siti@contoh.id)
----------------------------------------
2 x Laskar Pelangi             Rp190.000
2 x Pulpen Gel                  Rp16.000
----------------------------------------
Subtotal                       Rp206.000
Ongkir (1 kg)                     GRATIS
TOTAL                          Rp206.000
========================================
Gagal menambah item: Stok Negeri 5 Menara tidak cukup (sisa 2)
Gagal menambah item: Jumlah harus lebih dari 0
========================================
INVOICE INV002
========================================
Pelanggan : Budi Santoso (budi@contoh.id)
----------------------------------------
2 x Negeri 5 Menara            Rp178.000
3 x Map Plastik                 Rp15.000
----------------------------------------
Subtotal                       Rp193.000
Ongkir (2 kg)                   Rp20.000
TOTAL                          Rp213.000
========================================

=== RINGKASAN ===
=== KATALOG PustakaKita ===
[B01] Laskar Pelangi - Rp95.000 | stok 3 | penulis Andrea Hirata
[B02] Bumi Manusia - Rp120.000 | stok 3 | penulis Pramoedya Ananta Toer
[B03] Negeri 5 Menara - Rp89.000 | stok 0 | penulis Ahmad Fuadi
[T01] Pulpen Gel - Rp8.000 | stok 48 | warna hitam
[T02] Map Plastik - Rp5.000 | stok 37 | warna biru
Jumlah pesanan : 2
Total penjualan: Rp419.000
```

</details>

> [!TIP]
> **Coba sendiri:** ubah konstanta `BATAS_GRATIS_ONGKIR` di bagian atas file menjadi `150000`. Tebak dulu: apa yang berubah pada invoice Budi dan pada total penjualan?

<details>
<summary>Lihat jawaban</summary>

Subtotal Budi Rp193.000 kini sudah mencapai batas, sehingga ongkirnya menjadi `GRATIS` dan totalnya Rp193.000. Total penjualan menjadi Rp206.000 + Rp193.000 = **Rp399.000**. Cukup satu angka yang diubah, karena aturan itu disimpan sebagai konstanta.

</details>

## 3. Membandingkan Output-mu dengan Solusi

Targetnya, output programmu **sama persis** dengan contoh output di soal. Mencocokkan dengan mata itu melelahkan, jadi biarkan komputer yang membandingkan. Simpan output kedua program ke file teks:

```bash
python jawabanku.py > hasil_saya.txt
python soal_c1_peminjaman_alat.py > hasil_solusi.txt
```

Lalu bandingkan:

- **Command Prompt (Windows):** `fc hasil_saya.txt hasil_solusi.txt`
- **PowerShell (Windows):** `fc.exe hasil_saya.txt hasil_solusi.txt` (di PowerShell, `fc` tanpa `.exe` berarti perintah lain)
- **macOS/Linux:** `diff hasil_saya.txt hasil_solusi.txt`. Jika tidak ada yang tercetak, berarti kedua file sama.
- **VS Code:** klik kanan file pertama, pilih *Select for Compare*, lalu klik kanan file kedua dan pilih *Compare with Selected*.

> [!TIP]
> Perbedaan yang paling sering ditemukan adalah spasi di akhir baris, huruf besar/kecil pada pesan error, dan lebar kolom. Salin teks pesan langsung dari soal agar tidak salah ketik.

## 4. Kesalahan Umum dan Cara Membaca Pesan Error

Ingat, pesan error Python dibaca **dari bawah ke atas**: baris terakhir menyebutkan jenis error, dan baris-baris di atasnya menunjukkan jejak lokasinya.

### Kesalahan 1: Lupa memanggil `super().__init__()`

```python
class AlatElektronik(Alat):
    def __init__(self, kode, nama, daya_watt):
        self._daya_watt = daya_watt  # lupa super().__init__(kode, nama)
```

Saat objeknya dicetak, pesan error-nya:

```text
Traceback (most recent call last):
  File "contoh.py", line 19, in <module>
    print(proyektor)
  File "contoh.py", line 15, in __str__
    return f"{super().__str__()} | {self._daya_watt} watt"
  File "contoh.py", line 7, in __str__
    return f"[{self._kode}] {self._nama}"
AttributeError: 'AlatElektronik' object has no attribute '_kode'
```

**Artinya:** konstruktor induk tidak pernah berjalan, sehingga atribut `_kode` dan `_nama` tidak pernah dibuat. Error-nya baru muncul ketika atribut itu dibaca, jauh dari tempat kesalahan sebenarnya. **Perbaikan:** panggil `super().__init__(...)` di awal konstruktor anak.

### Kesalahan 2: Setter memanggil dirinya sendiri

```python
    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self.harga = nilai  # salah: seharusnya self._harga
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "contoh.py", line 16, in <module>
    buku = Produk(95000)
  File "contoh.py", line 3, in __init__
    self.harga = harga
  File "contoh.py", line 13, in harga
    self.harga = nilai  # salah: seharusnya self._harga
  File "contoh.py", line 13, in harga
    self.harga = nilai  # salah: seharusnya self._harga
  File "contoh.py", line 13, in harga
    self.harga = nilai  # salah: seharusnya self._harga
  [Previous line repeated 995 more times]
RecursionError: maximum recursion depth exceeded
```

**Artinya:** `self.harga = nilai` di dalam setter memanggil setter yang sama lagi, terus-menerus, sampai Python menyerah. **Perbaikan:** di dalam setter, simpan ke atribut berawalan garis bawah: `self._harga = nilai`.

### Kesalahan 3: Mengisi atribut *read-only*

```python
alat = Alat("A01")
alat.kode = "A99"
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "contoh.py", line 11, in <module>
    alat.kode = "A99"
AttributeError: property 'kode' of 'Alat' object has no setter
```

**Artinya:** `kode` dibuat dengan `@property` tanpa setter, jadi memang tidak boleh diubah dari luar. Enkapsulasinya bekerja! Di Python 3.10, pesannya berbunyi `can't set attribute 'kode'`. **Perbaikan:** jika suatu data memang perlu diubah, sediakan setter yang memvalidasi atau method khusus. Jika tidak, biarkan *read-only*.

### Kesalahan 4: Memakai hasil pencarian yang ternyata `None`

```python
alat = lab.cari_alat("A09")
alat.pinjamkan()
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "contoh.py", line 14, in <module>
    alat.pinjamkan()
AttributeError: 'NoneType' object has no attribute 'pinjamkan'
```

**Artinya:** alat berkode A09 tidak ada, sehingga `cari_alat` mengembalikan `None`, dan `None` tidak punya method `pinjamkan`. **Perbaikan:** periksa dulu dengan `if alat is None:` sebelum memakai hasil pencarian.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Python 3.11 ke atas juga menambahkan tanda `^^^^` di bawah bagian kode yang bermasalah. Fokuslah pada **jenis error** di baris terakhir dan pada nomor barisnya.

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Java: [☕ Solusi Java](../java/README.md). Kelas, urutan langkah, dan output-nya sama persis.
- Baca pembahasan rancangannya: [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).
- Kembali ke [Informasi UTS](../README.md) untuk mengecek checklist kesiapanmu.

---

[⬅️ Informasi UTS](../README.md) · [☕ Solusi Java](../java/README.md) · [Pembahasan ➡️](../pembahasan.md)
