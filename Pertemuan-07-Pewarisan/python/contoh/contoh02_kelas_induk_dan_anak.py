"""
Contoh 02 - Kelas Induk dan Kelas Anak
Pertemuan 07 - Pewarisan (Inheritance)

Kode kembar dari contoh 01 kini dikumpulkan di SATU kelas induk, Kendaraan.
Motor dan Mobil menjadi kelas anak: mereka mewarisi semua milik Kendaraan,
lalu hanya menulis bagian yang khusus milik mereka sendiri.
Output program ini SAMA PERSIS dengan contoh 01.

Cara menjalankan:
    python contoh02_kelas_induk_dan_anak.py
"""


class Kendaraan:  # [1] kelas induk: semua bagian yang SAMA dikumpulkan di sini
    """Kelas induk untuk semua kendaraan bermotor."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int):
        self._merek = merek
        self._plat_nomor = plat_nomor
        self._tahun = tahun

    @property
    def merek(self) -> str:
        return self._merek

    def info(self) -> str:
        return f"{self._merek} ({self._plat_nomor}) tahun {self._tahun}"

    def umur(self, tahun_sekarang: int) -> int:
        return tahun_sekarang - self._tahun


class Motor(Kendaraan):  # [2] Motor adalah Kendaraan
    """Sepeda motor: semua milik Kendaraan, ditambah jenis transmisi."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, transmisi: str):
        super().__init__(merek, plat_nomor, tahun)  # [3] bagian induk diisi induk
        self._transmisi = transmisi  # [4] atribut tambahan khusus motor

    def deskripsi(self) -> str:  # [5] method tambahan, memakai method warisan
        return f"Motor: {self.info()}, transmisi {self._transmisi}"


class Mobil(Kendaraan):
    """Mobil: semua milik Kendaraan, ditambah jumlah kursi."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, jumlah_kursi: int):
        super().__init__(merek, plat_nomor, tahun)
        self._jumlah_kursi = jumlah_kursi

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
    print(f"{beat.merek}: {beat.umur(2026)} tahun")  # [6] merek dan umur() warisan
    print(f"{avanza.merek}: {avanza.umur(2026)} tahun")


if __name__ == "__main__":
    main()
