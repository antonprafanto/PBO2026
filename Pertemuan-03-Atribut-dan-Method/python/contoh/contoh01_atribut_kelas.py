"""
Contoh 01 - Atribut Objek dan Atribut Kelas
Pertemuan 03 - Atribut dan Method Lebih Dalam

- Atribut OBJEK (nim, nama) dimiliki oleh setiap objek. Nilainya bisa
  berbeda-beda dan diisi di __init__ lewat self.
- Atribut KELAS (kampus, jumlah) dimiliki oleh kelas. Hanya ada SATU nilai
  yang dipakai bersama oleh semua objek. Atribut kelas ditulis langsung di
  badan kelas, di luar method.

Cara menjalankan:
    python contoh01_atribut_kelas.py
"""


class Mahasiswa:
    """Mahasiswa Informatika di Samarinda."""

    kampus = "Unmul"  # [1] atribut kelas: sama untuk semua mahasiswa
    jumlah = 0  # [2] atribut kelas: penghitung objek yang sudah dibuat

    def __init__(self, nim, nama):
        self.nim = nim  # [3] atribut objek: milik masing-masing mahasiswa
        self.nama = nama
        Mahasiswa.jumlah += 1  # [4] mengubah atribut kelas lewat NAMA KELAS

    def perkenalan(self):
        print(f"Saya {self.nama} ({self.nim}) dari {Mahasiswa.kampus}")  # [5]


def main():
    print("=== SEBELUM ADA OBJEK ===")
    print(f"Kampus          : {Mahasiswa.kampus}")  # [6] dibaca tanpa objek
    print(f"Jumlah mahasiswa: {Mahasiswa.jumlah}")

    ayu = Mahasiswa("2409106001", "Ayu Lestari")
    bima = Mahasiswa("2409106002", "Bima Saputra")
    citra = Mahasiswa("2409106003", "Citra Dewi")

    print()
    print("=== SETELAH TIGA OBJEK DIBUAT ===")
    ayu.perkenalan()
    bima.perkenalan()
    citra.perkenalan()
    print(f"Jumlah mahasiswa: {Mahasiswa.jumlah}")

    print()
    print("=== NAMA KAMPUS DITULIS LENGKAP ===")
    Mahasiswa.kampus = "Universitas Mulawarman"  # [7] berlaku untuk SEMUA objek
    ayu.perkenalan()
    bima.perkenalan()
    citra.perkenalan()


if __name__ == "__main__":
    main()
