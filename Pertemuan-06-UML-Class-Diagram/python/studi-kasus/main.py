"""
KedaiKita - Pertemuan 06: UML Class Diagram

Kode di pertemuan ini SAMA PERSIS dengan Pertemuan 05. Tugas kita kali ini
adalah membaca kode ini lalu menggambarkannya sebagai class diagram UML,
dan sebaliknya: memastikan setiap kotak & garis di diagram ada wujudnya di kode.

Daftar file:
    utilitas.py  -> format_rupiah()
    menu.py      -> Menu
    pelanggan.py -> Pelanggan
    pesanan.py   -> ItemPesanan, Pesanan
    kedai.py     -> Kedai
    main.py      -> program utama (file ini)

Cara menjalankan (dari dalam folder studi-kasus):
    python main.py
"""

from kedai import Kedai
from menu import Menu
from pelanggan import Pelanggan


def siapkan_kedai() -> Kedai:
    """Membuat kedai beserta lima menu awalnya."""
    kedai = Kedai("KedaiKita")
    kedai.tambah_menu(Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20))
    kedai.tambah_menu(Menu("M02", "Es Teh Manis", 8000, "Minuman", 30))
    kedai.tambah_menu(Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15))
    kedai.tambah_menu(Menu("M04", "Mie Goreng Jawa", 23000, "Makanan", 10))
    kedai.tambah_menu(Menu("M05", "Pisang Goreng Keju", 15000, "Makanan", 12))
    return kedai


def main():
    kedai = siapkan_kedai()
    kedai.tampilkan_menu()
    print(f"Jumlah menu: {kedai.jumlah_menu()}")
    print()

    budi = Pelanggan("Budi Santoso", "081234567890")
    siti = Pelanggan("Siti Aminah", "082198765432")

    # Pesanan pertama: Budi
    pesanan_budi = kedai.buat_pesanan(budi)
    pesanan_budi.tambah_item(kedai.cari_menu("M01"), 2)
    pesanan_budi.tambah_item(kedai.cari_menu("M03"), 1)
    pesanan_budi.cetak_struk()
    print()

    # Pesanan kedua: Siti (salah satu item gagal karena stok kurang)
    pesanan_siti = kedai.buat_pesanan(siti)
    pesanan_siti.tambah_item(kedai.cari_menu("M02"), 2)
    pesanan_siti.tambah_item(kedai.cari_menu("M05"), 1)
    try:
        pesanan_siti.tambah_item(kedai.cari_menu("M04"), 20)
    except ValueError as e:
        print(f"Gagal menambah item: {e}")
    pesanan_siti.cetak_struk()
    print()

    print("=== MENCARI MENU ===")
    for kode in ["M02", "M99"]:
        menu = kedai.cari_menu(kode)
        if menu is None:
            print(f"Cari {kode}: tidak ditemukan")
        else:
            print(f"Cari {kode}: {menu}")
    print()

    print("=== SETELAH TRANSAKSI ===")
    kedai.tampilkan_menu()
    print(f"Jumlah pesanan tercatat: {kedai.jumlah_pesanan()}")


if __name__ == "__main__":
    main()
