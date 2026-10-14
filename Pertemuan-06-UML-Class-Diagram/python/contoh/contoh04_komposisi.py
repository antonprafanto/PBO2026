"""
Contoh 04 - Komposisi: Bagian yang Dibuat oleh Keseluruhan
Pertemuan 06 - UML Class Diagram

Diagram (versi Python, sintaks Mermaid):

    Gedung "1" *-- "1..*" Lantai : _daftar_lantai

- Belah ketupat PENUH (*--) ada di sisi Gedung (si "keseluruhan").
- Objek Lantai dibuat DI DALAM konstruktor Gedung dan tidak pernah
  diserahkan ke luar. Lantai tidak punya arti tanpa gedungnya.
- Multiplisitas "1..*": gedung minimal punya satu lantai. Aturan ini
  dijaga oleh konstruktor Gedung.

Cara menjalankan:
    python contoh04_komposisi.py
"""


class Lantai:
    """Satu lantai gedung beserta nama-nama ruangannya."""

    def __init__(self, nomor: int):
        self._nomor = nomor
        self._ruangan: list[str] = []

    def tambah_ruangan(self, nama: str):
        self._ruangan.append(nama)

    def deskripsi(self) -> str:
        if not self._ruangan:
            return f"Lantai {self._nomor}: (kosong)"
        return f"Lantai {self._nomor}: {', '.join(self._ruangan)}"


class Gedung:
    """Gedung yang tersusun atas lantai-lantai."""

    def __init__(self, nama: str, jumlah_lantai: int):
        if jumlah_lantai < 1:  # [1] menjaga multiplisitas 1..*
            raise ValueError("Gedung minimal punya 1 lantai")
        self._nama = nama
        self._daftar_lantai: list[Lantai] = []
        for nomor in range(1, jumlah_lantai + 1):
            self._daftar_lantai.append(Lantai(nomor))  # [2] bagian dibuat OLEH gedung

    def tambah_ruangan(self, nomor_lantai: int, nama_ruangan: str):
        lantai = self._daftar_lantai[nomor_lantai - 1]
        lantai.tambah_ruangan(nama_ruangan)  # [3] gedung meneruskan perintah

    def jumlah_lantai(self) -> int:
        return len(self._daftar_lantai)

    def cetak_denah(self):
        print(f"=== DENAH {self._nama} ===")
        for lantai in self._daftar_lantai:
            print(lantai.deskripsi())


def main():
    gedung = Gedung("Gedung Informatika", 3)  # [4] hanya data mentah yang dikirim
    gedung.tambah_ruangan(1, "Lobi")
    gedung.tambah_ruangan(1, "Ruang Dosen")
    gedung.tambah_ruangan(2, "Lab Pemrograman")
    gedung.tambah_ruangan(2, "Lab Jaringan")
    gedung.cetak_denah()
    print(f"Jumlah lantai: {gedung.jumlah_lantai()}")

    print()
    print("=== MENCOBA GEDUNG TANPA LANTAI ===")
    try:
        Gedung("Gedung Khayalan", 0)
    except ValueError as e:
        print(f"Gagal membuat gedung: {e}")


if __name__ == "__main__":
    main()
