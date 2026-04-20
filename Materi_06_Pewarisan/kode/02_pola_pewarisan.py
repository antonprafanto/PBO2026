"""
Kode Praktik - Materi 06: Pewarisan (Inheritance)
File: 02_pola_pewarisan.py
Topik: Multilevel, Multiple Inheritance, MRO, dan Mixin

Jalankan: python 02_pola_pewarisan.py
"""

# ======================================================================
# BAGIAN 1: Multilevel Inheritance - Rantai Kendaraan
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Multilevel Inheritance - Kendaraan -> Mobil -> Sedan")
print("=" * 60)

class Kendaraan:
    """Kelas paling dasar - semua kendaraan."""
    def __init__(self, merk, tahun, cc_mesin):
        self.merk     = merk
        self.tahun    = tahun
        self.cc_mesin = cc_mesin

    def nyalakan_mesin(self):
        print(f"  [K] {self.merk} ({self.tahun}): Mesin {self.cc_mesin}cc menyala. Vroom!")

    def matikan_mesin(self):
        print(f"  [L] {self.merk}: Mesin dimatikan.")

    def __str__(self):
        return f"{self.merk} ({self.tahun}, {self.cc_mesin}cc)"


class Mobil(Kendaraan):
    """Kendaraan darat roda empat."""
    def __init__(self, merk, tahun, cc_mesin, jumlah_pintu=4):
        super().__init__(merk, tahun, cc_mesin)
        self.jumlah_pintu = jumlah_pintu
        self._kecepatan   = 0

    def gas(self, tambah_km_per_jam):
        self._kecepatan += tambah_km_per_jam
        print(f"  [>] {self.merk} mempercepat -> {self._kecepatan} km/jam")

    def rem(self):
        self._kecepatan = 0
        print(f"  [!] {self.merk} berhenti.")

    @property
    def kecepatan(self):
        return self._kecepatan

    def __str__(self):
        return f"Mobil | {super().__str__()} | {self.jumlah_pintu} pintu"


class Sedan(Mobil):
    """Mobil jenis sedan - spesifikasi lebih detail."""
    def __init__(self, merk, tahun, cc_mesin, transmisi="Manual", sunroof=False):
        super().__init__(merk, tahun, cc_mesin, jumlah_pintu=4)
        self.transmisi = transmisi
        self.sunroof   = sunroof

    def buka_sunroof(self):
        if not self.sunroof:
            print(f"  [X] {self.merk} tidak memiliki sunroof.")
            return
        print(f"  [*] Sunroof {self.merk} dibuka!")

    def __str__(self):
        fitur = "| Sunroof [OK]" if self.sunroof else ""
        return f"Sedan | {super().__str__()} | {self.transmisi} {fitur}"


# Demo: kelas terbawah mewarisi dari semua di atasnya
camry = Sedan("Toyota Camry", 2024, 2500, "Automatic", sunroof=True)
camry.nyalakan_mesin()   # dari Kendaraan
camry.gas(60)            # dari Mobil
camry.gas(40)            # dari Mobil
camry.buka_sunroof()     # milik Sedan
camry.rem()              # dari Mobil
camry.matikan_mesin()    # dari Kendaraan
print(camry)

# Lihat MRO
print(f"\n  MRO Sedan: {[k.__name__ for k in Sedan.__mro__]}")
# Sedan -> Mobil -> Kendaraan -> object


# ======================================================================
# BAGIAN 2: Multiple Inheritance - Itik yang Bisa Segalanya
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Multiple Inheritance - BisaTerbang + BisaBerenang")
print("=" * 60)

class BisaTerbang:
    """Mixin kemampuan terbang."""
    def terbang(self):
        print(f"  [^] {self.nama} mengepakkan sayap dan terbang!")

    def mendarat(self):
        print(f"  [v] {self.nama} mendarat dengan mulus.")


class BisaBerenang:
    """Mixin kemampuan berenang."""
    def renang(self):
        print(f"  [~] {self.nama} berenang di air!")

    def menyelam(self):
        print(f"  [_] {self.nama} menyelam ke kedalaman.")


class BisaLari:
    """Mixin kemampuan berlari."""
    def lari(self):
        print(f"  [>] {self.nama} berlari kencang!")


class Burung:
    def __init__(self, nama, spesies):
        self.nama    = nama
        self.spesies = spesies

    def berkicau(self):
        print(f"  [J] {self.nama} ({self.spesies}) berkicau.")


# Itik bisa terbang, berenang, LARI, DAN berkicau
class Itik(BisaTerbang, BisaBerenang, BisaLari, Burung):
    def __init__(self, nama):
        super().__init__(nama, "Anas platyrhynchos")  # Burung.__init__

    def quack(self):
        print(f"  [Q] {self.nama}: Kwek kwek kwek!")


# Penguin hanya bisa berenang dan berlari (tidak bisa terbang)
class Penguin(BisaBerenang, BisaLari, Burung):
    def __init__(self, nama):
        super().__init__(nama, "Spheniscidae")

    def slide(self):
        print(f"  [-] {self.nama} meluncur di es!")


donald = Itik("Donald")
donald.berkicau()
donald.terbang()
donald.renang()
donald.menyelam()
donald.lari()
donald.quack()

print()
pingu = Penguin("Pingu")
pingu.berkicau()
pingu.renang()
pingu.lari()
pingu.slide()
# pingu.terbang()   # <- AttributeError: tidak bisa terbang!

print(f"\n  MRO Itik   : {[k.__name__ for k in Itik.__mro__]}")
print(f"  MRO Penguin: {[k.__name__ for k in Penguin.__mro__]}")


# ======================================================================
# BAGIAN 3: MRO - Membuktikan Urutan Pencarian Method
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: MRO - Urutan Pencarian Method")
print("=" * 60)

class A:
    def hello(self):
        print("  Hello dari A")

class B(A):
    def hello(self):
        print("  Hello dari B")

class C(A):
    def hello(self):
        print("  Hello dari C")

class D(B, C):
    pass   # tidak override hello, akan mencari ke atas

class E(C, B):
    pass   # urutan terbalik!


print("  D().hello() ->", end=" ")
D().hello()   # B ditemukan lebih dulu

print("  E().hello() ->", end=" ")
E().hello()   # C ditemukan lebih dulu

print(f"\n  MRO D: {[k.__name__ for k in D.__mro__]}")
print(f"  MRO E: {[k.__name__ for k in E.__mro__]}")
# MRO D: D -> B -> C -> A -> object   (B sebelum C)
# MRO E: E -> C -> B -> A -> object   (C sebelum B)


# ======================================================================
# BAGIAN 4: Mixin - Fitur Modular yang Bisa Ditempel ke Mana Saja
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 4: Mixin - JSONMixin, LogMixin, ValidasiMixin")
print("=" * 60)

import json
from datetime import datetime


class JSONMixin:
    """Tambahkan kemampuan serialisasi ke JSON."""
    def to_json(self):
        return json.dumps(
            {k: v for k, v in self.__dict__.items() if not k.startswith('_')},
            default=str, ensure_ascii=False, indent=2
        )

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        obj  = cls.__new__(cls)
        obj.__dict__.update(data)
        return obj


class LogMixin:
    """Tambahkan kemampuan logging sederhana."""
    def log(self, pesan, level="INFO"):
        waktu = datetime.now().strftime("%H:%M:%S")
        print(f"  [{waktu}] [{level}] [{self.__class__.__name__}] {pesan}")


class ValidasiMixin:
    """Tambahkan metode validasi umum."""
    @staticmethod
    def wajib_isi(nilai, nama_field):
        if nilai is None or str(nilai).strip() == "":
            raise ValueError(f"'{nama_field}' tidak boleh kosong!")
        return str(nilai).strip()

    @staticmethod
    def angka_positif(nilai, nama_field):
        if nilai <= 0:
            raise ValueError(f"'{nama_field}' harus lebih dari 0, dapat: {nilai}")
        return nilai


# Produk menggunakan semua Mixin sekaligus
class Produk(JSONMixin, LogMixin, ValidasiMixin):
    def __init__(self, kode, nama, harga, stok):
        self.kode  = self.wajib_isi(kode, "kode")
        self.nama  = self.wajib_isi(nama, "nama")
        self.harga = self.angka_positif(harga, "harga")
        self.stok  = stok
        self.log(f"Produk '{self.nama}' dibuat.")

    def jual(self, qty):
        if qty > self.stok:
            self.log(f"Gagal jual {qty} - stok hanya {self.stok}", "WARNING")
            return
        self.stok -= qty
        self.log(f"Terjual {qty} unit. Sisa stok: {self.stok}")


laptop = Produk("PRD-001", "Laptop ASUS", 8_500_000, 10)
laptop.jual(3)
laptop.jual(9)   # Gagal - stok tidak cukup

print("\n  JSON Produk:")
print(laptop.to_json())

print()
