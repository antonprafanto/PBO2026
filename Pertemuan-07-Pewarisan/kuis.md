# Kuis Pertemuan 07: Pewarisan

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 08 ➡️](../Pertemuan-08-UTS/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Kelas `Makanan` dan `Minuman` di KedaiKita awalnya punya atribut dan *method* yang hampir sama persis. Masalah utama apa yang diselesaikan pewarisan dalam kasus ini?

- A. Program berjalan lebih cepat
- B. Bagian yang sama cukup ditulis sekali di kelas induk sehingga perubahan aturan hanya dilakukan di satu tempat
- C. Semua atribut otomatis menjadi privat
- D. Dari setiap kelas hanya bisa dibuat satu objek

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: pewarisan menghilangkan duplikasi. Bagian umum dikumpulkan di `Menu` (generalisasi), lalu `Makanan` dan `Minuman` hanya menulis bagian khususnya. Pewarisan tidak membuat program lebih cepat (A), tidak mengubah hak akses (C), dan tidak membatasi jumlah objek (D).

</details>

### Soal 2

Pasangan manakah yang paling tepat dimodelkan dengan pewarisan, dengan kelas **pertama** sebagai kelas anak dan kelas **kedua** sebagai kelas induk?

- A. `Mobil` dan `Mesin`
- B. `Pesanan` dan `ItemPesanan`
- C. `Dosen` dan `Pegawai`
- D. `Kedai` dan `Menu`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: uji dengan kalimat "X **adalah** Y". "Dosen adalah pegawai" benar, jadi hubungannya *is-a*. Tiga pilihan lain adalah hubungan *has-a*: mobil **punya** mesin, pesanan **punya** item pesanan (komposisi), dan kedai **punya** daftar menu (agregasi). Hubungan "punya" diwujudkan dengan atribut, bukan pewarisan.

</details>

### Soal 3

Perhatikan kode berikut. Cukup baca dan tebak hasilnya, tidak perlu dijalankan.

**Python:**

```python
class Hewan:
    def __init__(self):
        print("Hewan")


class Mamalia(Hewan):
    def __init__(self):
        super().__init__()
        print("Mamalia")


class Kucing(Mamalia):
    def __init__(self):
        super().__init__()
        print("Kucing")


Kucing()
```

**Java:**

```java
class Hewan {
    Hewan() { System.out.println("Hewan"); }
}

class Mamalia extends Hewan {
    Mamalia() { super(); System.out.println("Mamalia"); }
}

class Kucing extends Mamalia {
    Kucing() { super(); System.out.println("Kucing"); }
}

// di dalam main:
new Kucing();
```

Apa *output*-nya (dari atas ke bawah)?

- A. `Kucing`, `Mamalia`, `Hewan`
- B. `Kucing` saja
- C. `Hewan` saja
- D. `Hewan`, `Mamalia`, `Kucing`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: konstruktor `Kucing` memang dipanggil pertama, tetapi baris pertamanya memanggil konstruktor `Mamalia`, yang baris pertamanya memanggil konstruktor `Hewan`. Jadi, `Hewan` dicetak lebih dulu, lalu kembali ke `Mamalia`, terakhir `Kucing`. Prinsipnya: lapis induk selesai lebih dulu. Pilihan A adalah urutan **pemanggilan**, bukan urutan **selesainya**. Pilihan B dan C keliru karena ketiga konstruktor sama-sama berjalan dan masing-masing mencetak satu baris.

</details>

### Soal 4

Di Java, kelas `Kendaraan` hanya punya satu konstruktor, yaitu `Kendaraan(String merek)`. Konstruktor kelas anak `Motor` **tidak** menulis `super(...)` sama sekali. Apa yang terjadi?

- A. Java menyisipkan `super()` tanpa argumen secara otomatis sehingga kompilasi gagal
- B. Program berjalan normal, dan *field* `merek` bernilai `null`
- C. Java otomatis meneruskan semua parameter `Motor` ke konstruktor `Kendaraan`
- D. Konstruktor `Kendaraan` dilewati, hanya konstruktor `Motor` yang berjalan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: jika `super(...)` tidak ditulis, Java menyisipkan `super();` di baris pertama. Karena `Kendaraan` tidak punya konstruktor tanpa parameter, kompilasi gagal dengan pesan `constructor Kendaraan in class Kendaraan cannot be applied to given types`. Java tidak pernah melewati konstruktor induk (D), dan tidak menebak argumen apa yang harus diteruskan (C). Pilihan B mirip yang terjadi di Python jika lupa `super().__init__(...)`: programnya berjalan, lalu gagal belakangan saat atribut induk dipakai.

</details>

### Soal 5

Perhatikan kode berikut. Cukup baca dan tebak hasilnya, tidak perlu dijalankan.

**Python:**

```python
class Produk:
    def info(self) -> str:
        return "Produk"


class Minuman(Produk):
    def info(self) -> str:
        return super().info() + " > Minuman"


class KopiSusu(Minuman):
    def info(self) -> str:
        return super().info() + " > Kopi Susu"


print(KopiSusu().info())
```

**Java:**

```java
class Produk {
    public String info() { return "Produk"; }
}

class Minuman extends Produk {
    @Override
    public String info() { return super.info() + " > Minuman"; }
}

class KopiSusu extends Minuman {
    @Override
    public String info() { return super.info() + " > Kopi Susu"; }
}

// di dalam main:
System.out.println(new KopiSusu().info());
```

Apa *output*-nya?

- A. `Kopi Susu`
- B. `Produk`
- C. `Produk > Minuman > Kopi Susu`
- D. `Kopi Susu > Minuman > Produk`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `KopiSusu.info()` memanggil versi induknya (`Minuman.info()`), yang memanggil versi induknya lagi (`Produk.info()`). Hasil paling dalam adalah `"Produk"`, lalu setiap tingkat menambahkan teksnya di **belakang**: `"Produk > Minuman"`, kemudian `"Produk > Minuman > Kopi Susu"`. Pilihan D membalik urutan penggabungan. Pilihan A akan benar jika `KopiSusu` tidak memakai `super`, sedangkan B mengabaikan tambahan teks dari kedua kelas anak.

</details>

### Soal 6

Pernyataan yang **benar** tentang hak akses untuk kelas anak adalah ...

- A. Java `protected` terbuka untuk kelas anak dan juga semua kelas di paket yang sama, sedangkan Python memakai kesepakatan satu garis bawah seperti `_saldo`
- B. Java `protected` hanya bisa diakses oleh kelas anak, tidak oleh kelas lain mana pun
- C. Python `__saldo` (dua garis bawah) adalah cara yang tepat agar atribut bisa dipakai kelas anak
- D. Atribut `private` milik induk tidak ikut ada di objek kelas anak

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `protected` di Java juga terbuka untuk satu paket, jebakan yang sering terlupa (B salah). Di Python, `__saldo` justru memicu *name mangling* sehingga kelas anak **gagal** menemukannya (C salah). Atribut `private` tetap **ada** di objek anak, hanya saja tidak bisa disentuh langsung oleh kode kelas anak (D salah).

</details>

### Soal 7

Apa fungsi anotasi `@Override` di Java?

- A. Membuat *method* berjalan lebih cepat, dan di Python penandanya `super()`
- B. Meminta *compiler* memeriksa bahwa *method* itu benar-benar menimpa *method* induk; Python tidak punya pemeriksaan bawaan seperti ini
- C. Mengunci *method* agar tidak bisa ditimpa lagi oleh kelas cucu
- D. Wajib ditulis karena tanpa `@Override` *override* tidak akan terjadi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: dengan `@Override`, salah ketik nama *method* atau perbedaan parameter langsung ketahuan saat kompilasi (`method does not override or implement a method from a supertype`). *Override* tetap terjadi tanpa anotasi itu, jadi D salah, tetapi menulisnya sangat disarankan. Mengunci *method* adalah tugas `final` (C). Anotasi tidak memengaruhi kecepatan program, dan `super()` di Python adalah cara memanggil versi induk, bukan penanda *override* (A). Di Python, *method* yang salah ketik diam-diam menjadi *method* baru.

</details>

### Soal 8

Pernyataan yang **benar** tentang pewarisan ganda (*multiple inheritance*) adalah ...

- A. Python dan Java sama-sama mengizinkan satu kelas punya banyak induk
- B. Java mengizinkannya, sedangkan Python tidak
- C. Keduanya melarang karena pewarisan ganda selalu menimbulkan *error*
- D. Python mengizinkannya dan memakai MRO untuk menentukan urutan pencarian *method*, sedangkan Java hanya mengizinkan satu induk

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: Python menerima `class MobilAmfibi(KendaraanDarat, KendaraanAir):` dan mencari *method* mengikuti MRO (urutannya bisa dilihat dengan `MobilAmfibi.__mro__`). Java menolak `extends` dengan dua kelas, jadi A dan B salah. Pilihan C juga salah: Python mengizinkannya, dan pewarisan ganda yang dirancang dengan baik berjalan tanpa *error*. Untuk menggabungkan beberapa kemampuan, Java memakai *interface* (Pertemuan 10).

</details>

### Soal 9

Kelas `Anggora` mewarisi `Kucing`, dan `Kucing` mewarisi `Hewan`. Objek `oyen` dibuat dari kelas `Kucing`. Jika diperiksa dengan `isinstance` (Python) atau `instanceof` (Java), pernyataan mana yang benar?

- A. `oyen` termasuk `Hewan`, tetapi tidak termasuk `Anggora`
- B. `oyen` termasuk `Hewan` dan juga termasuk `Anggora`
- C. `oyen` tidak termasuk `Hewan`, tetapi termasuk `Anggora`
- D. `oyen` hanya termasuk `Kucing`, tidak termasuk kelas lain mana pun

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: setiap kucing adalah hewan, jadi `isinstance(oyen, Hewan)` dan `oyen instanceof Hewan` bernilai benar (D salah). Pemeriksaan hanya berlaku **ke atas**: oyen dibuat dari `Kucing`, bukan dari `Anggora`, dan tidak setiap kucing adalah anggora. Jadi, B dan C salah. Jika dicetak, Python menampilkan `True False`, sedangkan Java menampilkan `true false`.

</details>

### Soal 10

Kelas `Pelanggan` tidak menulis kelas induk apa pun, tetapi punya *method* `__str__` (Python) atau `toString()` dengan `@Override` (Java). Apa yang sebenarnya terjadi?

- A. Kita membuat *method* baru yang sama sekali tidak berhubungan dengan kelas lain
- B. Kita melakukan *overload* terhadap *method* `print`
- C. Kita meng-*override* *method* milik kelas akar `object` (Python) / `Object` (Java), yang otomatis menjadi induk setiap kelas
- D. Kita mewarisi *method* itu dari kelas `Menu`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: kelas yang tidak menulis induk tetap punya induk, yaitu kelas akar `object`/`Object`. Dari sanalah setiap objek mendapat teks bawaan, seperti `<__main__.Pelanggan object at 0x...>` atau `Pelanggan@1b6d3586`. Menulis `__str__`/`toString()` berarti menimpa versi bawaan itu. Karena itu pula, `@Override` di Java tidak protes. Jadi, *method* itu bukan *method* baru yang tidak berhubungan (A). Ini juga bukan *overload* karena tidak ada variasi parameter, dan `print` sendiri tidak diubah (B). `Pelanggan` tidak berhubungan dengan `Menu` (D).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Konsep pewarisan sudah kuat | Lanjut ke [Pertemuan 08 (UTS)](../Pertemuan-08-UTS/README.md) dan kerjakan latihan soalnya |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 6 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, lalu jalankan contoh 02 sampai 04 di halaman praktik sambil mencoba "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 08 ➡️](../Pertemuan-08-UTS/README.md)
