"""
Solusi Latihan 04 - Ojek Online: Satu Kelas, Banyak Interface
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- Armada adalah kelas abstrak: semua armada punya pengemudi dan jenis.
  Ini hubungan "adalah" (is-a), jadi cocok memakai kelas abstrak.
- BisaAntarPenumpang dan BisaAntarMakanan adalah "interface" (kemampuan,
  hubungan "bisa"). Satu kelas boleh memenuhi lebih dari satu kontrak.
- isinstance() dipakai untuk memeriksa KEMAMPUAN, bukan jenis kelasnya,
  sehingga tidak ada if berdasarkan nama kelas.

Cara menjalankan:
    python latihan04_ojek_online.py
"""

from abc import ABC, abstractmethod


class Armada(ABC):
    """Kelas abstrak: semua armada punya pengemudi."""

    def __init__(self, pengemudi: str):
        self._pengemudi = pengemudi

    @abstractmethod
    def jenis(self) -> str:
        """Jenis armada, misalnya 'Ojek motor'."""

    def __str__(self) -> str:
        return f"{self.jenis()} {self._pengemudi}"


class BisaAntarPenumpang(ABC):
    """Kontrak: bisa mengantar penumpang."""

    @abstractmethod
    def antar_penumpang(self, tujuan: str) -> str:
        """Mengembalikan keterangan perjalanan."""


class BisaAntarMakanan(ABC):
    """Kontrak: bisa mengantar pesanan makanan."""

    @abstractmethod
    def antar_makanan(self, warung: str) -> str:
        """Mengembalikan keterangan pengambilan pesanan."""


class OjekMotor(Armada, BisaAntarPenumpang, BisaAntarMakanan):
    """Ojek motor: bisa mengantar penumpang DAN makanan."""

    def jenis(self) -> str:
        return "Ojek motor"

    def antar_penumpang(self, tujuan: str) -> str:
        return f"{self} membonceng penumpang ke {tujuan}"

    def antar_makanan(self, warung: str) -> str:
        return f"{self} mengambil pesanan di {warung}"


class TaksiMobil(Armada, BisaAntarPenumpang):
    """Taksi mobil: hanya mengantar penumpang."""

    def jenis(self) -> str:
        return "Taksi mobil"

    def antar_penumpang(self, tujuan: str) -> str:
        return f"{self} mengantar penumpang ke {tujuan}"


class KurirSepeda(Armada, BisaAntarMakanan):
    """Kurir sepeda: hanya mengantar makanan."""

    def jenis(self) -> str:
        return "Kurir sepeda"

    def antar_makanan(self, warung: str) -> str:
        return f"{self} mengayuh sepeda ke {warung}"


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    armada: list[Armada] = [
        OjekMotor("Pak Rudi"),
        TaksiMobil("Pak Joko"),
        KurirSepeda("Mas Dimas"),
    ]

    print("=== KEMAMPUAN ARMADA ===")
    for kendaraan in armada:
        penumpang = ya_tidak(isinstance(kendaraan, BisaAntarPenumpang))
        makanan = ya_tidak(isinstance(kendaraan, BisaAntarMakanan))
        print(f"{kendaraan}: penumpang {penumpang}, makanan {makanan}")

    print()
    print("=== PESANAN MAKANAN DARI WARUNG SOTO BANJAR ===")
    for kendaraan in armada:
        if isinstance(kendaraan, BisaAntarMakanan):
            print(kendaraan.antar_makanan("Warung Soto Banjar"))

    print()
    print("=== PENUMPANG KE KAMPUS UNMUL ===")
    for kendaraan in armada:
        if isinstance(kendaraan, BisaAntarPenumpang):
            print(kendaraan.antar_penumpang("Kampus Unmul"))


if __name__ == "__main__":
    main()
