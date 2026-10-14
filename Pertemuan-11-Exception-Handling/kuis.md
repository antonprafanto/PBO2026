# Kuis Pertemuan 11: *Exception Handling*

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 12 ➡️](../Pertemuan-12-Koleksi-dan-Generics/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Program kasir berjalan lancar sampai selesai tanpa pesan *error* apa pun, tetapi potongan diskon yang dihitungnya selalu salah. Kesalahan ini termasuk jenis ...

- A. kesalahan sintaks
- B. kesalahan saat berjalan (*runtime error*)
- C. kesalahan logika
- D. *checked exception*

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: program tidak berhenti dan tidak ada *exception*, tetapi hasilnya salah. Itulah ciri kesalahan logika, yang hanya bisa ditemukan lewat pengujian. Kesalahan sintaks (A) membuat program tidak bisa dijalankan sama sekali. *Runtime error* (B) membuat program berhenti atau melempar *exception*. *Checked exception* (D) adalah jenis *exception* di Java, bukan jenis kesalahan logika.

</details>

### Soal 2

Sebuah *exception* tidak tertangkap sehingga muncul *traceback* (Python) atau *stack trace* (Java). Di mana kamu mencari **tempat *exception* itu lahir**?

- A. Python: blok `File ...` paling atas; Java: baris `at ...` paling bawah
- B. Python: blok `File ...` paling bawah (tepat di atas baris jenis *exception*); Java: baris `at ...` paling atas
- C. Di kedua bahasa, selalu di baris pertama laporan
- D. Di kedua bahasa, selalu di baris terakhir laporan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: Python menulis *most recent call last*, jadi panggilan terbaru (tempat *exception* lahir) ada di bawah, tepat di atas baris `JenisError: pesan`. Java kebalikannya: baris `at` paling atas adalah tempat *exception* lahir, dan baris paling bawah adalah titik awal (`main`). Pilihan A tertukar. C dan D salah karena arah baca kedua bahasa berlawanan.

</details>

### Soal 3

Perhatikan potongan kode berikut (versi Java ditulis di dalam `main`).

**Python:**

```python
nol = 0
try:
    print("1")
    hasil = 10 // nol
    print("2")
except ZeroDivisionError:
    print("3")
finally:
    print("4")
print("5")
```

**Java:**

```java
int nol = 0;
try {
    System.out.println("1");
    int hasil = 10 / nol;
    System.out.println("2");
} catch (ArithmeticException e) {
    System.out.println("3");
} finally {
    System.out.println("4");
}
System.out.println("5");
```

Angka apa saja yang tercetak, berurutan?

- A. 1 2 3 4 5
- B. 1 3 5
- C. 1 4 5
- D. 1 3 4 5

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: "1" tercetak, lalu pembagian dengan nol melempar *exception*. Sisa blok `try` ("2") dilewati. Penangkap yang cocok mencetak "3", `finally` selalu mencetak "4", lalu program lanjut ke baris setelah `try` dan mencetak "5". Pilihan A keliru karena "2" dilewati. Pilihan B melupakan `finally`. Pilihan C melupakan penangkapnya.

</details>

### Soal 4

Seorang pemrogram menulis penangkap `Exception` **di atas** penangkap pembagian dengan nol (`ZeroDivisionError` / `ArithmeticException`) dalam satu `try`. Apa akibatnya?

- A. Python menerimanya, tetapi penangkap pembagian dengan nol tidak pernah dijalankan; Java menolak mengompilasinya
- B. Kedua bahasa menolak menjalankan program
- C. Kedua bahasa otomatis memilih penangkap yang paling spesifik
- D. Python menolak menjalankan program; Java menerimanya tanpa masalah

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: penangkap diperiksa dari atas ke bawah, dan yang pertama cocok yang dijalankan. Karena `ZeroDivisionError`/`ArithmeticException` **adalah** turunan `Exception`, penangkap umum di atas selalu menang. Python tidak memperingatkan apa pun sehingga terjadi *bug* diam-diam. Java menolak dengan pesan `exception ArithmeticException has already been caught`. Tidak ada bahasa yang otomatis memilih yang paling spesifik (C).

</details>

### Soal 5

Perhatikan potongan kode berikut.

**Python:**

```python
def ambil(daftar: list[str], i: int) -> str:
    print("ambil")
    return daftar[i]


def umumkan(daftar: list[str], i: int):
    nama = ambil(daftar, i)
    print("umumkan " + nama)


try:
    umumkan(["Ayu", "Bima"], 5)
except IndexError:
    print("tidak ada")
```

**Java:**

```java
static String ambil(String[] daftar, int i) {
    System.out.println("ambil");
    return daftar[i];
}

static void umumkan(String[] daftar, int i) {
    String nama = ambil(daftar, i);
    System.out.println("umumkan " + nama);
}

// di dalam main:
try {
    umumkan(new String[] {"Ayu", "Bima"}, 5);
} catch (ArrayIndexOutOfBoundsException e) {
    System.out.println("tidak ada");
}
```

Apa *output*-nya?

- A. `ambil`, lalu `umumkan Bima`, lalu `tidak ada`
- B. `tidak ada` saja
- C. `ambil`, lalu `tidak ada`
- D. Program berhenti dengan *traceback*/*stack trace* karena `umumkan` tidak punya `try`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `ambil` sempat mencetak "ambil", lalu `daftar[5]` melempar *exception*. Karena `ambil` dan `umumkan` tidak menangkapnya, *exception* **merambat** ke pemanggil, dan baris `umumkan ...` ikut dilewati. Penangkap di tingkat paling atas mencetak "tidak ada". Pilihan D keliru: *method* tidak harus punya `try` sendiri, cukup ada yang menangkap di salah satu pemanggilnya.

</details>

### Soal 6

Di KedaiKita Pertemuan 11, pembayaran QRIS Siti gagal karena saldo kurang. Mengapa status pesanannya tetap `BARU` sampai kartu kredit berhasil?

- A. Karena `bayar()` menangkap kegagalan itu lalu mengembalikan nilai salah
- B. Karena *exception* dari `proses()` merambat keluar dari `bayar()` sehingga baris yang mengubah status menjadi `LUNAS` tidak pernah dijalankan
- C. Karena blok `finally` di program utama mengembalikan status menjadi `BARU`
- D. Karena status hanya bisa diubah oleh penangkap `KedaiError` / `KedaiException`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: `bayar()` memanggil `proses()` tanpa `try`. Saat `proses()` melempar `PembayaranGagalError` / `PembayaranGagalException`, sisa `bayar()` dilewati, termasuk baris pengubah status. Pilihan A adalah cara lama di Pertemuan 10 (nilai benar/salah). `finally` di program utama hanya mencatat log (C), dan penangkap tidak mengubah status (D).

</details>

### Soal 7

Pernyataan manakah yang **benar** tentang *checked exception*?

- A. Python mewajibkan setiap *exception* ditangkap atau diumumkan
- B. Di Java, turunan `RuntimeException` wajib diumumkan dengan `throws`
- C. *Checked exception* hanya bisa berasal dari kelas bawaan Java, tidak bisa dibuat sendiri
- D. Di Java, turunan `Exception` yang bukan turunan `RuntimeException` wajib ditangkap atau diumumkan dengan `throws`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: itulah definisi *checked exception*, dan `KedaiException extends Exception` di KedaiKita adalah contohnya. Python tidak punya konsep ini (A salah). Turunan `RuntimeException` justru *unchecked*, tidak wajib diumumkan (B salah). Kita bisa membuat *checked exception* sendiri, cukup dengan `extends Exception` (C salah).

</details>

### Soal 8

Mengapa *method* `transfer()` di contoh 07 menulis `raise TransferGagalError(pesan) from e` (Python) atau `throw new TransferGagalException(pesan, e);` (Java)?

- A. Untuk melempar *exception* baru yang lebih bermakna, sambil menyimpan *exception* lama sebagai penyebabnya
- B. Untuk menghapus *exception* lama agar tidak terlihat di laporan
- C. Untuk mengulang penarikan uang secara otomatis
- D. Supaya *exception* baru tidak perlu ditangkap lagi oleh siapa pun

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: ini disebut *exception chaining*. Pemanggil menerima "transfer gagal" yang mudah dipahami, tetapi penyebab aslinya (saldo kurang) tetap bisa dibaca lewat `e.__cause__` / `e.getCause()`, dan ikut tercetak di laporan (*The above exception was the direct cause...* / `Caused by:`). *Exception* lama justru disimpan, bukan dihapus (B). Tidak ada pengulangan otomatis (C), dan *exception* baru tetap harus ditangkap (D).

</details>

### Soal 9

Konstruktor `StokTidakCukupError` (Python) / `StokTidakCukupException` (Java) meneruskan pesan `"Stok Mie Goreng Jawa tinggal 10"` ke konstruktor induknya, lalu menyimpan `tersedia = 10` sebagai data tambahan. *Exception* ini dilempar, lalu ditangkap sebagai `e`. Apa hasil `print(e)` (Python) atau `e.getMessage()` (Java)?

- A. `('Mie Goreng Jawa', 10)`
- B. `StokTidakCukupError` atau `StokTidakCukupException`
- C. `Stok Mie Goreng Jawa tinggal 10`
- D. `10`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: pesan yang diteruskan ke konstruktor induk (`super().__init__(pesan)` / `super(pesan)`) itulah yang dikembalikan oleh `str(e)` / `e.getMessage()`. Data tambahan dibaca terpisah, lewat `e.tersedia` / `e.getTersedia()`, jadi D salah. Pilihan A adalah hasil di Python jika `super().__init__(pesan)` **lupa** dipanggil: Python menampilkan argumen mentahnya. Nama kelas (B) tidak tercetak oleh `print(e)` maupun `getMessage()`.

</details>

### Soal 10

Manakah kebiasaan yang **paling buruk** saat menangani *exception*?

- A. Menangkap *exception* di *method* yang tahu harus berbuat apa
- B. Menulis penangkap kosong (`except Exception: pass` / `catch (Exception e) { }`) supaya program tidak pernah terlihat *error*
- C. Memeriksa data sebelum mengubah atribut, lalu melempar *exception* jika datanya salah
- D. Mematikan atau menutup sumber daya di blok `finally`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: penangkap kosong "menelan" *exception*. Program terlihat lancar, tetapi hasilnya bisa salah tanpa jejak, seperti remote AC yang mencetak "Suhu diatur ke 10 derajat" padahal ditolak. Pilihan A, C, dan D justru praktik baik: menangkap di tempat yang tepat, validasi lebih awal, dan bersih-bersih di `finally`.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Kamu siap menangani kesalahan dengan rapi | Lanjut ke [Pertemuan 12](../Pertemuan-12-Koleksi-dan-Generics/README.md) |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep untuk soal yang salah, lalu jalankan lagi contoh 04, 05, dan 07 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, lalu kerjakan "Coba sendiri" di halaman praktik satu per satu |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 12 ➡️](../Pertemuan-12-Koleksi-dan-Generics/README.md)
