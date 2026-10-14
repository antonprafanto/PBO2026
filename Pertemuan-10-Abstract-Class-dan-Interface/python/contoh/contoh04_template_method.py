"""
Contoh 04 - Template Method: Kerangka Tetap, Detail Diisi Kelas Anak
Pertemuan 10 - Abstract Class dan Interface

Laporan adalah kelas abstrak dengan method konkret tampilkan(). Method ini
menentukan URUTAN langkah yang sama untuk semua laporan (kerangkanya),
lalu memanggil method abstrak judul() dan isi() yang diisi kelas anak.
penutup() adalah method biasa yang BOLEH di-override (disebut "hook").

Pola ini disebut template method. Pola desain lainnya kita bahas di
Pertemuan 14.

Cara menjalankan:
    python contoh04_template_method.py
"""

from abc import ABC, abstractmethod

LEBAR = 40


class Laporan(ABC):
    """Kelas abstrak untuk semua jenis laporan."""

    def tampilkan(self):  # [1] template method: urutan langkahnya selalu sama
        print("=" * LEBAR)
        print(self.judul())  # [2] langkah yang diisi kelas anak
        print("-" * LEBAR)
        for baris in self.isi():  # [2]
            print(baris)
        print("-" * LEBAR)
        print(self.penutup())  # [3] hook: sudah punya isi, boleh di-override
        print("=" * LEBAR)

    @abstractmethod
    def judul(self) -> str:
        """Judul laporan."""

    @abstractmethod
    def isi(self) -> list[str]:
        """Baris-baris isi laporan."""

    def penutup(self) -> str:
        return "Dicetak oleh Sistem Informasi Akademik"


class LaporanKehadiran(Laporan):
    """Rekap kehadiran seorang mahasiswa di satu mata kuliah."""

    def __init__(self, nama: str, mata_kuliah: str, hadir: int, pertemuan: int):
        self._nama = nama
        self._mata_kuliah = mata_kuliah
        self._hadir = hadir
        self._pertemuan = pertemuan

    def judul(self) -> str:
        return f"LAPORAN KEHADIRAN {self._mata_kuliah}"

    def isi(self) -> list[str]:
        persen = self._hadir * 100 // self._pertemuan
        return [
            f"Mahasiswa  : {self._nama}",
            f"Hadir      : {self._hadir} dari {self._pertemuan} pertemuan",
            f"Persentase : {persen}%",
        ]


class LaporanPerpustakaan(Laporan):
    """Rekap peminjaman buku perpustakaan dalam satu bulan."""

    def __init__(self, bulan: str, dipinjam: int, dikembalikan: int):
        self._bulan = bulan
        self._dipinjam = dipinjam
        self._dikembalikan = dikembalikan

    def judul(self) -> str:
        return f"LAPORAN PERPUSTAKAAN BULAN {self._bulan}"

    def isi(self) -> list[str]:
        belum = self._dipinjam - self._dikembalikan
        return [
            f"Buku dipinjam      : {self._dipinjam}",
            f"Sudah dikembalikan : {self._dikembalikan}",
            f"Belum dikembalikan : {belum}",
        ]

    def penutup(self) -> str:  # [4] meng-override hook
        return "Disahkan oleh Kepala Perpustakaan"


def main():
    daftar: list[Laporan] = [
        LaporanKehadiran("Ayu Lestari", "PBO", 14, 16),
        LaporanPerpustakaan("OKTOBER", 120, 112),
    ]
    print(f"=== MENCETAK {len(daftar)} LAPORAN ===")
    for laporan in daftar:
        print()
        laporan.tampilkan()  # [5] satu panggilan, kerangka sama, isi berbeda


if __name__ == "__main__":
    main()
