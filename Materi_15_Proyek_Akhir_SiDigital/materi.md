# Materi 15 -- Proyek Akhir: SiDigital

---

## 1. Tentang SiDigital

**SiDigital** (Sistem Informasi Kampus Digital) adalah proyek akhir semester yang mengintegrasikan seluruh konsep OOP yang telah dipelajari di Materi 1 sampai 14.

SiDigital adalah mini-aplikasi manajemen akademik kampus yang memiliki fitur:

- Kelola data **Mahasiswa** (CRUD)
- Kelola data **Dosen** (CRUD)
- Kelola **Matakuliah** (CRUD)
- **Input dan ubah Nilai** mahasiswa
- Cetak **Transkrip** lengkap per mahasiswa
- **Laporan statistik** per matakuliah
- **Export backup** ke JSON

---

## 2. Arsitektur Sistem (3-Tier)

SiDigital menggunakan arsitektur 3 lapisan:

```
+------------------------------------------+
|  PRESENTATION LAYER (04_main.py)          |
|  Demo CLI -- menampilkan output program   |
+------------------------------------------+
              |
              v
+------------------------------------------+
|  SERVICE LAYER (03_services.py)           |
|  SiDigitalService -- business logic       |
|  - daftar_mahasiswa()                     |
|  - input_nilai()                          |
|  - get_transkrip()                        |
|  - get_statistik_mk()                     |
|  - export_backup()                        |
+------------------------------------------+
              |
              v
+------------------------------------------+
|  DATA LAYER (02_repositories.py)          |
|  BaseRepository                           |
|  MahasiswaRepository, DosenRepository     |
|  MataKuliahRepository, NilaiRepository   |
+------------------------------------------+
              |
              v
+------------------------------------------+
|  STORAGE                                  |
|  sidigital.db  (SQLite)                   |
|  sidigital_backup.json (JSON export)      |
+------------------------------------------+
```

---

## 3. Model Data

### Entitas Utama

**Mahasiswa**
- `nim` (str) — Nomor Induk Mahasiswa, minimal 6 karakter
- `nama` (str) — Nama lengkap
- `angkatan` (int) — Tahun masuk
- `program_studi` (str) — Nama program studi

**Dosen**
- `nip` (str) — Nomor Induk Pegawai
- `nama` (str) — Nama lengkap
- `gelar` (str) — Gelar akademik (Prof., Dr., dst.)

**MataKuliah**
- `kode` (str) — Kode unik matakuliah
- `nama` (str) — Nama matakuliah
- `sks` (int) — Satuan kredit semester (1-6)
- `semester` (int) — Semester yang disarankan (1-8)

**Nilai**
- `nim` (str) — Referensi ke Mahasiswa
- `kode_mk` (str) — Referensi ke MataKuliah
- `nip_dosen` (str) — Referensi ke Dosen pengampu
- `nilai_angka` (float) — Nilai 0-100

### Konversi Grade

| Nilai Angka | Grade | Bobot |
|-------------|-------|-------|
| 80 - 100    | A     | 4.0   |
| 70 - 79     | B     | 3.0   |
| 60 - 69     | C     | 2.0   |
| 50 - 59     | D     | 1.0   |
| 0 - 49      | E     | 0.0   |

### Rumus IPK

$$\text{IPK} = \frac{\sum (\text{Bobot Grade} \times \text{SKS})}{\sum \text{SKS}}$$

---

## 4. Konsep OOP yang Diterapkan

| Konsep | Digunakan Di |
|--------|-------------|
| Class & Object (M2) | Semua model dan repository |
| Encapsulation (M4) | `_get_conn()`, `_batas_lulus`, private state |
| Inheritance (M6) | `BaseRepository` diwarisi semua repo |
| Polymorphism (M7) | `_create_table()` dan `insert()` di-override tiap subclass Repository |
| Magic Methods (M9) | `__repr__`, `__post_init__` di @dataclass |
| Exception Handling (M10) | Hierarki `SiDigitalError` + try/except |
| SOLID - SRP (M11) | Tiap repository 1 tanggung jawab |
| SOLID - DIP (M11) | Service bergantung pada abstraksi repo |
| Design Pattern (M12) | Repository Pattern (structural) |
| @dataclass (M13) | Semua model menggunakan @dataclass |
| Type Hints (M13) | Seluruh kode menggunakan type hints |
| JSON persistence (M14) | `export_backup()` ke JSON |
| SQLite ORM (M14) | Repository layer dengan sqlite3 |

---

## 5. Hierarki Exception

```
Exception
  └── SiDigitalError             (base semua error SiDigital)
        ├── MahasiswaTidakValid  (nim tidak valid, dll)
        ├── MahasiswaTidakDitemukan
        ├── DosenTidakDitemukan
        ├── MataKuliahTidakValid (sks di luar range, dll)
        ├── MataKuliahTidakDitemukan
        └── NilaiTidakValid      (nilai di luar 0-100)
```

---

## 6. Panduan Implementasi

### Langkah 1: Models (01_models.py)
Mulai dari definisi @dataclass dan custom exceptions. Pastikan:
- `__post_init__` untuk validasi
- `get_grade()` dan `get_bobot()` di Nilai
- `nama_lengkap()` di Dosen

### Langkah 2: Repositories (02_repositories.py)
Buat BaseRepository lalu extend untuk masing-masing entitas. Pastikan:
- `_create_table()` di setiap `__init__`
- Semua query menggunakan parameterized (`?`)
- `conn.row_factory = sqlite3.Row` untuk dict-like access

### Langkah 3: Service Layer (03_services.py)
Buat `SiDigitalService` yang menggunakan semua repository. Service harus:
- Raise exception jika entitas tidak ditemukan
- Hitung IPK dengan rumus bobot x SKS
- Export ke JSON menggunakan `asdict()`

### Langkah 4: Integrasi (04_main.py)
Jalankan demo lengkap:
- Populate data awal
- Demonstrasikan semua fitur
- Cetak laporan

---

## 7. Rubrik Penilaian Proyek Mandiri

| Komponen | Bobot | Kriteria |
|----------|-------|---------|
| Models dengan validasi | 20% | @dataclass, __post_init__, type hints |
| Repository Pattern | 20% | BaseRepository, CRUD, parameterized query |
| Service Layer | 20% | Business logic, exception handling |
| Fitur Transkrip & IPK | 15% | Hitung IPK dengan bobot SKS |
| Export JSON | 10% | Backup data ke JSON dengan asdict() |
| Clean Code | 15% | Naming, docstrings, cleanup, no hardcode |

---

## 8. Referensi

- Materi 02: Kelas dan Objek
- Materi 04: Enkapsulasi
- Materi 06: Pewarisan
- Materi 10: Exception Handling OOP
- Materi 11: Prinsip SOLID
- Materi 12: Design Pattern Dasar
- Materi 13: OOP Modern Python
- Materi 14: OOP + File & Database
