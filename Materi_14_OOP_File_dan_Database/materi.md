# Materi 14 -- OOP + File & Database

---

## 1. Mengapa Perlu Persistensi Data?

Selama belajar OOP, semua data ada di **memory (RAM)** — ketika program selesai, data hilang. Untuk menyimpan data secara permanen diperlukan **persistensi**:

- **File JSON** — Format teks, mudah dibaca manusia, cocok untuk konfigurasi dan data sederhana
- **File Pickle** — Format biner Python, menyimpan objects secara utuh
- **SQLite** — Database relasional ringan, tidak perlu server, file tunggal `.db`

---

## 2. JSON dengan OOP

**JSON (JavaScript Object Notation)** adalah format data standar yang universal.

### Konsep Dasar

```python
import json

# Python dict -> JSON string
data = {"nim": "2301001", "nama": "Budi", "nilai": 85.5}
json_str = json.dumps(data, indent=2)

# JSON string -> Python dict
data_kembali = json.loads(json_str)
```

### Serialisasi @dataclass ke JSON

```python
import json
from dataclasses import dataclass, asdict

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    angkatan: int

mhs = Mahasiswa("2301001", "Budi Santoso", 2023)

# @dataclass -> dict -> JSON
data = asdict(mhs)
json_str = json.dumps(data, indent=2)

# JSON -> dict -> @dataclass
data_dict = json.loads(json_str)
mhs_baru = Mahasiswa(**data_dict)
```

### Simpan dan Baca File JSON

```python
# Simpan ke file
with open("mahasiswa.json", "w") as f:
    json.dump(data, f, indent=2)

# Baca dari file
with open("mahasiswa.json", "r") as f:
    data = json.load(f)
```

### Repository Pattern untuk JSON

```python
class MahasiswaRepository:
    def __init__(self, filepath: str):
        self.filepath = filepath
    
    def save_all(self, mahasiswa_list: list) -> None:
        data = [asdict(m) for m in mahasiswa_list]
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
    
    def load_all(self) -> list:
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            return [Mahasiswa(**d) for d in data]
        except FileNotFoundError:
            return []
```

---

## 3. Pickle dengan OOP

**Pickle** adalah modul Python untuk serialisasi objects ke format biner.

### Kapan Gunakan Pickle vs JSON?

| Aspek | JSON | Pickle |
|-------|------|--------|
| Format | Teks (human-readable) | Biner |
| Portabilitas | Universal (semua bahasa) | Python only |
| Tipe data | Basic types | Semua Python objects |
| Keamanan | Aman | **JANGAN** buka pickle tidak dipercaya |
| Kecepatan | Lebih lambat | Lebih cepat |

### Serialisasi Objects

```python
import pickle

class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

mhs = Mahasiswa("2301001", "Budi")

# Simpan ke file
with open("data.pkl", "wb") as f:
    pickle.dump(mhs, f)

# Baca dari file (object utuh)
with open("data.pkl", "rb") as f:
    mhs_baru = pickle.load(f)

print(mhs_baru.nim)   # 2301001
print(mhs_baru.nama)  # Budi
```

### Pickle Menyimpan State Penuh

```python
# Pickle bisa menyimpan list of objects
mahasiswa_list = [
    Mahasiswa("2301001", "Budi"),
    Mahasiswa("2301002", "Sari"),
]

with open("data.pkl", "wb") as f:
    pickle.dump(mahasiswa_list, f)

with open("data.pkl", "rb") as f:
    loaded = pickle.load(f)

# loaded adalah list of Mahasiswa objects
print(type(loaded[0]))  # <class 'Mahasiswa'>
```

---

## 4. SQLite dengan OOP

**SQLite** adalah database SQL yang tersimpan dalam satu file. Cocok untuk aplikasi desktop dan akademik.

### Konsep Dasar sqlite3

```python
import sqlite3

# Connect ke database (auto-create jika belum ada)
conn = sqlite3.connect("akademik.db")
cursor = conn.cursor()

# Buat tabel
cursor.execute("""
    CREATE TABLE IF NOT EXISTS mahasiswa (
        nim TEXT PRIMARY KEY,
        nama TEXT NOT NULL,
        angkatan INTEGER NOT NULL
    )
""")
conn.commit()

# Insert data
cursor.execute(
    "INSERT INTO mahasiswa VALUES (?, ?, ?)",
    ("2301001", "Budi Santoso", 2023)
)
conn.commit()

# Query data
cursor.execute("SELECT * FROM mahasiswa")
rows = cursor.fetchall()

conn.close()
```

### ORM-like Repository Pattern

```python
class MahasiswaDB:
    """Repository class untuk table mahasiswa."""
    
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_table()
    
    def _get_conn(self):
        return sqlite3.connect(self.db_path)
    
    def _init_table(self):
        with self._get_conn() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS mahasiswa (
                    nim TEXT PRIMARY KEY,
                    nama TEXT NOT NULL,
                    angkatan INTEGER NOT NULL
                )
            """)
    
    def insert(self, mahasiswa) -> bool:
        try:
            with self._get_conn() as conn:
                conn.execute(
                    "INSERT INTO mahasiswa VALUES (?, ?, ?)",
                    (mahasiswa.nim, mahasiswa.nama, mahasiswa.angkatan)
                )
            return True
        except sqlite3.IntegrityError:
            return False
    
    def find_by_nim(self, nim: str):
        with self._get_conn() as conn:
            row = conn.execute(
                "SELECT * FROM mahasiswa WHERE nim = ?", (nim,)
            ).fetchone()
        if row:
            return Mahasiswa(*row)
        return None
    
    def find_all(self):
        with self._get_conn() as conn:
            rows = conn.execute("SELECT * FROM mahasiswa").fetchall()
        return [Mahasiswa(*row) for row in rows]
    
    def delete(self, nim: str) -> bool:
        with self._get_conn() as conn:
            cursor = conn.execute(
                "DELETE FROM mahasiswa WHERE nim = ?", (nim,)
            )
        return cursor.rowcount > 0
```

### Keuntungan Repository Pattern

1. **Separation of concerns** — Logic database terpisah dari logic bisnis
2. **Testable** — Bisa mock repository untuk unit testing
3. **Swappable** — Ganti dari JSON ke SQLite tanpa ubah logic bisnis
4. **Reusable** — Repository bisa dipakai di berbagai tempat

---

## 5. Best Practices

### 1. Gunakan context manager (with)
```python
# Baik -- otomatis close
with open("data.json", "r") as f:
    data = json.load(f)

# Jelek -- bisa lupa close
f = open("data.json", "r")
data = json.load(f)
f.close()
```

### 2. Handle FileNotFoundError
```python
def load_data(filepath: str) -> list:
    try:
        with open(filepath, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []  # Return empty jika file belum ada
    except json.JSONDecodeError:
        return []  # Return empty jika file corrupt
```

### 3. Gunakan parameterized queries (hindari SQL injection)
```python
# Baik -- parameterized
cursor.execute("SELECT * FROM mhs WHERE nim = ?", (nim,))

# BAHAYA -- SQL injection
cursor.execute(f"SELECT * FROM mhs WHERE nim = '{nim}'")
```

### 4. Gunakan asdict() untuk @dataclass ke JSON
```python
from dataclasses import asdict
data = asdict(mahasiswa_obj)  # Konversi otomatis ke dict
```

---

## 6. Referensi

- Python json module: https://docs.python.org/3/library/json.html
- Python pickle module: https://docs.python.org/3/library/pickle.html
- Python sqlite3 module: https://docs.python.org/3/library/sqlite3.html
- dataclasses.asdict(): https://docs.python.org/3/library/dataclasses.html#dataclasses.asdict
