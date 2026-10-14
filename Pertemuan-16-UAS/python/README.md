# 🐍 Solusi Praktik Python — Pertemuan 16: UAS

[⬅️ Pembahasan](../pembahasan.md) · [☕ Solusi Java](../java/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)

> **Prasyarat:** sudah mencoba sendiri [soal praktik](../latihan-soal.md#bagian-c-soal-praktik) dan membaca [pembahasan desainnya](../pembahasan.md#bagian-c-soal-praktik). Halaman ini membedah kode solusinya bagian demi bagian. Semua kode ada di folder `solusi/` dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Soal C1: Sistem Pemesanan Tiket Bioskop](#1-soal-c1-sistem-pemesanan-tiket-bioskop)
2. [Soal C2: Refactor Kasir Laundry](#2-soal-c2-refactor-kasir-laundry)
3. [Membuktikan Output Tidak Berubah](#3-membuktikan-output-tidak-berubah)
4. [Kesalahan Umum dan Cara Membaca Pesan Error](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
└── solusi/
    ├── soal_c1_tiket_bioskop.py   <- Soal C1
    ├── soal_c2_sebelum.py         <- Soal C2: kode awal yang berantakan
    └── soal_c2_sesudah.py         <- Soal C2: hasil refactor
```

Cara menjalankan dari terminal:

```bash
cd Pertemuan-16-UAS/python/solusi
python soal_c1_tiket_bioskop.py
python soal_c2_sebelum.py
python soal_c2_sesudah.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Semua solusi ditulis untuk Python 3.10 ke atas dan hanya memakai pustaka standar. Setiap solusi sengaja dibuat **satu file** agar mudah dijalankan saat ujian. Di proyek sungguhan, kelas-kelasnya sebaiknya dipisah ke beberapa modul, seperti KedaiKita sejak Pertemuan 05.

---

## 1. Soal C1: Sistem Pemesanan Tiket Bioskop

File: [`solusi/soal_c1_tiket_bioskop.py`](solusi/soal_c1_tiket_bioskop.py)

Saran urutan membaca: *exception* → `Tiket` dan kelas anaknya → `Jadwal` → `Bioskop` → program utama. Urutan ini sama dengan urutan saat kamu sebaiknya **menulis** kodenya: dari bagian yang tidak bergantung pada apa pun, menuju bagian yang memakai semuanya.

### 1.1 Exception Buatan Sendiri

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

- `BioskopError` sengaja kosong (hanya *docstring*). Gunanya sebagai **induk bersama**, sehingga semua error bioskop bisa ditangkap sekaligus dengan `except BioskopError`.
- **[1]** Pesan yang dikirim ke `super().__init__()` adalah teks yang muncul saat *exception* dicetak (`print(e)` atau `f"{e}"`). Jika baris ini dilupakan, hasil cetaknya menjadi aneh (lihat [Kesalahan 2](#kesalahan-2-lupa-memanggil-super__init__-pada-exception-buatan-sendiri)).
- **[2]** *Exception* adalah objek biasa, jadi boleh menyimpan atribut. Penangkap error bisa membaca `e.sisa_kursi` untuk memberi saran kepada pemesan.

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

- `Tiket` mewarisi `ABC`, dan atributnya hanya bisa dibaca lewat *property* tanpa *setter* (`kode_kursi`, `pemesan`, `harga_dasar`). Jadi tidak ada jalan resmi untuk mengubah tiket yang sudah terjual. (Ingat, awalan `_` di Python adalah kesepakatan antarprogrammer, bukan kunci pengaman.)
- **[3]** `@abstractmethod` menandai method yang **wajib** diisi kelas anak. Python menolak membuat objek dari kelas yang masih punya method abstrak kosong.
- **[4]** `__str__` ditulis **sekali** di kelas induk, tetapi memanggil `jenis()` dan `hitung_harga()` milik objek sebenarnya. Inilah polimorfisme dari dalam kelas induk (pola *Template Method* sederhana).
- Kelas anak tidak menulis `__init__` sama sekali, karena konstruktor induk sudah cukup. Konstanta `TAMBAHAN` menggantikan angka ajaib `25000`.

Objek tiket dibuat oleh sebuah Factory sederhana, supaya rantai `if` jenis tiket hanya ada di **satu** tempat:

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

- `_semua_kursi` adalah **list** karena urutannya penting (A1, A2, ..., C5) untuk menampilkan kursi kosong.
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
- **[8]** Kunci pengurutan berupa *tuple* `(-pendapatan, judul)`. Python membandingkan *tuple* elemen demi elemen: pendapatan dibalik dengan tanda minus agar yang terbesar di depan, dan jika sama, judul diurutkan A–Z. Tanda minus hanya bisa dipakai untuk angka (lihat [Kesalahan 3](#kesalahan-3-memakai-tanda-minus-untuk-mengurutkan-teks)).
- `hasil.get(kunci, 0) + 1` adalah pola menghitung frekuensi dengan dict. `dict(sorted(hasil.items()))` membuat dict baru yang urut berdasarkan kunci.

### 1.5 Program Utama: Menangkap Exception dengan Rapi

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
- **[10]** Dua error bioskop lainnya cukup ditangani sama: cetak pesannya. Inilah manfaat hierarki *exception*.
- **[11]** Blok `else` hanya jalan jika `try` sukses. Memisahkan "langkah yang mungkin gagal" (di `try`) dari "langkah setelah sukses" (di `else`) mencegah kita ikut menangkap error dari baris yang tidak dimaksud.
- Program **tidak** menangkap `Exception` secara umum. Kesalahan pemrograman yang tidak terduga tetap terlihat jelas, tidak tertelan diam-diam.

Cara menjalankan:

```bash
cd Pertemuan-16-UAS/python/solusi
python soal_c1_tiket_bioskop.py
```

**Output:**

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
> **Coba sendiri:** tambahkan kelas `TiketKeluarga` (harga dasar dikurangi Rp5.000) lalu tambahkan satu cabang di `TiketFactory`. Pesan satu tiket keluarga untuk `J01` kursi `C1`. Bagian mana saja yang perlu kamu ubah? Berapa total pendapatan baru?

<details>
<summary>Lihat jawaban</summary>

Hanya dua tempat: kelas baru `TiketKeluarga` dan satu cabang `if pilihan == "keluarga"` di `TiketFactory` (ditambah satu baris permintaan di data). `Jadwal`, `Bioskop`, dan laporan tidak berubah sama sekali. Tiket keluarga di `J01` berharga 30000 - 5000 = Rp25.000, sehingga total pendapatan menjadi 407000 + 25000 = **Rp432.000**.

</details>

---

## 2. Soal C2: Refactor Kasir Laundry

File: [`solusi/soal_c2_sebelum.py`](solusi/soal_c2_sebelum.py) (kode awal) dan [`solusi/soal_c2_sesudah.py`](solusi/soal_c2_sesudah.py) (hasil refactor)

### 2.1 Membaca Kode Sebelum Refactor

Potongan inti method `terima_cucian()` di kode awal:

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

Perhatikan komentar-komentar seperti `# hitung promo` dan `# kirim WhatsApp`. Setiap komentar yang menandai "babak" di dalam satu method adalah petunjuk bahwa method itu mengerjakan terlalu banyak hal. Daftar lengkap masalahnya ada di [pembahasan](../pembahasan.md#soal-c2-refactor-kasir-laundry-yang-berantakan).

### 2.2 Strategy untuk Promo

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

### 2.3 Katalog Layanan dan Exception

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
- **[2]** Kode awal mencetak `[DITOLAK] ...` lalu `return`, sehingga pemanggil tidak tahu ada kegagalan. Kini katalog melempar *exception*, dan lapisan tampilan yang memutuskan cara menampilkannya.

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
- Perhatikan komentar `dicek SEBELUM nomor dibuat`. Di kode awal, nomor order baru bertambah **setelah** layanan dinyatakan valid. Detail kecil seperti ini wajib dipertahankan, karena refactor tidak boleh mengubah perilaku.
- Fungsi `terima()` di program utama adalah lapisan tampilan kecil: ia memanggil kasir, menangkap `LayananTidakTersediaError`, mencetak `[DITOLAK] ...`, lalu mencetak baris kosong.

Cara menjalankan:

```bash
cd Pertemuan-16-UAS/python/solusi
python soal_c2_sebelum.py
python soal_c2_sesudah.py
```

Kedua program menghasilkan output yang sama persis.

**Output:**

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

## 3. Membuktikan Output Tidak Berubah

Mata manusia mudah melewatkan satu spasi. Komputer tidak. Simpan output kedua versi ke file, lalu bandingkan:

```bash
python soal_c2_sebelum.py > sebelum.txt
python soal_c2_sesudah.py > sesudah.txt
diff sebelum.txt sesudah.txt
```

Di macOS/Linux, `diff` **tidak mencetak apa pun** jika kedua file identik. Di Windows (Command Prompt), gunakan `fc sebelum.txt sesudah.txt`; jika identik, ia menulis `FC: no differences encountered`. Di PowerShell, tulis `fc.exe`.

Bagaimana jika ada perbedaan? Misalnya, saat refactor kamu tidak sengaja menulis `"Jumlah order: "` (spasi sebelum titik dua hilang) di `LaporanHarian`. Hasil `diff`-nya:

```text
62c62
< Jumlah order : 4
---
> Jumlah order: 4
```

Artinya: baris ke-62 berubah (`c` = *change*). Baris berawalan `<` berasal dari file pertama (sebelum), baris berawalan `>` dari file kedua (sesudah). Perbaiki sampai `diff` diam.

> [!TIP]
> Biasakan menjalankan `diff` **setiap kali** selesai memindahkan satu tanggung jawab ke kelas baru, bukan hanya di akhir. Jika muncul perbedaan, kamu langsung tahu langkah mana penyebabnya.

---

## 4. Kesalahan Umum dan Cara Membaca Pesan Error

Pesan error Python dibaca **dari bawah ke atas**: baris terakhir menyebut jenis error dan penyebabnya, baris-baris di atasnya menunjukkan jalur pemanggilan.

### Kesalahan 1: Lupa mengisi method abstrak di kelas anak

Misalkan method `hitung_harga()` di kelas `TiketVIP` terhapus. Program berjalan sampai ada yang mencoba membuat objek `TiketVIP`:

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

**Artinya:** `TiketVIP` masih punya method abstrak yang belum diisi, sehingga objeknya tidak boleh dibuat. Error muncul saat **membuat objek**, bukan saat kelas ditulis, sehingga tiket reguler sebelumnya sempat berhasil dipesan. Perhatikan juga: `TypeError` tidak tertangkap oleh `except BioskopError` maupun `except ValueError`, jadi program berhenti. Ini bagus, karena *bug* tidak tersembunyi. **Perbaikan:** tulis kembali `hitung_harga()` di `TiketVIP`.

### Kesalahan 2: Lupa memanggil `super().__init__` pada exception buatan sendiri

Jika baris `super().__init__(f"Kursi ... sudah terjual")` di `KursiSudahTerjualError` dihapus, program tetap berjalan, tetapi hasilnya:

```text
[GAGAL] ('A1', 'Mahakam Biru', 13)
```

**Artinya:** tanpa pesan untuk induknya, *exception* menyimpan semua argumen konstruktornya sebagai *tuple*, lalu *tuple* itulah yang tercetak. **Perbaikan:** selalu kirim pesan yang ramah ke `super().__init__(...)` di konstruktor *exception* buatanmu.

### Kesalahan 3: Memakai tanda minus untuk mengurutkan teks

Tanda minus hanya bekerja pada angka. Jika kamu menulis `key=lambda j: (-j.pendapatan(), -j.judul)` dengan maksud membalik urutan judul juga, bagian akhir pesan error-nya:

```text
  File "soal_c1_tiket_bioskop.py", line 259, in <lambda>
    key=lambda j: (-j.pendapatan(), -j.judul))  # [8]
                                    ^^^^^^^^
TypeError: bad operand type for unary -: 'str'
```

**Artinya:** operator minus satu operan (*unary*) tidak bisa diterapkan pada `str`. **Perbaikan:** untuk soal ini, judul memang harus A–Z, jadi cukup `j.judul`. Jika kamu benar-benar butuh dua kriteria yang **sama-sama** menurun, pakai `sorted(..., reverse=True)`. Jika arahnya berbeda dan salah satunya teks, urutkan dua kali: kriteria kedua dulu, lalu kriteria pertama (pengurutan Python stabil).

### Kesalahan 4: Urutan `except` terbalik

Jika `except BioskopError` ditulis **di atas** `except KursiSudahTerjualError`, Python tidak memberi pesan error apa pun. Hasilnya hanya berbeda sedikit:

```text
[GAGAL] Kursi A1 untuk Mahakam Biru sudah terjual
[OK]    J02/A3 Pelajar untuk Rina Marlina: Rp32.000
```

**Artinya:** baris "Saran: pilih kursi lain ..." hilang. Blok `BioskopError` sudah menangkap error itu lebih dulu, sehingga blok khusus di bawahnya tidak pernah tercapai. *Bug* seperti ini licin karena Python diam saja (berbeda dengan Java yang menolaknya saat kompilasi). **Perbaikan:** tulis `except` yang spesifik lebih dulu.

### Kesalahan 5: Mengakses dict dengan kunci yang tidak ada

```python
jadwal = {"J01": "Rindu di Tepian", "J02": "Mahakam Biru"}
print(jadwal["J05"])
```

```text
Traceback (most recent call last):
  File "contoh.py", line 2, in <module>
    print(jadwal["J05"])
          ~~~~~~^^^^^^^
KeyError: 'J05'
```

**Artinya:** kunci `'J05'` tidak ada di dict. `KeyError` bawaan Python ini kurang ramah bagi pengguna. **Perbaikan:** periksa dulu dengan `if kode not in ...`, lalu lempar *exception* yang lebih bermakna, seperti yang dilakukan `cari_jadwal()` dengan `JadwalTidakDitemukanError`. Untuk nilai bawaan, pakai `dict.get(kunci, nilai_bawaan)`.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi Python. Contohnya, Python 3.10 dan 3.11 menulis `Can't instantiate abstract class TiketVIP with abstract method hitung_harga`, dan versi lama tidak menampilkan penanda `~~~^^^`. Fokuslah pada **jenis error** dan kata-kata kuncinya.

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

- Bandingkan dengan solusi Java: [☕ Solusi Java](../java/README.md). Output-nya identik.
- Siapkan presentasi proyek akhir: [Presentasi Proyek Akhir](../README.md#8-presentasi-proyek-akhir).

---

[⬅️ Pembahasan](../pembahasan.md) · [☕ Solusi Java](../java/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)
