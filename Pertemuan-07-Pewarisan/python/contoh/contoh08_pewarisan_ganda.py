"""
Contoh 08 - Pewarisan Ganda (Multiple Inheritance) dan MRO  [KHUSUS PYTHON]
Pertemuan 07 - Pewarisan (Inheritance)

Python mengizinkan satu kelas punya LEBIH DARI SATU induk.
Jika dua induk punya method bernama sama, Python mencari method itu
mengikuti urutan tertentu yang disebut MRO (Method Resolution Order).
Java tidak mendukung ini; padanannya dibahas di halaman Jembatan.

Cara menjalankan:
    python contoh08_pewarisan_ganda.py
"""


class KendaraanDarat:
    """Kendaraan yang berjalan di jalan raya."""

    def jalan_di_darat(self) -> str:
        return "melaju di jalan raya"

    def info(self) -> str:
        return "Saya kendaraan darat"


class KendaraanAir:
    """Kendaraan yang berlayar di air."""

    def berlayar(self) -> str:
        return "berlayar di sungai"

    def info(self) -> str:
        return "Saya kendaraan air"


class MobilAmfibi(KendaraanDarat, KendaraanAir):  # [1] dua induk sekaligus
    """Mobil amfibi adalah kendaraan darat SEKALIGUS kendaraan air."""

    def __init__(self, nama: str):
        self._nama = nama

    def demo(self) -> str:
        return f"{self._nama} {self.jalan_di_darat()}, lalu {self.berlayar()}"


class PerahuBeroda(KendaraanAir, KendaraanDarat):  # [2] urutan induk dibalik
    """Sama-sama punya dua induk, tetapi KendaraanAir ditulis lebih dulu."""


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def urutan_mro(kelas: type) -> str:
    """Mengubah daftar MRO sebuah kelas menjadi teks 'A -> B -> C'."""
    return " -> ".join(k.__name__ for k in kelas.__mro__)  # [3]


def main():
    amfibi = MobilAmfibi("Amfibi Mahakam")

    print("=== SATU OBJEK, DUA INDUK ===")
    print(amfibi.demo())
    print(f"Termasuk KendaraanDarat? {ya_tidak(isinstance(amfibi, KendaraanDarat))}")
    print(f"Termasuk KendaraanAir?   {ya_tidak(isinstance(amfibi, KendaraanAir))}")

    print()
    print("=== METHOD BERNAMA SAMA: info() ===")
    print(f"MobilAmfibi  : {amfibi.info()}")  # [4] milik induk yang ditulis pertama
    print(f"PerahuBeroda : {PerahuBeroda().info()}")

    print()
    print("=== URUTAN PENCARIAN METHOD (MRO) ===")
    print(f"MobilAmfibi  : {urutan_mro(MobilAmfibi)}")
    print(f"PerahuBeroda : {urutan_mro(PerahuBeroda)}")


if __name__ == "__main__":
    main()
