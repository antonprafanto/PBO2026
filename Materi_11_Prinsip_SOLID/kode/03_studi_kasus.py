"""
Kode Praktik - Materi 11: Prinsip SOLID
File: 03_studi_kasus.py
Topik: Penerapan Prinsip SOLID pada Sistem KRS dan Penilaian Akademik

Jalankan: python 03_studi_kasus.py
"""

from abc import ABC, abstractmethod
from contextlib import contextmanager

# ======================================================================
# SKENARIO 1: Sistem Pendaftaran KRS dengan SOLID
# ======================================================================
print("=" * 60)
print("SKENARIO 1: Sistem Pendaftaran KRS Compliant SOLID")
print("=" * 60)

# ===== SRP: Setiap class satu tanggung jawab =====

class Mahasiswa:
    """Tanggung jawab: representasi data mahasiswa."""
    def __init__(self, nim, nama, ipk, tunggakan=0):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk
        self.tunggakan = tunggakan

    def __str__(self):
        return f"{self.nim} | {self.nama} (IPK {self.ipk})"


class MataKuliah:
    """Tanggung jawab: representasi mata kuliah."""
    def __init__(self, kode, nama, sks, prasyarat=None):
        self.kode = kode
        self.nama = nama
        self.sks = sks
        self.prasyarat = prasyarat or []

    def __str__(self):
        return f"{self.kode} | {self.nama} ({self.sks} SKS)"


# ===== OCP: Strategy untuk berbagai tipe validasi =====

class ValidasiPendaftaran(ABC):
    """Abstraksi validasi -- bisa extend tanpa modify."""
    @abstractmethod
    def validasi(self, mahasiswa, matkul):
        """Return True jika valid, raise exception jika tidak."""
        pass


class ValidasiTunggakan(ValidasiPendaftaran):
    """Strategi: cek tunggakan SPP."""
    def validasi(self, mahasiswa, matkul):
        if mahasiswa.tunggakan > 0:
            raise Exception(f"{mahasiswa.nama} ada tunggakan SPP Rp {mahasiswa.tunggakan}")
        return True


class ValidasiIPK(ValidasiPendaftaran):
    """Strategi: cek IPK minimum."""
    def __init__(self, ipk_minimum=2.0):
        self.ipk_minimum = ipk_minimum

    def validasi(self, mahasiswa, matkul):
        if mahasiswa.ipk < self.ipk_minimum:
            raise Exception(f"{mahasiswa.nama} IPK {mahasiswa.ipk} < {self.ipk_minimum}")
        return True


class ValidasiPrasyarat(ValidasiPendaftaran):
    """Strategi: cek prasyarat (akan di-implement di latihan)."""
    def __init__(self, riwayat_lulus):
        self.riwayat_lulus = riwayat_lulus

    def validasi(self, mahasiswa, matkul):
        # Simulasi: assume sudah lulus semua prasyarat
        return True


class ValidasiSKS(ValidasiPendaftaran):
    """Strategi: cek batas maksimal SKS."""
    def __init__(self, batas_sks=24):
        self.batas_sks = batas_sks
        self.sks_terdaftar = {}

    def set_sks_terdaftar(self, nim, total_sks):
        """Set total SKS yang sudah terdaftar untuk mahasiswa."""
        self.sks_terdaftar[nim] = total_sks

    def validasi(self, mahasiswa, matkul):
        total = self.sks_terdaftar.get(mahasiswa.nim, 0) + matkul.sks
        if total > self.batas_sks:
            raise Exception(f"{mahasiswa.nama}: {total} SKS > {self.batas_sks} (maks)")
        return True


# ===== LSP & ISP: Repository dengan kontrak jelas =====

class RepositoriMahasiswa(ABC):
    """Interface untuk akses data mahasiswa."""
    @abstractmethod
    def ambil(self, nim):
        pass


class RepositoriMataKuliah(ABC):
    """Interface untuk akses data matakuliah."""
    @abstractmethod
    def ambil(self, kode):
        pass


class RepositoriMahasiswaInMemory(RepositoriMahasiswa):
    """Implementasi in-memory (untuk demo)."""
    def __init__(self):
        self._data = {}

    def simpan(self, mahasiswa):
        self._data[mahasiswa.nim] = mahasiswa

    def ambil(self, nim):
        return self._data.get(nim)


class RepositoriMataKuliahInMemory(RepositoriMataKuliah):
    """Implementasi in-memory untuk matakuliah."""
    def __init__(self):
        self._data = {}

    def simpan(self, matkul):
        self._data[matkul.kode] = matkul

    def ambil(self, kode):
        return self._data.get(kode)


# ===== DIP: Sistem KRS inject repository dan validator =====

class SistemKRS:
    """
    Sistem KRS dengan SOLID:
    - SRP: hanya handle logic KRS
    - DIP: inject repository dan validator
    """
    def __init__(
        self,
        repo_mahasiswa: RepositoriMahasiswa,
        repo_matkul: RepositoriMataKuliah,
        validators: list
    ):
        self.repo_mhs = repo_mahasiswa
        self.repo_mk = repo_matkul
        self.validators = validators
        self._krs_data = {}  # nim -> list of kode_mk

    def daftar(self, nim, kode_mk):
        """Daftarkan mahasiswa ke matakuliah."""
        mhs = self.repo_mhs.ambil(nim)
        mk = self.repo_mk.ambil(kode_mk)

        if not mhs or not mk:
            raise Exception("Mahasiswa atau matakuliah tidak ditemukan")

        # Run semua validator
        for validator in self.validators:
            validator.validasi(mhs, mk)

        # Jika lolos semua, daftar
        if nim not in self._krs_data:
            self._krs_data[nim] = []
        self._krs_data[nim].append(kode_mk)

        return True

    def lihat_krs(self, nim):
        """Lihat KRS mahasiswa."""
        return self._krs_data.get(nim, [])


# --- Setup dan test ---
print("\n-- Setup data --")

# Repository
repo_mhs = RepositoriMahasiswaInMemory()
repo_mk = RepositoriMataKuliahInMemory()

# Populasi data
mhs1 = Mahasiswa("2301001", "Budi Santoso", 3.75, tunggakan=0)
mhs2 = Mahasiswa("2301042", "Sari Dewi", 3.45, tunggakan=2_000_000)
mhs3 = Mahasiswa("2301087", "Ahmad Fauzi", 1.80, tunggakan=0)

repo_mhs.simpan(mhs1)
repo_mhs.simpan(mhs2)
repo_mhs.simpan(mhs3)

mk1 = MataKuliah("IF204", "Pemrograman Berorientasi Objek", 3)
mk2 = MataKuliah("IF301", "Keamanan Informasi", 4)

repo_mk.simpan(mk1)
repo_mk.simpan(mk2)

# Setup validator dengan OCP
validators = [
    ValidasiTunggakan(),
    ValidasiIPK(ipk_minimum=2.0),
    ValidasiPrasyarat({}),
]

val_sks = ValidasiSKS(batas_sks=24)
val_sks.set_sks_terdaftar("2301001", 20)  # Sudah 20 SKS
validators.append(val_sks)

# Buat sistem KRS dengan DIP
sistem_krs = SistemKRS(repo_mhs, repo_mk, validators)

# Test pendaftaran
print("\n-- Pendaftaran Mahasiswa --")

test_cases = [
    ("2301001", "IF204", True),   # Should pass
    ("2301001", "IF301", False),  # 20+4=24, OK but exactly limit
    ("2301042", "IF204", False),  # Ada tunggakan
    ("2301087", "IF204", False),  # IPK terlalu rendah
]

for nim, kode, should_pass in test_cases:
    mhs = repo_mhs.ambil(nim)
    try:
        sistem_krs.daftar(nim, kode_mk=kode)
        status = "BERHASIL"
    except Exception as e:
        status = f"GAGAL: {str(e)[:50]}"

    symbol = "[OK]" if (should_pass and "BERHASIL" in status) or \
             (not should_pass and "GAGAL" in status) else "[?]"
    print(f"  {symbol} {nim} ({mhs.nama}) -> {kode}: {status}")

print("\n  KRS Budi Santoso:")
krs_budi = sistem_krs.lihat_krs("2301001")
print(f"  Terdaftar di: {krs_budi}")

# ======================================================================
# SKENARIO 2: Sistem Penilaian dengan SOLID
# ======================================================================
print()
print("=" * 60)
print("SKENARIO 2: Sistem Penilaian Akademik Compliant SOLID")
print("=" * 60)

# ===== SRP: Strategi kalkulasi nilai =====

class StrategiKalkulasiNilai(ABC):
    """Interface untuk strategi kalkulasi nilai."""
    @abstractmethod
    def kalkulasi(self, nilai_uts, nilai_uas, nilai_tugas=0):
        pass


class StrategiRegular(StrategiKalkulasiNilai):
    """Strategi regular: 40% UTS, 60% UAS."""
    def kalkulasi(self, nilai_uts, nilai_uas, nilai_tugas=0):
        return nilai_uts * 0.4 + nilai_uas * 0.6


class StrategiPraktik(StrategiKalkulasiNilai):
    """Strategi praktik: 20% UTS, 40% UAS, 40% praktik."""
    def kalkulasi(self, nilai_uts, nilai_uas, nilai_tugas=0):
        return nilai_uts * 0.2 + nilai_uas * 0.4 + nilai_tugas * 0.4


class StrategiSeminar(StrategiKalkulasiNilai):
    """Strategi seminar: 10% UTS, 30% UAS, 60% presentasi."""
    def kalkulasi(self, nilai_uts, nilai_uas, nilai_tugas=0):
        return nilai_uts * 0.1 + nilai_uas * 0.3 + nilai_tugas * 0.6


# ===== SRP: Konversi nilai ke huruf =====

class KonverterNilaiKeHuruf:
    """Tanggung jawab: konversi nilai numerik ke huruf."""
    @staticmethod
    def konversi(nilai):
        if nilai >= 85: return "A"
        if nilai >= 70: return "B"
        if nilai >= 55: return "C"
        if nilai >= 40: return "D"
        return "E"


# ===== SRP: Penyimpanan nilai =====

class RepositoriNilai:
    """Tanggung jawab: persist nilai ke storage."""
    def __init__(self):
        self._data = {}  # (nim, kode_mk) -> nilai_akhir

    def simpan(self, nim, kode_mk, nilai_akhir):
        self._data[(nim, kode_mk)] = nilai_akhir
        return True

    def ambil(self, nim, kode_mk):
        return self._data.get((nim, kode_mk))


# ===== DIP: Sistem penilaian inject strategi dan repository =====

class SistemPenilaian:
    """
    Sistem penilaian dengan SOLID:
    - SRP: hanya koordinasi penilaian
    - DIP: inject strategi kalkulasi dan repository
    """
    def __init__(self, repo_nilai: RepositoriNilai):
        self.repo = repo_nilai
        self.konverter = KonverterNilaiKeHuruf()

    def input_nilai(
        self,
        mahasiswa: Mahasiswa,
        matkul: MataKuliah,
        strategi: StrategiKalkulasiNilai,
        nilai_uts,
        nilai_uas,
        nilai_tugas=0
    ):
        """Input nilai dengan strategi tertentu."""
        # Kalkulasi
        nilai_akhir = strategi.kalkulasi(nilai_uts, nilai_uas, nilai_tugas)

        # Simpan
        self.repo.simpan(mahasiswa.nim, matkul.kode, nilai_akhir)

        return nilai_akhir

    def ambil_nilai(self, nim, kode_mk):
        """Ambil nilai yang sudah disimpan."""
        return self.repo.ambil(nim, kode_mk)

    def konversi_huruf(self, nilai):
        """Konversi nilai ke huruf."""
        return self.konverter.konversi(nilai)


# --- Setup dan test ---
print("\n-- Setup sistem penilaian --")

repo_nilai = RepositoriNilai()
sistem_nilai = SistemPenilaian(repo_nilai)

# Input nilai dengan berbagai strategi
print("\n-- Input Nilai dengan Strategi Berbeda --")

# Regular class
nilai_regular = sistem_nilai.input_nilai(
    mhs1, mk1,
    StrategiRegular(),
    nilai_uts=85, nilai_uas=90
)
print(f"  {mhs1.nama} ({mk1.kode}) Regular: {nilai_regular:.1f} -> {sistem_nilai.konversi_huruf(nilai_regular)}")

# Praktik class
nilai_praktik = sistem_nilai.input_nilai(
    mhs1, mk2,
    StrategiPraktik(),
    nilai_uts=80, nilai_uas=85, nilai_tugas=95
)
print(f"  {mhs1.nama} ({mk2.kode}) Praktik: {nilai_praktik:.1f} -> {sistem_nilai.konversi_huruf(nilai_praktik)}")

# Ambil kembali dari repository
print("\n-- Verifikasi Data di Repository --")
nilai_ambil = sistem_nilai.ambil_nilai("2301001", "IF204")
print(f"  Nilai {mhs1.nama} di IF204: {nilai_ambil:.1f}")

print()
print("Selesai! Kedua skenario menerapkan SOLID principles.")
