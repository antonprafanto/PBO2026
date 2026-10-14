# Kuis Pertemuan 05: Relasi Antarkelas

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 06 ➡️](../Pertemuan-06-UML-Class-Diagram/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Ayu memesan ojek daring untuk berangkat ke kampus. Setelah sampai, Ayu tidak lagi berurusan dengan pengemudinya. Di dalam program, objek `Ojek` hanya dikirim sebagai parameter ke *method* `pesan_ojek()`/`pesanOjek()` milik `Penumpang`, dan tidak disimpan sebagai atribut. Jenis relasi antara `Penumpang` dan `Ojek` adalah ...

- A. Komposisi
- B. Dependensi
- C. Agregasi
- D. Asosiasi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: objek `Ojek` hanya dipakai **sebentar**, selama *method* berjalan, lalu dilepas. Itulah dependensi. Asosiasi (D) mensyaratkan objek lain **disimpan** sebagai atribut. Komposisi (A) dan agregasi (C) adalah hubungan keseluruhan dan bagian, padahal penumpang tidak "terdiri atas" ojek.

</details>

### Soal 2

Manakah pasangan yang paling tepat digolongkan sebagai **komposisi**?

- A. Tim futsal dan para pemainnya
- B. *Playlist* dan lagu-lagu di dalamnya
- C. Mahasiswa dan dosen walinya
- D. Pesanan dan baris-baris item di dalamnya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: baris item seperti "2 x Kopi Susu Gula Aren" dibuat oleh pesanannya, hanya milik satu pesanan, dan tidak bermakna tanpa pesanan itu. Siklus hidupnya ikut pesanan, jadi komposisi. Pemain (A) dan lagu (B) bisa hidup sendiri dan boleh menjadi bagian dari beberapa tim atau *playlist* sehingga termasuk agregasi. Mahasiswa dan dosen wali (C) saling mengenal tanpa hubungan keseluruhan dan bagian sehingga termasuk asosiasi.

</details>

### Soal 3

Sebuah diagram menuliskan multiplisitas `0..1` di ujung `DosenWali` pada hubungan `Mahasiswa --> DosenWali`. Artinya ...

- A. Seorang mahasiswa boleh belum punya dosen wali, dan paling banyak punya satu
- B. Setiap mahasiswa wajib punya tepat satu dosen wali
- C. Seorang mahasiswa boleh punya banyak dosen wali
- D. Seorang dosen wali boleh tidak membimbing mahasiswa sama sekali

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `0..1` berarti nol atau satu. Angka itu dibaca dari sudut pandang **satu** mahasiswa karena ditulis di ujung `DosenWali`. Di kode, wujudnya adalah atribut yang awalnya `None`/`null`. Pilihan B adalah arti multiplisitas `1`, dan C adalah arti `*`. Pilihan D membicarakan sudut pandang dosen. Sudut pandang itu ditentukan oleh angka di ujung seberang (ujung `Mahasiswa`).

</details>

### Soal 4

Petunjuk paling kuat di dalam kode bahwa hubungan `Rumah` dan `Ruangan` adalah **komposisi** adalah ...

- A. `Rumah` punya *method* yang menerima objek `Ruangan` yang sudah jadi dari luar
- B. `Ruangan` menyimpan referensi ke objek `Rumah`
- C. Objek `Ruangan` dibuat di dalam *method* milik `Rumah` dari data yang dikirim, dan tidak dipegang pihak lain
- D. Kelas `Rumah` dan kelas `Ruangan` ditulis di *file* yang berbeda

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: pada komposisi, pemilik membuat sendiri objek bagiannya, misalnya `bangun_ruangan("Dapur", 3, 2)`. Kode luar hanya mengirim data sehingga tidak ada pihak lain yang memegang ruangan itu. Pilihan A justru ciri agregasi karena bagian dibuat di luar. Pilihan B hanya menunjukkan arah asosiasi. Pilihan D tidak ada hubungannya dengan jenis relasi.

</details>

### Soal 5

Kelas `Pemain` dan `Tim` sama seperti di contoh 03. Representasi teks pemain berbentuk `Andi (kiper)`. Apa yang dicetak oleh baris **terakhir**?

**Python:**

```python
andi = Pemain("Andi", "kiper")
tim = Tim("Tim Kelas TI-A")
tim.rekrut(andi)
tim = None
print(andi)
```

**Java:**

```java
Pemain andi = new Pemain("Andi", "kiper");
Tim tim = new Tim("Tim Kelas TI-A");
tim.rekrut(andi);
tim = null;
System.out.println(andi);
```

- A. `Andi (kiper)` karena objek pemain masih dipegang variabel `andi`
- B. *Error* karena pemain ikut terhapus bersama timnya
- C. `None` di Python atau `null` di Java
- D. `Tim Kelas TI-A`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: ini agregasi. Pemain dibuat di luar tim dan tetap dipegang variabel `andi`. Melepas objek tim tidak menghapus pemainnya, jadi B salah. Yang diisi `None`/`null` adalah variabel `tim`, bukan `andi` sehingga C salah. Yang dicetak adalah objek pemain, bukan nama timnya, sehingga D juga salah. Baris `Andi bergabung dengan Tim Kelas TI-A` memang ikut tercetak oleh `rekrut()`, tetapi itu bukan baris terakhir.

</details>

### Soal 6

Perhatikan kode berikut.

**Python:**

```python
class Kotak:
    def __init__(self):
        self._isi = ["pensil", "penghapus"]

    @property
    def isi(self) -> list[str]:
        return list(self._isi)


kotak = Kotak()
kotak.isi.append("penggaris")
print(len(kotak.isi))
```

**Java:**

```java
class Kotak {
    private List<String> isi = new ArrayList<>();

    Kotak() {
        isi.add("pensil");
        isi.add("penghapus");
    }

    public List<String> getIsi() {
        return new ArrayList<>(isi);
    }
}

// di dalam main:
Kotak kotak = new Kotak();
kotak.getIsi().add("penggaris");
System.out.println(kotak.getIsi().size());
```

Angka berapa yang tercetak?

- A. 3
- B. 1
- C. 2
- D. Program *error* karena *list* tidak boleh diubah

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: *getter* mengembalikan **salinan** *list*. `"penggaris"` ditambahkan ke salinan yang langsung dibuang, sedangkan *list* asli di dalam objek tetap berisi dua barang. Pemanggilan kedua membuat salinan baru dari *list* asli itu sehingga ukurannya 2. Jawaban A adalah hasil yang terjadi jika *getter* mengembalikan *list* aslinya. Jawaban B tidak mungkin karena tidak ada isi yang dihapus. Tidak ada *error* (D) karena salinannya sendiri boleh diubah.

</details>

### Soal 7

*Method* pencarian `cari_menu("M99")`/`cariMenu("M99")` mengembalikan `None`/`null` karena kode itu tidak ada. Apa yang sebaiknya dilakukan kode pemanggil?

- A. Langsung memanggil *method* milik hasilnya karena hasil pencarian pasti berisi objek
- B. Mengubah *method* pencarian agar menghentikan program setiap kali menu tidak ditemukan
- C. Membuat objek `Menu` baru dengan kode `M99` setiap kali pencarian gagal
- D. Memeriksa dulu apakah hasilnya `None`/`null` sebelum memakainya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `None`/`null` adalah jawaban yang wajar untuk "tidak ditemukan". Tugas pemanggil adalah memeriksanya, misalnya dengan `if menu is None:` atau `if (menu == null)`, lalu menampilkan pesan. Pilihan A justru menyebabkan `AttributeError` atau `NullPointerException`. Pilihan B membuat program kasir berhenti hanya karena salah ketik kode. Pilihan C mengarang menu yang sebenarnya tidak dijual.

</details>

### Soal 8

Program studi kasus terdiri atas beberapa *file* di folder `studi-kasus`. Terminalmu masih berada di folder induknya. Perintah `python main.py` menghasilkan `can't open file`, dan perintah `java Main` menghasilkan `Could not find or load main class Main`. Penyebab paling mungkin adalah ...

- A. Isi *file* `main.py` atau `Main.java` salah ketik
- B. Folder aktif terminal bukan folder tempat *file-file* program berada
- C. Python atau Java belum terpasang di komputer
- D. Nama kelas dan nama *file* seharusnya ditulis huruf kecil semua

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: kedua perintah mencari *file* di **folder aktif**. Perbaikannya, masuk dulu ke folder yang benar dengan `cd studi-kasus`, lalu jalankan lagi (untuk Java, kompilasi dulu dengan `javac *.java`). Jika isi *file* salah ketik (A), pesannya berupa *error* sintaks atau `cannot find symbol`, bukan "tidak menemukan *file*". Jika Python atau Java belum terpasang (C), perintah `python` atau `java` sendiri tidak dikenali. Pilihan D salah karena nama kelas Java justru memakai *PascalCase*.

</details>

### Soal 9

Kelas `Mahasiswa` dan `DosenWali` sama seperti di contoh 02. Apa yang dicetak oleh baris terakhir?

**Python:**

```python
bu_rina = DosenWali("Bu Rina", "C-201")
ayu = Mahasiswa("Ayu")
bima = Mahasiswa("Bima")
ayu.atur_dosen_wali(bu_rina)
bima.atur_dosen_wali(bu_rina)
bu_rina.pindah_ruangan("D-105")
print(bima.info_perwalian())
```

**Java:**

```java
DosenWali buRina = new DosenWali("Bu Rina", "C-201");
Mahasiswa ayu = new Mahasiswa("Ayu");
Mahasiswa bima = new Mahasiswa("Bima");
ayu.aturDosenWali(buRina);
bima.aturDosenWali(buRina);
buRina.pindahRuangan("D-105");
System.out.println(bima.infoPerwalian());
```

- A. `Bima: belum punya dosen wali`
- B. `Bima: dosen wali Bu Rina, ruang C-201`
- C. `Bima: dosen wali Bu Rina, ruang D-105`
- D. *Error* karena satu objek dosen tidak boleh dikenal dua mahasiswa

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: Ayu dan Bima menyimpan **referensi** ke objek dosen yang sama, bukan salinannya. Saat objek itu pindah ruangan, semua yang mengenalnya melihat ruangan baru. Pilihan A salah karena Bima sudah diberi dosen wali lewat `atur_dosen_wali()`/`aturDosenWali()`. Pilihan B adalah miskonsepsi bahwa asosiasi menyalin data. Satu objek boleh dikenal oleh banyak objek lain, jadi D salah.

</details>

### Soal 10

Di KedaiKita, `ItemPesanan` menyimpan referensi ke `Menu`, tetapi `Menu` tidak menyimpan daftar item yang memesannya. Pernyataan yang paling tepat adalah ...

- A. Desain ini salah karena asosiasi harus selalu dua arah
- B. Ini asosiasi satu arah, dan sudah cukup karena program hanya perlu bertanya dari item ke menunya
- C. Ini komposisi karena menu ikut hilang jika item dihapus
- D. Ini dependensi karena menu hanya dipakai sebentar oleh item

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: item perlu tahu nama dan harga menunya, sedangkan menu tidak perlu tahu sedang dipesan di item mana. Hubungan satu arah lebih sederhana dan lebih mudah dijaga, jadi A salah. Menu tidak ikut hilang saat item dihapus sehingga bukan komposisi (C). Menu juga disimpan sebagai atribut item selama item itu ada, jadi bukan sekadar dipakai sebentar (D).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Kamu sudah bisa memilih dan menulis relasi antarkelas | Lanjut ke [Pertemuan 06](../Pertemuan-06-UML-Class-Diagram/README.md) untuk menggambar relasi dengan diagram kelas UML |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 4 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, terutama bagian 3 sampai 9, dan jalankan semua contoh di halaman praktik |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 06 ➡️](../Pertemuan-06-UML-Class-Diagram/README.md)
