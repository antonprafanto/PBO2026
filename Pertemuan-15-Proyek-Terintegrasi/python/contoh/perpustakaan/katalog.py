"""
Modul katalog: kelas Katalog yang menyimpan banyak Buku.
"""

from perpustakaan.buku import Buku  # impor absolut: diawali nama package
from perpustakaan.pengecualian import BukuTidakDitemukanError


class Katalog:
    """Daftar buku perpustakaan, dicari berdasarkan kode."""

    def __init__(self):
        self._daftar: dict[str, Buku] = {}  # kode -> Buku

    def tambah(self, buku: Buku):
        self._daftar[buku.kode] = buku

    def cari(self, kode: str) -> Buku:
        """Mengembalikan Buku, atau melempar BukuTidakDitemukanError."""
        if kode not in self._daftar:
            raise BukuTidakDitemukanError(kode)
        return self._daftar[kode]

    def semua(self) -> list[Buku]:
        return list(self._daftar.values())
