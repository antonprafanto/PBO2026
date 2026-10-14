"""
Solusi Latihan 01 - Kelas Abstrak Perangkat
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- Perangkat adalah kelas abstrak. Konstruktor (merek, daya_watt) dan
  method konkret info() cukup ditulis SEKALI di sini.
- jenis() dan fungsi_utama() dibuat abstrak, karena jawabannya berbeda untuk
  setiap perangkat. info() memanggil keduanya (template method kecil).
- total_daya() menerima list Perangkat jenis apa pun.

Cara menjalankan:
    python latihan01_perangkat.py
"""

from abc import ABC, abstractmethod


class Perangkat(ABC):
    """Kelas abstrak untuk semua perangkat elektronik."""

    def __init__(self, merek: str, daya_watt: int):
        self._merek = merek
        self._daya_watt = daya_watt

    @property
    def daya_watt(self) -> int:
        return self._daya_watt

    @abstractmethod
    def jenis(self) -> str:
        """Jenis perangkat, misalnya 'Laptop'."""

    @abstractmethod
    def fungsi_utama(self) -> str:
        """Kegunaan utama perangkat."""

    def info(self) -> str:
        return (f"{self.jenis()} {self._merek} ({self._daya_watt} watt): "
                f"{self.fungsi_utama()}")


class Laptop(Perangkat):
    """Laptop untuk kuliah."""

    def jenis(self) -> str:
        return "Laptop"

    def fungsi_utama(self) -> str:
        return "mengetik laporan dan menulis kode"


class Ponsel(Perangkat):
    """Ponsel pintar."""

    def jenis(self) -> str:
        return "Ponsel"

    def fungsi_utama(self) -> str:
        return "menelepon dan mengirim pesan"


class Printer(Perangkat):
    """Printer di kamar kos."""

    def jenis(self) -> str:
        return "Printer"

    def fungsi_utama(self) -> str:
        return "mencetak tugas kuliah"


def total_daya(daftar: list[Perangkat]) -> int:
    total = 0
    for perangkat in daftar:
        total += perangkat.daya_watt
    return total


def main():
    daftar: list[Perangkat] = [
        Laptop("Lenovo", 65),
        Ponsel("Samsung", 18),
        Printer("Epson", 30),
    ]
    print("=== DAFTAR PERANGKAT ===")
    for perangkat in daftar:
        print(perangkat.info())
    print(f"Total daya jika menyala bersamaan: {total_daya(daftar)} watt")


if __name__ == "__main__":
    main()
