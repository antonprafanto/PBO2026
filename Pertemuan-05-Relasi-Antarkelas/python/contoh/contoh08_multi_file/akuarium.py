"""
Modul akuarium: berisi kelas Akuarium, yang memakai kelas Ikan dari ikan.py.

Bagian dari Contoh 08 - Program Banyak File (Pertemuan 05).
File ini hanya berisi kelas. Jalankan main.py, bukan file ini.
"""

from ikan import Ikan  # [1] ambil kelas Ikan dari file ikan.py


class Akuarium:
    """Akuarium yang menampung beberapa ikan (agregasi)."""

    def __init__(self, kapasitas: int):
        self._kapasitas = kapasitas
        self._daftar_ikan: list[Ikan] = []

    def masukkan(self, ikan: Ikan):
        if len(self._daftar_ikan) >= self._kapasitas:
            print(f"Gagal: akuarium penuh, {ikan.nama} tidak muat")
            return
        self._daftar_ikan.append(ikan)
        print(f"{ikan.nama} masuk akuarium")

    def tampilkan(self):
        print(f"Isi akuarium ({len(self._daftar_ikan)}/{self._kapasitas}):")
        for ikan in self._daftar_ikan:
            print(f"- {ikan}")
