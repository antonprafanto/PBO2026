"""
Contoh 02 - Satu Garis Bawah vs Dua Garis Bawah (Name Mangling)
Pertemuan 04 - Enkapsulasi
(Contoh ini khusus Python. Padanannya di Java: private + getter.)

- _pemilik (satu garis bawah): hanya KESEPAKATAN "ini urusan internal".
  Python tidak melarang siapa pun membacanya dari luar kelas.
- __pin (dua garis bawah): di dalam kelas, Python diam-diam MENGGANTI
  namanya menjadi _Brankas__pin. Proses ini disebut name mangling.
- Name mangling BUKAN pengamanan: nama barunya tetap bisa dibaca.

Cara menjalankan:
    python contoh02_name_mangling.py
"""


class Brankas:
    """Brankas sederhana: punya pemilik dan PIN."""

    def __init__(self, pemilik, pin):
        self._pemilik = pemilik  # [1] satu garis bawah: konvensi "internal"
        self.__pin = pin  # [2] dua garis bawah: namanya akan diganti oleh Python

    def buka(self, pin):
        if pin == self.__pin:  # [3] di DALAM kelas, __pin dipakai seperti biasa
            print(f"PIN benar. Brankas milik {self._pemilik} terbuka.")
        else:
            print("PIN salah. Brankas tetap terkunci.")


def ya_tidak(kondisi):
    """Mengubah True/False menjadi teks 'ya' atau 'tidak'."""
    if kondisi:
        return "ya"
    return "tidak"


def main():
    brankas = Brankas("Budi", "246810")

    print("=== MEMAKAI BRANKAS LEWAT METHOD ===")
    brankas.buka("123456")
    brankas.buka("246810")

    print()
    print("=== MENGINTIP DARI LUAR KELAS ===")
    print(f"brankas._pemilik      : {brankas._pemilik}")  # [4] tetap bisa dibaca
    print(f"Ada atribut '__pin'?  : {ya_tidak(hasattr(brankas, '__pin'))}")  # [5]
    print(f"Isi objek sebenarnya  : {vars(brankas)}")  # [6]

    print()
    print("=== NAME MANGLING BUKAN KEAMANAN ===")
    print(f"brankas._Brankas__pin : {brankas._Brankas__pin}")  # [7] PIN terbaca!


if __name__ == "__main__":
    main()
