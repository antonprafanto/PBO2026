# 📚 Referensi & Sumber Belajar PBO Python

## Buku Utama

1. **"Python 3 Object-Oriented Programming"** — Dusty Phillips (Packt Publishing)
   - Buku paling komprehensif tentang OOP Python
   
2. **"Clean Code"** — Robert C. Martin (Prentice Hall)
   - Panduan menulis kode yang bersih dan mudah dipelihara

3. **"Design Patterns: Elements of Reusable Object-Oriented Software"** — Gang of Four
   - Referensi klasik untuk design patterns

4. **"Fluent Python"** — Luciano Ramalho (O'Reilly)
   - Deep dive ke fitur Python termasuk magic methods & OOP lanjutan

---

## Dokumentasi Resmi

- 🔗 [Python Official Docs — Classes](https://docs.python.org/3/tutorial/classes.html)
- 🔗 [Python Official Docs — ABC Module](https://docs.python.org/3/library/abc.html)
- 🔗 [Python Official Docs — Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- 🔗 [Python Type Hints (PEP 484)](https://peps.python.org/pep-0484/)
- 🔗 [Python Dataclasses (PEP 557)](https://peps.python.org/pep-0557/)

---

## Tutorial Online Berkualitas

- 🔗 [Real Python — OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- 🔗 [Real Python — Inheritance and Composition](https://realpython.com/inheritance-composition-python/)
- 🔗 [Real Python — Python Magic Methods](https://realpython.com/python-magic-methods/)
- 🔗 [Real Python — Abstract Base Classes](https://realpython.com/python-interface/)
- 🔗 [Refactoring Guru — Design Patterns](https://refactoring.guru/design-patterns/python)

---

## Latihan & Tantangan Coding

- 🔗 [LeetCode](https://leetcode.com) — Latihan algoritma & struktur data
- 🔗 [HackerRank — Python](https://www.hackerrank.com/domains/python) — Latihan Python terstruktur
- 🔗 [Exercism.io — Python Track](https://exercism.org/tracks/python) — Latihan dengan mentor

---

## Video & Kursus

- 📺 [Corey Schafer — Python OOP Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc) — YouTube, gratis, sangat direkomendasikan
- 📺 [ArjanCodes — OOP & Design Patterns](https://www.youtube.com/@ArjanCodes) — YouTube, advanced
- 📺 [Tech With Tim — Python OOP](https://www.youtube.com/c/TechWithTim) — YouTube, pemula-menengah

---

## Cheat Sheet Cepat

### Struktur Kelas Dasar
```python
class NamaKelas:
    atribut_kelas = "nilai"          # Atribut kelas
    
    def __init__(self, param):
        self.atribut = param          # Atribut instance
    
    def method(self):                 # Method instance
        return self.atribut
    
    @classmethod
    def method_kelas(cls):            # Method kelas
        return cls.atribut_kelas
    
    @staticmethod
    def method_statis():              # Method statis
        return "tidak perlu self/cls"
```

### 4 Pilar OOP
| Pilar | Kata Kunci | Tujuan |
|-------|-----------|--------|
| Enkapsulasi | `_`, `__`, `@property` | Sembunyikan data |
| Pewarisan | `class Anak(Induk)` | Reuse kode |
| Polimorfisme | Method override | Banyak bentuk |
| Abstraksi | `ABC`, `@abstractmethod` | Kontrak kelas |

---

*Diperbarui: April 2026 | Informatika UNMUL*
