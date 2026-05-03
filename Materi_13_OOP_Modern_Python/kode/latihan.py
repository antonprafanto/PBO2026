"""
Latihan Materi 13 -- OOP Modern Python

File: latihan.py
Instruksi: Kerjakan semua SOAL dengan baik!

Jalankan: python latihan.py
"""

from dataclasses import dataclass
from typing import List, Dict, Optional

print("=" * 60)
print("LATIHAN MATERI 13: OOP Modern Python")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah): @dataclass untuk Class Nilai
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 1 (*Mudah): @dataclass untuk Class Nilai")
print("=" * 60)

# TODO: Implementasi class Nilai dengan @dataclass
# Requirements:
#   - Atribut: nim (str), kode_mk (str), nilai (float)
#   - Type hints lengkap
#   - Validation di __post_init__: nilai harus 0-100
#   - Method: is_lulus() -> bool (nilai >= 60)
#
# Contoh penggunaan:
#   nilai = Nilai("2301001", "IF201", 85)
#   print(nilai.is_lulus())  # True
#   print(nilai)  # Mahasiswa(...) dari __repr__

pass  # TODO: Implementasi Nilai class

# SOAL 1 TEST
print("\n-- SOAL 1: Test Nilai Class --")
print("[X] Soal 1 belum dikerjakan (stub)")
print("    TODO: Buat @dataclass Nilai dengan validation dan method")

# ======================================================================
# SOAL 2 (**Sedang): Type Hints untuk Sistem KRS
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 2 (**Sedang): Type Hints untuk Sistem KRS")
print("=" * 60)

# TODO: Implementasi class KRS dengan comprehensive type hints
# Requirements:
#   - @dataclass
#   - Atribut: nim (str), semester (int), matakuliah_list (List[str]),
#              sks_list (List[int]) -- simpan SKS tiap MK
#   - Type hints untuk SEMUA parameters, attributes, return values
#   - Methods:
#       - add_matakuliah(kode_mk: str, sks: int) -> bool
#       - get_total_sks() -> int  (sum dari sks_list)
#       - is_valid() -> bool (get_total_sks() <= 24)
#   - __post_init__ validation: semester harus 1-8
#
# CATATAN: Tidak gunakan __slots__ di sini karena field List tidak compatible
#          (lihat 03_slots_optimization.py untuk penjelasan limitasi __slots__)
#
# Contoh:
#   krs = KRS("2301001", 3)
#   krs.add_matakuliah("IF201", 3)
#   print(krs.is_valid())  # True
#   print(krs.get_total_sks())  # 3

pass  # TODO: Implementasi KRS class

# SOAL 2 TEST
print("\n-- SOAL 2: Test KRS Class --")
print("[X] Soal 2 belum dikerjakan (stub)")
print("    TODO: @dataclass + __slots__ + comprehensive type hints")

# ======================================================================
# SOAL 3 (***Sulit): Sistem Akademik Lengkap
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 3 (***Sulit): Sistem Akademik Lengkap")
print("=" * 60)

# TODO: Implementasi sistem akademik dengan semua modern features
# Requirements:
#   - @dataclass untuk Mahasiswa, MataKuliah, KRS
#   - __slots__ di semua classes untuk memory optimization
#   - Comprehensive type hints di semua methods
#   - Validation di __post_init__
#   - Class SistemAkademik untuk manage entities:
#       - register_mahasiswa(nim, nama, angkatan) -> Optional[Mahasiswa]
#       - create_matakuliah(kode, nama, sks) -> Optional[MataKuliah]
#       - input_nilai(nim, kode_mk, nilai) -> bool
#       - get_laporan(nim) -> Optional[Dict]
#
# Penggunaan:
#   sistem = SistemAkademik()
#   mhs = sistem.register_mahasiswa("2301001", "Budi", 2023)
#   mk = sistem.create_matakuliah("IF201", "Database", 3)
#   sistem.input_nilai("2301001", "IF201", 85)
#   laporan = sistem.get_laporan("2301001")

pass  # TODO: Implementasi sistem akademik lengkap

# SOAL 3 TEST
print("\n-- SOAL 3: Test Sistem Akademik --")
print("[X] Soal 3 belum dikerjakan (stub)")
print("    TODO: Full sistem dengan @dataclass + __slots__ + type hints")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n" + "=" * 60)
print("SUMMARY LATIHAN")
print("=" * 60)

print("""
SOAL 1 (MUDAH): @dataclass untuk Class Nilai
  Status: [X] Belum dikerjakan
  TODO:
    1. Buat @dataclass Nilai dengan 3 attributes
    2. Tambahkan type hints lengkap
    3. Validation di __post_init__: nilai 0-100
    4. Implementasi is_lulus() method
    5. Test dengan Nilai("2301001", "IF201", 85)
  Reference: Lihat 01_dataclass_basics.py
  Effort: ~10-15 menit

SOAL 2 (SEDANG): Type Hints untuk Sistem KRS
  Status: [X] Belum dikerjakan
  TODO:
    1. Buat @dataclass KRS (tanpa __slots__ karena conflict field List)
    2. Type hints untuk SEMUA attributes dan methods
    3. Implementasi 3 methods: add_matakuliah, get_total_sks, is_valid
    4. Validation di __post_init__: semester 1-8
    5. Test add dan validate total SKS <= 24
  Reference: Lihat 02_type_hints_advanced.py, 03_slots_optimization.py BAGIAN 3
  Effort: ~20-25 menit

SOAL 3 (SULIT): Sistem Akademik Lengkap
  Status: [X] Belum dikerjakan
  TODO:
    1. @dataclass untuk Mahasiswa, MataKuliah, KRS
    2. __slots__ di semua classes
    3. Comprehensive type hints di semua methods
    4. Class SistemAkademik untuk manage
    5. Implement 4 core methods
    6. Full validation dan error handling
  Reference: Lihat 04_studi_kasus.py untuk architecture
  Effort: ~40-50 menit

TIPS:
  1. Mulai dengan @dataclass - itu otomatis generate __init__, __repr__
  2. Tambahkan __slots__ untuk memory efficiency
  3. Type hints SEMUA parameters dan return values
  4. Validation di __post_init__ untuk data integrity
  5. Use Optional untuk nullable values
  6. Use Union jika multiple types

VALIDATION:
  - Cek: Semua class punya @dataclass
  - Cek: Semua punya type hints
  - Cek: __post_init__ validate input
  - Cek: Methods return correct types
  - Cek: __slots__ deklarasi di semua classes
  - Cek: Code runs tanpa errors
""")

print("\n" + "=" * 60)
print("Latihan selesai!")
print("=" * 60)
