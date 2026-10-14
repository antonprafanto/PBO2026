"""
Modul buku: kelas Buku.

Perhatikan baris import di bawah: modul lain di dalam package yang sama
di-import dengan nama lengkapnya (impor absolut), diawali nama package.
"""

from perpustakaan.pengecualian import BukuSedangDipinjamError


class Buku:
    """Satu buku di perpustakaan. Status pinjam hanya berubah lewat method."""

    def __init__(self, kode: str, judul: str, penulis: str):
        self._kode = kode
        self._judul = judul
        self._penulis = penulis
        self._dipinjam = False

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def judul(self) -> str:
        return self._judul

    def pinjam(self):
        if self._dipinjam:
            raise BukuSedangDipinjamError(self._judul)
        self._dipinjam = True

    def kembalikan(self):
        self._dipinjam = False

    def __str__(self) -> str:
        status = "dipinjam" if self._dipinjam else "tersedia"
        return f"[{self._kode}] {self._judul} - {self._penulis} ({status})"
