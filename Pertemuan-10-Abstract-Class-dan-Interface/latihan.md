# Latihan — Pertemuan 10: Abstract Class dan Interface

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

> [!TIP]
> Sebelum menulis kode, tanyakan dulu: "Kelas-kelas ini **bersaudara** (pakai kelas abstrak) atau hanya **sama-sama bisa** sesuatu (pakai interface)?" Jawaban pertanyaan itu menentukan desainmu.

---

## Latihan 1 — Kelas Abstrak Perangkat (⭐ Dasar)

**Tujuan:** membuat kelas abstrak dengan konstruktor, method abstrak, dan method konkret.

**Soal:** Buat kelas abstrak `Perangkat` yang menyimpan `merek` dan `daya_watt` lewat konstruktor. Isinya:

- method abstrak `jenis()` dan `fungsi_utama()` / `fungsiUtama()`,
- method konkret `info()` yang mengembalikan teks `Jenis Merek (daya watt): fungsi utama`.

Buat tiga kelas anak: `Laptop` (Lenovo, 65 watt), `Ponsel` (Samsung, 18 watt), dan `Printer` (Epson, 30 watt). Tambahkan fungsi `total_daya(daftar)` / method `totalDaya(daftar)` yang menjumlahkan daya semua perangkat. Terakhir, coba buat objek `Perangkat` secara langsung, lalu catat pesan error-nya (baris ini hapus lagi setelah dicoba).

**Contoh output yang diharapkan:**

```text
=== DAFTAR PERANGKAT ===
Laptop Lenovo (65 watt): mengetik laporan dan menulis kode
Ponsel Samsung (18 watt): menelepon dan mengirim pesan
Printer Epson (30 watt): mencetak tugas kuliah
Total daya jika menyala bersamaan: 113 watt
```

<details>
<summary>💡 Petunjuk</summary>

- `info()` cukup ditulis sekali di `Perangkat`, lalu memanggil `self.jenis()` dan `self.fungsi_utama()` (Python) atau `jenis()` dan `fungsiUtama()` (Java).
- Di Java, setiap kelas anak tetap perlu konstruktor yang memanggil `super(merek, dayaWatt)`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_perangkat.py) · [☕ Java](java/solusi/Latihan01Perangkat.java)

---

## Latihan 2 — Interface BisaDiisiUlang (⭐ Dasar)

**Tujuan:** membuat interface dan memakainya untuk kelas-kelas yang tidak bersaudara.

**Soal:** Buat interface `BisaDiisiUlang` dengan tiga method: `nama_alat()`, `persen_baterai()`, dan `isi_daya(menit)` (Java: `namaAlat()`, `persenBaterai()`, `isiDaya(menit)`). Buat tiga kelas yang memenuhinya, masing-masing dengan kecepatan isi daya berbeda. Baterai tidak boleh melebihi 100%.

| Kelas | Baterai awal | Kecepatan isi daya |
|---|---|---|
| `SepedaListrik` | 20% | 1% per menit |
| `Powerbank` | 50% | 2% per menit |
| `SikatGigiElektrik` | 90% | 5% per menit |

Buat fungsi `tampilkan_status(daftar)` dan `isi_semua(daftar, menit)` yang hanya mengenal interface-nya. Isi semua alat selama 30 menit, lalu hitung berapa yang sudah penuh.

**Contoh output yang diharapkan:**

```text
=== SEBELUM DIISI ===
Sepeda listrik: 20%
Powerbank: 50%
Sikat gigi elektrik: 90%

=== SETELAH DIISI 30 MENIT ===
Sepeda listrik: 50%
Powerbank: 100%
Sikat gigi elektrik: 100%
Sudah penuh: 2 dari 3 alat
```

<details>
<summary>💡 Petunjuk</summary>

- Pembatas 100%: `min(100, baterai + menit * kecepatan)` di Python, `Math.min(...)` di Java.
- Python: interface ditulis sebagai `class BisaDiisiUlang(ABC):` dengan tiga `@abstractmethod`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_bisa_diisi_ulang.py) · [☕ Java](java/solusi/Latihan02BisaDiisiUlang.java)

---

## Latihan 3 — Ongkos Kirim dengan Template Method (⭐⭐ Menengah)

**Tujuan:** menerapkan template method dan *hook*.

**Soal:** Buat kelas abstrak `Pengiriman` dengan method abstrak `nama_layanan()` dan `tarif_per_kg()`, *hook* `biaya_tambahan(berat_kg)` yang bawaannya 0, dan template method `hitung_ongkir(berat)` = `berat x tarif_per_kg() + biaya_tambahan(berat)`.

| Layanan | Tarif per kg | Aturan tambahan |
|---|---|---|
| `KirimReguler` | Rp8.000 | tidak ada |
| `KirimKilat` | Rp15.000 | biaya prioritas tetap Rp5.000 |
| `KirimKargo` | Rp5.000 | berat dihitung minimal 10 kg: kekurangannya ditagih sebagai biaya tambahan |

Tambahkan method `rincian(berat)` dan fungsi `termurah(daftar, berat)`. Bandingkan ketiga layanan untuk paket 3 kg dan 12 kg.

**Contoh output yang diharapkan:**

```text
=== ONGKOS KIRIM PAKET 3 KG ===
Reguler : 3 kg x Rp8.000 + tambahan Rp0 = Rp24.000
Kilat   : 3 kg x Rp15.000 + tambahan Rp5.000 = Rp50.000
Kargo   : 3 kg x Rp5.000 + tambahan Rp35.000 = Rp50.000
Termurah: Reguler (Rp24.000)

=== ONGKOS KIRIM PAKET 12 KG ===
Reguler : 12 kg x Rp8.000 + tambahan Rp0 = Rp96.000
Kilat   : 12 kg x Rp15.000 + tambahan Rp5.000 = Rp185.000
Kargo   : 12 kg x Rp5.000 + tambahan Rp0 = Rp60.000
Termurah: Kargo (Rp60.000)
```

<details>
<summary>💡 Petunjuk</summary>

- `KirimReguler` hanya mengisi dua method abstrak. `KirimKilat` dan `KirimKargo` juga meng-*override* `biaya_tambahan()`.
- Biaya tambahan kargo untuk 3 kg: `(10 - 3) x 5000 = 35000`.
- Format nama layanan selebar 8 karakter: `f"{nama:<8}"` (Python) atau `String.format(Locale.US, "%-8s", nama)` (Java).
- Pengguna Java: kelas `Rupiah` sudah ada di folder studi kasus, jadi tulis method `formatRupiah()` sendiri di kelas utama.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_ongkos_kirim.py) · [☕ Java](java/solusi/Latihan03OngkosKirim.java)

---

## Latihan 4 — Armada Ojek Online (⭐⭐ Menengah)

**Tujuan:** menggabungkan kelas abstrak dengan beberapa interface sekaligus.

**Soal:** Sebuah aplikasi ojek daring di Samarinda punya tiga jenis armada. Buat:

- kelas abstrak `Armada` yang menyimpan nama pengemudi, punya method abstrak `jenis()`, dan method `__str__`/`toString()` yang menghasilkan `jenis + nama pengemudi`,
- interface `BisaAntarPenumpang` (`antar_penumpang(tujuan)`) dan `BisaAntarMakanan` (`antar_makanan(warung)`),
- `OjekMotor` (bisa keduanya), `TaksiMobil` (hanya penumpang), dan `KurirSepeda` (hanya makanan).

Simpan ketiga armada dalam satu daftar bertipe `Armada`. Tampilkan kemampuan masing-masing, lalu kirim pesanan makanan dan penumpang hanya ke armada yang mampu.

**Contoh output yang diharapkan:**

```text
=== KEMAMPUAN ARMADA ===
Ojek motor Pak Rudi: penumpang ya, makanan ya
Taksi mobil Pak Joko: penumpang ya, makanan tidak
Kurir sepeda Mas Dimas: penumpang tidak, makanan ya

=== PESANAN MAKANAN DARI WARUNG SOTO BANJAR ===
Ojek motor Pak Rudi mengambil pesanan di Warung Soto Banjar
Kurir sepeda Mas Dimas mengayuh sepeda ke Warung Soto Banjar

=== PENUMPANG KE KAMPUS UNMUL ===
Ojek motor Pak Rudi membonceng penumpang ke Kampus Unmul
Taksi mobil Pak Joko mengantar penumpang ke Kampus Unmul
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa kemampuan dengan `isinstance(kendaraan, BisaAntarMakanan)` atau `kendaraan instanceof BisaAntarMakanan`.
- Di Java, setelah `instanceof` bernilai benar, ubah tipenya dengan *cast* `(BisaAntarMakanan) kendaraan` agar `antarMakanan()` bisa dipanggil (ingat *downcasting* di Pertemuan 09).
- Jangan memeriksa nama kelas (`if jenis == "Ojek motor"`). Periksa **kemampuannya**.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_ojek_online.py) · [☕ Java](java/solusi/Latihan04OjekOnline.java)

---

## Latihan 5 — KedaiKita: Menu Abstrak (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan kelas abstrak dan template method.

**Soal:** Di KedaiKita tidak ada "menu umum": setiap menu pasti makanan atau minuman. Buat versi ringkas kelas `Menu` (cukup `kode`, `nama`, `harga`) sebagai kelas abstrak:

1. Tambahkan method abstrak `kategori()` (mengembalikan `"Makanan"` atau `"Minuman"`) dan `keterangan()`.
2. Tulis `__str__`/`toString()` **sekali saja** di kelas abstrak, dengan format seperti di studi kasus: `[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | dingin`.
3. Buat kelas anak `Makanan` (keterangan `pedas level N`) dan `Minuman` (keterangan `dingin` atau `panas`), **tanpa** meng-*override* `__str__`/`toString()`.
4. Tampilkan menu M01 sampai M05 ditambah M06 Teh Tarik Hangat (Rp12.000, panas), lalu hitung jumlah menu per kategori.

**Contoh output yang diharapkan:**

```text
=== MENU KEDAIKITA (Menu kini abstrak) ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | pedas level 0
[M06] Teh Tarik Hangat (Minuman) - Rp12.000 | panas

=== JUMLAH PER KATEGORI ===
Makanan: 3
Minuman: 3
```

<details>
<summary>💡 Petunjuk</summary>

- Kategori kini "dijawab" kelas anak lewat `kategori()`, jadi tidak perlu dikirim lewat konstruktor lagi.
- Pengguna Java: jika membuka folder `java/` pertemuan ini di VS Code, beri nama kelasmu `MenuAbstrak`, `MenuMakanan`, dan `MenuMinuman` agar tidak bentrok dengan kelas `Menu`, `Makanan`, dan `Minuman` di folder studi kasus.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_menu_abstrak.py) · [☕ Java](java/solusi/Latihan05MenuAbstrak.java)

---

## Latihan 6 — Arena Karakter (⭐⭐⭐ Tantangan)

**Tujuan:** merancang program yang memakai kelas abstrak, template method, dan interface sekaligus.

**Soal:** Buat permainan arena sederhana.

- Kelas abstrak `Karakter` menyimpan nama, HP maksimal, dan HP sekarang. Method abstraknya `peran()` dan `kekuatan_serangan()`. Method konkretnya: `terima_serangan(jumlah)` (HP tidak boleh di bawah 0), `pulihkan(jumlah)` (HP tidak boleh melewati maksimal, kembalikan HP yang benar-benar naik), `masih_hidup()`, dan `__str__`/`toString()` (tambahkan `(tumbang)` jika HP 0).
- Template method `serang(lawan)`: karakter yang sudah tumbang tidak bisa menyerang. Selain itu, HP lawan berkurang sebesar `kekuatan_serangan()`.
- Peran: `Ksatria` (HP 100, serangan 20), `Pemanah` (HP 60, serangan 15), `Penyihir` (HP 50, serangan 25).
- Interface `BisaMenyembuhkan` dengan method `sembuhkan(target)`. `Penyihir` memenuhinya (memulihkan 30 HP). `RamuanObat` juga memenuhinya walaupun **bukan** karakter: sekali pakai, memulihkan sejumlah HP.
- Fungsi `fase_penyembuhan(daftar, target)` menerima daftar apa saja yang `BisaMenyembuhkan`.

Jalankan skenario: ronde 1 (Arga menyerang Laras, Laras menyerang Arga, Mira menyerang Laras), ronde 2 (Arga menyerang Laras, Laras menyerang Arga, Mira menyerang Arga), fase penyembuhan untuk Arga dengan `[mira, RamuanObat(50)]`, lalu coba pakai ramuan yang sama sekali lagi untuk Mira.

**Contoh output yang diharapkan:**

```text
=== PARA KARAKTER ===
Ksatria Arga: HP 100/100
Pemanah Laras: HP 60/60
Penyihir Mira: HP 50/50

=== RONDE 1 ===
Arga menyerang Laras: -20 HP (sisa 40)
Laras menyerang Arga: -15 HP (sisa 85)
Mira menyerang Laras: -25 HP (sisa 15)

=== RONDE 2 ===
Arga menyerang Laras: -20 HP (sisa 0)
Laras sudah tumbang dan tidak bisa menyerang
Mira menyerang Arga: -25 HP (sisa 60)

=== FASE PENYEMBUHAN UNTUK ARGA ===
Penyihir Mira menyembuhkan Arga: +30 HP
Ramuan Obat menyembuhkan Arga: +10 HP
Ramuan Obat sudah habis

=== STATUS AKHIR ===
Ksatria Arga: HP 100/100
Pemanah Laras: HP 0/60 (tumbang)
Penyihir Mira: HP 50/50
```

<details>
<summary>💡 Petunjuk</summary>

- `Penyihir` mewarisi `Karakter` **dan** memenuhi `BisaMenyembuhkan`. `RamuanObat` hanya memenuhi `BisaMenyembuhkan`.
- Ramuan hanya menambah 10 HP karena HP Arga sudah 90 dari maksimal 100. Itulah gunanya nilai kembalian `pulihkan()`.
- Simpan status "sudah dipakai" sebagai atribut `bool`/`boolean` di `RamuanObat`. Di Java, `serang()` bisa diberi `final` agar aturan pertarungan tidak diubah kelas anak.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_arena_karakter.py) · [☕ Java](java/solusi/Latihan06ArenaKarakter.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Pengelola Tagihan Anak Kos

**Kebutuhan** (program untuk membantu anak kos di sekitar kampus mengelola tagihan bulanan):

1. Kelas abstrak `Tagihan` yang menyimpan nama tagihan dan bulan. Punya method abstrak `hitung_jumlah()` / `hitungJumlah()` dan template method `rincian()` yang mencetak nama, bulan, dan jumlah tagihan dalam format yang seragam.
2. Minimal tiga kelas anak dengan cara hitung berbeda, misalnya `TagihanListrik` (pemakaian kWh x tarif), `TagihanAir` (pemakaian m3 x tarif + biaya beban tetap), dan `TagihanInternet` (biaya bulanan tetap).
3. Interface `BisaDicicil` dengan method `cicilan_per_bulan(kali)` / `cicilanPerBulan(kali)`. Interface ini dipenuhi oleh **minimal satu** kelas tagihan **dan** oleh satu kelas yang bukan tagihan, misalnya `PembelianLaptop`.
4. Fungsi untuk menghitung total semua tagihan, dan fungsi yang mencetak rencana cicilan untuk daftar apa saja yang `BisaDicicil`.
5. Program utama yang membuat minimal empat objek dan menampilkan rincian, total, serta rencana cicilan.
6. Semua nilai uang memakai bilangan bulat (Rupiah).

**Ketentuan pengumpulan:** satu file program (Python atau Java), diagram kelas sederhana (boleh foto gambar tangan atau Mermaid) yang menunjukkan kelas abstrak, interface, dan relasi realisasinya, serta tangkapan layar output.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Kelas abstrak `Tagihan` benar: method abstrak, template method, dan tidak bisa dibuat objeknya | 25% |
| Minimal tiga kelas anak dengan perhitungan yang benar | 20% |
| Interface `BisaDicicil` dipenuhi oleh kelas tagihan dan kelas non-tagihan, dan dipakai secara polimorfik | 25% |
| Diagram kelas memakai notasi yang benar (abstrak, `<<interface>>`, realisasi) | 15% |
| Kerapian kode: nama jelas, komentar secukupnya, output rapi | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
