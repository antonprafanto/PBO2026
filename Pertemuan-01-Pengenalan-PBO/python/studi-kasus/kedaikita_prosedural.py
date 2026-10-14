"""
KedaiKita - versi PROSEDURAL (tanpa kelas)
Pertemuan 01 - Pengenalan PBO

Program ini menyimpan data menu dalam TIGA list terpisah.
Menu ke-0 ada di indeks 0 pada ketiga list, menu ke-1 di indeks 1, dan seterusnya.
Cara ini terlihat sederhana, tetapi mudah sekali rusak. Perhatikan bagian akhir output!

Cara menjalankan:
    python kedaikita_prosedural.py
"""

# Data menu dipisah ke tiga list. Indeks yang sama = menu yang sama.
nama_menu = ["Kopi Susu Gula Aren", "Nasi Goreng Kampung", "Es Teh Manis"]
harga_menu = [18000, 25000, 8000]
stok_menu = [20, 15, 30]


def tampilkan_menu():
    """Mencetak semua menu beserta harga dan stoknya."""
    print("=== DAFTAR MENU KEDAIKITA ===")
    for i in range(len(nama_menu)):
        print(f"{i + 1}. {nama_menu[i]} - Rp{harga_menu[i]} (stok {stok_menu[i]})")


def hitung_total(daftar_pesanan):
    """Menghitung total harga sekaligus mengurangi stok.

    daftar_pesanan berisi pasangan (indeks_menu, jumlah).
    """
    total = 0
    for indeks, jumlah in daftar_pesanan:
        total = total + harga_menu[indeks] * jumlah
        stok_menu[indeks] = stok_menu[indeks] - jumlah
    return total


def main():
    tampilkan_menu()
    print()

    # Budi memesan 2 Kopi Susu Gula Aren (indeks 0) dan 1 Es Teh Manis (indeks 2)
    pesanan_budi = [(0, 2), (2, 1)]
    total = hitung_total(pesanan_budi)
    print("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis")
    print(f"Total bayar : Rp{total}")
    print()

    # Pemilik kedai ingin daftar menu tampil urut abjad.
    # Ia hanya mengurutkan list nama... dan lupa bahwa harga & stok ada di list lain!
    print("Mengurutkan nama menu sesuai abjad...")
    nama_menu.sort()
    tampilkan_menu()
    print()
    print("Lho? Es Teh Manis jadi Rp18000 dan Nasi Goreng Kampung jadi Rp8000!")
    print("Data satu menu tercerai-berai di tiga list, jadi mudah tertukar.")


if __name__ == "__main__":
    main()
