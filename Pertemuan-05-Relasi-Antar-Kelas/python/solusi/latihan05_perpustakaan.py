"""
Solusi Latihan 05 - Perpustakaan Mini
Pertemuan 05 - Relasi Antar Kelas

Relasi yang dipakai:
- Perpustakaan o-- Buku        : agregasi (buku dibuat di luar, lalu didaftarkan)
- Perpustakaan *-- Peminjaman  : komposisi (peminjaman dibuat OLEH perpustakaan)
- Peminjaman --> Buku, Anggota : asosiasi (peminjaman mengenal buku dan peminjamnya)
- Perpustakaan ..> Anggota     : dependensi (anggota hanya datang lewat parameter)

Ide penyelesaian:
- Status "sedang dipinjam" TIDAK disimpan di Buku. Status itu dicari dari
  daftar peminjaman yang masih aktif, sehingga datanya tidak pernah ganda.
- cari_buku() mengembalikan Buku atau None, dan pemanggilnya selalu
  memeriksa None lebih dulu.
- Membandingkan buku dan anggota memakai operator is (objek yang SAMA).

Cara menjalankan:
    python latihan05_perpustakaan.py
"""

BATAS_PINJAM = 2  # setiap anggota boleh meminjam paling banyak 2 buku


class Buku:
    """Satu buku di koleksi perpustakaan."""

    def __init__(self, kode: str, judul: str):
        self._kode = kode
        self._judul = judul

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def judul(self) -> str:
        return self._judul


class Anggota:
    """Anggota perpustakaan."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama


class Peminjaman:
    """Catatan satu kali peminjaman: buku apa, oleh siapa, masih aktif atau tidak."""

    def __init__(self, buku: Buku, anggota: Anggota):
        self._buku = buku
        self._anggota = anggota
        self._aktif = True

    @property
    def buku(self) -> Buku:
        return self._buku

    @property
    def anggota(self) -> Anggota:
        return self._anggota

    @property
    def aktif(self) -> bool:
        return self._aktif

    def selesaikan(self):
        self._aktif = False

    def __str__(self) -> str:
        if self._aktif:
            status = "aktif"
        else:
            status = "selesai"
        return f"{self._buku.judul} oleh {self._anggota.nama} ({status})"


class Perpustakaan:
    """Perpustakaan yang punya koleksi buku dan riwayat peminjaman."""

    def __init__(self, nama: str):
        self._nama = nama
        self._koleksi: list[Buku] = []
        self._riwayat: list[Peminjaman] = []

    def tambah_buku(self, buku: Buku):
        self._koleksi.append(buku)

    def cari_buku(self, kode: str) -> Buku | None:
        for buku in self._koleksi:
            if buku.kode == kode:
                return buku
        return None

    def _peminjaman_aktif(self, buku: Buku) -> Peminjaman | None:
        """Peminjaman yang masih berjalan untuk buku ini, atau None."""
        for peminjaman in self._riwayat:
            if peminjaman.aktif and peminjaman.buku is buku:
                return peminjaman
        return None

    def _jumlah_dipinjam(self, anggota: Anggota) -> int:
        jumlah = 0
        for peminjaman in self._riwayat:
            if peminjaman.aktif and peminjaman.anggota is anggota:
                jumlah += 1
        return jumlah

    def pinjam(self, kode: str, anggota: Anggota):
        buku = self.cari_buku(kode)
        if buku is None:
            print(f"Gagal: buku {kode} tidak ditemukan")
            return
        sedang = self._peminjaman_aktif(buku)
        if sedang is not None:
            print(f"Gagal: {buku.judul} sedang dipinjam {sedang.anggota.nama}")
            return
        if self._jumlah_dipinjam(anggota) >= BATAS_PINJAM:
            print(f"Gagal: {anggota.nama} sudah meminjam {BATAS_PINJAM} buku")
            return
        self._riwayat.append(Peminjaman(buku, anggota))  # dibuat OLEH perpustakaan
        print(f"{anggota.nama} meminjam {buku.judul}")

    def kembalikan(self, kode: str):
        buku = self.cari_buku(kode)
        if buku is None:
            print(f"Gagal: buku {kode} tidak ditemukan")
            return
        sedang = self._peminjaman_aktif(buku)
        if sedang is None:
            print(f"Gagal: {buku.judul} tidak sedang dipinjam")
            return
        sedang.selesaikan()
        print(f"{sedang.anggota.nama} mengembalikan {buku.judul}")

    def tampilkan_koleksi(self):
        print(f"Koleksi {self._nama}:")
        for buku in self._koleksi:
            sedang = self._peminjaman_aktif(buku)
            if sedang is None:
                status = "tersedia"
            else:
                status = f"dipinjam {sedang.anggota.nama}"
            print(f"- [{buku.kode}] {buku.judul}: {status}")

    def tampilkan_riwayat(self):
        print("Riwayat peminjaman:")
        for nomor, peminjaman in enumerate(self._riwayat, start=1):
            print(f"  {nomor}. {peminjaman}")


def main():
    perpustakaan = Perpustakaan("Pojok Baca TI")
    perpustakaan.tambah_buku(Buku("B01", "Laskar Pelangi"))
    perpustakaan.tambah_buku(Buku("B02", "Bumi Manusia"))
    perpustakaan.tambah_buku(Buku("B03", "Negeri 5 Menara"))
    ayu = Anggota("Ayu")
    bima = Anggota("Bima")

    print("=== KOLEKSI AWAL ===")
    perpustakaan.tampilkan_koleksi()

    print()
    print("=== PEMINJAMAN ===")
    perpustakaan.pinjam("B01", ayu)
    perpustakaan.pinjam("B02", ayu)
    perpustakaan.pinjam("B03", ayu)
    perpustakaan.pinjam("B02", bima)
    perpustakaan.pinjam("B99", bima)
    perpustakaan.pinjam("B03", bima)

    print()
    print("=== PENGEMBALIAN ===")
    perpustakaan.kembalikan("B01")
    perpustakaan.kembalikan("B01")

    print()
    print("=== KOLEKSI AKHIR ===")
    perpustakaan.tampilkan_koleksi()

    print()
    print("=== RIWAYAT ===")
    perpustakaan.tampilkan_riwayat()


if __name__ == "__main__":
    main()
