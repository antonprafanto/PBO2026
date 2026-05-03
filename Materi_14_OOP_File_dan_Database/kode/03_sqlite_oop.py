"""
Kode Praktik - Materi 14: OOP + File & Database
File: 03_sqlite_oop.py
Topik: SQLite CRUD dengan Repository Pattern

Jalankan: python 03_sqlite_oop.py
"""

import gc
import sqlite3
import os
from dataclasses import dataclass, field
from typing import List, Optional

DB_FILE = "test_akademik.db"

# ======================================================================
# BAGIAN 1: SQLite Basics
#           Fokus: connect, create table, insert, select
# ======================================================================
print("=" * 60)
print("BAGIAN 1: SQLite Basics")
print("=" * 60)

print("\n-- Connect dan Buat Tabel --")

# sqlite3.connect() membuat file .db jika belum ada
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        nim     TEXT PRIMARY KEY,
        nama    TEXT NOT NULL,
        angkatan INTEGER NOT NULL
    )
""")
conn.commit()
print(f"[OK] Database: {DB_FILE}")
print("[OK] Tabel mahasiswa siap")

print("\n-- Insert Data --")

# Parameterized query -- AMAN dari SQL injection
data_mhs = [
    ("2301001", "Budi Santoso", 2023),
    ("2301002", "Sari Dewi", 2023),
    ("2301003", "Ahmad Fauzi", 2023),
]

cursor.executemany("INSERT OR IGNORE INTO mahasiswa VALUES (?, ?, ?)", data_mhs)
conn.commit()
print(f"[OK] Inserted {cursor.rowcount} baris (OR IGNORE jika sudah ada)")

print("\n-- Select Data --")

cursor.execute("SELECT * FROM mahasiswa ORDER BY nim")
rows = cursor.fetchall()
print(f"Total: {len(rows)} mahasiswa")
for row in rows:
    print(f"  {row[0]} | {row[1]} | Angkatan {row[2]}")

conn.close()

# ======================================================================
# BAGIAN 2: Repository Pattern
#           Fokus: Abstraksi CRUD dalam class
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Repository Pattern (ORM-like)")
print("=" * 60)

@dataclass
class Mahasiswa:
    """Model Mahasiswa."""
    nim: str
    nama: str
    angkatan: int

@dataclass
class Nilai:
    """Model Nilai mahasiswa."""
    nim: str
    kode_mk: str
    nilai: float

class MahasiswaRepository:
    """Repository untuk CRUD tabel mahasiswa."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()
    
    def _get_conn(self) -> sqlite3.Connection:
        """Buat koneksi baru ke database."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row  # Row as dict-like
        return conn
    
    def _create_table(self) -> None:
        """Inisialisasi tabel jika belum ada."""
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim      TEXT PRIMARY KEY,
                    nama     TEXT NOT NULL,
                    angkatan INTEGER NOT NULL
                )
            """)
    
    def insert(self, mhs: Mahasiswa) -> bool:
        """Tambah mahasiswa baru. Return False jika NIM sudah ada."""
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
        """Cari mahasiswa berdasarkan NIM."""
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM mahasiswa WHERE nim = ?", (nim,)
            ).fetchone()
        if row:
            return Mahasiswa(row["nim"], row["nama"], row["angkatan"])
        return None
    
    def find_all(self) -> List[Mahasiswa]:
        """Ambil semua mahasiswa."""
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM mahasiswa ORDER BY nim"
            ).fetchall()
        return [Mahasiswa(r["nim"], r["nama"], r["angkatan"]) for r in rows]
    
    def update_nama(self, nim: str, nama_baru: str) -> bool:
        """Update nama mahasiswa."""
        with self._get_conn() as conn:
            cursor = conn.execute(
                "UPDATE mahasiswa SET nama = ? WHERE nim = ?",
                (nama_baru, nim)
            )
        return cursor.rowcount > 0
    
    def delete(self, nim: str) -> bool:
        """Hapus mahasiswa berdasarkan NIM."""
        with self._get_conn() as conn:
            cursor = conn.execute(
                "DELETE FROM mahasiswa WHERE nim = ?", (nim,)
            )
        return cursor.rowcount > 0
    
    def count(self) -> int:
        """Hitung total mahasiswa."""
        with self._get_conn() as conn:
            result = conn.execute(
                "SELECT COUNT(*) FROM mahasiswa"
            ).fetchone()
        return result[0]

DB2 = "test_repo.db"

print("\n-- Demo CRUD Repository --")
repo = MahasiswaRepository(DB2)

# CREATE
print("\n[CREATE]")
mhs_list = [
    Mahasiswa("2301001", "Budi Santoso", 2023),
    Mahasiswa("2301002", "Sari Dewi", 2023),
    Mahasiswa("2301003", "Ahmad Fauzi", 2023),
]
for m in mhs_list:
    ok = repo.insert(m)
    print(f"  Insert {m.nim}: {'[OK]' if ok else '[SKIP] sudah ada'}")

# READ
print("\n[READ]")
all_mhs = repo.find_all()
print(f"  Total: {repo.count()} mahasiswa")
for m in all_mhs:
    print(f"  - {m.nim}: {m.nama}")

# UPDATE
print("\n[UPDATE]")
ok = repo.update_nama("2301001", "Budi Santoso Wijaya")
print(f"  Update NIM 2301001: {'[OK]' if ok else '[FAIL]'}")
updated = repo.find_by_nim("2301001")
print(f"  Nama baru: {updated.nama}")

# DELETE
print("\n[DELETE]")
ok = repo.delete("2301003")
print(f"  Delete NIM 2301003: {'[OK]' if ok else '[FAIL]'}")
print(f"  Total sekarang: {repo.count()}")

# ======================================================================
# BAGIAN 3: Relasi Antar Tabel
#           Fokus: Tabel mahasiswa + nilai dengan JOIN
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Relasi Antar Tabel (JOIN)")
print("=" * 60)

class NilaiRepository:
    """Repository untuk tabel nilai."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._create_table()
    
    def _get_conn(self):
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn
    
    def _create_table(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS nilai (
                    id      INTEGER PRIMARY KEY AUTOINCREMENT,
                    nim     TEXT NOT NULL,
                    kode_mk TEXT NOT NULL,
                    nilai   REAL NOT NULL,
                    UNIQUE(nim, kode_mk)
                )
            """)
    
    def insert(self, n: Nilai) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO nilai (nim, kode_mk, nilai) VALUES (?, ?, ?)",
                    (n.nim, n.kode_mk, n.nilai)
                )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def get_rata_rata(self, nim: str) -> float:
        """Hitung rata-rata nilai untuk satu mahasiswa."""
        with self._get_conn() as conn:
            result = conn.execute(
                "SELECT AVG(nilai) FROM nilai WHERE nim = ?", (nim,)
            ).fetchone()
        return result[0] or 0.0
    
    def get_laporan(self, nim: str) -> List[dict]:
        """Ambil semua nilai dengan JOIN ke tabel mahasiswa."""
        with self._get_conn() as conn:
            rows = conn.execute("""
                SELECT m.nama, n.kode_mk, n.nilai
                FROM nilai n
                JOIN mahasiswa m ON n.nim = m.nim
                WHERE n.nim = ?
                ORDER BY n.kode_mk
            """, (nim,)).fetchall()
        return [{"nama": r["nama"], "kode_mk": r["kode_mk"], "nilai": r["nilai"]} for r in rows]

print("\n-- Demo Relasi Tabel dengan JOIN --")

nilai_repo = NilaiRepository(DB2)

# Input nilai
nilai_data = [
    Nilai("2301001", "IF201", 85.0),
    Nilai("2301001", "IF202", 90.0),
    Nilai("2301002", "IF201", 78.0),
    Nilai("2301002", "IF202", 82.0),
]
for n in nilai_data:
    nilai_repo.insert(n)

# Laporan dengan JOIN
print("\nLaporan Mahasiswa 2301001:")
laporan = nilai_repo.get_laporan("2301001")
for row in laporan:
    print(f"  {row['nama']} | {row['kode_mk']} | {row['nilai']}")
print(f"  Rata-rata: {nilai_repo.get_rata_rata('2301001'):.2f}")

# Cleanup -- hapus repo agar koneksi SQLite ditutup, lalu delete file
del repo, nilai_repo
gc.collect()
for f in [DB_FILE, DB2]:
    if os.path.exists(f):
        os.remove(f)
        print(f"\n[OK] Cleanup: {f}")

print("\n" + "=" * 60)
print("Bagian selesai!")
print("=" * 60)
