"""
Contoh 05 - Atribut Bergaris Bawah yang Dipakai Kelas Anak
Pertemuan 07 - Pewarisan (Inheritance)

Python tidak punya kata kunci protected. Sebagai gantinya, programmer Python
sepakat: atribut berawalan SATU garis bawah (_saldo) adalah urusan "internal"
kelas itu dan kelas-kelas anaknya. Kelas anak boleh memakainya langsung,
sedangkan kode di luar sebaiknya memakai pintu resmi (property atau method).

Cara menjalankan:
    python contoh05_akses_kelas_anak.py
"""


class RekeningBank:
    """Kelas induk rekening."""

    def __init__(self, pemilik: str, saldo_awal: int):
        self._pemilik = pemilik
        self._saldo = saldo_awal  # [1] satu garis bawah: internal kelas dan anaknya

    @property
    def saldo(self) -> int:  # [2] pintu resmi untuk membaca saldo dari luar
        return self._saldo

    def info(self) -> str:
        return f"Rekening {self._pemilik}: saldo Rp{self._saldo}"


class RekeningTabungan(RekeningBank):
    """Tabungan yang mendapat bunga bulanan (persen, bilangan bulat)."""

    def __init__(self, pemilik: str, saldo_awal: int, bunga_persen: int):
        super().__init__(pemilik, saldo_awal)
        self._bunga_persen = bunga_persen

    def tambah_bunga(self) -> int:
        bunga = self._saldo * self._bunga_persen // 100  # [3] membaca _saldo induk
        self._saldo += bunga  # [3] mengubah _saldo induk secara langsung
        return bunga


def main():
    tabungan = RekeningTabungan("Siti", 1000000, 2)

    print("=== TABUNGAN SITI ===")
    print(tabungan.info())
    print(f"Bunga bulan ini: Rp{tabungan.tambah_bunga()}")
    print(tabungan.info())

    print()
    print("=== DIBACA DARI LUAR KELAS ===")
    print(f"Lewat pintu resmi  : Rp{tabungan.saldo}")
    print(f"Langsung ke atribut: Rp{tabungan._saldo} (bisa, tetapi hindari)")  # [4]


if __name__ == "__main__":
    main()
