"""
Contoh 03 - Static Method dan Class Method
Pertemuan 03 - Atribut dan Method Lebih Dalam

Tiga jenis method di dalam kelas Python:
- method objek  : parameter pertama self; bekerja dengan data milik objek.
- @staticmethod : tanpa self dan tanpa cls; fungsi bantu yang "dititipkan"
                  di kelas karena isinya masih berhubungan dengan kelas itu.
- @classmethod  : parameter pertama cls (kelasnya sendiri); sering dipakai
                  sebagai konstruktor alternatif, misalnya dari_teks().

Cara menjalankan:
    python contoh03_static_dan_class_method.py
"""


class Tanggal:
    """Tanggal sederhana: hari, bulan, dan tahun (semuanya bilangan bulat)."""

    NAMA_BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli",
                  "Agustus", "September", "Oktober", "November", "Desember"]

    def __init__(self, hari, bulan, tahun):
        self.hari = hari
        self.bulan = bulan
        self.tahun = tahun

    def teks(self):  # [1] method objek: butuh data milik objek (self)
        return f"{self.hari} {Tanggal.NAMA_BULAN[self.bulan - 1]} {self.tahun}"

    @staticmethod
    def kabisat(tahun):  # [2] static method: tanpa self, cukup data dari parameter
        """True jika tahun kabisat (bulan Februari punya 29 hari)."""
        return (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0

    @classmethod
    def dari_teks(cls, teks):  # [3] class method: cls berisi kelas Tanggal
        """Konstruktor alternatif: membuat Tanggal dari teks 'hari-bulan-tahun'."""
        hari, bulan, tahun = teks.split("-")
        return cls(int(hari), int(bulan), int(tahun))  # [4] sama dengan Tanggal(...)


def main():
    print("=== METHOD OBJEK (butuh objek) ===")
    proklamasi = Tanggal(17, 8, 1945)
    print(f"Proklamasi kemerdekaan: {proklamasi.teks()}")

    print()
    print("=== STATIC METHOD (tanpa objek) ===")
    for tahun in [2024, 2026, 1900, 2000]:
        if Tanggal.kabisat(tahun):  # [5] dipanggil lewat nama kelas
            print(f"{tahun}: tahun kabisat")
        else:
            print(f"{tahun}: bukan tahun kabisat")

    print()
    print("=== KONSTRUKTOR ALTERNATIF (dari teks) ===")
    sumpah_pemuda = Tanggal.dari_teks("28-10-1928")  # [6] objek dibuat dari teks
    print(f"Sumpah Pemuda: {sumpah_pemuda.teks()}")
    pertempuran = Tanggal.dari_teks("10-11-1945")
    print(f"Pertempuran Surabaya: {pertempuran.teks()}")


if __name__ == "__main__":
    main()
