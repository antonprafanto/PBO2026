"""
Solusi Latihan 02 - Kelas Utilitas Konversi Satuan
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- Semua method diberi @staticmethod karena tidak membutuhkan data objek.
  Kita cukup memanggilnya lewat nama kelas: KonversiSatuan.km_ke_meter(5).
- Semua perhitungan memakai bilangan bulat:
  * detik -> jam, menit, detik memakai // (bagi bulat) dan % (sisa bagi).
  * Celsius -> Fahrenheit: celsius * 9 // 5 + 32 (kalikan dulu, baru bagi).
- Catatan: di Python, fungsi-fungsi ini juga boleh ditulis sebagai fungsi
  biasa di luar kelas. Kelas utilitas dipakai di sini untuk latihan
  @staticmethod dan agar setara dengan versi Java.

Cara menjalankan:
    python latihan02_konversi_satuan.py
"""


class KonversiSatuan:
    """Kumpulan fungsi konversi satuan. Tidak perlu dibuat objeknya."""

    @staticmethod
    def km_ke_meter(km):
        return km * 1000

    @staticmethod
    def detik_ke_teks(detik):
        jam = detik // 3600
        menit = detik % 3600 // 60
        sisa_detik = detik % 60
        return f"{jam} jam {menit} menit {sisa_detik} detik"

    @staticmethod
    def celsius_ke_fahrenheit(celsius):
        return celsius * 9 // 5 + 32


def main():
    print("=== KONVERSI SATUAN (tanpa membuat objek) ===")
    for km in [5, 12]:
        print(f"{km} km = {KonversiSatuan.km_ke_meter(km)} meter")
    for detik in [3725, 1985]:
        print(f"{detik} detik = {KonversiSatuan.detik_ke_teks(detik)}")
    for celsius in [0, 25, 30, 100]:
        print(f"{celsius} C = {KonversiSatuan.celsius_ke_fahrenheit(celsius)} F")


if __name__ == "__main__":
    main()
