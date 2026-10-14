"""
Solusi Latihan 02 - Kelas Ponsel
Pertemuan 02 - Kelas dan Objek

Ide penyelesaian:
- Atribut baterai berubah lewat method pakai() dan isi_daya().
- pakai(menit): setiap menit memakai 2% baterai. Jika baterai tidak cukup,
  baterai menjadi 0 dan ponsel mati.
- isi_daya(persen): baterai bertambah, tetapi tidak boleh lebih dari 100.

Cara menjalankan:
    python latihan02_ponsel.py
"""


class Ponsel:
    """Ponsel dengan baterai 0 sampai 100 persen."""

    def __init__(self, merek, baterai):
        self.merek = merek
        self.baterai = baterai

    def pakai(self, menit):
        kebutuhan = menit * 2
        if kebutuhan >= self.baterai:
            self.baterai = 0
            print(f"Dipakai {menit} menit... Baterai habis! Ponsel mati.")
        else:
            self.baterai = self.baterai - kebutuhan
            print(f"Dipakai {menit} menit, baterai berkurang {kebutuhan}%")

    def isi_daya(self, persen):
        self.baterai = self.baterai + persen
        if self.baterai > 100:
            self.baterai = 100
        print(f"Diisi daya {persen}%")

    def tampilkan_info(self):
        print(f"  Ponsel {self.merek} - baterai {self.baterai}%")


def main():
    hp = Ponsel("Samsung", 50)
    hp.tampilkan_info()
    hp.pakai(10)
    hp.tampilkan_info()
    hp.isi_daya(100)
    hp.tampilkan_info()
    hp.pakai(60)
    hp.tampilkan_info()


if __name__ == "__main__":
    main()
