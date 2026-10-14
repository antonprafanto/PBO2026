"""
Modul pasangan: kelas GENERIK Pasangan[A, B].

"Generik" artinya tipe isi wadahnya ditentukan saat dipakai, bukan saat
kelasnya ditulis. Pasangan[str, int] berisi (teks, angka), sedangkan
Pasangan[str, Menu] berisi (teks, objek Menu). Satu kelas, banyak kegunaan.

Catatan: Python tidak memeriksa tipe ini saat program berjalan. Petunjuk
tipe (type hint) membantu pembaca dan alat bantu seperti VS Code/mypy.
"""

from typing import Generic, TypeVar

A = TypeVar("A")
B = TypeVar("B")


class Pasangan(Generic[A, B]):
    """Wadah berisi dua nilai: pertama (tipe A) dan kedua (tipe B)."""

    def __init__(self, pertama: A, kedua: B):
        self._pertama = pertama
        self._kedua = kedua

    @property
    def pertama(self) -> A:
        return self._pertama

    @property
    def kedua(self) -> B:
        return self._kedua

    def __str__(self) -> str:
        return f"({self._pertama}, {self._kedua})"
