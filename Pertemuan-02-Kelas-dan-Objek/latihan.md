# Latihan — Pertemuan 02: Kelas dan Objek

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Tidak apa-apa jika kodemu berbeda dengan solusi. Yang penting output-nya benar dan kamu paham **mengapa** kodemu bekerja.

---

## Latihan 1 — Kelas Buku (⭐ Dasar)

**Tujuan:** membuat kelas dengan konstruktor, method yang mencetak, dan method yang mengembalikan nilai.

**Soal:** Buat kelas `Buku` dengan atribut `judul`, `penulis`, dan `tahun` yang diisi lewat konstruktor. Tambahkan:

- method `tampilkan_info()` / `tampilkanInfo()` yang mencetak `judul - penulis (tahun)`,
- method `umur(tahun_sekarang)` yang **mengembalikan** selisih tahun sekarang dengan tahun terbit.

Buat tiga objek buku: *Laskar Pelangi* (Andrea Hirata, 2005), *Bumi Manusia* (Pramoedya Ananta Toer, 1980), dan *Negeri 5 Menara* (Ahmad Fuadi, 2009).

**Contoh output yang diharapkan:**

```text
=== RAK BUKU ===
Laskar Pelangi - Andrea Hirata (2005)
Bumi Manusia - Pramoedya Ananta Toer (1980)
Negeri 5 Menara - Ahmad Fuadi (2009)

=== UMUR BUKU DI TAHUN 2026 ===
Laskar Pelangi: 21 tahun
Bumi Manusia: 46 tahun
Negeri 5 Menara: 17 tahun
```

<details>
<summary>💡 Petunjuk</summary>

- Method `umur` cukup berisi satu baris: kembalikan `tahun_sekarang - tahun` (ingat `self.` di Python).
- Panggil dengan `buku1.umur(2026)` dan tampilkan hasilnya.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_buku.py) · [☕ Java](java/solusi/Latihan01Buku.java)

---

## Latihan 2 — Kelas Ponsel (⭐ Dasar)

**Tujuan:** method yang mengubah keadaan objek dan menjaga batas nilai.

**Soal:** Buat kelas `Ponsel` dengan atribut `merek` dan `baterai` (0–100). Tambahkan method:

- `pakai(menit)`: setiap menit memakai 2% baterai. Jika baterai tidak cukup, baterai menjadi 0 dan cetak `Baterai habis! Ponsel mati.`
- `isi_daya(persen)` / `isiDaya(persen)`: baterai bertambah, tetapi tidak boleh melebihi 100.
- `tampilkan_info()` / `tampilkanInfo()`.

Uji dengan ponsel Samsung, baterai awal 50%: pakai 10 menit, isi daya 100%, lalu pakai 60 menit.

**Contoh output yang diharapkan:**

```text
  Ponsel Samsung - baterai 50%
Dipakai 10 menit, baterai berkurang 20%
  Ponsel Samsung - baterai 30%
Diisi daya 100%
  Ponsel Samsung - baterai 100%
Dipakai 60 menit... Baterai habis! Ponsel mati.
  Ponsel Samsung - baterai 0%
```

<details>
<summary>💡 Petunjuk</summary>

- Hitung dulu `kebutuhan = menit * 2`, lalu bandingkan dengan baterai.
- Pada `isi_daya`, tambahkan dulu, lalu jika lebih dari 100, set menjadi 100.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_ponsel.py) · [☕ Java](java/solusi/Latihan02Ponsel.java)

---

## Latihan 3 — Mahasiswa dan Predikat IPK (⭐⭐ Menengah)

**Tujuan:** method yang mengembalikan teks berdasarkan kondisi, dan banyak objek dalam list/array.

**Soal:** Buat kelas `Mahasiswa` dengan atribut `nim`, `nama`, dan `ipk`. Tambahkan method `predikat()` yang mengembalikan:

| IPK | Predikat |
|---|---|
| 3.51 ke atas | Dengan Pujian |
| 3.01 – 3.50 | Sangat Memuaskan |
| 2.76 – 3.00 | Memuaskan |
| di bawah 2.76 | Cukup |

Simpan empat mahasiswa dalam sebuah list (Python) atau array (Java), lalu tampilkan semuanya dengan perulangan.

**Contoh output yang diharapkan:**

```text
=== DAFTAR PREDIKAT ===
2409106001 Ayu Lestari - IPK 3.75 - Dengan Pujian
2409106002 Bima Saputra - IPK 3.2 - Sangat Memuaskan
2409106003 Citra Dewi - IPK 2.9 - Memuaskan
2409106004 Dimas Pratama - IPK 2.5 - Cukup
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa dari batas tertinggi dulu: `if ipk >= 3.51 ... elif ipk >= 3.01 ...`.
- Di Java, tipe IPK adalah `double`. Gabungkan langsung dengan teks (`"IPK " + ipk`) agar tercetak `3.75`.
- Buat method `tampilkan()` yang memanggil `predikat()` dari dalam kelas.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_mahasiswa.py) · [☕ Java](java/solusi/Latihan03Mahasiswa.java)

---

## Latihan 4 — Kalkulator Nilai Mata Kuliah (⭐⭐ Menengah)

**Tujuan:** method yang memanggil method lain milik objek yang sama.

**Soal:** Buat kelas `NilaiKuliah` dengan atribut `nama_mk`, `tugas`, `uts`, dan `uas` (semuanya bilangan bulat). Tambahkan method:

- `nilai_akhir()`: 30% tugas + 30% UTS + 40% UAS, dibulatkan ke bawah menjadi bilangan bulat,
- `huruf()`: A (≥ 80), B (≥ 70), C (≥ 60), D (≥ 50), E (di bawahnya). Gunakan `nilai_akhir()` di dalamnya,
- `lulus(batas)`: mengembalikan benar/salah apakah nilai akhir ≥ batas.

Uji dengan tiga mata kuliah berikut dan batas lulus 60.

| Mata kuliah | Tugas | UTS | UAS |
|---|---|---|---|
| Pemrograman Berorientasi Objek | 85 | 78 | 90 |
| Basis Data | 70 | 65 | 72 |
| Matematika Diskrit | 60 | 55 | 48 |

**Contoh output yang diharapkan:**

```text
=== KARTU HASIL STUDI (SEDERHANA) ===
Pemrograman Berorientasi Objek: 84 (A) - lulus
Basis Data: 69 (C) - lulus
Matematika Diskrit: 53 (D) - belum lulus
```

<details>
<summary>💡 Petunjuk</summary>

- Agar tetap bilangan bulat: `(30 * tugas + 30 * uts + 40 * uas) // 100` di Python, atau `/ 100` di Java (pembagian dua `int` membuang desimal).
- Di dalam `huruf()`, panggil `self.nilai_akhir()` (Python) atau `nilaiAkhir()` (Java).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_nilai_kuliah.py) · [☕ Java](java/solusi/Latihan04NilaiKuliah.java)

---

## Latihan 5 — Stok Menu KedaiKita (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita.

**Soal:** Salin kelas `Menu` dari studi kasus pertemuan ini, lalu:

1. Tambahkan atribut `stok` yang diisi lewat konstruktor.
2. Ubah `tampilkan_info()` agar ikut menampilkan stok.
3. Tambahkan method `jual(jumlah)`: jika stok cukup, kurangi stok, cetak pesan, dan **kembalikan** total harga. Jika stok tidak cukup, cetak pesan gagal dan kembalikan 0.

Uji dengan Kopi Susu Gula Aren (Rp18000, stok 20) dan Nasi Goreng Kampung (Rp25000, stok 2). Jual 2 kopi, 3 nasi goreng, lalu 2 nasi goreng, dan jumlahkan pendapatannya.

**Contoh output yang diharapkan:**

```text
=== STOK AWAL ===
Kopi Susu Gula Aren - Rp18000 (stok 20)
Nasi Goreng Kampung - Rp25000 (stok 2)

=== PENJUALAN ===
Terjual 2 Kopi Susu Gula Aren, total Rp36000
Gagal: stok Nasi Goreng Kampung tidak cukup (sisa 2)
Terjual 2 Nasi Goreng Kampung, total Rp50000
Pendapatan: Rp86000

=== STOK AKHIR ===
Kopi Susu Gula Aren - Rp18000 (stok 18)
Nasi Goreng Kampung - Rp25000 (stok 0)
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa kondisi gagal lebih dulu (`if jumlah > stok`), cetak pesan, lalu `return 0`.
- Pendapatan dihitung di program utama: `pendapatan = pendapatan + kopi.jual(2)`.
- Pengguna Java: jika membuka folder `java/` pertemuan ini di VS Code, beri nama kelasmu `MenuKedai` agar tidak bentrok dengan kelas `Menu` di folder studi kasus.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_stok_menu.py) · [☕ Java](java/solusi/Latihan05StokMenu.java)

---

## Latihan 6 — Robot Penjelajah (⭐⭐⭐ Tantangan)

**Tujuan:** mengelola beberapa atribut yang saling terkait dan memecah tugas menjadi beberapa method.

**Soal:** Sebuah robot berada di koordinat (0, 0) dan menghadap **Utara**. Buat kelas `Robot` dengan atribut `nama`, `x`, `y`, dan arah hadap. Tambahkan method:

- `belok_kanan()` dan `belok_kiri()`: urutan arah searah jarum jam adalah Utara → Timur → Selatan → Barat → Utara,
- `maju()`: maju satu langkah sesuai arah (Utara: y+1, Timur: x+1, Selatan: y−1, Barat: x−1),
- `posisi()`: mengembalikan teks seperti `(2, 2) menghadap Timur`,
- `jalankan(perintah)`: membaca teks perintah huruf demi huruf. `M` = maju, `R` = belok kanan, `L` = belok kiri. Huruf lain dilewati dengan pesan peringatan.

Jalankan perintah `MMRMM`, lalu `LLMX`.

**Contoh output yang diharapkan:**

```text
Posisi awal: (0, 0) menghadap Utara
Robi menjalankan perintah 'MMRMM'
  Posisi sekarang: (2, 2) menghadap Timur
Robi menjalankan perintah 'LLMX'
  Perintah 'X' tidak dikenal, dilewati
  Posisi sekarang: (1, 2) menghadap Barat
```

<details>
<summary>💡 Petunjuk</summary>

- Simpan arah sebagai **indeks** (0 sampai 3) ke daftar `["Utara", "Timur", "Selatan", "Barat"]`.
- Belok kanan: `indeks = (indeks + 1) % 4`. Belok kiri: `indeks = (indeks + 3) % 4`.
- Di dalam `jalankan()`, panggil method lain milik objek yang sama: `self.maju()` (Python) atau `maju()` (Java).
- Perulangan huruf: `for huruf in perintah:` (Python) atau `for (char huruf : perintah.toCharArray())` (Java).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_robot.py) · [☕ Java](java/solusi/Latihan06Robot.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Sistem Parkir Kampus

Parkiran kampus ingin mencatat kendaraan dan menghitung biaya parkir.

**Kebutuhan:**

1. Buat kelas `Kendaraan` dengan atribut: nomor plat, jenis (`"motor"` atau `"mobil"`), dan jam masuk (bilangan bulat 0–23).
2. Tambahkan method `lama_parkir(jam_keluar)` / `lamaParkir(jamKeluar)` yang mengembalikan lama parkir dalam jam. Anggap kendaraan keluar di hari yang sama, dan minimal dihitung 1 jam.
3. Tambahkan method `hitung_biaya(jam_keluar)` / `hitungBiaya(jamKeluar)`: motor Rp2.000 per jam, mobil Rp5.000 per jam.
4. Tambahkan method `cetak_karcis(jam_keluar)` / `cetakKarcis(jamKeluar)` yang mencetak plat, jenis, lama parkir, dan biaya.
5. Di program utama, buat minimal **empat** objek kendaraan (campuran motor dan mobil), simpan dalam list/array, cetak karcis semuanya, lalu tampilkan **total pendapatan** parkir.

**Ketentuan pengumpulan:** satu file program (Python atau Java) beserta tangkapan layar output-nya.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kelas dan konstruktor benar (atribut lengkap) | 25% |
| Method `lama_parkir` dan `hitung_biaya` benar, termasuk aturan minimal 1 jam | 30% |
| Program utama memakai list/array objek dan menghitung total pendapatan | 25% |
| Kerapian kode: nama variabel jelas, komentar secukupnya, output rapi | 20% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
