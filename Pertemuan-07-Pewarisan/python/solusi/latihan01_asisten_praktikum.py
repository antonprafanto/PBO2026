"""
Solusi Latihan 01 - Mahasiswa dan Asisten Praktikum
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
1. Mahasiswa adalah kelas induk: menyimpan NIM dan nama, punya perkenalan().
2. AsistenPraktikum(Mahasiswa) memanggil super().__init__(nim, nama), lalu
   menambah atribut praktikum dan method tugas().
3. perkenalan() TIDAK ditulis ulang di AsistenPraktikum, tetapi tetap bisa
   dipanggil karena diwarisi dari Mahasiswa.

Cara menjalankan:
    python latihan01_asisten_praktikum.py
"""


class Mahasiswa:
    """Mahasiswa dengan NIM dan nama."""

    def __init__(self, nim: str, nama: str):
        self._nim = nim
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def perkenalan(self) -> str:
        return f"Halo, saya {self._nama} (NIM {self._nim})"


class AsistenPraktikum(Mahasiswa):
    """Mahasiswa yang juga menjadi asisten sebuah praktikum."""

    def __init__(self, nim: str, nama: str, praktikum: str):
        super().__init__(nim, nama)  # bagian Mahasiswa diisi oleh Mahasiswa
        self._praktikum = praktikum  # atribut tambahan

    def tugas(self) -> str:
        return f"{self.nama} mengasisteni praktikum {self._praktikum}"


def main():
    bima = Mahasiswa("2409106002", "Bima Saputra")
    ayu = AsistenPraktikum("2309106001", "Ayu Lestari",
                           "Pemrograman Berorientasi Objek")

    print("=== MAHASISWA BIASA ===")
    print(bima.perkenalan())

    print()
    print("=== ASISTEN PRAKTIKUM ===")
    print(ayu.perkenalan())  # method warisan dari Mahasiswa
    print(ayu.tugas())  # method tambahan milik AsistenPraktikum
    jawaban = "ya" if isinstance(ayu, Mahasiswa) else "tidak"
    print(f"{ayu.nama} termasuk Mahasiswa? {jawaban}")


if __name__ == "__main__":
    main()
