# Materi 05 — Hubungan Kelas dan UML

---

## 1. Mengapa Butuh Lebih dari Satu Kelas?

Pada materi sebelumnya kita selalu bekerja dengan *satu kelas dalam satu waktu*. Namun di dunia nyata, sebuah sistem dibangun dari **banyak kelas yang saling berinteraksi**.

Bayangkan sistem akademik kampus:
- Seorang **Mahasiswa** mengambil banyak **Mata Kuliah**
- Setiap **Mata Kuliah** diajar oleh seorang **Dosen**
- **Dosen** terdaftar di sebuah **Jurusan**
- **Jurusan** memiliki banyak **Ruang Kelas**

Setiap baris di atas menggambarkan **hubungan (*relationship*)** antar kelas.

Di OOP, ada tiga jenis hubungan utama antar kelas:

| Jenis | Kata Kunci | Kekuatan | Contoh Nyata |
|-------|-----------|----------|-------------|
| **Asosiasi** | "menggunakan" | Lemah | Mahasiswa menggunakan Printer |
| **Agregasi** | "memiliki" | Sedang | Jurusan memiliki banyak Dosen |
| **Komposisi** | "terdiri dari" | Kuat | Rumah terdiri dari Kamar |

---

## 2. Asosiasi (Association)

**Asosiasi** adalah hubungan paling umum dan paling longgar. Objek A "mengenal" atau "menggunakan" objek B, tetapi **keduanya hidup secara independen** — satu bisa ada tanpa yang lain.

### Ciri-ciri Asosiasi:
- Objek B diterima sebagai **parameter** method, atau
- Dibuat sementara di dalam method, lalu dibuang
- Tidak ada "kepemilikan" — keduanya berdiri sendiri

### Contoh di Dunia Nyata:
```
Kasir ---------> Produk
(Kasir memproses Produk, tapi keduanya independen)

Dokter ---------> Pasien
(Dokter memeriksa Pasien, tapi Pasien bisa ke Dokter lain)
```

### Implementasi Python:

```python
class Printer:
    def __init__(self, merk, dpi):
        self.merk = merk
        self.dpi  = dpi

    def cetak(self, dokumen):
        print(f"[{self.merk}] Mencetak: '{dokumen}' @ {self.dpi} DPI")


class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    # Printer diterima sebagai PARAMETER — hubungan longgar
    def cetak_tugas(self, printer, nama_file):
        """Mahasiswa menggunakan Printer untuk mencetak tugas."""
        print(f"{self.nama} mencetak {nama_file}...")
        printer.cetak(nama_file)


# Kedua objek dibuat secara INDEPENDEN
printer_lab = Printer("HP LaserJet", 1200)
budi        = Mahasiswa("Budi Santoso", "2301001")

# Asosiasi terjadi saat method dipanggil
budi.cetak_tugas(printer_lab, "Laporan_PBO.pdf")

# Printer bisa digunakan oleh Mahasiswa lain
sari = Mahasiswa("Sari Dewi", "2301002")
sari.cetak_tugas(printer_lab, "UTS_Kalkulus.pdf")
```

### Diagram UML Asosiasi:
```
+-------------+       menggunakan       +----------+
|  Mahasiswa  | ----------------------> | Printer  |
+-------------+                         +----------+
| - nama      |                         | - merk   |
| - nim       |                         | - dpi    |
+-------------+                         +----------+
| cetak_tugas |                         | cetak()  |
+-------------+                         +----------+
```
**Notasi:** `---->` (panah biasa — asosiasi searah)

---

## 3. Agregasi (Aggregation)

**Agregasi** adalah hubungan "memiliki" yang lebih kuat dari asosiasi, tetapi masih **longgar dalam kepemilikan**. Objek B (*bagian*) **bisa hidup sendiri** tanpa objek A (*induk*).

### Ciri-ciri Agregasi:
- Objek bagian dibuat **di luar** objek induk
- Objek bagian **dikirim via konstruktor atau method**
- Jika objek induk dihapus, objek bagian **tetap hidup**

### Contoh di Dunia Nyata:
```
Jurusan  <>-------  Dosen
(Dosen milik Jurusan, tapi jika Jurusan dibubarkan,
 Dosen masih tetap ada — bisa pindah ke Jurusan lain)

Universitas <>-------  Mahasiswa
(Jika Universitas tutup, Mahasiswa masih ada — bisa pindah)
```

### Implementasi Python:

```python
class Dosen:
    def __init__(self, nama, nip, bidang):
        self.nama   = nama
        self.nip    = nip
        self.bidang = bidang

    def __str__(self):
        return f"Dosen: {self.nama} [{self.bidang}]"


class Jurusan:
    def __init__(self, nama, kode):
        self.nama   = nama
        self.kode   = kode
        self._dosen = []   # list untuk menyimpan objek Dosen

    def tambah_dosen(self, dosen):
        """Dosen DIKIRIM dari luar — Jurusan tidak membuat Dosen sendiri."""
        if isinstance(dosen, Dosen):
            self._dosen.append(dosen)
            print(f"  {dosen.nama} bergabung ke {self.nama}")

    def hapus_dosen(self, nip):
        """Menghapus dosen dari jurusan (bukan menghapus objek Dosen)."""
        self._dosen = [d for d in self._dosen if d.nip != nip]

    def tampilkan(self):
        print(f"\n  Jurusan: {self.nama} ({self.kode})")
        print(f"  Jumlah Dosen: {len(self._dosen)}")
        for d in self._dosen:
            print(f"    - {d}")


# Dosen dibuat INDEPENDEN dari Jurusan
dosen1 = Dosen("Dr. Anton",   "NIP001", "Machine Learning")
dosen2 = Dosen("Dr. Budi",    "NIP002", "Network Security")
dosen3 = Dosen("Dr. Citra",   "NIP003", "Database Systems")

# Jurusan MEMILIKI dosen (agregasi)
jurusan_if = Jurusan("Informatika", "IF")
jurusan_if.tambah_dosen(dosen1)
jurusan_if.tambah_dosen(dosen2)

jurusan_si = Jurusan("Sistem Informasi", "SI")
jurusan_si.tambah_dosen(dosen3)

# Satu dosen BISA dimiliki dua jurusan sekaligus (double appointment)
jurusan_si.tambah_dosen(dosen1)

jurusan_if.tampilkan()
jurusan_si.tampilkan()

# Jika jurusan_if dihapus, dosen1 dan dosen2 MASIH ADA
del jurusan_if
print(f"\n  dosen1 masih ada: {dosen1}")
print(f"  dosen2 masih ada: {dosen2}")
```

### Diagram UML Agregasi:
```
+----------+        memiliki        +---------+
| Jurusan  | <>-------------------- | Dosen   |
+----------+  1              *      +---------+
| - nama   |  (satu Jurusan        | - nama  |
| - kode   |   punya banyak Dosen) | - nip   |
+----------+                        +---------+
```
**Notasi:** `<>----` (diamond kosong di sisi induk)

> **Angka di garis UML:**
> - `1` = tepat satu
> - `*` = nol atau lebih (banyak)
> - `1..*` = satu atau lebih
> - `0..1` = nol atau satu (opsional)

---

## 4. Komposisi (Composition)

**Komposisi** adalah hubungan "terdiri dari" yang **paling kuat**. Objek B (*bagian*) **tidak bisa hidup tanpa** objek A (*induk*). Objek bagian **dibuat oleh** objek induk dan **dihancurkan bersama** objek induk.

### Ciri-ciri Komposisi:
- Objek bagian dibuat **di dalam** objek induk (di konstruktor atau method internal)
- Jika objek induk dihapus, objek bagian **ikut musnah**
- Tidak ada berbagi objek bagian antar dua induk

### Contoh di Dunia Nyata:
```
Rumah  *-------  Kamar
(Kamar tidak bisa berdiri sendiri tanpa Rumah)

Pesawat  *-------  Mesin
(Mesin pesawat tidak bisa eksis tanpa Pesawat itu)

Order  *-------  OrderItem
(Item pesanan tidak ada tanpa Order-nya)
```

### Implementasi Python:

```python
class Kamar:
    """Kamar tidak bisa hidup tanpa Rumah — ini adalah bagian dari Komposisi."""

    def __init__(self, nomor, fungsi, luas_m2):
        self.nomor   = nomor
        self.fungsi  = fungsi
        self.luas_m2 = luas_m2

    def __str__(self):
        return f"Kamar {self.nomor}: {self.fungsi} ({self.luas_m2} m2)"


class Rumah:
    """
    Rumah terdiri dari Kamar-kamar (Komposisi).
    Kamar dibuat DI DALAM Rumah dan hancur bersama Rumah.
    """

    def __init__(self, alamat, pemilik):
        self.alamat  = alamat
        self.pemilik = pemilik
        # Kamar dibuat LANGSUNG oleh Rumah — bukan dari luar
        self._kamar  = []

    def tambah_kamar(self, fungsi, luas_m2):
        """Rumah sendiri yang menciptakan Kamar baru."""
        nomor = len(self._kamar) + 1
        kamar_baru = Kamar(nomor, fungsi, luas_m2)   # dibuat DI SINI
        self._kamar.append(kamar_baru)
        print(f"  [+] {kamar_baru} ditambahkan")
        return kamar_baru

    @property
    def total_luas(self):
        return sum(k.luas_m2 for k in self._kamar)

    @property
    def jumlah_kamar(self):
        return len(self._kamar)

    def tampilkan(self):
        print(f"\n  Rumah milik {self.pemilik} @ {self.alamat}")
        print(f"  Total luas: {self.total_luas} m2 | {self.jumlah_kamar} kamar")
        for k in self._kamar:
            print(f"    - {k}")


# Rumah membuat Kamar-nya sendiri (Komposisi)
rumah_budi = Rumah("Jl. Mulawarman No. 5, Samarinda", "Budi Santoso")
rumah_budi.tambah_kamar("Ruang Tamu",  25)
rumah_budi.tambah_kamar("Kamar Tidur Utama", 20)
rumah_budi.tambah_kamar("Kamar Tidur 2",     15)
rumah_budi.tambah_kamar("Dapur",       12)
rumah_budi.tambah_kamar("Kamar Mandi",  6)

rumah_budi.tampilkan()

# Saat rumah_budi dihapus, semua Kamar-nya ikut musnah
# (tidak ada referensi lain ke Kamar-kamar tersebut)
```

### Diagram UML Komposisi:
```
+----------+        terdiri dari    +---------+
|  Rumah   | *--------------------- | Kamar   |
+----------+  1              1..*   +---------+
| - alamat |                        | - nomor |
| - pemilik|                        | - fungsi|
+----------+                        | - luas  |
```
**Notasi:** `*----` (diamond terisi di sisi induk)

---

## 5. Perbandingan Lengkap: Asosiasi vs Agregasi vs Komposisi

```
ASOSIASI (Menggunakan):
  Mahasiswa -----> Printer
  - Printer dibuat di luar Mahasiswa
  - Printer dikirim sebagai PARAMETER method
  - Printer bisa dipakai Mahasiswa lain juga
  - Printer tetap ada setelah method selesai
  - Hubungan: sementara, "meminjam"

AGREGASI (Memiliki — Has-A Lemah):
  Jurusan <>----> Dosen
  - Dosen dibuat di luar Jurusan
  - Dosen dikirim via tambah_dosen()
  - Satu Dosen bisa milik dua Jurusan
  - Hapus Jurusan => Dosen tetap hidup
  - Hubungan: permanen tapi longgar

KOMPOSISI (Terdiri Dari — Has-A Kuat):
  Rumah *----> Kamar
  - Kamar dibuat DI DALAM Rumah
  - Tidak ada yang bisa membuat Kamar tanpa Rumah
  - Kamar hanya milik SATU Rumah
  - Hapus Rumah => Kamar ikut musnah
  - Hubungan: permanen dan eksklusif
```

| Aspek | Asosiasi | Agregasi | Komposisi |
|-------|----------|----------|-----------|
| Dibuat di | Luar, dikirim sebagai parameter | Luar, dikirim ke konstruktor/method | Dalam objek induk |
| Kepemilikan | Tidak ada | Ya, tapi bisa berbagi | Ya, eksklusif |
| Hidup mandiri? | Ya | Ya | Tidak |
| Jika induk dihapus | Bagian tetap ada | Bagian tetap ada | Bagian ikut musnah |
| Notasi UML | `---->` | `<>---->` | `*---->` |

---

## 6. Studi Kasus: Sistem Order Toko Online

Sistem toko online adalah contoh sempurna yang menggabungkan ketiga hubungan sekaligus:

```python
# KOMPOSISI: Order terdiri dari OrderItem
# AGREGASI:  Order memiliki satu Pelanggan
# ASOSIASI:  Order menggunakan Kurir untuk pengiriman

class Pelanggan:
    """Pelanggan berdiri sendiri (eksis tanpa Order)."""
    def __init__(self, nama, email):
        self.nama  = nama
        self.email = email


class Produk:
    """Produk berdiri sendiri (eksis tanpa Order)."""
    def __init__(self, nama, harga):
        self.nama  = nama
        self.harga = harga


class OrderItem:
    """OrderItem tidak bisa eksis tanpa Order (Komposisi)."""
    def __init__(self, produk, qty):
        self.produk = produk
        self.qty    = qty

    @property
    def subtotal(self):
        return self.produk.harga * self.qty


class Kurir:
    """Kurir berdiri sendiri."""
    def __init__(self, nama, kode):
        self.nama = nama
        self.kode = kode

    def kirim(self, order_id, alamat):
        print(f"  [{self.kode}] Mengirim Order #{order_id} ke {alamat}")


class Order:
    _counter = 0

    def __init__(self, pelanggan, alamat_kirim):
        Order._counter += 1
        self.id           = Order._counter
        self.pelanggan    = pelanggan      # AGREGASI — Pelanggan dari luar
        self.alamat_kirim = alamat_kirim
        self._items       = []             # KOMPOSISI — items dibuat di dalam
        self._dikirim     = False

    def tambah_item(self, produk, qty):
        """Membuat OrderItem di dalam Order (Komposisi)."""
        item = OrderItem(produk, qty)
        self._items.append(item)

    @property
    def total(self):
        return sum(item.subtotal for item in self._items)

    def proses_pengiriman(self, kurir):
        """Menggunakan Kurir sebagai parameter (Asosiasi)."""
        kurir.kirim(self.id, self.alamat_kirim)
        self._dikirim = True

    def tampilkan(self):
        print(f"\n  Order #{self.id} — Pelanggan: {self.pelanggan.nama}")
        print(f"  Kirim ke: {self.alamat_kirim}")
        for item in self._items:
            print(f"    {item.produk.nama} x{item.qty} = Rp {item.subtotal:,.0f}")
        print(f"  TOTAL: Rp {self.total:,.0f}")
```

---

## 7. Panduan Singkat Diagram Kelas UML

Diagram Kelas UML adalah cara standar untuk menggambarkan struktur kelas secara visual sebelum menulis kode.

### Notasi Dasar Sebuah Kelas:
```
+---------------------------+
|       NamaKelas           |  <- bagian nama
+---------------------------+
| - atribut_private: tipe   |  <- bagian atribut
| # atribut_protected: tipe |    (-) private
| + atribut_public: tipe    |    (#) protected
+---------------------------+    (+) public
| + method_publik(): tipe   |  <- bagian method
| - _method_private(): void |
+---------------------------+
```

### Hubungan dan Notasinya:
```
A -----------> B   :  Asosiasi (A menggunakan B)
A <o>--------- B   :  Agregasi (A memiliki B, B bisa mandiri)
A <*>--------- B   :  Komposisi (A terdiri dari B, B tergantung A)
A <|---------- B   :  Pewarisan / Inheritance (nanti di Materi 06)
A <|..........B    :  Implementasi Interface (nanti di Materi 08)
```

### Multiplisitas (angka di garis):
```
1        = tepat satu
*  atau  n = nol atau lebih (banyak)
0..1     = opsional (nol atau satu)
1..*     = satu atau lebih
2..5     = antara dua sampai lima
```

### Contoh: Diagram Kelas Sistem Akademik
```
+--------------+      memiliki      +---------------+
|   Jurusan    | <>---------------  |    Dosen      |
+--------------+  1           *     +---------------+
| - nama       |                    | - nama        |
| - kode       |                    | - nip         |
+--------------+                    | - bidang      |
| + tampilkan()|                    +---------------+
+--------------+                    | + mengajar()  |
       |                            +---------------+
       | terdiri dari                      |
       | 1..*                              | mengajar
       |                                   |
+-------------+            1..*    +---------------+
|  MataKuliah | -------------------| Mahasiswa     |
+-------------+                    +---------------+
| - kode_mk   |                    | - nama        |
| - nama      |                    | - nim         |
| - sks       |                    | - ipk         |
+-------------+                    +---------------+
```

---

## 8. Tips Memilih Jenis Hubungan

Gunakan pertanyaan berikut sebagai panduan:

**1. Apakah B bisa eksis tanpa A?**
- Tidak bisa → **Komposisi**
- Bisa → lanjut pertanyaan 2

**2. Apakah A "memiliki" B secara permanen (B tersimpan sebagai atribut A)?**
- Ya → **Agregasi**
- Tidak (hanya dipakai sementara / dikirim sebagai parameter) → **Asosiasi**

### Contoh Praktis:
| Skenario | Hubungan |
|---------|---------|
| Mahasiswa menggunakan Komputer di lab | Asosiasi |
| Universitas memiliki Mahasiswa (mahasiswa bisa pindah) | Agregasi |
| Laptop memiliki CPU (CPU tidak bisa lepas dari laptop) | Komposisi |
| Rumah sakit menggunakan Obat untuk treatment | Asosiasi |
| Apotek memiliki stok Obat | Agregasi |
| Resep terdiri dari Daftar Obat yang diresepkan | Komposisi |

---

## Bacaan Lanjutan

- [Real Python: Composition vs Inheritance](https://realpython.com/inheritance-composition-python/)
- [Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)
- [UML Class Diagram Tutorial — Visual Paradigm](https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/)

---

*Lanjut ke: [Materi 06 — Pewarisan (Inheritance)](../Materi_06_Pewarisan/materi.md)*
