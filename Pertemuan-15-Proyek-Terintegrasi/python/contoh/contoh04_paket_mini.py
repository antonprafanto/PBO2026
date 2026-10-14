"""
Contoh 04 - Package Mini: Satu Folder, Beberapa Modul
Pertemuan 15 - Proyek Terintegrasi

Kelas-kelas perpustakaan tidak ditulis di file ini, tetapi di dalam
PACKAGE perpustakaan (sebuah folder berisi __init__.py):

    contoh/
    +-- contoh04_paket_mini.py   <- file ini (yang dijalankan)
    +-- perpustakaan/            <- package
        +-- __init__.py
        +-- pengecualian.py
        +-- buku.py
        +-- katalog.py

File ini cukup meng-import kelas yang dibutuhkan dengan nama lengkapnya.

Cara menjalankan (dari folder contoh):
    python contoh04_paket_mini.py
"""

from perpustakaan.buku import Buku  # [1] package.modul import Kelas
from perpustakaan.katalog import Katalog
from perpustakaan.pengecualian import PerpustakaanError


def main():
    katalog = Katalog()
    katalog.tambah(Buku("B01", "Laskar Pelangi", "Andrea Hirata"))
    katalog.tambah(Buku("B02", "Bumi Manusia", "Pramoedya Ananta Toer"))
    katalog.tambah(Buku("B03", "Negeri 5 Menara", "Ahmad Fuadi"))

    print("=== KATALOG PERPUSTAKAAN MINI ===")
    for buku in katalog.semua():
        print(buku)

    print()
    print("=== MEMINJAM BUKU ===")
    for kode in ["B02", "B02", "B09"]:  # [2] pinjam B02 dua kali, lalu kode asal
        try:
            buku = katalog.cari(kode)
            buku.pinjam()
            print(f"{kode}: berhasil dipinjam")
        except PerpustakaanError as e:  # [3] menangkap semua error milik package
            print(f"{kode}: gagal, {e}")

    print()
    print("=== KATALOG SETELAH PEMINJAMAN ===")
    for buku in katalog.semua():
        print(buku)


if __name__ == "__main__":
    main()
