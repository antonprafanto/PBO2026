"""
Contoh 04 - Polimorfisme dari dalam Kelas
Pertemuan 09 - Polimorfisme

Method tulis() hanya ditulis SEKALI, di kelas induk KartuUcapan. Di dalamnya,
tulis() memanggil self.salam() dan self.isi(). Karena self selalu menunjuk
objek yang sebenarnya, versi salam() dan isi() yang berjalan adalah milik
kelas anak (jika kelas anak meng-override-nya).

Cara menjalankan:
    python contoh04_polimorfisme_dari_dalam_kelas.py
"""


class KartuUcapan:
    """Kartu ucapan umum. Kerangka tulis() sama untuk semua jenis kartu."""

    def __init__(self, penerima: str, pengirim: str):
        self._penerima = penerima
        self._pengirim = pengirim

    def salam(self) -> str:
        return f"Halo, {self._penerima}!"

    def isi(self) -> str:
        return "Semoga harimu menyenangkan."

    def tulis(self):  # [1] method induk yang memanggil method lain lewat self
        print("-" * 40)
        print(self.salam())  # [2] versi siapa? tergantung objek self
        print(self.isi())
        print(f"Salam hangat, {self._pengirim}")
        print("-" * 40)


class KartuUlangTahun(KartuUcapan):
    def __init__(self, penerima: str, pengirim: str, umur: int):
        super().__init__(penerima, pengirim)
        self._umur = umur

    def isi(self) -> str:  # [3] hanya isi() yang di-override
        return f"Selamat ulang tahun yang ke-{self._umur}!"


class KartuWisuda(KartuUcapan):
    def salam(self) -> str:  # [4] salam() dan isi() sama-sama di-override
        return f"Selamat, {self._penerima}, S.Kom.!"

    def isi(self) -> str:
        return "Perjuanganmu terbayar lunas. " + super().isi()  # [5]


def main():
    daftar_kartu = [
        KartuUcapan("Siti", "Budi"),
        KartuUlangTahun("Rina", "Ayu", 20),
        KartuWisuda("Dimas", "Keluarga di Samarinda"),
    ]
    for nomor, kartu in enumerate(daftar_kartu, start=1):
        if nomor > 1:
            print()
        print(f"=== Kartu {nomor}: {type(kartu).__name__} ===")
        kartu.tulis()  # [6] tulis() milik induk, hasilnya berbeda-beda


if __name__ == "__main__":
    main()
