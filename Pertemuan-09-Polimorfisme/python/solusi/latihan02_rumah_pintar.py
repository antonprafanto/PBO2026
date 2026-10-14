"""
Solusi Latihan 02 - Rumah Pintar: Mode Tidur
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- status() di-override oleh Lampu dan AC, jadi menampilkan status semua
  perangkat cukup dengan satu perulangan (polimorfisme).
- Mode tidur butuh method KHUSUS: redupkan() hanya milik Lampu, atur_suhu()
  hanya milik AC. Karena itu jenis objek diperiksa dulu dengan isinstance()
  sebelum method khusus itu dipanggil. Perangkat lain cukup dimatikan.

Cara menjalankan:
    python latihan02_rumah_pintar.py
"""


class Perangkat:
    """Kelas induk semua perangkat rumah pintar."""

    def __init__(self, nama: str):
        self._nama = nama
        self._menyala = True

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def menyala(self) -> bool:
        return self._menyala

    def matikan(self):
        self._menyala = False
        print(f"{self._nama} dimatikan")

    def status(self) -> str:
        keadaan = "menyala" if self._menyala else "mati"
        return f"{self._nama}: {keadaan}"


class Lampu(Perangkat):
    def __init__(self, nama: str, kecerahan: int = 100):
        super().__init__(nama)
        self._kecerahan = kecerahan

    def redupkan(self, persen: int):  # method KHUSUS lampu
        self._kecerahan = persen
        print(f"{self._nama} diredupkan ke {persen}%")

    def status(self) -> str:
        if not self._menyala:
            return super().status()
        return f"{self._nama}: menyala {self._kecerahan}%"


class AC(Perangkat):
    def __init__(self, nama: str, suhu: int):
        super().__init__(nama)
        self._suhu = suhu

    def atur_suhu(self, derajat: int):  # method KHUSUS AC
        self._suhu = derajat
        print(f"{self._nama} diatur ke {derajat} derajat")

    def status(self) -> str:
        if not self._menyala:
            return super().status()
        return f"{self._nama}: menyala {self._suhu} derajat"


class Televisi(Perangkat):
    """Televisi tidak punya method khusus dan tidak meng-override status()."""


def tampilkan_status(daftar: list[Perangkat]):
    for perangkat in daftar:
        print(perangkat.status())  # polimorfisme: tanpa cek jenis


def mode_tidur(daftar: list[Perangkat]):
    for perangkat in daftar:
        if isinstance(perangkat, Lampu):  # cek jenis dulu ...
            perangkat.redupkan(10)  # ... baru panggil method khususnya
        elif isinstance(perangkat, AC):
            perangkat.atur_suhu(26)
        else:
            perangkat.matikan()


def main():
    rumah = [
        Lampu("Lampu Kamar"),
        AC("AC Kamar", 20),
        Televisi("Televisi"),
        Lampu("Lampu Teras"),
    ]
    print("=== SEBELUM MODE TIDUR ===")
    tampilkan_status(rumah)

    print()
    print("=== MODE TIDUR DIAKTIFKAN ===")
    mode_tidur(rumah)

    print()
    print("=== SESUDAH MODE TIDUR ===")
    tampilkan_status(rumah)


if __name__ == "__main__":
    main()
