# ☕ Praktik Java — Pertemuan 07: Pewarisan

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 07](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Masalah: Kode Kembar di Dua Kelas](#1-masalah-kode-kembar-di-dua-kelas)
2. [Kelas Induk dan Kelas Anak dengan `extends`](#2-kelas-induk-dan-kelas-anak-dengan-extends)
3. [`@Override` dan `super`](#3-override-dan-super)
4. [Urutan Konstruktor dan Pewarisan Bertingkat](#4-urutan-konstruktor-dan-pewarisan-bertingkat)
5. [`protected`: Akses untuk Kelas Anak](#5-protected-akses-untuk-kelas-anak)
6. [Kelas Akar `Object` dan `instanceof`](#6-kelas-akar-object-dan-instanceof)
7. [is-a atau has-a?](#7-is-a-atau-has-a)
8. [Satu Induk Saja, dan Kata Kunci `final`](#8-satu-induk-saja-dan-kata-kunci-final)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 7 contoh program satu file
├── studi-kasus/     <- KedaiKita versi Pertemuan 07 (satu kelas per file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file, jadi bisa langsung dijalankan:

```bash
cd Pertemuan-07-Pewarisan/java/contoh
java Contoh01MasalahDuplikasi.java
```

Studi kasus terdiri atas banyak file. Kompilasi semuanya dulu, lalu jalankan kelas `Main`:

```bash
cd Pertemuan-07-Pewarisan/java/studi-kasus
javac *.java
java Main
```

> [!TIP]
> Di VS Code, buka folder `java/` **milik pertemuan ini** saja (File → Open Folder). Nama kelas di dalam satu folder harus unik. Itulah sebabnya kelas di contoh 01 bernama `MotorLama`, karena nama `Motor` sudah dipakai contoh 02. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

## 1. Masalah: Kode Kembar di Dua Kelas

File: [`contoh/Contoh01MasalahDuplikasi.java`](contoh/Contoh01MasalahDuplikasi.java)

Sebelum belajar pewarisan, rasakan dulu masalahnya. File ini berisi dua kelas yang ditulis terpisah, `MotorLama` dan `MobilLama`. Akhiran "Lama" menandakan versi lama, sebelum memakai pewarisan. Berikut kelas `MotorLama`:

```java
/** Sepeda motor, ditulis tanpa pewarisan. */
class MotorLama {
    private String merek; // [1] tiga field ini kembar dengan milik MobilLama
    private String platNomor;
    private int tahun;
    private String transmisi; // [2] khusus motor: "matic" atau "manual"

    public MotorLama(String merek, String platNomor, int tahun, String transmisi) {
        this.merek = merek;
        this.platNomor = platNomor;
        this.tahun = tahun;
        this.transmisi = transmisi;
    }

    public String getMerek() {
        return merek;
    }

    public String info() { // [3] method kembar
        return merek + " (" + platNomor + ") tahun " + tahun;
    }

    public int umur(int tahunSekarang) { // [3] method kembar
        return tahunSekarang - tahun;
    }

    public String deskripsi() {
        return "Motor: " + info() + ", transmisi " + transmisi;
    }
}
```

Kelas `MobilLama` di file yang sama ditulis dengan pola yang **persis sama**. Bedanya hanya field `jumlahKursi` (pengganti `transmisi`) dan isi method `deskripsi()`. Bukalah file-nya dan bandingkan baris demi baris.

**Output:**

```text
=== DAFTAR KENDARAAN ===
Motor: Honda Beat (KT 1234 AB) tahun 2020, transmisi matic
Mobil: Toyota Avanza (KT 5678 CD) tahun 2018, 7 kursi

=== UMUR DI TAHUN 2026 ===
Honda Beat: 6 tahun
Toyota Avanza: 8 tahun
```

Penjelasan:

- **[1]** Field `merek`, `platNomor`, dan `tahun`, beserta isi konstruktornya, ditulis dua kali.
- **[2]** Hanya satu field yang benar-benar khas: `transmisi` untuk motor dan `jumlahKursi` untuk mobil.
- **[3]** Method `getMerek()`, `info()`, dan `umur()` sama persis, huruf demi huruf.

> [!TIP]
> **Coba sendiri:** tambahkan field `warna` ke semua kendaraan, lalu tampilkan di `info()`. Hitung berapa tempat yang harus kamu ubah. Bayangkan jika jenis kendaraannya ada sepuluh!

## 2. Kelas Induk dan Kelas Anak dengan `extends`

File: [`contoh/Contoh02KelasIndukDanAnak.java`](contoh/Contoh02KelasIndukDanAnak.java)

Sekarang semua bagian yang sama dikumpulkan ke satu **kelas induk**, `Kendaraan`. `Motor` dan `Mobil` menjadi **kelas anak** dengan kata kunci `extends`.

```java
/** Kelas induk untuk semua kendaraan bermotor. */
class Kendaraan { // [1] kelas induk: semua bagian yang SAMA dikumpulkan di sini
    private String merek;
    private String platNomor;
    private int tahun;

    public Kendaraan(String merek, String platNomor, int tahun) {
        this.merek = merek;
        this.platNomor = platNomor;
        this.tahun = tahun;
    }

    public String getMerek() {
        return merek;
    }

    public String info() {
        return merek + " (" + platNomor + ") tahun " + tahun;
    }

    public int umur(int tahunSekarang) {
        return tahunSekarang - tahun;
    }
}

/** Sepeda motor: semua milik Kendaraan, ditambah jenis transmisi. */
class Motor extends Kendaraan { // [2] Motor adalah Kendaraan
    private String transmisi; // [4] field tambahan khusus motor

    public Motor(String merek, String platNomor, int tahun, String transmisi) {
        super(merek, platNomor, tahun); // [3] bagian induk diisi induk, WAJIB paling awal
        this.transmisi = transmisi;
    }

    public String deskripsi() { // [5] method tambahan, memakai method warisan
        return "Motor: " + info() + ", transmisi " + transmisi;
    }
}
```

Kelas `Mobil` ditulis dengan pola yang sama: `extends Kendaraan`, field `jumlahKursi`, konstruktor yang memanggil `super(...)`, dan method `deskripsi()`. Program utamanya sama dengan contoh 01, kecuali tipe objeknya. Perhatikan bagian akhirnya:

```java
        // [6] getMerek() dan umur() tidak ditulis di Motor/Mobil: keduanya warisan
        System.out.println(beat.getMerek() + ": " + beat.umur(2026) + " tahun");
        System.out.println(avanza.getMerek() + ": " + avanza.umur(2026) + " tahun");
```

Jalankan file ini, lalu bandingkan: output-nya **sama persis** dengan output contoh 01. Bedanya, kodenya jauh lebih rapi. Mengubah cara menghitung umur kini cukup dilakukan di **satu** tempat.

Penjelasan:

- **[1]** `Kendaraan` adalah kelas biasa. Ia menjadi "induk" karena ada kelas lain yang mewarisinya.
- **[2]** `class Motor extends Kendaraan` berarti "Motor mewarisi Kendaraan". Kata `extends` secara harfiah berarti "memperluas": `Motor` adalah `Kendaraan` yang diperluas.
- **[3]** `super(...)` memanggil **konstruktor induk** untuk mengisi `merek`, `platNomor`, dan `tahun`. Di Java 17, baris ini wajib menjadi pernyataan pertama.
- **[4]** Setelah bagian induk terisi, kelas anak mengisi field tambahannya sendiri.
- **[5]** Method baru boleh memanggil method warisan. `info()` tidak ditulis di `Motor`, tetapi tersedia karena diwarisi dari `Kendaraan`.
- **[6]** `getMerek()` dan `umur()` juga warisan.

Ada dua hal penting yang khas Java:

| Fakta | Akibatnya |
|---|---|
| Field `merek` di `Kendaraan` bersifat `private` | `Motor` tidak bisa menulis `merek` secara langsung. Ia memakai method warisan seperti `info()` atau `getMerek()` (lihat [Kesalahan 3](#kesalahan-3-mengakses-field-private-milik-induk)) |
| Konstruktor **tidak** diwariskan | Setiap kelas anak wajib menulis konstruktornya sendiri, walaupun hanya untuk meneruskan data ke `super(...)`. Jika `Truk extends Kendaraan` tidak menulis konstruktor sama sekali, kompilasi gagal karena `Kendaraan` tidak punya konstruktor tanpa parameter (pesannya seperti [Kesalahan 1](#kesalahan-1-lupa-memanggil-super)). Di Python, kasus serupa justru berhasil karena `__init__` ikut diwariskan |

## 3. `@Override` dan `super`

File: [`contoh/Contoh03Override.java`](contoh/Contoh03Override.java)

Kelas anak bisa **menimpa** (*override*) method induk dengan menulis method yang tanda tangannya sama. Di dalam versi barunya, versi induk tetap bisa dipanggil lewat `super.namaMethod()`.

```java
/** Tiket reguler sebuah acara. */
class Tiket {
    private String acara;
    private int harga;

    public Tiket(String acara, int harga) {
        this.acara = acara;
        this.harga = harga;
    }

    public String getAcara() {
        return acara;
    }

    public String info() {
        return "Tiket " + acara + " - Rp" + harga;
    }

    public int hitungBayar(int jumlah) {
        return harga * jumlah;
    }
}

/** Tiket VIP: punya fasilitas dan ada biaya layanan per orang. */
class TiketVIP extends Tiket {
    private static final int BIAYA_LAYANAN_VIP = 25000; // per orang, dalam Rupiah

    private String fasilitas;

    public TiketVIP(String acara, int harga, String fasilitas) {
        super(acara, harga);
        this.fasilitas = fasilitas;
    }

    @Override // [1] override: nama, parameter, dan tipe kembalian sama dengan induk
    public String info() {
        return super.info() + " | VIP: " + fasilitas; // [2] versi induk + tambahan
    }

    @Override // [3] override kedua
    public int hitungBayar(int jumlah) {
        int hargaDasar = super.hitungBayar(jumlah); // [4] hitungan versi induk
        return hargaDasar + BIAYA_LAYANAN_VIP * jumlah;
    }
}
```

Di program utama, perhatikan dua baris ini:

```java
        System.out.println(reguler.info()); // [5] objek Tiket -> versi Tiket
        System.out.println(vip.info()); // [5] objek TiketVIP -> versi TiketVIP
```

**Output:**

```text
=== INFO TIKET ===
Tiket Festival Musik Kampus - Rp50000
Tiket Festival Musik Kampus - Rp120000 | VIP: kursi depan dan kaus

=== BAYAR UNTUK 3 ORANG ===
Reguler: Rp150000
VIP    : Rp435000
Acara  : Festival Musik Kampus
```

Penjelasan:

- **[1]** `@Override` adalah **anotasi**: catatan untuk *compiler* bahwa method ini dimaksudkan untuk menimpa method induk. *Compiler* lalu memeriksa bahwa method dengan tanda tangan yang sama memang ada di induk. Jika tidak ada, misalnya karena salah ketik, kompilasi langsung gagal.
- **[2]** `super.info()` menjalankan versi **induk** (`Tiket Festival Musik Kampus - Rp120000`), lalu versi anak menambahkan keterangan VIP. Rumus teks induk tidak ditulis ulang.
- **[3]** Satu kelas boleh meng-*override* beberapa method.
- **[4]** `super.hitungBayar(3)` menghasilkan 3 x 120000 = 360000. Versi anak lalu menambah biaya layanan 3 x 25000 = 75000, sehingga totalnya 435000.
- **[5]** Versi yang dipakai ditentukan oleh **objeknya**: `reguler` memakai versi `Tiket`, `vip` memakai versi `TiketVIP`.
- **[6]** (baris terakhir `main`) Method yang tidak di-*override*, seperti `getAcara()`, tetap memakai versi warisan.

Aturan *override* di Java: nama, parameter, **dan** tipe kembalian harus sama (jika parameternya berbeda, yang terjadi adalah *overload*), dan hak akses tidak boleh lebih sempit (lihat [Kesalahan 5](#kesalahan-5-memperkecil-hak-akses-saat-override)). `@Override` memang tidak wajib, tetapi selalu tulis agar terlindung dari salah ketik.

> [!TIP]
> **Coba sendiri:** hapus method `info()` (beserta `@Override` di atasnya) dari kelas `TiketVIP`, lalu jalankan lagi. Baris kedua output menjadi `Tiket Festival Musik Kampus - Rp120000`. Tanpa *override*, objek VIP kembali memakai versi warisan dari `Tiket`.

## 4. Urutan Konstruktor dan Pewarisan Bertingkat

File: [`contoh/Contoh04UrutanKonstruktor.java`](contoh/Contoh04UrutanKonstruktor.java)

Contoh ini punya tiga tingkat: `Perangkat` → `Komputer` → `Laptop`. Setiap konstruktor mencetak pesan **setelah** memanggil konstruktor induknya.

```java
/** Tingkat 1: semua perangkat elektronik. */
class Perangkat {
    private String merek;

    public Perangkat(String merek) {
        // [1] di sini Java diam-diam memanggil super() milik Object
        this.merek = merek;
        System.out.println("  Bagian Perangkat selesai: merek " + merek);
    }

    public String nyalakan() {
        return merek + " dinyalakan";
    }
}

/** Tingkat 2: Komputer adalah Perangkat. */
class Komputer extends Perangkat {
    private int ramGb;

    public Komputer(String merek, int ramGb) {
        super(merek); // [2] minta induk menyiapkan bagiannya dulu
        this.ramGb = ramGb;
        System.out.println("  Bagian Komputer selesai: RAM " + ramGb + " GB");
    }

    public String jalankan(String program) {
        return program + " berjalan dengan RAM " + ramGb + " GB";
    }
}

/** Tingkat 3: Laptop adalah Komputer, dan karena itu juga Perangkat. */
class Laptop extends Komputer {
    private int bateraiJam;

    public Laptop(String merek, int ramGb, int bateraiJam) {
        super(merek, ramGb); // [3] induk langsung Laptop adalah Komputer
        this.bateraiJam = bateraiJam;
        System.out.println("  Bagian Laptop selesai: baterai " + bateraiJam + " jam");
    }

    public String cekBaterai() {
        return "Baterai tahan " + bateraiJam + " jam";
    }
}
```

Program utamanya:

```java
        System.out.println("=== MEMBUAT LAPTOP (3 TINGKAT) ===");
        Laptop laptop = new Laptop("Lenovo", 16, 8); // [4]

        System.out.println();
        System.out.println("=== MEMBUAT KOMPUTER (2 TINGKAT) ===");
        new Komputer("Dell", 32); // [5] hanya dua bagian yang disiapkan

        System.out.println();
        System.out.println("=== METHOD DARI SETIAP TINGKAT ===");
        System.out.println(laptop.nyalakan()); // [6] warisan dari "kakek" (Perangkat)
        System.out.println(laptop.jalankan("VS Code")); // warisan dari induk (Komputer)
        System.out.println(laptop.cekBaterai()); // milik Laptop sendiri
```

**Output:**

```text
=== MEMBUAT LAPTOP (3 TINGKAT) ===
  Bagian Perangkat selesai: merek Lenovo
  Bagian Komputer selesai: RAM 16 GB
  Bagian Laptop selesai: baterai 8 jam

=== MEMBUAT KOMPUTER (2 TINGKAT) ===
  Bagian Perangkat selesai: merek Dell
  Bagian Komputer selesai: RAM 32 GB

=== METHOD DARI SETIAP TINGKAT ===
Lenovo dinyalakan
VS Code berjalan dengan RAM 16 GB
Baterai tahan 8 jam
```

Penjelasan:

- **[1]** `Perangkat` tidak menulis `extends`, jadi induknya adalah kelas akar `Object`. Karena konstruktor ini tidak menulis `super(...)`, Java otomatis menyisipkan `super();` di baris pertamanya.
- **[2]** Baris pertama konstruktor `Komputer` langsung menyerahkan pekerjaan ke induk.
- **[3]** `super(...)` di `Laptop` merujuk ke **induk langsungnya**, yaitu `Komputer`, bukan `Perangkat`.
- **[4]** Walaupun yang dibuat adalah `Laptop`, pesan pertama berasal dari `Perangkat`. Konstruktor `Laptop` memang dipanggil pertama, tetapi baris pertamanya memanggil `Komputer`, yang baris pertamanya memanggil `Perangkat`. Jadi, lapis paling atas selesai lebih dulu.
- **[5]** `new Komputer(...)` boleh ditulis sebagai pernyataan tersendiri tanpa disimpan ke variabel. Hanya dua konstruktor yang berjalan.
- **[6]** Objek `Laptop` bisa memakai method dari **semua** tingkat di atasnya.

Karena `super(...)` wajib di baris pertama, urutan "induk dulu, baru anak" **selalu** terjamin di Java 17 (lihat juga [Kesalahan 2](#kesalahan-2-super-bukan-di-baris-pertama)).

## 5. `protected`: Akses untuk Kelas Anak

File: [`contoh/Contoh05AksesKelasAnak.java`](contoh/Contoh05AksesKelasAnak.java)

Kamu sudah tahu dari Pertemuan 04: field `private` hanya bisa disentuh oleh kelasnya sendiri, **termasuk** tidak bisa oleh kelas anak. Jika kelas anak memang perlu akses langsung, Java menyediakan `protected`.

```java
/** Kelas induk rekening. */
class RekeningBank {
    private String pemilik; // [1] private: kelas anak pun tidak bisa menyentuhnya
    protected int saldo; // [2] protected: boleh dipakai kelas anak (dan satu paket)

    public RekeningBank(String pemilik, int saldoAwal) {
        this.pemilik = pemilik;
        this.saldo = saldoAwal;
    }

    public int getSaldo() { // pintu resmi untuk membaca saldo dari luar
        return saldo;
    }

    public String info() {
        return "Rekening " + pemilik + ": saldo Rp" + saldo;
    }
}

/** Tabungan yang mendapat bunga bulanan (persen, bilangan bulat). */
class RekeningTabungan extends RekeningBank {
    private int bungaPersen;

    public RekeningTabungan(String pemilik, int saldoAwal, int bungaPersen) {
        super(pemilik, saldoAwal);
        this.bungaPersen = bungaPersen;
    }

    public int tambahBunga() {
        int bunga = saldo * bungaPersen / 100; // [3] membaca field protected induk
        saldo += bunga; // [3] mengubah field protected induk secara langsung
        return bunga;
    }
}
```

Bagian akhir program utamanya:

```java
        System.out.println("Lewat pintu resmi  : Rp" + tabungan.getSaldo());
        System.out.println("Langsung ke atribut: Rp" + tabungan.saldo // [4] satu paket
                + " (bisa, tetapi hindari)");
```

**Output:**

```text
=== TABUNGAN SITI ===
Rekening Siti: saldo Rp1000000
Bunga bulan ini: Rp20000
Rekening Siti: saldo Rp1020000

=== DIBACA DARI LUAR KELAS ===
Lewat pintu resmi  : Rp1020000
Langsung ke atribut: Rp1020000 (bisa, tetapi hindari)
```

Penjelasan:

- **[1]** `pemilik` bersifat `private`. Field ini tetap **ada** di setiap objek `RekeningTabungan`, tetapi kode di kelas `RekeningTabungan` tidak boleh menyebutnya secara langsung.
- **[2]** `saldo` bersifat `protected`, jadi terbuka untuk kelas anak.
- **[3]** `tambahBunga()` membaca dan mengubah `saldo` secara langsung. Bunga 2% dari Rp1.000.000 adalah Rp20.000.
- **[4]** Ini jebakannya. `main` **bukan** kelas anak, tetapi tetap boleh membaca `tabungan.saldo`. Alasannya, semua kelas di file ini berada di paket yang sama (paket tanpa nama), dan `protected` juga terbuka untuk satu paket.

> [!WARNING]
> `protected` lebih longgar daripada kedengarannya. Untuk data penting seperti saldo, pilihan yang lebih aman tetap `private` ditambah method resmi, misalnya *setter* atau method `protected` yang memeriksa nilainya. KedaiKita mengikuti pola ini: tidak ada satu pun field `protected` di kelas `Menu`.

## 6. Kelas Akar `Object` dan `instanceof`

File: [`contoh/Contoh06KelasAkarDanCekTipe.java`](contoh/Contoh06KelasAkarDanCekTipe.java)

```java
/** Kelas induk semua alat musik. */
class AlatMusik { // [1] tidak menulis extends -> otomatis mewarisi Object
    private String nama;

    public AlatMusik(String nama) {
        this.nama = nama;
    }

    @Override // [2] override toString() bawaan Object
    public String toString() {
        return "Alat musik " + nama;
    }
}

/** Gitar adalah AlatMusik. Hanya punya konstruktor yang meneruskan nama. */
class Gitar extends AlatMusik {
    public Gitar(String nama) {
        super(nama);
    }
}
```

Kelas `Drum` ditulis persis seperti `Gitar`. Isi method `main`:

```java
        AlatMusik gitar = new Gitar("gitar akustik"); // variabel bertipe induk, objeknya Gitar
        AlatMusik drum = new Drum("drum elektrik");

        System.out.println("=== TEKS OBJEK ===");
        System.out.println(gitar); // [3] memanggil toString() warisan dari AlatMusik
        System.out.println(drum);

        System.out.println();
        System.out.println("=== CEK TIPE OBJEK ===");
        System.out.println("gitar adalah Gitar?        " + yaTidak(gitar instanceof Gitar)); // [4]
        System.out.println("gitar adalah AlatMusik?    " + yaTidak(gitar instanceof AlatMusik));
        System.out.println("gitar adalah Drum?         " + yaTidak(gitar instanceof Drum));
        System.out.println("gitar termasuk kelas akar? " + yaTidak(gitar instanceof Object));
        System.out.println("Kelas persis gitar: " + gitar.getClass().getSimpleName()); // [5]
        System.out.println("Kelas persis gitar = AlatMusik? "
                + yaTidak(gitar.getClass() == AlatMusik.class));

        System.out.println();
        System.out.println("=== CEK HUBUNGAN KELAS ===");
        System.out.println("Gitar turunan AlatMusik? "
                + yaTidak(AlatMusik.class.isAssignableFrom(Gitar.class))); // [6]
        System.out.println("AlatMusik turunan Gitar? "
                + yaTidak(Gitar.class.isAssignableFrom(AlatMusik.class)));

        System.out.println();
        System.out.println("=== KESAMAAN BAWAAN DARI KELAS AKAR ===");
        AlatMusik kembaran = new Gitar("gitar akustik"); // isi sama, tetapi objek berbeda
        System.out.println("gitar sama dengan kembarannya? "
                + yaTidak(gitar.equals(kembaran))); // [7] equals() warisan Object
        System.out.println("gitar sama dengan dirinya?     " + yaTidak(gitar.equals(gitar)));
```

**Output:**

```text
=== TEKS OBJEK ===
Alat musik gitar akustik
Alat musik drum elektrik

=== CEK TIPE OBJEK ===
gitar adalah Gitar?        ya
gitar adalah AlatMusik?    ya
gitar adalah Drum?         tidak
gitar termasuk kelas akar? ya
Kelas persis gitar: Gitar
Kelas persis gitar = AlatMusik? tidak

=== CEK HUBUNGAN KELAS ===
Gitar turunan AlatMusik? ya
AlatMusik turunan Gitar? tidak

=== KESAMAAN BAWAAN DARI KELAS AKAR ===
gitar sama dengan kembarannya? tidak
gitar sama dengan dirinya?     ya
```

Penjelasan:

- **[1]** `class AlatMusik` sama artinya dengan `class AlatMusik extends Object`. Setiap kelas Java berakar pada `java.lang.Object`.
- **[2]** `Object` sudah punya `toString()` bawaan. Tanpa *override*, `System.out.println(gitar)` mencetak teks seperti `Gitar@1b6d3586`, dengan angka yang bisa berubah setiap kali program dijalankan. Itulah sebabnya sejak Pertemuan 03 kita menulis `@Override public String toString()`.
- **[3]** `Gitar` tidak menulis `toString()`, jadi memakai versi warisan dari `AlatMusik`.
- **[4]** `objek instanceof Kelas` menjawab apakah objek termasuk kelas itu **atau turunannya**.
- **[5]** `getClass()` hanya melihat kelas **persisnya**. Karena itu, `gitar.getClass() == AlatMusik.class` bernilai `false`. Untuk memeriksa jenis objek, utamakan `instanceof`.
- **[6]** `A.class.isAssignableFrom(B.class)` menjawab "apakah B turunan A?". Ini padanan `issubclass` di Python. Perhatikan urutannya yang terbalik. Method ini jarang dipakai sehari-hari.
- **[7]** `equals()` bawaan dari `Object` hanya bernilai `true` untuk objek yang **sama persis**, sama seperti `==`. Cara mengubah aturan ini dibahas di Pertemuan 12.

> [!NOTE]
> Perhatikan baris pertama `main`: variabel bertipe `AlatMusik` diisi objek `Gitar`. Ini sah karena gitar **adalah** alat musik. Detailnya dibahas di Pertemuan 09. Jika variabelnya bertipe `Gitar`, *compiler* menolak `gitar instanceof Drum` dengan pesan `incompatible types: Gitar cannot be converted to Drum`, karena sebuah `Gitar` mustahil menjadi `Drum`. *Compiler* Java memang secerdas itu.

## 7. is-a atau has-a?

File: [`contoh/Contoh07IsADanHasA.java`](contoh/Contoh07IsADanHasA.java)

Contoh ini membandingkan dua rancangan untuk "mobil dan mesinnya". Kelas `Mesin` sederhana saja: field `cc` dan method `hidupkan()` yang mengembalikan teks seperti `"Mesin 1300 cc menyala"`.

```java
/** Rancangan keliru: mobil mewarisi mesin hanya demi memakai hidupkan(). */
class MobilKeliru extends Mesin { // [1] KELIRU: mobil dianggap "adalah" mesin
    private String nama;

    public MobilKeliru(String nama, int cc) {
        super(cc);
        this.nama = nama;
    }

    public String jalan() {
        return nama + ": " + hidupkan();
    }
}

/** Rancangan tepat: mobil MENYIMPAN objek Mesin sebagai field. */
class MobilTepat { // [2] TEPAT: mobil "punya" mesin
    private String nama;
    private Mesin mesin; // [3] has-a: field berisi objek lain

    public MobilTepat(String nama, Mesin mesin) {
        this.nama = nama;
        this.mesin = mesin;
    }

    public String jalan() {
        return nama + ": " + mesin.hidupkan(); // [4] tugas diteruskan ke objek mesin
    }

    public void gantiMesin(Mesin mesinBaru) { // [5] bagiannya bisa diganti
        this.mesin = mesinBaru;
    }
}
```

**Output:**

```text
=== RANCANGAN KELIRU: MOBIL MEWARISI MESIN ===
Avanza: Mesin 1300 cc menyala
Avanza adalah Mesin? ya (janggal!)

=== RANCANGAN TEPAT: MOBIL PUNYA MESIN ===
Xenia: Mesin 1300 cc menyala
Setelah ganti mesin -> Xenia: Mesin 1500 cc menyala
```

Penjelasan:

- **[1]** `MobilKeliru` mewarisi `Mesin` hanya agar bisa memakai `hidupkan()`. Programnya berjalan, tetapi `avanza instanceof Mesin` bernilai `true`. Menurut program, Avanza **adalah** sebuah mesin. Janggal!
- **[2]** `MobilTepat` tidak mewarisi apa pun selain `Object`. Ia **menyimpan** objek `Mesin`.
- **[3]** Inilah hubungan *has-a*, wujudnya sama seperti relasi antarkelas di Pertemuan 05.
- **[4]** Mobil **meneruskan** tugas menghidupkan mesin ke objek mesinnya. Teknik ini disebut **delegasi**.
- **[5]** Karena mesin hanyalah field, mesin bisa diganti kapan saja. `MobilKeliru` tidak bisa melakukannya.

Sebelum menulis `class X extends Y`, ucapkan "X **adalah** Y". Jika kalimatnya janggal, gunakan field (*has-a*). Prinsip ini dikenal sebagai ***composition over inheritance***.

## 8. Satu Induk Saja, dan Kata Kunci `final`

Bagian ini tidak punya file contoh. Kita langsung melihat apa yang ditolak *compiler*.

### Hanya boleh satu induk

Python mengizinkan pewarisan ganda (contoh 08 di jalur Python). Java **tidak**. Kode berikut ditolak:

```java
class MobilAmfibi extends KendaraanDarat, KendaraanAir {
}
```

```text
E6.java:12: error: '{' expected
class MobilAmfibi extends KendaraanDarat, KendaraanAir {
                                        ^
1 error
```

Setelah satu nama kelas induk, Java mengharapkan `{`, bukan koma. Untuk menggabungkan beberapa "kemampuan", Java memakai *interface* (Pertemuan 10), yang boleh diterapkan banyak sekaligus, atau *has-a* seperti di bagian 7.

### `final` pada kelas

Kelas yang diberi `final` tidak bisa diwarisi. Contoh terkenalnya adalah `String` milik Java sendiri:

```java
class TeksSaya extends String {
}
```

```text
E7.java:6: error: cannot inherit from final String
class TeksSaya extends String {
                       ^
1 error
```

### `final` pada method, dan alasannya di KedaiKita

Method `final` tidak bisa di-*override*. Di studi kasus, `Menu.setHarga()` dan `Makanan.setLevelPedas()` sengaja dibuat `final`. Jika ada kelas anak yang mencoba menimpanya:

```java
class Makanan extends Menu {
    @Override
    public void setHarga(int harga) {
        System.out.println("Harga makanan diubah");
    }
}
```

```text
E8.java:16: error: setHarga(int) in Makanan cannot override setHarga(int) in Menu
    public void setHarga(int harga) {
                ^
  overridden method is final
1 error
```

Mengapa dikunci? Ingat urutan konstruktor di bagian 4. Konstruktor `Menu` memanggil `setHarga()`, dan konstruktor `Makanan` memanggil `setLevelPedas()`. Andaikan kelas anak boleh menimpa method itu, versi anak akan berjalan **saat lapis anak belum selesai diisi**, sehingga bisa membaca field yang masih kosong (`0` atau `null`). Dengan `final`, method itu dijamin tidak diganti, jadi aman dipanggil dari konstruktor.

JDK 21 ke atas bahkan bisa memperingatkan situasi ini jika kita meminta pemeriksaan tambahan dengan opsi `-Xlint`. Berikut yang muncul jika kata `final` pada `setLevelPedas` dihapus, lalu studi kasus dikompilasi dengan `javac -Xlint:all *.java`:

```text
Makanan.java:8: warning: [this-escape] possible 'this' escape before subclass is fully initialized
        setLevelPedas(levelPedas); // lewat setter, jadi ikut divalidasi
                     ^
1 warning
```

Secara sederhana, artinya: "objek ini sudah 'kabur' ke method yang bisa ditimpa, padahal kelas turunannya belum selesai disiapkan". Ini hanya **peringatan**, jadi program tetap bisa dijalankan. Namun peringatan seperti ini sebaiknya ditanggapi, dan `final` adalah cara termudah untuk menghilangkannya.

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/Menu.java`](studi-kasus/Menu.java), [`studi-kasus/Makanan.java`](studi-kasus/Makanan.java), [`studi-kasus/Minuman.java`](studi-kasus/Minuman.java), dan [`studi-kasus/Main.java`](studi-kasus/Main.java)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-makanan-dan-minuman).

**Apa yang berubah dibanding Pertemuan 05/06?**

- Dua file baru: `Makanan.java` (dengan `levelPedas` 0 sampai 5) dan `Minuman.java` (dengan `dingin`). Keduanya `extends Menu`.
- `Menu.java` hanya berubah komentarnya. Kodenya sama, termasuk `setHarga()` yang sudah `final` sejak Pertemuan 05.
- `Main.java` membuat semua menu sebagai `Makanan` atau `Minuman`, lalu menambah bagian "CEK PEWARISAN" dan "MENAMBAH MENU BARU".
- `Pesanan.java`, `ItemPesanan.java`, `Kedai.java`, `Pelanggan.java`, dan `Rupiah.java` **tidak berubah sama sekali**.

Isi lengkap `Makanan.java`:

```java
/** Menu kategori makanan. Tambahan: level pedas 0 sampai 5. */
public class Makanan extends Menu {
    private int levelPedas;

    public Makanan(String kode, String nama, int harga, int stok, int levelPedas) {
        // Panggil konstruktor induk. Kategori diisi otomatis "Makanan".
        super(kode, nama, harga, "Makanan", stok);
        setLevelPedas(levelPedas); // lewat setter, jadi ikut divalidasi
    }

    public int getLevelPedas() {
        return levelPedas;
    }

    // final: setter ini tidak bisa di-override oleh kelas anak,
    // sehingga aman dipanggil dari konstruktor.
    public final void setLevelPedas(int levelPedas) {
        if (levelPedas < 0 || levelPedas > 5) {
            throw new IllegalArgumentException("Level pedas harus 0 sampai 5");
        }
        this.levelPedas = levelPedas;
    }

    @Override
    public String toString() {
        // Override: pakai teks dari induk, lalu tambahkan info pedas
        return super.toString() + " | pedas level " + levelPedas;
    }
}
```

`Minuman.java` berpola sama: `extends Menu`, field `dingin`, konstruktor yang memanggil `super(kode, nama, harga, "Minuman", stok)`, getter `isDingin()`, dan *override* berikut:

```java
    @Override
    public String toString() {
        String suhu = dingin ? "dingin" : "panas";
        return super.toString() + " | " + suhu;
    }
```

- **Konstruktor anak** tidak menerima kategori. Kategori `"Makanan"`/`"Minuman"` dikirim otomatis ke `super(...)` di baris pertama. Semua validasi milik `Menu` (stok tidak negatif, harga lebih dari 0) tetap berjalan, karena dikerjakan oleh konstruktor induk.
- **`setLevelPedas(levelPedas)`** dipanggil dari konstruktor agar nilai 0 sampai 5 ikut diperiksa sejak objek dibuat. Karena itulah method ini `final` (bagian 8).
- **`toString()` di-override** dengan gaya "memperluas": `super.toString()` menghasilkan teks lengkap dari `Menu`, lalu ditambah keterangan pedas atau suhu.

Bagian baru di `Main.java` (di dalam `main`):

```java
        System.out.println("=== CEK PEWARISAN ===");
        Menu kopi = kedai.cariMenu("M01");
        Menu nasi = kedai.cariMenu("M03");
        System.out.println(kopi.getNama() + " termasuk Minuman? "
                + yaTidak(kopi instanceof Minuman));
        System.out.println(kopi.getNama() + " termasuk Menu? "
                + yaTidak(kopi instanceof Menu));
        System.out.println(nasi.getNama() + " termasuk Minuman? "
                + yaTidak(nasi instanceof Minuman));
        System.out.println("Kategori " + nasi.getNama() + ": " + nasi.getKategori());
        String hargaPromo = Rupiah.format(kopi.hargaSetelahDiskon(10));
        System.out.println("Diskon 10% untuk " + kopi.getNama() + " (method warisan Menu): "
                + hargaPromo);
```

- **`siapkanKedai()`** kini membuat menu dengan `new Minuman(...)` dan `new Makanan(...)`, lalu mendaftarkannya lewat `kedai.tambahMenu(Menu menu)`. Parameter bertipe `Menu` boleh diisi `Minuman` atau `Makanan`, karena keduanya **adalah** `Menu`. Hal yang sama berlaku untuk `Pesanan.tambahItem(Menu menu, int jumlah)`.
- **`Menu kopi = kedai.cariMenu("M01")`**: variabel bertipe `Menu` berisi objek `Minuman`. `kopi instanceof Minuman` tetap menjawab `true`, karena yang diperiksa adalah objeknya.
- **`hargaSetelahDiskon(10)`** dan **`getKategori()`** tidak ditulis di kelas anak. Keduanya warisan dari `Menu`.
- **Bagian "MENAMBAH MENU BARU"** membuat `new Minuman("M06", "Kopi Tubruk", 12000, 25, false)`, lalu mencoba `new Makanan("M07", "Seblak Super Pedas", 20000, 10, 9)`. Level 9 ditolak oleh `setLevelPedas()`, lalu ditangkap dengan `try`/`catch` seperti di Pertemuan 04.

Jalankan dengan `javac *.java` lalu `java Main` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

**Output:**

```text
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 12 | pedas level 0

=== CEK PEWARISAN ===
Kopi Susu Gula Aren termasuk Minuman? ya
Kopi Susu Gula Aren termasuk Menu? ya
Nasi Goreng Kampung termasuk Minuman? tidak
Kategori Nasi Goreng Kampung: Makanan
Diskon 10% untuk Kopi Susu Gula Aren (method warisan Menu): Rp16.200

=== MENAMBAH MENU BARU ===
Ditambahkan: [M06] Kopi Tubruk (Minuman) - Rp12.000 | stok 25 | panas
Gagal menambah menu: Level pedas harus 0 sampai 5

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
----------------------------------------
1 x Kopi Tubruk                 Rp12.000
2 x Pisang Goreng Keju          Rp30.000
----------------------------------------
TOTAL                           Rp42.000
========================================

=== SETELAH TRANSAKSI ===
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 10 | pedas level 0
[M06] Kopi Tubruk (Minuman) - Rp12.000 | stok 24 | panas
Jumlah pesanan tercatat: 2
```

Output ini **identik** dengan versi Python. Perhatikan daftar menu: method `tampilkanMenu()` di `Kedai.java` hanya menulis `System.out.println(menu)` tanpa tahu jenisnya, tetapi setiap baris tampil dengan keterangan yang tepat. Setiap objek memakai `toString()` miliknya sendiri (dibahas tuntas di Pertemuan 09). Di struk, `kurangiStok()` warisan `Menu` juga bekerja sama baiknya untuk makanan maupun minuman.

> [!TIP]
> **Coba sendiri:**
> 1. Di `siapkanKedai()`, tambahkan `kedai.tambahMenu(new Minuman("M07", "Teh Tarik", 12000, 20, false));`. Tanpa mengubah kelas lain, apakah menu itu langsung tampil lengkap?
> 2. Hapus kata `final` dari `setLevelPedas` di `Makanan.java`, lalu kompilasi dengan `javac -Xlint:all *.java`. Peringatan apa yang muncul? Kembalikan lagi kata `final` setelahnya.

<details>
<summary>Lihat jawaban</summary>

1. Ya. Baris `[M07] Teh Tarik (Minuman) - Rp12.000 | stok 20 | panas` langsung muncul di daftar menu. `Kedai` tidak perlu diubah, karena Teh Tarik adalah `Menu`.
2. Dengan JDK 21 ke atas, muncul peringatan `[this-escape] possible 'this' escape before subclass is fully initialized` seperti di bagian 8. Program tetap bisa dijalankan, tetapi peringatan itu menandakan rancangan yang berisiko. Dengan JDK 17, opsi `-Xlint` belum punya pemeriksaan ini, jadi tidak ada peringatan.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Sebagian besar kesalahan pewarisan di Java tertangkap saat **kompilasi**. Pesannya diawali nama file dan nomor baris, dan tanda `^` menunjuk posisi masalahnya.

### Kesalahan 1: Lupa memanggil `super(...)`

```java
class Motor extends Kendaraan {
    private String transmisi;

    public Motor(String merek, String transmisi) {
        this.transmisi = transmisi; // lupa super(merek)
    }
}
```

Pesan error-nya (`Kendaraan` hanya punya konstruktor `Kendaraan(String merek)`):

```text
E1.java:18: error: constructor Kendaraan in class Kendaraan cannot be applied to given types;
    public Motor(String merek, String transmisi) {
                                                 ^
  required: String
  found:    no arguments
  reason: actual and formal argument lists differ in length
1 error
```

**Artinya:** karena tidak ada `super(...)`, Java diam-diam menyisipkan `super()` **tanpa argumen**. Padahal `Kendaraan` hanya punya konstruktor yang menerima `String` (*required: String*). **Perbaikan:** tulis `super(merek);` di baris pertama konstruktor `Motor`.

### Kesalahan 2: `super(...)` bukan di baris pertama

Misalkan konstruktor `Motor` menulis `this.transmisi = transmisi;` lebih dulu, baru `super(merek);`. Pesan error-nya (dicoba dengan JDK 21 dan `javac --release 17`):

```text
E2.java:20: error: call to super must be first statement in constructor
        super(merek);
             ^
1 error
```

**Artinya:** di Java 17, konstruktor induk harus dipanggil paling awal, agar lapis induk selalu siap lebih dulu. **Perbaikan:** pindahkan `super(merek);` ke baris pertama.

> [!NOTE]
> Java 25 melonggarkan aturan ini: beberapa pernyataan tertentu boleh ditulis sebelum `super(...)`, sehingga JDK yang lebih baru bisa menampilkan pesan yang berbeda. Kebiasaan menulis `super(...)` di baris pertama tetap aman di semua versi.

### Kesalahan 3: Mengakses field private milik induk

Misalkan method `deskripsi()` di `Motor` menyebut field `merek` milik `Kendaraan` secara langsung:

```text
E3.java:25: error: merek has private access in Kendaraan
        return "Motor: " + merek + ", transmisi " + transmisi;
                           ^
1 error
```

**Artinya:** `merek` adalah field `private` milik `Kendaraan`. Kelas anak pun tidak boleh menyebutnya langsung. **Perbaikan:** pakai method warisan, misalnya `getMerek()` atau `info()`. Jika kelas anak memang perlu akses langsung, pertimbangkan `protected` (bagian 5).

### Kesalahan 4: Salah ketik nama method yang di-`@Override`

```java
class TiketVIP extends Tiket {
    @Override
    public String inf0() {
        return "Tiket VIP";
    }
}
```

```text
E4.java:14: error: method does not override or implement a method from a supertype
    @Override
    ^
1 error
```

**Artinya:** `@Override` berjanji bahwa method di bawahnya menimpa method induk. Karena `Tiket` tidak punya method `inf0()` (dengan angka nol), janji itu dilanggar. Tanpa `@Override`, kesalahan ini lolos diam-diam dan versi induk yang berjalan. Inilah alasan untuk **selalu** menulis `@Override`. **Perbaikan:** ganti menjadi `info()`.

### Kesalahan 5: Memperkecil hak akses saat override

```java
class TiketVIP extends Tiket {
    @Override
    String info() {
        return "Tiket VIP";
    }
}
```

```text
E5.java:15: error: info() in TiketVIP cannot override info() in Tiket
    String info() {
           ^
  attempting to assign weaker access privileges; was public
1 error
```

**Artinya:** `info()` milik `Tiket` bersifat `public`, sedangkan versi `TiketVIP` tanpa *modifier* (lebih sempit). Aturan *override* melarang anak mempersempit hak akses, karena semua kode yang boleh memanggil `info()` pada sebuah `Tiket` harus tetap boleh memanggilnya pada `TiketVIP`. **Perbaikan:** tulis `public String info()`.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK. Fokuslah pada kata kuncinya, seperti `cannot be applied`, `private access`, `does not override`, dan `weaker access privileges`.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| Kelas anak | `class Anak extends Induk { ... }` | `public class Makanan extends Menu` |
| Memanggil konstruktor induk | `super(...);` di baris pertama | `super(kode, nama, harga, "Makanan", stok);` |
| Menimpa method | `@Override` + tanda tangan sama | `@Override public String toString()` |
| Memakai versi induk | `super.namaMethod(...)` | `super.toString()` |
| Field untuk kelas anak | `protected Tipe nama;` | `protected int saldo;` |
| Cek objek termasuk kelas | `objek instanceof Kelas` | `kopi instanceof Menu` |
| Kelas persis sebuah objek | `objek.getClass()` | `gitar.getClass().getSimpleName()` |
| Cek kelas turunan | `Induk.class.isAssignableFrom(Anak.class)` | `AlatMusik.class.isAssignableFrom(Gitar.class)` |
| Mengunci kelas | `final class Nama` | `String` adalah kelas `final` |
| Mengunci method | `public final void nama(...)` | `public final void setHarga(int harga)` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
