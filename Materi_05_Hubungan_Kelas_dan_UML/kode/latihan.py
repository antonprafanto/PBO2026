"""
============================================================
    MATERI 05 - Hubungan Kelas dan UML
    File: latihan.py
    Topik: Soal Latihan Mandiri
============================================================

PETUNJUK:
  - Kerjakan setiap soal di bagian yang sudah disediakan.
  - Jalankan file ini untuk melihat output:
      python latihan.py
  - Jika output sesuai komentar, jawabanmu BENAR!

TINGKAT KESULITAN:
  Soal 1: (*  ) Asosiasi dasar
  Soal 2: (** ) Agregasi dengan logika bisnis
  Soal 3: (** ) Komposisi bertingkat
  Soal 4: (***) Sistem lengkap menggabungkan ketiga hubungan
============================================================
"""

print("=" * 60)
print("         LATIHAN MANDIRI - MATERI 05")
print("         Hubungan Kelas dan UML")
print("=" * 60)


# ============================================================
# SOAL 1 - Asosiasi (Tingkat: *)
# ============================================================
# Buat dua kelas: `Pengemudi` dan `Kendaraan`.
#
# Kelas Kendaraan:
#   - Atribut: plat_nomor (str), jenis (str), kapasitas_bensin (float)
#   - Method: isi_bensin(liter) -> tambah ke bensin, cetak konfirmasi
#   - Method: __str__ -> "[plat_nomor] jenis"
#
# Kelas Pengemudi:
#   - Atribut: nama (str), sim_nomor (str)
#   - Method: kendarai(kendaraan, tujuan)
#       -> ASOSIASI: kendaraan diterima sebagai parameter
#       -> Cetak: "[nama] mengendarai [kendaraan] menuju [tujuan]"
#   - Method: isi_bahan_bakar(kendaraan, liter)
#       -> Panggil kendaraan.isi_bensin(liter)
# ============================================================

print("\n--- SOAL 1: Asosiasi - Pengemudi dan Kendaraan ---")


class Kendaraan:
    def __init__(self, plat_nomor, jenis, kapasitas_bensin):
        # TODO: Definisikan atribut
        pass

    def isi_bensin(self, liter):
        # TODO: Tambah liter ke bensin_saat_ini, cetak konfirmasi
        # Format: "  [plat] Terisi {liter}L. Bensin: {bensin_saat_ini}/{kapasitas}L"
        pass

    def __str__(self):
        # TODO: Kembalikan "[plat_nomor] jenis"
        pass


class Pengemudi:
    def __init__(self, nama, sim_nomor):
        # TODO: Definisikan atribut
        pass

    def kendarai(self, kendaraan, tujuan):
        # TODO: Cetak "[nama] mengendarai [kendaraan] menuju [tujuan]"
        pass

    def isi_bahan_bakar(self, kendaraan, liter):
        # TODO: Panggil kendaraan.isi_bensin(liter)
        pass


# Test Soal 1
mobil1 = Kendaraan("KB 1234 AB", "Toyota Avanza", 50)
mobil2 = Kendaraan("KT 5678 CD", "Honda Jazz",    40)

budi = Pengemudi("Budi Santoso", "SIM-A-001")
sari = Pengemudi("Sari Dewi",    "SIM-A-002")

budi.kendarai(mobil1, "Balikpapan")
# -> Budi Santoso mengendarai [KB 1234 AB] Toyota Avanza menuju Balikpapan

sari.kendarai(mobil1, "Bontang")
# -> Sari Dewi mengendarai [KB 1234 AB] Toyota Avanza menuju Bontang
# (Kendaraan yang SAMA bisa dikendarai pengemudi berbeda - Asosiasi!)

budi.isi_bahan_bakar(mobil2, 30)
# ->   [KT 5678 CD] Terisi 30L. Bensin: 30/40L

print()


# ============================================================
# SOAL 2 - Agregasi (Tingkat: **)
# ============================================================
# Buat sistem Perpustakaan dengan Agregasi.
#
# Kelas Buku:
#   - Atribut: isbn (str), judul (str), penulis (str), tersedia (bool=True)
#   - Method: pinjam() -> ubah tersedia=False, cetak konfirmasi
#   - Method: kembalikan() -> ubah tersedia=True, cetak konfirmasi
#   - Method: __str__ -> "[isbn] judul - penulis"
#
# Kelas Perpustakaan (Agregasi: memiliki banyak Buku):
#   - Method: daftarkan_buku(buku) -> tambah ke koleksi
#   - Method: cari_buku(kata_kunci) -> cari di judul/penulis, return list
#   - Method: pinjam_buku(isbn, peminjam_nama) ->
#       cari buku, pinjam jika tersedia, cetak siapa yang pinjam
#   - Method: kembalikan_buku(isbn) -> cari dan kembalikan buku
#   - Property: total_buku -> jumlah buku di koleksi
#   - Property: buku_tersedia -> buku yang tersedia (tersedia=True)
#   - Method: tampilkan_katalog() -> cetak semua buku + status
# ============================================================

print("--- SOAL 2: Agregasi - Sistem Perpustakaan ---")


class Buku:
    def __init__(self, isbn, judul, penulis):
        # TODO: Definisikan atribut (tersedia default True)
        pass

    def pinjam(self):
        # TODO: Set tersedia=False, cetak "[isbn] '[judul]' dipinjam"
        pass

    def kembalikan(self):
        # TODO: Set tersedia=True, cetak "[isbn] '[judul]' dikembalikan"
        pass

    def __str__(self):
        # TODO: Kembalikan "[isbn] judul - penulis"
        pass


class Perpustakaan:
    def __init__(self, nama, kota):
        # TODO: Definisikan atribut dan _koleksi (list kosong)
        pass

    def daftarkan_buku(self, buku):
        # TODO: Tambah buku ke _koleksi
        # BUKU DIKIRIM DARI LUAR - ini AGREGASI!
        pass

    def cari_buku(self, kata_kunci):
        # TODO: Cari di judul DAN penulis (case-insensitive)
        # Kembalikan list buku yang cocok
        pass

    def pinjam_buku(self, isbn, peminjam_nama):
        # TODO: Cari buku by isbn, jika tersedia: pinjam + cetak konfirmasi
        # Jika tidak tersedia: cetak peringatan
        # Jika tidak ditemukan: cetak peringatan
        pass

    def kembalikan_buku(self, isbn):
        # TODO: Cari buku by isbn, kembalikan
        pass

    @property
    def total_buku(self):
        # TODO: Kembalikan len(_koleksi)
        pass

    @property
    def buku_tersedia(self):
        # TODO: Kembalikan list buku yang tersedia=True
        pass

    def tampilkan_katalog(self):
        # TODO: Cetak semua buku beserta status [TERSEDIA] / [DIPINJAM]
        pass


# Test Soal 2
# Buku dibuat INDEPENDEN dari Perpustakaan (ciri khas Agregasi)
bk1 = Buku("978-001", "Clean Code",               "Robert C. Martin")
bk2 = Buku("978-002", "Pemrograman Python OOP",   "Anton Prafanto")
bk3 = Buku("978-003", "Design Patterns",           "Gang of Four")
bk4 = Buku("978-004", "The Pragmatic Programmer",  "David Thomas")

perpus = Perpustakaan("Perpustakaan FKTI Unmul", "Samarinda")
for b in [bk1, bk2, bk3, bk4]:
    perpus.daftarkan_buku(b)

print(f"  Total buku: {perpus.total_buku}")
# -> Total buku: 4

perpus.pinjam_buku("978-002", "Budi Santoso")
# -> [978-002] 'Pemrograman Python OOP' dipinjam oleh Budi Santoso

perpus.pinjam_buku("978-002", "Sari Dewi")
# -> [!] Buku '978-002' sedang dipinjam!

print(f"  Buku tersedia: {len(perpus.buku_tersedia)}")
# -> Buku tersedia: 3

hasil = perpus.cari_buku("python")
print(f"  Hasil cari 'python': {len(hasil)} buku")
# -> Hasil cari 'python': 1 buku

perpus.kembalikan_buku("978-002")
# -> [978-002] 'Pemrograman Python OOP' dikembalikan

perpus.tampilkan_katalog()
# -> isi katalog dengan status masing-masing

# Bukti Agregasi: Buku tetap ada setelah perpustakaan dihapus
del perpus
print(f"\n  Buku masih ada: {bk1}")
print()


# ============================================================
# SOAL 3 - Komposisi (Tingkat: **)
# ============================================================
# Buat sistem `LaporanKeuangan` yang terdiri dari `ItemLaporan`.
#
# Kelas ItemLaporan (BAGIAN - tidak bisa eksis sendiri):
#   - Atribut: deskripsi (str), jumlah (float), kategori (str)
#              kategori: "PEMASUKAN" atau "PENGELUARAN"
#   - Property: is_pemasukan -> True jika kategori == "PEMASUKAN"
#   - Method: __str__ -> "[kategori] deskripsi: Rp jumlah"
#
# Kelas LaporanKeuangan (INDUK yang membuat ItemLaporan):
#   - Atribut: judul (str), periode (str)
#   - Method: catat_pemasukan(deskripsi, jumlah)
#       -> Buat ItemLaporan di dalam method ini (Komposisi!)
#   - Method: catat_pengeluaran(deskripsi, jumlah)
#       -> Buat ItemLaporan di dalam method ini (Komposisi!)
#   - Property: total_pemasukan -> jumlah semua pemasukan
#   - Property: total_pengeluaran -> jumlah semua pengeluaran
#   - Property: saldo_akhir -> pemasukan - pengeluaran
#   - Method: tampilkan() -> cetak laporan lengkap dengan ringkasan
# ============================================================

print("--- SOAL 3: Komposisi - Laporan Keuangan ---")


class ItemLaporan:
    KATEGORI_VALID = {"PEMASUKAN", "PENGELUARAN"}

    def __init__(self, deskripsi, jumlah, kategori):
        # TODO: Validasi kategori, definisikan atribut
        pass

    @property
    def is_pemasukan(self):
        # TODO: Kembalikan True jika kategori == "PEMASUKAN"
        pass

    def __str__(self):
        # TODO: "[kategori] deskripsi: Rp jumlah:,.0f"
        pass


class LaporanKeuangan:
    def __init__(self, judul, periode):
        # TODO: Definisikan atribut + _items (list kosong)
        pass

    def catat_pemasukan(self, deskripsi, jumlah):
        # TODO: Buat ItemLaporan("PEMASUKAN") DI SINI lalu simpan ke _items
        pass

    def catat_pengeluaran(self, deskripsi, jumlah):
        # TODO: Buat ItemLaporan("PENGELUARAN") DI SINI lalu simpan ke _items
        pass

    @property
    def total_pemasukan(self):
        # TODO: Jumlahkan semua item bertipe PEMASUKAN
        pass

    @property
    def total_pengeluaran(self):
        # TODO: Jumlahkan semua item bertipe PENGELUARAN
        pass

    @property
    def saldo_akhir(self):
        # TODO: Kembalikan total_pemasukan - total_pengeluaran
        pass

    def tampilkan(self):
        # TODO: Cetak laporan rapi: judul, periode, semua item,
        #       ringkasan pemasukan/pengeluaran/saldo
        pass


# Test Soal 3
laporan = LaporanKeuangan("Laporan Keuangan HMIF", "Maret 2026")
laporan.catat_pemasukan("Iuran anggota",           2_500_000)
laporan.catat_pemasukan("Sponsor kegiatan",        5_000_000)
laporan.catat_pemasukan("Penjualan merchandise",     750_000)
laporan.catat_pengeluaran("Sewa gedung seminar",   3_000_000)
laporan.catat_pengeluaran("Konsumsi acara",        1_200_000)
laporan.catat_pengeluaran("Cetak spanduk",           350_000)
laporan.catat_pengeluaran("Operasional sekretariat", 500_000)

laporan.tampilkan()
# Diharapkan:
# ============ Laporan Keuangan HMIF ============
# Periode: Maret 2026
# ...daftar semua item...
# Total Pemasukan   : Rp 8,250,000
# Total Pengeluaran : Rp 5,050,000
# SALDO AKHIR       : Rp 3,200,000

print(f"  Saldo akhir: Rp {laporan.saldo_akhir:,.0f}")
# -> Saldo akhir: Rp 3,200,000
print()


# ============================================================
# SOAL 4 - Sistem Lengkap (Tingkat: ***)
# ============================================================
# Bangun sistem manajemen proyek sederhana yang menggabungkan:
#   - ASOSIASI:  Proyek menggunakan Tool saat eksekusi
#   - AGREGASI:  Proyek memiliki banyak Anggota Tim
#   - KOMPOSISI: Proyek terdiri dari Task-Task
#
# Kelas Tool:
#   - Atribut: nama (str), tipe (str)
#   - Method: gunakan(nama_task) -> cetak "[nama] digunakan untuk [nama_task]"
#
# Kelas AnggotaTim:
#   - Atribut: nama (str), peran (str), email (str)
#   - Method: __str__ -> "nama (peran)"
#
# Kelas Task (KOMPOSISI - bagian dari Proyek):
#   - Atribut: judul (str), prioritas (str: "Tinggi"/"Sedang"/"Rendah")
#              status (str: "Todo"/"On Progress"/"Done"), _ditugaskan ke (AnggotaTim/None)
#   - Method: mulai() -> ubah status ke "On Progress"
#   - Method: selesai() -> ubah status ke "Done"
#   - Method: tugaskan(anggota) -> set _ditugaskan ke anggota
#   - Method: __str__ -> "[status] judul (prioritas) -> penanggungjawab"
#
# Kelas Proyek:
#   - Atribut: nama (str), deskripsi (str)
#   - Method: tambah_anggota(anggota) -> AGREGASI: anggota dari luar
#   - Method: buat_task(judul, prioritas) -> KOMPOSISI: Task dibuat di sini
#   - Method: gunakan_tool(tool, nama_task) -> ASOSIASI: tool sbg parameter
#   - Method: tampilkan_dashboard() -> cetak ringkasan proyek
#   - Property: progres -> persentase task Done / total task
# ============================================================

print("--- SOAL 4: Sistem Proyek (Asosiasi + Agregasi + Komposisi) ---")


class Tool:
    def __init__(self, nama, tipe):
        # TODO
        pass

    def gunakan(self, nama_task):
        # TODO: Cetak "[nama Tool] digunakan untuk '[nama_task]'"
        pass


class AnggotaTim:
    def __init__(self, nama, peran, email):
        # TODO
        pass

    def __str__(self):
        # TODO: "nama (peran)"
        pass


class Task:
    PRIORITAS_VALID = {"Tinggi", "Sedang", "Rendah"}

    def __init__(self, judul, prioritas="Sedang"):
        # TODO: status default "Todo", _penanggungjawab = None
        pass

    def mulai(self):
        # TODO: status -> "On Progress", cetak konfirmasi
        pass

    def selesai(self):
        # TODO: status -> "Done", cetak konfirmasi
        pass

    def tugaskan(self, anggota):
        # TODO: Set _penanggungjawab ke anggota
        pass

    def __str__(self):
        # TODO: "[status] judul (prioritas) -> penanggungjawab atau 'Belum ditugaskan'"
        pass


class Proyek:
    def __init__(self, nama, deskripsi):
        # TODO: _anggota dan _tasks (list kosong)
        pass

    def tambah_anggota(self, anggota):
        # TODO: AGREGASI - anggota dikirim dari luar
        pass

    def buat_task(self, judul, prioritas="Sedang"):
        # TODO: KOMPOSISI - Task dibuat di dalam method ini
        # Kembalikan task yang baru dibuat
        pass

    def gunakan_tool(self, tool, nama_task):
        # TODO: ASOSIASI - tool diterima sebagai parameter
        pass

    @property
    def progres(self):
        # TODO: Persentase task berstatus "Done" dari total task
        # Kembalikan float 0-100, atau 0.0 jika tidak ada task
        pass

    def tampilkan_dashboard(self):
        # TODO: Cetak dashboard proyek yang rapi:
        # - Nama dan deskripsi proyek
        # - Daftar anggota tim
        # - Daftar task dengan status
        # - Progres keseluruhan
        pass


# Test Soal 4
# 1. Anggota Tim dibuat INDEPENDEN (akan di-AGREGASI ke Proyek)
a1 = AnggotaTim("Anton Prafanto", "Project Manager",  "anton@unmul.ac.id")
a2 = AnggotaTim("Budi Santoso",   "Backend Dev",      "budi@unmul.ac.id")
a3 = AnggotaTim("Sari Dewi",      "Frontend Dev",     "sari@unmul.ac.id")
a4 = AnggotaTim("Andi Wijaya",    "QA Engineer",      "andi@unmul.ac.id")

# 2. Tools berdiri sendiri (akan di-ASOSIASI ke Proyek)
git    = Tool("GitHub",   "Version Control")
docker = Tool("Docker",   "Containerization")
pytest = Tool("PyTest",   "Testing Framework")

# 3. Buat Proyek
proyek_ikn = Proyek(
    "SiMonitor IKN",
    "Sistem monitoring pembangunan IKN berbasis AI"
)

# 4. Tambah Anggota (AGREGASI)
proyek_ikn.tambah_anggota(a1)
proyek_ikn.tambah_anggota(a2)
proyek_ikn.tambah_anggota(a3)
proyek_ikn.tambah_anggota(a4)

# 5. Buat Task (KOMPOSISI)
t1 = proyek_ikn.buat_task("Setup repository dan CI/CD",  "Tinggi")
t2 = proyek_ikn.buat_task("Desain arsitektur sistem",    "Tinggi")
t3 = proyek_ikn.buat_task("Implementasi API backend",    "Tinggi")
t4 = proyek_ikn.buat_task("Implementasi dashboard UI",   "Sedang")
t5 = proyek_ikn.buat_task("Integrasi AI module",         "Sedang")
t6 = proyek_ikn.buat_task("Testing dan QA",              "Rendah")

# 6. Tugaskan dan kerjakan Task
t1.tugaskan(a2)
t2.tugaskan(a1)
t3.tugaskan(a2)
t4.tugaskan(a3)
t5.tugaskan(a2)
t6.tugaskan(a4)

t1.mulai()
t1.selesai()
t2.mulai()
t2.selesai()
t3.mulai()

# 7. Gunakan Tools (ASOSIASI)
proyek_ikn.gunakan_tool(git,    "Setup repository dan CI/CD")
proyek_ikn.gunakan_tool(docker, "Implementasi API backend")
proyek_ikn.gunakan_tool(pytest, "Testing dan QA")

# 8. Tampilkan Dashboard
proyek_ikn.tampilkan_dashboard()
# Diharapkan:
# == DASHBOARD PROYEK: SiMonitor IKN ==
# ...anggota tim...
# ...daftar task dengan status...
# Progres: X% (N/M task selesai)

print(f"\n  Anggota tim masih ada setelah proyek dihapus (Agregasi):")
del proyek_ikn
for a in [a1, a2, a3, a4]:
    print(f"  {a}")


print("\n\n" + "=" * 60)
print("  Selesai mengerjakan latihan Materi 05!")
print("  Cocokkan outputmu dengan komentar di setiap soal.")
print("=" * 60)
