"""
Solusi Latihan 02 - Nilai Mata Kuliah
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- angka punya getter dan setter. Setter menolak angka di luar 0-100.
- huruf dan lulus adalah property TANPA setter yang DIHITUNG dari angka.
  Keduanya tidak disimpan di atribut, sehingga selalu cocok dengan angka.
  (Kalau huruf disimpan terpisah, bisa saja angka berubah tetapi huruf lupa
  diperbarui. Data jadi tidak konsisten.)
- Konstruktor mengisi angka lewat setter.

Cara menjalankan:
    python latihan02_nilai_mata_kuliah.py
"""


class NilaiMataKuliah:
    """Nilai angka (0-100) satu mata kuliah."""

    BATAS_LULUS = 60

    def __init__(self, mata_kuliah, angka):
        self._mata_kuliah = mata_kuliah
        self.angka = angka  # lewat setter, jadi ikut diperiksa

    @property
    def mata_kuliah(self):
        return self._mata_kuliah

    @property
    def angka(self):
        return self._angka

    @angka.setter
    def angka(self, nilai):
        if nilai < 0 or nilai > 100:
            raise ValueError(f"Nilai harus 0-100, bukan {nilai}")
        self._angka = nilai

    @property
    def huruf(self):
        """Huruf mutu, dihitung dari angka (read-only)."""
        if self._angka >= 80:
            return "A"
        elif self._angka >= 70:
            return "B"
        elif self._angka >= 60:
            return "C"
        elif self._angka >= 50:
            return "D"
        else:
            return "E"

    @property
    def lulus(self):
        """True jika angka mencapai batas lulus (read-only)."""
        return self._angka >= NilaiMataKuliah.BATAS_LULUS

    def __str__(self):
        if self.lulus:
            keterangan = "lulus"
        else:
            keterangan = "belum lulus"
        return f"{self._mata_kuliah}: {self._angka} ({self.huruf}) - {keterangan}"


def main():
    pbo = NilaiMataKuliah("Pemrograman Berorientasi Objek", 85)
    basis_data = NilaiMataKuliah("Basis Data", 58)
    print("=== NILAI SEMESTER ===")
    print(pbo)
    print(basis_data)

    print()
    print("=== SETELAH PERBAIKAN NILAI ===")
    basis_data.angka = 72
    print(basis_data)

    print()
    print("=== INPUT NILAI SALAH ===")
    try:
        basis_data.angka = 105
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        NilaiMataKuliah("Statistika", -5)
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(basis_data)


if __name__ == "__main__":
    main()
