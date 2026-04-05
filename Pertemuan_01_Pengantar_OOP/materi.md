# Materi Pertemuan 01 — Pengantar Pemrograman Berorientasi Objek (OOP)

---

## 1. Apa Itu Pemrograman Berorientasi Objek?

**Pemrograman Berorientasi Objek (OOP / Object-Oriented Programming)** adalah sebuah *paradigma pemrograman* — cara pandang atau gaya berpikir dalam menulis kode program — yang **mengorganisasi kode menggunakan konsep "objek"**.

Bayangkan dunia nyata di sekitar kita. Semua yang kita lihat adalah **objek**:
- 🚗 Sebuah **mobil** memiliki → warna, merek, kecepatan (data/atribut) + bisa maju, mundur, berhenti (aksi/method)
- 📱 Sebuah **smartphone** memiliki → merk, RAM, baterai (atribut) + bisa menelepon, foto, browsing (method)
- 🎓 Seorang **mahasiswa** memiliki → nama, NIM, IPK (atribut) + bisa daftar KRS, ikut ujian (method)

OOP meniru cara berpikir ini ke dalam program komputer.

---

## 2. Paradigma Prosedural vs OOP

Sebelum OOP populer, programmer menggunakan paradigma **prosedural** (langkah-langkah berurutan). Mari kita bandingkan keduanya:

### 🔴 Cara Prosedural (Lama)

```python
# Data tersebar sebagai variabel biasa
nama_mahasiswa = "Budi"
nim_mahasiswa  = "2301001"
ipk_mahasiswa  = 3.75

# Fungsi terpisah dari data
def tampilkan_info(nama, nim, ipk):
    print(f"Nama: {nama}, NIM: {nim}, IPK: {ipk}")

def hitung_predikat(ipk):
    if ipk >= 3.5:
        return "Cum Laude"
    elif ipk >= 3.0:
        return "Sangat Memuaskan"
    else:
        return "Memuaskan"

tampilkan_info(nama_mahasiswa, nim_mahasiswa, ipk_mahasiswa)
# Output: Nama: Budi, NIM: 2301001, IPK: 3.75
```

**Masalahnya:** Semakin banyak mahasiswa, kode semakin kacau! Bagaimana kalau ada 100 mahasiswa? Kita butuh 300 variabel terpisah yang bertebaran.

### 🟢 Cara OOP (Modern)

```python
class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim  = nim
        self.ipk  = ipk

    def tampilkan_info(self):
        print(f"Nama: {self.nama}, NIM: {self.nim}, IPK: {self.ipk}")

    def hitung_predikat(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        return "Memuaskan"

# Membuat objek — semudah ini!
budi = Mahasiswa("Budi", "2301001", 3.75)
sari = Mahasiswa("Sari", "2301002", 3.20)

budi.tampilkan_info()
# Output: Nama: Budi, NIM: 2301001, IPK: 3.75

print(sari.hitung_predikat())
# Output: Sangat Memuaskan
```

**Hasilnya:** Data dan fungsi rapi dalam satu wadah. Mau 1000 mahasiswa pun tetap bersih!

---

## 3. Empat Konsep Dasar: Kelas, Objek, Atribut, dan Method

Sebelum masuk ke 4 pilar, kita harus paham 4 istilah fundamental ini:

### 🏗️ a) Kelas (Class) — Blueprint/Cetakan

**Kelas** adalah *cetakan* atau *template* untuk membuat objek. Ia mendefinisikan seperti apa objek yang akan dibuat.

Analogi:
| Kelas | Objek |
|-------|-------|
| Desain/denah rumah | Rumah yang sudah dibangun |
| Cetakan kue | Kue yang sudah jadi |
| Definisi "Mahasiswa" | "Budi si mahasiswa" secara spesifik |
| Blueprint kartu ID | Kartu ID yang sudah dicetak |

```
class Mahasiswa    ←── Kelas (cetakan/template)
      │
      ├── budi = Mahasiswa("Budi", ...)   ←── Objek 1
      ├── sari = Mahasiswa("Sari", ...)   ←── Objek 2
      └── andi = Mahasiswa("Andi", ...)   ←── Objek 3
```

### 📦 b) Objek (Object/Instance) — Wujud Nyata

**Objek** adalah *hasil cetakan* dari kelas — wujud konkret yang benar-benar ada di memori komputer. Satu kelas bisa menghasilkan tak terbatas objek.

Proses membuat objek dari kelas disebut **instansiasi** (*instantiation*).

```python
budi = Mahasiswa("Budi", "2301001", 3.75)
#  ▲       ▲         ▲
#  │       │         └── argumen yang dikirim ke __init__
#  │       └──────────── nama kelas (memanggil konstruktor)
#  └──────────────────── variabel yang menyimpan objek
```

### 🗂️ c) Atribut — Data yang Dimiliki Objek

**Atribut** adalah **data/informasi** yang dimiliki oleh sebuah objek. Setiap objek bisa memiliki nilai atribut yang berbeda-beda.

```python
class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.nama = nama   # ← atribut 'nama'
        self.nim  = nim    # ← atribut 'nim'
        self.ipk  = ipk    # ← atribut 'ipk'

budi = Mahasiswa("Budi", "2301001", 3.75)
sari = Mahasiswa("Sari", "2301002", 3.20)

# Mengakses atribut dengan titik (dot notation)
print(budi.nama)   # Output: Budi
print(sari.ipk)    # Output: 3.20
```

### ⚙️ d) Method — Perilaku/Aksi Objek

**Method** adalah **fungsi yang didefinisikan di dalam kelas**. Method mendeskripsikan apa yang bisa *dilakukan* oleh sebuah objek.

```python
class Mahasiswa:
    def __init__(self, nama, ipk):
        self.nama = nama
        self.ipk  = ipk

    def sapa(self):                        # ← method 'sapa'
        print(f"Halo, saya {self.nama}!")

    def hitung_predikat(self):             # ← method 'hitung_predikat'
        if self.ipk >= 3.5:
            return "Cum Laude"
        return "Sangat Memuaskan"

budi = Mahasiswa("Budi", 3.80)

# Memanggil method dengan titik (dot notation)
budi.sapa()                          # Output: Halo, saya Budi!
print(budi.hitung_predikat())        # Output: Cum Laude
```

> 💡 **Perbedaan Atribut vs Method:**
> - **Atribut** = *kata benda* (nama, usia, warna) → akses tanpa kurung: `objek.nama`
> - **Method** = *kata kerja* (sapa, hitung, tampilkan) → panggil dengan kurung: `objek.sapa()`

---

## 4. Empat Pilar OOP

OOP berdiri di atas 4 pilar utama. Di Pertemuan 01 ini kita kenalan dulu — masing-masing akan dipelajari mendalam di pertemuan tersendiri.

### 🔒 Pilar 1: Enkapsulasi (Encapsulation)
> *"Sembunyikan detail yang tidak perlu, tampilkan yang penting saja"*

Membungkus data (atribut) dan perilaku (method) dalam satu unit kelas, sekaligus **melindungi data** agar tidak bisa diubah sembarangan dari luar.

```
Kelas Mahasiswa
├── __ipk (tersembunyi/private)    ← tidak bisa diubah langsung dari luar
└── get_ipk()                      ← cara resmi/aman untuk membacanya
└── set_ipk(nilai_baru)            ← cara resmi/aman untuk mengubahnya
```

📌 *Dipelajari mendalam di: Pertemuan 04*

### 🧬 Pilar 2: Pewarisan (Inheritance)
> *"Anak mewarisi sifat orang tua, tapi bisa punya keunikannya sendiri"*

Kelas anak bisa **mewarisi atribut dan method** dari kelas induk, sehingga kode tidak perlu ditulis ulang (*code reuse*).

```
Pengguna (induk)  →  nama, email, login()
├── Mahasiswa (anak)  →  mewarisi + punya nim, ipk, daftar_krs()
└── Dosen (anak)      →  mewarisi + punya nip, bidang_ajar, ajar()
```

📌 *Dipelajari mendalam di: Pertemuan 06*

### 🎭 Pilar 3: Polimorfisme (Polymorphism)
> *"Satu perintah, banyak bentuk respons"*

Objek yang berbeda dapat merespons **perintah yang sama dengan cara yang berbeda** sesuai jenisnya.

```python
# Semua punya method suara(), tapi hasilnya berbeda
anjing.suara()  # "Guk!"
kucing.suara()  # "Meow!"
sapi.suara()    # "Moo!"
```

📌 *Dipelajari mendalam di: Pertemuan 07*

### 🎯 Pilar 4: Abstraksi (Abstraction)
> *"Fokus pada APA yang dilakukan, bukan BAGAIMANA caranya"*

Menyembunyikan kompleksitas internal dan hanya menampilkan antarmuka yang diperlukan. Seperti memakai remote TV — kamu tekan tombol, TV menyala. Kamu tidak perlu tahu sirkuit elektroniknya.

```python
# Kamu tidak perlu tahu cara kerjanya di dalam
# Cukup tahu bahwa method ini tersedia dan apa hasilnya
mahasiswa.daftar_krs(["PBO", "Basis Data"])
```

📌 *Dipelajari mendalam di: Pertemuan 08*

---

## 5. Terminologi Penting

Hafalkan istilah-istilah ini karena akan sering muncul:

| Istilah | Bahasa Indonesia | Contoh |
|---------|-----------------|--------|
| **Class** | Kelas / Cetakan | `class Mahasiswa:` |
| **Object / Instance** | Objek / Wujud nyata | `budi = Mahasiswa(...)` |
| **Instantiation** | Instansiasi / Pembuatan objek | Proses `budi = Mahasiswa(...)` |
| **Attribute** | Atribut | `self.nama`, `self.nim` |
| **Method** | Method / Fungsi kelas | `def tampilkan_info(self):` |
| **Constructor** | Konstruktor | `def __init__(self, ...):` |
| **`self`** | Referensi ke diri sendiri | Parameter pertama setiap method |
| **Dot Notation** | Notasi titik | `budi.nama`, `budi.sapa()` |

---

## 6. Mengapa Belajar OOP?

| Alasan | Penjelasan |
|--------|-----------|
| 📦 **Modular** | Kode tersusun dalam unit-unit yang jelas, mudah dicari |
| ♻️ **Reusable** | Kelas bisa dipakai ulang di banyak proyek tanpa tulis ulang |
| 🔧 **Maintainable** | Mudah diperbarui tanpa harus mengubah seluruh program |
| 🤝 **Kolaborasi** | Tim bisa bekerja di kelas berbeda secara bersamaan |
| 🏭 **Industri** | Hampir semua software profesional menggunakan OOP |
| 🤖 **AI/ML** | Framework AI seperti TensorFlow, PyTorch, scikit-learn berbasis OOP |

---

## 7. Ringkasan Visual

```
┌─────────────────────────────────────────────────────┐
│                    KELAS (Template)                 │
│                                                     │
│   class Mahasiswa:                                  │
│       ├── Atribut: nama, nim, ipk    ← DATA         │
│       └── Method:  tampilkan_info() ← PERILAKU      │
└─────────────────────────────────────────────────────┘
                          │
         ┌────────────────┼────────────────┐
         ▼                ▼                ▼
   ┌──────────┐    ┌──────────┐    ┌──────────┐
   │  Objek 1 │    │  Objek 2 │    │  Objek 3 │
   │   budi   │    │   sari   │    │   andi   │
   │ nama=... │    │ nama=... │    │ nama=... │
   │ nim=...  │    │ nim=...  │    │ nim=...  │
   └──────────┘    └──────────┘    └──────────┘
   (INDEPENDEN satu sama lain — ubah satu, tidak mempengaruhi lainnya)

4 Pilar OOP:
  🔒 Enkapsulasi  → Lindungi data dari akses sembarangan
  🧬 Pewarisan    → Wariskan kode dari kelas induk ke anak
  🎭 Polimorfisme → Satu perintah, respons berbeda-beda
  🎯 Abstraksi    → Sembunyikan kompleksitas, tampilkan yang perlu
```

---

## 📖 Bacaan Lanjutan

- 🔗 [Python Docs: Classes](https://docs.python.org/3/tutorial/classes.html)
- 🔗 [Real Python: OOP in Python](https://realpython.com/python3-object-oriented-programming/)
- 📺 [Corey Schafer — OOP Tutorial (YouTube)](https://www.youtube.com/playlist?list=PL-osiE80TeTsqhIuOqKhwlXsIBIdSeYtc)

---

*➡️ Lanjut ke: [Pertemuan 02 — Kelas dan Objek](../Pertemuan_02_Kelas_dan_Objek/materi.md)*
