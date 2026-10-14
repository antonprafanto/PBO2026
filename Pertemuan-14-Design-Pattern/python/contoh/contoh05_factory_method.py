"""
Contoh 05 - Factory Method (versi GoF): Subclass yang Memilih Produknya
Pertemuan 14 - Design Pattern Dasar

Bedanya dengan Simple Factory (contoh 04):
- Simple Factory : SATU method (biasanya static) berisi if/elif yang memilih
                   kelas mana yang dibuat.
- Factory Method : kelas induk punya method abstrak buat_angkutan(). Setiap
                   SUBCLASS meng-override-nya untuk membuat produk yang
                   berbeda. Kelas induk memakai produk itu tanpa tahu kelas
                   konkretnya. Tidak ada if/elif sama sekali.

Cara menjalankan:
    python contoh05_factory_method.py
"""

from abc import ABC, abstractmethod


class Angkutan(ABC):
    """Produk: sesuatu yang bisa mengantar paket."""

    @abstractmethod
    def antar(self, tujuan: str) -> str:
        """Keterangan perjalanan menuju tujuan."""


class Truk(Angkutan):
    def antar(self, tujuan: str) -> str:
        return f"Truk melaju lewat jalan darat menuju {tujuan}"


class KapalSungai(Angkutan):
    def antar(self, tujuan: str) -> str:
        return f"Kapal menyusuri Sungai Mahakam menuju {tujuan}"


class Ekspedisi(ABC):
    """Langkah kerja tetap, tetapi produk angkutannya diserahkan ke subclass."""

    @abstractmethod
    def nama(self) -> str:
        """Nama layanan ekspedisi."""

    @abstractmethod
    def buat_angkutan(self) -> Angkutan:  # [1] inilah FACTORY METHOD
        """Subclass memutuskan angkutan apa yang dibuat."""

    def kirim_paket(self, tujuan: str):  # [2] memakai produk tanpa tahu kelasnya
        print(f"[{self.nama()}] Paket ke {tujuan} dikemas")
        angkutan = self.buat_angkutan()
        print(f"  {angkutan.antar(tujuan)}")
        print(f"  Paket tiba di {tujuan}")


class EkspedisiDarat(Ekspedisi):
    def nama(self) -> str:
        return "Ekspedisi Darat"

    def buat_angkutan(self) -> Angkutan:  # [3] subclass memilih produknya
        return Truk()


class EkspedisiSungai(Ekspedisi):
    def nama(self) -> str:
        return "Ekspedisi Sungai"

    def buat_angkutan(self) -> Angkutan:
        return KapalSungai()


def main():
    print("=== FACTORY METHOD: SUBCLASS MEMILIH ANGKUTANNYA ===")
    darat: Ekspedisi = EkspedisiDarat()
    sungai: Ekspedisi = EkspedisiSungai()
    darat.kirim_paket("Balikpapan")  # [4] method sama, angkutan berbeda
    sungai.kirim_paket("Tenggarong")


if __name__ == "__main__":
    main()
