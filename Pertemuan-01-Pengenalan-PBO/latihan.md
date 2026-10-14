# Latihan — Pertemuan 01: Pengenalan PBO & Persiapan Alat

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Latihan pertemuan ini ada dua jenis. **Latihan analisis** (1, 3, dan 7) dikerjakan di kertas atau catatanmu, tanpa kode. **Latihan kode** (2, 4, 5, dan 6) dikerjakan dengan bahasa pilihanmu: Python **atau** Java.
2. Untuk latihan kode, buat file baru, jalankan, lalu bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka jawaban atau solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Tidak apa-apa jika jawaban atau kodemu berbeda dengan kunci. Pada latihan analisis, yang dinilai adalah alasanmu. Pada latihan kode, yang penting output-nya benar dan kamu paham **mengapa** kodemu bekerja.

---

## Latihan 1 — Mengenali Objek, Atribut, dan Method (⭐ Dasar)

**Tujuan:** melatih cara pandang objek: memilah data (atribut) dan perilaku (method).

**Soal:** untuk setiap deskripsi berikut, tentukan **nama kelas**, **atribut**, dan **method**-nya.

1. *"Setiap **buku** di perpustakaan kampus punya **judul**, **penulis**, **tahun terbit**, dan **status** (tersedia atau dipinjam). Buku bisa **dipinjam**, **dikembalikan**, dan **ditampilkan informasinya**."*
2. *"Seorang **pengemudi** ojek online punya **nama**, **plat nomor**, dan **rating**. Pengemudi bisa **menerima pesanan**, **mengantar penumpang**, dan **menyelesaikan perjalanan**."*
3. *"Sebuah **lampu lalu lintas** punya **warna yang sedang menyala** dan **lama nyala setiap warna** (dalam detik). Lampu bisa **berganti warna** dan **menampilkan warna saat ini**."*

<details>
<summary>💡 Petunjuk</summary>

- Kata benda utama di awal kalimat biasanya menjadi **nama kelas**.
- Kata benda atau keterangan yang menjelaskan kelas itu menjadi **atribut**.
- Kata kerja ("dipinjam", "menerima", "berganti") menjadi **method**.

</details>

<details>
<summary>Lihat jawaban</summary>

| No | Kelas | Atribut | Method |
|---|---|---|---|
| 1 | `Buku` | `judul`, `penulis`, `tahun_terbit`, `status` | `pinjam()`, `kembalikan()`, `tampilkan_info()` |
| 2 | `Pengemudi` | `nama`, `plat_nomor`, `rating` | `terima_pesanan()`, `antar_penumpang()`, `selesaikan_perjalanan()` |
| 3 | `LampuLaluLintas` | `warna_menyala`, `durasi_per_warna` | `ganti_warna()`, `tampilkan_warna()` |

Nama boleh sedikit berbeda, asalkan pembagiannya tepat. Perhatikan bahwa kata kerja pasif pada soal 1 ("dipinjam") tetap menjadi method `pinjam()`, karena menggambarkan aksi yang terjadi pada objek buku. Di Java, nama atribut dan method ditulis dengan gaya camelCase, misalnya `tahunTerbit` dan `tampilkanInfo()`.

</details>

---

## Latihan 2 — Struk Belanja Koperasi Mahasiswa (⭐ Dasar)

**Tujuan:** memakai list/array, perulangan, percabangan, dan penggabungan teks.

**Soal:** Koperasi mahasiswa mencatat belanjaan dalam **tiga list/array paralel**: nama barang, harga satuan, dan jumlah yang dibeli.

| Nama barang | Harga satuan | Jumlah |
|---|---|---|
| Buku Tulis | 5000 | 4 |
| Pulpen | 3000 | 3 |
| Map Plastik | 2000 | 5 |
| Kertas HVS | 45000 | 1 |

Buat program yang:

1. mencetak setiap baris struk dengan format `nama x jumlah = Rpsubtotal`,
2. menghitung jumlah barang dan total belanja,
3. memberi diskon 10% jika total belanja **minimal Rp50000** (hitung dengan bilangan bulat),
4. mencetak total yang harus dibayar.

**Contoh output yang diharapkan:**

```text
=== STRUK KOPERASI MAHASISWA ===
Buku Tulis x 4 = Rp20000
Pulpen x 3 = Rp9000
Map Plastik x 5 = Rp10000
Kertas HVS x 1 = Rp45000
------------------------------
Jumlah barang : 13 buah
Total belanja : Rp84000
Diskon        : Rp8400
Total bayar   : Rp75600
```

<details>
<summary>💡 Petunjuk</summary>

- Siapkan dua variabel penampung bernilai awal 0: `total` dan `total_barang` (Java: `totalBarang`).
- Perulangan dengan indeks: `for i in range(len(nama_barang)):` (Python) atau `for (int i = 0; i < namaBarang.length; i++)` (Java).
- Diskon: `total * 10 // 100` (Python) atau `total * 10 / 100` (Java).
- Garis pemisah: `"-" * 30` (Python) atau `"-".repeat(30)` (Java).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_struk_belanja.py) · [☕ Java](java/solusi/Latihan02StrukBelanja.java)

---

## Latihan 3 — Prosedural atau Berorientasi Objek? (⭐⭐ Menengah)

**Tujuan:** menimbang kapan PBO bermanfaat dan kapan gaya prosedural sudah cukup.

**Soal:** untuk setiap situasi berikut, tentukan gaya mana yang **lebih cocok**: prosedural atau berorientasi objek. Tuliskan alasanmu dalam satu atau dua kalimat.

1. Skrip sekali pakai untuk mengganti nama 300 file foto kegiatan KKN menjadi `kkn_001.jpg`, `kkn_002.jpg`, dan seterusnya.
2. Aplikasi ojek online dengan penumpang, pengemudi, pesanan, pembayaran, dan rating.
3. Program kecil untuk menghitung rata-rata nilai satu kelas dari daftar angka, dipakai sekali di akhir semester.
4. Sistem informasi akademik kampus (mahasiswa, dosen, mata kuliah, KRS, nilai) yang dikembangkan banyak programmer selama bertahun-tahun.
5. Game sederhana berisi pemain, musuh, dan barang, yang masing-masing punya posisi dan nyawa, serta bisa bergerak.

<details>
<summary>💡 Petunjuk</summary>

Tanyakan dua hal untuk setiap situasi: (1) apakah ada banyak "benda" yang masing-masing membawa data dan perilakunya sendiri? (2) apakah programnya akan terus membesar dan dikerjakan banyak orang?

</details>

<details>
<summary>Lihat jawaban</summary>

| No | Lebih cocok | Alasan |
|---|---|---|
| 1 | Prosedural | Tugasnya satu aliran langkah sederhana dan hanya dipakai sekali. Membuat kelas hanya menambah baris. |
| 2 | Berorientasi objek | Ada banyak benda yang jelas (penumpang, pengemudi, pesanan, pembayaran) yang saling mengirim pesan, dan aplikasinya terus berkembang. |
| 3 | Prosedural | Datanya hanya satu daftar angka dan programnya kecil. Beberapa baris perulangan sudah cukup. |
| 4 | Berorientasi objek | Programnya besar, dikerjakan banyak orang, dan berumur panjang. Kelas membantu membagi pekerjaan serta menjaga data tetap konsisten. |
| 5 | Berorientasi objek | Setiap pemain, musuh, dan barang adalah objek dengan data (posisi, nyawa) dan perilaku (bergerak) masing-masing. |

Tidak ada jawaban yang mutlak. Program kecil pun boleh memakai kelas, dan program besar tetap berisi langkah-langkah prosedural di dalam method-nya. Yang dinilai adalah alasanmu.

</details>

---

## Latihan 4 — Rekap Nilai Kuis dengan Fungsi (⭐⭐ Menengah)

**Tujuan:** memecah program menjadi fungsi (Python) atau method `static` (Java) yang menerima parameter dan mengembalikan nilai.

**Soal:** Nilai kuis enam mahasiswa adalah `85, 72, 58, 91, 66, 47`. Buat empat fungsi/method berikut, lalu pakai di program utama:

| Python | Java | Tugas |
|---|---|---|
| `hitung_rata_rata(daftar_nilai)` | `hitungRataRata(int[] daftarNilai)` | mengembalikan rata-rata, dibulatkan ke bawah |
| `cari_tertinggi(daftar_nilai)` | `cariTertinggi(int[] daftarNilai)` | mengembalikan nilai tertinggi, **tanpa** fungsi bawaan `max()` |
| `hitung_lulus(daftar_nilai, batas)` | `hitungLulus(int[] daftarNilai, int batas)` | mengembalikan banyaknya nilai yang **≥ batas** |
| `huruf_mutu(nilai)` | `hurufMutu(int nilai)` | mengembalikan huruf mutu: A (≥ 80), B (≥ 70), C (≥ 60), D (≥ 50), E (di bawahnya) |

Gunakan batas lulus 60.

**Contoh output yang diharapkan:**

```text
=== NILAI KUIS PBO ===
Mahasiswa 1: 85 (A)
Mahasiswa 2: 72 (B)
Mahasiswa 3: 58 (D)
Mahasiswa 4: 91 (A)
Mahasiswa 5: 66 (C)
Mahasiswa 6: 47 (E)

=== REKAP ===
Rata-rata : 69
Tertinggi : 91
Lulus     : 4 dari 6 mahasiswa
```

<details>
<summary>💡 Petunjuk</summary>

- Setiap fungsi cukup berisi satu perulangan, lalu `return` di akhir.
- Rata-rata: `total // len(daftar_nilai)` (Python) atau `total / daftarNilai.length` (Java).
- Di `huruf_mutu`, periksa dari batas tertinggi dulu: `if nilai >= 80 ... elif nilai >= 70 ...`.
- Fungsi yang mengembalikan nilai bisa langsung dipakai di dalam f-string atau penggabungan teks.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_rekap_nilai.py) · [☕ Java](java/solusi/Latihan04RekapNilai.java)

---

## Latihan 5 — KedaiKita: Laporan Stok (⭐⭐ Menengah)

**Tujuan:** mengembangkan KedaiKita versi prosedural dengan fungsi-fungsi baru.

**Soal:** Mulailah dari gaya studi kasus versi prosedural, tetapi kini dengan lima menu:

| Nama menu | Harga | Stok |
|---|---|---|
| Kopi Susu Gula Aren | 18000 | 20 |
| Es Teh Manis | 8000 | 30 |
| Nasi Goreng Kampung | 25000 | 15 |
| Mie Goreng Jawa | 23000 | 4 |
| Pisang Goreng Keju | 15000 | 3 |

Simpan datanya di tiga list/array global, lalu buat fungsi/method:

1. `tampilkan_menu()` / `tampilkanMenu()`: sama seperti studi kasus.
2. `cari_indeks_termurah()` / `cariIndeksTermurah()`: mengembalikan **indeks** menu termurah.
3. `hitung_nilai_stok()` / `hitungNilaiStok()`: mengembalikan jumlah dari harga x stok semua menu.
4. `tampilkan_stok_menipis(batas)` / `tampilkanStokMenipis(batas)`: mencetak menu yang stoknya **kurang dari** batas. Jika tidak ada, cetak `- (tidak ada)`.

Panggil `tampilkan_stok_menipis` dua kali, dengan batas 5 dan batas 3.

**Contoh output yang diharapkan:**

```text
=== DAFTAR MENU KEDAIKITA ===
1. Kopi Susu Gula Aren - Rp18000 (stok 20)
2. Es Teh Manis - Rp8000 (stok 30)
3. Nasi Goreng Kampung - Rp25000 (stok 15)
4. Mie Goreng Jawa - Rp23000 (stok 4)
5. Pisang Goreng Keju - Rp15000 (stok 3)

=== LAPORAN STOK ===
Menu termurah : Es Teh Manis (Rp8000)
Nilai stok    : Rp1112000
Stok menipis (kurang dari 5):
- Mie Goreng Jawa (sisa 4)
- Pisang Goreng Keju (sisa 3)
Stok menipis (kurang dari 3):
- (tidak ada)
```

<details>
<summary>💡 Petunjuk</summary>

- Mengapa mengembalikan **indeks**, bukan nama? Karena dengan indeks, pemanggil bisa mengambil nama **dan** harga dari dua list yang berbeda. Ciri khas data paralel!
- Cari termurah: anggap indeks 0 yang termurah, lalu bandingkan harga setiap menu dengan harga di indeks termurah sejauh ini.
- Stok menipis: pakai variabel `bool`/`boolean` bernama `ada` yang bernilai awal salah, lalu ubah menjadi benar setiap kali ada menu yang tercetak. Setelah perulangan, cetak `- (tidak ada)` jika `ada` masih salah.
- Pengguna Java: array global ditulis di dalam kelas, di luar method, dengan kata `static`, seperti di `KedaiKitaProsedural.java`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_laporan_stok.py) · [☕ Java](java/solusi/Latihan05LaporanStok.java)

---

## Latihan 6 — KedaiKita: Mengurutkan Tanpa Tertukar (⭐⭐⭐ Tantangan)

**Tujuan:** memperbaiki bug studi kasus dengan cara prosedural, lalu merasakan sendiri "biaya"-nya.

**Soal:** Salin versi prosedural studi kasus, lalu ganti perintah pengurutan bawaan (`nama_menu.sort()` / `Arrays.sort(namaMenu)`) dengan fungsi buatanmu sendiri, `urutkan_menu_berdasarkan_nama()` / `urutkanMenuBerdasarkanNama()`. Fungsi ini mengurutkan menu sesuai abjad nama, sambil **ikut memindahkan harga dan stok** sehingga data tidak tertukar. Jalankan skenario yang sama dengan studi kasus: tampilkan menu, proses pesanan Budi, urutkan, lalu tampilkan lagi.

**Contoh output yang diharapkan:**

```text
=== DAFTAR MENU KEDAIKITA ===
1. Kopi Susu Gula Aren - Rp18000 (stok 20)
2. Nasi Goreng Kampung - Rp25000 (stok 15)
3. Es Teh Manis - Rp8000 (stok 30)

Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis
Total bayar : Rp44000

Mengurutkan menu sesuai abjad (harga dan stok ikut ditukar)...
=== DAFTAR MENU KEDAIKITA ===
1. Es Teh Manis - Rp8000 (stok 29)
2. Kopi Susu Gula Aren - Rp18000 (stok 18)
3. Nasi Goreng Kampung - Rp25000 (stok 15)

Berhasil! Harga dan stok ikut pindah bersama namanya.
Tetapi jika nanti ada data baru (misalnya kategori),
kode pengurut ini harus diubah lagi agar data baru itu ikut ditukar.
```

<details>
<summary>💡 Petunjuk</summary>

- Tiru pola *bubble sort* di contoh 06 (data paralel), tetapi kali ini yang dibandingkan adalah **nama**.
- Python: teks bisa dibandingkan langsung, misalnya `nama_menu[i] > nama_menu[i + 1]` bernilai benar jika nama di kiri lebih belakang abjadnya.
- Java: gunakan `namaMenu[i].compareTo(namaMenu[i + 1]) > 0`. Method `compareTo` menghasilkan angka positif jika teks pertama lebih belakang abjadnya.
- Setiap kali menukar nama, tukar juga harga dan stok di posisi yang **sama**. Di Python cukup `a, b = b, a`. Di Java, pakai variabel sementara.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_urutkan_menu.py) · [☕ Java](java/solusi/Latihan06UrutkanMenu.java)

> [!NOTE]
> Bandingkan solusimu dengan versi objek di studi kasus. Di sana, pengurutan cukup **satu baris**, dan menambah data baru tidak mengubah baris itu sama sekali. Selisih "biaya" inilah salah satu alasan kita belajar PBO.

---

## Latihan 7 — Merancang Objek-Objek KedaiKita (⭐⭐⭐ Tantangan)

**Tujuan:** memandang sistem kasir sebagai kumpulan objek yang saling mengirim pesan.

**Soal:** Baca skenario berikut.

*"Budi datang ke KedaiKita dan memesan 2 Kopi Susu Gula Aren serta 1 Es Teh Manis. Kasir mencatat pesanan, stok setiap menu berkurang, dan total harga dihitung. Budi membayar dengan QRIS, lalu menerima struk. Karena terdaftar sebagai pelanggan, Budi juga mendapat poin."*

1. Tentukan minimal **empat kelas** beserta atribut dan method-nya.
2. Tuliskan urutan **pesan** antarobjek: siapa meminta apa kepada siapa, dari awal pesanan sampai struk dicetak.
3. Pilar PBO mana saja yang mungkin muncul di sistem ini? Berikan contoh untuk minimal **dua** pilar.

<details>
<summary>💡 Petunjuk</summary>

- Garis bawahi kata benda di skenario: menu, pesanan, pelanggan, pembayaran, kedai, struk.
- Pikirkan siapa yang paling pantas "mengurus" sesuatu. Misalnya, siapa yang paling tahu stok sebuah menu? Menu itu sendiri.
- Lihat lagi analogi pilar di [halaman konsep](README.md#6-empat-pilar-pbo-sekilas).

</details>

<details>
<summary>Lihat jawaban</summary>

**1. Kelas, atribut, dan method (salah satu kemungkinan):**

| Kelas | Atribut | Method |
|---|---|---|
| `Menu` | `nama`, `harga`, `stok` | `stok_cukup(jumlah)`, `kurangi_stok(jumlah)` |
| `Pelanggan` | `nama`, `no_hp`, `poin` | `tambah_poin(jumlah)` |
| `Pesanan` | `nomor`, `pelanggan`, `daftar_item`, `status` | `tambah_item(menu, jumlah)`, `hitung_total()`, `bayar(pembayaran)`, `cetak_struk()` |
| `Pembayaran` | `jumlah`, `metode` | `proses()` |
| `Kedai` | `nama`, `alamat`, `daftar_menu` | `cari_menu(nama)`, `buat_pesanan(pelanggan)` |

**2. Urutan pesan antarobjek:**

1. Kasir meminta `Kedai` membuatkan pesanan baru untuk Budi (`buat_pesanan`).
2. Kasir meminta `Pesanan` menambah 2 Kopi Susu Gula Aren (`tambah_item`).
3. `Pesanan` bertanya kepada `Menu` kopi apakah stoknya cukup, lalu memintanya mengurangi stok sebanyak 2.
4. Langkah 2 dan 3 diulang untuk 1 Es Teh Manis.
5. Kasir meminta `Pesanan` menghitung total (`hitung_total`), hasilnya Rp44000.
6. `Pesanan` meminta `Pembayaran` QRIS memproses Rp44000 (`proses`).
7. `Pesanan` meminta `Pelanggan` Budi menambah poinnya (`tambah_poin`).
8. Kasir meminta `Pesanan` mencetak struk (`cetak_struk`).

**3. Pilar yang mungkin muncul:**

- **Enkapsulasi:** stok hanya boleh berubah lewat `kurangi_stok`, yang menolak pengurangan melebihi stok (Pertemuan 04).
- **Pewarisan:** makanan dan minuman sama-sama menu, tetapi punya ciri tambahan masing-masing (Pertemuan 07).
- **Polimorfisme:** pembayaran tunai, QRIS, dan kartu sama-sama menanggapi pesan `proses`, tetapi dengan caranya sendiri (Pertemuan 09).
- **Abstraksi:** kasir cukup meminta pembayaran diproses tanpa perlu tahu detail cara kerja QRIS (Pertemuan 10).

Rancangan ini mirip dengan KedaiKita yang akan kita bangun sedikit demi sedikit sampai Pertemuan 15. Jawabanmu boleh berbeda, asalkan setiap kelas punya tanggung jawab yang jelas dan alasanmu masuk akal.

</details>

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Analisis Sistem di Sekitarmu

Pilih **satu** usaha atau layanan di sekitar kampus atau tempat tinggalmu, misalnya laundry kiloan, bengkel motor, apotek, rental sepeda, toko buku, atau fotokopi. Jangan memilih kafe, karena kafe sudah menjadi studi kasus kita.

**Kebutuhan:**

1. Tuliskan deskripsi singkat sistemnya dalam satu paragraf (5–8 kalimat): siapa saja yang terlibat dan apa saja yang terjadi.
2. Identifikasi minimal **tiga kelas**. Untuk setiap kelas, tuliskan minimal tiga atribut dan dua method dalam bentuk tabel.
3. Tuliskan satu skenario lengkap (minimal lima langkah) berupa urutan **pesan antarobjek**, seperti pada Latihan 7.
4. Tulis satu program **prosedural** (Python atau Java) untuk satu fitur sederhana dari sistem tersebut. Syaratnya: memakai minimal dua list/array paralel, minimal dua fungsi/method yang mengembalikan nilai, serta minimal satu percabangan dan satu perulangan. Output harus rapi dan diberi judul bagian.
5. Tulis refleksi singkat (3–5 kalimat): bagian mana dari programmu yang mudah rusak jika programnya membesar, dan bagaimana cara pandang objek bisa membantu.

**Ketentuan pengumpulan:** satu dokumen (PDF) berisi poin 1, 2, 3, dan 5, ditambah satu file program beserta tangkapan layar output-nya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Deskripsi sistem jelas dan sesuai tema yang dipilih | 10% |
| Identifikasi kelas, atribut, dan method tepat (data dan perilaku tidak tertukar) | 25% |
| Skenario pesan antarobjek runtut dan masuk akal | 20% |
| Program prosedural berjalan benar dan memenuhi semua syarat | 30% |
| Refleksi menunjukkan pemahaman tentang kelemahan data paralel dan manfaat PBO | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
