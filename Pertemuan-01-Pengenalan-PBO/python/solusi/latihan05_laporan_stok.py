"""
Solusi Latihan 05 - KedaiKita: Laporan Stok (versi prosedural)
Pertemuan 01 - Pengenalan PBO

Ide penyelesaian:
- Data menu tetap disimpan di tiga list paralel, seperti studi kasus.
- cari_indeks_termurah() mengembalikan INDEKS menu termurah (bukan namanya),
  sehingga pemanggil bisa membaca nama dan harga dari list yang berbeda.
- hitung_nilai_stok() menjumlahkan harga x stok untuk setiap menu.
- tampilkan_stok_menipis(batas) mencetak menu yang stoknya di bawah batas.
  Variabel ada (bool) mencatat apakah minimal satu menu sudah tercetak.

Cara menjalankan:
    python latihan05_laporan_stok.py
"""

# Data menu: tiga list paralel. Indeks yang sama = menu yang sama.
nama_menu = [
    "Kopi Susu Gula Aren",
    "Es Teh Manis",
    "Nasi Goreng Kampung",
    "Mie Goreng Jawa",
    "Pisang Goreng Keju",
]
harga_menu = [18000, 8000, 25000, 23000, 15000]
stok_menu = [20, 30, 15, 4, 3]


def tampilkan_menu():
    print("=== DAFTAR MENU KEDAIKITA ===")
    for i in range(len(nama_menu)):
        print(f"{i + 1}. {nama_menu[i]} - Rp{harga_menu[i]} (stok {stok_menu[i]})")


def cari_indeks_termurah():
    indeks_termurah = 0
    for i in range(len(harga_menu)):
        if harga_menu[i] < harga_menu[indeks_termurah]:
            indeks_termurah = i
    return indeks_termurah


def hitung_nilai_stok():
    total = 0
    for i in range(len(harga_menu)):
        total = total + harga_menu[i] * stok_menu[i]
    return total


def tampilkan_stok_menipis(batas):
    print(f"Stok menipis (kurang dari {batas}):")
    ada = False
    for i in range(len(nama_menu)):
        if stok_menu[i] < batas:
            print(f"- {nama_menu[i]} (sisa {stok_menu[i]})")
            ada = True
    if not ada:
        print("- (tidak ada)")


def main():
    tampilkan_menu()
    print()

    print("=== LAPORAN STOK ===")
    termurah = cari_indeks_termurah()
    print(f"Menu termurah : {nama_menu[termurah]} (Rp{harga_menu[termurah]})")
    print(f"Nilai stok    : Rp{hitung_nilai_stok()}")
    tampilkan_stok_menipis(5)
    tampilkan_stok_menipis(3)


if __name__ == "__main__":
    main()
