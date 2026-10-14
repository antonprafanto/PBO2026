"""
KedaiKita - Pertemuan 02: Kelas dan Objek

Versi pertama KedaiKita yang benar-benar memakai kelas.
- Kelas Menu adalah cetak biru (blueprint).
- kopi, es_teh, dan nasi_goreng adalah objek (hasil cetakan) dari kelas Menu.

Cara menjalankan:
    python kedaikita.py
"""


class Menu:
    """Cetak biru untuk setiap menu di KedaiKita."""

    def __init__(self, nama, harga):  # [1] konstruktor: dipanggil saat objek dibuat
        self.nama = nama  # [2] atribut milik objek
        self.harga = harga

    def tampilkan_info(self):  # [3] method: perilaku objek
        print(f"{self.nama} - Rp{self.harga}")

    def hitung_total(self, jumlah):  # [4] method yang mengembalikan nilai
        return self.harga * jumlah


def main():
    print("=== MENU KEDAIKITA ===")
    kopi = Menu("Kopi Susu Gula Aren", 18000)  # [5] membuat objek
    es_teh = Menu("Es Teh Manis", 8000)
    nasi_goreng = Menu("Nasi Goreng Kampung", 25000)

    kopi.tampilkan_info()  # [6] memanggil method milik objek
    es_teh.tampilkan_info()
    nasi_goreng.tampilkan_info()

    print()
    print("=== PESANAN BUDI ===")
    total_kopi = kopi.hitung_total(2)
    total_nasi = nasi_goreng.hitung_total(1)
    print(f"2 x {kopi.nama} = Rp{total_kopi}")  # [7] membaca atribut objek
    print(f"1 x {nasi_goreng.nama} = Rp{total_nasi}")
    print(f"Total bayar: Rp{total_kopi + total_nasi}")

    print()
    print("=== HARGA ES TEH NAIK ===")
    es_teh.harga = 10000  # [8] mengubah atribut satu objek
    es_teh.tampilkan_info()
    kopi.tampilkan_info()  # objek lain tidak ikut berubah


if __name__ == "__main__":
    main()
