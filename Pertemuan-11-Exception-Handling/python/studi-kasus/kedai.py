"""
Modul kedai: kelas Kedai, "pusat" yang menyimpan menu dan mencatat pesanan.

Relasi yang terlihat di sini:
- Kedai o-- Menu    : AGREGASI (menu dibuat di luar lalu didaftarkan ke kedai;
                      menu bisa tetap ada walau tidak terdaftar di kedai)
- Kedai --> Pesanan : ASOSIASI (kedai mencatat pesanan-pesanan yang dibuat)

Yang baru di Pertemuan 11: cari_menu() tidak lagi mengembalikan None,
tetapi melempar MenuTidakDitemukanError bila kode tidak terdaftar.
"""

from dapat_dicetak import DapatDicetak
from menu import Menu
from pelanggan import Pelanggan
from pengecualian import MenuTidakDitemukanError
from pesanan import Pesanan


class Kedai(DapatDicetak):
    """Kedai yang punya daftar menu dan catatan pesanan."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_menu: list[Menu] = []
        self._daftar_pesanan: list[Pesanan] = []

    @property
    def nama(self) -> str:
        return self._nama

    def tambah_menu(self, menu: Menu):
        self._daftar_menu.append(menu)

    def cari_menu(self, kode: str) -> Menu:
        """Mengembalikan objek Menu dengan kode tertentu.

        Melempar MenuTidakDitemukanError jika kode tidak terdaftar.
        """
        for menu in self._daftar_menu:
            if menu.kode == kode:
                return menu
        raise MenuTidakDitemukanError(kode)

    def jumlah_menu(self) -> int:
        return len(self._daftar_menu)

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = Pesanan(pelanggan)
        self._daftar_pesanan.append(pesanan)
        return pesanan

    def jumlah_pesanan(self) -> int:
        return len(self._daftar_pesanan)

    def cetak(self):
        """Mencetak daftar menu (memenuhi kontrak DapatDicetak)."""
        print(f"=== MENU {self._nama} ===")
        for menu in self._daftar_menu:
            print(menu)
