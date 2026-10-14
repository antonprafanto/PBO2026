"""
Solusi Latihan 02 - Factory Bangun Datar
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- Kelas abstrak Bentuk punya dua method abstrak: nama() dan luas().
- Tiga kelas konkret: Persegi, PersegiPanjang, Segitiga.
- BentukFactory.buat(jenis, a, b) adalah SATU-SATUNYA tempat yang memilih
  kelas mana yang dibuat. Jenis yang tidak dikenal -> ValueError.
- Program utama hanya mengenal Bentuk dan BentukFactory.

Cara menjalankan:
    python latihan02_factory_bentuk.py
"""

from abc import ABC, abstractmethod


class Bentuk(ABC):
    """Produk abstrak: bangun datar."""

    @abstractmethod
    def nama(self) -> str:
        """Keterangan bentuk beserta ukurannya."""

    @abstractmethod
    def luas(self) -> int:
        """Luas dalam satuan persegi."""


class Persegi(Bentuk):
    def __init__(self, sisi: int):
        self._sisi = sisi

    def nama(self) -> str:
        return f"Persegi sisi {self._sisi}"

    def luas(self) -> int:
        return self._sisi * self._sisi


class PersegiPanjang(Bentuk):
    def __init__(self, panjang: int, lebar: int):
        self._panjang = panjang
        self._lebar = lebar

    def nama(self) -> str:
        return f"Persegi panjang {self._panjang} x {self._lebar}"

    def luas(self) -> int:
        return self._panjang * self._lebar


class Segitiga(Bentuk):
    def __init__(self, alas: int, tinggi: int):
        self._alas = alas
        self._tinggi = tinggi

    def nama(self) -> str:
        return f"Segitiga alas {self._alas} tinggi {self._tinggi}"

    def luas(self) -> int:
        return self._alas * self._tinggi // 2


class BentukFactory:
    """Simple Factory untuk bangun datar."""

    @staticmethod
    def buat(jenis: str, a: int, b: int) -> Bentuk:
        """a dan b adalah ukuran; b tidak dipakai oleh persegi."""
        pilihan = jenis.lower()
        if pilihan == "persegi":
            return Persegi(a)
        if pilihan == "persegi panjang":
            return PersegiPanjang(a, b)
        if pilihan == "segitiga":
            return Segitiga(a, b)
        raise ValueError(f"Bentuk tidak dikenal: {jenis}")


def main():
    daftar_pesanan = [
        ("persegi", 5, 0),
        ("Persegi Panjang", 8, 3),
        ("SEGITIGA", 6, 4),
        ("lingkaran", 7, 0),
    ]
    total_luas = 0

    print("=== MEMBUAT BENTUK DARI PILIHAN TEKS ===")
    for jenis, a, b in daftar_pesanan:
        try:
            bentuk = BentukFactory.buat(jenis, a, b)
        except ValueError as e:
            print(f"Ditolak: {e}")
            continue
        print(f"{bentuk.nama():<30} luas {bentuk.luas()}")
        total_luas += bentuk.luas()

    print()
    print(f"Total luas bentuk yang berhasil dibuat: {total_luas}")


if __name__ == "__main__":
    main()
