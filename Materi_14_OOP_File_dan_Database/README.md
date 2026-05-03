# Materi 14 -- OOP + File & Database

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menyimpan dan membaca objects ke/dari file JSON
2. Menggunakan `dataclasses.asdict()` untuk serialisasi @dataclass
3. Menyimpan dan memuat Python objects dengan Pickle
4. Membuat database SQLite dengan sqlite3
5. Mengimplementasikan Repository Pattern untuk abstraksi database
6. Menerapkan CRUD (Create, Read, Update, Delete) dengan OOP

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| JSON | Simpan/baca data ke file teks, universal format |
| asdict() | Konversi @dataclass ke dict untuk JSON |
| Pickle | Serialisasi Python objects ke file biner |
| SQLite | Database ringan satu file, tidak perlu server |
| Repository Pattern | Abstraksi layer database dari logic bisnis |
| CRUD | Create, Read, Update, Delete dengan OOP |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_json_oop.py` | JSON serialisasi dengan @dataclass |
| `kode/02_pickle_oop.py` | Pickle serialisasi Python objects |
| `kode/03_sqlite_oop.py` | SQLite CRUD dengan Repository Pattern |
| `kode/04_studi_kasus.py` | Sistem akademik dengan file persistence |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) -- pahami JSON, Pickle, SQLite
2. Jalankan `01_json_oop.py` -- JSON serialisasi
3. Jalankan `02_pickle_oop.py` -- Pickle untuk objects
4. Jalankan `03_sqlite_oop.py` -- SQLite + Repository Pattern
5. Jalankan `04_studi_kasus.py` -- sistem dengan persistensi penuh
6. Kerjakan `latihan.py` -- implementasikan sendiri

---

## Checklist Pemahaman

Sebelum lanjut ke Proyek Akhir, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan JSON dan Pickle?
- [ ] Kapan gunakan JSON vs Pickle?
- [ ] Bagaimana cara konversi @dataclass ke JSON?
- [ ] Apa itu parameterized query dan mengapa penting?
- [ ] Apa itu Repository Pattern?
- [ ] Bagaimana implementasi CRUD dengan sqlite3?
- [ ] Mengapa harus gunakan `with` statement saat buka file?
- [ ] Apa bahaya SQL injection?

---

## Tips Praktis

### Cek file JSON yang dibuat

```python
import json

with open("data.json", "r") as f:
    data = json.load(f)
    print(json.dumps(data, indent=2, ensure_ascii=False))
```

### Lihat isi database SQLite

```python
import sqlite3

conn = sqlite3.connect("akademik.db")
for row in conn.execute("SELECT * FROM mahasiswa"):
    print(row)
conn.close()
```

### Hapus file test setelah selesai

```python
import os

if os.path.exists("test.db"):
    os.remove("test.db")
```
