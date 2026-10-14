"""
Solusi Latihan 04 - KedaiKita: Menolak Kode Menu Ganda
Pertemuan 11 - Exception Handling

Ide penyelesaian:
- MenuSudahAdaError adalah turunan KedaiError, sama seperti
  MenuTidakDitemukanError. Ia membawa data kode dan nama_lama (nama menu
  yang sudah lebih dulu memakai kode itu).
- Kedai.tambah_menu() memeriksa semua menu yang sudah terdaftar. Jika kodenya
  sama, lempar MenuSudahAdaError SEBELUM menu baru dimasukkan ke list.
- main() menangkap exception itu dan memberi pesan yang ramah.

Catatan: agar file ini bisa dijalankan sendiri, kelas KedaiError, Menu, dan
Kedai di bawah adalah SALINAN RINGKAS dari studi-kasus (hanya bagian yang
dibutuhkan). Di proyek KedaiKita-mu, tambahkan MenuSudahAdaError ke
pengecualian.py, lalu ubah tambah_menu() di kedai.py.

Cara menjalankan:
    python latihan04_menu_sudah_ada.py
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class KedaiError(Exception):
    """Induk semua error khusus KedaiKita."""


class MenuSudahAdaError(KedaiError):
    """Dilempar saat kode menu yang didaftarkan sudah dipakai menu lain."""

    def __init__(self, kode: str, nama_lama: str):
        super().__init__(f"Kode {kode} sudah dipakai oleh {nama_lama}")
        self.kode = kode
        self.nama_lama = nama_lama


class Menu:
    """Salinan ringkas kelas Menu dari studi kasus."""

    def __init__(self, kode: str, nama: str, harga: int):
        self._kode = kode
        self._nama = nama
        self._harga = harga

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"[{self._kode}] {self._nama} - {format_rupiah(self._harga)}"


class Kedai:
    """Salinan ringkas kelas Kedai dari studi kasus."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_menu: list[Menu] = []

    def tambah_menu(self, menu: Menu):
        """Mendaftarkan menu. Melempar MenuSudahAdaError jika kodenya ganda."""
        for terdaftar in self._daftar_menu:
            if terdaftar.kode == menu.kode:
                raise MenuSudahAdaError(menu.kode, terdaftar.nama)
        self._daftar_menu.append(menu)

    def jumlah_menu(self) -> int:
        return len(self._daftar_menu)


def main():
    kedai = Kedai("KedaiKita")
    menu_baru = [
        Menu("M01", "Kopi Susu Gula Aren", 18000),
        Menu("M02", "Es Teh Manis", 8000),
        Menu("M03", "Nasi Goreng Kampung", 25000),
        Menu("M04", "Mie Goreng Jawa", 23000),
        Menu("M05", "Pisang Goreng Keju", 15000),
        Menu("M02", "Es Jeruk", 10000),  # kode ganda
        Menu("M06", "Teh Tarik", 12000),
        Menu("M06", "Kopi Tubruk", 12000),  # kode ganda
    ]

    print("=== MENAMBAH MENU ===")
    for menu in menu_baru:
        try:
            kedai.tambah_menu(menu)
        except MenuSudahAdaError as e:
            print(f"[GAGAL] {e}")
            print(f"        {menu.nama} tidak ditambahkan, pilih kode selain {e.kode}")
        else:
            print(f"[OK] {menu}")
    print(f"Jumlah menu terdaftar: {kedai.jumlah_menu()}")


if __name__ == "__main__":
    main()
