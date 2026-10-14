"""
Solusi Latihan 02 - Inventaris Sekretariat Himpunan
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Stok disimpan dalam dict: nama barang -> jumlah. dict menjaga urutan
  barang sesuai urutan saat pertama kali didaftarkan.
- tambah(): barang baru otomatis terdaftar (mulai dari 0 lewat get).
- ambil(): melempar ValueError jika barang tidak terdaftar atau stok kurang
  (materi exception Pertemuan 11), sehingga pemanggil bisa menangkapnya.
- barang_habis(): list barang yang stoknya 0 (list comprehension).

Cara menjalankan:
    python latihan02_inventaris.py
"""


class Inventaris:
    """Catatan stok barang: nama barang -> jumlah."""

    def __init__(self):
        self._stok: dict[str, int] = {}

    def tambah(self, nama: str, jumlah: int):
        self._stok[nama] = self._stok.get(nama, 0) + jumlah

    def ambil(self, nama: str, jumlah: int):
        if nama not in self._stok:
            raise ValueError("barang tidak terdaftar")
        if jumlah > self._stok[nama]:
            raise ValueError(f"stok hanya {self._stok[nama]}")
        self._stok[nama] -= jumlah

    def cek(self, nama: str) -> int:
        return self._stok.get(nama, 0)

    def jumlah_jenis(self) -> int:
        return len(self._stok)

    def barang_habis(self) -> list[str]:
        return [nama for nama, jumlah in self._stok.items() if jumlah == 0]

    def tampilkan(self):
        for nama, jumlah in self._stok.items():
            print(f"  {nama:<18}{jumlah:>4}")


def ambil_dan_lapor(inventaris: Inventaris, nama: str, jumlah: int):
    try:
        inventaris.ambil(nama, jumlah)
        print(f"Ambil {nama} {jumlah} -> sisa {inventaris.cek(nama)}")
    except ValueError as e:
        print(f"Ambil {nama} {jumlah} -> gagal: {e}")


def main():
    inventaris = Inventaris()
    inventaris.tambah("spidol", 12)
    inventaris.tambah("kertas HVS (rim)", 5)
    inventaris.tambah("lakban", 3)
    print("=== INVENTARIS AWAL ===")
    inventaris.tampilkan()

    print()
    print("=== TRANSAKSI ===")
    inventaris.tambah("spidol", 6)
    print(f"Tambah spidol 6 -> stok {inventaris.cek('spidol')}")
    ambil_dan_lapor(inventaris, "lakban", 3)
    ambil_dan_lapor(inventaris, "kertas HVS (rim)", 10)
    ambil_dan_lapor(inventaris, "stapler", 1)
    inventaris.tambah("stapler", 2)
    print(f"Tambah stapler 2 -> stok {inventaris.cek('stapler')}")

    print()
    print("=== INVENTARIS AKHIR ===")
    inventaris.tampilkan()
    print(f"Jumlah jenis barang: {inventaris.jumlah_jenis()}")
    print(f"Barang habis       : {', '.join(inventaris.barang_habis())}")


if __name__ == "__main__":
    main()
