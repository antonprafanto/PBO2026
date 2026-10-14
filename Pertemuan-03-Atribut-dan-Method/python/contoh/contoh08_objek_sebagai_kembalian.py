"""
Contoh 08 - Objek sebagai Nilai Kembalian
Pertemuan 03 - Atribut dan Method Lebih Dalam

Method boleh mengembalikan OBJEK BARU. Durasi.tambah(lain) tidak mengubah
durasi yang lama; ia membuat lalu mengembalikan objek Durasi baru. Mirip
2 + 3 yang menghasilkan 5 tanpa mengubah angka 2 maupun 3.

Cara menjalankan:
    python contoh08_objek_sebagai_kembalian.py
"""


class Durasi:
    """Lama waktu dalam jam dan menit (bilangan bulat)."""

    def __init__(self, jam, menit):
        total = jam * 60 + menit  # [1] dirapikan: 1 jam 75 menit -> 2 jam 15 menit
        self.jam = total // 60
        self.menit = total % 60

    def total_menit(self):
        return self.jam * 60 + self.menit

    def tambah(self, lain):  # [2] menerima objek Durasi lain ...
        return Durasi(0, self.total_menit() + lain.total_menit())  # [3] ... objek BARU

    def lebih_lama_dari(self, lain):  # [4] method boolean dengan parameter objek
        return self.total_menit() > lain.total_menit()

    def __str__(self):
        return f"{self.jam} jam {self.menit} menit"


def main():
    kuliah = Durasi(2, 30)
    praktikum = Durasi(1, 40)

    print("=== MENJUMLAHKAN DUA DURASI ===")
    total = kuliah.tambah(praktikum)  # [5] hasilnya objek baru
    print(f"Kuliah    : {kuliah}")
    print(f"Praktikum : {praktikum}")
    print(f"Total     : {total}")
    print(f"Durasi aneh 1 jam 75 menit dirapikan menjadi {Durasi(1, 75)}")

    print()
    print("=== MEMANGGIL SECARA BERANTAI ===")
    istirahat = Durasi(0, 45)
    sehari = kuliah.tambah(istirahat).tambah(praktikum)  # [6] hasil dipakai lagi
    print(f"Kuliah + istirahat + praktikum = {sehari}")
    print(f"Kuliah tetap {kuliah}")  # [7] objek lama tidak berubah

    print()
    print("=== MEMBANDINGKAN DUA DURASI ===")
    batas = Durasi(4, 30)
    if total.lebih_lama_dari(batas):
        print(f"{total} lebih lama dari {batas}")
    else:
        print(f"{total} tidak lebih lama dari {batas}")


if __name__ == "__main__":
    main()
