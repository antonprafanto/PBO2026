# Kuis Pertemuan 01: Pengenalan PBO dan Persiapan Alat

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 02 ➡️](../Pertemuan-02-Kelas-dan-Objek/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Apa yang dimaksud dengan **paradigma pemrograman**?

- A. Bahasa pemrograman yang paling populer pada suatu masa
- B. Aplikasi editor yang dipakai untuk menulis kode
- C. Cara pandang atau gaya dalam menyusun program
- D. Aturan tanda baca, seperti titik koma dan kurung kurawal, dalam sebuah bahasa

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: paradigma adalah cara pandang dalam menyusun program: bagaimana masalah dipecah, di mana data disimpan, dan bagaimana bagian-bagian program bekerja sama. Contohnya paradigma prosedural, berorientasi objek, dan fungsional. Paradigma bukan nama bahasa (A), bukan aplikasi (B), dan bukan aturan tanda baca (D). Aturan tanda baca disebut sintaks, dan satu bahasa seperti Python bisa dipakai dengan beberapa paradigma.

</details>

### Soal 2

Manakah yang merupakan **ciri khas** program bergaya prosedural?

- A. Data disimpan terpisah dari fungsi-fungsi yang mengolahnya
- B. Setiap data selalu terbungkus bersama perilakunya di dalam objek
- C. Program sama sekali tidak boleh memakai perulangan
- D. Program hanya bisa ditulis dengan bahasa Java

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: pada gaya prosedural, data (variabel, *list*, *array*) disimpan di satu tempat, sedangkan fungsi-fungsi yang mengolahnya berada di tempat lain. Pilihan B adalah ciri **PBO**, bukan prosedural. Pilihan C keliru karena program prosedural justru banyak memakai perulangan. Pilihan D keliru karena gaya prosedural bisa ditulis di Python, Java, C, dan banyak bahasa lain.

</details>

### Soal 3

Pada KedaiKita versi prosedural, mengapa harga menu **tertukar** setelah daftar menu diurutkan?

- A. Python dan Java keliru saat menghitung harga setelah daftar diurutkan
- B. Harga disimpan sebagai bilangan pecahan sehingga nilainya menjadi tidak tepat
- C. Program menampilkan pesan *error*, lalu berhenti sebelum sempat menampilkan menu
- D. Hanya daftar nama yang diurutkan, sedangkan daftar harga dan stok tetap di tempatnya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: data satu menu tersebar di tiga daftar yang hanya direkatkan oleh indeks yang sama. Perintah pengurutan hanya memindahkan isi daftar nama sehingga nama di indeks 0 kini berpasangan dengan harga milik menu lain. Bahasa pemrogramannya tidak salah hitung (A), harganya bilangan bulat (B), dan justru tidak ada pesan *error* sama sekali (C). Itulah yang membuat kesalahan ini berbahaya.

</details>

### Soal 4

Dalam PBO, sebuah **objek** menyatukan dua hal, yaitu ...

- A. kelas dan fungsi global
- B. data (atribut) dan perilaku (*method*)
- C. variabel global dan indeks *list*
- D. *compiler* dan *interpreter*

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: objek membawa **atribut** (data atau ciri, misalnya nama dan harga sebuah menu) dan ***method*** (perilaku, misalnya mengurangi stok). Kelas adalah rancangan objek, bukan isi objek (A). Variabel global dan indeks justru ciri gaya prosedural (C). *Compiler* dan *interpreter* adalah alat untuk menerjemahkan dan menjalankan program, bukan isi sebuah objek (D).

</details>

### Soal 5

Perhatikan deskripsi berikut: *"Seorang mahasiswa punya nama, NIM, dan IPK. Mahasiswa bisa mengisi KRS dan membayar UKT."* Manakah yang paling tepat dijadikan ***method***?

- A. NIM
- B. IPK
- C. mengisi KRS
- D. mahasiswa

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: *method* adalah perilaku atau aksi, biasanya berupa kata kerja, seperti "mengisi KRS" dan "membayar UKT". NIM (A) dan IPK (B) adalah atribut karena merupakan data milik mahasiswa. "Mahasiswa" (D) adalah calon nama kelas.

</details>

### Soal 6

Di aplikasi ojek *online*, penumpang meminta aplikasi mencarikan pengemudi tanpa perlu tahu bagaimana aplikasi mencarinya. Dalam istilah PBO, tindakan penumpang ini paling tepat disebut ...

- A. mengirim pesan ke objek lain, yaitu memanggil *method*-nya
- B. mengubah data global milik aplikasi secara langsung tanpa perantara
- C. mewarisi semua atribut dan *method* milik objek aplikasi
- D. mengurutkan daftar pengemudi berdasarkan nomor indeks

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: dalam PBO, objek bekerja sama dengan **saling mengirim pesan**. Penumpang cukup meminta "carikan pengemudi", lalu objek aplikasi mengerjakannya dengan caranya sendiri. Penumpang tidak menyentuh data aplikasi secara langsung (B). Mewarisi (C) adalah konsep pewarisan antarkelas, bukan interaksi antarobjek. Pilihan D tidak berhubungan dengan skenario ini.

</details>

### Soal 7

Di mesin kasir, tombol "Bayar" bisa memproses pembayaran tunai, QRIS, atau kartu, dan masing-masing bekerja dengan caranya sendiri. Pilar PBO yang **paling** menggambarkan situasi ini adalah ...

- A. Enkapsulasi
- B. Pewarisan
- C. Abstraksi
- D. Polimorfisme

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: polimorfisme berarti "banyak bentuk": perintah yang sama ("bayar") ditanggapi dengan cara berbeda oleh objek yang berbeda (tunai, QRIS, kartu). Enkapsulasi (A) tentang membungkus dan melindungi data. Pewarisan (B) tentang kelas baru yang mewarisi ciri kelas lama. Abstraksi (C) memang ikut berperan karena kasir tidak perlu tahu detail cara kerja QRIS. Namun, inti situasi ini adalah **satu perintah dengan banyak cara**, dan itulah polimorfisme. Pilar ini dibahas tuntas di Pertemuan 09.

</details>

### Soal 8

Dalam situasi manakah PBO paling mungkin terasa **berlebihan**?

- A. Sistem informasi akademik yang dikembangkan banyak pemrogram selama bertahun-tahun
- B. Skrip sekali pakai untuk mengganti nama 200 *file* foto
- C. Aplikasi ojek *online* dengan penumpang, pengemudi, pesanan, dan pembayaran
- D. *Game* dengan banyak karakter yang masing-masing punya nyawa dan posisi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: skrip kecil sekali pakai berupa satu aliran langkah sederhana. Membuat kelas di sini hanya menambah baris tanpa manfaat berarti sehingga gaya prosedural lebih cocok. Pilihan A, C, dan D adalah program besar atau berisi banyak "benda" dengan data dan perilakunya sendiri, yaitu situasi tempat PBO paling bermanfaat.

</details>

### Soal 9

Perhatikan kode berikut.

**Python:**

```python
nama = ["Citra", "Ayu", "Bima"]
nilai = [70, 90, 80]
nama.sort()
print(nama[0], nilai[0])
```

**Java:**

```java
String[] nama = {"Citra", "Ayu", "Bima"};
int[] nilai = {70, 90, 80};
Arrays.sort(nama);
System.out.println(nama[0] + " " + nilai[0]);
```

Apa yang tercetak?

- A. `Ayu 90`
- B. `Ayu 70`
- C. `Citra 70`
- D. `Bima 80`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: setelah diurutkan, isi `nama` menjadi `Ayu, Bima, Citra`, tetapi `nilai` **tidak berubah**: `70, 90, 80`. Jadi `nama[0]` adalah `Ayu` dan `nilai[0]` adalah `70`, padahal 70 adalah nilai milik Citra. Pilihan A adalah jawaban "yang seharusnya" jika datanya tidak tertukar, dan justru itulah jebakannya. Pilihan C adalah isi sebelum diurutkan. Pilihan D tidak mungkin karena setelah diurutkan `nama[0]` adalah `Ayu`, bukan `Bima`. Ini masalah data paralel yang sama dengan KedaiKita.

</details>

### Soal 10

Perhatikan kode berikut.

**Python:**

```python
def hitung(harga, jumlah):
    return harga * jumlah


total = 0
for jumlah in range(1, 4):
    total = total + hitung(5000, jumlah)
print(total // 1000)
```

**Java:**

```java
static int hitung(int harga, int jumlah) {
    return harga * jumlah;
}

// di dalam main:
int total = 0;
for (int jumlah = 1; jumlah <= 3; jumlah++) {
    total = total + hitung(5000, jumlah);
}
System.out.println(total / 1000);
```

Apa yang tercetak?

- A. `15`
- B. `50`
- C. `30`
- D. `30000`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: perulangan berjalan untuk `jumlah` = 1, 2, 3 (`range(1, 4)` tidak menyertakan 4, sama seperti syarat `jumlah <= 3` di Java). Totalnya 5000 x 1 + 5000 x 2 + 5000 x 3 = 30000, lalu dibagi bulat dengan 1000 menjadi `30`. Pilihan B muncul jika kamu mengira angka 4 ikut dihitung. Pilihan D muncul jika kamu lupa pembagian di baris terakhir. Pilihan A muncul jika hanya putaran terakhir yang dihitung.

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Fondasimu sudah kuat | Lanjut ke [Pertemuan 02](../Pertemuan-02-Kelas-dan-Objek/README.md) |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 7 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, lalu jalankan studi kasus KedaiKita di halaman praktik sambil mencoba setiap "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 02 ➡️](../Pertemuan-02-Kelas-dan-Objek/README.md)
