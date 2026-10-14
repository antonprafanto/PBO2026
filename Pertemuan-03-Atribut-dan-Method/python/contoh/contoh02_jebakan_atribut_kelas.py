"""
Contoh 02 - Jebakan: Mengubah Atribut Kelas Lewat Objek
Pertemuan 03 - Atribut dan Method Lebih Dalam

MEMBACA atribut kelas lewat objek boleh: Python mencari nama atribut di
objek dulu, dan jika tidak ada, baru mencarinya di kelas.

Tetapi MENGISI atribut lewat objek (self.total += 1) selalu membuat atribut
OBJEK baru. Atribut objek baru itu "membayangi" atribut kelas yang bernama
sama, sedangkan nilai bersama di kelas TIDAK ikut berubah.

(Perilaku ini khas Python. Bandingkan dengan Contoh02AksesStatic.java.)

Cara menjalankan:
    python contoh02_jebakan_atribut_kelas.py
"""


class Pengunjung:
    """Pengunjung perpustakaan kampus."""

    total = 0  # atribut kelas: jumlah seluruh pengunjung hari ini

    def __init__(self, nama):
        self.nama = nama

    def masuk_lewat_objek(self):
        self.total += 1  # [1] JEBAKAN: membuat atribut OBJEK baru bernama total

    def masuk_lewat_kelas(self):
        Pengunjung.total += 1  # [2] BENAR: mengubah atribut kelas milik bersama


def main():
    ayu = Pengunjung("Ayu")
    bima = Pengunjung("Bima")

    print("=== LEWAT OBJEK: self.total += 1 ===")
    ayu.masuk_lewat_objek()
    bima.masuk_lewat_objek()
    print(f"Total menurut kelas : {Pengunjung.total}")  # [3] tetap 0!
    print(f"Total menurut ayu   : {ayu.total}")
    print(f"Total menurut bima  : {bima.total}")

    print()
    print("=== LEWAT NAMA KELAS: Pengunjung.total += 1 ===")
    citra = Pengunjung("Citra")
    dimas = Pengunjung("Dimas")
    citra.masuk_lewat_kelas()
    dimas.masuk_lewat_kelas()
    print(f"Total menurut kelas : {Pengunjung.total}")
    print(f"Total menurut citra : {citra.total}")  # [4] dibaca dari kelas
    print(f"Total menurut dimas : {dimas.total}")
    print(f"Total menurut ayu   : {ayu.total}")  # [5] ayu membaca "bayangannya" sendiri

    print()
    print("=== ISI MASING-MASING OBJEK ===")
    print(f"ayu   : {vars(ayu)}")  # [6] vars() menampilkan atribut milik objek
    print(f"citra : {vars(citra)}")


if __name__ == "__main__":
    main()
