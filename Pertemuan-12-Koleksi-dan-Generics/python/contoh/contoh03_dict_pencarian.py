"""
Contoh 03 - Dict: Mencari Data Lewat Kunci
Pertemuan 12 - Koleksi dan Generics

dict menyimpan pasangan KUNCI -> NILAI. Di sini kuncinya NIM (teks) dan
nilainya objek Mahasiswa. Mencari lewat kunci tidak perlu memeriksa data
satu per satu seperti pada list.

Cara menjalankan:
    python contoh03_dict_pencarian.py
"""


class Mahasiswa:
    """Data singkat seorang mahasiswa."""

    def __init__(self, nim: str, nama: str, prodi: str):
        self._nim = nim
        self._nama = nama
        self._prodi = prodi

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"{self._nim} {self._nama} ({self._prodi})"


def cari_di_list(daftar: list[Mahasiswa], nim: str) -> Mahasiswa | None:
    """Pencarian cara lama: periksa satu per satu dari depan."""
    langkah = 0
    for mhs in daftar:
        langkah += 1
        if mhs.nim == nim:
            print(f"  (list memeriksa {langkah} data sampai ditemukan)")
            return mhs
    return None


def main():
    daftar = [
        Mahasiswa("2409106001", "Ayu Lestari", "Informatika"),
        Mahasiswa("2409106002", "Bima Saputra", "Informatika"),
        Mahasiswa("2409106003", "Citra Dewi", "Informatika"),
        Mahasiswa("2409106004", "Dimas Pratama", "Informatika"),
    ]
    data: dict[str, Mahasiswa] = {}  # [1] dict kosong: NIM -> Mahasiswa
    for mhs in daftar:
        data[mhs.nim] = mhs  # [2] simpan dengan kunci NIM

    print("=== CARI MAHASISWA BERDASARKAN NIM ===")
    print(f"Lewat list : {cari_di_list(daftar, '2409106004')}")
    print(f"Lewat kunci: {data['2409106004']}")  # [3] langsung lewat kunci
    nim_asing = "2409106099"
    if nim_asing in data:  # [4] cek dulu apakah kuncinya ada
        print(data[nim_asing])
    else:
        print(f"NIM {nim_asing} tidak terdaftar")
    if data.get(nim_asing) is None:  # [5] get(): None jika kunci tidak ada
        print("get() untuk NIM asing: tidak ada hasil")

    print()
    print("=== MENGUBAH, MENGHAPUS, DAN NILAI CADANGAN ===")
    print(f"Jumlah data: {len(data)}")
    bima_baru = Mahasiswa("2409106002", "Bima Saputra", "Sistem Informasi")
    data["2409106002"] = bima_baru  # [6] kunci sudah ada: nilai lama DITIMPA
    print(f"Bima pindah prodi: {data['2409106002']}")
    print(f"Jumlah data: {len(data)}")  # tetap 4: kunci tidak bisa kembar
    del data["2409106001"]  # [7] hapus berdasarkan kunci
    print(f"Setelah 2409106001 dihapus: {len(data)} data")
    pinjaman: dict[str, int] = {"2409106003": 2}  # NIM -> jumlah buku dipinjam
    print(f"Buku dipinjam Citra: {pinjaman.get('2409106003', 0)}")  # [8] nilai cadangan
    print(f"Buku dipinjam Dimas: {pinjaman.get('2409106004', 0)}")


if __name__ == "__main__":
    main()
