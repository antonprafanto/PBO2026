# Kuis Pertemuan 03: Atribut dan *Method* Lebih Dalam

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 04 ➡️](../Pertemuan-04-Enkapsulasi/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar. Soal yang berisi kode ditampilkan dalam versi Python dan Java dengan arti yang sama; cukup baca versi bahasa pilihanmu.

---

### Soal 1

Kelas `Mahasiswa` punya beberapa data. Manakah yang paling tepat dijadikan **atribut kelas** (milik bersama), bukan atribut objek?

- A. NIM
- B. Nama lengkap
- C. Jumlah seluruh mahasiswa yang sudah terdaftar
- D. IPK

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: jumlah seluruh mahasiswa menggambarkan **semua** objek sekaligus, bukan milik satu mahasiswa tertentu. Karena itu, cocok menjadi atribut kelas (Java: `static`). NIM, nama, dan IPK berbeda untuk setiap mahasiswa, jadi tetap menjadi atribut objek. Jika NIM dijadikan atribut kelas, semua mahasiswa akan berbagi satu NIM yang sama.

</details>

### Soal 2

Perhatikan kode berikut.

**Python:**

```python
class Tiket:
    terjual = 0

    def __init__(self, film):
        self.film = film
        Tiket.terjual += 1


t1 = Tiket("Film A")
t2 = Tiket("Film B")
t3 = Tiket("Film C")
print(Tiket.terjual)
```

**Java:**

```java
class Tiket {
    static int terjual = 0;
    String film;

    Tiket(String film) {
        this.film = film;
        Tiket.terjual += 1;
    }
}

// di dalam main:
Tiket t1 = new Tiket("Film A");
Tiket t2 = new Tiket("Film B");
Tiket t3 = new Tiket("Film C");
System.out.println(Tiket.terjual);
```

Apa yang tercetak?

- A. `3`
- B. `1`
- C. `0`
- D. *Error* karena atribut kelas tidak boleh diubah di dalam konstruktor

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `terjual` adalah atribut kelas yang hanya ada satu. Setiap kali objek dibuat, konstruktor menambahnya **lewat nama kelas**, jadi setelah tiga objek nilainya 3. Pilihan B keliru karena menganggap setiap objek punya penghitung sendiri. Pilihan C (`0`) baru mungkin terjadi di Python jika penghitungnya ditulis `self.terjual += 1`, yaitu jebakan di contoh 02; di sini penghitungnya ditulis lewat nama kelas. Konstruktor boleh mengubah atribut kelas sehingga D juga salah.

</details>

### Soal 3

Sebuah kelas punya atribut kelas `total = 0`. Di dalam *method* objek, ada yang menulis `self.total += 1` (Python) atau `this.total += 1` (Java). Pernyataan yang **benar** adalah ...

- A. Di kedua bahasa, nilai bersama milik kelas bertambah dan tidak ada yang aneh
- B. Di kedua bahasa, objek itu mendapat atribut `total` baru miliknya sendiri
- C. Di Python nilai bersama bertambah, sedangkan di Java objek mendapat atribut `total` baru
- D. Di Python objek mendapat atribut `total` baru dan nilai bersama tetap; di Java nilai bersama bertambah, tetapi tulisannya menyesatkan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: di Python, mengisi atribut lewat objek selalu menyimpannya di objek itu sehingga lahir atribut "bayangan" dan atribut kelas tetap 0. Di Java, *field* `static` hanya ada satu, jadi `this.total` tetap berarti `NamaKelas.total`; hasilnya benar, tetapi tulisannya membuat pembaca mengira itu milik objek. Pilihan A hanya benar untuk Java, sedangkan B hanya benar untuk Python. Pilihan C adalah kebalikan dari yang sebenarnya terjadi. Pelajarannya sama untuk kedua bahasa: ubah atribut kelas lewat nama kelas.

</details>

### Soal 4

Perhatikan dua pemanggilan berikut (nama Java ditulis dalam kurung):

- `Tanggal.kabisat(2024)` (Java: `Tanggal.isKabisat(2024)`)
- `Tanggal.dari_teks("17-08-1945")` (Java: `Tanggal.dariTeks("17-08-1945")`)

Pernyataan yang **benar** adalah ...

- A. Keduanya *method* objek, jadi harus ada objek `Tanggal` lebih dulu
- B. Keduanya *method* milik kelas; yang pertama mengembalikan *boolean*, yang kedua membuat dan mengembalikan objek `Tanggal` baru
- C. Yang pertama adalah atribut kelas, sedangkan yang kedua adalah konstruktor biasa
- D. Keduanya mengubah atribut milik semua objek `Tanggal` yang sudah ada

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: keduanya dipanggil lewat **nama kelas** tanpa objek, jadi keduanya *method* milik kelas (Python: `@staticmethod` dan `@classmethod`; Java: *method* `static`). `kabisat` menjawab ya/tidak, sedangkan `dari_teks` adalah **konstruktor alternatif** yang membuat objek dari teks. Pilihan A salah karena *method* milik kelas justru tidak membutuhkan objek. Pilihan C salah karena keduanya dipanggil dengan tanda kurung seperti *method*, bukan dibaca seperti atribut, dan konstruktor biasa dipanggil dengan `Tanggal(...)` atau `new Tanggal(...)`. Keduanya juga tidak mengubah objek mana pun (D).

</details>

### Soal 5

Kelas `Durasi` punya *method* `tambah(lain)` yang **mengembalikan objek `Durasi` baru**. Setelah baris `total = kuliah.tambah(praktikum)` dijalankan, pernyataan yang benar adalah ...

- A. `total` menunjuk objek baru, sedangkan `kuliah` dan `praktikum` tidak berubah
- B. `kuliah` berubah menjadi hasil penjumlahan, lalu `total` menunjuk objek yang sama dengan `kuliah`
- C. `praktikum` dihapus karena sudah dijumlahkan
- D. `total` berisi angka biasa, bukan objek

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: *method* yang mengembalikan objek baru bekerja seperti `2 + 3`: hasilnya baru, angka asalnya tetap. `tambah()` membuat objek `Durasi` baru dan mengembalikannya, jadi `kuliah` dan `praktikum` tidak tersentuh. Pilihan B menggambarkan gaya *method* lain, yaitu *method* yang mengubah objeknya sendiri. Tidak ada objek yang terhapus hanya karena dipakai sebagai argumen (C). Hasil `tambah()` bertipe `Durasi`, bukan angka (D).

</details>

### Soal 6

Perhatikan kode berikut.

**Python:**

```python
class Menu:
    def __init__(self, kode, nama, harga, kategori, stok=0):
        self.nama = nama
        self.stok = stok


mie = Menu("M04", "Mie Goreng Jawa", 23000, "Makanan")
print(mie.stok)
```

**Java:**

```java
class Menu {
    String nama;
    int stok;

    Menu(String kode, String nama, int harga, String kategori, int stok) {
        this.nama = nama;
        this.stok = stok;
    }

    Menu(String kode, String nama, int harga, String kategori) {
        this(kode, nama, harga, kategori, 0);
    }
}

// di dalam main:
Menu mie = new Menu("M04", "Mie Goreng Jawa", 23000, "Makanan");
System.out.println(mie.stok);
```

Apa yang tercetak?

- A. *Error* karena argumen `stok` tidak dikirim
- B. `None` (Python) atau `null` (Java)
- C. `0`
- D. `23000`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: di Python, parameter `stok` punya nilai bawaan 0, jadi boleh tidak dikirim. Di Java, empat argumen memilih konstruktor kedua, yang meneruskan ke konstruktor lengkap lewat `this(..., 0)`. Hasilnya sama: stok 0. Tidak ada *error* (A). Stok juga tidak kosong (B) karena sudah diisi angka 0; di Java, atribut bertipe `int` bahkan tidak bisa berisi `null`. Nilai 23000 adalah harga, bukan stok (D).

</details>

### Soal 7

Apa tugas *method* `__str__` (Python) atau `toString()` (Java)?

- A. Mencetak semua atribut objek ke layar setiap kali objek dibuat
- B. Mengubah objek menjadi teks secara permanen sehingga atributnya hilang
- C. Membandingkan isi dua objek
- D. Mengembalikan teks yang mewakili objek; *method* ini dipanggil otomatis saat objek dicetak

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `print(objek)` atau `System.out.println(objek)` otomatis memanggil *method* ini untuk mendapatkan teksnya. *Method* ini harus **mengembalikan** teks dengan `return`, bukan mencetak sendiri (A). Objeknya tetap utuh setelah *method* dipanggil (B). Membandingkan isi objek adalah urusan `__eq__`/`equals()`, yang dibahas di Pertemuan 12 (C).

</details>

### Soal 8

Kelas `Ponsel` punya atribut `baterai` dan *method* `pakai(persen)` yang mengurangi baterai sebanyak `persen`. Perhatikan kode berikut.

**Python:**

```python
a = Ponsel("Budi", 80)
b = a
b.pakai(30)
print(a.baterai)
```

**Java:**

```java
Ponsel a = new Ponsel("Budi", 80);
Ponsel b = a;
b.pakai(30);
System.out.println(a.baterai);
```

Apa yang tercetak?

- A. `80`
- B. `50`
- C. `30`
- D. `110`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: `b = a` tidak membuat ponsel baru; `a` dan `b` menunjuk **objek yang sama** (*aliasing*). Memakai 30% lewat `b` berarti mengurangi baterai objek itu sehingga dilihat lewat `a` pun hasilnya 50. Pilihan A adalah miskonsepsi "`b = a` membuat salinan". Pilihan C (`30`) adalah banyaknya baterai yang dipakai, bukan sisanya, dan D (`110`) muncul jika `pakai()` dikira menambah baterai.

</details>

### Soal 9

Kelas `DompetDigital` punya atribut `saldo`. Perhatikan kode berikut.

**Python:**

```python
def tambah_bonus(dompet, angka):
    dompet.saldo = dompet.saldo + 5000
    angka = angka + 5000


d = DompetDigital("Siti", 20000)
x = 10000
tambah_bonus(d, x)
print(d.saldo, x)
```

**Java:**

```java
static void tambahBonus(DompetDigital dompet, int angka) {
    dompet.saldo = dompet.saldo + 5000;
    angka = angka + 5000;
}

// di dalam main:
DompetDigital d = new DompetDigital("Siti", 20000);
int x = 10000;
tambahBonus(d, x);
System.out.println(d.saldo + " " + x);
```

Apa yang tercetak?

- A. `20000 10000`
- B. `25000 15000`
- C. `25000 10000`
- D. `20000 15000`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: objek `d` dikirim sebagai referensi, jadi perubahan `dompet.saldo` mengubah objek yang sama milik pemanggil: saldonya menjadi 25000. Untuk angka, baris `angka = angka + 5000` hanya mengubah variabel `angka` milik fungsi (di Java, `angka` memang salinan nilai `x`; di Python, `angka` diarahkan ke angka baru). Jadi, `x` milik pemanggil tetap 10000. Pilihan B adalah jebakan bagi yang mengira angka juga ikut berubah. Pilihan A keliru karena objek yang dikirim memang ikut berubah, dan D adalah kebalikan dari yang sebenarnya terjadi.

</details>

### Soal 10

Pernyataan yang **benar** tentang membandingkan teks dan memeriksa variabel kosong adalah ...

- A. Isi teks dibandingkan dengan `==` di Python dan `.equals()` di Java; variabel kosong diperiksa dengan `x is None` (Python) atau `x == null` (Java)
- B. Isi teks dibandingkan dengan `is` di Python dan `==` di Java; variabel kosong diperiksa dengan `x == None` (Python) atau `x.equals(null)` (Java)
- C. `None`/`null` adalah objek kosong yang tetap punya *method* sehingga memanggil *method* lewat variabel kosong tidak menimbulkan *error*
- D. Di Java, `==` pada dua `String` selalu membandingkan isinya, sama seperti `==` di Python, jadi `.equals()` tidak diperlukan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: operator `==` punya arti berbeda. Di Python, `==` menanyakan isi; di Java, `==` pada objek menanyakan apakah objeknya sama sehingga teks harus dibandingkan dengan `.equals()` (B dan D salah). `is` di Python dipakai untuk pertanyaan "objek yang sama?" dan untuk memeriksa `None`. Pada pilihan B, `x.equals(null)` malah menimbulkan *error* jika `x` berisi `null` karena tidak ada objek yang bisa menjalankan `equals()`. `None`/`null` berarti tidak ada objek sehingga memanggil *method* lewatnya menimbulkan *error* (C salah).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Atribut dan *method* sudah kamu kuasai | Lanjut ke [Pertemuan 04](../Pertemuan-04-Enkapsulasi/README.md) |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 4 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan contoh 01, 02, 06, dan 07 di halaman praktik, lalu coba semua "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 04 ➡️](../Pertemuan-04-Enkapsulasi/README.md)
