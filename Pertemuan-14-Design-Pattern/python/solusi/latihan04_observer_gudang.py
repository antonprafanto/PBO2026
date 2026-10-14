"""
Solusi Latihan 04 - Observer Stok Gudang Menipis
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- Gudang adalah SUBJECT: menyimpan stok (dict) dan daftar pengamat.
- Setiap kali barang diambil dan sisanya di bawah BATAS_MINIMUM, gudang
  memanggil stok_menipis(nama_barang, sisa) milik SEMUA pengamat.
  Datanya langsung dikirim sebagai argumen (gaya PUSH).
- Dua pengamat yang berbeda jenis: Pemasok dan AdminGudang. Gudang tidak
  peduli jenisnya, cukup tahu bahwa keduanya PengamatGudang.

Cara menjalankan:
    python latihan04_observer_gudang.py
"""

from abc import ABC, abstractmethod


class PengamatGudang(ABC):
    """Observer: ingin diberi tahu saat stok sebuah barang menipis."""

    @abstractmethod
    def stok_menipis(self, nama_barang: str, sisa: int):
        """Dipanggil gudang saat sisa stok di bawah batas minimum."""


class Pemasok(PengamatGudang):
    def __init__(self, nama: str):
        self._nama = nama

    def stok_menipis(self, nama_barang: str, sisa: int):
        print(f"  [Pemasok {self._nama}] Siap mengirim {nama_barang} tambahan")


class AdminGudang(PengamatGudang):
    def __init__(self):
        self._jumlah_peringatan = 0

    def stok_menipis(self, nama_barang: str, sisa: int):
        self._jumlah_peringatan += 1
        print(f"  [Admin] Catat: stok {nama_barang} tinggal {sisa}")

    def jumlah_peringatan(self) -> int:
        return self._jumlah_peringatan


class Gudang:
    """Subject: memberi kabar ke semua pengamat saat stok menipis."""

    BATAS_MINIMUM = 10

    def __init__(self, nama: str):
        self._nama = nama
        self._stok: dict[str, int] = {}
        self._daftar_pengamat: list[PengamatGudang] = []

    def tambah_pengamat(self, pengamat: PengamatGudang):
        self._daftar_pengamat.append(pengamat)

    def isi_stok(self, nama_barang: str, jumlah: int):
        self._stok[nama_barang] = self._stok.get(nama_barang, 0) + jumlah

    def ambil(self, nama_barang: str, jumlah: int):
        if jumlah > self._stok[nama_barang]:
            raise ValueError(f"Stok {nama_barang} tidak cukup")
        self._stok[nama_barang] -= jumlah
        sisa = self._stok[nama_barang]
        print(f"Ambil {jumlah} {nama_barang}, sisa {sisa}")
        if sisa < Gudang.BATAS_MINIMUM:
            self._beri_kabar(nama_barang, sisa)

    def _beri_kabar(self, nama_barang: str, sisa: int):
        for pengamat in self._daftar_pengamat:
            pengamat.stok_menipis(nama_barang, sisa)


def main():
    gudang = Gudang("Gudang Sembako")
    gudang.isi_stok("Beras", 50)
    gudang.isi_stok("Gula", 20)
    gudang.isi_stok("Minyak", 15)
    admin = AdminGudang()
    gudang.tambah_pengamat(Pemasok("Pak Rahman"))
    gudang.tambah_pengamat(admin)

    print(f"=== TRANSAKSI GUDANG (BATAS MINIMUM {Gudang.BATAS_MINIMUM}) ===")
    gudang.ambil("Beras", 30)
    gudang.ambil("Gula", 12)
    gudang.ambil("Minyak", 3)
    gudang.ambil("Gula", 5)

    print()
    print("=== RINGKASAN ===")
    print(f"Peringatan yang dicatat admin: {admin.jumlah_peringatan()}")


if __name__ == "__main__":
    main()
