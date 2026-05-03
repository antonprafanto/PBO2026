"""
Kode Praktik - Materi 13: OOP Modern Python
File: 01_dataclass_basics.py
Topik: @dataclass fundamentals dan advantages

Jalankan: python 01_dataclass_basics.py
"""

from dataclasses import dataclass, field
from typing import List

# ======================================================================
# BAGIAN 1: @dataclass Basics
#           Fokus: Otomatis generate __init__, __repr__, __eq__
# ======================================================================
print("=" * 60)
print("BAGIAN 1: @dataclass Basics")
print("=" * 60)

# [JELEK] Manual class tanpa @dataclass
class MahasiswaManual:
    def __init__(self, nim, nama, angkatan):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
    
    def __repr__(self):
        return f"MahasiswaManual(nim={self.nim}, nama={self.nama}, angkatan={self.angkatan})"
    
    def __eq__(self, other):
        if not isinstance(other, MahasiswaManual):
            return False
        return self.nim == other.nim and self.nama == other.nama and self.angkatan == other.angkatan

print("\n-- Tanpa @dataclass (Manual) --")
mhs_manual = MahasiswaManual("2301001", "Budi Santoso", 2023)
print(f"Manual: {mhs_manual}")
print(f"Equals: {mhs_manual == MahasiswaManual('2301001', 'Budi Santoso', 2023)}")

# [BAIK] @dataclass - auto generate
@dataclass
class Mahasiswa:
    """Mahasiswa dengan @dataclass - much cleaner!"""
    nim: str
    nama: str
    angkatan: int

print("\n-- Dengan @dataclass (Auto) --")
mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
print(f"Auto: {mhs}")
print(f"Equals: {mhs == Mahasiswa('2301001', 'Budi Santoso', 2023)}")

print("\n-- Apa yang di-auto generate? --")
print("[OK] __init__(self, nim, nama, angkatan)")
print("[OK] __repr__() - untuk print()")
print("[OK] __eq__() - untuk comparison dengan ==")

# ======================================================================
# BAGIAN 2: @dataclass Advanced Features
#           Fokus: Default values, field(), frozen, order
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: @dataclass Advanced Features")
print("=" * 60)

@dataclass
class MataKuliah:
    """MataKuliah dengan default values dan field."""
    kode: str
    nama: str
    sks: int
    prerequisite: List[str] = field(default_factory=list)
    semester: int = 1

print("\n-- Default Values Demo --")
mk1 = MataKuliah("IF201", "Database", 3)
mk2 = MataKuliah("IF202", "Algoritma", 3, ["IF101", "IF102"], 2)

print(f"MK1: {mk1}")
print(f"MK2: {mk2}")

@dataclass(frozen=True)
class NilaiFrozen:
    """Immutable dataclass - can't modify."""
    nim: str
    kode_mk: str
    nilai: float

print("\n-- Frozen (Immutable) Demo --")
nilai = NilaiFrozen("2301001", "IF201", 85)
print(f"Frozen: {nilai}")

try:
    nilai.nilai = 90
    print("ERROR - should not reach")
except Exception as e:
    print(f"[OK] Cannot modify: {type(e).__name__}")

@dataclass(order=True)
class NilaiOrdered:
    """Dataclass with order support."""
    nilai: float
    nim: str

print("\n-- Ordered (Comparison) Demo --")
n1 = NilaiOrdered(85, "2301001")
n2 = NilaiOrdered(90, "2301002")
print(f"n1 < n2: {n1 < n2}")

# ======================================================================
# BAGIAN 3: Validation dengan __post_init__
#           Fokus: Validate values setelah init
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Validation dengan __post_init__")
print("=" * 60)

@dataclass
class MahasiswaValidated:
    """Mahasiswa dengan validation di __post_init__."""
    nim: str
    nama: str
    angkatan: int
    
    def __post_init__(self):
        """Validate values setelah __init__."""
        if len(self.nim) < 6:
            raise ValueError("NIM minimal 6 karakter")
        if self.angkatan < 2000 or self.angkatan > 2030:
            raise ValueError("Angkatan invalid")

print("\n-- Valid Data --")
try:
    mhs_valid = MahasiswaValidated("2301001", "Budi Santoso", 2023)
    print(f"[OK] Valid: {mhs_valid}")
except ValueError as e:
    print(f"ERROR: {e}")

print("\n-- Invalid Data --")
try:
    mhs_invalid = MahasiswaValidated("230", "Budi", 2023)
    print(f"Should not reach")
except ValueError as e:
    print(f"[OK] Caught: {e}")

print("\n" + "=" * 60)
print("Bagian selesai!")
print("=" * 60)
