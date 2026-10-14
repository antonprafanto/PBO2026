"""
Contoh 02 - Menyimpan dan Memuat Objek dengan File CSV
Pertemuan 15 - Proyek Terintegrasi

CSV (Comma-Separated Values) adalah file teks berbentuk tabel: satu baris =
satu data, kolom dipisahkan tanda tertentu. Di sini pemisahnya TITIK KOMA,
karena isi kolom (misalnya asal "Samarinda, Kaltim") boleh mengandung koma.

- csv.writer : mengubah list menjadi satu baris CSV
- csv.reader : mengubah satu baris CSV kembali menjadi list
- open(..., newline="") dianjurkan oleh dokumentasi modul csv

Cara menjalankan:
    python contoh02_csv.py
"""

import csv
import tempfile
from pathlib import Path

PEMISAH = ";"
JUDUL_KOLOM = ["nim", "nama", "asal", "sks", "catatan"]


class Mahasiswa:
    """Data mahasiswa yang akan disimpan ke file CSV."""

    def __init__(self, nim: str, nama: str, asal: str, sks: int, catatan: str):
        self.nim = nim
        self.nama = nama
        self.asal = asal
        self.sks = sks
        self.catatan = catatan

    def ke_kolom(self) -> list[str]:  # [1] objek -> list teks (satu baris)
        return [self.nim, self.nama, self.asal, str(self.sks), self.catatan]

    @staticmethod
    def dari_kolom(kolom: list[str]) -> "Mahasiswa":  # [2] list teks -> objek
        nim, nama, asal, teks_sks, catatan = kolom
        return Mahasiswa(nim, nama, asal, int(teks_sks), catatan)


def simpan(path: Path, daftar: list[Mahasiswa]):
    with open(path, "w", encoding="utf-8", newline="") as berkas:
        penulis = csv.writer(berkas, delimiter=PEMISAH, lineterminator="\n")  # [3]
        penulis.writerow(JUDUL_KOLOM)  # baris pertama: judul kolom
        for mhs in daftar:
            penulis.writerow(mhs.ke_kolom())


def muat(path: Path) -> list[Mahasiswa]:
    hasil = []
    with open(path, encoding="utf-8", newline="") as berkas:
        pembaca = csv.reader(berkas, delimiter=PEMISAH)  # [4]
        next(pembaca)  # [5] lewati baris judul kolom
        for nomor_baris, kolom in enumerate(pembaca, start=2):
            try:
                hasil.append(Mahasiswa.dari_kolom(kolom))
            except ValueError:  # [6] jumlah kolom salah atau sks bukan angka
                print(f"  Baris {nomor_baris} dilewati: data tidak valid")
    return hasil


def main():
    data_awal = [
        Mahasiswa("2409106001", "Ayu Lestari", "Samarinda, Kaltim", 20, "ketua kelas"),
        Mahasiswa("2409106002", "Bima Saputra", "Balikpapan, Kaltim", 18, ""),
        Mahasiswa("2409106003", "Citra Dewi", "Tenggarong, Kukar", 22, "asisten lab"),
    ]
    with tempfile.TemporaryDirectory() as folder:
        path = Path(folder) / "mahasiswa.csv"

        print("=== 1. MENYIMPAN 3 OBJEK KE CSV ===")
        simpan(path, data_awal)
        print(f"Tersimpan di {path.name}")

        print()
        print("=== 2. ISI FILE APA ADANYA ===")
        print(path.read_text(encoding="utf-8"), end="")  # [7]

        print()
        print("=== 3. MEMUAT KEMBALI MENJADI OBJEK ===")
        daftar = muat(path)
        total_sks = 0
        for mhs in daftar:
            catatan = mhs.catatan if mhs.catatan else "-"  # [8] kolom kosong
            print(f"{mhs.nama:<14}{mhs.asal:<20}{mhs.sks:>3} sks  ({catatan})")
            total_sks += mhs.sks
        print(f"Total {len(daftar)} mahasiswa, {total_sks} sks")

        print()
        print("=== 4. FILE DENGAN BARIS RUSAK ===")
        with open(path, "a", encoding="utf-8", newline="") as berkas:
            berkas.write("2409106004;Dimas Pratama;Bontang;dua puluh;\n")
            berkas.write("2409106005;Eka Putri\n")
        daftar = muat(path)
        print(f"Berhasil dimuat: {len(daftar)} mahasiswa")


if __name__ == "__main__":
    main()
