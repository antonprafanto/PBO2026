"""
Kode Praktik - Materi 13: OOP Modern Python
File: 03_slots_optimization.py
Topik: __slots__ dan memory optimization

Jalankan: python 03_slots_optimization.py
"""

import sys
from dataclasses import dataclass

# ======================================================================
# BAGIAN 1: __slots__ Basics
#           Fokus: Memory saving dengan __slots__
# ======================================================================
print("=" * 60)
print("BAGIAN 1: __slots__ Basics dan Memory Comparison")
print("=" * 60)

class TanpaSlots:
    """Class tanpa __slots__ - punya __dict__."""
    def __init__(self, nim, nama, angkatan):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan

class DenganSlots:
    """Class dengan __slots__ - restricted."""
    __slots__ = ('nim', 'nama', 'angkatan')
    
    def __init__(self, nim, nama, angkatan):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan

print("\n-- Memory Comparison --")

obj1 = TanpaSlots("2301001", "Budi Santoso", 2023)
obj2 = DenganSlots("2301001", "Budi Santoso", 2023)

size_without = sys.getsizeof(obj1) + sys.getsizeof(obj1.__dict__)
size_with = sys.getsizeof(obj2)

print(f"Tanpa __slots__: {size_without} bytes")
print(f"Dengan __slots__: {size_with} bytes")
print(f"Memory saving: {(size_without - size_with) / size_without * 100:.1f}%")

# ======================================================================
# BAGIAN 2: __slots__ dengan @dataclass
#           Fokus: Combine features
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: __slots__ dengan @dataclass")
print("=" * 60)

@dataclass
class MahasiswaNoSlots:
    """@dataclass tanpa __slots__."""
    nim: str
    nama: str
    angkatan: int

@dataclass
class MahasiswaWithSlots:
    """@dataclass dengan __slots__."""
    __slots__ = ('nim', 'nama', 'angkatan')
    nim: str
    nama: str
    angkatan: int

print("\n-- Size Comparison --")

mhs1 = MahasiswaNoSlots("2301001", "Budi Santoso", 2023)
mhs2 = MahasiswaWithSlots("2301001", "Budi Santoso", 2023)

# Perbandingan BENAR: harus tambahkan __dict__ untuk non-slots
size_no_slots = sys.getsizeof(mhs1) + sys.getsizeof(mhs1.__dict__)
size_with_slots = sys.getsizeof(mhs2)  # tidak punya __dict__

print(f"@dataclass tanpa slots: {size_no_slots} bytes (obj + __dict__)")
print(f"@dataclass dengan slots: {size_with_slots} bytes (tanpa __dict__)")
print(f"Memory saving: {(size_no_slots - size_with_slots) / size_no_slots * 100:.1f}%")
print()
print("Catatan: Tanpa __slots__, setiap object punya __dict__ yang menyimpan attributes.")
print("Dengan __slots__, tidak ada __dict__, attributes disimpan langsung di slot.")

# ======================================================================
# BAGIAN 3: __slots__ Restrictions
#           Fokus: Trade-offs
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: __slots__ Restrictions")
print("=" * 60)

@dataclass
class DenganSlotsRestricted:
    __slots__ = ('nim', 'nama')
    nim: str
    nama: str

mhs = DenganSlotsRestricted("2301001", "Budi Santoso")

print("\n-- Can't add dynamic attributes --")
try:
    mhs.angkatan = 2023
    print("ERROR: should not reach")
except AttributeError as e:
    print(f"[OK] Blocked: {type(e).__name__}")

print("\n-- But declared slots work fine --")
mhs.nim = "2301002"
print(f"[OK] Modified NIM: {mhs.nim}")

print("\n-- Best Practices --")
print("""
USE __slots__ KETIKA:
  1. Class memiliki banyak instances (>1000)
  2. Memory adalah concern
  3. Attributes tetap (fixed schema)
  4. Performance kritis

DON'T USE KETIKA:
  1. Class memiliki sedikit instances
  2. Perlu dynamic attributes
  3. Inheritance complex
  4. Early development stage
""")

print("=" * 60)
print("Bagian selesai!")
print("=" * 60)
