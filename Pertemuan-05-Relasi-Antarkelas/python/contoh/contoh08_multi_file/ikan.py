"""
Modul ikan: berisi kelas Ikan.

Bagian dari Contoh 08 - Program Banyak File (Pertemuan 05).
File ini hanya berisi kelas. Jalankan main.py, bukan file ini.
"""


class Ikan:
    """Seekor ikan hias."""

    def __init__(self, nama: str, jenis: str):
        self._nama = nama
        self._jenis = jenis

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"{self._nama} (ikan {self._jenis})"
