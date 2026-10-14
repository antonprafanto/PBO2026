# Latihan Pertemuan 07: Pewarisan

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Siapkan folder kerjamu sendiri **di luar** folder materi, yaitu `PBO-latihan-saya/pertemuan-07` (misalnya di dalam folder `Documents`; lihat [aturan emas 00-Persiapan](../00-Persiapan/git-dan-github.md#5-menyimpan-latihanmu-sendiri)). Jangan menyimpan jawaban di dalam folder `PBO2026`: jawabanmu bisa tertimpa saat materi diperbarui, dan khusus Java, nama kelasmu bisa bentrok dengan kelas di *file* solusi. Buka folder kerja itu di VS Code (**File → Open Folder**).
3. Buat satu *file* untuk setiap latihan, misalnya `latihan01.py` atau `Latihan01.java`. Untuk Java, tulis kelas yang punya `main` paling atas, dan samakan nama *file* dengan nama kelas itu.
4. Jalankan *file*-mu di VS Code: tombol ▷ (**Run Python File**) untuk Python, atau **Run** pada tulisan **Run | Debug** di atas `main` untuk Java. Bisa juga lewat terminal. Terminal VS Code di jendela itu sudah berada di folder `pertemuan-07`; dari terminal lain, masuk dulu dengan `cd Documents\PBO-latihan-saya\pertemuan-07` (Windows) atau `cd ~/Documents/PBO-latihan-saya/pertemuan-07` (macOS/Linux). Setelah itu, ketik `python latihan01.py` (macOS/Linux: `python3 latihan01.py`) atau `java Latihan01.java`.
5. Bandingkan *output*-mu dengan **contoh *output*** di soal. Teksnya harus sama persis, termasuk spasi dan tanda baca.
6. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri. Tautan **Solusi** di setiap soal membuka *file* solusinya. Untuk menjalankannya, ikuti cara di halaman praktik ([🐍 Python](python/README.md#cara-menjalankan-contoh) atau [☕ Java](java/README.md#cara-menjalankan-contoh)), tetapi masuklah ke folder `solusi`, bukan `contoh`. Contohnya, dari folder utama materi: `cd Pertemuan-07-Pewarisan/python/solusi` lalu `python latihan01_asisten_praktikum.py`.
7. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Sebelum menulis `class Anak(Induk)` atau `class Anak extends Induk`, ucapkan dulu kalimat "Anak **adalah** Induk". Jika terdengar janggal, mungkin yang kamu butuhkan bukan pewarisan.

---

## Latihan 1: Mahasiswa dan Asisten Praktikum (⭐ Dasar)

**Tujuan:** membuat kelas anak yang memanggil konstruktor induk, lalu menambah atribut dan *method*.

**Soal:** Buat kelas `Mahasiswa` dengan atribut NIM dan nama, serta *method* `perkenalan()` yang mengembalikan teks `Halo, saya <nama> (NIM <nim>)`. Lalu buat kelas anak `AsistenPraktikum` yang menambah atribut `praktikum` dan *method* `tugas()`.

Data uji: Bima Saputra (NIM 2409106002) sebagai mahasiswa biasa, dan Ayu Lestari (NIM 2309106001) sebagai asisten praktikum Pemrograman Berorientasi Objek. Tampilkan juga apakah Ayu termasuk `Mahasiswa`.

**Contoh *output* yang diharapkan:**

```text
=== MAHASISWA BIASA ===
Halo, saya Bima Saputra (NIM 2409106002)

=== ASISTEN PRAKTIKUM ===
Halo, saya Ayu Lestari (NIM 2309106001)
Ayu Lestari mengasisteni praktikum Pemrograman Berorientasi Objek
Ayu Lestari termasuk Mahasiswa? ya
```

<details>
<summary>💡 Petunjuk</summary>

- Baris pertama konstruktor anak: `super().__init__(nim, nama)` (Python) atau `super(nim, nama);` (Java).
- `perkenalan()` **tidak** perlu ditulis ulang di `AsistenPraktikum`.
- Di Java, nama milik induk bersifat `private`, jadi `tugas()` membacanya lewat `getNama()`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_asisten_praktikum.py) · [☕ Java](java/solusi/Latihan01AsistenPraktikum.java)

---

## Latihan 2: Akun dan Akun Premium (⭐ Dasar)

**Tujuan:** meng-*override* *method* sambil memakai versi induknya.

**Soal:** Buat kelas `Akun` (*username*, *email*) dengan dua *method*:

- `info()` mengembalikan *username*, spasi, lalu *email* di antara tanda `<` dan `>`, misalnya `budi_s <budi@contoh.id>`.
- `batas_unggah_mb()` / `batasUnggahMb()` mengembalikan 100.

Buat kelas anak `AkunPremium` yang menambah masa aktif (bulan). *Override* kedua *method*:

- `info()`: teks versi induk ditambah ` [PREMIUM <n> bulan]`.
- Batas unggah: **10 kali** hasil versi induk (jangan menulis angka 1000 secara langsung).

Data uji: akun biasa `budi_s` (`budi@contoh.id`) dan akun premium `siti_a` (`siti@contoh.id`, 6 bulan).

**Contoh *output* yang diharapkan:**

```text
=== DAFTAR AKUN ===
budi_s <budi@contoh.id>
siti_a <siti@contoh.id> [PREMIUM 6 bulan]

=== BATAS UNGGAH ===
budi_s: 100 MB
siti_a: 1000 MB
```

<details>
<summary>💡 Petunjuk</summary>

- Versi induk dipanggil dengan `super().info()` (Python) atau `super.info()` (Java).
- Di Java, tulis `@Override` di atas kedua *method* dan pertahankan `public`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_akun_premium.py) · [☕ Java](java/solusi/Latihan02AkunPremium.java)

---

## Latihan 3: Gaji Pegawai Tetap dan Kontrak (⭐⭐ Menengah)

**Tujuan:** dua kelas anak yang meng-*override* *method* yang sama dengan cara berbeda.

**Soal:** Kelas induk `Pegawai` menyimpan NIP, nama, dan gaji pokok (harus lebih dari 0). *Method* `hitung_gaji()` / `hitungGaji()` versi induk mengembalikan gaji pokok, dan teks objeknya `<nip> <nama>`. Buat dua kelas anak:

| Kelas anak | Tambahan | Gaji | Teks objek |
|---|---|---|---|
| `PegawaiTetap` | tunjangan | gaji pokok + tunjangan | ditambah ` (tetap)` |
| `PegawaiKontrak` | jam lembur (tidak boleh negatif) | gaji pokok + jam lembur x Rp40.000 | ditambah ` (kontrak)` |

Simpan tiga pegawai dalam *list*/`List`, lalu cetak slip gaji beserta totalnya. Uang ditampilkan dengan format Rupiah bertitik.

Data uji:

| NIP | Nama | Jenis | Gaji pokok | Tambahan |
|---|---|---|---|---|
| 198703 | Andi Wijaya | tetap | Rp6.000.000 | tunjangan Rp1.500.000 |
| 200105 | Rina Marlina | kontrak | Rp4.400.000 | lembur 20 jam |
| 199912 | Dodi Pratama | kontrak | Rp4.500.000 | lembur 0 jam |

**Contoh *output* yang diharapkan:**

```text
=== SLIP GAJI OKTOBER 2026 ===
198703 Andi Wijaya (tetap)       Rp7.500.000
200105 Rina Marlina (kontrak)    Rp5.200.000
199912 Dodi Pratama (kontrak)    Rp4.500.000
--------------------------------------------
Total gaji                      Rp17.200.000
```

<details>
<summary>💡 Petunjuk</summary>

- Kedua kelas anak memakai `super().hitung_gaji()` / `super.hitungGaji()`, lalu menambahkan komponennya masing-masing.
- Lebar kolom: Python `f"{str(p):<30}{format_rupiah(gaji):>14}"`, Java `String.format("%-30s%14s", ...)`. Garis pemisahnya 44 tanda `-`.
- Saat perulangan memanggil `hitung_gaji()`, setiap objek otomatis memakai versinya sendiri. Ini cikal bakal **polimorfisme** (Pertemuan 09).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_gaji_pegawai.py) · [☕ Java](java/solusi/Latihan03GajiPegawai.java)

---

## Latihan 4: *Playlist* Bukan Lagu (⭐⭐ Menengah)

**Tujuan:** membedakan *is-a* dan *has-a*, lalu memperbaiki rancangan yang keliru.

**Bagian A (analisis).** Untuk setiap pasangan kelas `X` dan `Y` berikut, tentukan apakah hubungannya *is-a* ("X adalah Y") atau *has-a* ("X punya Y"): (1) `Dosen` dan `Pegawai`, (2) `Laptop` dan `Keyboard`, (3) `Segitiga` dan `BangunDatar`, (4) `Perpustakaan` dan `Buku`, (5) `Playlist` dan `Lagu`.

<details>
<summary>Lihat jawaban Bagian A</summary>

1. *is-a*: dosen adalah pegawai.
2. *has-a*: laptop punya *keyboard*.
3. *is-a*: segitiga adalah bangun datar.
4. *has-a*: perpustakaan punya banyak buku (agregasi).
5. *has-a*: *playlist* punya banyak lagu. *Playlist* bukan sebuah lagu!

</details>

**Bagian B (kode).** Seorang teman menulis rancangan berikut (potongan kode, tidak untuk dijalankan sendiri). Programnya berjalan, tetapi rancangannya keliru.

**Python:**

```python
class Playlist(Lagu):  # KELIRU: playlist bukan lagu
    def __init__(self, nama: str):
        super().__init__(nama, 0)  # playlist dipaksa punya "durasi" sendiri
```

**Java:**

```java
class Playlist extends Lagu { // KELIRU: playlist bukan lagu
    public Playlist(String nama) {
        super(nama, 0); // playlist dipaksa punya "durasi" sendiri
    }
}
```

Tulis ulang `Playlist` **tanpa pewarisan**: simpan daftar objek `Lagu` (judul, durasi dalam detik) sebagai atribut, lalu buat *method* `tambah(lagu)`, `total_durasi()` / `totalDurasi()`, dan `tampilkan()`.

Data uji: *playlist* bernama Lagu Daerah Kalimantan berisi Ampar-Ampar Pisang (132 detik), Paris Barantai (185 detik), dan Indung-Indung (170 detik).

**Contoh *output* yang diharapkan:**

```text
=== PLAYLIST: Lagu Daerah Kalimantan ===
1. Ampar-Ampar Pisang (2:12)
2. Paris Barantai (3:05)
3. Indung-Indung (2:50)
Jumlah lagu : 3
Total durasi: 8 menit 7 detik
```

<details>
<summary>💡 Petunjuk</summary>

- Atribut daftar lagu: `self._daftar_lagu: list[Lagu] = []` (Python) atau `private List<Lagu> daftarLagu = new ArrayList<>();` (Java).
- Durasi 185 detik ditampilkan `3:05`: menit `185 // 60`, detik `185 % 60` dengan dua digit (`:02d` atau `String.format("%02d", ...)`).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_playlist.py) · [☕ Java](java/solusi/Latihan04Playlist.java)

---

## Latihan 5: *Snack* untuk KedaiKita (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan kelas anak baru.

**Soal:** Pemilik KedaiKita ingin menjual *snack*, misalnya amplang khas Samarinda. Buat kelas `Snack` sebagai anak `Menu`, seperti `Makanan` dan `Minuman`:

1. Konstruktor menerima kode, nama, harga, stok, dan **berat dalam gram**. Kategori diisi otomatis `"Snack"`.
2. Berat harus lebih dari 0. Jika tidak, tolak dengan `ValueError` / `IllegalArgumentException` berpesan `Berat harus lebih dari 0 gram`.
3. *Override* teks objek: teks versi induk ditambah ` | <berat> gram`.

Uji dengan Keripik Singkong Balado (M07, Rp10.000, stok 20, 150 gram) dan Amplang Ikan Pipih (M08, Rp15.000, stok 15, 100 gram). Pakai juga *method* warisan `harga_setelah_diskon(10)` / `hargaSetelahDiskon(10)`. Untuk menguji validasi, coba buat Kacang Sangrai (M09, Rp8.000, stok 10, 0 gram) di dalam `try`, lalu tampilkan pesan penolakannya.

**Contoh *output* yang diharapkan:**

```text
=== MENU BARU: SNACK ===
[M07] Keripik Singkong Balado (Snack) - Rp10.000 | stok 20 | 150 gram
[M08] Amplang Ikan Pipih (Snack) - Rp15.000 | stok 15 | 100 gram

=== CEK PEWARISAN ===
Amplang Ikan Pipih termasuk Menu? ya
Diskon 10% untuk Amplang Ikan Pipih: Rp13.500

=== VALIDASI ===
Gagal menambah menu: Berat harus lebih dari 0 gram
```

<details>
<summary>💡 Petunjuk</summary>

- Ikuti pola `Makanan` di studi kasus: panggil konstruktor induk dengan kategori `"Snack"`, baru periksa beratnya.
- Di proyek KedaiKita-mu, cukup tambahkan kelas `Snack` ke `menu.py` (Python) atau buat *file* `Snack.java` (Java). *File* solusi dibuat **satu *file*** berisi salinan ringkas kelas `Menu` agar bisa dijalankan sendiri. Di solusi Java, induknya bernama `MenuKedai` agar tidak bentrok dengan kelas `Menu` di folder studi kasus.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_snack_kedaikita.py) · [☕ Java](java/solusi/Latihan05SnackKedaiKita.java)

---

## Latihan 6: Kamar Wisma Tepian (⭐⭐⭐ Tantangan)

**Tujuan:** pewarisan bertingkat tiga dengan *override* berantai.

**Soal:** Sebuah penginapan, Wisma Tepian, punya tiga jenis kamar. Setiap tingkat **memakai hasil hitungan tingkat di atasnya** lewat `super`.

| Kelas | Induk | Tambahan | `hitung_biaya(malam)` / `hitungBiaya(malam)` |
|---|---|---|---|
| `Kamar` | - | nomor, tarif per malam | tarif x malam; tolak jika malam < 1 |
| `KamarDeluxe` | `Kamar` | jumlah tamu (1 sampai 4) | versi induk + Rp50.000 x tamu x malam (sarapan) |
| `KamarSuite` | `KamarDeluxe` | - | versi induk + Rp150.000 (antar-jemput bandara), lalu diskon 10% jika minimal 3 malam |

Teks objek juga berantai: `Kamar 301 - Rp800.000/malam | sarapan 2 tamu | antar-jemput bandara`.

Data uji: kamar 101 (`Kamar`, Rp300.000), kamar 205 (`KamarDeluxe`, Rp450.000, 2 tamu), dan kamar 301 (`KamarSuite`, Rp800.000, 2 tamu). Untuk menguji validasi, hitung biaya kamar 301 selama 0 malam, lalu coba buat kamar deluxe 206 (Rp450.000) untuk 6 tamu. Tangkap kedua penolakan itu dengan `try`.

**Contoh *output* yang diharapkan:**

```text
=== DAFTAR KAMAR WISMA TEPIAN ===
Kamar 101 - Rp300.000/malam
Kamar 205 - Rp450.000/malam | sarapan 2 tamu
Kamar 301 - Rp800.000/malam | sarapan 2 tamu | antar-jemput bandara

=== RINCIAN BIAYA ===
Kamar 101, 2 malam: Rp600.000
Kamar 205, 2 malam: Rp1.100.000
Kamar 301, 2 malam: Rp1.950.000
Kamar 301, 3 malam: Rp2.565.000

=== CEK PEWARISAN ===
Kamar 301 adalah KamarDeluxe? ya
Kamar 301 adalah Kamar?       ya
Kamar 205 adalah KamarSuite?  tidak

=== VALIDASI ===
Ditolak: Lama menginap minimal 1 malam
Ditolak: Jumlah tamu harus 1 sampai 4
```

<details>
<summary>💡 Petunjuk</summary>

- Hitung manual dulu kamar 301 selama 3 malam: 800.000 x 3 + 50.000 x 2 x 3 + 150.000 = 2.850.000, lalu dikurangi 10% menjadi 2.565.000.
- Validasi malam cukup ditulis **sekali** di `Kamar`. Karena tingkat di atasnya selalu memanggil `super`, validasi itu ikut berjalan.
- Python: `KamarSuite` tidak perlu `__init__`. Java: `KamarSuite` tetap wajib punya konstruktor yang memanggil `super(nomor, tarif, jumlahTamu)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_wisma_tepian.py) · [☕ Java](java/solusi/Latihan06WismaTepian.java)

---

## Tugas Mandiri (Dikumpulkan, tanpa Kunci Jawaban)

### Koleksi Perpustakaan Kampus

Perpustakaan kampus meminjamkan beberapa jenis koleksi dengan aturan denda keterlambatan yang berbeda.

**Kebutuhan:**

1. Kelas induk `Koleksi` dengan atribut kode, judul, dan tahun, *method* `hitung_denda(hari_terlambat)` / `hitungDenda(hariTerlambat)` (Rp1.000 per hari), dan teks objek yang rapi.
2. Minimal **tiga** kelas anak, misalnya `Buku` (penulis), `Majalah` (edisi), dan `Skripsi` (NIM penulis). Setiap kelas anak memanggil konstruktor induk, menambah minimal satu atribut, dan meng-*override* teks objek dengan memakai versi induk.
3. Minimal satu kelas anak meng-*override* `hitung_denda` dengan aturan sendiri, dan minimal satu tingkat pewarisan bertingkat, misalnya `BukuReferensi` sebagai anak `Buku` dengan denda dua kali lipat versi induknya.
4. Kelas `Perpustakaan` menyimpan daftar koleksi (*has-a*, **bukan** pewarisan) dan bisa menghitung berapa koleksi yang termasuk `Buku` dengan `isinstance`/`instanceof`.
5. Validasi: tahun dan hari terlambat tidak boleh negatif.
6. Di bagian atas *file*, tulis komentar 2—3 kalimat: mengapa `Perpustakaan` tidak mewarisi `Koleksi`?

**Ketentuan pengumpulan:** satu *file* program (Python atau Java), tangkapan layar *output*-nya, dan diagram kelas (Mermaid atau gambar tangan yang difoto).

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Hierarki benar: konstruktor induk dipanggil, atribut tambahan, minimal satu tingkat bertingkat | 30% |
| *Override* memakai `super` (teks objek dan denda) dan hasil denda benar | 25% |
| `Perpustakaan` memakai *has-a*, `isinstance`/`instanceof`, validasi, dan alasan desain di komentar | 25% |
| Diagram kelas sesuai kode, kerapian kode dan *output* | 20% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
