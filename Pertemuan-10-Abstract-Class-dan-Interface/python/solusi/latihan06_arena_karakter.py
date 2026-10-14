"""
Solusi Latihan 06 - Arena Karakter: Kelas Abstrak + Interface
Pertemuan 10 - Abstract Class dan Interface

Ide penyelesaian:
- Karakter adalah kelas abstrak (is-a): menyimpan nama dan HP, punya method
  konkret terima_serangan(), pulihkan(), masih_hidup(), dan serang().
- serang() adalah template method: aturan "yang tumbang tidak bisa
  menyerang" ditulis sekali, lalu besar serangan ditanyakan ke method
  abstrak kekuatan_serangan() milik kelas anak.
- BisaMenyembuhkan adalah "interface" (can-do). Penyihir (sebuah Karakter)
  dan RamuanObat (BUKAN Karakter) sama-sama memenuhinya sehingga
  fase_penyembuhan() bisa memakai keduanya.

Cara menjalankan:
    python latihan06_arena_karakter.py
"""

from abc import ABC, abstractmethod


class Karakter(ABC):
    """Kelas abstrak untuk semua karakter di arena."""

    def __init__(self, nama: str, hp_maks: int):
        self._nama = nama
        self._hp_maks = hp_maks
        self._hp = hp_maks

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def hp(self) -> int:
        return self._hp

    @abstractmethod
    def peran(self) -> str:
        """Nama peran, misalnya 'Ksatria'."""

    @abstractmethod
    def kekuatan_serangan(self) -> int:
        """Besar HP lawan yang berkurang setiap kali menyerang."""

    def masih_hidup(self) -> bool:
        return self._hp > 0

    def terima_serangan(self, jumlah: int):
        self._hp = max(0, self._hp - jumlah)

    def pulihkan(self, jumlah: int) -> int:
        """Menambah HP tanpa melewati HP maksimal. Mengembalikan HP yang naik."""
        sebelum = self._hp
        self._hp = min(self._hp_maks, self._hp + jumlah)
        return self._hp - sebelum

    # Tanda kutip pada "Karakter": kelas ini belum selesai didefinisikan.
    def serang(self, lawan: "Karakter"):
        """Template method: urutan dan aturannya sama untuk semua peran."""
        if not self.masih_hidup():
            print(f"{self._nama} sudah tumbang dan tidak bisa menyerang")
            return
        kekuatan = self.kekuatan_serangan()
        lawan.terima_serangan(kekuatan)
        print(f"{self._nama} menyerang {lawan.nama}: -{kekuatan} HP "
              f"(sisa {lawan.hp})")

    def __str__(self) -> str:
        teks = f"{self.peran()} {self._nama}: HP {self._hp}/{self._hp_maks}"
        if not self.masih_hidup():
            teks += " (tumbang)"
        return teks


class BisaMenyembuhkan(ABC):
    """Kontrak: bisa memulihkan HP sebuah karakter."""

    @abstractmethod
    def sembuhkan(self, target: Karakter):
        """Memulihkan HP target."""


class Ksatria(Karakter):
    """Ksatria: HP besar, serangan sedang."""

    def __init__(self, nama: str):
        super().__init__(nama, 100)

    def peran(self) -> str:
        return "Ksatria"

    def kekuatan_serangan(self) -> int:
        return 20


class Pemanah(Karakter):
    """Pemanah: HP sedang, serangan kecil."""

    def __init__(self, nama: str):
        super().__init__(nama, 60)

    def peran(self) -> str:
        return "Pemanah"

    def kekuatan_serangan(self) -> int:
        return 15


class Penyihir(Karakter, BisaMenyembuhkan):
    """Penyihir: HP kecil, serangan besar, dan bisa menyembuhkan."""

    def __init__(self, nama: str):
        super().__init__(nama, 50)

    def peran(self) -> str:
        return "Penyihir"

    def kekuatan_serangan(self) -> int:
        return 25

    def sembuhkan(self, target: Karakter):
        naik = target.pulihkan(30)
        print(f"Penyihir {self.nama} menyembuhkan {target.nama}: +{naik} HP")


class RamuanObat(BisaMenyembuhkan):
    """Ramuan sekali pakai. Bukan Karakter, tetapi BisaMenyembuhkan."""

    def __init__(self, kekuatan: int):
        self._kekuatan = kekuatan
        self._sudah_dipakai = False

    def sembuhkan(self, target: Karakter):
        if self._sudah_dipakai:
            print("Ramuan Obat sudah habis")
            return
        self._sudah_dipakai = True
        naik = target.pulihkan(self._kekuatan)
        print(f"Ramuan Obat menyembuhkan {target.nama}: +{naik} HP")


def fase_penyembuhan(daftar: list[BisaMenyembuhkan], target: Karakter):
    for penyembuh in daftar:
        penyembuh.sembuhkan(target)


def main():
    arga = Ksatria("Arga")
    laras = Pemanah("Laras")
    mira = Penyihir("Mira")
    semua: list[Karakter] = [arga, laras, mira]

    print("=== PARA KARAKTER ===")
    for karakter in semua:
        print(karakter)

    print()
    print("=== RONDE 1 ===")
    arga.serang(laras)
    laras.serang(arga)
    mira.serang(laras)

    print()
    print("=== RONDE 2 ===")
    arga.serang(laras)
    laras.serang(arga)
    mira.serang(arga)

    print()
    print("=== FASE PENYEMBUHAN UNTUK ARGA ===")
    ramuan = RamuanObat(50)
    fase_penyembuhan([mira, ramuan], arga)
    ramuan.sembuhkan(mira)

    print()
    print("=== STATUS AKHIR ===")
    for karakter in semua:
        print(karakter)


if __name__ == "__main__":
    main()
