"""
Solusi Latihan 01 - Kelas Buku
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
1. Buat kelas Buku dengan konstruktor yang menerima judul, penulis, tahun.
2. Simpan ketiganya sebagai atribut (self.judul, dst).
3. Method tampilkan_info() mencetak data; method umur(tahun_sekarang)
   MENGEMBALIKAN selisih tahun.

Cara menjalankan:
    python latihan01_buku.py
"""


class Buku:
    """Data sebuah buku."""

    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

    def tampilkan_info(self):
        print(f"{self.judul} - {self.penulis} ({self.tahun})")

    def umur(self, tahun_sekarang):
        return tahun_sekarang - self.tahun


def main():
    buku1 = Buku("Laskar Pelangi", "Andrea Hirata", 2005)
    buku2 = Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980)
    buku3 = Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009)

    print("=== RAK BUKU ===")
    buku1.tampilkan_info()
    buku2.tampilkan_info()
    buku3.tampilkan_info()

    print()
    print("=== UMUR BUKU DI TAHUN 2026 ===")
    print(f"{buku1.judul}: {buku1.umur(2026)} tahun")
    print(f"{buku2.judul}: {buku2.umur(2026)} tahun")
    print(f"{buku3.judul}: {buku3.umur(2026)} tahun")


if __name__ == "__main__":
    main()
