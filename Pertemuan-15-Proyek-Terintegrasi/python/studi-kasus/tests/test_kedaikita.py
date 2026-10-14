"""
Unit test untuk KedaiKita (Pertemuan 15).

Unit test adalah kode kecil yang memeriksa kode kita secara otomatis.
Setiap method yang namanya diawali "test_" adalah satu pengujian.

Cara menjalankan (dari dalam folder studi-kasus):
    python -m unittest discover -s tests -v
"""

import contextlib
import io
import tempfile
import unittest
from pathlib import Path

from kedaikita.diskon import DiskonHappyHour, DiskonMember, DiskonPersen
from kedaikita.menu import Makanan, Minuman
from kedaikita.pelanggan import Pelanggan
from kedaikita.pembayaran import PembayaranFactory, PembayaranTunai
from kedaikita.pengecualian import (FormatDataError, PembayaranGagalError,
                                    StokTidakCukupError)
from kedaikita.pesanan import Pesanan
from kedaikita.repositori import RepositoriMenuCSV
from kedaikita.struk import StrukPesanan


class TestMenu(unittest.TestCase):
    def test_harga_harus_positif(self):
        with self.assertRaises(ValueError):
            Minuman("X01", "Menu Uji", 0, 5)

    def test_level_pedas_maksimal_lima(self):
        with self.assertRaises(ValueError):
            Makanan("X02", "Menu Uji", 10000, 5, 6)

    def test_stok_tidak_berubah_jika_gagal(self):
        menu = Makanan("X03", "Menu Uji", 10000, 3)
        with self.assertRaises(StokTidakCukupError):
            menu.kurangi_stok(5)
        self.assertEqual(menu.stok, 3)


class TestPesanan(unittest.TestCase):
    def setUp(self):
        """Dijalankan ulang sebelum SETIAP test, agar tiap test mulai dari nol."""
        self.kopi = Minuman("M01", "Kopi Susu Gula Aren", 18000, 10)
        self.nasi = Makanan("M03", "Nasi Goreng Kampung", 25000, 10, 2)
        self.pelanggan = Pelanggan("Uji Coba", "080000000000")
        self.pesanan = Pesanan(self.pelanggan)
        self.pesanan.tambah_item(self.kopi, 2)
        self.pesanan.tambah_item(self.nasi, 1)

    def test_subtotal(self):
        self.assertEqual(self.pesanan.hitung_subtotal(), 61000)

    def test_total_sudah_termasuk_pajak_10_persen(self):
        self.assertEqual(self.pesanan.hitung_total(), 67100)

    def test_stok_berkurang_setelah_dipesan(self):
        self.assertEqual(self.kopi.stok, 8)

    def test_diskon_persen(self):
        self.pesanan.atur_diskon(DiskonPersen(10))
        self.assertEqual(self.pesanan.hitung_potongan(), 6100)

    def test_happy_hour_hanya_untuk_minuman(self):
        self.pesanan.atur_diskon(DiskonHappyHour())
        self.assertEqual(self.pesanan.hitung_potongan(), 7200)

    def test_diskon_member_butuh_10_poin(self):
        self.pesanan.atur_diskon(DiskonMember())
        self.assertEqual(self.pesanan.hitung_potongan(), 0)
        self.pelanggan.tambah_poin(10)
        self.assertEqual(self.pesanan.hitung_potongan(), 6100)

    def test_bayar_gagal_status_tetap_baru(self):
        with contextlib.redirect_stdout(io.StringIO()):  # sembunyikan print
            with self.assertRaises(PembayaranGagalError):
                self.pesanan.bayar(PembayaranTunai(1000))
        self.assertEqual(self.pesanan.status, "BARU")

    def test_struk_memuat_total(self):
        teks = StrukPesanan(self.pesanan).buat_teks()
        self.assertIn("TOTAL", teks)
        self.assertIn("Rp67.100", teks)


class TestPembayaranFactory(unittest.TestCase):
    def test_jenis_tidak_dikenal(self):
        with self.assertRaises(ValueError):
            PembayaranFactory.buat("bitcoin", 0, "")

    def test_huruf_besar_kecil_tidak_masalah(self):
        self.assertEqual(PembayaranFactory.buat("QRIS", 0, "").nama_metode(),
                         "QRIS")


class TestRepositoriMenuCSV(unittest.TestCase):
    def test_simpan_lalu_muat_kembali(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "menu.csv"
            repo = RepositoriMenuCSV(path)
            repo.simpan([Minuman("M01", "Kopi", 18000, 7, False),
                         Makanan("M02", "Nasi", 25000, 3, 4)])
            hasil = repo.muat()
        self.assertEqual(len(hasil), 2)
        self.assertEqual(hasil[0].stok, 7)
        self.assertFalse(hasil[0].dingin)
        self.assertEqual(hasil[1].level_pedas, 4)

    def test_file_rusak_ditolak(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "menu.csv"
            path.write_text("jenis;kode;nama;harga;stok;ekstra\n"
                            "Makanan;M01;Nasi;mahal;3;0\n", encoding="utf-8")
            with self.assertRaises(FormatDataError):
                RepositoriMenuCSV(path).muat()

    def test_kode_ganda_ditolak(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / "menu.csv"
            path.write_text("jenis;kode;nama;harga;stok;ekstra\n"
                            "Minuman;M01;Kopi;18000;5;dingin\n"
                            "Makanan;M01;Nasi;25000;3;0\n", encoding="utf-8")
            with self.assertRaises(FormatDataError):
                RepositoriMenuCSV(path).muat()


if __name__ == "__main__":
    unittest.main()
