"""
Solusi Latihan 02 - Interface BisaDiisiUlang
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- BisaDiisiUlang adalah "interface": ABC yang semua method-nya abstrak.
- Tiga alat yang tidak bersaudara memenuhi kontrak itu dengan caranya
  sendiri (kecepatan isi daya berbeda), tetapi baterai tidak boleh > 100%.
- tampilkan_status() dan isi_semua() hanya mengenal kontraknya.

Cara menjalankan:
    python latihan02_bisa_diisi_ulang.py
"""

from abc import ABC, abstractmethod


class BisaDiisiUlang(ABC):
    """Kontrak: alat yang baterainya bisa diisi ulang."""

    @abstractmethod
    def nama_alat(self) -> str:
        """Nama alat untuk ditampilkan."""

    @abstractmethod
    def persen_baterai(self) -> int:
        """Isi baterai saat ini (0 sampai 100)."""

    @abstractmethod
    def isi_daya(self, menit: int):
        """Mengisi baterai selama sekian menit."""


class SepedaListrik(BisaDiisiUlang):
    """Baterai besar: naik 1% per menit."""

    def __init__(self, baterai: int):
        self._baterai = baterai

    def nama_alat(self) -> str:
        return "Sepeda listrik"

    def persen_baterai(self) -> int:
        return self._baterai

    def isi_daya(self, menit: int):
        self._baterai = min(100, self._baterai + menit * 1)


class Powerbank(BisaDiisiUlang):
    """Naik 2% per menit."""

    def __init__(self, baterai: int):
        self._baterai = baterai

    def nama_alat(self) -> str:
        return "Powerbank"

    def persen_baterai(self) -> int:
        return self._baterai

    def isi_daya(self, menit: int):
        self._baterai = min(100, self._baterai + menit * 2)


class SikatGigiElektrik(BisaDiisiUlang):
    """Baterai kecil: naik 5% per menit."""

    def __init__(self, baterai: int):
        self._baterai = baterai

    def nama_alat(self) -> str:
        return "Sikat gigi elektrik"

    def persen_baterai(self) -> int:
        return self._baterai

    def isi_daya(self, menit: int):
        self._baterai = min(100, self._baterai + menit * 5)


def tampilkan_status(daftar: list[BisaDiisiUlang]):
    for alat in daftar:
        print(f"{alat.nama_alat()}: {alat.persen_baterai()}%")


def isi_semua(daftar: list[BisaDiisiUlang], menit: int):
    for alat in daftar:
        alat.isi_daya(menit)


def main():
    daftar: list[BisaDiisiUlang] = [
        SepedaListrik(20),
        Powerbank(50),
        SikatGigiElektrik(90),
    ]
    print("=== SEBELUM DIISI ===")
    tampilkan_status(daftar)

    print()
    print("=== SETELAH DIISI 30 MENIT ===")
    isi_semua(daftar, 30)
    tampilkan_status(daftar)

    penuh = 0
    for alat in daftar:
        if alat.persen_baterai() == 100:
            penuh += 1
    print(f"Sudah penuh: {penuh} dari {len(daftar)} alat")


if __name__ == "__main__":
    main()
