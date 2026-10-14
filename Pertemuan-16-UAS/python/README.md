# 🐍 Solusi Praktik Python Pertemuan 16: UAS

[⬅️ Pembahasan](../pembahasan.md) · [☕ Solusi Java](../java/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)

> **Prasyarat:** sudah mencoba sendiri [soal praktik](../latihan-soal.md#bagian-c-soal-praktik) dan membaca [pembahasan desainnya](../pembahasan.md#bagian-c-soal-praktik). Halaman ini membedah kode solusinya bagian demi bagian. Semua kode ada di folder `solusi/` dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
  - [Cara Menjalankan Solusi](#cara-menjalankan-solusi)
  - [Tempat Menyimpan Kodemu Sendiri](#tempat-menyimpan-kodemu-sendiri)
  - [Cara Membandingkan Jawabanmu dengan Solusi](#cara-membandingkan-jawabanmu-dengan-solusi)
  - [Cara Membaca Kode di Halaman Ini](#cara-membaca-kode-di-halaman-ini)

1. [Soal C1: Sistem Pemesanan Tiket Bioskop](#1-soal-c1-sistem-pemesanan-tiket-bioskop)
2. [Soal C2: *Refactor* Kasir *Laundry*](#2-soal-c2-refactor-kasir-laundry)
3. [Membuktikan *Output* Tidak Berubah](#3-membuktikan-output-tidak-berubah)
4. [Kesalahan Umum dan Cara Membaca Pesan *Error*](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

**Yang perlu sudah siap:** Python 3.10 atau lebih baru, VS Code dengan ekstensi Python, dan materi ini sudah ada di laptopmu. Belum? Ikuti dulu [00-Persiapan](../../00-Persiapan/README.md).

Struktur folder Python pertemuan ini:

```text
python/
└── solusi/
    ├── soal_c1_tiket_bioskop.py   <- solusi Soal C1
    ├── soal_c2_sebelum.py         <- Soal C2: kode awal yang berantakan
    └── soal_c2_sesudah.py         <- Soal C2: hasil refactor
```

Setiap solusi sengaja dibuat **satu *file*** dan hanya memakai pustaka standar agar mudah dijalankan dan dibandingkan. Di proyek sungguhan, kelas-kelasnya sebaiknya dipisah ke beberapa modul, seperti KedaiKita sejak Pertemuan 05. Saat ujian, ikuti aturan pengumpulan dari dosen.

### Cara Menjalankan Solusi

Pilih salah satu cara. Hasilnya sama.

**Cara 1: tombol ▷ di VS Code (paling mudah).** Di VS Code, pilih **File → Open Folder**, lalu buka folder `Pertemuan-16-UAS/python`. Di panel **Explorer**, buka folder `solusi`, klik *file* yang ingin dijalankan (misalnya `soal_c1_tiket_bioskop.py`), lalu klik tombol ▷ (**Run Python File**) di pojok kanan atas. Hasilnya muncul di panel **TERMINAL** di bagian bawah.

**Cara 2: lewat terminal.** Buka terminal, pastikan kamu berada di folder yang tepat, lalu ketik perintahnya.

| Terminalmu sedang berada di ... | Ketik dulu |
|---|---|
| folder utama materi (`PBO2026` atau `PBO2026-master`) | `cd Pertemuan-16-UAS/python/solusi` |
| folder `python` pertemuan ini (terminal VS Code setelah langkah Cara 1) | `cd solusi` |

Setelah itu, jalankan *file* yang ingin kamu lihat, satu perintah setiap kali:

```bash
python soal_c1_tiket_bioskop.py
python soal_c2_sebelum.py
python soal_c2_sesudah.py
```

Baris pertama *output* Soal C1 adalah `=== JADWAL TAYANG BioskopKita ===`. Kedua program Soal C2 diawali garis `====================================` dan *output*-nya sama persis. *Output* lengkapnya ada di bagian 1 dan 2.

> [!TIP]
> Cara paling cepat membuka terminal tepat di folder yang benar: di panel **Explorer** VS Code, klik kanan folder `solusi`, lalu pilih **Open in Integrated Terminal**. Kamu tidak perlu mengetik `cd` lagi.

> [!NOTE]
> Di macOS/Linux, ketik `python3` sebagai ganti `python`. Semua perintah `cd` di halaman ini ditulis dari **folder utama materi**. Jika terminalmu sudah berada di folder tujuan, lewati baris `cd`-nya.

### Tempat Menyimpan Kodemu Sendiri

Jawaban latihan UAS-mu jangan disimpan di folder materi, termasuk di folder `solusi/`. Simpan di folder milikmu sendiri **di luar** folder materi, misalnya `PBO-latihan-saya/uas`, agar pekerjaanmu tidak tertimpa saat materi diperbarui (lihat [aturan emas di Git dan GitHub bagian 5](../../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri)).

```text
Documents/
├── PBO2026/                     <- materi kuliah (jangan diubah)
└── PBO-latihan-saya/            <- milikmu sendiri
    └── uas/
        ├── jawaban_c1.py        <- jawabanmu untuk Soal C1
        ├── jawaban_c2.py        <- jawabanmu untuk Soal C2 (hasil refactor-mu)
        ├── soal_c2_sebelum.py   <- salinan kode awal Soal C2
        └── coba/                <- tempat bereksperimen dengan salinan solusi
```

Ingin bereksperimen dengan kode solusi, misalnya untuk "Coba sendiri" atau kesalahan di bagian 4? Salin dulu *file* solusinya ke folder `uas/coba` lewat File Explorer (Windows) atau Finder (macOS), lalu ubah salinannya. *File* di folder materi tetap utuh.

### Cara Membandingkan Jawabanmu dengan Solusi

Targetnya, *output* programmu **sama persis** dengan *output* solusi. Biarkan komputer yang membandingkan karena mata mudah melewatkan satu spasi.

1. Salin *file* solusi yang ingin dibandingkan, misalnya `soal_c1_tiket_bioskop.py`, ke folder `PBO-latihan-saya/uas`.
2. Buka terminal **di folder `uas` itu**. Caranya: di VS Code, pilih **File → Open Folder**, buka folder `uas`, lalu pilih **Terminal → New Terminal**.
3. Simpan *output* kedua program ke *file* teks. Tanda `>` artinya "jangan tampilkan di layar, simpan ke *file* ini":

   ```bash
   python jawaban_c1.py > hasil_saya.txt
   python soal_c1_tiket_bioskop.py > hasil_solusi.txt
   ```

4. Bandingkan kedua *file* dengan perintah yang sesuai dengan terminalmu:

   | Terminal | Perintah | Jika kedua *file* sama |
   |---|---|---|
   | Windows: Command Prompt | `fc hasil_saya.txt hasil_solusi.txt` | muncul `FC: no differences encountered` |
   | Windows: PowerShell (terminal bawaan VS Code) | `fc.exe hasil_saya.txt hasil_solusi.txt` | sama seperti di atas |
   | macOS/Linux | `diff hasil_saya.txt hasil_solusi.txt` | tidak mencetak apa pun |

Di PowerShell, `fc` tanpa `.exe` adalah singkatan perintah lain, jadi selalu tulis `fc.exe`. VS Code juga bisa membandingkan dua *file* tanpa terminal: klik kanan *file* pertama di panel **Explorer**, pilih **Select for Compare**, lalu klik kanan *file* kedua dan pilih **Compare with Selected**. Untuk Soal C2, cara yang sama dipakai untuk membuktikan bahwa *refactor*-mu tidak mengubah perilaku (lihat [bagian 3](#3-membuktikan-output-tidak-berubah)).

### Cara Membaca Kode di Halaman Ini

- Baris ***File*:** di awal bagian 1 dan 2 menunjuk *file* solusinya. Klik untuk melihat isi lengkapnya.
- Blok kode sesudahnya adalah **potongan** penting dari *file* itu, disalin persis beserta komentarnya. Jangan menjalankan potongannya sendiri. Jalankan *file* lengkapnya dengan cara di atas.
- Tanda `# [1]`, `# [2]`, dan seterusnya di komentar kode dijelaskan di daftar **Penjelasan** di bawah blok kodenya. Nomornya dimulai lagi dari `[1]` untuk setiap *file*.
- Blok berlabel ***Output:*** adalah hasil asli saat *file* itu dijalankan.

---

## 1. Soal C1: Sistem Pemesanan Tiket Bioskop

*File*: [`solusi/soal_c1_tiket_bioskop.py`](solusi/soal_c1_tiket_bioskop.py)

Saran urutan membaca: *exception* → `Tiket` dan kelas anaknya → `Jadwal` → `Bioskop` → program utama. Urutan ini sama dengan urutan saat kamu sebaiknya **menulis** kodenya: dari bagian yang tidak bergantung pada apa pun, menuju bagian yang memakai semuanya.

### 1.1 *Exception* Buatan Sendiri

```python
class BioskopError(Exception):
    """Induk semua error BioskopKita."""


class JadwalTidakDitemukanError(BioskopError):
    """Dilempar saat kode jadwal tidak terdaftar."""

    def __init__(self, kode_jadwal: str):
        super().__init__(f"Jadwal {kode_jadwal} tidak ditemukan")
        self.kode_jadwal = kode_jadwal
```

```python
class KursiSudahTerjualError(BioskopError):
    """Dilempar saat kursi sudah dipesan orang lain."""

    def __init__(self, kode_kursi: str, judul: str, sisa_kursi: int):
        super().__init__(f"Kursi {kode_kursi} untuk {judul} sudah terjual")  # [1]
        self.kode_kursi = kode_kursi
        self.judul = judul
        self.sisa_kursi = sisa_kursi  # [2] data tambahan untuk penangkap error
```

Penjelasan:

- `BioskopError` sengaja kosong (hanya *docstring*). Gunanya sebagai **induk bersama** sehingga semua *error* bioskop bisa ditangkap sekaligus dengan `except BioskopError`.
- **[1]** Pesan yang dikirim ke `super().__init__()` adalah teks yang muncul saat *exception* dicetak (`print(e)` atau `f"{e}"`). Jika baris ini dilupakan, hasil cetaknya menjadi aneh (lihat [Kesalahan 2](#kesalahan-2-lupa-memanggil-super__init__-pada-exception-buatan-sendiri)).
- **[2]** *Exception* adalah objek biasa, jadi boleh menyimpan atribut. Penangkap *error* bisa membaca `e.sisa_kursi` untuk memberi saran kepada pemesan.

### 1.2 Kelas Abstrak Tiket dan Tiga Kelas Anaknya

```python
class Tiket(ABC):
    """Kelas abstrak: kerangka untuk semua jenis tiket."""

    def __init__(self, kode_kursi: str, pemesan: str, harga_dasar: int):
        self._kode_kursi = kode_kursi
        self._pemesan = pemesan
        self._harga_dasar = harga_dasar
```

```python
    @abstractmethod
    def jenis(self) -> str:  # [3] method abstrak: WAJIB diisi kelas anak
        """Nama jenis tiket, misalnya 'Reguler'."""

    @abstractmethod
    def hitung_harga(self) -> int:
        """Harga akhir tiket dalam rupiah (bilangan bulat)."""

    def __str__(self) -> str:  # [4] method konkret yang memanggil method abstrak
        harga = format_rupiah(self.hitung_harga())
        return f"{self._kode_kursi:<4}{self.jenis():<9}{self._pemesan:<16}{harga:>10}"
```

Salah satu kelas anaknya:

```python
class TiketVIP(Tiket):
    """Kursi sofa + popcorn: harga dasar ditambah biaya tetap."""

    TAMBAHAN = 25000

    def jenis(self) -> str:
        return "VIP"

    def hitung_harga(self) -> int:
        return self.harga_dasar + TiketVIP.TAMBAHAN
```

Penjelasan:

- `Tiket` mewarisi `ABC`, dan atributnya hanya bisa dibaca lewat *property* tanpa *setter* (`kode_kursi`, `pemesan`, `harga_dasar`). Jadi, tidak ada jalan resmi untuk mengubah tiket yang sudah terjual. (Ingat, awalan `_` di Python adalah kesepakatan antarpemrogram, bukan kunci pengaman.)
- **[3]** `@abstractmethod` menandai *method* yang **wajib** diisi kelas anak. Python menolak membuat objek dari kelas yang masih punya *method* abstrak kosong.
- **[4]** `__str__` ditulis **sekali** di kelas induk, tetapi memanggil `jenis()` dan `hitung_harga()` milik objek sebenarnya. Inilah polimorfisme dari dalam kelas induk (pola *Template Method* sederhana).
- Kelas anak tidak menulis `__init__` sama sekali karena konstruktor induk sudah cukup. Konstanta `TAMBAHAN` menggantikan angka ajaib `25000`.

Objek tiket dibuat oleh sebuah *Factory* sederhana supaya rantai `if` jenis tiket hanya ada di **satu** tempat:

```python
class TiketFactory:
    """Factory sederhana: membuat objek Tiket dari pilihan berupa teks."""

    @staticmethod
    def buat(jenis: str, kode_kursi: str, pemesan: str,
             harga_dasar: int) -> Tiket:
        pilihan = jenis.lower()  # "VIP", "vip", dan "Vip" dianggap sama
        if pilihan == "reguler":
            return TiketReguler(kode_kursi, pemesan, harga_dasar)
        if pilihan == "vip":
            return TiketVIP(kode_kursi, pemesan, harga_dasar)
        if pilihan == "pelajar":
            return TiketPelajar(kode_kursi, pemesan, harga_dasar)
        raise ValueError(f"Jenis tiket '{jenis}' tidak dikenal")
```

### 1.3 Jadwal: Dict Kursi dan Polimorfisme

Bagian akhir konstruktor `Jadwal` menyiapkan daftar kursi dan dict kursi terjual:

```python
        self._semua_kursi: list[str] = []  # A1..A5, B1..B5, C1..C5
        for baris in Jadwal.BARIS:
            for nomor in range(1, Jadwal.KURSI_PER_BARIS + 1):
                self._semua_kursi.append(f"{baris}{nomor}")
        self._terjual: dict[str, Tiket] = {}  # [5] kode kursi -> Tiket
```

```python
    def tambah_tiket(self, tiket: Tiket):
        """Menyimpan tiket. Melempar error jika kursi tidak ada/sudah terjual."""
        kursi = tiket.kode_kursi
        if kursi not in self._semua_kursi:
            raise KursiTidakAdaError(kursi, self._studio)
        if kursi in self._terjual:  # [6] cek kunci dict
            raise KursiSudahTerjualError(kursi, self._judul,
                                         len(self.kursi_kosong()))
        self._terjual[kursi] = tiket

    def kursi_kosong(self) -> list[str]:
        return [k for k in self._semua_kursi if k not in self._terjual]

    def daftar_tiket(self) -> list[Tiket]:
        """Tiket terjual, diurutkan berdasarkan kode kursi."""
        return [self._terjual[kursi] for kursi in sorted(self._terjual)]

    def jumlah_terjual(self) -> int:
        return len(self._terjual)

    def pendapatan(self) -> int:
        total = 0
        for tiket in self._terjual.values():
            total += tiket.hitung_harga()  # [7] polimorfisme
        return total
```

Penjelasan:

- `_semua_kursi` adalah ***list*** karena urutannya penting (A1, A2, ..., C5) untuk menampilkan kursi kosong.
- **[5]** `_terjual` adalah **dict** dengan kode kursi sebagai kunci. Kunci dict selalu unik, jadi satu kursi mustahil tercatat untuk dua tiket.
- **[6]** `kursi in self._terjual` memeriksa **kunci** dict dengan cepat, tanpa perulangan.
- `daftar_tiket()` memakai `sorted(self._terjual)`. Mengurutkan dict berarti mengurutkan kuncinya, lalu tiket diambil sesuai urutan kunci itu.
- **[7]** `pendapatan()` tidak peduli jenis tiket. Setiap objek menjawab `hitung_harga()` dengan caranya sendiri.

### 1.4 Bioskop: Pemesanan dan Laporan Terurut

```python
    def pesan(self, kode_jadwal: str, jenis: str, kode_kursi: str,
              pemesan: str) -> Tiket:
        """Memesan satu tiket. Urutan pemeriksaan: jadwal, jenis, kursi."""
        jadwal = self.cari_jadwal(kode_jadwal)  # bisa JadwalTidakDitemukanError
        tiket = TiketFactory.buat(jenis, kode_kursi, pemesan,
                                  jadwal.harga_dasar)  # bisa ValueError
        jadwal.tambah_tiket(tiket)  # bisa KursiTidakAdaError / KursiSudahTerjualError
        return tiket
```

```python
    def laporan_per_film(self) -> list[Jadwal]:
        """Pendapatan terbesar dulu; jika sama, judul A-Z."""
        return sorted(self._daftar_jadwal.values(),
                      key=lambda j: (-j.pendapatan(), j.judul))  # [8]

    def jumlah_per_jenis(self) -> dict[str, int]:
        """Jenis tiket -> banyak tiket terjual, urut nama jenis."""
        hasil: dict[str, int] = {}
        for tiket in self.semua_tiket():
            hasil[tiket.jenis()] = hasil.get(tiket.jenis(), 0) + 1
        return dict(sorted(hasil.items()))
```

Penjelasan:

- `pesan()` sangat pendek karena **tidak menangkap** *exception* apa pun. Tugasnya hanya mengatur urutan langkah. Jika satu langkah gagal, *exception*-nya diteruskan ke pemanggil (program utama), yang lebih tahu cara menampilkannya.
- **[8]** Kunci pengurutan berupa *tuple* `(-pendapatan, judul)`. Python membandingkan *tuple* elemen demi elemen: pendapatan dibalik dengan tanda minus agar yang terbesar di depan, dan jika sama, judul diurutkan A—Z. Tanda minus hanya bisa dipakai untuk angka (lihat [Kesalahan 3](#kesalahan-3-memakai-tanda-minus-untuk-mengurutkan-teks)).
- `hasil.get(kunci, 0) + 1` adalah pola menghitung frekuensi dengan dict. `dict(sorted(hasil.items()))` membuat dict baru yang urut berdasarkan kunci.

### 1.5 Program Utama: Menangkap *Exception* dengan Rapi

```python
    print("=== PEMESANAN TIKET ===")
    for kode_jadwal, jenis, kursi, pemesan in DAFTAR_PERMINTAAN:
        try:
            tiket = bioskop.pesan(kode_jadwal, jenis, kursi, pemesan)
        except KursiSudahTerjualError as e:  # [9] yang spesifik ditulis dulu
            print(f"[GAGAL] {e}")
            print(f"        Saran: pilih kursi lain, masih ada "
                  f"{e.sisa_kursi} kursi kosong")
        except BioskopError as e:  # [10] semua error bioskop yang lain
            print(f"[GAGAL] {e}")
        except ValueError as e:  # jenis tiket tidak dikenal
            print(f"[GAGAL] {e}")
        else:  # [11] hanya dijalankan jika TIDAK ada exception
            harga = format_rupiah(tiket.hitung_harga())
            print(f"[OK]    {kode_jadwal}/{tiket.kode_kursi} {tiket.jenis()} "
                  f"untuk {tiket.pemesan}: {harga}")
    print()
```

Penjelasan:

- **[9]** `KursiSudahTerjualError` ditangkap **lebih dulu** karena butuh penanganan khusus (saran sisa kursi). Jika `except BioskopError` ditulis di atasnya, blok ini tidak akan pernah tercapai.
- **[10]** Dua *error* bioskop lainnya cukup ditangani sama: cetak pesannya. Inilah manfaat hierarki *exception*.
- **[11]** Blok `else` hanya jalan jika `try` sukses. Memisahkan "langkah yang mungkin gagal" (di `try`) dari "langkah setelah sukses" (di `else`) mencegah kita ikut menangkap *error* dari baris yang tidak dimaksud.
- Program **tidak** menangkap `Exception` secara umum. Kesalahan pemrograman yang tidak terduga tetap terlihat jelas, tidak tertelan diam-diam.

Cara menjalankan dari folder utama materi (cara lain ada di [Persiapan](#cara-menjalankan-solusi)):

```bash
cd Pertemuan-16-UAS/python/solusi
python soal_c1_tiket_bioskop.py
```

***Output:***

```text
=== JADWAL TAYANG BioskopKita ===
J01  13:00  Studio 1  Rindu di Tepian     Rp30.000
J02  16:00  Studio 2  Mahakam Biru        Rp40.000
J03  19:00  Studio 1  Detektif Kampus     Rp50.000

=== PEMESANAN TIKET ===
[OK]    J02/A1 Reguler untuk Budi Santoso: Rp40.000
[OK]    J02/A2 VIP untuk Siti Aminah: Rp65.000
[GAGAL] Kursi A1 untuk Mahakam Biru sudah terjual
        Saran: pilih kursi lain, masih ada 13 kursi kosong
[OK]    J02/A3 Pelajar untuk Rina Marlina: Rp32.000
[GAGAL] Kursi D1 tidak ada di Studio 1
[OK]    J03/C5 VIP untuk Andi Wijaya: Rp75.000
[GAGAL] Jadwal J05 tidak ditemukan
[GAGAL] Jenis tiket 'premium' tidak dikenal
[OK]    J01/B2 VIP untuk Dimas Pratama: Rp55.000
[OK]    J01/B3 Reguler untuk Ayu Lestari: Rp30.000
[OK]    J01/B4 Reguler untuk Bima Saputra: Rp30.000
[OK]    J03/C4 Pelajar untuk Citra Dewi: Rp40.000
[OK]    J02/B1 Reguler untuk Eko Prasetyo: Rp40.000

=== TIKET TERJUAL J02: Mahakam Biru ===
A1  Reguler  Budi Santoso      Rp40.000
A2  VIP      Siti Aminah       Rp65.000
A3  Pelajar  Rina Marlina      Rp32.000
B1  Reguler  Eko Prasetyo      Rp40.000
Kursi kosong (11): A4, A5, B2, B3, B4, B5, C1, C2, C3, C4, C5

=== LAPORAN PENDAPATAN PER FILM ===
1. Mahakam Biru       4 tiket   Rp177.000
2. Detektif Kampus    2 tiket   Rp115.000
3. Rindu di Tepian    3 tiket   Rp115.000
Total pendapatan: Rp407.000

=== REKAP PER JENIS TIKET ===
Pelajar   2 tiket    Rp72.000
Reguler   4 tiket   Rp140.000
VIP       3 tiket   Rp195.000
```

> [!TIP]
> **Coba sendiri:** salin `solusi/soal_c1_tiket_bioskop.py` ke folder latihanmu (`PBO-latihan-saya/uas/coba`), lalu buka salinannya. Tambahkan kelas `TiketKeluarga` (jenis `"Keluarga"`, harga dasar dikurangi Rp5.000), satu cabang `"keluarga"` di `TiketFactory`, dan satu permintaan baru di akhir `DAFTAR_PERMINTAAN`: `("J01", "keluarga", "C1", "Fajar Nugroho")`. Simpan, lalu jalankan `python soal_c1_tiket_bioskop.py` dari folder itu. Bagian mana saja yang perlu kamu ubah? Berapa total pendapatan baru?

<details>
<summary>Lihat jawaban</summary>

Hanya dua tempat di kode: kelas baru `TiketKeluarga` dan satu cabang `if pilihan == "keluarga"` di `TiketFactory`, ditambah satu baris permintaan di data. `Jadwal`, `Bioskop`, dan laporan tidak berubah sama sekali. Tiket keluarga di `J01` berharga 30000 - 5000 = Rp25.000 sehingga total pendapatan menjadi 407000 + 25000 = **Rp432.000**.

Di *output*, kamu akan melihat baris baru `[OK]    J01/C1 Keluarga untuk Fajar Nugroho: Rp25.000`. Laporan per film juga berubah: Rindu di Tepian naik ke urutan kedua (`4 tiket   Rp140.000`), dan rekap per jenis tiket diawali baris `Keluarga  1 tiket    Rp25.000`.

</details>

---

## 2. Soal C2: *Refactor* Kasir *Laundry*

*File*: [`solusi/soal_c2_sebelum.py`](solusi/soal_c2_sebelum.py) (kode awal) dan [`solusi/soal_c2_sesudah.py`](solusi/soal_c2_sesudah.py) (hasil *refactor*)

### 2.1 Membaca Kode Sebelum *Refactor*

Potongan inti *method* `terima_cucian()` di kode awal:

```python
        # hitung promo
        potongan = 0
        nama_promo = ""
        if promo == "member":
            potongan = subtotal * 10 // 100
            nama_promo = "Member 10%"
        elif promo == "gratis1kg":
            if berat >= 5:
                potongan = tarif
                nama_promo = "Gratis 1 kg"
        total = subtotal - potongan
```

```python
        # kirim WhatsApp
        print(f"[WA ke {no_hp}] Halo {nama}, cucian {kode} sudah kami terima. "
              f"Total {teks_total}.")

        # simpan riwayat
        self.riwayat.append((kode, nama, berat, total))
```

Perhatikan komentar-komentar seperti `# hitung promo` dan `# kirim WhatsApp`. Setiap komentar yang menandai "babak" di dalam satu *method* adalah petunjuk bahwa *method* itu mengerjakan terlalu banyak hal. Daftar lengkap masalahnya ada di [pembahasan](../pembahasan.md#soal-c2-refactor-kasir-laundry-yang-berantakan).

### 2.2 Katalog Layanan dan *Exception*

```python
class KatalogLayanan:
    """Daftar layanan. Layanan baru cukup DIDAFTARKAN, tanpa mengubah kode (OCP)."""

    def __init__(self):
        # [1] nama layanan -> Layanan. Katalog hanya dipakai untuk MENCARI.
        self._daftar: dict[str, Layanan] = {}

    def tambah(self, layanan: Layanan):
        self._daftar[layanan.nama] = layanan

    def cari(self, nama: str) -> Layanan:
        if nama not in self._daftar:
            raise LayananTidakTersediaError(nama)  # [2] bukan lagi print + return
        return self._daftar[nama]
```

Penjelasan:

- **[1]** Rantai `if layanan == "cuci kering" ...` berubah menjadi **data** di dalam dict. Layanan baru cukup didaftarkan dengan `katalog.tambah(...)`.
- **[2]** Kode awal mencetak `[DITOLAK] ...` lalu `return` sehingga pemanggil tidak tahu ada kegagalan. Kini katalog melempar *exception*, dan lapisan tampilan yang memutuskan cara menampilkannya.

### 2.3 *Strategy* untuk Promo

```python
class Promo(ABC):
    """Strategi promo. Promo baru = kelas baru; kelas lain tidak diubah (OCP)."""

    @abstractmethod
    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:  # [3]
        """Besar potongan dalam rupiah. Tidak pernah negatif (LSP)."""

    @abstractmethod
    def keterangan(self) -> str:
        """Nama promo untuk dicetak di nota."""
```

```python
class PromoGratisSatuKg(Promo):
    """Cucian minimal 5 kg: gratis 1 kg (potongan = tarif 1 kg)."""

    MINIMAL_BERAT = 5

    def hitung_potongan(self, pesanan: "PesananLaundry") -> int:
        if pesanan.berat < PromoGratisSatuKg.MINIMAL_BERAT:
            return 0
        return pesanan.layanan.tarif_per_kg

    def keterangan(self) -> str:
        return "Gratis 1 kg"
```

Di kelas `PesananLaundry`:

```python
    def subtotal(self) -> int:
        return self._layanan.tarif_per_kg * self._berat

    def potongan(self) -> int:
        return self._promo.hitung_potongan(self)  # [4] diserahkan ke strategi

    def total(self) -> int:
        return self.subtotal() - self.potongan()
```

Penjelasan:

- **[3]** Tipe parameter ditulis sebagai teks `"PesananLaundry"` karena kelas `PesananLaundry` baru didefinisikan **di bawah** `Promo`. Python mengizinkan *type hint* berupa teks untuk kasus seperti ini (*forward reference*).
- Setiap promo menjadi satu kelas kecil. Rantai `if promo == ...` hilang, dan salah ketik nama promo kini langsung ketahuan sebagai `NameError`, bukan promo yang diam-diam tidak berlaku.
- **[4]** `PesananLaundry` tidak tahu promo apa yang dipakainya. Ia cukup **meminta** strategi menghitung potongan, sambil memberikan dirinya sendiri (`self`) sebagai data.

### 2.4 Kasir yang Bergantung pada Abstraksi

```python
class Pengirim(ABC):
    """Kontrak kecil: cukup satu method untuk mengirim pesan (ISP)."""

    @abstractmethod
    def kirim(self, no_hp: str, pesan: str):
        """Mengirim pesan teks ke nomor HP."""


class PengirimWhatsApp(Pengirim):
    """Simulasi WhatsApp: pesan dicetak ke layar."""

    def kirim(self, no_hp: str, pesan: str):
        print(f"[WA ke {no_hp}] {pesan}")
```

```python
class KasirLaundry:
    """Mengatur alur kerja kasir dengan memakai kelas-kelas di atas."""

    def __init__(self, katalog: KatalogLayanan, pengirim: Pengirim):  # [5]
        self._katalog = katalog
        self._pengirim = pengirim  # bergantung pada ABSTRAKSI (DIP)
        self._riwayat: list[PesananLaundry] = []
        self._nomor_terakhir = 0

    def terima_cucian(self, pelanggan: Pelanggan, nama_layanan: str,
                      berat: int, promo: Promo) -> PesananLaundry:
        """Melempar LayananTidakTersediaError jika layanan tidak dikenal."""
        layanan = self._katalog.cari(nama_layanan)  # dicek SEBELUM nomor dibuat
        self._nomor_terakhir += 1
        kode = f"L{self._nomor_terakhir:03d}"
        pesanan = PesananLaundry(kode, pelanggan, layanan, berat, promo)
        print(NotaLaundry(pesanan).buat_teks())
        self._pengirim.kirim(pelanggan.no_hp,
                             f"Halo {pelanggan.nama}, cucian {kode} sudah kami "
                             f"terima. Total {format_rupiah(pesanan.total())}.")
        self._riwayat.append(pesanan)
        return pesanan
```

Program utamanya:

```python
def main():
    kasir = KasirLaundry(siapkan_katalog(), PengirimWhatsApp())  # [6] injeksi
    terima(kasir, Pelanggan("Budi Santoso", "081234567890"), "cuci setrika", 4,
           PromoMember())
```

Penjelasan:

- **[5]** `KasirLaundry` menerima katalog dan pengirim **dari luar** lewat konstruktor (*dependency injection*). Tipe parameternya abstrak (`Pengirim`), bukan `PengirimWhatsApp`.
- **[6]** Keputusan "pesan dikirim lewat WhatsApp" hanya ada di satu baris ini. Mengganti ke SMS cukup membuat `PengirimSMS(Pengirim)` dan mengubah baris ini; `KasirLaundry` tidak disentuh. Untuk pengujian, kita bahkan bisa menyuntikkan pengirim palsu yang hanya mencatat pesan.
- Perhatikan komentar `dicek SEBELUM nomor dibuat`. Di kode awal, nomor order baru bertambah **setelah** layanan dinyatakan valid. Detail kecil seperti ini wajib dipertahankan karena *refactor* tidak boleh mengubah perilaku.
- Fungsi `terima()` di program utama adalah lapisan tampilan kecil: ia memanggil kasir, menangkap `LayananTidakTersediaError`, mencetak `[DITOLAK] ...`, lalu mencetak baris kosong.

Cara menjalankan dari folder utama materi (baris ketiga dan keempat dijalankan satu per satu):

```bash
cd Pertemuan-16-UAS/python/solusi
python soal_c2_sebelum.py
python soal_c2_sesudah.py
```

Kedua program menghasilkan *output* yang sama persis.

***Output:***

```text
====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L001
Pelanggan : Budi Santoso
Layanan   : cuci setrika
Berat     : 4 kg x Rp8.000
------------------------------------
Subtotal                    Rp32.000
Promo Member 10%            -Rp3.200
TOTAL                       Rp28.800
====================================
[WA ke 081234567890] Halo Budi Santoso, cucian L001 sudah kami terima. Total Rp28.800.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L002
Pelanggan : Siti Aminah
Layanan   : cuci kering
Berat     : 6 kg x Rp6.000
------------------------------------
Subtotal                    Rp36.000
Promo Gratis 1 kg           -Rp6.000
TOTAL                       Rp30.000
====================================
[WA ke 082198765432] Halo Siti Aminah, cucian L002 sudah kami terima. Total Rp30.000.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L003
Pelanggan : Rina Marlina
Layanan   : setrika saja
Berat     : 3 kg x Rp5.000
------------------------------------
Subtotal                    Rp15.000
TOTAL                       Rp15.000
====================================
[WA ke 085312345678] Halo Rina Marlina, cucian L003 sudah kami terima. Total Rp15.000.

[DITOLAK] Layanan 'dry clean' tidak tersedia

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L004
Pelanggan : Dimas Pratama
Layanan   : cuci setrika
Berat     : 5 kg x Rp8.000
------------------------------------
Subtotal                    Rp40.000
TOTAL                       Rp40.000
====================================
[WA ke 081355577799] Halo Dimas Pratama, cucian L004 sudah kami terima. Total Rp40.000.

=== LAPORAN HARIAN ===
L001  Budi Santoso      4 kg    Rp28.800
L002  Siti Aminah       6 kg    Rp30.000
L003  Rina Marlina      3 kg    Rp15.000
L004  Dimas Pratama     5 kg    Rp40.000
Jumlah order : 4
Total berat  : 18 kg
Pendapatan   : Rp113.800
```

---

## 3. Membuktikan *Output* Tidak Berubah

Mata manusia mudah melewatkan satu spasi. Komputer tidak. Untuk Soal C2, bandingkan *output* kode awal dengan *output* hasil *refactor*-mu memakai langkah di [Persiapan](#cara-membandingkan-jawabanmu-dengan-solusi). Ketik perintah berikut di terminal yang berada di folder `PBO-latihan-saya/uas` (berisi salinan `soal_c2_sebelum.py` dan jawabanmu `jawaban_c2.py`):

```bash
python soal_c2_sebelum.py > sebelum.txt
python jawaban_c2.py > sesudah.txt
diff sebelum.txt sesudah.txt
```

Baris ketiga untuk macOS/Linux. Di Windows, ganti dengan `fc sebelum.txt sesudah.txt` (Command Prompt) atau `fc.exe sebelum.txt sesudah.txt` (PowerShell). Jika kedua *file* identik, `diff` **tidak mencetak apa pun**, sedangkan `fc` menulis `FC: no differences encountered`. Ingin melihat solusi lulus pemeriksaan yang sama? Salin juga `soal_c2_sesudah.py` ke folder itu, lalu ganti `jawaban_c2.py` di baris kedua dengan `soal_c2_sesudah.py`.

Bagaimana jika ada perbedaan? Misalnya, saat *refactor* kamu tidak sengaja menulis `"Jumlah order: "` (spasi sebelum titik dua hilang) di `LaporanHarian`. Hasil `diff`-nya:

```text
62c62
< Jumlah order : 4
---
> Jumlah order: 4
```

Artinya: baris ke-62 berubah (`c` = *change*). Baris berawalan `<` berasal dari *file* pertama (sebelum), baris berawalan `>` dari *file* kedua (sesudah). Perbaiki sampai `diff` diam. Di Windows, `fc` juga menampilkan baris yang berbeda dari kedua *file*, hanya saja dengan tampilan yang sedikit lain.

> [!TIP]
> Biasakan menjalankan `diff` **setiap kali** selesai memindahkan satu tanggung jawab ke kelas baru, bukan hanya di akhir. Jika muncul perbedaan, kamu langsung tahu langkah mana penyebabnya.

---

## 4. Kesalahan Umum dan Cara Membaca Pesan *Error*

Pesan *error* Python dibaca **dari bawah ke atas**: baris terakhir menyebut jenis *error* dan penyebabnya, baris-baris di atasnya menunjukkan jalur pemanggilan.

Ingin mencoba sendiri kesalahan-kesalahan di bawah? Jangan mengubah *file* di folder materi. Salin dulu `solusi/soal_c1_tiket_bioskop.py` ke folder `PBO-latihan-saya/uas/coba`, buat kesalahannya di salinan itu, lalu jalankan dari folder tersebut. Di layarmu, nama *file* di pesan *error* tampil lengkap dengan alamat foldernya. Di sini alamatnya dipendekkan menjadi nama *file* saja.

### Kesalahan 1: Lupa mengisi *method* abstrak di kelas anak

Misalkan dua baris *method* `hitung_harga()` di kelas `TiketVIP` (baris `def` dan `return`-nya) dihapus. Program berjalan sampai ada yang mencoba membuat objek `TiketVIP`, lalu berhenti dengan pesan berikut:

```text
Traceback (most recent call last):
  File "soal_c1_tiket_bioskop.py", line 352, in <module>
    main()
    ~~~~^^
  File "soal_c1_tiket_bioskop.py", line 313, in main
    tiket = bioskop.pesan(kode_jadwal, jenis, kursi, pemesan)
  File "soal_c1_tiket_bioskop.py", line 234, in pesan
    tiket = TiketFactory.buat(jenis, kode_kursi, pemesan,
                              jadwal.harga_dasar)  # bisa ValueError
  File "soal_c1_tiket_bioskop.py", line 136, in buat
    return TiketVIP(kode_kursi, pemesan, harga_dasar)
TypeError: Can't instantiate abstract class TiketVIP without an implementation for abstract method 'hitung_harga'
```

**Artinya:** `TiketVIP` masih punya *method* abstrak yang belum diisi sehingga objeknya tidak boleh dibuat. *Error* muncul saat **membuat objek**, bukan saat kelas ditulis, sehingga tiket reguler sebelumnya sempat berhasil dipesan. Perhatikan juga: `TypeError` tidak tertangkap oleh `except BioskopError` maupun `except ValueError`, jadi program berhenti. Ini bagus karena *bug* tidak tersembunyi. **Perbaikan:** tulis kembali `hitung_harga()` di `TiketVIP`.

### Kesalahan 2: Lupa memanggil `super().__init__` pada *exception* buatan sendiri

Jika baris `super().__init__(f"Kursi ... sudah terjual")` di `KursiSudahTerjualError` dihapus, program tetap berjalan, tetapi baris pesan gagalnya menjadi:

```text
[GAGAL] ('A1', 'Mahakam Biru', 13)
```

**Artinya:** tanpa pesan untuk induknya, *exception* menyimpan semua argumen konstruktornya sebagai *tuple*, lalu *tuple* itulah yang tercetak. **Perbaikan:** selalu kirim pesan yang ramah ke `super().__init__(...)` di konstruktor *exception* buatanmu.

### Kesalahan 3: Memakai tanda minus untuk mengurutkan teks

Tanda minus hanya bekerja pada angka. Jika kamu menulis `key=lambda j: (-j.pendapatan(), -j.judul)` dengan maksud membalik urutan judul juga, bagian akhir pesan *error*-nya:

```text
  File "soal_c1_tiket_bioskop.py", line 259, in <lambda>
    key=lambda j: (-j.pendapatan(), -j.judul))  # [8]
                                    ^^^^^^^^
TypeError: bad operand type for unary -: 'str'
```

**Artinya:** operator minus satu operan (*unary*) tidak bisa diterapkan pada `str`. **Perbaikan:** untuk soal ini, judul memang harus A—Z, jadi cukup `j.judul`. Jika kamu benar-benar butuh dua kriteria yang **sama-sama** menurun, pakai `sorted(..., reverse=True)`. Jika arahnya berbeda dan salah satunya teks, urutkan dua kali: kriteria kedua dulu, lalu kriteria pertama (pengurutan Python stabil).

### Kesalahan 4: Urutan `except` terbalik

Jika `except BioskopError` ditulis **di atas** `except KursiSudahTerjualError`, Python tidak memberi pesan *error* apa pun. Hasilnya hanya berbeda sedikit:

```text
[GAGAL] Kursi A1 untuk Mahakam Biru sudah terjual
[OK]    J02/A3 Pelajar untuk Rina Marlina: Rp32.000
```

**Artinya:** baris "Saran: pilih kursi lain ..." hilang. Blok `BioskopError` sudah menangkap *error* itu lebih dulu sehingga blok khusus di bawahnya tidak pernah tercapai. *Bug* seperti ini licin karena Python diam saja (berbeda dengan Java yang menolaknya saat kompilasi). **Perbaikan:** tulis `except` yang spesifik lebih dulu.

### Kesalahan 5: Mengakses dict dengan kunci yang tidak ada

Kesalahan ini tidak memakai *file* solusi. Buat *file* baru bernama `coba.py` di folder `PBO-latihan-saya/uas/coba`, isi dengan dua baris berikut, simpan, lalu jalankan dengan `python coba.py` dari folder itu:

```python
jadwal = {"J01": "Rindu di Tepian", "J02": "Mahakam Biru"}
print(jadwal["J05"])
```

Pesan *error*-nya:

```text
Traceback (most recent call last):
  File "coba.py", line 2, in <module>
    print(jadwal["J05"])
          ~~~~~~^^^^^^^
KeyError: 'J05'
```

**Artinya:** kunci `'J05'` tidak ada di dict. `KeyError` bawaan Python ini kurang ramah bagi pengguna. **Perbaikan:** periksa dulu dengan `if kode not in ...`, lalu lempar *exception* yang lebih bermakna, seperti yang dilakukan `cari_jadwal()` dengan `JadwalTidakDitemukanError`. Untuk nilai bawaan, pakai `dict.get(kunci, nilai_bawaan)`.

> [!NOTE]
> Pesan di halaman ini berasal dari Python 3.13. Bunyinya bisa sedikit berbeda antarversi. Contohnya, Python 3.10 dan 3.11 menulis `Can't instantiate abstract class TiketVIP with abstract method hitung_harga`. Penanda `~` dan `^` di bawah baris kode juga berbeda-beda, dan Python 3.10 sama sekali tidak menampilkannya. Fokuslah pada **jenis *error*** dan kata-kata kuncinya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh dari solusi |
|---|---|---|
| Kelas abstrak | `class Nama(ABC):` + `@abstractmethod` | `class Tiket(ABC):` |
| *Exception* buatan sendiri | `class X(Induk):` + `super().__init__(pesan)` | `class KursiSudahTerjualError(BioskopError):` |
| Melempar | `raise X(...)` | `raise JadwalTidakDitemukanError(kode)` |
| Menangkap berurutan | `except Anak as e:` lalu `except Induk as e:` | `except KursiSudahTerjualError as e:` |
| Blok sukses | `try: ... except ...: ... else: ...` | `else:` mencetak `[OK]` |
| Cek kunci dict | `kunci in d` | `kursi in self._terjual` |
| Hitung frekuensi | `d[k] = d.get(k, 0) + 1` | `jumlah_per_jenis()` |
| Urut dua kriteria | `sorted(xs, key=lambda x: (-angka, teks))` | `laporan_per_film()` |
| *Forward reference* | *type hint* sebagai teks | `pesanan: "PesananLaundry"` |
| *Dependency injection* | objek pendukung lewat konstruktor | `KasirLaundry(katalog, PengirimWhatsApp())` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Java: [☕ Solusi Java](../java/README.md). *Output*-nya identik.
- Siapkan presentasi proyek akhir: [Presentasi Proyek Akhir](../README.md#8-presentasi-proyek-akhir).

---

[⬅️ Pembahasan](../pembahasan.md) · [☕ Solusi Java](../java/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)
