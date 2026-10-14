"""
Solusi Latihan 06 - Turnamen Mini RPG
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- serang(lawan) ditulis SEKALI di kelas induk Karakter. Di dalamnya ada DUA
  panggilan polimorfik sekaligus:
    self.hitung_serangan()         -> versi milik PENYERANG
    lawan.terima_serangan(damage)  -> versi milik yang DISERANG
- Prajurit meng-override terima_serangan(): damage dikurangi perisai
  (minimal tetap 1).
- Penyihir meng-override hitung_serangan(): setiap serangan ke-3, ke-6, ...
  menjadi bola api (3 kali kekuatan).
- Pemanah meng-override terima_serangan(): setiap serangan ke-2, ke-4, ...
  yang mengarah kepadanya berhasil dihindari (damage 0).
- Tidak ada angka acak, jadi hasil turnamen selalu sama.

Cara menjalankan:
    python latihan06_turnamen_rpg.py
"""

RONDE_MAKS = 10


class Karakter:
    """Kelas induk semua karakter."""

    def __init__(self, nama: str, hp: int, kekuatan: int):
        self._nama = nama
        self._hp = hp
        self._kekuatan = kekuatan

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def hp(self) -> int:
        return self._hp

    def masih_hidup(self) -> bool:
        return self._hp > 0

    def hitung_serangan(self) -> int:
        return self._kekuatan

    def terima_serangan(self, damage: int) -> int:
        """Mengurangi HP, lalu mengembalikan damage yang benar-benar diterima."""
        self._hp = max(self._hp - damage, 0)
        return damage

    def serang(self, lawan: "Karakter"):
        damage = self.hitung_serangan()  # polimorfisme: versi penyerang
        diterima = lawan.terima_serangan(damage)  # polimorfisme: versi lawan
        print(f"  {self._nama} menyerang {lawan.nama}: {diterima} damage, "
              f"HP {lawan.nama} tinggal {lawan.hp}")


class Prajurit(Karakter):
    def __init__(self, nama: str, hp: int, kekuatan: int, perisai: int):
        super().__init__(nama, hp, kekuatan)
        self._perisai = perisai

    def terima_serangan(self, damage: int) -> int:
        dikurangi = max(damage - self._perisai, 1)
        return super().terima_serangan(dikurangi)  # memperluas versi induk


class Penyihir(Karakter):
    def __init__(self, nama: str, hp: int, kekuatan: int):
        super().__init__(nama, hp, kekuatan)
        self._jumlah_serangan = 0

    def hitung_serangan(self) -> int:
        self._jumlah_serangan += 1
        if self._jumlah_serangan % 3 == 0:
            return self._kekuatan * 3  # bola api
        return self._kekuatan


class Pemanah(Karakter):
    def __init__(self, nama: str, hp: int, kekuatan: int):
        super().__init__(nama, hp, kekuatan)
        self._jumlah_diserang = 0

    def terima_serangan(self, damage: int) -> int:
        self._jumlah_diserang += 1
        if self._jumlah_diserang % 2 == 0:
            return 0  # berhasil menghindar, HP tidak berkurang
        return super().terima_serangan(damage)


def duel(a: Karakter, b: Karakter):
    print(f"=== DUEL: {a.nama} ({type(a).__name__}) vs "
          f"{b.nama} ({type(b).__name__}) ===")
    for ronde in range(1, RONDE_MAKS + 1):
        print(f"Ronde {ronde}")
        a.serang(b)
        if not b.masih_hidup():
            break
        b.serang(a)
        if not a.masih_hidup():
            break
    if a.masih_hidup() and b.masih_hidup():
        print("Hasil: seri")
    elif a.masih_hidup():
        print(f"Pemenang: {a.nama}")
    else:
        print(f"Pemenang: {b.nama}")


def main():
    duel(Prajurit("Bima", 60, 10, 4), Penyihir("Sari", 45, 9))
    print()
    duel(Penyihir("Sari", 45, 9), Pemanah("Raka", 50, 8))


if __name__ == "__main__":
    main()
