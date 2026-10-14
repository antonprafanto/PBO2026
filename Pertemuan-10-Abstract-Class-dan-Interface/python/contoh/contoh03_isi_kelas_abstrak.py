"""
Contoh 03 - Kelas Abstrak Boleh Punya Konstruktor, Atribut, dan Method Biasa
Pertemuan 10 - Abstract Class dan Interface

Kelas abstrak bukan kelas "kosong". Kendaraan di bawah ini punya:
- konstruktor dan atribut (plat, bensin) yang dipakai bersama anak-anaknya,
- method biasa (konkret) isi_bensin(), jarak_tempuh(), dan info(),
- method abstrak km_per_liter() yang WAJIB diisi setiap kelas anak.

Konstruktor kelas abstrak tetap berjalan, yaitu saat objek kelas anak dibuat.

Cara menjalankan:
    python contoh03_isi_kelas_abstrak.py
"""

from abc import ABC, abstractmethod


class Kendaraan(ABC):
    """Kelas abstrak: data dan perilaku bersama semua kendaraan."""

    def __init__(self, plat: str, bensin_liter: int):  # [1] konstruktor
        print(f"  (konstruktor Kendaraan dijalankan untuk {plat})")
        self._plat = plat  # [2] atribut bersama
        self._bensin = bensin_liter

    @property
    def plat(self) -> str:
        return self._plat

    def isi_bensin(self, liter: int):  # [3] method konkret: langsung diwarisi
        self._bensin += liter
        print(f"{self._plat} mengisi bensin {liter} liter")

    def jarak_tempuh(self) -> int:  # [4] method konkret yang memakai method abstrak
        return self._bensin * self.km_per_liter()

    def info(self) -> str:
        return (f"{type(self).__name__} {self._plat}: bensin {self._bensin} liter, "
                f"bisa menempuh {self.jarak_tempuh()} km")

    @abstractmethod
    def km_per_liter(self) -> int:  # [5] berbeda untuk setiap jenis kendaraan
        """Jarak (km) yang bisa ditempuh dengan 1 liter bensin."""


class Motor(Kendaraan):
    """Motor: tidak menulis __init__, jadi memakai konstruktor Kendaraan."""

    def km_per_liter(self) -> int:
        return 40


class Mobil(Kendaraan):
    """Mobil: punya atribut tambahan jumlah kursi."""

    def __init__(self, plat: str, bensin_liter: int, jumlah_kursi: int):
        super().__init__(plat, bensin_liter)  # [6] konstruktor kelas abstrak
        self._jumlah_kursi = jumlah_kursi

    def km_per_liter(self) -> int:
        return 12

    def info(self) -> str:  # method konkret milik induk juga boleh di-override
        return f"{super().info()}, {self._jumlah_kursi} kursi"


def main():
    print("=== MEMBUAT KENDARAAN ===")
    motor = Motor("KT 1234 AB", 3)
    mobil = Mobil("KT 5678 CD", 20, 7)

    print()
    print("=== INFO AWAL ===")
    print(motor.info())
    print(mobil.info())

    print()
    print("=== ISI BENSIN (method konkret milik Kendaraan) ===")
    motor.isi_bensin(2)
    mobil.isi_bensin(10)
    print(motor.info())
    print(mobil.info())


if __name__ == "__main__":
    main()
