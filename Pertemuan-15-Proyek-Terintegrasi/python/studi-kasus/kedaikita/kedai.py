"""
Modul kedai: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.

Yang berubah di Pertemuan 13 (DIP - Dependency Inversion):
- Kedai tidak lagi membuat list riwayat sendiri. Tempat penyimpanan
  pesanan "disuntikkan" lewat konstruktor (dependency injection) dan
  bertipe abstrak PenyimpananPesanan. Kedai tidak peduli apakah pesanan
  disimpan di memori, di file, atau di database.
"""

from kedaikita.dapat_dicetak import DapatDicetak
from kedaikita.menu import Menu
from kedaikita.pelanggan import Pelanggan
from kedaikita.pengecualian import MenuTidakDitemukanError
from kedaikita.penyimpanan import PenyimpananPesanan
from kedaikita.pesanan import Pesanan


class Kedai(DapatDicetak):
    """Kedai yang punya daftar menu dan catatan pesanan."""

    def __init__(self, nama: str, penyimpanan: PenyimpananPesanan):
        self._nama = nama
        self._daftar_menu: dict[str, Menu] = {}  # kode -> objek Menu
        self._penyimpanan = penyimpanan  # bergantung pada ABSTRAKSI

    @property
    def nama(self) -> str:
        return self._nama

    def tambah_menu(self, menu: Menu):
        if menu.kode in self._daftar_menu:
            raise ValueError(f"Kode {menu.kode} sudah dipakai")
        self._daftar_menu[menu.kode] = menu

    def cari_menu(self, kode: str) -> Menu:
        """Mengembalikan Menu berdasarkan kode.

        Melempar MenuTidakDitemukanError jika kode tidak terdaftar.
        """
        if kode not in self._daftar_menu:
            raise MenuTidakDitemukanError(kode)
        return self._daftar_menu[kode]

    def semua_menu(self) -> list[Menu]:
        """Salinan daftar menu, urut sesuai urutan saat ditambahkan."""
        return list(self._daftar_menu.values())

    def menu_berdasarkan_kategori(self, kategori: str) -> list[Menu]:
        return [menu for menu in self._daftar_menu.values()
                if menu.kategori == kategori]

    def daftar_kategori(self) -> list[str]:
        """Kategori unik (tanpa duplikat), diurutkan abjad."""
        kategori_unik: set[str] = set()
        for menu in self._daftar_menu.values():
            kategori_unik.add(menu.kategori)
        return sorted(kategori_unik)

    def jumlah_menu(self) -> int:
        return len(self._daftar_menu)

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = Pesanan(pelanggan)
        self._penyimpanan.simpan(pesanan)
        return pesanan

    def riwayat_pesanan(self) -> list[Pesanan]:
        return self._penyimpanan.semua()

    def jumlah_pesanan(self) -> int:
        return self._penyimpanan.jumlah()

    def cetak(self):
        """Mencetak daftar menu (memenuhi kontrak DapatDicetak)."""
        print(f"=== MENU {self._nama} ===")
        for menu in self._daftar_menu.values():
            print(menu)
