"""
Contoh 01 - Data Bocor vs Data Terlindungi
Pertemuan 04 - Enkapsulasi

- TabunganBocor: saldo adalah atribut biasa. Kode di luar kelas bebas
  mengubahnya, termasuk membuatnya negatif atau "menyulap" saldo.
- TabunganAman: saldo disimpan di atribut _saldo (garis bawah = urusan
  internal kelas). Saldo hanya berubah lewat method setor() dan tarik()
  yang memeriksa aturan lebih dulu.

Cara menjalankan:
    python contoh01_data_bocor.py
"""


class TabunganBocor:
    """Tabungan tanpa perlindungan: atribut saldo bisa diubah siapa saja."""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo  # [1] atribut biasa, bebas diubah dari luar kelas


class TabunganAman:
    """Tabungan yang menjaga saldonya sendiri."""

    def __init__(self, pemilik, saldo):
        self._pemilik = pemilik
        self._saldo = saldo  # [2] garis bawah: "urusan internal, jangan disentuh"

    def setor(self, jumlah):  # [3] pintu resmi untuk menambah saldo
        if jumlah <= 0:
            print(f"Setor Rp{jumlah} ditolak: jumlah harus lebih dari 0")
        else:
            self._saldo += jumlah
            print(f"Setor Rp{jumlah} berhasil")

    def tarik(self, jumlah):  # [4] pintu resmi untuk mengurangi saldo
        if jumlah <= 0:
            print(f"Tarik Rp{jumlah} ditolak: jumlah harus lebih dari 0")
        elif jumlah > self._saldo:
            print(f"Tarik Rp{jumlah} ditolak: saldo tidak cukup")
        else:
            self._saldo -= jumlah
            print(f"Tarik Rp{jumlah} berhasil")

    def cek_saldo(self):
        print(f"  Saldo {self._pemilik}: Rp{self._saldo}")


def main():
    print("=== TABUNGAN BOCOR ===")
    bocor = TabunganBocor("Budi", 500000)
    print(f"Saldo awal Budi: Rp{bocor.saldo}")
    bocor.saldo = bocor.saldo - 2000000  # [5] tarik melebihi saldo, tidak dicegah
    print(f"Setelah ditarik Rp2000000: Rp{bocor.saldo}")
    bocor.saldo = 999999999  # [6] saldo "disulap" langsung dari luar kelas
    print(f"Setelah disulap: Rp{bocor.saldo}")

    print()
    print("=== TABUNGAN AMAN ===")
    aman = TabunganAman("Siti", 500000)
    aman.cek_saldo()
    aman.tarik(2000000)  # [7] semua perubahan lewat method, aturan selalu dicek
    aman.setor(-100000)
    aman.setor(250000)
    aman.tarik(100000)
    aman.cek_saldo()


if __name__ == "__main__":
    main()
