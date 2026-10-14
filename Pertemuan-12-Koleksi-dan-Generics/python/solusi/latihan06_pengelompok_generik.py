"""
Solusi Latihan 06 - Pengelompok Generik
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Fungsi generik kelompokkan(daftar, kunci) bekerja untuk tipe isi APA PUN (T)
  dan tipe kunci APA PUN (K).
- kunci adalah fungsi (boleh lambda) yang mengubah satu isi menjadi kuncinya.
  Callable[[T], K] dibaca "fungsi yang menerima T dan mengembalikan K".
- Hasilnya dict K -> list[T]. Jika kunci belum ada, buat list kosong dulu.
- dict menjaga urutan kunci sesuai kemunculan pertama.

Cara menjalankan:
    python latihan06_pengelompok_generik.py
"""

from typing import Callable, TypeVar

T = TypeVar("T")
K = TypeVar("K")


def kelompokkan(daftar: list[T], kunci: Callable[[T], K]) -> dict[K, list[T]]:
    hasil: dict[K, list[T]] = {}
    for isi in daftar:
        k = kunci(isi)
        if k not in hasil:
            hasil[k] = []  # kunci baru: siapkan list kosong
        hasil[k].append(isi)
    return hasil


class Anggota:
    """Anggota UKM beserta angkatannya."""

    def __init__(self, nama: str, angkatan: int):
        self._nama = nama
        self._angkatan = angkatan

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def angkatan(self) -> int:
        return self._angkatan


def main():
    buah = ["apel", "anggur", "belimbing", "ceri", "bisbul", "alpukat"]

    print("=== BUAH PER HURUF AWAL ===")
    per_huruf = kelompokkan(buah, lambda kata: kata[0])  # T = str, K = str
    for huruf, daftar in per_huruf.items():
        print(f"{huruf}: {', '.join(daftar)}")

    print()
    print("=== BUAH PER PANJANG NAMA ===")
    per_panjang = kelompokkan(buah, len)  # fungsi bawaan pun bisa jadi kunci
    for panjang, daftar in per_panjang.items():
        print(f"{panjang} huruf: {', '.join(daftar)}")

    print()
    print("=== ANGGOTA UKM PER ANGKATAN ===")
    anggota = [
        Anggota("Bima", 2023),
        Anggota("Ayu", 2024),
        Anggota("Eka", 2023),
        Anggota("Citra", 2024),
        Anggota("Dimas", 2025),
    ]
    per_angkatan = kelompokkan(anggota, lambda a: a.angkatan)  # T = Anggota, K = int
    for angkatan, daftar in per_angkatan.items():
        nama = [a.nama for a in daftar]
        print(f"{angkatan}: {', '.join(nama)} ({len(daftar)} orang)")


if __name__ == "__main__":
    main()
