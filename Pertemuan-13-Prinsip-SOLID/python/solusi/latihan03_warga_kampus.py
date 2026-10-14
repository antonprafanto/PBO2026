"""
Solusi Latihan 03 - Interface Ramping untuk Warga Kampus (ISP)
Pertemuan 13 - Prinsip SOLID

Ide penyelesaian:
- Kontrak gemuk WargaKampus (ikut_kuliah, bayar_ukt, mengajar, isi_nilai)
  dipecah menjadi dua kontrak kecil:
    Pelajar  -> ikut_kuliah(), bayar_ukt()
    Pengajar -> mengajar(), isi_nilai()
- Mahasiswa hanya Pelajar, Dosen hanya Pengajar. Tidak ada lagi method palsu
  seperti "Dosen.bayar_ukt()" yang melempar error.
- AsistenPraktikum memenuhi DUA kontrak sekaligus, sehingga ia boleh masuk ke
  daftar pelajar maupun daftar pengajar.

Cara menjalankan:
    python latihan03_warga_kampus.py
"""

from abc import ABC, abstractmethod


class Pelajar(ABC):
    """Kontrak kecil untuk orang yang belajar."""

    @abstractmethod
    def ikut_kuliah(self, matkul: str) -> str:
        """Kalimat yang menjelaskan kegiatan kuliah."""

    @abstractmethod
    def bayar_ukt(self) -> str:
        """Kalimat yang menjelaskan pembayaran UKT."""


class Pengajar(ABC):
    """Kontrak kecil untuk orang yang mengajar dan menilai."""

    @abstractmethod
    def mengajar(self, matkul: str) -> str:
        """Kalimat yang menjelaskan kegiatan mengajar."""

    @abstractmethod
    def isi_nilai(self, nama_mahasiswa: str, nilai: str) -> str:
        """Kalimat yang menjelaskan pengisian nilai."""


class Mahasiswa(Pelajar):
    def __init__(self, nama: str):
        self._nama = nama

    def ikut_kuliah(self, matkul: str) -> str:
        return f"{self._nama} mengikuti kuliah {matkul}"

    def bayar_ukt(self) -> str:
        return f"{self._nama} membayar UKT semester depan"


class Dosen(Pengajar):
    def __init__(self, nama: str):
        self._nama = nama

    def mengajar(self, matkul: str) -> str:
        return f"{self._nama} mengajar {matkul}"

    def isi_nilai(self, nama_mahasiswa: str, nilai: str) -> str:
        return f"{self._nama} mengisi nilai {nilai} untuk {nama_mahasiswa}"


class AsistenPraktikum(Pelajar, Pengajar):  # memenuhi dua kontrak kecil
    def __init__(self, nama: str):
        self._nama = nama

    def ikut_kuliah(self, matkul: str) -> str:
        return f"{self._nama} mengikuti kuliah {matkul}"

    def bayar_ukt(self) -> str:
        return f"{self._nama} membayar UKT semester depan"

    def mengajar(self, matkul: str) -> str:
        return f"{self._nama} membimbing praktikum {matkul}"

    def isi_nilai(self, nama_mahasiswa: str, nilai: str) -> str:
        return f"{self._nama} mengisi nilai praktikum {nilai} untuk {nama_mahasiswa}"


def main():
    hendra = Dosen("Dr. Hendra")
    ayu = Mahasiswa("Ayu")
    rizky = AsistenPraktikum("Rizky")

    pengajar: list[Pengajar] = [hendra, rizky]  # hanya yang memenuhi Pengajar
    pelajar: list[Pelajar] = [ayu, rizky]  # hanya yang memenuhi Pelajar

    print("=== PARA PENGAJAR ===")
    for orang in pengajar:
        print(orang.mengajar("PBO"))
        print(orang.isi_nilai("Ayu", "A"))

    print()
    print("=== PARA PELAJAR ===")
    for orang in pelajar:
        print(orang.ikut_kuliah("Basis Data"))
        print(orang.bayar_ukt())

    print()
    print(f"Jumlah pengajar: {len(pengajar)}, jumlah pelajar: {len(pelajar)}")
    print("Rizky ada di kedua daftar karena ia mahasiswa sekaligus asisten.")


if __name__ == "__main__":
    main()
