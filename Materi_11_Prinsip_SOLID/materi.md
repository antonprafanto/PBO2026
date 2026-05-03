# Materi 11 — Prinsip SOLID

---

## 1. Apa Itu SOLID?

**SOLID** adalah singkatan dari lima prinsip desain yang membantu kita menulis kode yang:

- **Lebih mudah dipahami** — nama dan tanggung jawab jelas
- **Lebih mudah diubah** — minimal side-effect saat refactor
- **Lebih mudah diuji** — kelas kecil, focused, testable
- **Lebih mudah dikembangkan** — API stabil, extensible

Prinsip ini universal untuk OOP, tapi di sini kita fokus pada **Python**.

> *"SOLID bukan tentang menulis code yang perfect — tapi tentang menulis code yang sustainable."*

---

## 2. S — Single Responsibility Principle (SRP)

**Satu kelas harus punya satu alasan untuk berubah.**

Atau: *"Kelas harus punya satu tanggung jawab utama."*

### Anti-Pattern: Godly Class

```python
# [JELEK] Satu kelas melakukan segalanya
class Mahasiswa:
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk
    
    def hitung_uks(self):              # Tanggung jawab 1: menghitung UKS
        return self.ipk * 4
    
    def kirim_email_nilai(self):       # Tanggung jawab 2: mengirim email
        # ... SMTP connection logic ...
        pass
    
    def cetak_transkrip(self):         # Tanggung jawab 3: cetak dokumen
        # ... PDF generation logic ...
        pass
    
    def simpan_ke_database(self):      # Tanggung jawab 4: database
        # ... SQL logic ...
        pass
```

**Masalah:**
- Perubahan logic email memaksa test ulang seluruh Mahasiswa class
- Sulit reuse data Mahasiswa di context berbeda (tanpa email/database)
- Class terlalu besar, sulit dipahami

### Pattern: Separation of Concerns

```python
# [BAIK] Pisahkan tanggung jawab
class Mahasiswa:
    """Representasi data mahasiswa saja."""
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk
    
    def hitung_uks(self):
        return self.ipk * 4

class PenghitungAkademik:
    """Logika perhitungan akademik."""
    @staticmethod
    def validasi_ipk(ipk):
        if not (0.0 <= ipk <= 4.0):
            raise ValueError(f"IPK tidak valid: {ipk}")
        return True

class PengirimEmail:
    """Tanggung jawab mengirim email."""
    def kirim_nilai(self, mahasiswa, nilai):
        # ... SMTP logic ...
        pass

class PencetakDokumen:
    """Tanggung jawab cetak dokumen."""
    def cetak_transkrip(self, mahasiswa):
        # ... PDF logic ...
        pass

class RepositoriMahasiswa:
    """Tanggung jawab database."""
    def simpan(self, mahasiswa):
        # ... SQL logic ...
        pass
```

**Keuntungan:**
- Setiap class punya satu alasan untuk berubah
- Mudah test: PengirimEmail bisa ditest tanpa Mahasiswa class
- Mudah reuse: PenghitungAkademik bisa digunakan di mana saja

---

## 3. O — Open/Closed Principle (OCP)

**Kelas harus open untuk extension, closed untuk modification.**

Atau: *"Tambah fitur dengan inheritance/composition, bukan dengan mengubah kode lama."*

### Anti-Pattern: Modification-Heavy

```python
# [JELEK] Setiap tipe baru, ubah method yang ada
class KalkulatorNilai:
    def hitung(self, nilai, tipe_mahasiswa):
        if tipe_mahasiswa == "reguler":
            return nilai * 1.0
        elif tipe_mahasiswa == "beasiswa":
            return nilai * 1.2   # bonus untuk beasiswa
        elif tipe_mahasiswa == "bidikmisi":
            return nilai * 1.15  # bonus berbeda
        elif tipe_mahasiswa == "afirmasi":
            return nilai * 1.25  # bonus lagi
        # Setiap tipe baru = ubah method ini!
```

### Pattern: Polymorphism + Inheritance

```python
# [BAIK] Extend tanpa ubah kode lama
class StrategiPerhitungan:
    """Base class (interface) untuk strategi perhitungan."""
    def hitung(self, nilai):
        raise NotImplementedError

class StrategiReguler(StrategiPerhitungan):
    """Strategi untuk mahasiswa reguler."""
    def hitung(self, nilai):
        return nilai * 1.0

class StrategiBeasiswa(StrategiPerhitungan):
    """Strategi untuk mahasiswa beasiswa."""
    def hitung(self, nilai):
        return nilai * 1.2

class StrategiBidikmisi(StrategiPerhitungan):
    """Strategi untuk mahasiswa bidikmisi."""
    def hitung(self, nilai):
        return nilai * 1.15

class StrategiAfirmasi(StrategiPerhitungan):
    """Strategi untuk mahasiswa afirmasi."""
    def hitung(self, nilai):
        return nilai * 1.25

class KalkulatorNilai:
    def __init__(self, strategi):
        self.strategi = strategi
    
    def hitung(self, nilai):
        """Satu method, tidak perlu ubah."""
        return self.strategi.hitung(nilai)

# Penggunaan
kalkulasi = KalkulatorNilai(StrategiBeasiswa())
hasil = kalkulasi.hitung(85)   # 85 * 1.2 = 102
```

**Keuntungan:**
- Tambah tipe baru tanpa ubah KalkulatorNilai
- Kode lama tetap stabil
- Testing lebih mudah (mock strategy)

---

## 4. L — Liskov Substitution Principle (LSP)

**Subclass harus bisa menggantikan parent class tanpa error.**

Atau: *"Jangan breakkan kontrak parent class di subclass."*

### Anti-Pattern: Broken Contract

```python
# [JELEK] Bird class dan subclass-nya
class Burung:
    """Burung bisa terbang."""
    def terbang(self):
        return "Terbang tinggi ke langit"

class BurungCarah(Burung):
    """Burung carah (burung unta) tidak bisa terbang."""
    def terbang(self):
        raise NotImplementedError("Burung carah tidak bisa terbang!")

# Problem: kode yang expect Burung akan error jika dapat BurungCarah
def simulasi(burung: Burung):
    print(burung.terbang())   # CRASH jika burung = BurungCarah()
```

### Pattern: Proper Hierarchy

```python
# [BAIK] Hierarki yang menghormati kontrak
class Burung:
    """Base class untuk semua burung."""
    def bernyanyi(self):
        raise NotImplementedError

class BurungTerbang(Burung):
    """Burung yang bisa terbang."""
    def terbang(self):
        raise NotImplementedError

class BurungPipit(BurungTerbang):
    """Pipit — bisa terbang dan bernyanyi."""
    def terbang(self):
        return "Terbang gesit"
    
    def bernyanyi(self):
        return "Cuit cuit cuit"

class BurungCarah(Burung):
    """Burung carah — hanya bisa bernyanyi."""
    def bernyanyi(self):
        return "Dengusan kasar"

# Sekarang aman: BurungCarah tidak claim bisa terbang
def simulasi_terbang(burung: BurungTerbang):
    """Hanya terima BurungTerbang, tidak akan dapat BurungCarah."""
    print(burung.terbang())
```

**Keuntungan:**
- Subclass dapat diandalkan di tempat parent diharapkan
- Tidak ada surprise exception
- Kontrak jelas, hierarchy sound

---

## 5. I — Interface Segregation Principle (ISP)

**Client tidak harus depend pada interface yang tidak digunakan.**

Atau: *"Pisahkan interface besar menjadi yang kecil dan specific."*

### Anti-Pattern: Fat Interface

```python
# [JELEK] Interface raksasa
class PekerjaAkademik:
    """Semua orang akademik harus implement SEMUA ini."""
    def mengajar(self):
        raise NotImplementedError
    
    def meneliti(self):
        raise NotImplementedError
    
    def administrasi(self):
        raise NotImplementedError
    
    def mentoring(self):
        raise NotImplementedError
    
    def presentasi_internasional(self):
        raise NotImplementedError

class DosenPenuh(PekerjaAkademik):
    """Dosen penuh harus implement semua."""
    def mengajar(self): ...
    def meneliti(self): ...
    def administrasi(self): ...
    def mentoring(self): ...
    def presentasi_internasional(self): ...

class Asisten(PekerjaAkademik):
    """Asisten paksa implement semua, meskipun tidak semua applicable."""
    def mengajar(self): raise NotImplementedError("Asisten tidak mengajar")
    def meneliti(self): ...
    def administrasi(self): ...
    def mentoring(self): raise NotImplementedError("Asisten tidak mentoring")
    def presentasi_internasional(self): raise NotImplementedError("Asisten tidak presentasi internasional")
```

### Pattern: Segregated Interfaces

```python
# [BAIK] Interface kecil dan focused
class Pengajar:
    """Hanya untuk yang bisa mengajar."""
    def mengajar(self):
        raise NotImplementedError

class Peneliti:
    """Hanya untuk yang melakukan riset."""
    def meneliti(self):
        raise NotImplementedError

class Administrator:
    """Hanya untuk yang menangani administrasi."""
    def administrasi(self):
        raise NotImplementedError

class Mentor:
    """Hanya untuk yang membimbing."""
    def mentoring(self):
        raise NotImplementedError

class Presenter:
    """Hanya untuk yang presentasi."""
    def presentasi(self):
        raise NotImplementedError

# Sekarang fleksibel
class DosenPenuh(Pengajar, Peneliti, Administrator, Mentor, Presenter):
    """Dosen penuh — kembali semua."""
    def mengajar(self): ...
    def meneliti(self): ...
    def administrasi(self): ...
    def mentoring(self): ...
    def presentasi(self): ...

class Asisten(Peneliti, Administrator):
    """Asisten — hanya research & admin."""
    def meneliti(self): ...
    def administrasi(self): ...

class Dosen Adjaran(Pengajar):
    """Dosen adjaran — hanya mengajar."""
    def mengajar(self): ...
```

**Keuntungan:**
- Setiap class implement hanya interface yang relevan
- Tidak ada NotImplementedError yang artificial
- API lebih jelas dan focused

---

## 6. D — Dependency Inversion Principle (DIP)

**Bergantung pada abstraksi, bukan pada konkret.**

Atau: *"Inject dependency, jangan hardcode."*

### Anti-Pattern: Tight Coupling

```python
# [JELEK] Kelas langsung depend pada konkret
class RepositoriMahasiswaSQLite:
    """Database konkret — SQLite."""
    def ambil(self, nim):
        # SQL query langsung
        pass

class SistemAkademik:
    """Langsung depend pada SQLite — tidak fleksibel."""
    def __init__(self):
        self.repo = RepositoriMahasiswaSQLite()  # Hardcoded!
    
    def cari_mahasiswa(self, nim):
        return self.repo.ambil(nim)

# Masalah: jika mau ganti SQLite ke PostgreSQL, harus ubah SistemAkademik
```

### Pattern: Dependency Injection

```python
# [BAIK] Depend pada abstraksi
class RepositoriMahasiswa:
    """Abstraksi — interface saja."""
    def ambil(self, nim):
        raise NotImplementedError

class RepositoriMahasiswaSQLite(RepositoriMahasiswa):
    """Konkret — SQLite."""
    def ambil(self, nim):
        # SQLite query
        pass

class RepositoriMahasiswaPostgreSQL(RepositoriMahasiswa):
    """Konkret — PostgreSQL."""
    def ambil(self, nim):
        # PostgreSQL query
        pass

class RepositoriMahasiswaAPI(RepositoriMahasiswa):
    """Konkret — REST API."""
    def ambil(self, nim):
        # HTTP request
        pass

class SistemAkademik:
    """Depend pada abstraksi, tidak pada konkret."""
    def __init__(self, repo: RepositoriMahasiswa):
        self.repo = repo   # Inject dependency!
    
    def cari_mahasiswa(self, nim):
        return self.repo.ambil(nim)

# Penggunaan — flexible!
sistem1 = SistemAkademik(RepositoriMahasiswaSQLite())
sistem2 = SistemAkademik(RepositoriMahasiswaPostgreSQL())
sistem3 = SistemAkademik(RepositoriMahasiswaAPI())
# Semua berfungsi, tanpa ubah SistemAkademik
```

**Keuntungan:**
- Mudah ganti implementasi (testing, production)
- Loose coupling — lebih flexible
- Mudah test dengan mock object

---

## 7. Kombinasi SOLID

| Prinsip | Fokus | Keuntungan |
|---------|-------|-----------|
| **SRP** | Satu tanggung jawab per kelas | Mudah test, mudah reuse |
| **OCP** | Extend, jangan modify | Kode lama aman, fitur baru clean |
| **LSP** | Subclass menghormati kontrak | Hierarki sound, substitutable |
| **ISP** | Interface kecil dan focused | Tidak ada dummy implementation |
| **DIP** | Bergantung pada abstraksi | Flexible, decoupled, testable |

**Bersama-sama:**
- SRP + OCP = kelas kecil dan extensible
- LSP + DIP = kelas dapat disubstitusi dan di-inject
- ISP = kelas punya interface yang jelas
- **Hasil:** Code yang maintainable, sustainable, professional

---

## 8. Anti-Pattern vs Pattern Ringkas

### SRP
```
[X] Satu class melakukan banyak hal
[O] Satu class, satu tanggung jawab
```

### OCP
```
[X] Ubah kode lama saat tambah fitur baru
[O] Extend dengan subclass/strategy, jangan modify
```

### LSP
```
[X] Subclass break kontrak parent
[O] Subclass extend, tidak break
```

### ISP
```
[X] Implement semua method di interface, meskipun tidak digunakan
[O] Hanya implement method yang relevan
```

### DIP
```
[X] Hardcode dependency konkret
[O] Inject dependency abstrak
```

---

## 9. Tips Implementasi SOLID di Python

### Gunakan ABC (Abstract Base Classes)

```python
from abc import ABC, abstractmethod

class RepositoriMahasiswa(ABC):
    """Interface menggunakan ABC."""
    @abstractmethod
    def ambil(self, nim):
        pass
```

### Type Hints untuk Dokumentasi

```python
def cari_mahasiswa(self, repo: RepositoriMahasiswa) -> Mahasiswa:
    """Type hint mengkomunikasikan dependency."""
    return repo.ambil("2301001")
```

### Composition over Inheritance

```python
# [KURANG BAIK] Deep inheritance
class StaffAdministrasi(Pegawai):
    pass

class DosenStaffAd(StaffAdministrasi):
    pass

# [LEBIH BAIK] Composition
class Dosen:
    def __init__(self, pegawai: Pegawai, role: Role):
        self.pegawai = pegawai
        self.role = role   # Flexible: bisa Role.Pengajar, Role.Peneliti, dll
```

---

## 10. Cara Mendeteksi Kode yang Melanggar SOLID

### SRP Violation — Tanda-tanda:
- **Nama kelas panjang/kompleks** — Mahasiswa + Email + Dokumen + Database = god class
- **Method yang tidak related** — kelas punya method untuk berbagai domain
- **Test sulit untuk satu aspek** — harus setup seluruh class hanya untuk test satu method
- **Alasan perubahan banyak** — perubahan di bisnis logic, email logic, database logic semua di class yang sama

### OCP Violation — Tanda-tanda:
- **if-elif-elif-elif chains** — switch/case statement untuk setiap tipe baru
- **Magic strings/enums** — `if tipe == "reguler" elif tipe == "beasiswa" ...`
- **Kode harus dimodify untuk tambah fitur** — perubahan kode yang sudah tested
- **Duplicate logic** — kode serupa di banyak tempat

### LSP Violation — Tanda-tanda:
- **NotImplementedError di subclass** — subclass raise exception untuk method dari parent
- **Type checking dalam function** — `if isinstance(obj, SubclassA)` untuk handle case berbeda
- **Unexpected behavior** — subclass berperilaku berbeda dari janji parent

### ISP Violation — Tanda-tanda:
- **Dummy implementations** — subclass implement method dengan `pass` atau raise error
- **Banyak interface yang tidak digunakan** — class implement interface tapi pakai hanya 1-2 method
- **"Forced compliance"** — client dipaksa depend pada interface yang tidak perlu

### DIP Violation — Tanda-tanda:
- **Hardcoded dependencies** — `self.db = DatabaseSQLite()` di dalam __init__
- **Coupling ke concrete class** — `new RepositoriMahasiswaSQLite()` tersebar di kode
- **Sulit test dengan mock** — tidak bisa inject fake database untuk testing
- **Sulit ganti implementasi** — perubahan database perlu ubah banyak kode

### Checklist Refactoring:
- [ ] Apakah satu class punya banyak alasan untuk berubah? (SRP)
- [ ] Apakah ada if-elif chains untuk tipe-tipe? (OCP)
- [ ] Apakah subclass break kontrak parent? (LSP)
- [ ] Apakah semua method interface digunakan semua client? (ISP)
- [ ] Apakah dependency hardcoded atau di-inject? (DIP)

---

## 11. Referensi

- Clean Code — Robert C. Martin (Bab 10)
- Design Patterns: Elements of Reusable Object-Oriented Software — Gang of Four
- SOLID Principles in Python — Medium, blogs berbagai
- Python ABC (Abstract Base Classes) — Official docs
