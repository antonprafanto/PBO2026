"""
Contoh 08 - Program Multi-File
Pertemuan 05 - Relasi Antar Kelas

Program kecil ini terdiri atas tiga file di folder yang sama:
    ikan.py     -> kelas Ikan
    akuarium.py -> kelas Akuarium (memakai Ikan)
    main.py     -> program utama (file ini)

Cara menjalankan (dari DALAM folder contoh08_multi_file):
    python main.py
"""

from akuarium import Akuarium  # [2] ambil kelas dari file akuarium.py
from ikan import Ikan


def main():
    print("=== AKUARIUM DI MEJA BELAJAR ===")
    akuarium = Akuarium(2)
    akuarium.masukkan(Ikan("Oren", "cupang"))  # [3] objek dari modul lain
    akuarium.masukkan(Ikan("Belang", "koi"))
    akuarium.masukkan(Ikan("Si Biru", "guppy"))
    akuarium.tampilkan()


if __name__ == "__main__":  # [4] main() hanya jalan jika file ini dijalankan langsung
    main()
