"""
KedaiKita - Pertemuan 04: Enkapsulasi

Yang baru dibanding Pertemuan 03:
- Atribut tidak lagi diakses langsung. Namanya diberi awalan garis bawah (_harga),
  tanda bahwa atribut itu urusan internal kelas.
- Akses dari luar lewat @property (getter) dan setter yang MEMVALIDASI data.
- kode, nama, kategori, dan stok bersifat read-only dari luar.
- Stok hanya bisa berubah lewat method tambah_stok() dan kurangi_stok().
- Poin pelanggan hanya bisa berubah lewat tambah_poin() dan tukar_poin().
- Data yang tidak valid ditolak dengan raise ValueError(...).
  Cara menangkapnya (try/except) baru kita intip sekilas; bahasan lengkapnya
  ada di Pertemuan 11.

Cara menjalankan:
    python kedaikita.py
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
        self._nama = nama
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
    def nama(self):
        return self._nama

    @property
    def kategori(self):
        return self._kategori

    @property
    def stok(self):
        return self._stok

    # ----- getter + setter dengan validasi -----
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

    # ----- method lain (sama seperti Pertemuan 03) -----
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


class Pelanggan:
    """Pelanggan KedaiKita. Poin hanya berubah lewat method resmi."""

    def __init__(self, nama, no_hp):
        self._nama = nama
        self._no_hp = no_hp
        self._poin = 0

    @property
    def nama(self):
        return self._nama

    @property
    def no_hp(self):
        return self._no_hp

    @property
    def poin(self):
        return self._poin

    def tambah_poin(self, jumlah):
        if jumlah <= 0:
            raise ValueError("Poin yang ditambahkan harus lebih dari 0")
        self._poin += jumlah

    def tukar_poin(self, jumlah):
        """Menukar poin menjadi potongan harga. 1 poin = Rp1.000."""
        if jumlah > self._poin:
            raise ValueError(f"Poin tidak cukup (sisa {self._poin})")
        self._poin -= jumlah
        return jumlah * 1000

    def __str__(self):
        return f"{self._nama} ({self._no_hp}) - {self._poin} poin"


def main():
    kopi = Menu("M01", "Kopi Susu Gula Aren", 18000, "Minuman", 20)
    es_teh = Menu("M02", "Es Teh Manis", 8000, "Minuman", 30)
    nasi_goreng = Menu("M03", "Nasi Goreng Kampung", 25000, "Makanan", 15)

    print("=== MENU KEDAIKITA ===")
    print(kopi)
    print(es_teh)
    print(nasi_goreng)
    print(f"Jumlah menu terdaftar: {Menu.jumlah_menu()}")

    print()
    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        Menu("M09", "Menu Gratis", 0, "Minuman")
    except ValueError as e:
        print(f"Gagal membuat menu: {e}")
    print(f"Jumlah menu terdaftar tetap: {Menu.jumlah_menu()}")

    print()
    print("=== MENGUBAH HARGA LEWAT SETTER ===")
    es_teh.harga = 10000
    print(f"Harga {es_teh.nama} naik menjadi {format_rupiah(es_teh.harga)}")
    try:
        es_teh.harga = -5000
    except ValueError as e:
        print(f"Gagal mengubah harga: {e}")
    print(f"Harga {es_teh.nama} tetap {format_rupiah(es_teh.harga)}")

    print()
    print("=== MENGELOLA STOK ===")
    print(f"Stok awal {kopi.nama}: {kopi.stok}")
    kopi.kurangi_stok(5)
    print(f"Terjual 5, stok sekarang {kopi.stok}")
    kopi.tambah_stok(10)
    print(f"Restok 10, stok sekarang {kopi.stok}")
    try:
        kopi.kurangi_stok(30)
    except ValueError as e:
        print(f"Gagal menjual: {e}")

    print()
    print("=== POIN PELANGGAN ===")
    budi = Pelanggan("Budi Santoso", "081234567890")
    print(budi)
    budi.tambah_poin(12)
    print(budi)
    potongan = budi.tukar_poin(10)
    print(f"Tukar 10 poin -> potongan {format_rupiah(potongan)}")
    print(budi)
    try:
        budi.tukar_poin(5)
    except ValueError as e:
        print(f"Gagal menukar poin: {e}")


if __name__ == "__main__":
    main()
