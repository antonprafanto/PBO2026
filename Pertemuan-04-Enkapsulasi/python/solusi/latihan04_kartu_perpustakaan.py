"""
Solusi Latihan 04 - Kartu Perpustakaan
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- Penghitung anggota disimpan di atribut KELAS internal _jumlah_anggota.
  Penghitung naik hanya SETELAH nama dinyatakan valid, sehingga nomor
  anggota tidak pernah terlewat. Dibaca lewat @classmethod jumlah_anggota().
- nomor, nama, dan dipinjam bersifat read-only (property tanpa setter).
- Jumlah buku yang dipinjam hanya berubah lewat pinjam() dan kembalikan(),
  dua "pintu resmi" yang menjaga aturan batas pinjam.
- Versi sederhana: kita hanya menghitung JUMLAH buku, belum mencatat judulnya
  satu per satu (daftar objek dibahas di Pertemuan 05).

Cara menjalankan:
    python latihan04_kartu_perpustakaan.py
"""


class KartuPerpustakaan:
    """Kartu anggota perpustakaan kampus."""

    BATAS_PINJAM = 3
    _jumlah_anggota = 0  # atribut kelas internal

    def __init__(self, nama):
        if nama.strip() == "":
            raise ValueError("Nama anggota tidak boleh kosong")
        KartuPerpustakaan._jumlah_anggota += 1  # naik hanya jika nama valid
        self._nomor = f"AGT-{KartuPerpustakaan._jumlah_anggota:03d}"
        self._nama = nama
        self._dipinjam = 0

    @classmethod
    def jumlah_anggota(cls):
        return cls._jumlah_anggota

    @property
    def nomor(self):
        return self._nomor

    @property
    def nama(self):
        return self._nama

    @property
    def dipinjam(self):
        return self._dipinjam

    def pinjam(self, judul):
        if self._dipinjam >= KartuPerpustakaan.BATAS_PINJAM:
            raise ValueError(f"{self._nama} sudah mencapai batas "
                             f"{KartuPerpustakaan.BATAS_PINJAM} buku")
        self._dipinjam += 1
        print(f"{self._nama} meminjam '{judul}' "
              f"({self._dipinjam}/{KartuPerpustakaan.BATAS_PINJAM})")

    def kembalikan(self, judul):
        if self._dipinjam == 0:
            raise ValueError(f"{self._nama} tidak sedang meminjam buku")
        self._dipinjam -= 1
        print(f"{self._nama} mengembalikan '{judul}' "
              f"({self._dipinjam}/{KartuPerpustakaan.BATAS_PINJAM})")


def main():
    print("=== PENDAFTARAN ANGGOTA ===")
    ayu = KartuPerpustakaan("Ayu Lestari")
    print(f"{ayu.nomor} {ayu.nama}")
    bima = KartuPerpustakaan("Bima Saputra")
    print(f"{bima.nomor} {bima.nama}")
    try:
        KartuPerpustakaan("   ")
    except ValueError as e:
        print(f"Ditolak: {e}")
    citra = KartuPerpustakaan("Citra Dewi")
    print(f"{citra.nomor} {citra.nama}")
    print(f"Jumlah anggota: {KartuPerpustakaan.jumlah_anggota()}")

    print()
    print("=== PEMINJAMAN BUKU ===")
    ayu.pinjam("Laskar Pelangi")
    ayu.pinjam("Bumi Manusia")
    ayu.pinjam("Negeri 5 Menara")
    try:
        ayu.pinjam("Sang Pemimpi")
    except ValueError as e:
        print(f"Ditolak: {e}")
    ayu.kembalikan("Bumi Manusia")
    ayu.pinjam("Sang Pemimpi")
    try:
        bima.kembalikan("Laskar Pelangi")
    except ValueError as e:
        print(f"Ditolak: {e}")


if __name__ == "__main__":
    main()
