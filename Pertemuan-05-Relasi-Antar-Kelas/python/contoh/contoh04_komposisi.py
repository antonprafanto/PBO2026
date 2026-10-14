"""
Contoh 04 - Komposisi: Bagian yang Dibuat dan Dimiliki Penuh
Pertemuan 05 - Relasi Antar Kelas

Rumah MEMBUAT sendiri objek-objek Ruangan miliknya. Kode di luar kelas
hanya mengirim DATA (nama, panjang, lebar), tidak pernah membuat Ruangan.
Karena hanya rumah yang memegang ruangannya, ruangan ikut hilang bersama
rumahnya.

Cara menjalankan:
    python contoh04_komposisi.py
"""


class Ruangan:
    """Satu ruangan di dalam rumah. Ukuran dalam meter."""

    def __init__(self, nama: str, panjang: int, lebar: int):
        self._nama = nama
        self._panjang = panjang
        self._lebar = lebar

    def luas(self) -> int:
        return self._panjang * self._lebar

    def __str__(self) -> str:
        return f"{self._nama} {self._panjang}x{self._lebar} m = {self.luas()} m2"


class Rumah:
    """Rumah yang membuat dan memiliki ruangan-ruangannya sendiri."""

    def __init__(self, pemilik: str):
        self._pemilik = pemilik
        self._daftar_ruangan: list[Ruangan] = []

    def bangun_ruangan(self, nama: str, panjang: int, lebar: int):  # [1]
        ruangan = Ruangan(nama, panjang, lebar)  # [2] dibuat DI DALAM rumah
        self._daftar_ruangan.append(ruangan)

    def luas_total(self) -> int:
        total = 0
        for ruangan in self._daftar_ruangan:
            total += ruangan.luas()  # [3] rumah bertanya ke setiap ruangan
        return total

    def tampilkan(self):
        print(f"Rumah {self._pemilik}:")
        for ruangan in self._daftar_ruangan:
            print(f"- {ruangan}")
        print(f"Luas total: {self.luas_total()} m2")


def main():
    print("=== MEMBANGUN RUMAH ===")
    rumah = Rumah("Pak Hasan")
    rumah.bangun_ruangan("Ruang tamu", 4, 3)  # [4] hanya mengirim data
    rumah.bangun_ruangan("Kamar tidur", 3, 3)
    rumah.bangun_ruangan("Dapur", 3, 2)
    rumah.tampilkan()

    print()
    print("=== RUMAH DIROBOHKAN ===")
    rumah = None  # [5] satu-satunya pemegang ruangan dilepas
    print("Rumah dirobohkan. Tidak ada variabel lain yang memegang ruangannya,")
    print("jadi ruangan-ruangan itu ikut hilang bersama rumahnya.")


if __name__ == "__main__":
    main()
