# Materi 13 -- OOP Modern Python

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menggunakan @dataclass decorator untuk mengurangi boilerplate code
2. Menulis comprehensive type hints untuk OOP classes
3. Menggunakan __slots__ untuk memory optimization
4. Mengkombinasikan @dataclass, type hints, dan __slots__ dalam production code
5. Melakukan validation dengan __post_init__
6. Menggunakan mypy untuk static type checking

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| @dataclass | Otomatis generate __init__, __repr__, __eq__, etc |
| Type Hints | Comprehensive typing untuk parameters dan return values |
| __slots__ | Memory optimization dengan attribute restrictions |
| Kombinasi | Best practice: @dataclass + Type Hints + __slots__ |
| Validation | __post_init__ untuk validate values |
| mypy | Static type checking untuk find bugs early |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_dataclass_basics.py` | @dataclass fundamentals dan advantages |
| `kode/02_type_hints_advanced.py` | Comprehensive type hints untuk OOP |
| `kode/03_slots_optimization.py` | __slots__ dan memory optimization |
| `kode/04_studi_kasus.py` | Sistem akademik dengan modern Python OOP |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) -- pahami @dataclass, type hints, __slots__
2. Jalankan `01_dataclass_basics.py` -- lihat @dataclass features
3. Jalankan `02_type_hints_advanced.py` -- pelajari comprehensive type hints
4. Jalankan `03_slots_optimization.py` -- kuasai __slots__ untuk memory saving
5. Jalankan `04_studi_kasus.py` -- integrasi semua features
6. Kerjakan `latihan.py` -- implementasikan modern OOP patterns

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 14, pastikan Anda bisa menjawab:

- [ ] Apa keuntungan @dataclass dibanding manual __init__?
- [ ] Apa yang di-generate otomatis oleh @dataclass?
- [ ] Bagaimana cara menulis comprehensive type hints?
- [ ] Apa itu __slots__ dan mengapa penting?
- [ ] Berapa persen memory saving dengan __slots__?
- [ ] Bagaimana combine @dataclass + type hints + __slots__?
- [ ] Bagaimana cara gunakan __post_init__ untuk validation?
- [ ] Apa bedanya frozen=True dengan default @dataclass?

---

## Tips Praktis

### Run Type Checking dengan mypy

```bash
# Install mypy
pip install mypy

# Check types untuk satu file
mypy program.py

# Strict mode (recommended)
mypy --strict program.py
```

### Memory Testing __slots__

```python
import sys

class TanpaSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class DenganSlots:
    __slots__ = ('x', 'y')
    def __init__(self, x, y):
        self.x = x
        self.y = y

obj1 = TanpaSlots(1, 2)
obj2 = DenganSlots(1, 2)

print(sys.getsizeof(obj1.__dict__))  # Without slots: ~144 bytes
print(sys.getsizeof(obj2))  # With slots: ~56 bytes
```
