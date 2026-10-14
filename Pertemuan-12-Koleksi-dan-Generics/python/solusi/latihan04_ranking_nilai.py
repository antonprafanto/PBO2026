"""
Solusi Latihan 04 - Ranking Nilai Mahasiswa
Pertemuan 12 - Koleksi dan Generics

Ide penyelesaian:
- Urutan ALAMI mahasiswa = urut NIM, ditulis di __lt__.
  Jadi sorted(kelas) tanpa key langsung urut NIM.
- Ranking memakai urutan KHUSUS dengan key tuple tiga kriteria:
    (-nilai_akhir, -nilai_uas, nama)
  Tanda minus membuat angka terbesar berada di depan; nama tetap A-Z.

Cara menjalankan:
    python latihan04_ranking_nilai.py
"""


class NilaiMahasiswa:
    """Nilai akhir dan nilai UAS seorang mahasiswa."""

    def __init__(self, nim: str, nama: str, nilai_akhir: int, nilai_uas: int):
        self._nim = nim
        self._nama = nama
        self._nilai_akhir = nilai_akhir
        self._nilai_uas = nilai_uas

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def nilai_akhir(self) -> int:
        return self._nilai_akhir

    @property
    def nilai_uas(self) -> int:
        return self._nilai_uas

    def __lt__(self, lain: "NilaiMahasiswa") -> bool:
        return self._nim < lain._nim  # urutan alami: NIM terkecil dulu

    def __str__(self) -> str:
        return f"{self._nim} {self._nama}"


def main():
    kelas = [
        NilaiMahasiswa("2409106003", "Citra Dewi", 88, 90),
        NilaiMahasiswa("2409106001", "Ayu Lestari", 88, 85),
        NilaiMahasiswa("2409106005", "Eka Putri", 75, 80),
        NilaiMahasiswa("2409106002", "Bima Saputra", 75, 80),
        NilaiMahasiswa("2409106004", "Dimas Pratama", 64, 60),
    ]

    print("=== URUT NIM (urutan alami) ===")
    for mhs in sorted(kelas):
        print(mhs)

    print()
    print("=== RANKING KELAS ===")
    ranking = sorted(kelas, key=lambda m: (-m.nilai_akhir, -m.nilai_uas, m.nama))
    for nomor, mhs in enumerate(ranking, start=1):
        print(f"{nomor}. {mhs.nama:<15}{mhs.nilai_akhir:>3} (UAS {mhs.nilai_uas})")

    print()
    lulus = [mhs.nama for mhs in ranking if mhs.nilai_akhir >= 70]
    print(f"Lulus (nilai akhir >= 70): {len(lulus)} orang")
    print(f"Peringkat 1: {ranking[0].nama}")


if __name__ == "__main__":
    main()
