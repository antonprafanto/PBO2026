"""
Kode Praktik - Materi 08: Abstraksi (Abstraction)
File: 02_abstract_property_dan_interface.py
Topik: Template Method Pattern, Multiple Interface, Hierarki Abstrak

Jalankan: python 02_abstract_property_dan_interface.py
"""

from abc import ABC, abstractmethod

# ======================================================================
# BAGIAN 1: Template Method Pattern
#
# Konsep: Kelas abstrak mendefinisikan URUTAN langkah-langkah suatu
# algoritma (template). Kelas anak hanya mengisi DETAIL tiap langkah.
#
# Skenario: Proses Registrasi Mahasiswa di Sistem Akademik
#   Urutan selalu sama: validasi -> simpan data -> buat akun -> kirim email
#   Tapi detail implementasinya berbeda untuk setiap jalur masuk.
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Template Method Pattern — Registrasi Mahasiswa")
print("=" * 60)


class RegistrasiMahasiswaABC(ABC):
    """
    Template Method: proses_registrasi() mendefinisikan URUTAN langkah.
    Subkelas hanya perlu mengisi detail setiap langkah yang berbeda.
    """

    def proses_registrasi(self, nama, nim, data_tambahan=None):
        """
        TEMPLATE METHOD — urutan ini tidak berubah untuk semua jalur masuk.
        Ini adalah method konkret yang memanggil method abstrak di bawahnya.
        """
        print(f"\n  Memulai registrasi: {nama} ({nim})")
        print(f"  Jalur: {self.nama_jalur()}")
        print("  " + "-" * 46)

        if not self.validasi_persyaratan(nim, data_tambahan):
            print("  [X] Registrasi gagal: persyaratan tidak terpenuhi.")
            return False

        self._simpan_ke_database(nama, nim)
        akun = self._buat_akun_sistem(nim)
        self._kirim_notifikasi(nama, nim, akun)

        # Hook method — punya default, boleh di-override
        self._langkah_tambahan(nama, nim, data_tambahan)

        print(f"  [OK] Registrasi {nama} berhasil! Akun: {akun}")
        return True

    # -- Abstract methods ------------------------------------------------

    @abstractmethod
    def nama_jalur(self):
        """Nama jalur penerimaan mahasiswa."""
        pass

    @abstractmethod
    def validasi_persyaratan(self, nim, data_tambahan):
        """Validasi persyaratan khusus setiap jalur. Return True/False."""
        pass

    # -- Concrete methods (implementasi default, boleh di-override) ------

    def _simpan_ke_database(self, nama, nim):
        """Langkah yang sama untuk semua jalur."""
        print(f"  [DB] Menyimpan data: {nama} / {nim}")

    def _buat_akun_sistem(self, nim):
        """Membuat akun dengan format default."""
        return f"{nim}@student.unmul.ac.id"

    def _kirim_notifikasi(self, nama, nim, akun):
        """Mengirim notifikasi standar."""
        print(f"  [Email] Notifikasi dikirim ke akun {akun}")

    def _langkah_tambahan(self, nama, nim, data_tambahan):
        """Hook method — subkelas bisa override untuk langkah ekstra."""
        pass   # default: tidak ada langkah tambahan


class RegistrasiSNBP(RegistrasiMahasiswaABC):
    """Registrasi jalur SNBP (undangan berdasarkan nilai rapor)."""

    NILAI_MINIMUM = 75.0

    def nama_jalur(self):
        return "SNBP (Seleksi Nasional Berdasarkan Prestasi)"

    def validasi_persyaratan(self, nim, data_tambahan):
        nilai_rapor = data_tambahan.get("nilai_rapor", 0) if data_tambahan else 0
        if nilai_rapor < self.NILAI_MINIMUM:
            print(f"  [Validasi] Nilai rapor {nilai_rapor} < minimum {self.NILAI_MINIMUM}")
            return False
        print(f"  [Validasi] Nilai rapor {nilai_rapor} OK")
        return True

    def _langkah_tambahan(self, nama, nim, data_tambahan):
        print(f"  [SNBP] Mendaftarkan ke program beasiswa prestasi")


class RegistrasiSNBT(RegistrasiMahasiswaABC):
    """Registrasi jalur SNBT (tes tertulis nasional)."""

    SKOR_MINIMUM = 550

    def nama_jalur(self):
        return "SNBT (Seleksi Nasional Berdasarkan Tes)"

    def validasi_persyaratan(self, nim, data_tambahan):
        skor = data_tambahan.get("skor_utbk", 0) if data_tambahan else 0
        if skor < self.SKOR_MINIMUM:
            print(f"  [Validasi] Skor UTBK {skor} < minimum {self.SKOR_MINIMUM}")
            return False
        print(f"  [Validasi] Skor UTBK {skor} OK")
        return True


class RegistrasiMandiri(RegistrasiMahasiswaABC):
    """Registrasi jalur mandiri (ujian langsung oleh universitas)."""

    def nama_jalur(self):
        return "Jalur Mandiri Universitas Mulawarman"

    def validasi_persyaratan(self, nim, data_tambahan):
        lulus_ujian = data_tambahan.get("lulus_ujian", False) if data_tambahan else False
        bukti_bayar = data_tambahan.get("bukti_bayar", False) if data_tambahan else False

        if not lulus_ujian:
            print("  [Validasi] Ujian mandiri belum lulus")
            return False
        if not bukti_bayar:
            print("  [Validasi] Bukti pembayaran belum ada")
            return False

        print("  [Validasi] Lulus ujian & bukti bayar OK")
        return True

    def _buat_akun_sistem(self, nim):
        """Override: akun jalur mandiri punya format berbeda."""
        return f"mnd.{nim}@student.unmul.ac.id"

    def _langkah_tambahan(self, nama, nim, data_tambahan):
        print(f"  [Mandiri] Mengarsipkan berkas fisik ke bagian kemahasiswaan")


# --- Demo Template Method ---
snbp    = RegistrasiSNBP()
snbt    = RegistrasiSNBT()
mandiri = RegistrasiMandiri()

snbp.proses_registrasi("Budi Santoso",   "2601001", {"nilai_rapor": 88.5})
snbt.proses_registrasi("Sari Dewi",      "2601002", {"skor_utbk": 620})
snbt.proses_registrasi("Eko Prasetyo",   "2601003", {"skor_utbk": 480})   # gagal
mandiri.proses_registrasi("Rini Wahyuni","2601004", {"lulus_ujian": True,
                                                      "bukti_bayar": True})
print()


# ======================================================================
# BAGIAN 2: Multiple Interface (Kelas Abstrak Berganda)
#
# Satu kelas mengimplementasikan LEBIH DARI SATU ABC sekaligus.
# Mirip konsep "interface" di Java/C#.
#
# Skenario: Dosen di Universitas bisa punya banyak peran
# ======================================================================
print("=" * 60)
print("BAGIAN 2: Multiple Interface — Peran Dosen Kampus")
print("=" * 60)


class BisaMengajar(ABC):
    """Interface: semua yang bisa mengajar."""

    @abstractmethod
    def mengajar(self, mata_kuliah):
        """Kegiatan mengajar."""
        pass

    @abstractmethod
    def buat_soal_ujian(self, mata_kuliah):
        """Membuat soal ujian."""
        pass


class BisaMenulis(ABC):
    """Interface: semua yang bisa menulis karya ilmiah."""

    @abstractmethod
    def tulis_jurnal(self, judul):
        """Menulis artikel jurnal."""
        pass

    @abstractmethod
    def sitasi_karya(self):
        """Mengembalikan jumlah sitasi karya."""
        pass


class BisaMembimbing(ABC):
    """Interface: semua yang bisa membimbing mahasiswa."""

    @abstractmethod
    def bimbing_skripsi(self, nama_mahasiswa):
        """Membimbing skripsi mahasiswa."""
        pass

    @abstractmethod
    def bimbing_pkl(self, nama_mahasiswa):
        """Membimbing PKL/magang."""
        pass


class DosenBiasa(BisaMengajar, BisaMembimbing):
    """
    Dosen biasa: bisa mengajar dan membimbing,
    tapi tidak punya kewajiban menulis jurnal.
    """

    def __init__(self, nama, nidn):
        self.nama  = nama
        self.nidn  = nidn
        self._mhs_bimbingan = []

    def mengajar(self, mata_kuliah):
        print(f"  {self.nama} mengajar {mata_kuliah} di kelas")

    def buat_soal_ujian(self, mata_kuliah):
        print(f"  {self.nama} membuat soal UTS/UAS untuk {mata_kuliah}")

    def bimbing_skripsi(self, nama_mahasiswa):
        self._mhs_bimbingan.append(nama_mahasiswa)
        print(f"  {self.nama} mulai membimbing skripsi {nama_mahasiswa}")

    def bimbing_pkl(self, nama_mahasiswa):
        print(f"  {self.nama} membimbing PKL {nama_mahasiswa}")

    def __str__(self):
        return f"Dosen {self.nama} (NIDN: {self.nidn})"


class DosenLektor(BisaMengajar, BisaMenulis, BisaMembimbing):
    """
    Dosen Lektor: mengimplementasikan TIGA interface sekaligus.
    Wajib: mengajar, menulis jurnal, dan membimbing.
    """

    def __init__(self, nama, nidn, jumlah_sitasi=0):
        self.nama             = nama
        self.nidn             = nidn
        self._sitasi          = jumlah_sitasi
        self._jurnal_ditulis  = []

    def mengajar(self, mata_kuliah):
        print(f"  Prof. {self.nama} mengajar {mata_kuliah} (metode riset terapan)")

    def buat_soal_ujian(self, mata_kuliah):
        print(f"  Prof. {self.nama} membuat soal berbasis kasus riset untuk {mata_kuliah}")

    def tulis_jurnal(self, judul):
        self._jurnal_ditulis.append(judul)
        print(f"  Prof. {self.nama} menulis jurnal: \"{judul}\"")

    def sitasi_karya(self):
        return self._sitasi

    def bimbing_skripsi(self, nama_mahasiswa):
        print(f"  Prof. {self.nama} membimbing skripsi (level S1/S2): {nama_mahasiswa}")

    def bimbing_pkl(self, nama_mahasiswa):
        print(f"  Prof. {self.nama} mengarahkan PKL ke laboratorium riset: {nama_mahasiswa}")

    def __str__(self):
        return f"Dr. {self.nama} (Lektor, {self._sitasi} sitasi)"


# --- Demo Multiple Interface ---
print()
dosen1  = DosenBiasa("Ahmad Fauzi", "0012345678")
lektor  = DosenLektor("Sri Mulyani", "0087654321", jumlah_sitasi=145)

dosen1.mengajar("Pemrograman Web")
dosen1.bimbing_skripsi("Budi Santoso")
print()
lektor.mengajar("Kecerdasan Buatan")
lektor.tulis_jurnal("Deep Learning untuk Deteksi Penyakit Tanaman di Kalimantan")
lektor.bimbing_skripsi("Sari Dewi")
print()

# Cek interface mana yang diimplementasikan
print(f"  DosenBiasa mengimplementasikan BisaMengajar  : "
      f"{isinstance(dosen1, BisaMengajar)}")
print(f"  DosenBiasa mengimplementasikan BisaMenulis   : "
      f"{isinstance(dosen1, BisaMenulis)}")
print(f"  DosenLektor mengimplementasikan BisaMenulis  : "
      f"{isinstance(lektor, BisaMenulis)}")
print(f"  DosenLektor mengimplementasikan BisaMembimbing: "
      f"{isinstance(lektor, BisaMembimbing)}")

print()

# Fungsi yang hanya menerima BisaMengajar — tidak peduli tipe lain
def jadwalkan_mengajar(pengajar: BisaMengajar, matakuliah: str):
    """Hanya butuh kontrak BisaMengajar."""
    print(f"\n  Menjadwalkan {matakuliah}:")
    pengajar.mengajar(matakuliah)
    pengajar.buat_soal_ujian(matakuliah)

jadwalkan_mengajar(dosen1, "Basis Data")
jadwalkan_mengajar(lektor, "Machine Learning")
print()


# ======================================================================
# BAGIAN 3: Hierarki Kelas Abstrak Bertingkat
#
# Kelas abstrak bisa mewarisi kelas abstrak lain.
# Ini berguna untuk membangun kontrak yang bertingkat.
#
# Skenario: Hierarki laporan akademik
#   LaporanABC -> LaporanMahasiswaABC -> LaporanNilaiMahasiswa
# ======================================================================
print("=" * 60)
print("BAGIAN 3: Hierarki Kelas Abstrak Bertingkat — Laporan Akademik")
print("=" * 60)


class LaporanABC(ABC):
    """
    Level 1 — Kontrak dasar semua laporan di sistem akademik.
    Setiap laporan WAJIB punya: judul, header, dan isi.
    """

    def __init__(self, periode):
        self.periode = periode

    @abstractmethod
    def judul(self):
        pass

    @abstractmethod
    def _header(self):
        """Baris header tabel/laporan."""
        pass

    @abstractmethod
    def _isi(self):
        """Isi utama laporan."""
        pass

    def cetak(self):
        """Template konkret: judul -> header -> isi -> footer."""
        garis = "=" * 60
        print(f"\n  {garis}")
        print(f"  {self.judul()}")
        print(f"  Periode: {self.periode}")
        print(f"  {'-' * 58}")
        self._header()
        print(f"  {'-' * 58}")
        self._isi()
        print(f"  {garis}")


class LaporanMahasiswaABC(LaporanABC):
    """
    Level 2 — Abstrak lagi: spesialisasi untuk laporan mahasiswa.
    Menambahkan kontrak baru: ringkasan_statistik().
    judul(), _header(), _isi() masih wajib diimplementasikan.
    """

    def __init__(self, periode, prodi):
        super().__init__(periode)
        self.prodi = prodi

    @abstractmethod
    def ringkasan_statistik(self):
        """Statistik ringkasan (rata-rata, total, dll.)."""
        pass

    def cetak(self):
        """Override template — tambah ringkasan di akhir."""
        super().cetak()
        print(f"\n  Ringkasan:")
        self.ringkasan_statistik()


class LaporanIPSMahasiswa(LaporanMahasiswaABC):
    """
    Level 3 — Kelas KONKRET: laporan IPS per semester.
    Mengimplementasikan SEMUA method abstrak dari dua level di atas.
    """

    def __init__(self, periode, prodi, data_ips):
        """
        data_ips: list of dict {nama, nim, ips}
        """
        super().__init__(periode, prodi)
        self._data = data_ips

    def judul(self):
        return f"LAPORAN IPS MAHASISWA — {self.prodi.upper()}"

    def _header(self):
        print(f"  {'No':>3}  {'NIM':<12} {'Nama Mahasiswa':<25} {'IPS':>6}")

    def _isi(self):
        for i, mhs in enumerate(self._data, 1):
            ips = mhs["ips"]
            predikat = "[*]" if ips >= 3.50 else ("" if ips >= 2.75 else "[!]")
            print(f"  {i:>3}  {mhs['nim']:<12} {mhs['nama']:<25} "
                  f"{ips:>6.2f} {predikat}")

    def ringkasan_statistik(self):
        nilai_ips = [m["ips"] for m in self._data]
        rata = sum(nilai_ips) / len(nilai_ips)
        tertinggi = max(nilai_ips)
        terendah  = min(nilai_ips)
        di_atas   = sum(1 for n in nilai_ips if n >= 3.00)
        print(f"  Total Mahasiswa : {len(self._data)}")
        print(f"  Rata-rata IPS   : {rata:.2f}")
        print(f"  IPS Tertinggi   : {tertinggi:.2f}")
        print(f"  IPS Terendah    : {terendah:.2f}")
        print(f"  IPS >= 3.00      : {di_atas} mahasiswa "
              f"({di_atas/len(self._data)*100:.1f}%)")


class LaporanKehadiranMahasiswa(LaporanMahasiswaABC):
    """Kelas konkret lain: laporan kehadiran per matakuliah."""

    def __init__(self, periode, prodi, matakuliah, data_hadir):
        super().__init__(periode, prodi)
        self.matakuliah = matakuliah
        self._data      = data_hadir   # list of dict {nama, nim, hadir, total}

    def judul(self):
        return f"LAPORAN KEHADIRAN — {self.matakuliah.upper()}"

    def _header(self):
        print(f"  {'No':>3}  {'NIM':<12} {'Nama':<22} "
              f"{'Hadir':>6} {'Total':>6} {'%':>7}")

    def _isi(self):
        for i, mhs in enumerate(self._data, 1):
            persen = mhs["hadir"] / mhs["total"] * 100
            status = "[OK]" if persen >= 75 else "[X]"
            print(f"  {i:>3}  {mhs['nim']:<12} {mhs['nama']:<22} "
                  f"{mhs['hadir']:>6} {mhs['total']:>6} {persen:>6.1f}% {status}")

    def ringkasan_statistik(self):
        data_persen = [m["hadir"] / m["total"] * 100 for m in self._data]
        lulus_hadir = sum(1 for p in data_persen if p >= 75)
        print(f"  Memenuhi syarat hadir (>=75%): {lulus_hadir}/{len(self._data)}")
        print(f"  Rata-rata kehadiran: {sum(data_persen)/len(data_persen):.1f}%")


# --- Demo Hierarki Abstrak ---
data_ips = [
    {"nim": "2301001", "nama": "Budi Santoso",    "ips": 3.75},
    {"nim": "2301002", "nama": "Sari Dewi",        "ips": 3.20},
    {"nim": "2301003", "nama": "Eko Prasetyo",     "ips": 2.50},
    {"nim": "2301004", "nama": "Rini Wahyuni",     "ips": 3.85},
    {"nim": "2301005", "nama": "Dian Pratama",     "ips": 2.90},
]

data_hadir = [
    {"nim": "2301001", "nama": "Budi Santoso",  "hadir": 14, "total": 16},
    {"nim": "2301002", "nama": "Sari Dewi",      "hadir": 12, "total": 16},
    {"nim": "2301003", "nama": "Eko Prasetyo",   "hadir":  9, "total": 16},
    {"nim": "2301004", "nama": "Rini Wahyuni",   "hadir": 16, "total": 16},
    {"nim": "2301005", "nama": "Dian Pratama",   "hadir": 11, "total": 16},
]

laporan_ips    = LaporanIPSMahasiswa(
    "Genap 2025/2026", "Informatika", data_ips)
laporan_hadir  = LaporanKehadiranMahasiswa(
    "Genap 2025/2026", "Informatika", "Pemrograman Berorientasi Objek", data_hadir)

laporan_ips.cetak()
laporan_hadir.cetak()

print()

# Verifikasi hierarki abstrak
print("  Verifikasi isinstance() hierarki abstrak:")
print(f"  LaporanIPSMahasiswa is LaporanABC          : "
      f"{isinstance(laporan_ips, LaporanABC)}")
print(f"  LaporanIPSMahasiswa is LaporanMahasiswaABC : "
      f"{isinstance(laporan_ips, LaporanMahasiswaABC)}")
print(f"  LaporanIPSMahasiswa is LaporanIPSMahasiswa : "
      f"{isinstance(laporan_ips, LaporanIPSMahasiswa)}")
