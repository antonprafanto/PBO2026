# Latihan — Pertemuan 04: Enkapsulasi

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Tidak apa-apa jika kodemu berbeda dengan solusi. Yang penting output-nya benar, data tidak bisa dirusak dari luar kelas, dan kamu paham **mengapa** kodemu bekerja.

Aturan umum untuk semua latihan:

- Python: simpan data di atribut bergaris bawah (`self._suhu`) dan sediakan *property*. Java: semua field `private`, konstruktor dan method untuk umum `public`.
- Data yang tidak valid ditolak dengan `raise ValueError(...)` / `throw new IllegalArgumentException(...)`, lalu ditangkap di program utama dengan `try`/`except` atau `try`/`catch` untuk mencetak pesannya.

---

## Latihan 1 — Pengatur Suhu AC (⭐ Dasar)

**Tujuan:** membuat getter dan setter dengan validasi, serta memakai setter dari konstruktor.

**Soal:** Buat kelas `AC` (pendingin ruangan) dengan:

- atribut `ruangan` yang **read-only**,
- atribut `suhu` (derajat Celsius, bilangan bulat) yang bisa dibaca dan diubah, tetapi hanya boleh bernilai **16 sampai 30**. Nilai di luar batas ditolak dengan pesan `Suhu harus 16-30 derajat, bukan X`,
- konstruktor `AC(ruangan, suhu)` yang juga menolak suhu awal yang tidak valid.

Uji dengan AC di Ruang Dosen (suhu awal 24): atur ke 20, coba atur ke 10 dan 35, lalu tampilkan suhunya. Terakhir, coba pasang AC di Lab Komputer dengan suhu awal 40.

**Contoh output yang diharapkan:**

```text
=== AC RUANG DOSEN ===
Suhu awal: 24 derajat
Suhu diatur ke 20 derajat
Ditolak: Suhu harus 16-30 derajat, bukan 10
Ditolak: Suhu harus 16-30 derajat, bukan 35
Suhu sekarang: 20 derajat

=== MEMASANG AC BARU ===
Gagal memasang AC: Suhu harus 16-30 derajat, bukan 40
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `@property` untuk `ruangan` dan `suhu`, lalu `@suhu.setter` untuk pemeriksaannya. Di konstruktor tulis `self.suhu = suhu` (tanpa garis bawah) agar setter ikut bekerja.
- Java: `getRuangan()`, `getSuhu()`, dan `setSuhu(int suhu)`. Di konstruktor panggil `setSuhu(suhu);`.
- Simpan batas 16 dan 30 sebagai konstanta, misalnya `SUHU_MIN` dan `SUHU_MAKS`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_ac.py) · [☕ Java](java/solusi/Latihan01AC.java)

---

## Latihan 2 — Nilai Mata Kuliah (⭐ Dasar)

**Tujuan:** membuat atribut read-only yang dihitung dari atribut lain, termasuk getter bernilai ya/tidak.

**Soal:** Buat kelas `NilaiMataKuliah` dengan:

- `mata_kuliah` / `mataKuliah` yang read-only,
- `angka` (0–100) yang bisa dibaca dan diubah. Nilai di luar batas ditolak dengan pesan `Nilai harus 0-100, bukan X`,
- `huruf` yang read-only dan **dihitung** dari angka: A (≥ 80), B (≥ 70), C (≥ 60), D (≥ 50), E (di bawahnya),
- `lulus` yang read-only dan bernilai benar jika angka ≥ 60. Di Java, getter-nya bernama `isLulus()`,
- representasi teks seperti `Basis Data: 72 (B) - lulus` (`__str__` / `toString()`).

Uji dengan PBO (85) dan Basis Data (58). Perbaiki nilai Basis Data menjadi 72, lalu coba ubah menjadi 105 dan coba buat nilai Statistika -5.

**Contoh output yang diharapkan:**

```text
=== NILAI SEMESTER ===
Pemrograman Berorientasi Objek: 85 (A) - lulus
Basis Data: 58 (D) - belum lulus

=== SETELAH PERBAIKAN NILAI ===
Basis Data: 72 (B) - lulus

=== INPUT NILAI SALAH ===
Ditolak: Nilai harus 0-100, bukan 105
Ditolak: Nilai harus 0-100, bukan -5
Basis Data: 72 (B) - lulus
```

<details>
<summary>💡 Petunjuk</summary>

- Jangan simpan `huruf` dan `lulus` sebagai atribut. Hitung keduanya dari `angka` setiap kali diminta, agar selalu cocok dengan angka terbaru.
- Python: `huruf` dan `lulus` adalah `@property` tanpa setter. Java: `getHuruf()` dan `isLulus()` tanpa setter.
- Jangan mencetak `True`/`true` secara langsung. Ubah menjadi teks "lulus" atau "belum lulus".

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_nilai_mata_kuliah.py) · [☕ Java](java/solusi/Latihan02NilaiMataKuliah.java)

---

## Latihan 3 — Akun Pengguna dengan Password (⭐⭐ Menengah)

**Tujuan:** menyembunyikan data sepenuhnya (tanpa getter) dan menyediakan method penjaga aturan.

**Soal:** Buat kelas `AkunPengguna` dengan:

- `username` yang read-only,
- password yang disimpan tersembunyi dan **tidak bisa dibaca** dari luar kelas (tanpa getter sama sekali),
- aturan password minimal **8 karakter**, berlaku di konstruktor maupun saat mengganti password. Pesan penolakannya `Password minimal 8 karakter`,
- method `cek_password(teks)` / `cekPassword(teks)` yang mengembalikan benar/salah,
- method `ganti_password(lama, baru)` / `gantiPassword(lama, baru)` yang menolak jika password lama salah (`Password lama salah`) dan menolak password baru yang terlalu pendek.

Uji dengan akun `ayu_unmul` (password `rahasia123`) dan akun `bima_unmul` (password `12345`), lalu jalankan skenario seperti contoh output.

**Contoh output yang diharapkan:**

```text
=== MEMBUAT AKUN ===
Akun ayu_unmul berhasil dibuat
Gagal membuat akun: Password minimal 8 karakter

=== LOGIN ===
Login ayu_unmul dengan 'salah123': gagal
Login ayu_unmul dengan 'rahasia123': berhasil

=== GANTI PASSWORD ===
Ditolak: Password lama salah
Ditolak: Password minimal 8 karakter
Password berhasil diganti
Login ayu_unmul dengan 'rahasia123': gagal
Login ayu_unmul dengan 'kopiSusu2026': berhasil
```

<details>
<summary>💡 Petunjuk</summary>

- Aturan "minimal 8 karakter" dipakai di dua tempat. Tulis sekali di method internal: `_periksa_password()` di Python, atau `private void periksaPassword(String password)` di Java.
- Java: bandingkan teks dengan `.equals()`, bukan `==`.
- Buat fungsi/method bantu `coba_login(akun, password)` di program utama agar tidak menulis `if` yang sama berulang-ulang.

</details>

> [!NOTE]
> Di aplikasi sungguhan, password **tidak pernah** disimpan sebagai teks asli, melainkan diubah dulu dengan fungsi *hash*. Latihan ini sengaja disederhanakan agar kamu fokus pada enkapsulasi.

**Solusi:** [🐍 Python](python/solusi/latihan03_akun_pengguna.py) · [☕ Java](java/solusi/Latihan03AkunPengguna.java)

---

## Latihan 4 — Kartu Perpustakaan (⭐⭐ Menengah)

**Tujuan:** melindungi atribut kelas dan membuat method penjaga aturan.

**Soal:** Buat kelas `KartuPerpustakaan` dengan:

- nomor anggota otomatis `AGT-001`, `AGT-002`, dan seterusnya, dari penghitung milik kelas yang **privat**. Nomor tidak boleh terlewat jika pendaftaran gagal,
- `nama` yang tidak boleh kosong atau berisi spasi saja (`Nama anggota tidak boleh kosong`),
- nomor, nama, dan jumlah buku yang sedang dipinjam bersifat read-only,
- jumlah buku hanya berubah lewat `pinjam(judul)` dan `kembalikan(judul)`. Batasnya 3 buku. Pesan penolakannya `<nama> sudah mencapai batas 3 buku` dan `<nama> tidak sedang meminjam buku`,
- `pinjam` dan `kembalikan` yang berhasil mencetak baris seperti `Ayu Lestari meminjam 'Laskar Pelangi' (1/3)`,
- jumlah anggota dibaca lewat `KartuPerpustakaan.jumlah_anggota()` / `KartuPerpustakaan.getJumlahAnggota()`.

Uji dengan mendaftarkan Ayu Lestari, Bima Saputra, satu nama yang hanya berisi spasi, lalu Citra Dewi. Setelah itu, Ayu mencoba meminjam empat buku (buku keempat ditolak), mengembalikan satu, lalu meminjam lagi. Terakhir, Bima mencoba mengembalikan buku.

**Contoh output yang diharapkan:**

```text
=== PENDAFTARAN ANGGOTA ===
AGT-001 Ayu Lestari
AGT-002 Bima Saputra
Ditolak: Nama anggota tidak boleh kosong
AGT-003 Citra Dewi
Jumlah anggota: 3

=== PEMINJAMAN BUKU ===
Ayu Lestari meminjam 'Laskar Pelangi' (1/3)
Ayu Lestari meminjam 'Bumi Manusia' (2/3)
Ayu Lestari meminjam 'Negeri 5 Menara' (3/3)
Ditolak: Ayu Lestari sudah mencapai batas 3 buku
Ayu Lestari mengembalikan 'Bumi Manusia' (2/3)
Ayu Lestari meminjam 'Sang Pemimpi' (3/3)
Ditolak: Bima Saputra tidak sedang meminjam buku
```

<details>
<summary>💡 Petunjuk</summary>

- Naikkan penghitung **setelah** nama dinyatakan valid, persis seperti `TiketAntrean` di contoh 07.
- Format nomor: `f"AGT-{nomor:03d}"` di Python, `String.format("AGT-%03d", nomor)` di Java.
- Untuk sekarang, cukup hitung **jumlah** buku yang dipinjam. Mencatat judul satu per satu membutuhkan daftar objek, yang dibahas di Pertemuan 05.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_kartu_perpustakaan.py) · [☕ Java](java/solusi/Latihan04KartuPerpustakaan.java)

---

## Latihan 5 — Validasi Nama Menu KedaiKita (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan setter baru yang memvalidasi dan merapikan data.

**Soal:** Salin kelas `Menu` dari studi kasus pertemuan ini, lalu:

1. Tambahkan **setter** untuk `nama`. Setter menolak nama yang kosong atau berisi spasi saja dengan pesan `Nama menu tidak boleh kosong`.
2. Sebelum disimpan, spasi di awal dan akhir nama **dirapikan**. Jadi `"  Nasi Goreng Kampung  "` tersimpan sebagai `"Nasi Goreng Kampung"`.
3. Ubah konstruktor agar mengisi nama **lewat setter**, sehingga menu tanpa nama ditolak sejak dibuat dan tidak ikut dihitung.

Uji dengan skenario seperti contoh output: ganti nama es teh, coba ganti dengan nama kosong, buat menu dengan nama berspasi, lalu coba buat menu tanpa nama.

**Contoh output yang diharapkan:**

```text
=== MENU AWAL ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30

=== GANTI NAMA MENU ===
Nama baru: Es Teh Manis Jumbo
Ditolak: Nama menu tidak boleh kosong
[M02] Es Teh Manis Jumbo (Minuman) - Rp8.000 | stok 30

=== NAMA DIRAPIKAN OTOMATIS ===
Nama tersimpan: 'Nasi Goreng Kampung'
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15

=== MENU BARU TANPA NAMA ===
Gagal membuat menu: Nama menu tidak boleh kosong
Jumlah menu terdaftar: 3
```

<details>
<summary>💡 Petunjuk</summary>

- Python: ganti `self._nama = nama` di konstruktor menjadi `self.nama = nama`, lalu tambahkan `@nama.setter`. Rapikan dengan `nilai.strip()`.
- Java: tambahkan `setNama(String nama)`, lalu panggil dari konstruktor. Rapikan dengan `nama.strip()` dan periksa dengan `isEmpty()`.
- Pengguna Java: jika membuka folder `java/` pertemuan ini di VS Code, beri nama kelasmu `MenuKedai` agar tidak bentrok dengan kelas `Menu` dan `Rupiah` di folder studi kasus.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_nama_menu.py) · [☕ Java](java/solusi/Latihan05NamaMenu.java)

---

## Latihan 6 — Dompet Digital dengan Batas Harian (⭐⭐⭐ Tantangan)

**Tujuan:** menjaga beberapa aturan yang saling terkait, termasuk data internal yang sama sekali tidak terlihat dari luar.

**Soal:** Buat kelas `DompetDigital(pemilik, batas_harian)`:

- `saldo` dimulai dari 0 dan bersifat read-only,
- `isi_saldo(jumlah)` / `isiSaldo(jumlah)` menolak jumlah di bawah Rp10000 (`Isi saldo minimal Rp10000`),
- `bayar(jumlah)` memeriksa tiga aturan **berurutan**: jumlah harus lebih dari 0 (`Jumlah pembayaran harus lebih dari 0`), saldo harus cukup (`Saldo tidak cukup (saldo RpX)`), dan total pembayaran hari ini tidak boleh melebihi batas harian (`Melebihi batas harian (sisa RpX)`),
- `sisa_batas_hari_ini` / `getSisaBatasHariIni()` bersifat read-only dan dihitung dari batas harian dikurangi pemakaian hari ini,
- `ganti_hari()` / `gantiHari()` mengembalikan pemakaian hari ini ke 0,
- jumlah pemakaian hari ini disimpan di dalam objek, tetapi **tidak** boleh punya getter maupun setter.

Uji dengan dompet milik Siti (batas harian Rp100000) sesuai skenario di contoh output.

**Contoh output yang diharapkan:**

```text
=== HARI PERTAMA ===
  Saldo Rp0 | sisa batas hari ini Rp100000
Isi saldo Rp150000 berhasil
Isi saldo Rp5000 ditolak: Isi saldo minimal Rp10000
Bayar Rp45000 (makan siang) berhasil
Bayar Rp30000 (fotokopi modul) berhasil
Bayar Rp40000 (pulsa) ditolak: Melebihi batas harian (sisa Rp25000)
  Saldo Rp75000 | sisa batas hari ini Rp25000

=== HARI KEDUA ===
  Saldo Rp75000 | sisa batas hari ini Rp100000
Bayar Rp40000 (pulsa) berhasil
Bayar Rp50000 (buku) ditolak: Saldo tidak cukup (saldo Rp35000)
Bayar Rp-10000 (uji coba curang) ditolak: Jumlah pembayaran harus lebih dari 0
  Saldo Rp35000 | sisa batas hari ini Rp60000
```

<details>
<summary>💡 Petunjuk</summary>

- Simpan empat data internal: pemilik, saldo, batas harian, dan pemakaian hari ini (`_terpakai_hari_ini` / `terpakaiHariIni`).
- `bayar()` baru mengubah data setelah **ketiga** pemeriksaan lolos. Jika salah satu gagal, saldo dan pemakaian hari ini tidak boleh berubah sedikit pun.
- Buat fungsi/method bantu `coba_bayar(dompet, jumlah, keterangan)` di program utama yang berisi `try`/`except` (atau `try`/`catch`), agar program utamamu tetap ringkas.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_dompet_digital.py) · [☕ Java](java/solusi/Latihan06DompetDigital.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Pengelolaan Kamar Kos

Pemilik kos-kosan dekat kampus ingin mencatat kamar dan penghuninya dengan program sederhana. Data kamar tidak boleh bisa dirusak dari luar kelas.

**Kebutuhan:**

1. Buat kelas `KamarKos` dengan data: nomor kamar (read-only, misalnya `"A-01"`), harga sewa per bulan (bisa diubah lewat setter, harus lebih dari 0), dan nama penghuni (kosong jika belum ada penghuni).
2. Nama penghuni **tidak** boleh punya setter. Penghuni hanya berubah lewat method `check_in(nama)` / `checkIn(nama)` yang menolak jika kamar sudah terisi atau nama kosong, dan `check_out()` / `checkOut()` yang menolak jika kamar masih kosong.
3. Sediakan property/getter bernilai benar/salah `kosong` / `isKosong()`.
4. Tambahkan method `tagihan(bulan)` yang mengembalikan total sewa untuk sejumlah bulan. Jumlah bulan minimal 1.
5. Sediakan penghitung jumlah kamar milik kelas yang privat, dibaca lewat getter milik kelas. Kamar yang gagal dibuat tidak boleh ikut terhitung.
6. Di program utama, buat minimal **tiga** kamar. Tunjukkan minimal tiga operasi yang berhasil dan tiga operasi yang ditolak (ditangkap dengan `try`/`except` atau `try`/`catch`). Akhiri dengan ringkasan semua kamar dan jumlah kamar.

**Ketentuan pengumpulan:** satu file program (Python atau Java) beserta tangkapan layar output-nya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Data privat dan pintu resmi yang tepat (getter, setter, method penjaga aturan, tanpa setter yang tidak perlu) | 30% |
| Validasi di setter dan konstruktor, dengan pesan penolakan yang jelas | 25% |
| Penghitung milik kelas yang terlindungi dan akurat | 15% |
| Program utama mendemonstrasikan operasi yang berhasil dan yang ditolak | 15% |
| Kerapian kode: nama variabel jelas, komentar secukupnya, output rapi | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
