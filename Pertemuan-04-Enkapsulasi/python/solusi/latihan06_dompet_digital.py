"""
Solusi Latihan 06 - Dompet Digital dengan Batas Harian
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- Ada empat data internal: _pemilik, _saldo, _batas_harian, dan
  _terpakai_hari_ini. Tidak ada satu pun yang punya setter.
- _terpakai_hari_ini bahkan tidak punya getter. Dari luar, yang terlihat
  hanyalah hasil hitungannya: sisa_batas_hari_ini.
- Saldo hanya berubah lewat isi_saldo() dan bayar().
  bayar() memeriksa TIGA aturan sekaligus: jumlah positif, saldo cukup,
  dan tidak melebihi sisa batas hari ini.
- ganti_hari() adalah satu-satunya cara mengembalikan pemakaian harian ke 0.

Cara menjalankan:
    python latihan06_dompet_digital.py
"""


class DompetDigital:
    """Dompet digital dengan batas pembayaran per hari."""

    ISI_MINIMAL = 10000

    def __init__(self, pemilik, batas_harian):
        if batas_harian <= 0:
            raise ValueError("Batas harian harus lebih dari 0")
        self._pemilik = pemilik
        self._saldo = 0
        self._batas_harian = batas_harian
        self._terpakai_hari_ini = 0  # tanpa getter dan tanpa setter

    @property
    def pemilik(self):
        return self._pemilik

    @property
    def saldo(self):
        return self._saldo

    @property
    def batas_harian(self):
        return self._batas_harian

    @property
    def sisa_batas_hari_ini(self):
        return self._batas_harian - self._terpakai_hari_ini

    def isi_saldo(self, jumlah):
        if jumlah < DompetDigital.ISI_MINIMAL:
            raise ValueError(f"Isi saldo minimal Rp{DompetDigital.ISI_MINIMAL}")
        self._saldo += jumlah

    def bayar(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah pembayaran harus lebih dari 0")
        if jumlah > self._saldo:
            raise ValueError(f"Saldo tidak cukup (saldo Rp{self._saldo})")
        if jumlah > self.sisa_batas_hari_ini:
            raise ValueError(
                f"Melebihi batas harian (sisa Rp{self.sisa_batas_hari_ini})")
        self._saldo -= jumlah
        self._terpakai_hari_ini += jumlah

    def ganti_hari(self):
        """Dipanggil saat hari berganti: pemakaian harian kembali ke 0."""
        self._terpakai_hari_ini = 0


def tampilkan(dompet):
    print(f"  Saldo Rp{dompet.saldo} | sisa batas hari ini "
          f"Rp{dompet.sisa_batas_hari_ini}")


def coba_bayar(dompet, jumlah, keterangan):
    try:
        dompet.bayar(jumlah)
        print(f"Bayar Rp{jumlah} ({keterangan}) berhasil")
    except ValueError as e:
        print(f"Bayar Rp{jumlah} ({keterangan}) ditolak: {e}")


def main():
    dompet = DompetDigital("Siti", 100000)

    print("=== HARI PERTAMA ===")
    tampilkan(dompet)
    dompet.isi_saldo(150000)
    print("Isi saldo Rp150000 berhasil")
    try:
        dompet.isi_saldo(5000)
    except ValueError as e:
        print(f"Isi saldo Rp5000 ditolak: {e}")
    coba_bayar(dompet, 45000, "makan siang")
    coba_bayar(dompet, 30000, "fotokopi modul")
    coba_bayar(dompet, 40000, "pulsa")
    tampilkan(dompet)

    print()
    print("=== HARI KEDUA ===")
    dompet.ganti_hari()
    tampilkan(dompet)
    coba_bayar(dompet, 40000, "pulsa")
    coba_bayar(dompet, 50000, "buku")
    coba_bayar(dompet, -10000, "uji coba curang")
    tampilkan(dompet)


if __name__ == "__main__":
    main()
