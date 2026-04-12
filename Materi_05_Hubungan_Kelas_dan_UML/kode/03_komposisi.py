"""
============================================================
    MATERI 05 - Hubungan Kelas dan UML
    File: 03_komposisi.py
    Topik: Komposisi - Hubungan "Terdiri dari" (Has-A Kuat)
============================================================

Komposisi adalah hubungan PALING KUAT.
Objek bagian TIDAK BISA HIDUP tanpa induknya.
Bagian dibuat DAN dihancurkan bersama induknya.

Ciri khas:
  - Objek bagian dibuat DI DALAM objek induk
  - Tidak bisa dibagikan ke induk lain
  - Jika induk dihapus, bagian ikut musnah

Diagram UML:
    Rumah *------------- Kamar
           "terdiri dari" 1  1..*
============================================================
"""

print("=" * 58)
print("  MATERI 05 - Hubungan Kelas dan UML")
print("  03_komposisi.py")
print("=" * 58)


# ============================================================
# CONTOH 1: Komposisi Dasar
# Rumah terdiri dari Kamar-kamar
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 1: Rumah * Kamar (Terdiri Dari)")
print("=" * 58)


class Kamar:
    """
    Kamar TIDAK BISA EKSIS tanpa Rumah.
    Dibuat oleh Rumah, hancur bersama Rumah.
    """

    def __init__(self, nomor, fungsi, luas_m2):
        self.nomor   = nomor
        self.fungsi  = fungsi
        self.luas_m2 = luas_m2

    def __str__(self):
        return f"Kamar {self.nomor}: {self.fungsi} ({self.luas_m2} m2)"


class Rumah:
    """
    Rumah terdiri dari Kamar (Komposisi).
    Rumah yang menciptakan dan mengontrol semua Kamarnya.
    """

    def __init__(self, alamat, pemilik):
        self.alamat  = alamat
        self.pemilik = pemilik
        self._kamar  = []   # dibuat kosong, diisi lewat method internal

    def tambah_kamar(self, fungsi, luas_m2):
        """Kamar DIBUAT DI DALAM Rumah, bukan dikirim dari luar."""
        nomor    = len(self._kamar) + 1
        kamar_baru = Kamar(nomor, fungsi, luas_m2)   # diciptakan di sini
        self._kamar.append(kamar_baru)
        return kamar_baru

    def bangun_standar(self):
        """Bangun ruangan standar sekaligus."""
        self.tambah_kamar("Ruang Tamu",        25)
        self.tambah_kamar("Kamar Tidur Utama", 20)
        self.tambah_kamar("Kamar Tidur 2",     15)
        self.tambah_kamar("Dapur",             12)
        self.tambah_kamar("Kamar Mandi",        6)
        print(f"  Rumah {self.pemilik} dibangun dengan {len(self._kamar)} kamar.")

    @property
    def total_luas(self):
        return sum(k.luas_m2 for k in self._kamar)

    @property
    def jumlah_kamar(self):
        return len(self._kamar)

    def tampilkan(self):
        print(f"\n  Rumah milik: {self.pemilik}")
        print(f"  Alamat     : {self.alamat}")
        print(f"  Total luas : {self.total_luas} m2 | {self.jumlah_kamar} kamar")
        for k in self._kamar:
            print(f"    - {k}")

    def __str__(self):
        return (f"Rumah @ {self.alamat} "
                f"({self.jumlah_kamar} kamar, {self.total_luas} m2)")


# ---- Demo Contoh 1 ----
rumah_budi = Rumah("Jl. Mulawarman No. 5, Samarinda", "Budi Santoso")
rumah_budi.bangun_standar()
rumah_budi.tambah_kamar("Garasi", 18)
rumah_budi.tampilkan()

rumah_sari = Rumah("Jl. Gatot Subroto No. 12, Samarinda", "Sari Dewi")
rumah_sari.tambah_kamar("Ruang Tamu",  30)
rumah_sari.tambah_kamar("Kamar Tidur", 22)
rumah_sari.tambah_kamar("Kamar Mandi", 8)
rumah_sari.tampilkan()

print(f"\n  {rumah_budi}")
print(f"  {rumah_sari}")


# ============================================================
# CONTOH 2: Komposisi dengan Method Kaya
# Order terdiri dari OrderItem
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 2: Order * OrderItem (E-Commerce)")
print("=" * 58)


class Produk:
    """Produk berdiri sendiri di katalog (bukan bagian dari Order)."""

    def __init__(self, kode, nama, harga, stok=0):
        self.kode  = kode
        self.nama  = nama
        self.harga = harga
        self.stok  = stok

    def __str__(self):
        return f"[{self.kode}] {self.nama} - Rp {self.harga:,.0f}"


class OrderItem:
    """
    OrderItem adalah BAGIAN dari Order (Komposisi).
    Tidak ada OrderItem tanpa Order.
    """

    def __init__(self, produk, qty):
        if not isinstance(produk, Produk):
            raise TypeError("produk harus objek Produk!")
        if qty <= 0:
            raise ValueError("qty harus positif!")
        self.produk = produk
        self.qty    = qty

    @property
    def subtotal(self):
        return self.produk.harga * self.qty

    def __str__(self):
        return (f"{self.produk.nama} x{self.qty} "
                f"@ Rp {self.produk.harga:,.0f} = Rp {self.subtotal:,.0f}")


class Order:
    """
    Order terdiri dari OrderItem (Komposisi).
    Order juga memiliki Pelanggan (Agregasi - dikirim dari luar).
    """

    _counter = 0

    def __init__(self, pelanggan_nama, alamat_kirim):
        Order._counter   += 1
        self.id           = f"ORD-{Order._counter:04d}"
        self.pelanggan    = pelanggan_nama
        self.alamat_kirim = alamat_kirim
        self._items       = []    # KOMPOSISI: items dibuat di dalam Order
        self._status      = "Pending"

    def tambah_item(self, produk, qty):
        """Membuat OrderItem baru di dalam Order (Komposisi)."""
        # Cek stok
        if produk.stok < qty:
            raise ValueError(
                f"Stok {produk.nama} tidak cukup! "
                f"Tersedia: {produk.stok}, diminta: {qty}"
            )
        # Cek apakah produk sudah ada di order (update qty)
        for item in self._items:
            if item.produk.kode == produk.kode:
                item.qty += qty
                produk.stok -= qty
                print(f"  [UPDATE] {produk.nama} qty menjadi {item.qty}")
                return
        # Buat OrderItem baru
        item_baru = OrderItem(produk, qty)   # dibuat di sini
        self._items.append(item_baru)
        produk.stok -= qty
        print(f"  [+] {item_baru}")

    def hapus_item(self, kode_produk):
        """Menghapus OrderItem dari Order (bukan objek Produk-nya)."""
        sebelum = len(self._items)
        for item in self._items:
            if item.produk.kode == kode_produk:
                item.produk.stok += item.qty   # kembalikan stok
        self._items = [i for i in self._items if i.produk.kode != kode_produk]
        if len(self._items) < sebelum:
            print(f"  [-] Produk {kode_produk} dihapus dari order")

    @property
    def total(self):
        return sum(item.subtotal for item in self._items)

    @property
    def jumlah_item(self):
        return len(self._items)

    def konfirmasi(self):
        if not self._items:
            raise RuntimeError("Order kosong! Tambahkan item dulu.")
        self._status = "Dikonfirmasi"
        print(f"\n  [OK] Order {self.id} dikonfirmasi!")

    def cetak_struk(self):
        print(f"\n  {'='*48}")
        print(f"  STRUK ORDER: {self.id}")
        print(f"  Pelanggan  : {self.pelanggan}")
        print(f"  Kirim ke   : {self.alamat_kirim}")
        print(f"  Status     : {self._status}")
        print(f"  {'-'*48}")
        for item in self._items:
            print(f"  {item}")
        print(f"  {'-'*48}")
        print(f"  TOTAL      : Rp {self.total:,.0f}")
        print(f"  {'='*48}")

    def __str__(self):
        return f"Order {self.id} | {self.pelanggan} | {self.jumlah_item} item | Rp {self.total:,.0f}"


# ---- Demo Contoh 2 ----
# Produk di katalog (independen)
laptop  = Produk("LPT-001", "Laptop ASUS VivoBook",    8_500_000, stok=10)
mouse   = Produk("MSE-001", "Mouse Logitech M330",       150_000, stok=50)
kboard  = Produk("KBD-001", "Keyboard Mechanical",       350_000, stok=20)
headset = Produk("HDS-001", "Headset Sony WH-1000XM5",  4_200_000, stok=5)

print("\nKatalog Produk:")
for p in [laptop, mouse, kboard, headset]:
    print(f"  {p} | Stok: {p.stok}")

print("\nMembuat Order 1:")
order1 = Order("Budi Santoso", "Jl. Mulawarman No. 5, Samarinda")
order1.tambah_item(laptop, 1)
order1.tambah_item(mouse,  2)
order1.tambah_item(kboard, 1)
order1.konfirmasi()
order1.cetak_struk()

print("\nMembuat Order 2:")
order2 = Order("Sari Dewi", "Jl. Gatot Subroto No. 12, Samarinda")
order2.tambah_item(headset, 1)
order2.tambah_item(mouse,   1)
order2.tambah_item(mouse,   2)   # update qty

print("\nCoba hapus item:")
order2.hapus_item("MSE-001")
print(f"  Stok mouse kembali: {mouse.stok}")
order2.cetak_struk()

print("\nSemua order:")
for o in [order1, order2]:
    print(f"  {o}")

print(f"\nStok produk setelah semua order:")
for p in [laptop, mouse, kboard, headset]:
    print(f"  {p.nama}: tersisa {p.stok}")


# ============================================================
# CONTOH 3: Perbandingan - Kenapa ini BUKAN Agregasi
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 3: Ringkasan Perbandingan Komposisi vs Agregasi")
print("=" * 58)

print("""
  KOMPOSISI (Contoh 1 & 2 di atas):
    - rumah_budi.tambah_kamar("Dapur", 12)
      Kamar diciptakan DI DALAM method tambah_kamar()
      Tidak ada referensi ke Kamar selain dari rumah itu

    - order1.tambah_item(laptop, 1)
      OrderItem diciptakan DI DALAM method tambah_item()
      OrderItem tidak bisa berdiri sendiri

  AGREGASI (Perbandingan):
    - jurusan.tambah_dosen(dosen)   <-- dosen sudah ada!
      Dosen diciptakan DI LUAR Jurusan
      Dosen bisa ikut jurusan lain juga
      Jika jurusan dihapus, dosen tetap ada

  PERTANYAAN KUNCI: "Apakah bagian bisa hidup tanpa induk?"
    - Kamar tanpa Rumah? Tidak masuk akal.    -> KOMPOSISI
    - Dosen tanpa Jurusan? Masuk akal.        -> AGREGASI
    - Printer tanpa Mahasiswa? Masuk akal.    -> ASOSIASI
""")


print("\n[OK] Selesai: 03_komposisi.py")
print("     Lanjut ke: latihan.py")
