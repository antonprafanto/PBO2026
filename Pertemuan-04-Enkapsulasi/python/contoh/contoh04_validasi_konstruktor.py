"""
Contoh 04 - Validasi di Konstruktor
Pertemuan 04 - Enkapsulasi

Setter yang rajin memeriksa data belum cukup jika konstruktor menyimpan data
secara langsung. Objek bisa "lahir cacat" lewat pintu belakang itu.

- MahasiswaBercelah: setter memeriksa, tetapi konstruktor menyimpan langsung.
- Mahasiswa: konstruktor mengisi atribut LEWAT setter, sehingga aturan yang
  sama berlaku sejak objek lahir. Aturannya cukup ditulis satu kali.

(Batas semester 1-14 hanyalah aturan contoh di program ini.)

Cara menjalankan:
    python contoh04_validasi_konstruktor.py
"""


class MahasiswaBercelah:
    """Setter-nya memeriksa data, tetapi konstruktornya tidak."""

    def __init__(self, nama, semester):
        self._nama = nama
        self._semester = semester  # [1] celah: disimpan langsung tanpa diperiksa

    @property
    def nama(self):
        return self._nama

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, nilai):
        if nilai < 1 or nilai > 14:
            raise ValueError(f"Semester harus 1-14, bukan {nilai}")
        self._semester = nilai


class Mahasiswa:
    """Konstruktor memakai setter, jadi data diperiksa sejak objek lahir."""

    def __init__(self, nama, semester):
        self.nama = nama  # [2] tanpa garis bawah: yang dipanggil adalah setter nama
        self.semester = semester  # [3] setter semester ikut memeriksa

    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):
        if nilai.strip() == "":  # [4] strip() membuang spasi di awal dan akhir
            raise ValueError("Nama tidak boleh kosong")
        self._nama = nilai

    @property
    def semester(self):
        return self._semester

    @semester.setter
    def semester(self, nilai):
        if nilai < 1 or nilai > 14:
            raise ValueError(f"Semester harus 1-14, bukan {nilai}")
        self._semester = nilai


def main():
    print("=== VERSI BERCELAH ===")
    ayu = MahasiswaBercelah("Ayu", 20)  # [5] semester 20 lolos begitu saja!
    print(f"{ayu.nama} tercatat di semester {ayu.semester}")
    try:
        ayu.semester = 21
    except ValueError as e:
        print(f"Mengubah lewat setter ditolak: {e}")

    print()
    print("=== VERSI AMAN ===")
    bima = Mahasiswa("Bima", 3)
    print(f"{bima.nama} tercatat di semester {bima.semester}")
    try:
        citra = Mahasiswa("Citra", 20)  # [6] ditolak sejak lahir
        print(f"{citra.nama} berhasil dibuat")  # tidak pernah dijalankan
    except ValueError as e:
        print(f"Gagal membuat mahasiswa: {e}")
    try:
        Mahasiswa("   ", 2)  # nama berisi spasi saja
    except ValueError as e:
        print(f"Gagal membuat mahasiswa: {e}")


if __name__ == "__main__":
    main()
