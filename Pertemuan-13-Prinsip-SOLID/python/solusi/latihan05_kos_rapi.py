"""
Solusi Latihan 05 - Membongkar KosSerbaBisa (SRP + refactoring)
Pertemuan 13 - Prinsip SOLID

Ide penyelesaian:
- KosSerbaBisa punya empat tugas. Setiap tugas kini punya kelasnya sendiri:
    Kamar             -> data satu kamar (nomor, penghuni, sewa)
    PenghitungTagihan -> aturan denda dan total tagihan
    PencetakKuitansi  -> format kuitansi
    BukuKas           -> catatan pembayaran dan pemasukan
- PengelolaKos hanya mengatur URUTAN kerja. Rekan kerjanya disuntikkan lewat
  konstruktor, sehingga mudah diganti (misalnya pencetak kuitansi versi lain).
- Sengaja TIDAK dibuat ABC untuk setiap kelas: program sekecil ini belum
  membutuhkannya (ingat YAGNI). Abstraksi bisa ditambahkan saat ada kebutuhan.
- Refactor = perilaku tidak berubah: output program ini SAMA PERSIS dengan
  output KosSerbaBisa. Buktikan dengan fc (Windows) atau diff (macOS/Linux).

Cara menjalankan:
    python latihan05_kos_rapi.py
"""


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Kamar:
    """Data satu kamar kos."""

    def __init__(self, nomor: str, penghuni: str, sewa: int):
        self._nomor = nomor
        self._penghuni = penghuni
        self._sewa = sewa

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def penghuni(self) -> str:
        return self._penghuni

    @property
    def sewa(self) -> int:
        return self._sewa


class PenghitungTagihan:
    """Satu-satunya tempat aturan denda keterlambatan."""

    DENDA_PER_HARI = 10000
    DENDA_MAKSIMAL = 100000

    def denda(self, hari_terlambat: int) -> int:
        if hari_terlambat <= 0:
            return 0
        return min(hari_terlambat * PenghitungTagihan.DENDA_PER_HARI,
                   PenghitungTagihan.DENDA_MAKSIMAL)

    def total(self, kamar: Kamar, hari_terlambat: int) -> int:
        return kamar.sewa + self.denda(hari_terlambat)


class PencetakKuitansi:
    """Satu-satunya tempat format kuitansi."""

    def cetak(self, kamar: Kamar, hari_terlambat: int, denda: int, total: int):
        print(f"KUITANSI KOS MAWAR - KAMAR {kamar.nomor}")
        print(f"Penghuni : {kamar.penghuni}")
        print(f"Sewa     : {format_rupiah(kamar.sewa)}")
        if denda > 0:
            print(f"Denda    : {format_rupiah(denda)} ({hari_terlambat} hari)")
        print(f"Total    : {format_rupiah(total)}")
        print("-" * 30)


class BukuKas:
    """Mencatat setiap pembayaran yang masuk."""

    def __init__(self):
        self._daftar_total: list[int] = []

    def catat(self, total: int):
        self._daftar_total.append(total)

    def jumlah_transaksi(self) -> int:
        return len(self._daftar_total)

    def pemasukan(self) -> int:
        return sum(self._daftar_total)


class PengelolaKos:
    """Koordinator: mengatur urutan kerja, detailnya diserahkan ke rekan kerja."""

    def __init__(self, penghitung: PenghitungTagihan, pencetak: PencetakKuitansi,
                 buku_kas: BukuKas):
        self._daftar_kamar: dict[str, Kamar] = {}
        self._penghitung = penghitung
        self._pencetak = pencetak
        self._buku_kas = buku_kas

    def tambah_kamar(self, kamar: Kamar):
        self._daftar_kamar[kamar.nomor] = kamar

    def bayar(self, nomor: str, hari_terlambat: int):
        kamar = self._daftar_kamar[nomor]
        denda = self._penghitung.denda(hari_terlambat)
        total = self._penghitung.total(kamar, hari_terlambat)
        self._pencetak.cetak(kamar, hari_terlambat, denda, total)
        self._buku_kas.catat(total)


def main():
    buku_kas = BukuKas()
    kos = PengelolaKos(PenghitungTagihan(), PencetakKuitansi(), buku_kas)
    kos.tambah_kamar(Kamar("A1", "Ayu", 750000))
    kos.tambah_kamar(Kamar("A2", "Bima", 750000))
    kos.tambah_kamar(Kamar("B1", "Citra", 900000))

    kos.bayar("A1", 0)
    kos.bayar("B1", 3)
    kos.bayar("A2", 14)
    print(f"Kamar lunas: {buku_kas.jumlah_transaksi()}, "
          f"pemasukan: {format_rupiah(buku_kas.pemasukan())}")


if __name__ == "__main__":
    main()
