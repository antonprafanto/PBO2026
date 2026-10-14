"""
Solusi Latihan 06 - Kamar Penginapan Wisma Tepian (Pewarisan Bertingkat)
Pertemuan 07 - Pewarisan (Inheritance)

Ide penyelesaian:
- Tiga tingkat: Kamar -> KamarDeluxe -> KamarSuite.
- Setiap tingkat meng-override hitung_biaya(malam) dan __str__(), dan SELALU
  memulai dari hasil versi induknya (super()). Jadi aturan tingkat bawah
  (validasi malam, tarif x malam) otomatis ikut berlaku di tingkat atas.
- KamarSuite tidak menambah atribut, sehingga tidak perlu menulis __init__:
  konstruktor KamarDeluxe diwarisi apa adanya.
- Semua uang berupa bilangan bulat; diskon dihitung dengan // 100.

Cara menjalankan:
    python latihan06_wisma_tepian.py
"""

SARAPAN_PER_TAMU = 50000  # per tamu per malam
ANTAR_JEMPUT = 150000  # sekali jalan, khusus suite
DISKON_PERSEN = 10  # diskon suite untuk menginap minimal 3 malam
MALAM_MINIMAL_DISKON = 3


def format_rupiah(angka: int) -> str:
    """Mengubah 300000 menjadi 'Rp300.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Kamar:
    """Tingkat 1: kamar standar."""

    def __init__(self, nomor: str, tarif: int):
        if tarif <= 0:
            raise ValueError("Tarif harus lebih dari 0")
        self._nomor = nomor
        self._tarif = tarif

    @property
    def nomor(self) -> str:
        return self._nomor

    def hitung_biaya(self, malam: int) -> int:
        if malam < 1:
            raise ValueError("Lama menginap minimal 1 malam")
        return self._tarif * malam

    def __str__(self) -> str:
        return f"Kamar {self._nomor} - {format_rupiah(self._tarif)}/malam"


class KamarDeluxe(Kamar):
    """Tingkat 2: kamar dengan sarapan untuk setiap tamu."""

    def __init__(self, nomor: str, tarif: int, jumlah_tamu: int):
        super().__init__(nomor, tarif)
        if jumlah_tamu < 1 or jumlah_tamu > 4:
            raise ValueError("Jumlah tamu harus 1 sampai 4")
        self._jumlah_tamu = jumlah_tamu

    def hitung_biaya(self, malam: int) -> int:
        biaya_kamar = super().hitung_biaya(malam)  # validasi malam ikut berjalan
        return biaya_kamar + SARAPAN_PER_TAMU * self._jumlah_tamu * malam

    def __str__(self) -> str:
        return f"{super().__str__()} | sarapan {self._jumlah_tamu} tamu"


class KamarSuite(KamarDeluxe):
    """Tingkat 3: deluxe + antar-jemput bandara + diskon menginap lama."""

    def hitung_biaya(self, malam: int) -> int:
        biaya = super().hitung_biaya(malam) + ANTAR_JEMPUT
        if malam >= MALAM_MINIMAL_DISKON:
            biaya -= biaya * DISKON_PERSEN // 100
        return biaya

    def __str__(self) -> str:
        return f"{super().__str__()} | antar-jemput bandara"


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    standar = Kamar("101", 300000)
    deluxe = KamarDeluxe("205", 450000, 2)
    suite = KamarSuite("301", 800000, 2)

    print("=== DAFTAR KAMAR WISMA TEPIAN ===")
    print(standar)
    print(deluxe)
    print(suite)

    print()
    print("=== RINCIAN BIAYA ===")
    print(f"Kamar {standar.nomor}, 2 malam: {format_rupiah(standar.hitung_biaya(2))}")
    print(f"Kamar {deluxe.nomor}, 2 malam: {format_rupiah(deluxe.hitung_biaya(2))}")
    print(f"Kamar {suite.nomor}, 2 malam: {format_rupiah(suite.hitung_biaya(2))}")
    print(f"Kamar {suite.nomor}, 3 malam: {format_rupiah(suite.hitung_biaya(3))}")

    print()
    print("=== CEK PEWARISAN ===")
    print(f"Kamar 301 adalah KamarDeluxe? {ya_tidak(isinstance(suite, KamarDeluxe))}")
    print(f"Kamar 301 adalah Kamar?       {ya_tidak(isinstance(suite, Kamar))}")
    print(f"Kamar 205 adalah KamarSuite?  {ya_tidak(isinstance(deluxe, KamarSuite))}")

    print()
    print("=== VALIDASI ===")
    try:
        suite.hitung_biaya(0)
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        KamarDeluxe("206", 450000, 6)
    except ValueError as e:
        print(f"Ditolak: {e}")


if __name__ == "__main__":
    main()
