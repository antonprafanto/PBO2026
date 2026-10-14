# 🌉 Jembatan Python ↔ Java — Pertemuan 04: Enkapsulasi

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Tujuan enkapsulasi **sama persis** di Python dan Java: data disembunyikan, pihak luar memakai pintu resmi, dan data yang tidak masuk akal ditolak. Yang berbeda adalah **siapa yang menjaga aturannya** dan **bagaimana pintu itu ditulis**. Halaman ini membantumu membaca kode di kedua bahasa, dan menjelaskan *mengapa* perbedaan itu ada.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Menandai data internal | `self._harga` (kesepakatan) | `private int harga;` (dijaga compiler) |
| Tingkat akses yang tersedia | publik dan "internal" (lewat nama) | `public`, `protected`, *default*, `private` |
| Kode luar menyentuh data internal | tetap berjalan, tetapi melanggar kesepakatan | ditolak saat kompilasi: `has private access` |
| Nama berawalan dua garis bawah `__x` | *name mangling* menjadi `_Kelas__x` | tidak ada padanannya |
| Getter | `@property` + `def harga(self)` | `public int getHarga()` |
| Setter | `@harga.setter` + `def harga(self, nilai)` | `public void setHarga(int harga)` |
| Memakai getter | `kopi.harga` | `kopi.getHarga()` |
| Memakai setter | `kopi.harga = 20000` | `kopi.setHarga(20000)` |
| Getter bernilai ya/tidak | `parkiran.penuh` | `parkiran.isPenuh()` |
| Read-only | property tanpa setter | getter tanpa setter (bisa ditambah `final`) |
| Mengubah data read-only | `AttributeError` saat program berjalan | error kompilasi `cannot find symbol` |
| Menolak data | `raise ValueError("...")` | `throw new IllegalArgumentException("...");` |
| Menangkap (intip, detail di Pertemuan 11) | `try: ... except ValueError as e:` | `try { ... } catch (IllegalArgumentException e) { ... }` |
| Membaca pesan exception | `f"{e}"` atau `str(e)` | `e.getMessage()` |
| Atribut kelas privat | `_jumlah_menu = 0` | `private static int jumlahMenu = 0;` |
| Getter milik kelas | `@classmethod` + `def jumlah_menu(cls)` | `public static int getJumlahMenu()` |
| Method internal | `def _periksa_password(self, ...)` | `private void periksaPassword(...)` |

## 1. Dijaga Compiler atau Dijaga Kesepakatan?

**Python:**

```python
aman = TabunganAman("Siti", 500000)
aman._saldo = 999999999   # berjalan tanpa error, tetapi melanggar kesepakatan
```

**Java:**

```java
TabunganAman aman = new TabunganAman("Siti", 500000);
aman.saldo = 999999999;   // error: saldo has private access in TabunganAman
```

**Mengapa berbeda?** Java menekankan pemeriksaan ketat oleh compiler, sehingga pelanggaran aturan akses sudah ketahuan sebelum program berjalan. Pemeriksaan seperti ini sangat membantu pada proyek besar yang dikerjakan banyak orang.

Python memegang prinsip bahwa programmer adalah orang dewasa yang bertanggung jawab. Garis bawah adalah rambu "dilarang masuk", bukan gembok. Keduanya punya tujuan yang sama: mengarahkan programmer agar memakai pintu resmi.

## 2. Name Mangling: Fitur Khusus Python

Contoh 02 di jalur Python menunjukkan bahwa `self.__pin` diam-diam disimpan sebagai `_Brankas__pin`. Java tidak punya fitur seperti ini, sehingga contoh 02 di jalur Java membahas `private` + getter sebagai padanannya.

| | Python `__pin` | Java `private String pin;` |
|---|---|---|
| Apa yang terjadi | Namanya diganti menjadi `_Brankas__pin` | Nama tetap, aksesnya dibatasi |
| Bisa dibaca dari luar? | Bisa, lewat nama barunya | Tidak, ditolak compiler |
| Tujuan utamanya | Mencegah bentrok nama pada pewarisan | Membatasi akses |

> [!WARNING]
> Jika kamu berasal dari Java, jangan menganggap `__harga` sebagai "versi Python dari `private`". Kebiasaan Python adalah satu garis bawah (`_harga`) ditambah *property*.

## 3. Property vs Getter dan Setter

**Python:**

```python
tv.volume = 25            # setter bekerja di balik layar
tv.volume += 10           # getter lalu setter
print(tv.volume)          # getter
```

**Java:**

```java
tv.setVolume(25);
tv.setVolume(tv.getVolume() + 10);
System.out.println(tv.getVolume());
```

**Mengapa berbeda?** Di Python, membaca atribut biasa dan membaca property ditulis **sama persis**: `kopi.harga`. Jadi kelas boleh dimulai dengan atribut biasa, lalu diubah menjadi property saat butuh validasi, tanpa mengubah satu baris pun di kode pemakainya. Itulah yang terjadi pada KedaiKita dari Pertemuan 03 ke 04.

Di Java, membaca field (`kopi.harga`) dan memanggil method (`kopi.getHarga()`) ditulis berbeda. Jika kelak sebuah field publik perlu divalidasi, semua kode pemakainya harus diubah. Karena itu, programmer Java terbiasa menyiapkan getter dan setter sejak awal untuk data yang memang perlu dibaca atau diubah dari luar.

## 4. Menolak dan Menangkap

**Python:**

```python
if nilai <= 0:
    raise ValueError("Harga harus lebih dari 0")

try:
    es_teh.harga = -5000
except ValueError as e:
    print(f"Gagal mengubah harga: {e}")
```

**Java:**

```java
if (harga <= 0) {
    throw new IllegalArgumentException("Harga harus lebih dari 0");
}

try {
    esTeh.setHarga(-5000);
} catch (IllegalArgumentException e) {
    System.out.println("Gagal mengubah harga: " + e.getMessage());
}
```

- Python memakai kata `raise`, Java memakai `throw`. Di Java, exception adalah objek yang dibuat dengan `new`. Di Python juga objek, hanya saja Python memang tidak memakai kata `new`.
- `ValueError` (Python) dan `IllegalArgumentException` (Java) sama-sama exception bawaan untuk "nilai atau argumen yang tidak sah".
- Pesan exception dibaca dengan `f"{e}"` di Python dan `e.getMessage()` di Java.
- Java punya pembagian *checked* dan *unchecked exception* yang tidak ada di Python. `IllegalArgumentException` termasuk *unchecked*, jadi method yang melemparnya tidak wajib mencantumkan klausa `throws`. Semua ini dibahas di Pertemuan 11.

## 5. Read-Only dan final

| | Python | Java |
|---|---|---|
| Membuat read-only dari luar | property **tanpa** setter | getter **tanpa** setter |
| Mencegah perubahan dari dalam kelas juga | tidak ada mekanisme yang dijaga saat program berjalan | tambahkan `final` pada field |
| Jika dilanggar | `AttributeError: property 'nik' of 'Penduduk' object has no setter` | `cannot find symbol` (tidak ada setter) atau `cannot assign a value to final variable nik` |

Di Java, `final` adalah lapisan pengaman tambahan untuk data yang tidak pernah berubah, seperti NIK atau kode menu.

## 6. Atribut Kelas yang Dilindungi

**Python:**

```python
class Menu:
    _jumlah_menu = 0

    @classmethod
    def jumlah_menu(cls):
        return cls._jumlah_menu

print(Menu.jumlah_menu())
```

**Java:**

```java
class Menu {
    private static int jumlahMenu = 0;

    public static int getJumlahMenu() {
        return jumlahMenu;
    }
}

System.out.println(Menu.getJumlahMenu());
```

Keduanya dipanggil lewat **nama kelas**. Di Python, `@classmethod` menerima kelasnya sebagai parameter `cls`. Di Java, method `static` langsung memakai field `static` tanpa perlu parameter tambahan.

## Yang Sama di Kedua Bahasa

- Prinsip enkapsulasi: data disembunyikan, pihak luar memakai pintu resmi.
- Validasi ditulis di setter, lalu konstruktor **memanggil setter** agar aturannya berlaku sejak objek lahir.
- Data read-only cukup diberi getter, tanpa setter.
- Perubahan yang punya makna (restok, terjual, setor) memakai **method penjaga aturan**, bukan setter.
- Penghitung milik kelas dibuat privat dan dinaikkan paling akhir di konstruktor.
- Prinsip ***tell, don't ask***: suruh objek bekerja, jangan ambil datanya lalu putuskan di luar.
- Output studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan Saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Menulis `kopi.harga` dan mengira getter terpanggil. Di Java itu akses field langsung, dan ditolak karena `private` |
| Python | Java | Lupa tanda kurung pada getter: `kopi.getHarga` (error `cannot find symbol`) |
| Python | Java | Menamai getter boolean dengan `getPenuh()`. Kesepakatan Java adalah `isPenuh()` |
| Python | Java | Membandingkan teks dengan `==`. Gunakan `.equals()`, misalnya saat memeriksa PIN atau password |
| Java | Python | Menulis `get_harga()` dan `set_harga()`. Gaya Python adalah *property* |
| Java | Python | Mengira `_harga` atau `__harga` benar-benar terkunci. Keduanya tetap bisa diakses |
| Java | Python | Di dalam setter menulis `self.harga = nilai`, sehingga setter memanggil dirinya sendiri (`RecursionError`). Tulis `self._harga = nilai` |
| Java | Python | Memanggil property dengan tanda kurung: `kopi.harga()` (error `'int' object is not callable`) |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
