"""
Contoh 05 - Mengurutkan dengan key dan lambda
Pertemuan 12 - Koleksi dan Generics

Satu daftar produk bisa diurutkan dengan banyak cara, seperti tombol
"Termurah", "Terlaris", dan "Rating" di toko online.
- sorted(daftar, key=f)            -> list BARU yang sudah urut menurut f
- key=lambda p: p.terjual          -> lambda = fungsi kecil tanpa nama
- reverse=True                     -> urutan dibalik (terbesar dulu)
- key=lambda p: (-p.rating, p.harga) -> beberapa kriteria sekaligus

Cara menjalankan:
    python contoh05_sorting_key.py
"""


def rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Produk:
    """Produk di toko online kampus."""

    def __init__(self, nama: str, harga: int, rating: int, terjual: int):
        self._nama = nama
        self._harga = harga
        self._rating = rating
        self._terjual = terjual

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def harga(self) -> int:
        return self._harga

    @property
    def rating(self) -> int:
        return self._rating

    @property
    def terjual(self) -> int:
        return self._terjual

    def __str__(self) -> str:
        return (f"{self._nama:<20}{rupiah(self._harga):>11}"
                f"  rating {self._rating}  terjual {self._terjual}")


def tampilkan(judul: str, daftar: list[Produk]):
    print(f"=== {judul} ===")
    for produk in daftar:
        print(produk)
    print()


def ambil_harga(produk: Produk) -> int:  # [1] fungsi biasa sebagai kunci
    return produk.harga


def main():
    daftar = [
        Produk("Flashdisk 64GB", 85000, 5, 120),
        Produk("Mouse Wireless", 75000, 4, 340),
        Produk("Kabel Data USB-C", 25000, 4, 520),
        Produk("Headset Gaming", 150000, 5, 95),
        Produk("Powerbank 10000mAh", 125000, 4, 210),
    ]
    tampilkan("URUTAN ASLI", daftar)
    tampilkan("TERMURAH", sorted(daftar, key=ambil_harga))  # [2] tanpa tanda ()
    terlaris = sorted(daftar, key=lambda p: p.terjual, reverse=True)  # [3] lambda
    tampilkan("TERLARIS", terlaris)
    rating = sorted(daftar, key=lambda p: (-p.rating, p.harga))  # [4] dua kriteria
    tampilkan("RATING TERTINGGI, LALU TERMURAH", rating)

    print("=== LAIN-LAIN ===")
    urut_nama = sorted(daftar, key=lambda p: p.nama)  # [5]
    print(f"Nama A-Z      : {', '.join([p.nama for p in urut_nama])}")
    print(f"Paling murah  : {min(daftar, key=lambda p: p.harga).nama}")  # [6]
    print(f"Paling mahal  : {max(daftar, key=lambda p: p.harga).nama}")
    print(f"Urutan asli tetap, pertama: {daftar[0].nama}")  # [7]
    rating_5 = [p.nama for p in daftar if p.rating == 5]  # [8] bonus
    print(f"Rating 5      : {', '.join(rating_5)}")


if __name__ == "__main__":
    main()
