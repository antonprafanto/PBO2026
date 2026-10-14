"""
Contoh 06 - Kelas Akar object, isinstance(), dan issubclass()
Pertemuan 07 - Pewarisan (Inheritance)

- Kelas yang tidak menulis induk otomatis mewarisi kelas akar bernama object.
  Dari object-lah setiap kelas mendapat __str__ dan __eq__ bawaan.
- isinstance(objek, Kelas) menjawab: "apakah objek ini termasuk Kelas itu
  (atau turunannya)?"
- issubclass(KelasA, KelasB) menjawab: "apakah KelasA turunan KelasB?"

Cara menjalankan:
    python contoh06_kelas_akar_dan_cek_tipe.py
"""


class AlatMusik:  # [1] tidak menulis induk -> otomatis mewarisi object
    """Kelas induk semua alat musik."""

    def __init__(self, nama: str):
        self._nama = nama

    def __str__(self) -> str:  # [2] override __str__ bawaan object
        return f"Alat musik {self._nama}"


class Gitar(AlatMusik):
    """Gitar adalah AlatMusik. Tidak menambah apa pun."""


class Drum(AlatMusik):
    """Drum adalah AlatMusik. Tidak menambah apa pun."""


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    gitar = Gitar("gitar akustik")
    drum = Drum("drum elektrik")

    print("=== TEKS OBJEK ===")
    print(gitar)  # [3] memanggil __str__ warisan dari AlatMusik
    print(drum)

    print()
    print("=== CEK TIPE OBJEK ===")
    print(f"gitar adalah Gitar?        {ya_tidak(isinstance(gitar, Gitar))}")  # [4]
    print(f"gitar adalah AlatMusik?    {ya_tidak(isinstance(gitar, AlatMusik))}")
    print(f"gitar adalah Drum?         {ya_tidak(isinstance(gitar, Drum))}")
    print(f"gitar termasuk kelas akar? {ya_tidak(isinstance(gitar, object))}")
    print(f"Kelas persis gitar: {type(gitar).__name__}")  # [5]
    print(f"Kelas persis gitar = AlatMusik? {ya_tidak(type(gitar) is AlatMusik)}")

    print()
    print("=== CEK HUBUNGAN KELAS ===")
    print(f"Gitar turunan AlatMusik? {ya_tidak(issubclass(Gitar, AlatMusik))}")  # [6]
    print(f"AlatMusik turunan Gitar? {ya_tidak(issubclass(AlatMusik, Gitar))}")

    print()
    print("=== KESAMAAN BAWAAN DARI KELAS AKAR ===")
    kembaran = Gitar("gitar akustik")  # isi sama, tetapi objek berbeda
    print(f"gitar sama dengan kembarannya? {ya_tidak(gitar == kembaran)}")  # [7]
    print(f"gitar sama dengan dirinya?     {ya_tidak(gitar == gitar)}")


if __name__ == "__main__":
    main()
