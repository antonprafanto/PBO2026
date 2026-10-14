"""
Contoh 04 - Method dengan Parameter dan Nilai Kembalian
Pertemuan 02 - Kelas dan Objek

- Method boleh menerima parameter tambahan (selain self).
- Method boleh MENGEMBALIKAN nilai dengan return, sehingga hasilnya bisa
  disimpan ke variabel, dihitung lagi, atau dicetak.

Cara menjalankan (dari folder python/contoh; macOS/Linux: python3):
    python contoh04_parameter_dan_return.py
"""


class PersegiPanjang:
    """Bangun datar persegi panjang dengan panjang dan lebar (cm)."""

    def __init__(self, panjang, lebar):
        self.panjang = panjang
        self.lebar = lebar

    def hitung_luas(self):  # [1] mengembalikan nilai
        return self.panjang * self.lebar

    def hitung_keliling(self):
        return 2 * (self.panjang + self.lebar)

    def perbesar(self, faktor):  # [2] menerima parameter dan mengubah atribut
        self.panjang = self.panjang * faktor
        self.lebar = self.lebar * faktor


def main():
    meja = PersegiPanjang(120, 60)
    luas = meja.hitung_luas()  # [3] hasil return disimpan ke variabel
    print("=== MEJA BELAJAR ===")
    print(f"Ukuran   : {meja.panjang} x {meja.lebar} cm")
    print(f"Luas     : {luas} cm2")
    print(f"Keliling : {meja.hitung_keliling()} cm")  # [4] langsung dipakai

    print()
    meja.perbesar(2)  # [5] mengirim argumen ke parameter faktor
    print("=== SETELAH DIPERBESAR 2 KALI ===")
    print(f"Ukuran   : {meja.panjang} x {meja.lebar} cm")
    print(f"Luas     : {meja.hitung_luas()} cm2")
    print(f"Luas naik {meja.hitung_luas() // luas} kali lipat")


if __name__ == "__main__":
    main()
