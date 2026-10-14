"""
Modul penyimpanan: abstraksi tempat menyimpan pesanan.

DIP (Dependency Inversion): Kedai tidak bergantung pada "list di memori"
secara langsung, melainkan pada abstraksi PenyimpananPesanan.
Hari ini kita memakai PenyimpananMemori. Kelak kita bisa membuat
PenyimpananFile atau PenyimpananDatabase TANPA mengubah kelas Kedai
(coba di latihan!).

ISP (Interface Segregation): kontraknya kecil, hanya simpan() dan semua().
"""

from abc import ABC, abstractmethod

from kedaikita.pesanan import Pesanan


class PenyimpananPesanan(ABC):
    """Kontrak penyimpanan pesanan."""

    @abstractmethod
    def simpan(self, pesanan: Pesanan):
        """Menyimpan satu pesanan."""

    @abstractmethod
    def semua(self) -> list[Pesanan]:
        """Semua pesanan yang tersimpan, urut sesuai waktu disimpan."""

    def jumlah(self) -> int:
        return len(self.semua())


class PenyimpananMemori(PenyimpananPesanan):
    """Menyimpan pesanan di list (hilang saat program ditutup)."""

    def __init__(self):
        self._data: list[Pesanan] = []

    def simpan(self, pesanan: Pesanan):
        self._data.append(pesanan)

    def semua(self) -> list[Pesanan]:
        return list(self._data)
