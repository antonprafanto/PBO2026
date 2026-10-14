"""
Solusi Latihan 04 - Validasi Nomor HP dan Unit Test-nya
Pertemuan 15 - Proyek Terintegrasi

Ide penyelesaian:
- validasi_no_hp() membersihkan spasi dan tanda hubung, lalu memeriksa aturan
  satu per satu. Setiap pelanggaran melempar ValueError dengan pesan jelas.
  Jika lolos semua aturan, nomor yang sudah bersih dikembalikan.
- Unit test memeriksa kasus normal, kasus gagal, dan kasus BATAS (tepat 10
  dan tepat 13 digit), karena bug paling sering bersembunyi di batas.
- Test dijalankan dari dalam program dengan pencatat hasil sendiri (seperti
  contoh 05) agar output tidak memuat catatan waktu.

Cara menjalankan:
    python latihan04_validasi_no_hp.py
"""

import unittest


def validasi_no_hp(teks: str) -> str:
    """Mengembalikan nomor HP yang sudah bersih, atau melempar ValueError."""
    bersih = teks.replace(" ", "").replace("-", "")
    if bersih == "":
        raise ValueError("Nomor HP tidak boleh kosong")
    for huruf in bersih:
        if huruf < "0" or huruf > "9":
            raise ValueError("Nomor HP hanya boleh berisi angka")
    if not bersih.startswith("08"):
        raise ValueError("Nomor HP harus diawali 08")
    if len(bersih) < 10 or len(bersih) > 13:
        raise ValueError("Nomor HP harus 10 sampai 13 digit")
    return bersih


class UjiValidasiNoHp(unittest.TestCase):
    def test_batas_10_dan_13_digit_diterima(self):
        """Panjang tepat 10 dan tepat 13 digit diterima"""
        self.assertEqual(validasi_no_hp("0812345678"), "0812345678")
        self.assertEqual(validasi_no_hp("0812345678901"), "0812345678901")

    def test_format_dibersihkan(self):
        """Spasi dan tanda hubung dibersihkan"""
        self.assertEqual(validasi_no_hp("0812-3456 7890"), "081234567890")

    def test_huruf_ditolak(self):
        """Nomor berisi huruf ditolak dengan pesan yang tepat"""
        with self.assertRaises(ValueError) as konteks:
            validasi_no_hp("0812abc4567")
        self.assertEqual(str(konteks.exception), "Nomor HP hanya boleh berisi angka")

    def test_kosong_ditolak(self):
        """Nomor kosong ditolak"""
        with self.assertRaises(ValueError):
            validasi_no_hp("   ")

    def test_terlalu_panjang_ditolak(self):
        """Lebih dari 13 digit ditolak"""
        with self.assertRaises(ValueError):
            validasi_no_hp("08123456789012")

    def test_terlalu_pendek_ditolak(self):
        """Kurang dari 10 digit ditolak"""
        with self.assertRaises(ValueError):
            validasi_no_hp("08123")

    def test_tidak_diawali_08_ditolak(self):
        """Nomor yang tidak diawali 08 ditolak"""
        with self.assertRaises(ValueError):
            validasi_no_hp("6281234567890")


class HasilRingkas(unittest.TestResult):
    """Pencatat hasil buatan sendiri: satu baris per test, tanpa waktu."""

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"[LULUS] {test.shortDescription()}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"[GAGAL] {test.shortDescription()}")
        print(f"        -> {err[1]}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"[ERROR] {test.shortDescription()}")
        print(f"        -> {err[1]}")


def main():
    print("=== VALIDASI NOMOR HP ===")
    for teks in ["0812-3456-7890", "0812 3456 789", "08123", "0812abc4567",
                 "6281234567890", ""]:
        try:
            print(f"'{teks}' -> {validasi_no_hp(teks)}")
        except ValueError as e:
            print(f"'{teks}' -> ditolak: {e}")

    print()
    print("=== UNIT TEST ===")
    kumpulan = unittest.defaultTestLoader.loadTestsFromTestCase(UjiValidasiNoHp)
    hasil = HasilRingkas()
    kumpulan.run(hasil)
    gagal = len(hasil.failures) + len(hasil.errors)
    print(f"Hasil: {hasil.testsRun - gagal} lulus, {gagal} gagal")


if __name__ == "__main__":
    main()
