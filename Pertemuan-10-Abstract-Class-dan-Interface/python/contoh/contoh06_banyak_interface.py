"""
Contoh 06 - Satu Kelas, Banyak Kemampuan
Pertemuan 10 - Abstract Class dan Interface

- Hewan adalah kelas abstrak (punya data nama + method abstrak bersuara).
- BisaTerbang dan BisaBerenang adalah "interface" (ABC berisi method
  abstrak saja).
- Bebek mewarisi Hewan DAN memenuhi dua kontrak sekaligus.
- Pesawat bukan Hewan, tetapi tetap BisaTerbang.

Cara menjalankan:
    python contoh06_banyak_interface.py
"""

from abc import ABC, abstractmethod


class Hewan(ABC):
    """Kelas abstrak: semua hewan punya nama dan suara."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    @abstractmethod
    def bersuara(self) -> str:
        """Bunyi khas hewan."""


class BisaTerbang(ABC):
    """Kontrak kemampuan terbang."""

    @abstractmethod
    def terbang(self) -> str:
        """Menjelaskan cara terbang."""


class BisaBerenang(ABC):
    """Kontrak kemampuan berenang."""

    @abstractmethod
    def berenang(self) -> str:
        """Menjelaskan cara berenang."""


class Bebek(Hewan, BisaTerbang, BisaBerenang):  # [1] satu induk + dua kemampuan
    """Bebek: hewan yang bisa terbang dan berenang."""

    def bersuara(self) -> str:
        return "Kwek kwek!"

    def terbang(self) -> str:
        return f"{self.nama} terbang rendah di atas sawah"

    def berenang(self) -> str:
        return f"{self.nama} mengapung sambil mengayuh kaki"


class Ikan(Hewan, BisaBerenang):
    """Ikan: hewan yang bisa berenang, tetapi tidak bisa terbang."""

    def bersuara(self) -> str:
        return "(diam saja)"

    def berenang(self) -> str:
        return f"{self.nama} berenang di Sungai Mahakam"


class Pesawat(BisaTerbang):  # [2] bukan Hewan, tetapi BisaTerbang
    """Pesawat: benda mati yang bisa terbang."""

    def __init__(self, nama: str):
        self._nama = nama

    def terbang(self) -> str:
        return f"Pesawat {self._nama} terbang di atas awan"


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    bebek = Bebek("Bebek Kuning")
    ikan = Ikan("Ikan Patin")
    pesawat = Pesawat("Rajawali 01")

    print("=== SEMUA HEWAN BERSUARA ===")
    semua_hewan: list[Hewan] = [bebek, ikan]
    for hewan in semua_hewan:
        print(f"{hewan.nama}: {hewan.bersuara()}")

    print()
    print("=== YANG BISA TERBANG ===")
    penerbang: list[BisaTerbang] = [bebek, pesawat]  # [3] dikelompokkan per kontrak
    for benda in penerbang:
        print(benda.terbang())

    print()
    print("=== YANG BISA BERENANG ===")
    perenang: list[BisaBerenang] = [bebek, ikan]
    for benda in perenang:
        print(benda.berenang())

    print()
    print("=== CEK KEMAMPUAN ===")
    print(f"{'Kelas':<8} | {'Hewan':<5} | {'Terbang':<7} | Berenang")
    for benda in [bebek, ikan, pesawat]:
        nama = type(benda).__name__
        hewan = ya_tidak(isinstance(benda, Hewan))  # [4]
        terbang = ya_tidak(isinstance(benda, BisaTerbang))
        berenang = ya_tidak(isinstance(benda, BisaBerenang))
        print(f"{nama:<8} | {hewan:<5} | {terbang:<7} | {berenang}")


if __name__ == "__main__":
    main()
