"""
Solusi Latihan 02 - Diskon Ulang Tahun (OCP + LSP)
Pertemuan 13 - Prinsip SOLID

Ide penyelesaian:
- Aturan diskon baru = kelas BARU turunan Diskon. Kelas Pesanan, kelas diskon
  lain, dan pencetak struk TIDAK diubah (OCP).
- DiskonUlangTahun: gratis 1 porsi menu TERMURAH di dalam pesanan.
- Menepati janji Diskon (LSP): potongan tidak pernah negatif, tidak pernah
  melebihi subtotal, dan pesanan kosong tidak membuat program error.

Agar file ini bisa dijalankan sendiri, kelas-kelas studi kasus yang
dibutuhkan disalin dalam versi RINGKAS. Satu-satunya kelas yang BARU adalah
DiskonUlangTahun. Di proyekmu, cukup tambahkan kelas itu ke diskon.py.

Cara menjalankan:
    python latihan02_diskon_ulang_tahun.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


# ------------------------------- salinan RINGKAS dari studi kasus (tidak diubah)
class Menu:
    def __init__(self, nama: str, harga: int):
        self._nama = nama
        self._harga = harga

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga(self) -> int:
        return self._harga


class ItemPesanan:
    def __init__(self, menu: Menu, jumlah: int):
        self._menu = menu
        self._jumlah = jumlah

    @property
    def menu(self) -> Menu:
        return self._menu

    @property
    def jumlah(self) -> int:
        return self._jumlah

    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah


class Pelanggan:
    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama


class Diskon(ABC):
    @abstractmethod
    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        """Besar potongan dalam rupiah (tidak pernah negatif)."""

    @abstractmethod
    def keterangan(self) -> str:
        """Nama singkat diskon untuk ditampilkan di struk."""

    @staticmethod
    def subtotal_dari(daftar_item: list[ItemPesanan]) -> int:
        total = 0
        for item in daftar_item:
            total += item.hitung_subtotal()
        return total


class TanpaDiskon(Diskon):
    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        return 0

    def keterangan(self) -> str:
        return "Tanpa diskon"


class Pesanan:
    def __init__(self, pelanggan: Pelanggan):
        self._pelanggan = pelanggan
        self._daftar_item: list[ItemPesanan] = []
        self._diskon: Diskon = TanpaDiskon()

    @property
    def pelanggan(self) -> Pelanggan:
        return self._pelanggan

    @property
    def diskon(self) -> Diskon:
        return self._diskon

    @property
    def daftar_item(self) -> list[ItemPesanan]:
        return list(self._daftar_item)

    def tambah_item(self, menu: Menu, jumlah: int):
        self._daftar_item.append(ItemPesanan(menu, jumlah))

    def atur_diskon(self, diskon: Diskon):
        self._diskon = diskon

    def hitung_subtotal(self) -> int:
        return Diskon.subtotal_dari(self._daftar_item)

    def hitung_potongan(self) -> int:
        return self._diskon.hitung_potongan(list(self._daftar_item), self._pelanggan)

    def hitung_total(self) -> int:
        return self.hitung_subtotal() - self.hitung_potongan()


# ------------------------------------------------------------------- KELAS BARU
class DiskonUlangTahun(Diskon):
    """Hadiah ulang tahun: gratis 1 porsi menu termurah di dalam pesanan."""

    def hitung_potongan(self, daftar_item: list[ItemPesanan],
                        pelanggan: Pelanggan) -> int:
        if not daftar_item:  # pesanan kosong: potongan 0, bukan error (LSP)
            return 0
        termurah = daftar_item[0].menu.harga
        for item in daftar_item:
            if item.menu.harga < termurah:
                termurah = item.menu.harga
        return termurah  # selalu >= 0 dan tidak melebihi subtotal

    def keterangan(self) -> str:
        return "Ulang Tahun"


# ------------------------------------------------------------- program utama
def cetak_struk(pesanan: Pesanan):
    print(f"Pesanan {pesanan.pelanggan.nama}")
    for item in pesanan.daftar_item:
        kiri = f"{item.jumlah} x {item.menu.nama}"
        print(f"{kiri:<30}{format_rupiah(item.hitung_subtotal()):>10}")
    print(f"{'Subtotal':<30}{format_rupiah(pesanan.hitung_subtotal()):>10}")
    potongan = pesanan.hitung_potongan()
    if potongan > 0:
        kiri = f"Diskon {pesanan.diskon.keterangan()}"
        print(f"{kiri:<30}{'-' + format_rupiah(potongan):>10}")
    print(f"{'TOTAL':<30}{format_rupiah(pesanan.hitung_total()):>10}")


def main():
    es_teh = Menu("Es Teh Manis", 8000)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000)
    pisang = Menu("Pisang Goreng Keju", 15000)

    print("=== SITI BERULANG TAHUN ===")
    pesanan_siti = Pesanan(Pelanggan("Siti Aminah"))
    pesanan_siti.tambah_item(es_teh, 2)
    pesanan_siti.tambah_item(pisang, 1)
    pesanan_siti.atur_diskon(DiskonUlangTahun())  # cukup objek diskon baru
    cetak_struk(pesanan_siti)

    print()
    print("=== BUDI BERULANG TAHUN, PESAN SATU MENU ===")
    pesanan_budi = Pesanan(Pelanggan("Budi Santoso"))
    pesanan_budi.tambah_item(nasi_goreng, 1)
    pesanan_budi.atur_diskon(DiskonUlangTahun())
    cetak_struk(pesanan_budi)


    print()
    print("=== PESANAN KOSONG (UJI LSP) ===")
    kosong = Pesanan(Pelanggan("Andi Wijaya"))
    kosong.atur_diskon(DiskonUlangTahun())
    print(f"Potongan: {format_rupiah(kosong.hitung_potongan())}, "
          f"total: {format_rupiah(kosong.hitung_total())}")


if __name__ == "__main__":
    main()
