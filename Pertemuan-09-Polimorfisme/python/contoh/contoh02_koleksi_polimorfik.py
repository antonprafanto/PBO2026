"""
Contoh 02 - Koleksi Polimorfik: Menambah Jenis Baru Tanpa Mengubah Pemanggil
Pertemuan 09 - Polimorfisme

Satu list berisi bermacam bangun datar. Fungsi cetak_laporan() memanggil
nama() dan luas() pada setiap objek TANPA menyebut satu pun kelas anak.
Akibatnya, jenis baru (Trapesium) bisa ditambahkan belakangan tanpa
mengubah fungsi itu sedikit pun.

Semua ukuran dalam cm dan berupa bilangan bulat.

Cara menjalankan:
    python contoh02_koleksi_polimorfik.py
"""


class BangunDatar:
    """Kelas induk semua bangun datar."""

    def nama(self) -> str:
        return "Bangun datar"

    def luas(self) -> int:
        return 0  # [1] bangun datar "umum" tidak punya rumus luas


class Persegi(BangunDatar):
    def __init__(self, sisi: int):
        self._sisi = sisi

    def nama(self) -> str:
        return f"Persegi {self._sisi}x{self._sisi}"

    def luas(self) -> int:
        return self._sisi * self._sisi


class PersegiPanjang(BangunDatar):
    def __init__(self, panjang: int, lebar: int):
        self._panjang = panjang
        self._lebar = lebar

    def nama(self) -> str:
        return f"Persegi panjang {self._panjang}x{self._lebar}"

    def luas(self) -> int:
        return self._panjang * self._lebar


class Segitiga(BangunDatar):
    def __init__(self, alas: int, tinggi: int):
        self._alas = alas
        self._tinggi = tinggi

    def nama(self) -> str:
        return f"Segitiga alas {self._alas} tinggi {self._tinggi}"

    def luas(self) -> int:
        return self._alas * self._tinggi // 2


# ----- Jenis BARU yang ditambahkan belakangan -----
class Trapesium(BangunDatar):  # [2] cukup menulis kelas baru
    def __init__(self, sisi_atas: int, sisi_bawah: int, tinggi: int):
        self._sisi_atas = sisi_atas
        self._sisi_bawah = sisi_bawah
        self._tinggi = tinggi

    def nama(self) -> str:
        return f"Trapesium {self._sisi_atas}/{self._sisi_bawah} tinggi {self._tinggi}"

    def luas(self) -> int:
        return (self._sisi_atas + self._sisi_bawah) * self._tinggi // 2


def cetak_laporan(daftar: list[BangunDatar]):  # [3] tidak kenal kelas anak mana pun
    total = 0
    for bangun in daftar:
        luas = bangun.luas()  # [4] versi luas() milik objek yang sebenarnya
        print(f"{bangun.nama():<30} luas {luas:>4} cm2")
        total += luas
    print(f"Total luas: {total} cm2")


def main():
    print("=== LAPORAN AWAL: TIGA JENIS ===")
    daftar = [Persegi(10), PersegiPanjang(12, 5), Segitiga(8, 6)]  # [5]
    cetak_laporan(daftar)

    print()
    print("=== SETELAH ADA JENIS BARU ===")
    daftar.append(Trapesium(6, 10, 4))  # [6] cetak_laporan() tidak diubah
    daftar.append(BangunDatar())
    cetak_laporan(daftar)


if __name__ == "__main__":
    main()
