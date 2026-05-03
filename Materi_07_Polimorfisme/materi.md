# Materi 07 — Polimorfisme (Polymorphism)

---

## 1. Apa Itu Polimorfisme?

**Polimorfisme** berasal dari bahasa Yunani: *poly* (banyak) + *morphe* (bentuk). Dalam OOP, polimorfisme berarti **satu antarmuka, banyak implementasi** — kode yang sama dapat bekerja dengan objek dari tipe yang berbeda, selama objek tersebut memiliki method yang diharapkan.

> *"Satu perintah, banyak cara menjawab — itulah polimorfisme."*

### Analogi Dunia Nyata

Bayangkan seorang dosen yang berkata: **"Tolong perkenalkan diri kalian!"**

Setiap mahasiswa *menjawab dengan caranya sendiri* — ada yang singkat, ada yang panjang, ada yang memperkenalkan hobi. Dosen tidak perlu tahu persis *bagaimana* setiap orang akan menjawab; ia cukup berkata "perkenalkan diri" dan setiap orang merespons sesuai kepribadiannya.

Dalam OOP:
```
dosen.minta_perkenalan(mahasiswa_A)  # -> "Hai, saya Budi dari Informatika"
dosen.minta_perkenalan(mahasiswa_B)  # -> "Saya Sari, suka coding dan desain"
dosen.minta_perkenalan(dosen_tamu)   # -> "Dr. Reza, peneliti AI dari ITS"
```

Satu method `minta_perkenalan()`, banyak bentuk output — itulah polimorfisme.

---

## 2. Dua Jenis Polimorfisme di Python

| Jenis | Mekanisme | Contoh |
|-------|-----------|--------|
| **Polimorfisme via Pewarisan** | Method override di kelas anak | `hewan.suara()` berbeda tiap kelas |
| **Duck Typing** | Python tidak cek tipe, cek method | Objek apapun yang punya `.luas()` bisa diproses |

Python **tidak mendukung** method overloading (seperti Java/C++) secara native — sebagai gantinya Python menggunakan default arguments dan duck typing yang jauh lebih fleksibel.

> 💡 **Simulasi Method Overloading di Python:** Meski tidak ada sintaks khusus, efek serupa dapat dicapai dengan default parameters atau `*args`/`**kwargs`:
> ```python
> class Kalkulator:
>     def tambah(self, a, b=0, c=0):   # satu method, beberapa "versi"
>         return a + b + c             # tambah(5), tambah(3,4), tambah(1,2,3)
>
>     def luas(self, *args):           # persegi atau persegi_panjang
>         return args[0]**2 if len(args) == 1 else args[0] * args[1]
> ```

---

## 3. Polimorfisme via Pewarisan

Ini adalah bentuk polimorfisme yang paling eksplisit: kelas anak **meng-override** method dari kelas induk, sehingga satu pemanggilan menghasilkan perilaku yang berbeda tergantung tipe objeknya.

```python
class Hewan:
    def __init__(self, nama):
        self.nama = nama

    def suara(self):
        return "..."

    def bergerak(self):
        return "bergerak"


class Anjing(Hewan):
    def suara(self):
        return "Guk! Guk!"

    def bergerak(self):
        return "berlari"


class Kucing(Hewan):
    def suara(self):
        return "Meow~"

    def bergerak(self):
        return "berjalan anggun"


class Ular(Hewan):
    def suara(self):
        return "Sssss..."

    def bergerak(self):
        return "merayap"


# Polimorfisme: satu loop, tiga perilaku berbeda
kebun_binatang = [Anjing("Rex"), Kucing("Kitty"), Ular("Nagini")]

for hewan in kebun_binatang:
    print(f"{hewan.nama}: '{hewan.suara()}' — {hewan.bergerak()}")

# Output:
# Rex: 'Guk! Guk!' — berlari
# Kitty: 'Meow~' — berjalan anggun
# Nagini: 'Sssss...' — merayap
```

**Kunci polimorfisme:** fungsi/kode yang memanggil `hewan.suara()` **tidak perlu tahu** apakah `hewan` adalah `Anjing`, `Kucing`, atau `Ular`. Python mencari method `suara()` di tipe yang sebenarnya pada saat *runtime* — ini disebut **dynamic dispatch**.

---

## 4. Duck Typing — Polimorfisme Tanpa Pewarisan

> *"Jika ia berjalan seperti bebek dan bersuara seperti bebek, maka ia adalah bebek."*

Duck typing adalah filosofi Python: **tipe suatu objek tidak penting, yang penting adalah method apa yang ia miliki**. Selama suatu objek memiliki method yang dibutuhkan, ia bisa digunakan — tidak perlu ada hubungan pewarisan.

```python
class Lingkaran:
    def __init__(self, jari_jari):
        self.jari_jari = jari_jari

    def luas(self):
        import math
        return math.pi * self.jari_jari ** 2

    def __str__(self):
        return f"Lingkaran(r={self.jari_jari})"


class Persegi:
    def __init__(self, sisi):
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def __str__(self):
        return f"Persegi(sisi={self.sisi})"


class SegitigaSiku:
    def __init__(self, alas, tinggi):
        self.alas   = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi

    def __str__(self):
        return f"SegitigaSiku(alas={self.alas}, tinggi={self.tinggi})"


# Tidak ada pewarisan sama sekali — tapi semuanya bisa diproses bersama
def cetak_luas(bentuk):
    """Tidak peduli tipe bentuk, selama ia punya method luas()."""
    print(f"  {bentuk}: Luas = {bentuk.luas():.2f}")


bentuk_list = [Lingkaran(7), Persegi(5), SegitigaSiku(3, 4)]

for b in bentuk_list:
    cetak_luas(b)

# Output:
# Lingkaran(r=7): Luas = 153.94
# Persegi(sisi=5): Luas = 25.00
# SegitigaSiku(alas=3, tinggi=4): Luas = 6.00
```

Duck typing membuat Python sangat fleksibel — kelas dari library yang berbeda pun bisa dipakai bersama selama punya method yang sama.

---

## 5. Abstract Base Class (ABC) — Kontrak Polimorfisme

Duck typing sangat fleksibel, tapi juga rawan: bagaimana jika seseorang lupa mengimplementasikan method `luas()`? Programnya baru meledak saat runtime!

**Abstract Base Class (ABC)** adalah solusinya: ia memaksa kelas anak untuk mengimplementasikan method tertentu, atau program **langsung error saat objek dibuat** — jauh lebih aman.

```python
from abc import ABC, abstractmethod


class BentukDasar(ABC):
    """Kelas abstrak — tidak bisa di-instansiasi langsung."""

    def __init__(self, warna="putih"):
        self.warna = warna

    @abstractmethod
    def luas(self):
        """Wajib diimplementasikan oleh kelas anak."""
        pass

    @abstractmethod
    def keliling(self):
        """Wajib diimplementasikan oleh kelas anak."""
        pass

    def info(self):
        """Method konkret — bisa langsung dipakai kelas anak."""
        print(f"  {self} | Warna: {self.warna}")
        print(f"    Luas    : {self.luas():.2f}")
        print(f"    Keliling: {self.keliling():.2f}")

    def __str__(self):
        return self.__class__.__name__


class Persegi(BentukDasar):
    def __init__(self, sisi, warna="putih"):
        super().__init__(warna)
        self.sisi = sisi

    def luas(self):
        return self.sisi ** 2

    def keliling(self):
        return 4 * self.sisi

    def __str__(self):
        return f"Persegi(sisi={self.sisi})"


class Lingkaran(BentukDasar):
    def __init__(self, jari_jari, warna="putih"):
        import math
        super().__init__(warna)
        self.jari_jari = jari_jari
        self._pi = math.pi

    def luas(self):
        return self._pi * self.jari_jari ** 2

    def keliling(self):
        return 2 * self._pi * self.jari_jari

    def __str__(self):
        return f"Lingkaran(r={self.jari_jari})"


# Kelas yang TIDAK mengimplementasikan semua abstract method:
class BentukTidakLengkap(BentukDasar):
    def luas(self):          # hanya mengimplementasikan luas()
        return 0
    # Lupa keliling()!


# Uji ABC:
try:
    b = BentukDasar()        # Error! Kelas abstrak tidak bisa dibuat objek
except TypeError as e:
    print(f"  Error: {e}")
    # Can't instantiate abstract class BentukDasar without an implementation for abstract methods ...

try:
    x = BentukTidakLengkap()  # Error! Belum implementasi keliling()
except TypeError as e:
    print(f"  Error: {e}")

# Ini berhasil karena semua method terimplementasi:
p = Persegi(5, "merah")
l = Lingkaran(7)
p.info()
l.info()
```

> 💡 **Eksplorasi Langsung di Kode Praktik**
> File `kode/01_polimorfisme_dasar.py` mendemonstrasikan konsep ini secara mendalam:
> 1. **Bagian 1:** Polimorfisme via pewarisan — hierarki `Kendaraan` dengan `hitung_biaya_sewa()` berbeda.
> 2. **Bagian 2:** Duck typing — fungsi `distribusikan_dokumen()` yang bekerja dengan kelas apapun.
> 3. **Bagian 3:** ABC — sistem `Laporan` yang memaksa implementasi `generate()`.
>
> *Jalankan dan amati bagaimana satu antarmuka menghasilkan output yang berbeda-beda!*

---

## 6. Operator Overloading — Polimorfisme pada Operator

Python memungkinkan kita mendefinisikan **ulang perilaku operator** (`+`, `-`, `*`, `<`, `==`, dll.) untuk kelas buatan sendiri. Ini adalah bentuk polimorfisme karena operator yang sama berperilaku berbeda tergantung tipe operannya.

```python
class Vektor:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):      # mendefinisikan operator +
        return Vektor(self.x + other.x, self.y + other.y)

    def __sub__(self, other):      # mendefinisikan operator -
        return Vektor(self.x - other.x, self.y - other.y)

    def __mul__(self, skalar):     # mendefinisikan operator * (skalar)
        return Vektor(self.x * skalar, self.y * skalar)

    def __eq__(self, other):       # mendefinisikan operator ==
        return self.x == other.x and self.y == other.y

    def __abs__(self):             # mendefinisikan abs()
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __str__(self):
        return f"Vektor({self.x}, {self.y})"

    def __repr__(self):
        return f"Vektor(x={self.x}, y={self.y})"


v1 = Vektor(3, 4)
v2 = Vektor(1, 2)

print(v1 + v2)    # Vektor(4, 6)   <- __add__
print(v1 - v2)    # Vektor(2, 2)   <- __sub__
print(v1 * 3)     # Vektor(9, 12)  <- __mul__
print(v1 == v2)   # False          <- __eq__
print(abs(v1))    # 5.0            <- __abs__ (= sqrt(3^2 + 4^2))
```

**Tabel Operator dan Magic Method-nya:**

| Operator | Magic Method | Contoh |
|----------|-------------|--------|
| `+` | `__add__` | `a + b` |
| `-` | `__sub__` | `a - b` |
| `*` | `__mul__` | `a * b` |
| `/` | `__truediv__` | `a / b` |
| `==` | `__eq__` | `a == b` |
| `<` | `__lt__` | `a < b` |
| `>` | `__gt__` | `a > b` |
| `len()` | `__len__` | `len(a)` |
| `abs()` | `__abs__` | `abs(a)` |
| `str()` | `__str__` | `str(a)` |

---

## 7. `isinstance()` dalam Konteks Polimorfisme

Saat menggunakan polimorfisme, kadang kita perlu tahu tipe suatu objek. Gunakan `isinstance()` — **jangan** gunakan `type()` karena `type()` tidak mengenali pewarisan.

```python
class Hewan:       pass
class Anjing(Hewan): pass
class Kucing(Hewan): pass

rex = Anjing()

# Cara BENAR - isinstance() mengenali hierarki
print(isinstance(rex, Anjing))  # True
print(isinstance(rex, Hewan))   # True  <- mewarisi Hewan

# Cara KURANG TEPAT - type() tidak mengenali hierarki
print(type(rex) == Anjing)      # True
print(type(rex) == Hewan)       # False <- padahal Rex adalah Hewan!
```

### Pola Umum: Dispatch Berdasarkan Tipe

```python
def proses_hewan(hewan):
    if isinstance(hewan, Anjing):
        print(f"  {hewan.nama} diajak jalan-jalan!")
    elif isinstance(hewan, Kucing):
        print(f"  {hewan.nama} diberi mainan bola!")
    elif isinstance(hewan, Hewan):
        print(f"  {hewan.nama} diberi makan.")
```

> ⚠️ **Jebakan:** Jika terlalu banyak `isinstance()` di satu tempat, itu sinyal bahwa desain kelas perlu diperbaiki — pindahkan logik khusus ke dalam method kelas masing-masing, bukan di luar.

---

## 8. Polimorfisme dengan Fungsi Built-in Python

Polimorfisme bukan hanya untuk kode kita sendiri — fungsi built-in Python pun polimorfis!

```python
# len() bekerja untuk berbagai tipe
print(len("Universitas Mulawarman"))   # 22  <- string
print(len([1, 2, 3, 4, 5]))            # 5   <- list
print(len({"a": 1, "b": 2}))           # 2   <- dict

# Kita bisa buat kelas sendiri yang kompatibel dengan len()
class Matkul:
    def __init__(self, nama, daftar_mahasiswa):
        self.nama = nama
        self._mahasiswa = daftar_mahasiswa

    def __len__(self):
        return len(self._mahasiswa)

    def __str__(self):
        return f"{self.nama} ({len(self)} mahasiswa)"


pbo = Matkul("PBO", ["Budi", "Sari", "Rudi", "Ayu"])
print(len(pbo))   # 4
print(pbo)        # PBO (4 mahasiswa)

# sorted() bekerja jika kelas mengimplementasikan __lt__
class Mahasiswa:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.ipk  = ipk

    def __lt__(self, other):   # kurang dari
        return self.ipk < other.ipk

    def __str__(self):
        return f"{self.nama} (IPK: {self.ipk})"


mahasiswas = [
    Mahasiswa("Budi", 3.50),
    Mahasiswa("Sari", 3.85),
    Mahasiswa("Rudi", 3.20),
]

# sorted() otomatis menggunakan __lt__
for m in sorted(mahasiswas, reverse=True):
    print(f"  {m}")
# Output (dari IPK tertinggi):
#   Sari (IPK: 3.85)
#   Budi (IPK: 3.50)
#   Rudi (IPK: 3.20)
```

> 💡 **Eksplorasi Lanjutan di Kode Praktik**
> File `kode/02_duck_typing_dan_abc.py` mendemonstrasikan konsep ini secara mendalam:
> 1. **Bagian 1:** Duck typing murni — plugin sistem pembayaran tanpa ABC.
> 2. **Bagian 2:** ABC `Pembayaran` — kontrak yang dipaksakan.
> 3. **Bagian 3:** Operator overloading — kelas `Matriks2x2` dan `NilaiMahasiswa`.
> 4. **Bagian 4:** Integrasi dengan built-in (`len`, `sorted`, `max`) via magic methods.
>
> *Perhatikan bagaimana duck typing dan ABC melengkapi satu sama lain!*

---

## 9. Studi Kasus Nyata — Sistem Penilaian Akademik

Semua konsep berpadu dalam satu sistem yang realistis: sebuah **sistem penilaian** yang mampu menangani berbagai jenis komponen nilai (tugas, UTS, UAS, proyek) menggunakan polimorfisme.

```python
from abc import ABC, abstractmethod


class KomponenNilai(ABC):
    """Kelas abstrak — dasar semua komponen penilaian."""

    def __init__(self, nama, bobot):
        self.nama  = nama
        self.bobot = bobot   # bobot dalam persen (0-100)

    @abstractmethod
    def hitung_nilai(self):
        """Kembalikan nilai akhir komponen ini (0-100)."""
        pass

    def nilai_terbobot(self):
        return self.hitung_nilai() * (self.bobot / 100)

    def __str__(self):
        return (f"  {self.nama:<20} | Bobot: {self.bobot:>3}% | "
                f"Nilai: {self.hitung_nilai():>6.2f} | "
                f"Terbobot: {self.nilai_terbobot():>6.2f}")


class NilaiTugas(KomponenNilai):
    def __init__(self, nama, bobot, daftar_nilai):
        super().__init__(nama, bobot)
        self._daftar = daftar_nilai   # list nilai per tugas

    def hitung_nilai(self):
        return sum(self._daftar) / len(self._daftar) if self._daftar else 0


class NilaiUjian(KomponenNilai):
    def __init__(self, nama, bobot, nilai_benar, total_soal):
        super().__init__(nama, bobot)
        self._benar = nilai_benar
        self._total = total_soal

    def hitung_nilai(self):
        return (self._benar / self._total) * 100


class NilaiProyek(KomponenNilai):
    def __init__(self, nama, bobot, nilai_teknis, nilai_presentasi,
                 nilai_dokumentasi):
        super().__init__(nama, bobot)
        self._teknis       = nilai_teknis
        self._presentasi   = nilai_presentasi
        self._dokumentasi  = nilai_dokumentasi

    def hitung_nilai(self):
        return (self._teknis * 0.5 +
                self._presentasi * 0.3 +
                self._dokumentasi * 0.2)


class NilaiKuis(KomponenNilai):
    def __init__(self, nama, bobot, daftar_nilai, ambil_terbaik=None):
        super().__init__(nama, bobot)
        self._nilai  = daftar_nilai
        self._ambil  = ambil_terbaik or len(daftar_nilai)

    def hitung_nilai(self):
        terbaik = sorted(self._nilai, reverse=True)[:self._ambil]
        return sum(terbaik) / len(terbaik)


class LembarNilai:
    """Mengumpulkan KomponenNilai dan menghitung nilai akhir."""

    _PREDIKAT = [
        (87, "A"),  (82, "A-"), (78, "B+"), (75, "B"),
        (71, "B-"), (67, "C+"), (64, "C"),  (56, "D"),
        (0,  "E"),
    ]

    def __init__(self, mahasiswa, matkul):
        self.mahasiswa  = mahasiswa
        self.matkul     = matkul
        self._komponen  = []

    def tambah(self, komponen):
        self._komponen.append(komponen)
        return self  # mendukung method chaining

    def nilai_akhir(self):
        return sum(k.nilai_terbobot() for k in self._komponen)

    def predikat(self):
        na = self.nilai_akhir()
        for batas, huruf in self._PREDIKAT:
            if na >= batas:
                return huruf
        return "E"

    def cetak(self):
        print(f"\n  {'=' * 60}")
        print(f"  Mahasiswa : {self.mahasiswa}")
        print(f"  Matkul    : {self.matkul}")
        print(f"  {'-' * 60}")
        for k in self._komponen:
            print(k)
        print(f"  {'-' * 60}")
        print(f"  Nilai Akhir : {self.nilai_akhir():.2f}")
        print(f"  Predikat    : {self.predikat()}")
        print(f"  {'=' * 60}")


# Demonstrasi:
lembar = LembarNilai("Budi Santoso (2301001)", "PBO — 2024/2025 Genap")

lembar.tambah(NilaiKuis("Kuis Harian",   15, [70, 85, 90, 65, 80], ambil_terbaik=4))
lembar.tambah(NilaiTugas("Tugas Harian", 20, [85, 90, 78, 92, 88]))
lembar.tambah(NilaiUjian("UTS",          25, 38, 50))
lembar.tambah(NilaiProyek("Proyek Akhir",20, 88, 82, 90))
lembar.tambah(NilaiUjian("UAS",          20, 44, 50))

lembar.cetak()
```

> 💡 **Eksplorasi Lanjutan di Kode Praktik**
> File `kode/03_studi_kasus.py` menghadirkan **dua skenario polimorfisme nyata**:
> 1. **Skenario 1:** Sistem Penilaian Akademik — `KomponenNilai` abstrak dengan `NilaiKuis`, `NilaiTugas`, `NilaiUjian`, dan `NilaiProyek`.
> 2. **Skenario 2:** Sistem Notifikasi Multi-Kanal — `KanalNotifikasi` abstrak dengan Email, SMS, Push Notification, dan Webhook.
>
> *File ini menunjukkan bagaimana polimorfisme membuat kode mudah diperluas tanpa mengubah yang sudah ada!*

---

## 10. Polimorfisme vs Pewarisan — Jangan Tertukar!

Keduanya terkait erat tapi bukan hal yang sama:

| Aspek | Pewarisan | Polimorfisme |
|-------|-----------|-------------|
| **Pertanyaan** | "Kelas apa yang mewarisi siapa?" | "Antarmuka apa yang dipenuhi?" |
| **Fokus** | Struktur dan hubungan kelas | Perilaku dan cara dipanggil |
| **Mekanisme** | `class Anak(Induk)` | Method override, duck typing, ABC |
| **Tujuan** | Reuse kode dari induk | Satu antarmuka, banyak implementasi |
| **Tanpa pewarisan?** | Tidak mungkin | Bisa! (duck typing) |

Polimorfisme **bisa terjadi tanpa pewarisan** (duck typing), tapi pewarisan **sangat membantu** menegakkan kontrak antarmuka (ABC).

### Kapan Gunakan ABC vs Duck Typing?

| Situasi | ABC | Duck Typing |
|---------|-----|-------------|
| Ingin **memaksa** implementasi method tertentu | ✅ | ✗ |
| Bekerja dengan kelas dari **library eksternal** | ✗ | ✅ |
| Error terdeteksi **saat instansiasi**, bukan saat method dipanggil | ✅ | ✗ |
| **Fleksibilitas maksimal** tanpa hierarki kelas | ✗ | ✅ |
| Tim besar, butuh **kontrak formal** antar developer | ✅ | ✗ |
| Prototipe cepat atau skrip kecil | ✗ | ✅ |

> **Panduan:** Gunakan **ABC** ketika Anda mendefinisikan hierarki kelas sendiri dan ingin menjamin kontrak implementasi. Gunakan **duck typing** ketika bekerja dengan kelas dari pihak lain atau ketika fleksibilitas lebih penting dari keamanan tipe.

### Anti-Pattern yang Harus Dihindari

```python
# [BURUK]: Memeriksa tipe secara manual — bukan polimorfisme!
def cetak_suara(hewan):
    if type(hewan) == Anjing:
        print("Guk!")
    elif type(hewan) == Kucing:
        print("Meow!")
    # Harus dimodifikasi setiap ada hewan baru!

# [BENAR]: Biarkan objek tahu cara merespons sendiri
def cetak_suara(hewan):
    print(hewan.suara())   # Polimorfis — tidak perlu tahu tipe
```

---

## 11. Ringkasan Visual

```
Polimorfisme Python
│
├── Via Pewarisan (Inheritance Polymorphism)
│   ├── Kelas anak override method induk
│   ├── Satu method name, banyak implementasi
│   └── Python pilih implementasi saat runtime (dynamic dispatch)
│
├── Duck Typing
│   ├── Tidak perlu hierarki kelas
│   ├── Cukup punya method yang sama namanya
│   └── "If it quacks like a duck, it's a duck"
│
├── Abstract Base Class (ABC)
│   ├── Paksa kelas anak implementasi method tertentu
│   ├── from abc import ABC, abstractmethod
│   └── Error saat buat objek, bukan saat panggil method
│
└── Operator Overloading
    ├── __add__, __sub__, __mul__, dll.
    ├── __eq__, __lt__, __gt__ untuk perbandingan
    └── __len__, __abs__, __str__ untuk built-in
```

**Tabel Ringkasan:**

| Konsep | Sintaks / Cara | Keterangan |
|--------|---------------|------------|
| Override method | Definisikan ulang di kelas anak | Nama method sama |
| Duck typing | Pastikan method ada | Tidak perlu pewarisan |
| ABC | `class X(ABC)` + `@abstractmethod` | Error saat instansiasi |
| Operator overloading | `def __add__(self, other)` | Mendefinisikan `+` |
| Cek tipe polimorfis | `isinstance(obj, Kelas)` | Kenali hierarki |

---

## Bacaan Lanjutan

- [Real Python: Polymorphism in Python](https://realpython.com/python-interface/)
- [Python Docs: abc — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python: Operator and Function Overloading](https://realpython.com/operator-function-overloading/)
- [PEP 3119 — Abstract Base Classes](https://peps.python.org/pep-3119/)

---

*Sebelumnya: [Materi 06 — Pewarisan](../Materi_06_Pewarisan/materi.md)*
*Selanjutnya: [Materi 08 — Abstraksi](../Materi_08_Abstraksi/materi.md)*
