"""
Solusi Latihan 05 - Validasi Nama Menu KedaiKita
Pertemuan 04 - Enkapsulasi

Ide penyelesaian:
- Salin kelas Menu dari studi kasus pertemuan ini. Bagian yang berubah
  ditandai dengan komentar "BARU".
- nama kini punya setter. Setter merapikan spasi di awal/akhir dengan
  strip(), lalu menolak nama yang kosong.
- Konstruktor mengisi nama LEWAT setter (self.nama = nama), sehingga menu
  tanpa nama ditolak sejak dibuat dan tidak ikut dihitung di jumlah_menu.

Cara menjalankan:
    python latihan05_nama_menu.py
"""


def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Menu:
    """Satu menu KedaiKita. Datanya dilindungi dan hanya diubah lewat method."""

    _jumlah_menu = 0  # atribut kelas, dibaca lewat Menu.jumlah_menu()

    def __init__(self, kode, nama, harga, kategori, stok=0):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        self._kode = kode
        self.nama = nama  # BARU: lewat setter, jadi ikut divalidasi
        self._kategori = kategori
        self._stok = stok
        self.harga = harga  # lewat setter, jadi ikut divalidasi
        Menu._jumlah_menu += 1  # dihitung hanya jika objek berhasil dibuat

    @classmethod
    def jumlah_menu(cls):
        """Banyaknya objek Menu yang berhasil dibuat."""
        return cls._jumlah_menu

    # ----- getter (read-only) -----
    @property
    def kode(self):
        return self._kode

    @property
    def kategori(self):
        return self._kategori

    @property
    def stok(self):
        return self._stok

    # ----- getter + setter dengan validasi -----
    @property
    def nama(self):
        return self._nama

    @nama.setter
    def nama(self, nilai):  # BARU: setter nama
        nama_rapi = nilai.strip()  # buang spasi di awal dan akhir
        if nama_rapi == "":
            raise ValueError("Nama menu tidak boleh kosong")
        self._nama = nama_rapi

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai

    # ----- method pengubah stok -----
    def tambah_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._stok += jumlah

    def kurangi_stok(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if jumlah > self._stok:
            raise ValueError(f"Stok {self._nama} tidak cukup (sisa {self._stok})")
        self._stok -= jumlah

    # ----- method lain -----
    def hitung_total(self, jumlah):
        return self._harga * jumlah

    def harga_setelah_diskon(self, persen):
        potongan = self._harga * persen // 100
        return self._harga - potongan

    def stok_cukup(self, jumlah):
        return self._stok >= jumlah

    def __str__(self):
        return (f"[{self._kode}] {self._nama} ({self._kategori}) - "
                f"{format_rupiah(self._harga)} | stok {self._stok}")


def main():
    kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
    es_teh = Menu("M02", "Es Teh Manis", 8000, "Minuman", 30)
    print("=== MENU AWAL ===")
    print(kopi)
    print(es_teh)

    print()
    print("=== GANTI NAMA MENU ===")
    es_teh.nama = "Es Teh Manis Jumbo"
    print(f"Nama baru: {es_teh.nama}")
    try:
        es_teh.nama = "   "
    except ValueError as e:
        print(f"Ditolak: {e}")
    print(es_teh)

    print()
    print("=== NAMA DIRAPIKAN OTOMATIS ===")
    nasi_goreng = Menu("M03", "  Nasi Goreng Kampung  ", 25000, "Makanan", 15)
    print(f"Nama tersimpan: '{nasi_goreng.nama}'")
    print(nasi_goreng)

    print()
    print("=== MENU BARU TANPA NAMA ===")
    try:
        Menu("M04", "", 23000, "Makanan")
    except ValueError as e:
        print(f"Gagal membuat menu: {e}")
    print(f"Jumlah menu terdaftar: {Menu.jumlah_menu()}")


if __name__ == "__main__":
    main()
