# 🌉 Jembatan Python ↔ Java Pertemuan 13: Prinsip SOLID

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Kelima prinsip SOLID **sama persis** di Python dan Java. Keduanya memakai kontrak, polimorfisme, dan *dependency injection* lewat konstruktor. Yang berbeda adalah **alat** untuk menulis kontrak dan **kapan** pelanggaran kontrak ketahuan. Halaman ini membantumu membaca kedua versi studi kasus dan memahami alasan perbedaannya.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Menulis kontrak | `class Diskon(ABC):` + `@abstractmethod` | `public interface Diskon { ... }` |
| Memenuhi kontrak | `class TanpaDiskon(Diskon):` | `class TanpaDiskon implements Diskon` |
| Memenuhi beberapa kontrak kecil | `class KasirLengkap(PencetakStruk, PemindaiBarcode, LaciUang):` | `class KasirLengkap implements PencetakStruk, PemindaiBarcode, LaciUang` |
| *Method* bantu milik kontrak | `@staticmethod` di ABC, **ikut diwariskan** | *method* `static` di *interface*, **tidak diwariskan** |
| *Method* berisi di dalam kontrak | *method* biasa di ABC | *method* `default` |
| Lupa menulis *method* wajib | `TypeError` saat objek dibuat | *compile error* |
| Menulis *method* dari kontrak | cukup nama yang sama | wajib `public`; `@Override` sangat dianjurkan |
| Menyuntikkan objek yang tidak memenuhi kontrak | diterima, *error* baru muncul saat *method* yang hilang dipanggil | ditolak *compiler*: `incompatible types` |
| Menolak "tidak didukung" (*code smell* LSP) | `raise NotImplementedError(...)` | `throw new UnsupportedOperationException(...)` |
| Impor melingkar | bisa terjadi (`ImportError`) | tidak terjadi |
| Pembagian bulat untuk rupiah | `//` (`/` menghasilkan `float`) | `/` pada dua `int` |
| Menyimpan *output* ke *file* | `python main.py > hasil.txt` | `java Main > hasil.txt` |

## 1. Kontrak: ABC atau *Interface*

Potongan berikut disederhanakan dari studi kasus (hanya satu *method* yang ditampilkan), jadi tidak untuk dijalankan sendiri.

**Python** (dari `diskon.py`):

```python
class Diskon(ABC):
    @abstractmethod
    def keterangan(self) -> str:
        """Nama singkat diskon untuk ditampilkan di struk."""


class TanpaDiskon(Diskon):
    def keterangan(self) -> str:
        return "Tanpa diskon"
```

**Java** (dari `Diskon.java` dan `TanpaDiskon.java`; di Java, setiap kelas `public` berada di *file*-nya sendiri):

```java
public interface Diskon {
    String keterangan();
}

public class TanpaDiskon implements Diskon {
    @Override
    public String keterangan() {
        return "Tanpa diskon";
    }
}
```

**Mengapa berbeda?** Python tidak punya kata kunci `interface`. Cara yang lazim adalah kelas abstrak turunan `ABC` yang *method*-nya abstrak (Pertemuan 10). Java punya `interface` khusus, dan semua *method* abstraknya otomatis `public`. Karena itu, *method* yang mengimplementasikannya juga wajib `public`. Lupa menulis `public` menghasilkan *error* *weaker access privileges* (lihat halaman praktik Java).

## 2. *Method* Bantu Milik Kontrak: Diwariskan atau Tidak?

`Diskon` di studi kasus punya *method* bantu untuk menjumlahkan subtotal. Kedua bahasa menulisnya di dalam kontrak, tetapi aturannya berbeda.

**Python** (`@staticmethod` di dalam ABC). Untuk mencobanya, buat *file* `coba_static.py` di salinan folder `studi-kasus/sesudah` milikmu (bukan di folder materi), lalu jalankan `python coba_static.py` dari folder itu:

```python
from diskon import Diskon, DiskonPersen

print(Diskon.subtotal_dari([]))
print(DiskonPersen.subtotal_dari([]))
print(DiskonPersen(10).subtotal_dari([]))
```

Ketiga baris `print` berjalan dan mencetak `0`. Di Python, `@staticmethod` ikut diwariskan sehingga bisa dipanggil lewat kelas induk, kelas anak, maupun objek.

**Java** (*method* `static` di dalam *interface*; potongan dari dalam `main`, dengan `daftar` bertipe `List<ItemPesanan>`):

```java
System.out.println(Diskon.subtotalDari(daftar));        // boleh
System.out.println(DiskonPersen.subtotalDari(daftar));  // ditolak compiler
```

Pesan *error* baris kedua: `cannot find symbol ... location: class DiskonPersen`. Memanggilnya lewat variabel objek juga ditolak: jika variabelnya bertipe `DiskonPersen`, pesannya `cannot find symbol`; jika bertipe `Diskon`, pesannya `illegal static interface method call`. Program lengkap untuk mencobanya ada di halaman praktik Java, bagian 8 (kesalahan 4).

**Mengapa berbeda?** Sebuah kelas Java boleh mengimplementasikan banyak *interface*. Jika dua *interface* punya *method* `static` bernama sama, mewariskan keduanya akan membingungkan. Secara sederhana, Java menghindari kebingungan itu dengan aturan tegas: *method* `static` milik *interface* hanya dipanggil lewat nama *interface*-nya. Kebiasaan ini sebenarnya juga baik di Python: tulis `Diskon.subtotal_dari(...)`, seperti di studi kasus, agar jelas milik siapa *method* itu.

## 3. *Method* Berisi di dalam Kontrak

`PenyimpananPesanan` punya *method* `jumlah()` yang sudah berisi sehingga kelas yang memenuhinya tidak perlu menulis ulang.

| | Python | Java |
|---|---|---|
| Cara menulis | *method* biasa (tanpa `@abstractmethod`) di dalam ABC | *method* bertanda `default` di dalam *interface* |
| Contoh | `def jumlah(self) -> int: return len(self.semua())` | `default int jumlah() { return semua().size(); }` |
| Boleh ditulis ulang di kelas anak? | boleh (*override*) | boleh (`@Override`) |

Konsepnya sama: kontrak boleh menyediakan perilaku bawaan yang dibangun di atas *method* abstraknya sendiri.

## 4. Kapan Kesalahan Penyuntikan Ketahuan?

Misalkan seseorang menyuntikkan objek `CatatanAsal` yang punya *method* `simpan()`, tetapi **tidak** mewarisi atau mengimplementasikan `PenyimpananPesanan`.

Kedua percobaan di bawah memakai kelas-kelas studi kasus. Jika ingin mencobanya, buat *file*-nya di salinan folder `studi-kasus/sesudah` milikmu, bukan di folder materi.

**Python** (*file* `salah4.py`):

```python
from kedai import Kedai
from pelanggan import Pelanggan


class CatatanAsal:
    def simpan(self, pesanan):
        print("disimpan")


kedai = Kedai("KedaiKita", CatatanAsal())
kedai.buat_pesanan(Pelanggan("Budi Santoso", "081234567890"))
print(kedai.jumlah_pesanan())
```

Python menerimanya. Pesanan bahkan sempat tersimpan karena `simpan()` memang ada. *Error* baru muncul saat `Kedai` memanggil *method* yang tidak dimiliki `CatatanAsal`. Hasilnya di Python 3.13 (tanda `~` dan `^` bisa berbeda di versi lain):

```text
disimpan
Traceback (most recent call last):
  File "salah4.py", line 12, in <module>
    print(kedai.jumlah_pesanan())
          ~~~~~~~~~~~~~~~~~~~~^^
  File "kedai.py", line 72, in jumlah_pesanan
    return self._penyimpanan.jumlah()
           ^^^^^^^^^^^^^^^^^^^^^^^^
AttributeError: 'CatatanAsal' object has no attribute 'jumlah'
```

**Java** (*file* `Coba.java`, dikompilasi dengan `javac *.java`):

```java
public class Coba {
    public static void main(String[] args) {
        Kedai kedai = new Kedai("KedaiKita", new CatatanAsal());
    }
}

class CatatanAsal {
    public void simpan(Pesanan pesanan) {
        System.out.println("disimpan");
    }
}
```

Java menolaknya sebelum program berjalan:

```text
Coba.java:3: error: incompatible types: CatatanAsal cannot be converted to PenyimpananPesanan
        Kedai kedai = new Kedai("KedaiKita", new CatatanAsal());
                                             ^
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
1 error
```

Baris `Note: ...` hanya catatan bahwa pesannya diringkas; inti *error*-nya ada di baris pertama.

**Mengapa berbeda?** Python memakai prinsip *duck typing* (Pertemuan 09): "jika ia bisa `simpan()`, anggap saja ia penyimpanan". Petunjuk tipe `penyimpanan: PenyimpananPesanan` tidak diperiksa saat program berjalan (Pertemuan 12). Java memeriksa tipe saat kompilasi sehingga hanya objek yang benar-benar mengimplementasikan `PenyimpananPesanan` yang boleh masuk.

> [!TIP]
> Di Python, biasakan kelas penyimpanan baru **mewarisi** ABC-nya, misalnya `class PenyimpananTerbatas(PenyimpananPesanan):`. Dengan begitu, *method* abstrak yang lupa ditulis langsung ketahuan saat objek dibuat (`TypeError`), dan *method* berisi seperti `jumlah()` ikut diwariskan. Hasilnya, Python ikut "menagih janji" kontrak lebih awal.

## 5. Impor Melingkar: Masalah Khas Python

Di versi Python, `ItemPesanan` harus dipindah ke `item_pesanan.py`. Jika tidak, `diskon.py` dan `pesanan.py` saling meng-*import* dan Python gagal dengan `ImportError: cannot import name 'Diskon' from partially initialized module 'diskon'` (bunyi persisnya berbeda mulai Python 3.13). Di versi Java, `Diskon` dan `Pesanan` saling menyebut tanpa masalah.

**Mengapa berbeda?** Saat meng-*import* sebuah *file*, Python **menjalankan** isinya dari atas ke bawah. Jika di tengah jalan ia diminta mengambil kelas dari *file* yang sedang setengah dijalankan, kelas itu belum ada. Java bekerja dengan cara lain: `javac *.java` membaca **semua** *file* sekaligus sebelum program berjalan sehingga kelas-kelas boleh saling merujuk. Penjelasan lengkap dan pesan *error* aslinya ada di [halaman praktik Python](python/README.md#mengapa-itempesanan-pindah-ke-file-sendiri).

## 6. Jebakan Pembagian saat *Refactoring*

Di halaman praktik, kami sengaja membuat satu kesalahan kecil pada `DiskonPersen` di masing-masing bahasa, lalu `diff` langsung menangkapnya:

| | Python | Java |
|---|---|---|
| Kode yang keliru | `subtotal * persen / 100` | `persen / 100 * subtotal` |
| Yang terjadi | `/` selalu menghasilkan `float`: tercetak `Rp6.150.0` | `15 / 100` pada `int` bernilai `0`: potongan hilang |
| Kode yang benar | `subtotal * persen // 100` | `subtotal * persen / 100` |

Jebakannya berbeda, tetapi cara membuktikannya sama: simpan *output* lama, jalankan versi baru, lalu bandingkan dengan `fc` atau `diff`.

## Yang Sama di Kedua Bahasa

- Kelima prinsip SOLID dan prinsip pendamping DRY, KISS, YAGNI.
- Pemisahan tugas studi kasus: `Kedai`, `Pesanan`, `Diskon` dan turunannya, `StrukPesanan`, `PenyimpananPesanan`.
- *Dependency injection* lewat konstruktor, dengan program utama sebagai tempat merakit objek.
- *Refactoring* dibuktikan dengan membandingkan *output*, dan *output* keempat program studi kasus (sebelum dan sesudah, Python dan Java) **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa `public` saat menulis *method* dari *interface* |
| Python | Java | Memanggil *method* `static` *interface* lewat kelas anak, misalnya `DiskonPersen.subtotalDari(...)` |
| Python | Java | Menulis `persen / 100 * subtotal` dan mengira hasilnya pecahan |
| Java | Python | Menganggap petunjuk tipe `penyimpanan: PenyimpananPesanan` akan menolak objek yang salah |
| Java | Python | Lupa mewarisi ABC sehingga *method* yang lupa ditulis baru ketahuan di tengah program |
| Java | Python | Menaruh dua kelas yang saling membutuhkan di dua *file* yang saling meng-*import* |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
