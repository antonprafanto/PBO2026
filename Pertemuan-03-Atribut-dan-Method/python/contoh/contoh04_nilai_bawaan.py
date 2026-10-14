"""
Contoh 04 - Parameter dengan Nilai Bawaan (Default)
Pertemuan 03 - Atribut dan Method Lebih Dalam

Parameter boleh diberi nilai bawaan, misalnya ram=8 dan penyimpanan=512.
Jika argumen untuk parameter itu tidak dikirim, nilai bawaanlah yang dipakai.
Akibatnya, SATU konstruktor bisa dipanggil dengan 1, 2, atau 3 argumen.
(Java tidak punya nilai bawaan; Java memakai overloading konstruktor.)

Cara menjalankan:
    python contoh04_nilai_bawaan.py
"""


class Laptop:
    """Laptop dengan kapasitas RAM dan penyimpanan (dalam GB)."""

    def __init__(self, merek, ram=8, penyimpanan=512):  # [1] punya nilai bawaan
        self.merek = merek
        self.ram = ram
        self.penyimpanan = penyimpanan

    def tambah_ram(self, tambahan=8):  # [2] method biasa juga boleh punya nilai bawaan
        self.ram = self.ram + tambahan

    def info(self):
        return f"{self.merek}: RAM {self.ram} GB, SSD {self.penyimpanan} GB"


def main():
    print("=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===")
    laptop_ayu = Laptop("Asus")  # [3] ram dan penyimpanan memakai nilai bawaan
    laptop_bima = Laptop("Lenovo", 16)  # [4] penyimpanan memakai nilai bawaan
    laptop_citra = Laptop("Acer", 16, 1024)  # [5] semua argumen dikirim
    laptop_dimas = Laptop("HP", penyimpanan=256)  # [6] argumen bernama (keyword)
    print(laptop_ayu.info())
    print(laptop_bima.info())
    print(laptop_citra.info())
    print(laptop_dimas.info())

    print()
    print("=== MENAMBAH RAM ===")
    laptop_ayu.tambah_ram()  # [7] tambahan memakai nilai bawaan 8
    laptop_bima.tambah_ram(16)
    print(laptop_ayu.info())
    print(laptop_bima.info())


if __name__ == "__main__":
    main()
