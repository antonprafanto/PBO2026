"""
Solusi Latihan 05 - KedaiKita: Membuat Menu dari Teks
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- Salin fungsi format_rupiah() dan kelas Menu dari studi kasus.
- Tambahkan class method dari_teks(teks) sebagai konstruktor alternatif.
  teks.split(";") memecah "M09;Teh Tarik;12000;Minuman;10" menjadi list
  berisi 5 bagian. Harga dan stok diubah ke bilangan bulat dengan int().
- Jika teks hanya berisi 4 bagian (tanpa stok), panggil konstruktor tanpa
  stok sehingga nilai bawaan stok=0 yang dipakai.
- cls(...) di dalam class method sama artinya dengan Menu(...), jadi
  penghitung jumlah_menu tetap bertambah.

Cara menjalankan:
    python latihan05_menu_dari_teks.py
"""


def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Menu KedaiKita yang kini bisa dibuat dari sebaris teks."""

    jumlah_menu = 0

    def __init__(self, kode, nama, harga, kategori, stok=0):
        self.kode = kode
        self.nama = nama
        self.harga = harga
        self.kategori = kategori
        self.stok = stok
        Menu.jumlah_menu += 1

    @classmethod
    def dari_teks(cls, teks):
        """Konstruktor alternatif dari teks 'kode;nama;harga;kategori;stok'."""
        bagian = teks.split(";")
        kode, nama, harga, kategori = bagian[0], bagian[1], int(bagian[2]), bagian[3]
        if len(bagian) == 5:
            return cls(kode, nama, harga, kategori, int(bagian[4]))
        return cls(kode, nama, harga, kategori)  # stok memakai nilai bawaan 0

    def __str__(self):
        return (f"[{self.kode}] {self.nama} ({self.kategori}) - "
                f"{format_rupiah(self.harga)} | stok {self.stok}")


def main():
    data = [
        "M09;Teh Tarik;12000;Minuman;10",
        "M10;Roti Bakar Cokelat;15000;Makanan",
        "M11;Es Jeruk;10000;Minuman;25",
    ]
    print("=== MENU DARI TEKS ===")
    for baris in data:
        menu = Menu.dari_teks(baris)
        print(baris)
        print(f"  -> {menu}")
    print(f"Jumlah menu terdaftar: {Menu.jumlah_menu}")


if __name__ == "__main__":
    main()
