"""
KedaiKita - Pertemuan 03: Atribut dan Method Lebih Dalam

Yang baru dibanding Pertemuan 02:
- Menu punya atribut lebih lengkap: kode, nama, harga, kategori, stok.
- Parameter stok punya nilai bawaan (default) 0.
- Atribut KELAS jumlah_menu: dimiliki bersama oleh semua objek Menu.
- Method __str__ agar objek bisa langsung dicetak dengan print().
- Method yang mengembalikan nilai: hitung_total, harga_setelah_diskon, stok_cukup.
- Fungsi bantu format_rupiah() untuk menampilkan uang dengan titik ribuan.
- Kelas baru: Pelanggan.

Cara menjalankan:
    python kedaikita.py
"""


def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Cetak biru untuk setiap menu di KedaiKita."""

    jumlah_menu = 0  # atribut KELAS: satu nilai untuk semua objek Menu

    def __init__(self, kode, nama, harga, kategori, stok=0):
        self.kode = kode  # atribut OBJEK: tiap objek punya nilainya sendiri
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.stok = stok
        Menu.jumlah_menu += 1  # setiap ada objek baru, penghitung bertambah

    def __str__(self):
        """Teks yang muncul saat objek dicetak dengan print()."""
        return (f"[{self.kode}] {self.nama} ({self.kategori}) - "
                f"{format_rupiah(self.harga)} | stok {self.stok}")

    def hitung_total(self, jumlah):
        """Total harga untuk sejumlah porsi."""
        return self.harga * jumlah

    def harga_setelah_diskon(self, persen):
        """Harga setelah dipotong diskon sekian persen."""
        potongan = self.harga * persen // 100
        return self.harga - potongan

    def stok_cukup(self, jumlah):
        """True jika stok masih cukup untuk sejumlah porsi."""
        return self.stok >= jumlah


class Pelanggan:
    """Data pelanggan KedaiKita beserta poin belanjanya."""

    def __init__(self, nama, no_hp):
        self.nama = nama
        self.no_hp = no_hp
        self.poin = 0  # setiap pelanggan baru mulai dari 0 poin

    def __str__(self):
        return f"{self.nama} ({self.no_hp}) - {self.poin} poin"

    def tambah_poin(self, jumlah):
        self.poin += jumlah


def main():
    kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
    es_teh = Menu("M02", "Es Teh Manis", 8000, "Minuman", 30)
    nasi_goreng = Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15)
    mie_goreng = Menu("M04", "Mie Goreng Jawa", 23000, "Makanan")  # stok bawaan 0

    print("=== MENU KEDAIKITA ===")
    print(kopi)
    print(es_teh)
    print(nasi_goreng)
    print(mie_goreng)
    print(f"Jumlah menu terdaftar: {Menu.jumlah_menu}")

    print()
    print("=== CEK STOK ===")
    if kopi.stok_cukup(2):
        print(f"Pesan 2 {kopi.nama}? Bisa")
    else:
        print(f"Pesan 2 {kopi.nama}? Stok tidak cukup")
    if mie_goreng.stok_cukup(1):
        print(f"Pesan 1 {mie_goreng.nama}? Bisa")
    else:
        print(f"Pesan 1 {mie_goreng.nama}? Stok tidak cukup")

    print()
    print("=== PROMO HARI INI: DISKON 10% ===")
    for menu in [kopi, nasi_goreng]:
        harga_baru = menu.harga_setelah_diskon(10)
        print(f"{menu.nama}: {format_rupiah(menu.harga)} -> "
              f"{format_rupiah(harga_baru)}")

    print()
    print("=== PELANGGAN ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    print(budi)
    belanja = kopi.hitung_total(2) + es_teh.hitung_total(1)
    poin_baru = belanja // 10000  # 1 poin untuk setiap Rp10.000
    budi.tambah_poin(poin_baru)
    print(f"Budi belanja {format_rupiah(belanja)}, dapat {poin_baru} poin")
    print(budi)


if __name__ == "__main__":
    main()
