# Latihan — Pertemuan 15: Proyek Terintegrasi

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Latihan 1–4 adalah program mandiri: jalankan, lalu bandingkan output-mu dengan **contoh output**. Latihan 5–6 mengembangkan KedaiKita: kerjakan pada **salinan** folder `studi-kasus`.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Biasakan menulis file latihan ke **folder sementara** (`tempfile.TemporaryDirectory()` atau `Files.createTempDirectory()`), seperti di semua solusi. Folder latihanmu tetap bersih, dan program bisa dijalankan berulang kali dengan hasil yang sama.

## Latihan 1 — Buku Tamu Pameran (⭐ Dasar)

**Tujuan:** menulis, menambah, dan membaca file teks.

**Soal:** Pameran proyek PBO mencatat tamu di file `buku-tamu.txt`, satu tamu per baris dengan format `Nama - Asal`. Tulis tiga tamu pertama ke file baru: Ayu Lestari (Samarinda), Bima Saputra (Balikpapan), Citra Dewi (Samarinda). Lalu tambahkan tamu susulan **tanpa menghapus** isi lama: Dimas Pratama (Bontang). Terakhir, baca file baris demi baris, tampilkan bernomor, dan hitung jumlah tamu serta tamu dari Samarinda.

**Contoh output yang diharapkan:**

```text
=== BUKU TAMU PAMERAN PROYEK PBO ===
3 tamu pertama ditulis ke buku-tamu.txt
1 tamu susulan ditambahkan

Isi buku tamu:
1. Ayu Lestari (Samarinda)
2. Bima Saputra (Balikpapan)
3. Citra Dewi (Samarinda)
4. Dimas Pratama (Bontang)

Jumlah tamu         : 4
Tamu dari Samarinda : 2
```

<details>
<summary>💡 Petunjuk</summary>

- Mode `"w"` untuk tiga tamu pertama, mode `"a"` untuk tamu susulan. Di Java: `Files.writeString(...)` lalu `Files.writeString(..., StandardOpenOption.APPEND)`.
- Pecah setiap baris dengan `split(" - ")`. Di Python, buang `"\n"` dulu dengan `strip()`. Di Java, bandingkan teks dengan `equals()`, bukan `==`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_buku_tamu.py) · [☕ Java](java/solusi/Latihan01BukuTamu.java)

## Latihan 2 — Simpan dan Muat Data Pelanggan (⭐ Dasar)

**Tujuan:** menyimpan objek ke CSV dan menghidupkannya kembali.

**Soal:** Buat kelas pelanggan (nama, no HP, poin) dengan method `ke_kolom()`/`keKolom()` dan `dari_kolom()`/`dariKolom()`, serta kelas `RepositoriPelangganCSV` dengan method `simpan(daftar)` dan `muat()`. Format file: `nama;no_hp;poin` dengan baris judul. Simpan Budi Santoso (081234567890, 12 poin), Siti Aminah (082198765432, 3 poin), dan Rina Marlina (085312345678, 0 poin). Muat kembali, tambahkan 5 poin untuk Siti, simpan lagi, lalu **muat ulang dari file** untuk membuktikan perubahannya tersimpan.

**Contoh output yang diharapkan:**

```text
=== SIMPAN 3 PELANGGAN ===
Isi pelanggan.csv:
nama;no_hp;poin
Budi Santoso;081234567890;12
Siti Aminah;082198765432;3
Rina Marlina;085312345678;0

=== MUAT KEMBALI ===
Budi Santoso (081234567890) - 12 poin
Siti Aminah (082198765432) - 3 poin
Rina Marlina (085312345678) - 0 poin

=== SITI BERTRANSAKSI (+5 POIN), LALU DISIMPAN ULANG ===
Setelah dimuat ulang dari file:
Budi Santoso (081234567890) - 12 poin
Siti Aminah (082198765432) - 8 poin
Rina Marlina (085312345678) - 0 poin
Total poin semua pelanggan: 20
```

<details>
<summary>💡 Petunjuk</summary>

- Tiru `RepositoriMenuCSV` di studi kasus, tetapi dengan tiga kolom saja. File hanya menyimpan teks: ubah poin dengan `str()`/`String.valueOf()` saat menyimpan dan `int()`/`Integer.parseInt()` saat memuat.
- Pengguna Java: beri nama kelasmu `PelangganKedai`, karena folder `java/` pertemuan ini sudah punya kelas `Pelanggan`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_simpan_pelanggan.py) · [☕ Java](java/solusi/Latihan02SimpanPelanggan.java)

## Latihan 3 — Melanjutkan Nomor Pesanan dari File (⭐⭐ Menengah)

**Tujuan:** membaca data lama untuk melanjutkan keadaan program.

**Soal:** Di mode interaktif KedaiKita, nomor pesanan selalu mulai dari P001 setiap kali aplikasi dibuka, sehingga `transaksi.csv` bisa berisi nomor ganda. Buat fungsi `nomor_berikutnya(path)` / `nomorBerikutnya(path)` yang membaca file transaksi (format `nomor;pelanggan;no_hp;jumlah_porsi;total`) dan mengembalikan nomor berikutnya. Jika file belum ada atau hanya berisi judul, hasilnya `P001`. Selain itu, ambil angka **terbesar**, tambah 1, dan format sebagai `P` + minimal 3 digit. Uji dengan skenario di bawah, lalu tunjukkan mengapa nomor tidak boleh dibandingkan sebagai teks.

**Contoh output yang diharapkan:**

```text
=== NOMOR PESANAN BERIKUTNYA ===
File belum ada              -> P001
Hanya baris judul           -> P001
P001, P002, P003            -> P004
P001, P002, P001 (ganda)    -> P003
P998, P999, P1000           -> P1001

=== JEBAKAN: MEMBANDINGKAN SEBAGAI TEKS ===
Nomor terbesar menurut abjad: P999 (SALAH)
```

<details>
<summary>💡 Petunjuk</summary>

- `"P012"[1:]` (Python) atau `"P012".substring(1)` (Java) menghasilkan `"012"`, lalu ubah ke `int`. Format kembali dengan `f"P{angka:03d}"` atau `String.format("P%03d", angka)`.
- Sebagai teks, `"P999"` lebih besar daripada `"P1000"`, karena dibandingkan huruf demi huruf (`'9' > '1'`).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_nomor_pesanan.py) · [☕ Java](java/solusi/Latihan03NomorPesanan.java)

<details>
<summary>Bonus: memasang solusinya ke KedaiKita</summary>

Tambahkan method milik kelas di `Pesanan` untuk mengatur penghitung nomor (Python, di `pesanan.py`):

```python
    @classmethod
    def lanjutkan_nomor(cls, nomor_terakhir: int):
        """Nomor pesanan berikutnya dimulai setelah nomor_terakhir."""
        cls._nomor_terakhir = nomor_terakhir
```

Lalu panggil di `AplikasiKasir.jalankan()`, tepat setelah `layanan` disiapkan:

```python
        terbesar = 0
        for kolom in pencatat.baca_semua():
            terbesar = max(terbesar, int(kolom[0][1:]))  # "P012" -> 12
        Pesanan.lanjutkan_nomor(terbesar)
```

Versi Java sama persis polanya: method `public static void lanjutkanNomor(int nomorTerakhirDiFile)` di `Pesanan` yang mengisi field `static` `nomorTerakhir`, lalu perulangan atas `pencatat.bacaSemua()` dengan `Integer.parseInt(kolom[0].substring(1))` dan `Math.max()`. Sekarang sesi kedua mencatat `P002`, bukan `P001` lagi, sedangkan mode demo tidak terpengaruh.

</details>

## Latihan 4 — Validasi Nomor HP dan Unit Test-nya (⭐⭐ Menengah)

**Tujuan:** menulis validasi input yang jelas, lalu mengujinya secara otomatis.

**Soal:** Buat fungsi `validasi_no_hp(teks)` / `validasiNoHp(teks)` yang membuang spasi dan tanda hubung, lalu memeriksa aturan berikut **sesuai urutan**. Pelanggaran melempar `ValueError`/`IllegalArgumentException` dengan pesan di tabel. Tulis juga **minimal 7 unit test**: kasus normal, kasus gagal, kasus **batas** (tepat 10 dan tepat 13 digit), dan satu test yang memeriksa **isi pesan** error-nya.

| Aturan | Pesan jika dilanggar |
|---|---|
| tidak kosong | `Nomor HP tidak boleh kosong` |
| hanya angka 0–9 | `Nomor HP hanya boleh berisi angka` |
| diawali `08` | `Nomor HP harus diawali 08` |
| panjang 10–13 digit | `Nomor HP harus 10 sampai 13 digit` |

**Contoh output yang diharapkan:**

```text
=== VALIDASI NOMOR HP ===
'0812-3456-7890' -> 081234567890
'0812 3456 789' -> 08123456789
'08123' -> ditolak: Nomor HP harus 10 sampai 13 digit
'0812abc4567' -> ditolak: Nomor HP hanya boleh berisi angka
'6281234567890' -> ditolak: Nomor HP harus diawali 08
'' -> ditolak: Nomor HP tidak boleh kosong

=== UNIT TEST ===
[LULUS] Panjang tepat 10 dan tepat 13 digit diterima
[LULUS] Spasi dan tanda hubung dibersihkan
[LULUS] Nomor berisi huruf ditolak dengan pesan yang tepat
[LULUS] Nomor kosong ditolak
[LULUS] Lebih dari 13 digit ditolak
[LULUS] Kurang dari 10 digit ditolak
[LULUS] Nomor yang tidak diawali 08 ditolak
Hasil: 7 lulus, 0 gagal
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa angka satu per satu: `"0" <= huruf <= "9"` (Python) atau `huruf >= '0' && huruf <= '9'` (Java).
- Python: `with self.assertRaises(ValueError) as konteks:` lalu `str(konteks.exception)` berisi pesannya. Java: buat `harusMelempar()` yang **mengembalikan** *exception* yang tertangkap (seperti `assertThrows` di JUnit).
- Untuk output tanpa catatan waktu, tiru pencatat hasil di contoh 05.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_validasi_no_hp.py) · [☕ Java](java/solusi/Latihan04ValidasiNoHp.java)

## Latihan 5 — Menu "Ubah Harga" di Aplikasi Kasir (⭐⭐⭐ Tantangan)

**Tujuan:** menambah fitur ke aplikasi berlapis tanpa melanggar pembagian tugas antarlapisan.

**Soal:** Tambahkan pilihan `5. Ubah harga menu` di menu utama KedaiKita. Kasir memasukkan kode menu dan harga baru. Kode yang salah dan harga ≤ 0 harus ditolak dengan pesan `[GAGAL] ...`, dan harga baru harus ikut tersimpan ke `menu.csv` saat keluar. Tambahkan juga unit test-nya.

**Contoh interaksi yang diharapkan** (ketikan kasir ditulis setelah tanda titik dua):

```text
Pilihan: 5
Kode menu: m01
Harga baru: 20000
Harga Kopi Susu Gula Aren kini Rp20.000
...
Pilihan: 5
Kode menu: M02
Harga baru: nol
  Harap isi dengan angka bulat, misalnya 2 atau 50000.
Harga baru: 0
[GAGAL] Harga harus lebih dari 0
```

<details>
<summary>💡 Petunjuk</summary>

- Lapisan **layanan**: method `ubah_harga(kode, harga_baru)` / `ubahHarga(kode, hargaBaru)` di `LayananKasir`. Jangan menulis ulang aturan "harga > 0"; *setter* harga milik `Menu` sudah menjaganya.
- Lapisan **tampilan**: satu cabang baru di menu utama dan method kecil yang bertanya kode dan harga (pakai `_tanya_angka`/`tanyaAngka`). Penyimpanan tidak perlu diubah.

</details>

<details>
<summary>Lihat solusi</summary>

**Python**, `kedaikita/layanan.py` dan `kedaikita/aplikasi.py` (ditambah `print("5. Ubah harga menu")`, cabang `elif pilihan == "5":`, dan impor `format_rupiah`):

```python
    def ubah_harga(self, kode: str, harga_baru: int) -> Menu:
        """Mengubah harga menu. Aturan harga tetap dijaga oleh setter Menu."""
        menu = self._kedai.cari_menu(kode)  # MenuTidakDitemukanError jika kode salah
        menu.harga = harga_baru  # ValueError jika harga <= 0
        return menu
```

```python
    def _alur_ubah_harga(self, layanan: LayananKasir):
        kode = self._tanya("Kode menu: ").upper()
        harga_baru = self._tanya_angka("Harga baru: ")
        try:
            menu = layanan.ubah_harga(kode, harga_baru)
            print(f"Harga {menu.nama} kini {format_rupiah(menu.harga)}")
        except (KedaiError, ValueError) as e:
            print(f"[GAGAL] {e}")
```

**Java:** `LayananKasir` mendapat method `public Menu ubahHarga(String kode, int hargaBaru) throws KedaiException` berisi `kedai.cariMenu(kode)` lalu `menu.setHarga(hargaBaru)`. Method tampilan `alurUbahHarga()` di `AplikasiKasir` mengikuti pola Python dengan `catch (KedaiException | IllegalArgumentException e)`.

**Unit test:** buat `Kedai` berisi satu menu (misalnya `Minuman("M01", "Kopi", 18000, 5)`) dan `LayananKasir(kedai, [])`, lalu periksa bahwa `ubah_harga("M01", 20000)` mengubah harganya, sedangkan `ubah_harga("M01", 0)` melempar `ValueError` dan harganya tetap 18000.

**Catatan desain:** `ItemPesanan` menyimpan *referensi* ke objek `Menu` (Pertemuan 05), bukan salinan harganya. Jika harga diubah setelah ada pesanan LUNAS, "Laporan penjualan sesi ini" ikut dihitung ulang dengan harga baru, padahal `transaksi.csv` tetap mencatat total lama. Aplikasi kasir sungguhan menyimpan harga **saat transaksi** di dalam item pesanan. Coba perbaiki ini sebagai tantangan tambahan.

</details>

## Latihan 6 — Ekspor Laporan ke File Teks (⭐⭐⭐ Tantangan)

**Tujuan:** memisahkan "menyusun teks" dari "menampilkan teks" agar hasilnya bisa dipakai ulang.

**Soal:** Tambahkan pilihan `6. Ekspor laporan ke file teks` yang menyimpan laporan penjualan sesi ini ke `data/laporan.txt`. Isi file harus **sama persis** dengan yang dicetak pilihan 3. Tambahkan unit test yang membuktikannya.

<details>
<summary>💡 Petunjuk</summary>

- Tiru `StrukPesanan`: pindahkan isi `cetak()` milik `LaporanPenjualan` ke method baru `buat_teks()`/`buatTeks()` yang **mengembalikan** teks. `cetak()` cukup mencetak hasilnya, dan method baru `simpan_ke(path)`/`simpanKe(path)` menulisnya ke file. Karena keduanya memakai `buat_teks()`, isi layar dan file dijamin sama.
- Tambahkan `**/data/laporan.txt` ke `.gitignore` agar file hasil aplikasi tidak ikut tersimpan di Git.

</details>

<details>
<summary>Lihat solusi</summary>

Di `buat_teks()`/`buatTeks()`, setiap baris yang tadinya dicetak dikumpulkan ke sebuah list, misalnya `baris.append(f"{kategori:<30}{format_rupiah(nilai):>10}")`, lalu dikembalikan sebagai `"\n".join(baris)` / `String.join("\n", baris)`. Sisanya:

**Python**, `kedaikita/laporan.py` (tambahkan `from pathlib import Path`):

```python
    def cetak(self):
        print(self.buat_teks())

    def simpan_ke(self, path: Path):
        """Menyimpan laporan ke file teks (isi lama ditimpa)."""
        with open(path, "w", encoding="utf-8", newline="") as berkas:
            berkas.write(self.buat_teks() + "\n")
```

**Java:** `cetak()` cukup berisi `System.out.println(buatTeks());`, dan method baru `public void simpanKe(Path path) throws IOException` berisi `Files.writeString(path, buatTeks() + "\n", StandardCharsets.UTF_8);`.

Cabang pilihan `"6"` di `AplikasiKasir` cukup memanggil `layanan.laporan().simpan_ke(...)` dengan path `data/laporan.txt`, lalu mencetak `Laporan disimpan ke data/laporan.txt`. Test-nya menyimpan laporan ke folder sementara, lalu memeriksa bahwa isi file sama dengan `buat_teks() + "\n"`. Output mode demo tidak berubah sedikit pun setelah *refactoring* ini, dan `laporan.txt` versi Python dan Java isinya identik.

</details>

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Tahap 1 Proyek Akhir: Kebutuhan dan Rancangan

Tugas ini adalah langkah pertama [proyek akhirmu](proyek-akhir.md). Pilih **satu tema** dari daftar di dokumen proyek akhir (bukan kafe), lalu siapkan dokumen rancangan berisi:

1. **Deskripsi singkat** (3–5 kalimat): siapa penggunanya dan masalah apa yang diselesaikan.
2. **Daftar kebutuhan**: minimal 6 kebutuhan fungsional dan 3 kebutuhan non-fungsional, dalam tabel seperti di bagian 1 halaman konsep.
3. **Diagram kelas UML** (Mermaid): minimal 6 kelas dengan atribut, method utama, relasi, satu hierarki pewarisan, dan satu kelas abstrak atau *interface*.
4. **Peta lapisan**: kelas mana di lapisan tampilan, layanan, model, dan penyimpanan.
5. **Format file data**: nama kolom tiap file CSV beserta 3 baris contoh.
6. **Rencana 5 kasus uji**: minimal satu kasus normal, satu kasus gagal, dan satu kasus batas.

**Ketentuan pengumpulan:** satu file `RANCANGAN.md` di repositori proyekmu (atau format lain sesuai arahan dosen).

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kebutuhan jelas, terukur, dan sesuai tema | 20% |
| Diagram kelas benar (notasi, relasi, multiplisitas) dan memenuhi kebutuhan minimum | 35% |
| Peta lapisan masuk akal dan konsisten dengan diagram | 15% |
| Format file data dan rencana kasus uji (normal, gagal, batas) | 20% |
| Kerapian dan kejelasan dokumen | 10% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
