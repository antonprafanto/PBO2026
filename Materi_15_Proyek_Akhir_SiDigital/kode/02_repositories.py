"""
Proyek Akhir SiDigital -- Materi 15
File: 02_repositories.py
Topik: Repository Pattern -- SQLite CRUD untuk setiap entitas

Jalankan: python 02_repositories.py
"""

import gc
import sqlite3
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional

DB_PATH = "test_sidigital.db"

# ======================================================================
# MODELS (ringkas -- versi lengkap di 01_models.py)
# ======================================================================

class SiDigitalError(Exception):
    pass

class NilaiTidakValid(SiDigitalError):
    pass

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    angkatan: int
    program_studi: str = "Informatika"

@dataclass
class Dosen:
    nip: str
    nama: str
    gelar: str = ""

    def nama_lengkap(self) -> str:
        return f"{self.gelar} {self.nama}".strip() if self.gelar else self.nama

@dataclass
class MataKuliah:
    kode: str
    nama: str
    sks: int
    semester: int = 1

@dataclass
class Nilai:
    nim: str
    kode_mk: str
    nip_dosen: str
    nilai_angka: float

    def get_grade(self) -> str:
        if self.nilai_angka >= 80: return "A"
        elif self.nilai_angka >= 70: return "B"
        elif self.nilai_angka >= 60: return "C"
        elif self.nilai_angka >= 50: return "D"
        else: return "E"

    def get_bobot(self) -> float:
        return {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}[self.get_grade()]

# ======================================================================
# BAGIAN 1: BaseRepository
#           Fokus: Shared logic untuk semua repo (Inheritance)
# ======================================================================
print("=" * 60)
print("BAGIAN 1: BaseRepository (Inheritance)")
print("=" * 60)

class BaseRepository:
    """Base class -- shared koneksi SQLite (SOLID DIP)."""

    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_conn(self) -> sqlite3.Connection:
        """Buat koneksi baru. Caller bertanggung jawab menutup."""
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

print("  BaseRepository didefinisikan -- [OK]")
print("  Semua repo mewarisi _get_conn() dari BaseRepository")

# ======================================================================
# BAGIAN 2: MahasiswaRepository & DosenRepository
#           Fokus: CRUD mahasiswa dan dosen
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: MahasiswaRepository & DosenRepository")
print("=" * 60)

class MahasiswaRepository(BaseRepository):
    """CRUD untuk tabel mahasiswa."""

    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()

    def _create_table(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim           TEXT PRIMARY KEY,
                    nama          TEXT NOT NULL,
                    angkatan      INTEGER NOT NULL,
                    program_studi TEXT NOT NULL
                )
            """)

    def insert(self, mhs: Mahasiswa) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO mahasiswa VALUES (?, ?, ?, ?)",
                    (mhs.nim, mhs.nama, mhs.angkatan, mhs.program_studi)
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
            return Mahasiswa(row["nim"], row["nama"], row["angkatan"], row["program_studi"])
        return None

    def find_all(self) -> List[Mahasiswa]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM mahasiswa ORDER BY nim").fetchall()
        return [Mahasiswa(r["nim"], r["nama"], r["angkatan"], r["program_studi"]) for r in rows]

    def update(self, mhs: Mahasiswa) -> bool:
        with self._get_conn() as conn:
            cur = conn.execute(
                "UPDATE mahasiswa SET nama=?, angkatan=?, program_studi=? WHERE nim=?",
                (mhs.nama, mhs.angkatan, mhs.program_studi, mhs.nim)
            )
        return cur.rowcount > 0

    def delete(self, nim: str) -> bool:
        with self._get_conn() as conn:
            cur = conn.execute("DELETE FROM mahasiswa WHERE nim = ?", (nim,))
        return cur.rowcount > 0


class DosenRepository(BaseRepository):
    """CRUD untuk tabel dosen."""

    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()

    def _create_table(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS dosen (
                    nip   TEXT PRIMARY KEY,
                    nama  TEXT NOT NULL,
                    gelar TEXT
                )
            """)

    def insert(self, dosen: Dosen) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO dosen VALUES (?, ?, ?)",
                    (dosen.nip, dosen.nama, dosen.gelar)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_nip(self, nip: str) -> Optional[Dosen]:
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM dosen WHERE nip = ?", (nip,)
            ).fetchone()
        if row:
            return Dosen(row["nip"], row["nama"], row["gelar"] or "")
        return None

    def find_all(self) -> List[Dosen]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM dosen ORDER BY nip").fetchall()
        return [Dosen(r["nip"], r["nama"], r["gelar"] or "") for r in rows]

print("\n-- Demo MahasiswaRepository --")
mhs_repo = MahasiswaRepository(DB_PATH)

data_mhs = [
    Mahasiswa("2301001", "Budi Santoso", 2023),
    Mahasiswa("2301002", "Sari Dewi", 2023),
    Mahasiswa("2301003", "Ahmad Fauzi", 2023, "Sistem Informasi"),
]
for m in data_mhs:
    ok = mhs_repo.insert(m)
    print(f"  Insert {m.nim}: {'[OK]' if ok else '[SKIP]'}")

print(f"  Total mahasiswa: {len(mhs_repo.find_all())}")
found = mhs_repo.find_by_nim("2301001")
print(f"  Cari NIM 2301001: {found.nama}")

print("\n-- Demo DosenRepository --")
dosen_repo = DosenRepository(DB_PATH)

data_dosen = [
    Dosen("198501001", "Ahmad Wahyudi", "Dr."),
    Dosen("198602002", "Siti Rahayu", "M.Kom."),
]
for d in data_dosen:
    ok = dosen_repo.insert(d)
    print(f"  Insert {d.nip}: {'[OK]' if ok else '[SKIP]'} -- {d.nama_lengkap()}")

# ======================================================================
# BAGIAN 3: MataKuliahRepository & NilaiRepository
#           Fokus: CRUD MK dan relasi Nilai (multi-FK)
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: MataKuliahRepository & NilaiRepository")
print("=" * 60)

class MataKuliahRepository(BaseRepository):
    """CRUD untuk tabel matakuliah."""

    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()

    def _create_table(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS matakuliah (
                    kode     TEXT PRIMARY KEY,
                    nama     TEXT NOT NULL,
                    sks      INTEGER NOT NULL,
                    semester INTEGER NOT NULL
                )
            """)

    def insert(self, mk: MataKuliah) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO matakuliah VALUES (?, ?, ?, ?)",
                    (mk.kode, mk.nama, mk.sks, mk.semester)
                )
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_kode(self, kode: str) -> Optional[MataKuliah]:
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM matakuliah WHERE kode = ?", (kode,)
            ).fetchone()
        if row:
            return MataKuliah(row["kode"], row["nama"], row["sks"], row["semester"])
        return None

    def find_all(self) -> List[MataKuliah]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM matakuliah ORDER BY kode").fetchall()
        return [MataKuliah(r["kode"], r["nama"], r["sks"], r["semester"]) for r in rows]


class NilaiRepository(BaseRepository):
    """CRUD untuk tabel nilai (relasi Mahasiswa x MataKuliah)."""

    def __init__(self, db_path: str):
        super().__init__(db_path)
        self._create_table()

    def _create_table(self) -> None:
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS nilai (
                    nim         TEXT NOT NULL,
                    kode_mk     TEXT NOT NULL,
                    nip_dosen   TEXT NOT NULL,
                    nilai_angka REAL NOT NULL,
                    PRIMARY KEY (nim, kode_mk)
                )
            """)

    def insert_or_update(self, n: Nilai) -> None:
        """Insert nilai baru atau update jika sudah ada."""
        with self._get_conn() as conn:
            conn.execute("""
                INSERT INTO nilai VALUES (?, ?, ?, ?)
                ON CONFLICT(nim, kode_mk) DO UPDATE SET
                    nip_dosen   = excluded.nip_dosen,
                    nilai_angka = excluded.nilai_angka
            """, (n.nim, n.kode_mk, n.nip_dosen, n.nilai_angka))

    def get_by_nim(self, nim: str) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM nilai WHERE nim = ? ORDER BY kode_mk", (nim,)
            ).fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nip_dosen"], r["nilai_angka"]) for r in rows]

    def get_by_kode_mk(self, kode_mk: str) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM nilai WHERE kode_mk = ? ORDER BY nim", (kode_mk,)
            ).fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nip_dosen"], r["nilai_angka"]) for r in rows]

print("\n-- Demo MataKuliahRepository --")
mk_repo = MataKuliahRepository(DB_PATH)

data_mk = [
    MataKuliah("IF201", "Pemrograman Berorientasi Objek", 3, 3),
    MataKuliah("IF202", "Basis Data", 3, 3),
    MataKuliah("IF203", "Jaringan Komputer", 2, 4),
]
for mk in data_mk:
    ok = mk_repo.insert(mk)
    print(f"  Insert {mk.kode}: {'[OK]' if ok else '[SKIP]'} -- {mk.nama}")

print("\n-- Demo NilaiRepository --")
nilai_repo = NilaiRepository(DB_PATH)

data_nilai = [
    Nilai("2301001", "IF201", "198501001", 90.0),
    Nilai("2301001", "IF202", "198602002", 82.5),
    Nilai("2301002", "IF201", "198501001", 75.0),
    Nilai("2301002", "IF202", "198602002", 68.0),
    Nilai("2301003", "IF201", "198501001", 55.0),
]
for n in data_nilai:
    nilai_repo.insert_or_update(n)
    print(f"  Nilai {n.nim}/{n.kode_mk}: {n.nilai_angka} ({n.get_grade()})")

print("\n-- Cek Nilai Mahasiswa 2301001 --")
nilai_budi = nilai_repo.get_by_nim("2301001")
for n in nilai_budi:
    print(f"  {n.kode_mk}: {n.nilai_angka} | Grade: {n.get_grade()} | Bobot: {n.get_bobot()}")

# Cleanup
del mhs_repo, dosen_repo, mk_repo, nilai_repo
gc.collect()
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"\n[OK] Cleanup: {DB_PATH}")

print("\n" + "=" * 60)
print("02_repositories.py selesai!")
print("=" * 60)
