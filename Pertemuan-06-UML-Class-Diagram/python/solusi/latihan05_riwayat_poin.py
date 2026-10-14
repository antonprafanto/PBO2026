"""
Solusi Latihan 05 - KedaiKita: Riwayat Poin Pelanggan
Pertemuan 06 - UML Class Diagram

Ide penyelesaian (dari diagram ke kode):
- Pelanggan "1" *-- "*" RiwayatPoin : riwayat
  KOMPOSISI: setiap kali poin berubah, Pelanggan sendiri yang MEMBUAT objek
  RiwayatPoin lalu menyimpannya di list _riwayat.
- tambah_poin() dan tukar_poin() tetap memakai parameter yang sama seperti
  di studi kasus. Isinya hanya ditambah satu baris untuk mencatat riwayat,
  sehingga kode lain yang memakai Pelanggan tidak perlu diubah.
- getRiwayat() di diagram ditulis sebagai property riwayat yang
  mengembalikan SALINAN list (seperti daftar_item di Pesanan).

Cara menjalankan:
    python latihan05_riwayat_poin.py
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 5000 menjadi 'Rp5.000' (sama seperti utilitas.py)."""
    return f"Rp{angka:,}".replace(",", ".")


class RiwayatPoin:
    """Satu catatan perubahan poin: positif = bertambah, negatif = berkurang."""

    def __init__(self, keterangan: str, perubahan: int):
        self._keterangan = keterangan
        self._perubahan = perubahan

    @property
    def keterangan(self) -> str:
        return self._keterangan

    @property
    def perubahan(self) -> int:
        return self._perubahan

    def __str__(self) -> str:
        return f"{self._keterangan:<14}{self._perubahan:+d}"


class Pelanggan:
    """Pelanggan KedaiKita (versi Pertemuan 05) ditambah riwayat poin."""

    def __init__(self, nama: str, no_hp: str):
        self._nama = nama
        self._no_hp = no_hp
        self._poin = 0
        self._riwayat: list[RiwayatPoin] = []  # BARU: bagian milik Pelanggan

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def no_hp(self) -> str:
        return self._no_hp

    @property
    def poin(self) -> int:
        return self._poin

    @property
    def riwayat(self) -> list[RiwayatPoin]:
        """BARU: mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._riwayat)

    def tambah_poin(self, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Poin yang ditambahkan harus lebih dari 0")
        self._poin += jumlah
        self._riwayat.append(RiwayatPoin("Tambah poin", jumlah))  # BARU

    def tukar_poin(self, jumlah: int) -> int:
        """Menukar poin menjadi potongan harga. 1 poin = Rp1.000."""
        if jumlah <= 0:
            raise ValueError("Poin yang ditukar harus lebih dari 0")
        if jumlah > self._poin:
            raise ValueError(f"Poin tidak cukup (sisa {self._poin})")
        self._poin -= jumlah
        self._riwayat.append(RiwayatPoin("Tukar poin", -jumlah))  # BARU
        return jumlah * 1000

    def cetak_riwayat(self):
        """BARU: mencetak semua catatan poin secara berurutan."""
        print(f"=== RIWAYAT POIN: {self._nama} ===")
        nomor = 1
        for catatan in self._riwayat:
            print(f"{nomor}. {catatan}")
            nomor += 1
        print(f"Saldo poin akhir: {self._poin}")

    def __str__(self) -> str:
        return f"{self._nama} ({self._no_hp}) - {self._poin} poin"


def main():
    budi = Pelanggan("Budi Santoso", "081234567890")

    print("=== TRANSAKSI POIN ===")
    budi.tambah_poin(6)
    budi.tambah_poin(3)
    potongan = budi.tukar_poin(5)
    print(f"Tukar 5 poin -> potongan {format_rupiah(potongan)}")
    try:
        budi.tukar_poin(10)  # gagal: tidak tercatat di riwayat
    except ValueError as e:
        print(f"Gagal tukar 10 poin: {e}")
    print(budi)

    print()
    budi.cetak_riwayat()

    print()
    print("=== MENCOBA MERUSAK RIWAYAT DARI LUAR ===")
    salinan = budi.riwayat
    salinan.clear()
    print(f"Isi salinan  : {len(salinan)} catatan")
    print(f"Riwayat asli : {len(budi.riwayat)} catatan")


if __name__ == "__main__":
    main()
