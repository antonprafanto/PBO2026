"""
KedaiKita - Pertemuan 15: Proyek Terintegrasi

Titik masuk aplikasi kasir KedaiKita. Semua kelas kini berada di dalam
package kedaikita/ dan data disimpan di folder data/.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py           -> mode interaktif (kasir mengetik pilihan)
    python main.py --demo    -> mode demo (tanpa input, untuk dicoba cepat)

Cara menjalankan unit test:
    python -m unittest discover -s tests -v
"""

import sys
from pathlib import Path

from kedaikita.aplikasi import AplikasiKasir
from kedaikita.pengecualian import KedaiError

# Folder data dicari relatif terhadap lokasi file ini, sehingga program tetap
# berjalan walaupun dijalankan dari folder lain.
FOLDER_DATA = Path(__file__).resolve().parent / "data"


def main():
    aplikasi = AplikasiKasir(FOLDER_DATA)
    try:
        if "--demo" in sys.argv:
            aplikasi.jalankan_demo()
        else:
            aplikasi.jalankan()
    except (KedaiError, OSError) as e:
        # Lapisan terluar: error tak terduga ditampilkan dengan sopan
        print(f"Terjadi kesalahan: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
