"""
Modul aplikasi: AplikasiKasir, antarmuka teks (CLI) kasir KedaiKita.

Ada dua cara menjalankan:
- jalankan()      : mode interaktif, kasir mengetik pilihan lewat keyboard.
                    Stok disimpan ke data/menu.csv, transaksi ke data/transaksi.csv.
- jalankan_demo() : mode demo tanpa input, selalu menghasilkan output yang sama.
                    Memakai file data/demo-menu.csv dan data/demo-transaksi.csv.
"""

from pathlib import Path

from kedaikita.diskon import (Diskon, DiskonHappyHour, DiskonMember,
                              TanpaDiskon)
from kedaikita.kedai import Kedai
from kedaikita.layanan import LayananKasir
from kedaikita.pengecualian import KedaiError
from kedaikita.penyimpanan import PenyimpananMemori
from kedaikita.pesanan import Pesanan
from kedaikita.repositori import PencatatTransaksiCSV, RepositoriMenuCSV
from kedaikita.struk import StrukPesanan

PILIHAN_DISKON = {"1": TanpaDiskon, "2": DiskonMember, "3": DiskonHappyHour}


class AplikasiKasir:
    """Menghubungkan pengguna (keyboard & layar) dengan LayananKasir."""

    def __init__(self, folder_data: Path):
        self._folder_data = folder_data

    # ------------------------------------------------------------ persiapan
    def _siapkan(self, file_menu: Path,
                 pencatat: PencatatTransaksiCSV) -> LayananKasir:
        kedai = Kedai("KedaiKita", PenyimpananMemori())
        for menu in RepositoriMenuCSV(file_menu).muat():
            kedai.tambah_menu(menu)
        print(f"Memuat menu dari data/{file_menu.name}: "
              f"{kedai.jumlah_menu()} menu")
        return LayananKasir(kedai, [pencatat])

    # ------------------------------------------------------------ mode demo
    def jalankan_demo(self):
        print("=== MODE DEMO KASIR KEDAIKITA ===")
        file_transaksi = self._folder_data / "demo-transaksi.csv"
        pencatat = PencatatTransaksiCSV(file_transaksi, mulai_baru=True)
        layanan = self._siapkan(self._folder_data / "menu_awal.csv", pencatat)
        layanan.kedai.cetak()
        print()

        print("--- Transaksi 1: Budi, tanpa diskon, bayar tunai ---")
        budi = layanan.pelanggan("Budi Santoso", "081234567890")
        pesanan1 = layanan.buat_pesanan(budi)
        layanan.tambah_item(pesanan1, "M01", 2)
        layanan.tambah_item(pesanan1, "M03", 1)
        layanan.bayar(pesanan1, "tunai", 100000, "")
        StrukPesanan(pesanan1).cetak()
        print()

        print("--- Transaksi 2: Siti, Happy Hour, QRIS gagal lalu kartu ---")
        siti = layanan.pelanggan("Siti Aminah", "082198765432")
        pesanan2 = layanan.buat_pesanan(siti)
        layanan.tambah_item(pesanan2, "M02", 2)
        layanan.tambah_item(pesanan2, "M05", 1)
        pesanan2.atur_diskon(DiskonHappyHour())
        try:
            layanan.bayar(pesanan2, "qris", 20000, "")
        except KedaiError as e:
            print(f"[GAGAL] {e}")
        layanan.bayar(pesanan2, "kartu", 0, "BNI")
        StrukPesanan(pesanan2).cetak()
        print()

        print("--- Transaksi 3: input keliru ditangani dengan rapi ---")
        rina = layanan.pelanggan("Rina Marlina", "085312345678")
        pesanan3 = layanan.buat_pesanan(rina)
        for kode, jumlah in [("M99", 1), ("M04", 100), ("M06", 2)]:
            try:
                menu = layanan.tambah_item(pesanan3, kode, jumlah)
                print(f"  -> {jumlah} x {menu.nama} ditambahkan")
            except KedaiError as e:
                print(f"  [GAGAL] {e}")
        layanan.bayar(pesanan3, "qris", 100000, "")
        print()

        print("=== LAPORAN SESI INI ===")
        layanan.laporan().cetak()
        print()

        print("=== RIWAYAT DARI FILE data/demo-transaksi.csv ===")
        for kolom in pencatat.baca_semua():
            print(" | ".join(kolom))
        print()

        file_menu = self._folder_data / "demo-menu.csv"
        RepositoriMenuCSV(file_menu).simpan(layanan.kedai.semua_menu())
        print(f"Stok terbaru disimpan ke data/{file_menu.name}. Isinya:")
        print(file_menu.read_text(encoding="utf-8"), end="")

    # ------------------------------------------------------ mode interaktif
    def jalankan(self):
        file_menu = self._folder_data / "menu.csv"
        sumber = file_menu if file_menu.exists() else (
            self._folder_data / "menu_awal.csv")
        pencatat = PencatatTransaksiCSV(self._folder_data / "transaksi.csv")
        layanan = self._siapkan(sumber, pencatat)
        print("Selamat datang di Kasir KedaiKita!")
        try:
            while True:
                print()
                print("=========== MENU UTAMA ===========")
                print("1. Lihat daftar menu")
                print("2. Buat pesanan baru")
                print("3. Laporan penjualan sesi ini")
                print("4. Riwayat transaksi (dari file)")
                print("0. Simpan dan keluar")
                pilihan = self._tanya("Pilihan: ")
                if pilihan == "1":
                    layanan.kedai.cetak()
                elif pilihan == "2":
                    self._alur_pesanan(layanan)
                elif pilihan == "3":
                    layanan.laporan().cetak()
                elif pilihan == "4":
                    self._tampilkan_riwayat(pencatat)
                elif pilihan == "0":
                    break
                else:
                    print("Pilihan tidak dikenal, coba lagi.")
        except EOFError:  # input habis (misalnya saat input dari file)
            print()
            print("Input berakhir.")
        RepositoriMenuCSV(file_menu).simpan(layanan.kedai.semua_menu())
        print(f"Stok terbaru disimpan ke data/{file_menu.name}. Sampai jumpa!")

    def _alur_pesanan(self, layanan: LayananKasir):
        nama = self._tanya("Nama pelanggan: ")
        no_hp = self._tanya("No. HP: ")
        pesanan = layanan.buat_pesanan(layanan.pelanggan(nama, no_hp))
        print("Masukkan kode menu satu per satu (kosongkan untuk selesai).")
        while True:
            kode = self._tanya("  Kode menu: ").upper()
            if kode == "":
                break
            jumlah = self._tanya_angka("  Jumlah: ")
            try:
                menu = layanan.tambah_item(pesanan, kode, jumlah)
                print(f"  -> {jumlah} x {menu.nama} ditambahkan")
            except (KedaiError, ValueError) as e:
                print(f"  [GAGAL] {e}")
        if not pesanan.daftar_item:
            print("Pesanan kosong, tidak diproses.")
            return
        pesanan.atur_diskon(self._pilih_diskon())
        StrukPesanan(pesanan).cetak()
        self._alur_bayar(layanan, pesanan)
        StrukPesanan(pesanan).cetak()

    def _pilih_diskon(self) -> Diskon:
        print("Diskon: 1. Tanpa diskon  2. Member  3. Happy Hour")
        while True:
            pilihan = self._tanya("Pilihan diskon: ")
            if pilihan in PILIHAN_DISKON:
                return PILIHAN_DISKON[pilihan]()
            print("Pilihan tidak dikenal, coba lagi.")

    def _alur_bayar(self, layanan: LayananKasir, pesanan: Pesanan):
        while pesanan.status != "LUNAS":
            print("Pembayaran: 1. Tunai  2. QRIS  3. Kartu kredit")
            pilihan = self._tanya("Pilihan pembayaran: ")
            try:
                if pilihan == "1":
                    uang = self._tanya_angka("Uang diterima: ")
                    layanan.bayar(pesanan, "tunai", uang, "")
                elif pilihan == "2":
                    saldo = self._tanya_angka("Saldo e-wallet: ")
                    layanan.bayar(pesanan, "qris", saldo, "")
                elif pilihan == "3":
                    bank = self._tanya("Nama bank: ")
                    layanan.bayar(pesanan, "kartu", 0, bank)
                else:
                    print("Pilihan tidak dikenal, coba lagi.")
            except KedaiError as e:
                print(f"[GAGAL] {e}")

    def _tampilkan_riwayat(self, pencatat: PencatatTransaksiCSV):
        daftar = pencatat.baca_semua()
        if not daftar:
            print("Belum ada transaksi tercatat.")
        for kolom in daftar:
            print(" | ".join(kolom))

    # ------------------------------------------------------ bantuan input
    @staticmethod
    def _tanya(pertanyaan: str) -> str:
        return input(pertanyaan).strip()

    def _tanya_angka(self, pertanyaan: str) -> int:
        while True:
            teks = self._tanya(pertanyaan)
            try:
                return int(teks)
            except ValueError:
                print("  Harap isi dengan angka bulat, misalnya 2 atau 50000.")
