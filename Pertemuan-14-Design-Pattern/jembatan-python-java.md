# 🌉 Jembatan Python ↔ Java — Pertemuan 14: Design Pattern Dasar

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Design pattern adalah gagasan, bukan sintaks, jadi keempat pola hari ini **sama persis** di Python dan Java: perannya sama, nama kelasnya sama, bahkan output studi kasusnya identik. Yang berbeda adalah alat yang disediakan masing-masing bahasa. Halaman ini menunjukkan perbedaan itu dan menjelaskan *mengapa* ada.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Tempat objek Singleton | atribut kelas `_instance = None` | field `private static PengaturanKedai instance = null;` |
| Menutup konstruktor | tidak bisa; dipasang penjaga `raise RuntimeError` di `__init__` | konstruktor `private`, diperiksa *compiler* |
| Pintu masuk Singleton | `@classmethod` `get_instance(cls)` | method `public static getInstance()` |
| Singleton *eager* | objek tingkat modul: `pencatat = PencatatLog()` | `private static final PencatatLog INSTANCE = new PencatatLog();` |
| Singleton *lazy* aman untuk banyak *thread* | butuh kunci dari modul `threading` (tidak dibahas) | `public static synchronized ... getInstance()` |
| Method factory | `@staticmethod` | method `static` |
| Mengabaikan huruf besar/kecil | `jenis.lower() == "qris"` | `jenis.equalsIgnoreCase("qris")` |
| Menolak pilihan tak dikenal | `raise ValueError(...)` | `throw new IllegalArgumentException(...)` |
| Parameter factory yang opsional | nilai bawaan: `nominal: int = 0` | tidak ada; semua argumen dikirim |
| Kontrak Strategy dan Observer | kelas `ABC` + `@abstractmethod` | `interface` |
| Strategi yang sangat sederhana | fungsi biasa atau `lambda` | `lambda`, jika *interface*-nya hanya punya satu method abstrak |
| Daftar pengamat | `list[PengamatPesanan]` | `List<PengamatPesanan>` + `new ArrayList<>()` |
| Tipe parameter `perbarui()` di KedaiKita | tanpa petunjuk tipe (cegah impor melingkar) | `Pesanan pesanan` (aman) |
| Memeriksa objek yang sama | `a is b` | `a == b` |

## 1. Menutup Pintu Konstruktor

**Python:**

```python
class PengaturanKedai:
    _instance = None

    def __init__(self):
        if PengaturanKedai._instance is not None:
            raise RuntimeError("... Gunakan PengaturanKedai.get_instance()")
```

**Java:**

```java
public class PengaturanKedai {
    private static PengaturanKedai instance = null;

    private PengaturanKedai() {
        // ...
    }
```

**Mengapa berbeda?** Java punya *access modifier* `private` yang dijaga oleh *compiler*. Kode `new PengaturanKedai()` di kelas lain ditolak **sebelum** program berjalan. Python berpegang pada prinsip "kita semua orang dewasa": tidak ada yang benar-benar *private* (ingat Pertemuan 04). Penjaga di `__init__` baru bekerja **saat program berjalan**, dan hanya jika objek resminya sudah ada. Jika `PengaturanKedai()` dipanggil sebelum `get_instance()` yang pertama, objek liar tetap tercipta. Karena itu, di Python, Singleton lebih banyak bergantung pada **kesepakatan** tim.

## 2. Singleton *Eager*: Modul atau `static final`

**Python:**

```python
pencatat = PencatatLog()  # dibuat SEKALI saat modul dimuat
```

**Java:**

```java
private static final PencatatLog INSTANCE = new PencatatLog();
```

Keduanya membuat objek sekali di awal, tanpa pemeriksaan `None`/`null`. Di Python, sebuah modul hanya dijalankan sekali walaupun di-*import* berkali-kali, sehingga objek di dalamnya otomatis "tunggal". Inilah cara Singleton paling sederhana dan paling sering dipakai programmer Python. Bedanya, objek modul tidak mencegah siapa pun memanggil `PencatatLog()` lagi. Di Java, kombinasi konstruktor `private` dan field `static final` menjamin objeknya benar-benar satu. Pengisian field `static` juga dijamin Java hanya terjadi sekali, sehingga versi *eager* otomatis aman untuk banyak *thread*.

Python juga punya variasi lewat `__new__`, method yang benar-benar membuat objek. Java tidak punya padanannya, karena `new` di Java **selalu** membuat objek baru. Jebakan `__new__`: Python tetap memanggil `__init__` setiap kali `Tema()` ditulis, jadi perlu penjaga agar data tidak ter-*reset*.

## 3. Strategi Tidak Harus Berupa Kelas

Jika sebuah strategi hanyalah satu rumus, kedua bahasa punya jalan pintas.

**Python** (fungsi adalah objek, jadi bisa dikirim sebagai argumen):

```python
def hitung_ongkir(berat_kg: int, rumus) -> int:
    return rumus(berat_kg)


def ongkir_kilat(berat_kg: int) -> int:
    return 15000 * berat_kg + 5000


print(hitung_ongkir(2, ongkir_kilat))                # 35000
print(hitung_ongkir(2, lambda b: 5000 * max(b, 3)))  # 15000
```

**Java** (*lambda* untuk *interface* yang hanya punya satu method abstrak):

```java
interface RumusOngkir {
    int hitung(int beratKg);
}

static int hitungOngkir(int beratKg, RumusOngkir rumus) {
    return rumus.hitung(beratKg);
}

hitungOngkir(2, berat -> 15000 * berat + 5000);      // 35000
hitungOngkir(2, berat -> 5000 * Math.max(berat, 3)); // 15000
```

**Mengapa KedaiKita tetap memakai kelas?** Kontrak `Diskon` punya **dua** method abstrak, `hitung_potongan()` dan `keterangan()`, begitu pula `StrategiOngkir` (`hitung()` dan `nama()`). Fungsi atau *lambda* hanya bisa mewakili satu method. Selain itu, kelas bisa menyimpan data sendiri, seperti `persen` di `DiskonPersen`.

Kamu sebenarnya sudah memakai strategi kecil sejak Pertemuan 12: `key=` pada `sorted()` di Python dan `Comparator` pada `sort()` di Java. Aturan urutannya bisa ditukar tanpa mengubah algoritma pengurutannya. Itulah Strategy!

## 4. Impor Melingkar: Masalah Khusus Python

Di KedaiKita, `Pesanan` memakai `PengamatPesanan`, dan `PengamatPesanan` menerima `Pesanan`. Kedua kelas saling menyebut.

| | Python | Java |
|---|---|---|
| Kapan nama kelas lain "dicari" | saat baris `import` **dijalankan**, dari atas ke bawah | saat **kompilasi**, semua file dibaca bersama oleh `javac *.java` |
| Jika dua file saling menyebut | gagal: `ImportError ... partially initialized module` | tidak masalah |
| Solusi di KedaiKita | `pengamat.py` tidak meng-*import* `pesanan.py`; parameter `pesanan` tanpa petunjuk tipe | `void perbarui(Pesanan pesanan);` ditulis apa adanya |

Di Python, `import` adalah perintah yang benar-benar dijalankan. Saat `pesanan.py` baru setengah dimuat lalu meng-*import* `pengamat.py`, dan `pengamat.py` balik meminta `Pesanan`, kelas itu belum ada. Java tidak menjalankan apa pun saat kompilasi; ia cukup mengumpulkan semua nama kelas dulu, baru memeriksa pemakaiannya.

## 5. Hasil Factory dan Method Khusus Subclass

Factory mengembalikan tipe abstrak (`Pembayaran`). Bagaimana jika kamu butuh `kembalian`, yang hanya dimiliki `PembayaranTunai`?

**Python:**

```python
pembayaran = PembayaranFactory.buat("tunai", 100000)
pembayaran.proses(67100)
print(pembayaran.kembalian)  # jalan: objek aslinya memang PembayaranTunai
```

**Java:**

```java
Pembayaran pembayaran = PembayaranFactory.buat("tunai", 100000, "");
System.out.println(pembayaran.getKembalian()); // error kompilasi: cannot find symbol
```

**Mengapa berbeda?** Python memeriksa atribut saat program berjalan, berdasarkan objek yang **sebenarnya**. Petunjuk tipe `-> Pembayaran` hanya catatan bagi pembaca dan editor. Java memeriksa saat kompilasi, berdasarkan **tipe variabel**. Di Java, kamu perlu `instanceof` lalu *cast*: `((PembayaranTunai) pembayaran).getKembalian()`. Kebebasan Python ini nyaman, tetapi kesalahan seperti salah ketik nama atribut baru ketahuan saat baris itu dijalankan.

## Yang Sama di Kedua Bahasa

- Keempat pola punya peran yang sama: Singleton (objek tunggal + satu pintu), Factory (pembuat objek), Strategy (*context* + strategi yang bisa ditukar), Observer (*subject* + daftar pengamat).
- Singleton *lazy* memakai pola yang sama: periksa kosong, buat jika perlu, kembalikan objek yang tersimpan.
- Factory mengembalikan tipe **abstrak**, sehingga pemanggil tidak bergantung pada kelas konkret.
- *Context* Strategy menyimpan strategi di atribut/field dan mendelegasikan pekerjaan kepadanya.
- *Subject* Observer menyusuri daftar pengamat dan memanggil `perbarui(self)` / `perbarui(this)`. Keduanya memakai gaya **pull**.
- Uang tetap bilangan bulat, pajak dihitung dengan pembagian bulat, dan output studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan Saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa `static` pada `getInstance()`, sehingga muncul *non-static method cannot be referenced from a static context* |
| Python | Java | Memanggil method khusus subclass pada hasil factory, sehingga muncul *cannot find symbol*; perlu `instanceof` dan *cast* |
| Python | Java | Membandingkan pilihan teks dengan `==`; gunakan `equals()` atau `equalsIgnoreCase()` |
| Python | Java | Mencari nilai bawaan parameter untuk factory; di Java semua argumen harus dikirim |
| Java | Python | Mengira konstruktor bisa ditutup; panggilan `PengaturanKedai()` sebelum `get_instance()` menciptakan objek liar |
| Java | Python | Menulis petunjuk tipe yang membuat dua modul saling meng-*import*, sehingga muncul `ImportError` |
| Java | Python | Lupa bahwa Singleton lewat `__new__` tetap menjalankan `__init__` di setiap pemanggilan |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
