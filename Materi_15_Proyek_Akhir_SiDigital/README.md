# Materi 15 -- Proyek Akhir: SiDigital

## Tujuan Pembelajaran

Setelah menyelesaikan proyek ini, mahasiswa mampu:

1. Merancang sistem OOP dari nol dengan arsitektur 3-tier
2. Mengimplementasikan Repository Pattern dengan SQLite
3. Membangun Service Layer dengan business logic
4. Menerapkan hierarki custom Exception
5. Mengintegrasikan JSON persistence sebagai backup
6. Menerapkan seluruh prinsip OOP (encapsulation, inheritance, polymorphism)

---

## Ringkasan Proyek

**SiDigital** adalah Sistem Informasi Kampus Digital yang mengintegrasikan semua konsep OOP Materi 1-14.

| Lapisan | File | Deskripsi |
|---------|------|-----------|
| Models + Exceptions | `kode/01_models.py` | @dataclass, validasi, custom error |
| Repository Layer | `kode/02_repositories.py` | CRUD SQLite, BaseRepository |
| Service Layer | `kode/03_services.py` | Business logic, transkrip, statistik |
| Aplikasi Lengkap | `kode/04_main.py` | Demo penuh SiDigital |
| Proyek Mandiri | `kode/latihan.py` | Pengembangan fitur lanjutan |

---

## Urutan Belajar

1. Baca [materi.md](./materi.md) -- arsitektur & model data
2. Jalankan `01_models.py` -- pahami models dan exceptions
3. Jalankan `02_repositories.py` -- Repository Pattern + SQLite
4. Jalankan `03_services.py` -- Service Layer + business logic
5. Jalankan `04_main.py` -- sistem terintegrasi penuh
6. Kerjakan `latihan.py` -- kembangkan fitur mandiri

---

## Checklist Pemahaman

- [ ] Bisa menjelaskan fungsi tiap lapisan (Model, Repo, Service)?
- [ ] Mengapa BaseRepository digunakan?
- [ ] Apa bedanya `insert()` di Repository vs `daftar_mahasiswa()` di Service?
- [ ] Bagaimana cara hitung IPK dengan bobot SKS?
- [ ] Kapan raise `MahasiswaTidakDitemukan` vs return `None`?
- [ ] Mengapa parameterized query wajib di SQLite?
- [ ] Bagaimana cara export seluruh data ke JSON backup?

---

## Cara Menjalankan

```bash
cd Materi_15_Proyek_Akhir_SiDigital/kode
python 01_models.py
python 02_repositories.py
python 03_services.py
python 04_main.py
```

---

## Struktur File

```
Materi_15_Proyek_Akhir_SiDigital/
├── materi.md          -- Project spec, arsitektur, rubrik
├── README.md          -- Panduan ini
└── kode/
    ├── 01_models.py          -- @dataclass + custom exceptions
    ├── 02_repositories.py    -- Repository layer (SQLite CRUD)
    ├── 03_services.py        -- Service layer (business logic)
    ├── 04_main.py            -- Aplikasi SiDigital lengkap
    └── latihan.py            -- Soal pengembangan mandiri
```
