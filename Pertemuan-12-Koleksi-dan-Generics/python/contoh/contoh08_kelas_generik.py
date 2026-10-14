"""
Contoh 08 - Kelas Generik Kotak[T] dan Petunjuk Tipe
Pertemuan 12 - Koleksi dan Generics

- TypeVar("T") membuat "variabel tipe": T bisa berarti int, str, dan seterusnya.
- class Kotak(Generic[T]) adalah kelas GENERIK: tipe isinya ditentukan saat
  dipakai, misalnya Kotak[int] atau Kotak[str].
- def pertama(daftar: list[T]) -> T adalah fungsi generik.
- PENTING: Python TIDAK memeriksa petunjuk tipe (type hint) saat program
  berjalan. Petunjuk tipe membantu pembaca, VS Code, dan alat seperti mypy.

Cara menjalankan:
    python contoh08_kelas_generik.py
"""

from typing import Generic, TypeVar

T = TypeVar("T")  # [1] variabel tipe bernama T


class Kotak(Generic[T]):  # [2] kelas generik dengan satu parameter tipe
    """Kotak yang berisi satu barang bertipe T."""

    def __init__(self, isi: T):
        self._isi = isi

    @property
    def isi(self) -> T:  # [3] tipe kembalian mengikuti T
        return self._isi

    def ganti(self, isi_baru: T):
        self._isi = isi_baru

    def __str__(self) -> str:
        return f"Kotak berisi {self._isi}"


class KotakLama:
    """Kotak tanpa petunjuk tipe: boleh diisi apa saja."""

    def __init__(self, isi):
        self.isi = isi


def pertama(daftar: list[T]) -> T:  # [4] fungsi generik
    """Mengembalikan isi pertama sebuah list, apa pun tipe isinya."""
    return daftar[0]


def main():
    kotak_angka: Kotak[int] = Kotak(42)  # [5] di sini T = int
    kotak_teks: Kotak[str] = Kotak("bekal nasi kuning")  # di sini T = str
    print("=== KOTAK GENERIK ===")
    print(kotak_angka)
    print(kotak_teks)
    print(f"Isi kotak angka + 8   : {kotak_angka.isi + 8}")
    print(f"Isi kotak teks kapital: {kotak_teks.isi.upper()}")
    kotak_angka.ganti(100)
    print(f"Setelah diganti       : {kotak_angka}")

    print()
    print("=== FUNGSI/METHOD GENERIK ===")
    print(f"Hari pertama : {pertama(['Senin', 'Rabu', 'Jumat'])}")
    print(f"Angka pertama: {pertama([10, 20, 30])}")

    print()
    print("=== KOTAK TANPA TIPE ===")
    kotak_lama = KotakLama("pulpen")
    print(f"Isi kotak lama: {kotak_lama.isi.upper()}")  # [6]


if __name__ == "__main__":
    main()
