"""
Solusi Latihan 05 - Kelas Snack untuk KedaiKita
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
- Snack adalah Menu (is-a), sama seperti Makanan dan Minuman.
- Konstruktor Snack memanggil super().__init__(...) dengan kategori "Snack",
  lalu menyimpan berat_gram (harus lebih dari 0, ditolak dengan ValueError).
- __str__ di-override: teks versi induk + " | <berat> gram".
- harga_setelah_diskon() tidak ditulis ulang: cukup diwarisi dari Menu.

Catatan: agar file ini bisa dijalankan sendiri, kelas Menu di bawah adalah
SALINAN RINGKAS dari studi-kasus/menu.py (hanya bagian yang dibutuhkan).
Di proyek KedaiKita-mu, cukup tambahkan kelas Snack ke menu.py.

Cara menjalankan:
    python latihan05_snack_kedaikita.py
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Salinan ringkas kelas induk Menu dari studi kasus."""

    def __init__(self, kode: str, nama: str, harga: int, kategori: str,
                 stok: int = 0):
        if harga <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._kode = kode
        self._nama = nama
        self._harga = harga
        self._kategori = kategori
        self._stok = stok

    @property
    def nama(self) -> str:
        return self._nama

    def harga_setelah_diskon(self, persen: int) -> int:
        potongan = self._harga * persen // 100
        return self._harga - potongan

    def __str__(self) -> str:
        return (f"[{self._kode}] {self._nama} ({self._kategori}) - "
                f"{format_rupiah(self._harga)} | stok {self._stok}")


class Snack(Menu):
    """Menu kategori snack. Tambahan: berat per porsi dalam gram."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int,
                 berat_gram: int):
        super().__init__(kode, nama, harga, "Snack", stok)  # kategori otomatis
        if berat_gram <= 0:
            raise ValueError("Berat harus lebih dari 0 gram")
        self._berat_gram = berat_gram

    @property
    def berat_gram(self) -> int:
        return self._berat_gram

    def __str__(self) -> str:
        return f"{super().__str__()} | {self._berat_gram} gram"


def main():
    keripik = Snack("M07", "Keripik Singkong Balado", 10000, 20, 150)
    amplang = Snack("M08", "Amplang Ikan Pipih", 15000, 15, 100)

    print("=== MENU BARU: SNACK ===")
    print(keripik)
    print(amplang)

    print()
    print("=== CEK PEWARISAN ===")
    jawaban = "ya" if isinstance(amplang, Menu) else "tidak"
    print(f"{amplang.nama} termasuk Menu? {jawaban}")
    harga_promo = format_rupiah(amplang.harga_setelah_diskon(10))
    print(f"Diskon 10% untuk {amplang.nama}: {harga_promo}")

    print()
    print("=== VALIDASI ===")
    try:
        Snack("M09", "Kacang Sangrai", 8000, 10, 0)
    except ValueError as e:
        print(f"Gagal menambah menu: {e}")


if __name__ == "__main__":
    main()
