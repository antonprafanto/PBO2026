"""
Contoh 01 - Kelas dan Objek Pertamamu
Pertemuan 02 - Kelas dan Objek

- Kelas Kucing adalah cetak biru (blueprint).
- oyen dan belang adalah dua objek (hasil cetakan) dari kelas Kucing.
- Atribut diisi dari luar dengan notasi titik: objek.atribut = nilai

Catatan: mengisi atribut dari luar seperti ini memang bisa di Python,
tetapi bukan kebiasaan yang baik. Di contoh 02 kita memakai konstruktor.

Cara menjalankan (dari folder python/contoh; macOS/Linux: python3):
    python contoh01_kelas_dan_objek.py
"""


class Kucing:  # [1] mendefinisikan kelas bernama Kucing
    """Cetak biru untuk semua kucing."""


def main():
    oyen = Kucing()  # [2] membuat objek pertama dari kelas Kucing
    oyen.nama = "Oyen"  # [3] mengisi atribut milik objek oyen
    oyen.warna = "oranye"

    belang = Kucing()  # objek kedua dari kelas yang SAMA
    belang.nama = "Belang"
    belang.warna = "hitam putih"

    print("=== DUA OBJEK DARI SATU KELAS ===")
    print(f"Kucing pertama: {oyen.nama}, warnanya {oyen.warna}")  # [4]
    print(f"Kucing kedua  : {belang.nama}, warnanya {belang.warna}")
    print(f"oyen dibuat dari kelas  : {type(oyen).__name__}")  # [5]
    print(f"belang dibuat dari kelas: {type(belang).__name__}")
    if oyen is belang:  # [6] apakah keduanya objek yang sama?
        print("oyen dan belang adalah objek yang sama")
    else:
        print("oyen dan belang adalah dua objek yang berbeda")


if __name__ == "__main__":
    main()
