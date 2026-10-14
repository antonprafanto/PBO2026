# 🐍 Solusi Praktik Python Pertemuan 08: UTS

[⬅️ Informasi UTS](../README.md) · [☕ Solusi Java](../java/README.md) · [Pembahasan ➡️](../pembahasan.md)

> **Prasyarat:** sudah mencoba sendiri [Soal C1 dan C2](../latihan-soal.md#bagian-c-soal-praktik). Halaman ini menjelaskan cara menjalankan solusi Python, bagian-bagian terpenting kodenya, dan cara membandingkan *output* jawabanmu dengan solusi. Alasan pemilihan kelas dan relasi dibahas di [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Solusi](#cara-menjalankan-solusi)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membandingkan Jawabanmu dengan Solusi](#cara-membandingkan-jawabanmu-dengan-solusi)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Soal C1: Peminjaman Alat Laboratorium](#1-soal-c1-peminjaman-alat-laboratorium)
2. [Soal C2: Toko Buku Daring](#2-soal-c2-toko-buku-daring)
3. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#3-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
└── solusi/
    ├── soal_c1_peminjaman_alat.py   <- solusi Soal C1
    └── soal_c2_toko_buku.py         <- solusi Soal C2
```

Setiap solusi ditulis dalam **satu *file*** agar mudah dibaca dan dikumpulkan. Di proyek sungguhan, kelas-kelasnya bisa dipecah ke beberapa *file* seperti KedaiKita sejak Pertemuan 05. Untuk ujian yang sebenarnya, ikuti aturan pengumpulan dari dosen.

### Cara Menjalankan Solusi

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-08-UTS/python`. Di panel **Explorer**, buka folder `solusi`, klik *file* yang ingin dicoba (misalnya `soal_c1_peminjaman_alat.py`), lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah. Baris pertama di panel itu berisi perintah panjang yang diketik VS Code secara otomatis; *output* programmu muncul di bawahnya.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-08-UTS/python/solusi` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd solusi` |

Setelah itu, jalankan solusi yang kamu inginkan:

```bash
python soal_c1_peminjaman_alat.py
python soal_c2_toko_buku.py
```

Baris pertama yang tercetak adalah `=== ALAT Lab Pemrograman ===` (Soal C1) atau `=== KATALOG PustakaKita ===` (Soal C2). *Output* lengkapnya ada di bagian 1 dan 2, dan sama persis dengan contoh *output* di soal.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `solusi`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya. Solusi ini membutuhkan Python 3.10 atau lebih baru karena memakai petunjuk tipe seperti `Alat | None`.

### Tempat Menyimpan Kodemu Sendiri

Kerjakan Soal C1 dan C2 di folder milikmu sendiri **di luar** folder materi, yaitu `PBO-latihan-saya/uts/` (aturan emasnya ada di [Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri)). Folder materi cukup dibaca dan dijalankan, tidak diubah. Susunan yang disarankan:

```text
Documents/
├── PBO2026/                    <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/           <- milikmu sendiri
    └── uts/
        ├── jawaban_c1.py       <- jawabanmu untuk Soal C1
        ├── jawaban_c2.py       <- jawabanmu untuk Soal C2
        └── coba/               <- tempat bereksperimen dengan salinan solusi
```

Untuk mengerjakan jawabanmu, buka folder `uts` di jendela VS Code baru (**File → New Window**, lalu **File → Open Folder**). Ingin bereksperimen dengan kode solusi, misalnya untuk "Coba sendiri" atau kesalahan di bagian 3? Salin dulu *file* solusinya dari folder `Pertemuan-08-UTS/python/solusi` ke folder `uts/coba` lewat File Explorer (Windows) atau Finder (macOS), lalu ubah salinannya. *File* di folder materi tetap utuh.

### Cara Membandingkan Jawabanmu dengan Solusi

Targetnya, *output* programmu **sama persis** dengan contoh *output* di soal, yang juga sama dengan *output* solusi. Biarkan komputer yang membandingkan karena mata mudah melewatkan satu spasi. Contoh di bawah memakai Soal C1.

1. **Salin *file* solusi yang ingin dibandingkan**, yaitu `soal_c1_peminjaman_alat.py`, ke folder `PBO-latihan-saya/uts`. Salinan ini jangan diubah karena menjadi patokan.
2. **Buka terminal di folder `uts` itu.** Caranya: di VS Code yang sedang membuka folder `uts`, pilih **Terminal → New Terminal**. Ketik `dir` (Windows) atau `ls` (macOS/Linux), lalu pastikan `jawaban_c1.py` dan `soal_c1_peminjaman_alat.py` muncul di daftar.
3. **Simpan *output* kedua program ke *file* teks.** Tanda `>` artinya "jangan tampilkan hasilnya di layar, tetapi tulis ke *file* ini":

   ```bash
   python jawaban_c1.py > hasil_saya.txt
   python soal_c1_peminjaman_alat.py > hasil_solusi.txt
   ```

   Kedua perintah itu tidak menampilkan apa-apa di layar, kecuali jika programmu berhenti karena *error*. Di macOS/Linux, ketik `python3`.
4. **Bandingkan kedua *file*** dengan perintah yang sesuai dengan terminalmu:

   | Terminal | Perintah | Jika kedua *file* sama persis |
   |---|---|---|
   | Windows: Command Prompt | `fc hasil_saya.txt hasil_solusi.txt` | muncul `FC: no differences encountered` |
   | Windows: PowerShell (terminal bawaan VS Code) | `fc.exe hasil_saya.txt hasil_solusi.txt` | sama seperti di atas |
   | macOS/Linux | `diff hasil_saya.txt hasil_solusi.txt` | tidak ada yang tercetak |

   Di PowerShell, `fc` tanpa `.exe` berarti perintah lain, jadi selalu tulis `fc.exe`. Jika ada perbedaan, perintah itu menampilkan baris-baris yang tidak sama dari kedua *file*.

Lebih suka cara klik? Di panel **Explorer** VS Code, klik kanan `hasil_saya.txt`, pilih **Select for Compare**, lalu klik kanan `hasil_solusi.txt` dan pilih **Compare with Selected**. VS Code menandai baris yang berbeda dengan warna. Untuk Soal C2, pakai `jawaban_c2.py` dan salinan `soal_c2_toko_buku.py`.

> [!TIP]
> Perbedaan yang paling sering ditemukan adalah spasi di akhir baris, huruf besar/kecil pada pesan *error*, dan lebar kolom. Salin teks pesan langsung dari soal agar tidak salah ketik.

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal bagian 1 dan 2 menunjuk *file* solusinya. Klik untuk melihat isi lengkapnya.
- Blok kode di bawahnya adalah **potongan** penting dari *file* itu, disalin persis. Jangan menjalankan potongannya sendiri. Jalankan *file* lengkapnya dengan cara di atas.
- Tanda `# [1]`, `# [2]`, dan seterusnya di komentar kode dijelaskan di daftar **Penjelasan** di bawah blok kodenya.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.
- Kode di bagian 3 sengaja dibuat **salah** untuk menunjukkan pesan *error*. Jangan ditiru.

## 1. Soal C1: Peminjaman Alat Laboratorium

*File*: [`solusi/soal_c1_peminjaman_alat.py`](solusi/soal_c1_peminjaman_alat.py)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Mahasiswa` | Menyimpan data peminjam secara *read-only* | `@property` tanpa *setter* (P04), `__str__` (P03) |
| `Alat` | Menyimpan data dan status alat; meminjamkan, menerima kembali, menghitung denda | Enkapsulasi, *method* penjaga aturan (P04) |
| `AlatElektronik`, `KitPraktikum` | Menambah atribut, menentukan denda per hari, meng-*override* `__str__` | Pewarisan, `super()` (P07) |
| `Peminjaman` | Nomor otomatis, daftar alat, pengembalian dan denda, bukti peminjaman | Atribut kelas (P03), agregasi dan asosiasi (P05) |
| `Laboratorium` | Daftar alat, pencarian alat, catatan peminjaman | Agregasi, `None` (P05) |

### Kelas induk `Alat` dan kelas anaknya

Bagian awal kelas `Alat` (potongan dari *file* di atas):

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

Setelah deretan `@property`, kelas `Alat` punya *method* berikut:

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

Salah satu kelas anaknya, `AlatElektronik`:

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

- **[1]** Status awal tidak diambil dari parameter. Setiap alat baru otomatis tersedia. Atribut ini hanya dibaca lewat `@property tersedia` dan **tidak punya *setter***.
- **[2]** `pinjamkan()` adalah satu-satunya pintu untuk mengubah status menjadi dipinjam. Jika alat sedang dipinjam, *method* menolak **sebelum** mengubah apa pun.
- **[3]** Kelas anak memanggil konstruktor induk dan mengirim denda per hari yang tetap, yaitu konstanta `DENDA_ELEKTRONIK = 10000` di bagian atas *file*. Karena itu, `hitung_denda()` cukup ditulis sekali di `Alat`. Pemeriksaan `daya_watt` dilakukan setelahnya, sama seperti urutan di versi Java.
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

Dua *method* terpentingnya:

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
- **[6]** Penghitung diubah lewat **nama kelas** (`Peminjaman._nomor_terakhir`), bukan lewat `self` agar tidak terjadi jebakan atribut bayangan. Penghitung juga baru bertambah setelah `lama_hari` lolos pemeriksaan sehingga peminjaman 10 hari yang ditolak tidak "menghabiskan" nomor.
- **[7]** Peminjaman hanya **menyimpan referensi** ke objek `Mahasiswa` yang sudah ada (asosiasi).
- **[8]** *List* alat berisi objek-objek yang dibuat di luar, yaitu yang didaftarkan ke lab (agregasi). *Getter* `daftar_alat` mengembalikan `list(self._daftar_alat)`, yaitu salinannya.
- **[9]** `pinjamkan()` dipanggil **sebelum** `append`. Jika alat sedang dipinjam, `ValueError` dilempar dan baris `append` tidak pernah dijalankan.
- **[10]** Peminjaman "mengirim pesan" ke setiap alat: terima kembali, lalu hitung dendamu. Total denda **dikembalikan** dengan `return`, bukan dicetak.

Cara menjalankannya dijelaskan di [Persiapan](#cara-menjalankan-solusi). Ringkasnya, dari folder utama materi:

```bash
cd Pertemuan-08-UTS/python/solusi
python soal_c1_peminjaman_alat.py
```

<details>
<summary>Lihat hasil lengkap Soal C1</summary>

***Output:***

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
> **Coba sendiri:** buka salinan `soal_c1_peminjaman_alat.py` di folder latihanmu (`PBO-latihan-saya/uts/coba`). Di fungsi `main()` salinan itu, ubah `proses_pengembalian(pinjam_bima, 0)` menjadi `proses_pengembalian(pinjam_bima, 3)`, simpan, lalu jalankan. Tebak dulu: berapa denda Bima?

<details>
<summary>Lihat jawaban</summary>

Bima hanya meminjam satu alat elektronik (Laptop Cadangan, denda Rp10.000 per hari). Terlambat 3 hari berarti 3 × Rp10.000 sehingga baris itu berubah menjadi `PJ002 kembali terlambat 3 hari, denda Rp30.000`. Baris lainnya tetap sama.

</details>

## 2. Soal C2: Toko Buku Daring

*File*: [`solusi/soal_c2_toko_buku.py`](solusi/soal_c2_toko_buku.py)

**Peta kelas:**

| Kelas | Tanggung jawab | Konsep |
|---|---|---|
| `Pelanggan` | Menyimpan data pemesan secara *read-only* | `@property`, `__str__` |
| `Produk` | Data produk; harga tervalidasi; stok hanya berkurang lewat *method* | *Setter* dengan validasi, *method* penjaga aturan (P04) |
| `Buku`, `AlatTulis` | Menambah atribut dan meng-*override* `__str__` | Pewarisan (P07) |
| `ItemPesanan` | Satu baris pesanan: produk, jumlah, subtotal, berat | Asosiasi ke `Produk` (P05) |
| `Pesanan` | Nomor otomatis, daftar item, subtotal, ongkos kirim (ongkir), total, *invoice* | Komposisi (P05), atribut kelas (P03) |
| `TokoBuku` | Katalog produk, pencarian, catatan pesanan, total penjualan | Agregasi, `None` (P05) |

### Harga dijaga oleh *setter*

Konstruktor `Produk` mengisi harga **lewat *setter*** (potongan dari *file* di atas):

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

*Getter* dan *setter* harganya:

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

- **[1]** `self.harga = harga` (tanpa garis bawah) **memanggil *setter***. Aturan "harga harus lebih dari 0" hanya ditulis sekali, tetapi berlaku saat produk dibuat maupun saat harganya diubah.
- **[2]** *Setter* memeriksa dulu, baru menyimpan. Itu sebabnya harga Bumi Manusia tetap Rp120.000 setelah percobaan mengisi -5000.
- **[3]** Judul buku dikirim ke induk sebagai `nama`. Semua atribut umum disiapkan oleh konstruktor `Produk`.
- **[4]** Pola *override* yang sama dengan Soal C1 dan dengan `Makanan` di KedaiKita. Kelas `AlatTulis` menambahkan ` | warna ...` dengan cara yang sama.

### Kelas `Pesanan`: komposisi dan perhitungan

Empat *method* milik kelas `Pesanan`:

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

- **[5]** Objek `ItemPesanan` dibuat **di dalam** pesanan sehingga hubungannya komposisi. Konstruktor `ItemPesanan` sekaligus memeriksa jumlah, jadi jumlah 0 sudah ditolak di langkah ini, sebelum stok tersentuh.
- **[6]** Stok hanya berkurang lewat `kurangi_stok()`, yang menolak permintaan melebihi stok.
- **[7]** Item baru disimpan setelah kedua pemeriksaan lolos. Jika salah satu gagal, `ValueError` menghentikan *method* sebelum baris ini.
- **[8]** `(berat_gram + 999) // 1000` membulatkan ke atas tanpa bilangan pecahan: 720 gram menjadi 1 kg, 1.080 gram menjadi 2 kg, dan 1.000 gram tetap 1 kg. Operator `//` adalah pembagian bulat (hasilnya dibulatkan ke bawah), jadi tambahan 999 itulah yang membuatnya "naik" ke kilogram berikutnya.

Dari folder utama materi:

```bash
cd Pertemuan-08-UTS/python/solusi
python soal_c2_toko_buku.py
```

<details>
<summary>Lihat hasil lengkap Soal C2</summary>

***Output:***

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
> **Coba sendiri:** buka salinan `soal_c2_toko_buku.py` di folder latihanmu (`PBO-latihan-saya/uts/coba`). Di bagian atas salinan itu, ubah konstanta `BATAS_GRATIS_ONGKIR` menjadi `150000`, simpan, lalu jalankan. Tebak dulu: apa yang berubah pada *invoice* Budi dan pada total penjualan?

<details>
<summary>Lihat jawaban</summary>

Subtotal Budi Rp193.000 kini sudah mencapai batas sehingga ongkirnya menjadi `GRATIS` dan totalnya Rp193.000. Total penjualan menjadi Rp206.000 + Rp193.000 = **Rp399.000**. Cukup satu angka yang diubah karena aturan itu disimpan sebagai konstanta.

</details>

## 3. Kesalahan Umum dan Cara Membaca Pesan *Error*

Ingat, pesan *error* Python dibaca **dari bawah ke atas**: baris terakhir menyebutkan jenis *error*, dan baris-baris di atasnya menunjukkan jejak lokasinya.

Setiap kesalahan di bawah ini dibuat dengan mengubah sedikit **salinan** *file* solusi di folder latihanmu (`PBO-latihan-saya/uts/coba`), lalu menjalankannya. Jadi, kamu bisa mencobanya sendiri. Jangan ubah *file* solusi di folder materi. Setelah selesai mencoba satu kesalahan, salin ulang *file* solusi dari folder materi agar salinanmu kembali utuh. Alamat *file* di pesan *error* sengaja disingkat menjadi nama *file*-nya saja.

### Kesalahan 1: Lupa memanggil `super().__init__()`

Di salinan `soal_c1_peminjaman_alat.py`, hapus baris `super().__init__(kode, nama, DENDA_ELEKTRONIK)` dari konstruktor `AlatElektronik`. Konstruktornya kini menjadi seperti ini (kode yang salah, jangan ditiru):

```python
    def __init__(self, kode: str, nama: str, daya_watt: int):
        if daya_watt <= 0:
            raise ValueError("Daya harus lebih dari 0 watt")
        self._daya_watt = daya_watt
```

Saat dijalankan, baris `=== ALAT Lab Pemrograman ===` masih tercetak, lalu program berhenti dengan pesan *error* ini:

```text
Traceback (most recent call last):
  File "soal_c1_peminjaman_alat.py", line 326, in <module>
    main()
    ~~~~^^
  File "soal_c1_peminjaman_alat.py", line 274, in main
    lab.tampilkan_alat()
    ~~~~~~~~~~~~~~~~~~^^
  File "soal_c1_peminjaman_alat.py", line 244, in tampilkan_alat
    print(alat)  # memanggil __str__ milik kelas anak
    ~~~~~^^^^^^
  File "soal_c1_peminjaman_alat.py", line 109, in __str__
    return f"{super().__str__()} | {self._daya_watt} watt"
              ~~~~~~~~~~~~~~~^^
  File "soal_c1_peminjaman_alat.py", line 91, in __str__
    status = "tersedia" if self._tersedia else "dipinjam"
                           ^^^^^^^^^^^^^^
AttributeError: 'AlatElektronik' object has no attribute '_tersedia'. Did you mean: 'tersedia'?
```

**Artinya:** konstruktor induk tidak pernah berjalan sehingga atribut `_kode`, `_nama`, `_denda_per_hari`, dan `_tersedia` tidak pernah dibuat. Python tidak protes saat objeknya dibuat. *Error* baru muncul ketika atribut induk pertama kali dibaca, yaitu `_tersedia` di `__str__` milik `Alat`, jauh dari tempat kesalahan sebenarnya. Saran *Did you mean: 'tersedia'?* kali ini menyesatkan: masalahnya bukan salah ketik. **Perbaikan:** panggil `super().__init__(kode, nama, DENDA_ELEKTRONIK)` di baris pertama konstruktor anak.

### Kesalahan 2: *Setter* memanggil dirinya sendiri

Di salinan `soal_c2_toko_buku.py`, ubah baris terakhir *setter* harga dari `self._harga = nilai` menjadi `self.harga = nilai` (kode yang salah, jangan ditiru):

```python
    @harga.setter
    def harga(self, nilai: int):
        if nilai <= 0:
            # [2] ditolak SEBELUM atribut diubah, jadi harga lama tetap aman
            raise ValueError("Harga harus lebih dari 0")
        self.harga = nilai
```

Program langsung berhenti saat membuat produk pertama. Pesan *error*-nya sangat panjang. Bagian akhirnya seperti ini:

```text
  File "soal_c2_toko_buku.py", line 62, in __init__
    self.harga = harga  # [1] lewat setter, jadi ikut divalidasi
    ^^^^^^^^^^
  File "soal_c2_toko_buku.py", line 89, in harga
    self.harga = nilai
    ^^^^^^^^^^
  File "soal_c2_toko_buku.py", line 89, in harga
    self.harga = nilai
    ^^^^^^^^^^
  File "soal_c2_toko_buku.py", line 89, in harga
    self.harga = nilai
    ^^^^^^^^^^
  [Previous line repeated 992 more times]
RecursionError: maximum recursion depth exceeded
```

**Artinya:** di dalam *setter*, `self.harga = nilai` memanggil *setter* yang sama lagi, lalu lagi, terus-menerus, sampai Python menyerah setelah sekitar seribu panggilan. Angka 992 bisa sedikit berbeda di komputermu. Di Python 3.10, baris terakhirnya berbunyi `RecursionError: maximum recursion depth exceeded in comparison`. **Perbaikan:** di dalam *setter*, simpan nilainya ke atribut berawalan garis bawah: `self._harga = nilai`.

### Kesalahan 3: Mengisi atribut *read-only*

Di salinan `soal_c1_peminjaman_alat.py`, tambahkan dua baris berikut tepat di bawah baris `lab = siapkan_lab()` di fungsi `main()` (kode yang salah, jangan ditiru):

```python
    proyektor = lab.cari_alat("A01")
    proyektor.kode = "A99"
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "soal_c1_peminjaman_alat.py", line 329, in <module>
    main()
    ~~~~^^
  File "soal_c1_peminjaman_alat.py", line 276, in main
    proyektor.kode = "A99"
    ^^^^^^^^^^^^^^
AttributeError: property 'kode' of 'AlatElektronik' object has no setter
```

**Artinya:** `kode` dibuat dengan `@property` tanpa *setter*, jadi memang tidak boleh diubah dari luar. Enkapsulasinya bekerja! Pesan itu menyebut `AlatElektronik` karena objek A01 adalah alat elektronik, sedangkan *property* `kode` sendiri diwarisi dari `Alat`. Di Python 3.10, pesannya berbunyi `AttributeError: can't set attribute 'kode'`. **Perbaikan:** jika suatu data memang perlu diubah, sediakan *setter* yang memvalidasi atau *method* khusus. Jika tidak, biarkan *read-only*.

### Kesalahan 4: Memakai hasil pencarian yang ternyata `None`

Di salinan `soal_c1_peminjaman_alat.py`, tambahkan dua baris berikut tepat di bawah baris `lab = siapkan_lab()` di fungsi `main()` (kode yang salah, jangan ditiru):

```python
    alat = lab.cari_alat("A09")
    alat.pinjamkan()
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "soal_c1_peminjaman_alat.py", line 329, in <module>
    main()
    ~~~~^^
  File "soal_c1_peminjaman_alat.py", line 276, in main
    alat.pinjamkan()
    ^^^^^^^^^^^^^^
AttributeError: 'NoneType' object has no attribute 'pinjamkan'
```

**Artinya:** alat berkode A09 tidak ada sehingga `cari_alat` mengembalikan `None`, dan `None` tidak punya *method* `pinjamkan`. **Perbaikan:** periksa dulu dengan `if alat is None:` sebelum memakai hasil pencarian, seperti pencarian `X99` di fungsi `main()` solusi.

> [!NOTE]
> Pesan di atas diambil dari Python 3.13. Bunyinya bisa sedikit berbeda antarversi Python. Mulai Python 3.11, di bawah sebagian baris juga muncul tanda `^` (kadang bersama `~`) yang menunjuk bagian kode yang bermasalah. Fokuslah pada **jenis *error*** di baris terakhir dan pada nomor barisnya.

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Java: [☕ Solusi Java](../java/README.md). Kelas, urutan langkah, dan *output*-nya sama persis.
- Baca pembahasan rancangannya: [Pembahasan Bagian C](../pembahasan.md#pembahasan-bagian-c).
- Kembali ke [Informasi UTS](../README.md) untuk mengecek *checklist* kesiapanmu.

---

[⬅️ Informasi UTS](../README.md) · [☕ Solusi Java](../java/README.md) · [Pembahasan ➡️](../pembahasan.md)
