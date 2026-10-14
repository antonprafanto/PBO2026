"""
Solusi Latihan 01 - Nomor Antrean Otomatis
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- jumlah_pasien adalah atribut KELAS: satu penghitung untuk semua pasien.
- Setiap kali objek Pasien dibuat, penghitung dinaikkan LEWAT NAMA KELAS
  (Pasien.jumlah_pasien += 1), lalu nilainya disalin menjadi atribut OBJEK
  nomor. Dengan begitu, setiap pasien menyimpan nomornya sendiri.
- kode_antrean() menyusun teks "A001". Format {nomor:03d} menambahkan angka 0
  di depan sampai panjangnya 3 digit.

Cara menjalankan:
    python latihan01_antrean_pasien.py
"""


class Pasien:
    """Pasien yang mendaftar di loket puskesmas."""

    jumlah_pasien = 0  # atribut kelas: penghitung bersama

    def __init__(self, nama, keluhan):
        Pasien.jumlah_pasien += 1  # lewat nama kelas, BUKAN self.jumlah_pasien
        self.nomor = Pasien.jumlah_pasien  # atribut objek: nomor milik pasien ini
        self.nama = nama
        self.keluhan = keluhan

    def kode_antrean(self):
        return f"A{self.nomor:03d}"

    def __str__(self):
        return f"{self.kode_antrean()} - {self.nama} ({self.keluhan})"


def main():
    print("=== ANTREAN PUSKESMAS ===")
    print(f"Jumlah pasien awal: {Pasien.jumlah_pasien}")
    pasien1 = Pasien("Andi Wijaya", "demam")
    pasien2 = Pasien("Nurul Hidayah", "batuk")
    pasien3 = Pasien("Yusuf Hamdani", "sakit gigi")
    print(pasien1)
    print(pasien2)
    print(pasien3)
    print(f"Jumlah pasien: {Pasien.jumlah_pasien}")

    print()
    print("=== PASIEN BARU DATANG ===")
    pasien4 = Pasien("Maya Sari", "pusing")
    print(pasien4)
    print(f"Jumlah pasien: {Pasien.jumlah_pasien}")
    print(f"Nomor pasien pertama tetap {pasien1.kode_antrean()}")


if __name__ == "__main__":
    main()
