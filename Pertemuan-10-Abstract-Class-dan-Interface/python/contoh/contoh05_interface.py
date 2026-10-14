"""
Contoh 05 - "Interface" di Python: Kontrak Kemampuan
Pertemuan 10 - Abstract Class dan Interface

Python tidak punya kata kunci interface seperti Java. Cara yang lazim:
membuat kelas abstrak (turunan ABC) yang SEMUA method-nya abstrak.
Kelas seperti ini tidak menyimpan data. Isinya hanya daftar kemampuan
yang dijanjikan.

Lampu, KomporGas, dan Televisi tidak bersaudara: ketiganya tidak punya
kelas induk bersama selain kontrak BisaDinyalakan. Fungsi matikan_semua()
cukup mengenal kontraknya, tidak perlu tahu jenis asli objeknya.

Cara menjalankan:
    python contoh05_interface.py
"""

from abc import ABC, abstractmethod


class BisaDinyalakan(ABC):  # [1] "interface": semua method-nya abstrak
    """Kontrak: benda ini bisa dinyalakan dan dimatikan."""

    @abstractmethod
    def nyalakan(self):
        """Menyalakan benda."""

    @abstractmethod
    def matikan(self):
        """Mematikan benda."""

    @abstractmethod
    def sedang_menyala(self) -> bool:
        """True jika benda sedang menyala."""


class Lampu(BisaDinyalakan):  # [2] memenuhi kontrak dengan mewarisinya
    """Lampu di sebuah ruangan."""

    def __init__(self, ruangan: str):
        self._ruangan = ruangan
        self._menyala = False

    def nyalakan(self):
        self._menyala = True
        print(f"Lampu {self._ruangan} menyala")

    def matikan(self):
        self._menyala = False
        print(f"Lampu {self._ruangan} padam")

    def sedang_menyala(self) -> bool:
        return self._menyala


class KomporGas(BisaDinyalakan):
    """Kompor gas: bukan alat listrik, tetapi juga bisa dinyalakan."""

    def __init__(self):
        self._api_menyala = False

    def nyalakan(self):
        self._api_menyala = True
        print("Kompor gas: klik... api biru menyala")

    def matikan(self):
        self._api_menyala = False
        print("Kompor gas: api dimatikan, katup gas ditutup")

    def sedang_menyala(self) -> bool:
        return self._api_menyala


class Televisi(BisaDinyalakan):
    """Televisi dengan nomor saluran."""

    def __init__(self, saluran: int):
        self._saluran = saluran
        self._menyala = False

    def nyalakan(self):
        self._menyala = True
        print(f"TV menyala di saluran {self._saluran}")

    def matikan(self):
        self._menyala = False
        print("TV dimatikan")

    def sedang_menyala(self) -> bool:
        return self._menyala


def matikan_semua(daftar: list[BisaDinyalakan]):  # [3] parameter bertipe kontrak
    """Mematikan semua benda yang masih menyala, apa pun jenisnya."""
    print(f"Memeriksa {len(daftar)} benda...")
    for benda in daftar:
        if benda.sedang_menyala():  # [4] yang dipakai hanya method dari kontrak
            benda.matikan()
    print("Semua sudah padam. Aman!")


def main():
    lampu = Lampu("teras")
    kompor = KomporGas()
    tv = Televisi(5)

    print("=== PAGI HARI ===")
    lampu.nyalakan()
    kompor.nyalakan()
    tv.nyalakan()
    tv.matikan()

    print()
    print("=== SEBELUM BERANGKAT KULIAH ===")
    matikan_semua([lampu, kompor, tv])


if __name__ == "__main__":
    main()
