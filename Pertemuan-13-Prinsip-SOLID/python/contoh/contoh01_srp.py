"""
Contoh 01 - SRP: Satu Kelas, Satu Alasan untuk Berubah
Pertemuan 13 - Prinsip SOLID

Versi MELANGGAR: LaporanSerbaBisa menghitung nilai, menentukan predikat,
DAN mencetak laporan di dalam satu method. Hasil hitungannya "terkunci"
di dalam print, sehingga tidak bisa dipakai untuk keperluan lain.

Versi SESUAI SRP:
- PenghitungNilai  -> hanya menghitung (rata-rata dan predikat)
- PencetakLaporan  -> hanya menyusun dan mencetak laporan
Laporannya SAMA PERSIS, tetapi hitungannya kini bisa dipakai ulang.

Cara menjalankan:
    python contoh01_srp.py
"""


# ------------------------------------------------------------ MELANGGAR SRP
class LaporanSerbaBisa:
    """Menghitung DAN mencetak sekaligus (dua alasan untuk berubah)."""

    def __init__(self, data_nilai: dict[str, list[int]]):
        self._data_nilai = data_nilai  # nama -> daftar nilai

    def cetak_laporan(self):
        print("LAPORAN NILAI KELAS PBO")
        for nama, daftar in self._data_nilai.items():
            rata = sum(daftar) // len(daftar)  # [1] aturan hitung...
            if rata >= 80:
                predikat = "A"
            elif rata >= 70:
                predikat = "B"
            elif rata >= 60:
                predikat = "C"
            else:
                predikat = "D"
            print(f"  {nama:<8}{rata:>4}  {predikat}")  # [2] ...bercampur format


# -------------------------------------------------------------- SESUAI SRP
class PenghitungNilai:
    """Hanya menghitung. Tidak pernah mencetak apa pun."""

    def rata_rata(self, daftar: list[int]) -> int:
        return sum(daftar) // len(daftar)

    def predikat(self, rata: int) -> str:  # [3] satu-satunya tempat aturan predikat
        if rata >= 80:
            return "A"
        if rata >= 70:
            return "B"
        if rata >= 60:
            return "C"
        return "D"


class PencetakLaporan:
    """Hanya menyusun dan mencetak laporan."""

    def __init__(self, penghitung: PenghitungNilai):
        self._penghitung = penghitung  # [4] hitungan diminta dari ahlinya

    def cetak(self, data_nilai: dict[str, list[int]]):
        print("LAPORAN NILAI KELAS PBO")
        for nama, daftar in data_nilai.items():
            rata = self._penghitung.rata_rata(daftar)
            predikat = self._penghitung.predikat(rata)
            print(f"  {nama:<8}{rata:>4}  {predikat}")


def main():
    data_nilai = {
        "Ayu": [85, 90, 78],
        "Bima": [70, 65, 80],
        "Citra": [55, 60, 58],
    }

    print("=== VERSI MELANGGAR SRP ===")
    LaporanSerbaBisa(data_nilai).cetak_laporan()

    print()
    print("=== VERSI SESUAI SRP ===")
    penghitung = PenghitungNilai()
    PencetakLaporan(penghitung).cetak(data_nilai)

    print()
    print("=== BONUS SRP: HITUNGAN DIPAKAI ULANG ===")
    for nama, daftar in data_nilai.items():
        rata = penghitung.rata_rata(daftar)  # [5] tanpa ikut mencetak laporan
        if penghitung.predikat(rata) == "D":
            print(f"{nama} perlu remedial (rata-rata {rata})")


if __name__ == "__main__":
    main()
