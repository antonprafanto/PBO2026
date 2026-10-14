# Kuis — Pertemuan 10: Abstract Class dan Interface

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 11 ➡️](../Pertemuan-11-Exception-Handling/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Saat menyetir mobil, kamu cukup memakai setir, pedal gas, dan rem tanpa perlu tahu cara kerja mesinnya. Prinsip PBO yang paling tepat digambarkan oleh contoh ini adalah ...

- A. Pewarisan: mobil mewarisi kemampuan dari kendaraan
- B. Abstraksi: yang penting ditonjolkan, detail yang rumit disembunyikan
- C. *Overloading*: satu nama method untuk banyak parameter
- D. Instansiasi: membuat objek dari kelas

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: abstraksi berarti menonjolkan hal penting bagi pemakai (setir, gas, rem) dan menyembunyikan detail yang tidak perlu diketahuinya (cara kerja mesin). Pewarisan (A) membahas hubungan kelas induk dan anak, bukan "apa yang ditunjukkan kepada pemakai". *Overloading* (C) dan instansiasi (D) tidak berhubungan dengan menyembunyikan detail.

</details>

### Soal 2

Pernyataan yang **benar** tentang kelas abstrak adalah ...

- A. Semua method di dalam kelas abstrak wajib abstrak
- B. Kelas abstrak tidak boleh punya atribut maupun konstruktor
- C. Kelas abstrak hanya boleh punya satu kelas anak
- D. Kelas abstrak boleh punya atribut, konstruktor, dan method konkret, tetapi objeknya tidak bisa dibuat secara langsung

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: kelas abstrak tetap boleh berisi atribut, konstruktor, dan method yang sudah berisi. Contohnya `Kendaraan` (punya `plat`, konstruktor, dan `isi_bensin()`) serta `Pembayaran` di KedaiKita (punya method konkret `deskripsi()`). Yang dilarang hanyalah membuat objeknya secara langsung. Pilihan A dan B adalah miskonsepsi yang sering muncul. Pilihan C salah karena kelas abstrak boleh punya kelas anak sebanyak apa pun.

</details>

### Soal 3

Perhatikan kode berikut.

**Python:**

```python
class Hewan(ABC):
    @abstractmethod
    def bersuara(self) -> str: ...


class Kucing(Hewan):
    pass


print("Mulai")
oyen = Kucing()
print("Selesai")
```

**Java:**

```java
abstract class Hewan {
    public abstract String bersuara();
}

class Kucing extends Hewan {
}

// di dalam main:
System.out.println("Mulai");
Kucing oyen = new Kucing();
System.out.println("Selesai");
```

Apa yang terjadi saat program dijalankan?

- A. Python mencetak `Mulai` lalu berhenti dengan `TypeError`, sedangkan Java gagal dikompilasi sehingga tidak mencetak apa pun
- B. Keduanya mencetak `Mulai` dan `Selesai`, karena `bersuara()` tidak pernah dipanggil
- C. Keduanya gagal sebelum mencetak apa pun
- D. Python mencetak `Mulai` dan `Selesai`, sedangkan Java gagal dikompilasi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `Kucing` belum mengisi method abstrak `bersuara()`, sehingga `Kucing` masih abstrak. Python baru memeriksanya saat objek dibuat, jadi `Mulai` sempat tercetak sebelum `TypeError: Can't instantiate abstract class Kucing ...` muncul. Java memeriksanya saat kompilasi (*Kucing is not abstract and does not override abstract method bersuara()*), sehingga tidak ada satu baris pun yang dijalankan. Pilihan B dan D keliru: walaupun `bersuara()` tidak pernah dipanggil, satu method abstrak yang belum diisi sudah cukup membuat `Kucing` abstrak, sehingga objeknya tidak boleh dibuat.

</details>

### Soal 4

Method konkret di kelas abstrak yang menetapkan **urutan langkah** sebuah proses, lalu memanggil method abstrak untuk langkah-langkah yang berbeda di setiap kelas anak, disebut ...

- A. Konstruktor
- B. *Default method*
- C. Template method
- D. *Getter*

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: template method, misalnya `tampilkan()` pada `Laporan` atau `deskripsi()` pada `Pembayaran`, menetapkan kerangka yang sama untuk semua kelas anak. *Default method* (B) adalah method berisi di dalam interface Java. Memang bisa memanggil method abstrak juga, tetapi istilah untuk pola "kerangka tetap di kelas abstrak" adalah template method. Konstruktor (A) dan *getter* (D) tidak berhubungan dengan urutan langkah.

</details>

### Soal 5

Situasi manakah yang **paling tepat** diselesaikan dengan *interface*?

- A. `Makanan` dan `Minuman` sama-sama menu yang punya kode, nama, dan harga
- B. `Kedai` dan `Pesanan` tidak bersaudara, tetapi sama-sama perlu bisa dicetak oleh satu fungsi yang sama
- C. Membuat banyak objek menu dari satu kelas `Menu`
- D. Menyembunyikan atribut harga agar tidak diubah sembarangan dari luar kelas

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: interface cocok untuk hubungan "bisa" (*can-do*) antara kelas-kelas yang tidak bersaudara, persis seperti `DapatDicetak` di KedaiKita. Pilihan A adalah hubungan "adalah" dengan data bersama, sehingga lebih cocok memakai kelas induk (atau kelas abstrak). Pilihan C adalah konsep kelas dan objek biasa. Pilihan D adalah enkapsulasi.

</details>

### Soal 6

`Bebek` mewarisi kelas abstrak `Hewan` dan memenuhi interface `BisaTerbang`. `Pesawat` hanya memenuhi interface `BisaTerbang`. Pernyataan yang **benar** adalah ...

- A. `Pesawat` termasuk `Hewan`, karena sama-sama bisa terbang seperti `Bebek`
- B. `Bebek` dan `Pesawat` tidak boleh dimasukkan ke dalam satu daftar yang sama
- C. `Bebek` termasuk `BisaTerbang`, sedangkan `Pesawat` tidak termasuk `Hewan`
- D. `Bebek` tidak lagi termasuk `Hewan`, karena sudah memenuhi sebuah interface

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `Bebek` lolos pemeriksaan `isinstance(bebek, BisaTerbang)` / `bebek instanceof BisaTerbang`, karena ia memenuhi kontrak itu. Sebaliknya, `Pesawat` tidak termasuk `Hewan`, karena ia tidak mewarisi `Hewan`. Pilihan A adalah jebakan "semua yang bisa terbang pasti hewan": interface menyatukan kemampuan, bukan silsilah. Keduanya justru boleh masuk ke satu daftar bertipe `BisaTerbang` (B salah), dan `Bebek` tetap seekor `Hewan` walaupun memenuhi interface (D salah).

</details>

### Soal 7

Perhatikan kode berikut.

**Python:**

```python
class Laporan(ABC):
    def tampilkan(self):
        print(f"[{self.judul()}] {self.penutup()}")

    @abstractmethod
    def judul(self) -> str: ...

    def penutup(self) -> str:
        return "selesai"


class LaporanKas(Laporan):
    def judul(self) -> str:
        return "KAS"


LaporanKas().tampilkan()
```

**Java:**

```java
abstract class Laporan {
    public void tampilkan() {
        System.out.println("[" + judul() + "] " + penutup());
    }

    public abstract String judul();

    public String penutup() {
        return "selesai";
    }
}

class LaporanKas extends Laporan {
    @Override
    public String judul() {
        return "KAS";
    }
}

// di dalam main:
new LaporanKas().tampilkan();
```

Apa output-nya?

- A. Error, karena `LaporanKas` tidak meng-*override* `penutup()`
- B. Error, karena `tampilkan()` ditulis di kelas abstrak
- C. `[KAS]` saja, tanpa penutup
- D. `[KAS] selesai`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `tampilkan()` adalah template method milik kelas abstrak, dan objek yang menjalankannya adalah `LaporanKas`. `judul()` terpanggil dari `LaporanKas` (`KAS`). `penutup()` adalah *hook* yang sudah punya isi bawaan, jadi kelas anak **boleh** tidak meng-*override*-nya. Yang wajib diisi hanyalah method abstrak, sehingga A salah. Method konkret di kelas abstrak boleh dipakai objek kelas anak, sehingga B juga salah.

</details>

### Soal 8

Di Java, sebuah kelas boleh ...

- A. meng-*extends* paling banyak satu kelas, tetapi meng-*implements* banyak interface
- B. meng-*extends* banyak kelas dan banyak interface
- C. meng-*implements* paling banyak satu interface
- D. memilih salah satu saja: meng-*extends* kelas atau meng-*implements* interface, tidak boleh keduanya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: Java hanya mengizinkan satu kelas induk (Pertemuan 07), tetapi interface boleh banyak, misalnya `class Bebek extends Hewan implements BisaTerbang, BisaBerenang`. Contoh itu sekaligus menunjukkan bahwa D salah: `extends` dan `implements` boleh dipakai bersamaan. Kata kunci untuk interface adalah `implements`, bukan `extends`, sehingga B juga salah.

</details>

### Soal 9

Pada diagram kelas UML, relasi yang digambar dengan **garis putus-putus** dan **segitiga kosong** yang menunjuk ke sebuah `<<interface>>` disebut ...

- A. Pewarisan (*inheritance*)
- B. Komposisi (*composition*)
- C. Realisasi (*realization*)
- D. Asosiasi (*association*)

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: realisasi menunjukkan bahwa sebuah kelas memenuhi (mengimplementasikan) interface, misalnya `Kedai ..|> DapatDicetak` di Mermaid. Pewarisan (A) juga memakai segitiga kosong, tetapi garisnya **lurus**. Komposisi (B) memakai belah ketupat penuh, dan asosiasi (D) memakai garis lurus biasa.

</details>

### Soal 10

Di KedaiKita Pertemuan 10, method `cetak_struk()` milik `Pesanan` diganti nama menjadi `cetak()`. Apa alasan utamanya?

- A. Agar struk tercetak lebih cepat
- B. Kontrak `DapatDicetak` mewajibkan method bernama `cetak()`. Dengan nama yang seragam, `cetak_semua()` bisa mencetak kedai maupun pesanan lewat satu panggilan yang sama
- C. Karena nama method di Python dan Java tidak boleh mengandung kata "struk"
- D. Karena `Pesanan` kini menjadi kelas abstrak

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: `Pesanan` menyatakan diri memenuhi `DapatDicetak`, dan kontrak itu menuntut method bernama persis `cetak()`. Tanpa penggantian nama, kontraknya tidak terpenuhi: Python menolak membuat objek `Pesanan` dan Java menolak mengompilasinya. Nama yang seragam itulah yang membuat `cetak_semua()` bisa memanggil `dokumen.cetak()` tanpa peduli jenis dokumennya. `Pesanan` tetap kelas konkret (D salah), dan penggantian nama tidak memengaruhi kecepatan (A).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Kamu sudah bisa membedakan kelas abstrak dan interface | Lanjut ke [Pertemuan 11](../Pertemuan-11-Exception-Handling/README.md) |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian [Kelas Abstrak atau Interface?](README.md#9-kelas-abstrak-atau-interface) dan kerjakan Latihan 4 dan 5 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, lalu jalankan contoh 01 sampai 06 di halaman praktik sambil mencoba bagian "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 11 ➡️](../Pertemuan-11-Exception-Handling/README.md)
