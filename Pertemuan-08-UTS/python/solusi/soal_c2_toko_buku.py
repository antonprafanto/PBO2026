"""
Solusi Soal C2 - Toko Buku Daring
Pertemuan 08 - UTS (latihan persiapan, BUKAN soal ujian asli)

Ide penyelesaian:
- Produk adalah kelas induk untuk semua barang yang dijual. Buku dan
  AlatTulis mewarisinya, menambah atribut sendiri, dan meng-override __str__.
- Harga dijaga oleh setter (harus > 0). Stok hanya berubah lewat method
  kurangi_stok() yang menolak permintaan melebihi stok.
- Pesanan MEMBUAT objek ItemPesanan di dalam tambah_item() (komposisi).
  TokoBuku menyimpan produk yang dibuat di luar (agregasi). Pesanan mengenal
  Pelanggan pemesannya (asosiasi).
- Ongkir dihitung dari total berat (dibulatkan ke atas per kg) dan gratis
  bila subtotal mencapai batas tertentu.

Cara menjalankan (dari folder python/solusi; macOS/Linux: python3):
    python soal_c2_toko_buku.py
"""

ONGKIR_PER_KG = 10000  # Rupiah per kilogram
BATAS_GRATIS_ONGKIR = 200000  # subtotal minimal agar ongkir gratis
LEBAR_INVOICE = 40


def format_rupiah(angka: int) -> str:
    """Mengubah 206000 menjadi 'Rp206.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Pelanggan:
    """Pembeli di toko daring. Datanya read-only dari luar."""

    def __init__(self, nama: str, email: str):
        self._nama = nama
        self._email = email

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def email(self) -> str:
        return self._email

    def __str__(self) -> str:
        return f"{self._nama} ({self._email})"


class Produk:
    """Kelas induk: data dan perilaku yang dimiliki SEMUA produk toko."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int,
                 berat_gram: int):
        if stok < 0:
            raise ValueError("Stok tidak boleh negatif")
        if berat_gram <= 0:
            raise ValueError("Berat harus lebih dari 0 gram")
        self._kode = kode
        self._nama = nama
        self._stok = stok
        self._berat_gram = berat_gram
        self.harga = harga  # [1] lewat setter, jadi ikut divalidasi

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def stok(self) -> int:
        return self._stok

    @property
    def berat_gram(self) -> int:
        return self._berat_gram

    @property
    def harga(self) -> int:
        return self._harga

    @harga.setter
    def harga(self, nilai: int):
        if nilai <= 0:
            # [2] ditolak SEBELUM atribut diubah, jadi harga lama tetap aman
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai

    def stok_cukup(self, jumlah: int) -> bool:
        return self._stok >= jumlah

    def kurangi_stok(self, jumlah: int):
        """Satu-satunya pintu untuk mengurangi stok."""
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        if not self.stok_cukup(jumlah):
            raise ValueError(f"Stok {self._nama} tidak cukup (sisa {self._stok})")
        self._stok -= jumlah

    def __str__(self) -> str:
        return (f"[{self._kode}] {self._nama} - "
                f"{format_rupiah(self._harga)} | stok {self._stok}")


class Buku(Produk):
    """Produk berupa buku. Tambahan: penulis."""

    def __init__(self, kode: str, judul: str, harga: int, stok: int,
                 berat_gram: int, penulis: str):
        super().__init__(kode, judul, harga, stok, berat_gram)  # [3]
        self._penulis = penulis

    @property
    def penulis(self) -> str:
        return self._penulis

    def __str__(self) -> str:
        # [4] override: pakai teks dari induk, lalu tambahkan nama penulis
        return f"{super().__str__()} | penulis {self._penulis}"


class AlatTulis(Produk):
    """Produk berupa alat tulis. Tambahan: warna."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int,
                 berat_gram: int, warna: str):
        super().__init__(kode, nama, harga, stok, berat_gram)
        self._warna = warna

    @property
    def warna(self) -> str:
        return self._warna

    def __str__(self) -> str:
        return f"{super().__str__()} | warna {self._warna}"


class ItemPesanan:
    """Satu baris pesanan: produk apa dan berapa banyak."""

    def __init__(self, produk: Produk, jumlah: int):
        if jumlah <= 0:
            raise ValueError("Jumlah harus lebih dari 0")
        self._produk = produk  # menyimpan REFERENSI ke objek Produk
        self._jumlah = jumlah

    @property
    def produk(self) -> Produk:
        return self._produk

    @property
    def jumlah(self) -> int:
        return self._jumlah

    def hitung_subtotal(self) -> int:
        return self._produk.harga * self._jumlah

    def hitung_berat(self) -> int:
        return self._produk.berat_gram * self._jumlah

    def __str__(self) -> str:
        return f"{self._jumlah} x {self._produk.nama}"


class Pesanan:
    """Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan."""

    _nomor_terakhir = 0  # atribut kelas untuk nomor otomatis

    def __init__(self, pelanggan: Pelanggan):
        Pesanan._nomor_terakhir += 1
        self._nomor = f"INV{Pesanan._nomor_terakhir:03d}"  # INV001, INV002, ...
        self._pelanggan = pelanggan  # asosiasi
        self._daftar_item: list[ItemPesanan] = []  # komposisi

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def pelanggan(self) -> Pelanggan:
        return self._pelanggan

    @property
    def daftar_item(self) -> list[ItemPesanan]:
        """Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._daftar_item)

    def tambah_item(self, produk: Produk, jumlah: int):
        item = ItemPesanan(produk, jumlah)  # [5] item dibuat OLEH pesanan
        produk.kurangi_stok(jumlah)  # [6] gagal (ValueError) jika stok kurang
        self._daftar_item.append(item)  # [7] hanya disimpan jika semua lolos

    def hitung_subtotal(self) -> int:
        subtotal = 0
        for item in self._daftar_item:
            subtotal += item.hitung_subtotal()
        return subtotal

    def hitung_berat_kg(self) -> int:
        """Total berat dalam kg, DIBULATKAN KE ATAS (1080 gram -> 2 kg)."""
        berat_gram = 0
        for item in self._daftar_item:
            berat_gram += item.hitung_berat()
        return (berat_gram + 999) // 1000  # [8] pembulatan ke atas tanpa float

    def hitung_ongkir(self) -> int:
        if self.hitung_subtotal() >= BATAS_GRATIS_ONGKIR:
            return 0
        return self.hitung_berat_kg() * ONGKIR_PER_KG

    def hitung_total(self) -> int:
        return self.hitung_subtotal() + self.hitung_ongkir()

    def cetak_invoice(self):
        garis = "=" * LEBAR_INVOICE
        print(garis)
        print(f"INVOICE {self._nomor}")
        print(garis)
        print(f"Pelanggan : {self._pelanggan}")
        print("-" * LEBAR_INVOICE)
        for item in self._daftar_item:
            subtotal = format_rupiah(item.hitung_subtotal())
            print(f"{str(item):<30}{subtotal:>10}")
        print("-" * LEBAR_INVOICE)
        print(f"{'Subtotal':<30}{format_rupiah(self.hitung_subtotal()):>10}")
        ongkir = self.hitung_ongkir()
        teks_ongkir = "GRATIS" if ongkir == 0 else format_rupiah(ongkir)
        label_ongkir = f"Ongkir ({self.hitung_berat_kg()} kg)"
        print(f"{label_ongkir:<30}{teks_ongkir:>10}")
        print(f"{'TOTAL':<30}{format_rupiah(self.hitung_total()):>10}")
        print(garis)


class TokoBuku:
    """Toko daring yang punya katalog produk dan catatan pesanan."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_produk: list[Produk] = []  # agregasi
        self._daftar_pesanan: list[Pesanan] = []  # asosiasi (catatan)

    @property
    def nama(self) -> str:
        return self._nama

    def tambah_produk(self, produk: Produk):
        self._daftar_produk.append(produk)

    def cari_produk(self, kode: str) -> Produk | None:
        """Mengembalikan objek Produk dengan kode tertentu, atau None."""
        for produk in self._daftar_produk:
            if produk.kode == kode:
                return produk
        return None

    def buat_pesanan(self, pelanggan: Pelanggan) -> Pesanan:
        pesanan = Pesanan(pelanggan)
        self._daftar_pesanan.append(pesanan)
        return pesanan

    def jumlah_pesanan(self) -> int:
        return len(self._daftar_pesanan)

    def total_penjualan(self) -> int:
        total = 0
        for pesanan in self._daftar_pesanan:
            total += pesanan.hitung_total()
        return total

    def tampilkan_katalog(self):
        print(f"=== KATALOG {self._nama} ===")
        for produk in self._daftar_produk:
            print(produk)  # memanggil __str__ milik kelas anak


def siapkan_toko() -> TokoBuku:
    """Membuat toko beserta lima produk awalnya."""
    toko = TokoBuku("PustakaKita")
    toko.tambah_produk(Buku("B01", "Laskar Pelangi", 95000, 5, 350,
                            "Andrea Hirata"))
    toko.tambah_produk(Buku("B02", "Bumi Manusia", 120000, 3, 600,
                            "Pramoedya Ananta Toer"))
    toko.tambah_produk(Buku("B03", "Negeri 5 Menara", 89000, 2, 450,
                            "Ahmad Fuadi"))
    toko.tambah_produk(AlatTulis("T01", "Pulpen Gel", 8000, 50, 10, "hitam"))
    toko.tambah_produk(AlatTulis("T02", "Map Plastik", 5000, 40, 60, "biru"))
    return toko


def main():
    toko = siapkan_toko()
    toko.tampilkan_katalog()
    print()

    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        toko.tambah_produk(Buku("B09", "Buku Tanpa Harga", 0, 5, 300, "Anonim"))
    except ValueError as e:
        print(f"Gagal menambah produk: {e}")
    bumi_manusia = toko.cari_produk("B02")
    try:
        bumi_manusia.harga = -5000
    except ValueError as e:
        print(f"Gagal mengubah harga: {e}")
    print(f"Harga {bumi_manusia.nama} tetap {format_rupiah(bumi_manusia.harga)}")
    if toko.cari_produk("B99") is None:
        print("Cari B99: produk tidak ditemukan")
    print()

    print("=== PESANAN ===")
    siti = Pelanggan("Siti Aminah", "siti@contoh.id")
    budi = Pelanggan("Budi Santoso", "budi@contoh.id")

    pesanan_siti = toko.buat_pesanan(siti)
    pesanan_siti.tambah_item(toko.cari_produk("B01"), 2)
    pesanan_siti.tambah_item(toko.cari_produk("T01"), 2)
    pesanan_siti.cetak_invoice()

    pesanan_budi = toko.buat_pesanan(budi)
    try:
        pesanan_budi.tambah_item(toko.cari_produk("B03"), 3)  # stok hanya 2
    except ValueError as e:
        print(f"Gagal menambah item: {e}")
    try:
        pesanan_budi.tambah_item(toko.cari_produk("T02"), 0)
    except ValueError as e:
        print(f"Gagal menambah item: {e}")
    pesanan_budi.tambah_item(toko.cari_produk("B03"), 2)
    pesanan_budi.tambah_item(toko.cari_produk("T02"), 3)
    pesanan_budi.cetak_invoice()
    print()

    print("=== RINGKASAN ===")
    toko.tampilkan_katalog()
    print(f"Jumlah pesanan : {toko.jumlah_pesanan()}")
    print(f"Total penjualan: {format_rupiah(toko.total_penjualan())}")


if __name__ == "__main__":
    main()
