"""
Solusi Latihan 05 - KedaiKita: Porsi per Menu, Menu Tak Laku, Rata-rata Porsi
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Daftar menu disimpan di dict kode -> nama (urutan sesuai daftar menu).
- Setiap pesanan lunas = list ItemBeli(kode, jumlah). Datanya sama dengan
  4 pesanan lunas di studi kasus, ditambah dua menu baru (M06, M07).
- porsi_per_menu(): semua kode diisi 0 dulu (dict comprehension), supaya
  menu yang tidak pernah dipesan tetap muncul dengan angka 0.
- menu_tak_laku(): selisih himpunan = semua kode - kode yang pernah terjual.
- Rata-rata porsi = total porsi / jumlah pesanan. Agar tetap bilangan bulat,
  hitung "kali 100" dulu: 11 * 100 // 4 = 275, lalu dicetak sebagai 2.75.

Cara menjalankan:
    python latihan05_menu_tak_laku.py
"""


class ItemBeli:
    """Satu baris pesanan: kode menu dan jumlah porsi."""

    def __init__(self, kode: str, jumlah: int):
        self._kode = kode
        self._jumlah = jumlah

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def jumlah(self) -> int:
        return self._jumlah


class AnalisisPenjualan:
    """Analisis tambahan untuk laporan penjualan KedaiKita."""

    def __init__(self, daftar_menu: dict[str, str],
                 pesanan_lunas: list[list[ItemBeli]]):
        self._daftar_menu = daftar_menu
        self._pesanan_lunas = pesanan_lunas

    def porsi_per_menu(self) -> dict[str, int]:
        hasil = {kode: 0 for kode in self._daftar_menu}  # semua mulai dari 0
        for pesanan in self._pesanan_lunas:
            for item in pesanan:
                hasil[item.kode] += item.jumlah
        return hasil

    def menu_tak_laku(self) -> list[str]:
        terjual: set[str] = set()
        for pesanan in self._pesanan_lunas:
            for item in pesanan:
                terjual.add(item.kode)
        return sorted(set(self._daftar_menu) - terjual)

    def total_porsi(self) -> int:
        return sum(self.porsi_per_menu().values())

    def rata_rata_porsi_x100(self) -> int:
        return self.total_porsi() * 100 // len(self._pesanan_lunas)


def main():
    daftar_menu = {
        "M01": "Kopi Susu Gula Aren",
        "M02": "Es Teh Manis",
        "M03": "Nasi Goreng Kampung",
        "M04": "Mie Goreng Jawa",
        "M05": "Pisang Goreng Keju",
        "M06": "Teh Tarik",
        "M07": "Roti Bakar Cokelat",
    }
    pesanan_lunas = [
        [ItemBeli("M01", 2), ItemBeli("M03", 1)],  # P001 Budi
        [ItemBeli("M02", 2), ItemBeli("M05", 1)],  # P002 Siti
        [ItemBeli("M01", 1), ItemBeli("M04", 1)],  # P003 Rina
        [ItemBeli("M01", 1), ItemBeli("M02", 2)],  # P004 Budi
    ]
    analisis = AnalisisPenjualan(daftar_menu, pesanan_lunas)

    print("=== PORSI TERJUAL PER MENU ===")
    for kode, porsi in analisis.porsi_per_menu().items():
        print(f"{kode} {daftar_menu[kode]:<24}{porsi:>3}")

    print()
    print("=== RINGKASAN ===")
    rata = analisis.rata_rata_porsi_x100()
    print(f"Pesanan lunas  : {len(pesanan_lunas)}")
    print(f"Total porsi    : {analisis.total_porsi()}")
    print(f"Rata-rata porsi: {rata // 100}.{rata % 100:02d} porsi per pesanan")
    nama_tak_laku = [daftar_menu[kode] for kode in analisis.menu_tak_laku()]
    print(f"Menu tak laku  : {', '.join(nama_tak_laku)}")


if __name__ == "__main__":
    main()
