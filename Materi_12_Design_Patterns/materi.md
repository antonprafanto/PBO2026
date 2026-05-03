# Materi 12 -- Pola Desain (Design Patterns)

---

## 1. Apa Itu Design Patterns?

**Design patterns** adalah solusi umum dan terbukti untuk masalah yang sering muncul dalam software design.

Bukan code library, tapi **blueprint** atau **template** untuk struktur kode.

### Mengapa Design Patterns Penting?

- **Reusable solutions**: Jangan reinvent the wheel
- **Better communication**: Standar terminology di tim
- **Faster development**: Sudah proven, tinggal adapt
- **Maintainable code**: Pattern umum lebih mudah dimengerti
- **Production-ready**: Tested dan refined oleh jutaan developers

### Kategori Design Patterns

1. **Creational Patterns** -- cara buat objects
   - Singleton, Factory, Builder, Prototype
2. **Structural Patterns** -- bagaimana compose objects
   - Adapter, Decorator, Facade, Proxy
3. **Behavioral Patterns** -- interaksi antara objects
   - Observer, Strategy, Template Method, Iterator

Di materi ini, kami fokus pada 4 patterns yang paling umum dan praktis.

---

## 2. Singleton Pattern

**Problem**: Ada beberapa resource yang hanya boleh ada satu instance -- logger, database connection, configuration manager, queue.

```python
# [JELEK] Banyak instance database connection
class DatabaseConnection:
    def __init__(self):
        self.connection = "DB_CONNECTION_123"
        print(f"Creating connection: {self.connection}")

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()
# Problem: 3 connection instances! Inefficient, tapi seharusnya hanya 1.
```

**Solution**: Gunakan Singleton -- hanya satu instance yang pernah ada.

### Implementasi Class-based Singleton

```python
# [BAIK] Singleton dengan class variable + class method
class DatabaseConnection:
    """Hanya satu instance di seluruh aplikasi."""
    _instance = None
    
    def __new__(cls):
        """__new__ dipanggil sebelum __init__, untuk kontrol instantiation."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Creating first database connection...")
        return cls._instance
    
    def query(self, sql):
        return f"Executing: {sql}"

db1 = DatabaseConnection()
db2 = DatabaseConnection()
db3 = DatabaseConnection()
# Semua menunjuk ke instance yang sama!
assert db1 is db2 is db3  # True
```

**Keuntungan**:
- Hanya satu resource dipakai
- Lazy initialization (buat hanya saat pertama diakses)
- Thread-safe dengan proper implementation

**Kelemahan**:
- Global state (sulit untuk test)
- Hidden dependency (kode yang depend pada singleton tidak jelas terlihat)

### Implementasi Decorator Singleton

```python
# Alternative: Singleton sebagai decorator
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

log1 = Logger()
log2 = Logger()
# log1 is log2 -- True
```

---

## 3. Factory Pattern

**Problem**: Kode harus membuat objects berbeda tapi tergantung kondisi/type. Banyak if-elif untuk determine class mana yang dibuat.

```python
# [JELEK] Hardcode creation logic di mana-mana
class SistemNotifikasi:
    def kirim_notifikasi(self, tipe, pesan):
        if tipe == "email":
            notif = NotifikasiEmail()
        elif tipe == "sms":
            notif = NotifikasiSMS()
        elif tipe == "push":
            notif = NotifikasiPush()
        else:
            raise ValueError(f"Unknown type: {tipe}")
        notif.kirim(pesan)

# Di banyak tempat di kode, logic yang sama berulang!
# Sulit untuk maintenance jika ada tipe baru.
```

**Solution**: Gunakan Factory Pattern -- delegate object creation ke factory.

### Simple Factory

```python
# [BAIK] Centralized creation logic
class Notifikasi:
    def kirim(self, pesan):
        raise NotImplementedError

class NotifikasiEmail(Notifikasi):
    def kirim(self, pesan):
        return f"Email: {pesan}"

class NotifikasiSMS(Notifikasi):
    def kirim(self, pesan):
        return f"SMS: {pesan}"

class NotifikasiPush(Notifikasi):
    def kirim(self, pesan):
        return f"Push: {pesan}"

class NotifikasiFactory:
    """Factory untuk create Notifikasi objects."""
    @staticmethod
    def create(tipe):
        if tipe == "email":
            return NotifikasiEmail()
        elif tipe == "sms":
            return NotifikasiSMS()
        elif tipe == "push":
            return NotifikasiPush()
        else:
            raise ValueError(f"Unknown type: {tipe}")

# Penggunaan -- simple dan clean
notif = NotifikasiFactory.create("email")
notif.kirim("Hello!")
```

### Factory Method Pattern

```python
# [LEBIH BAIK] Flexible -- setiap subclass define factory method-nya sendiri
class NotifikasiProducer:
    """Base class dengan factory method."""
    def create_notifikasi(self):
        """Factory method -- subclass override ini."""
        raise NotImplementedError
    
    def kirim_dengan_retry(self, pesan):
        notif = self.create_notifikasi()
        for i in range(3):
            try:
                return notif.kirim(pesan)
            except Exception as e:
                if i == 2:
                    raise

class ProduserEmail(NotifikasiProducer):
    def create_notifikasi(self):
        return NotifikasiEmail()

class ProduserSMS(NotifikasiProducer):
    def create_notifikasi(self):
        return NotifikasiSMS()

# Penggunaan -- polymorphic
def send_to_user(producer: NotifikasiProducer, msg):
    producer.kirim_dengan_retry(msg)

send_to_user(ProduserEmail(), "Welcome!")
send_to_user(ProduserSMS(), "Verify OTP")
```

**Keuntungan Factory**:
- Decouples creation logic dari usage
- Mudah tambah tipe baru (just add new factory subclass)
- Follows Open/Closed Principle

---

## 4. Observer Pattern

**Problem**: Multiple objects perlu tahu ketika ada event terjadi. Coupling tinggi jika hard-code dependency.

```python
# [JELEK] Tight coupling -- sistem kampus hardcode notify siapa
class Mahasiswa:
    def update_nilai(self, nilai):
        self.nilai = nilai
        
        # Hardcode notify ke siapa aja
        orang_tua = OrangTua(self.nama)
        orang_tua.terima_laporan(nilai)  # Problem: Mahasiswa tahu OrangTua
        
        dosen = Dosen(self.nama)
        dosen.update_statistik(nilai)    # Problem: Mahasiswa tahu Dosen
        
        admin = AdminAkademik()
        admin.record_nilai(nilai)        # Problem: Mahasiswa tahu Admin
```

**Solution**: Observer Pattern -- decouple events dari handlers.

```python
# [BAIK] Event-driven architecture
class Subject:
    """Base class untuk object yang punya observers."""
    def __init__(self):
        self._observers = []
    
    def subscribe(self, observer):
        """Subscribe observer untuk events."""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def unsubscribe(self, observer):
        """Unsubscribe observer."""
        self._observers.remove(observer)
    
    def notify(self, event):
        """Notify semua observers tentang event."""
        for observer in self._observers:
            observer.update(event)

class Observer:
    """Base class untuk observer."""
    def update(self, event):
        raise NotImplementedError

class Mahasiswa(Subject):
    """Mahasiswa = Subject yang emit events."""
    def __init__(self, nim, nama):
        super().__init__()
        self.nim = nim
        self.nama = nama
        self.nilai = 0
    
    def update_nilai(self, nilai):
        self.nilai = nilai
        # Notify semua observers tentang nilai baru
        self.notify({
            "tipe": "nilai_diupdate",
            "nim": self.nim,
            "nama": self.nama,
            "nilai": nilai
        })

class OrangTuaObserver(Observer):
    """Observer -- menerima notifikasi nilai."""
    def __init__(self, nama):
        self.nama = nama
    
    def update(self, event):
        if event["tipe"] == "nilai_diupdate":
            print(f"OrangTua {self.nama}: Nilai {event['nama']} = {event['nilai']}")

class DosenObserver(Observer):
    """Observer -- track statistik kelas."""
    def update(self, event):
        if event["tipe"] == "nilai_diupdate":
            print(f"Dosen: Statistik update untuk {event['nim']}")

# Penggunaan
mhs = Mahasiswa("2301001", "Budi Santoso")
mhs.subscribe(OrangTuaObserver("Bapak Santoso"))
mhs.subscribe(DosenObserver())

mhs.update_nilai(85)  # Semua observers notified!
```

**Keuntungan Observer**:
- Decoupled: Mahasiswa tidak tahu siapa observernya
- Flexible: Bisa add/remove observers at runtime
- Event-driven: Natural untuk async systems

---

## 5. Decorator Pattern

**Problem**: Butuh tambah behavior ke object tanpa modify original class. Banyak kombinasi behavior = explosion of subclasses.

```python
# [JELEK] Inheritance explosion
class MataKuliahBase:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    def harga(self):
        return self.sks * 100_000

# Kalau mau add features (praktik, tugas, ujian, lab)
# Kombinasinya banyak!
class MataKuliahRegular(MataKuliahBase):
    pass

class MataKuliahDenganPraktik(MataKuliahBase):
    def harga(self):
        return super().harga() + 200_000

class MataKuliahDenganPraktikDanLab(MataKuliahBase):
    def harga(self):
        return super().harga() + 200_000 + 300_000

# Nightmare kombinatorial!
```

**Solution**: Decorator Pattern -- wrap object dengan behavior tanpa subclass.

```python
# [BAIK] Composition instead of inheritance
class MataKuliah:
    def __init__(self, nama, sks):
        self.nama = nama
        self.sks = sks
    
    def harga(self):
        return self.sks * 100_000
    
    def deskripsi(self):
        return f"{self.nama} ({self.sks} SKS)"

class MataKuliahDecorator(MataKuliah):
    """Base decorator -- wraps MataKuliah."""
    def __init__(self, matkul: MataKuliah):
        self.matkul = matkul
    
    def harga(self):
        return self.matkul.harga()
    
    def deskripsi(self):
        return self.matkul.deskripsi()

class DenganPraktik(MataKuliahDecorator):
    """Decorator -- add praktik."""
    def harga(self):
        return super().harga() + 200_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Praktik"

class DenganLab(MataKuliahDecorator):
    """Decorator -- add lab."""
    def harga(self):
        return super().harga() + 300_000
    
    def deskripsi(self):
        return f"{super().deskripsi()} + Lab"

# Penggunaan -- flexible combination!
mk = MataKuliah("Pemrograman Python", 3)
mk = DenganPraktik(mk)      # Add praktik
mk = DenganLab(mk)          # Add lab
print(mk.deskripsi())       # "Pemrograman Python (3 SKS) + Praktik + Lab"
print(f"Harga: Rp {mk.harga()}")  # 300000 + 200000 + 300000 = 800000
```

**Keuntungan Decorator**:
- Flexible: Bisa combine behaviors dinamis
- No inheritance explosion: Tidak perlu subclass untuk setiap kombinasi
- Single Responsibility: Setiap decorator punya satu tanggung jawab
- Runtime composition: Bisa construct objects at runtime

**Python Alternative: Using Functions**

```python
def dengan_praktik(harga_func):
    """Decorator function -- wrap harga calculation."""
    def wrapper():
        return harga_func() + 200_000
    return wrapper

@dengan_praktik
def harga_matakuliah():
    return 300_000

print(harga_matakuliah())  # 500000
```

---

## 6. Pola-Pola Lainnya

### Template Method Pattern

```python
class ProsesAkademik:
    """Define template -- subclass override specific steps."""
    def proses(self):
        self.validasi()
        self.eksekusi()
        self.laporan()
    
    def validasi(self):
        raise NotImplementedError
    
    def eksekusi(self):
        raise NotImplementedError
    
    def laporan(self):
        raise NotImplementedError
```

Sudah detailed di Materi 11 (OCP), tapi ini adalah classic behavioral pattern.

### Adapter Pattern

```python
# Old interface
class DatabaseLama:
    def get_data(self):
        return "Data lama format"

# New interface yang diharapkan kode baru
class DatabaseBaru:
    def fetch_data(self):
        raise NotImplementedError

# Adapter
class AdapterDatabaseLama(DatabaseBaru):
    def __init__(self, db_lama):
        self.db_lama = db_lama
    
    def fetch_data(self):
        return self.db_lama.get_data()
```

---

## 7. Kapan Gunakan Pattern Mana?

| Pattern | Gunakan Ketika | Keuntungan |
|---------|----------------|-----------|
| **Singleton** | Hanya 1 instance diperlukan (logger, config, DB) | Kontrol akses, shared state |
| **Factory** | Banyak tipe object, creation logic kompleks | Decoupling, extensible |
| **Observer** | Multiple objects perlu tahu tentang events | Event-driven, loosely coupled |
| **Decorator** | Tambah behavior dynamis ke objects | Flexible, no inheritance explosion |
| **Template Method** | Framework dengan customizable steps | Code reuse, inversion of control |

---

## 8. Anti-Patterns (Patterns to Avoid)

### God Object
```python
# [JELEK] Object yang melakukan semuanya
class SistemAkademik:
    def daftar_mahasiswa(self): ...
    def input_nilai(self): ...
    def kirim_notifikasi(self): ...
    def generate_laporan(self): ...
    def backup_database(self): ...
    # Nightmare to maintain!
```

### Leaky Abstraction
```python
# [JELEK] Abstraction yang expose internal details
class Database:
    def query(self, sql):  # SQL visible -- not abstracted
        # ...
        pass

# [BAIK] Hide implementation
class StudentRepository:
    def find_by_nim(self, nim):  # Simple, focused interface
        # ...
        pass
```

### Diamond Dependency
```python
# [JELEK] Complex inheritance
class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass  # Who's method to call?

# [BAIK] Use composition atau single inheritance
class D:
    def __init__(self, b: B, c: C):
        self.b = b
        self.c = c
```

---

## 9. Best Practices

1. **Don't over-engineer** -- gunakan pattern hanya ketika problem jelas
2. **Favor composition over inheritance** -- lebih flexible
3. **Keep patterns simple** -- jika pattern membuat kode lebih kompleks, skip it
4. **Learn from frameworks** -- Django, Flask, FastAPI punya patterns hidden
5. **Test your patterns** -- patterns harus testable

---

## 10. Referensi

- Design Patterns: Elements of Reusable Object-Oriented Software -- Gang of Four (the book)
- Head First Design Patterns -- Freeman & Robson (more accessible)
- Refactoring.Guru -- patterns dengan visual explanations
- Python Design Patterns -- various Python community sources
