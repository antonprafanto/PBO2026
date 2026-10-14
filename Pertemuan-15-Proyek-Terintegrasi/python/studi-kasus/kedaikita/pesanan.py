"""
Modul pesanan: kelas Pesanan.

Relasi yang terlihat di sini:
- Pesanan --> Pelanggan   : ASOSIASI (pesanan "milik" seorang pelanggan,
                            tetapi pelanggan tetap ada walau pesanan selesai)
- Pesanan *-- ItemPesanan : KOMPOSISI (item dibuat di dalam pesanan dan
                            tidak punya arti tanpa pesanannya)

Yang baru di Pertemuan 14 (design pattern):
- Pajak: persentasenya dibaca dari PengaturanKedai (Singleton).
- Observer: Pesanan menyimpan daftar pengamat (PengamatPesanan) dan memberi
  tahu mereka setiap kali status berubah lewat ubah_status().
- Strategy: objek Diskon (sudah ada sejak Pertemuan 13) bisa ditukar kapan saja.
"""

from kedaikita.diskon import Diskon, TanpaDiskon
from kedaikita.item_pesanan import ItemPesanan
from kedaikita.menu import Menu
from kedaikita.pelanggan import Pelanggan
from kedaikita.pembayaran import Pembayaran
from kedaikita.pengamat import PengamatPesanan
from kedaikita.pengaturan import PengaturanKedai
from kedaikita.pengecualian import KedaiError
from kedaikita.utilitas import format_rupiah

STATUS_VALID = ("BARU", "LUNAS", "DIPROSES", "SIAP", "SELESAI")


class Pesanan:
    """Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan."""

    _nomor_terakhir = 0  # atribut kelas untuk membuat nomor otomatis

    def __init__(self, pelanggan: Pelanggan):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"P{Pesanan._nomor_terakhir:03d}"  # P001, P002, ...
        self._pelanggan = pelanggan
        self._daftar_item: list[ItemPesanan] = []
        self._status = "BARU"
        self._diskon: Diskon = TanpaDiskon()
        self._daftar_pengamat: list[PengamatPesanan] = []

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
    def diskon(self) -> Diskon:
        return self._diskon

    @property
    def daftar_item(self) -> list[ItemPesanan]:
        """Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._daftar_item)

    def tambah_item(self, menu: Menu, jumlah: int = 1):
        if self._status != "BARU":  # sudah dibayar (LUNAS atau sesudahnya)
            raise KedaiError(f"Pesanan {self._nomor} sudah lunas, tidak bisa diubah")
        item = ItemPesanan(menu, jumlah)  # objek item dibuat OLEH pesanan
        menu.kurangi_stok(jumlah)  # bisa melempar StokTidakCukupError
        self._daftar_item.append(item)

    def atur_diskon(self, diskon: Diskon):
        if self._status != "BARU":  # sudah dibayar (LUNAS atau sesudahnya)
            raise KedaiError(f"Pesanan {self._nomor} sudah lunas, tidak bisa diubah")
        self._diskon = diskon

    def hitung_subtotal(self) -> int:
        total = 0
        for item in self._daftar_item:
            total += item.hitung_subtotal()
        return total

    def hitung_potongan(self) -> int:
        return self._diskon.hitung_potongan(list(self._daftar_item),
                                            self._pelanggan)

    def hitung_pajak(self) -> int:
        """Pajak dihitung dari subtotal setelah dipotong diskon."""
        persen = PengaturanKedai.get_instance().pajak_persen
        return (self.hitung_subtotal() - self.hitung_potongan()) * persen // 100

    def hitung_total(self) -> int:
        return self.hitung_subtotal() - self.hitung_potongan() + self.hitung_pajak()

    # ----- pola Observer -----
    def tambah_pengamat(self, pengamat: PengamatPesanan):
        self._daftar_pengamat.append(pengamat)

    def ubah_status(self, status_baru: str):
        """Mengubah status lalu memberi tahu SEMUA pengamat."""
        if status_baru not in STATUS_VALID:
            raise ValueError(f"Status tidak dikenal: {status_baru}")
        self._status = status_baru
        for pengamat in self._daftar_pengamat:
            pengamat.perbarui(self)

    def bayar(self, pembayaran: Pembayaran):
        """Membayar pesanan. Melempar KedaiError jika gagal."""
        if self._status != "BARU":  # sudah dibayar (LUNAS atau sesudahnya)
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
        poin = total // 10000
        if poin > 0:
            self._pelanggan.tambah_poin(poin)
        print(f"  Status       : LUNAS (+{poin} poin)")
        self.ubah_status("LUNAS")  # pengamat ikut diberi tahu
