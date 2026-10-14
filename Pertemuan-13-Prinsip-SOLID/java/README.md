# ☕ Praktik Java — Pertemuan 13: Prinsip SOLID

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 13](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [SRP: Memisahkan Hitung dan Cetak](#1-srp-memisahkan-hitung-dan-cetak)
2. [OCP: Layanan Baru Cukup Kelas Baru](#2-ocp-layanan-baru-cukup-kelas-baru)
3. [LSP: Menepati Janji Kelas Induk](#3-lsp-menepati-janji-kelas-induk)
4. [ISP: Satu Kelas, Beberapa Interface Kecil](#4-isp-satu-kelas-beberapa-interface-kecil)
5. [DIP: Menyuntikkan Dependensi lewat Konstruktor](#5-dip-menyuntikkan-dependensi-lewat-konstruktor)
6. [Refactoring Aman: Bandingkan Hasil Lama dan Baru](#6-refactoring-aman-bandingkan-hasil-lama-dan-baru)
7. [Studi Kasus KedaiKita](#7-studi-kasus-kedaikita)
8. [Kesalahan Umum dan Cara Membaca Pesan Error](#8-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/              <- 6 program satu file: satu per prinsip, ditambah refactoring
├── studi-kasus/
│   ├── sebelum/         <- KasirSerbaBisa.java (program satu file)
│   └── sesudah/         <- KedaiKita hasil refactoring (satu kelas per file)
└── solusi/              <- solusi latihan (buka setelah mencoba sendiri!)
```

Contoh dan versi `sebelum` adalah program satu file. Versi `sesudah` terdiri atas banyak file, jadi kompilasi semuanya dulu, lalu jalankan kelas `Main`:

```bash
cd Pertemuan-13-Prinsip-SOLID/java/contoh
java Contoh01Srp.java

cd ../studi-kasus/sebelum
java KasirSerbaBisa.java

cd ../sesudah
javac *.java
java Main
```

> [!TIP]
> Di VS Code, buka folder `java/` **milik pertemuan ini** saja (File → Open Folder). Nama kelas di dalam satu folder harus unik, sehingga kelas-kelas di `contoh/` dan `solusi/` sengaja diberi nama yang berbeda dari kelas studi kasus. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

Setiap file contoh berisi **dua desain** yang dipisahkan baris komentar `MELANGGAR` dan `SESUAI`. Baca bagian yang melanggar lebih dulu dan cari *code smell*-nya, baru bandingkan dengan perbaikannya.

## 1. SRP: Memisahkan Hitung dan Cetak

File: [`contoh/Contoh01Srp.java`](contoh/Contoh01Srp.java)

Desain yang **melanggar** SRP: method `cetakLaporan()` milik `LaporanSerbaBisa` menghitung rata-rata, menentukan predikat, dan mencetak sekaligus.

```java
    public void cetakLaporan() {
        System.out.println("LAPORAN NILAI KELAS PBO");
        for (Map.Entry<String, List<Integer>> entri : dataNilai.entrySet()) {
            int jumlah = 0;
            for (int nilai : entri.getValue()) {
                jumlah += nilai;
            }
            int rata = jumlah / entri.getValue().size(); // [1] aturan hitung...
            String predikat;
            if (rata >= 80) {
                predikat = "A";
            } else if (rata >= 70) {
                predikat = "B";
            } else if (rata >= 60) {
                predikat = "C";
            } else {
                predikat = "D";
            }
            System.out.println(String.format("  %-8s%4s  %s",
                    entri.getKey(), rata, predikat)); // [2] ...bercampur format
        }
    }
```

Desain yang **sesuai** SRP: dua kelas, masing-masing satu urusan.

```java
/** Hanya menghitung. Tidak pernah mencetak apa pun. */
class PenghitungNilai {

    public int rataRata(List<Integer> daftar) {
        int jumlah = 0;
        for (int nilai : daftar) {
            jumlah += nilai;
        }
        return jumlah / daftar.size();
    }

    public String predikat(int rata) { // [3] satu-satunya tempat aturan predikat
        if (rata >= 80) {
            return "A";
        }
        if (rata >= 70) {
            return "B";
        }
        if (rata >= 60) {
            return "C";
        }
        return "D";
    }
}

/** Hanya menyusun dan mencetak laporan. */
class PencetakLaporan {
    private PenghitungNilai penghitung;

    public PencetakLaporan(PenghitungNilai penghitung) {
        this.penghitung = penghitung; // [4] hitungan diminta dari ahlinya
    }
```

Method `cetak(dataNilai)` milik `PencetakLaporan` mencetak judul, lalu untuk setiap mahasiswa memanggil `penghitung.rataRata(...)` dan `penghitung.predikat(rata)` sebelum mencetak barisnya dengan format yang sama. Di `main`, data nilai disimpan di `LinkedHashMap` agar urutannya tetap (Pertemuan 12), lalu kedua desain mencetak laporan. Bagian terakhirnya memakai ulang hasil hitungan:

```java
        System.out.println("=== BONUS SRP: HITUNGAN DIPAKAI ULANG ===");
        for (Map.Entry<String, List<Integer>> entri : dataNilai.entrySet()) {
            int rata = penghitung.rataRata(entri.getValue()); // [5] tanpa ikut mencetak laporan
            if (penghitung.predikat(rata).equals("D")) {
                System.out.println(entri.getKey() + " perlu remedial (rata-rata " + rata + ")");
            }
        }
```

**Output:**

```text
=== VERSI MELANGGAR SRP ===
LAPORAN NILAI KELAS PBO
  Ayu       84  A
  Bima      71  B
  Citra     57  D

=== VERSI SESUAI SRP ===
LAPORAN NILAI KELAS PBO
  Ayu       84  A
  Bima      71  B
  Citra     57  D

=== BONUS SRP: HITUNGAN DIPAKAI ULANG ===
Citra perlu remedial (rata-rata 57)
```

Penjelasan:

- **[1]** dan **[2]** Aturan hitung dan format cetak bercampur di satu method. Hasil hitungan hanya hidup di dalam perulangan, lalu hilang setelah dicetak. Format `%4s` dipakai untuk angka agar hasilnya tidak terpengaruh pengaturan bahasa (*locale*) komputer.
- **[3]** Aturan predikat kini hanya tertulis di **satu tempat**. Method-nya **mengembalikan** nilai, bukan mencetak.
- **[4]** `PencetakLaporan` tidak menghitung sendiri. Ia menerima objek `PenghitungNilai` lewat konstruktor dan meminta hasil hitungan darinya.
- **[5]** Daftar remedial dibuat tanpa ikut mencetak seluruh laporan. Dengan `LaporanSerbaBisa`, kita terpaksa **menyalin** rumus rata-rata dan predikat. Itu awal dari kode kembar.

> [!TIP]
> **Coba sendiri:** naikkan batas predikat A menjadi 85 di `PenghitungNilai.predikat()`. Hanya satu baris yang berubah, tetapi laporan **dan** daftar remedial langsung mengikuti. Pada versi sesuai SRP, Ayu (rata-rata 84) kini mendapat B.

## 2. OCP: Layanan Baru Cukup Kelas Baru

File: [`contoh/Contoh02Ocp.java`](contoh/Contoh02Ocp.java)

Desain yang **melanggar** OCP: rumus dipilih dengan rantai `if`/`else if`.

```java
/** Setiap layanan baru memaksa method hitung() dibongkar. */
class KalkulatorOngkirKaku {

    public int hitung(String layanan, int beratKg) {
        if (layanan.equals("reguler")) {
            return 9000 * beratKg;
        } else if (layanan.equals("kilat")) {
            return 15000 * beratKg;
        }
        return 0; // [1] layanan lain belum dikenal: diam-diam dianggap gratis!
    }
}
```

Desain yang **sesuai** OCP diawali *interface* `LayananKirim` dengan dua method: `String nama()` dan `int ongkir(int beratKg)`. `LayananReguler` dan `LayananKilat` meng-*implements* kontrak itu dengan rumus masing-masing. Lalu datang layanan baru:

```java
class LayananSameDay implements LayananKirim { // [2] layanan BARU = kelas baru, kode lama aman
    @Override
    public String nama() {
        return "Same Day";
    }

    @Override
    public int ongkir(int beratKg) {
        return 25000 + 5000 * beratKg;
    }
}

/** Tidak pernah menyebut nama layanan apa pun, jadi tidak perlu diubah. */
class KalkulatorOngkir {

    public int hitung(LayananKirim layanan, int beratKg) {
        if (beratKg < 1) { // aturan umum: berat dihitung minimal 1 kg
            beratKg = 1;
        }
        return layanan.ongkir(beratKg); // [3] polimorfisme bekerja di sini
    }
}
```

**Output:**

```text
=== VERSI MELANGGAR OCP (rantai percabangan) ===
reguler  3 kg: Rp27.000
kilat    3 kg: Rp45.000
sameday  3 kg: Rp0
Layanan baru dianggap gratis! Method hitung() harus dibongkar dulu.

=== VERSI SESUAI OCP (satu kelas per layanan) ===
Reguler  3 kg: Rp27.000
Kilat    3 kg: Rp45.000
Same Day 3 kg: Rp40.000
Layanan Same Day cukup ditambahkan sebagai kelas baru.
```

Penjelasan:

- **[1]** Selain kaku, rantai percabangan juga rawan *bug* diam-diam. Layanan yang belum terdaftar tidak memicu error, tetapi malah dianggap gratis.
- **[2]** Menambah layanan berarti **menulis kelas baru**. `LayananReguler`, `LayananKilat`, dan `KalkulatorOngkir` tidak disentuh.
- **[3]** `KalkulatorOngkir` hanya mengenal tipe `LayananKirim`. Java memanggil `ongkir()` milik objek yang sebenarnya (polimorfisme, Pertemuan 09).

> [!TIP]
> **Coba sendiri:** tambahkan kelas `LayananHemat implements LayananKirim` dengan tarif Rp6.000 per kg, lalu tambahkan `new LayananHemat()` ke `daftarLayanan` di `main`. Kelas apa saja yang perlu kamu ubah? Baris apa yang muncul di output?

<details>
<summary>Lihat jawaban</summary>

Tidak ada kelas lama yang diubah. Kamu hanya menulis satu kelas baru dan menambah satu objek ke `List.of(...)`. Baris barunya: `Hemat    3 kg: Rp18.000`.

</details>

## 3. LSP: Menepati Janji Kelas Induk

File: [`contoh/Contoh03Lsp.java`](contoh/Contoh03Lsp.java)

Desain yang **melanggar** LSP: kelas `Burung` menyimpan `nama` dan berjanji bisa terbang lewat `terbang()`, yang mengembalikan teks "... terbang tinggi". Lalu `Penguin` mengingkarinya:

```java
class Penguin extends Burung {
    public Penguin(String nama) {
        super(nama);
    }

    @Override
    public String terbang() { // [1] meng-override hanya untuk menolak
        throw new UnsupportedOperationException(getNama() + " tidak bisa terbang");
    }
}
```

Method `lepasKeUdara(List<Burung> daftar)` di kelas utama percaya pada janji `Burung`: ia memanggil `terbang()` untuk setiap burung. Namun, ia terpaksa membungkus panggilan itu dengan `try`/`catch (UnsupportedOperationException e)` (ditandai `// [2]` di file) dan mencetak `[KEJUTAN]` jika janji diingkari.

Desain yang **sesuai** LSP: `BurungDasar` hanya berisi `nama` dan `bertelur()`, yaitu janji yang ditepati semua burung. Janji terbang dipindah ke kelas anak khusus.

```java
/** Janji tambahan: burung jenis ini benar-benar bisa terbang. */
class BurungTerbang extends BurungDasar {
    public BurungTerbang(String nama) {
        super(nama);
    }

    public String terbang() {
        return getNama() + " terbang tinggi";
    }
}

class PenguinKutub extends BurungDasar { // [3] tidak mewarisi janji terbang
    public PenguinKutub(String nama) {
        super(nama);
    }

    public String berenang() {
        return getNama() + " berenang di air dingin";
    }
}
```

Di `main`, setiap list diberi tipe sesuai janji yang dibutuhkan:

```java
        System.out.println("Janji BurungDasar: bisa bertelur");
        List<BurungDasar> semuaBurung = List.of(merpati, elang, penguin); // [4]
        for (BurungDasar burung : semuaBurung) {
            System.out.println("  " + burung.bertelur());
        }

        System.out.println("Janji BurungTerbang: bisa terbang");
        List<BurungTerbang> penerbang = List.of(merpati, elang); // [5]
        for (BurungTerbang burung : penerbang) {
            System.out.println("  " + burung.terbang());
        }
```

**Output:**

```text
=== VERSI MELANGGAR LSP ===
Melepas semua Burung ke udara:
  Merpati terbang tinggi
  Elang terbang tinggi
  [KEJUTAN] Penguin tidak bisa terbang

=== VERSI SESUAI LSP ===
Janji BurungDasar: bisa bertelur
  Merpati bertelur
  Elang bertelur
  Penguin bertelur
Janji BurungTerbang: bisa terbang
  Merpati terbang tinggi
  Elang terbang tinggi
Kemampuan khusus penguin:
  Penguin berenang di air dingin
Tidak ada kejutan: setiap kelas anak menepati janji induknya.
```

Penjelasan:

- **[1]** `Penguin` meng-*override* `terbang()` hanya untuk melempar `UnsupportedOperationException`. Compiler tidak keberatan, tetapi janji kelas induk diingkari.
- **[2]** Akibatnya, pemanggil terpaksa memasang `try`/`catch` untuk *exception* yang tidak pernah dijanjikan `Burung`.
- **[3]** `PenguinKutub` tidak pernah berjanji bisa terbang, jadi ia tidak perlu mengingkari apa pun.
- **[4]** Ketiga burung boleh masuk ke `List<BurungDasar>`, karena semuanya menepati janji bertelur.
- **[5]** Hanya burung yang benar-benar bisa terbang yang boleh masuk ke `List<BurungTerbang>`.

> [!TIP]
> **Coba sendiri:** tambahkan `penguin` ke `List.of(merpati, elang)` pada baris **[5]**. Kali ini compiler Java langsung menolak sebelum program berjalan, dengan pesan `incompatible types: inference variable E has incompatible bounds`, disertai keterangan bahwa `PenguinKutub` bukan `BurungTerbang`. Desain yang jujur membuat kesalahan seperti ini tertangkap lebih awal.

## 4. ISP: Satu Kelas, Beberapa Interface Kecil

File: [`contoh/Contoh04Isp.java`](contoh/Contoh04Isp.java)

Desain yang **melanggar** ISP memakai *interface* gemuk `PerangkatKasir` berisi `cetakStruk()`, `pindaiBarcode()`, dan `bukaLaci()`. Printer bluetooth yang hanya bisa mencetak dipaksa meng-*implements* semuanya:

```java
class PrinterBluetooth implements PerangkatKasir {
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Printer Bluetooth] mencetak: " + teks);
    }

    @Override
    public String pindaiBarcode() { // [1] method palsu: dipaksa ada
        throw new UnsupportedOperationException("Printer Bluetooth tidak punya pemindai barcode");
    }

    @Override
    public void bukaLaci() { // method palsu kedua
        throw new UnsupportedOperationException("Printer Bluetooth tidak punya laci uang");
    }
}
```

Desain yang **sesuai** ISP memecahnya menjadi tiga *interface* kecil:

```java
/** Kontrak kecil: bisa mencetak struk. */
interface PencetakStruk { // [2] tiga kontrak kecil, masing-masing satu kemampuan
    void cetakStruk(String teks);
}

/** Kontrak kecil: bisa memindai barcode. */
interface PemindaiBarcode {
    String pindaiBarcode();
}

/** Kontrak kecil: punya laci uang. */
interface LaciUang {
    void bukaLaci();
}

class KasirLengkap implements PencetakStruk, PemindaiBarcode, LaciUang { // [3]
```

Isi `KasirLengkap` sama dengan `MesinKasirLengkap` pada versi lama. Perangkat yang lebih sederhana cukup meng-*implements* satu *interface*:

```java
class PrinterThermal implements PencetakStruk { // [4] cukup satu kontrak, tanpa method palsu
    @Override
    public void cetakStruk(String teks) {
        System.out.println("[Printer Thermal] mencetak: " + teks);
    }
}
```

Di `main`, perangkat dikelompokkan menurut kemampuan yang dibutuhkan:

```java
        KasirLengkap kasir = new KasirLengkap();
        List<PencetakStruk> pencetak = List.of(kasir, new PrinterThermal()); // [5]
        List<PemindaiBarcode> pemindai = List.of(kasir, new PemindaiGenggam());
```

**Output:**

```text
=== VERSI MELANGGAR ISP (interface gemuk) ===
[Mesin Kasir] mencetak: Terima kasih!
Hasil pindai: 8991234567890
[Printer Bluetooth] mencetak: Terima kasih!
[KEJUTAN] Printer Bluetooth tidak punya pemindai barcode

=== VERSI SESUAI ISP (interface kecil) ===
-- semua PencetakStruk --
[Mesin Kasir] mencetak: Terima kasih!
[Printer Thermal] mencetak: Terima kasih!
-- semua PemindaiBarcode --
Hasil pindai: 8991234567890
Hasil pindai: 8997654321098
Setiap perangkat hanya berjanji sebanyak kemampuannya.
```

Penjelasan:

- **[1]** Dua method palsu ini ada hanya karena *interface*-nya memaksa. Selain melanggar ISP, keduanya juga melanggar LSP: pemanggil `PerangkatKasir` mendapat *exception* yang tidak dijanjikan.
- **[2]** Setiap *interface* kecil hanya berisi satu kemampuan.
- **[3]** Sebuah kelas Java hanya boleh meng-*extends* **satu** kelas, tetapi boleh meng-*implements* **banyak** *interface* (Pertemuan 10). Inilah cara memenuhi beberapa kontrak kecil sekaligus.
- **[4]** `PrinterThermal` cukup memenuhi satu kontrak. Tidak ada lagi method yang hanya berisi penolakan.
- **[5]** Objek `kasir` yang sama boleh masuk ke `List<PencetakStruk>` maupun `List<PemindaiBarcode>`, karena ia meng-*implements* keduanya.

## 5. DIP: Menyuntikkan Dependensi lewat Konstruktor

File: [`contoh/Contoh05Dip.java`](contoh/Contoh05Dip.java)

Desain yang **melanggar** DIP: kelas pengingat menciptakan sendiri alat kirimnya.

```java
class PengingatKaku {
    private SmsGateway sms;

    public PengingatKaku() {
        this.sms = new SmsGateway(); // [1] membuat sendiri kelas konkret: terkunci
    }
```

Method `ingatkan(nomor, matkul, jam)` lalu memanggil `sms.kirimSms(...)`. Desain yang **sesuai** DIP diawali *interface* `Pengirim` yang hanya berisi `void kirim(String tujuan, String pesan)`. `PengirimSms` dan `PengirimWhatsApp` meng-*implements*-nya dan mencetak pesan. Ada juga `PengirimTiruan` untuk pengujian: method `kirim()` miliknya tidak mencetak apa pun, hanya menambahkan `"tujuan: pesan"` ke sebuah list yang bisa dibaca lewat `getCatatan()`. Lalu kelas pengingat yang hanya mengenal abstraksi:

```java
class PengingatJadwal {
    private Pengirim pengirim; // [3] tipenya abstraksi, bukan kelas konkret

    public PengingatJadwal(Pengirim pengirim) { // [2] disuntikkan dari luar
        this.pengirim = pengirim;
    }

    public void ingatkan(String nomor, String matkul, String jam) {
        pengirim.kirim(nomor, "Besok kuliah " + matkul + " jam " + jam);
    }
}
```

Potongan `main`:

```java
        System.out.println("Disuntik PengirimSms:");
        new PengingatJadwal(new PengirimSms()).ingatkan("081234567890", "PBO", "08.00"); // [4]
        System.out.println("Disuntik PengirimWhatsApp:");
        new PengingatJadwal(new PengirimWhatsApp()).ingatkan("081234567890", "PBO", "08.00");

        System.out.println("Disuntik PengirimTiruan (untuk pengujian):");
        PengirimTiruan tiruan = new PengirimTiruan();
        PengingatJadwal pengingat = new PengingatJadwal(tiruan);
        pengingat.ingatkan("081234567890", "PBO", "08.00");
        pengingat.ingatkan("082198765432", "Basis Data", "10.00");
        List<String> catatan = tiruan.getCatatan(); // [5] memeriksa hasil tanpa mengirim pesan sungguhan
```

**Output:**

```text
=== VERSI MELANGGAR DIP ===
  [SMS ke 081234567890] Besok kuliah PBO jam 08.00
Mau pindah ke WhatsApp? Kelas PengingatKaku harus dibongkar.

=== VERSI SESUAI DIP ===
Disuntik PengirimSms:
  [SMS ke 081234567890] Besok kuliah PBO jam 08.00
Disuntik PengirimWhatsApp:
  [WA ke 081234567890] Besok kuliah PBO jam 08.00
Disuntik PengirimTiruan (untuk pengujian):
  Pesan tercatat: 2
  Pesan kedua   : 082198765432: Besok kuliah Basis Data jam 10.00
  Sesuai harapan? ya
```

Penjelasan:

- **[1]** `new SmsGateway()` di dalam konstruktor mengunci `PengingatKaku` pada SMS. Untuk pindah ke WhatsApp, atau sekadar menguji tanpa mengirim SMS sungguhan, kelas ini harus dibongkar.
- **[2]** Objek pengirim kini **diterima** lewat parameter konstruktor. Inilah *dependency injection*.
- **[3]** Tipe field-nya adalah *interface* `Pengirim`, sehingga objek dari kelas apa pun yang meng-*implements* `Pengirim` bisa disuntikkan.
- **[4]** Kelas `PengingatJadwal` yang **sama** dipakai dengan pengirim berbeda. Pilihan pengirim dibuat di `main`, tempat merakit program.
- **[5]** `PengirimTiruan` mencatat pesan alih-alih mengirimnya, sehingga hasilnya bisa diperiksa tanpa menghabiskan pulsa. Teknik ini sangat berguna saat pengujian otomatis (Pertemuan 15).

## 6. Refactoring Aman: Bandingkan Hasil Lama dan Baru

File: [`contoh/Contoh06RefactorAman.java`](contoh/Contoh06RefactorAman.java)

Kelas `DendaLama` menghitung denda keterlambatan perpustakaan. Hasilnya benar, tetapi rumus yang sama ditulis tiga kali (melanggar DRY):

```java
class DendaLama {

    public int hitung(String jenis, int hariTerlambat) {
        if (jenis.equals("buku")) {
            if (hariTerlambat <= 0) {
                return 0;
            }
            int denda = hariTerlambat * 1000;
            if (denda > 20000) {
                denda = 20000;
            }
            return denda;
        } else if (jenis.equals("majalah")) { // [1] pola yang sama ditulis ulang...
```

Cabang `majalah` (Rp500 per hari, maksimal Rp10.000) dan `referensi` (Rp5.000 per hari, maksimal Rp50.000) ditulis dengan pola yang persis sama, lalu jenis lain menghasilkan 0. Hasil *refactoring*-nya:

```java
/** Satu rumus denda untuk semua jenis pustaka. */
class AturanDenda {
    private int tarifPerHari;
    private int dendaMaksimal;

    public AturanDenda(int tarifPerHari, int dendaMaksimal) {
        this.tarifPerHari = tarifPerHari;
        this.dendaMaksimal = dendaMaksimal;
    }

    public int hitung(int hariTerlambat) { // [2] rumus ditulis SEKALI
        if (hariTerlambat <= 0) {
            return 0;
        }
        return Math.min(hariTerlambat * tarifPerHari, dendaMaksimal);
    }
}

class DendaBaru {
    private Map<String, AturanDenda> aturan = new LinkedHashMap<>();

    public DendaBaru() {
        aturan.put("buku", new AturanDenda(1000, 20000)); // [3] jenis baru cukup ditambah satu baris
        aturan.put("majalah", new AturanDenda(500, 10000));
        aturan.put("referensi", new AturanDenda(5000, 50000));
    }

    public int hitung(String jenis, int hariTerlambat) {
        if (!aturan.containsKey(jenis)) {
            return 0; // [4] perilaku lama dipertahankan, termasuk yang ini
        }
        return aturan.get(jenis).hitung(hariTerlambat);
    }
}
```

Bagaimana kita **tahu** keduanya berperilaku sama? `main` menyiapkan dua list kasus uji, `jenisKasus` dan `hariKasus` (ditandai `// [5]` di file). Lalu kedua versi dijalankan dan hasilnya dibandingkan:

```java
        for (int i = 0; i < jenisKasus.size(); i++) {
            String jenis = jenisKasus.get(i);
            int hari = hariKasus.get(i);
            int hasilLama = lama.hitung(jenis, hari);
            int hasilBaru = baru.hitung(jenis, hari);
            String status;
            if (hasilLama == hasilBaru) { // [6] bukti: hasil harus sama persis
                jumlahSama++;
                status = "sama";
            } else {
                status = "BEDA";
            }
```

**Output:**

```text
=== MEMBANDINGKAN SEBELUM DAN SESUDAH REFACTOR ===
jenis     hari      lama      baru   hasil
buku         0       Rp0       Rp0   sama
buku         3   Rp3.000   Rp3.000   sama
buku        25  Rp20.000  Rp20.000   sama
majalah      4   Rp2.000   Rp2.000   sama
majalah     30  Rp10.000  Rp10.000   sama
referensi    2  Rp10.000  Rp10.000   sama
referensi   12  Rp50.000  Rp50.000   sama
komik        5       Rp0       Rp0   sama
Kasus diuji: 8, sama: 8, beda: 0
Kesimpulan: refactor aman, perilaku tidak berubah.
```

Penjelasan:

- **[1]** Tiga cabang dengan pola identik, hanya angkanya yang berbeda. Jika aturan "denda maksimal" berubah, tiga tempat harus diubah.
- **[2]** Rumusnya kini tertulis sekali. `Math.min()` mengambil nilai terkecil, sehingga denda tidak melewati batas maksimal.
- **[3]** Perbedaan antarjenis disimpan sebagai **data** di `Map`, bukan sebagai cabang `if`.
- **[4]** Jenis yang tidak dikenal (misalnya "komik") tetap menghasilkan 0, persis seperti versi lama. *Refactoring* mempertahankan **semua** perilaku, termasuk yang mungkin terasa janggal.
- **[5]** Kasus uji sengaja mencakup nilai tepi: terlambat 0 hari, denda yang menyentuh batas maksimal, dan jenis yang tidak dikenal.
- **[6]** Setiap pasang hasil dibandingkan. Karena keduanya `int`, operator `==` membandingkan nilainya secara langsung.

## 7. Studi Kasus KedaiKita

Folder: [`studi-kasus/sebelum/`](studi-kasus/sebelum/KasirSerbaBisa.java) dan [`studi-kasus/sesudah/`](studi-kasus/sesudah/Main.java)

Rancangan dan pemetaan tugasnya sudah dibahas di [halaman konsep](../README.md#12-studi-kasus-kedaikita-membongkar-kasirserbabisa). Di sini kita membedah kodenya.

**Apa yang berubah dibanding Pertemuan 12?**

- File **baru**: `Diskon.java` (*interface*), `TanpaDiskon.java`, `DiskonPersen.java`, `DiskonMember.java`, `StrukPesanan.java`, `PenyimpananPesanan.java` (*interface*), dan `PenyimpananMemori.java`.
- File **berubah**: `Pesanan.java` (tidak lagi mencetak, mendapat `aturDiskon()` dan `hitungPotongan()`), `Kedai.java` (menerima penyimpanan lewat konstruktor), `LaporanPenjualan.java` (judul bagian menjadi "Penjualan per kategori (sebelum diskon)"), dan `Main.java` (skenario yang sama dengan `sebelum/`).
- File lainnya, termasuk `ItemPesanan.java`, sama dengan Pertemuan 12.

### Sebelum: `KasirSerbaBisa.java`

Seluruh pekerjaan ada di satu method `prosesPesanan()`. Komentar "Tugas 1" sampai "Tugas 4" di dalam file menandai urusan-urusan yang bercampur. Setelah membuat nomor pesanan dan menghitung subtotal, bagian diskonnya berbunyi:

```java
        // Tugas 2 (lanjutan): diskon memakai rantai if/else if.
        // Setiap ada jenis promo baru, method ini HARUS dibongkar (melanggar OCP).
        int potongan;
        String keterangan;
        if (jenisDiskon.equals("member")) {
            if (poinPelanggan >= 10) {
                potongan = subtotal * 10 / 100;
                keterangan = "Member 10%";
            } else {
                potongan = 0;
                keterangan = "Member (poin belum cukup)";
            }
        } else if (jenisDiskon.equals("promo")) {
            potongan = subtotal * 15 / 100;
            keterangan = "Promo 15%";
        } else {
            potongan = 0;
            keterangan = "Tanpa diskon";
        }
        int total = subtotal - potongan;
```

Setelah itu, method yang sama masih mencetak belasan baris struk (Tugas 3) dan menambah riwayat ke list (Tugas 4). Data pelanggan dikirim sebagai nilai lepas (`namaPelanggan`, `poinPelanggan`), dan jenis diskon berupa teks seperti `"member"`. Salah ketik `"membr"` tidak memicu error, tetapi diam-diam dianggap tanpa diskon.

Di bagian bawah file ada tiga kelas kecil, `DataMenu`, `ItemBeli`, dan `CatatanRiwayat`, yang ditulis **di dalam** kelas `KasirSerbaBisa` dengan kata kunci `private static class`. Kelas seperti ini disebut kelas bersarang (*nested class*). Karena `private`, ketiganya hanya bisa dipakai di dalam file itu.

### `Diskon.java`: interface dengan method `static` (OCP dan LSP)

```java
/** Kontrak semua aturan diskon. */
public interface Diskon {

    /** Besar potongan dalam rupiah (tidak pernah negatif). */
    int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan);

    /** Nama singkat diskon untuk ditampilkan di struk. */
    String keterangan();

    /** Method static milik interface: jumlah subtotal semua item. */
    static int subtotalDari(List<ItemPesanan> daftarItem) {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }
}
```

- **Dua method abstrak** adalah isi kontraknya. Komentar "tidak pernah negatif" adalah **janji** yang wajib ditepati semua kelas yang meng-*implements* `Diskon` (LSP).
- **`subtotalDari()`** adalah method `static` milik *interface*, fitur Java 8 yang sudah disinggung di Pertemuan 10. Method ini dipanggil lewat nama *interface*-nya: `Diskon.subtotalDari(...)`. Dengan begitu, rumus subtotal tidak disalin ke setiap kelas diskon (DRY).

Cabang-cabang `if` di versi lama kini menjadi tiga kelas yang meng-*implements* `Diskon`. Contohnya `DiskonMember`: konstanta `PERSEN` dan `MINIMAL_POIN` bernilai 10, `hitungPotongan()` mengembalikan 0 jika `pelanggan.getPoin() < MINIMAL_POIN`, dan selain itu `Diskon.subtotalDari(daftarItem) * PERSEN / 100`. Method `keterangan()`-nya mengembalikan `"Member 10%"`. `TanpaDiskon` selalu mengembalikan 0. `DiskonPersen(persen)` menolak persen di luar 1 sampai 100 dengan `IllegalArgumentException`, sehingga potongannya tidak pernah melebihi subtotal.

> [!NOTE]
> Versi lama punya keterangan "Member (poin belum cukup)", tetapi teks itu **tidak pernah tercetak**, karena baris diskon hanya muncul jika potongan lebih dari nol. Karena itu `DiskonMember` boleh membuangnya tanpa mengubah perilaku. Saat *refactoring*, yang dijaga adalah perilaku yang **terlihat**, bukan setiap baris kode lama.

### `Pesanan.java` dan `StrukPesanan.java`: memisahkan hitung dan cetak (SRP)

Konstruktor `Pesanan` kini mengisi field baru `this.diskon = new TanpaDiskon();`, sehingga pesanan tanpa diskon tetap punya objek diskon yang sah. Method `aturDiskon(diskon)` menggantinya, kecuali pesanan sudah LUNAS (melempar `KedaiException`, seperti `tambahItem()`). Perhitungannya:

```java
    public int hitungPotongan() {
        return diskon.hitungPotongan(new ArrayList<>(daftarItem), pelanggan);
    }

    public int hitungTotal() {
        return hitungSubtotal() - hitungPotongan();
    }
```

`hitungPotongan()` tidak tahu diskon jenis apa yang sedang dipakai. Ia hanya meminta objek diskonnya menghitung. Itulah sebabnya promo baru tidak pernah mengubah kelas `Pesanan`.

Method `cetak()` sudah tidak ada di `Pesanan`. Tugas itu pindah ke `StrukPesanan`, yang hanya **membaca** data pesanan. Method `buatTeks()` mengumpulkan baris-baris struk di `List<String> baris`. Bagian akhirnya:

```java
        int potongan = p.hitungPotongan();
        if (potongan > 0) {
            baris.add(barisRapi("Diskon " + p.getDiskon().keterangan(),
                    "-" + Rupiah.format(potongan)));
        }
        baris.add(barisRapi("TOTAL", Rupiah.format(p.hitungTotal())));
        baris.add(garis);
        return String.join("\n", baris);
    }

    @Override
    public void cetak() {
        System.out.println(buatTeks());
    }
```

`buatTeks()` **mengembalikan** teks struk sebagai `String` yang barisnya disambung dengan `"\n"`. `cetak()` tinggal mencetaknya. Teks yang sama kelak bisa disimpan ke file atau dikirim lewat pesan tanpa mengubah cara menyusunnya. `StrukPesanan` meng-*implements* `DapatDicetak` dari Pertemuan 10.

### `PenyimpananPesanan.java` dan `Kedai.java`: menyuntikkan penyimpanan (DIP dan ISP)

```java
/** Kontrak penyimpanan pesanan. */
public interface PenyimpananPesanan {

    /** Menyimpan satu pesanan. */
    void simpan(Pesanan pesanan);

    /** Semua pesanan yang tersimpan, urut sesuai waktu disimpan. */
    List<Pesanan> semua();

    /**
     * Method default: sudah punya isi, jadi kelas yang meng-implements
     * interface ini tidak wajib menulisnya ulang.
     */
    default int jumlah() {
        return semua().size();
    }
}
```

Kontraknya kecil (ISP): kelas yang meng-*implements*-nya hanya **wajib** menulis `simpan()` dan `semua()`. Method `default` `jumlah()` sudah berisi (Pertemuan 10), sehingga `PenyimpananMemori` cukup menyimpan pesanan di sebuah `ArrayList` dan mengembalikan salinannya dari `semua()`.

Konstruktor `Kedai` menerima penyimpanan dari luar (sudah kita lihat di halaman konsep). Salah satu method yang memakainya:

```java
    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = new Pesanan(pelanggan);
        penyimpanan.simpan(pesanan);
        return pesanan;
    }
```

Dengan pola yang sama, `riwayatPesanan()` mengembalikan `penyimpanan.semua()` dan `jumlahPesanan()` mengembalikan `penyimpanan.jumlah()`. Tidak satu pun baris di `Kedai` menyebut `PenyimpananMemori` atau `ArrayList` untuk pesanan. `Kedai` hanya tahu bahwa penyimpanannya bisa `simpan()`, `semua()`, dan `jumlah()`.

### `Main.java`: tempat merakit

```java
    // Meneruskan KedaiException (throws) ke pemanggil: di skenario ini semua
    // kode menu terdaftar dan stoknya cukup, jadi tidak ada yang perlu ditangani.
    public static void prosesPesanan(Kedai kedai, Pelanggan pelanggan,
            List<Pasangan<String, Integer>> daftarBeli, Diskon diskon) throws KedaiException {
        Pesanan pesanan = kedai.buatPesanan(pelanggan);
        for (Pasangan<String, Integer> beli : daftarBeli) {
            pesanan.tambahItem(kedai.cariMenu(beli.getPertama()), beli.getKedua());
        }
        pesanan.aturDiskon(diskon);
        new StrukPesanan(pesanan).cetak();
    }

    // main ikut meneruskan KedaiException dari prosesPesanan() (alasannya sama).
    public static void main(String[] args) throws KedaiException {
        // DIP: jenis penyimpanan ditentukan DI SINI, bukan di dalam Kedai.
        PenyimpananPesanan penyimpanan = new PenyimpananMemori();
        Kedai kedai = siapkanKedai(penyimpanan);
```

Perhatikan tipe variabel `penyimpanan`: *interface* di kiri, wujud di kanan, persis kebiasaan `List<Menu> daftar = new ArrayList<>()` dari Pertemuan 12. Setelah menyiapkan Budi, Siti (`siti.tambahPoin(12)`), dan Rina, program memanggil `prosesPesanan()` tiga kali, masing-masing dengan `new TanpaDiskon()`, `new DiskonMember()`, dan `new DiskonPersen(15)`. Diskon kini berupa **objek**, sehingga salah ketik nama kelas langsung ditolak compiler.

Jalankan `javac *.java` lalu `java Main` dari dalam folder `sesudah`. Program mencetak tiga struk. Struk Budi (P001) tidak punya baris Diskon karena potongannya nol, sedangkan struk Siti (P002) sudah kamu lihat di halaman konsep. Bagian akhirnya:

**Output:**

```text
========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P003
Pelanggan   : Rina Marlina
Status      : BARU
----------------------------------------
1 x Kopi Susu Gula Aren         Rp18.000
1 x Mie Goreng Jawa             Rp23.000
----------------------------------------
Subtotal                        Rp41.000
Diskon Promo 15%                -Rp6.150
TOTAL                           Rp34.850
========================================

=== RIWAYAT PESANAN ===
P001  Budi Santoso            Rp61.000
P002  Siti Aminah             Rp27.900
P003  Rina Marlina            Rp34.850
Total pendapatan: Rp123.750
```

Potongan Rina adalah 15% x 41.000 = 6.150. Menjalankan `java KasirSerbaBisa.java` di folder `sebelum` menghasilkan output yang persis sama, bahkan sama dengan versi Python.

### Membuktikan Output Sama dengan `fc` dan `diff`

"Persis sama" jangan dibuktikan dengan mata. Simpan output kedua versi ke file memakai tanda `>`, lalu bandingkan. Mulailah dari folder `java/studi-kasus`.

Di **Windows** (Command Prompt):

```bash
cd sebelum
java KasirSerbaBisa.java > ..\hasil_sebelum.txt
cd ..\sesudah
javac *.java
java Main > ..\hasil_sesudah.txt
cd ..
fc hasil_sebelum.txt hasil_sesudah.txt
```

Jika kedua file sama, hasilnya:

```text
Comparing files hasil_sebelum.txt and HASIL_SESUDAH.TXT
FC: no differences encountered
```

Di **macOS/Linux**:

```bash
cd sebelum
java KasirSerbaBisa.java > ../hasil_sebelum.txt
cd ../sesudah
javac *.java
java Main > ../hasil_sesudah.txt
cd ..
diff hasil_sebelum.txt hasil_sesudah.txt
```

`diff` **tidak mencetak apa pun** jika kedua file sama. Jika ingin pesan yang tegas, tambahkan pilihan `-s` (`diff -s hasil_sebelum.txt hasil_sesudah.txt`). Hasilnya:

```text
Files hasil_sebelum.txt and hasil_sesudah.txt are identical
```

> [!WARNING]
> Di **PowerShell** (terminal bawaan VS Code di Windows), `fc` adalah singkatan perintah lain milik PowerShell. Tulis `fc.exe hasil_sebelum.txt hasil_sesudah.txt` agar yang dijalankan benar-benar program pembanding file. Pesan dari `fc` bisa sedikit berbeda tergantung versi dan bahasa Windows.

Ada satu detail khusus Java di Windows. `println` mengakhiri baris dengan pemisah baris sistem operasi, yaitu dua karakter tak kasatmata CR dan LF. Sebaliknya, `StrukPesanan` menyambung baris-baris struk dengan `"\n"` (LF saja). Teks setiap barisnya tetap sama, tetapi jika alat pembanding di komputermu ikut mempersoalkan tanda akhir baris, bandingkan **isi barisnya** dengan JShell, alat bawaan JDK:

```text
jshell> import java.nio.file.*

jshell> Files.readAllLines(Path.of("hasil_sebelum.txt")).equals(Files.readAllLines(Path.of("hasil_sesudah.txt")))
$2 ==> true
```

`Files.readAllLines()` memecah file menjadi list baris dan mengenali kedua jenis akhir baris. Jawaban `true` berarti semua baris sama dan urutannya pun sama. Cara ini bekerja di semua sistem operasi.

Seperti apa jika *refactoring*-nya keliru? Kami sengaja "merapikan" rumus di `DiskonPersen` menjadi `persen / 100 * Diskon.subtotalDari(daftarItem)`, lalu menjalankan ulang langkah di atas. Hasil `diff`:

```text
41,42c41
< Diskon Promo 15%                -Rp6.150
< TOTAL                           Rp34.850
---
> TOTAL                           Rp41.000
48,49c47,48
< P003  Rina Marlina            Rp34.850
< Total pendapatan: Rp123.750
---
> P003  Rina Marlina            Rp41.000
> Total pendapatan: Rp129.900
```

Cara membacanya: `41,42c41` berarti baris 41 sampai 42 di file pertama **berubah** (*change*) menjadi baris 41 di file kedua. Baris bertanda `<` berasal dari file pertama, sedangkan `>` dari file kedua. Penyebabnya pembagian bilangan bulat: `15 / 100` bernilai 0 di Java, sehingga potongan Rina menjadi nol dan baris diskonnya hilang. Urutan operasi ternyata penting, dan kesalahannya langsung tertangkap.

> [!NOTE]
> Versi Python studi kasus ini harus memindahkan `ItemPesanan` ke file sendiri untuk menghindari **impor melingkar**. Java tidak mengalami masalah itu: `ItemPesanan.java` memang sudah terpisah sejak Pertemuan 05, dan `javac *.java` membaca semua file sekaligus sebelum program berjalan, sehingga kelas-kelas boleh saling menyebut. Penjelasannya ada di [Jembatan](../jembatan-python-java.md).

## 8. Kesalahan Umum dan Cara Membaca Pesan Error

Semua kesalahan di bawah adalah *compile error*, jadi ketahuan **sebelum** program berjalan. Contoh-contohnya dikompilasi bersama file-file di folder `studi-kasus/sesudah`.

### Kesalahan 1: Diskon baru lupa menulis salah satu method

```java
import java.util.List;

public class DiskonUlangTahun implements Diskon {
    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        return 0;
    }
}
```

```text
DiskonUlangTahun.java:3: error: DiskonUlangTahun is not abstract and does not override abstract method keterangan() in Diskon
public class DiskonUlangTahun implements Diskon {
       ^
1 error
```

**Artinya:** *interface* `Diskon` mewajibkan dua method, tetapi `keterangan()` belum ditulis. **Perbaikan:** tambahkan `public String keterangan()` yang mengembalikan teks, misalnya `"Ulang Tahun"`.

### Kesalahan 2: Lupa menulis `public` pada method dari interface

```java
    @Override
    String keterangan() {
        return "Ulang Tahun";
    }
```

```text
DiskonUlangTahun.java:10: error: keterangan() in DiskonUlangTahun cannot implement keterangan() in Diskon
    String keterangan() {
           ^
  attempting to assign weaker access privileges; was public
1 error
```

**Artinya:** semua method di dalam *interface* otomatis `public`. Kelas yang meng-*implements*-nya tidak boleh "mempersempit" akses itu (*weaker access privileges*). **Perbaikan:** tulis `public String keterangan()`.

### Kesalahan 3: Lupa menyuntikkan penyimpanan

```java
        Kedai kedai = new Kedai("KedaiKita");
```

```text
Coba.java:3: error: constructor Kedai in class Kedai cannot be applied to given types;
        Kedai kedai = new Kedai("KedaiKita");
                      ^
  required: String,PenyimpananPesanan
  found:    String
  reason: actual and formal argument lists differ in length
1 error
```

**Artinya:** sejak pertemuan ini, konstruktor `Kedai` **meminta** penyimpanan. **Perbaikan:** `new Kedai("KedaiKita", new PenyimpananMemori())`. Mencoba `new PenyimpananPesanan()` juga ditolak, dengan pesan `PenyimpananPesanan is abstract; cannot be instantiated`, karena *interface* tidak bisa dibuat objeknya.

### Kesalahan 4: Memanggil method `static` interface lewat kelas atau objek

```java
        System.out.println(DiskonPersen.subtotalDari(daftar));
```

```text
Coba.java:8: error: cannot find symbol
        System.out.println(DiskonPersen.subtotalDari(daftar));
                                       ^
  symbol:   method subtotalDari(List<ItemPesanan>)
  location: class DiskonPersen
1 error
```

**Artinya:** method `static` milik *interface* **tidak diwariskan** ke kelas yang meng-*implements*-nya. Memanggilnya lewat objek, misalnya `diskon.subtotalDari(daftar)`, juga ditolak dengan pesan `illegal static interface method call` dan saran `the receiver expression should be replaced with the type qualifier 'Diskon'`. **Perbaikan:** selalu panggil lewat nama *interface*-nya: `Diskon.subtotalDari(daftar)`.

> [!NOTE]
> Pesan di atas berasal dari JDK 21 (dikompilasi dengan `--release 17`). Bunyi pesan bisa sedikit berbeda antarversi JDK. Fokuslah pada nomor baris, tanda `^`, dan kata kuncinya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Kontrak (abstraksi) | `interface Nama { ... }` | `public interface Diskon { ... }` |
| Memenuhi beberapa kontrak kecil | `class K implements A, B, C` | `class KasirLengkap implements PencetakStruk, PemindaiBarcode, LaciUang` |
| Method `static` milik interface | `static Tipe nama(...) { ... }` | `Diskon.subtotalDari(daftarItem)` |
| Method berisi di dalam interface | `default Tipe nama() { ... }` | `default int jumlah()` |
| *Dependency injection* | parameter konstruktor bertipe *interface* | `public Kedai(String nama, PenyimpananPesanan penyimpanan)` |
| Merakit objek | di `main` | `new Kedai("KedaiKita", new PenyimpananMemori())` |
| Tipe kontrak di kiri, wujud di kanan | `Interface var = new Kelas();` | `PenyimpananPesanan penyimpanan = new PenyimpananMemori();` |
| Simpan output ke file | `perintah > file` | `java Main > ..\hasil_sesudah.txt` |
| Bandingkan dua file | `fc` (Windows) / `diff` (macOS/Linux) | `diff hasil_sebelum.txt hasil_sesudah.txt` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
