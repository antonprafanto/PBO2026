"""
Contoh 06 - Refactoring Aman: Struktur Berubah, Perilaku Tetap
Pertemuan 13 - Prinsip SOLID

DendaLama menghitung denda keterlambatan perpustakaan. Kodenya benar, tetapi
rumus yang sama ditulis tiga kali (melanggar DRY: Don't Repeat Yourself).

DendaBaru adalah hasil refactor: rumusnya ditulis SEKALI di AturanDenda,
dan setiap jenis pustaka cukup didaftarkan dengan tarif dan batas maksimalnya.

Bagian main() membuktikan refactor itu aman: kedua versi dijalankan dengan
banyak kasus, lalu hasilnya dibandingkan satu per satu.

Cara menjalankan:
    python contoh06_refactor_aman.py
"""


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


# ---------------------------------------------------------- SEBELUM REFACTOR
class DendaLama:
    def hitung(self, jenis: str, hari_terlambat: int) -> int:
        if jenis == "buku":
            if hari_terlambat <= 0:
                return 0
            denda = hari_terlambat * 1000
            if denda > 20000:
                denda = 20000
            return denda
        elif jenis == "majalah":  # [1] pola yang sama ditulis ulang...
            if hari_terlambat <= 0:
                return 0
            denda = hari_terlambat * 500
            if denda > 10000:
                denda = 10000
            return denda
        elif jenis == "referensi":  # ...dan ditulis ulang lagi
            if hari_terlambat <= 0:
                return 0
            denda = hari_terlambat * 5000
            if denda > 50000:
                denda = 50000
            return denda
        return 0


# ---------------------------------------------------------- SESUDAH REFACTOR
class AturanDenda:
    """Satu rumus denda untuk semua jenis pustaka."""

    def __init__(self, tarif_per_hari: int, denda_maksimal: int):
        self._tarif_per_hari = tarif_per_hari
        self._denda_maksimal = denda_maksimal

    def hitung(self, hari_terlambat: int) -> int:  # [2] rumus ditulis SEKALI
        if hari_terlambat <= 0:
            return 0
        return min(hari_terlambat * self._tarif_per_hari, self._denda_maksimal)


class DendaBaru:
    def __init__(self):
        self._aturan = {  # [3] jenis baru cukup ditambah satu baris
            "buku": AturanDenda(1000, 20000),
            "majalah": AturanDenda(500, 10000),
            "referensi": AturanDenda(5000, 50000),
        }

    def hitung(self, jenis: str, hari_terlambat: int) -> int:
        if jenis not in self._aturan:
            return 0  # [4] perilaku lama dipertahankan, termasuk yang ini
        return self._aturan[jenis].hitung(hari_terlambat)


def main():
    lama = DendaLama()
    baru = DendaBaru()
    kasus = [  # [5] daftar kasus uji: (jenis, hari terlambat)
        ("buku", 0), ("buku", 3), ("buku", 25),
        ("majalah", 4), ("majalah", 30),
        ("referensi", 2), ("referensi", 12),
        ("komik", 5),
    ]

    print("=== MEMBANDINGKAN SEBELUM DAN SESUDAH REFACTOR ===")
    print(f"{'jenis':<10}{'hari':>4}{'lama':>10}{'baru':>10}   hasil")
    jumlah_sama = 0
    for jenis, hari in kasus:
        hasil_lama = lama.hitung(jenis, hari)
        hasil_baru = baru.hitung(jenis, hari)
        if hasil_lama == hasil_baru:  # [6] bukti: hasil harus sama persis
            jumlah_sama += 1
            status = "sama"
        else:
            status = "BEDA"
        print(f"{jenis:<10}{hari:>4}{format_rupiah(hasil_lama):>10}"
              f"{format_rupiah(hasil_baru):>10}   {status}")

    print(f"Kasus diuji: {len(kasus)}, sama: {jumlah_sama}, "
          f"beda: {len(kasus) - jumlah_sama}")
    if jumlah_sama == len(kasus):
        print("Kesimpulan: refactor aman, perilaku tidak berubah.")
    else:
        print("Kesimpulan: ADA perilaku yang berubah, periksa lagi!")


if __name__ == "__main__":
    main()
