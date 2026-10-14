# Kuis Pertemuan 12: Koleksi dan *Generics*

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 13 ➡️](../Pertemuan-13-Prinsip-SOLID/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar. Kode di dalam soal hanyalah potongan; anggap baris `import` dan kelas yang dibutuhkan sudah ada.

---

### Soal 1

Panitia seminar ingin mencatat NIM peserta yang memindai QR di pintu masuk. Peserta yang memindai dua kali harus tetap dihitung **sekali**, dan panitia sering bertanya "apakah NIM ini sudah tercatat?". Koleksi yang paling tepat adalah ...

- A. *list* karena bisa menampung data kembar
- B. set karena otomatis membuang data kembar dan cepat menjawab "ada atau tidak"
- C. *tuple* karena isinya tidak bisa diubah
- D. map dengan kunci nomor urut pindai

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: set menolak data kembar dan memeriksa keanggotaan dengan cepat lewat kode *hash*. *List* (A) justru menyimpan hasil pindai ganda sehingga peserta dihitung dua kali, dan pemeriksaan `in`/`contains` pada *list* memeriksa satu per satu. *Tuple* (C) tidak bisa ditambah saat peserta baru datang. Map dengan kunci nomor urut pindai (D) tetap menyimpan NIM yang sama berkali-kali sebagai nilai.

</details>

### Soal 2

Pernyataan yang **benar** tentang urutan isi koleksi saat dijelajahi adalah ...

- A. `HashMap` di Java selalu mengikuti urutan data dimasukkan
- B. `set` di Python selalu tersusun urut abjad
- C. `dict` di Python (3.7 ke atas) dan `LinkedHashMap` di Java menjaga urutan kunci dimasukkan
- D. `TreeMap` di Java mengikuti urutan data dimasukkan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `dict` Python dijamin menjaga urutan kunci dimasukkan sejak versi 3.7, dan `LinkedHashMap` dibuat khusus untuk itu. `HashMap` (A) dan `set` Python (B) tidak menjamin urutan apa pun; urutan set berisi teks bahkan bisa berubah setiap kali program dijalankan. `TreeMap` (D) mengurutkan kuncinya, bukan mengikuti urutan masuk.

</details>

### Soal 3

Perhatikan kode berikut.

**Python:**

```python
hitung = {}
for huruf in ["a", "b", "a", "c", "a"]:
    hitung[huruf] = hitung.get(huruf, 0) + 1
print(hitung["a"], len(hitung))
```

**Java:**

```java
Map<String, Integer> hitung = new HashMap<>();
for (String huruf : List.of("a", "b", "a", "c", "a")) {
    hitung.put(huruf, hitung.getOrDefault(huruf, 0) + 1);
}
System.out.println(hitung.get("a") + " " + hitung.size());
```

Apa yang tercetak?

- A. `3 3`
- B. `3 5`
- C. `1 3`
- D. `5 3`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: huruf "a" muncul 3 kali sehingga nilainya 3. Kunci map unik, jadi isinya hanya tiga kunci: "a", "b", dan "c". Pilihan B keliru karena mengira jumlah isi map sama dengan jumlah data masukan (5). Pilihan C lupa bahwa nilai lama ditambah 1 setiap kali huruf yang sama muncul. Pilihan D mengira nilai "a" sama dengan jumlah semua huruf (5), padahal yang dihitung hanya kemunculan "a".

</details>

### Soal 4

Di Java, mengapa daftar menu ditulis `List<Menu> daftar = new ArrayList<>();`, bukan `ArrayList<Menu> daftar = new ArrayList<>();`?

- A. Karena `ArrayList` tidak boleh dipakai sebagai tipe variabel
- B. Agar *list* menjadi tetap (*immutable*) dan tidak bisa diubah
- C. Karena `List` bekerja lebih cepat daripada `ArrayList`
- D. Agar kode lain hanya bergantung pada kontrak `List` sehingga wujudnya bisa diganti tanpa mengubah kode lain

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `List` adalah *interface* (kontrak), sedangkan `ArrayList` adalah wujudnya. Menulis tipe kontrak membuat kode lebih lentur, sama seperti prinsip *interface* di Pertemuan 10. Pilihan A salah karena `ArrayList<Menu> daftar` tetap sah, hanya kurang lentur. *List* tetap dibuat dengan `List.of`, bukan dengan menulis tipe `List` (B). Pilihan C juga salah: `List` hanyalah kontrak tanpa kode yang bekerja, jadi kecepatannya ditentukan oleh wujudnya, yaitu `ArrayList` itu sendiri.

</details>

### Soal 5

Perhatikan kode berikut. Kelas `Peserta` punya nama dan skor.

**Python:**

```python
data = [Peserta("Ayu", 80), Peserta("Bima", 90), Peserta("Citra", 80)]
data.sort(key=lambda p: (-p.skor, p.nama))
```

**Java:**

```java
List<Peserta> data = new ArrayList<>(List.of(new Peserta("Ayu", 80),
        new Peserta("Bima", 90), new Peserta("Citra", 80)));
data.sort(Comparator.comparing(Peserta::getSkor).reversed()
        .thenComparing(Peserta::getNama));
```

Setelah diurutkan, urutan nama pesertanya adalah ...

- A. Ayu, Bima, Citra
- B. Bima, Citra, Ayu
- C. Citra, Ayu, Bima
- D. Bima, Ayu, Citra

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: kriteria pertama adalah skor terbesar dulu (tanda minus di Python, `.reversed()` di Java), jadi Bima (90) di depan. Ayu dan Citra seri 80 sehingga kriteria kedua (nama A-Z) menempatkan Ayu sebelum Citra. Pilihan A hanya urut nama. Pilihan B membalik nama juga, padahal `.reversed()` ditulis sebelum `thenComparing` sehingga hanya membalik skor. Pilihan C mengurutkan skor dari yang terkecil, kebalikan dari tanda minus di Python dan `.reversed()` di Java.

</details>

### Soal 6

Jika dua objek dianggap sama (`a == b` di Python, `a.equals(b)` di Java), aturan yang **wajib** dipenuhi adalah ...

- A. kode *hash* keduanya harus sama
- B. kode *hash* keduanya harus berbeda
- C. keduanya harus objek yang sama persis
- D. keduanya harus dibuat dengan konstruktor yang sama

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: set dan map memakai kode *hash* untuk menentukan "rak" penyimpanan, lalu membandingkan isi rak dengan `__eq__`/`equals()`. Jika dua objek yang sama punya *hash* berbeda, keduanya masuk rak berbeda dan data kembar lolos. Sebaliknya, dua objek berbeda **boleh** punya *hash* sama (B salah). Objek yang dianggap sama tidak harus objek yang sama persis (C); justru itulah gunanya aturan kesamaan. Cara objek dibuat (D) tidak ada hubungannya dengan aturan kesamaan, yang hanya melihat datanya, misalnya NIK.

</details>

### Soal 7

Seorang pemrogram meng-*override* `equals()` pada kelas `Buku` (sama jika ISBN-nya sama), tetapi **lupa** `hashCode()`. Dua objek `Buku` ber-ISBN sama lalu dimasukkan ke `HashSet`. Apa yang paling mungkin terjadi di Java?

- A. Program gagal dikompilasi
- B. Program berjalan, tetapi `HashSet` berisi dua buku yang seharusnya dianggap sama
- C. `HashSet` berisi satu buku karena `equals()` saja sudah cukup
- D. Muncul `NullPointerException`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: Java tidak memeriksa kontrak `equals`/`hashCode` saat kompilasi (A salah). `hashCode()` bawaan berbeda untuk setiap objek sehingga kedua buku masuk rak berbeda dan `equals()` tidak pernah dipanggil. Hasilnya *bug* diam-diam (C salah). Tidak ada `null` yang dipakai di sini sehingga `NullPointerException` (D) juga tidak muncul. Di Python, kesalahan serupa (menulis `__eq__` tanpa `__hash__`) justru langsung ketahuan karena objeknya menjadi *unhashable* dan memunculkan `TypeError`.

</details>

### Soal 8

Pernyataan yang **benar** tentang *generics* adalah ...

- A. `List<int>` boleh dipakai di Java asalkan isinya angka kecil
- B. Python menolak menjalankan program jika isi `list[int]` ternyata teks
- C. Java memeriksa tipe *generics* saat kompilasi, sedangkan petunjuk tipe Python tidak diperiksa saat program berjalan
- D. Di Java, dua `Integer` yang angkanya sama selalu menghasilkan benar jika dibandingkan dengan `==`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: *compiler* Java menolak isi yang salah tipe sebelum program berjalan, sedangkan Python hanya menjadikan `list[int]` petunjuk untuk manusia dan alat bantu seperti VS Code atau mypy (B salah). Isi `< >` di Java harus kelas, jadi yang benar `List<Integer>` (A salah). Pilihan D adalah jebakan terkenal: `==` membandingkan objek sehingga `Integer` bernilai 128 bisa menghasilkan salah. Bandingkan dengan `equals()`.

</details>

### Soal 9

Perhatikan kode berikut.

**Python:**

```python
a = {"Ayu", "Bima", "Citra"}
b = {"Bima", "Dimas"}
print(len(a | b), len(a & b), len(a - b))
```

**Java:**

```java
Set<String> a = new HashSet<>(List.of("Ayu", "Bima", "Citra"));
Set<String> b = new HashSet<>(List.of("Bima", "Dimas"));
Set<String> gabung = new HashSet<>(a);
gabung.addAll(b);
Set<String> iris = new HashSet<>(a);
iris.retainAll(b);
Set<String> selisih = new HashSet<>(a);
selisih.removeAll(b);
System.out.println(gabung.size() + " " + iris.size() + " " + selisih.size());
```

Apa yang tercetak?

- A. `4 1 2`
- B. `5 1 2`
- C. `4 2 1`
- D. `4 1 3`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: gabungan berisi Ayu, Bima, Citra, Dimas (4 nama karena Bima tidak dihitung dua kali). Irisan hanya Bima (1). Selisih `a - b` berisi Ayu dan Citra (2). Pilihan B lupa bahwa set membuang data kembar. Pilihan C menukar hasil irisan dan selisih. Pilihan D lupa bahwa Bima ikut dibuang dari `a`.

</details>

### Soal 10

Kelas `Mahasiswa` sudah punya urutan alami berdasarkan NIM. Dosen meminta daftar mahasiswa diurutkan dari IPK tertinggi, **tanpa** mengubah urutan alami itu. Cara yang paling tepat adalah ...

- A. Mengubah `__lt__`/`compareTo` agar membandingkan IPK
- B. Memberikan `key=` (Python) atau `Comparator` (Java) berisi aturan IPK saat mengurutkan
- C. Membuat kelas baru `MahasiswaIPK` yang menyalin semua atribut
- D. Mengurutkan dengan urutan alami, lalu membalik hasilnya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: urutan khusus diberikan dari luar kelas, dan jumlahnya boleh sebanyak yang dibutuhkan, misalnya `sorted(daftar, key=lambda m: m.ipk, reverse=True)` atau `Comparator.comparing(Mahasiswa::getIpk).reversed()`. Pilihan A merusak urutan alami yang dipakai bagian program lain. Pilihan C berlebihan. Pilihan D hanya membalik urutan NIM, bukan mengurutkan IPK.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Koleksi dan *generics* sudah kamu kuasai | Lanjut ke [Pertemuan 13](../Pertemuan-13-Prinsip-SOLID/README.md) |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep untuk soal yang salah (terutama urutan isi dan aturan kesamaan), lalu kerjakan Latihan 3 dan 4 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan semua contoh di halaman praktik, dan coba setiap "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 13 ➡️](../Pertemuan-13-Prinsip-SOLID/README.md)
