"""
Solusi Latihan 05 - Menambah Stok pada Menu KedaiKita
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
- Salin kelas Menu dari studi kasus, lalu tambahkan atribut stok.
- jual(jumlah): jika stok cukup, kurangi stok dan KEMBALIKAN total harga;
  jika tidak cukup, cetak pesan dan kembalikan 0.

Cara menjalankan (dari folder python/solusi; macOS/Linux: python3):
    python latihan05_stok_menu.py
"""


class Menu:
    """Menu KedaiKita yang kini punya stok."""

    def __init__(self, nama, harga, stok):
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def tampilkan_info(self):
        print(f"{self.nama} - Rp{self.harga} (stok {self.stok})")

    def jual(self, jumlah):
        if jumlah > self.stok:
            print(f"Gagal: stok {self.nama} tidak cukup (sisa {self.stok})")
            return 0
        self.stok = self.stok - jumlah
        total = self.harga * jumlah
        print(f"Terjual {jumlah} {self.nama}, total Rp{total}")
        return total


def main():
    kopi = Menu("Kopi Susu Gula Aren", 18000, 20)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000, 2)

    print("=== STOK AWAL ===")
    kopi.tampilkan_info()
    nasi_goreng.tampilkan_info()

    print()
    print("=== PENJUALAN ===")
    pendapatan = 0
    pendapatan = pendapatan + kopi.jual(2)
    pendapatan = pendapatan + nasi_goreng.jual(3)
    pendapatan = pendapatan + nasi_goreng.jual(2)
    print(f"Pendapatan: Rp{pendapatan}")

    print()
    print("=== STOK AKHIR ===")
    kopi.tampilkan_info()
    nasi_goreng.tampilkan_info()


if __name__ == "__main__":
    main()
