"""
Solusi Latihan 06 - KedaiKita: Mengurutkan Tanpa Tertukar (cara prosedural)
Pertemuan 01 - Pengenalan PBO

Ide penyelesaian:
- Pakai bubble sort seperti contoh 06: bandingkan dua menu yang bertetangga,
  lalu tukar jika nama di kiri lebih belakang abjadnya daripada nama di kanan.
- KUNCINYA: setiap kali menukar nama, tukar juga harga dan stok di posisi
  yang sama. Ketiga list harus selalu bergerak bersama.
- Bandingkan dengan versi OOP (studi-kasus/kedaikita_oop.py): di sana cukup
  satu baris sort, karena data satu menu sudah terbungkus dalam satu objek.

Cara menjalankan:
    python latihan06_urutkan_menu.py
"""

# Data menu sama dengan studi kasus: tiga list paralel.
nama_menu = ["Kopi Susu Gula Aren", "Nasi Goreng Kampung", "Es Teh Manis"]
harga_menu = [18000, 25000, 8000]
stok_menu = [20, 15, 30]


def tampilkan_menu():
    print("=== DAFTAR MENU KEDAIKITA ===")
    for i in range(len(nama_menu)):
        print(f"{i + 1}. {nama_menu[i]} - Rp{harga_menu[i]} (stok {stok_menu[i]})")


def hitung_total(daftar_pesanan):
    """Sama dengan studi kasus: daftar_pesanan berisi pasangan (indeks, jumlah)."""
    total = 0
    for indeks, jumlah in daftar_pesanan:
        total = total + harga_menu[indeks] * jumlah
        stok_menu[indeks] = stok_menu[indeks] - jumlah
    return total


def urutkan_menu_berdasarkan_nama():
    n = len(nama_menu)
    for putaran in range(n - 1):
        for i in range(n - 1 - putaran):
            if nama_menu[i] > nama_menu[i + 1]:  # teks dibandingkan sesuai abjad
                # tukar SEMUA data milik dua menu ini, bukan hanya namanya
                nama_menu[i], nama_menu[i + 1] = nama_menu[i + 1], nama_menu[i]
                harga_menu[i], harga_menu[i + 1] = harga_menu[i + 1], harga_menu[i]
                stok_menu[i], stok_menu[i + 1] = stok_menu[i + 1], stok_menu[i]


def main():
    tampilkan_menu()
    print()

    pesanan_budi = [(0, 2), (2, 1)]
    total = hitung_total(pesanan_budi)
    print("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis")
    print(f"Total bayar : Rp{total}")
    print()

    print("Mengurutkan menu sesuai abjad (harga dan stok ikut ditukar)...")
    urutkan_menu_berdasarkan_nama()
    tampilkan_menu()
    print()
    print("Berhasil! Harga dan stok ikut pindah bersama namanya.")
    print("Namun, jika nanti ada data baru (misalnya kategori),")
    print("kode pengurut ini harus diubah lagi agar data baru itu ikut ditukar.")


if __name__ == "__main__":
    main()
