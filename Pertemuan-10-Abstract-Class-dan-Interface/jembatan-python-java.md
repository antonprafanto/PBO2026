# 🌉 Jembatan Python ↔ Java Pertemuan 10: *Abstract Class* dan *Interface*

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Konsep kelas abstrak dan *interface* **sama** di Python dan Java: ada kerangka yang tidak bisa dibuat objeknya, ada *method* wajib yang harus diisi kelas anak, dan ada kontrak kemampuan untuk kelas yang tidak bersaudara. Yang berbeda adalah cara menuliskannya dan **kapan** pelanggarannya ketahuan. Halaman ini menjelaskan perbedaan itu beserta alasannya.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Menandai kelas abstrak | mewarisi `ABC` (dari modul `abc`) | kata kunci `abstract class` |
| *Method* abstrak | dekorator `@abstractmethod`, isinya cukup *docstring* atau `...` | `public abstract Tipe nama(...);` tanpa badan |
| Membuat objek kelas abstrak | `TypeError` saat baris itu **dijalankan** | *error* **kompilasi**: *is abstract; cannot be instantiated* |
| Kelas anak lupa mengisi *method* abstrak | `TypeError` saat objek kelas anak dibuat | *error* kompilasi: *is not abstract and does not override abstract method* |
| Kelas abstrak tanpa satu pun *method* abstrak | objeknya **boleh** dibuat | objeknya tetap **tidak boleh** dibuat |
| Konstruktor kelas anak | boleh tidak ditulis (`__init__` ikut diwariskan) | wajib ditulis jika induk tidak punya konstruktor tanpa parameter |
| *Interface* | kelas `ABC` yang berisi *method* abstrak saja | kata kunci `interface` |
| Memenuhi *interface* | ditulis di dalam kurung: `class Kedai(DapatDicetak):` | `class Kedai implements DapatDicetak` |
| Satu induk + banyak *interface* | `class Bebek(Hewan, BisaTerbang, BisaBerenang):` | `class Bebek extends Hewan implements BisaTerbang, BisaBerenang` |
| *Method* berisi di dalam *interface* | *method* biasa di dalam kelas `ABC` | *default method* (Java 8+) |
| *Method* pembantu milik *interface* | *method* biasa di dalam kelas `ABC` | *method* `static` (Java 8+) dan `private` (Java 9+) |
| Konstanta di *interface* | atribut kelas dengan nama `HURUF_BESAR` (kesepakatan) | *field* otomatis `public static final` |
| Kontrak struktural (tanpa mewarisi) | `typing.Protocol` | tidak ada |
| Melarang *override* *template method* | tidak dicegah saat berjalan; dekorator `typing.final` hanya dibaca alat pemeriksa tipe | `final` |
| Hak akses *method* yang mengisi *interface* | tidak ada aturan | wajib `public` |
| Memeriksa kemampuan | `isinstance(x, BisaTerbang)` | `x instanceof BisaTerbang` |

## 1. Kapan Pelanggaran Ketahuan?

Dua potongan berikut hanya ilustrasi (bukan program utuh). `Bentuk` adalah kelas abstrak seperti di contoh 02.

**Python:**

```python
print("Baris ini sempat tercetak")
bentuk = Bentuk()  # TypeError di sini, saat program berjalan
```

**Java:**

```java
System.out.println("Baris ini TIDAK sempat tercetak");
Bentuk bentuk = new Bentuk(); // ditolak saat kompilasi
```

| | Python | Java |
|---|---|---|
| Siapa yang memeriksa? | Python ketika objek dibuat | *compiler* (`javac`), sebelum program berjalan |
| Baris sebelum kesalahan | sudah sempat dijalankan | tidak ada yang dijalankan |
| Kesalahan di cabang `if` yang jarang dilewati | bisa lolos sampai suatu hari cabang itu dijalankan | tetap ketahuan saat kompilasi |

**Mengapa berbeda?** Python adalah bahasa bertipe **dinamis**: tipe diperiksa ketika program berjalan. Java bertipe **statis**: *compiler* memeriksa seluruh kode lebih dulu. Ini perbedaan yang sama dengan yang kamu temui di Pertemuan 02 (salah ketik nama atribut). Kelebihan Python: kode lebih ringkas. Kelebihan Java: kesalahan desain ketahuan lebih awal.

## 2. *Interface*: Kata Kunci Khusus atau Kesepakatan?

**Python:**

```python
class DapatDicetak(ABC):
    @abstractmethod
    def cetak(self):
        """Mencetak isi objek ke layar."""


class Kedai(DapatDicetak):
    ...
```

**Java:**

```java
// File DapatDicetak.java
public interface DapatDicetak {
    void cetak();
}

// File Kedai.java
public class Kedai implements DapatDicetak {
    // ...
}
```

**Mengapa berbeda?** Java hanya mengizinkan **satu** kelas induk. Supaya sebuah kelas tetap bisa punya banyak "tipe", Java menyediakan konsep terpisah, yaitu `interface`. Satu kelas boleh mengimplementasikan *interface* sebanyak apa pun. Python sejak awal mengizinkan banyak kelas induk sehingga tidak butuh kata kunci khusus. "*Interface*" di Python cukup berupa kelas `ABC` yang semua *method*-nya abstrak. Bedanya hanya pada **cara kita memakainya**, bukan pada aturan bahasanya.

## 3. Satu Induk, Banyak Kemampuan

**Python:**

```python
class Bebek(Hewan, BisaTerbang, BisaBerenang):
    ...
```

**Java:**

```java
class Bebek extends Hewan implements BisaTerbang, BisaBerenang {
    // ...
}
```

Di Python, semua ditulis di dalam satu kurung. Biasakan menulis kelas induk "jenis" lebih dulu, baru kontrak-kontraknya. Di Java, ada dua kata kunci dengan urutan tetap: `extends` (paling banyak satu kelas) lalu `implements` (boleh banyak *interface*).

## 4. *Default Method* dan Padanannya di Python

**Java** (potongan dari contoh 08, disederhanakan):

```java
interface BisaDinilai {
    int BINTANG_MAKS = 5;

    int totalBintang();
    int jumlahUlasan();

    default int rataRata() {
        if (jumlahUlasan() == 0) {
            return 0;
        }
        return totalBintang() / jumlahUlasan();
    }
}
```

**Python** (padanannya, sebagai ilustrasi):

```python
class BisaDinilai(ABC):
    BINTANG_MAKS = 5

    @abstractmethod
    def total_bintang(self) -> int: ...

    @abstractmethod
    def jumlah_ulasan(self) -> int: ...

    def rata_rata(self) -> int:  # method biasa = padanan default method
        if self.jumlah_ulasan() == 0:
            return 0
        return self.total_bintang() // self.jumlah_ulasan()
```

**Mengapa Java butuh kata `default`?** Sebelum Java 8, *interface* sama sekali tidak boleh berisi kode. Kata `default` ditambahkan agar *interface* yang sudah dipakai banyak kelas bisa diberi *method* baru tanpa merusak kelas-kelas itu. Di Python, kelas `ABC` sejak awal boleh berisi *method* biasa, jadi tidak perlu kata kunci khusus.

## 5. `typing.Protocol`: Hanya Ada di Python

Versi ringkas dari contoh 07 Python (tanpa *docstring* dan dekorator):

```python
class BisaBersuara(Protocol):
    def bersuara(self) -> str:
        ...


class Kucing:  # tidak menyebut BisaBersuara sama sekali
    def bersuara(self) -> str:
        return "Meong!"
```

Di Java, kelas **harus** menulis `implements BisaBersuara` agar dianggap memenuhi kontrak. Punya *method* `bersuara()` saja tidak cukup. Java memeriksa kontrak berdasarkan **pernyataan** tertulis (*nominal typing*), sedangkan `Protocol` memeriksa berdasarkan **bentuk** kelas (*structural typing*). `Protocol` adalah cara Python meresmikan *duck typing* yang sudah kamu kenal di Pertemuan 09. Pemeriksanya adalah alat pemeriksa tipe seperti Pylance atau mypy, bukan Python saat program berjalan. Di VS Code, pemeriksaan tipe Pylance perlu dinyalakan dulu (caranya ada di halaman praktik Python bagian 7).

## 6. Konstruktor di Kelas Anak

Versi ringkas kelas `Motor` dari contoh 03:

**Python:**

```python
class Motor(Kendaraan):
    def km_per_liter(self) -> int:
        return 40
```

**Java:**

```java
class Motor extends Kendaraan {
    public Motor(String plat, int bensinLiter) {
        super(plat, bensinLiter);
    }
    // ... kmPerLiter()
}
```

Di Python, `__init__` milik `Kendaraan` ikut diwariskan, jadi `Motor` tidak perlu menulisnya. Di Java, konstruktor **tidak** diwariskan, sehingga `Motor` wajib menulis konstruktor yang meneruskan data ke `super(...)`.

## Yang Sama di Kedua Bahasa

- Kelas abstrak dan *interface* tidak bisa dibuat objeknya.
- Kelas anak menjadi kelas konkret hanya jika **semua** *method* abstrak sudah diisi.
- Kelas abstrak boleh punya atribut, konstruktor, dan *method* konkret.
- Pola *template method* dan *hook* ditulis dengan cara yang sama: *method* konkret di kelas abstrak memanggil *method* abstrak.
- Variabel, parameter, dan *list* boleh bertipe kelas abstrak atau *interface*, lalu diisi objek kelas konkret (polimorfisme).
- `isinstance()`/`instanceof` bisa memeriksa kelas abstrak maupun *interface*.
- *Output* studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa menulis `public` saat mengisi *method interface* (*weaker access privileges*) |
| Python | Java | Memakai `extends` untuk *interface*, atau `implements` untuk kelas |
| Python | Java | Memberi badan `{ }` pada *method* `abstract`, atau lupa menandai kelasnya `abstract` |
| Python | Java | Lupa menulis konstruktor kelas anak yang memanggil `super(...)` |
| Java | Python | Menulis `@abstractmethod` tetapi lupa mewarisi `ABC`: tidak ada *error*, dekoratornya diam saja |
| Java | Python | Mengira kelas `ABC` tanpa *method* abstrak tidak bisa dibuat objeknya (ternyata bisa) |
| Java | Python | Mencari kata kunci `interface`, `implements`, atau `abstract` yang tidak ada di Python |
| Java | Python | Mengira `Protocol` diperiksa Python saat program berjalan |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
