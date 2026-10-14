"""
Contoh 05 - Unit Test Mini dengan unittest
Pertemuan 15 - Proyek Terintegrasi

Unit test adalah kode kecil yang memeriksa kode lain secara OTOMATIS.
- Kelas uji mewarisi unittest.TestCase.
- setUp() dijalankan ulang sebelum SETIAP test, agar tiap test mulai dari nol.
- Setiap method yang namanya diawali test_ adalah satu pengujian.
- assertEqual(a, b) lulus jika a == b; assertRaises(X) lulus jika X dilempar.

Biasanya test dijalankan dengan perintah:
    python -m unittest discover -s tests -v
Di contoh ini test dijalankan dari dalam program (lihat jalankan_uji()) dan
hasilnya dicetak dengan format sendiri tanpa catatan waktu, sehingga output
selalu sama setiap kali program dijalankan.

Cara menjalankan:
    python contoh05_unit_test_mini.py
"""

import unittest

BATAS_GRATIS_ONGKIR = 100000
ONGKIR = 10000


class KeranjangBelanja:
    """Keranjang belanja daring. Gratis ongkir jika belanja minimal Rp100.000."""

    def __init__(self):
        self._daftar: list[tuple[str, int, int]] = []  # (nama, harga, jumlah)

    def tambah(self, nama: str, harga: int, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._daftar.append((nama, harga, jumlah))

    def subtotal(self) -> int:
        total = 0
        for _, harga, jumlah in self._daftar:
            total += harga * jumlah
        return total

    def ongkir(self) -> int:
        if self.subtotal() >= BATAS_GRATIS_ONGKIR:
            return 0
        return ONGKIR

    def total(self) -> int:
        return self.subtotal() + self.ongkir()


class KeranjangBerbug(KeranjangBelanja):
    """Versi yang SENGAJA diberi bug: memakai > padahal seharusnya >=."""

    def ongkir(self) -> int:
        if self.subtotal() > BATAS_GRATIS_ONGKIR:  # BUG: tepat 100000 tidak gratis
            return 0
        return ONGKIR


class UjiKeranjang(unittest.TestCase):
    """Kumpulan test untuk KeranjangBelanja."""

    def setUp(self):  # [1] dijalankan ulang sebelum SETIAP test
        self.keranjang = KeranjangBelanja()

    def test_jumlah_nol_ditolak(self):
        """Jumlah barang 0 ditolak"""
        with self.assertRaises(ValueError):  # [2] lulus jika ValueError dilempar
            self.keranjang.tambah("Buku tulis", 5000, 0)

    def test_ongkir_di_bawah_batas(self):
        """Belanja Rp99.000 kena ongkir Rp10.000"""
        self.keranjang.tambah("Kaos", 99000, 1)
        self.assertEqual(self.keranjang.ongkir(), 10000)  # [3] hasil, harapan

    def test_ongkir_gratis_tepat_di_batas(self):
        """Belanja tepat Rp100.000 gratis ongkir"""
        self.keranjang.tambah("Sepatu", 100000, 1)
        self.assertEqual(self.keranjang.ongkir(), 0)

    def test_subtotal_dua_barang(self):
        """Subtotal dua barang dijumlahkan"""
        self.keranjang.tambah("Pulpen", 3000, 4)
        self.keranjang.tambah("Map", 8000, 2)
        self.assertEqual(self.keranjang.subtotal(), 28000)

    def test_total_termasuk_ongkir(self):
        """Total = subtotal + ongkir"""
        self.keranjang.tambah("Topi", 60000, 1)
        self.assertEqual(self.keranjang.total(), 70000)


class UjiKeranjangBerbug(UjiKeranjang):
    """Test yang SAMA (diwarisi), tetapi dijalankan pada KeranjangBerbug."""

    def setUp(self):  # [4] hanya cara membuat objeknya yang diganti
        self.keranjang = KeranjangBerbug()


class HasilRingkas(unittest.TestResult):
    """Pencatat hasil buatan sendiri: satu baris per test, tanpa waktu."""

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"[LULUS] {test.shortDescription()}")  # [5] baris pertama docstring

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"[GAGAL] {test.shortDescription()}")
        print(f"        -> {err[1]}")  # [6] pesan dari assertEqual

    def addError(self, test, err):
        super().addError(test, err)
        print(f"[ERROR] {test.shortDescription()}")
        print(f"        -> {err[1]}")


def jalankan_uji(kelas_uji):
    """Menjalankan semua test di kelas_uji (urut abjad nama method)."""
    kumpulan = unittest.defaultTestLoader.loadTestsFromTestCase(kelas_uji)  # [7]
    hasil = HasilRingkas()
    kumpulan.run(hasil)
    gagal = len(hasil.failures) + len(hasil.errors)
    print(f"Hasil: {hasil.testsRun - gagal} lulus, {gagal} gagal")


def main():
    print("=== UJI 1: KeranjangBelanja ===")
    jalankan_uji(UjiKeranjang)

    print()
    print("=== UJI 2: KeranjangBerbug (sengaja diberi bug) ===")
    jalankan_uji(UjiKeranjangBerbug)


if __name__ == "__main__":
    main()
