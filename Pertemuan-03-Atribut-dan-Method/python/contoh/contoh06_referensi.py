"""
Contoh 06 - Referensi dan Aliasing
Pertemuan 03 - Atribut dan Method Lebih Dalam

Variabel TIDAK menyimpan objek, melainkan REFERENSI (penunjuk) ke objek.
- b = a   -> b menunjuk objek yang SAMA dengan a (aliasing), tidak ada salinan
- a is b  -> True jika a dan b menunjuk objek yang sama
- None    -> nilai khusus untuk variabel yang tidak menunjuk objek apa pun

Cara menjalankan:
    python contoh06_referensi.py
"""


class Ponsel:
    """Ponsel dengan persentase baterai."""

    def __init__(self, pemilik, baterai):
        self.pemilik = pemilik
        self.baterai = baterai

    def pakai(self, persen):
        self.baterai = self.baterai - persen


def main():
    print("=== DUA VARIABEL, SATU OBJEK ===")
    ponsel_budi = Ponsel("Budi", 80)
    ponsel_dipinjam = ponsel_budi  # [1] TIDAK membuat ponsel baru
    ponsel_dipinjam.pakai(30)  # [2] Siti memakai ponsel yang ia pinjam
    print(f"Baterai dilihat lewat variabel peminjam: {ponsel_dipinjam.baterai}%")
    print(f"Baterai dilihat lewat variabel pemilik : {ponsel_budi.baterai}%")  # [3]
    if ponsel_budi is ponsel_dipinjam:  # [4] apakah objeknya sama?
        print("Keduanya menunjuk objek yang SAMA")
    else:
        print("Keduanya menunjuk objek yang berbeda")

    print()
    print("=== DUA OBJEK DENGAN DATA KEMBAR ===")
    ponsel_a = Ponsel("Rina", 50)
    ponsel_b = Ponsel("Rina", 50)  # [5] objek baru, walaupun datanya kembar
    if ponsel_a is ponsel_b:
        print("Ponsel A dan ponsel B menunjuk objek yang SAMA")
    else:
        print("Ponsel A dan ponsel B menunjuk objek yang berbeda")
    ponsel_a.pakai(10)
    print(f"Baterai ponsel A: {ponsel_a.baterai}%, ponsel B: {ponsel_b.baterai}%")

    print()
    print("=== VARIABEL TANPA OBJEK ===")
    ponsel_dimas = None  # [6] Dimas belum punya ponsel
    if ponsel_dimas is None:  # [7] cara memeriksa None
        print("Dimas belum punya ponsel")
    ponsel_dipinjam = None  # [8] Siti mengembalikan ponsel: "label"-nya dilepas
    print(f"Ponsel Budi tetap ada, baterainya {ponsel_budi.baterai}%")


if __name__ == "__main__":
    main()
