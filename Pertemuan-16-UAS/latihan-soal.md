# Latihan Soal UAS — Pemrograman Berorientasi Objek

[⬅️ Informasi UAS](README.md) · [🏠 Beranda](../README.md) · [Pembahasan ➡️](pembahasan.md)

> [!IMPORTANT]
> Ini adalah soal **latihan persiapan UAS**, bukan soal ujian yang sebenarnya. Bentuk, jumlah soal, bobot, dan aturan ujian yang sesungguhnya mengikuti pengumuman dosen.

**Cara memakai halaman ini sebagai simulasi ujian:**

1. Siapkan kertas atau berkas jawaban dan sebuah timer.
2. Kerjakan Bagian A dan B **tanpa** membuka catatan dan tanpa menjalankan kode.
3. Kerjakan Bagian C di komputer, dengan bahasa jalurmu (Python **atau** Java).
4. Setelah semua selesai, baru cocokkan di [Pembahasan](pembahasan.md).

| Bagian | Bentuk | Jumlah | Saran waktu | Skor latihan |
|---|---|---|---|---|
| A | Pilihan ganda (6 soal membaca kode Python dan Java) | 15 | 30 menit | 15 × 2 = 30 |
| B | Esai dan analisis desain | 5 | 60 menit | 5 × 6 = 30 |
| C | Praktik di komputer | 2 | 150 menit | 2 × 20 = 40 |

> [!TIP]
> Pada soal membaca kode, versi Python dan Java selalu **bermakna sama**. Baca versi jalurmu saja, lalu lirik versi satunya untuk melatih kemampuan membaca dua bahasa.

## Daftar Isi

- [Bagian A: Pilihan Ganda](#bagian-a-pilihan-ganda)
- [Bagian B: Esai dan Analisis Desain](#bagian-b-esai-dan-analisis-desain)
- [Bagian C: Soal Praktik](#bagian-c-soal-praktik)

---

## Bagian A: Pilihan Ganda

Pilih **satu** jawaban yang paling tepat. Catat jawabanmu, misalnya `A1-B, A2-C, ...`, lalu cocokkan di [Pembahasan Bagian A](pembahasan.md#bagian-a-pilihan-ganda).

### Soal A1

Perhatikan kode berikut.

**Python:**

```python
class Hewan:
    def suara(self):
        return "hmm"

    def perkenalan(self):
        return "Aku bilang " + self.suara()


class Kucing(Hewan):
    def suara(self):
        return "meong"


class Anjing(Hewan):
    def perkenalan(self):
        return super().perkenalan() + "!"


daftar = [Kucing(), Anjing(), Hewan()]
for h in daftar:
    print(h.perkenalan())
```

**Java:**

```java
class Hewan {
    String suara() {
        return "hmm";
    }

    String perkenalan() {
        return "Aku bilang " + suara();
    }
}

class Kucing extends Hewan {
    @Override
    String suara() {
        return "meong";
    }
}

class Anjing extends Hewan {
    @Override
    String perkenalan() {
        return super.perkenalan() + "!";
    }
}

// di dalam main:
Hewan[] daftar = {new Kucing(), new Anjing(), new Hewan()};
for (Hewan h : daftar) {
    System.out.println(h.perkenalan());
}
```

Tiga baris yang tercetak berturut-turut adalah ...

- A. `Aku bilang meong`, `Aku bilang hmm!`, `Aku bilang hmm`
- B. `Aku bilang hmm`, `Aku bilang hmm!`, `Aku bilang hmm`
- C. `Aku bilang meong`, `Aku bilang meong!`, `Aku bilang hmm`
- D. `Aku bilang meong`, `Aku bilang hmm`, `Aku bilang hmm`

### Soal A2

Pernyataan yang **benar** tentang *overloading* dan *overriding* adalah ...

- A. *Overriding* terjadi di dalam satu kelas yang sama, sedangkan *overloading* selalu membutuhkan pewarisan
- B. Python mendukung *overloading*: dua `def hitung(...)` dengan jumlah parameter berbeda di satu kelas akan dipilih sesuai jumlah argumen
- C. Di Java, versi *overload* dipilih saat kompilasi berdasarkan daftar parameter, sedangkan versi *override* dipilih saat program berjalan berdasarkan objek sebenarnya
- D. Method yang di-*override* di kelas anak boleh mempersempit hak aksesnya, misalnya dari `public` menjadi `private`

### Soal A3

Perhatikan kode berikut. Baris diberi tanda (1), (2), dan (3).

**Python:**

```python
from abc import ABC, abstractmethod


class Bentuk(ABC):
    def __init__(self, nama):
        self.nama = nama

    @abstractmethod
    def luas(self):
        pass

    def info(self):
        return f"{self.nama}: {self.luas()}"


class Persegi(Bentuk):
    def __init__(self, sisi):
        super().__init__("Persegi")
        self.sisi = sisi

    def luas(self):
        return self.sisi * self.sisi


print(Persegi(4).info())  # (1)
b = Bentuk("Umum")        # (2)
print(b.info())           # (3)
```

**Java:**

```java
abstract class Bentuk {
    String nama;

    Bentuk(String nama) {
        this.nama = nama;
    }

    abstract int luas();

    String info() {
        return nama + ": " + luas();
    }
}

class Persegi extends Bentuk {
    int sisi;

    Persegi(int sisi) {
        super("Persegi");
        this.sisi = sisi;
    }

    @Override
    int luas() {
        return sisi * sisi;
    }
}

// di dalam main:
System.out.println(new Persegi(4).info()); // (1)
Bentuk b = new Bentuk("Umum");             // (2)
System.out.println(b.info());              // (3)
```

Apa yang terjadi?

- A. Keduanya mencetak `Persegi: 16`, lalu error di baris (3) saat `luas()` milik `Bentuk` dipanggil
- B. Python mencetak `Persegi: 16` lalu berhenti dengan `TypeError` di baris (2); Java ditolak *compiler* karena baris (2), sehingga tidak ada yang tercetak
- C. Keduanya mencetak `Persegi: 16` dan `Umum: 0`
- D. Keduanya error di baris (1), karena kelas abstrak `Bentuk` tidak boleh punya konstruktor

### Soal A4

Aplikasi akademik punya kelas `Mahasiswa`, `Dosen`, dan `Ruangan`. Di versi Java, `Mahasiswa` dan `Dosen` **sudah** mewarisi kelas `Orang`. Kini ketiga kelas itu harus bisa diekspor ke CSV dengan method `ke_csv()` / `keCsv()`, dan kelak kelas lain (misalnya `MataKuliah`) juga perlu kemampuan yang sama. Rancangan yang paling tepat adalah ...

- A. Kelas abstrak `DataKampus` berisi method abstrak `ke_csv()`, lalu ketiga kelas mewarisinya
- B. Kelas biasa `Ekspor` yang memeriksa jenis objek dengan rantai `isinstance(...)` / `instanceof`
- C. Menjadikan `Ruangan` kelas anak `Dosen` agar ikut mewarisi `ke_csv()`
- D. *Interface* `BisaDiekspor` yang diimplementasikan ketiga kelas (di Python: ABC yang hanya berisi method abstrak, atau `typing.Protocol`)

### Soal A5

Perhatikan kode berikut.

**Python:**

```python
def bagi(a, b):
    try:
        hasil = a // b
    except ZeroDivisionError:
        print("A", end="")
        return -1
    else:
        print("B", end="")
        return hasil
    finally:
        print("C", end="")


x = bagi(10, 0)
y = bagi(10, 5)
print()
print(x, y)
```

**Java:**

```java
static int bagi(int a, int b) {
    try {
        int hasil = a / b;
        System.out.print("B");
        return hasil;
    } catch (ArithmeticException e) {
        System.out.print("A");
        return -1;
    } finally {
        System.out.print("C");
    }
}

// di dalam main:
int x = bagi(10, 0);
int y = bagi(10, 5);
System.out.println();
System.out.println(x + " " + y);
```

Output program adalah ...

- A. `AB` lalu `-1 2`
- B. `ACBC` lalu `-1 2`
- C. `ACB` lalu `-1 2`
- D. `A` lalu program berhenti karena pembagian dengan nol

### Soal A6

`StokTidakCukupError` (Java: `StokTidakCukupException`) adalah kelas anak dari `KedaiError` (Java: `KedaiException`). Mengapa blok `except`/`catch` untuk kelas anak itu harus ditulis **sebelum** blok untuk induknya?

- A. Blok diperiksa dari atas, dan hanya blok **pertama** yang cocok yang dijalankan; jika blok induk ditulis lebih dulu, blok anak tidak akan pernah tercapai (di Java bahkan menjadi error kompilasi)
- B. Agar program berjalan lebih cepat, karena *exception* kelas anak lebih ringan
- C. Karena *exception* kelas anak tidak bisa ditangkap oleh blok milik induknya
- D. Karena Python dan Java mewajibkan blok `except`/`catch` diurutkan menurut abjad nama kelasnya

### Soal A7

Pernyataan yang **benar** tentang *checked exception* di Java adalah ...

- A. Semua turunan `RuntimeException`, misalnya `IllegalArgumentException`, termasuk *checked exception*
- B. *Checked exception* hanya bisa terjadi saat kompilasi, tidak pernah saat program berjalan
- C. Python juga punya *checked exception*, ditandai kata kunci `throws` setelah `def`
- D. *Compiler* Java mewajibkan *checked exception* ditangkap dengan `try-catch` atau dideklarasikan dengan `throws` pada method

### Soal A8

Perhatikan kode berikut.

**Python:**

```python
class Peserta:
    def __init__(self, nama, skor):
        self.nama = nama
        self.skor = skor


daftar = [Peserta("Dimas", 80), Peserta("Ayu", 92),
          Peserta("Citra", 80), Peserta("Bima", 75)]
urut = sorted(daftar, key=lambda p: (-p.skor, p.nama))
print(", ".join(p.nama for p in urut))
```

**Java:**

```java
// Peserta punya getNama() dan getSkor()
List<Peserta> daftar = new ArrayList<>(List.of(new Peserta("Dimas", 80),
        new Peserta("Ayu", 92), new Peserta("Citra", 80), new Peserta("Bima", 75)));
daftar.sort(Comparator.comparing(Peserta::getSkor).reversed()
        .thenComparing(Peserta::getNama));
List<String> nama = new ArrayList<>();
for (Peserta p : daftar) {
    nama.add(p.getNama());
}
System.out.println(String.join(", ", nama));
```

Output program adalah ...

- A. `Ayu, Dimas, Citra, Bima`
- B. `Bima, Citra, Dimas, Ayu`
- C. `Ayu, Citra, Dimas, Bima`
- D. `Ayu, Bima, Citra, Dimas`

### Soal A9

Perhatikan kode berikut.

**Python:**

```python
class Buku:
    def __init__(self, kode, judul):
        self.kode = kode
        self.judul = judul

    def __eq__(self, lain):
        return isinstance(lain, Buku) and self.kode == lain.kode

    def __hash__(self):
        return hash(self.kode)


rak = set()
rak.add(Buku("B01", "Laskar Pelangi"))
rak.add(Buku("B02", "Bumi Manusia"))
rak.add(Buku("B01", "Laskar Pelangi (cetak ulang)"))
print(len(rak))
```

**Java:**

```java
class Buku {
    String kode;
    String judul;

    Buku(String kode, String judul) {
        this.kode = kode;
        this.judul = judul;
    }

    @Override
    public boolean equals(Object lain) {
        if (!(lain instanceof Buku)) {
            return false;
        }
        return kode.equals(((Buku) lain).kode);
    }

    @Override
    public int hashCode() {
        return kode.hashCode();
    }
}

// di dalam main:
Set<Buku> rak = new HashSet<>();
rak.add(new Buku("B01", "Laskar Pelangi"));
rak.add(new Buku("B02", "Bumi Manusia"));
rak.add(new Buku("B01", "Laskar Pelangi (cetak ulang)"));
System.out.println(rak.size());
```

Output program adalah ...

- A. `2`
- B. `3`
- C. `1`
- D. Error, karena set tidak boleh berisi objek dari kelas buatan sendiri

### Soal A10

Kamu menyimpan stok barang dengan kunci berupa kode barang. Laporan stok harus **selalu** tercetak sesuai urutan barang dimasukkan. Di Java, implementasi `Map` yang tepat adalah ...

- A. `HashMap`, karena urutan kuncinya selalu sama dengan urutan dimasukkan
- B. `LinkedHashMap`
- C. `TreeMap`, karena ia mengingat urutan saat data dimasukkan
- D. `HashSet`, karena kode barang tidak pernah ganda

### Soal A11

Kelas `LaporanNilai` menghitung rata-rata nilai, menyusun tabel teks, mengirim email ke dosen wali, dan menyimpan hasilnya ke file. Prinsip SOLID yang **paling jelas** dilanggar adalah ...

- A. LSP, karena kelas itu tidak punya kelas anak
- B. ISP, karena kelas itu tidak mengimplementasikan *interface*
- C. SRP, karena kelas itu punya banyak alasan untuk berubah
- D. DIP, karena setiap kelas wajib mengimplementasikan minimal satu *interface*

### Soal A12

Kelas `Burung` punya method `terbang()`. Kelas `Penguin` mewarisi `Burung` lalu meng-*override* `terbang()` agar melempar *exception* "Penguin tidak bisa terbang". Akibatnya, kode lama yang memanggil `terbang()` untuk setiap objek di daftar burung tiba-tiba gagal. Prinsip yang dilanggar dan perbaikan yang tepat adalah ...

- A. SRP; pindahkan `terbang()` ke sebuah kelas utilitas terpisah
- B. DIP; suntikkan objek `Penguin` lewat konstruktor
- C. OCP; tambahkan pemeriksaan `isinstance(burung, Penguin)` / `instanceof` di setiap pemanggil
- D. LSP; pisahkan kemampuan terbang ke *interface* atau kelas tersendiri (misalnya `BisaTerbang`) yang hanya dimiliki burung yang memang bisa terbang

### Soal A13

Perhatikan kode berikut.

**Python:**

```python
class Kanal:
    def __init__(self):
        self._pelanggan = []

    def langganan(self, penonton):
        self._pelanggan.append(penonton)

    def unggah(self, judul):
        for penonton in self._pelanggan:
            penonton.perbarui(judul)


class Penonton:
    def __init__(self, nama):
        self.nama = nama
        self.notifikasi = 0

    def perbarui(self, judul):
        self.notifikasi += 1


kanal = Kanal()
ayu = Penonton("Ayu")
bima = Penonton("Bima")
kanal.langganan(ayu)
kanal.unggah("Video 1")
kanal.langganan(bima)
kanal.unggah("Video 2")
kanal.langganan(ayu)
kanal.unggah("Video 3")
print(ayu.notifikasi, bima.notifikasi)
```

**Java:**

```java
class Kanal {
    private List<Penonton> pelanggan = new ArrayList<>();

    void langganan(Penonton penonton) {
        pelanggan.add(penonton);
    }

    void unggah(String judul) {
        for (Penonton penonton : pelanggan) {
            penonton.perbarui(judul);
        }
    }
}

class Penonton {
    String nama;
    int notifikasi = 0;

    Penonton(String nama) {
        this.nama = nama;
    }

    void perbarui(String judul) {
        notifikasi++;
    }
}

// di dalam main:
Kanal kanal = new Kanal();
Penonton ayu = new Penonton("Ayu");
Penonton bima = new Penonton("Bima");
kanal.langganan(ayu);
kanal.unggah("Video 1");
kanal.langganan(bima);
kanal.unggah("Video 2");
kanal.langganan(ayu);
kanal.unggah("Video 3");
System.out.println(ayu.notifikasi + " " + bima.notifikasi);
```

Output program adalah ...

- A. `3 3`
- B. `3 2`
- C. `4 2`
- D. `2 2`

### Soal A14

Aplikasi ojek online menghitung tarif dengan beberapa aturan: tarif normal, tarif jam sibuk, dan tarif promo. Aturan yang dipakai dipilih saat aplikasi berjalan, dan aturan baru sering ditambahkan tanpa boleh mengubah kelas `Perjalanan`. Pola yang paling cocok adalah ...

- A. Strategy
- B. Singleton
- C. Observer
- D. Factory

### Soal A15

Aplikasi kasir dibangun berlapis: tampilan (CLI), layanan, model, dan penyimpanan (file CSV). Di mana aturan "harga menu harus lebih dari 0" **paling tepat** ditegakkan?

- A. Di lapisan tampilan, karena di sanalah kasir mengetik harga
- B. Di lapisan model (kelas `Menu`, lewat konstruktor dan *setter*/*property*), agar aturan berlaku dari mana pun objek dibuat atau diubah
- C. Di lapisan penyimpanan, karena data akhirnya ditulis ke file CSV
- D. Cukup di *unit test*, karena test akan menangkap harga yang salah

---

## Bagian B: Esai dan Analisis Desain

Jawab dengan kalimatmu sendiri. Jawaban yang baik memuat **definisi, contoh, dan alasan**. Setiap soal bernilai 6 poin; rincian poin ada di tiap soal. Jawaban model ada di [Pembahasan Bagian B](pembahasan.md#bagian-b-esai-dan-analisis-desain).

### Soal B1: Empat Pilar PBO di KedaiKita

1. Jelaskan keempat pilar PBO (enkapsulasi, pewarisan, polimorfisme, abstraksi) dengan kalimatmu sendiri. Untuk setiap pilar, tunjukkan satu contoh nyata dari KedaiKita (versi P09–P15) atau dari proyek akhirmu. **(4 poin)**
2. Seorang teman menulis `class Pesanan(ItemPesanan)` (Java: `class Pesanan extends ItemPesanan`) dengan alasan "supaya `Pesanan` langsung punya menu dan jumlah". Jelaskan mengapa desain ini keliru dan apa yang seharusnya dipakai. **(2 poin)**

### Soal B2: Kelas Abstrak atau Interface?

1. Bandingkan kelas abstrak dan *interface* dalam sebuah tabel, minimal empat aspek. Contoh aspek: bisa dibuat objeknya atau tidak, boleh menyimpan atribut atau tidak, boleh berisi method lengkap atau tidak, berapa yang boleh diwarisi/diimplementasikan satu kelas, dan kapan dipakai. **(3 poin)**
2. Tentukan pilihanmu beserta alasannya untuk dua kasus berikut. **(2 poin)**
   - Aplikasi rental: semua kendaraan punya nomor polisi, tarif per hari, dan method `info()` yang sama persis, tetapi cara menghitung denda keterlambatan berbeda untuk mobil, motor, dan sepeda.
   - Kelas `Struk`, `LaporanBulanan`, dan `KartuAnggota` tidak berkerabat, tetapi semuanya harus bisa dicetak ke PDF.
3. Khusus Python: apa bedanya membuat kontrak dengan ABC dan dengan `typing.Protocol`? **(1 poin)**

### Soal B3: Checked dan Unchecked Exception

1. Jelaskan perbedaan *checked* dan *unchecked exception* di Java, beserta satu contoh kelas bawaan untuk masing-masing. **(2 poin)**
2. Mengapa Python tidak punya konsep ini? Apa yang perlu dilakukan programmer Python sebagai gantinya? **(1 poin)**
3. Di KedaiKita versi Java, `KedaiException` dibuat *checked* (turunan `Exception`). Sebutkan satu keuntungan dan satu konsekuensinya bagi kode yang memanggil `cariMenu()`. **(2 poin)**
4. Kapan kamu justru memilih *unchecked exception*? Beri satu contoh. **(1 poin)**

### Soal B4: Analisis SOLID pada Pengelola Nilai

Perhatikan kelas berikut. Programnya berjalan, tetapi desainnya bermasalah.

**Python:**

```python
class PengelolaNilai:
    def __init__(self):
        self.data = []  # isi: (nim, nama, nilai)

    def tambah(self, nim, nama, nilai):
        self.data.append((nim, nama, nilai))

    def huruf(self, nilai):
        if nilai >= 80:
            return "A"
        elif nilai >= 70:
            return "B"
        elif nilai >= 60:
            return "C"
        return "D"

    def cetak_laporan(self, format_laporan):
        for nim, nama, nilai in self.data:
            if format_laporan == "teks":
                print(f"{nim} {nama}: {nilai} ({self.huruf(nilai)})")
            elif format_laporan == "csv":
                print(f"{nim};{nama};{nilai};{self.huruf(nilai)}")

    def simpan(self):
        with open("nilai.txt", "w", encoding="utf-8") as berkas:
            for nim, nama, nilai in self.data:
                berkas.write(f"{nim};{nama};{nilai}\n")

    def kirim_email(self, alamat):
        print(f"Menghubungi server email kampus... terkirim ke {alamat}")
```

**Java:**

```java
class PengelolaNilai {
    List<String[]> data = new ArrayList<>(); // isi: {nim, nama, nilai}

    void tambah(String nim, String nama, int nilai) {
        data.add(new String[] {nim, nama, String.valueOf(nilai)});
    }

    String huruf(int nilai) {
        if (nilai >= 80) {
            return "A";
        } else if (nilai >= 70) {
            return "B";
        } else if (nilai >= 60) {
            return "C";
        }
        return "D";
    }

    void cetakLaporan(String formatLaporan) {
        for (String[] d : data) {
            int nilai = Integer.parseInt(d[2]);
            if (formatLaporan.equals("teks")) {
                System.out.println(d[0] + " " + d[1] + ": " + nilai + " (" + huruf(nilai) + ")");
            } else if (formatLaporan.equals("csv")) {
                System.out.println(d[0] + ";" + d[1] + ";" + nilai + ";" + huruf(nilai));
            }
        }
    }

    void simpan() throws IOException {
        StringBuilder isi = new StringBuilder();
        for (String[] d : data) {
            isi.append(d[0] + ";" + d[1] + ";" + d[2] + "\n");
        }
        Files.writeString(Path.of("nilai.txt"), isi.toString(), StandardCharsets.UTF_8);
    }

    void kirimEmail(String alamat) {
        System.out.println("Menghubungi server email kampus... terkirim ke " + alamat);
    }
}
```

Baris `import` pada versi Java tidak ditampilkan agar ringkas.

1. Identifikasi **minimal tiga** pelanggaran prinsip SOLID. Untuk setiap pelanggaran, sebutkan prinsipnya, buktinya di kode (nama method atau baris), dan akibatnya jika kebutuhan berubah. **(3 poin)**
2. Usulkan rancangan perbaikan: daftar kelas/*interface* beserta tanggung jawabnya. Boleh berupa diagram kelas sederhana. **(2 poin)**
3. Sebutkan satu hal yang menurutmu **tidak perlu** dipecah atau diabstraksikan sekarang, beserta alasannya. **(1 poin)**

<details>
<summary>💡 Petunjuk</summary>

- Hitung ada berapa "alasan untuk berubah" yang ditanggung kelas ini: aturan nilai, format laporan, tempat penyimpanan, cara pengiriman.
- Apa yang harus diedit jika muncul format laporan baru, misalnya HTML?
- Bisakah kelas ini diuji tanpa benar-benar menulis file atau menghubungi server email?
- Apa yang terjadi jika `cetak_laporan("html")` dipanggil?

</details>

### Soal B5: Memilih Design Pattern untuk Bank Sampah

Himpunan mahasiswa membuat aplikasi bank sampah (fiktif). Ada empat kebutuhan:

1. Setiap kali nasabah menyetor sampah, beberapa pihak harus diberi tahu: layar saldo nasabah, notifikasi WhatsApp, dan berkas log. Ke depan akan ditambah dasbor admin.
2. Nilai setoran dihitung dengan aturan bonus yang bisa diganti saat aplikasi berjalan: tanpa bonus, bonus akhir bulan, dan bonus Hari Bumi. Aturan bonus baru sering muncul.
3. Seluruh bagian aplikasi harus membaca **satu** pengaturan yang sama: nama bank sampah dan daftar harga per kg.
4. Petugas mengetik jenis sampah sebagai teks (`"plastik"`, `"kertas"`, `"logam"`), lalu aplikasi membuat objek `Sampah` yang sesuai.

Untuk **setiap** kebutuhan, tuliskan: (a) pola yang paling cocok, (b) alasannya dalam 1–2 kalimat, (c) kelas atau *interface* utamanya, dan (d) satu kekurangan atau risiko pola tersebut. **(1,5 poin per kebutuhan)**

---

## Bagian C: Soal Praktik

Kerjakan di komputer dengan bahasa jalurmu. Buat **satu file** untuk setiap soal. Pembahasan desain ada di [Pembahasan Bagian C](pembahasan.md#bagian-c-soal-praktik).

### Soal C1: Sistem Pemesanan Tiket Bioskop

**Bobot:** 20 poin · **Saran waktu:** 90 menit

**Kompetensi yang diuji:** kelas abstrak, polimorfisme, *exception* buatan sendiri, koleksi (dict/Map dan pengurutan), enkapsulasi.

**Cerita:** BioskopKita, bioskop kecil di Samarinda, ingin mengganti pencatatan tiket di buku tulis dengan program sederhana. Setiap hari ada beberapa jadwal tayang. Setiap studio punya 15 kursi: baris `A` sampai `C`, nomor `1` sampai `5` (kursi `A1` sampai `C5`).

**Kebutuhan:**

1. **Kelas abstrak `Tiket`** dengan atribut kode kursi, nama pemesan, dan harga dasar yang hanya bisa dibaca dari luar (Python: *property* tanpa *setter*; Java: field `private final` + *getter*). Method abstraknya `jenis()` dan `hitung_harga()` / `hitungHarga()`. Method konkret `__str__` / `toString()` memakai kedua method abstrak itu.
2. **Tiga kelas anak** dengan aturan harga berikut (semua bilangan bulat):

   | Jenis | Aturan harga |
   |---|---|
   | Reguler | sama dengan harga dasar jadwal |
   | VIP | harga dasar + Rp25.000 (kursi sofa dan popcorn) |
   | Pelajar | harga dasar dikurangi 20% |

3. **Kelas `Jadwal`** menyimpan kode jadwal, judul film, jam, nomor studio, harga dasar (harus lebih dari 0), dan kursi terjual dalam dict/Map (kode kursi → `Tiket`). Sediakan method untuk menambah tiket, daftar kursi kosong, daftar tiket terjual (urut kode kursi), jumlah tiket terjual, dan pendapatan. Pendapatan dihitung **tanpa** memeriksa jenis tiket.
4. **Kelas `Bioskop`** menyimpan jadwal dalam dict/Map (kode jadwal → `Jadwal`) dan menyediakan:
   - `cari_jadwal(kode)` / `cariJadwal(kode)`;
   - `pesan(kode_jadwal, jenis, kode_kursi, pemesan)` dengan urutan pemeriksaan: **jadwal → jenis tiket → kursi**;
   - laporan per film, urut **pendapatan terbesar**; jika pendapatannya sama, urut **judul A–Z**;
   - rekap jumlah tiket dan pendapatan per jenis tiket, urut nama jenis.
5. ***Exception* buatan sendiri**, semuanya turunan `BioskopError` (Python) atau `BioskopException` (Java, *checked*):

   | *Exception* | Kapan dilempar | Contoh pesan |
   |---|---|---|
   | `JadwalTidakDitemukanError` / `...Exception` | Kode jadwal tidak terdaftar | `Jadwal J05 tidak ditemukan` |
   | `KursiTidakAdaError` / `...Exception` | Kode kursi di luar `A1`–`C5` | `Kursi D1 tidak ada di Studio 1` |
   | `KursiSudahTerjualError` / `...Exception` | Kursi sudah dipesan; membawa data **sisa kursi kosong** | `Kursi A1 untuk Mahakam Biru sudah terjual` |

   Jenis tiket yang tidak dikenal ditolak dengan `ValueError` / `IllegalArgumentException` berpesan `Jenis tiket 'premium' tidak dikenal`. Penulisan jenis tidak membedakan huruf besar dan kecil (`"VIP"` sama dengan `"vip"`).
6. **Program utama**: tampilkan jadwal, proses 13 permintaan di bawah satu per satu, dan tangani setiap kegagalan tanpa menghentikan program. Untuk kursi yang sudah terjual, tampilkan juga saran berisi jumlah kursi kosong. Setelah itu tampilkan tiket terjual dan kursi kosong untuk jadwal `J02`, laporan per film, dan rekap per jenis tiket.

**Data jadwal:**

| Kode | Judul | Jam | Studio | Harga dasar |
|---|---|---|---|---|
| J01 | Rindu di Tepian | 13:00 | 1 | 30000 |
| J02 | Mahakam Biru | 16:00 | 2 | 40000 |
| J03 | Detektif Kampus | 19:00 | 1 | 50000 |

**Data permintaan (diproses berurutan):**

| No | Jadwal | Jenis | Kursi | Pemesan |
|---|---|---|---|---|
| 1 | J02 | reguler | A1 | Budi Santoso |
| 2 | J02 | VIP | A2 | Siti Aminah |
| 3 | J02 | pelajar | A1 | Rina Marlina |
| 4 | J02 | pelajar | A3 | Rina Marlina |
| 5 | J03 | vip | D1 | Andi Wijaya |
| 6 | J03 | vip | C5 | Andi Wijaya |
| 7 | J05 | reguler | A1 | Dimas Pratama |
| 8 | J01 | premium | B2 | Dimas Pratama |
| 9 | J01 | vip | B2 | Dimas Pratama |
| 10 | J01 | reguler | B3 | Ayu Lestari |
| 11 | J01 | reguler | B4 | Bima Saputra |
| 12 | J03 | pelajar | C4 | Citra Dewi |
| 13 | J02 | reguler | B1 | Eko Prasetyo |

**Contoh output yang diharapkan:**

```text
=== JADWAL TAYANG BioskopKita ===
J01  13:00  Studio 1  Rindu di Tepian     Rp30.000
J02  16:00  Studio 2  Mahakam Biru        Rp40.000
J03  19:00  Studio 1  Detektif Kampus     Rp50.000

=== PEMESANAN TIKET ===
[OK]    J02/A1 Reguler untuk Budi Santoso: Rp40.000
[OK]    J02/A2 VIP untuk Siti Aminah: Rp65.000
[GAGAL] Kursi A1 untuk Mahakam Biru sudah terjual
        Saran: pilih kursi lain, masih ada 13 kursi kosong
[OK]    J02/A3 Pelajar untuk Rina Marlina: Rp32.000
[GAGAL] Kursi D1 tidak ada di Studio 1
[OK]    J03/C5 VIP untuk Andi Wijaya: Rp75.000
[GAGAL] Jadwal J05 tidak ditemukan
[GAGAL] Jenis tiket 'premium' tidak dikenal
[OK]    J01/B2 VIP untuk Dimas Pratama: Rp55.000
[OK]    J01/B3 Reguler untuk Ayu Lestari: Rp30.000
[OK]    J01/B4 Reguler untuk Bima Saputra: Rp30.000
[OK]    J03/C4 Pelajar untuk Citra Dewi: Rp40.000
[OK]    J02/B1 Reguler untuk Eko Prasetyo: Rp40.000

=== TIKET TERJUAL J02: Mahakam Biru ===
A1  Reguler  Budi Santoso      Rp40.000
A2  VIP      Siti Aminah       Rp65.000
A3  Pelajar  Rina Marlina      Rp32.000
B1  Reguler  Eko Prasetyo      Rp40.000
Kursi kosong (11): A4, A5, B2, B3, B4, B5, C1, C2, C3, C4, C5

=== LAPORAN PENDAPATAN PER FILM ===
1. Mahakam Biru       4 tiket   Rp177.000
2. Detektif Kampus    2 tiket   Rp115.000
3. Rindu di Tepian    3 tiket   Rp115.000
Total pendapatan: Rp407.000

=== REKAP PER JENIS TIKET ===
Pelajar   2 tiket    Rp72.000
Reguler   4 tiket   Rp140.000
VIP       3 tiket   Rp195.000
```

Spasi dan perataan kolom boleh sedikit berbeda, tetapi **angka, urutan baris, dan pesan error** harus sama.

<details>
<summary>💡 Petunjuk</summary>

- Mulailah dari hierarki `Tiket`, lalu uji ketiga kelas anaknya dengan harga dasar 40000 (hasilnya 40000, 65000, 32000).
- Untuk membuat objek tiket dari teks jenis, buat satu tempat khusus (misalnya kelas `TiketFactory` dengan method `buat(...)`), supaya rantai `if` jenis tiket tidak tersebar ke mana-mana.
- Daftar 15 kursi bisa dibuat dengan dua perulangan bersarang: baris `"ABC"` dan nomor 1 sampai 5.
- Pengurutan dua kriteria: Python `key=lambda j: (-j.pendapatan(), j.judul)`; Java `Comparator.comparing(Jadwal::pendapatan).reversed().thenComparing(Jadwal::getJudul)`.
- Perhatikan laporan per film: pendapatan Detektif Kampus dan Rindu di Tepian **sama** (Rp115.000), jadi kriteria kedua (judul A–Z) yang menentukan urutannya.
- Urutan `except`/`catch`: tangkap `KursiSudahTerjual...` lebih dulu (perlu data sisa kursi), baru induknya.

</details>

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kelas abstrak `Tiket` + tiga kelas anak dengan *override* yang benar | 20% |
| Polimorfisme: pendapatan dan laporan dihitung tanpa memeriksa jenis tiket | 15% |
| *Exception* buatan sendiri (hierarki, pesan, data tambahan) dan penanganannya (urutan spesifik → umum, program tidak berhenti) | 20% |
| Koleksi: dict/Map untuk jadwal dan kursi, daftar kursi kosong, pengurutan dua kriteria, rekap per jenis | 20% |
| Enkapsulasi dan validasi (atribut tidak diubah dari luar, harga dasar harus positif) | 10% |
| Output sesuai contoh; kode rapi (nama jelas, komentar secukupnya) | 15% |

**Solusi:** [🐍 Python](python/solusi/soal_c1_tiket_bioskop.py) · [☕ Java](java/solusi/SoalC1TiketBioskop.java)

### Soal C2: Refactor Kasir Laundry yang Berantakan

**Bobot:** 20 poin · **Saran waktu:** 60 menit

**Kompetensi yang diuji:** mengenali *code smell*, menerapkan SOLID, memakai *design pattern*, dan membuktikan bahwa refactoring tidak mengubah perilaku.

**Cerita:** Laundry Bersih Kilat (fiktif), langganan anak kos di sekitar kampus, memakai program kasir yang ditulis terburu-buru. Programnya benar, tetapi setiap kali pemilik ingin menambah promo atau mengganti WhatsApp dengan SMS, programmer harus membongkar kelas yang sama. Berikut kode awalnya. Pilih versi jalurmu.

<details>
<summary>🐍 Kode awal versi Python</summary>

```python
class LaundrySerbaBisa:
    def __init__(self):
        self.riwayat = []  # isi: (kode, nama, berat, total)
        self.nomor = 0

    def terima_cucian(self, nama, no_hp, layanan, berat, promo):
        # cari tarif per kg
        if layanan == "cuci kering":
            tarif = 6000
        elif layanan == "cuci setrika":
            tarif = 8000
        elif layanan == "setrika saja":
            tarif = 5000
        else:
            print(f"[DITOLAK] Layanan '{layanan}' tidak tersedia")
            return
        self.nomor += 1
        kode = f"L{self.nomor:03d}"
        subtotal = tarif * berat

        # hitung promo
        potongan = 0
        nama_promo = ""
        if promo == "member":
            potongan = subtotal * 10 // 100
            nama_promo = "Member 10%"
        elif promo == "gratis1kg":
            if berat >= 5:
                potongan = tarif
                nama_promo = "Gratis 1 kg"
        total = subtotal - potongan

        # cetak nota
        print("=" * 36)
        print("LAUNDRY BERSIH KILAT")
        print("=" * 36)
        print(f"No. Order : {kode}")
        print(f"Pelanggan : {nama}")
        print(f"Layanan   : {layanan}")
        teks_tarif = f"Rp{tarif:,}".replace(",", ".")
        print(f"Berat     : {berat} kg x {teks_tarif}")
        print("-" * 36)
        teks_subtotal = f"Rp{subtotal:,}".replace(",", ".")
        print(f"{'Subtotal':<24}{teks_subtotal:>12}")
        if potongan > 0:
            teks_potongan = "-" + f"Rp{potongan:,}".replace(",", ".")
            print(f"{'Promo ' + nama_promo:<24}{teks_potongan:>12}")
        teks_total = f"Rp{total:,}".replace(",", ".")
        print(f"{'TOTAL':<24}{teks_total:>12}")
        print("=" * 36)

        # kirim WhatsApp
        print(f"[WA ke {no_hp}] Halo {nama}, cucian {kode} sudah kami terima. "
              f"Total {teks_total}.")

        # simpan riwayat
        self.riwayat.append((kode, nama, berat, total))

    def cetak_laporan(self):
        print("=== LAPORAN HARIAN ===")
        total_berat = 0
        pendapatan = 0
        for kode, nama, berat, total in self.riwayat:
            teks = f"Rp{total:,}".replace(",", ".")
            print(f"{kode}  {nama:<16}{berat:>3} kg{teks:>12}")
            total_berat += berat
            pendapatan += total
        print(f"Jumlah order : {len(self.riwayat)}")
        print(f"Total berat  : {total_berat} kg")
        print("Pendapatan   : " + f"Rp{pendapatan:,}".replace(",", "."))


def main():
    laundry = LaundrySerbaBisa()
    laundry.terima_cucian("Budi Santoso", "081234567890", "cuci setrika", 4,
                          "member")
    print()
    laundry.terima_cucian("Siti Aminah", "082198765432", "cuci kering", 6,
                          "gratis1kg")
    print()
    laundry.terima_cucian("Rina Marlina", "085312345678", "setrika saja", 3,
                          "gratis1kg")
    print()
    laundry.terima_cucian("Andi Wijaya", "087711223344", "dry clean", 2, "")
    print()
    laundry.terima_cucian("Dimas Pratama", "081355577799", "cuci setrika", 5, "")
    print()
    laundry.cetak_laporan()


if __name__ == "__main__":
    main()
```

</details>

<details>
<summary>☕ Kode awal versi Java</summary>

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class SoalC2Sebelum {

    public static void main(String[] args) {
        LaundrySerbaBisa laundry = new LaundrySerbaBisa();
        laundry.terimaCucian("Budi Santoso", "081234567890", "cuci setrika", 4, "member");
        System.out.println();
        laundry.terimaCucian("Siti Aminah", "082198765432", "cuci kering", 6, "gratis1kg");
        System.out.println();
        laundry.terimaCucian("Rina Marlina", "085312345678", "setrika saja", 3, "gratis1kg");
        System.out.println();
        laundry.terimaCucian("Andi Wijaya", "087711223344", "dry clean", 2, "");
        System.out.println();
        laundry.terimaCucian("Dimas Pratama", "081355577799", "cuci setrika", 5, "");
        System.out.println();
        laundry.cetakLaporan();
    }
}

class LaundrySerbaBisa {
    List<String[]> riwayat = new ArrayList<>(); // isi: {kode, nama, berat, total}
    int nomor = 0;

    void terimaCucian(String nama, String noHp, String layanan, int berat, String promo) {
        // cari tarif per kg
        int tarif;
        if (layanan.equals("cuci kering")) {
            tarif = 6000;
        } else if (layanan.equals("cuci setrika")) {
            tarif = 8000;
        } else if (layanan.equals("setrika saja")) {
            tarif = 5000;
        } else {
            System.out.println("[DITOLAK] Layanan '" + layanan + "' tidak tersedia");
            return;
        }
        nomor++;
        String kode = String.format("L%03d", nomor);
        int subtotal = tarif * berat;

        // hitung promo
        int potongan = 0;
        String namaPromo = "";
        if (promo.equals("member")) {
            potongan = subtotal * 10 / 100;
            namaPromo = "Member 10%";
        } else if (promo.equals("gratis1kg")) {
            if (berat >= 5) {
                potongan = tarif;
                namaPromo = "Gratis 1 kg";
            }
        }
        int total = subtotal - potongan;

        // cetak nota
        System.out.println("=".repeat(36));
        System.out.println("LAUNDRY BERSIH KILAT");
        System.out.println("=".repeat(36));
        System.out.println("No. Order : " + kode);
        System.out.println("Pelanggan : " + nama);
        System.out.println("Layanan   : " + layanan);
        String teksTarif = "Rp" + String.format(Locale.US, "%,d", tarif).replace(',', '.');
        System.out.println("Berat     : " + berat + " kg x " + teksTarif);
        System.out.println("-".repeat(36));
        String teksSubtotal = "Rp" + String.format(Locale.US, "%,d", subtotal).replace(',', '.');
        System.out.println(String.format("%-24s%12s", "Subtotal", teksSubtotal));
        if (potongan > 0) {
            String teksPotongan = "-Rp"
                    + String.format(Locale.US, "%,d", potongan).replace(',', '.');
            System.out.println(String.format("%-24s%12s", "Promo " + namaPromo, teksPotongan));
        }
        String teksTotal = "Rp" + String.format(Locale.US, "%,d", total).replace(',', '.');
        System.out.println(String.format("%-24s%12s", "TOTAL", teksTotal));
        System.out.println("=".repeat(36));

        // kirim WhatsApp
        System.out.println("[WA ke " + noHp + "] Halo " + nama + ", cucian " + kode
                + " sudah kami terima. Total " + teksTotal + ".");

        // simpan riwayat
        riwayat.add(new String[] {kode, nama, String.valueOf(berat), String.valueOf(total)});
    }

    void cetakLaporan() {
        System.out.println("=== LAPORAN HARIAN ===");
        int totalBerat = 0;
        int pendapatan = 0;
        for (String[] data : riwayat) {
            int berat = Integer.parseInt(data[2]);
            int total = Integer.parseInt(data[3]);
            String teks = "Rp" + String.format(Locale.US, "%,d", total).replace(',', '.');
            System.out.println(String.format("%s  %-16s%3d kg%12s", data[0], data[1], berat,
                    teks));
            totalBerat += berat;
            pendapatan += total;
        }
        System.out.println("Jumlah order : " + riwayat.size());
        System.out.println("Total berat  : " + totalBerat + " kg");
        System.out.println("Pendapatan   : Rp"
                + String.format(Locale.US, "%,d", pendapatan).replace(',', '.'));
    }
}
```

</details>

Kode awal ini juga tersedia sebagai file siap jalan: [`python/solusi/soal_c2_sebelum.py`](python/solusi/soal_c2_sebelum.py) dan [`java/solusi/SoalC2Sebelum.java`](java/solusi/SoalC2Sebelum.java). Jangan buka file `..._sesudah` sebelum mencoba sendiri.

**Output kode awal (harus tetap sama setelah refactor):**

```text
====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L001
Pelanggan : Budi Santoso
Layanan   : cuci setrika
Berat     : 4 kg x Rp8.000
------------------------------------
Subtotal                    Rp32.000
Promo Member 10%            -Rp3.200
TOTAL                       Rp28.800
====================================
[WA ke 081234567890] Halo Budi Santoso, cucian L001 sudah kami terima. Total Rp28.800.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L002
Pelanggan : Siti Aminah
Layanan   : cuci kering
Berat     : 6 kg x Rp6.000
------------------------------------
Subtotal                    Rp36.000
Promo Gratis 1 kg           -Rp6.000
TOTAL                       Rp30.000
====================================
[WA ke 082198765432] Halo Siti Aminah, cucian L002 sudah kami terima. Total Rp30.000.

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L003
Pelanggan : Rina Marlina
Layanan   : setrika saja
Berat     : 3 kg x Rp5.000
------------------------------------
Subtotal                    Rp15.000
TOTAL                       Rp15.000
====================================
[WA ke 085312345678] Halo Rina Marlina, cucian L003 sudah kami terima. Total Rp15.000.

[DITOLAK] Layanan 'dry clean' tidak tersedia

====================================
LAUNDRY BERSIH KILAT
====================================
No. Order : L004
Pelanggan : Dimas Pratama
Layanan   : cuci setrika
Berat     : 5 kg x Rp8.000
------------------------------------
Subtotal                    Rp40.000
TOTAL                       Rp40.000
====================================
[WA ke 081355577799] Halo Dimas Pratama, cucian L004 sudah kami terima. Total Rp40.000.

=== LAPORAN HARIAN ===
L001  Budi Santoso      4 kg    Rp28.800
L002  Siti Aminah       6 kg    Rp30.000
L003  Rina Marlina      3 kg    Rp15.000
L004  Dimas Pratama     5 kg    Rp40.000
Jumlah order : 4
Total berat  : 18 kg
Pendapatan   : Rp113.800
```

**Tugas:**

1. Tulis daftar **minimal empat** masalah desain pada kode awal beserta prinsip yang dilanggar, sebagai komentar di bagian atas file jawabanmu.
2. Refactor kode menjadi beberapa kelas yang menerapkan **minimal tiga** prinsip SOLID dan **minimal satu** *design pattern*. Tulis nama prinsip/pola di komentar kelas yang bersangkutan.
3. Output program hasil refactor harus **sama persis** dengan output di atas. Buktikan dengan perintah `diff` (macOS/Linux) atau `fc` (Windows), lalu sertakan hasilnya.
4. Pertanyaan lanjutan (jawab di komentar, tanpa mengubah output): apa saja yang perlu **ditambah** dan apa yang perlu **diubah** jika (a) ada promo baru "Pelajar 15%", dan (b) ada layanan baru "cuci bed cover" seharga Rp12.000 per kg?

<details>
<summary>💡 Petunjuk</summary>

- Tandai setiap komentar di kode awal (`# cari tarif`, `# hitung promo`, `# cetak nota`, ...). Setiap komentar seperti itu adalah calon kelas tersendiri.
- Rantai `if promo == ...` adalah kandidat kuat pola Strategy: setiap promo menjadi satu kelas yang menghitung potongannya sendiri.
- Tarif layanan bisa disimpan sebagai **data** (dict/Map nama layanan → tarif), bukan sebagai rantai `if`.
- Agar pengiriman WhatsApp mudah diganti SMS, buat abstraksi pengirim dan berikan objeknya lewat konstruktor kasir.
- Perhatikan detail kecil yang memengaruhi output: nomor order hanya bertambah jika layanan valid, dan baris promo hanya dicetak jika potongannya lebih dari 0.

</details>

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Output tetap sama persis, dibuktikan dengan `diff`/`fc` | 25% |
| SRP: perhitungan, nota, pengiriman pesan, dan laporan dipisah ke kelas yang tepat | 20% |
| OCP dan *design pattern*: promo (dan layanan) bisa ditambah tanpa mengubah kelas lain; pola dipakai dengan benar | 25% |
| DIP/ISP: kasir bergantung pada abstraksi kecil yang disuntikkan lewat konstruktor | 15% |
| Kerapian: format uang di satu tempat (DRY), nama jelas, tidak berlebihan (KISS/YAGNI), daftar masalah dan jawaban pertanyaan lanjutan | 15% |

**Solusi:** [🐍 Python](python/solusi/soal_c2_sesudah.py) · [☕ Java](java/solusi/SoalC2Sesudah.java)

---

Selesai mengerjakan semuanya? Hebat! Sekarang cocokkan jawabanmu di [Pembahasan](pembahasan.md). Jangan berkecil hati jika ada yang salah; justru dari situlah persiapanmu menjadi matang.

---

[⬅️ Informasi UAS](README.md) · [🏠 Beranda](../README.md) · [Pembahasan ➡️](pembahasan.md)
