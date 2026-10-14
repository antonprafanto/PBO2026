"""
Contoh 03 - Pernyataan with: Membuka dan Menutup Sumber Daya dengan Aman
Pertemuan 15 - Proyek Terintegrasi

File, koneksi printer, atau koneksi database adalah SUMBER DAYA: setelah
dibuka, ia wajib ditutup lagi. Pernyataan with menjamin penutupan itu,
bahkan ketika terjadi error di tengah blok.

Objek yang bisa dipakai dengan with disebut context manager. Ia punya dua
method khusus:
- __enter__() : dijalankan saat masuk ke blok with
- __exit__()  : dijalankan SELALU saat keluar dari blok, ada error atau tidak

Cara menjalankan:
    python contoh03_with_aman.py
"""

import tempfile
from pathlib import Path


class SambunganPrinter:
    """Sumber daya pura-pura: setelah dibuka, wajib ditutup lagi."""

    def __init__(self, nama: str):
        self._nama = nama

    def __enter__(self) -> "SambunganPrinter":  # [1] saat masuk blok with
        print(f"  [{self._nama}] sambungan dibuka")
        return self  # objek inilah yang diterima variabel setelah "as"

    def __exit__(self, jenis_error, error, jejak) -> bool:  # [2] SELALU dipanggil
        print(f"  [{self._nama}] sambungan ditutup")
        return False  # [3] False: error (jika ada) tetap diteruskan ke luar

    def cetak(self, halaman: str):
        if halaman == "":
            raise ValueError("Halaman kosong tidak bisa dicetak")
        print(f"  [{self._nama}] mencetak {halaman}")


def main():
    print("=== 1. BLOK SELESAI TANPA ERROR ===")
    with SambunganPrinter("Printer Lab") as printer:
        printer.cetak("Laporan Praktikum")
    print("Setelah blok selesai")

    print()
    print("=== 2. ERROR DI TENGAH BLOK ===")
    try:
        with SambunganPrinter("Printer Lab") as printer:
            printer.cetak("Halaman 1")
            printer.cetak("")  # [4] melempar ValueError
            printer.cetak("Halaman 3")  # tidak pernah dijalankan
    except ValueError as e:
        print(f"Error ditangkap: {e}")  # [5] sambungan SUDAH ditutup di sini

    print()
    print("=== 3. DUA SUMBER DAYA SEKALIGUS ===")
    with SambunganPrinter("Printer A") as a, SambunganPrinter("Printer B") as b:
        a.cetak("Sampul")
        b.cetak("Isi")
    print("Ditutup dengan urutan terbalik: yang terakhir dibuka, pertama ditutup")

    print()
    print("=== 4. MENULIS DAN MEMBACA FILE ===")
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "daftar-hadir.txt"
        with open(path, "w", encoding="utf-8") as penulis:  # [6]
            for nama in ["Ayu", "Bima", "Citra"]:
                penulis.write(nama + "\n")
        with open(path, encoding="utf-8") as pembaca:
            for baris in pembaca:
                print(f"Hadir: {baris.strip()}")


if __name__ == "__main__":
    main()
