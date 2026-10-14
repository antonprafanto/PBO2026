# Latihan — Pertemuan 05: Relasi Antar Kelas

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Sebelum menulis kode, tentukan dulu **jenis relasi** dan **multiplisitas** setiap hubungan di soal. Tulis sebagai komentar di bagian atas file.
3. Jalankan programmu, lalu bandingkan dengan **contoh output** di soal. Buka petunjuk hanya jika benar-benar buntu, dan buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Tidak apa-apa jika kodemu berbeda dengan solusi. Yang penting output-nya benar dan kamu bisa menjelaskan **mengapa** memilih relasi itu.

---

## Latihan 1 — Mobil dan Mesin (⭐ Dasar)

**Tujuan:** membuat komposisi satu-ke-satu dan meneruskan perintah ke objek bagian.

**Soal:** Buat kelas `Mesin` dengan atribut `kapasitas_cc` dan `menyala` (awalnya mati), method `hidupkan()`, `matikan()`, dan representasi teks seperti `mesin 1300 cc (mati)`. Lalu buat kelas `Mobil(merek, kapasitas_cc)` dengan aturan:

- objek `Mesin` dibuat **di dalam** konstruktor `Mobil`, bukan di luar,
- `nyalakan()` dan `matikan()` meneruskan perintah ke mesinnya,
- `jalan(km)` menambah odometer hanya jika mesin menyala; jika mati, cetak pesan gagal,
- representasi teks mobil: merek, keadaan mesin, dan odometer.

Uji dengan Avanza 1300 cc: coba jalan 5 km saat mesin mati, nyalakan, jalan 12 km dan 5 km, lalu matikan.

**Contoh output yang diharapkan:**

```text
=== MOBIL BARU ===
Avanza, mesin 1300 cc (mati), odometer 0 km

=== PERJALANAN ===
Avanza belum bisa jalan: mesin masih mati
Mesin 1300 cc dihidupkan
Avanza melaju 12 km
Avanza melaju 5 km
Mesin 1300 cc dimatikan

=== SETELAH PERJALANAN ===
Avanza, mesin 1300 cc (mati), odometer 17 km
```

<details>
<summary>💡 Petunjuk</summary>

- Di konstruktor `Mobil`: `self._mesin = Mesin(kapasitas_cc)` (Python) atau `this.mesin = new Mesin(kapasitasCc);` (Java).
- Mobil perlu bertanya ke mesin apakah sedang menyala. Sediakan property `menyala` (Python) atau getter `isMenyala()` (Java) di kelas `Mesin`.
- Representasi teks mobil bisa memakai representasi teks mesin: `f"{self._merek}, {self._mesin}, ..."`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_mobil_mesin.py) · [☕ Java](java/solusi/Latihan01MobilMesin.java)

---

## Latihan 2 — Playlist dan Lagu (⭐ Dasar)

**Tujuan:** membuat agregasi dengan list, dan melindungi list dengan salinan.

**Soal:** Buat kelas `Lagu(judul, penyanyi, durasi_detik)` dan kelas `Playlist(nama)` dengan:

- `tambah(lagu)`: memasukkan objek lagu yang **sudah dibuat di luar**,
- `daftar_lagu` (Python, *property*) atau `getDaftarLagu()` (Java): mengembalikan **salinan** list,
- `total_durasi()`: jumlah durasi semua lagu dalam detik,
- `tampilkan()`: nama playlist, jumlah lagu, total durasi, dan daftar lagunya.

Buat tiga lagu: *Indonesia Pusaka* (Ismail Marzuki, 215 detik), *Ampar-Ampar Pisang* (Lagu Daerah Kalimantan Selatan, 132 detik), dan *Bengawan Solo* (Gesang, 187 detik). Playlist "Teman Belajar" berisi Indonesia Pusaka dan Bengawan Solo. Playlist "Perjalanan Mudik" berisi Ampar-Ampar Pisang dan Bengawan Solo. Terakhir, ambil salinan daftar lagu "Teman Belajar", kosongkan salinan itu, lalu tampilkan playlist-nya lagi.

**Contoh output yang diharapkan:**

```text
=== DAFTAR PLAYLIST ===
Teman Belajar (2 lagu, total 6:42):
  1. Indonesia Pusaka - Ismail Marzuki (3:35)
  2. Bengawan Solo - Gesang (3:07)
Perjalanan Mudik (2 lagu, total 5:19):
  1. Ampar-Ampar Pisang - Lagu Daerah Kalimantan Selatan (2:12)
  2. Bengawan Solo - Gesang (3:07)

=== MENGOSONGKAN SALINAN DARI LUAR ===
Salinan di luar kini berisi 0 lagu
Teman Belajar (2 lagu, total 6:42):
  1. Indonesia Pusaka - Ismail Marzuki (3:35)
  2. Bengawan Solo - Gesang (3:07)
```

<details>
<summary>💡 Petunjuk</summary>

- Format durasi `m:ss`: `f"{detik // 60}:{detik % 60:02d}"` (Python) atau `String.format("%d:%02d", detik / 60, detik % 60)` (Java).
- Salinan list: `list(self._daftar_lagu)` (Python) atau `new ArrayList<>(daftarLagu)` (Java).
- Objek `bengawan` cukup dibuat **sekali**, lalu dimasukkan ke dua playlist.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_playlist.py) · [☕ Java](java/solusi/Latihan02Playlist.java)

---

## Latihan 3 — Gudang Paket dan Kurir (⭐⭐ Menengah)

**Tujuan:** memakai asosiasi `0..1`, mencari objek yang bisa gagal, dan membandingkan objek.

**Soal:** Sebuah gudang ekspedisi di Samarinda menampung paket sebelum diantar.

- `Kurir(nama)`.
- `Paket(resi, tujuan, berat_kg)`. Setiap paket punya **nol atau satu** kurir. Awalnya belum ada kurir. Method `tugaskan(kurir)` mengisi kurirnya.
- `Gudang(nama)` dengan method `terima(paket)`, `cari_paket(resi)` yang mengembalikan objek `Paket` atau `None`/`null`, `tugaskan_kurir(resi, kurir)` yang mencetak pesan gagal jika resinya tidak ada, `jumlah_paket_kurir(kurir)`, dan `tampilkan()`.

Data: SMD001 ke Jl. Juanda (2 kg), SMD002 ke Jl. Pahlawan (5 kg), SMD003 ke Jl. Antasari (1 kg); kurir Joko dan Wawan. Tugaskan Joko ke SMD001 dan SMD003, Wawan ke SMD009 (tidak ada), lalu Wawan ke SMD002.

**Contoh output yang diharapkan:**

```text
=== PAKET MASUK ===
Gudang Samarinda (3 paket):
- SMD001 ke Jl. Juanda, 2 kg - kurir: belum ada
- SMD002 ke Jl. Pahlawan, 5 kg - kurir: belum ada
- SMD003 ke Jl. Antasari, 1 kg - kurir: belum ada

=== PENUGASAN KURIR ===
SMD001 diantar oleh Joko
SMD003 diantar oleh Joko
Gagal: paket SMD009 tidak ditemukan
SMD002 diantar oleh Wawan

=== STATUS AKHIR ===
Gudang Samarinda (3 paket):
- SMD001 ke Jl. Juanda, 2 kg - kurir: Joko
- SMD002 ke Jl. Pahlawan, 5 kg - kurir: Wawan
- SMD003 ke Jl. Antasari, 1 kg - kurir: Joko
Paket yang dibawa Joko: 2
Paket yang dibawa Wawan: 1
```

<details>
<summary>💡 Petunjuk</summary>

- Saat menampilkan paket, periksa dulu apakah kurirnya `None`/`null`. Jika ya, tulis `belum ada`.
- Di `tugaskan_kurir()`, simpan hasil `cari_paket()` ke variabel dan periksa sebelum memanggil `tugaskan()`.
- Untuk menghitung paket milik seorang kurir, bandingkan referensinya: `paket.kurir is kurir` (Python) atau `paket.getKurir() == kurir` (Java).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_gudang_paket.py) · [☕ Java](java/solusi/Latihan03GudangPaket.java)

---

## Latihan 4 — Ringkasan Penjualan KedaiKita (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dan merasakan pesan berantai antarobjek.

**Soal:** Salin folder `studi-kasus` pertemuan ini, lalu tambahkan:

1. Method `jumlah_porsi()` / `jumlahPorsi()` di kelas `Pesanan`: total porsi semua item dalam pesanan itu.
2. Property `daftar_pesanan` (Python) atau getter `getDaftarPesanan()` (Java) di kelas `Kedai` yang mengembalikan **salinan** list pesanan.
3. Method `total_pendapatan()` / `totalPendapatan()` di kelas `Kedai`: jumlah total semua pesanan yang tercatat.

Tulis ulang program utama agar hanya berisi skenario berikut: buat pesanan Budi (2 Kopi Susu Gula Aren dan 1 Nasi Goreng Kampung) dan pesanan Siti (2 Es Teh Manis dan 1 Pisang Goreng Keju), tampilkan ringkasannya, lalu buktikan bahwa mengosongkan salinan daftar pesanan tidak merusak catatan kedai.

**Contoh output yang diharapkan:**

```text
=== RINGKASAN PESANAN ===
P001 - Budi Santoso: 3 porsi, Rp61.000
P002 - Siti Aminah: 3 porsi, Rp31.000
Total pendapatan KedaiKita: Rp92.000

=== SALINAN TIDAK MERUSAK CATATAN ===
Salinan dikosongkan, pesanan tercatat tetap 2
```

<details>
<summary>💡 Petunjuk</summary>

- `jumlah_porsi()` mirip `hitung_total()`: perulangan atas item, tetapi yang dijumlahkan adalah `item.jumlah` / `item.getJumlah()`.
- `total_pendapatan()` cukup bertanya ke setiap pesanan lewat `hitung_total()`. Jangan menghitung ulang harga menu di kelas `Kedai`.
- File solusi berupa **satu file** berisi versi ringkas kelas-kelas studi kasus, agar mudah dijalankan. Di versi Java, kelas-kelasnya diberi akhiran `Ringkas` (misalnya `PesananRingkas`) agar tidak bentrok dengan kelas `Pesanan` di folder studi kasus. Di proyekmu sendiri, cukup ubah file `pesanan.py`/`Pesanan.java` dan `kedai.py`/`Kedai.java`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_ringkasan_kedai.py) · [☕ Java](java/solusi/Latihan04RingkasanKedai.java)

---

## Latihan 5 — Perpustakaan Mini (⭐⭐⭐ Tantangan)

**Tujuan:** memadukan agregasi, komposisi, asosiasi, dan dependensi dalam satu program.

**Soal:** Pojok Baca TI meminjamkan buku kepada anggotanya.

- `Buku(kode, judul)` dan `Anggota(nama)`.
- `Peminjaman(buku, anggota)`: mengenal buku dan peminjamnya, punya status aktif atau selesai.
- `Perpustakaan(nama)`:
  - `tambah_buku(buku)`: buku dibuat di luar lalu didaftarkan (agregasi),
  - `pinjam(kode, anggota)`: membuat objek `Peminjaman` **di dalam** perpustakaan (komposisi), dengan aturan berikut, diperiksa berurutan: buku harus ada, buku tidak sedang dipinjam, dan anggota paling banyak meminjam **2** buku sekaligus,
  - `kembalikan(kode)`: menyelesaikan peminjaman yang masih aktif untuk buku itu,
  - `tampilkan_koleksi()` dan `tampilkan_riwayat()`.

Skenario: daftarkan B01 *Laskar Pelangi*, B02 *Bumi Manusia*, dan B03 *Negeri 5 Menara*. Ayu meminjam B01, B02, lalu B03. Bima meminjam B02, B99, lalu B03. Setelah itu, B01 dikembalikan dua kali.

**Contoh output yang diharapkan:**

```text
=== KOLEKSI AWAL ===
Koleksi Pojok Baca TI:
- [B01] Laskar Pelangi: tersedia
- [B02] Bumi Manusia: tersedia
- [B03] Negeri 5 Menara: tersedia

=== PEMINJAMAN ===
Ayu meminjam Laskar Pelangi
Ayu meminjam Bumi Manusia
Gagal: Ayu sudah meminjam 2 buku
Gagal: Bumi Manusia sedang dipinjam Ayu
Gagal: buku B99 tidak ditemukan
Bima meminjam Negeri 5 Menara

=== PENGEMBALIAN ===
Ayu mengembalikan Laskar Pelangi
Gagal: Laskar Pelangi tidak sedang dipinjam

=== KOLEKSI AKHIR ===
Koleksi Pojok Baca TI:
- [B01] Laskar Pelangi: tersedia
- [B02] Bumi Manusia: dipinjam Ayu
- [B03] Negeri 5 Menara: dipinjam Bima

=== RIWAYAT ===
Riwayat peminjaman:
  1. Laskar Pelangi oleh Ayu (selesai)
  2. Bumi Manusia oleh Ayu (aktif)
  3. Negeri 5 Menara oleh Bima (aktif)
```

<details>
<summary>💡 Petunjuk</summary>

- Status "sedang dipinjam" tidak perlu disimpan di `Buku`. Buat method pembantu `_peminjaman_aktif(buku)` / `peminjamanAktif(buku)` yang mencari peminjaman aktif untuk buku itu di riwayat, atau mengembalikan `None`/`null`.
- Buat juga method pembantu yang menghitung jumlah peminjaman aktif milik seorang anggota.
- Bandingkan buku dan anggota dengan `is` (Python) atau `==` (Java), karena yang dicari adalah objek yang **sama**.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_perpustakaan.py) · [☕ Java](java/solusi/Latihan05Perpustakaan.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Unit Kegiatan Mahasiswa (UKM)

Sebuah UKM di kampus ingin mencatat anggota dan kegiatannya.

**Kebutuhan:**

1. Kelas `Mahasiswa` (NIM, nama). Seorang mahasiswa boleh menjadi anggota beberapa UKM.
2. Kelas `UKM` (nama) yang menyimpan daftar anggota (**agregasi**) dan daftar kegiatan (**komposisi**).
3. Kelas `Kegiatan` (nama kegiatan, tanggal sebagai teks, misalnya `"12 Oktober"`). Setiap kegiatan punya **tepat satu** penanggung jawab dan **nol atau lebih** peserta. Keduanya harus anggota UKM itu.
4. Method `UKM.buat_kegiatan(nama, tanggal, nim_penanggung_jawab)`: membuat objek `Kegiatan` **di dalam** UKM. Tolak dengan pesan yang jelas jika NIM penanggung jawab bukan anggota (gunakan pencarian yang mengembalikan `None`/`null`).
5. Method untuk mendaftarkan peserta kegiatan berdasarkan NIM, dengan aturan yang sama.
6. Getter daftar anggota dan daftar kegiatan wajib mengembalikan **salinan** list.
7. Program dipecah menjadi **beberapa file**: satu kelas per file ditambah `main.py`/`Main.java`. Tulis cara menjalankannya di komentar bagian atas file utama.
8. Program utama menampilkan minimal: daftar anggota, dua kegiatan beserta penanggung jawab dan pesertanya, serta satu percobaan yang ditolak.

**Ketentuan pengumpulan:** folder program (Python atau Java), tangkapan layar output, dan diagram kelas sederhana (boleh Mermaid atau gambar tangan) yang menunjukkan jenis relasi serta multiplisitasnya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Pemilihan jenis relasi tepat dan dijelaskan di komentar atau diagram | 25% |
| Aturan multiplisitas dan pencarian `None`/`null` ditangani dengan benar | 25% |
| Getter mengembalikan salinan list; data tidak bisa dirusak dari luar | 15% |
| Program multi-file berjalan dari foldernya sesuai petunjuk | 20% |
| Kerapian kode: nama jelas, komentar secukupnya, output rapi | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
