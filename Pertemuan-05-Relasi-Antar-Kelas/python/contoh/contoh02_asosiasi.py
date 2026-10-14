"""
Contoh 02 - Asosiasi: Objek yang Mengenal Objek Lain
Pertemuan 05 - Relasi Antar Kelas

Setiap Mahasiswa MENGENAL dosen walinya lewat sebuah atribut yang berisi
referensi ke objek DosenWali. Beberapa mahasiswa bisa mengenal dosen yang
SAMA, dan mahasiswa baru boleh belum punya dosen wali (None).

Cara menjalankan:
    python contoh02_asosiasi.py
"""


class DosenWali:
    """Dosen yang membimbing perwalian mahasiswa."""

    def __init__(self, nama: str, ruangan: str):
        self._nama = nama
        self._ruangan = ruangan

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def ruangan(self) -> str:
        return self._ruangan

    def pindah_ruangan(self, ruangan_baru: str):
        self._ruangan = ruangan_baru


class Mahasiswa:
    """Mahasiswa yang mengenal dosen walinya."""

    def __init__(self, nama: str):
        self._nama = nama
        self._dosen_wali: DosenWali | None = None  # [1] awalnya belum ada

    def atur_dosen_wali(self, dosen: DosenWali):
        self._dosen_wali = dosen  # [2] menyimpan REFERENSI, bukan salinan

    def info_perwalian(self) -> str:
        if self._dosen_wali is None:  # [3] periksa dulu sebelum dipakai
            return f"{self._nama}: belum punya dosen wali"
        dosen = self._dosen_wali
        return f"{self._nama}: dosen wali {dosen.nama}, ruang {dosen.ruangan}"  # [4]


def main():
    bu_rina = DosenWali("Bu Rina", "C-201")
    ayu = Mahasiswa("Ayu")
    bima = Mahasiswa("Bima")
    citra = Mahasiswa("Citra")

    print("=== SEBELUM PERWALIAN ===")
    print(ayu.info_perwalian())

    ayu.atur_dosen_wali(bu_rina)  # [5] dua mahasiswa mengenal objek yang SAMA
    bima.atur_dosen_wali(bu_rina)

    print()
    print("=== SETELAH PERWALIAN ===")
    for mahasiswa in [ayu, bima, citra]:
        print(mahasiswa.info_perwalian())

    print()
    print("=== BU RINA PINDAH RUANGAN ===")
    bu_rina.pindah_ruangan("D-105")  # [6] diubah di satu tempat saja
    print(ayu.info_perwalian())
    print(bima.info_perwalian())


if __name__ == "__main__":
    main()
