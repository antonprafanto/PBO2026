"""
Proyek Akhir SiDigital -- Materi 15
File: 04_main.py
Topik: Aplikasi SiDigital Lengkap -- Integrasi semua konsep OOP

Jalankan: python 04_main.py
"""

import gc
import json
import sqlite3
import os
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

DB_FILE = "sidigital.db"
JSON_BACKUP = "sidigital_backup.json"

# ==============================================================
# EXCEPTIONS
# ==============================================================

class SiDigitalError(Exception):
    """Base exception SiDigital."""
    pass

class MahasiswaTidakValid(SiDigitalError):
    pass

class MahasiswaTidakDitemukan(SiDigitalError):
    pass

class DosenTidakDitemukan(SiDigitalError):
    pass

class MataKuliahTidakValid(SiDigitalError):
    pass

class MataKuliahTidakDitemukan(SiDigitalError):
    pass

class NilaiTidakValid(SiDigitalError):
    pass

# ==============================================================
# MODELS
# ==============================================================

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    angkatan: int
    program_studi: str = "Informatika"

    def __post_init__(self):
        if len(self.nim) < 6:
            raise MahasiswaTidakValid(f"NIM minimal 6 karakter: '{self.nim}'")

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

    def __post_init__(self):
        if not (1 <= self.sks <= 6):
            raise MataKuliahTidakValid(f"SKS harus 1-6: {self.sks}")

@dataclass
class Nilai:
    nim: str
    kode_mk: str
    nip_dosen: str
    nilai_angka: float

    def __post_init__(self):
        if not (0 <= self.nilai_angka <= 100):
            raise NilaiTidakValid(f"Nilai harus 0-100: {self.nilai_angka}")

    def get_grade(self) -> str:
        if self.nilai_angka >= 80: return "A"
        elif self.nilai_angka >= 70: return "B"
        elif self.nilai_angka >= 60: return "C"
        elif self.nilai_angka >= 50: return "D"
        else: return "E"

    def get_bobot(self) -> float:
        return {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}[self.get_grade()]

# ==============================================================
# REPOSITORIES
# ==============================================================

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

    def update(self, m: Mahasiswa) -> bool:
        with self._get_conn() as conn:
            cur = conn.execute(
                "UPDATE mahasiswa SET nama=?, angkatan=?, program_studi=? WHERE nim=?",
                (m.nama, m.angkatan, m.program_studi, m.nim))
        return cur.rowcount > 0

    def delete(self, nim: str) -> bool:
        with self._get_conn() as conn:
            cur = conn.execute("DELETE FROM mahasiswa WHERE nim=?", (nim,))
        return cur.rowcount > 0


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

    def count_by_nim(self, nim: str) -> int:
        with self._get_conn() as conn:
            return conn.execute(
                "SELECT COUNT(*) FROM nilai WHERE nim=?", (nim,)).fetchone()[0]

# ==============================================================
# SERVICE LAYER
# ==============================================================

class SiDigitalService:
    """Service layer SiDigital -- semua business logic di sini."""

    def __init__(self, db_path: str):
        self.mhs_repo = MahasiswaRepository(db_path)
        self.dosen_repo = DosenRepository(db_path)
        self.mk_repo = MataKuliahRepository(db_path)
        self.nilai_repo = NilaiRepository(db_path)

    # ---- Registrasi ----
    def daftar_mahasiswa(self, nim: str, nama: str, angkatan: int,
                         prodi: str = "Informatika") -> Optional[Mahasiswa]:
        mhs = Mahasiswa(nim, nama, angkatan, prodi)
        return mhs if self.mhs_repo.insert(mhs) else None

    def tambah_dosen(self, nip: str, nama: str, gelar: str = "") -> Optional[Dosen]:
        d = Dosen(nip, nama, gelar)
        return d if self.dosen_repo.insert(d) else None

    def tambah_mk(self, kode: str, nama: str, sks: int,
                  semester: int = 1) -> Optional[MataKuliah]:
        mk = MataKuliah(kode, nama, sks, semester)
        return mk if self.mk_repo.insert(mk) else None

    # ---- Nilai ----
    def input_nilai(self, nim: str, kode_mk: str, nip_dosen: str,
                    nilai_angka: float) -> Nilai:
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

    # ---- Transkrip & IPK ----
    def get_transkrip(self, nim: str) -> Dict:
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
            total_bobot_sks += n.get_bobot() * sks
            total_sks += sks
            detail.append({
                "kode_mk": n.kode_mk,
                "nama_mk": mk.nama if mk else "?",
                "sks": sks,
                "nilai_angka": n.nilai_angka,
                "grade": n.get_grade(),
            })

        ipk = round(total_bobot_sks / total_sks, 2) if total_sks > 0 else 0.0
        return {
            "nim": mhs.nim, "nama": mhs.nama,
            "program_studi": mhs.program_studi, "angkatan": mhs.angkatan,
            "detail_nilai": detail, "total_sks": total_sks,
            "ipk": ipk, "status": "Lulus" if ipk >= 2.0 else "Tidak Lulus",
        }

    # ---- Statistik ----
    def get_statistik_mk(self, kode_mk: str) -> Dict:
        mk = self.mk_repo.find_by_kode(kode_mk)
        if not mk:
            raise MataKuliahTidakDitemukan(kode_mk)
        nilai_list = self.nilai_repo.get_by_kode_mk(kode_mk)
        if not nilai_list:
            return {"kode_mk": kode_mk, "nama": mk.nama, "jumlah_peserta": 0}
        angka_list = [n.nilai_angka for n in nilai_list]
        distribusi: Dict[str, int] = {}
        for n in nilai_list:
            g = n.get_grade()
            distribusi[g] = distribusi.get(g, 0) + 1
        return {
            "kode_mk": kode_mk, "nama": mk.nama,
            "jumlah_peserta": len(nilai_list),
            "rata_rata": round(sum(angka_list) / len(angka_list), 2),
            "nilai_tertinggi": max(angka_list),
            "nilai_terendah": min(angka_list),
            "distribusi_grade": dict(sorted(distribusi.items())),
        }

    # ---- Export ----
    def export_backup(self, filepath: str) -> None:
        data = {
            "mahasiswa": [asdict(m) for m in self.mhs_repo.find_all()],
            "dosen": [asdict(d) for d in self.dosen_repo.find_all()],
            "matakuliah": [asdict(mk) for mk in self.mk_repo.find_all()],
            "nilai": [asdict(n) for n in self.nilai_repo.find_all()],
        }
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"[OK] Backup disimpan ke {filepath}")

# ==============================================================
# APLIKASI SIDIGITAL
# ==============================================================
print("=" * 60)
print("SIDIGITAL -- Sistem Informasi Kampus Digital")
print("Universitas Mulawarman -- Informatika")
print("=" * 60)

app = SiDigitalService(DB_FILE)

# ----- Setup Awal -----
print("\n[1] Registrasi Mahasiswa")
mahasiswa_data = [
    ("2301001", "Budi Santoso", 2023),
    ("2301002", "Sari Dewi", 2023),
    ("2301003", "Ahmad Fauzi", 2023),
    ("2301004", "Diana Putri", 2023, "Sistem Informasi"),
    ("2301005", "Erik Wijaya", 2023),
]
for row in mahasiswa_data:
    nim, nama, angkatan = row[0], row[1], row[2]
    prodi = row[3] if len(row) > 3 else "Informatika"
    m = app.daftar_mahasiswa(nim, nama, angkatan, prodi)
    if m:
        print(f"  [OK] {m.nim} -- {m.nama} ({m.program_studi})")

print("\n[2] Registrasi Dosen")
dosen_data = [
    ("198501001", "Ahmad Wahyudi", "Dr."),
    ("198602002", "Siti Rahayu", "M.Kom."),
    ("197803003", "Bambang Prasetyo", "Prof. Dr."),
]
for nip, nama, gelar in dosen_data:
    d = app.tambah_dosen(nip, nama, gelar)
    if d:
        print(f"  [OK] {d.nip} -- {d.nama_lengkap()}")

print("\n[3] Setup Matakuliah")
mk_data = [
    ("IF201", "Pemrograman Berorientasi Objek", 3, 3),
    ("IF202", "Basis Data", 3, 3),
    ("IF203", "Jaringan Komputer", 2, 4),
    ("IF204", "Kecerdasan Buatan", 3, 5),
]
for kode, nama, sks, sem in mk_data:
    mk = app.tambah_mk(kode, nama, sks, sem)
    if mk:
        print(f"  [OK] {mk.kode} -- {mk.nama} ({mk.sks} SKS, Sem {mk.semester})")

print("\n[4] Input Nilai")
nilai_data = [
    ("2301001", "IF201", "198501001", 92.0),
    ("2301001", "IF202", "198602002", 85.0),
    ("2301001", "IF203", "197803003", 78.0),
    ("2301001", "IF204", "198501001", 88.0),
    ("2301002", "IF201", "198501001", 75.0),
    ("2301002", "IF202", "198602002", 68.0),
    ("2301002", "IF203", "197803003", 82.0),
    ("2301003", "IF201", "198501001", 55.0),
    ("2301003", "IF202", "198602002", 62.0),
    ("2301004", "IF201", "198501001", 95.0),
    ("2301004", "IF202", "198602002", 91.0),
    ("2301004", "IF204", "198501001", 87.0),
    ("2301005", "IF201", "198501001", 48.0),
    ("2301005", "IF202", "198602002", 52.0),
]
for nim, kode_mk, nip, angka in nilai_data:
    try:
        n = app.input_nilai(nim, kode_mk, nip, angka)
        print(f"  [OK] {nim} | {kode_mk}: {angka} ({n.get_grade()})")
    except SiDigitalError as e:
        print(f"  [FAIL] {e}")

# ----- Laporan Transkrip -----
print("\n" + "=" * 60)
print("[5] Transkrip Nilai")
print("=" * 60)

for nim in ["2301001", "2301002", "2301003", "2301004", "2301005"]:
    t = app.get_transkrip(nim)
    print(f"\n  Mahasiswa : {t['nama']} ({t['nim']})")
    print(f"  Prodi     : {t['program_studi']} | Angkatan: {t['angkatan']}")
    for d in t["detail_nilai"]:
        print(f"    {d['kode_mk']} -- {d['nama_mk']:<35} {d['sks']} SKS | "
              f"{d['nilai_angka']:5.1f} ({d['grade']})")
    print(f"  Total SKS : {t['total_sks']} | IPK: {t['ipk']:4.2f} | Status: {t['status']}")

# ----- Statistik MK -----
print("\n" + "=" * 60)
print("[6] Statistik Matakuliah")
print("=" * 60)

for kode in ["IF201", "IF202", "IF203"]:
    s = app.get_statistik_mk(kode)
    print(f"\n  {s['nama']} ({s['kode_mk']})")
    print(f"  Peserta: {s['jumlah_peserta']} | Rata-rata: {s['rata_rata']}")
    print(f"  Tertinggi: {s['nilai_tertinggi']} | Terendah: {s['nilai_terendah']}")
    print(f"  Distribusi Grade: {s['distribusi_grade']}")

# ----- Error Handling Demo -----
print("\n" + "=" * 60)
print("[7] Demo Error Handling")
print("=" * 60)

error_cases = [
    ("NIM tidak ada", lambda: app.get_transkrip("9999999")),
    ("NIM invalid", lambda: app.daftar_mahasiswa("12", "Test", 2023)),
    ("Nilai > 100", lambda: app.input_nilai("2301001", "IF201", "198501001", 110.0)),
    ("Dosen tidak ada", lambda: app.input_nilai("2301001", "IF201", "NIPXXX", 80.0)),
]
for label, fn in error_cases:
    try:
        fn()
        print(f"  [FAIL] {label}: seharusnya error!")
    except SiDigitalError as e:
        print(f"  [OK] {label}: {type(e).__name__}")

# ----- Export Backup -----
print("\n" + "=" * 60)
print("[8] Export JSON Backup")
print("=" * 60)
app.export_backup(JSON_BACKUP)
with open(JSON_BACKUP, "r", encoding="utf-8") as f:
    bk = json.load(f)
print(f"  Backup: {len(bk['mahasiswa'])} mahasiswa | "
      f"{len(bk['dosen'])} dosen | {len(bk['matakuliah'])} matakuliah | "
      f"{len(bk['nilai'])} nilai")

# Cleanup
del app
gc.collect()
for f in [DB_FILE, JSON_BACKUP]:
    if os.path.exists(f):
        os.remove(f)
        print(f"[OK] Cleanup: {f}")

print("\n" + "=" * 60)
print("SiDigital selesai! Semua konsep OOP berhasil diterapkan.")
print("=" * 60)
