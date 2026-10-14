"""
Contoh 02 - Kelas Abstrak Pertamamu
Pertemuan 10 - Abstract Class dan Interface

- Bentuk mewarisi ABC (Abstract Base Class) dari modul abc.
- luas() dan keliling() diberi dekorator @abstractmethod: method abstrak,
  hanya "janji" tanpa isi. Setiap kelas anak WAJIB mengisinya.
- Objek Bentuk tidak bisa dibuat langsung. Objek kelas anaknya bisa.

Cara menjalankan:
    python contoh02_kelas_abstrak.py
"""

from abc import ABC, abstractmethod


class Bentuk(ABC):  # [1] mewarisi ABC -> kelas ini boleh punya method abstrak
    """Kelas abstrak: konsep umum semua bangun datar."""

    @abstractmethod  # [2] method abstrak: tanpa isi, wajib diisi kelas anak
    def luas(self) -> int:
        """Menghitung luas (cm2)."""

    @abstractmethod
    def keliling(self) -> int:
        """Menghitung keliling (cm)."""


class PersegiPanjang(Bentuk):
    """Persegi panjang dengan panjang dan lebar."""

    def __init__(self, panjang: int, lebar: int):
        self.panjang = panjang
        self.lebar = lebar

    def luas(self) -> int:  # [3] mengisi (meng-override) method abstrak
        return self.panjang * self.lebar

    def keliling(self) -> int:
        return 2 * (self.panjang + self.lebar)


class SegitigaSiku(Bentuk):
    """Segitiga siku-siku dengan alas, tinggi, dan sisi miring."""

    def __init__(self, alas: int, tinggi: int, miring: int):
        self.alas = alas
        self.tinggi = tinggi
        self.miring = miring

    def luas(self) -> int:
        return self.alas * self.tinggi // 2

    def keliling(self) -> int:
        return self.alas + self.tinggi + self.miring


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    # bentuk_umum = Bentuk()  # [4] hapus tanda # di awal baris ini -> TypeError

    kartu = PersegiPanjang(8, 5)
    penggaris = SegitigaSiku(6, 8, 10)
    daftar: list[Bentuk] = [kartu, penggaris]  # [5] list bertipe kelas abstrak

    print("=== DAFTAR BENTUK ===")
    for bentuk in daftar:
        nama = type(bentuk).__name__
        print(f"{nama}: luas {bentuk.luas()} cm2, keliling {bentuk.keliling()} cm")

    print()
    print("=== CEK JENIS ===")
    print(f"kartu dibuat dari kelas: {type(kartu).__name__}")
    print(f"Apakah kartu termasuk Bentuk? {ya_tidak(isinstance(kartu, Bentuk))}")  # [6]


if __name__ == "__main__":
    main()
