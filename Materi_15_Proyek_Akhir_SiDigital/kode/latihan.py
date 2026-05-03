"""
Proyek Akhir SiDigital -- Materi 15
File: latihan.py
Topik: Pengembangan Fitur SiDigital secara Mandiri

Instruksi: Pilih minimal 2 dari 3 soal untuk diselesaikan!
Jalankan: python latihan.py
"""

import gc
import json
import sqlite3
import os
from dataclasses import dataclass, asdict
from typing import List, Optional, Dict

print("=" * 60)
print("LATIHAN MATERI 15: Proyek Akhir SiDigital")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Sedang): Fitur Pencarian dan Filter
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 1 (*Sedang): Pencarian dan Filter")
print("=" * 60)

# Kamu sudah punya sistem SiDigital dari 04_main.py.
# Sekarang tambahkan fitur pencarian dan filter ke SiDigitalService.
#
# TODO: Implementasi method berikut di SiDigitalService:
#
# 1. cari_mahasiswa_by_nama(self, keyword: str) -> List[Mahasiswa]
#    - Cari mahasiswa yang namanya mengandung keyword (case-insensitive)
#    - Gunakan SQL: WHERE LOWER(nama) LIKE ?
#    - Contoh: cari_mahasiswa_by_nama("budi") -> [Mahasiswa(...)]
#
# 2. filter_mahasiswa_by_prodi(self, prodi: str) -> List[Mahasiswa]
#    - Filter mahasiswa berdasarkan program studi
#    - Gunakan SQL: WHERE program_studi = ?
#
# 3. get_mahasiswa_ipk_diatas(self, batas: float) -> List[Dict]
#    - Ambil semua mahasiswa yang IPK-nya >= batas
#    - Gunakan get_transkrip() untuk hitung IPK tiap mahasiswa
#    - Urutkan dari IPK tertinggi ke terendah
#    - Return: [{"nim": ..., "nama": ..., "ipk": ...}, ...]
#
# Contoh penggunaan:
#   service = SiDigitalService("latihan1.db")
#   # ... populate data dulu ...
#   hasil = service.cari_mahasiswa_by_nama("budi")
#   print(hasil)
#   hasil = service.get_mahasiswa_ipk_diatas(3.0)
#   for m in hasil:
#       print(f"{m['nama']}: IPK {m['ipk']}")
#   # Cleanup: del service; gc.collect(); os.remove("latihan1.db")
#
# TIPS:
#   - LIKE query: execute("... WHERE LOWER(nama) LIKE ?", (f"%{keyword.lower()}%",))
#   - Sort list of dict: sorted(hasil, key=lambda x: x["ipk"], reverse=True)

pass  # TODO: Implementasi di sini

print("\n-- SOAL 1: Test Pencarian & Filter --")
print("[X] Soal 1 belum dikerjakan (stub)")
print("    TODO: cari_mahasiswa_by_nama(), filter_by_prodi(), get_ipk_diatas()")

# ======================================================================
# SOAL 2 (**Sedang): Fitur Update dan Delete
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 2 (**Sedang): Update dan Delete")
print("=" * 60)

# SiDigitalService belum punya method update dan delete yang aman.
# Tambahkan method berikut dengan validasi yang proper.
#
# TODO: Implementasi method berikut di SiDigitalService:
#
# 1. update_mahasiswa(self, nim: str, nama_baru: str = None,
#                     prodi_baru: str = None) -> Mahasiswa
#    - Cari mahasiswa, raise MahasiswaTidakDitemukan jika tidak ada
#    - Update hanya field yang tidak None
#    - Simpan ke DB dan return mahasiswa yang sudah diupdate
#
# 2. hapus_mahasiswa(self, nim: str) -> bool
#    - Cari mahasiswa, raise MahasiswaTidakDitemukan jika tidak ada
#    - Hapus SEMUA nilai milik mahasiswa ini dulu (cascade delete manual)
#    - Baru hapus record mahasiswa
#    - Return True jika berhasil
#
# 3. update_nilai(self, nim: str, kode_mk: str,
#                 nilai_baru: float) -> Nilai
#    - Cek mahasiswa dan MK ada, raise exception jika tidak
#    - Validasi nilai_baru 0-100
#    - Update nilai menggunakan insert_or_update()
#    - Return Nilai yang sudah diupdate
#
# Contoh penggunaan:
#   mhs = service.update_mahasiswa("2301001", nama_baru="Budi S. Wijaya")
#   print(mhs.nama)  # Budi S. Wijaya
#   service.hapus_mahasiswa("2301003")  # hapus beserta nilainya
#   nilai = service.update_nilai("2301001", "IF201", 95.0)
#   print(nilai.get_grade())  # A
#
# TIPS:
#   - UPDATE SQL: SET nama=COALESCE(?, nama) untuk update kondisional
#   - Atau: baca dulu, modifikasi object, lalu save ulang
#   - Untuk cascade delete nilai: DELETE FROM nilai WHERE nim=?

pass  # TODO: Implementasi di sini

print("\n-- SOAL 2: Test Update & Delete --")
print("[X] Soal 2 belum dikerjakan (stub)")
print("    TODO: update_mahasiswa(), hapus_mahasiswa(), update_nilai()")

# ======================================================================
# SOAL 3 (***Sulit): Fitur Absensi dan Laporan Lengkap
# ======================================================================
print("\n" + "=" * 60)
print("SOAL 3 (***Sulit): Fitur Absensi + Laporan")
print("=" * 60)

# Tambahkan fitur absensi dan laporan akademik yang lebih lengkap.
#
# TODO:
#
# BAGIAN A: Model dan Repository Absensi
#
# 1. @dataclass Absensi:
#    - nim (str), kode_mk (str), tanggal (str, format "YYYY-MM-DD")
#    - hadir (bool) -- True=hadir, False=tidak hadir
#
# 2. AbsensiRepository(BaseRepository):
#    - _create_table(): CREATE TABLE absensi (nim, kode_mk, tanggal, hadir, PK(nim,kode_mk,tanggal))
#    - catat(self, absensi: Absensi) -> bool
#    - get_by_nim_mk(self, nim: str, kode_mk: str) -> List[Absensi]
#    - hitung_kehadiran(self, nim: str, kode_mk: str) -> float
#      (return persentase kehadiran: jumlah_hadir / total_pertemuan * 100)
#
# BAGIAN B: Integrasi ke SiDigitalService
#
# 3. tambah method catat_absensi(self, nim, kode_mk, tanggal, hadir=True) -> Absensi
# 4. tambah method get_laporan_kehadiran(self, nim: str) -> Dict
#    Return: {"nim": ..., "nama": ...,
#             "kehadiran": [{"kode_mk": ..., "nama_mk": ..., "persen": 80.0}, ...]}
#
# BAGIAN C: Rule bisnis
# 5. Modifikasi input_nilai(): jika kehadiran mahasiswa < 75%, raise exception
#    dengan pesan "Kehadiran di bawah 75%, tidak bisa input nilai"
#
# Contoh penggunaan:
#   # Catat absensi 10 pertemuan
#   for i in range(10):
#       service.catat_absensi("2301001", "IF201",
#                             f"2024-03-{i+1:02d}", hadir=(i < 8))  # 8 hadir 2 absen
#   laporan = service.get_laporan_kehadiran("2301001")
#   print(laporan)  # {"nim":..., "kehadiran": [{"kode_mk":"IF201", "persen": 80.0}]}
#
# TIPS:
#   - Hitung persen: COUNT(*) WHERE hadir=1 / COUNT(*) * 100
#   - Untuk rule bisnis di input_nilai():
#     persen = self.absensi_repo.hitung_kehadiran(nim, kode_mk)
#     if persen > 0 and persen < 75: raise NilaiTidakValid("...")

pass  # TODO: Implementasi di sini

print("\n-- SOAL 3: Test Absensi + Laporan --")
print("[X] Soal 3 belum dikerjakan (stub)")
print("    TODO: AbsensiRepository + integrasi + rule bisnis 75%")

# ======================================================================
# SUMMARY
# ======================================================================
print("\n" + "=" * 60)
print("SUMMARY PROYEK AKHIR SIDIGITAL")
print("=" * 60)
print("""
SOAL 1 (*Sedang): Pencarian & Filter
  Status : [X] Belum dikerjakan
  Fitur  : cari_mahasiswa_by_nama(), filter_by_prodi(), get_ipk_diatas()
  Konsep : SQL LIKE query, sort list of dict
  Effort : ~30-40 menit

SOAL 2 (**Sedang): Update & Delete
  Status : [X] Belum dikerjakan
  Fitur  : update_mahasiswa(), hapus_mahasiswa(), update_nilai()
  Konsep : UPDATE SQL, cascade delete, exception handling
  Effort : ~35-45 menit

SOAL 3 (***Sulit): Absensi + Laporan
  Status : [X] Belum dikerjakan
  Fitur  : AbsensiRepository, catat_absensi(), get_laporan_kehadiran()
  Konsep : Tabel baru, rule bisnis, integrasi service
  Effort : ~60-80 menit

RUBRIK PENILAIAN:
  - Soal 1 saja     : 40/100
  - Soal 1 + 2      : 70/100
  - Soal 1 + 2 + 3  : 100/100

PANDUAN UMUM:
  1. Salin seluruh code dari 04_main.py sebagai base
  2. Tambahkan fitur yang diminta di atas
  3. Buat demo/test di bagian bawah
  4. Cleanup semua file .db dan .json setelah test
  5. Pastikan: parameterized query, encoding utf-8, tidak ada print Unicode

REFERENSI:
  - 03_services.py : pola SiDigitalService
  - 04_main.py     : pola demo lengkap
  - Materi_14/kode/03_sqlite_oop.py : pola repository SQLite
""")
print("=" * 60)
print("Latihan selesai!")
print("=" * 60)
