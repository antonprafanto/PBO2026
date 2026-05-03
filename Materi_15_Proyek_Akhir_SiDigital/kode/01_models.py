"""
Proyek Akhir SiDigital -- Materi 15
File: 01_models.py
Topik: @dataclass Models + Custom Exception Hierarchy

Jalankan: python 01_models.py
"""

from dataclasses import dataclass, field, asdict
from typing import List, Optional

# ======================================================================
# BAGIAN 1: Custom Exception Hierarchy
#           Fokus: Hierarki exception spesifik domain SiDigital
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Custom Exception Hierarchy")
print("=" * 60)

class SiDigitalError(Exception):
    """Base exception untuk semua error SiDigital."""
    pass

class MahasiswaTidakValid(SiDigitalError):
    """NIM tidak valid atau data mahasiswa tidak lengkap."""
    pass

class MahasiswaTidakDitemukan(SiDigitalError):
    """NIM tidak ada di database."""
    pass

class DosenTidakDitemukan(SiDigitalError):
    """NIP tidak ada di database."""
    pass

class MataKuliahTidakValid(SiDigitalError):
    """SKS di luar range atau data tidak lengkap."""
    pass

class MataKuliahTidakDitemukan(SiDigitalError):
    """Kode MK tidak ada di database."""
    pass

class NilaiTidakValid(SiDigitalError):
    """Nilai di luar range 0-100."""
    pass

print("\n-- Demo Custom Exception --")
try:
    raise MahasiswaTidakValid("NIM harus minimal 6 karakter: '123'")
except SiDigitalError as e:
    print(f"  [SiDigitalError] {type(e).__name__}: {e}")

try:
    raise NilaiTidakValid("Nilai 150 di luar range 0-100")
except NilaiTidakValid as e:
    print(f"  [NilaiTidakValid] {e}")

print("  Hierarki exception: [OK]")

# ======================================================================
# BAGIAN 2: @dataclass Models
#           Fokus: Mahasiswa, Dosen, MataKuliah, Nilai
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: @dataclass Models")
print("=" * 60)

@dataclass
class Mahasiswa:
    """Model data mahasiswa."""
    nim: str
    nama: str
    angkatan: int
    program_studi: str = "Informatika"

    def __post_init__(self):
        if len(self.nim) < 6:
            raise MahasiswaTidakValid(f"NIM minimal 6 karakter: '{self.nim}'")
        if not self.nama.strip():
            raise MahasiswaTidakValid("Nama mahasiswa tidak boleh kosong")

@dataclass
class Dosen:
    """Model data dosen."""
    nip: str
    nama: str
    gelar: str = ""

    def nama_lengkap(self) -> str:
        """Nama dosen dengan gelar."""
        if self.gelar:
            return f"{self.gelar} {self.nama}"
        return self.nama

@dataclass
class MataKuliah:
    """Model data matakuliah."""
    kode: str
    nama: str
    sks: int
    semester: int = 1

    def __post_init__(self):
        if not (1 <= self.sks <= 6):
            raise MataKuliahTidakValid(f"SKS harus 1-6, dapat: {self.sks}")
        if not (1 <= self.semester <= 8):
            raise MataKuliahTidakValid(f"Semester harus 1-8, dapat: {self.semester}")

@dataclass
class Nilai:
    """Model data nilai mahasiswa."""
    nim: str
    kode_mk: str
    nip_dosen: str
    nilai_angka: float

    def __post_init__(self):
        if not (0 <= self.nilai_angka <= 100):
            raise NilaiTidakValid(f"Nilai harus 0-100, dapat: {self.nilai_angka}")

    def get_grade(self) -> str:
        """Konversi nilai angka ke grade huruf."""
        if self.nilai_angka >= 80:
            return "A"
        elif self.nilai_angka >= 70:
            return "B"
        elif self.nilai_angka >= 60:
            return "C"
        elif self.nilai_angka >= 50:
            return "D"
        else:
            return "E"

    def get_bobot(self) -> float:
        """Bobot numerik grade (skala 0-4)."""
        mapping = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
        return mapping[self.get_grade()]

print("\n-- Demo Mahasiswa --")
mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
print(f"  {mhs}")
print(f"  Prodi: {mhs.program_studi}")

print("\n-- Demo Dosen --")
dosen = Dosen("198501001", "Ahmad Fauzi", "Dr.")
print(f"  {dosen}")
print(f"  Nama lengkap: {dosen.nama_lengkap()}")

print("\n-- Demo MataKuliah --")
mk = MataKuliah("IF201", "Pemrograman Berorientasi Objek", 3, 3)
print(f"  {mk}")

print("\n-- Demo Nilai --")
nilai = Nilai("2301001", "IF201", "198501001", 87.5)
print(f"  {nilai}")
print(f"  Grade: {nilai.get_grade()} | Bobot: {nilai.get_bobot()}")

# ======================================================================
# BAGIAN 3: Validasi dan Error Handling
#           Fokus: __post_init__ mencegah data invalid
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Validasi Model")
print("=" * 60)

test_cases = [
    ("NIM terlalu pendek", lambda: Mahasiswa("123", "Test", 2023)),
    ("Nama kosong", lambda: Mahasiswa("2301001", "  ", 2023)),
    ("SKS invalid", lambda: MataKuliah("XX001", "Test", 0)),
    ("Nilai > 100", lambda: Nilai("2301001", "IF201", "NIP001", 101.0)),
    ("Nilai negatif", lambda: Nilai("2301001", "IF201", "NIP001", -5.0)),
]

for label, fn in test_cases:
    try:
        fn()
        print(f"  [FAIL] {label}: seharusnya error!")
    except SiDigitalError as e:
        print(f"  [OK] {label}: {type(e).__name__}")

print("\n-- Serialisasi @dataclass ke dict --")
print(f"  asdict(mhs)  = {asdict(mhs)}")
print(f"  asdict(nilai) = {asdict(nilai)}")

print("\n" + "=" * 60)
print("01_models.py selesai!")
print("=" * 60)
