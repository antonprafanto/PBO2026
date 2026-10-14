# Latihan — Pertemuan 13: Prinsip SOLID

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)

**Cara mengerjakan:**

1. Kerjakan dengan bahasa pilihanmu (Python **atau** Java). Kalau sempat, coba juga di bahasa satunya.
2. Buat file baru untuk setiap latihan, lalu jalankan dan bandingkan output-mu dengan **contoh output** di soal.
3. Buka petunjuk hanya jika benar-benar buntu. Buka solusi **setelah** kamu mencoba sendiri.
4. Tingkat kesulitan: ⭐ Dasar · ⭐⭐ Menengah · ⭐⭐⭐ Tantangan.

---

## Latihan 1 — Detektif Desain (⭐ Dasar)

**Tujuan:** mengenali pelanggaran prinsip SOLID dari deskripsi sebuah rancangan.

**Soal:** Untuk setiap rancangan berikut, tentukan prinsip yang paling jelas dilanggar (SRP, OCP, LSP, ISP, atau DIP), lalu usulkan perbaikannya dalam satu atau dua kalimat. Hati-hati, ada satu rancangan yang sebenarnya tidak perlu diubah. Latihan ini tidak punya file solusi; jawabannya ada di bawah.

1. Kelas `AplikasiApotek` punya method `hitung_total()`, `cetak_nota()`, `kirim_email_promo()`, `simpan_ke_database()`, dan `buat_laporan_pajak()`.
2. Fungsi `hitung_gaji(jenis)` berisi `if jenis == "tetap" ... elif jenis == "kontrak" ... elif jenis == "magang"`. Bagian kepegawaian baru saja meminta jenis "paruh waktu".
3. Kelas `VoucherHemat` turunan `Diskon` mengembalikan potongan **-5000** untuk belanja di bawah Rp20.000, dengan alasan "biaya tambahan".
4. Kontrak `PerangkatKelas` mewajibkan `proyeksikan()`, `cetak()`, `pindai()`, dan `fotokopi()`. Kelas `Proyektor` mengisi tiga method terakhir dengan melempar *error*.
5. Konstruktor `LaporanHarian` berisi `self.db = DatabaseMySQL("localhost")` (Java: `this.db = new DatabaseMySQL("localhost");`). Akibatnya, laporan tidak bisa diuji tanpa server *database*.
6. Skrip 25 baris untuk sekali menghitung rata-rata nilai kuis satu kelas, ditulis sebagai satu fungsi tanpa kelas.

<details>
<summary>Lihat jawaban</summary>

| No | Prinsip | Alasan dan usulan perbaikan |
|---|---|---|
| 1 | SRP | Lima urusan dengan lima alasan berubah. Pecah menjadi kelas-kelas fokus, misalnya `PenghitungTotal`, `PencetakNota`, `PengirimPromo`, `PenyimpananTransaksi`, dan `LaporanPajak`. |
| 2 | OCP | Setiap jenis baru membongkar fungsi lama. Buat kontrak `Karyawan` dengan method `gaji()`, lalu satu kelas untuk setiap jenis; "paruh waktu" cukup menjadi kelas baru. |
| 3 | LSP | Janji `Diskon` adalah potongan tidak negatif. Potongan negatif membuat total naik secara mengejutkan. Biaya tambahan adalah konsep lain, jadi buat kelas tersendiri (misalnya `BiayaLayanan`). |
| 4 | ISP (dan LSP) | `Proyektor` dipaksa berjanji melebihi kemampuannya. Pecah menjadi kontrak kecil seperti `BisaMemproyeksikan`, `BisaMencetak`, dan `BisaMemindai`. |
| 5 | DIP | `LaporanHarian` menciptakan sendiri koneksi konkret. Terima abstraksi (misalnya `SumberData`) lewat konstruktor; saat diuji, suntikkan sumber data tiruan. |
| 6 | Tidak perlu diubah | Program kecil sekali pakai. Memecahnya menjadi banyak kelas justru melanggar KISS dan YAGNI. |

</details>

---

## Latihan 2 — Diskon Ulang Tahun (⭐ Dasar)

**Tujuan:** menerapkan OCP dan LSP pada studi kasus KedaiKita.

**Soal:** KedaiKita memberi hadiah kepada pelanggan yang berulang tahun (kasir memeriksa KTP-nya): **gratis 1 porsi menu termurah** di pesanannya. Tambahkan kelas `DiskonUlangTahun` turunan `Diskon` **tanpa mengubah** `Pesanan`, `StrukPesanan`, maupun kelas diskon lain.

- `keterangan()` mengembalikan `"Ulang Tahun"`.
- Potongannya adalah harga satu porsi menu termurah di pesanan.
- Pesanan kosong menghasilkan potongan 0, bukan *error* (janji LSP).

Uji dengan pesanan Siti (2 Es Teh Manis, 1 Pisang Goreng Keju), pesanan Budi (1 Nasi Goreng Kampung), dan pesanan kosong milik Andi Wijaya. Ketiganya sedang berulang tahun. Agar ringkas, cetak struk sederhana seperti contoh di bawah. Jika kamu mengerjakannya langsung di folder studi kasus dengan `StrukPesanan`, angka-angkanya harus sama.

**Contoh output yang diharapkan:**

```text
=== SITI BERULANG TAHUN ===
Pesanan Siti Aminah
2 x Es Teh Manis                Rp16.000
1 x Pisang Goreng Keju          Rp15.000
Subtotal                        Rp31.000
Diskon Ulang Tahun              -Rp8.000
TOTAL                           Rp23.000

=== BUDI BERULANG TAHUN, PESAN SATU MENU ===
Pesanan Budi Santoso
1 x Nasi Goreng Kampung         Rp25.000
Subtotal                        Rp25.000
Diskon Ulang Tahun             -Rp25.000
TOTAL                                Rp0

=== PESANAN KOSONG (UJI LSP) ===
Potongan: Rp0, total: Rp0
```

<details>
<summary>💡 Petunjuk</summary>

- Periksa pesanan kosong lebih dulu, lalu cari harga termurah dengan perulangan: mulai dari harga item pertama, ganti jika menemukan yang lebih murah (`item.menu.harga` / `item.getMenu().getHarga()`).
- Potongan sebesar harga menu termurah tidak mungkin negatif dan tidak mungkin melebihi subtotal.
- Pengguna Java: buat file baru `DiskonUlangTahun.java` berisi `implements Diskon`. File solusi memakai salinan ringkas kelas studi kasus dengan akhiran `Mini`, karena nama kelas di satu folder `java/` harus unik.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan02_diskon_ulang_tahun.py) · [☕ Java](java/solusi/Latihan02DiskonUlangTahun.java)

---

## Latihan 3 — Interface Ramping untuk Warga Kampus (⭐⭐ Menengah)

**Tujuan:** memecah kontrak gemuk menjadi kontrak-kontrak kecil (ISP).

**Soal:** Sistem akademik sebuah kampus punya kontrak gemuk `WargaKampus` berisi `ikut_kuliah(matkul)`, `bayar_ukt()`, `mengajar(matkul)`, dan `isi_nilai(nama_mahasiswa, nilai)` (Java: `ikutKuliah`, `bayarUkt`, `mengajar`, `isiNilai`). Akibatnya, kelas `Dosen` terpaksa menulis `bayar_ukt()` yang melempar *error*, dan `Mahasiswa` terpaksa menulis `mengajar()`. Pecah kontrak itu menjadi **`Pelajar`** (ikut kuliah, bayar UKT) dan **`Pengajar`** (mengajar, isi nilai). Lalu buat `Mahasiswa`, `Dosen`, dan `AsistenPraktikum`, yaitu mahasiswa yang juga membimbing praktikum. Di program utama, buat list pengajar (Dr. Hendra dan Rizky) dan list pelajar (Ayu dan Rizky).

**Contoh output yang diharapkan:**

```text
=== PARA PENGAJAR ===
Dr. Hendra mengajar PBO
Dr. Hendra mengisi nilai A untuk Ayu
Rizky membimbing praktikum PBO
Rizky mengisi nilai praktikum A untuk Ayu

=== PARA PELAJAR ===
Ayu mengikuti kuliah Basis Data
Ayu membayar UKT semester depan
Rizky mengikuti kuliah Basis Data
Rizky membayar UKT semester depan

Jumlah pengajar: 2, jumlah pelajar: 2
Rizky ada di kedua daftar karena ia mahasiswa sekaligus asisten.
```

<details>
<summary>💡 Petunjuk</summary>

- Python: `class AsistenPraktikum(Pelajar, Pengajar):`. Java: `class AsistenPraktikum implements Pelajar, Pengajar`.
- Beri tipe list sesuai kontraknya: `list[Pengajar]` / `List<Pengajar>`. Objek `rizky` yang sama boleh masuk ke kedua list.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan03_warga_kampus.py) · [☕ Java](java/solusi/Latihan03WargaKampus.java)

---

## Latihan 4 — Penyimpanan Terbatas untuk Kedai (⭐⭐ Menengah)

**Tujuan:** menambah wujud abstraksi baru dan menyuntikkannya tanpa mengubah `Kedai` (DIP).

**Soal:** Mesin kasir cabang KedaiKita memorinya kecil. Buat `PenyimpananTerbatas(maksimal)` turunan `PenyimpananPesanan` yang hanya menyimpan **N pesanan terakhir**; jika penuh, pesanan terlama dibuang. Maksimal di bawah 1 ditolak dengan `ValueError` / `IllegalArgumentException` berpesan `Maksimal pesanan harus minimal 1`. Kelas `Kedai` **tidak boleh diubah**. Uji dengan dua kedai, satu memakai `PenyimpananMemori` dan satu memakai `PenyimpananTerbatas(2)`. Setiap kedai melayani Budi Santoso, Siti Aminah, Rina Marlina, dan Andi Wijaya, lalu mencetak jumlah dan isi riwayatnya. Terakhir, coba buat `PenyimpananTerbatas(0)`.

**Contoh output yang diharapkan:**

```text
=== KEDAI DENGAN PENYIMPANAN MEMORI (TANPA BATAS) ===
Pesanan tersimpan: 4
  P001  Budi Santoso
  P002  Siti Aminah
  P003  Rina Marlina
  P004  Andi Wijaya

=== KEDAI DENGAN PENYIMPANAN TERBATAS (MAKSIMAL 2) ===
Pesanan tersimpan: 2
  P007  Rina Marlina
  P008  Andi Wijaya

=== MAKSIMAL YANG TIDAK MASUK AKAL ===
Ditolak: Maksimal pesanan harus minimal 1
```

<details>
<summary>💡 Petunjuk</summary>

- Nomor kedai kedua dimulai dari P005, karena penghitung nomor adalah milik kelas `Pesanan`, bukan milik kedai.
- Simpan pesanan di list. Setelah menambah, jika ukurannya melebihi maksimal, buang elemen pertama: `pop(0)` / `remove(0)`.
- Cukup tulis `simpan()` dan `semua()`. Method `jumlah()` sudah tersedia di kontraknya.
- Pengguna Java: file solusi memakai salinan ringkas kelas studi kasus dengan akhiran `Ringkas`, karena nama kelas di satu folder `java/` harus unik.

</details>

**Pertanyaan refleksi:** apakah `PenyimpananTerbatas` menepati janji kontrak "semua pesanan yang tersimpan, urut sesuai waktu disimpan"?

<details>
<summary>Lihat jawaban</summary>

Ya. Kontraknya menjanjikan pesanan yang **tersimpan**, dan urutannya tetap. Namun, pemanggil yang mengira riwayat selalu lengkap (misalnya untuk pendapatan harian) bisa terkejut, sehingga perilaku "membuang yang terlama" wajib ditulis jelas di dokumentasi kelas. LSP selalu bertanya: apa yang **diharapkan** pemanggil dari kontrak ini?

</details>

**Solusi:** [🐍 Python](python/solusi/latihan04_penyimpanan_terbatas.py) · [☕ Java](java/solusi/Latihan04PenyimpananTerbatas.java)

---

## Latihan 5 — Membongkar KosSerbaBisa (⭐⭐⭐ Tantangan)

**Tujuan:** melakukan *refactoring* kelas serba bisa (SRP, DIP) dan membuktikan perilakunya tidak berubah.

**Soal:** Kos Mawar di dekat kampus memakai kelas `KosSerbaBisa` di bawah ini. Kelas itu menyimpan data kamar, menghitung tagihan (denda Rp10.000 per hari terlambat, maksimal Rp100.000), mencetak kuitansi, **dan** mencatat kas. Lakukan *refactoring* dengan ketentuan:

1. Setiap tugas punya kelasnya sendiri (data kamar, aturan tagihan, format kuitansi, catatan kas), ditambah satu kelas koordinator.
2. Rekan kerja koordinator disuntikkan lewat konstruktor.
3. Tidak wajib membuat ABC/*interface*. Tulis alasanmu dalam komentar (ingat YAGNI).
4. Output harus **sama persis** dengan output program lama. Buktikan dengan `fc` atau `diff`.

<details>
<summary>Kode awal (Python)</summary>

```python
def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class KosSerbaBisa:
    """Menyimpan data kamar, menghitung tagihan, mencetak kuitansi, DAN mencatat kas."""

    def __init__(self):
        self.kamar = {"A1": ("Ayu", 750000), "A2": ("Bima", 750000),
                      "B1": ("Citra", 900000)}
        self.kas = []

    def bayar(self, nomor: str, hari_terlambat: int):
        penghuni, sewa = self.kamar[nomor]
        denda = 0
        if hari_terlambat > 0:
            denda = min(hari_terlambat * 10000, 100000)
        total = sewa + denda
        print(f"KUITANSI KOS MAWAR - KAMAR {nomor}")
        print(f"Penghuni : {penghuni}")
        print(f"Sewa     : {format_rupiah(sewa)}")
        if denda > 0:
            print(f"Denda    : {format_rupiah(denda)} ({hari_terlambat} hari)")
        print(f"Total    : {format_rupiah(total)}")
        print("-" * 30)
        self.kas.append(total)
```

</details>

<details>
<summary>Kode awal (Java)</summary>

```java
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;
import java.util.Map;

public class KosSerbaBisa {
    private Map<String, String> penghuni = Map.of("A1", "Ayu", "A2", "Bima", "B1", "Citra");
    private Map<String, Integer> sewa = Map.of("A1", 750000, "A2", 750000, "B1", 900000);
    private List<Integer> kas = new ArrayList<>();

    public void bayar(String nomor, int hariTerlambat) {
        int denda = 0;
        if (hariTerlambat > 0) {
            denda = Math.min(hariTerlambat * 10000, 100000);
        }
        int total = sewa.get(nomor) + denda;
        System.out.println("KUITANSI KOS MAWAR - KAMAR " + nomor);
        System.out.println("Penghuni : " + penghuni.get(nomor));
        System.out.println("Sewa     : " + rupiah(sewa.get(nomor)));
        if (denda > 0) {
            System.out.println("Denda    : " + rupiah(denda) + " (" + hariTerlambat + " hari)");
        }
        System.out.println("Total    : " + rupiah(total));
        System.out.println("-".repeat(30));
        kas.add(total);
    }

    static String rupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}
```

</details>

Lengkapi kode awal itu dengan program utama: buat objek `KosSerbaBisa`, panggil `bayar("A1", 0)`, `bayar("B1", 3)`, dan `bayar("A2", 14)`, lalu cetak baris `Kamar lunas: <banyak isi kas>, pemasukan: <jumlah isi kas>` seperti baris terakhir output di bawah. Jalankan, lalu simpan output-nya ke file sebelum mulai *refactoring*.

**Output program lama (harus tetap sama setelah refactoring):**

```text
KUITANSI KOS MAWAR - KAMAR A1
Penghuni : Ayu
Sewa     : Rp750.000
Total    : Rp750.000
------------------------------
KUITANSI KOS MAWAR - KAMAR B1
Penghuni : Citra
Sewa     : Rp900.000
Denda    : Rp30.000 (3 hari)
Total    : Rp930.000
------------------------------
KUITANSI KOS MAWAR - KAMAR A2
Penghuni : Bima
Sewa     : Rp750.000
Denda    : Rp100.000 (14 hari)
Total    : Rp850.000
------------------------------
Kamar lunas: 3, pemasukan: Rp2.530.000
```

<details>
<summary>💡 Petunjuk</summary>

- Calon kelas: `Kamar`, `PenghitungTagihan`, `PencetakKuitansi`, `BukuKas`, dan koordinator `PengelolaKos`.
- Koordinator hanya mengatur urutan: ambil kamar, minta denda dan total, minta kuitansi dicetak, catat ke buku kas.
- Kerjakan bertahap: pindahkan satu tugas, jalankan, bandingkan output, baru lanjut.

</details>

**Solusi:** [🐍 Python](python/solusi/latihan05_kos_rapi.py) · [☕ Java](java/solusi/Latihan05KosRapi.java)

---

## Tugas Mandiri (dikumpulkan, tanpa kunci jawaban)

### Sistem Sewa Motor Mahasiswa

Sebuah usaha sewa motor di dekat kampus menyewakan motor matic, bebek, dan listrik. Setiap jenis punya tarif harian dan aturan potongannya sendiri.

**Kebutuhan:**

1. Tulis versi **serba bisa**: satu kelas yang menyimpan daftar motor, menghitung biaya dengan rantai percabangan jenis, mencetak nota, dan mencatat riwayat. Simpan output-nya ke file.
2. *Refactor* menjadi desain yang menerapkan **kelima** prinsip SOLID: tarif per jenis (OCP), nota (SRP), riwayat yang disuntikkan (DIP), kontrak kecil (ISP), dan semua tarif menepati janji "biaya tidak pernah negatif" (LSP).
3. Buktikan dengan `fc` atau `diff` bahwa output versi baru **sama persis** dengan versi lama, lalu tambahkan jenis motor keempat **tanpa mengubah** kelas lama.
4. Buat tabel "tugas di kelas lama → kelas baru → prinsip" seperti di halaman konsep.

**Ketentuan pengumpulan:** kedua versi program (Python atau Java), tangkapan layar hasil `fc`/`diff`, dan tabel pemetaan tugas.

**Rubrik penilaian:**

| Aspek | Bobot |
|---|---|
| Versi serba bisa berjalan dan output-nya tersimpan | 10% |
| Desain baru menerapkan SRP, OCP, LSP, ISP, dan DIP dengan tepat (tidak berlebihan) | 40% |
| Bukti `fc`/`diff` bahwa output sama persis | 20% |
| Jenis motor keempat ditambahkan tanpa mengubah kelas lama | 15% |
| Tabel pemetaan tugas dan kerapian kode | 15% |

---

[⬅️ Konsep](README.md) · [🏠 Beranda](../README.md) · [Kuis ➡️](kuis.md)
