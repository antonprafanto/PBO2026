"""
Contoh 03 - Method: Perilaku Sebuah Objek
Pertemuan 02 - Kelas dan Objek

Method adalah fungsi yang "menempel" pada objek. Method bisa membaca dan
mengubah atribut milik objeknya sendiri lewat self.

Cara menjalankan (dari folder python/contoh; macOS/Linux: python3):
    python contoh03_method.py
"""


class Lampu:
    """Lampu yang bisa dinyalakan dan dimatikan."""

    def __init__(self, ruangan):
        self.ruangan = ruangan
        self.menyala = False  # [1] nilai awal tidak harus dari parameter

    def nyalakan(self):  # [2] method yang mengubah atribut
        self.menyala = True
        print(f"Lampu {self.ruangan} dinyalakan")

    def matikan(self):
        self.menyala = False
        print(f"Lampu {self.ruangan} dimatikan")

    def tampilkan_status(self):  # [3] method yang hanya membaca atribut
        if self.menyala:
            print(f"Status lampu {self.ruangan}: MENYALA")
        else:
            print(f"Status lampu {self.ruangan}: PADAM")


def main():
    lampu_kamar = Lampu("kamar")
    lampu_dapur = Lampu("dapur")

    print("=== KONDISI AWAL ===")
    lampu_kamar.tampilkan_status()  # [4] memanggil method
    lampu_dapur.tampilkan_status()

    print()
    print("=== SETELAH DIOPERASIKAN ===")
    lampu_kamar.nyalakan()
    lampu_kamar.tampilkan_status()
    lampu_dapur.tampilkan_status()  # lampu dapur tidak terpengaruh
    lampu_kamar.matikan()
    lampu_kamar.tampilkan_status()


if __name__ == "__main__":
    main()
