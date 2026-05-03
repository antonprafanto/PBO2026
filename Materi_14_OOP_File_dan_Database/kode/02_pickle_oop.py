"""
Kode Praktik - Materi 14: OOP + File & Database
File: 02_pickle_oop.py
Topik: Pickle serialisasi Python objects

Jalankan: python 02_pickle_oop.py
"""

import pickle
import os
from dataclasses import dataclass, field
from typing import List, Dict

# ======================================================================
# BAGIAN 1: Pickle Basics
#           Fokus: pickle.dump(), pickle.load(), simpan objects
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Pickle Basics")
print("=" * 60)

@dataclass
class Mahasiswa:
    """Mahasiswa dengan data lengkap."""
    nim: str
    nama: str
    angkatan: int
    nilai_dict: Dict[str, float] = field(default_factory=dict)
    
    def hitung_rata_rata(self) -> float:
        if not self.nilai_dict:
            return 0.0
        return sum(self.nilai_dict.values()) / len(self.nilai_dict)

PICKLE_FILE = "test_mahasiswa.pkl"

print("\n-- Simpan object ke file Pickle --")

mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
mhs.nilai_dict = {"IF201": 85.0, "IF202": 92.0, "IF203": 78.0}

with open(PICKLE_FILE, "wb") as f:
    pickle.dump(mhs, f)

print(f"[OK] Saved: {mhs}")

print("\n-- Baca kembali dari file Pickle --")

with open(PICKLE_FILE, "rb") as f:
    mhs_loaded = pickle.load(f)

print(f"[OK] Loaded: {mhs_loaded}")
print(f"Type: {type(mhs_loaded)}")
print(f"Rata-rata: {mhs_loaded.hitung_rata_rata():.2f}")
print(f"Methods masih bisa dipanggil: [OK]")

# ======================================================================
# BAGIAN 2: Pickle vs JSON
#           Fokus: Kapan pakai mana
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Pickle vs JSON - Kapan Pakai Mana?")
print("=" * 60)

class SistemNilai:
    """Class dengan methods - susah di-JSON, mudah di-Pickle."""
    
    def __init__(self, nama: str):
        self.nama = nama
        self._nilai_list = []
        self._batas_lulus = 60.0
    
    def tambah_nilai(self, nilai: float) -> None:
        self._nilai_list.append(nilai)
    
    def rata_rata(self) -> float:
        if not self._nilai_list:
            return 0.0
        return sum(self._nilai_list) / len(self._nilai_list)
    
    def is_lulus(self) -> bool:
        return self.rata_rata() >= self._batas_lulus
    
    def __repr__(self):
        return f"SistemNilai(nama={self.nama}, rata={self.rata_rata():.1f})"

PICKLE_FILE2 = "test_sistem.pkl"

print("\n-- Pickle bisa simpan object dengan methods --")

sistem = SistemNilai("Budi Santoso")
sistem.tambah_nilai(85.0)
sistem.tambah_nilai(90.0)
sistem.tambah_nilai(78.0)
sistem._batas_lulus = 70.0  # Custom batas lulus

print(f"Sebelum: {sistem}")
print(f"  Lulus: {sistem.is_lulus()}")
print(f"  Batas: {sistem._batas_lulus}")

with open(PICKLE_FILE2, "wb") as f:
    pickle.dump(sistem, f)

with open(PICKLE_FILE2, "rb") as f:
    sistem_loaded = pickle.load(f)

print(f"\nSetelah load: {sistem_loaded}")
print(f"  Lulus: {sistem_loaded.is_lulus()}")
print(f"  Batas lulus (custom): {sistem_loaded._batas_lulus}")
print(f"  State terjaga dengan Pickle: [OK]")

# ======================================================================
# BAGIAN 3: Repository Pattern dengan Pickle
#           Fokus: Simpan dan load list of objects
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Repository Pattern dengan Pickle")
print("=" * 60)

PICKLE_REPO_FILE = "test_repo.pkl"

class MahasiswaPickleRepo:
    """Repository Mahasiswa menggunakan Pickle."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def save_all(self, mahasiswa_list: List[Mahasiswa]) -> None:
        """Simpan semua mahasiswa."""
        with open(self.filepath, "wb") as f:
            pickle.dump(mahasiswa_list, f)
        print(f"[OK] Saved {len(mahasiswa_list)} records ke {self.filepath}")
    
    def load_all(self) -> List[Mahasiswa]:
        """Baca semua mahasiswa."""
        try:
            with open(self.filepath, "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
    
    def add(self, mahasiswa: Mahasiswa) -> None:
        """Tambah satu mahasiswa."""
        data = self.load_all()
        data.append(mahasiswa)
        self.save_all(data)
    
    def find_by_nim(self, nim: str) -> Mahasiswa:
        """Cari mahasiswa berdasarkan NIM."""
        for m in self.load_all():
            if m.nim == nim:
                return m
        return None

print("\n-- Demo Pickle Repository --")

repo = MahasiswaPickleRepo(PICKLE_REPO_FILE)

mhs_list = [
    Mahasiswa("2301001", "Budi Santoso", 2023, {"IF201": 85.0}),
    Mahasiswa("2301002", "Sari Dewi", 2023, {"IF201": 90.0}),
]

repo.save_all(mhs_list)

loaded = repo.load_all()
print(f"Loaded {len(loaded)} mahasiswa:")
for m in loaded:
    print(f"  - {m.nim}: {m.nama}")

found = repo.find_by_nim("2301002")
print(f"\nCari NIM 2301002: {found}")

# Cleanup
for f in [PICKLE_FILE, PICKLE_FILE2, PICKLE_REPO_FILE]:
    if os.path.exists(f):
        os.remove(f)
        print(f"[OK] Cleanup: {f}")

print("\n" + "=" * 60)
print("Bagian selesai!")
print("=" * 60)
