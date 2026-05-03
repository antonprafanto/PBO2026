"""
Proyek Akhir SiDigital -- Materi 15
File: 03_services.py
Topik: Service Layer -- Business Logic SiDigital

Jalankan: python 03_services.py
"""

import gc
import json
import sqlite3
import os
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

DB_PATH = "test_service.db"

# ======================================================================
# MODELS & EXCEPTIONS (ringkas)
# ======================================================================

class SiDigitalError(Exception):
    pass

class MahasiswaTidakDitemukan(SiDigitalError):
    pass

class DosenTidakDitemukan(SiDigitalError):
    pass

class MataKuliahTidakDitemukan(SiDigitalError):
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
# REPOSITORIES (ringkas)
# ======================================================================

class BaseRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def _get_conn(self) -> sqlite3.Connection:
        conn = sqlite3.connect(self.db_path)
        conn.row_factory = sqlite3.Row
        return conn

class MahasiswaRepository(BaseRepository):
    def __init__(self, db_path: str):
        super().__init__(db_path)
        with self._get_conn() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS mahasiswa (
                nim TEXT PRIMARY KEY, nama TEXT NOT NULL,
                angkatan INTEGER NOT NULL, program_studi TEXT NOT NULL)""")

    def insert(self, m: Mahasiswa) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute("INSERT INTO mahasiswa VALUES (?,?,?,?)",
                             (m.nim, m.nama, m.angkatan, m.program_studi))
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_nim(self, nim: str) -> Optional[Mahasiswa]:
        with self._get_conn() as conn:
            r = conn.execute("SELECT * FROM mahasiswa WHERE nim=?", (nim,)).fetchone()
        return Mahasiswa(r["nim"], r["nama"], r["angkatan"], r["program_studi"]) if r else None

    def find_all(self) -> List[Mahasiswa]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM mahasiswa ORDER BY nim").fetchall()
        return [Mahasiswa(r["nim"], r["nama"], r["angkatan"], r["program_studi"]) for r in rows]

class DosenRepository(BaseRepository):
    def __init__(self, db_path: str):
        super().__init__(db_path)
        with self._get_conn() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS dosen (
                nip TEXT PRIMARY KEY, nama TEXT NOT NULL, gelar TEXT)""")

    def insert(self, d: Dosen) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute("INSERT INTO dosen VALUES (?,?,?)", (d.nip, d.nama, d.gelar))
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_nip(self, nip: str) -> Optional[Dosen]:
        with self._get_conn() as conn:
            r = conn.execute("SELECT * FROM dosen WHERE nip=?", (nip,)).fetchone()
        return Dosen(r["nip"], r["nama"], r["gelar"] or "") if r else None

    def find_all(self) -> List[Dosen]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM dosen ORDER BY nip").fetchall()
        return [Dosen(r["nip"], r["nama"], r["gelar"] or "") for r in rows]

class MataKuliahRepository(BaseRepository):
    def __init__(self, db_path: str):
        super().__init__(db_path)
        with self._get_conn() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS matakuliah (
                kode TEXT PRIMARY KEY, nama TEXT NOT NULL,
                sks INTEGER NOT NULL, semester INTEGER NOT NULL)""")

    def insert(self, mk: MataKuliah) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute("INSERT INTO matakuliah VALUES (?,?,?,?)",
                             (mk.kode, mk.nama, mk.sks, mk.semester))
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_kode(self, kode: str) -> Optional[MataKuliah]:
        with self._get_conn() as conn:
            r = conn.execute("SELECT * FROM matakuliah WHERE kode=?", (kode,)).fetchone()
        return MataKuliah(r["kode"], r["nama"], r["sks"], r["semester"]) if r else None

    def find_all(self) -> List[MataKuliah]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM matakuliah ORDER BY kode").fetchall()
        return [MataKuliah(r["kode"], r["nama"], r["sks"], r["semester"]) for r in rows]

class NilaiRepository(BaseRepository):
    def __init__(self, db_path: str):
        super().__init__(db_path)
        with self._get_conn() as conn:
            conn.execute("""CREATE TABLE IF NOT EXISTS nilai (
                nim TEXT NOT NULL, kode_mk TEXT NOT NULL,
                nip_dosen TEXT NOT NULL, nilai_angka REAL NOT NULL,
                PRIMARY KEY (nim, kode_mk))""")

    def insert_or_update(self, n: Nilai) -> None:
        with self._get_conn() as conn:
            conn.execute("""INSERT INTO nilai VALUES (?,?,?,?)
                ON CONFLICT(nim, kode_mk) DO UPDATE SET
                nip_dosen=excluded.nip_dosen, nilai_angka=excluded.nilai_angka""",
                (n.nim, n.kode_mk, n.nip_dosen, n.nilai_angka))

    def get_by_nim(self, nim: str) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM nilai WHERE nim=? ORDER BY kode_mk", (nim,)).fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nip_dosen"], r["nilai_angka"]) for r in rows]

    def get_by_kode_mk(self, kode_mk: str) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute(
                "SELECT * FROM nilai WHERE kode_mk=? ORDER BY nim", (kode_mk,)).fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nip_dosen"], r["nilai_angka"]) for r in rows]

    def find_all(self) -> List[Nilai]:
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM nilai ORDER BY nim, kode_mk").fetchall()
        return [Nilai(r["nim"], r["kode_mk"], r["nip_dosen"], r["nilai_angka"]) for r in rows]

# ======================================================================
# BAGIAN 1: SiDigitalService -- Business Logic
#           Fokus: Orchestrate repositories, hitung IPK
# ======================================================================
print("=" * 60)
print("BAGIAN 1: SiDigitalService -- Business Logic")
print("=" * 60)

class SiDigitalService:
    """
    Service layer SiDigital.
    Mengorkestrasi semua repository dan mengandung business logic.
    """

    def __init__(self, db_path: str):
        self.mhs_repo = MahasiswaRepository(db_path)
        self.dosen_repo = DosenRepository(db_path)
        self.mk_repo = MataKuliahRepository(db_path)
        self.nilai_repo = NilaiRepository(db_path)

    # ----------------------------------------------------------------
    # CRUD helpers
    # ----------------------------------------------------------------
    def daftar_mahasiswa(self, nim: str, nama: str, angkatan: int,
                         prodi: str = "Informatika") -> Mahasiswa:
        mhs = Mahasiswa(nim, nama, angkatan, prodi)
        self.mhs_repo.insert(mhs)
        return mhs

    def tambah_dosen(self, nip: str, nama: str, gelar: str = "") -> Dosen:
        d = Dosen(nip, nama, gelar)
        self.dosen_repo.insert(d)
        return d

    def tambah_mk(self, kode: str, nama: str, sks: int,
                  semester: int = 1) -> MataKuliah:
        mk = MataKuliah(kode, nama, sks, semester)
        self.mk_repo.insert(mk)
        return mk

    # ----------------------------------------------------------------
    # Nilai
    # ----------------------------------------------------------------
    def input_nilai(self, nim: str, kode_mk: str, nip_dosen: str,
                    nilai_angka: float) -> Nilai:
        """Input nilai -- validasi entitas terkait ada di database."""
        if not self.mhs_repo.find_by_nim(nim):
            raise MahasiswaTidakDitemukan(f"NIM tidak ditemukan: {nim}")
        if not self.dosen_repo.find_by_nip(nip_dosen):
            raise DosenTidakDitemukan(f"NIP tidak ditemukan: {nip_dosen}")
        if not self.mk_repo.find_by_kode(kode_mk):
            raise MataKuliahTidakDitemukan(f"Kode MK tidak ditemukan: {kode_mk}")
        if not (0 <= nilai_angka <= 100):
            raise NilaiTidakValid(f"Nilai harus 0-100: {nilai_angka}")

        n = Nilai(nim, kode_mk, nip_dosen, nilai_angka)
        self.nilai_repo.insert_or_update(n)
        return n

    # ----------------------------------------------------------------
    # Transkrip & IPK
    # ----------------------------------------------------------------
    def get_transkrip(self, nim: str) -> Dict:
        """
        Hitung transkrip lengkap satu mahasiswa termasuk IPK.

        IPK = Sum(bobot * sks) / Sum(sks)
        """
        mhs = self.mhs_repo.find_by_nim(nim)
        if not mhs:
            raise MahasiswaTidakDitemukan(f"NIM tidak ditemukan: {nim}")

        nilai_list = self.nilai_repo.get_by_nim(nim)
        total_bobot_sks = 0.0
        total_sks = 0
        detail = []

        for n in nilai_list:
            mk = self.mk_repo.find_by_kode(n.kode_mk)
            sks = mk.sks if mk else 0
            bobot_sks = n.get_bobot() * sks
            total_bobot_sks += bobot_sks
            total_sks += sks
            detail.append({
                "kode_mk": n.kode_mk,
                "nama_mk": mk.nama if mk else "?",
                "sks": sks,
                "nilai_angka": n.nilai_angka,
                "grade": n.get_grade(),
                "bobot": n.get_bobot(),
            })

        ipk = round(total_bobot_sks / total_sks, 2) if total_sks > 0 else 0.0

        return {
            "nim": mhs.nim,
            "nama": mhs.nama,
            "program_studi": mhs.program_studi,
            "angkatan": mhs.angkatan,
            "detail_nilai": detail,
            "total_sks": total_sks,
            "ipk": ipk,
            "status": "Lulus" if ipk >= 2.0 else "Tidak Lulus",
        }

    # ----------------------------------------------------------------
    # Statistik
    # ----------------------------------------------------------------
    def get_statistik_mk(self, kode_mk: str) -> Dict:
        """Statistik nilai per matakuliah."""
        mk = self.mk_repo.find_by_kode(kode_mk)
        if not mk:
            raise MataKuliahTidakDitemukan(f"Kode MK tidak ditemukan: {kode_mk}")

        nilai_list = self.nilai_repo.get_by_kode_mk(kode_mk)
        if not nilai_list:
            return {"kode_mk": kode_mk, "nama": mk.nama, "jumlah_peserta": 0,
                    "rata_rata": 0.0, "nilai_tertinggi": 0.0, "nilai_terendah": 0.0,
                    "distribusi_grade": {}}

        angka_list = [n.nilai_angka for n in nilai_list]
        distribusi: Dict[str, int] = {}
        for n in nilai_list:
            g = n.get_grade()
            distribusi[g] = distribusi.get(g, 0) + 1

        return {
            "kode_mk": kode_mk,
            "nama": mk.nama,
            "jumlah_peserta": len(nilai_list),
            "rata_rata": round(sum(angka_list) / len(angka_list), 2),
            "nilai_tertinggi": max(angka_list),
            "nilai_terendah": min(angka_list),
            "distribusi_grade": distribusi,
        }

    # ----------------------------------------------------------------
    # Export
    # ----------------------------------------------------------------
    def export_backup(self, filepath: str) -> None:
        """Export seluruh data ke file JSON."""
        data = {
            "mahasiswa": [asdict(m) for m in self.mhs_repo.find_all()],
            "dosen": [asdict(d) for d in self.dosen_repo.find_all()],
            "matakuliah": [asdict(mk) for mk in self.mk_repo.find_all()],
            "nilai": [asdict(n) for n in self.nilai_repo.find_all()],
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Export ke {filepath} selesai")


# ======================================================================
# DEMO
# ======================================================================
print("\n-- Inisialisasi SiDigitalService --")
service = SiDigitalService(DB_PATH)

# Populate data
print("\n-- Tambah Data --")
service.daftar_mahasiswa("2301001", "Budi Santoso", 2023)
service.daftar_mahasiswa("2301002", "Sari Dewi", 2023)
service.daftar_mahasiswa("2301003", "Ahmad Fauzi", 2023, "Sistem Informasi")
service.tambah_dosen("198501001", "Ahmad Wahyudi", "Dr.")
service.tambah_dosen("198602002", "Siti Rahayu", "M.Kom.")
service.tambah_mk("IF201", "Pemrograman Berorientasi Objek", 3, 3)
service.tambah_mk("IF202", "Basis Data", 3, 3)
service.tambah_mk("IF203", "Jaringan Komputer", 2, 4)
print("  Data mahasiswa, dosen, matakuliah: [OK]")

# Input nilai
print("\n-- Input Nilai --")
nilai_data = [
    ("2301001", "IF201", "198501001", 90.0),
    ("2301001", "IF202", "198602002", 82.5),
    ("2301001", "IF203", "198501001", 77.0),
    ("2301002", "IF201", "198501001", 75.0),
    ("2301002", "IF202", "198602002", 65.0),
    ("2301003", "IF201", "198501001", 55.0),
    ("2301003", "IF202", "198602002", 60.0),
]
for nim, kode_mk, nip, angka in nilai_data:
    n = service.input_nilai(nim, kode_mk, nip, angka)
    print(f"  {nim} | {kode_mk}: {angka} ({n.get_grade()})")

# BAGIAN 2: Transkrip dengan IPK
print("\n" + "=" * 60)
print("BAGIAN 2: Transkrip dan IPK")
print("=" * 60)

for nim in ["2301001", "2301002", "2301003"]:
    t = service.get_transkrip(nim)
    print(f"\n  Transkrip: {t['nama']} ({t['nim']})")
    print(f"  Program Studi: {t['program_studi']}")
    for d in t["detail_nilai"]:
        print(f"    {d['kode_mk']} ({d['sks']} SKS): {d['nilai_angka']} ({d['grade']})")
    print(f"  Total SKS: {t['total_sks']} | IPK: {t['ipk']} | Status: {t['status']}")

# BAGIAN 3: Statistik MK
print("\n" + "=" * 60)
print("BAGIAN 3: Statistik per Matakuliah")
print("=" * 60)

for kode in ["IF201", "IF202"]:
    stat = service.get_statistik_mk(kode)
    print(f"\n  {stat['nama']} ({stat['kode_mk']})")
    print(f"  Peserta: {stat['jumlah_peserta']} | Rata-rata: {stat['rata_rata']}")
    print(f"  Tertinggi: {stat['nilai_tertinggi']} | Terendah: {stat['nilai_terendah']}")
    print(f"  Distribusi: {stat['distribusi_grade']}")

# Export JSON
print("\n-- Export Backup JSON --")
JSON_PATH = "test_backup.json"
service.export_backup(JSON_PATH)
with open(JSON_PATH, "r", encoding="utf-8") as f:
    backup = json.load(f)
print(f"  Berisi: {len(backup['mahasiswa'])} mahasiswa, "
      f"{len(backup['dosen'])} dosen, {len(backup['matakuliah'])} mk, "
      f"{len(backup['nilai'])} nilai")

# Cleanup
del service
gc.collect()
for f in [DB_PATH, JSON_PATH]:
    if os.path.exists(f):
        os.remove(f)
        print(f"[OK] Cleanup: {f}")

print("\n" + "=" * 60)
print("03_services.py selesai!")
print("=" * 60)
