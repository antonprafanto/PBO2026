"""
Contoh 03 - LSP: Kelas Anak Harus Bisa Menggantikan Induknya
Pertemuan 13 - Prinsip SOLID

Versi MELANGGAR: kelas Burung berjanji "semua burung bisa terbang".
Penguin mewarisi Burung, lalu mengingkari janji itu dengan melempar
exception. Pemanggil yang percaya pada janji induk pun terkejut.

Versi SESUAI LSP: janji dipecah sesuai kenyataan.
- BurungDasar   -> janji yang ditepati SEMUA burung: bisa bertelur
- BurungTerbang -> janji tambahan khusus burung penerbang: bisa terbang
PenguinKutub cukup mewarisi BurungDasar, sehingga tidak ada janji yang diingkari.

Cara menjalankan:
    python contoh03_lsp.py
"""


# ------------------------------------------------------------ MELANGGAR LSP
class Burung:
    """Janji kelas induk: setiap burung bisa terbang."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def terbang(self) -> str:
        return f"{self._nama} terbang tinggi"


class Penguin(Burung):
    def terbang(self) -> str:  # [1] meng-override hanya untuk menolak
        raise NotImplementedError(f"{self.nama} tidak bisa terbang")


def lepas_ke_udara(daftar: list[Burung]):
    """Pemanggil yang percaya pada janji kelas Burung."""
    for burung in daftar:
        try:
            print(f"  {burung.terbang()}")
        except NotImplementedError as e:  # [2] pemanggil terpaksa berjaga-jaga
            print(f"  [KEJUTAN] {e}")


# -------------------------------------------------------------- SESUAI LSP
class BurungDasar:
    """Hanya berisi janji yang ditepati SEMUA burung."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def bertelur(self) -> str:
        return f"{self._nama} bertelur"


class BurungTerbang(BurungDasar):
    """Janji tambahan: burung jenis ini benar-benar bisa terbang."""

    def terbang(self) -> str:
        return f"{self.nama} terbang tinggi"


class PenguinKutub(BurungDasar):  # [3] tidak mewarisi janji terbang
    def berenang(self) -> str:
        return f"{self.nama} berenang di air dingin"


def main():
    print("=== VERSI MELANGGAR LSP ===")
    print("Melepas semua Burung ke udara:")
    lepas_ke_udara([Burung("Merpati"), Burung("Elang"), Penguin("Penguin")])

    print()
    print("=== VERSI SESUAI LSP ===")
    merpati = BurungTerbang("Merpati")
    elang = BurungTerbang("Elang")
    penguin = PenguinKutub("Penguin")

    print("Janji BurungDasar: bisa bertelur")
    semua_burung: list[BurungDasar] = [merpati, elang, penguin]  # [4]
    for burung in semua_burung:
        print(f"  {burung.bertelur()}")

    print("Janji BurungTerbang: bisa terbang")
    penerbang: list[BurungTerbang] = [merpati, elang]  # [5]
    for burung in penerbang:
        print(f"  {burung.terbang()}")

    print("Kemampuan khusus penguin:")
    print(f"  {penguin.berenang()}")
    print("Tidak ada kejutan: setiap kelas anak menepati janji induknya.")


if __name__ == "__main__":
    main()
