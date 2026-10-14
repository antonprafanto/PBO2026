"""
Contoh 07 - Exception Buatan Sendiri dan Exception Chaining
Pertemuan 11 - Exception Handling

Exception hanyalah KELAS. Kita bisa membuat jenis baru dengan PEWARISAN:

    Exception                (bawaan Python)
    +-- RekeningError        (induk semua error rekening)
        +-- SaldoTidakCukupError   (membawa data: saldo, diminta, kekurangan)
        +-- TransferGagalError

- Penangkap boleh memilih: tangkap yang spesifik, atau tangkap induknya.
- Exception boleh membawa DATA TAMBAHAN, bukan hanya pesan.
- "raise ... from e" (exception chaining) melempar exception baru sambil
  menyimpan exception lama sebagai PENYEBAB-nya (e.__cause__).

Cara menjalankan:
    python contoh07_exception_buatan_sendiri.py
"""


class RekeningError(Exception):  # [1] turunan Exception
    """Induk semua error yang berhubungan dengan rekening."""


class SaldoTidakCukupError(RekeningError):  # [2] turunan RekeningError
    """Dilempar saat saldo tidak cukup untuk penarikan."""

    def __init__(self, saldo: int, diminta: int):
        super().__init__(f"Saldo tidak cukup: saldo Rp{saldo}, "
                         f"diminta Rp{diminta}")  # [3] pesan untuk str(e)
        self.saldo = saldo  # [4] data tambahan untuk penangkap
        self.diminta = diminta

    @property
    def kekurangan(self) -> int:
        return self.diminta - self.saldo


class TransferGagalError(RekeningError):
    """Dilempar saat transfer tidak bisa diselesaikan."""


class Rekening:
    """Rekening tabungan sederhana."""

    def __init__(self, pemilik: str, saldo: int):
        self._pemilik = pemilik
        self._saldo = saldo

    @property
    def pemilik(self) -> str:
        return self._pemilik

    @property
    def saldo(self) -> int:
        return self._saldo

    def tarik(self, jumlah: int):
        if jumlah > self._saldo:
            raise SaldoTidakCukupError(self._saldo, jumlah)  # [5]
        self._saldo -= jumlah

    def setor(self, jumlah: int):
        self._saldo += jumlah


def transfer(asal: Rekening, tujuan: Rekening, jumlah: int):
    try:
        asal.tarik(jumlah)
    except SaldoTidakCukupError as e:
        pesan = f"Transfer {asal.pemilik} ke {tujuan.pemilik} gagal"
        raise TransferGagalError(pesan) from e  # [6] simpan penyebab aslinya
    tujuan.setor(jumlah)
    print(f"Transfer Rp{jumlah} dari {asal.pemilik} ke {tujuan.pemilik} berhasil")


def main():
    budi = Rekening("Budi", 500000)
    siti = Rekening("Siti", 100000)

    print("=== TARIK TUNAI ===")
    for jumlah in [200000, 400000]:
        try:
            budi.tarik(jumlah)
            print(f"Tarik Rp{jumlah} berhasil, sisa saldo Rp{budi.saldo}")
        except SaldoTidakCukupError as e:  # [7] tangkap yang spesifik
            print(f"Gagal: {e}")
            print(f"  Kurang Rp{e.kekurangan}. Coba tarik paling banyak "
                  f"Rp{e.saldo}.")  # [8] memakai data tambahan

    print()
    print("=== TRANSFER ===")
    for asal, tujuan, jumlah in [(budi, siti, 50000), (siti, budi, 250000)]:
        try:
            transfer(asal, tujuan, jumlah)
        except RekeningError as e:  # [9] tangkap induknya: semua error rekening
            print(f"Gagal: {e}")
            print(f"  Penyebab: {e.__cause__}")  # [10] exception lama tersimpan

    print()
    print(f"Saldo akhir: Budi Rp{budi.saldo}, Siti Rp{siti.saldo}")


if __name__ == "__main__":
    main()
