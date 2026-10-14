"""
Solusi Latihan 05 - KedaiKita: Menu Menjadi Kelas Abstrak
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- Versi ringkas Menu (kode, nama, harga) dijadikan kelas abstrak, karena
  di KedaiKita tidak ada "menu umum": setiap menu pasti Makanan atau Minuman.
- kategori() dan keterangan() menjadi method abstrak. Kategori tidak lagi
  dikirim lewat konstruktor, tetapi "dijawab" oleh setiap kelas anak.
- __str__ ditulis SEKALI di Menu dan memanggil kedua method abstrak itu
  (template method). Makanan dan Minuman tidak perlu meng-override __str__.

Cara menjalankan:
    python latihan05_menu_abstrak.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Menu(ABC):
    """Kelas abstrak: data bersama semua menu KedaiKita."""

    def __init__(self, kode: str, nama: str, harga: int):
        self._kode = kode
        self._nama = nama
        self._harga = harga

    @abstractmethod
    def kategori(self) -> str:
        """'Makanan' atau 'Minuman'."""

    @abstractmethod
    def keterangan(self) -> str:
        """Informasi khusus setiap jenis menu."""

    def __str__(self) -> str:
        return (f"[{self._kode}] {self._nama} ({self.kategori()}) - "
                f"{format_rupiah(self._harga)} | {self.keterangan()}")


class Makanan(Menu):
    """Makanan dengan level pedas 0 sampai 5."""

    def __init__(self, kode: str, nama: str, harga: int, level_pedas: int):
        super().__init__(kode, nama, harga)
        self._level_pedas = level_pedas

    def kategori(self) -> str:
        return "Makanan"

    def keterangan(self) -> str:
        return f"pedas level {self._level_pedas}"


class Minuman(Menu):
    """Minuman yang disajikan dingin atau panas."""

    def __init__(self, kode: str, nama: str, harga: int, dingin: bool):
        super().__init__(kode, nama, harga)
        self._dingin = dingin

    def kategori(self) -> str:
        return "Minuman"

    def keterangan(self) -> str:
        return "dingin" if self._dingin else "panas"


def main():
    daftar_menu: list[Menu] = [
        Minuman("M01", "Kopi Susu Gula Aren", 18000, True),
        Minuman("M02", "Es Teh Manis", 8000, True),
        Makanan("M03", "Nasi Goreng Kampung", 25000, 2),
        Makanan("M04", "Mie Goreng Jawa", 23000, 1),
        Makanan("M05", "Pisang Goreng Keju", 15000, 0),
        Minuman("M06", "Teh Tarik Hangat", 12000, False),
    ]
    print("=== MENU KEDAIKITA (Menu kini abstrak) ===")
    for menu in daftar_menu:
        print(menu)

    print()
    print("=== JUMLAH PER KATEGORI ===")
    jumlah_makanan = 0
    jumlah_minuman = 0
    for menu in daftar_menu:
        if menu.kategori() == "Makanan":
            jumlah_makanan += 1
        else:
            jumlah_minuman += 1
    print(f"Makanan: {jumlah_makanan}")
    print(f"Minuman: {jumlah_minuman}")


if __name__ == "__main__":
    main()
