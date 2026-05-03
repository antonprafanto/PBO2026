"""
Kode Praktik - Materi 11: Prinsip SOLID
File: 02_lsp_isp_dip.py
Topik: Liskov Substitution (LSP), Interface Segregation (ISP), Dependency Inversion (DIP)

Jalankan: python 02_lsp_isp_dip.py
"""

from abc import ABC, abstractmethod

# ======================================================================
# BAGIAN 1: Liskov Substitution Principle (LSP)
#           Fokus: subclass harus bisa menggantikan parent class
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Liskov Substitution Principle (LSP)")
print("=" * 60)

# --- Anti-pattern: Broken Contract ---
print("\n-- Demo Anti-Pattern: Subclass yang break kontrak parent --")


class AktivitasAkademikJelek:
    """
    [JELEK] Base class menjanjikan bisa ikut ujian.
    """
    def ikut_ujian(self):
        return "Mengikuti ujian dengan normal"


class MahasiswaAktifJelek(AktivitasAkademikJelek):
    """Mahasiswa aktif -- bisa ikut ujian."""
    pass


class MahasiswaCutiJelek(AktivitasAkademikJelek):
    """
    Mahasiswa cuti -- TIDAK BISA ikut ujian.
    Tapi masih inherit dari AktivitasAkademik yang menjanjikan ikut ujian!
    """
    def ikut_ujian(self):
        raise Exception("Mahasiswa cuti tidak boleh ikut ujian!")


def proses_ujian(peserta: AktivitasAkademikJelek):
    """
    Expect peserta bisa ikut ujian (dari type annotation).
    """
    hasil = peserta.ikut_ujian()
    print(f"  Peserta ujian: {hasil}")


print("  Mahasiswa aktif:")
proses_ujian(MahasiswaAktifJelek())   # OK

print("  Mahasiswa cuti:")
try:
    proses_ujian(MahasiswaCutiJelek())  # CRASH!
except Exception as e:
    print(f"  ERROR: {e}")

# --- Pattern: Proper Hierarchy ---
print("\n-- Demo Pattern: Hierarchy yang menghormati LSP --")


class StatusMahasiswa:
    """Base class untuk semua status mahasiswa."""
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama


class MahasiswaAktif(StatusMahasiswa):
    """
    Mahasiswa aktif -- bisa ikut ujian.
    """
    def ikut_ujian(self):
        return f"{self.nama} mengikuti ujian dengan normal"

    def ikut_kelas(self):
        return f"{self.nama} hadir di kelas"


class MahasiswaCuti(StatusMahasiswa):
    """
    Mahasiswa cuti -- TIDAK punya method ikut_ujian.
    Tidak claim bisa melakukan sesuatu yang tidak bisa.
    """
    def cuti_dari_akademik(self):
        return f"{self.nama} sedang cuti akademik"


class MahasiswaDO(StatusMahasiswa):
    """
    Mahasiswa DO -- TIDAK punya method ikut_ujian atau ikut_kelas.
    """
    def status_keluar(self):
        return f"{self.nama} telah keluar dari kampus"


def proses_ujian_baik(peserta: MahasiswaAktif):
    """
    [BAIK] Hanya terima MahasiswaAktif, bukan base class.
    Jaminan: peserta pasti bisa ikut ujian.
    """
    hasil = peserta.ikut_ujian()
    print(f"  Peserta ujian: {hasil}")


def proses_status(mahasiswa: StatusMahasiswa):
    """
    [BAIK] Terima base class StatusMahasiswa.
    Hanya panggil method yang pasti ada di semua subclass.
    """
    print(f"  Mahasiswa: {mahasiswa.nama} (NIM {mahasiswa.nim})")


print()
aktif = MahasiswaAktif("2301001", "Budi Santoso")
cuti = MahasiswaCuti("2301042", "Sari Dewi")
do = MahasiswaDO("2301087", "Ahmad Fauzi")

print("  Proses ujian (hanya MahasiswaAktif):")
proses_ujian_baik(aktif)

print("\n  Proses status (semua status):")
proses_status(aktif)
proses_status(cuti)
proses_status(do)

print("\n  [POINT] Tidak ada surprise exception!")
print("          Kontrak hierarchy jelas dan dihormati.")

# ======================================================================
# BAGIAN 2: Interface Segregation Principle (ISP)
#           Fokus: interface kecil dan focused, bukan fat interface
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Interface Segregation Principle (ISP)")
print("=" * 60)

# --- Anti-pattern: Fat Interface ---
print("\n-- Demo Anti-Pattern: Interface besar yang harus di-implement semua --")


class PekerjaAkademikJelek(ABC):
    """
    [JELEK] Interface raksasa -- semua orang akademik harus implement ini.
    Tapi tidak semua orang akademik melakukan semua tugas!
    """
    @abstractmethod
    def mengajar(self):
        pass

    @abstractmethod
    def meneliti(self):
        pass

    @abstractmethod
    def mentoring_mahasiswa(self):
        pass

    @abstractmethod
    def publikasi_internasional(self):
        pass

    @abstractmethod
    def memimpin_laboratorium(self):
        pass


class DosenPenuhJelek(PekerjaAkademikJelek):
    """Dosen penuh -- implement semua."""
    def mengajar(self): return "Mengajar IF204"
    def meneliti(self): return "Riset AI"
    def mentoring_mahasiswa(self): return "Bimbing 5 mahasiswa"
    def publikasi_internasional(self): return "Publikasi di IEEE"
    def memimpin_laboratorium(self): return "Pimpin Lab AI"


class AsistenJelek(PekerjaAkademikJelek):
    """
    Asisten -- paksa implement semua, padahal tidak semua bisa dilakukan.
    """
    def mengajar(self): raise NotImplementedError("Asisten tidak mengajar")
    def meneliti(self): return "Bantu riset dosen"
    def mentoring_mahasiswa(self): raise NotImplementedError("Asisten tidak mentoring")
    def publikasi_internasional(self): raise NotImplementedError("Asisten tidak publikasi")
    def memimpin_laboratorium(self): return "Jaga lab"


print("  Fat interface -- banyak NotImplementedError yang artificial")
asisten_jelek = AsistenJelek()
try:
    print(f"  - {asisten_jelek.mengajar()}")
except NotImplementedError as e:
    print(f"  - NotImplementedError: {e}")
try:
    print(f"  - {asisten_jelek.mentoring_mahasiswa()}")
except NotImplementedError as e:
    print(f"  - NotImplementedError: {e}")

# --- Pattern: Segregated Interfaces ---
print("\n-- Demo Pattern: Interface kecil, hanya method yang relevan --")


class Pengajar(ABC):
    """Interface untuk yang bisa mengajar."""
    @abstractmethod
    def mengajar(self):
        pass


class Peneliti(ABC):
    """Interface untuk yang melakukan riset."""
    @abstractmethod
    def meneliti(self):
        pass


class Mentor(ABC):
    """Interface untuk yang membimbing."""
    @abstractmethod
    def mentoring_mahasiswa(self):
        pass


class Penulis(ABC):
    """Interface untuk publikasi."""
    @abstractmethod
    def publikasi_internasional(self):
        pass


class PemimpinLab(ABC):
    """Interface untuk memimpin lab."""
    @abstractmethod
    def memimpin_laboratorium(self):
        pass


class DosenPenuh(Pengajar, Peneliti, Mentor, Penulis, PemimpinLab):
    """Dosen penuh -- implement semua interface yang applicable."""
    def mengajar(self): return "Mengajar IF204"
    def meneliti(self): return "Riset AI"
    def mentoring_mahasiswa(self): return "Bimbing 5 mahasiswa"
    def publikasi_internasional(self): return "Publikasi di IEEE"
    def memimpin_laboratorium(self): return "Pimpin Lab AI"


class Asisten(Peneliti, PemimpinLab):
    """Asisten -- hanya implement interface yang bisa dilakukan."""
    def meneliti(self): return "Bantu riset dosen"
    def memimpin_laboratorium(self): return "Jaga lab"


class DosenAdjaran(Pengajar):
    """Dosen adjaran -- hanya mengajar, bukan peneliti."""
    def mengajar(self): return "Mengajar IF101 (2 kelas)"


class PenelitiBaru(Peneliti):
    """Peneliti baru -- fokus riset, bukan mengajar dulu."""
    def meneliti(self): return "Riset Machine Learning"


print()
print("  Segregated interfaces -- hanya implement yang relevan:")

dosen_penuh = DosenPenuh()
print(f"  DosenPenuh: {dosen_penuh.mengajar()}")
print(f"  DosenPenuh: {dosen_penuh.meneliti()}")
print(f"  DosenPenuh: {dosen_penuh.publikasi_internasional()}")

asisten = Asisten()
print(f"  Asisten: {asisten.meneliti()}")
print(f"  Asisten: {asisten.memimpin_laboratorium()}")

dosen_adjaran = DosenAdjaran()
print(f"  DosenAdjaran: {dosen_adjaran.mengajar()}")

print("\n  [POINT] Tidak ada NotImplementedError!")
print("          Setiap class implement hanya method yang relevan.")

# ======================================================================
# BAGIAN 3: Dependency Inversion Principle (DIP)
#           Fokus: depend pada abstraksi, bukan konkret
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 3: Dependency Inversion Principle (DIP)")
print("=" * 60)

# --- Anti-pattern: Tight Coupling ---
print("\n-- Demo Anti-Pattern: Hardcode dependency konkret --")


class DatabaseSQLiteJelek:
    """Database konkret -- SQLite."""
    def ambil_mahasiswa(self, nim):
        print(f"    [SQLite] SELECT * FROM mahasiswa WHERE nim='{nim}'")
        return {"nim": nim, "nama": "Budi", "ipk": 3.75}


class SistemAkademikJelek:
    """
    [JELEK] Hardcode depend pada DatabaseSQLiteJelek.
    Tidak bisa ganti database tanpa ubah kode!
    """
    def __init__(self):
        self.db = DatabaseSQLiteJelek()  # Hardcoded!

    def cari_mahasiswa(self, nim):
        return self.db.ambil_mahasiswa(nim)


print("  Hardcoded dependency:")
sistem_jelek = SistemAkademikJelek()
print(f"  Cari mahasiswa 2301001: {sistem_jelek.cari_mahasiswa('2301001')}")
print("  Problem: Jika mau ganti SQLite -> PostgreSQL, harus ubah SistemAkademikJelek!")

# --- Pattern: Dependency Injection ---
print("\n-- Demo Pattern: Inject dependency, depend pada abstraksi --")


class RepositoriMahasiswa(ABC):
    """Abstraksi -- interface saja."""
    @abstractmethod
    def ambil_mahasiswa(self, nim):
        pass

    @abstractmethod
    def simpan_mahasiswa(self, mahasiswa):
        pass


class RepositoriMahasiswaSQLite(RepositoriMahasiswa):
    """Konkret -- SQLite."""
    def ambil_mahasiswa(self, nim):
        print(f"    [SQLite] SELECT * FROM mahasiswa WHERE nim='{nim}'")
        return {"nim": nim, "nama": "Budi", "ipk": 3.75}

    def simpan_mahasiswa(self, mahasiswa):
        print(f"    [SQLite] INSERT INTO mahasiswa VALUES (...)")
        return True


class RepositoriMahasiswaPostgreSQL(RepositoriMahasiswa):
    """Konkret -- PostgreSQL."""
    def ambil_mahasiswa(self, nim):
        print(f"    [PostgreSQL] SELECT * FROM public.mahasiswa WHERE nim=$1")
        return {"nim": nim, "nama": "Sari", "ipk": 3.45}

    def simpan_mahasiswa(self, mahasiswa):
        print(f"    [PostgreSQL] INSERT INTO public.mahasiswa VALUES (...)")
        return True


class RepositoriMahasiswaAPI(RepositoriMahasiswa):
    """Konkret -- REST API."""
    def ambil_mahasiswa(self, nim):
        print(f"    [API] GET /api/mahasiswa/{nim}")
        return {"nim": nim, "nama": "Ahmad", "ipk": 3.55}

    def simpan_mahasiswa(self, mahasiswa):
        print(f"    [API] POST /api/mahasiswa")
        return True


class SistemAkademikBaik:
    """
    [BAIK] Depend pada abstraksi RepositoriMahasiswa.
    Bisa inject repository apa saja!
    """
    def __init__(self, repository: RepositoriMahasiswa):
        self.repo = repository  # Inject -- tidak hardcoded!

    def cari_mahasiswa(self, nim):
        return self.repo.ambil_mahasiswa(nim)

    def daftar_mahasiswa_baru(self, mahasiswa):
        return self.repo.simpan_mahasiswa(mahasiswa)


print()
print("  Dependency injection -- flexible!")

print("\n  -- Dengan SQLite --")
sistem_sqlite = SistemAkademikBaik(RepositoriMahasiswaSQLite())
print(f"  Cari: {sistem_sqlite.cari_mahasiswa('2301001')}")

print("\n  -- Dengan PostgreSQL --")
sistem_postgres = SistemAkademikBaik(RepositoriMahasiswaPostgreSQL())
print(f"  Cari: {sistem_postgres.cari_mahasiswa('2301001')}")

print("\n  -- Dengan API --")
sistem_api = SistemAkademikBaik(RepositoriMahasiswaAPI())
print(f"  Cari: {sistem_api.cari_mahasiswa('2301001')}")

print("\n  [POINT] Tanpa ubah SistemAkademikBaik, bisa ganti repository!")
print("          Testing juga mudah -- inject mock repository.")


class RepositoriMahasiswaMock(RepositoriMahasiswa):
    """Mock untuk testing."""
    def ambil_mahasiswa(self, nim):
        return {"nim": nim, "nama": "Test", "ipk": 4.0}

    def simpan_mahasiswa(self, mahasiswa):
        return True


print("\n  -- Testing dengan Mock --")
sistem_test = SistemAkademikBaik(RepositoriMahasiswaMock())
print(f"  Cari (mock): {sistem_test.cari_mahasiswa('TEST001')}")

print()
print("Selesai! LSP, ISP, dan DIP dijalankan tanpa error.")
