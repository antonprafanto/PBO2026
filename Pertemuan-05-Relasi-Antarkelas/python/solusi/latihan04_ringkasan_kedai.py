"""
Solusi Latihan 04 - Ringkasan Penjualan KedaiKita
Pertemuan 05 - Relasi Antarkelas

Ide penyelesaian:
- Pesanan.jumlah_porsi(): jumlahkan atribut jumlah dari setiap ItemPesanan.
- Kedai.daftar_pesanan: kembalikan SALINAN list pesanan.
- Kedai.total_pendapatan(): Kedai bertanya ke setiap Pesanan lewat
  hitung_total(), dan setiap Pesanan bertanya ke ItemPesanan miliknya.

Catatan: di studi kasus, kelas-kelas ini tersebar di beberapa file. Agar
solusi ini bisa dijalankan sebagai SATU file, kelas yang dibutuhkan disalin
ke sini dalam versi ringkas (hanya bagian yang dipakai). Di proyekmu,
cukup tambahkan method baru ke pesanan.py dan kedai.py.

Cara menjalankan:
    python latihan04_ringkasan_kedai.py
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Versi ringkas kelas Menu dari studi kasus."""

    def __init__(self, kode: str, nama: str, harga: int, kategori: str,
                 stok: int = 0):
        self._kode = kode
        self._nama = nama
        self._harga = harga
        self._kategori = kategori
        self._stok = stok

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def harga(self) -> int:
        return self._harga

    def kurangi_stok(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if jumlah > self._stok:
            raise ValueError(f"Stok {self._nama} tidak cukup (sisa {self._stok})")
        self._stok -= jumlah


class Pelanggan:
    """Versi ringkas kelas Pelanggan dari studi kasus."""

    def __init__(self, nama: str, no_hp: str):
        self._nama = nama
        self._no_hp = no_hp

    @property
    def nama(self) -> str:
        return self._nama


class ItemPesanan:
    """Satu baris pesanan: menu apa dan berapa porsi."""

    def __init__(self, menu: Menu, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._menu = menu
        self._jumlah = jumlah

    @property
    def jumlah(self) -> int:
        return self._jumlah

    def hitung_subtotal(self) -> int:
        return self._menu.harga * self._jumlah


class Pesanan:
    """Pesanan milik seorang pelanggan, berisi beberapa ItemPesanan."""

    _nomor_terakhir = 0

    def __init__(self, pelanggan: Pelanggan):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"P{Pesanan._nomor_terakhir:03d}"
        self._pelanggan = pelanggan
        self._daftar_item: list[ItemPesanan] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def pelanggan(self) -> Pelanggan:
        return self._pelanggan

    def tambah_item(self, menu: Menu, jumlah: int):
        item = ItemPesanan(menu, jumlah)
        menu.kurangi_stok(jumlah)
        self._daftar_item.append(item)

    def hitung_total(self) -> int:
        total = 0
        for item in self._daftar_item:
            total += item.hitung_subtotal()
        return total

    def jumlah_porsi(self) -> int:  # BARU
        porsi = 0
        for item in self._daftar_item:
            porsi += item.jumlah
        return porsi


class Kedai:
    """Kedai yang punya daftar menu dan catatan pesanan."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_menu: list[Menu] = []
        self._daftar_pesanan: list[Pesanan] = []

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def daftar_pesanan(self) -> list[Pesanan]:  # BARU
        """Mengembalikan SALINAN list, agar catatan asli tidak diubah dari luar."""
        return list(self._daftar_pesanan)

    def tambah_menu(self, menu: Menu):
        self._daftar_menu.append(menu)

    def cari_menu(self, kode: str) -> Menu | None:
        for menu in self._daftar_menu:
            if menu.kode == kode:
                return menu
        return None

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = Pesanan(pelanggan)
        self._daftar_pesanan.append(pesanan)
        return pesanan

    def jumlah_pesanan(self) -> int:
        return len(self._daftar_pesanan)

    def total_pendapatan(self) -> int:  # BARU
        total = 0
        for pesanan in self._daftar_pesanan:
            total += pesanan.hitung_total()  # Kedai -> Pesanan -> ItemPesanan
        return total


def main():
    kedai = Kedai("KedaiKita")
    kedai.tambah_menu(Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20))
    kedai.tambah_menu(Menu("M02", "Es Teh Manis", 8000, "Minuman", 30))
    kedai.tambah_menu(Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15))
    kedai.tambah_menu(Menu("M04", "Mie Goreng Jawa", 23000, "Makanan", 10))
    kedai.tambah_menu(Menu("M05", "Pisang Goreng Keju", 15000, "Makanan", 12))
    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")

    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"), 1)
    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"), 1)

    print("=== RINGKASAN PESANAN ===")
    for pesanan in kedai.daftar_pesanan:
        total = format_rupiah(pesanan.hitung_total())
        print(f"{pesanan.nomor} - {pesanan.pelanggan.nama}: "
              f"{pesanan.jumlah_porsi()} porsi, {total}")
    print(f"Total pendapatan {kedai.nama}: "
          f"{format_rupiah(kedai.total_pendapatan())}")

    print()
    print("=== SALINAN TIDAK MERUSAK CATATAN ===")
    salinan = kedai.daftar_pesanan
    salinan.clear()
    print(f"Salinan dikosongkan, pesanan tercatat tetap {kedai.jumlah_pesanan()}")


if __name__ == "__main__":
    main()
