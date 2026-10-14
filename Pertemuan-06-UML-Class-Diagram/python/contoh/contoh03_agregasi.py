"""
Contoh 03 - Agregasi: Bagian yang Bisa Hidup Sendiri
Pertemuan 06 - UML Class Diagram

Diagram (versi Python, sintaks Mermaid):

    KelasKuliah "*" o-- "*" Mahasiswa : _peserta

- Belah ketupat KOSONG (o--) ada di sisi KelasKuliah (si "keseluruhan").
- Objek Mahasiswa dibuat DI LUAR kelas kuliah, lalu dikirim lewat parameter.
- Satu mahasiswa boleh ikut banyak kelas kuliah, dan tetap ada walaupun
  sebuah kelas kuliah sudah selesai.

Cara menjalankan:
    python contoh03_agregasi.py
"""


class Mahasiswa:
    """Mahasiswa dengan NIM dan nama."""

    def __init__(self, nim: str, nama: str):
        self._nim = nim
        self._nama = nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama


class KelasKuliah:
    """Kelas kuliah yang menampung mahasiswa sampai kapasitas tertentu."""

    def __init__(self, nama_mk: str, kapasitas: int):
        self._nama_mk = nama_mk
        self._kapasitas = kapasitas
        self._peserta: list[Mahasiswa] = []  # [1] list berisi referensi Mahasiswa

    @property
    def nama_mk(self) -> str:
        return self._nama_mk

    def tambah_peserta(self, mahasiswa: Mahasiswa) -> bool:  # [2] bagian dari luar
        if len(self._peserta) >= self._kapasitas:
            return False
        self._peserta.append(mahasiswa)
        return True

    def daftar_peserta(self) -> list[Mahasiswa]:
        return list(self._peserta)  # [3] salinan list, isi asli tetap aman


def main():
    ayu = Mahasiswa("2409106001", "Ayu Lestari")  # [4] bagian dibuat di luar
    bima = Mahasiswa("2409106002", "Bima Saputra")
    citra = Mahasiswa("2409106003", "Citra Dewi")

    pbo = KelasKuliah("Pemrograman Berorientasi Objek", 2)
    basis_data = KelasKuliah("Basis Data", 40)

    print("=== PENDAFTARAN KELAS PBO ===")
    for mhs in [ayu, bima, citra]:
        if pbo.tambah_peserta(mhs):
            print(f"{mhs.nama} masuk kelas {pbo.nama_mk}")
        else:
            print(f"{mhs.nama} gagal: kelas {pbo.nama_mk} penuh")
    basis_data.tambah_peserta(ayu)  # [5] Ayu ikut dua kelas sekaligus
    basis_data.tambah_peserta(citra)

    print()
    print("=== PESERTA BASIS DATA ===")
    for mhs in basis_data.daftar_peserta():
        print(f"{mhs.nim} {mhs.nama}")
    if pbo.daftar_peserta()[0] is basis_data.daftar_peserta()[0]:
        print("Ayu di kelas PBO dan di kelas Basis Data adalah objek yang SAMA")

    print()
    print("=== KELAS PBO SELESAI ===")
    pbo = None  # [6] si keseluruhan dibubarkan
    print(f"{ayu.nama} tetap ada, NIM {ayu.nim}")
    print(f"Peserta Basis Data masih {len(basis_data.daftar_peserta())} orang")


if __name__ == "__main__":
    main()
