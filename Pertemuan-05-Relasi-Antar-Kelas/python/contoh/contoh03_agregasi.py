"""
Contoh 03 - Agregasi: Kumpulan Objek yang Bisa Hidup Sendiri
Pertemuan 05 - Relasi Antar Kelas

Tim MENGUMPULKAN objek Pemain yang dibuat di luar tim. Satu pemain boleh
ikut dua tim, dan pemain tetap ada walaupun salah satu timnya bubar.

Cara menjalankan:
    python contoh03_agregasi.py
"""


class Pemain:
    """Pemain futsal. Ia bisa ada tanpa tim mana pun."""

    def __init__(self, nama: str, posisi: str):
        self._nama = nama
        self._posisi = posisi

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"{self._nama} ({self._posisi})"


class Tim:
    """Tim futsal yang mengumpulkan pemain-pemain yang sudah ada."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_pemain: list[Pemain] = []  # [1] list kosong: 0 pemain

    def rekrut(self, pemain: Pemain):  # [2] menerima OBJEK yang sudah jadi
        self._daftar_pemain.append(pemain)
        print(f"{pemain.nama} bergabung dengan {self._nama}")

    def jumlah_pemain(self) -> int:
        return len(self._daftar_pemain)

    def tampilkan(self):
        print(f"{self._nama} ({self.jumlah_pemain()} pemain):")
        for nomor, pemain in enumerate(self._daftar_pemain, start=1):  # [3]
            print(f"  {nomor}. {pemain}")


def main():
    andi = Pemain("Andi", "kiper")  # [4] pemain lahir lebih dulu, tanpa tim
    bayu = Pemain("Bayu", "anchor")
    candra = Pemain("Candra", "pivot")
    tim_kelas = Tim("Tim Kelas TI-A")
    tim_fakultas = Tim("Tim Fakultas")

    print("=== MEMBENTUK TIM ===")
    tim_kelas.rekrut(andi)
    tim_kelas.rekrut(bayu)
    tim_kelas.rekrut(candra)
    tim_fakultas.rekrut(bayu)  # [5] satu pemain boleh ikut dua tim

    print()
    tim_kelas.tampilkan()
    tim_fakultas.tampilkan()

    print()
    print("=== TIM KELAS DIBUBARKAN ===")
    tim_kelas = None  # [6] objek tim dilepas, pemain tidak ikut hilang
    print(f"Pemain tetap ada: {andi}, {bayu}, {candra}")
    tim_fakultas.tampilkan()


if __name__ == "__main__":
    main()
