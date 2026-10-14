"""
Contoh 01 - Masalah: Kode Kembar di Dua Kelas
Pertemuan 07 - Pewarisan (Inheritance)

Kelas Motor dan Mobil ditulis TERPISAH, tanpa pewarisan. Perhatikan betapa
banyak bagian yang sama persis: atribut merek, plat nomor, tahun, serta
method info() dan umur(). Di contoh 02, kita merapikannya dengan pewarisan.

Cara menjalankan:
    python contoh01_masalah_duplikasi.py
"""


class Motor:
    """Sepeda motor, ditulis tanpa pewarisan."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, transmisi: str):
        self._merek = merek  # [1] tiga atribut ini kembar dengan milik Mobil
        self._plat_nomor = plat_nomor
        self._tahun = tahun
        self._transmisi = transmisi  # [2] khusus motor: "matic" atau "manual"

    @property
    def merek(self) -> str:
        return self._merek

    def info(self) -> str:  # [3] method kembar
        return f"{self._merek} ({self._plat_nomor}) tahun {self._tahun}"

    def umur(self, tahun_sekarang: int) -> int:  # [3] method kembar
        return tahun_sekarang - self._tahun

    def deskripsi(self) -> str:
        return f"Motor: {self.info()}, transmisi {self._transmisi}"


class Mobil:
    """Mobil, ditulis tanpa pewarisan. Bandingkan baris demi baris dengan Motor!"""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, jumlah_kursi: int):
        self._merek = merek
        self._plat_nomor = plat_nomor
        self._tahun = tahun
        self._jumlah_kursi = jumlah_kursi  # khusus mobil

    @property
    def merek(self) -> str:
        return self._merek

    def info(self) -> str:
        return f"{self._merek} ({self._plat_nomor}) tahun {self._tahun}"

    def umur(self, tahun_sekarang: int) -> int:
        return tahun_sekarang - self._tahun

    def deskripsi(self) -> str:
        return f"Mobil: {self.info()}, {self._jumlah_kursi} kursi"


def main():
    beat = Motor("Honda Beat", "KT 1234 AB", 2020, "matic")
    avanza = Mobil("Toyota Avanza", "KT 5678 CD", 2018, 7)

    print("=== DAFTAR KENDARAAN ===")
    print(beat.deskripsi())
    print(avanza.deskripsi())

    print()
    print("=== UMUR DI TAHUN 2026 ===")
    print(f"{beat.merek}: {beat.umur(2026)} tahun")
    print(f"{avanza.merek}: {avanza.umur(2026)} tahun")


if __name__ == "__main__":
    main()
