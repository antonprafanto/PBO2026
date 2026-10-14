# 🌉 Jembatan Python ↔ Java Pertemuan 01: Pengenalan PBO dan Persiapan Alat

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Di pertemuan ini kamu memanaskan kembali dasar-dasar pemrograman dan melihat sendiri kelemahan data paralel pada KedaiKita. Konsepnya **sama** di kedua bahasa: variabel, percabangan, perulangan, *list* atau *array*, serta fungsi atau *method*. Yang berbeda hanyalah **cara menuliskannya**. Halaman ini membantumu membaca kode di kedua bahasa, sekaligus menjelaskan *mengapa* perbedaan itu ada.

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| Kerangka program | fungsi `main()` + `if __name__ == "__main__":` | `public class Nama { public static void main(String[] args) { ... } }` |
| Kode wajib di dalam kelas? | tidak | ya |
| Menampilkan teks | `print("Halo")` | `System.out.println("Halo");` |
| Akhir sebuah perintah | akhir baris | titik koma `;` |
| Penanda blok | titik dua `:` + indentasi | kurung kurawal `{ }` |
| Komentar | `# ...` dan *docstring* `""" ... """` | `// ...`, `/* ... */`, dan `/** ... */` |
| Membuat variabel | `harga = 18000` | `int harga = 18000;` |
| Bilangan bulat dan pecahan | `int` dan `float` | `int` (juga `long`) dan `double` |
| Teks dan satu karakter | `str` untuk keduanya: `"Ayu"`, `"A"` | `String` untuk teks (`"Ayu"`), `char` untuk satu karakter (`'A'`) |
| Nilai benar/salah | `True`, `False` | `true`, `false` |
| Operator logika | `and`, `or`, `not` | `&&`, `\|\|`, `!` |
| Hasil `7 / 2` | `3.5` | `3` (karena kedua angkanya `int`) |
| Pembagian bulat | `7 // 2` → `3` | `7 / 2` → `3` |
| Menyisipkan nilai ke teks | *f-string*: `f"Rp{harga}"` | penggabungan: `"Rp" + harga` |
| Membandingkan isi teks | `hari == "Sabtu"` | `hari.equals("Sabtu")` |
| Wadah banyak data | *list*: `[78, 92, 65]`, ukurannya bisa bertambah | *array*: `int[] nilai = {78, 92, 65};`, ukurannya tetap |
| Banyak elemen | `len(nilai)` | `nilai.length` |
| Perulangan dengan penghitung | `for i in range(1, 6):` | `for (int i = 1; i <= 5; i++) { ... }` |
| Perulangan tiap elemen | `for n in nilai:` | `for (int n : nilai) { ... }` |
| Mengurutkan | `nilai.sort()` | `Arrays.sort(nilai);` |
| Mencetak seluruh isi | `print(nilai)` | `System.out.println(Arrays.toString(nilai));` |
| Mengulang teks | `"-" * 32` | `"-".repeat(32)` |
| Fungsi | `def hitung_ongkos(jarak_km):` | `static int hitungOngkos(int jarakKm) { ... }` |
| Konstanta | `TARIF_DASAR = 10000` (hanya kesepakatan) | `static final int TARIF_DASAR = 10000;` (dijaga *compiler*) |
| Menukar dua nilai | `a, b = b, a` | butuh variabel sementara |
| Menjalankan program | `python nama_file.py` | `java NamaFile.java`, atau `javac` lalu `java` |
| Gaya nama variabel dan fungsi | `snake_case` | `camelCase` |

## 1. Kerangka Program: Bebas atau Wajib di dalam Kelas?

Kedua program di bawah adalah versi ringkas contoh 01 dari halaman praktik. Versi lengkapnya ada di [`python/contoh/contoh01_halo.py`](python/contoh/contoh01_halo.py) dan [`java/contoh/Contoh01Halo.java`](java/contoh/Contoh01Halo.java).

**Python:**

```python
def main():
    print("Halo, Samarinda!")


if __name__ == "__main__":
    main()
```

**Java:**

```java
public class Halo {
    public static void main(String[] args) {
        System.out.println("Halo, Samarinda!");
    }
}
```

**Mengapa berbeda?** Python adalah bahasa **multiparadigma**. Sebuah *file* Python boleh berisi perintah biasa tanpa fungsi maupun kelas sehingga `main()` hanyalah **kebiasaan baik** agar titik awal program jelas. Java dirancang **berorientasi objek** sejak awal sehingga setiap kode **wajib** berada di dalam kelas, dan `main` adalah titik awal yang **diwajibkan** bahasanya. Itulah sebabnya program Java pertamamu sudah memakai `class` meskipun isinya masih prosedural.

## 2. Tipe Data: Dinamis atau Statis?

Potongan kode di bagian 2 sampai 6 hanya untuk dibaca dan dibandingkan, bukan untuk dijalankan sendiri. Program lengkap yang memakai konsep yang sama ada di folder `contoh/` masing-masing bahasa.

**Python:**

```python
semester = 3
semester = "empat"   # diterima: tipe variabel ikut berubah
print(semester + 1)  # baru gagal di sini, saat program berjalan (TypeError)
```

**Java:**

```java
int semester = 3;
semester = "empat"; // ditolak saat kompilasi:
                    // incompatible types: String cannot be converted to int
```

| | Python | Java |
|---|---|---|
| Tipe variabel | ditentukan oleh nilai yang sedang disimpan, bisa berubah | ditentukan saat deklarasi, tidak bisa berubah |
| Kesalahan tipe ketahuan | saat baris itu **dijalankan** | saat **kompilasi**, sebelum program berjalan |

**Mengapa berbeda?** Python memakai **tipe dinamis**: kode lebih ringkas dan cepat ditulis, tetapi kesalahan tipe baru muncul saat program berjalan. Java memakai **tipe statis**: lebih banyak yang harus diketik, tetapi *compiler* menangkap banyak kesalahan lebih awal, dan editor bisa membantu lebih banyak. Keduanya punya kelebihan masing-masing.

## 3. Pembagian: Jebakan yang Paling Sering Terjadi

**Python:**

```python
print(7 / 2)   # 3.5 -> / selalu menghasilkan pecahan
print(7 // 2)  # 3   -> // adalah pembagian bulat
```

**Java:**

```java
System.out.println(7 / 2);   // 3   -> int dibagi int menghasilkan int
System.out.println(7.0 / 2); // 3.5 -> jika ada double, hasilnya double
```

Di Python 3, operator `/` **selalu** menghasilkan pecahan. Di Java, jenis hasilnya mengikuti jenis angkanya. Untuk bilangan bulat yang tidak negatif (nol atau positif), `//` di Python sama dengan `/` di Java pada dua `int`. Itulah sebabnya rumus persen di materi ini ditulis `nilai * persen // 100` di Python dan `nilai * persen / 100` di Java.

> [!NOTE]
> Untuk bilangan **negatif**, keduanya berbeda: `-7 // 2` di Python menghasilkan `-4` (dibulatkan ke bawah), sedangkan `-7 / 2` di Java menghasilkan `-3` (dipotong ke arah nol). Di materi ini kita hanya membagi bilangan yang tidak negatif, jadi hasilnya selalu sama.

## 4. Menggabungkan Teks dengan Angka

**Python:**

```python
semester = 3
print(f"Semester: {semester}")  # cara yang disarankan
print("Semester: " + semester)  # TypeError: teks tidak bisa ditambah angka
```

**Java:**

```java
int semester = 3;
System.out.println("Semester: " + semester); // angka otomatis diubah menjadi teks
```

Python **menolak** `"teks" + angka` karena tidak mau menebak maksudmu. Java **otomatis** mengubah angka menjadi teks begitu `+` bertemu `String`. Kemudahan Java ini punya jebakan: `"Total: Rp" + 36000 + 8000` menghasilkan `Total: Rp360008000`, bukan `Total: Rp44000`. Di Java, bungkus penjumlahan dengan kurung.

## 5. *List* Python dan *Array* Java

| | *List* Python | *Array* Java |
|---|---|---|
| Ukuran | bisa bertambah dengan `append` | tetap sejak dibuat (yang bisa bertambah: `ArrayList`, Pertemuan 05) |
| Tipe elemen | boleh campur, tetapi sebaiknya seragam | wajib seragam, sesuai deklarasi (`int[]`, `String[]`) |
| Banyak elemen | `len(nilai)` | `nilai.length` (tanpa kurung); untuk teks `nama.length()` (dengan kurung) |
| Dicetak langsung | menampilkan isinya: `[78, 92, 65]` | menampilkan tanda pengenal seperti `[I@1ee807c6`; pakai `Arrays.toString()` |
| Mengurutkan | *method* milik *list*: `nilai.sort()` | *method* milik kelas `Arrays`: `Arrays.sort(nilai)` |

Persamaannya justru yang paling penting untuk pertemuan ini: indeks dimulai dari 0, pengurutan mengubah isi wadah itu sendiri, dan **masalah data paralel terjadi persis sama** di kedua bahasa. Mengurutkan satu *list* atau *array* tidak pernah ikut memindahkan *list* atau *array* lain.

## 6. Fungsi Python dan *Method* `static` Java

**Python:**

```python
def hitung_ongkos(jarak_km):
    if jarak_km <= 4:
        return TARIF_DASAR
    return TARIF_DASAR + (jarak_km - 4) * TARIF_PER_KM
```

**Java:**

```java
static int hitungOngkos(int jarakKm) {
    if (jarakKm <= 4) {
        return TARIF_DASAR;
    }
    return TARIF_DASAR + (jarakKm - 4) * TARIF_PER_KM;
}
```

| | Python | Java |
|---|---|---|
| Letak | boleh di mana saja dalam *file* | wajib di dalam kelas |
| Tipe parameter dan nilai kembalian | tidak ditulis | wajib ditulis (`int jarakKm`, `int` di depan nama) |
| Tidak mengembalikan apa pun | tanpa `return`, hasilnya otomatis `None` | ditandai `void` |
| Lupa `return` di salah satu cabang | diam-diam mengembalikan `None` | ditolak *compiler*: `missing return statement` |

Kata `static` di Java membuat *method* bisa dipanggil langsung dari `main` tanpa membuat objek. Untuk program bergaya prosedural, itulah padanan paling dekat dari fungsi biasa di Python. Arti lengkap `static` dibahas di Pertemuan 03.

## 7. Menjalankan Program: *Interpreter* dan *Compiler*

| | Python | Java |
|---|---|---|
| Perintah | `python contoh01_halo.py` | `java Contoh01Halo.java`, atau `javac Contoh01Halo.java` lalu `java Contoh01Halo` |
| Proses (secara sederhana) | *interpreter* Python membaca *file* lalu langsung menjalankannya | `javac` mengompilasi kode menjadi *bytecode* (`.class`), lalu JVM menjalankannya |
| Kapan kesalahan ketahuan | kesalahan sintaks (misalnya `IndentationError`) ketahuan sebelum program berjalan; kesalahan lain (`NameError`, `TypeError`) baru muncul saat barisnya dijalankan | kesalahan sintaks **dan** kesalahan tipe ketahuan saat kompilasi; sisanya (misalnya indeks di luar batas) saat berjalan |

## Yang Sama di Kedua Bahasa

- Perintah dijalankan berurutan dari atas ke bawah, dimulai dari `main`.
- Konsep percabangan (`if`) dan perulangan (`for`, `while`) sama persis. Hanya cara menulisnya yang berbeda.
- Indeks *list* dan *array* dimulai dari 0. Operator `%` menghasilkan sisa bagi, dan `==` membandingkan angka.
- Fungsi dan *method* sama-sama menerima parameter dan mengembalikan nilai dengan `return`.
- Masalah data paralel di KedaiKita terjadi dengan cara yang sama, dan versi objeknya menyelesaikan masalah itu dengan cara yang sama pula.
- *Output* setiap contoh, solusi latihan, dan studi kasus versi Python dan Java **identik**.
- Keduanya mendukung PBO sepenuhnya. Bedanya, Java **mewajibkan** kelas, sedangkan Python **mempersilakan**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Lupa titik koma `;`, lupa menulis tipe variabel, atau lupa kurung kurawal |
| Python | Java | Menulis `True`/`False`, `and`/`or`; di Java seharusnya `true`/`false` dan `&&`/`\|\|` |
| Python | Java | Mengira `7 / 2` menghasilkan `3.5`, padahal di Java hasilnya `3` |
| Python | Java | Membandingkan teks dengan `==`; di Java gunakan `.equals()` |
| Python | Java | Memakai kutip tunggal untuk teks, misalnya `'Halo'`; di Java kutip tunggal hanya untuk satu karakter |
| Python | Java | Mencetak *array* secara langsung dan mendapat tulisan aneh seperti `[I@1ee807c6` |
| Java | Python | Menulis komentar dengan `//`; di Python `//` adalah pembagian bulat, dan komentar memakai `#` |
| Java | Python | Lupa titik dua di akhir baris `if`, `for`, `while`, atau `def`, atau indentasinya tidak rapi |
| Java | Python | Menulis `i++`, yang menghasilkan `SyntaxError`. Lebih licin lagi, `++i` tidak *error*, tetapi juga tidak menambah apa pun. Gunakan `i = i + 1` atau `i += 1` |
| Java | Python | Menggabungkan teks dan angka dengan `+`, lalu mendapat `TypeError` |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
