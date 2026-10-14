"""
Solusi Latihan 04 - Kelas NilaiKuliah
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
- nilai_akhir() = 30% tugas + 30% UTS + 40% UAS.
  Supaya hasilnya bilangan bulat, kalikan dulu baru bagi:
  (30 * tugas + 30 * uts + 40 * uas) // 100
- huruf() memakai nilai_akhir() (method memanggil method lain lewat self).
- lulus(batas) mengembalikan True/False.

Cara menjalankan:
    python latihan04_nilai_kuliah.py
"""


class NilaiKuliah:
    """Nilai satu mata kuliah."""

    def __init__(self, nama_mk, tugas, uts, uas):
        self.nama_mk = nama_mk
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def nilai_akhir(self):
        return (30 * self.tugas + 30 * self.uts + 40 * self.uas) // 100

    def huruf(self):
        nilai = self.nilai_akhir()
        if nilai >= 80:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        elif nilai >= 50:
            return "D"
        else:
            return "E"

    def lulus(self, batas):
        return self.nilai_akhir() >= batas


def main():
    daftar = [
        NilaiKuliah("Pemrograman Berorientasi Objek", 85, 78, 90),
        NilaiKuliah("Basis Data", 70, 65, 72),
        NilaiKuliah("Matematika Diskrit", 60, 55, 48),
    ]
    print("=== KARTU HASIL STUDI (SEDERHANA) ===")
    for mk in daftar:
        if mk.lulus(60):
            keterangan = "lulus"
        else:
            keterangan = "belum lulus"
        print(f"{mk.nama_mk}: {mk.nilai_akhir()} ({mk.huruf()}) - {keterangan}")


if __name__ == "__main__":
    main()
