# Kuis — Pertemuan 09: Polimorfisme

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 10 ➡️](../Pertemuan-10-Abstract-Class-dan-Interface/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Pernyataan mana yang paling tepat menggambarkan **polimorfisme**?

- A. Satu kelas boleh punya banyak atribut dengan tipe berbeda
- B. Kelas anak mewarisi semua atribut dan method kelas induk
- C. Objek dari kelas berbeda menanggapi pemanggilan method yang sama dengan caranya masing-masing
- D. Atribut disembunyikan agar hanya bisa diubah lewat method resmi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: polimorfisme berarti "banyak bentuk". Pemanggilan yang sama, misalnya `pembayaran.proses(total)`, ditanggapi berbeda oleh tunai, QRIS, dan kartu. Pilihan B adalah pewarisan, yang memang menjadi dasar polimorfisme, tetapi bukan polimorfisme itu sendiri. Pilihan D adalah enkapsulasi, dan pilihan A tidak berhubungan dengan polimorfisme.

</details>

### Soal 2

Perhatikan kode berikut.

**Python:**

```python
class Hewan:
    def bersuara(self):
        return "..."


class Kucing(Hewan):
    def bersuara(self):
        return "Meong"


class Ikan(Hewan):
    pass


for h in [Kucing(), Ikan(), Hewan()]:
    print(h.bersuara())
```

**Java:**

```java
class Hewan {
    String bersuara() { return "..."; }
}
class Kucing extends Hewan {
    @Override
    String bersuara() { return "Meong"; }
}
class Ikan extends Hewan { }

// di dalam main:
List<Hewan> daftar = List.of(new Kucing(), new Ikan(), new Hewan());
for (Hewan h : daftar) {
    System.out.println(h.bersuara());
}
```

Apa output-nya (tiga baris, berurutan)?

- A. `Meong`, `...`, `...`
- B. `...`, `...`, `...`
- C. `Meong`, `Meong`, `Meong`
- D. Error, karena `Ikan` tidak menulis method `bersuara`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: objek `Kucing` memakai versi miliknya sendiri (`Meong`). `Ikan` tidak meng-*override*, jadi pencarian method naik ke kelas induk dan menemukan versi `Hewan` (`...`). Objek `Hewan` tentu memakai versinya sendiri. Pilihan B keliru karena mengira tipe variabel `Hewan` yang menentukan versi. Pilihan D keliru karena kelas anak tidak wajib meng-*override*.

</details>

### Soal 3

Untuk method yang di-*override*, versi mana yang dijalankan ditentukan oleh ...

- A. tipe variabel yang tertulis di kode
- B. kelas yang paling dulu ditulis di dalam file
- C. jumlah kelas anak yang dimiliki kelas induk
- D. tipe objek yang sebenarnya, saat program berjalan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: inilah *dynamic dispatch*. Variabel bertipe `Hewan` yang menunjuk objek `Kucing` menjalankan `bersuara()` milik `Kucing`. Tipe variabel (pilihan A) hanya menentukan method apa saja yang **boleh dipanggil** di Java, bukan versi mana yang berjalan. Pilihan B dan C tidak berpengaruh sama sekali.

</details>

### Soal 4

Di Latihan 5, kelas `PembayaranVoucher` ditambahkan ke KedaiKita. Mengapa method `Pesanan.bayar()` **tidak perlu diubah**?

- A. Karena `bayar()` sudah memeriksa semua jenis pembayaran dengan `isinstance`/`instanceof`
- B. Karena `bayar()` hanya memanggil method milik `Pembayaran`, dan objek voucher **adalah** `Pembayaran` yang meng-*override* method-method itu
- C. Karena voucher tidak dikenai biaya layanan
- D. Karena Python dan Java otomatis menulis ulang `bayar()` saat ada kelas baru

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: `bayar()` memanggil `hitung_biaya_layanan`, `nama_metode`, dan `proses` tanpa tahu jenis pembayarannya. Kelas baru cukup meng-*override* method itu. Pilihan A justru keliru: `bayar()` tidak punya pemeriksaan jenis, dan jika punya, kelas baru akan memaksa `bayar()` diubah. Pilihan C benar tentang voucher, tetapi bukan alasannya. Pilihan D tidak pernah terjadi.

</details>

### Soal 5

Perhatikan kode berikut.

**Python:**

```python
class Kendaraan:
    def roda(self):
        return 4

    def info(self):
        return f"Punya {self.roda()} roda"


class Motor(Kendaraan):
    def roda(self):
        return 2


k = Motor()
print(k.info())
```

**Java:**

```java
class Kendaraan {
    int roda() { return 4; }
    String info() { return "Punya " + roda() + " roda"; }
}
class Motor extends Kendaraan {
    @Override
    int roda() { return 2; }
}

// di dalam main:
Kendaraan k = new Motor();
System.out.println(k.info());
```

Apa output-nya?

- A. `Punya 4 roda`
- B. Error, karena `Motor` tidak menulis method `info`
- C. `Punya 2 roda`
- D. `Punya 4 roda`, lalu `Punya 2 roda`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `info()` memang milik `Kendaraan`, tetapi di dalamnya `roda()` dipanggil lewat `self`/`this`, yaitu objek `Motor`. Karena itu versi `Motor` yang dipakai. Inilah polimorfisme dari dalam kelas. Pilihan A adalah jebakan "kode induk pasti memanggil versi induk". Pilihan B keliru karena `info()` diwarisi.

</details>

### Soal 6

Pernyataan yang **benar** tentang *upcasting* dan *downcasting* adalah ...

- A. *Downcasting* sebaiknya didahului pemeriksaan jenis, karena objek yang dipandang sebagai induk belum tentu kelas anak yang dituju
- B. *Upcasting* di Java wajib ditulis eksplisit, misalnya `(Pengguna) mhs`
- C. *Casting* mengubah objek `Dosen` menjadi objek `Mahasiswa`
- D. *Upcasting* berbahaya karena bisa memicu `ClassCastException`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: setiap mahasiswa pasti pengguna, jadi *upcasting* selalu aman dan otomatis (B dan D salah). Sebaliknya, tidak setiap pengguna adalah mahasiswa, jadi *downcasting* perlu `isinstance`/`instanceof` dulu. *Casting* hanya mengubah cara memandang objek, bukan objeknya (C salah). Salah *downcast* di Java menghasilkan `ClassCastException`.

</details>

### Soal 7

Kelas `Mahasiswa` adalah anak kelas `Pengguna`. Hanya `Mahasiswa` yang punya method `isi_krs()`/`isiKrs()`, yang mengembalikan `"KRS terisi"`. Perhatikan kode berikut.

**Python:**

```python
p = Mahasiswa()
print(p.isi_krs())
```

**Java:**

```java
Pengguna p = new Mahasiswa();
System.out.println(p.isiKrs());
```

Apa yang terjadi?

- A. Keduanya mencetak `KRS terisi`
- B. Keduanya gagal saat program berjalan
- C. Python gagal dengan `AttributeError`, sedangkan Java mencetak `KRS terisi`
- D. Python mencetak `KRS terisi`, sedangkan Java ditolak saat kompilasi karena tipe variabel `p` adalah `Pengguna`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: Python mencari method pada **objek** saat baris dijalankan. Objeknya `Mahasiswa`, jadi `isi_krs()` ditemukan. *Compiler* Java melihat **tipe variabel** `Pengguna`, yang tidak punya `isiKrs()`, sehingga muncul `cannot find symbol`. Perbaikannya di Java: `if (p instanceof Mahasiswa m) { ... m.isiKrs() ... }`. Pilihan C membalik perilaku kedua bahasa.

</details>

### Soal 8

Apa yang dimaksud dengan ***duck typing***?

- A. Java mengizinkan objek tanpa induk bersama disimpan dalam satu `List`
- B. Python menganggap objek cocok selama ia punya method yang dibutuhkan, tanpa memeriksa kelasnya
- C. Teknik memeriksa jenis objek dengan `isinstance` sebelum memanggil method
- D. Teknik menulis beberapa method bernama sama dengan parameter berbeda

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: "jika berbunyi seperti bebek, anggap saja bebek". Ayam jago, alarm, dan kentongan tanpa induk bersama tetap bisa diproses asalkan punya `bunyikan()`. Pilihan A keliru: Java justru butuh tipe bersama. Pilihan C adalah pemeriksaan jenis, kebalikan dari semangat *duck typing*. Pilihan D adalah *overloading*.

</details>

### Soal 9

Sebuah kelas Python punya dua method bernama `sapa`: yang pertama hanya punya parameter `self`, sedangkan yang kedua (ditulis di bawahnya) punya parameter `self` dan `nama`. Apa yang terjadi?

- A. Python memilih versi yang cocok berdasarkan jumlah argumen, seperti *overloading* di Java
- B. Python menolak kelas itu dengan `SyntaxError`
- C. Method kedua menimpa method pertama, sehingga `sapa()` tanpa argumen menghasilkan `TypeError`
- D. Kedua method otomatis digabung menjadi satu method dengan nilai bawaan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: Python tidak punya *overloading*. Nama `sapa` hanya bisa menunjuk satu method, jadi `def` kedua menimpa `def` pertama tanpa pesan error. Error baru muncul saat seseorang memanggil `sapa()` tanpa argumen: `missing 1 required positional argument: 'nama'`. Cara Python yang benar adalah nilai bawaan, misalnya `def sapa(self, nama="teman")`.

</details>

### Soal 10

Pasangan pernyataan mana yang **benar**?

- A. *Overloading*: di kelas anak, nama dan parameter sama. *Overriding*: nama sama, parameter berbeda
- B. *Overloading*: nama sama, parameter berbeda, dipilih saat kompilasi (Java). *Overriding*: nama dan parameter sama di kelas anak, dipilih saat program berjalan
- C. Keduanya dipilih saat kompilasi berdasarkan tipe variabel
- D. *Overloading* boleh dibedakan hanya dari tipe kembaliannya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: pilihan A tertukar. Pilihan C keliru, karena *overriding* dipilih saat program berjalan berdasarkan objek (ingat contoh 07 Java: `sambut(rina)` memakai versi `Tamu`, tetapi `rina.fasilitas()` memakai versi `TamuVip`). Pilihan D keliru, karena dua method dengan nama dan parameter sama ditolak *compiler* walaupun tipe kembaliannya berbeda (`is already defined`).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Konsep polimorfisme sudah kuat | Lanjut ke [Pertemuan 10](../Pertemuan-10-Abstract-Class-dan-Interface/README.md) |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 2 dan 4 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan contoh 01, 03, dan 04 di halaman praktik, lalu coba "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 10 ➡️](../Pertemuan-10-Abstract-Class-dan-Interface/README.md)
