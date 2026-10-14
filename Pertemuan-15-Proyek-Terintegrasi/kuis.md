# Kuis Pertemuan 15: Proyek Terintegrasi

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Proyek Akhir ➡️](proyek-akhir.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Urutan langkah membangun aplikasi yang dianjurkan di pertemuan ini adalah ...

- A. Implementasi → Pengujian → Kebutuhan → Rancangan
- B. Kebutuhan → Rancangan (diagram kelas UML) → Implementasi → Pengujian, lalu berulang jika ada yang kurang
- C. Rancangan → Implementasi → Kebutuhan, tanpa pengujian karena kode sudah dirancang
- D. Implementasi sekaligus semua kelas, lalu menggambar diagram kelas dari kode yang sudah jadi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: kita menulis dulu **apa** yang harus bisa dilakukan aplikasi (kebutuhan), lalu merancang kelas-kelasnya dengan diagram UML, baru menulis kode sedikit demi sedikit dan mengujinya. Temuan dari pengujian sering memunculkan kebutuhan baru, jadi alurnya berputar. Pilihan A menulis kode sebelum tahu apa yang dibutuhkan. Pilihan C keliru karena pengujian tetap wajib. Pilihan D (menggambar diagram dari kode jadi) boleh dilakukan untuk dokumentasi, tetapi bukan cara merancang.

</details>

### Soal 2

Di KedaiKita, kode yang mencetak `Pilihan: ` lalu membaca ketikan kasir seharusnya berada di lapisan ...

- A. Model karena `Menu` dan `Pesanan` paling tahu datanya
- B. Penyimpanan karena ketikan kasir akhirnya disimpan ke *file*
- C. Layanan karena `LayananKasir` mengatur alur kerja
- D. Tampilan, yaitu `AplikasiKasir`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: urusan tanya-jawab dengan pengguna (mencetak pertanyaan, membaca keyboard, memeriksa bentuk jawaban) adalah tugas lapisan tampilan. `LayananKasir` (C) memang mengatur alur kerja, tetapi ia menerima data yang sudah jadi dan tidak pernah membaca keyboard sehingga bisa dipakai oleh tampilan lain dan mudah diuji. Model (A) dan penyimpanan (B) sama sekali tidak boleh tahu ada keyboard.

</details>

### Soal 3

Manfaat **utama** arsitektur berlapis adalah ...

- A. Satu lapisan, misalnya tampilan teks, bisa diganti (misalnya menjadi aplikasi web) tanpa membongkar lapisan layanan dan model
- B. Program berjalan jauh lebih cepat karena dibagi menjadi beberapa lapisan
- C. Jumlah baris kode menjadi lebih sedikit
- D. Kita tidak perlu lagi menulis validasi di kelas model

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: karena setiap lapisan punya tugas sendiri dan arah ketergantungannya jelas (atas memakai bawah), bagian yang berubah tidak merembet ke mana-mana. Arsitektur berlapis tidak membuat program lebih cepat (B), dan biasanya justru menambah sedikit kode (C). Validasi aturan bisnis tetap dijaga model (D salah).

</details>

### Soal 4

Pernyataan yang **benar** tentang *package* di kedua bahasa adalah ...

- A. Di Python, modul di dalam *package* cukup di-*import* dengan `import menu`, tanpa nama *package*
- B. Di Java, kelas `Main` di *package* `kedaikita` dijalankan dengan `java -cp out Main`
- C. Python menandai *package* dengan folder berisi `__init__.py`, sedangkan Java memakai baris `package kedaikita;` di setiap *file*, dan nama lengkap kelasnya memuat nama *package*
- D. *Package* hanya berguna untuk aplikasi yang sangat besar sehingga KedaiKita tidak memakainya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: KedaiKita memakai `from kedaikita.menu import Menu` (impor absolut, A salah) dan `java -cp out kedaikita.Main` (B salah; tanpa nama *package* muncul `ClassNotFoundException: Main`). Pilihan D keliru karena KedaiKita justru memakai *package* untuk merapikan lebih dari 20 *file*.

</details>

### Soal 5

KedaiKita memisahkan kolom CSV dengan titik koma (`;`), bukan koma. Alasan yang **paling tepat** adalah ...

- A. Titik koma membuat ukuran *file* lebih kecil
- B. Isi kolom seperti alamat atau catatan sering mengandung koma, dan Excel berpengaturan Indonesia umumnya memakai titik koma sebagai pemisah
- C. Python dan Java tidak bisa membaca *file* yang mengandung koma
- D. Titik koma wajib dipakai oleh semua *file* berakhiran `.csv`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: jika pemisahnya koma, nilai seperti `Samarinda, Kalimantan Timur` akan terbelah menjadi dua kolom. Di pengaturan wilayah Indonesia, koma dipakai sebagai pemisah desimal sehingga Excel umumnya memakai titik koma untuk CSV. Ukuran *file* (A) praktis sama. Pilihan C salah: kedua bahasa bisa membaca koma. Pilihan D salah: CSV standar justru memakai koma; titik koma adalah pilihan kita.

</details>

### Soal 6

Perhatikan kode berikut.

**Python:**

```python
class Sumber:
    def __enter__(self):
        print("buka")
        return self

    def __exit__(self, jenis, error, jejak):
        print("tutup")
        return False


try:
    with Sumber():
        print("kerja")
        raise ValueError("rusak")
except ValueError:
    print("tangkap")
```

**Java:**

```java
// class Sumber implements AutoCloseable:
//   konstruktornya mencetak "buka", close() mencetak "tutup"
try (Sumber s = new Sumber()) {
    System.out.println("kerja");
    throw new IllegalArgumentException("rusak");
} catch (IllegalArgumentException e) {
    System.out.println("tangkap");
}
```

Urutan teks yang tercetak adalah ...

- A. `buka`, `kerja`, `tangkap`, `tutup`
- B. `buka`, `kerja`, `tangkap` (tanpa `tutup` karena terjadi *error*)
- C. `kerja`, `buka`, `tutup`, `tangkap`
- D. `buka`, `kerja`, `tutup`, `tangkap`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: sumber daya dibuka saat masuk blok, lalu `kerja` tercetak. Ketika *exception* dilempar, sumber daya **ditutup lebih dulu** (`__exit__`/`close`), baru blok `except`/`catch` berjalan. Pilihan A menebak urutan yang terbalik. Pilihan C keliru karena `buka` selalu tercetak lebih dulu: sumber daya dibuka sebelum isi blok dijalankan. Pilihan B adalah miskonsepsi berbahaya: penutupan justru dijamin terjadi walaupun ada *error*.

</details>

### Soal 7

Perhatikan kode berikut.

**Python:**

```python
def tanya_jumlah(daftar_jawaban):
    for teks in daftar_jawaban:
        print(f"Jumlah (1-5): {teks}")
        if teks == "":
            print("  kosong")
            continue
        angka = int(teks)
        if angka < 1 or angka > 5:
            print("  di luar batas")
            continue
        return angka
    raise EOFError("input habis")


print("Hasil:", tanya_jumlah(["", "7", "3"]))
```

**Java:**

```java
static int tanyaJumlah(List<String> daftarJawaban) {
    for (String teks : daftarJawaban) {
        System.out.println("Jumlah (1-5): " + teks);
        if (teks.isEmpty()) {
            System.out.println("  kosong");
            continue;
        }
        int angka = Integer.parseInt(teks);
        if (angka < 1 || angka > 5) {
            System.out.println("  di luar batas");
            continue;
        }
        return angka;
    }
    throw new NoSuchElementException("input habis");
}

// di dalam main:
System.out.println("Hasil: " + tanyaJumlah(List.of("", "7", "3")));
```

Apa yang terjadi?

- A. Tercetak `kosong` sekali dan `di luar batas` sekali, lalu `Hasil: 3`
- B. Tercetak `kosong` sekali, lalu `Hasil: 7`
- C. Program berhenti dengan *error* karena teks kosong diubah menjadi angka
- D. Tercetak `di luar batas` dua kali, lalu `EOFError`/`NoSuchElementException`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: jawaban kosong ditangkap lebih dulu oleh pemeriksaan `teks == ""` sehingga tidak pernah sampai ke `int()`/`parseInt()` (C salah). Angka 7 berbentuk benar, tetapi di luar batas, jadi ditolak (B salah). Angka 3 valid dan dikembalikan sebelum jawaban habis sehingga *exception* akhir *input* tidak pernah dilempar (D salah). Inilah pola "validasi lalu tanya ulang".

</details>

### Soal 8

Di `unittest` Python, *method* `setUp()` berguna untuk ...

- A. Menjalankan semua *test* sekaligus dari terminal
- B. Menandai *method* mana yang merupakan *test*
- C. Menyiapkan objek baru sebelum **setiap** *test* sehingga *test* tidak saling memengaruhi
- D. Menyimpan hasil *test* ke *file*

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `setUp()` dijalankan ulang sebelum setiap *test*. Di KedaiKita, setiap *test* `TestPesanan` mendapat pesanan dan stok yang baru sehingga *test* "stok berkurang" tidak mengganggu *test* lain. *Test* dijalankan dengan `python -m unittest discover -s tests -v` (A), dan *method test* ditandai dengan awalan nama `test_` (B). `setUp()` juga tidak menyimpan apa pun ke *file* (D); hasil *test* hanya dicetak ke terminal. Padanannya di JUnit adalah `@BeforeEach`.

</details>

### Soal 9

Kapan `PencatatTransaksiCSV` menambahkan satu baris ke `transaksi.csv`?

- A. Setiap kali kasir menambahkan item ke pesanan
- B. Satu kali saat aplikasi ditutup, untuk semua pesanan sekaligus
- C. Setiap kali status pesanan berubah, apa pun statusnya
- D. Saat `Pesanan` memberi tahu pengamatnya bahwa statusnya berubah, dan status itu adalah LUNAS

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `PencatatTransaksiCSV` adalah pengamat (pola *Observer*). `Pesanan` memanggil `perbarui()` milik semua pengamat setiap kali statusnya berubah, dan pencatat hanya menulis jika statusnya LUNAS (C hampir benar, tetapi status lain diabaikan). Menambah item tidak mengubah status (A salah), dan pencatatan terjadi saat itu juga, bukan dikumpulkan sampai aplikasi ditutup (B salah). Dengan begitu, kelas `Pesanan` tidak perlu diubah sama sekali untuk fitur pencatatan ini.

</details>

### Soal 10

Aturan toko daring: "gratis ongkir jika belanja **minimal** Rp100.000". Seorang pemrogram keliru menulis `subtotal > 100000` alih-alih `subtotal >= 100000`. *Test* dengan belanja berapa yang **paling mungkin** menangkap kekeliruan ini?

- A. Rp50.000
- B. Rp99.000
- C. Tepat Rp100.000
- D. Rp150.000

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: untuk Rp50.000, Rp99.000, dan Rp150.000, kode yang benar dan kode yang keliru memberi hasil yang **sama** sehingga *test*-nya tetap lulus. Hanya di **batas** (tepat Rp100.000) keduanya berbeda: kode yang keliru masih menagih ongkir. Inilah alasan kasus batas wajib diuji (contoh 05 di halaman praktik).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8—10 | Mantap! Kamu siap membangun aplikasi sendiri | Baca [Spesifikasi Proyek Akhir](proyek-akhir.md) dan mulai tahap pertamanya |
| 5—7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 4 |
| 0—4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan semua contoh di halaman praktik, dan coba mode demo serta mode interaktif KedaiKita |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Proyek Akhir ➡️](proyek-akhir.md)
