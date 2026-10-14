"""
Solusi Latihan 04 - Penyimpanan Terbatas untuk Kedai (DIP)
Pertemuan 13 - Prinsip SOLID

Ide penyelesaian:
- PenyimpananTerbatas adalah turunan BARU dari PenyimpananPesanan. Ia hanya
  menyimpan N pesanan TERAKHIR; jika penuh, pesanan terlama dibuang.
- Kelas Kedai tidak diubah sedikit pun. Ia tetap menerima "apa saja yang
  memenuhi kontrak PenyimpananPesanan" lewat konstruktor (dependency injection).
- Jenis penyimpanan dipilih di main(), satu-satunya tempat yang perlu tahu.
- Maksimal kurang dari 1 tidak masuk akal, jadi ditolak sejak objek dibuat.

Agar file ini bisa dijalankan sendiri, Pesanan, PenyimpananPesanan,
PenyimpananMemori, dan Kedai disalin dalam versi RINGKAS. Satu-satunya kelas
yang BARU adalah PenyimpananTerbatas. Di salinan studi kasus milikmu (Cara A
di latihan.md), tambahkan kelas itu di file baru, misalnya
penyimpanan_terbatas.py.

Cara menjalankan:
    python latihan04_penyimpanan_terbatas.py
"""

from abc import ABC, abstractmethod


# ------------------------------- salinan RINGKAS dari studi kasus (tidak diubah)
class Pesanan:
    """Versi ringkas: cukup nomor otomatis dan nama pelanggan."""

    _nomor_terakhir = 0  # atribut kelas: penomoran berlanjut untuk semua kedai

    def __init__(self, nama_pelanggan: str):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"P{Pesanan._nomor_terakhir:03d}"
        self._nama_pelanggan = nama_pelanggan

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def nama_pelanggan(self) -> str:
        return self._nama_pelanggan


class PenyimpananPesanan(ABC):
    @abstractmethod
    def simpan(self, pesanan: Pesanan):
        """Menyimpan satu pesanan."""

    @abstractmethod
    def semua(self) -> list[Pesanan]:
        """Semua pesanan yang tersimpan, urut sesuai waktu disimpan."""

    def jumlah(self) -> int:
        return len(self.semua())


class PenyimpananMemori(PenyimpananPesanan):
    def __init__(self):
        self._data: list[Pesanan] = []

    def simpan(self, pesanan: Pesanan):
        self._data.append(pesanan)

    def semua(self) -> list[Pesanan]:
        return list(self._data)


class Kedai:
    def __init__(self, nama: str, penyimpanan: PenyimpananPesanan):
        self._nama = nama
        self._penyimpanan = penyimpanan  # bergantung pada ABSTRAKSI

    def buat_pesanan(self, nama_pelanggan: str) -> Pesanan:
        pesanan = Pesanan(nama_pelanggan)
        self._penyimpanan.simpan(pesanan)
        return pesanan

    def riwayat_pesanan(self) -> list[Pesanan]:
        return self._penyimpanan.semua()

    def jumlah_pesanan(self) -> int:
        return self._penyimpanan.jumlah()


# ------------------------------------------------------------------- KELAS BARU
class PenyimpananTerbatas(PenyimpananPesanan):
    """Hanya menyimpan N pesanan TERAKHIR. Pesanan terlama dibuang."""

    def __init__(self, maksimal: int):
        if maksimal < 1:
            raise ValueError("Maksimal pesanan harus minimal 1")
        self._maksimal = maksimal
        self._data: list[Pesanan] = []

    def simpan(self, pesanan: Pesanan):
        self._data.append(pesanan)
        if len(self._data) > self._maksimal:
            self._data.pop(0)  # buang pesanan yang paling lama

    def semua(self) -> list[Pesanan]:
        return list(self._data)  # jumlah() cukup memakai versi induknya


# ------------------------------------------------------------- program utama
def layani_pelanggan(kedai: Kedai):
    """Membuat empat pesanan, lalu menampilkan isi riwayat kedai."""
    for nama in ["Budi Santoso", "Siti Aminah", "Rina Marlina", "Andi Wijaya"]:
        kedai.buat_pesanan(nama)
    print(f"Pesanan tersimpan: {kedai.jumlah_pesanan()}")
    for pesanan in kedai.riwayat_pesanan():
        print(f"  {pesanan.nomor}  {pesanan.nama_pelanggan}")


def main():
    print("=== KEDAI DENGAN PENYIMPANAN MEMORI (TANPA BATAS) ===")
    layani_pelanggan(Kedai("KedaiKita", PenyimpananMemori()))

    print()
    print("=== KEDAI DENGAN PENYIMPANAN TERBATAS (MAKSIMAL 2) ===")
    layani_pelanggan(Kedai("KedaiKita", PenyimpananTerbatas(2)))

    print()
    print("=== MAKSIMAL YANG TIDAK MASUK AKAL ===")
    try:
        PenyimpananTerbatas(0)
    except ValueError as e:
        print(f"Ditolak: {e}")


if __name__ == "__main__":
    main()
