"""
Modul layanan: LayananKasir, "otak" alur kerja kasir.

Aplikasi kita kini tersusun berlapis (layered):
    aplikasi.py   TAMPILAN     -> hanya urusan tanya-jawab dengan pengguna
    layanan.py    LAYANAN      -> alur kerja: pelanggan, pesanan, bayar, laporan
    model         DATA/ATURAN  -> Menu, Pesanan, Pembayaran, Diskon, dan lainnya
    repositori.py PENYIMPANAN  -> membaca/menulis file CSV

Lapisan tampilan boleh diganti (misalnya menjadi aplikasi web) tanpa
mengubah lapisan layanan dan model.
"""

from kedaikita.kedai import Kedai
from kedaikita.laporan import LaporanPenjualan
from kedaikita.menu import Menu
from kedaikita.pelanggan import Pelanggan
from kedaikita.pembayaran import PembayaranFactory
from kedaikita.pengamat import PengamatPesanan
from kedaikita.pesanan import Pesanan


class LayananKasir:
    """Menjalankan alur kerja kasir di atas sebuah Kedai."""

    def __init__(self, kedai: Kedai, daftar_pengamat: list[PengamatPesanan]):
        self._kedai = kedai
        self._daftar_pengamat = daftar_pengamat  # dipasang ke setiap pesanan
        self._pelanggan: dict[str, Pelanggan] = {}  # no HP -> Pelanggan

    @property
    def kedai(self) -> Kedai:
        return self._kedai

    def pelanggan(self, nama: str, no_hp: str) -> Pelanggan:
        """Mengambil pelanggan lama (berdasarkan no HP) atau mendaftarkan baru."""
        if no_hp not in self._pelanggan:
            self._pelanggan[no_hp] = Pelanggan(nama, no_hp)
        return self._pelanggan[no_hp]

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = self._kedai.buat_pesanan(pelanggan)
        for pengamat in self._daftar_pengamat:
            pesanan.tambah_pengamat(pengamat)
        return pesanan

    def tambah_item(self, pesanan: Pesanan, kode: str, jumlah: int) -> Menu:
        """Menambah item berdasarkan kode menu. Mengembalikan menu tersebut."""
        menu = self._kedai.cari_menu(kode)
        pesanan.tambah_item(menu, jumlah)
        return menu

    def bayar(self, pesanan: Pesanan, jenis: str, nominal: int, bank: str):
        """Membayar memakai PembayaranFactory (pola Factory)."""
        pembayaran = PembayaranFactory.buat(jenis, nominal, bank)
        pesanan.bayar(pembayaran)

    def laporan(self) -> LaporanPenjualan:
        return LaporanPenjualan(self._kedai.riwayat_pesanan())
