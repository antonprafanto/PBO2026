"""
Modul diskon: abstraksi Diskon dan beberapa aturan diskon.

Prinsip yang diterapkan:
- OCP (Open/Closed): ingin promo baru? Buat kelas turunan Diskon yang baru.
  Kelas Pesanan TIDAK perlu diubah sama sekali.
- LSP (Liskov Substitution): semua turunan Diskon bisa dipakai di mana pun
  Diskon diharapkan, dan selalu mengembalikan potongan >= 0.

Di Pertemuan 14 kita mengenali bahwa desain ini adalah pola STRATEGY:
setiap kelas diskon adalah satu "strategi" yang bisa ditukar saat program
berjalan. Strategi baru: DiskonHappyHour.
"""

from abc import ABC, abstractmethod

from kedaikita.item_pesanan import ItemPesanan
from kedaikita.pelanggan import Pelanggan


class Diskon(ABC):
    """Kontrak semua aturan diskon."""

    @abstractmethod
    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        """Besar potongan dalam rupiah (tidak pernah negatif)."""

    @abstractmethod
    def keterangan(self) -> str:
        """Nama singkat diskon untuk ditampilkan di struk."""

    @staticmethod
    def subtotal_dari(daftar_item: list[ItemPesanan]) -> int:
        total = 0
        for item in daftar_item:
            total += item.hitung_subtotal()
        return total


class TanpaDiskon(Diskon):
    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        return 0

    def keterangan(self) -> str:
        return "Tanpa diskon"


class DiskonPersen(Diskon):
    """Promo potongan sekian persen untuk semua item."""

    def __init__(self, persen: int):
        if persen <= 0 or persen > 100:
            raise ValueError("Persen diskon harus 1 sampai 100")
        self._persen = persen

    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        return Diskon.subtotal_dari(daftar_item) * self._persen // 100

    def keterangan(self) -> str:
        return f"Promo {self._persen}%"


class DiskonMember(Diskon):
    """Diskon 10% untuk pelanggan yang sudah punya minimal 10 poin."""

    PERSEN = 10
    MINIMAL_POIN = 10

    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        if pelanggan.poin < DiskonMember.MINIMAL_POIN:
            return 0
        return Diskon.subtotal_dari(daftar_item) * DiskonMember.PERSEN // 100

    def keterangan(self) -> str:
        return "Member 10%"


class DiskonHappyHour(Diskon):
    """Happy hour: diskon 20% khusus untuk item minuman."""

    PERSEN = 20

    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        total_minuman = 0
        for item in daftar_item:
            if item.menu.kategori == "Minuman":
                total_minuman += item.hitung_subtotal()
        return total_minuman * DiskonHappyHour.PERSEN // 100

    def keterangan(self) -> str:
        return "Happy Hour (minuman)"
