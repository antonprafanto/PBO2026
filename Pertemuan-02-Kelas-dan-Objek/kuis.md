# Kuis — Pertemuan 02: Kelas dan Objek

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 03 ➡️](../Pertemuan-03-Atribut-dan-Method/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Manakah analogi yang paling tepat untuk menggambarkan hubungan **kelas** dan **objek**?

- A. Kelas adalah rumah, objek adalah denahnya
- B. Kelas adalah denah rumah, objek adalah rumah yang dibangun dari denah itu
- C. Kelas adalah tukang bangunan, objek adalah semennya
- D. Kelas dan objek sama-sama denah, hanya namanya yang berbeda

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: kelas adalah cetak biru (denah), sedangkan objek adalah wujud nyata yang dibuat berdasarkan cetak biru itu (rumah). Pilihan A terbalik. Pilihan C tidak menggambarkan hubungan "cetak biru dan hasilnya". Pilihan D salah karena kelas dan objek adalah dua hal yang berbeda.

</details>

### Soal 2

Perhatikan deskripsi berikut: *"Setiap motor punya plat nomor dan warna. Motor bisa dinyalakan dan diisi bensin."* Manakah yang paling tepat dijadikan **method**?

- A. plat nomor
- B. warna
- C. motor
- D. diisi bensin

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: method adalah perilaku atau aksi, biasanya berupa kata kerja: "dinyalakan" dan "diisi bensin". "Plat nomor" dan "warna" adalah atribut (ciri), sedangkan "motor" adalah calon nama kelas.

</details>

### Soal 3

Kapan konstruktor dijalankan?

- A. Tepat saat sebuah objek dibuat, secara otomatis
- B. Saat method pertama milik objek dipanggil
- C. Hanya jika programmer memanggilnya secara manual setelah objek dibuat
- D. Saat program selesai berjalan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: konstruktor (`__init__` di Python, method bernama sama dengan kelas di Java) berjalan otomatis ketika objek dibuat, misalnya `Menu("Kopi", 18000)` atau `new Menu("Kopi", 18000)`. Kita tidak perlu memanggilnya secara manual, sehingga pilihan C salah.

</details>

### Soal 4

Di dalam sebuah method, `self` (Python) atau `this` (Java) merujuk pada ...

- A. kelas tempat method itu ditulis
- B. objek pertama yang pernah dibuat dari kelas itu
- C. objek yang sedang menjalankan method tersebut
- D. semua objek yang dibuat dari kelas itu

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: saat menjalankan `kopi.tampilkan_info()`, `self`/`this` adalah objek `kopi`. Saat menjalankan `es_teh.tampilkan_info()`, `self`/`this` adalah objek `es_teh`. Kata ganti ini menunjuk objek yang **sedang** bekerja, bukan kelasnya (A), bukan objek pertama (B), dan bukan semua objek (D).

</details>

### Soal 5

Perhatikan kode berikut.

**Python:**

```python
class Lampu:
    def __init__(self):
        self.menyala = False

    def nyalakan(self):
        self.menyala = True


a = Lampu()
b = Lampu()
a.nyalakan()
```

**Java:**

```java
class Lampu {
    boolean menyala = false;

    void nyalakan() {
        menyala = true;
    }
}

// di dalam main:
Lampu a = new Lampu();
Lampu b = new Lampu();
a.nyalakan();
```

Setelah kode dijalankan, nilai atribut `menyala` milik `a` dan milik `b` berturut-turut adalah ...

- A. benar (`True`/`true`) dan salah (`False`/`false`)
- B. benar dan benar
- C. salah dan salah
- D. salah dan benar

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `a` dan `b` adalah dua objek berbeda yang masing-masing menyimpan atribut `menyala` sendiri. Hanya `a` yang menjalankan `nyalakan()`, sehingga hanya milik `a` yang berubah. Pilihan B adalah miskonsepsi "semua objek ikut berubah".

</details>

### Soal 6

Kedua kode berikut punya masalah yang sama.

**Python:**

```python
class Menu:
    def __init__(self, nama, harga):
        nama = nama
        harga = harga
```

**Java:**

```java
class Menu {
    String nama;
    int harga;

    Menu(String nama, int harga) {
        nama = nama;
        harga = harga;
    }
}
```

Apa penyebab masalahnya?

- A. Konstruktor tidak pernah dipanggil
- B. Tipe data parameter dan atribut tertukar
- C. Kelas tidak memiliki method apa pun
- D. Nilai parameter tidak disimpan ke atribut objek karena tidak memakai `self.`/`this.`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `nama = nama` hanya mengisi variabel parameter dengan dirinya sendiri. Atribut objek tidak tersentuh. Akibatnya, di Python membaca `kopi.nama` menghasilkan `AttributeError`, sedangkan di Java tercetak `null`. Perbaikannya: `self.nama = nama` atau `this.nama = nama`. Konstruktor tetap dipanggil (A salah), dan kelas tanpa method tetap sah (C bukan penyebabnya).

</details>

### Soal 7

Pernyataan yang **benar** tentang beberapa objek yang dibuat dari kelas yang sama adalah ...

- A. Nilai atributnya pasti selalu sama
- B. Mengubah atribut satu objek otomatis mengubah objek lainnya
- C. Masing-masing objek menyimpan nilai atributnya sendiri
- D. Dari satu kelas hanya boleh dibuat satu objek

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: objek-objek dari kelas yang sama punya **jenis** atribut yang sama (misalnya semua menu punya `nama` dan `harga`), tetapi **nilainya** milik masing-masing. Satu kelas bisa menghasilkan objek sebanyak apa pun, sehingga D salah.

</details>

### Soal 8

Perhatikan kode berikut.

**Python:**

```python
m1 = Menu("Kopi", 18000)
m2 = Menu("Teh", 8000)
m3 = m1
```

**Java:**

```java
Menu m1 = new Menu("Kopi", 18000);
Menu m2 = new Menu("Teh", 8000);
Menu m3 = m1;
```

Berapa banyak **objek** `Menu` yang tercipta?

- A. 1
- B. 2
- C. 3
- D. 0

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: objek baru hanya tercipta saat `Menu(...)` atau `new Menu(...)` dijalankan, dan itu terjadi dua kali. Baris `m3 = m1` tidak membuat objek baru. Variabel `m3` hanya ikut menunjuk ke objek yang sama dengan `m1`. Hal ini kita bahas lebih dalam di Pertemuan 03.

</details>

### Soal 9

Method `hitung_total(jumlah)` mengembalikan hasilnya dengan `return`, bukan langsung mencetaknya. Apa keuntungan utamanya?

- A. Program pasti berjalan lebih cepat
- B. Method tidak lagi membutuhkan parameter
- C. Method tidak perlu dipanggil
- D. Hasilnya bisa disimpan, dihitung lagi, atau dicetak sesuai kebutuhan pemanggil

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: nilai kembalian bisa dipakai ulang, misalnya dijumlahkan dengan total menu lain seperti di studi kasus KedaiKita. Method yang hanya mencetak, hasilnya tidak bisa diolah lebih lanjut. Pilihan A, B, dan C tidak berhubungan dengan `return`.

</details>

### Soal 10

Pada diagram kelas sederhana berbentuk kotak tiga bagian, bagian **tengah** berisi ...

- A. daftar atribut
- B. nama kelas
- C. daftar method
- D. nama-nama objek

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: bagian atas berisi nama kelas, bagian tengah berisi atribut, dan bagian bawah berisi method. Nama objek tidak dicantumkan di diagram kelas, karena diagram kelas menggambarkan cetak birunya.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Konsep kelas dan objek sudah kuat | Lanjut ke [Pertemuan 03](../Pertemuan-03-Atribut-dan-Method/README.md) |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 4 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan dan jalankan semua contoh di halaman praktik sambil mencoba "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 03 ➡️](../Pertemuan-03-Atribut-dan-Method/README.md)
