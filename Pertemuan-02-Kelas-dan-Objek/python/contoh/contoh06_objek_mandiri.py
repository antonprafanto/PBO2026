"""
Contoh 06 - Setiap Objek Menyimpan Datanya Sendiri
Pertemuan 02 - Kelas dan Objek

Dua rekening dibuat dari kelas yang sama. Transaksi pada satu rekening
tidak memengaruhi rekening lain, karena setiap objek punya atribut sendiri.

Cara menjalankan:
    python contoh06_objek_mandiri.py
"""


class RekeningBank:
    """Rekening tabungan sederhana."""

    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.saldo = saldo_awal

    def setor(self, jumlah):
        self.saldo = self.saldo + jumlah
        print(f"{self.pemilik} setor Rp{jumlah}")

    def tarik(self, jumlah):
        if jumlah > self.saldo:
            print(f"{self.pemilik} gagal tarik Rp{jumlah}: saldo tidak cukup")
        else:
            self.saldo = self.saldo - jumlah
            print(f"{self.pemilik} tarik Rp{jumlah}")

    def cek_saldo(self):
        print(f"  Saldo {self.pemilik}: Rp{self.saldo}")


def main():
    rekening_budi = RekeningBank("Budi", 500000)
    rekening_siti = RekeningBank("Siti", 750000)

    print("=== SALDO AWAL ===")
    rekening_budi.cek_saldo()
    rekening_siti.cek_saldo()

    print()
    print("=== TRANSAKSI ===")
    rekening_budi.setor(200000)
    rekening_budi.tarik(1000000)
    rekening_siti.tarik(250000)

    print()
    print("=== SALDO AKHIR ===")
    rekening_budi.cek_saldo()
    rekening_siti.cek_saldo()


if __name__ == "__main__":
    main()
