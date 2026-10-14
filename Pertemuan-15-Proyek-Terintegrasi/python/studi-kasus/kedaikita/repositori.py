"""
Modul repositori: membaca dan menulis data KedaiKita ke file CSV.

- RepositoriMenuCSV    : memuat daftar menu dari file, dan menyimpan stok
                         terbaru kembali ke file.
- PencatatTransaksiCSV : sebuah PENGAMAT (Observer, Pertemuan 14) yang
                         menulis satu baris ke file setiap kali ada pesanan
                         berstatus LUNAS. Pesanan tidak perlu diubah sedikit pun.

Format CSV yang dipakai memisahkan kolom dengan titik koma (;).
Contoh baris menu:  Minuman;M01;Kopi Susu Gula Aren;18000;20;dingin
"""

import csv
from pathlib import Path

from kedaikita.menu import Makanan, Menu, Minuman
from kedaikita.pengamat import PengamatPesanan
from kedaikita.pengecualian import FormatDataError
from kedaikita.pesanan import Pesanan

PEMISAH = ";"
KOLOM_MENU = ["jenis", "kode", "nama", "harga", "stok", "ekstra"]
KOLOM_TRANSAKSI = ["nomor", "pelanggan", "no_hp", "jumlah_porsi", "total"]


class RepositoriMenuCSV:
    """Menghubungkan objek Menu dengan file CSV."""

    def __init__(self, path: Path):
        self._path = path

    def muat(self) -> list[Menu]:
        """Membaca file CSV menjadi daftar objek Menu.

        Isi file yang rusak SELALU dilaporkan sebagai FormatDataError lengkap
        dengan nomor barisnya; ValueError bawaan Python tidak lolos keluar.
        """
        hasil: list[Menu] = []
        kode_terpakai: set[str] = set()
        with open(self._path, encoding="utf-8", newline="") as berkas:
            pembaca = csv.reader(berkas, delimiter=PEMISAH)
            # Lewati baris judul kolom. Nilai bawaan None membuat next() tidak
            # melempar StopIteration jika file benar-benar kosong.
            if next(pembaca, None) is None:
                return hasil  # file kosong: belum ada menu
            for nomor_baris, kolom in enumerate(pembaca, start=2):
                if not kolom:  # lewati baris kosong
                    continue
                menu = self._buat_menu(kolom, nomor_baris)
                if menu.kode in kode_terpakai:
                    raise FormatDataError(f"Baris {nomor_baris}: kode {menu.kode} "
                                          f"sudah dipakai")
                kode_terpakai.add(menu.kode)
                hasil.append(menu)
        return hasil

    @staticmethod
    def _buat_menu(kolom: list[str], nomor_baris: int) -> Menu:
        """Factory kecil: mengubah satu baris CSV menjadi Makanan/Minuman."""
        if len(kolom) != len(KOLOM_MENU):
            raise FormatDataError(f"Baris {nomor_baris}: harus ada "
                                  f"{len(KOLOM_MENU)} kolom")
        jenis, kode, nama, teks_harga, teks_stok, ekstra = kolom
        if jenis not in ("Makanan", "Minuman"):
            raise FormatDataError(f"Baris {nomor_baris}: jenis '{jenis}' tidak dikenal")
        level_pedas = 0  # hanya dipakai oleh Makanan
        try:
            harga = int(teks_harga)
            stok = int(teks_stok)
            if jenis == "Makanan":
                level_pedas = int(ekstra)
        except ValueError:
            raise FormatDataError(f"Baris {nomor_baris}: harga, stok, dan level "
                                  f"pedas harus berupa angka") from None
        try:
            if jenis == "Makanan":
                return Makanan(kode, nama, harga, stok, level_pedas)
            return Minuman(kode, nama, harga, stok, ekstra == "dingin")
        except ValueError as e:  # ditolak validasi Menu, misalnya harga 0
            raise FormatDataError(f"Baris {nomor_baris}: {e}") from None

    @staticmethod
    def _ke_kolom(menu: Menu) -> list[str]:
        """Kebalikan _buat_menu: objek Menu menjadi satu baris CSV."""
        if isinstance(menu, Makanan):
            ekstra = str(menu.level_pedas)
        elif isinstance(menu, Minuman):
            ekstra = "dingin" if menu.dingin else "panas"
        else:
            ekstra = ""
        return [menu.kategori, menu.kode, menu.nama, str(menu.harga),
                str(menu.stok), ekstra]

    def simpan(self, daftar_menu: list[Menu]):
        """Menulis ulang file CSV dengan data menu terbaru."""
        with open(self._path, "w", encoding="utf-8", newline="") as berkas:
            penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")
            penulis.writerow(KOLOM_MENU)
            for menu in daftar_menu:
                penulis.writerow(self._ke_kolom(menu))


class PencatatTransaksiCSV(PengamatPesanan):
    """Observer: mencatat setiap pesanan LUNAS ke file CSV."""

    def __init__(self, path: Path, mulai_baru: bool = False):
        self._path = path
        if mulai_baru or not path.exists():
            with open(path, "w", encoding="utf-8", newline="") as berkas:
                penulis = csv.writer(berkas, delimiter=PEMISAH,
                                     lineterminator="\n")
                penulis.writerow(KOLOM_TRANSAKSI)

    def perbarui(self, pesanan: Pesanan):
        if pesanan.status != "LUNAS":
            return
        porsi = 0
        for item in pesanan.daftar_item:
            porsi += item.jumlah
        baris = [pesanan.nomor, pesanan.pelanggan.nama, pesanan.pelanggan.no_hp,
                 str(porsi), str(pesanan.hitung_total())]
        with open(self._path, "a", encoding="utf-8", newline="") as berkas:
            penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")
            penulis.writerow(baris)

    def baca_semua(self) -> list[list[str]]:
        """Semua baris transaksi di file (tanpa baris judul)."""
        with open(self._path, encoding="utf-8", newline="") as berkas:
            pembaca = csv.reader(berkas, delimiter=PEMISAH)
            if next(pembaca, None) is None:  # lewati baris judul kolom
                return []  # file kosong: belum ada transaksi
            return [kolom for kolom in pembaca if kolom]
