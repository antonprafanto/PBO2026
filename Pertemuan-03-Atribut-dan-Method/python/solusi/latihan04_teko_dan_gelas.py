"""
Solusi Latihan 04 - Teko dan Gelas
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- tuang_ke(tujuan, jumlah) menerima OBJEK Wadah lain sebagai parameter dan
  mengubah isi KEDUA objek. Banyaknya yang benar-benar dituang adalah nilai
  terkecil dari: yang diminta, isi sumber, dan sisa ruang di tujuan.
- kosong() dan penuh() adalah method boolean (jawabannya ya/tidak).
- gelas_tamu = gelas_bima TIDAK membuat gelas baru. Keduanya menunjuk objek
  yang sama, jadi minum lewat gelas_tamu ikut mengurangi isi gelas_bima.
- Nilai boolean tidak dicetak mentah; fungsi ya_tidak() mengubahnya menjadi
  teks "ya" atau "tidak".

Cara menjalankan:
    python latihan04_teko_dan_gelas.py
"""


class Wadah:
    """Wadah minuman (teko, gelas, botol) dengan kapasitas dalam ml."""

    def __init__(self, nama, kapasitas, isi=0):
        self.nama = nama
        self.kapasitas = kapasitas
        self.isi = isi

    def kosong(self):
        return self.isi == 0

    def penuh(self):
        return self.isi == self.kapasitas

    def sisa_ruang(self):
        return self.kapasitas - self.isi

    def tuang_ke(self, tujuan, jumlah):
        """Menuang ke wadah lain. Mengembalikan banyaknya ml yang dituang."""
        dituang = min(jumlah, self.isi, tujuan.sisa_ruang())
        self.isi = self.isi - dituang
        tujuan.isi = tujuan.isi + dituang  # mengubah objek yang dikirim
        return dituang

    def minum(self, jumlah):
        self.isi = max(0, self.isi - jumlah)

    def __str__(self):
        return f"{self.nama}: {self.isi}/{self.kapasitas} ml"


def ya_tidak(nilai):
    if nilai:
        return "ya"
    return "tidak"


def tuang(sumber, tujuan, jumlah):
    dituang = sumber.tuang_ke(tujuan, jumlah)
    print(f"{sumber.nama} -> {tujuan.nama}: diminta {jumlah} ml, dituang {dituang} ml")


def main():
    teko = Wadah("Teko", 1000, 900)
    gelas_ayu = Wadah("Gelas Ayu", 250)  # isi bawaan 0
    gelas_bima = Wadah("Gelas Bima", 250)

    print("=== KONDISI AWAL ===")
    print(teko)
    print(gelas_ayu)
    print(gelas_bima)

    print()
    print("=== MENUANG DARI TEKO ===")
    tuang(teko, gelas_ayu, 300)
    tuang(teko, gelas_bima, 200)
    tuang(teko, gelas_bima, 100)
    print(teko)
    print(f"Gelas Ayu penuh? {ya_tidak(gelas_ayu.penuh())}")
    print(f"Teko kosong? {ya_tidak(teko.kosong())}")

    print()
    print("=== GELAS BIMA DIPAKAI TAMU ===")
    gelas_tamu = gelas_bima  # bukan gelas baru, hanya nama lain
    gelas_tamu.minum(150)
    print("Tamu minum 150 ml")
    print(gelas_bima)
    print(f"Gelas Bima penuh? {ya_tidak(gelas_bima.penuh())}")


if __name__ == "__main__":
    main()
