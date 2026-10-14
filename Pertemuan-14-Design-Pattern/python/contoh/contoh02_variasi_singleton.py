"""
Contoh 02 - Variasi Singleton ala Python: Objek Tingkat Modul dan __new__
Pertemuan 14 - Design Pattern Dasar

Variasi 1 (EAGER, disiapkan di awal): cukup buat SATU objek di tingkat modul.
    Sebuah modul hanya dimuat sekali, jadi objek di dalamnya juga hanya
    dibuat sekali. Inilah cara yang paling sering dipakai pemrogram Python.
Variasi 2 (LAZY, dibuat saat pertama diminta): override __new__, yaitu method
    yang benar-benar MEMBUAT objek (dipanggil sebelum __init__). Setiap
    pemanggilan Tema() mengembalikan objek yang sama.

Output contoh ini sengaja sama dengan versi Java-nya, walaupun cara kerjanya
berbeda (lihat Jembatan Python <-> Java).

Cara menjalankan:
    python contoh02_variasi_singleton.py
"""


class PencatatLog:
    """Pencatat kegiatan aplikasi."""

    def __init__(self):
        self._catatan: list[str] = []

    def catat(self, sumber: str, pesan: str):
        self._catatan.append(f"{sumber}: {pesan}")
        print(f"[LOG {len(self._catatan)}] {sumber}: {pesan}")

    def jumlah(self) -> int:
        return len(self._catatan)


# [1] Variasi 1: objek tingkat modul, dibuat SEKALI saat file ini dimuat
pencatat = PencatatLog()


class Tema:
    """Variasi 2: Singleton lewat __new__."""

    _instance = None
    _sudah_diisi = False

    def __new__(cls):  # [2] __new__ MEMBUAT objek, dipanggil sebelum __init__
        if cls._instance is None:
            print("  (objek Tema dibuat)")
            cls._instance = super().__new__(cls)
        return cls._instance  # [3] selalu mengembalikan objek yang sama

    def __init__(self):
        if Tema._sudah_diisi:  # [4] __init__ tetap terpanggil di SETIAP Tema()
            return
        Tema._sudah_diisi = True
        self._warna = "terang"

    @property
    def warna(self) -> str:
        return self._warna

    @warna.setter
    def warna(self, nilai: str):
        self._warna = nilai


def modul_kasir():
    pencatat.catat("kasir", "transaksi dibuka")  # [5] memakai objek modul


def modul_laporan():
    pencatat.catat("laporan", "laporan harian dibuat")


def main():
    print("=== VARIASI 1: OBJEK DISIAPKAN DI AWAL (EAGER) ===")
    modul_kasir()
    modul_laporan()
    print(f"Jumlah catatan: {pencatat.jumlah()}")

    print()
    print("=== VARIASI 2: DIBUAT SAAT PERTAMA DIMINTA (LAZY) ===")
    print("Permintaan pertama:")
    t1 = Tema()  # [6] terlihat seperti membuat objek baru...
    print("Permintaan kedua:")
    t2 = Tema()  # ...padahal hasilnya objek yang sama
    print(f"t1 dan t2 objek yang sama? {'ya' if t1 is t2 else 'tidak'}")
    t1.warna = "gelap"
    print("Warna diubah lewat t1 menjadi gelap")
    print(f"Warna dibaca lewat t2: {t2.warna}")


if __name__ == "__main__":
    main()
