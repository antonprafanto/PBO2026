"""
Solusi Latihan 03 - Peminjaman Buku Perpustakaan
Pertemuan 11 - Exception Handling

Ide penyelesaian:
- Hierarki exception:
      PerpustakaanError                 (induk)
      +-- BukuSedangDipinjamError       (data: judul, peminjam)
      +-- BatasPinjamError              (data: nama, batas)
- Anggota.pinjam() memeriksa dua aturan, lalu melempar exception yang
  sesuai. Data tambahan di exception dipakai penangkap untuk memberi saran.
- Anggota.kembalikan() melempar PerpustakaanError (induknya langsung),
  karena kesalahan ini tidak butuh jenis khusus.
- Urutan except: yang spesifik di atas. coba_kembalikan() cukup menangkap
  induknya, PerpustakaanError.

Cara menjalankan:
    python latihan03_peminjaman_buku.py
"""


class PerpustakaanError(Exception):
    """Induk semua error perpustakaan."""


class BukuSedangDipinjamError(PerpustakaanError):
    """Dilempar saat buku yang diminta sedang dipinjam orang lain."""

    def __init__(self, judul: str, peminjam: str):
        super().__init__(f"Buku '{judul}' sedang dipinjam oleh {peminjam}")
        self.judul = judul
        self.peminjam = peminjam


class BatasPinjamError(PerpustakaanError):
    """Dilempar saat anggota sudah meminjam sebanyak batas maksimal."""

    def __init__(self, nama: str, batas: int):
        super().__init__(f"{nama} sudah meminjam {batas} buku (batas maksimal)")
        self.nama = nama
        self.batas = batas


class Buku:
    """Buku perpustakaan. Menyimpan nama peminjamnya (None jika tersedia)."""

    def __init__(self, judul: str):
        self._judul = judul
        self._peminjam: str | None = None

    @property
    def judul(self) -> str:
        return self._judul

    @property
    def peminjam(self) -> str | None:
        return self._peminjam

    def catat_peminjam(self, nama: str | None):
        """Mencatat nama peminjam. None berarti buku sudah kembali."""
        self._peminjam = nama


class Anggota:
    """Anggota perpustakaan dengan batas jumlah pinjaman."""

    def __init__(self, nama: str, batas: int = 2):
        self._nama = nama
        self._batas = batas
        self._pinjaman: list[Buku] = []

    @property
    def nama(self) -> str:
        return self._nama

    def pinjam(self, buku: Buku):
        if buku.peminjam is not None:
            raise BukuSedangDipinjamError(buku.judul, buku.peminjam)
        if len(self._pinjaman) >= self._batas:
            raise BatasPinjamError(self._nama, self._batas)
        buku.catat_peminjam(self._nama)  # baru dicatat setelah lolos semua aturan
        self._pinjaman.append(buku)

    def kembalikan(self, buku: Buku):
        if buku not in self._pinjaman:
            raise PerpustakaanError(f"{self._nama} tidak sedang meminjam "
                                    f"'{buku.judul}'")
        buku.catat_peminjam(None)
        self._pinjaman.remove(buku)


def coba_pinjam(anggota: Anggota, buku: Buku):
    try:
        anggota.pinjam(buku)
        print(f"{anggota.nama} meminjam '{buku.judul}'")
    except BukuSedangDipinjamError as e:
        print(f"Gagal: {e}")
        print(f"  Saran: tunggu sampai {e.peminjam} mengembalikannya")
    except BatasPinjamError as e:
        print(f"Gagal: {e}")
        print(f"  Saran: kembalikan dulu salah satu dari {e.batas} buku")


def coba_kembalikan(anggota: Anggota, buku: Buku):
    try:
        anggota.kembalikan(buku)
        print(f"{anggota.nama} mengembalikan '{buku.judul}'")
    except PerpustakaanError as e:
        print(f"Gagal: {e}")


def main():
    laskar = Buku("Laskar Pelangi")
    bumi = Buku("Bumi Manusia")
    negeri = Buku("Negeri 5 Menara")
    ayu = Anggota("Ayu")
    bima = Anggota("Bima")

    print("=== PEMINJAMAN BUKU ===")
    coba_pinjam(ayu, laskar)
    coba_pinjam(ayu, bumi)
    coba_pinjam(ayu, negeri)  # melewati batas 2 buku
    coba_pinjam(bima, laskar)  # sedang dipinjam Ayu

    print()
    print("=== PENGEMBALIAN ===")
    coba_kembalikan(bima, bumi)  # Bima tidak meminjam buku ini
    coba_kembalikan(ayu, laskar)
    coba_pinjam(bima, laskar)  # sekarang berhasil


if __name__ == "__main__":
    main()
