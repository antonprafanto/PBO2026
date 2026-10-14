"""
Solusi Latihan 05 - KedaiKita: Strategi Baru DiskonPelajar
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- DiskonPelajar adalah STRATEGY baru: potongan 10% dari subtotal, tetapi
  paling banyak Rp5.000. Kuncinya: min(potongan, MAKSIMAL).
- Kelas Keranjang (context) TIDAK diubah sama sekali saat strategi baru
  ditambahkan. Inilah OCP (Pertemuan 13) yang diwujudkan oleh pola Strategy.
- Pajak 10% dihitung dari subtotal SETELAH dipotong diskon, sama seperti
  Pesanan.hitung_pajak() di studi kasus.

Supaya file ini bisa dijalankan sendiri, kita memakai versi MINI dari kelas
studi kasus dengan nama berbeda: MenuKedai (Menu), ItemKeranjang
(ItemPesanan), AturanDiskon (Diskon), Keranjang (Pesanan). Di salinan studi
kasusmu sendiri, cukup tambahkan kelas DiskonPelajar(Diskon) ke diskon.py.

Cara menjalankan:
    python latihan05_diskon_pelajar.py
"""

from abc import ABC, abstractmethod


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class MenuKedai:
    def __init__(self, nama: str, harga: int, kategori: str):
        self._nama = nama
        self._harga = harga
        self._kategori = kategori

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga(self) -> int:
        return self._harga

    @property
    def kategori(self) -> str:
        return self._kategori


class ItemKeranjang:
    def __init__(self, menu: MenuKedai, jumlah: int):
        self._menu = menu
        self._jumlah = jumlah

    @property
    def menu(self) -> MenuKedai:
        return self._menu

    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah


class AturanDiskon(ABC):
    """Strategy: kontrak semua aturan diskon (sama dengan Diskon)."""

    @abstractmethod
    def hitung_potongan(self, daftar_item: list[ItemKeranjang]) -> int:
        """Besar potongan dalam rupiah (tidak pernah negatif)."""

    @abstractmethod
    def keterangan(self) -> str:
        """Nama singkat aturan diskon."""

    @staticmethod
    def subtotal_dari(daftar_item: list[ItemKeranjang]) -> int:
        total = 0
        for item in daftar_item:
            total += item.hitung_subtotal()
        return total


class TanpaPotongan(AturanDiskon):
    def hitung_potongan(self, daftar_item: list[ItemKeranjang]) -> int:
        return 0

    def keterangan(self) -> str:
        return "Tanpa diskon"


class PotonganHappyHour(AturanDiskon):
    """20% khusus untuk item minuman."""

    def hitung_potongan(self, daftar_item: list[ItemKeranjang]) -> int:
        total_minuman = 0
        for item in daftar_item:
            if item.menu.kategori == "Minuman":
                total_minuman += item.hitung_subtotal()
        return total_minuman * 20 // 100

    def keterangan(self) -> str:
        return "Happy Hour (minuman)"


class DiskonPelajar(AturanDiskon):
    """Strategi BARU: potongan 10% untuk pelajar, paling banyak Rp5.000."""

    PERSEN = 10
    MAKSIMAL = 5000

    def hitung_potongan(self, daftar_item: list[ItemKeranjang]) -> int:
        potongan = AturanDiskon.subtotal_dari(daftar_item) * DiskonPelajar.PERSEN // 100
        return min(potongan, DiskonPelajar.MAKSIMAL)  # dibatasi Rp5.000

    def keterangan(self) -> str:
        return "Pelajar 10%"


class Keranjang:
    """Context (versi mini Pesanan). TIDAK diubah saat strategi baru ditambah."""

    PAJAK_PERSEN = 10

    def __init__(self):
        self._daftar_item: list[ItemKeranjang] = []
        self._diskon: AturanDiskon = TanpaPotongan()

    def tambah(self, menu: MenuKedai, jumlah: int):
        self._daftar_item.append(ItemKeranjang(menu, jumlah))

    def atur_diskon(self, diskon: AturanDiskon):
        self._diskon = diskon

    def hitung_subtotal(self) -> int:
        return AturanDiskon.subtotal_dari(self._daftar_item)

    def hitung_potongan(self) -> int:
        return self._diskon.hitung_potongan(list(self._daftar_item))

    def hitung_pajak(self) -> int:
        dasar = self.hitung_subtotal() - self.hitung_potongan()
        return dasar * Keranjang.PAJAK_PERSEN // 100

    def hitung_total(self) -> int:
        return self.hitung_subtotal() - self.hitung_potongan() + self.hitung_pajak()


def bandingkan(judul: str, keranjang: Keranjang):
    print(f"=== {judul} ===")
    print(f"Subtotal: {format_rupiah(keranjang.hitung_subtotal())}")
    for strategi in [TanpaPotongan(), PotonganHappyHour(), DiskonPelajar()]:
        keranjang.atur_diskon(strategi)
        potongan = format_rupiah(keranjang.hitung_potongan())
        total = format_rupiah(keranjang.hitung_total())
        print(f"{strategi.keterangan():<22} potongan {potongan:>8}, "
              f"total {total:>8}")


def main():
    kopi = MenuKedai("Kopi Susu Gula Aren", 18000, "Minuman")
    es_teh = MenuKedai("Es Teh Manis", 8000, "Minuman")
    mie = MenuKedai("Mie Goreng Jawa", 23000, "Makanan")
    pisang = MenuKedai("Pisang Goreng Keju", 15000, "Makanan")

    pesanan_kecil = Keranjang()
    pesanan_kecil.tambah(es_teh, 2)
    pesanan_kecil.tambah(pisang, 1)
    bandingkan("2 ES TEH MANIS + 1 PISANG GORENG KEJU", pesanan_kecil)

    print()
    pesanan_besar = Keranjang()
    pesanan_besar.tambah(kopi, 2)
    pesanan_besar.tambah(mie, 1)
    bandingkan("2 KOPI SUSU GULA AREN + 1 MIE GORENG JAWA", pesanan_besar)


if __name__ == "__main__":
    main()
