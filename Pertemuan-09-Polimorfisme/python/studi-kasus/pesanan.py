"""
Modul pesanan: kelas ItemPesanan dan Pesanan.

Relasi yang terlihat di sini:
- Pesanan --> Pelanggan   : ASOSIASI (pesanan "milik" seorang pelanggan,
                            tetapi pelanggan tetap ada walau pesanan selesai)
- Pesanan *-- ItemPesanan : KOMPOSISI (item dibuat di dalam pesanan dan
                            tidak punya arti tanpa pesanannya)
- ItemPesanan --> Menu    : ASOSIASI (item menunjuk ke menu yang dipesan)

Yang baru di Pertemuan 09:
- tambah_item() punya nilai bawaan jumlah=1 (Python tidak punya overloading,
  jadi nilai bawaan inilah penggantinya; Java memakai overloading).
- Pesanan punya status: "BARU" lalu "LUNAS" setelah dibayar.
- Method bayar() menerima objek Pembayaran JENIS APA PUN (polimorfisme).
"""

from menu import Menu
from pelanggan import Pelanggan
from pembayaran import Pembayaran
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


class Pesanan:
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
        item = ItemPesanan(menu, jumlah)  # objek item dibuat OLEH pesanan
        menu.kurangi_stok(jumlah)  # gagal (ValueError) jika stok kurang
        self._daftar_item.append(item)

    def hitung_total(self) -> int:
        total = 0
        for item in self._daftar_item:
            total += item.hitung_subtotal()
        return total

    def bayar(self, pembayaran: Pembayaran) -> bool:
        """Membayar pesanan dengan metode pembayaran apa pun."""
        total = self.hitung_total()
        biaya = pembayaran.hitung_biaya_layanan(total)  # polimorfisme
        total_bayar = total + biaya
        print(f"Pembayaran pesanan {self._nomor} ({self._pelanggan.nama})")
        print(f"  Metode       : {pembayaran.nama_metode()}")  # polimorfisme
        if biaya > 0:
            print(f"  Biaya layanan: {format_rupiah(biaya)}")
        print(f"  Total bayar  : {format_rupiah(total_bayar)}")
        berhasil = pembayaran.proses(total_bayar)  # polimorfisme
        if berhasil:
            self._status = "LUNAS"
            poin = total // 10000
            if poin > 0:
                self._pelanggan.tambah_poin(poin)
            print(f"  Status       : LUNAS (+{poin} poin)")
        else:
            print("  Status       : GAGAL, silakan pilih metode lain")
        return berhasil

    def cetak_struk(self):
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
