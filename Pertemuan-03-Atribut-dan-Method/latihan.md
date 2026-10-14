# Latihan Pertemuan 03: Atribut dan *Method* Lebih Dalam

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. **Pilih bahasa.** Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. **Simpan jawabanmu di folder kerjamu sendiri**, yaitu `PBO-latihan-saya/pertemuan-03/` di **luar** folder materi (lihat [aturan emas 00-Persiapan](../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri)). Jangan menyimpan jawaban di dalam folder `PBO2026` agar tidak tercampur dengan materi. Untuk Java, cara ini juga mencegah nama kelasmu bentrok dengan kelas di folder `java/` pertemuan ini. Buka folder `pertemuan-03` di VS Code lewat **File → Open Folder**.
3. **Buat satu *file* untuk setiap latihan**, misalnya `latihan01.py` (Python) atau `Latihan01.java` (Java). Untuk Java, samakan nama *file* dengan nama kelas yang berisi `main` (misalnya `public class Latihan01`), dan tulis kelas itu paling atas.
4. **Jalankan programmu** dengan tombol ▷ **Run Python File** (Python) atau tulisan **Run** pada **Run | Debug** di atas `main` (Java) di VS Code. Bisa juga lewat terminal: pilih **Terminal → New Terminal** (terminal ini otomatis terbuka di folder kerjamu), lalu ketik `python latihan01.py` (macOS/Linux: `python3 latihan01.py`) atau `java Latihan01.java`.
5. **Bandingkan *output*-mu** dengan blok **Contoh *output* yang diharapkan** di soal, baris demi baris, termasuk spasi dan tanda bacanya.
6. **Buka petunjuk** hanya jika benar-benar buntu. **Buka solusi setelah** kamu mencoba sendiri: klik tautan **Solusi** untuk membaca kodenya, atau jalankan *file* solusinya untuk membandingkan *output* (perintahnya ada di tabel di bawah).
7. **Tingkat kesulitan:** ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

Menjalankan *file* solusi lewat terminal, dari folder utama materi (ganti nama *file*-nya sesuai nomor latihan; di macOS/Linux, ketik `python3`):

| Jalur | Ketik dulu | Lalu jalankan |
|---|---|---|
| 🐍 Python | `cd Pertemuan-03-Atribut-dan-Method/python/solusi` | `python latihan01_antrean_pasien.py` |
| ☕ Java | `cd Pertemuan-03-Atribut-dan-Method/java/solusi` | `java Latihan01AntreanPasien.java` |

> [!TIP]
> Tidak apa-apa jika kodemu berbeda dengan solusi. Yang penting *output*-nya benar dan kamu paham **mengapa** kodemu bekerja. Di setiap latihan, nama Python ditulis lebih dulu, lalu nama Java setelah garis miring, misalnya `kode_antrean()` / `kodeAntrean()`.

---

## Latihan 1: Nomor Antrean Otomatis (⭐ Dasar)

**Tujuan:** memakai atribut kelas sebagai penghitung, lalu menyalin nilainya ke atribut objek.

**Soal:** Loket puskesmas ingin nomor antrean dibuat otomatis. Buat kelas `Pasien` dengan:

- atribut kelas `jumlah_pasien` / `jumlahPasien` yang dimulai dari 0,
- atribut objek `nama`, `keluhan`, dan `nomor`. Nilai `nomor` **tidak** dikirim lewat konstruktor, tetapi diambil dari penghitung saat pasien dibuat (pasien pertama 1, kedua 2, dan seterusnya),
- *method* `kode_antrean()` / `kodeAntrean()` yang mengembalikan teks seperti `A001`,
- representasi teks (`__str__` / `toString()`) seperti `A001 - Andi Wijaya (demam)`.

Daftarkan tiga pasien: Andi Wijaya (demam), Nurul Hidayah (batuk), dan Yusuf Hamdani (sakit gigi). Setelah itu, datang pasien keempat, Maya Sari (pusing).

**Contoh *output* yang diharapkan:**

```text
=== ANTREAN PUSKESMAS ===
Jumlah pasien awal: 0
A001 - Andi Wijaya (demam)
A002 - Nurul Hidayah (batuk)
A003 - Yusuf Hamdani (sakit gigi)
Jumlah pasien: 3

=== PASIEN BARU DATANG ===
A004 - Maya Sari (pusing)
Jumlah pasien: 4
Nomor pasien pertama tetap A001
```

<details>
<summary>💡 Petunjuk</summary>

- Di konstruktor, naikkan dulu penghitungnya **lewat nama kelas**, lalu salin: `self.nomor = Pasien.jumlah_pasien` (Java: `this.nomor = Pasien.jumlahPasien;`).
- Format tiga digit: Python `f"A{self.nomor:03d}"`, Java `String.format("A%03d", nomor)`.
- Pertanyaan tambahan (khusus Python): apa yang terjadi jika baris penghitung ditulis `self.jumlah_pasien += 1`? Coba dulu, lalu cocokkan dengan jawaban singkat ini: setiap pasien mendapat atribut `jumlah_pasien` "bayangan" miliknya sendiri, sedangkan `Pasien.jumlah_pasien` tetap 0. Akibatnya, semua pasien mendapat nomor yang sama. (Ingat contoh 02.)

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_antrean_pasien.py) · [☕ Java](java/solusi/Latihan01AntreanPasien.java)

---

## Latihan 2: Kelas Utilitas Konversi Satuan (⭐ Dasar)

**Tujuan:** membuat *method* milik kelas (*static method*) yang dipanggil tanpa membuat objek.

**Soal:** Buat kelas `KonversiSatuan` yang **semua** *method*-nya adalah *method* milik kelas:

- `km_ke_meter(km)` / `kmKeMeter(km)`: mengembalikan jarak dalam meter,
- `detik_ke_teks(detik)` / `detikKeTeks(detik)`: mengembalikan teks seperti `1 jam 2 menit 5 detik`,
- `celsius_ke_fahrenheit(celsius)` / `celsiusKeFahrenheit(celsius)`: rumusnya celsius × 9 / 5 + 32, memakai bilangan bulat.

Panggil ketiganya **tanpa membuat objek** `KonversiSatuan`, untuk data: 5 km dan 12 km; 3725 detik dan 1985 detik; 0, 25, 30, dan 100 derajat Celsius.

**Contoh *output* yang diharapkan:**

```text
=== KONVERSI SATUAN (tanpa membuat objek) ===
5 km = 5000 meter
12 km = 12000 meter
3725 detik = 1 jam 2 menit 5 detik
1985 detik = 0 jam 33 menit 5 detik
0 C = 32 F
25 C = 77 F
30 C = 86 F
100 C = 212 F
```

<details>
<summary>💡 Petunjuk</summary>

- Satu jam = 3600 detik. Jam = `detik // 3600`, menit = `detik % 3600 // 60`, sisa detik = `detik % 60` (Java memakai `/` untuk pembagian bulat).
- Python: tulis `@staticmethod` di atas setiap `def`, tanpa parameter `self`. Java: tambahkan kata kunci `static`.
- Agar tetap bilangan bulat, kalikan dulu baru bagi: `celsius * 9 // 5 + 32`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_konversi_satuan.py) · [☕ Java](java/solusi/Latihan02KonversiSatuan.java)

---

## Latihan 3: Paket Kiriman (⭐⭐ Menengah)

**Tujuan:** membuat konstruktor yang luwes (nilai bawaan atau *overloading*) dan representasi teks.

**Soal:** Buat kelas `Paket` dengan atribut `resi`, `tujuan`, `berat_gram`, dan `layanan`. Jika layanan tidak disebut saat membuat paket, layanannya otomatis `"REG"`. Tambahkan:

- `berat_kg()` / `beratKg()`: berat dibulatkan **ke atas** ke kilogram terdekat (1200 gram dihitung 2 kg),
- `ongkir()`: layanan `REG` Rp9.000 per kg, layanan `KILAT` Rp15.000 per kg,
- representasi teks seperti `[PKT001] Balikpapan, 1200 gram, REG - ongkir Rp18000` (latihan ini sengaja mencetak uang tanpa titik ribuan).

Buat tiga paket: PKT001 ke Balikpapan 1200 gram (tanpa menyebut layanan), PKT002 ke Bontang 500 gram layanan KILAT, dan PKT003 ke Tenggarong 2100 gram (tanpa menyebut layanan). Tampilkan semuanya beserta total ongkirnya.

**Contoh *output* yang diharapkan:**

```text
=== DAFTAR PAKET ===
[PKT001] Balikpapan, 1200 gram, REG - ongkir Rp18000
[PKT002] Bontang, 500 gram, KILAT - ongkir Rp15000
[PKT003] Tenggarong, 2100 gram, REG - ongkir Rp27000
Total ongkir: Rp60000
```

<details>
<summary>💡 Petunjuk</summary>

- Pembulatan ke atas dengan bilangan bulat: `(berat_gram + 999) // 1000`.
- Python: `def __init__(self, resi, tujuan, berat_gram, layanan="REG"):`.
- Java: buat dua konstruktor. Konstruktor tiga parameter cukup berisi `this(resi, tujuan, beratGram, "REG");`.
- Java: bandingkan teks layanan dengan `layanan.equals("KILAT")`, bukan `==`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_paket_kiriman.py) · [☕ Java](java/solusi/Latihan03PaketKiriman.java)

---

## Latihan 4: Teko dan Gelas (⭐⭐ Menengah)

**Tujuan:** memakai objek sebagai parameter, membuat *method boolean*, dan memahami *aliasing*.

**Soal:** Buat kelas `Wadah` dengan atribut `nama`, `kapasitas` (ml), dan `isi` (ml, bawaannya 0). Tambahkan:

- `kosong()` dan `penuh()`: *method boolean*,
- `sisa_ruang()` / `sisaRuang()`: kapasitas dikurangi isi,
- `tuang_ke(tujuan, jumlah)` / `tuangKe(tujuan, jumlah)`: menuang ke **wadah lain**. Banyaknya yang benar-benar dituang adalah nilai **terkecil** dari: jumlah yang diminta, isi wadah ini, dan sisa ruang di tujuan. *Method* ini mengubah isi kedua wadah dan **mengembalikan** banyaknya ml yang dituang,
- `minum(jumlah)`: mengurangi isi, tetapi tidak sampai di bawah 0,
- representasi teks seperti `Teko: 900/1000 ml`.

Skenario: teko berkapasitas 1000 ml berisi 900 ml, serta dua gelas kosong 250 ml milik Ayu dan Bima. Tuang 300 ml ke gelas Ayu, 200 ml ke gelas Bima, lalu 100 ml lagi ke gelas Bima. Setelah itu, seorang tamu memakai gelas Bima: `gelas_tamu = gelas_bima` (Java: `gelasTamu = gelasBima`), lalu tamu minum 150 ml lewat `gelas_tamu`.

> [!TIP]
> **Tebak dulu** sebelum menjalankan programmu: berapa isi **gelas Bima** di akhir program? Lalu cocokkan dengan baris `Gelas Bima: .../250 ml` di bagian akhir *output* di bawah.

**Contoh *output* yang diharapkan:**

```text
=== KONDISI AWAL ===
Teko: 900/1000 ml
Gelas Ayu: 0/250 ml
Gelas Bima: 0/250 ml

=== MENUANG DARI TEKO ===
Teko -> Gelas Ayu: diminta 300 ml, dituang 250 ml
Teko -> Gelas Bima: diminta 200 ml, dituang 200 ml
Teko -> Gelas Bima: diminta 100 ml, dituang 50 ml
Teko: 400/1000 ml
Gelas Ayu penuh? ya
Teko kosong? tidak

=== GELAS BIMA DIPAKAI TAMU ===
Tamu minum 150 ml
Gelas Bima: 100/250 ml
Gelas Bima penuh? tidak
```

<details>
<summary>💡 Petunjuk</summary>

- Nilai terkecil dari tiga angka: Python `min(jumlah, self.isi, tujuan.sisa_ruang())`, Java `Math.min(jumlah, Math.min(isi, tujuan.sisaRuang()))`.
- Jangan cetak nilai *boolean* mentah-mentah. Buat fungsi kecil `ya_tidak(nilai)` / `yaTidak(nilai)` yang mengembalikan `"ya"` atau `"tidak"`.
- `gelas_tamu = gelas_bima` tidak membuat gelas baru. Minum lewat `gelas_tamu` berarti minum dari gelas Bima.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_teko_dan_gelas.py) · [☕ Java](java/solusi/Latihan04TekoDanGelas.java)

---

## Latihan 5 (KedaiKita): Menu dari Teks (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan konstruktor alternatif.

**Soal:** Pemilik KedaiKita menyimpan daftar menu baru sebagai baris-baris teks seperti `M09;Teh Tarik;12000;Minuman;10` (kode;nama;harga;kategori;stok). Salin kelas `Menu` dan `format_rupiah()` / `Rupiah` dari studi kasus pertemuan ini, lalu tambahkan **konstruktor alternatif** `dari_teks(teks)` / `dariTeks(teks)`:

- Python: *class method* (`@classmethod`). Java: *method* `static` yang mengembalikan objek menu.
- Jika teks hanya berisi 4 bagian (tanpa stok), stoknya 0.

Uji dengan tiga baris: `M09;Teh Tarik;12000;Minuman;10`, `M10;Roti Bakar Cokelat;15000;Makanan`, dan `M11;Es Jeruk;10000;Minuman;25`. Cetak setiap baris teks, menu yang dihasilkan, lalu jumlah menu yang terdaftar.

**Contoh *output* yang diharapkan:**

```text
=== MENU DARI TEKS ===
M09;Teh Tarik;12000;Minuman;10
  -> [M09] Teh Tarik (Minuman) - Rp12.000 | stok 10
M10;Roti Bakar Cokelat;15000;Makanan
  -> [M10] Roti Bakar Cokelat (Makanan) - Rp15.000 | stok 0
M11;Es Jeruk;10000;Minuman;25
  -> [M11] Es Jeruk (Minuman) - Rp10.000 | stok 25
Jumlah menu terdaftar: 3
```

<details>
<summary>💡 Petunjuk</summary>

- `teks.split(";")` menghasilkan *list* (Python) atau *array* (Java) berisi bagian-bagian teks.
- Ubah harga dan stok menjadi angka: Python `int(bagian[2])`, Java `Integer.parseInt(bagian[2])`.
- Periksa banyaknya bagian: Python `len(bagian) == 5`, Java `bagian.length == 5`.
- Pengguna Java: beri nama kelasmu `MenuKedai` dan `RupiahKedai`, seperti di solusi. Folder `pertemuan-03`-mu mungkin sudah berisi salinan `KedaiKita.java` (dari "Coba sendiri") yang punya kelas `Menu` dan `Rupiah`, dan dua kelas bernama sama dalam satu folder membuat VS Code protes `The type Menu is already defined`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_menu_dari_teks.py) · [☕ Java](java/solusi/Latihan05MenuDariTeks.java)

---

## Latihan 6: Kelas Pecahan (⭐⭐⭐ Tantangan)

**Tujuan:** menggabungkan *method* milik kelas, konstruktor alternatif, *method* yang mengembalikan objek baru, dan *method boolean*.

**Soal:** Buat kelas `Pecahan` untuk pecahan **positif**, dengan atribut `pembilang` dan `penyebut` (bawaannya 1). Ketentuannya:

- Pecahan **selalu disederhanakan** saat dibuat. `Pecahan(6, 8)` tersimpan sebagai 3/4.
- *Method* milik kelas `fpb(a, b)` menghitung faktor persekutuan terbesar dengan algoritma Euclid.
- `tambah(lain)` dan `kali(lain)` **mengembalikan objek `Pecahan` baru**; pecahan asalnya tidak berubah.
- `sama_dengan(lain)` / `samaDengan(lain)`: *method boolean* yang membandingkan isi dua pecahan.
- Konstruktor alternatif `dari_teks("3/4")` / `dariTeks("3/4")`.
- Representasi teks `3/4`. Jika penyebutnya 1, cukup tampilkan pembilangnya, misalnya `2`.

**Contoh *output* yang diharapkan:**

```text
=== PENYEDERHANAAN OTOMATIS ===
6/8 -> 3/4
10/5 -> 2
Dari teks "10/4" -> 5/2

=== OPERASI MENGHASILKAN OBJEK BARU ===
1/2 + 1/3 = 5/6
2/3 x 3/4 = 1/2
1/4 + 3/4 = 1
3 + 1/2 = 7/2
Setengah tetap 1/2

=== MEMBANDINGKAN ISI ===
2/4 sama dengan 1/2? ya
1/3 sama dengan 2/5? tidak
```

<details>
<summary>💡 Petunjuk</summary>

- Algoritma Euclid: selama `b` tidak 0, hitung `sisa = a % b`, lalu `a = b` dan `b = sisa`. Jika `b` sudah 0, FPB-nya adalah `a`.
- Sederhanakan di dalam konstruktor dengan membagi pembilang dan penyebut dengan FPB keduanya. Dengan begitu, hasil `tambah()` dan `kali()` otomatis ikut sederhana.
- Rumus: a/b + c/d = (a × d + c × b) / (b × d), dan a/b × c/d = (a × c) / (b × d).
- Java: konstruktor satu parameter cukup berisi `this(pembilang, 1);`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_pecahan.py) · [☕ Java](java/solusi/Latihan06Pecahan.java)

---

## Tugas Mandiri (Dikumpulkan, tanpa Kunci Jawaban)

### Jadwal Kuliah dengan Kelas `Waktu`

Kamu diminta membuat program kecil untuk mengatur jadwal kuliah sehari.

**Kebutuhan:**

1. Buat kelas `Waktu` dengan atribut `jam` (0—23) dan `menit` (0—59). Menit boleh tidak disebut saat membuat objek; nilainya otomatis 0 (Python: nilai bawaan, Java: *overloading* konstruktor).
2. Representasi teks selalu dua digit, misalnya `07:05` atau `13:30`.
3. *Method* milik kelas `valid(jam, menit)` / `isValid(jam, menit)` yang mengembalikan benar jika jam dan menit berada dalam rentang yang benar.
4. Konstruktor alternatif `dari_teks("07:30")` / `dariTeks("07:30")`.
5. *Method* `tambah_menit(n)` / `tambahMenit(n)` (dengan `n` tidak negatif) yang **mengembalikan objek `Waktu` baru**. Jika melewati tengah malam, waktunya berputar kembali, misalnya 23:50 ditambah 20 menit menjadi 00:10. Petunjuk: hitung dalam total menit, lalu gunakan sisa bagi `% (24 * 60)`.
6. *Method boolean* `lebih_awal_dari(lain)` / `lebihAwalDari(lain)` yang menerima objek `Waktu` lain.
7. Atribut kelas yang menghitung berapa objek `Waktu` yang sudah dibuat.
8. Di program utama, susun jadwal minimal **empat** mata kuliah (jam mulai dibuat dari teks, ditambah lama kuliah dalam menit). Cetak jam mulai dan selesai setiap kuliah, periksa apakah ada dua kuliah berurutan yang **bentrok** (kuliah berikutnya mulai sebelum kuliah sebelumnya selesai), lalu cetak jumlah objek `Waktu` yang dibuat.

**Ketentuan pengumpulan:** satu *file* program (Python atau Java) beserta tangkapan layar *output*-nya. Program tidak boleh meminta *input* dari *keyboard*; semua data ditulis langsung di kode.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kelas `Waktu`, konstruktor yang luwes, dan representasi teks dua digit | 25% |
| `valid` dan `dari_teks` ditulis sebagai *method* milik kelas dan bekerja benar | 20% |
| `tambah_menit` mengembalikan objek baru (termasuk lewat tengah malam) dan `lebih_awal_dari` benar | 25% |
| Program utama: jadwal, pemeriksaan bentrok, dan penghitung objek | 15% |
| Kerapian kode: nama jelas, komentar secukupnya, *output* rapi | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
