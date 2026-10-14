"""
Solusi Latihan 02 - Jam Digital yang Menolak Waktu Mustahil
Pertemuan 11 - Exception Handling

Ide penyelesaian:
- atur(jam, menit) MEMERIKSA dulu, baru mengubah atribut. Jika jam atau
  menit di luar batas, lempar ValueError berisi pesan yang jelas. Karena
  pemeriksaan dilakukan sebelum perubahan, waktu lama tetap utuh.
- Di main(), tampilan jam dicetak di blok finally, sehingga SELALU muncul,
  baik pengaturan berhasil maupun ditolak.

Cara menjalankan:
    python latihan02_jam_digital.py
"""


class JamDigital:
    """Jam digital 24 jam. Waktu awal 00:00."""

    def __init__(self):
        self._jam = 0
        self._menit = 0

    def atur(self, jam: int, menit: int):
        if jam < 0 or jam > 23:
            raise ValueError("jam harus 0 sampai 23")
        if menit < 0 or menit > 59:
            raise ValueError("menit harus 0 sampai 59")
        self._jam = jam  # hanya sampai di sini jika keduanya valid
        self._menit = menit

    def tampilan(self) -> str:
        return f"{self._jam:02d}:{self._menit:02d}"


def main():
    jam_dinding = JamDigital()
    print("=== JAM DIGITAL ===")
    print(f"Tampilan awal: {jam_dinding.tampilan()}")
    percobaan = [(7, 30), (25, 0), (12, 75), (23, 59), (-1, 10)]
    for jam, menit in percobaan:
        try:
            jam_dinding.atur(jam, menit)
            print(f"Atur ke jam {jam} menit {menit} -> berhasil")
        except ValueError as e:
            print(f"Atur ke jam {jam} menit {menit} -> ditolak: {e}")
        finally:
            print(f"  Tampilan jam: {jam_dinding.tampilan()}")


if __name__ == "__main__":
    main()
