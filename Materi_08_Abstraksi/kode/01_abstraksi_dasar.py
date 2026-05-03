"""
Kode Praktik - Materi 08: Abstraksi (Abstraction)
File: 01_abstraksi_dasar.py
Topik: Kelas abstrak, @abstractmethod, dan abstract property

Jalankan: python 01_abstraksi_dasar.py
"""

from abc import ABC, abstractmethod
import math

# ======================================================================
# BAGIAN 1: Motivasi — Masalah Tanpa Abstraksi
#           Tanpa abstraksi, kelas anak bisa "lupa" mengimplementasikan
#           method penting dan error baru muncul saat runtime.
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Motivasi — Masalah Tanpa Abstraksi")
print("=" * 60)

class HewanTanpaABC:
    """Kelas biasa — tidak ada enforcement."""

    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan suara()")


class KucingBiasa(HewanTanpaABC):
    def suara(self):
        return "Meow~"


class AnjingLupa(HewanTanpaABC):
    pass  # LUPA mengimplementasikan suara()!
    # Tidak ada error saat membuat objek...


kucing = KucingBiasa("Kitty")
anjing = AnjingLupa("Rex")

print(f"\n  {kucing.nama} bersuara: {kucing.suara()}")

# Error baru muncul saat kita MEMANGGIL method — ini terlambat!
try:
    print(f"  {anjing.nama} bersuara: {anjing.suara()}")
except NotImplementedError as e:
    print(f"  Error pada {anjing.nama}: {e}")
    print("  [!] Error muncul saat runtime -- bisa terlambat diketahui!")

print()


# ======================================================================
# BAGIAN 2: Solusi — Kelas Abstrak dengan ABC
#           Error terjadi saat objek DIBUAT — jauh lebih awal dan aman.
# ======================================================================
print("=" * 60)
print("BAGIAN 2: Solusi — Kelas Abstrak dengan ABC")
print("=" * 60)

class HewanABC(ABC):
    """
    Kelas abstrak — mendefinisikan KONTRAK yang wajib dipenuhi
    oleh semua kelas hewan.
    """

    def __init__(self, nama, umur):
        self.nama = nama
        self.umur = umur

    @abstractmethod
    def suara(self):
        """Wajib diimplementasikan: suara khas hewan ini."""
        pass

    @abstractmethod
    def bergerak(self):
        """Wajib diimplementasikan: cara bergerak hewan ini."""
        pass

    # Method KONKRET — sudah ada implementasinya, langsung diwarisi
    def perkenalan(self):
        """Method ini tidak perlu di-override — memanfaatkan method abstrak."""
        print(f"  Nama  : {self.nama}")
        print(f"  Umur  : {self.umur} tahun")
        print(f"  Suara : {self.suara()}")
        print(f"  Gerak : {self.bergerak()}")

    def __str__(self):
        return f"{self.__class__.__name__}({self.nama})"


# Mencoba membuat objek dari kelas abstrak — langsung error!
print("\n  Mencoba membuat HewanABC() langsung:")
try:
    h = HewanABC("Hewan", 1)
except TypeError as e:
    print(f"  TypeError: {e}")

print()

# Kelas anak yang LENGKAP — mengimplementasikan semua abstract method
class Kucing(HewanABC):
    """Kelas konkret — mengimplementasikan semua kontrak dari HewanABC."""

    def suara(self):
        return "Meow~ Meow~"

    def bergerak(self):
        return "berjalan anggun, kadang melompat"


class Elang(HewanABC):
    def __init__(self, nama, umur, rentang_sayap_cm):
        super().__init__(nama, umur)
        self.rentang_sayap_cm = rentang_sayap_cm

    def suara(self):
        return "Kreeee! Kreeee!"

    def bergerak(self):
        return f"terbang dengan rentang sayap {self.rentang_sayap_cm} cm"


class Buaya(HewanABC):
    def suara(self):
        return "Grrrrr..."

    def bergerak(self):
        return "merangkak di darat, berenang di air"


# Kelas anak yang TIDAK LENGKAP — akan error saat instansiasi
class HewanTidakLengkap(HewanABC):
    def suara(self):
        return "???"
    # Lupa bergerak()!


print("  Mencoba membuat HewanTidakLengkap() — lupa bergerak():")
try:
    x = HewanTidakLengkap("X", 1)
except TypeError as e:
    print(f"  TypeError: {e}")
    print("  [OK] Error muncul saat INSTANSIASI -- lebih awal dan aman!\n")

# Kelas konkret yang lengkap bisa dibuat objek
kebun_binatang = [
    Kucing("Kitty", 3),
    Elang("Garuda", 5, 220),
    Buaya("Kroko", 12),
]

print("  Perkenalan semua hewan di kebun binatang:")
print("  " + "-" * 56)
for hewan in kebun_binatang:
    hewan.perkenalan()
    print()


# ======================================================================
# BAGIAN 3: Abstract Property
#           Properti (getter) juga bisa dijadikan abstrak — memaksa
#           setiap kelas anak mendefinisikan "atribut" tertentu.
# ======================================================================
print("=" * 60)
print("BAGIAN 3: Abstract Property")
print("=" * 60)

class ProdukABC(ABC):
    """
    Kelas abstrak produk kampus.
    'harga' dan 'kategori' adalah abstract property —
    setiap subkelas wajib mendefinisikannya.
    """

    def __init__(self, nama, stok):
        self._nama  = nama
        self._stok  = stok

    @property
    def nama(self):
        return self._nama          # property konkret — langsung diwarisi

    @property
    def stok(self):
        return self._stok

    @property
    @abstractmethod
    def harga(self):
        """Harga wajib didefinisikan oleh setiap subkelas."""
        pass

    @property
    @abstractmethod
    def kategori(self):
        """Kategori produk wajib didefinisikan."""
        pass

    def info(self):
        status = f"Stok: {self.stok}" if self.stok > 0 else "HABIS"
        print(f"  [{self.kategori:>12}] {self.nama:<28} "
              f"Rp {self.harga:>10,.0f}  {status}")

    def __str__(self):
        return f"{self.nama} (Rp {self.harga:,.0f})"


class BukuKuliah(ProdukABC):
    """Buku kuliah — harga tetap, kategori 'Buku'."""

    def __init__(self, nama, stok, harga_jual):
        super().__init__(nama, stok)
        self._harga = harga_jual

    @property
    def harga(self):
        return self._harga

    @property
    def kategori(self):
        return "Buku Kuliah"


class AlatTulis(ProdukABC):
    """Alat tulis — harga satuan, kategori 'Alat Tulis'."""

    def __init__(self, nama, stok, harga_satuan):
        super().__init__(nama, stok)
        self._harga_satuan = harga_satuan

    @property
    def harga(self):
        return self._harga_satuan

    @property
    def kategori(self):
        return "Alat Tulis"


class LaptopKampus(ProdukABC):
    """Laptop refurbished kampus — harga dengan diskon khusus mahasiswa."""

    DISKON_MAHASISWA = 0.05     # 5% diskon

    def __init__(self, nama, stok, harga_normal):
        super().__init__(nama, stok)
        self._harga_normal = harga_normal

    @property
    def harga(self):
        return self._harga_normal * (1 - self.DISKON_MAHASISWA)

    @property
    def kategori(self):
        return "Laptop"

    @property
    def harga_normal(self):
        return self._harga_normal


# Demonstrasi abstract property
print("\n  Katalog Koperasi Kampus Universitas Mulawarman:")
print("  " + "-" * 65)
print(f"  {'Kategori':>12}  {'Nama Produk':<28} {'Harga':>14}  {'Stok'}")
print("  " + "-" * 65)

katalog = [
    BukuKuliah("Pemrograman Python Dasar", 15, 85_000),
    BukuKuliah("Struktur Data & Algoritma", 8,  120_000),
    AlatTulis("Pulpen Pilot G2",           50, 8_500),
    AlatTulis("Penggaris 30cm",            30, 5_000),
    AlatTulis("Buku Tulis Sinar Dunia",    0,  12_000),
    LaptopKampus("Lenovo ThinkPad T14 Refurb", 3, 8_500_000),
]

for produk in katalog:
    produk.info()

print()

# isinstance() mengenali ABC
buku = BukuKuliah("Kalkulus", 5, 95_000)
print(f"  isinstance(buku, ProdukABC)    : {isinstance(buku, ProdukABC)}")
print(f"  isinstance(buku, BukuKuliah)   : {isinstance(buku, BukuKuliah)}")
print(f"  issubclass(BukuKuliah, ProdukABC): {issubclass(BukuKuliah, ProdukABC)}")
print()


# ======================================================================
# BAGIAN 4: ABC dengan Method Konkret dan Abstrak Bercampur
#           Kelas abstrak BISA punya method konkret yang memanggil
#           method abstrak — ini adalah inti dari Template Method.
# ======================================================================
print("=" * 60)
print("BAGIAN 4: Method Konkret + Abstrak Bercampur")
print("=" * 60)

class BentukGeometri(ABC):
    """
    Kelas abstrak bentuk geometri.
    - luas() dan keliling() WAJIB diimplementasikan (abstrak)
    - info() sudah ada implementasinya (konkret) dan memanggil
      kedua method abstrak di atas — polimorfisme + abstraksi!
    """

    def __init__(self, warna="putih"):
        self.warna = warna

    @abstractmethod
    def luas(self) -> float:
        pass

    @abstractmethod
    def keliling(self) -> float:
        pass

    @abstractmethod
    def nama_bentuk(self) -> str:
        pass

    def info(self):
        """Method konkret — memanfaatkan semua method abstrak di atas."""
        print(f"  Bentuk    : {self.nama_bentuk()}")
        print(f"  Warna     : {self.warna}")
        print(f"  Luas      : {self.luas():.4f} satuan^2")
        print(f"  Keliling  : {self.keliling():.4f} satuan")

    def bandingkan_luas(self, lain):
        """Membandingkan luas dua bentuk — hanya perlu tahu interface-nya."""
        if self.luas() > lain.luas():
            return f"{self.nama_bentuk()} lebih besar dari {lain.nama_bentuk()}"
        elif self.luas() < lain.luas():
            return f"{self.nama_bentuk()} lebih kecil dari {lain.nama_bentuk()}"
        else:
            return f"{self.nama_bentuk()} sama luas dengan {lain.nama_bentuk()}"


class Lingkaran(BentukGeometri):
    def __init__(self, jari_jari, warna="putih"):
        super().__init__(warna)
        self.r = jari_jari

    def luas(self):
        return math.pi * self.r ** 2

    def keliling(self):
        return 2 * math.pi * self.r

    def nama_bentuk(self):
        return f"Lingkaran (r={self.r})"


class PersegiPanjang(BentukGeometri):
    def __init__(self, panjang, lebar, warna="putih"):
        super().__init__(warna)
        self.panjang = panjang
        self.lebar   = lebar

    def luas(self):
        return self.panjang * self.lebar

    def keliling(self):
        return 2 * (self.panjang + self.lebar)

    def nama_bentuk(self):
        return f"Persegi Panjang ({self.panjang}x{self.lebar})"


class SegitigaSamaKaki(BentukGeometri):
    def __init__(self, alas, tinggi, warna="putih"):
        super().__init__(warna)
        self.alas   = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

    def keliling(self):
        sisi = math.sqrt((self.alas / 2) ** 2 + self.tinggi ** 2)
        return self.alas + 2 * sisi

    def nama_bentuk(self):
        return f"Segitiga Sama Kaki (a={self.alas}, t={self.tinggi})"


bentuk_list = [
    Lingkaran(7, "merah"),
    PersegiPanjang(10, 5, "biru"),
    SegitigaSamaKaki(6, 4, "hijau"),
]

print()
for bentuk in bentuk_list:
    bentuk.info()
    print()

# Fungsi generik yang bekerja dengan SEMUA subkelas BentukGeometri
def cari_luas_terbesar(daftar_bentuk):
    """Hanya peduli pada interface — tidak peduli tipe konkret."""
    return max(daftar_bentuk, key=lambda b: b.luas())

terbesar = cari_luas_terbesar(bentuk_list)
print(f"  Bentuk dengan luas terbesar: {terbesar.nama_bentuk()}")
print(f"  Luas: {terbesar.luas():.4f} satuan^2")
print()

lingkaran = Lingkaran(5)
persegi   = PersegiPanjang(8, 4)
print(f"  Perbandingan: {lingkaran.bandingkan_luas(persegi)}")
