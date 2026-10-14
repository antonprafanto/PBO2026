# Latihan Pertemuan 11: *Exception Handling*

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. **Pilih bahasa.** Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. **Siapkan folder jawabanmu.** Simpan jawaban di folder milikmu sendiri **di luar** folder materi, yaitu folder `pertemuan-11` yang sama dengan tempat percobaan di halaman praktik. Jangan menyimpannya di dalam folder `PBO2026`: perubahanmu bisa bentrok saat materi diperbarui, dan di jalur Java nama kelasmu bisa bentrok dengan kelas di folder `solusi`.

   ```text
   Documents/
   ├── PBO2026/                              <- materi (jangan diubah)
   └── PBO-latihan-saya/
       └── pertemuan-11/                     <- jawabanmu di sini
           ├── latihan01_rata_rata_nilai.py  (jalur Python)
           └── Latihan01RataRataNilai.java   (jalur Java)
   ```

3. **Buat satu *file* untuk setiap latihan.** Beri nama yang sama dengan *file* solusinya agar mudah dibandingkan, misalnya `latihan01_rata_rata_nilai.py` atau `Latihan01RataRataNilai.java`.
   - Python: tulis kelas dan fungsi yang diminta, fungsi `main()`, dan dua baris penutup `if __name__ == "__main__":` lalu `main()`, seperti di contoh.
   - Java: nama *file* harus sama dengan nama kelas `public` yang berisi `main`. Kelas lain (misalnya kelas *exception*-mu) ditulis di bawahnya **tanpa** `public`, seperti di contoh.
4. **Jalankan *file*-mu.**
   - Lewat VS Code: buka folder `pertemuan-11` (**File → Open Folder**), buka *file*-nya, lalu klik ▷ (Python) atau **Run** di atas baris `public static void main` (Java).
   - Lewat terminal: terminal VS Code di jendela itu sudah berada di folder `pertemuan-11`. Dari terminal lain, masuk dulu dengan `cd Documents\PBO-latihan-saya\pertemuan-11` (Windows) atau `cd ~/Documents/PBO-latihan-saya/pertemuan-11` (macOS/Linux). Setelah itu, ketik `python latihan01_rata_rata_nilai.py` (macOS/Linux: `python3 latihan01_rata_rata_nilai.py`) atau `java Latihan01RataRataNilai.java`.
5. **Bandingkan hasilnya.** Cocokkan *output*-mu dengan **contoh *output*** di soal, baris demi baris. Spasi, huruf besar-kecil, dan tanda baca sebaiknya sama persis.
6. **Baru lihat solusi.** Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri: klik tautan **Solusi** di bawah setiap latihan untuk membaca kodenya, atau jalankan *file* solusinya dari folder `python/solusi` atau `java/solusi` pertemuan ini (caranya sama dengan menjalankan contoh di halaman praktik).

Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Tidak apa-apa jika kodemu berbeda dengan solusi. Yang penting *output*-nya benar, dan kamu bisa menjelaskan **di mana** *exception* dilempar, **siapa** yang menangkapnya, dan **mengapa** di situ.

---

## Latihan 1: Rata-Rata Nilai dari Teks (⭐ Dasar)

**Tujuan:** menangkap *exception* bawaan dan membiarkan *exception* merambat ke pemanggil yang tepat.

**Soal:** Nilai ujian dikirim sebagai teks. Buat dua fungsi (Java: *method* `static`):

1. `rata_rata_nilai(daftar_teks)` / `rataRataNilai(String[] daftarTeks)`: ubah setiap teks menjadi bilangan bulat. Teks yang bukan angka dilewati dengan pesan `'<teks>' bukan angka, dilewati`. Kembalikan rata-rata nilai yang valid (bilangan bulat, dibulatkan ke bawah). **Jangan** tangkap pembagian dengan nol di fungsi ini.
2. `proses_kelas(nama_kelas, daftar_teks)` / `prosesKelas(...)`: cetak judul, panggil fungsi pertama, lalu cetak rata-ratanya. Jika tidak ada satu pun nilai yang valid, tangkap *exception* pembagian dengan nol dan cetak pesan yang ramah.

Uji dengan Kelas A `["80", "75", "sembilan puluh", "92", ""]` dan Kelas B `["-", "tidak hadir"]`.

**Contoh *output* yang diharapkan:**

```text
=== KELAS A ===
  'sembilan puluh' bukan angka, dilewati
  '' bukan angka, dilewati
Rata-rata: 82

=== KELAS B ===
  '-' bukan angka, dilewati
  'tidak hadir' bukan angka, dilewati
Tidak ada nilai yang valid, rata-rata tidak bisa dihitung
```

<details>
<summary>💡 Petunjuk</summary>

- Hitung `total` dan `jumlah_valid` hanya untuk teks yang berhasil diubah. Di Python, blok `else` cocok untuk itu.
- Jika `jumlah_valid` bernilai 0, pembagian `total // jumlah_valid` (Java: `total / jumlahValid`) melempar `ZeroDivisionError` / `ArithmeticException`. Biarkan *exception* itu merambat ke `proses_kelas()`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_rata_rata_nilai.py) · [☕ Java](java/solusi/Latihan01RataRataNilai.java)

---

## Latihan 2: Jam Digital yang Menolak Waktu Mustahil (⭐ Dasar)

**Tujuan:** melempar *exception* untuk validasi dan memakai `finally`.

**Soal:** Buat kelas `JamDigital` (format 24 jam, awalnya `00:00`) dengan:

- *method* `atur(jam, menit)`: tolak jam di luar 0 sampai 23 dengan pesan `jam harus 0 sampai 23`, dan menit di luar 0 sampai 59 dengan pesan `menit harus 0 sampai 59` (`ValueError` / `IllegalArgumentException`). Waktu lama **tidak boleh** berubah jika ditolak.
- *method* `tampilan()`: mengembalikan teks dua digit, misalnya `07:30`.

Di program utama, coba atur ke (7, 30), (25, 0), (12, 75), (23, 59), dan (-1, 10). Setelah **setiap** percobaan, berhasil maupun gagal, cetak tampilan jam dari blok `finally`.

**Contoh *output* yang diharapkan:**

```text
=== JAM DIGITAL ===
Tampilan awal: 00:00
Atur ke jam 7 menit 30 -> berhasil
  Tampilan jam: 07:30
Atur ke jam 25 menit 0 -> ditolak: jam harus 0 sampai 23
  Tampilan jam: 07:30
Atur ke jam 12 menit 75 -> ditolak: menit harus 0 sampai 59
  Tampilan jam: 07:30
Atur ke jam 23 menit 59 -> berhasil
  Tampilan jam: 23:59
Atur ke jam -1 menit 10 -> ditolak: jam harus 0 sampai 23
  Tampilan jam: 23:59
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa jam dan menit **sebelum** mengubah atribut. Jika ada yang salah, lempar *exception*; baris pengubah atribut tidak akan tercapai.
- Dua digit: Python `f"{jam:02d}:{menit:02d}"`, Java `String.format("%02d:%02d", jam, menit)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_jam_digital.py) · [☕ Java](java/solusi/Latihan02JamDigital.java)

---

## Latihan 3: Peminjaman Buku Perpustakaan (⭐⭐ Menengah)

**Tujuan:** membuat hierarki *exception* sendiri yang membawa data tambahan.

**Soal:** Buat hierarki *exception* berikut (Java: akhiran `Exception`, turunan `Exception`):

- `PerpustakaanError`: induk semua *error* perpustakaan.
- `BukuSedangDipinjamError(judul, peminjam)`: pesan `Buku '<judul>' sedang dipinjam oleh <peminjam>`.
- `BatasPinjamError(nama, batas)`: pesan `<nama> sudah meminjam <batas> buku (batas maksimal)`.

Lalu buat kelas `Buku` (judul, nama peminjam atau kosong) dan `Anggota` (nama, batas pinjam 2 buku) dengan *method* `pinjam(buku)` dan `kembalikan(buku)`. Mengembalikan buku yang tidak sedang dipinjam ditolak dengan `PerpustakaanError` langsung. Penangkap untuk `pinjam` memakai **data tambahan** *exception* untuk memberi saran.

**Contoh *output* yang diharapkan:**

```text
=== PEMINJAMAN BUKU ===
Ayu meminjam 'Laskar Pelangi'
Ayu meminjam 'Bumi Manusia'
Gagal: Ayu sudah meminjam 2 buku (batas maksimal)
  Saran: kembalikan dulu salah satu dari 2 buku
Gagal: Buku 'Laskar Pelangi' sedang dipinjam oleh Ayu
  Saran: tunggu sampai Ayu mengembalikannya

=== PENGEMBALIAN ===
Gagal: Bima tidak sedang meminjam 'Bumi Manusia'
Ayu mengembalikan 'Laskar Pelangi'
Bima meminjam 'Laskar Pelangi'
```

<details>
<summary>💡 Petunjuk</summary>

- Urutan pemanggilan: Ayu meminjam *Laskar Pelangi*, *Bumi Manusia*, *Negeri 5 Menara*; Bima meminjam *Laskar Pelangi*; Bima mengembalikan *Bumi Manusia*; Ayu mengembalikan *Laskar Pelangi*; Bima meminjam *Laskar Pelangi* lagi.
- Simpan data tambahan sebagai atribut (Python) atau *field* + *getter* (Java), lalu pakai di penangkap: `e.peminjam` / `e.getPeminjam()`.
- Java: tulis `throws BukuSedangDipinjamException, BatasPinjamException` di kepala `pinjam()`. Semua kelas ini adalah *checked exception*.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_peminjaman_buku.py) · [☕ Java](java/solusi/Latihan03PeminjamanBuku.java)

---

## Latihan 4 (KedaiKita): Menolak Kode Menu Ganda (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan *exception* baru.

**Soal:** Saat ini `tambah_menu()` / `tambahMenu()` menerima menu apa saja, termasuk menu yang kodenya sudah dipakai. Akibatnya, `cari_menu("M02")` bisa menemukan menu yang salah.

1. Buat `MenuSudahAdaError` sebagai turunan `KedaiError` (Java: `MenuSudahAdaException extends KedaiException`). *Exception* ini membawa `kode` dan `nama_lama` (nama menu yang sudah memakai kode itu), dengan pesan `Kode <kode> sudah dipakai oleh <nama_lama>`.
2. Ubah `tambah_menu()` agar melempar *exception* itu **sebelum** menu baru dimasukkan ke daftar. Di Java, jangan lupa `throws`.
3. Uji: tambahkan lima menu awal (M01 sampai M05), lalu Es Jeruk (M02, Rp10.000), Teh Tarik (M06, Rp12.000), dan Kopi Tubruk (M06, Rp12.000).

**Contoh *output* yang diharapkan:**

```text
=== MENAMBAH MENU ===
[OK] [M01] Kopi Susu Gula Aren - Rp18.000
[OK] [M02] Es Teh Manis - Rp8.000
[OK] [M03] Nasi Goreng Kampung - Rp25.000
[OK] [M04] Mie Goreng Jawa - Rp23.000
[OK] [M05] Pisang Goreng Keju - Rp15.000
[GAGAL] Kode M02 sudah dipakai oleh Es Teh Manis
        Es Jeruk tidak ditambahkan, pilih kode selain M02
[OK] [M06] Teh Tarik - Rp12.000
[GAGAL] Kode M06 sudah dipakai oleh Teh Tarik
        Kopi Tubruk tidak ditambahkan, pilih kode selain M06
Jumlah menu terdaftar: 6
```

<details>
<summary>💡 Petunjuk</summary>

- Di `tambah_menu()`, periksa setiap menu yang sudah terdaftar. Jika kodenya sama, lempar *exception* berisi kode dan nama menu lama.
- Ada dua cara mengerjakannya. **Cara A:** salin seluruh folder `studi-kasus` ke folder `pertemuan-11` milikmu (seperti "Coba sendiri" bagian 9 di halaman praktik), lalu di salinan itu tambahkan kelas baru di `pengecualian.py` (Python) atau buat *file* `MenuSudahAdaException.java` (Java), dan ubah `tambah_menu()`/`tambahMenu()`. **Cara B:** buat satu *file* berisi salinan ringkas kelas yang dibutuhkan, seperti *file* solusinya.
- Di solusi Java (Cara B), nama kelasnya diganti (`MenuKedai`, `KedaiKopi`, `KedaiKopiException`) agar tidak bentrok dengan kelas di folder studi kasus. Jika di folder `pertemuan-11` milikmu sudah ada salinan studi kasus, lakukan hal yang sama pada *file*-mu agar VS Code tidak protes *The type ... is already defined*.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_menu_sudah_ada.py) · [☕ Java](java/solusi/Latihan04MenuSudahAda.java)

---

## Latihan 5: Impor Data Pendaftar Lomba (⭐⭐⭐ Tantangan)

**Tujuan:** menggabungkan *exception* buatan sendiri, validasi bertingkat, dan *exception chaining*.

**Soal:** Panitia Lomba Debat Mahasiswa menerima data pendaftar berformat `nama;umur`. Buat:

1. `BarisDataError(nomor_baris, alasan)` (Java: `BarisDataException`, *checked*) dengan pesan `Baris <nomor>: <alasan>`.
2. Fungsi `baca_pendaftar(nomor_baris, teks)` / `bacaPendaftar(...)` yang mengembalikan objek `Pendaftar`, atau melempar `BarisDataError` dengan alasan:
   - `format harus nama;umur` jika jumlah kolom bukan 2,
   - `nama tidak boleh kosong`,
   - `umur '<teks>' bukan angka`: bungkus *exception* konversi aslinya sebagai **penyebab** (`raise ... from e` / konstruktor dengan `Throwable`),
   - `umur <n> di luar syarat 17-25 tahun`.
3. Program utama yang memproses semua baris, mencetak `[OK]` atau `[DITOLAK]`, menambahkan keterangan `(penyebab asli: kesalahan konversi angka)` jika *exception*-nya punya penyebab, lalu mencetak ringkasan.

Data: `"Ayu Lestari;20"`, `"Bima Saputra"`, `"Citra Dewi;dua puluh"`, `";19"`, `"Dimas Pratama;30"`, `"Eka Putri;18"`, `"Fajar Nugraha;21;Samarinda"`.

**Contoh *output* yang diharapkan:**

```text
=== IMPOR DATA PENDAFTAR LOMBA DEBAT ===
[OK] Baris 1: Ayu Lestari (20 tahun)
[DITOLAK] Baris 2: format harus nama;umur
[DITOLAK] Baris 3: umur 'dua puluh' bukan angka
          (penyebab asli: kesalahan konversi angka)
[DITOLAK] Baris 4: nama tidak boleh kosong
[DITOLAK] Baris 5: umur 30 di luar syarat 17-25 tahun
[OK] Baris 6: Eka Putri (18 tahun)
[DITOLAK] Baris 7: format harus nama;umur

Diterima: 2, ditolak: 5
Daftar peserta:
- Ayu Lestari (20 tahun)
- Eka Putri (18 tahun)
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa dari yang paling mendasar: jumlah kolom, lalu nama, lalu umur angka, lalu rentang umur. Dengan begitu, pemanggil cukup menangkap **satu** jenis *exception*.
- Bersihkan spasi di tepi teks dengan `strip()` / `trim()` sebelum memeriksa.
- Penyebab dibaca dengan `e.__cause__` / `e.getCause()`. Nilainya `None` / `null` jika tidak ada.
- Java: buat dua konstruktor untuk `BarisDataException`, salah satunya menerima `Throwable penyebab` dan memanggil `super(pesan, penyebab)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_impor_pendaftar.py) · [☕ Java](java/solusi/Latihan05ImporPendaftar.java)

---

## Tugas Mandiri (Dikumpulkan, tanpa Kunci Jawaban)

### Mesin Penjual Minuman di Gedung Kuliah

Fakultas memasang mesin penjual minuman otomatis. Buat simulasinya dengan *exception handling* yang rapi.

**Kebutuhan:**

1. Kelas `Produk` (kode, nama, harga, stok) dan kelas `MesinMinuman` yang menyimpan minimal **empat** produk.
2. Hierarki *exception*: `MesinError` sebagai induk, dengan turunan `ProdukTidakAdaError` (membawa kode), `StokHabisError` (membawa nama produk), dan `UangKurangError` (membawa kekurangan uang). Java: akhiran `Exception`; jelaskan di komentar apakah kamu memilih *checked* atau *unchecked* dan mengapa.
3. *Method* `beli(kode, uang)` yang mengembalikan kembalian, atau melempar *exception* yang sesuai. Uang dan stok **tidak boleh** berubah jika transaksi gagal.
4. Program utama yang mensimulasikan minimal **enam** transaksi (campuran berhasil dan gagal). Setiap kegagalan ditangani dengan pesan yang ramah dan memakai data tambahan *exception* (misalnya "uang kurang Rp2.000"). Gunakan `finally` untuk mencetak `Mesin siap melayani pembeli berikutnya` setelah setiap transaksi.
5. Di akhir, cetak total pendapatan dan sisa stok setiap produk.

**Ketentuan pengumpulan:** satu *file* program (Python atau Java) beserta tangkapan layar *output*-nya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Hierarki *exception* benar (induk dan tiga turunan) dan membawa data tambahan | 25% |
| `beli()` melempar *exception* yang tepat dan tidak mengubah data saat gagal | 25% |
| Program utama: urutan penangkap benar, pesan ramah, `finally` dipakai dengan tepat | 30% |
| Kerapian kode: nama jelas, komentar secukupnya, tidak ada *exception* yang ditelan diam-diam | 20% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
