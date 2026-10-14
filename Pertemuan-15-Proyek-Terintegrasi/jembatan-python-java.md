# 🌉 Jembatan Python ↔ Java — Pertemuan 15: Proyek Terintegrasi

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Arsitektur berlapis, *package*, file CSV, validasi input, dan *unit test* adalah konsep yang **sama** di kedua bahasa. Buktinya, KedaiKita versi Python dan Java mencetak output mode demo yang sama persis, baris demi baris. Yang berbeda adalah alat-alatnya: Python membawa banyak alat siap pakai (`csv`, `unittest`), sedangkan Java lebih ketat soal *package* dan *exception*.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Penanda *package* | folder berisi `__init__.py` | `package kedaikita;` di setiap file + folder bernama sama |
| Memakai kelas dari *package* | `from kedaikita.menu import Menu` | `import kedaikita.Menu;` (sesama *package*: tanpa `import`) |
| Menjalankan proyek | `python main.py --demo` | `javac -d out src/kedaikita/*.java` lalu `java -cp out kedaikita.Main --demo` |
| Lokasi folder data | `Path(__file__).resolve().parent / "data"` | `Path.of("data")`, relatif terhadap folder kerja |
| Menyusun path | `Path(folder) / "menu.csv"` | `folder.resolve("menu.csv")` |
| Menulis / menambah teks | `open(p, "w")` / `open(p, "a")` + `encoding="utf-8"` | `Files.writeString(p, teks, UTF_8)` / `+ StandardOpenOption.APPEND` |
| Membaca semua isi | `berkas.read()` atau `p.read_text(encoding="utf-8")` | `Files.readString(p, UTF_8)` |
| Membaca per baris | `for baris in berkas:` (baris masih berisi `"\n"`) | `Files.readAllLines(p, UTF_8)` (tanpa `"\n"`) |
| CSV | modul `csv` (paham tanda kutip) | `String.join(";", ...)` dan `split(";", -1)` |
| Menutup otomatis | `with ... as x:` | `try (Tipe x = ...) { ... }` |
| Sumber daya buatan sendiri | `__enter__()` dan `__exit__()` | `implements AutoCloseable` + `close()` |
| File tidak ada | `FileNotFoundError` | `NoSuchFileException` |
| Error I/O umum | `OSError` (tidak wajib ditangkap) | `IOException` (*checked*, wajib ditangkap atau `throws`) |
| Teks bukan angka | `ValueError` dari `int("dua")` | `NumberFormatException` dari `Integer.parseInt("dua")` |
| Input habis | `EOFError` dari `input()` | `NoSuchElementException` dari `Scanner.nextLine()` |
| Pustaka *unit test* | `unittest` (bawaan) | JUnit (unduh terpisah); di materi ini: runner mini |
| Persiapan tiap test | `setUp()` | JUnit `@BeforeEach`; runner mini: `siapkanPesanan()` |
| Memeriksa nilai | `assertEqual(hasil, harapan)` | JUnit `assertEquals(harapan, hasil)` |
| Memeriksa *exception* | `with self.assertRaises(X):` | JUnit `assertThrows(X.class, () -> ...)` |
| Folder sementara | `tempfile.TemporaryDirectory()` | `Files.createTempDirectory("awalan")` + hapus sendiri |

## 1. Package: Folder atau Pernyataan

**Python:**

```python
# kedaikita/__init__.py ada, maka folder kedaikita adalah package
from kedaikita.menu import Menu
from kedaikita.pengecualian import KedaiError
```

**Java:**

```java
package kedaikita;          // baris pertama setiap file di src/kedaikita/

import java.nio.file.Path;  // kelas dari package lain tetap di-import
// Menu, KedaiException, dll. sesama package: langsung dipakai tanpa import
```

**Mengapa berbeda?** Di Python, *package* ditentukan oleh **folder**: modul ikut *package* karena letak filenya. Di Java, *package* ditentukan oleh **pernyataan** `package` di dalam file, dan folder harus menyesuaikan. Java juga memisahkan kompilasi dan eksekusi, sehingga perlu `-d out` (ke mana `.class` disimpan) dan `-cp out` (di mana mencarinya). Python cukup dijalankan dari folder yang tepat.

## 2. Di Mana Folder `data/`?

Python menyusun path dari lokasi file `main.py` sendiri (`__file__`), sehingga `python studi-kasus/main.py --demo` dari folder lain pun tetap berhasil. Java memakai `Path.of("data")` yang relatif terhadap **folder kerja**, sehingga perintah `java` harus dijalankan dari folder `studi-kasus`. Skrip `jalankan.sh`/`jalankan.bat` mengurusnya dengan berpindah ke foldernya sendiri dulu.

Java sebenarnya bisa mencari lokasi file `.class`-nya, tetapi caranya jauh lebih rumit daripada `__file__`. Untuk proyek kecil, skrip pembantu adalah solusi yang paling sederhana.

## 3. CSV: Modul `csv` atau `split`

| | Python `csv` | Java `split(";", -1)` |
|---|---|---|
| Isi kolom mengandung pemisah | dibungkus tanda kutip otomatis, dibaca kembali dengan benar | baris terpecah salah; harus dihindari |
| Kolom kosong di akhir baris | tetap terbaca sebagai `""` | tetap ada **hanya** jika memakai `-1` |
| Ganti baris | atur `newline=""` dan `lineterminator="\n"` | gabungkan baris dengan `"\n"` sendiri |

Jebakan terbesar di Java: `"a;b;".split(";")` menghasilkan **2** elemen, karena string kosong di akhir dibuang. Dengan `split(";", -1)`, hasilnya 3 elemen, sama seperti `"a;b;".split(";")` di Python.

## 4. `with` atau Try-with-resources

**Python:**

```python
with SambunganPrinter("Printer Lab") as printer:
    printer.cetak("Halaman 1")
# __exit__() sudah dipanggil di sini
```

**Java:**

```java
try (SambunganPrinter printer = new SambunganPrinter("Printer Lab")) {
    printer.cetak("Halaman 1");
} // close() sudah dipanggil di sini
```

Keduanya menjamin penutupan, termasuk saat terjadi *exception*, dan menutup beberapa sumber daya dengan urutan terbalik. Perbedaan kecilnya: di Python, objek "dibuka" di `__enter__()`; di Java, objek dianggap terbuka begitu dibuat di dalam kurung `try`. Di Java, method sekali jalan seperti `Files.readAllLines()` sudah menutup file sendiri, jadi try-with-resources hanya perlu untuk objek yang kamu pegang, seperti `BufferedReader`.

## 5. *Checked Exception* di Dalam Observer (Khusus Java)

`PencatatTransaksiCSV.perbarui()` menulis file, dan menulis file bisa gagal. Di Python, `OSError` cukup dibiarkan merambat ke `main.py`. Di Java, `IOException` adalah *checked exception*, sedangkan method `perbarui()` di *interface* `PengamatPesanan` tidak mendeklarasikan `throws IOException`. Method yang meng-*override* tidak boleh menambah *checked exception* baru, sehingga Java membungkusnya:

```java
} catch (IOException e) {
    throw new UncheckedIOException(e.getMessage(), e);
}
```

Inilah harga keamanan *checked exception*: lebih banyak kode, tetapi compiler memaksa kita memikirkan setiap kemungkinan gagal.

## 6. Akhir Input

| | Python | Java |
|---|---|---|
| Membaca satu baris | `input("Pilihan: ")` (pertanyaan dicetak oleh `input`) | `System.out.print("Pilihan: ");` lalu `masukan.nextLine()` |
| Input habis | `EOFError` | `NoSuchElementException` (*unchecked*) |
| Teks bukan angka | `ValueError` dari `int()` | `NumberFormatException` dari `Integer.parseInt()` |
| Spasi di sekitar angka | `int(" 2 ")` berhasil | `Integer.parseInt(" 2 ")` gagal; `trim()` dulu |

Di Java, cukup buat **satu** `Scanner(System.in)` untuk seluruh program, seperti di `AplikasiKasir`. Jangan menutupnya, karena `System.in` ikut tertutup dan tidak bisa dibuka lagi.

## 7. Unit Test: `unittest` atau JUnit

| | Python `unittest` | Java JUnit 5 |
|---|---|---|
| Tersedia | bawaan Python | pustaka terpisah (biasanya lewat Maven/Gradle) |
| Menandai test | nama method diawali `test_` | anotasi `@Test` |
| Persiapan | `setUp()` | `@BeforeEach` |
| Urutan argumen *assert* | bebas; di materi ini `(hasil, harapan)` | `assertEquals(harapan, hasil)` |
| Menjalankan | `python -m unittest discover -s tests -v` | tombol *Run Test* di editor, atau `mvn test`/`gradle test` |

Karena JUnit tidak ikut di JDK, studi kasus Java memakai runner mini `UjiKedaiKita` dengan 16 pemeriksaan yang sama dengan 16 test Python. Prinsipnya sama persis: siapkan, jalankan, periksa.

## Yang Sama di Kedua Bahasa

- Arsitektur berlapis yang sama: `AplikasiKasir` → `LayananKasir` → model → `RepositoriMenuCSV`/`PencatatTransaksiCSV`.
- Format file yang sama: CSV bertitik koma, UTF-8, baris judul kolom, ganti baris `"\n"`. File data hasil versi Python bisa dibaca versi Java, dan sebaliknya.
- Pesan `FormatDataError`/`FormatDataException` yang sama, lengkap dengan nomor baris.
- Pola Observer yang sama untuk mencatat transaksi, tanpa mengubah `Pesanan`.
- Validasi input yang sama: periksa, tanya ulang, tangani akhir input.
- Output mode demo dan mode interaktif **identik**.

## Jebakan Saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Memakai `split(";")` tanpa `-1`, sehingga kolom kosong di akhir hilang |
| Python | Java | Menjalankan `java -cp out Main`, padahal nama lengkapnya `kedaikita.Main` |
| Python | Java | Mengompilasi hanya `Main.java`, bukan seluruh `src/kedaikita/*.java` |
| Python | Java | Menjalankan dari folder lain, padahal `Path.of("data")` bergantung pada folder kerja |
| Python | Java | Mengandalkan kata kunci `assert`, padahal nonaktif tanpa opsi `-ea` |
| Java | Python | Menjalankan `python kedaikita/aplikasi.py` langsung, sehingga muncul `ModuleNotFoundError` |
| Java | Python | Lupa `encoding="utf-8"`, padahal `Files` di Java memakai UTF-8 secara bawaan |
| Java | Python | Lupa bahwa baris dari `for baris in berkas` masih berisi `"\n"` (pakai `strip()`) |
| Keduanya | Keduanya | Menulis file data ke folder repositori saat pengujian; pakai folder sementara |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
