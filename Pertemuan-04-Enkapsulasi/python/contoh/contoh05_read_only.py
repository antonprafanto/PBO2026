"""
Contoh 05 - Atribut Read-Only
Pertemuan 04 - Enkapsulasi

Tidak semua data boleh diubah setelah objek dibuat. NIK di KTP tidak pernah
berubah, sedangkan alamat bisa berubah saat pemiliknya pindah rumah.

- nik dan nama : property TANPA setter -> hanya bisa dibaca (read-only).
- alamat       : property DENGAN setter -> boleh diubah, tetapi tetap diperiksa.

Karena nik tidak punya setter, pemeriksaannya ditulis langsung di konstruktor.

Cara menjalankan:
    python contoh05_read_only.py
"""


class Penduduk:
    """Data kependudukan sederhana."""

    def __init__(self, nik, nama, alamat):
        if len(nik) != 16:  # [1] satu-satunya kesempatan memeriksa NIK
            raise ValueError("NIK harus 16 digit")
        self._nik = nik
        self._nama = nama
        self.alamat = alamat  # lewat setter alamat

    @property
    def nik(self):  # [2] hanya getter, TANPA setter -> read-only
        return self._nik

    @property
    def nama(self):
        return self._nama

    @property
    def alamat(self):
        return self._alamat

    @alamat.setter
    def alamat(self, nilai):  # [3] alamat boleh berubah, asal tidak kosong
        if nilai.strip() == "":
            raise ValueError("Alamat tidak boleh kosong")
        self._alamat = nilai


def main():
    warga = Penduduk("1234567890123456", "Rina Wulandari", "Jl. Pramuka, Samarinda")
    print("=== DATA AWAL ===")
    print(f"NIK   : {warga.nik}")
    print(f"Nama  : {warga.nama}")
    print(f"Alamat: {warga.alamat}")

    print()
    print("=== PINDAH RUMAH ===")
    warga.alamat = "Jl. Juanda, Samarinda"  # [4] diizinkan: alamat punya setter
    print(f"Alamat baru: {warga.alamat}")
    # warga.nik = "9999999999999999"  # [5] hapus tanda # untuk melihat error-nya

    print()
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        warga.alamat = ""
    except ValueError as e:
        print(f"Ditolak: {e}")
    try:
        Penduduk("12345", "Doni Saputra", "Jl. Merdeka, Samarinda")
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(f"Alamat {warga.nama} tetap: {warga.alamat}")


if __name__ == "__main__":
    main()
