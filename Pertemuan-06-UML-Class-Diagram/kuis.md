# Kuis Pertemuan 06: UML *Class Diagram*

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 07 ➡️](../Pertemuan-07-Pewarisan/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Pernyataan yang paling tepat tentang UML adalah ...

- A. UML adalah bahasa pemodelan visual standar untuk menggambarkan dan merancang perangkat lunak
- B. UML adalah bahasa pemrograman berorientasi objek buatan OMG
- C. UML adalah aplikasi yang otomatis mengubah kode menjadi gambar
- D. UML hanya bisa dipakai untuk program yang ditulis dengan Java

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: UML adalah bahasa **pemodelan** visual yang distandarkan oleh OMG sejak 1997. UML bukan bahasa pemrograman (B salah) dan tidak bisa dijalankan. Mermaid atau StarUML adalah **alat** untuk menggambar UML, bukan UML itu sendiri (C salah). UML netral terhadap bahasa sehingga bisa dipakai untuk Python, Java, maupun bahasa lain (D salah).

</details>

### Soal 2

Di sebuah kotak kelas tertulis `#biayaAdmin : int`. Artinya ...

- A. atribut publik bertipe `int`
- B. atribut milik kelas (*static*) bernama `biayaAdmin`
- C. atribut *protected*: boleh diakses kelas itu sendiri dan kelas anaknya
- D. atribut yang hanya boleh diakses kelas-kelas dalam satu paket

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `#` berarti *protected*. Publik ditulis `+` (A), akses satu paket ditulis `~` (D), sedangkan *static* tidak ditandai dengan simbol di depan, tetapi dengan garis bawah (di Mermaid: `$` di akhir baris) sehingga B salah.

</details>

### Soal 3

Kamu ingin menuliskan *method* *static* `jumlahPaket()` yang mengembalikan `int` di dalam kotak kelas Mermaid. Penulisan yang benar adalah ...

- A. `+$jumlahPaket() int`
- B. `+static jumlahPaket() int`
- C. `+jumlahPaket() int*`
- D. `+jumlahPaket() int$`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: di Mermaid, anggota *static* ditandai `$` di **paling akhir** baris, lalu digambar bergaris bawah. Tanda `*` di akhir baris (C) berarti **abstrak** sehingga *method* tampil miring. Mermaid tidak menganggap kata `static` sebagai penanda (B); kata itu hanya ikut tercetak sebagai bagian dari nama. Tanda `$` di depan nama (A) juga hanya tercetak sebagai huruf biasa, tanpa garis bawah.

</details>

### Soal 4

Perhatikan relasi `Pesanan "1" *-- "*" ItemPesanan`. Pernyataan yang benar adalah ...

- A. Setiap pesanan berisi nol atau lebih item, dan setiap item milik tepat satu pesanan
- B. Setiap item boleh dimiliki banyak pesanan sekaligus
- C. Setiap pesanan berisi tepat satu item
- D. Pesanan dan item bisa hidup terpisah tanpa saling bergantung

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: dibaca dari `Pesanan`, angka di ujung seberang adalah `*`: satu pesanan berisi nol atau lebih item. Dibaca dari `ItemPesanan`, angka di ujung seberang adalah `1`: setiap item milik tepat satu pesanan, jadi B dan C salah. Belah ketupat penuh berarti komposisi: item tidak berarti tanpa pesanannya sehingga D juga salah.

</details>

### Soal 5

*"Sebuah formulir pendaftaran terdiri atas beberapa isian. Isian dibuat oleh formulir itu sendiri dan tidak berarti tanpa formulirnya."* Relasi yang paling tepat antara `Formulir` dan `Isian` adalah ...

- A. Asosiasi
- B. Agregasi
- C. Dependensi
- D. Komposisi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: tiga ciri komposisi terpenuhi: bagian dibuat oleh keseluruhan, tidak dibagi dengan formulir lain, dan berakhir bersama formulirnya. Agregasi (B) dipakai jika bagian dibuat di luar dan bisa hidup sendiri. Asosiasi (A) terlalu umum untuk hubungan seerat ini, sedangkan dependensi (C) hanya untuk pemakaian sementara.

</details>

### Soal 6

Penulisan Mermaid yang benar untuk menyatakan "Makanan **adalah** Menu" adalah ...

- A. `Makanan <|-- Menu`
- B. `Menu <|-- Makanan`
- C. `Menu *-- Makanan`
- D. `Menu ..> Makanan`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: pada generalisasi, segitiga kosong menempel pada **induk**. `Menu <|-- Makanan` menaruh segitiga di sisi `Menu`, artinya Makanan adalah Menu. Pilihan A adalah kesalahan klasik "panah terbalik" yang berarti Menu adalah Makanan. C adalah komposisi dan D adalah dependensi, bukan hubungan "adalah".

</details>

### Soal 7

Perhatikan potongan kode berikut.

**Python:**

```python
class Motor:
    def isi_bensin(self, spbu: SPBU, liter: int) -> int:
        return liter * spbu.harga_per_liter
```

**Java:**

```java
class Motor {
    public int isiBensin(SPBU spbu, int liter) {
        return liter * spbu.getHargaPerLiter();
    }
}
```

Relasi `Motor` ke `SPBU` yang paling tepat adalah ...

- A. `Motor --> SPBU` (asosiasi)
- B. `Motor o-- SPBU` (agregasi)
- C. `Motor ..> SPBU` (dependensi)
- D. `SPBU <|-- Motor` (generalisasi)

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: objek `SPBU` hanya datang sebagai **parameter** dan tidak disimpan di atribut atau *field* mana pun. Pemakaian sementara seperti ini adalah dependensi. Asosiasi (A) dan agregasi (B) mensyaratkan referensi yang disimpan di atribut. Motor juga bukan "jenis" SPBU (D).

</details>

### Soal 8

Perhatikan potongan kode berikut.

**Python:**

```python
class Tiket:
    _terjual = 0

    def __init__(self, harga: int):
        Tiket._terjual += 1
        self._harga = harga
```

**Java:**

```java
class Tiket {
    private static int terjual = 0;
    private int harga;

    public Tiket(int harga) {
        terjual++;
        this.harga = harga;
    }
}
```

Baris diagram yang tepat untuk penghitung `terjual` (versi Python: `_terjual`) adalah ...

- A. `+terjual : int`
- B. `-terjual : int = 0$`
- C. `-terjual() int`
- D. `#terjual : int$`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: penghitung itu **privat** (Java `private`, Python awalan `_`), bertipe `int`, bernilai awal 0, dan **milik kelas** (Java `static`, Python atribut kelas) sehingga ditulis `-terjual : int = 0$`. A salah visibilitas dan tidak *static*. C menggambarkannya sebagai *method*. D memakai `#` (*protected*), yang tidak sesuai dengan kodenya.

</details>

### Soal 9

Perhatikan potongan kode berikut.

**Python:**

```python
class Kursi:
    def __init__(self, nomor: str):
        self._nomor = nomor
        self._penonton: Penonton | None = None

    def pesan(self, penonton: Penonton):
        self._penonton = penonton
```

**Java:**

```java
class Kursi {
    private String nomor;
    private Penonton penonton; // null selama kursi belum dipesan

    public Kursi(String nomor) {
        this.nomor = nomor;
        this.penonton = null;
    }

    public void pesan(Penonton penonton) {
        this.penonton = penonton;
    }
}
```

Multiplisitas yang tepat di ujung `Penonton` pada relasi `Kursi --> Penonton` adalah ...

- A. `0..1`
- B. `1`
- C. `1..*`
- D. `*`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: setiap kursi menyimpan **paling banyak satu** penonton, dan nilainya boleh kosong (`None`/`null`) sebelum dipesan. Itulah `0..1`. Multiplisitas `1` (B) berarti wajib ada sejak awal, biasanya lewat konstruktor. `1..*` (C) dan `*` (D) berarti banyak penonton, padahal atributnya hanya satu objek, bukan *list*.

</details>

### Soal 10

Kamu bergabung dengan proyek lama yang tidak punya dokumentasi. Langkah pertamamu adalah menggambar diagram kelas dari kode yang sudah ada agar paham strukturnya. Kegiatan ini disebut ...

- A. *Forward engineering*
- B. *Refactoring*
- C. *Reverse engineering*
- D. *Debugging*

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: membuat diagram **dari** kode yang sudah ada disebut *reverse engineering*, seperti mengukur rumah tua lalu menggambar ulang denahnya. *Forward engineering* (A) adalah kebalikannya: menulis kode dari diagram. *Refactoring* (B) mengubah struktur kode tanpa mengubah perilakunya (Pertemuan 13), dan *debugging* (D) adalah mencari dan memperbaiki kesalahan program.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Kamu sudah fasih membaca dan menulis diagram kelas | Lanjut ke [Pertemuan 07](../Pertemuan-07-Pewarisan/README.md) dan bawa diagram rencana `Menu`, `Makanan`, `Minuman` |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 2 dan 3 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, terutama bagian relasi dan multiplisitas, lalu cocokkan setiap contoh di halaman praktik dengan diagramnya |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 07 ➡️](../Pertemuan-07-Pewarisan/README.md)
