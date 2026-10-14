"""
Modul pengecualian: exception milik package perpustakaan.

Hierarki:
    Exception
    +-- PerpustakaanError
        +-- BukuTidakDitemukanError
        +-- BukuSedangDipinjamError
"""


class PerpustakaanError(Exception):
    """Induk semua error di package perpustakaan."""


class BukuTidakDitemukanError(PerpustakaanError):
    """Dilempar saat kode buku tidak terdaftar di katalog."""

    def __init__(self, kode: str):
        super().__init__(f"buku dengan kode {kode} tidak ditemukan")
        self.kode = kode


class BukuSedangDipinjamError(PerpustakaanError):
    """Dilempar saat buku yang sedang dipinjam ingin dipinjam lagi."""

    def __init__(self, judul: str):
        super().__init__(f"buku '{judul}' sedang dipinjam")
        self.judul = judul
