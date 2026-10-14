"""
KedaiKita - versi BERORIENTASI OBJEK (sekilas)
Pertemuan 01 - Pengenalan PBO

Masalah yang sama seperti kedaikita_prosedural.py, tetapi kali ini setiap menu
adalah SATU OBJEK yang membawa nama, harga, dan stoknya sendiri.
Jangan khawatir bila ada sintaks yang belum kamu pahami (class, __init__, self).
Semuanya akan kita bahas pelan-pelan mulai Pertemuan 02.

Cara menjalankan:
    python kedaikita_oop.py
"""


class Menu:
    """Cetak biru untuk satu menu: punya nama, harga, dan stok."""

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def kurangi_stok(self, jumlah):
        self.stok = self.stok - jumlah


def tampilkan_menu(daftar_menu):
    print("=== DAFTAR MENU KEDAIKITA ===")
    nomor = 1
    for menu in daftar_menu:
        print(f"{nomor}. {menu.nama} - Rp{menu.harga} (stok {menu.stok})")
        nomor = nomor + 1


def main():
    kopi = Menu("Kopi Susu Gula Aren", 18000, 20)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000, 15)
    es_teh = Menu("Es Teh Manis", 8000, 30)
    daftar_menu = [kopi, nasi_goreng, es_teh]

    tampilkan_menu(daftar_menu)
    print()

    # Budi memesan 2 Kopi Susu Gula Aren dan 1 Es Teh Manis
    total = kopi.harga * 2 + es_teh.harga * 1
    kopi.kurangi_stok(2)
    es_teh.kurangi_stok(1)
    print("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis")
    print(f"Total bayar : Rp{total}")
    print()

    # Mengurutkan daftar menu berdasarkan nama.
    # Yang dipindah adalah OBJEK-nya, jadi harga & stok ikut terbawa.
    print("Mengurutkan menu sesuai abjad...")
    daftar_menu.sort(key=lambda menu: menu.nama)
    tampilkan_menu(daftar_menu)
    print()
    print("Aman! Setiap menu membawa datanya sendiri, jadi tidak ada yang tertukar.")


if __name__ == "__main__":
    main()
