"""
Kode Praktik - Materi 14: OOP + File & Database
File: 01_json_oop.py
Topik: JSON serialisasi dengan @dataclass

Jalankan: python 01_json_oop.py
"""

import json
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional

# ======================================================================
# BAGIAN 1: JSON Basics dengan @dataclass
#           Fokus: asdict(), json.dumps(), json.loads()
# ======================================================================
print("=" * 60)
print("BAGIAN 1: JSON Basics dengan @dataclass")
print("=" * 60)

@dataclass
class MataKuliah:
    """Representasi matakuliah."""
    kode: str
    nama: str
    sks: int

@dataclass
class Mahasiswa:
    """Representasi mahasiswa dengan nilai."""
    nim: str
    nama: str
    angkatan: int
    nilai_dict: dict = field(default_factory=dict)
    matakuliah: List[str] = field(default_factory=list)

print("\n-- asdict(): @dataclass ke dict --")
mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
mhs.nilai_dict = {"IF201": 85.0, "IF202": 90.0}
mhs.matakuliah = ["IF201", "IF202"]

data_dict = asdict(mhs)
print(f"Type: {type(data_dict)}")
print(f"Dict: {data_dict}")

print("\n-- dict ke JSON string --")
json_str = json.dumps(data_dict, indent=2)
print(json_str)

print("\n-- JSON string ke dict ke @dataclass --")
data_kembali = json.loads(json_str)
mhs_baru = Mahasiswa(**data_kembali)
print(f"Mahasiswa: {mhs_baru}")
print(f"Nilai: {mhs_baru.nilai_dict}")

# ======================================================================
# BAGIAN 2: Simpan dan Baca File JSON
#           Fokus: json.dump(), json.load(), error handling
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Simpan dan Baca File JSON")
print("=" * 60)

FILEPATH = "test_mahasiswa.json"

class MahasiswaJsonRepo:
    """Repository untuk menyimpan data Mahasiswa ke JSON."""
    
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def save_all(self, mahasiswa_list: List[Mahasiswa]) -> None:
        """Simpan semua mahasiswa ke JSON file."""
        data = [asdict(m) for m in mahasiswa_list]
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Saved {len(data)} mahasiswa ke {self.filepath}")
    
    def load_all(self) -> List[Mahasiswa]:
        """Baca semua mahasiswa dari JSON file."""
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Mahasiswa(**d) for d in data]
        except FileNotFoundError:
            print(f"[INFO] File {self.filepath} belum ada, return list kosong")
            return []
        except json.JSONDecodeError:
            print(f"[ERROR] File {self.filepath} corrupt")
            return []
    
    def save_one(self, mahasiswa: Mahasiswa) -> None:
        """Tambah satu mahasiswa ke JSON file."""
        existing = self.load_all()
        existing.append(mahasiswa)
        self.save_all(existing)

print("\n-- Demo Repository JSON --")

repo = MahasiswaJsonRepo(FILEPATH)

# Buat data
mhs_list = [
    Mahasiswa("2301001", "Budi Santoso", 2023, {"IF201": 85.0}),
    Mahasiswa("2301002", "Sari Dewi", 2023, {"IF201": 90.0, "IF202": 78.0}),
    Mahasiswa("2301003", "Ahmad Fauzi", 2023, {}),
]

# Simpan
repo.save_all(mhs_list)

# Baca kembali
loaded = repo.load_all()
print(f"\n[OK] Loaded {len(loaded)} mahasiswa:")
for m in loaded:
    print(f"  - {m.nim}: {m.nama} | nilai: {m.nilai_dict}")

# ======================================================================
# BAGIAN 3: JSON dengan Nested Objects
#           Fokus: Nested @dataclass serialisasi
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: JSON dengan Nested Objects")
print("=" * 60)

@dataclass
class Transaksi:
    """Transaksi pembayaran."""
    id: str
    nim: str
    jumlah: float
    keterangan: str

@dataclass
class DataAkademik:
    """Gabungan mahasiswa dan transaksi."""
    mahasiswa: Mahasiswa
    transaksi: List[Transaksi] = field(default_factory=list)

print("\n-- Nested @dataclass ke JSON --")

da = DataAkademik(
    mahasiswa=Mahasiswa("2301001", "Budi Santoso", 2023, {"IF201": 85.0}),
    transaksi=[
        Transaksi("TXN001", "2301001", 5000000.0, "Pembayaran SPP"),
        Transaksi("TXN002", "2301001", 200000.0, "Biaya praktikum"),
    ]
)

# asdict() bekerja rekursif untuk nested dataclass
data_nested = asdict(da)
json_nested = json.dumps(data_nested, indent=2, ensure_ascii=False)
print(json_nested)

# Cleanup file test
if os.path.exists(FILEPATH):
    os.remove(FILEPATH)
    print(f"\n[OK] Cleanup: {FILEPATH} dihapus")

print("\n" + "=" * 60)
print("Bagian selesai!")
print("=" * 60)
