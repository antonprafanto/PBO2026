"""
Contoh 01 - Masalah: Kelas Induk yang Terlalu Umum
Pertemuan 10 - Abstract Class dan Interface

BangunDatar di sini masih kelas induk BIASA (belum abstrak). Akibatnya:
1. Objek "bangun datar umum" bisa dibuat, padahal tidak ada artinya.
2. Kelas anak yang LUPA menulis luas() tidak diprotes sama sekali.
   Ia diam-diam memakai luas() milik induk yang selalu 0.

Contoh 02 memperbaiki kedua masalah ini dengan kelas abstrak.

Cara menjalankan:
    python contoh01_masalah_induk_umum.py
"""


class BangunDatar:
    """Kelas induk biasa (BELUM abstrak) untuk semua bangun datar."""

    def __init__(self, nama: str):
        self.nama = nama

    def luas(self) -> int:
        return 0  # [1] luas "bangun datar umum"? Tidak ada jawaban yang masuk akal

    def info(self) -> str:
        return f"{self.nama}: luas {self.luas()} cm2"


class Persegi(BangunDatar):
    """Persegi dengan panjang sisi tertentu."""

    def __init__(self, sisi: int):
        super().__init__("Persegi")
        self.sisi = sisi

    def luas(self) -> int:  # override dengan benar
        return self.sisi * self.sisi


class Segitiga(BangunDatar):
    """Segitiga dengan alas dan tinggi."""

    def __init__(self, alas: int, tinggi: int):
        super().__init__("Segitiga")
        self.alas = alas
        self.tinggi = tinggi

    # [2] Pemrogram LUPA menulis method luas() di sini!


def main():
    print("=== MASALAH 1: OBJEK 'UMUM' BISA DIBUAT ===")
    misterius = BangunDatar("Bangun datar misterius")  # [3] tidak ada yang melarang
    print(misterius.info())

    print()
    print("=== MASALAH 2: LUPA OVERRIDE, TIDAK ADA YANG PROTES ===")
    daftar = [Persegi(5), Segitiga(6, 4)]
    for bangun in daftar:
        print(bangun.info())  # [4] Segitiga memakai luas() milik induk
    print("Padahal luas segitiga seharusnya 6 x 4 / 2 = 12 cm2!")


if __name__ == "__main__":
    main()
