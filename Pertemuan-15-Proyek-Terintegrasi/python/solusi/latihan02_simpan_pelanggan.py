"""
Solusi Latihan 02 - Simpan dan Muat Data Pelanggan
Pertemuan 15 - Proyek Terintegrasi

Ide penyelesaian:
- Kelas Pelanggan punya dua method "penerjemah":
    ke_kolom()           : objek -> list teks (satu baris CSV)
    dari_kolom(kolom)    : list teks -> objek (static method)
- RepositoriPelangganCSV meniru RepositoriMenuCSV di studi kasus:
    simpan(daftar) menulis ulang file, muat() membaca kembali menjadi objek.
- Bukti data benar-benar tersimpan: ubah poin, simpan, lalu MUAT ULANG dari
  file (bukan memakai objek lama di memori).

Cara menjalankan:
    python latihan02_simpan_pelanggan.py
"""

import csv
import tempfile
from pathlib import Path

PEMISAH = ";"
JUDUL_KOLOM = ["nama", "no_hp", "poin"]


class Pelanggan:
    """Pelanggan dengan poin. Poin hanya bertambah lewat tambah_poin()."""

    def __init__(self, nama: str, no_hp: str, poin: int = 0):
        self._nama = nama
        self._no_hp = no_hp
        self._poin = poin

    @property
    def poin(self) -> int:
        return self._poin

    def tambah_poin(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Poin yang ditambahkan harus lebih dari 0")
        self._poin += jumlah

    def ke_kolom(self) -> list[str]:
        return [self._nama, self._no_hp, str(self._poin)]

    @staticmethod
    def dari_kolom(kolom: list[str]) -> "Pelanggan":
        nama, no_hp, teks_poin = kolom
        return Pelanggan(nama, no_hp, int(teks_poin))

    def __str__(self) -> str:
        return f"{self._nama} ({self._no_hp}) - {self._poin} poin"


class RepositoriPelangganCSV:
    """Menghubungkan objek Pelanggan dengan file CSV."""

    def __init__(self, path: Path):
        self._path = path

    def simpan(self, daftar: list[Pelanggan]):
        with open(self._path, "w", encoding="utf-8", newline="") as berkas:
            penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")
            penulis.writerow(JUDUL_KOLOM)
            for pelanggan in daftar:
                penulis.writerow(pelanggan.ke_kolom())

    def muat(self) -> list[Pelanggan]:
        with open(self._path, encoding="utf-8", newline="") as berkas:
            pembaca = csv.reader(berkas, delimiter=PEMISAH)
            next(pembaca)  # lewati baris judul kolom
            return [Pelanggan.dari_kolom(kolom) for kolom in pembaca if kolom]


def tampilkan(daftar: list[Pelanggan]):
    for pelanggan in daftar:
        print(pelanggan)


def main():
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "pelanggan.csv"
        repo = RepositoriPelangganCSV(path)

        print("=== SIMPAN 3 PELANGGAN ===")
        repo.simpan([Pelanggan("Budi Santoso", "081234567890", 12),
                     Pelanggan("Siti Aminah", "082198765432", 3),
                     Pelanggan("Rina Marlina", "085312345678")])
        print(f"Isi {path.name}:")
        print(path.read_text(encoding="utf-8"), end="")

        print()
        print("=== MUAT KEMBALI ===")
        daftar = repo.muat()
        tampilkan(daftar)

        print()
        print("=== SITI BERTRANSAKSI (+5 POIN), LALU DISIMPAN ULANG ===")
        daftar[1].tambah_poin(5)
        repo.simpan(daftar)
        daftar_baru = repo.muat()  # objek-objek BARU hasil membaca file
        print("Setelah dimuat ulang dari file:")
        tampilkan(daftar_baru)
        total = 0
        for pelanggan in daftar_baru:
            total += pelanggan.poin
        print(f"Total poin semua pelanggan: {total}")


if __name__ == "__main__":
    main()
