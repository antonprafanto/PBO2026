"""
Modul pesanan: kelas ItemPesanan dan Pesanan.

Relasi yang terlihat di sini:
- Pesanan --> Pelanggan   : ASOSIASI (pesanan "milik" seorang pelanggan,
                            tetapi pelanggan tetap ada walau pesanan selesai)
- Pesanan *-- ItemPesanan : KOMPOSISI (item dibuat di dalam pesanan dan
                            tidak punya arti tanpa pesanannya)
- ItemPesanan --> Menu    : ASOSIASI (item menunjuk ke menu yang dipesan)

Yang baru di Pertemuan 11:
- Pesanan yang sudah LUNAS tidak boleh diubah atau dibayar lagi:
  method yang bersangkutan melempar KedaiError.
- bayar() tidak lagi mengembalikan True/False. Jika pembayaran gagal,
  PembayaranGagalError dari proses() "diteruskan" ke pemanggil, dan
  status pesanan tetap BARU.
"""

from dapat_dicetak import DapatDicetak
from menu import Menu
from pelanggan import Pelanggan
from pembayaran import Pembayaran
from pengecualian import KedaiError
from utilitas import format_rupiah

LEBAR_STRUK = 40


class ItemPesanan:
    """Satu baris pesanan: menu apa dan berapa porsi."""

    def __init__(self, menu: Menu, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._menu = menu  # menyimpan REFERENSI ke objek Menu
        self._jumlah = jumlah

    @property
    def menu(self) -> Menu:
        return self._menu

    @property
    def jumlah(self) -> int:
        return self._jumlah

    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah

    def __str__(self) -> str:
        return f"{self._jumlah} x {self._menu.nama}"


class Pesanan(DapatDicetak):
    """Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan."""

    _nomor_terakhir = 0  # atribut kelas untuk membuat nomor otomatis

    def __init__(self, pelanggan: Pelanggan):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"P{Pesanan._nomor_terakhir:03d}"  # P001, P002, ...
        self._pelanggan = pelanggan
        self._daftar_item: list[ItemPesanan] = []
        self._status = "BARU"

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def pelanggan(self) -> Pelanggan:
        return self._pelanggan

    @property
    def status(self) -> str:
        return self._status

    @property
    def daftar_item(self) -> list[ItemPesanan]:
        """Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._daftar_item)

    def tambah_item(self, menu: Menu, jumlah: int = 1):
        if self._status == "LUNAS":
            raise KedaiError(f"Pesanan {self._nomor} sudah lunas, tidak bisa diubah")
        item = ItemPesanan(menu, jumlah)  # objek item dibuat OLEH pesanan
        menu.kurangi_stok(jumlah)  # bisa melempar StokTidakCukupError
        self._daftar_item.append(item)

    def hitung_total(self) -> int:
        total = 0
        for item in self._daftar_item:
            total += item.hitung_subtotal()
        return total

    def bayar(self, pembayaran: Pembayaran):
        """Membayar pesanan. Melempar KedaiError jika gagal."""
        if self._status == "LUNAS":
            raise KedaiError(f"Pesanan {self._nomor} sudah lunas")
        total = self.hitung_total()
        biaya = pembayaran.hitung_biaya_layanan(total)
        total_bayar = total + biaya
        print(f"Pembayaran pesanan {self._nomor} ({self._pelanggan.nama})")
        print(f"  Metode       : {pembayaran.nama_metode()}")
        if biaya > 0:
            print(f"  Biaya layanan: {format_rupiah(biaya)}")
        print(f"  Total bayar  : {format_rupiah(total_bayar)}")
        pembayaran.proses(total_bayar)  # jika gagal, baris di bawah tidak dijalankan
        self._status = "LUNAS"
        poin = total // 10000
        if poin > 0:
            self._pelanggan.tambah_poin(poin)
        print(f"  Status       : LUNAS (+{poin} poin)")

    def cetak(self):
        """Mencetak struk pesanan (memenuhi kontrak DapatDicetak)."""
        garis = "=" * LEBAR_STRUK
        print(garis)
        print("KEDAIKITA - STRUK PESANAN")
        print(garis)
        print(f"No. Pesanan : {self._nomor}")
        print(f"Pelanggan   : {self._pelanggan.nama}")
        print(f"Status      : {self._status}")
        print("-" * LEBAR_STRUK)
        for item in self._daftar_item:
            subtotal = format_rupiah(item.hitung_subtotal())
            print(f"{str(item):<30}{subtotal:>10}")
        print("-" * LEBAR_STRUK)
        print(f"{'TOTAL':<30}{format_rupiah(self.hitung_total()):>10}")
        print(garis)
