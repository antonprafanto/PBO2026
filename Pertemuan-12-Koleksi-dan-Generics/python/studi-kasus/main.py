"""
KedaiKita - Pertemuan 12: Koleksi dan Generics

Yang baru dibanding Pertemuan 11:
- Kedai menyimpan menu di dict (kode -> Menu) dan bisa memfilter,
  mengurutkan, serta mengambil kategori unik (set).
- Menu punya __eq__, __hash__, dan __lt__ (kesamaan dan urutan alami).
- pasangan.py: kelas generik Pasangan[A, B].
- laporan.py: LaporanPenjualan yang merangkum penjualan hari ini.

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from kedai import Kedai
from laporan import LaporanPenjualan
from menu import Makanan, Minuman
from pasangan import Pasangan
from pelanggan import Pelanggan
from pembayaran import (Pembayaran, PembayaranKartu, PembayaranQRIS,
                        PembayaranTunai)
from pengecualian import KedaiError
from pesanan import Pesanan
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


def transaksi(kedai: Kedai, pelanggan: Pelanggan,
              daftar_beli: list[Pasangan[str, int]],
              pembayaran: Pembayaran) -> Pesanan:
    """Membuat pesanan, mengisi item (kode, jumlah), lalu membayarnya."""
    pesanan = kedai.buat_pesanan(pelanggan)
    try:
        for beli in daftar_beli:
            pesanan.tambah_item(kedai.cari_menu(beli.pertama), beli.kedua)
        pesanan.bayar(pembayaran)
    except KedaiError as e:
        print(f"  [GAGAL] {e}")
    return pesanan


def main():
    kedai = siapkan_kedai()
    kedai.cetak()
    print()

    print("=== KATEGORI UNIK ===")
    print(", ".join(kedai.daftar_kategori()))
    print()

    print("=== FILTER: MINUMAN SAJA ===")
    for menu in kedai.menu_berdasarkan_kategori("Minuman"):
        print(menu)
    print()

    print("=== URUT HARGA TERMURAH (urutan alami) ===")
    for menu in sorted(kedai.semua_menu()):
        print(f"{format_rupiah(menu.harga):>10}  {menu.nama}")
    print()

    print("=== URUT NAMA A-Z (kunci pengurutan) ===")
    for menu in sorted(kedai.semua_menu(), key=lambda m: m.nama):
        print(f"{menu.kode}  {menu.nama}")
    print()

    print("=== KODE GANDA DITOLAK ===")
    try:
        kedai.tambah_menu(Minuman("M01", "Kopi Hitam", 10000, 5))
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Jumlah menu tetap {kedai.jumlah_menu()}")
    print()

    print("=== KESAMAAN OBJEK ===")
    kopi_a = kedai.cari_menu("M01")
    kopi_b = Minuman("M01", "Kopi Susu Gula Aren", 18000, 20)
    print(f"Sama isinya (kode sama)? {ya_tidak(kopi_a == kopi_b)}")
    print(f"Objek yang sama persis? {ya_tidak(kopi_a is kopi_b)}")
    print()

    print("=== TRANSAKSI HARI INI ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")
    rina = Pelanggan("Rina Marlina", "085312345678")
    andi = Pelanggan("Andi Wijaya", "087711223344")
    transaksi(kedai, budi, [Pasangan("M01", 2), Pasangan("M03", 1)],
              PembayaranTunai(100000))
    transaksi(kedai, siti, [Pasangan("M02", 2), Pasangan("M05", 1)],
              PembayaranKartu("BNI"))
    transaksi(kedai, rina, [Pasangan("M01", 1), Pasangan("M04", 1)],
              PembayaranQRIS(100000))
    transaksi(kedai, budi, [Pasangan("M01", 1), Pasangan("M02", 2)],
              PembayaranTunai(50000))
    transaksi(kedai, andi, [Pasangan("M03", 1)], PembayaranQRIS(10000))
    print()

    print(f"Pesanan tercatat: {kedai.jumlah_pesanan()}")
    laporan = LaporanPenjualan(kedai.riwayat_pesanan())
    laporan.cetak()


if __name__ == "__main__":
    main()
