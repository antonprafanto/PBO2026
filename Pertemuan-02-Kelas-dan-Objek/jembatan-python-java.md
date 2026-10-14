# 🌉 Jembatan Python ↔ Java Pertemuan 02: Kelas dan Objek

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Konsep kelas dan objek **sama persis** di Python dan Java: ada cetak biru, ada objek, ada atribut, ada *method*, ada konstruktor. Yang berbeda hanyalah **cara menuliskannya**. Halaman ini membantumu membaca kode di kedua bahasa dan menjelaskan *mengapa* perbedaan itu ada.

Potongan kode di halaman ini hanya untuk dibandingkan, tidak untuk dijalankan sendiri. Versi lengkap yang bisa dijalankan ada di folder `contoh/` dan `studi-kasus/` milik masing-masing bahasa.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Mendefinisikan kelas | `class Menu:` | `class Menu { ... }` |
| Badan kelas ditandai dengan | indentasi (spasi) | kurung kurawal `{ }` |
| Deklarasi atribut | tidak perlu, langsung diisi di `__init__` | wajib dideklarasikan beserta tipenya: `int harga;` |
| Konstruktor | *method* bernama `__init__` | nama sama dengan kelas, tanpa tipe kembalian |
| Kata ganti objek | `self` | `this` |
| Parameter `self`/`this` di *method* | wajib ditulis sebagai parameter pertama | tidak ditulis, tersedia otomatis |
| Membuat objek | `Menu("Kopi", 18000)` | `new Menu("Kopi", 18000)` |
| Tipe variabel objek | tidak ditulis: `kopi = ...` | ditulis: `Menu kopi = ...` |
| *Method* tanpa nilai kembalian | `def tampilkan_info(self):` | `void tampilkanInfo() { ... }` |
| *Method* dengan nilai kembalian | `def hitung_total(self, jumlah):` | `int hitungTotal(int jumlah) { ... }` |
| Gaya nama *method* | `snake_case` | `camelCase` |
| Cek "objek yang sama" | `a is b` | `a == b` |
| Nama kelas asal sebuah objek | `type(oyen).__name__` | `oyen.getClass().getSimpleName()` |
| Atribut belum diisi lalu dibaca | *error* `AttributeError` | nilai bawaan `null`, `0`, atau `false` |
| Menambah atribut baru dari luar kelas | bisa (tetapi sebaiknya dihindari) | tidak bisa, *error* kompilasi |
| Titik masuk program | `if __name__ == "__main__": main()` | `public static void main(String[] args)` |

## 1. `self` Wajib Ditulis, `this` Tersedia Otomatis

**Python:**

```python
class Menu:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

    def hitung_total(self, jumlah):
        return self.harga * jumlah
```

**Java:**

```java
class Menu {
    String nama;
    int harga;

    Menu(String nama, int harga) {
        this.nama = nama;
        this.harga = harga;
    }

    int hitungTotal(int jumlah) {
        return harga * jumlah;
    }
}
```

**Mengapa berbeda?** Python memegang prinsip "eksplisit lebih baik daripada implisit". Objek pemanggil dikirim sebagai parameter pertama secara terang-terangan sehingga `self` harus ditulis di setiap *method* **dan** setiap kali mengakses atribut. Java menyembunyikan objek pemanggil di balik kata kunci `this` yang selalu tersedia. Di dalam *method* Java, `harga` otomatis berarti `this.harga`, kecuali ada parameter yang bernama sama.

## 2. Atribut: Dideklarasikan atau Dibuat saat Diisi?

Di Java, semua *field* harus **didaftarkan di awal**, lengkap dengan tipenya. *Compiler* lalu bisa memeriksa bahwa kita tidak salah ketik nama atau salah memasukkan tipe data.

Di Python, atribut "lahir" saat pertama kali diisi, misalnya `self.harga = harga`. Fleksibel, tetapi kesalahan seperti salah ketik baru ketahuan saat program dijalankan.

| | Python | Java |
|---|---|---|
| Salah ketik `kopi.hrga` | ketahuan saat program **berjalan** (`AttributeError`) | ketahuan saat **kompilasi** (`cannot find symbol`) |
| Menulis `kopi.harga = "mahal"` | diterima; lalu `kopi.hitung_total(2)` menghasilkan `"mahalmahal"` | ditolak saat kompilasi (`incompatible types`) |

Inilah perbedaan mendasar **tipe dinamis** (Python) dan **tipe statis** (Java). Pada tipe dinamis, tipe data baru diperiksa saat program berjalan. Pada tipe statis, tipe data ditulis di kode dan diperiksa sebelum program berjalan. Keduanya punya kelebihan: Python lebih ringkas dan cepat ditulis, sedangkan Java lebih cepat menangkap kesalahan.

## 3. Kata Kunci `new`

**Python:**

```python
kopi = Menu("Kopi Susu Gula Aren", 18000)
```

**Java:**

```java
Menu kopi = new Menu("Kopi Susu Gula Aren", 18000);
```

Java mewajibkan `new` agar jelas bahwa sebuah objek **baru** sedang dibuat. Python cukup "memanggil" nama kelas seperti memanggil fungsi. Hasilnya sama: objek baru dibuat, konstruktor dijalankan, lalu objek disimpan ke variabel.

## 4. Konstruktor: `__init__` atau Nama Kelas

| | Python | Java |
|---|---|---|
| Nama | selalu `__init__` | sama dengan nama kelas (`Menu`) |
| Tipe kembalian | tidak ditulis | tidak ditulis (bukan `void`!) |
| Jika tidak ditulis | objek tetap bisa dibuat tanpa argumen | Java menyediakan konstruktor bawaan tanpa parameter |

> [!WARNING]
> Kesalahan klasik saat pindah dari Python ke Java: menulis `void Menu(...)`. Dengan `void`, Java menganggapnya *method* biasa, **bukan** konstruktor.

## 5. Satu *File*, Berapa Kelas?

- **Python:** satu *file* boleh berisi banyak kelas dan fungsi, dengan nama *file* bebas.
- **Java:** satu *file* boleh berisi banyak kelas, tetapi hanya **satu** yang boleh `public`, dan nama *file* harus sama dengan nama kelas `public` itu. Itu sebabnya *file* `KedaiKita.java` berisi `public class KedaiKita` dan kelas `Menu` tanpa kata `public`.

## Yang Sama di Kedua Bahasa

- Konsep kelas sebagai cetak biru dan objek sebagai wujud nyatanya.
- Satu kelas bisa menghasilkan banyak objek, dan setiap objek menyimpan datanya sendiri.
- Konstruktor berjalan otomatis saat objek dibuat.
- Notasi titik untuk membaca atribut dan memanggil *method*: `kopi.harga`, `kopi.hitung_total(2)` atau `kopi.hitungTotal(2)`.
- Nama kelas memakai *PascalCase*.
- *Output* studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa `new`, lupa titik koma `;`, lupa menulis tipe *field*, atau menulis `void` pada konstruktor |
| Python | Java | Membandingkan teks dengan `==` (di Java, gunakan `.equals()`; dibahas di Pertemuan 03) |
| Java | Python | Lupa menulis `self` sebagai parameter pertama *method* |
| Java | Python | Menulis `harga` padahal maksudnya `self.harga` (di Python, `self.` tidak pernah opsional) |
| Java | Python | Mencari kata kunci `new`, padahal Python tidak memakainya |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
