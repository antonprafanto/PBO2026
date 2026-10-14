"""
Modul laporan: kelas LaporanPenjualan.

Contoh nyata pemakaian koleksi:
- list   : daftar pesanan yang sudah lunas
- dict   : menghitung jumlah porsi per menu & pendapatan per kategori
- sort   : mengurutkan menu terlaris (porsi terbanyak dulu)
- generik: hasil menu terlaris berupa list[Pasangan[str, int]]
"""

from dapat_dicetak import DapatDicetak
from pasangan import Pasangan
from pesanan import Pesanan
from utilitas import format_rupiah

LEBAR = 40


class LaporanPenjualan(DapatDicetak):
    """Ringkasan penjualan dari pesanan yang sudah dibayar (LUNAS dst.)."""

    def __init__(self, daftar_pesanan: list[Pesanan]):
        self._pesanan_lunas = [p for p in daftar_pesanan if p.status != "BARU"]

    def jumlah_pesanan(self) -> int:
        return len(self._pesanan_lunas)

    def total_pendapatan(self) -> int:
        total = 0
        for pesanan in self._pesanan_lunas:
            total += pesanan.hitung_total()
        return total

    def jumlah_terjual(self) -> dict[str, int]:
        """Nama menu -> total porsi terjual."""
        hasil: dict[str, int] = {}
        for pesanan in self._pesanan_lunas:
            for item in pesanan.daftar_item:
                nama = item.menu.nama
                hasil[nama] = hasil.get(nama, 0) + item.jumlah
        return hasil

    def menu_terlaris(self, n: int = 3) -> list[Pasangan[str, int]]:
        """n menu dengan porsi terbanyak. Jika seri, urut nama A-Z."""
        daftar = [Pasangan(nama, jumlah)
                  for nama, jumlah in self.jumlah_terjual().items()]
        daftar.sort(key=lambda p: (-p.kedua, p.pertama))
        return daftar[:n]

    def pendapatan_per_kategori(self) -> dict[str, int]:
        """Kategori -> jumlah harga menu terjual (sebelum diskon & pajak).

        Hasilnya diurutkan berdasarkan nama kategori.
        """
        hasil: dict[str, int] = {}
        for pesanan in self._pesanan_lunas:
            for item in pesanan.daftar_item:
                kategori = item.menu.kategori
                hasil[kategori] = hasil.get(kategori, 0) + item.hitung_subtotal()
        return dict(sorted(hasil.items()))

    def cetak(self):
        garis = "=" * LEBAR
        print(garis)
        print("LAPORAN PENJUALAN KEDAIKITA")
        print(garis)
        print(f"{'Pesanan lunas':<30}{self.jumlah_pesanan():>10}")
        total = format_rupiah(self.total_pendapatan())
        print(f"{'Total pendapatan':<30}{total:>10}")
        print("-" * LEBAR)
        print("Menu terlaris:")
        for nomor, pasangan in enumerate(self.menu_terlaris(), start=1):
            print(f"{nomor}. {pasangan.pertama} ({pasangan.kedua} porsi)")
        print("-" * LEBAR)
        print("Penjualan per kategori (sebelum diskon & pajak):")
        for kategori, nilai in self.pendapatan_per_kategori().items():
            print(f"{kategori:<30}{format_rupiah(nilai):>10}")
        print(garis)
