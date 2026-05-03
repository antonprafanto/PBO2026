"""
Latihan Materi 14 -- OOP + File & Database

File: latihan.py
Instruksi: Kerjakan semua SOAL dengan baik!

Jalankan: python latihan.py
"""

import json
import sqlite3
import os
from dataclasses import dataclass, field, asdict
from typing import List, Optional

print("=" * 60)
print("LATIHAN MATERI 14: OOP + File & Database")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah): JSON Repository untuk Buku
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 1 (*Mudah): JSON Repository untuk Buku")
print("=" * 60)

# TODO: Implementasi @dataclass Buku dan BukuJsonRepo
#
# 1. Buat @dataclass Buku:
#    - Atribut: isbn (str), judul (str), pengarang (str), tahun (int)
#    - Validation di __post_init__: tahun harus 1900-2030
#
# 2. Buat class BukuJsonRepo:
#    - __init__(self, filepath: str)
#    - save_all(self, buku_list: List[Buku]) -> None
#    - load_all(self) -> List[Buku]
#    - add(self, buku: Buku) -> None      (tambah satu buku, simpan ulang)
#    - find_by_isbn(self, isbn: str) -> Optional[Buku]
#
# Contoh:
#   repo = BukuJsonRepo("buku.json")
#   repo.add(Buku("978-1", "Python OOP", "Anton", 2024))
#   repo.add(Buku("978-2", "Clean Code", "Martin", 2008))
#   buku = repo.find_by_isbn("978-1")
#   print(buku.judul)  # Python OOP
#   os.remove("buku.json")
#
# TIPS:
#   - Gunakan asdict() untuk konversi @dataclass ke dict
#   - Gunakan Buku(**d) untuk konversi dict ke @dataclass
#   - Handle FileNotFoundError di load_all()

pass  # TODO: Implementasi di sini

print("\n-- SOAL 1: Test BukuJsonRepo --")
print("[X] Soal 1 belum dikerjakan (stub)")
print("    TODO: @dataclass Buku + BukuJsonRepo dengan JSON")

# ======================================================================
# SOAL 2 (**Sedang): SQLite Repository untuk Produk
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 2 (**Sedang): SQLite Repository untuk Produk")
print("=" * 60)

# TODO: Implementasi @dataclass Produk dan ProdukRepository
#
# 1. Buat @dataclass Produk:
#    - Atribut: id (str), nama (str), harga (float), stok (int)
#    - Validation: harga >= 0, stok >= 0
#
# 2. Buat class ProdukRepository:
#    - __init__(self, db_path: str)  -- auto create table
#    - _get_conn(self)
#    - _create_table(self)   -- tabel produk (id PK, nama, harga, stok)
#    - insert(self, produk: Produk) -> bool
#    - find_by_id(self, id: str) -> Optional[Produk]
#    - find_all(self) -> List[Produk]
#    - update_stok(self, id: str, stok_baru: int) -> bool
#    - delete(self, id: str) -> bool
#
# Contoh:
#   repo = ProdukRepository("toko.db")
#   repo.insert(Produk("P001", "Laptop", 8500000.0, 10))
#   repo.insert(Produk("P002", "Mouse", 150000.0, 50))
#   repo.update_stok("P001", 9)  # beli 1
#   print(repo.find_all())
#   os.remove("toko.db")
#
# TIPS:
#   - Gunakan parameterized query: execute("... WHERE id = ?", (id,))
#   - JANGAN string interpolation f"WHERE id = '{id}'" (SQL injection!)
#   - Gunakan conn.row_factory = sqlite3.Row untuk akses by name
#   - Gunakan try/except IntegrityError untuk duplicate insert

pass  # TODO: Implementasi di sini

print("\n-- SOAL 2: Test ProdukRepository --")
print("[X] Soal 2 belum dikerjakan (stub)")
print("    TODO: @dataclass Produk + SQLite CRUD Repository")

# ======================================================================
# SOAL 3 (***Sulit): Sistem Perpustakaan dengan JSON + SQLite
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 3 (***Sulit): Sistem Perpustakaan")
print("=" * 60)

# TODO: Implementasi sistem perpustakaan lengkap
#
# 1. @dataclass Buku(isbn, judul, pengarang, tahun, stok)
# 2. @dataclass Anggota(id_anggota, nama, email)
# 3. @dataclass Peminjaman(id_pinjam, id_anggota, isbn, tanggal, is_kembali)
#
# 4. BukuRepository(SQLite):
#    - insert, find_by_isbn, find_all, update_stok
#
# 5. AnggotaRepository(SQLite):
#    - insert, find_by_id, find_all
#
# 6. PeminjamanRepository(SQLite):
#    - insert(peminjaman) -- cek stok dulu, kurangi stok buku
#    - kembalikan(id_pinjam) -- tandai is_kembali=True, tambah stok
#    - get_aktif_by_anggota(id_anggota) -- daftar pinjaman belum kembali
#
# 7. PerpustakaanService:
#    - __init__(db_path)  -- init semua repositories
#    - daftarkan_anggota(id, nama, email)
#    - tambah_buku(isbn, judul, pengarang, tahun, stok)
#    - pinjam_buku(id_anggota, isbn) -> bool
#    - kembalikan_buku(id_pinjam) -> bool
#    - laporan_anggota(id_anggota) -> dict
#    - export_backup(filepath) -- export ke JSON
#
# Contoh:
#   service = PerpustakaanService("perpus.db")
#   service.daftarkan_anggota("A001", "Budi", "budi@email.com")
#   service.tambah_buku("978-1", "Python OOP", "Anton", 2024, 3)
#   service.pinjam_buku("A001", "978-1")
#   laporan = service.laporan_anggota("A001")
#   service.export_backup("perpus_backup.json")
#   # Cleanup: os.remove("perpus.db"), os.remove("perpus_backup.json")

pass  # TODO: Implementasi di sini

print("\n-- SOAL 3: Test Sistem Perpustakaan --")
print("[X] Soal 3 belum dikerjakan (stub)")
print("    TODO: Full sistem dengan JSON + SQLite + Service layer")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n" + "=" * 60)
print("SUMMARY LATIHAN")
print("=" * 60)

print("""
SOAL 1 (MUDAH): JSON Repository untuk Buku
  Status: [X] Belum dikerjakan
  TODO:
    1. @dataclass Buku dengan validation
    2. BukuJsonRepo: save_all, load_all, add, find_by_isbn
    3. Gunakan asdict() dan Buku(**d)
    4. Handle FileNotFoundError di load_all()
    5. Cleanup file setelah test
  Reference: 01_json_oop.py
  Effort: ~15-20 menit

SOAL 2 (SEDANG): SQLite Repository untuk Produk
  Status: [X] Belum dikerjakan
  TODO:
    1. @dataclass Produk dengan validation
    2. ProdukRepository dengan CRUD lengkap
    3. Parameterized query (WAJIB, hindari SQL injection)
    4. row_factory = sqlite3.Row untuk akses kolom by name
    5. Cleanup file .db setelah test
  Reference: 03_sqlite_oop.py
  Effort: ~25-30 menit

SOAL 3 (SULIT): Sistem Perpustakaan
  Status: [X] Belum dikerjakan
  TODO:
    1. 3 dataclasses: Buku, Anggota, Peminjaman
    2. 3 repositories: BukuRepo, AnggotaRepo, PeminjamanRepo
    3. Service layer yang combine semua repos
    4. Logic bisnis: cek stok saat pinjam, update saat kembali
    5. Export JSON backup
    6. Full cleanup setelah test
  Reference: 04_studi_kasus.py untuk arsitektur
  Effort: ~50-60 menit

TIPS UMUM:
  1. Selalu gunakan 'with open()' untuk buka file
  2. Selalu parameterized query untuk SQLite
  3. Handle FileNotFoundError dan IntegrityError
  4. Cleanup file test (.json, .db) setelah selesai
  5. Gunakan asdict() untuk @dataclass ke JSON
  6. row_factory = sqlite3.Row untuk akses kolom by name
""")

print("=" * 60)
print("Latihan selesai!")
print("=" * 60)
