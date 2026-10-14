"""
KedaiKita - Pertemuan 07: Pewarisan (Inheritance)

Yang baru dibanding Pertemuan 05/06:
- menu.py kini berisi kelas induk Menu dan dua kelas anak: Makanan dan Minuman.
- Semua menu dibuat sebagai Makanan atau Minuman.
- Kelas Pesanan, ItemPesanan, Kedai, dan Pelanggan TIDAK diubah sama sekali,
  tetapi tetap bisa bekerja dengan Makanan dan Minuman. Itulah kekuatan pewarisan.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from kedai import Kedai
from menu import Makanan, Menu, Minuman
from pelanggan import Pelanggan
from utilitas import format_rupiah


def siapkan_kedai() -> Kedai:
    """Membuat kedai beserta lima menu awalnya."""
    kedai = Kedai("KedaiKita")
    kedai.tambah_menu(Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, True))
    kedai.tambah_menu(Minuman("M02", "Es Teh Manis", 8000, 30, True))
    kedai.tambah_menu(Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2))
    kedai.tambah_menu(Makanan("M04", "Mie Goreng Jawa", 23000, 10, 1))
    kedai.tambah_menu(Makanan("M05", "Pisang Goreng Keju", 15000, 12, 0))
    return kedai


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    kedai = siapkan_kedai()
    kedai.tampilkan_menu()
    print()

    print("=== CEK PEWARISAN ===")
    kopi = kedai.cari_menu("M01")
    nasi = kedai.cari_menu("M03")
    print(f"{kopi.nama} termasuk Minuman? {ya_tidak(isinstance(kopi, Minuman))}")
    print(f"{kopi.nama} termasuk Menu? {ya_tidak(isinstance(kopi, Menu))}")
    print(f"{nasi.nama} termasuk Minuman? {ya_tidak(isinstance(nasi, Minuman))}")
    print(f"Kategori {nasi.nama}: {nasi.kategori}")
    harga_promo = format_rupiah(kopi.harga_setelah_diskon(10))
    print(f"Diskon 10% untuk {kopi.nama} (method warisan Menu): {harga_promo}")
    print()

    print("=== MENAMBAH MENU BARU ===")
    kopi_tubruk = Minuman("M06", "Kopi Tubruk", 12000, 25, False)
    kedai.tambah_menu(kopi_tubruk)
    print(f"Ditambahkan: {kopi_tubruk}")
    try:
        Makanan("M07", "Seblak Super Pedas", 20000, 10, 9)
    except ValueError as e:
        print(f"Gagal menambah menu: {e}")
    print()

    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")

    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"), 1)
    pesanan_budi.cetak_struk()
    print()

    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M06"), 1)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"), 2)
    pesanan_siti.cetak_struk()
    print()

    print("=== SETELAH TRANSAKSI ===")
    kedai.tampilkan_menu()
    print(f"Jumlah pesanan tercatat: {kedai.jumlah_pesanan()}")


if __name__ == "__main__":
    main()
