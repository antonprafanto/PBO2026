# Materi 08 — Abstraksi (Abstraction)

---

## 1. Apa Itu Abstraksi?

**Abstraksi** adalah kemampuan untuk **menyembunyikan detail implementasi** dan hanya menampilkan hal-hal yang penting bagi pengguna. Ini adalah salah satu dari **empat pilar OOP** — bersama Enkapsulasi, Pewarisan, dan Polimorfisme.

> *"Abstraksi bukan berarti samar-samar, tapi berarti memilih perspektif yang tepat."*
> — Grady Booch

### Analogi Dunia Nyata

Bayangkan Anda menggunakan **mesin ATM**:
- Anda tahu cara: masukkan kartu → masukkan PIN → pilih tarik tunai → ambil uang
- Anda **tidak tahu** (dan tidak perlu tahu): protokol enkripsi PIN, koneksi ke server bank, validasi saldo di database

ATM **mengabstraksi** kerumitan sistem perbankan menjadi antarmuka yang sederhana dan seragam. Itu adalah abstraksi!

Dalam OOP, kelas abstrak melakukan hal yang sama:
- **Mendefinisikan ANTARMUKA** (apa yang bisa dilakukan)
- **Menyembunyikan IMPLEMENTASI** (bagaimana melakukannya)

---

## 2. Abstraksi vs Enkapsulasi

Sering kali dua konsep ini dicampuradukkan. Berikut perbedaan utamanya:

| Aspek | Enkapsulasi | Abstraksi |
|-------|-------------|-----------|
| **Tujuan** | Melindungi data dari akses luar | Menyembunyikan kompleksitas implementasi |
| **Fokus** | *Bagaimana* data disimpan (privat/publik) | *Apa* yang bisa dilakukan (antarmuka) |
| **Mekanisme** | `_protected`, `__private`, `@property` | Kelas abstrak, `@abstractmethod` |
| **Analogi** | Kapsul obat — isi tersembunyi di dalam | Mesin ATM — detail mesin tersembunyi |
| **Siapa yang dilindungi?** | Objek dari manipulasi luar | Pengguna dari kerumitan implementasi |

> 💡 **Mudah diingat:**
> - **Enkapsulasi** = *"Kamu tidak boleh menyentuh isi ini langsung"*
> - **Abstraksi** = *"Kamu tidak perlu tahu cara kerjanya, cukup gunakan antarmukanya"*

---

## 3. Kelas Abstrak di Python — Modul `abc`

Python menggunakan modul `abc` (*Abstract Base Classes*) untuk mendefinisikan kelas abstrak. Ada dua elemen utama:

1. **`ABC`** — kelas dasar yang membuat suatu kelas menjadi abstrak
2. **`@abstractmethod`** — dekorator yang menandai method sebagai *wajib diimplementasikan*

```python
from abc import ABC, abstractmethod

class KendaraanAbstrak(ABC):
    """Kelas abstrak — mendefinisikan kontrak kendaraan."""

    def __init__(self, merk, tahun):
        self.merk  = merk
        self.tahun = tahun

    @abstractmethod
    def nyalakan_mesin(self):
        """Setiap kendaraan punya cara berbeda nyalakan mesin."""
        pass

    @abstractmethod
    def hitung_konsumsi_bbm(self, jarak_km):
        """Setiap kendaraan punya konsumsi berbeda."""
        pass

    # Method KONKRET — sudah ada implementasinya, boleh dipakai langsung
    def info(self):
        print(f"Kendaraan: {self.merk} ({self.tahun})")
```

**Aturan penting:**
- Kelas abstrak **tidak bisa di-instansiasi** langsung
- Kelas anak **WAJIB** mengimplementasikan semua `@abstractmethod`
- Kelas abstrak **boleh** memiliki method konkret (sudah ada isinya)
- Kelas abstrak **boleh** memiliki `__init__` dan atribut

---

## 4. Abstract Property

Selain method, properti (getter/setter) juga bisa dijadikan abstrak menggunakan kombinasi `@property` dan `@abstractmethod`:

```python
from abc import ABC, abstractmethod

class Produk(ABC):
    """Kelas abstrak produk — properti harga wajib diimplementasikan."""

    def __init__(self, nama):
        self._nama = nama

    @property
    def nama(self):
        return self._nama          # property konkret — boleh diwarisi

    @property
    @abstractmethod
    def harga(self):
        """Harga wajib didefinisikan oleh setiap subkelas."""
        pass

    @property
    @abstractmethod
    def kategori(self):
        """Kategori produk wajib didefinisikan."""
        pass

    def info(self):
        print(f"  [{self.kategori}] {self.nama}: Rp {self.harga:,.0f}")
```

> ⚠️ **Urutan dekorator penting!**
> `@property` harus ditulis **sebelum** `@abstractmethod` agar keduanya bekerja dengan benar.

---

## 5. Template Method Pattern

**Template Method** adalah salah satu pola desain (*design pattern*) paling populer yang memanfaatkan abstraksi. Idenya:

> Kelas abstrak mendefinisikan **kerangka algoritma** (urutan langkah-langkahnya), tapi membiarkan kelas anak mengisi **detail setiap langkah**.

```python
from abc import ABC, abstractmethod

class ProsesPembayaran(ABC):
    """
    Template Method: proses() mendefinisikan URUTAN langkah pembayaran.
    Subkelas mengisi detail setiap langkah.
    """

    def proses(self, jumlah):
        """TEMPLATE METHOD — urutan langkah tidak berubah."""
        print(f"\n  Memproses pembayaran Rp {jumlah:,.0f}")
        self.validasi_akun()
        self.verifikasi_dana(jumlah)
        self.transfer_dana(jumlah)
        self.kirim_notifikasi(jumlah)
        print("  ✓ Pembayaran selesai")

    @abstractmethod
    def validasi_akun(self):
        pass

    @abstractmethod
    def verifikasi_dana(self, jumlah):
        pass

    @abstractmethod
    def transfer_dana(self, jumlah):
        pass

    def kirim_notifikasi(self, jumlah):
        """Hook method — punya default, boleh di-override."""
        print(f"  Notifikasi: Pembayaran Rp {jumlah:,.0f} berhasil")
```

Dengan Template Method:
- Urutan proses dijamin **konsisten** di semua implementasi
- Subkelas hanya fokus pada **perbedaannya** saja
- Sangat berguna untuk algoritma yang punya tahapan tetap

---

## 6. Multiple Abstract Interface

Python mendukung **multiple inheritance**, sehingga sebuah kelas bisa mengimplementasikan **lebih dari satu antarmuka abstrak** sekaligus. Ini mirip konsep *interface* di Java/C#.

```python
from abc import ABC, abstractmethod

class Bisa_Terbang(ABC):
    @abstractmethod
    def terbang(self):
        pass

    @abstractmethod
    def ketinggian_maksimum(self):
        pass


class Bisa_Berenang(ABC):
    @abstractmethod
    def berenang(self):
        pass

    @abstractmethod
    def kecepatan_renang(self):
        pass


class Bebek(Bisa_Terbang, Bisa_Berenang):
    """Bebek bisa terbang DAN berenang — mengimplementasikan dua interface."""

    def terbang(self):
        return "Terbang rendah dengan kepak sayap cepat"

    def ketinggian_maksimum(self):
        return 50  # meter

    def berenang(self):
        return "Berenang di permukaan air"

    def kecepatan_renang(self):
        return 3  # km/jam
```

**Kapan pakai Multiple Interface?**
- Ketika sebuah objek punya **beberapa peran** yang berbeda
- Untuk memastikan kelas memenuhi **kontrak dari beberapa sistem** sekaligus

---

## 7. Hierarki Kelas Abstrak

Kelas abstrak **bisa mewarisi kelas abstrak lain**. Ini memungkinkan pembuatan hierarki kontrak yang bertingkat:

```
HewanABC (abstrak — suara(), bergerak())
    └── HewanDaratABC (abstrak — berlari(), menggali())
            └── HewanPeliharaanABC (abstrak — nama_pemilik())
                    └── Anjing (konkret — mengimplementasikan semua)
```

```python
from abc import ABC, abstractmethod

class HewanABC(ABC):
    @abstractmethod
    def suara(self): pass

    @abstractmethod
    def bergerak(self): pass


class HewanDaratABC(HewanABC):        # Abstrak mewarisi abstrak
    @abstractmethod
    def berlari(self): pass
    # suara() dan bergerak() masih wajib diimplementasikan oleh kelas konkret


class Anjing(HewanDaratABC):          # Kelas KONKRET — wajib isi semuanya
    def suara(self):   return "Guk!"
    def bergerak(self): return "berjalan"
    def berlari(self): return "berlari kencang"
```

---

## 8. `isinstance()` dan `issubclass()` dengan ABC

ABC juga memperkuat pemeriksaan tipe:

```python
from abc import ABC, abstractmethod

class Serializable(ABC):
    @abstractmethod
    def to_dict(self): pass

    @abstractmethod
    def to_json(self): pass


class Mahasiswa(Serializable):
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    def to_dict(self):
        return {"nama": self.nama, "nim": self.nim}

    def to_json(self):
        import json
        return json.dumps(self.to_dict())


m = Mahasiswa("Budi", "2301001")

print(isinstance(m, Mahasiswa))      # True
print(isinstance(m, Serializable))  # True  ← ABC dikenali!
print(issubclass(Mahasiswa, Serializable))  # True
```

`isinstance()` dengan ABC sangat berguna untuk **memvalidasi** bahwa sebuah objek memenuhi kontrak tertentu sebelum diproses.

---

## 9. ABC dengan `__subclasshook__` — Virtual Subclass

ABC di Python punya fitur canggih: **virtual subclass**. Dengan mengimplementasikan `__subclasshook__`, kita bisa membuat kelas yang tidak secara eksplisit mewarisi ABC pun tetap dianggap sebagai subclass-nya — asalkan memiliki method yang diperlukan.

```python
from abc import ABC, abstractmethod

class Iterable(ABC):
    @abstractmethod
    def __iter__(self): pass

    @classmethod
    def __subclasshook__(cls, C):
        """Kelas apapun yang punya __iter__ dianggap Iterable."""
        if cls is Iterable:
            if any("__iter__" in B.__dict__ for B in C.__mro__):
                return True
        return NotImplemented


# List tidak secara eksplisit mewarisi Iterable, tapi punya __iter__
print(isinstance([], Iterable))      # True  ← virtual subclass!
print(isinstance({}, Iterable))      # True
print(isinstance(42, Iterable))      # False
```

> 💡 **Catatan:** `__subclasshook__` adalah fitur lanjutan. Untuk kebanyakan kasus, pewarisan eksplisit dari ABC sudah cukup.

---

## 10. Perbandingan: ABC vs Duck Typing vs Protocol

| Pendekatan | Cara Kerja | Keunggulan | Kelemahan |
|------------|-----------|------------|-----------|
| **Duck Typing** | Tidak ada cek tipe — asal punya method, jalan | Paling fleksibel, sedikit kode | Error baru muncul saat runtime |
| **ABC** | `from abc import ABC, abstractmethod` | Error saat objek dibuat (lebih awal) | Perlu eksplisit mewarisi ABC |
| **typing.Protocol** | `from typing import Protocol` (Python 3.8+) | Structural typing — tanpa pewarisan | Hanya cek tipe, tidak enforce |

```python
# Duck Typing — paling sederhana
def cetak_luas(bentuk):
    print(bentuk.luas())    # error saat runtime jika tidak ada luas()

# ABC — lebih aman, error saat instansiasi
from abc import ABC, abstractmethod
class Bentuk(ABC):
    @abstractmethod
    def luas(self): pass

# Protocol — untuk type checking (mypy, pyright)
from typing import Protocol
class BentukProtocol(Protocol):
    def luas(self) -> float: ...
```

**Panduan Memilih:**
- **Duck typing**: Codebase kecil, prototipe cepat, atau kelas independen
- **ABC**: Library/framework, tim besar, kontrak yang *harus* ditegakkan
- **Protocol**: Ingin type checking statis tanpa coupling hierarki pewarisan

---

## 11. Studi Kasus Ringkas — Sistem Plugin

Abstraksi sangat berguna dalam **arsitektur plugin**: inti sistem tidak tahu implementasi plugin, tapi tahu *kontrak* yang harus dipenuhi.

```python
from abc import ABC, abstractmethod


class EksporPlugin(ABC):
    """Kontrak yang harus dipenuhi oleh semua plugin ekspor."""

    @property
    @abstractmethod
    def format_file(self):
        """Kembalikan ekstensi file, misalnya 'csv', 'pdf', 'xlsx'."""
        pass

    @abstractmethod
    def ekspor(self, data, nama_file):
        """Ekspor data ke file dengan format tertentu."""
        pass

    def nama_file_lengkap(self, nama):
        return f"{nama}.{self.format_file}"


class EksporCSV(EksporPlugin):
    @property
    def format_file(self):
        return "csv"

    def ekspor(self, data, nama_file):
        path = self.nama_file_lengkap(nama_file)
        print(f"  [CSV] Menulis {len(data)} baris ke '{path}'")


class EksporJSON(EksporPlugin):
    @property
    def format_file(self):
        return "json"

    def ekspor(self, data, nama_file):
        import json
        path = self.nama_file_lengkap(nama_file)
        print(f"  [JSON] Menulis {json.dumps(data)[:50]}... ke '{path}'")


# Sistem inti tidak tahu implementasi detail plugin:
def jalankan_ekspor(plugin: EksporPlugin, data, nama):
    print(f"\n  Menggunakan plugin: {plugin.__class__.__name__}")
    plugin.ekspor(data, nama)


data = [{"nim": "2301001", "nama": "Budi"}, {"nim": "2301002", "nama": "Sari"}]
jalankan_ekspor(EksporCSV(),  data, "mahasiswa")
jalankan_ekspor(EksporJSON(), data, "mahasiswa")
```

---

## 12. Ringkasan

| Konsep | Sintaks | Kapan Dipakai |
|--------|---------|---------------|
| Kelas abstrak | `class X(ABC):` | Ingin mendefinisikan kontrak |
| Method abstrak | `@abstractmethod` | Method wajib diimplementasikan anak |
| Property abstrak | `@property` + `@abstractmethod` | Atribut wajib dengan getter/setter |
| Template Method | Method konkret memanggil method abstrak | Algoritma bertahap dengan variasi detail |
| Multiple interface | `class X(ABC1, ABC2):` | Objek punya banyak peran |
| Hierarki abstrak | Abstrak mewarisi abstrak | Kontrak bertingkat |

---

## Referensi Lanjutan

- [Python Docs — abc module](https://docs.python.org/3/library/abc.html)
- [Real Python — Abstract Base Classes in Python](https://realpython.com/python-interface/)
- [ArjanCodes — Abstract Classes in Python](https://www.youtube.com/c/ArjanCodes)
- Design Patterns: *Template Method* — GoF (Gamma et al.)
