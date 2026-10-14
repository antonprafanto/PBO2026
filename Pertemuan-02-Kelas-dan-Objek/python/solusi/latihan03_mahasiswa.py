"""
Solusi Latihan 03 - Kelas Mahasiswa dan Predikat IPK
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
- predikat() memeriksa IPK dari yang tertinggi dulu (if-elif-else),
  lalu MENGEMBALIKAN teks predikat.
- Aturan predikat mengikuti soal:
    IPK >= 3.51 -> Dengan Pujian
    IPK >= 3.01 -> Sangat Memuaskan
    IPK >= 2.76 -> Memuaskan
    lainnya     -> Cukup

Cara menjalankan:
    python latihan03_mahasiswa.py
"""


class Mahasiswa:
    """Data mahasiswa beserta IPK-nya."""

    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk

    def predikat(self):
        if self.ipk >= 3.51:
            return "Dengan Pujian"
        elif self.ipk >= 3.01:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.76:
            return "Memuaskan"
        else:
            return "Cukup"

    def tampilkan(self):
        print(f"{self.nim} {self.nama} - IPK {self.ipk} - {self.predikat()}")


def main():
    daftar = [
        Mahasiswa("2409106001", "Ayu Lestari", 3.75),
        Mahasiswa("2409106002", "Bima Saputra", 3.2),
        Mahasiswa("2409106003", "Citra Dewi", 2.9),
        Mahasiswa("2409106004", "Dimas Pratama", 2.5),
    ]
    print("=== DAFTAR PREDIKAT ===")
    for mhs in daftar:
        mhs.tampilkan()


if __name__ == "__main__":
    main()
