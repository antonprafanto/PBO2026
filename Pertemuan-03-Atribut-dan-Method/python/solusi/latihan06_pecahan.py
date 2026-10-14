"""
Solusi Latihan 06 - Kelas Pecahan
Pertemuan 03 - Atribut dan Method Lebih Dalam

Ide penyelesaian:
- Konstruktor langsung menyederhanakan pecahan: pembilang dan penyebut
  dibagi dengan FPB keduanya. Jadi Pecahan(6, 8) tersimpan sebagai 3/4.
- fpb(a, b) adalah static method (algoritma Euclid). Ia tidak butuh data
  objek, hanya dua angka dari parameter.
- penyebut punya nilai bawaan 1, sehingga Pecahan(3) berarti 3/1 = 3.
- tambah() dan kali() menerima objek Pecahan lain dan MENGEMBALIKAN objek
  Pecahan BARU. Objek asalnya tidak diubah.
    a/b + c/d = (a*d + c*b) / (b*d)        a/b x c/d = (a*c) / (b*d)
- dari_teks("10/4") adalah class method (konstruktor alternatif).
- sama_dengan() membandingkan isi dua pecahan yang sudah disederhanakan.
- Pecahan di latihan ini selalu positif, agar semua pembagian bulat
  menghasilkan angka yang sama di Python maupun Java.

Cara menjalankan:
    python latihan06_pecahan.py
"""


class Pecahan:
    """Pecahan positif yang selalu disimpan dalam bentuk paling sederhana."""

    def __init__(self, pembilang, penyebut=1):
        faktor = Pecahan.fpb(pembilang, penyebut)
        self.pembilang = pembilang // faktor
        self.penyebut = penyebut // faktor

    @staticmethod
    def fpb(a, b):
        """Faktor persekutuan terbesar (FPB) dengan algoritma Euclid."""
        while b != 0:
            sisa = a % b
            a = b
            b = sisa
        return a

    @classmethod
    def dari_teks(cls, teks):
        """Membuat Pecahan dari teks seperti '3/4'."""
        pembilang, penyebut = teks.split("/")
        return cls(int(pembilang), int(penyebut))

    def tambah(self, lain):
        pembilang = self.pembilang * lain.penyebut + lain.pembilang * self.penyebut
        return Pecahan(pembilang, self.penyebut * lain.penyebut)

    def kali(self, lain):
        return Pecahan(self.pembilang * lain.pembilang, self.penyebut * lain.penyebut)

    def sama_dengan(self, lain):
        return self.pembilang == lain.pembilang and self.penyebut == lain.penyebut

    def __str__(self):
        if self.penyebut == 1:
            return f"{self.pembilang}"
        return f"{self.pembilang}/{self.penyebut}"


def ya_tidak(nilai):
    if nilai:
        return "ya"
    return "tidak"


def main():
    print("=== PENYEDERHANAAN OTOMATIS ===")
    print(f"6/8 -> {Pecahan(6, 8)}")
    print(f"10/5 -> {Pecahan(10, 5)}")
    print(f'Dari teks "10/4" -> {Pecahan.dari_teks("10/4")}')

    print()
    print("=== OPERASI MENGHASILKAN OBJEK BARU ===")
    setengah = Pecahan(1, 2)
    sepertiga = Pecahan(1, 3)
    print(f"{setengah} + {sepertiga} = {setengah.tambah(sepertiga)}")
    dua_pertiga = Pecahan(2, 3)
    tiga_perempat = Pecahan.dari_teks("3/4")
    print(f"{dua_pertiga} x {tiga_perempat} = {dua_pertiga.kali(tiga_perempat)}")
    seperempat = Pecahan(1, 4)
    print(f"{seperempat} + {tiga_perempat} = {seperempat.tambah(tiga_perempat)}")
    tiga = Pecahan(3)  # penyebut memakai nilai bawaan 1
    print(f"{tiga} + {setengah} = {tiga.tambah(setengah)}")
    print(f"Setengah tetap {setengah}")

    print()
    print("=== MEMBANDINGKAN ISI ===")
    hasil = Pecahan(2, 4).sama_dengan(setengah)
    print(f"2/4 sama dengan 1/2? {ya_tidak(hasil)}")
    hasil = sepertiga.sama_dengan(Pecahan(2, 5))
    print(f"1/3 sama dengan 2/5? {ya_tidak(hasil)}")


if __name__ == "__main__":
    main()
