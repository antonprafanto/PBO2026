# 🌉 Jembatan Python ↔ Java — Pertemuan 03: Atribut dan Method Lebih Dalam

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Konsep pertemuan ini **sama** di kedua bahasa: ada atribut milik bersama, ada method yang tidak butuh objek, ada konstruktor yang luwes, ada representasi teks, dan variabel selalu menyimpan referensi. Yang berbeda adalah **cara menuliskannya**. Di satu tempat, yaitu mengubah atribut kelas lewat objek, **perilakunya** pun berbeda. Halaman ini menjelaskan perbedaan itu beserta alasannya.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Atribut kelas | ditulis di badan kelas: `jumlah_menu = 0` | kata kunci `static`: `static int jumlahMenu = 0;` |
| Mengubah atribut kelas | `Menu.jumlah_menu += 1` | `Menu.jumlahMenu += 1;` |
| Mengisi atribut kelas lewat objek | membuat atribut objek baru (bayangan) | tetap mengubah nilai bersama (menyesatkan) |
| Konstanta milik kelas | huruf kapital (kesepakatan): `NAMA_BULAN = [...]` | `static final String[] NAMA_BULAN = {...};` |
| Method tanpa objek | `@staticmethod` | method `static` |
| Konstruktor alternatif | `@classmethod` + `return cls(...)` | method `static` + `return new Tanggal(...);` |
| Fungsi di luar kelas | boleh: `format_rupiah()` | tidak boleh: kelas utilitas `Rupiah.format()` |
| Nilai bawaan parameter | `stok=0` | tidak ada; pakai *overloading* + `this(...)` |
| Argumen bernama | `Laptop("HP", penyimpanan=256)` | tidak ada |
| *Overloading* | tidak ada (`def` kedua menimpa yang pertama) | ada, untuk konstruktor dan method |
| Representasi teks | `def __str__(self):` | `@Override public String toString()` |
| Objek yang sama? | `a is b` | `a == b` |
| Isi sama? | `a == b` | `a.equals(b)` |
| Membandingkan teks | `==` | `.equals()` |
| Tidak menunjuk objek | `None`, diperiksa dengan `x is None` | `null`, diperiksa dengan `x == null` |
| Memanggil method lewat variabel kosong | `AttributeError: 'NoneType' object ...` | `NullPointerException` |
| Contoh nama method boolean | `stok_cukup()`, `kabisat()` | `stokCukup()`, `isKabisat()` |

## 1. Atribut Kelas: Dua Kejutan yang Berlawanan

Kode berikut terlihat setara, tetapi hasilnya berbeda.

**Python:**

```python
class Pengunjung:
    total = 0

    def masuk(self):
        self.total += 1
```

**Java:**

```java
class Pengunjung {
    static int total = 0;

    void masuk() {
        this.total += 1;
    }
}
```

Setelah `ayu.masuk()` dan `bima.masuk()` dijalankan:

| | Python | Java |
|---|---|---|
| Total milik kelas | `0` (tidak berubah!) | `2` |
| `ayu.total` | `1` (atribut objek baru milik `ayu`) | `2` (nilai bersama) |
| Kejutannya | nilai bersama **tidak** bertambah | tulisan `this.total` terlihat seperti milik objek, padahal milik bersama |

**Mengapa berbeda?** Di Python, objek itu luwes: mengisi `objek.atribut = nilai` **selalu** menyimpan atribut di objek itu, dan atribut baru boleh lahir kapan saja. Ingat `oyen.nama = "Oyen"` di Pertemuan 02. Jadi `self.total += 1` membaca total milik kelas, lalu menyimpan hasilnya sebagai atribut **baru** milik objek. Di Java, daftar field sudah pasti sejak kompilasi dan field `static` hanya ada **satu**. Objek tidak mungkin punya `total` sendiri, sehingga compiler mengartikan `this.total` sebagai `Pengunjung.total`.

Kedua bahasa konsisten dengan aturannya masing-masing. Kebiasaan yang aman di keduanya sama: **ubah atribut kelas selalu lewat nama kelas**. Program lengkapnya ada di [`contoh02_jebakan_atribut_kelas.py`](python/contoh/contoh02_jebakan_atribut_kelas.py) dan [`Contoh02AksesStatic.java`](java/contoh/Contoh02AksesStatic.java). Jalankan keduanya dan bandingkan outputnya.

## 2. Tiga Jenis Method di Python, Dua di Java

**Python:**

```python
@staticmethod
def kabisat(tahun):
    return (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0

@classmethod
def dari_teks(cls, teks):
    hari, bulan, tahun = teks.split("-")
    return cls(int(hari), int(bulan), int(tahun))
```

**Java:**

```java
static boolean isKabisat(int tahun) {
    return (tahun % 4 == 0 && tahun % 100 != 0) || tahun % 400 == 0;
}

static Tanggal dariTeks(String teks) {
    String[] bagian = teks.split("-");
    int hari = Integer.parseInt(bagian[0]);
    int bulan = Integer.parseInt(bagian[1]);
    int tahun = Integer.parseInt(bagian[2]);
    return new Tanggal(hari, bulan, tahun);
}
```

**Mengapa berbeda?** Java hanya punya satu jenis method milik kelas, yaitu method `static`. Untuk membuat objek, method `static` cukup menulis nama kelasnya: `new Tanggal(...)`. Python membedakan dua jenis. `@staticmethod` tidak menerima apa pun secara otomatis. `@classmethod` menerima **kelasnya sendiri** sebagai `cls`, karena di Python kelas juga sebuah objek yang bisa dikirim sebagai argumen. Manfaat `cls` baru terasa saat pewarisan di Pertemuan 07.

## 3. `format_rupiah()` atau `Rupiah.format()`?

Studi kasus KedaiKita menampilkan uang dengan dua cara yang terlihat berbeda:

**Python:**

```python
def format_rupiah(angka):
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")

print(format_rupiah(18000))
```

**Java:**

```java
class Rupiah {
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

System.out.println(Rupiah.format(18000));
```

**Mengapa berbeda?**

- **Python boleh punya fungsi di luar kelas.** File Python (modul) bisa berisi kelas **dan** fungsi biasa. `format_rupiah()` tidak membutuhkan data objek dan dipakai oleh banyak bagian program, jadi paling sederhana ditulis sebagai fungsi biasa.
- **Java mewajibkan setiap method berada di dalam kelas.** Di Java 17, menulis method di luar kelas langsung ditolak compiler dengan pesan `class, interface, enum, or record expected`. Karena itu kita membuat **kelas utilitas** `Rupiah` yang hanya berisi method `static`, sama seperti kelas bawaan `Math` (`Math.max`) atau `Integer` (`Integer.parseInt`).
- **Namanya enak dibaca.** Nama kelas menjadi "awalan" yang menjelaskan isi method: `Rupiah.format(18000)` dibaca "format sebagai rupiah". Itulah sebabnya method-nya cukup bernama `format`.
- **Format angkanya juga berbeda perilakunya.** Di Python, `{angka:,}` **selalu** memakai koma, apa pun pengaturan bahasa komputermu. Di Java, `%,d` mengikuti pengaturan bahasa (*locale*) komputer: di komputer berbahasa Indonesia hasilnya `18.000`, di komputer berbahasa Inggris (AS) `18,000`, dan di komputer berbahasa Prancis pemisahnya malah berupa karakter spasi khusus. Karena itu Java mengunci formatnya ke `Locale.US` (selalu koma) lalu menggantinya dengan titik. Hasil akhir kedua bahasa jadi **identik** di komputer mana pun.

> [!NOTE]
> Java 25 memperkenalkan *compact source file*: program kecil boleh ditulis dengan method tanpa deklarasi kelas. Namun, di balik layar method itu tetap dimasukkan ke dalam sebuah kelas yang dibuat otomatis. Di mata kuliah ini kita tetap memakai gaya Java 17: semua method berada di dalam kelas.

## 4. Nilai Bawaan atau Overloading?

**Python:**

```python
class Menu:
    def __init__(self, kode, nama, harga, kategori, stok=0):
        ...
```

**Java:**

```java
Menu(String kode, String nama, int harga, String kategori, int stok) { ... }

Menu(String kode, String nama, int harga, String kategori) {
    this(kode, nama, harga, kategori, 0);
}
```

**Mengapa berbeda?** Java memilih konstruktor (dan method) berdasarkan **jumlah dan tipe** argumen saat kompilasi, sehingga beberapa versi bernama sama bisa hidup berdampingan. Python tidak mencatat tipe parameter, jadi sebuah nama di dalam kelas hanya bisa menunjuk **satu** fungsi. Jika kamu menulis dua `def __init__`, yang kedua menimpa yang pertama. Misalnya `__init__(self, merek)` lalu `__init__(self, merek, ram)`, maka `Laptop("Asus")` gagal:

```text
TypeError: Laptop.__init__() missing 1 required positional argument: 'ram'
```

Sebaliknya, Java tidak punya nilai bawaan dan argumen bernama, jadi keluwesannya didapat lewat *overloading*. Kedua cara menghasilkan objek yang sama; perbedaannya hanya di cara menulis. *Overloading* akan dibahas lagi di Pertemuan 09.

## 5. `__str__` atau `toString()`?

| | Python `__str__` | Java `toString()` |
|---|---|---|
| Penulisan | `def __str__(self):` | `@Override public String toString()` |
| Dipanggil otomatis oleh | `print(obj)`, `str(obj)`, f-string | `println(obj)`, `"teks" + obj` |
| Jika tidak dibuat | `<__main__.Motor object at 0x...>` | `Motor@130f889` |
| Wajib mengembalikan | teks (`str`) | teks (`String`) |
| Aturan tambahan | tidak ada | wajib `public`; `@Override` sangat dianjurkan |
| Pasangan untuk programmer | `__repr__` (dipakai saat list dicetak) | cukup `toString()` |

**Mengapa Java butuh `@Override` dan `public`?** Di Java, `toString()` sudah ada sejak awal di kelas `Object`, induk dari semua kelas, dan bersifat `public`. Membuat `toString()` sendiri berarti **menimpa** versi itu, dan Java melarang penimpa punya hak akses yang lebih sempit. Python tidak punya aturan hak akses seperti itu (dibahas di Pertemuan 04), jadi cukup menulis `def __str__(self):`.

## 6. Membandingkan Objek dan Teks

| Pertanyaan | Python | Java |
|---|---|---|
| Apakah objeknya sama? | `a is b` | `a == b` |
| Apakah isinya sama? | `a == b` | `a.equals(b)` |
| Apakah dua teks sama? | `nama == "Kopi"` | `nama.equals("Kopi")` |
| Apakah variabel kosong? | `x is None` | `x == null` |

Perhatikan bahwa operator `==` punya arti **berbeda** di kedua bahasa. Di Python, `==` menanyakan isi. Di Java, `==` pada objek menanyakan apakah objeknya sama. Itulah sebabnya teks di Java wajib dibandingkan dengan `.equals()`. Untuk kelas buatan sendiri, "isi sama" di kedua bahasa secara bawaan masih berarti "objek yang sama". Cara mengubahnya (`__eq__` dan `equals()`) dibahas di Pertemuan 12.

## Yang Sama di Kedua Bahasa

- Atribut kelas hanya ada satu dan dipakai bersama; cara aman mengubahnya adalah lewat nama kelas.
- Method milik kelas dipanggil lewat nama kelas, tanpa objek, dan tidak bisa memakai `self`/`this`.
- Konstruktor alternatif adalah method milik kelas yang mengembalikan objek baru.
- Variabel menyimpan **referensi**. `b = a` membuat *aliasing*, bukan salinan objek.
- Method bisa mengubah isi objek yang dikirim sebagai parameter, tetapi tidak bisa mengganti objek yang dipegang variabel pemanggil.
- Method boleh mengembalikan objek baru, misalnya `Durasi.tambah()`.
- Representasi teks dipanggil otomatis saat objek dicetak dan harus **mengembalikan** teks.
- Uang selalu bilangan bulat, dan output studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan Saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Mencari nilai bawaan `stok=0`, padahal Java memakai *overloading* dan `this(...)` |
| Python | Java | Menulis `toString()` tanpa `public`, atau salah ketik tanpa `@Override` |
| Python | Java | Membandingkan teks dengan `==`, padahal harus `.equals()` |
| Python | Java | Menulis fungsi di luar kelas, padahal Java 17 mewajibkan semuanya di dalam kelas |
| Python | Java | Memanggil method objek langsung dari `main` yang `static` |
| Java | Python | Menulis dua `__init__` untuk *overloading*; yang kedua menimpa yang pertama |
| Java | Python | Mengubah atribut kelas dengan `self.x += 1`, sehingga lahir atribut bayangan |
| Java | Python | Lupa `@staticmethod`, lalu method tanpa `self` gagal saat dipanggil lewat objek |
| Java | Python | Memakai `is` untuk membandingkan isi teks atau angka; `is` hanya untuk "objek yang sama" dan `None` |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
