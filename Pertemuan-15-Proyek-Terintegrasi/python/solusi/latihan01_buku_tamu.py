"""
Solusi Latihan 01 - Buku Tamu Pameran
Pertemuan 15 - Proyek Terintegrasi

Ide penyelesaian:
1. Tulis 3 tamu pertama dengan mode "w" (file baru), satu tamu per baris
   dengan format "Nama - Asal".
2. Tambahkan tamu susulan dengan mode "a" (append), isi lama tidak hilang.
3. Baca file baris demi baris, pecah dengan split(" - "), lalu tampilkan
   bernomor sambil menghitung jumlah tamu dan tamu dari Samarinda.
Semua file dibuat di folder sementara, jadi tidak ada sisa file.

Cara menjalankan:
    python latihan01_buku_tamu.py
"""

import tempfile
from pathlib import Path


def tulis_tamu(path: Path, daftar: list[tuple[str, str]], mode: str):
    """Menulis tamu ke file. mode "w" = file baru, mode "a" = tambah di akhir."""
    with open(path, mode, encoding="utf-8") as berkas:
        for nama, asal in daftar:
            berkas.write(f"{nama} - {asal}\n")


def main():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "buku-tamu.txt"

        print("=== BUKU TAMU PAMERAN PROYEK PBO ===")
        tulis_tamu(path, [("Ayu Lestari", "Samarinda"),
                          ("Bima Saputra", "Balikpapan"),
                          ("Citra Dewi", "Samarinda")], "w")
        print(f"3 tamu pertama ditulis ke {path.name}")
        tulis_tamu(path, [("Dimas Pratama", "Bontang")], "a")
        print("1 tamu susulan ditambahkan")

        print()
        print("Isi buku tamu:")
        jumlah = 0
        dari_samarinda = 0
        with open(path, encoding="utf-8") as berkas:
            for baris in berkas:
                nama, asal = baris.strip().split(" - ")
                jumlah += 1
                if asal == "Samarinda":
                    dari_samarinda += 1
                print(f"{jumlah}. {nama} ({asal})")

    print()
    print(f"Jumlah tamu         : {jumlah}")
    print(f"Tamu dari Samarinda : {dari_samarinda}")


if __name__ == "__main__":
    main()
