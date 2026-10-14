"""
Contoh 01 - Satu Perintah, Banyak Bentuk
Pertemuan 09 - Polimorfisme

Kucing, Anjing, dan Bebek meng-override method bersuara() milik Hewan.
Perintahnya SAMA (hewan.bersuara()), tetapi hasilnya BERBEDA, tergantung
objek apa yang sebenarnya ditunjuk oleh variabel. Ikan tidak meng-override,
jadi Ikan memakai versi milik induknya.

Cara menjalankan:
    python contoh01_satu_perintah_banyak_bentuk.py
"""


class Hewan:
    """Kelas induk semua hewan."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def bersuara(self) -> str:
        return "(diam saja)"  # [1] versi umum milik induk


class Kucing(Hewan):
    def bersuara(self) -> str:  # [2] override: versi khusus kucing
        return "Meong!"


class Anjing(Hewan):
    def bersuara(self) -> str:
        return "Guk guk!"


class Bebek(Hewan):
    def bersuara(self) -> str:
        return "Kwek kwek!"


class Ikan(Hewan):
    """Ikan tidak meng-override bersuara(), jadi memakai versi Hewan."""


def suruh_bersuara(hewan: Hewan):  # [3] parameter bertipe kelas induk
    jenis = type(hewan).__name__
    print(f"{hewan.nama} si {jenis}: {hewan.bersuara()}")  # [4]


def main():
    print("=== SATU VARIABEL, BERGANTI OBJEK ===")
    hewan = Kucing("Oyen")  # [5] variabel hewan menunjuk objek Kucing
    print(hewan.bersuara())
    hewan = Anjing("Bruno")  # sekarang menunjuk objek Anjing
    print(hewan.bersuara())  # baris yang sama persis, hasilnya berbeda

    print()
    print("=== SATU PERINTAH UNTUK SEMUA HEWAN ===")
    kebun = [Kucing("Oyen"), Anjing("Bruno"), Bebek("Kuning"), Ikan("Koki")]  # [6]
    for satwa in kebun:
        suruh_bersuara(satwa)


if __name__ == "__main__":
    main()
