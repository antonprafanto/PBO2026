"""
Kode Praktik - Materi 14: OOP + File & Database
File: 04_studi_kasus.py
Topik: Sistem Akademik dengan File Persistence (JSON + SQLite)

Jalankan: python 04_studi_kasus.py
"""

import gc
import json
import sqlite3
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional, Dict

DB_FILE = "studi_akademik.db"
JSON_BACKUP = "studi_akademik_backup.json"

# ======================================================================
# MODELS
# ======================================================================

@dataclass
class MataKuliah:
    """Model matakuliah."""
    kode: str
    nama: str
    sks: int
    
    def __post_init__(self):
        if not (1 <= self.sks <= 6):
            raise ValueError("SKS harus 1-6")

@dataclass
class Mahasiswa:
    """Model mahasiswa."""
    nim: str
    nama: str
    angkatan: int
    
    def __post_init__(self):
        if len(self.nim) < 6:
            raise ValueError("NIM minimal 6 karakter")

@dataclass
class Nilai:
    """Model nilai."""
    nim: str
    kode_mk: str
    nilai: float
    
    def __post_init__(self):
        if not (0 <= self.nilai <= 100):
            raise ValueError("Nilai harus 0-100")
    
    def get_grade(self) -> str:
        if self.nilai >= 80:
            return "A"
        elif self.nilai >= 70:
            return "B"
        elif self.nilai >= 60:
            return "C"
        else:
            return "D"

# ======================================================================
# REPOSITORIES
# ======================================================================

class BaseRepository:
    """Base class untuk semua repositories."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
    
    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

class MataKuliahRepository(BaseRepository):
    """Repository untuk matakuliah."""
    
    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()
    
    def _create_table(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS matakuliah (
                    kode TEXT PRIMARY KEY,
                    nama TEXT NOT NULL,
                    sks  INTEGER NOT NULL
                )
            """)
    
    def insert(self, mk: MataKuliah) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO matakuliah VALUES (?, ?, ?)",
                    (mk.kode, mk.nama, mk.sks)
                )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def find_all(self) -> List[MataKuliah]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM matakuliah ORDER BY kode").fetchall()
        return [MataKuliah(r["kode"], r["nama"], r["sks"]) for r in rows]

class MahasiswaRepository(BaseRepository):
    """Repository untuk mahasiswa."""
    
    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()
    
    def _create_table(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim      TEXT PRIMARY KEY,
                    nama     TEXT NOT NULL,
                    angkatan INTEGER NOT NULL
                )
            """)
    
    def insert(self, mhs: Mahasiswa) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO mahasiswa VALUES (?, ?, ?)",
                    (mhs.nim, mhs.nama, mhs.angkatan)
                )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def find_by_nim(self, nim: str) -> Optional[Mahasiswa]:
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM mahasiswa WHERE nim = ?", (nim,)
            ).fetchone()
        if row:
            return Mahasiswa(row["nim"], row["nama"], row["angkatan"])
        return None
    
    def find_all(self) -> List[Mahasiswa]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM mahasiswa ORDER BY nim").fetchall()
        return [Mahasiswa(r["nim"], r["nama"], r["angkatan"]) for r in rows]

class NilaiRepository(BaseRepository):
    """Repository untuk nilai."""
    
    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()
    
    def _create_table(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS nilai (
                    nim     TEXT NOT NULL,
                    kode_mk TEXT NOT NULL,
                    nilai   REAL NOT NULL,
                    PRIMARY KEY (nim, kode_mk)
                )
            """)
    
    def insert(self, n: Nilai) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO nilai VALUES (?, ?, ?)",
                    (n.nim, n.kode_mk, n.nilai)
                )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_by_nim(self, nim: str) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM nilai WHERE nim = ? ORDER BY kode_mk", (nim,)
            ).fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nilai"]) for r in rows]
    
    def get_rata_rata(self, nim: str) -> float:
        with self._get_conn() as conn:
            result = conn.execute(
                "SELECT AVG(nilai) FROM nilai WHERE nim = ?", (nim,)
            ).fetchone()
        return result[0] or 0.0

# ======================================================================
# SERVICE LAYER
# ======================================================================

class SistemAkademikService:
    """Service layer yang menggunakan repositories."""
    
    def __init__(self, db_path: str):
        self.mk_repo = MataKuliahRepository(db_path)
        self.mhs_repo = MahasiswaRepository(db_path)
        self.nilai_repo = NilaiRepository(db_path)
    
    def daftarkan_mahasiswa(self, nim: str, nama: str, angkatan: int) -> Optional[Mahasiswa]:
        """Daftarkan mahasiswa baru."""
        mhs = Mahasiswa(nim, nama, angkatan)
        if self.mhs_repo.insert(mhs):
            return mhs
        return None
    
    def tambah_matakuliah(self, kode: str, nama: str, sks: int) -> Optional[MataKuliah]:
        """Tambah matakuliah baru."""
        mk = MataKuliah(kode, nama, sks)
        if self.mk_repo.insert(mk):
            return mk
        return None
    
    def input_nilai(self, nim: str, kode_mk: str, nilai: float) -> bool:
        """Input nilai mahasiswa."""
        if not self.mhs_repo.find_by_nim(nim):
            return False
        n = Nilai(nim, kode_mk, nilai)
        return self.nilai_repo.insert(n)
    
    def get_laporan(self, nim: str) -> Optional[Dict]:
        """Generate laporan lengkap satu mahasiswa."""
        mhs = self.mhs_repo.find_by_nim(nim)
        if not mhs:
            return None
        
        nilai_list = self.nilai_repo.get_by_nim(nim)
        rata_rata = self.nilai_repo.get_rata_rata(nim)
        
        if rata_rata >= 80:
            grade = "A"
        elif rata_rata >= 70:
            grade = "B"
        elif rata_rata >= 60:
            grade = "C"
        else:
            grade = "D"
        
        return {
            "nim": mhs.nim,
            "nama": mhs.nama,
            "angkatan": mhs.angkatan,
            "nilai": [{"kode_mk": n.kode_mk, "nilai": n.nilai, "grade": n.get_grade()} for n in nilai_list],
            "rata_rata": round(rata_rata, 2),
            "grade_akhir": grade,
        }
    
    def export_json(self, filepath: str) -> None:
        """Export semua data ke JSON backup."""
        data = {
            "mahasiswa": [asdict(m) for m in self.mhs_repo.find_all()],
            "matakuliah": [asdict(mk) for mk in self.mk_repo.find_all()],
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Export ke {filepath} berhasil")

# ======================================================================
# DEMO
# ======================================================================
print("=" * 60)
print("STUDI KASUS: Sistem Akademik dengan File Persistence")
print("=" * 60)

service = SistemAkademikService(DB_FILE)

print("\n-- Setup Data --")

mhs_data = [
    ("2301001", "Budi Santoso", 2023),
    ("2301002", "Sari Dewi", 2023),
    ("2301003", "Ahmad Fauzi", 2023),
]
for nim, nama, angkatan in mhs_data:
    m = service.daftarkan_mahasiswa(nim, nama, angkatan)
    if m:
        print(f"  [OK] Daftar: {m.nama} ({m.nim})")

mk_data = [
    ("IF201", "Pemrograman Web", 3),
    ("IF202", "Basis Data", 3),
    ("IF203", "Jaringan Komputer", 2),
]
for kode, nama, sks in mk_data:
    mk = service.tambah_matakuliah(kode, nama, sks)
    if mk:
        print(f"  [OK] MK: {mk.nama} ({mk.sks} SKS)")

print("\n-- Input Nilai --")

nilai_data = [
    ("2301001", "IF201", 88.0),
    ("2301001", "IF202", 92.0),
    ("2301001", "IF203", 75.0),
    ("2301002", "IF201", 70.0),
    ("2301002", "IF202", 65.0),
    ("2301003", "IF201", 55.0),
    ("2301003", "IF202", 60.0),
]
for nim, kode_mk, nilai in nilai_data:
    ok = service.input_nilai(nim, kode_mk, nilai)
    if ok:
        print(f"  [OK] {nim} | {kode_mk}: {nilai}")

print("\n-- Laporan Mahasiswa --")

for nim, _, _ in mhs_data:
    laporan = service.get_laporan(nim)
    if laporan:
        print(f"\n{laporan['nama']} ({laporan['nim']})")
        for n in laporan["nilai"]:
            print(f"  {n['kode_mk']}: {n['nilai']} ({n['grade']})")
        print(f"  Rata-rata: {laporan['rata_rata']} | Grade Akhir: {laporan['grade_akhir']}")

print("\n-- Export JSON Backup --")
service.export_json(JSON_BACKUP)

# Verifikasi backup
with open(JSON_BACKUP, "r", encoding="utf-8") as f:
    backup = json.load(f)
print(f"  Backup berisi {len(backup['mahasiswa'])} mahasiswa, {len(backup['matakuliah'])} matakuliah")

# Cleanup -- hapus service agar koneksi SQLite ditutup, lalu delete file
del service
gc.collect()
for f in [DB_FILE, JSON_BACKUP]:
    if os.path.exists(f):
        os.remove(f)
        print(f"[OK] Cleanup: {f}")

print("\n" + "=" * 60)
print("Studi kasus selesai!")
print("=" * 60)
