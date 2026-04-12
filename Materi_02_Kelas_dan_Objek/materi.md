# Materi 02 — Kelas dan Objek

---

## 1. Sintaks Lengkap Mendefinisikan Kelas

Sebuah kelas di Python dituliskan dengan pola berikut:

```python
class NamaKelas:                    # ← Nama kelas: PascalCase
    """Docstring: penjelasan kelas""" # ← Opsional tapi sangat direkomendasikan

    def __init__(self, param1, param2):  # ← Konstruktor
        self.atribut1 = param1           # ← Definisi atribut instance
        self.atribut2 = param2

    def nama_method(self):          # ← Method instance
        # isi method
        return self.atribut1
```

### Konvensi Penamaan (wajib diikuti!)

| Elemen | Konvensi | Contoh |
|--------|----------|--------|
| Nama Kelas | **PascalCase** | `MataKuliah`, `NilaiMahasiswa`, `RekeningBank` |
| Nama Atribut | **snake_case** | `nama_depan`, `nilai_akhir`, `no_rekening` |
| Nama Method | **snake_case** | `hitung_nilai()`, `tampilkan_info()` |
| Nama File | **snake_case** | `mata_kuliah.py`, `rekening_bank.py` |

> 💡 **Mengapa PascalCase untuk kelas?** Ini adalah konvensi Python (PEP 8) yang dipatuhi seluruh dunia. Dengan PascalCase, kita langsung tahu bahwa sebuah nama adalah kelas, bukan variabel atau fungsi biasa.

---

## 2. Konstruktor: `__init__`

`__init__` adalah **method spesial** yang dipanggil **secara otomatis** setiap kali objek baru dibuat. Tugas utamanya adalah **menginisialisasi atribut** objek.

```python
class Laptop:
    def __init__(self, merk, ram, storage):
        #  ▲          ▲     ▲    ▲
        #  │          │     │    └─── parameter ke-3
        #  │          │     └──────── parameter ke-2
        #  │          └────────────── parameter ke-1
        #  └ 'self' selalu parameter PERTAMA (wajib)

        self.merk    = merk      # simpan ke atribut instance
        self.ram     = ram
        self.storage = storage

laptop = Laptop("Asus", 16, 512)
print(laptop.merk)    # Output: Asus
print(laptop.ram)     # Output: 16
```

### Nilai Default pada Konstruktor

Parameter bisa diberi **nilai default** sehingga tidak wajib diisi saat membuat objek:

```python
class Mahasiswa:
    def __init__(self, nama, nim, semester=1, aktif=True):
        #                              ▲           ▲
        #                        nilai default  nilai default
        self.nama     = nama
        self.nim      = nim
        self.semester = semester
        self.aktif    = aktif

# Semua cara ini valid:
mhs1 = Mahasiswa("Andi", "2301001")                  # semester=1, aktif=True (default)
mhs2 = Mahasiswa("Budi", "2301002", 3)               # aktif=True (default)
mhs3 = Mahasiswa("Citra", "2301003", 5, False)       # semua diisi
```

> ⚠️ **Aturan:** Parameter dengan nilai default harus diletakkan **setelah** parameter wajib. Contoh yang salah: `def __init__(self, semester=1, nama)` → Error!

---

## 3. Positional vs Keyword Argument

Saat membuat objek, ada **dua cara** memberikan argumen:

### a) Positional Argument — berdasarkan URUTAN

```python
class Dosen:
    def __init__(self, nama, nip, bidang):
        self.nama   = nama
        self.nip    = nip
        self.bidang = bidang

# Positional: urutan argumen harus tepat sesuai definisi
dosen1 = Dosen("Anton Prafanto", "198501012010011001", "Rekayasa Perangkat Lunak")
#                   ▲                   ▲                         ▲
#                  nama                nip                      bidang
```

### b) Keyword Argument — berdasarkan NAMA parameter

```python
# Keyword: urutan bebas, tapi nama parameter harus benar
dosen2 = Dosen(
    bidang = "Basis Data",
    nama   = "Siti Rahayu",
    nip    = "197803152005012002"
)
# Hasilnya sama saja!
print(dosen2.nama)    # Output: Siti Rahayu
print(dosen2.bidang)  # Output: Basis Data
```

### c) Campuran (Positional dulu, baru Keyword)

```python
# Positional di depan, keyword di belakang
dosen3 = Dosen("Andi Wijaya", nip="196912201995011001", bidang="Jaringan")
```

| Cara | Keunggulan | Kekurangan |
|------|-----------|------------|
| **Positional** | Lebih singkat | Harus ingat urutan |
| **Keyword** | Lebih jelas | Lebih panjang |
| **Campuran** | Fleksibel | Perlu hati-hati urutan |

---

## 4. Membuat Banyak Objek dari Satu Kelas

Satu kelas bisa menghasilkan tak terbatas objek. Simpan dalam list untuk kemudahan pengelolaan:

```python
class Produk:
    def __init__(self, nama, harga, stok):
        self.nama  = nama
        self.harga = harga
        self.stok  = stok

# List berisi banyak objek Produk
katalog = [
    Produk("Laptop",   8_500_000, 10),
    Produk("Mouse",      150_000, 50),
    Produk("Keyboard",   350_000, 25),
]

# Loop semua objek
for p in katalog:
    print(f"{p.nama}: Rp {p.harga:,.0f}")
# Output:
# Laptop: Rp 8,500,000
# Mouse: Rp 150,000
# Keyboard: Rp 350,000

# Filter menggunakan list comprehension
murah = [p for p in katalog if p.harga < 500_000]

# Urutkan berdasarkan harga
terurut = sorted(katalog, key=lambda p: p.harga)

# Hitung total nilai stok
total = sum(p.harga * p.stok for p in katalog)
print(f"Total inventori: Rp {total:,.0f}")
# Output: Total inventori: Rp 95,750,000
```

---

## 5. Mengakses, Mengubah, dan Menghapus Atribut

### Mengakses Atribut (Dot Notation)

```python
mhs = Mahasiswa("Budi", "2301001")

print(mhs.nama)    # Output: Budi     ← baca atribut
print(mhs.nim)     # Output: 2301001  ← baca atribut
```

### Mengubah Atribut

```python
mhs.nama     = "Budi Santoso"   # ubah atribut
mhs.semester = 3                 # ubah atribut

print(mhs.nama)     # Output: Budi Santoso
print(mhs.semester) # Output: 3
```

### Menghapus Objek

```python
mhs = Mahasiswa("Budi", "2301001")
del mhs              # hapus referensi ke objek

# print(mhs)         # → NameError: name 'mhs' is not defined
```

> 💡 Python sebenarnya punya **Garbage Collector** yang otomatis membersihkan objek saat tidak ada lagi variabel yang merujuknya. `del` hanya menghapus referensi variabelnya.

---

## 6. Menampilkan Objek: Sekilas Tentang `__str__`

Coba print objek langsung — hasilnya kurang informatif:

```python
mhs = Mahasiswa("Budi", "2301001")
print(mhs)
# Output: <__main__.Mahasiswa object at 0x000001A2...>  ← tidak informatif!
```

Solusinya adalah mendefinisikan method `__str__` (akan dipelajari detail di Materi 09):

```python
class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    def __str__(self):
        return f"Mahasiswa({self.nama}, {self.nim})"

mhs = Mahasiswa("Budi", "2301001")
print(mhs)
# Output: Mahasiswa(Budi, 2301001)  ← jauh lebih informatif!
```

> 📌 Untuk sekarang, kita menggunakan method `info()` atau `tampilkan_info()` sebagai alternatif yang lebih eksplisit. Kita akan bahas `__str__` detail di Materi 09.

---

## 7. Objek sebagai Parameter dan Return Value

Objek bisa dikirim ke fungsi sebagai argumen, dan dikembalikan sebagai nilai return:

```python
def cari_terbaik(daftar_mhs):
    """Menerima list objek Mahasiswa, kembalikan yang IPK tertinggi."""
    return max(daftar_mhs, key=lambda m: m.ipk)

def buat_mahasiswa(nama, nim, ipk):
    """Membuat dan mengembalikan objek Mahasiswa."""
    return Mahasiswa(nama, nim, ipk)  # ← return objek!

mhs_baru = buat_mahasiswa("Andi", "2301001", 3.85)   # ← terima objek
terbaik  = cari_terbaik([mhs1, mhs2, mhs3])           # ← kirim list objek
```

---

## 8. Ringkasan Visual

```
┌─────────────────────────────────────────────┐
│              DEFINISI KELAS                 │
│                                             │
│  class NamaKelas:                           │
│      def __init__(self, wajib, opsional=0): │
│          self.atribut = wajib               │
│      def method(self):                      │
│          return self.atribut                │
└─────────────────────────────────────────────┘
              │
   ┌──────────┴──────────┐
   │    Cara Membuat Objek│
   ├──────────────────────┤
   │ Positional:          │
   │  obj = Kelas(a, b)   │
   │ Keyword:             │
   │  obj = Kelas(x=a,    │
   │              y=b)    │
   └──────────────────────┘
              │
   Hasilnya → obj.atribut  (baca)
              obj.atribut = nilai  (ubah)
              obj.method()  (panggil)
              del obj  (hapus)

Banyak objek → simpan dalam list:
  daftar = [Kelas(...), Kelas(...), ...]
  for obj in daftar: obj.method()
```

---

## 📖 Bacaan Lanjutan

- 🔗 [Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)
- 🔗 [Real Python: Python Classes](https://realpython.com/python3-object-oriented-programming/#python-objects-revisited)
- 🔗 [PEP 8 — Style Guide](https://peps.python.org/pep-0008/#class-names)

---

*➡️ Lanjut ke: [Materi 03 — Atribut dan Method](../Materi_03_Atribut_dan_Method/materi.md)*
