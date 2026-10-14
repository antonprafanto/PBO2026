"""
Contoh 06 - Pengganti Overloading: Nilai Bawaan, Argumen Kata Kunci, dan *args
Pertemuan 09 - Polimorfisme

Python TIDAK punya overloading (beberapa method bernama sama dengan daftar
parameter berbeda). Jika kita menulis dua def bernama sama, def kedua
menimpa def pertama. Sebagai gantinya, Python memakai:
- nilai bawaan (default)  -> parameter boleh tidak diisi,
- argumen kata kunci      -> pilih parameter yang diisi lewat namanya,
- *args                   -> jumlah argumen bebas.

Hasilnya: SATU method yang bisa dipanggil dengan banyak cara.
Bandingkan dengan Contoh06Overloading.java (output-nya sama persis).

Cara menjalankan:
    python contoh06_pengganti_overloading.py
"""


class Buku:
    """Data sebuah buku."""

    def __init__(self, judul: str, penulis: str, tahun: int):
        self._judul = judul
        self._penulis = penulis
        self._tahun = tahun

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def tahun(self) -> int:
        return self._tahun

    def __str__(self) -> str:
        return f"{self._judul} ({self._tahun})"


class Perpustakaan:
    """Perpustakaan sederhana yang bisa menyimpan dan mencari buku."""

    def __init__(self, nama: str = "Perpustakaan Kampus"):  # [1] nilai bawaan
        self._nama = nama
        self._koleksi: list[Buku] = []
        print(f"{self._nama} dibuka")

    def tambah_buku(self, *daftar_buku: Buku):  # [2] *args: berapa pun jumlahnya
        for buku in daftar_buku:  # daftar_buku berupa tuple berisi semua argumen
            self._koleksi.append(buku)
        print(f"{self._nama}: {len(daftar_buku)} buku ditambahkan")

    def cari(self, kata_kunci: str = "", tahun: int = 0) -> list[Buku]:  # [3]
        """Cari berdasarkan judul, tahun, atau keduanya (tahun 0 = bebas)."""
        hasil = []
        for buku in self._koleksi:
            cocok_judul = kata_kunci in buku.judul  # teks kosong selalu cocok
            cocok_tahun = tahun == 0 or buku.tahun == tahun
            if cocok_judul and cocok_tahun:
                hasil.append(buku)
        return hasil


def tampilkan(label: str, hasil: list[Buku]):
    teks_buku = []
    for buku in hasil:
        teks_buku.append(str(buku))
    if not teks_buku:
        teks_buku.append("(tidak ada)")
    print(f"{label:<28}: {', '.join(teks_buku)}")


def main():
    print("=== KONSTRUKTOR DENGAN NILAI BAWAAN ===")
    pusat = Perpustakaan()  # [4] nama tidak diisi -> nilai bawaan dipakai
    pojok = Perpustakaan("Pojok Baca Informatika")

    print()
    print("=== SATU METHOD, JUMLAH ARGUMEN BEBAS ===")
    pusat.tambah_buku(Buku("Laskar Pelangi", "Andrea Hirata", 2005))  # [5] 1 buku
    pusat.tambah_buku(
        Buku("Sang Pemimpi", "Andrea Hirata", 2006),
        Buku("Bumi Manusia", "Pramoedya Ananta Toer", 1980),
        Buku("Negeri 5 Menara", "Ahmad Fuadi", 2009),
    )  # 3 buku sekaligus
    pojok.tambah_buku()  # 0 buku pun boleh

    print()
    print("=== SATU NAMA METHOD, BANYAK CARA CARI ===")
    tampilkan("Judul memuat 'Pe'", pusat.cari("Pe"))  # [6]
    tampilkan("Tahun 1980", pusat.cari(tahun=1980))  # [7] argumen kata kunci
    tampilkan("Judul memuat 'a', tahun 2006", pusat.cari("a", 2006))  # [8]
    tampilkan("Judul memuat 'Kancil'", pusat.cari("Kancil"))


if __name__ == "__main__":
    main()
