"""
Modul item_pesanan: kelas ItemPesanan.

Relasi yang terlihat di sini:
- ItemPesanan --> Menu : ASOSIASI (item menunjuk ke menu yang dipesan)

Yang baru di Pertemuan 13: ItemPesanan dipindah dari pesanan.py ke file
sendiri. Alasannya, diskon.py membutuhkan ItemPesanan, sementara pesanan.py
membutuhkan Diskon. Jika ItemPesanan tetap di pesanan.py, kedua file akan
saling meng-import (circular import) dan Python akan gagal memuatnya.
"""

from kedaikita.menu import Menu


class ItemPesanan:
    """Satu baris pesanan: menu apa dan berapa porsi."""

    def __init__(self, menu: Menu, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._menu = menu  # menyimpan REFERENSI ke objek Menu
        self._jumlah = jumlah

    @property
    def menu(self) -> Menu:
        return self._menu

    @property
    def jumlah(self) -> int:
        return self._jumlah

    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah

    def __str__(self) -> str:
        return f"{self._jumlah} x {self._menu.nama}"
