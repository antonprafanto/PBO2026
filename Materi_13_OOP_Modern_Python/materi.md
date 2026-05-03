# Materi 13 -- OOP Modern Python

---

## 1. Python Modern Features untuk OOP

**Python terus berkembang** dengan fitur-fitur baru yang membuat OOP lebih efficient dan clean. Di materi ini fokus pada 3 fitur modern utama:

1. **@dataclass** — Otomatis generate `__init__`, `__repr__`, `__eq__`
2. **Type Hints** — Dokumentasi tipe yang checked oleh IDE dan type checkers
3. **__slots__** — Optimasi memory usage untuk classes dengan banyak instances

### Kenapa Penting?

- **@dataclass**: Mengurangi boilerplate code untuk simple data classes
- **Type Hints**: Catch errors early, better IDE support, self-documenting
- **__slots__**: Significant memory saving (40-80% tergantung jumlah attributes)

---

## 2. @dataclass Decorator

**@dataclass** adalah decorator dari modul `dataclasses` yang otomatis generate common magic methods.

### Tanpa @dataclass (Jelek)

```python
class Mahasiswa:
    def __init__(self, nim, nama, angkatan):
        self.nim = nim
        self.nama = nama
        self.angkatan = angkatan
    
    def __repr__(self):
        return f"Mahasiswa(nim={self.nim}, nama={self.nama}, angkatan={self.angkatan})"
    
    def __eq__(self, other):
        if not isinstance(other, Mahasiswa):
            return False
        return self.nim == other.nim and self.nama == other.nama and self.angkatan == other.angkatan
```

**Banyak boilerplate!** Harus menulis `__init__`, `__repr__`, `__eq__` manual.

### Dengan @dataclass (Baik)

```python
from dataclasses import dataclass

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    angkatan: int

# Automatic __init__, __repr__, __eq__ di-generate!
mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
print(mhs)  # Mahasiswa(nim='2301001', nama='Budi Santoso', angkatan=2023)
```

**Much cleaner!** Hanya perlu declare fields dengan type hints, sisanya otomatis.

### @dataclass Advanced Features

```python
from dataclasses import dataclass, field
from typing import List

@dataclass
class MataKuliah:
    kode: str
    nama: str
    sks: int
    prerequisite: List[str] = field(default_factory=list)
    semester: int = 1

@dataclass(frozen=True)  # Immutable dataclass
class NilaiImmutable:
    mahasiswa_nim: str
    kode_mk: str
    nilai: float

@dataclass(order=True)  # Support comparison operators
class NilaiOrdered:
    nilai: float
    nim: str
```

### Keuntungan @dataclass

1. **Less boilerplate** — Tidak perlu menulis `__init__`, `__repr__`, `__eq__`
2. **Type-safe** — Type hints built-in, IDE bisa provide autocomplete
3. **Immutable option** — `frozen=True` untuk immutable dataclasses
4. **Ordering support** — `order=True` untuk comparison operators
5. **Default values** — Support default values dan default factories
6. **Field customization** — `field()` untuk advanced customization

---

## 3. Type Hints Comprehensive

**Type hints** memberitahu IDE dan type checkers tentang tipe dari variables, parameters, dan return values.

### Basic Type Hints

```python
def input_nilai(nim: str, nilai: float) -> bool:
    """Input nilai untuk mahasiswa."""
    return 0 <= nilai <= 100

def hitung_total(nilai1: float, nilai2: float, nilai3: float) -> float:
    return nilai1 + nilai2 + nilai3
```

### Complex Type Hints

```python
from typing import List, Dict, Optional, Union, Tuple

# List of specific type
def get_nilai_list(nim: str) -> List[float]:
    return [80, 90, 85]

# Dictionary with key-value types
def get_nilai_dict(nim: str) -> Dict[str, float]:
    return {"IF201": 85, "IF202": 90}

# Optional (can be None)
def find_mahasiswa(nim: str) -> Optional[dict]:
    pass

# Union (multiple possible types)
def convert_nilai(nilai: Union[str, int, float]) -> float:
    return float(nilai)

# Tuple with fixed types
def get_info() -> Tuple[str, str, int]:
    return ("2301001", "Budi", 2023)
```

### Type Hints di Class

```python
from dataclasses import dataclass
from typing import Dict, List

@dataclass
class Mahasiswa:
    nim: str
    nama: str
    nilai_dict: Dict[str, float]
    
    def hitung_rata_rata(self) -> float:
        if not self.nilai_dict:
            return 0
        return sum(self.nilai_dict.values()) / len(self.nilai_dict)
    
    def get_nilai_list(self) -> List[float]:
        return list(self.nilai_dict.values())
```

### Type Checking dengan mypy

```bash
pip install mypy
mypy program.py
mypy --strict program.py
```

---

## 4. __slots__ untuk Memory Optimization

**__slots__** membatasi attributes yang bisa di-set pada object, menghemat memory signifikan.

### Tanpa __slots__

```python
class TanpaSlots:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

class DenganSlots:
    __slots__ = ('nim', 'nama')
    
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama

# Memory usage BENAR: harus tambahkan __dict__ untuk non-slots
import sys
obj1 = TanpaSlots("2301001", "Budi")
obj2 = DenganSlots("2301001", "Budi")

size1 = sys.getsizeof(obj1) + sys.getsizeof(obj1.__dict__)  # obj + __dict__
size2 = sys.getsizeof(obj2)  # hanya obj, tidak ada __dict__

print(f"Tanpa __slots__: {size1} bytes")
print(f"Dengan __slots__: {size2} bytes")
# Saving sekitar 40-80% tergantung jumlah attributes
```

### @dataclass + __slots__

```python
from dataclasses import dataclass

@dataclass
class Mahasiswa:
    __slots__ = ('nim', 'nama', 'angkatan')
    nim: str
    nama: str
    angkatan: int

# Combine benefits: @dataclass + memory optimization
```

### Keuntungan dan Trade-offs

**Keuntungan:**
- Memory efficiency hingga 80%
- Faster attribute access
- Attribute protection (can't add arbitrary attributes)

**Disadvantages:**
- Can't add dynamic attributes
- Inheritance dengan __slots__ bisa tricky
- Must declare all attributes upfront

---

## 5. Kombinasi: @dataclass + Type Hints + __slots__

**Best practice untuk modern Python OOP classes:**

```python
from dataclasses import dataclass
from typing import Dict, List, Optional

@dataclass
class Mahasiswa:
    __slots__ = ('nim', 'nama', 'angkatan', 'nilai_dict')
    
    nim: str
    nama: str
    angkatan: int
    nilai_dict: Dict[str, float] = None
    
    def __post_init__(self):
        if self.nilai_dict is None:
            self.nilai_dict = {}
    
    def input_nilai(self, kode_mk: str, nilai: float) -> None:
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai harus 0-100")
        self.nilai_dict[kode_mk] = nilai
    
    def hitung_rata_rata(self) -> float:
        if not self.nilai_dict:
            return 0
        return sum(self.nilai_dict.values()) / len(self.nilai_dict)
```

**Keuntungan kombinasi:**
- ✅ Clean code (@dataclass)
- ✅ Type-safe (Type Hints)
- ✅ Memory efficient (__slots__)
- ✅ IDE support
- ✅ Self-documenting

---

## 6. Best Practices

### 1. Gunakan @dataclass untuk data classes
```python
# Baik
@dataclass
class Mahasiswa:
    nim: str
    nama: str

# Jelek
class Mahasiswa:
    def __init__(self, nim, nama):
        self.nim = nim
        self.nama = nama
```

### 2. Selalu gunakan type hints
```python
# Baik
def hitung_rata_rata(nilai_list: List[float]) -> float:
    pass

# Jelek
def hitung_rata_rata(nilai_list):
    pass
```

### 3. Gunakan __slots__ untuk classes dengan banyak instances
```python
@dataclass
class Transaksi:
    __slots__ = ('id', 'nim', 'jumlah')
    id: str
    nim: str
    jumlah: float
```

### 4. Gunakan frozen=True untuk immutable data
```python
@dataclass(frozen=True)
class Nilai:
    nim: str
    kode_mk: str
    nilai: float
```

### 5. Validasi di __post_init__
```python
@dataclass
class Mahasiswa:
    nim: str
    angkatan: int
    
    def __post_init__(self):
        if len(self.nim) < 6:
            raise ValueError("NIM minimal 6 karakter")
```

---

## 7. Referensi

- PEP 557 -- Data Classes: https://peps.python.org/pep-0557/
- PEP 484 -- Type Hints: https://peps.python.org/pep-0484/
- Python dataclasses docs: https://docs.python.org/3/library/dataclasses.html
- mypy documentation: https://mypy.readthedocs.io/
