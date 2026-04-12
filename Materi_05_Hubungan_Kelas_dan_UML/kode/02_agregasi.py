"""
============================================================
    MATERI 05 - Hubungan Kelas dan UML
    File: 02_agregasi.py
    Topik: Agregasi - Hubungan "Memiliki" (Has-A Lemah)
============================================================

Agregasi adalah hubungan "memiliki" yang LEBIH KUAT dari asosiasi,
namun bagian masih bisa HIDUP SENDIRI tanpa induknya.

Ciri khas:
  - Objek bagian dibuat DI LUAR objek induk
  - Dikirim via konstruktor atau method
  - Jika induk dihapus, bagian TETAP HIDUP

Diagram UML:
    Jurusan <>------------- Dosen
             "memiliki"  1    *
============================================================
"""

print("=" * 58)
print("  MATERI 05 - Hubungan Kelas dan UML")
print("  02_agregasi.py")
print("=" * 58)


# ============================================================
# CONTOH 1: Agregasi Dasar
# Jurusan memiliki Dosen - Dosen bisa pindah atau tetap ada
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 1: Jurusan <> Dosen (Has-A Lemah)")
print("=" * 58)


class Dosen:
    """Dosen berdiri sendiri - bisa bergabung/keluar dari Jurusan apapun."""

    def __init__(self, nama, nip, bidang_keahlian):
        self.nama            = nama
        self.nip             = nip
        self.bidang_keahlian = bidang_keahlian

    @property
    def info_singkat(self):
        return f"{self.nama} (Bid: {self.bidang_keahlian})"

    def __str__(self):
        return f"Dosen: {self.nama} | NIP: {self.nip} | Bidang: {self.bidang_keahlian}"


class Jurusan:
    """
    Jurusan MEMILIKI banyak Dosen (Agregasi).
    Dosen dikirim dari luar - bukan dibuat oleh Jurusan.
    """

    def __init__(self, nama, kode):
        self.nama  = nama
        self.kode  = kode
        self._dosen = []   # list referensi ke objek Dosen dari luar

    def tambah_dosen(self, dosen):
        """Dosen DIKIRIM dari luar - bukan diciptakan di sini."""
        if not isinstance(dosen, Dosen):
            raise TypeError("Harus objek Dosen!")
        if dosen.nip in [d.nip for d in self._dosen]:
            print(f"  [!] {dosen.nama} sudah terdaftar di {self.nama}")
            return
        self._dosen.append(dosen)
        print(f"  [+] {dosen.nama} bergabung ke Jurusan {self.nama}")

    def keluarkan_dosen(self, nip):
        """Menghapus referensi dosen dari Jurusan, BUKAN menghapus objek."""
        before = len(self._dosen)
        self._dosen = [d for d in self._dosen if d.nip != nip]
        if len(self._dosen) < before:
            print(f"  [-] Dosen dengan NIP {nip} dikeluarkan dari {self.nama}")

    @property
    def jumlah_dosen(self):
        return len(self._dosen)

    def tampilkan(self):
        print(f"\n  Jurusan: {self.nama} ({self.kode})")
        print(f"  Jumlah Dosen: {self.jumlah_dosen}")
        for d in self._dosen:
            print(f"    - {d.info_singkat}")

    def __str__(self):
        return f"Jurusan {self.nama} ({self.kode}) - {self.jumlah_dosen} dosen"


# ---- Demo Contoh 1 ----
print("\nMembuat objek Dosen secara INDEPENDEN:")
d1 = Dosen("Dr. Anton Prafanto", "NIP001", "Machine Learning")
d2 = Dosen("Dr. Budi Hartono",   "NIP002", "Network Security")
d3 = Dosen("Dr. Citra Lestari",  "NIP003", "Database Systems")
d4 = Dosen("Dr. Dewi Rahayu",    "NIP004", "Software Engineering")

for d in [d1, d2, d3, d4]:
    print(f"  {d}")

print("\nMenghubungkan Dosen ke Jurusan (Agregasi):")
jurusan_if = Jurusan("Informatika", "IF")
jurusan_si = Jurusan("Sistem Informasi", "SI")

jurusan_if.tambah_dosen(d1)
jurusan_if.tambah_dosen(d2)
jurusan_if.tambah_dosen(d3)

jurusan_si.tambah_dosen(d3)    # d3 bisa ada di DUA Jurusan sekaligus
jurusan_si.tambah_dosen(d4)

# Mencoba menambah duplikat
jurusan_if.tambah_dosen(d1)

jurusan_if.tampilkan()
jurusan_si.tampilkan()

print("\nTest: dosen pindah jurusan")
jurusan_if.keluarkan_dosen("NIP002")
jurusan_if.tambah_dosen(d4)
jurusan_if.tampilkan()

# Bukti: hapus jurusan_if, dosen-dosennya masih ada
print("\nHapus jurusan_if:")
del jurusan_if
print(f"  d1 masih ada: {d1}")
print(f"  d2 masih ada: {d2}")
print(f"  d3 masih ada di jurusan_si: {jurusan_si}")


# ============================================================
# CONTOH 2: Agregasi Bersarang
# Universitas memiliki banyak Fakultas
# Setiap Fakultas memiliki banyak Jurusan
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 2: Universitas <> Fakultas <> Jurusan")
print("=" * 58)


class JurusanSimple:
    """Jurusan sederhana untuk demo Universitas."""

    def __init__(self, nama, jenjang="S1"):
        self.nama    = nama
        self.jenjang = jenjang

    def __str__(self):
        return f"{self.jenjang} {self.nama}"


class Fakultas:
    """Fakultas memiliki banyak Jurusan (Agregasi)."""

    def __init__(self, nama, dekan):
        self.nama   = nama
        self.dekan  = dekan
        self._jurusan = []

    def tambah_jurusan(self, jurusan):
        self._jurusan.append(jurusan)

    def tampilkan(self):
        print(f"\n  Fakultas: {self.nama}")
        print(f"  Dekan   : {self.dekan}")
        print(f"  Jurusan ({len(self._jurusan)}):")
        for j in self._jurusan:
            print(f"    - {j}")


class Universitas:
    """Universitas memiliki banyak Fakultas (Agregasi)."""

    def __init__(self, nama, kota):
        self.nama     = nama
        self.kota     = kota
        self._fakultas = []

    def tambah_fakultas(self, fakultas):
        self._fakultas.append(fakultas)
        print(f"  [+] Fakultas '{fakultas.nama}' bergabung ke {self.nama}")

    @property
    def total_jurusan(self):
        return sum(len(f._jurusan) for f in self._fakultas)

    def tampilkan_lengkap(self):
        print(f"\n  {'='*50}")
        print(f"  UNIVERSITAS: {self.nama.upper()}")
        print(f"  Kota: {self.kota}")
        print(f"  Total Fakultas: {len(self._fakultas)}")
        print(f"  Total Jurusan : {self.total_jurusan}")
        print(f"  {'='*50}")
        for f in self._fakultas:
            f.tampilkan()


# ---- Demo Contoh 2 ----
# Buat Jurusan (independen)
j_if   = JurusanSimple("Informatika")
j_si   = JurusanSimple("Sistem Informasi")
j_te   = JurusanSimple("Teknik Elektro")
j_tm   = JurusanSimple("Teknik Mesin")
j_ak   = JurusanSimple("Akuntansi")
j_manaj = JurusanSimple("Manajemen")

# Buat Fakultas dan tambahkan Jurusan
fti = Fakultas("Teknik Informatika", "Prof. Budi Santoso, Ph.D")
fti.tambah_jurusan(j_if)
fti.tambah_jurusan(j_si)

ft  = Fakultas("Teknik", "Prof. Sari Dewi, Ph.D")
ft.tambah_jurusan(j_te)
ft.tambah_jurusan(j_tm)

feb = Fakultas("Ekonomi dan Bisnis", "Prof. Andi Wijaya, Ph.D")
feb.tambah_jurusan(j_ak)
feb.tambah_jurusan(j_manaj)

# Buat Universitas dan tambahkan Fakultas
unmul = Universitas("Universitas Mulawarman", "Samarinda")
unmul.tambah_fakultas(fti)
unmul.tambah_fakultas(ft)
unmul.tambah_fakultas(feb)

unmul.tampilkan_lengkap()


# ============================================================
# CONTOH 3: Agregasi vs Asosiasi - Perbedaan Jelas
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 3: Agregasi vs Asosiasi - Perbedaan Kunci")
print("=" * 58)


class ProyekRiset:
    """
    Proyek Riset MEMILIKI anggota peneliti (Agregasi).
    Peneliti bisa keluar/masuk proyek dan tetap eksis.
    Tapi Proyek MENGGUNAKAN Lab sebagai tempat kerja (Asosiasi).
    """

    def __init__(self, judul, ketua):
        self.judul   = judul
        self.ketua   = ketua
        self._anggota = []   # AGREGASI: peneliti dikirim dari luar

    def tambah_anggota(self, peneliti):
        """AGREGASI: peneliti adalah objek yang sudah ada sebelumnya."""
        self._anggota.append(peneliti)
        print(f"  [+] {peneliti} bergabung ke '{self.judul}'")

    def lakukan_riset_di_lab(self, lab):
        """ASOSIASI: lab diterima sebagai parameter, dipakai sementara."""
        print(f"\n  [LAB] Tim '{self.judul}' menggunakan {lab}")
        print(f"  [LAB] Anggota ({len(self._anggota)}):")
        for a in self._anggota:
            print(f"         - {a}")

    def __str__(self):
        return f"Proyek: {self.judul} (Ketua: {self.ketua})"


class Peneliti:
    def __init__(self, nama, keahlian):
        self.nama     = nama
        self.keahlian = keahlian

    def __str__(self):
        return f"{self.nama} [{self.keahlian}]"


class Lab:
    def __init__(self, nama, kapasitas):
        self.nama      = nama
        self.kapasitas = kapasitas

    def __str__(self):
        return f"Lab {self.nama} (kapasitas {self.kapasitas} orang)"


# ---- Demo Contoh 3 ----
p1 = Peneliti("Dr. Anton", "AI")
p2 = Peneliti("Dr. Budi",  "IoT")
p3 = Peneliti("Dr. Citra", "Big Data")

lab_ai  = Lab("Artificial Intelligence", 20)
lab_iot = Lab("Internet of Things", 15)

proyek_ikn = ProyekRiset("Sistem Cerdas Monitoring IKN", "Dr. Anton")
proyek_ikn.tambah_anggota(p1)   # AGREGASI
proyek_ikn.tambah_anggota(p2)   # AGREGASI
proyek_ikn.tambah_anggota(p3)   # AGREGASI

proyek_ikn.lakukan_riset_di_lab(lab_ai)   # ASOSIASI
proyek_ikn.lakukan_riset_di_lab(lab_iot)  # ASOSIASI (lab berbeda)

print(f"\n  Ringkasan:")
print(f"  {proyek_ikn}")
print(f"  Peneliti masih ada setelah proyek:")
for p in [p1, p2, p3]:
    print(f"    - {p}")


print("\n[OK] Selesai: 02_agregasi.py")
print("     Lanjut ke: 03_komposisi.py")
