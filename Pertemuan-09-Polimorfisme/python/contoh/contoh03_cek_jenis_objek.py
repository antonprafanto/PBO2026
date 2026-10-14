"""
Contoh 03 - Memeriksa Jenis Objek dengan isinstance()
Pertemuan 09 - Polimorfisme

Mahasiswa dan Dosen adalah Pengguna Sistem Informasi Akademik (SIA).
- Method BERSAMA (peran, menu_utama) aman dipanggil pada semua pengguna,
  dan versi yang berjalan selalu milik objek sebenarnya.
- Method KHUSUS (isi_krs hanya milik Mahasiswa, input_nilai hanya milik
  Dosen) hanya boleh dipanggil setelah jenis objeknya diperiksa dengan
  isinstance().

Cara menjalankan:
    python contoh03_cek_jenis_objek.py
"""


class Pengguna:
    """Pengguna Sistem Informasi Akademik (SIA) kampus."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama

    def peran(self) -> str:
        return "Pengguna"

    def menu_utama(self) -> str:
        return "Profil"


class Mahasiswa(Pengguna):
    def __init__(self, nama: str, nim: str):
        super().__init__(nama)
        self._nim = nim

    def peran(self) -> str:
        return "Mahasiswa"

    def menu_utama(self) -> str:
        return "Profil, KRS, KHS"

    def isi_krs(self, sks: int) -> str:  # [1] method KHUSUS mahasiswa
        return f"{self._nama} ({self._nim}) mengisi KRS {sks} SKS"


class Dosen(Pengguna):
    def __init__(self, nama: str, nip: str):
        super().__init__(nama)
        self._nip = nip

    def peran(self) -> str:
        return "Dosen"

    def menu_utama(self) -> str:
        return "Profil, Input Nilai, Jadwal Mengajar"

    def input_nilai(self, mata_kuliah: str, nilai: str) -> str:  # khusus dosen
        return f"{self._nama} memasukkan nilai {mata_kuliah}: {nilai}"


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    daftar = [
        Mahasiswa("Ayu Lestari", "2409106001"),
        Dosen("Rahmat Hidayat", "198003152005011002"),
        Mahasiswa("Bima Saputra", "2409106002"),
    ]

    print("=== SEMUA PENGGUNA LOGIN ===")
    for pengguna in daftar:  # [2] method bersama: aman untuk semua pengguna
        print(f"{pengguna.nama} [{pengguna.peran()}] menu: {pengguna.menu_utama()}")

    print()
    print("=== FITUR KHUSUS: CEK JENIS DULU ===")
    for pengguna in daftar:
        if isinstance(pengguna, Mahasiswa):  # [3] pastikan dulu jenisnya
            print(pengguna.isi_krs(21))  # [4] baru panggil method khususnya
        elif isinstance(pengguna, Dosen):
            print(pengguna.input_nilai("PBO", "A"))

    print()
    print("=== CEK JENIS IKUT MENGENAL INDUK ===")
    ayu = daftar[0]
    print(f"Ayu termasuk Mahasiswa? {ya_tidak(isinstance(ayu, Mahasiswa))}")
    print(f"Ayu termasuk Pengguna?  {ya_tidak(isinstance(ayu, Pengguna))}")  # [5]
    print(f"Ayu termasuk Dosen?     {ya_tidak(isinstance(ayu, Dosen))}")


if __name__ == "__main__":
    main()
