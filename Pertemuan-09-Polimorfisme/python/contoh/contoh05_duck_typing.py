"""
Contoh 05 - Duck Typing: Tanpa Pewarisan pun Bisa
Pertemuan 09 - Polimorfisme

AyamJago, AlarmPonsel, Kentongan, dan BelSekolah TIDAK punya kelas induk
bersama. Satu-satunya kesamaan mereka: sama-sama punya method bunyikan().
Bagi Python, itu sudah cukup. Python tidak memeriksa "kamu kelas apa?",
melainkan "kamu bisa melakukan ini atau tidak?".

"Jika ia berjalan seperti bebek dan berbunyi seperti bebek,
 anggap saja ia bebek." Itulah asal nama duck typing.

Cara menjalankan:
    python contoh05_duck_typing.py
"""


class AyamJago:  # [1] tidak mewarisi kelas apa pun (selain object)
    def bunyikan(self) -> str:
        return "Kukuruyuuuk!"


class AlarmPonsel:
    def __init__(self, jam: str):
        self._jam = jam

    def bunyikan(self) -> str:
        return f"Kriiing! Sudah pukul {self._jam}"


class Kentongan:
    def bunyikan(self) -> str:
        return "Tung tung tung!"


class BelSekolah:  # [2] kelas baru, juga tanpa induk bersama
    def bunyikan(self) -> str:
        return "Teeet! Waktunya masuk kelas"


def bangunkan_semua(daftar: list):  # [3] tidak menyebut tipe khusus apa pun
    for benda in daftar:
        nama = type(benda).__name__
        print(f"{nama:<12}: {benda.bunyikan()}")  # [4] cukup punya bunyikan()


def main():
    print("=== PAGI DI ASRAMA ===")
    bangunkan_semua([AyamJago(), AlarmPonsel("05.00"), Kentongan()])

    print()
    print("=== PAGI DI SEKOLAH ===")
    bangunkan_semua([BelSekolah(), AlarmPonsel("06.45")])


if __name__ == "__main__":
    main()
