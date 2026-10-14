# ☕ Solusi Praktik Java — Pertemuan 16: UAS

[⬅️ Pembahasan](../pembahasan.md) · [🐍 Solusi Python](../python/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)

> **Prasyarat:** sudah mencoba sendiri [soal praktik](../latihan-soal.md#bagian-c-soal-praktik) dan membaca [pembahasan desainnya](../pembahasan.md#bagian-c-soal-praktik). Halaman ini membedah kode solusinya bagian demi bagian. Semua kode ada di folder `solusi/` dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Soal C1: Sistem Pemesanan Tiket Bioskop](#1-soal-c1-sistem-pemesanan-tiket-bioskop)
2. [Soal C2: Refactor Kasir Laundry](#2-soal-c2-refactor-kasir-laundry)
3. [Membuktikan Output Tidak Berubah](#3-membuktikan-output-tidak-berubah)
4. [Kesalahan Umum dan Cara Membaca Pesan Error](#4-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
└── solusi/
    ├── SoalC1TiketBioskop.java   <- Soal C1
    ├── SoalC2Sebelum.java        <- Soal C2: kode awal yang berantakan
    └── SoalC2Sesudah.java        <- Soal C2: hasil refactor
```

Setiap solusi adalah **program satu file**, jadi bisa langsung dijalankan (Java 11 ke atas):

```bash
cd Pertemuan-16-UAS/java/solusi
java SoalC1TiketBioskop.java
java SoalC2Sebelum.java
java SoalC2Sesudah.java
```

Cara klasik dua langkah juga bisa dipakai, misalnya `javac SoalC1TiketBioskop.java` lalu `java SoalC1TiketBioskop`.

> [!IMPORTANT]
> Di setiap file, kelas `public` yang memiliki `main` ditulis **paling atas**, dan kelas-kelas pembantunya (tanpa `public`) ditulis di bawahnya. Urutan ini syarat perintah `java NamaFile.java`.

> [!NOTE]
> Semua nama kelas di folder `java/` ini **unik**. Itulah sebabnya kelas format uang di `SoalC2Sesudah.java` bernama `RupiahLaundry`, bukan `Rupiah`: `SoalC1TiketBioskop.java` sudah punya kelas `Rupiah`. Editor seperti VS Code memperlakukan satu folder sebagai satu proyek dan akan protes `The type Rupiah is already defined` jika ada dua kelas bernama sama (lihat [Kesalahan 6](#kesalahan-6-dua-kelas-bernama-sama-dalam-satu-folder)). Di proyekmu sendiri, setiap kelas sebaiknya punya file sendiri.

---

## 1. Soal C1: Sistem Pemesanan Tiket Bioskop

File: [`solusi/SoalC1TiketBioskop.java`](solusi/SoalC1TiketBioskop.java)

Saran urutan membaca: *exception* → `Tiket` dan kelas anaknya → `Jadwal` → `Bioskop` → `main`. Urutan ini sama dengan urutan saat kamu sebaiknya **menulis** kodenya: dari bagian yang tidak bergantung pada apa pun, menuju bagian yang memakai semuanya.

### 1.1 Exception Buatan Sendiri (Checked)

```java
/** Induk semua error BioskopKita. CHECKED: wajib ditangkap atau dideklarasikan. */
class BioskopException extends Exception {
    public BioskopException(String pesan) {
        super(pesan);
    }
}
```

```java
/** Dilempar saat kursi sudah dipesan orang lain. */
class KursiSudahTerjualException extends BioskopException {
    private final String kodeKursi;
    private final String judul;
    private final int sisaKursi; // [2] data tambahan untuk penangkap error

    public KursiSudahTerjualException(String kodeKursi, String judul, int sisaKursi) {
        super("Kursi " + kodeKursi + " untuk " + judul + " sudah terjual"); // [1]
        this.kodeKursi = kodeKursi;
        this.judul = judul;
        this.sisaKursi = sisaKursi;
    }

    public String getKodeKursi() {
        return kodeKursi;
    }

    public String getJudul() {
        return judul;
    }

    public int getSisaKursi() {
        return sisaKursi;
    }
}
```

Penjelasan:

- `BioskopException` mewarisi `Exception` (bukan `RuntimeException`), sehingga ia ***checked***. Setiap method yang bisa melemparnya harus menulis `throws`, dan setiap pemanggilnya harus menangkap atau ikut mendeklarasikannya. *Compiler* yang menjaga agar tidak ada yang lupa.
- **[1]** Pesan dikirim ke konstruktor induk lewat `super(...)`. Pesan inilah yang dikembalikan `e.getMessage()`.
- **[2]** *Exception* adalah objek biasa: field-nya `private final` dan dibaca lewat *getter*. Penangkap error memakai `e.getSisaKursi()` untuk memberi saran.

### 1.2 Kelas Abstrak Tiket dan Tiga Kelas Anaknya

```java
/** Kelas abstrak: kerangka untuk semua jenis tiket. */
abstract class Tiket {
    private final String kodeKursi;
    private final String pemesan;
    private final int hargaDasar;

    public Tiket(String kodeKursi, String pemesan, int hargaDasar) {
        this.kodeKursi = kodeKursi;
        this.pemesan = pemesan;
        this.hargaDasar = hargaDasar;
    }
```

```java
    /** Nama jenis tiket, misalnya "Reguler". */
    public abstract String jenis(); // [3] method abstrak: WAJIB diisi kelas anak

    /** Harga akhir tiket dalam rupiah (bilangan bulat). */
    public abstract int hitungHarga();

    @Override
    public String toString() { // [4] method konkret yang memanggil method abstrak
        String harga = Rupiah.format(hitungHarga());
        return String.format("%-4s%-9s%-16s%10s", kodeKursi, jenis(), pemesan, harga);
    }
}
```

Salah satu kelas anaknya:

```java
/** Kursi sofa + popcorn: harga dasar ditambah biaya tetap. */
class TiketVIP extends Tiket {
    static final int TAMBAHAN = 25000;

    public TiketVIP(String kodeKursi, String pemesan, int hargaDasar) {
        super(kodeKursi, pemesan, hargaDasar);
    }

    @Override
    public String jenis() {
        return "VIP";
    }

    @Override
    public int hitungHarga() {
        return getHargaDasar() + TAMBAHAN;
    }
}
```

Penjelasan:

- Kelas abstrak boleh punya field dan **konstruktor**. Konstruktor itu dipanggil kelas anak lewat `super(...)` di baris pertama konstruktornya.
- Field dibuat `private final`: tiket yang sudah terjual tidak bisa diubah dari luar, dan kelas anak membaca harga dasar lewat `getHargaDasar()`.
- **[3]** Method `abstract` tidak punya badan, diakhiri titik koma. Kelas anak yang tidak mengisinya ditolak *compiler*.
- **[4]** `toString()` ditulis sekali di kelas induk, tetapi memanggil `jenis()` dan `hitungHarga()` milik objek sebenarnya (pola *Template Method* sederhana).

Objek tiket dibuat oleh sebuah Factory sederhana, supaya rantai `if` jenis tiket hanya ada di **satu** tempat:

```java
/** Factory sederhana: membuat objek Tiket dari pilihan berupa teks. */
class TiketFactory {
    static Tiket buat(String jenis, String kodeKursi, String pemesan, int hargaDasar) {
        // "VIP", "vip", dan "Vip" dianggap sama. Locale.ROOT membuat aturan huruf
        // kecilnya sama di semua komputer, apa pun bahasa sistem operasinya.
        String pilihan = jenis.toLowerCase(Locale.ROOT);
        if (pilihan.equals("reguler")) {
            return new TiketReguler(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("vip")) {
            return new TiketVIP(kodeKursi, pemesan, hargaDasar);
        }
        if (pilihan.equals("pelajar")) {
            return new TiketPelajar(kodeKursi, pemesan, hargaDasar);
        }
        throw new IllegalArgumentException("Jenis tiket '" + jenis + "' tidak dikenal");
    }
}
```

Teks dibandingkan dengan `.equals()`, bukan `==`. `IllegalArgumentException` adalah *unchecked*, sehingga method `buat` tidak perlu menulis `throws`.

### 1.3 Jadwal: Map Kursi dan Polimorfisme

Field koleksi di kelas `Jadwal`:

```java
    private final List<String> semuaKursi = new ArrayList<>(); // A1..A5, B1..B5, C1..C5
    // [5] kode kursi -> Tiket. TreeMap selalu urut berdasarkan kunci (A1, A2, ...)
    private final Map<String, Tiket> terjual = new TreeMap<>();
```

Di konstruktornya, daftar kursi dibuat dengan dua perulangan:

```java
        for (char baris : BARIS.toCharArray()) {
            for (int nomor = 1; nomor <= KURSI_PER_BARIS; nomor++) {
                semuaKursi.add(baris + String.valueOf(nomor));
            }
        }
```

Lalu method-method utamanya:

```java
    /** Menyimpan tiket. Melempar exception jika kursi tidak ada/sudah terjual. */
    public void tambahTiket(Tiket tiket) throws KursiTidakAdaException,
            KursiSudahTerjualException {
        String kursi = tiket.getKodeKursi();
        if (!semuaKursi.contains(kursi)) {
            throw new KursiTidakAdaException(kursi, studio);
        }
        if (terjual.containsKey(kursi)) { // [6] cek kunci Map
            throw new KursiSudahTerjualException(kursi, judul, kursiKosong().size());
        }
        terjual.put(kursi, tiket);
    }

    public List<String> kursiKosong() {
        List<String> hasil = new ArrayList<>();
        for (String kursi : semuaKursi) {
            if (!terjual.containsKey(kursi)) {
                hasil.add(kursi);
            }
        }
        return hasil;
    }

    /** Tiket terjual, sudah urut kode kursi karena memakai TreeMap. */
    public List<Tiket> daftarTiket() {
        return new ArrayList<>(terjual.values());
    }

    public int jumlahTerjual() {
        return terjual.size();
    }

    public int pendapatan() {
        int total = 0;
        for (Tiket tiket : terjual.values()) {
            total += tiket.hitungHarga(); // [7] polimorfisme
        }
        return total;
    }
```

Penjelasan:

- Tipe field ditulis sebagai *interface* (`List`, `Map`), implementasinya dipilih di sebelah kanan (`ArrayList`, `TreeMap`).
- **[5]** `TreeMap` menyimpan kunci dalam keadaan **terurut**. Akibatnya, `daftarTiket()` cukup menyalin `terjual.values()` dan tiket otomatis urut kode kursi. Versi Python memakai dict biasa lalu `sorted()`.
- `baris + String.valueOf(nomor)` menghasilkan teks `"A1"`. Hati-hati: `baris + nomor` (tanpa `String.valueOf`) adalah penjumlahan **angka**, karena `char` diperlakukan sebagai kode karakternya. `'A' + 1` menghasilkan `66`, bukan `"A1"`.
- `tambahTiket` mendeklarasikan **dua** *exception* yang bisa dilemparnya secara tepat, sehingga pembaca langsung tahu kegagalan apa saja yang mungkin terjadi.
- **[6]** `containsKey` memeriksa kunci tanpa perulangan. Kunci `Map` selalu unik, jadi satu kursi mustahil tercatat untuk dua tiket.
- **[7]** `pendapatan()` tidak peduli jenis tiket; setiap objek menjawab `hitungHarga()` dengan caranya sendiri.

### 1.4 Bioskop: Pemesanan dan Laporan Terurut

```java
    /** Memesan satu tiket. Urutan pemeriksaan: jadwal, jenis, kursi. */
    public Tiket pesan(String kodeJadwal, String jenis, String kodeKursi, String pemesan)
            throws BioskopException { // mencakup ketiga turunannya
        Jadwal jadwal = cariJadwal(kodeJadwal);
        Tiket tiket = TiketFactory.buat(jenis, kodeKursi, pemesan, jadwal.getHargaDasar());
        jadwal.tambahTiket(tiket);
        return tiket;
    }
```

```java
    /** Pendapatan terbesar dulu; jika sama, judul A-Z. */
    public List<Jadwal> laporanPerFilm() {
        List<Jadwal> hasil = new ArrayList<>(daftarJadwal.values());
        hasil.sort(Comparator.comparing(Jadwal::pendapatan).reversed()
                .thenComparing(Jadwal::getJudul)); // [8]
        return hasil;
    }

    /** Jenis tiket -> banyak tiket terjual. TreeMap: urut nama jenis. */
    public Map<String, Integer> jumlahPerJenis() {
        Map<String, Integer> hasil = new TreeMap<>();
        for (Tiket tiket : semuaTiket()) {
            hasil.put(tiket.jenis(), hasil.getOrDefault(tiket.jenis(), 0) + 1);
        }
        return hasil;
    }
```

Penjelasan:

- `pesan` cukup menulis `throws BioskopException`, karena ketiga *exception* bioskop adalah turunannya. Method ini tidak menangkap apa pun; kegagalan diteruskan ke `main`, yang lebih tahu cara menampilkannya.
- **[8]** `Comparator.comparing(Jadwal::pendapatan)` mengurutkan berdasarkan pendapatan (naik), `.reversed()` membaliknya (turun), lalu `.thenComparing(Jadwal::getJudul)` dipakai jika pendapatannya sama. Pakailah *method reference* (`Jadwal::pendapatan`) seperti ini; versi *lambda* tanpa tipe bisa membingungkan *compiler* (lihat [Kesalahan 5](#kesalahan-5-lambda-tanpa-tipe-sebelum-reversed)).
- `getOrDefault(kunci, 0) + 1` adalah pola menghitung frekuensi dengan `Map`. Karena `hasil` adalah `TreeMap`, kuncinya urut nama jenis (Pelajar, Reguler, VIP).

### 1.5 Program Utama: Menangkap Exception dengan Rapi

```java
    // main boleh melempar BioskopException karena cariJadwal("J02") di bawah
    // dipanggil di luar try (seperti versi Python). J02 pasti ada; jika tidak,
    // program berhenti dan Java menampilkan stack trace.
    public static void main(String[] args) throws BioskopException {
```

```java
        System.out.println("=== PEMESANAN TIKET ===");
        for (String[] permintaan : DAFTAR_PERMINTAAN) {
            String kodeJadwal = permintaan[0];
            try {
                Tiket tiket = bioskop.pesan(kodeJadwal, permintaan[1], permintaan[2],
                        permintaan[3]);
                // Java tidak punya "else" pada try: baris sukses ditulis di dalam try
                String harga = Rupiah.format(tiket.hitungHarga());
                System.out.println("[OK]    " + kodeJadwal + "/" + tiket.getKodeKursi() + " "
                        + tiket.jenis() + " untuk " + tiket.getPemesan() + ": " + harga);
            } catch (KursiSudahTerjualException e) { // [9] yang spesifik ditulis dulu
                System.out.println("[GAGAL] " + e.getMessage());
                System.out.println("        Saran: pilih kursi lain, masih ada "
                        + e.getSisaKursi() + " kursi kosong");
            } catch (BioskopException e) { // [10] semua error bioskop yang lain
                System.out.println("[GAGAL] " + e.getMessage());
            } catch (IllegalArgumentException e) { // jenis tiket tidak dikenal
                System.out.println("[GAGAL] " + e.getMessage());
            }
        }
        System.out.println();
```

Penjelasan:

- `main` menulis `throws BioskopException` karena di bagian laporan ada `bioskop.cariJadwal("J02")` di luar `try`. Tanpa `throws`, *compiler* menolak (lihat [Kesalahan 2](#kesalahan-2-checked-exception-tidak-ditangani)).
- **[9]** Blok `catch` untuk kelas anak **wajib** ditulis sebelum kelas induknya. Jika terbalik, Java menolaknya saat kompilasi.
- **[10]** Dua *exception* bioskop lainnya ditangani sama, cukup dengan satu blok milik induknya.
- `IllegalArgumentException` tidak berkerabat dengan `BioskopException` (yang satu *unchecked*, yang lain *checked*), jadi urutan kedua blok terakhir bebas.
- Data permintaan disimpan sebagai `String[][]`, karena keempat isinya sama-sama teks.

Kelas `Rupiah` di file ini memformat uang dengan `Locale.US` agar hasilnya sama di semua komputer:

```java
/** Kelas utilitas format uang: 18000 -> "Rp18.000". */
class Rupiah {
    static String format(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}
```

Cara menjalankan:

```bash
cd Pertemuan-16-UAS/java/solusi
java SoalC1TiketBioskop.java
```

**Output:**

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

Output ini **identik** dengan versi Python.

> [!TIP]
> **Coba sendiri:** ubah `terjual` menjadi `new HashMap<>()` lalu jalankan lagi. Apakah daftar tiket J02 masih pasti urut A1, A2, A3, B1? Mengapa?

<details>
<summary>Lihat jawaban</summary>

Tidak ada jaminan. `HashMap` tidak menjaga urutan apa pun; urutan yang terlihat bergantung pada nilai *hash* kuncinya. Bisa saja kebetulan terlihat urut pada data sekecil ini, dan justru itulah jebakannya. Jika tetap memakai `HashMap`, `daftarTiket()` harus mengurutkan sendiri, misalnya dengan `hasil.sort(Comparator.comparing(Tiket::getKodeKursi))`.

</details>

---

## 2. Soal C2: Refactor Kasir Laundry

File: [`solusi/SoalC2Sebelum.java`](solusi/SoalC2Sebelum.java) (kode awal) dan [`solusi/SoalC2Sesudah.java`](solusi/SoalC2Sesudah.java) (hasil refactor)

### 2.1 Membaca Kode Sebelum Refactor

Potongan inti method `terimaCucian()` di kode awal:

```java
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
```

```java
        // kirim WhatsApp
        System.out.println("[WA ke " + noHp + "] Halo " + nama + ", cucian " + kode
                + " sudah kami terima. Total " + teksTotal + ".");

        // simpan riwayat
        riwayat.add(new String[] {kode, nama, String.valueOf(berat), String.valueOf(total)});
```

Perhatikan komentar-komentar seperti `// hitung promo` dan `// kirim WhatsApp`. Setiap komentar yang menandai "babak" di dalam satu method adalah petunjuk bahwa method itu mengerjakan terlalu banyak hal. Perhatikan juga riwayat yang disimpan sebagai array `String`: berat dan total diubah menjadi teks, lalu di `cetakLaporan()` di-*parse* lagi dengan `Integer.parseInt`. Daftar lengkap masalahnya ada di [pembahasan](../pembahasan.md#soal-c2-refactor-kasir-laundry-yang-berantakan).

### 2.2 Strategy untuk Promo

```java
/** Strategi promo. Promo baru = kelas baru; kelas lain tidak diubah (OCP). */
interface Promo {
    /** Besar potongan dalam rupiah. Tidak pernah negatif (LSP). */
    int hitungPotongan(PesananLaundry pesanan); // [3]

    /** Nama promo untuk dicetak di nota. */
    String keterangan();
}
```

```java
/** Cucian minimal 5 kg: gratis 1 kg (potongan = tarif 1 kg). */
class PromoGratisSatuKg implements Promo {
    static final int MINIMAL_BERAT = 5;

    @Override
    public int hitungPotongan(PesananLaundry pesanan) {
        if (pesanan.getBerat() < MINIMAL_BERAT) {
            return 0;
        }
        return pesanan.getLayanan().getTarifPerKg();
    }

    @Override
    public String keterangan() {
        return "Gratis 1 kg";
    }
}
```

Di kelas `PesananLaundry`:

```java
    public int subtotal() {
        return layanan.getTarifPerKg() * berat;
    }

    public int potongan() {
        return promo.hitungPotongan(this); // [4] diserahkan ke strategi
    }

    public int total() {
        return subtotal() - potongan();
    }
```

Penjelasan:

- **[3]** Method di dalam `interface` otomatis `public` dan abstrak, jadi tidak perlu menulis kedua kata itu. Kelas yang mengimplementasikannya wajib menulis `public` saat meng-*override*.
- Setiap promo menjadi satu kelas kecil. Rantai `if (promo.equals(...))` hilang, dan salah ketik nama promo kini ditolak *compiler* (`cannot find symbol`), bukan promo yang diam-diam tidak berlaku.
- **[4]** `PesananLaundry` tidak tahu promo apa yang dipakainya. Ia cukup **meminta** strategi menghitung potongan, sambil memberikan dirinya sendiri (`this`) sebagai data.

### 2.3 Katalog Layanan dan Exception

```java
/** Daftar layanan. Layanan baru cukup DIDAFTARKAN, tanpa mengubah kode (OCP). */
class KatalogLayanan {
    // [1] nama layanan -> Layanan. HashMap cukup karena katalog hanya dipakai
    //     untuk MENCARI, tidak pernah dicetak berurutan.
    private final Map<String, Layanan> daftar = new HashMap<>();

    public void tambah(Layanan layanan) {
        daftar.put(layanan.getNama(), layanan);
    }

    public Layanan cari(String nama) throws LayananTidakTersediaException {
        if (!daftar.containsKey(nama)) {
            throw new LayananTidakTersediaException(nama); // [2] bukan lagi print + return
        }
        return daftar.get(nama);
    }
}
```

Penjelasan:

- **[1]** Rantai `if (layanan.equals("cuci kering")) ...` berubah menjadi **data** di dalam `Map`. Di sini `HashMap` sudah cukup karena isinya tidak pernah dicetak berurutan. Seandainya kelak perlu menampilkan daftar layanan, gantilah dengan `LinkedHashMap`.
- **[2]** Kode awal mencetak `[DITOLAK] ...` lalu `return`, sehingga pemanggil tidak tahu ada kegagalan. Kini katalog melempar `LayananTidakTersediaException` (*checked*), dan *compiler* memastikan pemanggilnya menangani kemungkinan itu.

### 2.4 Kasir yang Bergantung pada Abstraksi

```java
/** Kontrak kecil: cukup satu method untuk mengirim pesan (ISP). */
interface Pengirim {
    void kirim(String noHp, String pesan);
}

/** Simulasi WhatsApp: pesan dicetak ke layar. */
class PengirimWhatsApp implements Pengirim {
    @Override
    public void kirim(String noHp, String pesan) {
        System.out.println("[WA ke " + noHp + "] " + pesan);
    }
}
```

```java
/** Mengatur alur kerja kasir dengan memakai kelas-kelas di atas. */
class KasirLaundry {
    private final KatalogLayanan katalog;
    private final Pengirim pengirim; // bergantung pada ABSTRAKSI (DIP)
    private final List<PesananLaundry> riwayat = new ArrayList<>();
    private int nomorTerakhir = 0;

    public KasirLaundry(KatalogLayanan katalog, Pengirim pengirim) { // [5]
        this.katalog = katalog;
        this.pengirim = pengirim;
    }

    /** Melempar LayananTidakTersediaException jika layanan tidak dikenal. */
    public PesananLaundry terimaCucian(Pelanggan pelanggan, String namaLayanan, int berat,
            Promo promo) throws LayananTidakTersediaException {
        Layanan layanan = katalog.cari(namaLayanan); // dicek SEBELUM nomor dibuat
        nomorTerakhir++;
        String kode = String.format("L%03d", nomorTerakhir);
        PesananLaundry pesanan = new PesananLaundry(kode, pelanggan, layanan, berat, promo);
        System.out.println(new NotaLaundry(pesanan).buatTeks());
        pengirim.kirim(pelanggan.getNoHp(), "Halo " + pelanggan.getNama() + ", cucian " + kode
                + " sudah kami terima. Total " + RupiahLaundry.format(pesanan.total()) + ".");
        riwayat.add(pesanan);
        return pesanan;
    }
```

Lapisan tampilan kecil dan program utamanya:

```java
    /** Lapisan tampilan: memanggil kasir dan menampilkan pesan bila ditolak. */
    static void terima(KasirLaundry kasir, Pelanggan pelanggan, String namaLayanan,
            int berat, Promo promo) {
        try {
            kasir.terimaCucian(pelanggan, namaLayanan, berat, promo);
        } catch (LayananTidakTersediaException e) {
            System.out.println("[DITOLAK] " + e.getMessage());
        }
        System.out.println();
    }

    public static void main(String[] args) {
        KasirLaundry kasir = new KasirLaundry(siapkanKatalog(), new PengirimWhatsApp()); // [6]
        terima(kasir, new Pelanggan("Budi Santoso", "081234567890"), "cuci setrika", 4,
                new PromoMember());
```

Penjelasan:

- **[5]** `KasirLaundry` menerima katalog dan pengirim **dari luar** lewat konstruktor (*dependency injection*). Tipe field-nya `Pengirim` (*interface*), bukan `PengirimWhatsApp`.
- **[6]** Keputusan "pesan dikirim lewat WhatsApp" hanya ada di satu baris ini. Mengganti ke SMS cukup membuat `PengirimSMS implements Pengirim` dan mengubah baris ini; `KasirLaundry` tidak disentuh.
- Komentar `dicek SEBELUM nomor dibuat` menjaga detail perilaku kode awal: nomor order hanya bertambah jika layanannya valid. Refactor tidak boleh mengubah perilaku sekecil apa pun.
- `main` tidak perlu `throws`, karena satu-satunya *checked exception* (`LayananTidakTersediaException`) sudah ditangkap di `terima()`.
- `riwayat()` mengembalikan **salinan** list (`new ArrayList<>(riwayat)`), sehingga isi riwayat tidak bisa dirusak dari luar.

Cara menjalankan:

```bash
cd Pertemuan-16-UAS/java/solusi
java SoalC2Sebelum.java
java SoalC2Sesudah.java
```

Kedua program menghasilkan output yang sama persis, dan sama pula dengan versi Python.

**Output:**

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

---

## 3. Membuktikan Output Tidak Berubah

Simpan output kedua versi ke file, lalu bandingkan dengan perintah sistem operasi:

```bash
java SoalC2Sebelum.java > sebelum.txt
java SoalC2Sesudah.java > sesudah.txt
diff sebelum.txt sesudah.txt
```

Di macOS/Linux, `diff` **tidak mencetak apa pun** jika kedua file identik. Di Windows (Command Prompt), gunakan `fc sebelum.txt sesudah.txt`; jika identik, ia menulis `FC: no differences encountered`. Di PowerShell, tulis `fc.exe`, karena `fc` di sana adalah perintah lain.

Kamu juga bisa membandingkan output Java dengan output Python dengan cara yang sama, misalnya `python ../../python/solusi/soal_c2_sesudah.py > python.txt` lalu `diff sesudah.txt python.txt`. Contoh membaca hasil `diff` yang **berbeda** ada di [Solusi Python](../python/README.md#3-membuktikan-output-tidak-berubah).

> [!TIP]
> Jalankan `diff` setiap kali selesai memindahkan **satu** tanggung jawab ke kelas baru. Jika muncul perbedaan, kamu langsung tahu langkah mana penyebabnya.

---

## 4. Kesalahan Umum dan Cara Membaca Pesan Error

Sebagian besar kesalahan di bawah ini adalah **error kompilasi**: Java menolak menjalankan program sama sekali. Pesannya diawali nama file dan nomor baris, dan tanda `^` menunjuk posisi masalahnya.

### Kesalahan 1: Urutan catch terbalik

Jika `catch (BioskopException e)` ditulis **di atas** `catch (KursiSudahTerjualException e)`:

```text
SoalC1TiketBioskop.java:78: error: exception KursiSudahTerjualException has already been caught
            } catch (KursiSudahTerjualException e) {
              ^
1 error
```

**Artinya:** setiap `KursiSudahTerjualException` juga merupakan `BioskopException`, jadi blok di atasnya sudah menangkapnya. Blok di bawah tidak akan pernah tercapai, dan Java menganggap itu kesalahan. (Python diam saja untuk kasus yang sama, sehingga *bug*-nya lebih licin.) **Perbaikan:** tulis `catch` yang lebih spesifik lebih dulu.

### Kesalahan 2: Checked exception tidak ditangani

Jika `throws BioskopException` dihapus dari `main`:

```text
SoalC1TiketBioskop.java:88: error: unreported exception JadwalTidakDitemukanException; must be caught or declared to be thrown
        Jadwal jadwal = bioskop.cariJadwal("J02");
                                          ^
1 error
```

**Artinya:** `cariJadwal` bisa melempar *checked exception*, dan baris ini tidak berada di dalam `try`, sementara `main` juga tidak mendeklarasikannya. **Perbaikan:** bungkus dengan `try-catch`, atau tambahkan `throws` pada method yang memanggilnya. Pilih yang paling masuk akal: tangkap di tempat yang bisa **menangani** kegagalan dengan baik.

### Kesalahan 3: Lupa mengisi method abstrak

Jika method `hitungHarga()` di `TiketVIP` terhapus:

```text
SoalC1TiketBioskop.java:249: error: TiketVIP is not abstract and does not override abstract method hitungHarga() in Tiket
class TiketVIP extends Tiket {
^
1 error
```

**Artinya:** kelas konkret wajib mengisi semua method abstrak induknya. Berbeda dengan Python yang baru protes saat objek dibuat, Java menolak sejak kompilasi. **Perbaikan:** tambahkan `hitungHarga()` lengkap dengan `@Override`.

### Kesalahan 4: Membuat objek dari kelas abstrak

```java
        Tiket coba = new Tiket("A1", "Budi Santoso", 40000);
```

```text
SoalC1TiketBioskop.java:59: error: Tiket is abstract; cannot be instantiated
        Tiket coba = new Tiket("A1", "Budi Santoso", 40000);
                     ^
1 error
```

**Artinya:** kelas abstrak hanya kerangka. **Perbaikan:** buat objek dari kelas anaknya, misalnya `Tiket coba = new TiketReguler("A1", "Budi Santoso", 40000);`. Variabelnya boleh tetap bertipe `Tiket` (*upcasting*).

### Kesalahan 5: Lambda tanpa tipe sebelum `reversed()`

Jika `Comparator.comparing(Jadwal::pendapatan)` diganti dengan *lambda* `Comparator.comparing(j -> j.pendapatan())`, bagian awal pesan error-nya:

```text
SoalC1TiketBioskop.java:458: error: cannot find symbol
        hasil.sort(Comparator.comparing(j -> j.pendapatan()).reversed()
                                              ^
  symbol:   method pendapatan()
  location: variable j of type Object
```

Setelah itu muncul pesan kedua yang panjang tentang `thenComparing`.

**Artinya:** karena ada `.reversed()` yang menempel, *compiler* tidak bisa menebak tipe `j`, lalu menganggapnya `Object`, padahal `Object` tidak punya method `pendapatan()`. **Perbaikan:** pakai *method reference* `Jadwal::pendapatan`, atau tulis tipenya secara eksplisit: `(Jadwal j) -> j.pendapatan()`.

### Kesalahan 6: Dua kelas bernama sama dalam satu folder

Jika kelas `RupiahLaundry` di `SoalC2Sesudah.java` dinamai `Rupiah`, lalu kedua file dikompilasi bersama (`javac SoalC1TiketBioskop.java SoalC2Sesudah.java`):

```text
SoalC2Sesudah.java:73: error: duplicate class: Rupiah
class Rupiah {
^
1 error
```

**Artinya:** dalam satu paket (di sini paket bawaan tanpa nama), nama kelas harus unik. VS Code menampilkan masalah yang sama sebagai `The type Rupiah is already defined`. **Perbaikan:** beri nama yang berbeda, atau letakkan kelas di file/paket sendiri seperti pada proyek berpaket di Pertemuan 15.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK; fokuslah pada kata kuncinya. Jika kamu mengompilasi dengan `javac -Xlint:all`, javac juga memberi peringatan `[serial] serializable class BioskopException has no definition of serialVersionUID`. Itu hanya **peringatan**, bukan error: kelas *exception* bisa diserialisasi, dan Java menyarankan nomor versi. Untuk latihan ini aman diabaikan; jika ingin menghilangkannya, tambahkan `private static final long serialVersionUID = 1L;` di kelas *exception*.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh dari solusi |
|---|---|---|
| Kelas abstrak | `abstract class Nama` + `public abstract Tipe method();` | `abstract class Tiket` |
| *Interface* | `interface Nama { Tipe method(...); }` + `implements` | `interface Promo` |
| *Checked exception* | `class X extends Exception` | `class BioskopException extends Exception` |
| Deklarasi lemparan | `Tipe method(...) throws X` | `Tiket pesan(...) throws BioskopException` |
| Menangkap berurutan | `catch (Anak e)` lalu `catch (Induk e)` | `catch (KursiSudahTerjualException e)` |
| Map terurut kunci | `Map<K, V> m = new TreeMap<>();` | `terjual`, `jumlahPerJenis()` |
| Map urutan masuk | `Map<K, V> m = new LinkedHashMap<>();` | `daftarJadwal` |
| Hitung frekuensi | `m.put(k, m.getOrDefault(k, 0) + 1)` | `jumlahPerJenis()` |
| Urut dua kriteria | `comparing(A::x).reversed().thenComparing(A::y)` | `laporanPerFilm()` |
| Huruf kecil tanpa jebakan *locale* | `teks.toLowerCase(Locale.ROOT)` | `TiketFactory.buat()` |
| *Dependency injection* | objek pendukung lewat konstruktor | `new KasirLaundry(katalog, new PengirimWhatsApp())` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan solusi Python: [🐍 Solusi Python](../python/README.md). Output-nya identik.
- Siapkan presentasi proyek akhir: [Presentasi Proyek Akhir](../README.md#8-presentasi-proyek-akhir).

---

[⬅️ Pembahasan](../pembahasan.md) · [🐍 Solusi Python](../python/README.md) · [Presentasi Proyek Akhir ➡️](../README.md#8-presentasi-proyek-akhir)
