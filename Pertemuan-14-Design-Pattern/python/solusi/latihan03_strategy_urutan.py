"""
Solusi Latihan 03 - Strategy Pengurutan Daftar Mahasiswa
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- StrategiUrut adalah kontrak: nama() dan urutkan(daftar) -> list baru.
- Tiga strategi: UrutNim, UrutNama, UrutNilai (nilai tertinggi dulu; jika
  nilainya sama, urut nama A-Z).
- DaftarPeringkat (context) menyimpan SATU strategi dan bisa menukarnya
  kapan saja lewat atur_strategi().
- Perhatikan: key di sorted() sebenarnya juga sebuah "strategi kecil".

Cara menjalankan:
    python latihan03_strategy_urutan.py
"""

from abc import ABC, abstractmethod


class Mahasiswa:
    def __init__(self, nim: str, nama: str, nilai: int):
        self._nim = nim
        self._nama = nama
        self._nilai = nilai

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nilai(self) -> int:
        return self._nilai

    def __str__(self) -> str:
        return f"{self._nim} {self._nama:<15}{self._nilai:>4}"


class StrategiUrut(ABC):
    """Strategy: kontrak semua cara mengurutkan mahasiswa."""

    @abstractmethod
    def nama(self) -> str:
        """Nama aturan urutan."""

    @abstractmethod
    def urutkan(self, daftar: list[Mahasiswa]) -> list[Mahasiswa]:
        """Mengembalikan list BARU yang sudah urut (list asli tidak diubah)."""


class UrutNim(StrategiUrut):
    def nama(self) -> str:
        return "NIM terkecil"

    def urutkan(self, daftar: list[Mahasiswa]) -> list[Mahasiswa]:
        return sorted(daftar, key=lambda m: m.nim)


class UrutNama(StrategiUrut):
    def nama(self) -> str:
        return "Nama A-Z"

    def urutkan(self, daftar: list[Mahasiswa]) -> list[Mahasiswa]:
        return sorted(daftar, key=lambda m: m.nama)


class UrutNilai(StrategiUrut):
    def nama(self) -> str:
        return "Nilai tertinggi"

    def urutkan(self, daftar: list[Mahasiswa]) -> list[Mahasiswa]:
        # minus nilai = nilai terbesar dulu; jika seri, nama A-Z
        return sorted(daftar, key=lambda m: (-m.nilai, m.nama))


class DaftarPeringkat:
    """Context: menampilkan mahasiswa memakai strategi yang sedang dipasang."""

    def __init__(self, daftar: list[Mahasiswa], strategi: StrategiUrut):
        self._daftar = list(daftar)
        self._strategi = strategi

    def atur_strategi(self, strategi: StrategiUrut):
        self._strategi = strategi

    def tampilkan(self):
        print(f"=== URUT: {self._strategi.nama().upper()} ===")
        hasil = self._strategi.urutkan(self._daftar)
        for nomor, mahasiswa in enumerate(hasil, start=1):
            print(f"{nomor}. {mahasiswa}")


def main():
    kelas_pbo = [
        Mahasiswa("2409106004", "Ayu Lestari", 85),
        Mahasiswa("2409106002", "Bima Saputra", 92),
        Mahasiswa("2409106001", "Citra Dewi", 85),
        Mahasiswa("2409106003", "Dimas Pratama", 78),
    ]
    peringkat = DaftarPeringkat(kelas_pbo, UrutNim())
    peringkat.tampilkan()

    for strategi in [UrutNama(), UrutNilai()]:
        print()
        peringkat.atur_strategi(strategi)  # tukar strategi saat program berjalan
        peringkat.tampilkan()


if __name__ == "__main__":
    main()
