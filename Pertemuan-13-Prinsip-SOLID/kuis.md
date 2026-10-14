# Kuis — Pertemuan 13: Prinsip SOLID

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 14 ➡️](../Pertemuan-14-Design-Pattern/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Kelas `LaporanSerbaBisa` menghitung rata-rata nilai **dan** mencetak laporan. Permintaan "batas predikat A naik menjadi 85" dan permintaan "laporan dibuat bergaris" sama-sama memaksa kelas itu diubah. Prinsip apa yang dilanggar?

- A. OCP, karena laporan tidak bisa ditambah kolom baru
- B. SRP, karena kelas itu punya dua alasan untuk berubah yang datang dari urusan berbeda
- C. LSP, karena laporan tidak bisa menggantikan kelas induknya
- D. DIP, karena laporan mencetak langsung ke layar

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: aturan penilaian dan format cetak adalah dua urusan berbeda dengan sumber perubahan berbeda. SRP meminta keduanya dipisah, misalnya menjadi `PenghitungNilai` dan `PencetakLaporan`. Pilihan A, C, dan D menyebut prinsip lain yang tidak berhubungan dengan masalah "satu kelas, banyak urusan".

</details>

### Soal 2

Sebuah ekspedisi menambah jenis layanan pengiriman baru setiap beberapa bulan. Rancangan mana yang paling sesuai dengan OCP?

- A. Satu method `hitung_ongkir(jenis)` / `hitungOngkir(jenis)` berisi rantai percabangan untuk setiap jenis
- B. Menyalin method hitung ongkir lama setiap ada layanan baru, lalu mengganti angkanya
- C. Kontrak `LayananKirim` dengan satu kelas untuk setiap layanan, sehingga layanan baru cukup menjadi kelas baru
- D. Menyimpan semua rumus ongkir di satu variabel global agar mudah dicari

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: OCP berarti terbuka untuk ditambah, tertutup untuk diubah. Dengan kontrak dan polimorfisme, layanan baru ditambahkan tanpa membongkar kelas lama. Pilihan A memaksa method lama dibongkar setiap kali, pilihan B melahirkan kode kembar (melanggar DRY), dan pilihan D tidak menyelesaikan masalah sama sekali.

</details>

### Soal 3

Kontrak `Diskon` berjanji: "potongan tidak pernah negatif". Perhatikan kelas baru berikut.

**Python:**

```python
class VoucherAneh(Diskon):
    def hitung_potongan(self, subtotal: int) -> int:
        if subtotal < 20000:
            return -5000
        return 2000


def total_bayar(subtotal: int, diskon: Diskon) -> int:
    return subtotal - diskon.hitung_potongan(subtotal)


print(total_bayar(15000, VoucherAneh()))
```

**Java:**

```java
class VoucherAneh implements Diskon {
    @Override
    public int hitungPotongan(int subtotal) {
        if (subtotal < 20000) {
            return -5000;
        }
        return 2000;
    }
}

// method static di kelas utama:
static int totalBayar(int subtotal, Diskon diskon) {
    return subtotal - diskon.hitungPotongan(subtotal);
}

// di dalam main:
System.out.println(totalBayar(15000, new VoucherAneh()));
```

Apa yang tercetak, dan bagaimana menilai desain ini?

- A. `10000`, dan tidak ada prinsip yang dilanggar
- B. `15000`, karena potongan negatif otomatis diabaikan
- C. Program berhenti dengan *error*
- D. `20000`; "diskon" itu malah menaikkan total, sehingga melanggar LSP

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: 15000 dikurangi -5000 sama dengan 20000. Program berjalan tanpa *error* (C salah), dan tidak ada aturan bahasa yang mengabaikan nilai negatif (B salah). Masalahnya ada pada **perilaku**: kelas anak mengingkari janji kontrak induknya, sehingga pemanggil yang percaya pada `Diskon` terkejut. Itulah pelanggaran LSP, walaupun kodenya lolos kompilasi.

</details>

### Soal 4

Kontrak `PerangkatKasir` mewajibkan `cetak_struk()`, `pindai_barcode()`, dan `buka_laci()`. Printer bluetooth yang hanya bisa mencetak terpaksa mengisi dua method lain dengan melempar *error*. Perbaikan yang paling tepat adalah ...

- A. Memecah kontrak menjadi kontrak kecil seperti `PencetakStruk`, `PemindaiBarcode`, dan `LaciUang`
- B. Mengisi kedua method itu dengan isi kosong agar tidak ada *error*
- C. Menambahkan lebih banyak method ke `PerangkatKasir` agar lengkap
- D. Menghapus semua kontrak dan memeriksa jenis perangkat dengan percabangan

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: ISP meminta *interface* kecil yang fokus, sehingga setiap perangkat hanya berjanji sebanyak kemampuannya. Pilihan B menyembunyikan masalah: pemanggil mengira pemindaian berhasil padahal tidak terjadi apa-apa (tetap melanggar LSP). Pilihan C memperparah kontrak gemuk, dan pilihan D kembali ke rantai percabangan yang melanggar OCP.

</details>

### Soal 5

Perhatikan dua versi konstruktor `Kedai` berikut.

**Python:**

```python
# Versi 1
class Kedai:
    def __init__(self, nama: str):
        self._penyimpanan = PenyimpananMemori()


# Versi 2
class Kedai:
    def __init__(self, nama: str, penyimpanan: PenyimpananPesanan):
        self._penyimpanan = penyimpanan
```

**Java:**

```java
// Versi 1
public Kedai(String nama) {
    this.penyimpanan = new PenyimpananMemori();
}

// Versi 2
public Kedai(String nama, PenyimpananPesanan penyimpanan) {
    this.penyimpanan = penyimpanan;
}
```

Versi mana yang mengikuti DIP?

- A. Versi 1, karena `Kedai` memegang kendali penuh atas penyimpanannya
- B. Keduanya sama saja, karena hasilnya sama-sama menyimpan pesanan
- C. Versi 2, karena `Kedai` hanya bergantung pada abstraksi yang disuntikkan dari luar
- D. Tidak ada, karena DIP melarang konstruktor menerima parameter

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: versi 2 menerapkan *dependency injection*. `Kedai` hanya mengenal kontrak `PenyimpananPesanan`, sehingga penyimpanan apa pun (memori, terbatas, file) bisa dipasang tanpa mengubah `Kedai`. Versi 1 mengunci `Kedai` pada satu kelas konkret (A salah). Hasil hari ini memang sama (B), tetapi kemudahan diganti dan diuji sangat berbeda. DIP justru sering diwujudkan lewat parameter konstruktor (D salah).

</details>

### Soal 6

Pernyataan yang paling tepat tentang *refactoring* adalah ...

- A. Merapikan kode sambil menambah fitur baru agar sekali jalan
- B. Mengubah struktur kode tanpa mengubah perilakunya, lalu membuktikannya dengan membandingkan hasil
- C. Menulis ulang seluruh program dari nol dengan bahasa lain
- D. Memperbaiki semua *bug* sekaligus agar program lebih benar

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: *refactoring* hanya mengubah susunan kode. Output, hasil hitungan, dan reaksi terhadap kesalahan harus tetap sama. Menambah fitur (A) atau memperbaiki *bug* (D) mengubah perilaku, jadi sebaiknya dikerjakan sebagai langkah terpisah. Menulis ulang dari nol (C) bukan *refactoring* yang bertahap.

</details>

### Soal 7

Setelah *refactoring*, kamu menyimpan output versi lama dan versi baru ke dua file, lalu menjalankan `diff hasil_sebelum.txt hasil_sesudah.txt`. Ternyata **tidak ada apa pun** yang tercetak. Artinya ...

- A. Perintah `diff` gagal berjalan
- B. File `hasil_sesudah.txt` pasti kosong
- C. Kamu tetap harus membandingkan kedua file baris demi baris dengan mata
- D. Kedua file sama persis, sehingga untuk skenario yang dijalankan perilaku program tidak berubah

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: `diff` hanya mencetak sesuatu jika ada perbedaan. Diam berarti sama (`diff -s` bahkan menuliskannya dengan tegas). Jika hanya salah satu file yang kosong, `diff` justru mencetak banyak perbedaan, jadi B salah. Perhatikan juga kata "untuk skenario yang dijalankan": membandingkan output hanya membuktikan kasus yang dicoba, sehingga semakin banyak kasus, semakin kuat buktinya.

</details>

### Soal 8

Andi menulis skrip 30 baris untuk sekali menghitung rata-rata nilai kuis satu kelas. Ia berencana memecahnya menjadi empat *interface* dan enam kelas "agar SOLID". Saran terbaik untuk Andi adalah ...

- A. Tidak perlu. Program kecil sekali pakai cukup ditulis sederhana (KISS, YAGNI); prinsip diterapkan saat perubahan mulai terasa menyulitkan
- B. Wajib, karena setiap program tanpa kecuali harus memenuhi kelima prinsip SOLID
- C. Tambahkan satu *interface* lagi untuk setiap method agar lebih fleksibel
- D. Tulis ulang dalam Java, karena Python tidak bisa menerapkan SOLID

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: SOLID adalah panduan untuk mengelola perubahan, bukan aturan mati. Memecah program kecil sekali pakai menjadi banyak kelas adalah *over-engineering* yang melanggar KISS dan YAGNI. Pilihan C memperparah masalah, dan pilihan D keliru karena kelima prinsip bisa diterapkan di Python maupun Java.

</details>

### Soal 9

Di KedaiKita versi sesudah *refactoring*, pemilik ingin struk menampilkan nomor WhatsApp kedai. Kelas mana yang paling tepat diubah?

- A. `Pesanan`
- B. `StrukPesanan`
- C. `Diskon`
- D. `Kedai`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: menyusun dan mencetak struk adalah satu-satunya urusan `StrukPesanan` (SRP). `Pesanan` hanya mengurus item dan perhitungan, `Diskon` hanya mengurus potongan, dan `Kedai` mengurus menu serta pembuatan pesanan. Inilah manfaat SRP: kamu langsung tahu harus membuka file yang mana.

</details>

### Soal 10

Contoh praktik DIP memakai `PengirimTiruan`, pengirim pura-pura yang hanya mencatat pesan. Apa keuntungan utama yang ditunjukkannya?

- A. Pesan terkirim lebih cepat karena tidak memakai jaringan
- B. `PengingatJadwal` tidak perlu lagi punya konstruktor
- C. Program tidak lagi membutuhkan *interface* `Pengirim`
- D. `PengingatJadwal` bisa diuji tanpa mengirim pesan sungguhan, karena pengirimnya disuntikkan dari luar

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: karena `PengingatJadwal` hanya bergantung pada abstraksi `Pengirim`, kita bebas menyuntikkan objek tiruan saat pengujian, lalu memeriksa catatannya. Pengirim tiruan tidak mengirim apa pun, jadi A salah. Konstruktor justru menjadi jalan masuk penyuntikan (B salah), dan *interface* `Pengirim` tetap dibutuhkan sebagai kontraknya (C salah).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Kamu siap merancang kode yang tahan perubahan | Lanjut ke [Pertemuan 14](../Pertemuan-14-Design-Pattern/README.md) |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian konsep untuk prinsip yang soalnya kamu jawab salah, lalu kerjakan Latihan 1 dan 2 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan, jalankan keenam contoh di halaman praktik, dan bandingkan bagian MELANGGAR dengan bagian SESUAI |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 14 ➡️](../Pertemuan-14-Design-Pattern/README.md)
