# Materi 09 — Magic Methods (Metode Ajaib)

---

## 1. Apa Itu Magic Methods?

**Magic methods** (juga disebut **dunder methods** — *double underscore methods*) adalah method khusus di Python yang namanya diawali dan diakhiri dengan dua garis bawah: `__nama__`.

Method-method ini tidak dipanggil secara langsung oleh programmer. Python memanggilnya **secara otomatis** sebagai respons terhadap operasi tertentu — seperti penjumlahan, perbandingan, konversi ke string, atau penggunaan `len()`.

> *"Magic methods adalah jembatan antara objek buatan Anda dan sintaks built-in Python."*

### Analogi Dunia Nyata

Bayangkan sebuah **mesin kopi otomatis** di kantin kampus:
- Anda **menekan tombol "Kopi Susu"** — mesin secara otomatis: panaskan air, tuang kopi, tambahkan susu, sajikan.
- Anda tidak perlu tahu langkah-langkah internalnya; mesin sudah "tahu" harus melakukan apa saat tombol tertentu ditekan.

Magic methods bekerja persis seperti itu:
- Anda menulis `nilai_a + nilai_b` — Python otomatis memanggil `nilai_a.__add__(nilai_b)`
- Anda menulis `len(daftar_mhs)` — Python otomatis memanggil `daftar_mhs.__len__()`
- Anda menulis `print(mahasiswa)` — Python otomatis memanggil `mahasiswa.__str__()`

Anda yang "menekan tombol" (menggunakan sintaks Python), objek yang menentukan respons (via magic methods).

---

## 2. Mengapa Magic Methods Penting?

Magic methods memungkinkan objek buatan Anda **berperilaku seperti tipe data bawaan Python**.

Tanpa magic methods:
```python
mhs = Mahasiswa("Budi", 3.75)
print(mhs)             # <__main__.Mahasiswa object at 0x...>  (tidak informatif)
len(mhs)               # TypeError: object of type 'Mahasiswa' has no len()
mhs_a + mhs_b          # TypeError: unsupported operand type(s)
```

Dengan magic methods:
```python
mhs = Mahasiswa("Budi", 3.75)
print(mhs)             # Mahasiswa: Budi | IPK: 3.75
len(kelas)             # 35  (jumlah mahasiswa)
nilai_a + nilai_b      # NilaiGabungan(85, "A")
```

---

## 3. Representasi String: `__str__` dan `__repr__`

Ini adalah dua magic methods yang paling sering diimplementasikan:

| Method | Dipanggil oleh | Tujuan |
|--------|---------------|--------|
| `__str__` | `print()`, `str()`, f-string | Representasi ramah-pengguna |
| `__repr__` | `repr()`, shell interaktif, debugging | Representasi teknis/formal |

### Aturan Praktis

- `__str__` untuk **pengguna akhir** — bisa ringkas dan deskriptif
- `__repr__` untuk **developer** — idealnya bisa dieksekusi kembali sebagai kode Python
- Jika hanya ada `__repr__`, Python menggunakannya untuk `str()` juga
- Jika hanya ada `__str__`, `repr()` tetap menampilkan format default `<objek...>`

```python
class Mahasiswa:
    def __init__(self, nim, nama, ipk):
        self.nim  = nim
        self.nama = nama
        self.ipk  = ipk

    def __str__(self):
        # Untuk print() — ramah dibaca manusia
        return f"[{self.nim}] {self.nama} — IPK: {self.ipk:.2f}"

    def __repr__(self):
        # Untuk debugging — bisa digunakan untuk membuat ulang objek
        return f"Mahasiswa(nim='{self.nim}', nama='{self.nama}', ipk={self.ipk})"

mhs = Mahasiswa("2301001", "Budi Santoso", 3.75)
print(str(mhs))    # [2301001] Budi Santoso — IPK: 3.75
print(repr(mhs))   # Mahasiswa(nim='2301001', nama='Budi Santoso', ipk=3.75)
```

---

## 4. Magic Methods Numerik: `__len__`, `__bool__`, `__abs__`

### `__len__(self)` — dipanggil oleh `len()`

Harus mengembalikan integer non-negatif. Digunakan untuk objek yang memiliki "ukuran" atau "jumlah anggota".

```python
class KelasKuliah:
    def __init__(self, nama_mk):
        self.nama_mk   = nama_mk
        self.mahasiswa = []

    def tambah(self, mhs):
        self.mahasiswa.append(mhs)

    def __len__(self):
        return len(self.mahasiswa)

kelas = KelasKuliah("Pemrograman Berorientasi Objek")
kelas.tambah("Budi")
kelas.tambah("Sari")
print(len(kelas))   # 2
```

### `__bool__(self)` — dipanggil dalam konteks boolean

Jika tidak didefinisikan, Python menggunakan `__len__` (objek kosong = False). Jika keduanya tidak ada, objek selalu `True`.

```python
class KelasKuliah:
    ...
    def __bool__(self):
        # Kelas "aktif" hanya jika ada minimal 5 mahasiswa terdaftar
        return len(self.mahasiswa) >= 5

kelas_kecil = KelasKuliah("Seminar")
if not kelas_kecil:
    print("Kelas belum cukup peserta untuk dibuka")
```

### `__abs__(self)` — dipanggil oleh `abs()`

```python
class Vektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __abs__(self):
        return (self.x**2 + self.y**2) ** 0.5   # panjang vektor

v = Vektor2D(3, 4)
print(abs(v))   # 5.0
```

---

## 5. Operator Aritmatika

Python memetakan setiap operator ke magic method tertentu:

| Operator | Magic Method | Contoh |
|----------|-------------|--------|
| `+` | `__add__(self, other)` | `a + b` |
| `-` | `__sub__(self, other)` | `a - b` |
| `*` | `__mul__(self, other)` | `a * b` |
| `/` | `__truediv__(self, other)` | `a / b` |
| `//` | `__floordiv__(self, other)` | `a // b` |
| `%` | `__mod__(self, other)` | `a % b` |
| `**` | `__pow__(self, other)` | `a ** b` |
| `-` (unary) | `__neg__(self)` | `-a` |
| `+` (unary) | `__pos__(self)` | `+a` |

### In-place Operators

Untuk `+=`, `-=`, `*=`, dst.:

| Operator | Magic Method |
|----------|-------------|
| `+=` | `__iadd__(self, other)` |
| `-=` | `__isub__(self, other)` |
| `*=` | `__imul__(self, other)` |

Jika `__iadd__` tidak didefinisikan, Python otomatis menggunakan `__add__` sebagai fallback.

### Reflected (Right-Hand Side) Operators

Ketika `a + b` gagal (karena tipe `a` tidak tahu cara menangani `b`), Python mencoba `b.__radd__(a)`:

| Operator | Reflected Method |
|----------|-----------------|
| `+` | `__radd__(self, other)` |
| `-` | `__rsub__(self, other)` |
| `*` | `__rmul__(self, other)` |

```python
class Vektor2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vektor2D(self.x + other.x, self.y + other.y)

    def __mul__(self, skalar):
        return Vektor2D(self.x * skalar, self.y * skalar)

    def __rmul__(self, skalar):
        # Dipanggil saat: 3 * vektor (bukan vektor * 3)
        return self.__mul__(skalar)

v1 = Vektor2D(1, 2)
v2 = Vektor2D(3, 4)
v3 = v1 + v2      # -> Vektor2D(4, 6)
v4 = v1 * 3       # -> Vektor2D(3, 6)
v5 = 3 * v1       # -> Vektor2D(3, 6)  — menggunakan __rmul__
```

---

## 6. Operator Perbandingan

| Operator | Magic Method |
|----------|-------------|
| `==` | `__eq__(self, other)` |
| `!=` | `__ne__(self, other)` |
| `<`  | `__lt__(self, other)` |
| `<=` | `__le__(self, other)` |
| `>`  | `__gt__(self, other)` |
| `>=` | `__ge__(self, other)` |

### Tips: `@functools.total_ordering`

Jika Anda mendefinisikan `__eq__` dan salah satu dari `__lt__`/`__le__`/`__gt__`/`__ge__`, decorator `@total_ordering` otomatis melengkapi sisanya:

```python
from functools import total_ordering

@total_ordering
class NilaiMahasiswa:
    def __init__(self, angka):
        self.angka = angka

    def __eq__(self, other):
        return self.angka == other.angka

    def __lt__(self, other):
        return self.angka < other.angka

    # Secara otomatis tersedia: __le__, __gt__, __ge__

n1 = NilaiMahasiswa(85)
n2 = NilaiMahasiswa(90)
print(n1 < n2)    # True
print(n1 >= n2)   # False  — dibuat otomatis oleh total_ordering
print(sorted([n2, n1]))  # [NilaiMahasiswa(85), NilaiMahasiswa(90)]
```

### Catatan Penting: `__eq__` dan `__hash__`

Jika Anda mendefinisikan `__eq__`, Python secara otomatis menetapkan `__hash__ = None`, menjadikan objek **tidak bisa di-hash** (tidak bisa dimasukkan ke set/dict).

Jika objek harus bisa di-hash setelah `__eq__` didefinisikan:

```python
def __hash__(self):
    return hash(self.angka)   # atau hash((field1, field2, ...))
```

---

## 7. Magic Methods Container

Untuk membuat kelas yang berperilaku seperti list, dict, atau set:

| Magic Method | Dipanggil oleh | Contoh |
|-------------|---------------|--------|
| `__getitem__(self, key)` | `obj[key]` | `kelas[0]` |
| `__setitem__(self, key, val)` | `obj[key] = val` | `kelas[0] = mhs_baru` |
| `__delitem__(self, key)` | `del obj[key]` | `del kelas[0]` |
| `__contains__(self, item)` | `item in obj` | `"Budi" in kelas` |
| `__iter__(self)` | `for x in obj`, `list()`, dll. | `for mhs in kelas:` |
| `__next__(self)` | digunakan bersama `__iter__` | (jika class berfungsi sebagai iterator) |
| `__reversed__(self)` | `reversed(obj)` | `for mhs in reversed(kelas):` |

```python
class DaftarMataKuliah:
    def __init__(self):
        self._matkul = []

    def tambah(self, nama_mk):
        self._matkul.append(nama_mk)

    def __getitem__(self, index):
        return self._matkul[index]

    def __contains__(self, nama_mk):
        return nama_mk in self._matkul

    def __iter__(self):
        return iter(self._matkul)

    def __len__(self):
        return len(self._matkul)

dmk = DaftarMataKuliah()
dmk.tambah("PBO")
dmk.tambah("Struktur Data")
print(dmk[0])                  # PBO
print("PBO" in dmk)            # True
for mk in dmk:
    print(mk)                  # iterasi berfungsi
```

---

## 8. Context Manager: `__enter__` dan `__exit__`

Magic methods ini memungkinkan objek Anda digunakan dengan pernyataan `with`:

```python
class KoneksiDatabase:
    def __init__(self, nama_db):
        self.nama_db = nama_db
        self.terhubung = False

    def __enter__(self):
        print(f"Membuka koneksi ke {self.nama_db}...")
        self.terhubung = True
        return self   # nilai yang diterima oleh 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Menutup koneksi ke {self.nama_db}...")
        self.terhubung = False
        return False  # False = tidak menekan (suppress) exception

# Penggunaan:
with KoneksiDatabase("akademik.db") as db:
    print(f"Status: {db.terhubung}")
    # Koneksi otomatis ditutup setelah blok 'with' selesai
```

### Parameter `__exit__`

- `exc_type`: tipe exception (atau `None` jika tidak ada error)
- `exc_val`: nilai/pesan exception
- `exc_tb`: traceback
- Return `True` untuk **menekan exception** (exception tidak menyebar)
- Return `False` atau `None` untuk **membiarkan exception menyebar**

---

## 9. Callable: `__call__`

Membuat instance bisa dipanggil seperti fungsi:

```python
class KalkulatorSKS:
    def __init__(self, tarif_per_sks):
        self.tarif_per_sks = tarif_per_sks

    def __call__(self, jumlah_sks):
        return jumlah_sks * self.tarif_per_sks

hitung_biaya = KalkulatorSKS(tarif_per_sks=750_000)
tagihan_reguler = hitung_biaya(20)   # sama seperti hitung_biaya.__call__(20)
print(f"Tagihan: Rp {tagihan_reguler:,.0f}")  # Tagihan: Rp 15,000,000
```

Ini berguna untuk membuat objek yang berperilaku seperti fungsi tapi bisa menyimpan state (berbeda dengan fungsi biasa).

---

## 10. `__format__` — Format String Kustom

Dipanggil ketika objek digunakan dalam `format()` atau f-string dengan format spec:

```python
class NilaiAkhir:
    def __init__(self, angka):
        self.angka = angka

    def __format__(self, spec):
        if spec == "huruf":
            if self.angka >= 85:  return "A"
            if self.angka >= 70:  return "B"
            if self.angka >= 55:  return "C"
            if self.angka >= 40:  return "D"
            return "E"
        if spec == "predikat":
            if self.angka >= 85:  return "Cumlaude"
            if self.angka >= 70:  return "Sangat Memuaskan"
            return "Memuaskan"
        return str(self.angka)  # default

n = NilaiAkhir(88)
print(f"Nilai: {n}")              # Nilai: 88
print(f"Nilai: {n:huruf}")        # Nilai: A
print(f"Nilai: {n:predikat}")     # Nilai: Cumlaude
```

---

## 11. `__del__` — Destruktor

Dipanggil saat objek akan dihapus dari memori (garbage collected). Jarang digunakan secara eksplisit.

```python
class SesiKuliah:
    def __init__(self, nama_mk):
        self.nama_mk = nama_mk
        print(f"Sesi '{nama_mk}' dimulai")

    def __del__(self):
        print(f"Sesi '{self.nama_mk}' berakhir — memori dibebaskan")

sesi = SesiKuliah("Algoritma")
del sesi   # memicu __del__
```

> **Peringatan:** Jangan mengandalkan `__del__` untuk menutup file atau koneksi. Gunakan context manager (`with`) sebagai gantinya — lebih prediktabel.

---

## 12. Tabel Ringkasan Magic Methods

### Representasi & Konversi

| Method | Dipanggil oleh | Keterangan |
|--------|---------------|------------|
| `__str__` | `print()`, `str()` | String ramah pengguna |
| `__repr__` | `repr()`, shell | String teknis/formal |
| `__format__` | `format()`, f-string | Format kustom |
| `__bool__` | `bool()`, `if obj:` | Nilai kebenaran |
| `__int__` | `int(obj)` | Konversi ke integer |
| `__float__` | `float(obj)` | Konversi ke float |
| `__len__` | `len(obj)` | Ukuran/panjang |
| `__abs__` | `abs(obj)` | Nilai absolut |
| `__hash__` | `hash(obj)`, set/dict | Nilai hash |

### Operator Aritmatika

| Method | Operator |
|--------|---------|
| `__add__` | `+` |
| `__sub__` | `-` |
| `__mul__` | `*` |
| `__truediv__` | `/` |
| `__floordiv__` | `//` |
| `__mod__` | `%` |
| `__pow__` | `**` |
| `__neg__` | `-a` (unary) |
| `__pos__` | `+a` (unary) |

### Operator Perbandingan

| Method | Operator |
|--------|---------|
| `__eq__` | `==` |
| `__ne__` | `!=` |
| `__lt__` | `<` |
| `__le__` | `<=` |
| `__gt__` | `>` |
| `__ge__` | `>=` |

### Container & Iterasi

| Method | Dipanggil oleh |
|--------|---------------|
| `__getitem__` | `obj[key]` |
| `__setitem__` | `obj[key] = val` |
| `__delitem__` | `del obj[key]` |
| `__contains__` | `item in obj` |
| `__iter__` | `for x in obj` |
| `__next__` | `next(iterator)` |
| `__reversed__` | `reversed(obj)` |

### Manajemen & Lain-lain

| Method | Dipanggil oleh |
|--------|---------------|
| `__init__` | `Kelas(...)` — konstruktor |
| `__del__` | Saat GC menghapus objek |
| `__call__` | `obj()` — callable |
| `__enter__` | `with obj:` — masuk blok |
| `__exit__` | Akhir blok `with` |

---

## 13. Urutan Pemanggilan & Prioritas

Ketika `a + b` dieksekusi, Python mengikuti urutan:

1. Coba `a.__add__(b)` — jika mengembalikan `NotImplemented`, lanjut
2. Coba `b.__radd__(a)` — reflected operator
3. Jika keduanya `NotImplemented`, lempar `TypeError`

Kembalikan `NotImplemented` (bukan raise exception) agar Python bisa mencoba reflected method:

```python
def __add__(self, other):
    if not isinstance(other, NilaiMahasiswa):
        return NotImplemented   # biarkan Python coba alternatif
    return NilaiMahasiswa(self.angka + other.angka)
```

---

## 14. Studi Kasus Ringkas: Kelas `Transkrip`

Dengan menggabungkan berbagai magic methods, sebuah kelas bisa berperilaku sangat natural:

```python
transkrip = Transkrip("Budi Santoso")
transkrip += MataKuliah("PBO", 3, 88)
transkrip += MataKuliah("Kalkulus", 4, 72)

print(transkrip)            # __str__
print(len(transkrip))       # __len__  -> jumlah matkul
print(transkrip[0])         # __getitem__
print("PBO" in transkrip)   # __contains__

for mk in transkrip:        # __iter__
    print(mk)

if transkrip:               # __bool__ -> ada matkul yang diambil
    print("Transkrip tidak kosong")
```

Ini adalah gaya penulisan Python yang idiomatis — memanfaatkan magic methods sehingga kelas buatan Anda terasa seperti bagian dari bahasa Python itu sendiri.

---

## Referensi

- [Python Data Model — Dokumentasi Resmi](https://docs.python.org/3/reference/datamodel.html)
- [functools.total_ordering](https://docs.python.org/3/library/functools.html#functools.total_ordering)
- Fluent Python, 2nd Ed. — Luciano Ramalho (Bab 1, 11, 16)
- Python Cookbook, 3rd Ed. — David Beazley & Brian Jones (Bab 8)
