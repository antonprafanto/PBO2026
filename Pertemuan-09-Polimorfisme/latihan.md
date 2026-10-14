# Latihan — Pertemuan 09: Polimorfisme

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.
5. Uji kecil untuk setiap solusimu: apakah program utama memanggil method yang **sama** pada objek berbeda jenis, tanpa deretan `if` berdasarkan jenis? Jika ya, kamu sudah memakai polimorfisme.

---

## Latihan 1 — Notifikasi Kampus (⭐ Dasar)

**Tujuan:** meng-*override* method dan memproses objek berbeda jenis dalam satu list.

**Soal:** Buat kelas induk `Notifikasi` dengan atribut `tujuan`, method `kirim(pesan)` yang **mengembalikan** teks `[UMUM] Kepada <tujuan>: <pesan>`, dan method `biaya()` yang mengembalikan 0. Lalu buat tiga kelas anak:

| Kelas | `kirim(pesan)` mengembalikan | `biaya()` |
|---|---|---|
| `NotifEmail` | `[EMAIL] Kepada <tujuan>: <pesan>` | warisan induk (0) |
| `NotifSMS` | `[SMS] Kepada <tujuan>: <pesan>`. Pesan lebih dari 20 karakter dipotong menjadi 20 karakter pertama + `...` | 150 |
| `NotifWhatsApp` | `[WA] Kepada <tujuan>: *PENGUMUMAN* <pesan>` | warisan induk (0) |

Simpan tiga notifikasi dalam satu list: email `ayu@kampus.ac.id`, SMS `081234567890`, dan WA `082198765432`. Kirim dua pesan, `Kuliah PBO pindah ke Ruang D-201` dan `Kuis besok jam 8`, lalu tampilkan total biaya. Program utama **tidak boleh** memeriksa jenis notifikasi.

**Contoh output yang diharapkan:**

```text
=== KIRIM: Kuliah PBO pindah ke Ruang D-201 ===
[EMAIL] Kepada ayu@kampus.ac.id: Kuliah PBO pindah ke Ruang D-201
[SMS] Kepada 081234567890: Kuliah PBO pindah ke...
[WA] Kepada 082198765432: *PENGUMUMAN* Kuliah PBO pindah ke Ruang D-201

=== KIRIM: Kuis besok jam 8 ===
[EMAIL] Kepada ayu@kampus.ac.id: Kuis besok jam 8
[SMS] Kepada 081234567890: Kuis besok jam 8
[WA] Kepada 082198765432: *PENGUMUMAN* Kuis besok jam 8

Total biaya pengiriman: Rp300
```

<details>
<summary>💡 Petunjuk</summary>

- Pakai dua perulangan bertingkat: luar untuk pesan, dalam untuk notifikasi. Memotong teks: `pesan[:20]` (Python) atau `pesan.substring(0, 20)` (Java).
- Di dalam perulangan, cukup `total_biaya += notif.biaya()`. Biarkan polimorfisme memilih versinya.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan01_notifikasi.py) · [☕ Java](java/solusi/Latihan01Notifikasi.java)

---

## Latihan 2 — Rumah Pintar: Mode Tidur (⭐ Dasar)

**Tujuan:** memeriksa jenis objek sebelum memanggil method khusus (`isinstance`, atau `instanceof` + *downcasting*).

**Soal:** Buat kelas induk `Perangkat(nama)`. Setiap perangkat awalnya menyala. Method `matikan()` mencetak `<nama> dimatikan`, dan `status()` mengembalikan `<nama>: menyala` atau `<nama>: mati`. Kelas anaknya:

- `Lampu(nama, kecerahan)` dengan kecerahan bawaan 100. Method khusus `redupkan(persen)` mencetak `<nama> diredupkan ke <persen>%`. Saat menyala, `status()` mengembalikan `<nama>: menyala <kecerahan>%`.
- `AC(nama, suhu)`. Method khusus `atur_suhu(derajat)` / `aturSuhu(derajat)` mencetak `<nama> diatur ke <derajat> derajat`. Saat menyala, `status()` mengembalikan `<nama>: menyala <suhu> derajat`.
- `Televisi(nama)` tanpa tambahan apa pun.

Buat fungsi `mode_tidur(daftar)` / `modeTidur(daftar)`: lampu diredupkan ke 10%, AC diatur ke 26 derajat, dan perangkat lain dimatikan. Uji dengan Lampu Kamar, AC Kamar (20 derajat), Televisi, dan Lampu Teras.

**Contoh output yang diharapkan** (sebelumnya, bagian `=== SEBELUM MODE TIDUR ===` menampilkan status awal: kedua lampu `menyala 100%`, AC `menyala 20 derajat`, dan televisi `menyala`):

```text
=== MODE TIDUR DIAKTIFKAN ===
Lampu Kamar diredupkan ke 10%
AC Kamar diatur ke 26 derajat
Televisi dimatikan
Lampu Teras diredupkan ke 10%

=== SESUDAH MODE TIDUR ===
Lampu Kamar: menyala 10%
AC Kamar: menyala 26 derajat
Televisi: mati
Lampu Teras: menyala 10%
```

<details>
<summary>💡 Petunjuk</summary>

- Menampilkan status cukup dengan `print(perangkat.status())` untuk semua perangkat, **tanpa** cek jenis. Di `mode_tidur`, urutan pemeriksaannya: `Lampu`, lalu `AC`, lalu sisanya `matikan()`.
- Java: setelah `instanceof Lampu`, lakukan *cast* `(Lampu) perangkat`, atau pakai `instanceof Lampu lampu`. Karena Java tidak punya nilai bawaan, buat dua konstruktor `Lampu`.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_rumah_pintar.py) · [☕ Java](java/solusi/Latihan02RumahPintar.java)

---

## Latihan 3 — Tarif Ojek Online (⭐⭐ Menengah)

**Tujuan:** menyediakan banyak cara memanggil satu kemampuan: *overloading* (Java) atau nilai bawaan dan argumen kata kunci (Python).

**Soal:** Buat kelas `Ojek` dengan `nama_driver` dan `tarif_per_km` (bawaan Rp2.500). Method `info()` mengembalikan `Pak Darto (Rp2500/km)`. Method `hitung_tarif` / `hitungTarif` harus bisa dipanggil dengan tiga cara: (jarak), (jarak, jam sibuk), dan (jarak, jam sibuk, kode promo). Aturannya, berurutan:

1. Tarif = jarak (km) × tarif per km, **minimal** Rp10.000.
2. Jika jam sibuk, tarif naik 20%.
3. Jika kode promo `HEMAT10`, tarif dipotong 10%. Kode lain diabaikan.

Gunakan bilangan bulat (`nilai * persen // 100` atau `/ 100`). Di Java, buat dua konstruktor dan tiga versi `hitungTarif`. Di Python, cukup satu konstruktor dan satu method dengan nilai bawaan.

**Contoh output yang diharapkan:**

```text
=== DRIVER ===
Pak Darto (Rp2500/km)
Mbak Yuni (Rp3000/km)

=== HITUNG TARIF ===
Pak Darto, 3 km                     : Rp10000
Pak Darto, 8 km                     : Rp20000
Pak Darto, 8 km, jam sibuk          : Rp24000
Pak Darto, 8 km, jam sibuk, HEMAT10 : Rp21600
Mbak Yuni, 5 km, HEMAT10            : Rp13500
Mbak Yuni, 5 km, kode SALAH         : Rp15000
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `def hitung_tarif(self, jarak_km, jam_sibuk=False, kode_promo="")`, lalu panggil `yuni.hitung_tarif(5, kode_promo="HEMAT10")`.
- Java: dua versi yang pendek cukup memanggil versi terlengkap, misalnya `return hitungTarif(jarakKm, false, "");`. Dengan begitu, rumusnya hanya ditulis sekali.
- Java: bandingkan teks dengan `kodePromo.equals("HEMAT10")`, bukan `==`. Python: ingat, tiga `def hitung_tarif` hanya menyisakan yang terakhir.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_tarif_ojek.py) · [☕ Java](java/solusi/Latihan03TarifOjek.java)

---

## Latihan 4 — Resi Ekspedisi (⭐⭐ Menengah)

**Tujuan:** polimorfisme dari dalam kelas dan menambah jenis baru tanpa mengubah kode lama.

**Soal:** Buat kelas induk `Pengiriman(kode, kota_tujuan, berat_kg)` dengan tiga method kecil: `nama_layanan()`, `tarif_per_kg()`, dan `berat_ditagih()` (bawaannya berat asli). Dua method berikut ditulis **hanya di induk**:

- `ongkir()` = `berat_ditagih()` × `tarif_per_kg()`.
- `cetak_resi()` mencetak satu baris: kode dalam kurung siku, nama layanan rata kiri 8 karakter, kota rata kiri 11 karakter, berat rata kanan 3 karakter, lalu ongkir.

Kelas anak: `Reguler` (Rp9.000/kg), `Kilat` (Rp15.000/kg), dan `Kargo` (Rp6.000/kg, berat yang ditagih **minimal 10 kg**). Fungsi `cetak_manifest(daftar)` mencetak semua resi dan total ongkir.

**Bagian 2:** tambahkan layanan `SameDay` (Rp20.000/kg ditambah biaya kurir Rp10.000 per kiriman) **tanpa mengubah** kelas `Pengiriman` maupun `cetak_manifest`.

Manifest pagi: KK001 Reguler Balikpapan 2 kg, KK002 Kilat Bontang 3 kg, KK003 Kargo Tenggarong 4 kg, KK004 Kargo Sangatta 25 kg. Manifest sore: KK005 SameDay Samarinda 1 kg, KK006 Reguler Balikpapan 5 kg, KK007 SameDay Samarinda 3 kg.

**Contoh output yang diharapkan:**

```text
=== MANIFEST PAGI ===
[KK001] Reguler  Balikpapan   2 kg  Rp18000
[KK002] Kilat    Bontang      3 kg  Rp45000
[KK003] Kargo    Tenggarong   4 kg  Rp60000
[KK004] Kargo    Sangatta    25 kg  Rp150000
Total ongkir: Rp273000

=== MANIFEST SORE (ADA LAYANAN BARU) ===
[KK005] SameDay  Samarinda    1 kg  Rp30000
[KK006] Reguler  Balikpapan   5 kg  Rp45000
[KK007] SameDay  Samarinda    3 kg  Rp70000
Total ongkir: Rp145000
```

<details>
<summary>💡 Petunjuk</summary>

- Format satu baris resi: `f"[{kode}] {layanan:<8} {kota:<11}{berat:>3} kg  Rp{ongkir}"` (Python) atau `String.format("[%s] %-8s %-11s%3d kg  Rp%d", ...)` (Java).
- `Kargo` cukup meng-*override* `berat_ditagih()` dengan `max(berat, 10)` / `Math.max(berat, 10)`. `SameDay` meng-*override* `ongkir()` dengan gaya "memperluas": versi induk lewat `super` ditambah 10000.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_resi_ekspedisi.py) · [☕ Java](java/solusi/Latihan04ResiEkspedisi.java)

---

## Latihan 5 — KedaiKita: Bayar dengan Voucher (⭐⭐ Menengah)

**Tujuan:** mengembangkan studi kasus KedaiKita dengan jenis pembayaran baru **tanpa mengubah** `Pesanan.bayar()`.

**Soal:** Tambahkan kelas `PembayaranVoucher(kode, nilai)` sebagai anak `Pembayaran`:

- `nama_metode()` mengembalikan `Voucher <kode>`. Voucher tidak dikenai biaya layanan.
- `proses(total)`: jika voucher **sudah pernah dipakai**, cetak `  Voucher <kode> sudah pernah dipakai` lalu gagal. Jika nilainya kurang dari total, cetak `  Nilai voucher <nilai> tidak cukup` lalu gagal. Selain itu, tandai voucher sudah terpakai, cetak `  Voucher <kode> dipakai, sisa <sisa> hangus`, lalu berhasil.

Skenario dengan **satu** voucher `KEDAI50` senilai Rp50.000: pesanan P001 Budi (Rp61.000) gagal dibayar voucher lalu dibayar tunai Rp100.000, pesanan P002 Siti (Rp31.000) dibayar voucher, dan pesanan P003 Budi (Rp15.000) mencoba voucher yang sama.

**Contoh output yang diharapkan** (potongan awal):

```text
=== VOUCHER TIDAK CUKUP, GANTI TUNAI ===
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Voucher KEDAI50
  Total bayar  : Rp61.000
  Nilai voucher Rp50.000 tidak cukup
  Status       : GAGAL, silakan pilih metode lain
Pembayaran pesanan P001 (Budi Santoso)
  Metode       : Tunai
  Total bayar  : Rp61.000
  Uang diterima Rp100.000, kembalian Rp39.000
  Status       : LUNAS (+6 poin)
```

Pada akhirnya, P001 dan P002 berstatus `LUNAS`, P003 tetap `BARU`, poin Budi 6, dan poin Siti 3.

<details>
<summary>💡 Petunjuk</summary>

- Simpan status pemakaian di atribut, misalnya `_terpakai = False`. Periksa "sudah dipakai" **sebelum** memeriksa nilai.
- `hitung_biaya_layanan` tidak perlu ditulis. Versi induk (0) sudah tepat. Solusi dibuat satu file agar bisa langsung dijalankan, sehingga berisi salinan ringkas `Pembayaran`, `PembayaranTunai`, dan `Pesanan` (total pesanan langsung diisi). Logika `bayar()` di dalamnya sama persis dengan studi kasus. Di proyekmu, cukup tambahkan kelas baru ke `pembayaran.py` / `PembayaranVoucher.java`.
- Pengguna Java: salinan ringkas di solusi diberi nama `PembayaranKedai`, `PesananKedai`, dan seterusnya, agar tidak bentrok dengan kelas studi kasus di folder `java/` yang sama.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_pembayaran_voucher.py) · [☕ Java](java/solusi/Latihan05PembayaranVoucher.java)

---

## Latihan 6 — Turnamen Mini RPG (⭐⭐⭐ Tantangan)

**Tujuan:** merancang method induk yang berisi **dua** panggilan polimorfik sekaligus.

**Soal:** Buat kelas induk `Karakter(nama, hp, kekuatan)` dengan method:

- `hitung_serangan()` mengembalikan `kekuatan`.
- `terima_serangan(damage)` mengurangi HP (tidak kurang dari 0) dan mengembalikan damage yang benar-benar diterima.
- `serang(lawan)` memanggil `hitung_serangan()` milik dirinya dan `terima_serangan()` milik lawan, lalu mencetak `  <nama> menyerang <lawan>: <diterima> damage, HP <lawan> tinggal <hp>`.

Kelas anak: `Prajurit` (punya `perisai`; damage yang diterima dikurangi perisai, minimal 1), `Penyihir` (setiap serangan ke-3, ke-6, dan seterusnya bernilai 3 kali kekuatan), dan `Pemanah` (setiap serangan ke-2, ke-4, dan seterusnya yang mengarah kepadanya berhasil dihindari, damage 0).

Fungsi `duel(a, b)` berjalan paling banyak 10 ronde. Setiap ronde, `a` menyerang `b`, lalu `b` menyerang `a` jika masih hidup. Duel berhenti saat HP salah satu habis. Duel 1: Prajurit Bima (HP 60, kekuatan 10, perisai 4) melawan Penyihir Sari (HP 45, kekuatan 9). Duel 2: Penyihir Sari yang baru (HP 45, kekuatan 9) melawan Pemanah Raka (HP 50, kekuatan 8).

**Contoh output yang diharapkan:**

```text
=== DUEL: Bima (Prajurit) vs Sari (Penyihir) ===
Ronde 1
  Bima menyerang Sari: 10 damage, HP Sari tinggal 35
  Sari menyerang Bima: 5 damage, HP Bima tinggal 55
Ronde 2
  Bima menyerang Sari: 10 damage, HP Sari tinggal 25
  Sari menyerang Bima: 5 damage, HP Bima tinggal 50
Ronde 3
  Bima menyerang Sari: 10 damage, HP Sari tinggal 15
  Sari menyerang Bima: 23 damage, HP Bima tinggal 27
Ronde 4
  Bima menyerang Sari: 10 damage, HP Sari tinggal 5
  Sari menyerang Bima: 5 damage, HP Bima tinggal 22
Ronde 5
  Bima menyerang Sari: 10 damage, HP Sari tinggal 0
Pemenang: Bima
```

Duel kedua dimenangkan Raka di ronde 6. Di ronde 2, 4, dan 6, serangan Sari tercetak `0 damage` karena Raka menghindar. Di ronde 3, bola api Sari memberi `27 damage`.

<details>
<summary>💡 Petunjuk</summary>

- Simpan penghitung di atribut objek: jumlah serangan untuk `Penyihir`, jumlah kali diserang untuk `Pemanah`. Pakai `% 3 == 0` dan `% 2 == 0`.
- `Prajurit` dan `Pemanah` sebaiknya tetap memakai versi induk lewat `super` untuk benar-benar mengurangi HP. Nama kelas di judul duel: `type(a).__name__` (Python) atau `a.getClass().getSimpleName()` (Java).

</details>

**Solusi:** [🐍 Python](python/solusi/latihan06_turnamen_rpg.py) · [☕ Java](java/solusi/Latihan06TurnamenRpg.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Loket Tiket Taman Rekreasi

Sebuah taman rekreasi di Samarinda ingin aplikasi loket tiket sederhana dengan kebutuhan berikut:

1. Kelas induk `Tiket` dengan nama pengunjung, method `harga()`, dan method `keterangan()`.
2. Minimal **tiga** kelas anak yang meng-*override* `harga()` dan `keterangan()`, misalnya `TiketDewasa`, `TiketAnak`, dan `TiketPelajar` (wajib menyimpan nomor kartu pelajar). Tentukan sendiri harganya (bilangan bulat).
3. Kelas `Loket` dengan kemampuan menjual tiket **dengan atau tanpa** jumlah: Java memakai *overloading* (`jual(Tiket)` dan `jual(Tiket, int)`), Python memakai nilai bawaan.
4. Method `rekap()` mencetak semua penjualan dan total pendapatan, **tanpa** memeriksa jenis tiket.
5. Laporan khusus jumlah tiket pelajar, satu-satunya tempat yang boleh memakai `isinstance`/`instanceof`.
6. Setelah semuanya berjalan, tambahkan satu jenis tiket baru (misalnya `TiketRombongan`), lalu tunjukkan bahwa `rekap()` tidak perlu diubah.

**Ketentuan pengumpulan:** program Python atau Java (boleh beberapa file) beserta tangkapan layar output-nya. Output harus selalu sama setiap kali dijalankan.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Hierarki `Tiket` dan *override* `harga()`/`keterangan()` benar | 25% |
| `rekap()` polimorfik, tanpa percabangan berdasarkan jenis | 25% |
| Penjualan dengan/tanpa jumlah (*overloading* atau nilai bawaan) | 20% |
| Pemeriksaan jenis hanya untuk laporan khusus, dan jenis tiket baru tanpa mengubah `rekap()` | 20% |
| Kerapian kode: nama jelas, komentar secukupnya, output rapi | 10% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
