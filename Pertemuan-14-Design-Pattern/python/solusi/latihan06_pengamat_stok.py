"""
Solusi Latihan 06 - KedaiKita: PengamatStok (Observer Baru)
Pertemuan 14 - Design Pattern Dasar

Ide penyelesaian:
- PengamatStok adalah OBSERVER baru. Ia hanya bereaksi saat status pesanan
  menjadi LUNAS; status lain diabaikan.
- Ia memakai gaya PULL: menerima objek pesanan, lalu MENARIK sendiri data
  yang dibutuhkan (daftar item dan stok setiap menu).
- Jika stok sebuah menu <= batas, cetak peringatan.
- Kelas pesanan (subject) TIDAK diubah: pengamat baru cukup didaftarkan
  lewat tambah_pengamat().

Supaya file ini bisa dijalankan sendiri, kita memakai versi MINI dari kelas
studi kasus dengan nama berbeda: MenuStok (Menu), BarisPesanan
(ItemPesanan), PesananKedai (Pesanan), PengamatStatus (PengamatPesanan),
LayarPesanan (mirip LayarDapur).

Cara menjalankan:
    python latihan06_pengamat_stok.py
"""

from abc import ABC, abstractmethod


class MenuStok:
    def __init__(self, nama: str, stok: int):
        self._nama = nama
        self._stok = stok

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def stok(self) -> int:
        return self._stok

    def kurangi_stok(self, jumlah: int):
        if jumlah > self._stok:
            raise ValueError(f"Stok {self._nama} tidak cukup")
        self._stok -= jumlah


class BarisPesanan:
    def __init__(self, menu: MenuStok, jumlah: int):
        self._menu = menu
        self._jumlah = jumlah

    @property
    def menu(self) -> MenuStok:
        return self._menu

    def __str__(self) -> str:
        return f"{self._jumlah} x {self._menu.nama}"


class PengamatStatus(ABC):
    """Observer: diberi tahu setiap kali status pesanan berubah."""

    @abstractmethod
    def perbarui(self, pesanan: "PesananKedai"):
        """Pesanan mengirim DIRINYA SENDIRI (gaya pull)."""


class PesananKedai:
    """Subject (versi mini Pesanan)."""

    def __init__(self, nomor: str):
        self._nomor = nomor
        self._daftar_baris: list[BarisPesanan] = []
        self._status = "BARU"
        self._daftar_pengamat: list[PengamatStatus] = []

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def status(self) -> str:
        return self._status

    @property
    def daftar_baris(self) -> list[BarisPesanan]:
        return list(self._daftar_baris)

    def tambah_item(self, menu: MenuStok, jumlah: int):
        menu.kurangi_stok(jumlah)  # stok berkurang saat item ditambahkan
        self._daftar_baris.append(BarisPesanan(menu, jumlah))

    def tambah_pengamat(self, pengamat: PengamatStatus):
        self._daftar_pengamat.append(pengamat)

    def ubah_status(self, status_baru: str):
        self._status = status_baru
        for pengamat in self._daftar_pengamat:
            pengamat.perbarui(self)


class LayarPesanan(PengamatStatus):
    """Pengamat lama: menampilkan setiap perubahan status."""

    def perbarui(self, pesanan: PesananKedai):
        print(f"  [LAYAR] {pesanan.nomor} -> {pesanan.status}")


class PengamatStok(PengamatStatus):
    """Pengamat BARU: memberi peringatan saat stok menu menipis."""

    def __init__(self, batas: int):
        self._batas = batas

    def perbarui(self, pesanan: PesananKedai):
        if pesanan.status != "LUNAS":  # hanya peduli saat pesanan lunas
            return
        for baris in pesanan.daftar_baris:  # PULL: tarik data dari pesanan
            menu = baris.menu
            if menu.stok <= self._batas:
                print(f"  [STOK] Peringatan: {menu.nama} tinggal {menu.stok} porsi")


def main():
    kopi = MenuStok("Kopi Susu Gula Aren", 20)
    nasi_goreng = MenuStok("Nasi Goreng Kampung", 6)
    pisang_goreng = MenuStok("Pisang Goreng Keju", 5)
    layar = LayarPesanan()
    pengamat_stok = PengamatStok(5)

    p001 = PesananKedai("P001")
    p001.tambah_item(kopi, 2)
    p001.tambah_item(nasi_goreng, 3)
    p001.tambah_pengamat(layar)
    p001.tambah_pengamat(pengamat_stok)  # pengamat baru cukup didaftarkan
    print("=== PESANAN P001 ===")
    print("Isi: " + ", ".join(str(baris) for baris in p001.daftar_baris))
    p001.ubah_status("LUNAS")  # di studi kasus, bayar() yang memanggil ini
    p001.ubah_status("DIPROSES")

    print()
    p002 = PesananKedai("P002")
    p002.tambah_item(kopi, 1)
    p002.tambah_item(pisang_goreng, 1)
    p002.tambah_pengamat(layar)
    p002.tambah_pengamat(pengamat_stok)
    print("=== PESANAN P002 ===")
    print("Isi: " + ", ".join(str(baris) for baris in p002.daftar_baris))
    p002.ubah_status("LUNAS")

    print()
    print("=== SISA STOK ===")
    for menu in [kopi, nasi_goreng, pisang_goreng]:
        print(f"{menu.nama:<20}{menu.stok:>3} porsi")


if __name__ == "__main__":
    main()
