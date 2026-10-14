# ☕ Praktik Java — Pertemuan 12: Koleksi dan Generics

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 12](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [List: Interface dan Wujudnya](#1-list-interface-dan-wujudnya)
2. [Set: HashSet dan TreeSet](#2-set-hashset-dan-treeset)
3. [Map: Mencari Lewat Kunci](#3-map-mencari-lewat-kunci)
4. [Menjelajahi Map dan Menjaga Urutan](#4-menjelajahi-map-dan-menjaga-urutan)
5. [Mengurutkan dengan Comparator dan Lambda](#5-mengurutkan-dengan-comparator-dan-lambda)
6. [Urutan Alami dengan `Comparable`](#6-urutan-alami-dengan-comparable)
7. [Kesamaan Objek: `equals` dan `hashCode`](#7-kesamaan-objek-equals-dan-hashcode)
8. [Generics dan Kelas Pembungkus `Integer`](#8-generics-dan-kelas-pembungkus-integer)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Java pertemuan ini:

```text
java/
├── contoh/          <- 9 contoh program satu file (contoh 09 khusus Java)
├── studi-kasus/     <- KedaiKita versi Pertemuan 12 (satu kelas per file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Setiap contoh adalah program satu file. Studi kasus terdiri atas banyak file, jadi kompilasi semuanya dulu, lalu jalankan kelas `Main`:

```bash
cd Pertemuan-12-Koleksi-dan-Generics/java/contoh
java Contoh01ListDanListTetap.java

cd ../studi-kasus
javac *.java
java Main
```

> [!TIP]
> Di VS Code, buka folder `java/` **milik pertemuan ini** saja (File → Open Folder), karena nama kelas di dalam satu folder harus unik. Semua kelas koleksi berada di paket `java.util`, jadi setiap file diawali beberapa baris `import java.util.List;` dan seterusnya. Panduan lengkap ada di [00-Persiapan](../../00-Persiapan/README.md).

## 1. List: Interface dan Wujudnya

File: [`contoh/Contoh01ListDanListTetap.java`](contoh/Contoh01ListDanListTetap.java)

`ArrayList` sudah kamu pakai sejak Pertemuan 05. Kali ini kita lihat kemampuannya lebih lengkap, lalu membandingkannya dengan list **tetap** buatan `List.of`.

```java
        List<String> belanja = new ArrayList<>(List.of("beras", "telur", "minyak")); // [1]
        System.out.println("=== LIST: DAFTAR BELANJA ANAK KOS ===");
        System.out.println("Isi awal      : " + String.join(", ", belanja));

        belanja.add("gula");      // [2] tambah di akhir
        belanja.add(0, "kopi");   // sisipkan di indeks 0 (paling depan)
        belanja.remove("minyak"); // [3] hapus berdasarkan ISI, bukan indeks
        belanja.add("telur");     // data kembar boleh
        System.out.println("Setelah diubah: " + String.join(", ", belanja));
        System.out.println("Jumlah item   : " + belanja.size());
        System.out.println("Item pertama  : " + belanja.get(0)); // [4] akses lewat indeks
        System.out.println("Item terakhir : " + belanja.get(belanja.size() - 1));
        if (belanja.contains("gula")) { // [5] cek keanggotaan
            System.out.println("Posisi gula   : indeks " + belanja.indexOf("gula"));
        }
        System.out.println("Telur dicatat : " + Collections.frequency(belanja, "telur") + " kali");

        System.out.println();
        System.out.println("=== DATA TETAP: HARI KULIAH PBO ===");
        List<String> hariKuliah = List.of("Senin", "Rabu"); // [6] list tetap (immutable)
        System.out.println("Hari kuliah   : " + String.join(", ", hariKuliah));
        try {
            hariKuliah.set(0, "Selasa"); // [7] mencoba mengubah isi list tetap
        } catch (UnsupportedOperationException e) {
            System.out.println("Gagal mengubah: isinya tetap (immutable)");
        }
```

Bagian terakhir program membuat dua list baru, `hurufBesar` dan `pendek`, dengan perulangan for biasa (penanda **[8]** dan **[9]** di file).

**Output:**

```text
=== LIST: DAFTAR BELANJA ANAK KOS ===
Isi awal      : beras, telur, minyak
Setelah diubah: kopi, beras, telur, gula, telur
Jumlah item   : 5
Item pertama  : kopi
Item terakhir : telur
Posisi gula   : indeks 3
Telur dicatat : 2 kali

=== DATA TETAP: HARI KULIAH PBO ===
Hari kuliah   : Senin, Rabu
Gagal mengubah: isinya tetap (immutable)

=== MEMBUAT LIST BARU DARI LIST LAMA ===
Huruf besar   : KOPI, BERAS, TELUR, GULA, TELUR
Nama pendek   : kopi, gula
List asli     : kopi, beras, telur, gula, telur
```

Penjelasan:

- **[1]** Tipe variabelnya `List<String>` (kontrak), objeknya `ArrayList` (wujud). `List.of(...)` membuat list tetap berisi tiga teks, lalu `new ArrayList<>(...)` menyalinnya ke list yang **bisa** diubah. `String.join(", ", ...)` dipakai agar hasil cetaknya rapi.
- **[2]** `add(x)` menambah di akhir, sedangkan `add(indeks, x)` menyisipkan di posisi tertentu.
- **[3]** `remove(x)` menghapus isi **pertama** yang `equals()` dengan `x`, lalu mengembalikan `true`/`false`. Hati-hati dengan `List<Integer>`: `remove(1)` justru berarti "hapus indeks 1" (contoh 09).
- **[4]** `get(indeks)` mengambil isi. Java tidak punya indeks negatif, jadi item terakhir diambil dengan `get(size() - 1)`.
- **[5]** `contains()` memeriksa keanggotaan satu per satu dari depan. Ada juga `indexOf()` dan `Collections.frequency()` untuk menghitung kemunculan.
- **[6]** `List.of(...)` membuat list **tetap**. Java tidak punya tuple, dan inilah padanan terdekatnya.
- **[7]** Mengubah list tetap memunculkan `UnsupportedOperationException`, yang kita tangkap seperti di Pertemuan 11.
- **[8]** dan **[9]** Python punya *list comprehension*. Di Java, kita memakai perulangan biasa dengan `if` di dalamnya (atau *Stream* sebagai bonus, lihat contoh 05). List aslinya tidak berubah.

## 2. Set: HashSet dan TreeSet

File: [`contoh/Contoh02SetHimpunan.java`](contoh/Contoh02SetHimpunan.java)

Pendaftaran workshop sering kacau karena ada yang mengisi formulir dua kali. Set membereskannya secara otomatis.

```java
    /** Mencetak isi set dalam urutan abjad agar hasilnya selalu sama. */
    static void cetak(String judul, Set<String> isi) {
        Set<String> urut = new TreeSet<>(isi); // [5] TreeSet: isinya selalu urut
        System.out.println(String.format("%-14s: %s", judul, String.join(", ", urut)));
    }

    public static void main(String[] args) {
        List<String> pendaftar = List.of("Ayu", "Bima", "Citra", "Ayu", "Dimas", "Bima"); // [1]
        Set<String> pesertaPython = new HashSet<>(pendaftar); // [2] duplikat hilang
        Set<String> pesertaJava = new HashSet<>(List.of("Citra", "Eka", "Ayu", "Fajar")); // [3]

        System.out.println("=== PENDAFTARAN WORKSHOP PYTHON ===");
        System.out.println("Formulir masuk: " + pendaftar.size());
        System.out.println("Peserta unik  : " + pesertaPython.size());
        cetak("Peserta Python", pesertaPython);
        pesertaPython.add("Eka"); // [4] tambah anggota baru (add mengembalikan true)
        pesertaPython.add("Ayu"); // sudah ada: diabaikan (add mengembalikan false)
        System.out.println("Setelah tambah Eka dan Ayu: " + pesertaPython.size() + " peserta");

        System.out.println();
        System.out.println("=== OPERASI HIMPUNAN ===");
        cetak("Peserta Java", pesertaJava);
        Set<String> irisan = new HashSet<>(pesertaPython); // [6] salin dulu!
        irisan.retainAll(pesertaJava);
        cetak("Ikut keduanya", irisan);
        Set<String> gabungan = new HashSet<>(pesertaPython);
        gabungan.addAll(pesertaJava);
        cetak("Semua peserta", gabungan);
        Set<String> selisih = new HashSet<>(pesertaPython);
        selisih.removeAll(pesertaJava);
        cetak("Hanya Python", selisih);
        if (!pesertaPython.contains("Fajar")) { // [7] cek keanggotaan
            System.out.println("Fajar belum ikut workshop Python");
        }
```

**Output:**

```text
=== PENDAFTARAN WORKSHOP PYTHON ===
Formulir masuk: 6
Peserta unik  : 4
Peserta Python: Ayu, Bima, Citra, Dimas
Setelah tambah Eka dan Ayu: 5 peserta

=== OPERASI HIMPUNAN ===
Peserta Java  : Ayu, Citra, Eka, Fajar
Ikut keduanya : Ayu, Citra, Eka
Semua peserta : Ayu, Bima, Citra, Dimas, Eka, Fajar
Hanya Python  : Bima, Dimas
Fajar belum ikut workshop Python
```

Penjelasan:

- **[1]** dan **[2]** List `pendaftar` berisi data kembar (Ayu dan Bima dua kali). Konstruktor `new HashSet<>(koleksi)` menyalin isinya, dan data kembar otomatis dibuang, sehingga 6 formulir menjadi 4 peserta.
- **[3]** Set ditulis dengan pola yang sama: tipe kontrak `Set<String>`, wujud `HashSet`.
- **[4]** `add()` mengembalikan `true` jika berhasil menambah, `false` jika isinya sudah ada. Tidak ada error.
- **[5]** Urutan isi `HashSet` **tidak dijamin** ([buktinya di halaman konsep](../README.md#4-urutan-isi-jangan-mengandalkan-kebetulan)). `TreeSet` selalu menyimpan isinya dalam keadaan urut, jadi cocok untuk dicetak. Ada juga `LinkedHashSet` yang menjaga urutan masuk.
- **[6]** `retainAll` (irisan), `addAll` (gabungan), dan `removeAll` (selisih) **mengubah** set yang memanggilnya. Karena itu kita bekerja pada salinan, agar `pesertaPython` tetap utuh.
- **[7]** `contains()` pada `HashSet` sangat cepat, karena langsung menuju "rak" lewat kode hash.

## 3. Map: Mencari Lewat Kunci

File: [`contoh/Contoh03MapPencarian.java`](contoh/Contoh03MapPencarian.java)

File ini berisi kelas `Mahasiswa` sederhana dan method `cariDiList()` yang mencari dengan cara lama: memeriksa list satu per satu sambil menghitung langkahnya. Kita bandingkan dengan `Map`.

```java
        Map<String, Mahasiswa> data = new HashMap<>(); // [1] Map kosong: NIM -> Mahasiswa
        for (Mahasiswa mhs : daftar) {
            data.put(mhs.getNim(), mhs); // [2] simpan dengan kunci NIM
        }

        System.out.println("=== CARI MAHASISWA BERDASARKAN NIM ===");
        System.out.println("Lewat list : " + cariDiList(daftar, "2409106004"));
        System.out.println("Lewat kunci: " + data.get("2409106004")); // [3] langsung lewat kunci
        String nimAsing = "2409106099";
        if (data.containsKey(nimAsing)) { // [4] cek dulu apakah kuncinya ada
            System.out.println(data.get(nimAsing));
        } else {
            System.out.println("NIM " + nimAsing + " tidak terdaftar");
        }
        if (data.get(nimAsing) == null) { // [5] get(): null jika kunci tidak ada
            System.out.println("get() untuk NIM asing: tidak ada hasil");
        }
```

Bagian kedua mencoba tiga operasi lain: `data.put("2409106002", bimaBaru)` dengan kunci yang sudah ada (penanda **[6]**), `data.remove("2409106001")` (**[7]**), dan `pinjaman.getOrDefault("2409106003", 0)` pada map kedua yang mencatat jumlah buku dipinjam (**[8]**).

**Output:**

```text
=== CARI MAHASISWA BERDASARKAN NIM ===
  (list memeriksa 4 data sampai ketemu)
Lewat list : 2409106004 Dimas Pratama (Informatika)
Lewat kunci: 2409106004 Dimas Pratama (Informatika)
NIM 2409106099 tidak terdaftar
get() untuk NIM asing: tidak ada hasil

=== MENGUBAH, MENGHAPUS, DAN NILAI CADANGAN ===
Jumlah data: 4
Bima pindah prodi: 2409106002 Bima Saputra (Sistem Informasi)
Jumlah data: 4
Setelah 2409106001 dihapus: 3 data
Buku dipinjam Citra: 2
Buku dipinjam Dimas: 0
```

Penjelasan:

- **[1]** `Map<String, Mahasiswa>` dibaca "map dengan kunci `String` dan nilai `Mahasiswa`". `HashMap` adalah wujud yang paling umum.
- **[2]** `put(kunci, nilai)` menyimpan pasangan baru.
- **[3]** `get(kunci)` langsung mengambil nilainya, sedangkan list harus memeriksa 4 data dulu. Dengan ribuan mahasiswa, bedanya sangat terasa.
- **[4]** `containsKey()` memeriksa **kunci**. Untuk memeriksa nilai, ada `containsValue()` (tetapi lambat, karena memeriksa satu per satu).
- **[5]** `get()` untuk kunci yang tidak ada mengembalikan `null`, tanpa error. Inilah beda penting dengan Python, yang melempar `KeyError`.
- **[6]** `put()` dengan kunci yang **sudah ada** menimpa nilai lama. Jumlah data tetap 4.
- **[7]** `remove(kunci)` menghapus pasangan berdasarkan kuncinya.
- **[8]** `getOrDefault(kunci, cadangan)` mengembalikan nilai cadangan jika kunci tidak ada. Dimas belum meminjam buku, jadi hasilnya 0.

## 4. Menjelajahi Map dan Menjaga Urutan

File: [`contoh/Contoh04IterasiMap.java`](contoh/Contoh04IterasiMap.java)

Pola paling terkenal dari `Map` adalah **menghitung kemunculan**, misalnya menghitung suara pemilihan ketua himpunan.

```java
        List<String> suara = List.of("Bima", "Ayu", "Bima", "Citra", "Ayu", "Bima"); // [1]
        Map<String, Integer> hitung = new LinkedHashMap<>(); // menjaga urutan masuk
        for (String nama : suara) {
            hitung.put(nama, hitung.getOrDefault(nama, 0) + 1); // [2] belum ada -> mulai dari 0
        }

        System.out.println("=== HASIL PEMILIHAN KETUA HIMPUNAN ===");
        System.out.println("Kandidat   : " + String.join(", ", hitung.keySet())); // [3] kunci saja
        int total = 0;
        for (int jumlah : hitung.values()) { // [4] nilai saja (unboxing Integer -> int)
            total += jumlah;
        }
        System.out.println("Total suara: " + total);
        for (Map.Entry<String, Integer> entri : hitung.entrySet()) { // [5] pasangan kunci-nilai
            System.out.println(entri.getKey() + ": " + entri.getValue() + " suara");
        }

        System.out.println();
        System.out.println("=== URUT NAMA KANDIDAT (A-Z) ===");
        Map<String, Integer> urut = new TreeMap<>(hitung); // [6] TreeMap: kunci selalu urut
        for (Map.Entry<String, Integer> entri : urut.entrySet()) {
            System.out.println(entri.getKey() + ": " + entri.getValue() + " suara");
        }
```

Bagian terakhir membuat `LinkedHashMap` baru bernama `persen` dari isi `hitung` (penanda **[7]**), lalu mencetaknya.

**Output:**

```text
=== HASIL PEMILIHAN KETUA HIMPUNAN ===
Kandidat   : Bima, Ayu, Citra
Total suara: 6
Bima: 3 suara
Ayu: 2 suara
Citra: 1 suara

=== URUT NAMA KANDIDAT (A-Z) ===
Ayu: 2 suara
Bima: 3 suara
Citra: 1 suara

=== PERSENTASE (dibulatkan ke bawah) ===
Bima: 50%
Ayu: 33%
Citra: 16%
```

Penjelasan:

- **[1]** dan **[2]** Setiap isi list adalah satu suara. Pola hitung: ambil jumlah lama (0 jika nama belum ada), tambah 1, lalu simpan lagi. Pola ini juga dipakai di `LaporanPenjualan`.
- **[3]** `keySet()` berisi kunci saja. Karena wujudnya `LinkedHashMap`, urutannya sesuai urutan kunci **pertama kali** dimasukkan: Bima dulu.
- **[4]** `values()` berisi nilai saja. Isinya `Integer`, tetapi boleh langsung ditampung variabel `int` (dibuka otomatis, lihat bagian 8).
- **[5]** `entrySet()` berisi pasangan `Map.Entry<K, V>`. Ambil isinya dengan `getKey()` dan `getValue()`.
- **[6]** `new TreeMap<>(hitung)` menyalin isi map ke `TreeMap`, yang selalu mengurutkan kuncinya.
- **[7]** Python punya *dict comprehension*. Di Java, kita membangun map baru dengan perulangan.

| Wujud `Map` | Urutan saat dijelajahi | Kapan dipakai |
|---|---|---|
| `HashMap` | tidak dijamin | pilihan umum jika urutan tidak penting |
| `LinkedHashMap` | sesuai urutan kunci dimasukkan | perilakunya seperti `dict` Python |
| `TreeMap` | kunci selalu urut | laporan yang harus urut abjad atau angka |

## 5. Mengurutkan dengan Comparator dan Lambda

File: [`contoh/Contoh05SortingComparator.java`](contoh/Contoh05SortingComparator.java)

Toko online selalu punya tombol "Termurah", "Terlaris", dan "Rating". Datanya sama, aturan urutnya berbeda. Inilah **urutan khusus**. File ini berisi kelas `Produk` (dengan getter `getNama()`, `getHarga()`, `getRating()`, `getTerjual()`) dan method `tampilkan()` yang mencetak judul lalu setiap produk.

```java
        List<Produk> termurah = new ArrayList<>(daftar); // [1] salin dulu: sort mengubah list
        termurah.sort((a, b) -> Integer.compare(a.getHarga(), b.getHarga())); // [2] lambda
        tampilkan("TERMURAH", termurah);

        List<Produk> terlaris = new ArrayList<>(daftar);
        terlaris.sort(Comparator.comparing(Produk::getTerjual).reversed()); // [3]
        tampilkan("TERLARIS", terlaris);

        List<Produk> rating = new ArrayList<>(daftar);
        rating.sort(Comparator.comparing(Produk::getRating).reversed()
                .thenComparing(Produk::getHarga)); // [4] dua kriteria
        tampilkan("RATING TERTINGGI, LALU TERMURAH", rating);

        System.out.println("=== LAIN-LAIN ===");
        List<Produk> urutNama = new ArrayList<>(daftar);
        urutNama.sort(Comparator.comparing(p -> p.getNama())); // [5] lambda sebagai kunci
        List<String> nama = new ArrayList<>();
        for (Produk p : urutNama) {
            nama.add(p.getNama());
        }
        System.out.println("Nama A-Z      : " + String.join(", ", nama));
        Produk murah = Collections.min(daftar, Comparator.comparing(Produk::getHarga)); // [6]
        Produk mahal = Collections.max(daftar, Comparator.comparing(Produk::getHarga));
        System.out.println("Paling murah  : " + murah.getNama());
        System.out.println("Paling mahal  : " + mahal.getNama());
        System.out.println("Urutan asli tetap, pertama: " + daftar.get(0).getNama()); // [7]
        List<String> rating5 = daftar.stream() // [8] bonus: Stream (boleh dilewati)
                .filter(p -> p.getRating() == 5)
                .map(Produk::getNama)
                .toList();
        System.out.println("Rating 5      : " + String.join(", ", rating5));
```

Sebelum potongan ini, `daftar` diisi lima produk dengan `List.of(...)`, lalu dicetak sebagai URUTAN ASLI. Bagian berikutnya:

**Output:**

```text
=== TERMURAH ===
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210
Headset Gaming        Rp150.000  rating 5  terjual 95

=== TERLARIS ===
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Headset Gaming        Rp150.000  rating 5  terjual 95

=== RATING TERTINGGI, LALU TERMURAH ===
Flashdisk 64GB         Rp85.000  rating 5  terjual 120
Headset Gaming        Rp150.000  rating 5  terjual 95
Kabel Data USB-C       Rp25.000  rating 4  terjual 520
Mouse Wireless         Rp75.000  rating 4  terjual 340
Powerbank 10000mAh    Rp125.000  rating 4  terjual 210

=== LAIN-LAIN ===
Nama A-Z      : Flashdisk 64GB, Headset Gaming, Kabel Data USB-C, Mouse Wireless, Powerbank 10000mAh
Paling murah  : Kabel Data USB-C
Paling mahal  : Headset Gaming
Urutan asli tetap, pertama: Flashdisk 64GB
Rating 5      : Flashdisk 64GB, Headset Gaming
```

Penjelasan:

- **[1]** `list.sort(...)` mengurutkan list **itu sendiri**. Lagi pula `daftar` adalah list tetap dari `List.of`, sehingga tidak bisa diurutkan langsung. Karena itu kita selalu mengurutkan **salinan**.
- **[2]** `sort` membutuhkan sebuah `Comparator`: aturan yang menerima dua produk `a` dan `b`, lalu mengembalikan negatif, nol, atau positif. Aturan sesingkat ini ditulis sebagai **lambda**: di kiri panah `->` ada parameternya `(a, b)`, di kanan ada nilai yang dikembalikan (tanpa kata `return`). `Integer.compare(x, y)` menghasilkan angka yang tepat tanpa risiko salah hitung.
- **[3]** `Comparator.comparing(kunci)` membuat pembanding dari sebuah "kunci". `Produk::getTerjual` adalah ***method reference***, singkatan dari lambda `p -> p.getTerjual()`. `.reversed()` membalik urutan menjadi terbesar dulu.
- **[4]** `.thenComparing(...)` menambahkan kriteria kedua yang hanya dipakai jika kriteria pertama seri. `.reversed()` di sini hanya membalik rating, karena ditulis sebelum `thenComparing`.
- **[5]** Kunci juga boleh ditulis sebagai lambda biasa: `p -> p.getNama()`.
- **[6]** `Collections.min()` dan `Collections.max()` juga menerima `Comparator`.
- **[7]** Karena kita selalu bekerja pada salinan, `daftar` tetap pada urutan aslinya.
- **[8]** Bonus: *Stream* menyaring (`filter`) lalu mengambil nama (`map`) dalam satu rantai, mirip list comprehension Python. Stream tidak wajib di mata kuliah ini.

## 6. Urutan Alami dengan `Comparable`

File: [`contoh/Contoh06Comparable.java`](contoh/Contoh06Comparable.java)

Untuk peserta lomba lari, urutan yang paling wajar selalu sama: yang tercepat di depan. Aturan baku seperti ini sebaiknya ditulis **di dalam kelas** sebagai urutan alami.

Kelas `Pelari` dideklarasikan `class Pelari implements Comparable<Pelari>` (penanda **[1]**), lalu mengisi method `compareTo`:

```java
    // [2] negatif: objek ini duluan; positif: objek lain duluan; 0: setara
    @Override
    public int compareTo(Pelari lain) {
        if (waktuDetik != lain.waktuDetik) {
            return Integer.compare(waktuDetik, lain.waktuDetik);
        }
        return Integer.compare(nomor, lain.nomor); // waktu sama: nomor dada kecil dulu
    }
```

Program utamanya (setelah mencetak catatan panitia):

```java
        List<Pelari> peringkat = new ArrayList<>(hasil);
        Collections.sort(peringkat); // [3] tanpa Comparator: memakai compareTo()
        for (int i = 0; i < peringkat.size(); i++) {
            System.out.println((i + 1) + ". " + peringkat.get(i));
        }
        System.out.println("Juara 1: " + Collections.min(hasil).getNama()); // [4]
        Pelari rudi = hasil.get(0);
        Pelari joko = hasil.get(2);
        String jawaban = joko.compareTo(rudi) < 0 ? "ya" : "tidak"; // [5]
        System.out.println("Joko lebih cepat dari Rudi? " + jawaban);
```

Dua bagian terakhir mengurutkan salinan dengan `terlambat.sort(Collections.reverseOrder())` (penanda **[6]**) dan `absensi.sort(Comparator.comparing(Pelari::getNama))` (**[7]**). Sebelum peringkat, program mencetak catatan panitia sesuai urutan di list (Rudi, Maya, Joko, Lina, Fikri). Bagian berikutnya:

**Output:**

```text
=== PERINGKAT (urutan alami: tercepat dulu) ===
1. #112 Maya  18:45
2. #101 Joko  19:58
3. #103 Fikri 19:58
4. #105 Rudi  21:30
5. #108 Lina  25:10
Juara 1: Maya
Joko lebih cepat dari Rudi? ya

=== DARI YANG TERLAMBAT ===
#108 Lina  25:10
#105 Rudi  21:30
#103 Fikri 19:58
#101 Joko  19:58
#112 Maya  18:45

=== ABSENSI (urutan khusus: nama A-Z) ===
Fikri, Joko, Lina, Maya, Rudi
```

Penjelasan:

- **[1]** `Comparable<Pelari>` adalah *interface* bawaan Java (ingat Pertemuan 10). Kontraknya satu method: `compareTo`.
- **[2]** `compareTo` mengembalikan **negatif** jika objek ini harus di depan, **positif** jika objek lain di depan, dan **nol** jika setara. Joko dan Fikri sama-sama 19:58, jadi kriteria kedua (nomor dada) membuat hasilnya selalu pasti.
- **[3]** `Collections.sort(list)` tanpa `Comparator` memakai `compareTo`. Kode ini hanya bisa dikompilasi jika isi list meng-*implements* `Comparable`.
- **[4]** `Collections.min()` mencari isi "terkecil", artinya yang tercepat.
- **[5]** Java tidak mengizinkan `joko < rudi` untuk objek. Kita menulis `joko.compareTo(rudi) < 0`.
- **[6]** `Collections.reverseOrder()` adalah `Comparator` yang membalik urutan alami.
- **[7]** Urutan alami tidak mengunci kita. `Comparator` tetap bisa memberi urutan khusus kapan saja.

## 7. Kesamaan Objek: `equals` dan `hashCode`

File: [`contoh/Contoh07EqualsHashCode.java`](contoh/Contoh07EqualsHashCode.java)

Kita bandingkan dua kelas. `PemilihPolos` tidak meng-*override* apa pun, sedangkan `Pemilih` (dengan getter `getNik()` dan `getNama()`) menganggap dua pemilih sama jika NIK-nya sama:

```java
    @Override
    public boolean equals(Object lain) { // [1] parameternya WAJIB bertipe Object
        if (!(lain instanceof Pemilih)) {
            return false; // bukan Pemilih (atau null): pasti tidak sama
        }
        Pemilih pemilihLain = (Pemilih) lain;
        return nik.equals(pemilihLain.nik);
    }

    @Override
    public int hashCode() { // [2] hash dari data yang SAMA dengan equals()
        return nik.hashCode();
    }
```

Program utamanya mula-mula membuat dua `PemilihPolos` dengan data identik, mencetak `yaTidak(a1.equals(a2))` (penanda **[3]**), lalu jumlah isi `HashSet` yang berisi keduanya. Setelah itu versi B:

```java
        Pemilih b1 = new Pemilih("6472010000000001", "Budi Santoso");
        Pemilih b2 = new Pemilih("6472010000000001", "Budi Santosa"); // salah ketik nama
        Pemilih b3 = new Pemilih("6472010000000002", "Siti Aminah");
        System.out.println("Dianggap sama     : " + yaTidak(b1.equals(b2))); // [4]
        System.out.println("Objek sama persis : " + yaTidak(b1 == b2));
        System.out.println("Kode hash sama    : " + yaTidak(b1.hashCode() == b2.hashCode()));
        Set<Pemilih> dpt = new HashSet<>(); // DPT = daftar pemilih tetap
        dpt.add(b1);
        dpt.add(b2); // [5] NIK sudah ada: diabaikan (add mengembalikan false)
        dpt.add(b3);
```

Isi set lalu disalin ke `ArrayList` dan diurutkan berdasarkan NIK sebelum dicetak (isi `HashSet` tidak boleh dicetak apa adanya). Bagian terakhir:

```java
        Map<Pemilih, String> tps = new HashMap<>(); // [6] objek sebagai kunci
        tps.put(b1, "TPS 05");
        tps.put(b3, "TPS 12");
        Pemilih pencari = new Pemilih("6472010000000002", "Siti A."); // NIK milik Siti
        System.out.println("Terdaftar di DPT  : " + yaTidak(dpt.contains(pencari))); // [7]
        System.out.println("Lokasi TPS        : " + tps.get(pencari));
```

**Output:**

```text
=== VERSI A: TANPA ATURAN KESAMAAN ===
Dianggap sama     : tidak
Isi set           : 2 pemilih

=== VERSI B: SAMA JIKA NIK SAMA ===
Dianggap sama     : ya
Objek sama persis : tidak
Kode hash sama    : ya
Isi set           : 2 pemilih
  6472010000000001 Budi Santoso
  6472010000000002 Siti Aminah

=== MENCARI DENGAN OBJEK LAIN YANG NIK-NYA SAMA ===
Terdaftar di DPT  : ya
Lokasi TPS        : TPS 12
```

Penjelasan:

- **[1]** Tanda tangan `equals` harus **persis** `public boolean equals(Object lain)`, sama dengan milik `Object`. Di dalamnya, kita periksa jenis objeknya dengan `instanceof` (Pertemuan 09), *cast*, lalu bandingkan NIK dengan `equals` milik `String`.
- **[2]** `hashCode()` dihitung dari **data yang sama** dengan `equals()`. Cara termudah: pinjam `hashCode()` milik teks NIK.
- **[3]** Tanpa *override*, `equals()` bawaan `Object` sama seperti `==`. Set berisi dua "Budi".
- **[4]** Kini `b1.equals(b2)` bernilai benar walaupun `b1 == b2` tetap salah (dua objek berbeda).
- **[5]** Saat `b2` ditambahkan, `HashSet` menemukan `b1` di rak yang sama dan menolak `b2`. Yang tersimpan tetap `b1` ("Budi Santoso").
- **[6]** Objek `Pemilih` boleh menjadi kunci `HashMap`.
- **[7]** `pencari` adalah objek **baru**, tetapi NIK-nya milik Siti. Pencarian tetap berhasil.

### Bug diam-diam: `equals` tanpa `hashCode`

Program kecil berikut meng-*override* `equals()` dengan benar, tetapi **lupa** `hashCode()`:

```java
        Set<Pemilih> dpt = new HashSet<>();
        dpt.add(new Pemilih("6472010000000001"));
        dpt.add(new Pemilih("6472010000000001")); // NIK sama, mestinya ditolak
        System.out.println("Isi set: " + dpt.size() + " pemilih");
        boolean ada = dpt.contains(new Pemilih("6472010000000001"));
        System.out.println("Dicari dengan objek baru: " + (ada ? "ketemu" : "tidak ketemu"));
```

Hasilnya:

```text
Isi set: 2 pemilih
Dicari dengan objek baru: tidak ketemu
```

Tidak ada error sama sekali, tetapi hasilnya **salah**. `hashCode()` bawaan berbeda untuk setiap objek, jadi ketiga objek itu diantar ke rak yang berbeda dan `equals()` tidak pernah sempat dipanggil. Inilah alasan kontrak "sama berarti hash sama" di [halaman konsep](../README.md#7-kapan-dua-objek-dianggap-sama).

> [!WARNING]
> Menulis `public boolean equals(Pemilih lain)` (parameter `Pemilih`, bukan `Object`) adalah *overload*, bukan *override*, sehingga tidak pernah dipanggil oleh koleksi. Untungnya `@Override` membongkarnya saat kompilasi: `error: method does not override or implement a method from a supertype`. Selalu tulis `@Override` di atas `equals`, `hashCode`, dan `compareTo`.

## 8. Generics dan Kelas Pembungkus `Integer`

### Kelas generik `Kotak<T>`

File: [`contoh/Contoh08KelasGenerik.java`](contoh/Contoh08KelasGenerik.java)

```java
/** Kotak yang berisi satu barang bertipe T. */
class Kotak<T> { // [1] T = parameter tipe
    private T isi; // [2] tipe field mengikuti T

    public Kotak(T isi) {
        this.isi = isi;
    }

    public T getIsi() { // [3] tipe kembalian mengikuti T
        return isi;
    }
```

Method generik dan program utamanya:

```java
    static <T> T pertama(List<T> daftar) { // [4] <T> sebelum tipe kembalian
        return daftar.get(0);
    }

    public static void main(String[] args) {
        Kotak<Integer> kotakAngka = new Kotak<>(42); // [5] di sini T = Integer
        Kotak<String> kotakTeks = new Kotak<>("bekal nasi kuning"); // di sini T = String
```

Program lalu mencetak kedua kotak, menghitung `int angka = kotakAngka.getIsi();` tanpa *cast*, memanggil `pertama(...)` untuk list hari dan list angka, dan terakhir memakai `KotakLama` (versi tanpa generics yang menyimpan `Object`):

```java
        KotakLama kotakLama = new KotakLama("pulpen");
        String teks = (String) kotakLama.getIsi(); // [6] wajib cast dari Object
```

**Output:**

```text
=== KOTAK GENERIK ===
Kotak berisi 42
Kotak berisi bekal nasi kuning
Isi kotak angka + 8   : 50
Isi kotak teks kapital: BEKAL NASI KUNING
Setelah diganti       : Kotak berisi 100

=== FUNGSI/METHOD GENERIK ===
Hari pertama : Senin
Angka pertama: 10

=== KOTAK TANPA TIPE ===
Isi kotak lama: PULPEN
```

Penjelasan:

- **[1]** `<T>` setelah nama kelas mendeklarasikan **parameter tipe** bernama `T`. Nama `T` (*type*) hanyalah kebiasaan; `E` (*element*), `K` (*key*), dan `V` (*value*) juga sering dipakai.
- **[2]** Di dalam kelas, `T` dipakai seperti tipe biasa, misalnya sebagai tipe field.
- **[3]** `getIsi()` milik `Kotak<String>` mengembalikan `String`, sehingga `toUpperCase()` bisa langsung dipanggil tanpa *cast*.
- **[4]** Method generik menulis `<T>` **sebelum** tipe kembaliannya. Java menebak `T` dari argumen: `String` untuk daftar hari, `Integer` untuk daftar angka.
- **[5]** Tanda `<>` kosong di sebelah kanan disebut ***diamond***. Java mengisinya sendiri dari tipe di sebelah kiri.
- **[6]** `KotakLama` menyimpan `Object`. Saat mengambil isinya, kita **wajib** *cast* ke `String`. Jika ternyata isinya angka, program baru gagal saat berjalan dengan `ClassCastException`. Dengan `Kotak<String>`, kesalahan seperti itu sudah ditolak compiler (lihat [bagian 10](#10-kesalahan-umum-dan-cara-membaca-pesan-error)).

### Kelas pembungkus dan jebakannya

File: [`contoh/Contoh09WrapperInteger.java`](contoh/Contoh09WrapperInteger.java) (khusus Java)

Generics hanya menerima **kelas**, bukan tipe primitif. Menulis `List<int>` ditolak compiler dengan `error: unexpected type` (`required: reference`, `found: int`). Karena itu angka disimpan dengan **kelas pembungkus** (*wrapper class*): `Integer` untuk `int`, `Double` untuk `double`, `Boolean` untuk `boolean`, dan `Character` untuk `char`.

Java membungkus `int` menjadi `Integer` secara otomatis (***autoboxing***), misalnya pada `nilaiKuis.add(85)` (penanda **[1]**). Java juga membukanya kembali secara otomatis (***unboxing***), misalnya pada `int pertama = nilaiKuis.get(0)` (**[2]**). Kemudahan ini menyimpan tiga jebakan:

```java
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;
        System.out.println("127 == 127      ? " + yaTidak(a == b)); // [3] kebetulan ya
        System.out.println("128 == 128      ? " + yaTidak(c == d)); // [4] TIDAK!
        System.out.println("128 equals 128  ? " + yaTidak(c.equals(d))); // [5] cara benar
        System.out.println("128 sebagai int ? " + yaTidak(c.intValue() == d.intValue()));

        System.out.println();
        System.out.println("=== JEBAKAN 2: remove(1) PADA List<Integer> ===");
        List<Integer> angka = new ArrayList<>(List.of(10, 20, 1, 30));
        System.out.println("Awal                     : " + angka);
        angka.remove(1); // [6] menghapus INDEKS 1, yaitu angka 20!
        System.out.println("Setelah remove(1)        : " + angka);
        angka.remove(Integer.valueOf(1)); // [7] menghapus ANGKA 1
        System.out.println("Setelah remove(Integer 1): " + angka);
```

Jebakan ketiga memakai `Map<String, Integer> stok` yang hanya berisi `"pulpen"`. `stok.get("pensil")` menghasilkan `null` (penanda **[8]**), dan cara amannya adalah `getOrDefault("pensil", 0)` (**[9]**).

**Output:**

```text
=== AUTOBOXING DAN UNBOXING ===
Nilai pertama + 5 = 90

=== JEBAKAN 1: == PADA Integer ===
127 == 127      ? ya
128 == 128      ? tidak
128 equals 128  ? ya
128 sebagai int ? ya

=== JEBAKAN 2: remove(1) PADA List<Integer> ===
Awal                     : [10, 20, 1, 30]
Setelah remove(1)        : [10, 1, 30]
Setelah remove(Integer 1): [10, 30]

=== JEBAKAN 3: UNBOXING null ===
Stok pensil belum tercatat (null)
Stok pensil (getOrDefault): 0
```

Penjelasan:

- **[3]** `==` pada dua `Integer` membandingkan **objek**, bukan angka. Java menyimpan objek siap pakai untuk angka -128 sampai 127, sehingga `127 == 127` kebetulan menunjuk objek yang sama.
- **[4]** Angka 128 berada di luar jangkauan itu, sehingga dibuat dua objek berbeda dan `==` menjawab "tidak". Jebakan ini licin, karena program yang diuji dengan angka kecil terlihat benar.
- **[5]** Bandingkan `Integer` dengan `equals()`, atau buka dulu menjadi `int`.
- **[6]** `List` punya dua `remove`: `remove(int indeks)` dan `remove(Object isi)`. Angka `1` cocok dengan versi `int`, jadi yang terhapus adalah **indeks** 1.
- **[7]** `Integer.valueOf(1)` membuat objek, sehingga yang dipanggil versi `remove(Object)`.
- **[8]** dan **[9]** Menampung `null` ke variabel `Integer` masih aman. Tetapi menampungnya ke variabel `int` memicu unboxing dan langsung gagal. Jika baris komentar terakhir di file diaktifkan (`int bahaya = stok.get("pensil");`), program berhenti dengan pesan berikut (nama file dan nomor barisnya dari uji coba kami):

```text
Exception in thread "main" java.lang.NullPointerException: Cannot invoke "java.lang.Integer.intValue()" because the return value of "java.util.Map.get(Object)" is null
	at E6.main(E6.java:8)
```

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/Kedai.java`](studi-kasus/Kedai.java), [`studi-kasus/Menu.java`](studi-kasus/Menu.java), [`studi-kasus/Minuman.java`](studi-kasus/Minuman.java), [`studi-kasus/Pasangan.java`](studi-kasus/Pasangan.java), [`studi-kasus/LaporanPenjualan.java`](studi-kasus/LaporanPenjualan.java), dan [`studi-kasus/Main.java`](studi-kasus/Main.java)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#9-studi-kasus-kedaikita-apa-yang-kita-bangun-hari-ini).

**Apa yang berubah dibanding Pertemuan 11?**

- `Kedai.java`: menu disimpan di `Map<String, Menu>` berwujud `LinkedHashMap`, kode ganda ditolak dengan `IllegalArgumentException`, `cariMenu()` mencari langsung lewat kunci, dan ada empat method baru.
- `Menu.java`: kini `implements Comparable<Menu>`, serta meng-*override* `equals()` dan `hashCode()`.
- `Minuman.java`: konstruktor *overload* empat parameter tanpa `dingin` (dianggap dingin), padanan nilai bawaan `dingin=True` di Python.
- File baru `Pasangan.java` (kelas generik `Pasangan<A, B>`) dan `LaporanPenjualan.java`.
- `Main.java` ditulis ulang untuk memamerkan filter, pengurutan, kesamaan objek, transaksi, dan laporan.
- `Pesanan`, `ItemPesanan`, `Pelanggan`, kelas pembayaran, exception, `DapatDicetak`, dan `Rupiah` **tidak berubah**.

### `Kedai.java`: menu kini di dalam Map

Field-nya kini `private Map<String, Menu> daftarMenu; // kode -> objek Menu`, diisi `new LinkedHashMap<>()` di konstruktor. Method yang berubah dan yang baru:

```java
    public void tambahMenu(Menu menu) {
        if (daftarMenu.containsKey(menu.getKode())) {
            throw new IllegalArgumentException("Kode " + menu.getKode() + " sudah dipakai");
        }
        daftarMenu.put(menu.getKode(), menu);
    }

    /**
     * Mengembalikan Menu berdasarkan kode.
     *
     * Melempar MenuTidakDitemukanException jika kode tidak terdaftar.
     */
    public Menu cariMenu(String kode) throws MenuTidakDitemukanException {
        if (!daftarMenu.containsKey(kode)) {
            throw new MenuTidakDitemukanException(kode);
        }
        return daftarMenu.get(kode);
    }
```

Di antara keduanya ada `semuaMenu()` yang mengembalikan `new ArrayList<>(daftarMenu.values())` dan `menuBerdasarkanKategori()` yang menyaring dengan perulangan. Lalu:

```java
    /** Kategori unik (tanpa duplikat), diurutkan abjad. */
    public List<String> daftarKategori() {
        Set<String> kategoriUnik = new HashSet<>();
        for (Menu menu : daftarMenu.values()) {
            kategoriUnik.add(menu.getKategori());
        }
        List<String> hasil = new ArrayList<>(kategoriUnik);
        Collections.sort(hasil); // urutan isi HashSet tidak tentu, jadi diurutkan dulu
        return hasil;
    }
```

- **`LinkedHashMap`** dipilih agar urutan menu saat dicetak sesuai urutan ditambahkan, sama seperti `dict` Python.
- **`tambahMenu()`** memeriksa kunci dulu. Tanpa pemeriksaan ini, `put()` akan **menimpa** menu lama secara diam-diam (ingat contoh 03).
- **`cariMenu()`** tidak lagi memakai `for`. Kontraknya tetap sama dengan Pertemuan 11, termasuk `throws MenuTidakDitemukanException`.
- **`semuaMenu()`** mengembalikan **salinan** berupa `ArrayList`, sehingga pemanggil bebas mengurutkannya tanpa merusak isi kedai (prinsip dari Pertemuan 05).
- **`daftarKategori()`** memakai `HashSet` agar unik, lalu memindahkannya ke `ArrayList` dan mengurutkannya.

### `Menu.java`, `Minuman.java`, dan `Pasangan.java`

Kelas `Menu` kini dideklarasikan `public class Menu implements Comparable<Menu>`, dengan tiga method baru:

```java
    @Override
    public boolean equals(Object lain) {
        if (!(lain instanceof Menu)) {
            return false; // bukan Menu (atau null): pasti tidak sama
        }
        Menu menuLain = (Menu) lain;
        return kode.equals(menuLain.kode);
    }

    @Override
    public int hashCode() {
        return kode.hashCode();
    }

    /** Urutan alami: harga termurah dulu; jika harga sama, urut kode. */
    @Override
    public int compareTo(Menu lain) {
        if (harga != lain.harga) {
            return Integer.compare(harga, lain.harga);
        }
        return kode.compareTo(lain.kode);
    }
```

Dua menu dianggap sama jika **kodenya** sama. Kode adalah pilihan tepat, karena tidak punya *setter* sejak Pertemuan 04, sehingga `hashCode()`-nya tidak pernah berubah. Ketiga method ini diwarisi oleh `Makanan` dan `Minuman`. `Minuman` juga mendapat konstruktor baru:

```java
    /** Versi overload: tanpa parameter dingin, minuman dianggap disajikan dingin. */
    public Minuman(String kode, String nama, int harga, int stok) {
        this(kode, nama, harga, stok, true);
    }
```

`Pasangan.java` berisi `public class Pasangan<A, B>` dengan dua field (`A pertama`, `B kedua`), getter `getPertama()` dan `getKedua()`, serta `toString()`. Polanya sama dengan `Kotak<T>` di contoh 08, hanya saja parameter tipenya **dua**.

### `LaporanPenjualan.java`: koleksi bekerja bersama

Konstruktornya hanya menyalin pesanan yang statusnya `"LUNAS"`. Method `jumlahTerjual()` memakai pola hitung dari contoh 04 dengan `LinkedHashMap` (nama menu → total porsi). Dua method berikutnya:

```java
    /** n menu dengan porsi terbanyak. Jika seri, urut nama A-Z. */
    public List<Pasangan<String, Integer>> menuTerlaris(int n) {
        List<Pasangan<String, Integer>> daftar = new ArrayList<>();
        for (Map.Entry<String, Integer> entri : jumlahTerjual().entrySet()) {
            daftar.add(new Pasangan<>(entri.getKey(), entri.getValue()));
        }
        daftar.sort((a, b) -> {
            int banding = Integer.compare(b.getKedua(), a.getKedua()); // porsi terbanyak dulu
            if (banding != 0) {
                return banding;
            }
            return a.getPertama().compareTo(b.getPertama()); // jika seri: nama A-Z
        });
        return new ArrayList<>(daftar.subList(0, Math.min(n, daftar.size())));
    }
```

- Lambda boleh berisi **beberapa baris** jika dibungkus kurung kurawal, dan saat itu kata `return` wajib ditulis.
- `Integer.compare(b..., a...)` (b dulu, baru a) menghasilkan urutan terbesar dulu.
- `subList(0, ...)` mengambil `n` teratas, dan `Math.min` menjaga agar tidak melewati ukuran list. Ada juga versi *overload* `menuTerlaris()` tanpa parameter yang memanggil `menuTerlaris(3)`.
- `pendapatanPerKategori()` menjumlahkan subtotal per kategori ke dalam **`TreeMap`**, sehingga kategori otomatis urut abjad.

### `Main.java`: memakai semuanya

- **Pengurutan**: urut harga memakai `Collections.sort(urutHarga); // memakai compareTo() milik Menu`, sedangkan urut nama memakai `urutNama.sort(Comparator.comparing(m -> m.getNama()));`. Keduanya mengurutkan hasil `kedai.semuaMenu()`, yaitu salinan, sehingga isi kedai tidak ikut teracak.
- **`transaksi()`** menerima daftar belanja bertipe `List<Pasangan<String, Integer>>`, misalnya `List.of(new Pasangan<>("M01", 2), new Pasangan<>("M03", 1))`, lalu menangkap semua error kedai dengan `catch (KedaiException e)`.
- **`main` dideklarasikan `throws KedaiException`**. Bagian KESAMAAN OBJEK memanggil `kedai.cariMenu("M01")` di luar `try` karena kita yakin M01 terdaftar, jadi `main` cukup meneruskan *checked exception* itu (Pertemuan 11).

Jalankan `javac *.java` lalu `java Main` dari dalam folder `studi-kasus`. Setelah mencetak lima menu lewat `kedai.cetak()`, program mencetak kategori unik (`Makanan, Minuman`) dan hasil filter (dua minuman). Bagian berikutnya:

**Output:**

```text
=== URUT HARGA TERMURAH (urutan alami) ===
   Rp8.000  Es Teh Manis
  Rp15.000  Pisang Goreng Keju
  Rp18.000  Kopi Susu Gula Aren
  Rp23.000  Mie Goreng Jawa
  Rp25.000  Nasi Goreng Kampung

=== URUT NAMA A-Z (kunci pengurutan) ===
M02  Es Teh Manis
M01  Kopi Susu Gula Aren
M04  Mie Goreng Jawa
M03  Nasi Goreng Kampung
M05  Pisang Goreng Keju

=== KODE GANDA DITOLAK ===
Ditolak: Kode M01 sudah dipakai
Jumlah menu tetap 5

=== KESAMAAN OBJEK ===
Sama isinya (kode sama)? ya
Objek yang sama persis? tidak
```

Setelah itu tercetak lima transaksi. Empat berhasil, sedangkan pesanan P005 milik Andi gagal karena saldo QRIS-nya kurang. Bagian penutupnya:

**Output:**

```text
Pembayaran pesanan P005 (Andi Wijaya)
  Metode       : QRIS
  Total bayar  : Rp25.000
  [GAGAL] Pembayaran QRIS gagal: saldo e-wallet tidak cukup (saldo Rp10.000)

Pesanan tercatat: 5
========================================
LAPORAN PENJUALAN KEDAIKITA
========================================
Pesanan lunas                          4
Total pendapatan               Rp167.000
----------------------------------------
Menu terlaris:
1. Es Teh Manis (4 porsi)
2. Kopi Susu Gula Aren (4 porsi)
3. Mie Goreng Jawa (1 porsi)
----------------------------------------
Pendapatan per kategori:
Makanan                         Rp63.000
Minuman                        Rp104.000
========================================
```

Output lengkapnya **identik** dengan versi Python.

- **Kesamaan objek**: `kopiB` adalah objek baru, tetapi kodenya M01, sehingga `equals()` menjawab "ya" sementara `==` menjawab "tidak".
- **Pesanan P005** tetap berstatus BARU. Pesanan itu tercatat di riwayat (5 pesanan), tetapi tidak ikut dihitung di laporan (4 pesanan lunas).
- **Total pendapatan** Rp167.000 adalah 61.000 + 31.000 + 41.000 + 34.000. Biaya layanan kartu (Rp620) tidak ikut, karena `hitungTotal()` hanya menjumlahkan harga item.

> [!TIP]
> **Coba sendiri:** di `LaporanPenjualan.java`, ganti `new TreeMap<>()` pada `pendapatanPerKategori()` menjadi `new LinkedHashMap<>()`. Kategori mana yang kini tercetak lebih dulu?

<details>
<summary>Lihat jawaban</summary>

Minuman, karena `LinkedHashMap` mengikuti urutan kunci pertama kali dimasukkan, dan item pertama pesanan P001 adalah kopi. `TreeMap` mengurutkan kunci menurut abjad, sehingga Makanan di atas.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Sebagian besar kesalahan generics tertangkap saat **kompilasi**. Itulah keuntungan utamanya: salah isi ditolak sebelum program sempat berjalan.

### Kesalahan 1: Memasukkan isi yang salah tipe

```java
        List<String> nama = new ArrayList<>();
        nama.add(123);
```

```text
E1.java:7: error: incompatible types: int cannot be converted to String
        nama.add(123);
                 ^
Note: Some messages have been simplified; recompile with -Xdiags:verbose to get full output
1 error
```

**Artinya:** list berlabel `String` menolak angka. **Perbaikan:** masukkan teks, atau ubah tipe list sesuai isi yang memang dibutuhkan.

### Kesalahan 2: Lambda kehilangan tipe saat dirangkai `.reversed()`

```java
        daftar.sort(Comparator.comparing(p -> p.getHarga()).reversed());
```

```text
E2.java:8: error: cannot find symbol
        daftar.sort(Comparator.comparing(p -> p.getHarga()).reversed());
                                               ^
  symbol:   method getHarga()
  location: variable p of type Object
1 error
```

**Artinya:** saat dirangkai dengan `.reversed()`, Java tidak bisa menebak tipe `p`, sehingga menganggapnya `Object`, dan `Object` tidak punya `getHarga()`. **Perbaikan:** pakai *method reference* `Comparator.comparing(Produk::getHarga).reversed()`, atau sebutkan tipenya: `(Produk p) -> p.getHarga()`. Tanpa `.reversed()`, lambda biasa seperti di `Main.java` tetap aman.

### Kesalahan 3: Menghapus isi list di dalam for-each

```java
        List<String> belanja = new ArrayList<>(List.of("kopi", "gula", "teh", "susu"));
        for (String barang : belanja) {
            if (barang.equals("gula")) {
                belanja.remove(barang);
            }
        }
```

```text
Exception in thread "main" java.util.ConcurrentModificationException
	at java.base/java.util.ArrayList$Itr.checkForComodification(ArrayList.java:1095)
	at java.base/java.util.ArrayList$Itr.next(ArrayList.java:1049)
	at E3.main(E3.java:7)
```

**Artinya:** list diubah saat sedang dijelajahi oleh for-each. Baca *stack trace* sampai menemukan file milikmu: baris `at E3.main(E3.java:7)` adalah baris `for` di kode kita. **Perbaikan:** `belanja.removeIf(barang -> barang.equals("gula"));`, atau kumpulkan dulu yang mau dihapus lalu hapus setelah perulangan.

> [!NOTE]
> Bunyi pesan error bisa sedikit berbeda antarversi JDK. Pesan di atas berasal dari JDK 21. Nomor baris di dalam `java.base/...` juga bisa berbeda; yang penting adalah baris yang menunjuk file milikmu.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Java | Contoh |
|---|---|---|
| List | `List<T> x = new ArrayList<>();` | `List<String> belanja = new ArrayList<>();` |
| Set | `Set<T> x = new HashSet<>();` | `new TreeSet<>(isi)` untuk versi urut |
| Map | `Map<K, V> x = new HashMap<>();` | `new LinkedHashMap<>()`, `new TreeMap<>()` |
| Jelajah map | `for (Map.Entry<K, V> e : map.entrySet())` | `e.getKey()`, `e.getValue()` |
| Lambda | `(a, b) -> ekspresi` | `(a, b) -> Integer.compare(a.getHarga(), b.getHarga())` |
| Comparator | `Comparator.comparing(kunci)` | `Comparator.comparing(Produk::getNama).reversed()` |
| Urutan alami | `implements Comparable<T>` + `compareTo` | `return Integer.compare(harga, lain.harga);` |
| Kesamaan + hash | `equals(Object)` + `hashCode()` | `return kode.hashCode();` |
| Kelas generik | `class Nama<T> { ... }` | `class Pasangan<A, B>` |
| Kelas pembungkus | `Integer`, `Double`, `Boolean` | bandingkan dengan `equals()`, bukan `==` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Python: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [🐍 Praktik Python](../python/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
