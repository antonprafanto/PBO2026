# Materi 03 — Atribut dan Method

---

## 1. Dua Jenis Atribut dalam Python

Ingat dari Materi 02 bahwa atribut adalah *data* yang dimiliki objek. Namun, di Python ada **dua jenis atribut** yang berperilaku sangat berbeda:

| | **Atribut Instance** | **Atribut Kelas** |
|---|---|---|
| **Milik** | Setiap objek secara individu | Kelas itu sendiri (dibagi ke SEMUA objek) |
| **Didefinisikan** | Di dalam `__init__` via `self.xxx` | Di badan kelas, di luar method apapun |
| **Berbeda per objek?** | ✅ Ya | ❌ Tidak (sama untuk semua) |
| **Akses** | `self.nama` atau `objek.nama` | `NamaKelas.nama` atau `self.nama` |

---

## 2. Atribut Instance

**Atribut instance** adalah atribut yang nilainya *unik untuk setiap objek*. Inilah atribut yang paling sering kita gunakan.

```python
class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        # Semua ini adalah atribut INSTANCE
        self.nama = nama   # ← tiap objek punya nilai 'nama' sendiri
        self.nim  = nim
        self.ipk  = ipk

budi  = Mahasiswa("Budi",  "2301001", 3.75)
sari  = Mahasiswa("Sari",  "2301002", 3.50)
andi  = Mahasiswa("Andi",  "2301003", 3.20)

print(budi.nama)   # Budi  ← nilai milik budi sendiri
print(sari.nama)   # Sari  ← nilai milik sari sendiri (independen!)

# Mengubah atribut instance SATU OBJEK tidak mempengaruhi objek lain
budi.ipk = 3.90
print(budi.ipk)    # 3.90 ← berubah
print(sari.ipk)    # 3.50 ← tidak berubah sama sekali
```

---

## 3. Atribut Kelas

**Atribut kelas** dimiliki oleh *kelas itu sendiri* dan **diakses bersama oleh semua objek**. Biasanya digunakan untuk data yang memang sama untuk semua instance.

```python
class Mahasiswa:
    # Atribut KELAS — didefinisikan di LUAR __init__
    universitas  = "Universitas Mulawarman"   # ← milik kelas
    program_studi = "Informatika"
    jumlah_mhs   = 0                           # ← counter objek

    def __init__(self, nama, nim):
        self.nama = nama   # ← atribut INSTANCE
        self.nim  = nim
        Mahasiswa.jumlah_mhs += 1  # update atribut kelas stiap ada mhs baru

budi = Mahasiswa("Budi", "2301001")
sari = Mahasiswa("Sari", "2301002")
andi = Mahasiswa("Andi", "2301003")

# Akses atribut kelas via nama kelas (cara yang direkomendasikan)
print(Mahasiswa.universitas)    # Universitas Mulawarman
print(Mahasiswa.jumlah_mhs)     # 3

# Atribut kelas juga bisa diakses via objek (tapi hati-hati!)
print(budi.universitas)         # Universitas Mulawarman (baca dari kelas)
```

> ⚠️ **Jebakan!** Jika kamu *mengubah* atribut kelas via objek (`budi.universitas = "..."`) Python akan membuat **atribut instance baru** untuk `budi`, bukan mengubah atribut kelas. Selalu ubah atribut kelas via `NamaKelas.atribut = nilai`.

```python
# BAHAYA: jangan lakukan ini kalau maksudnya mengubah atribut KELAS
budi.universitas = "Universitas Lain"

print(budi.universitas)       # "Universitas Lain" ← shadowed oleh instance attr
print(Mahasiswa.universitas)  # "Universitas Mulawarman" ← kelas tidak berubah!
print(sari.universitas)       # "Universitas Mulawarman" ← sari tidak terpengaruh
```

### Kapan Gunakan Atribut Kelas?

- **Konstanta** yang berlaku untuk semua objek (nama institusi, nilai minimum, dll.)
- **Counter** untuk menghitung jumlah objek yang dibuat
- **Cache / shared state** yang memang perlu dibagi

---

## 4. Tiga Jenis Method

Sama seperti atribut, method di Python juga ada **tiga jenis**:

| | **Instance Method** | **Class Method** | **Static Method** |
|---|---|---|---|
| **Decorator** | *(tidak ada)* | `@classmethod` | `@staticmethod` |
| **Parameter pertama** | `self` (objek) | `cls` (kelas) | *(tidak ada)* |
| **Bisa akses** | Atribut instance & kelas | Atribut kelas saja | Tidak bisa keduanya |
| **Dipanggil via** | `objek.method()` | `Kelas.method()` | `Kelas.method()` |

---

## 5. Method Instance

**Method instance** adalah jenis method yang paling umum. Parameter pertamanya adalah `self` yang merujuk ke objek itu sendiri, sehingga bisa mengakses semua atribut instance maupun kelas.

```python
class Rekening:
    def __init__(self, pemilik, saldo=0):
        self.pemilik = pemilik
        self.saldo   = saldo

    # Method instance — akses self
    def setor(self, jumlah):
        """Menambah saldo."""
        if jumlah <= 0:
            print("Jumlah setor harus positif!")
            return
        self.saldo += jumlah
        print(f"Setor Rp {jumlah:,.0f}. Saldo baru: Rp {self.saldo:,.0f}")

    def tarik(self, jumlah):
        """Menarik saldo."""
        if jumlah > self.saldo:
            print("Saldo tidak mencukupi!")
            return
        self.saldo -= jumlah
        print(f"Tarik Rp {jumlah:,.0f}. Saldo baru: Rp {self.saldo:,.0f}")

    def info(self):
        """Menampilkan ringkasan rekening."""
        print(f"Pemilik: {self.pemilik} | Saldo: Rp {self.saldo:,.0f}")

rek = Rekening("Budi", 1_000_000)
rek.setor(500_000)    # Setor Rp 500,000. Saldo baru: Rp 1,500,000
rek.tarik(200_000)    # Tarik Rp 200,000. Saldo baru: Rp 1,300,000
rek.info()            # Pemilik: Budi | Saldo: Rp 1,300,000
```

---

## 6. Class Method (`@classmethod`)

**Class method** menerima `cls` (bukan `self`) sebagai parameter pertama — `cls` merujuk ke *kelas* itu sendiri, bukan ke objek. Ia hanya bisa mengakses **atribut kelas**.

### Kegunaan Utama: Factory Method (Alternatif Konstruktor)

Salah satu pola desain paling umum adalah menggunakan `@classmethod` sebagai **factory method** — cara alternatif untuk membuat objek dari format data yang berbeda-beda.

```python
class Mahasiswa:
    universitas = "Universitas Mulawarman"

    def __init__(self, nama, nim, semester, ipk):
        self.nama     = nama
        self.nim      = nim
        self.semester = semester
        self.ipk      = ipk

    # Factory Method 1: buat dari string CSV
    @classmethod
    def dari_csv(cls, baris_csv):
        """Alternatif konstruktor: buat Mahasiswa dari baris CSV."""
        # "Budi,2301001,3,3.75"
        nama, nim, semester, ipk = baris_csv.split(",")
        return cls(nama, nim.strip(), int(semester), float(ipk))

    # Factory Method 2: buat mahasiswa baru (semester 1, IPK default)
    @classmethod
    def mahasiswa_baru(cls, nama, nim):
        """Buat mahasiswa semester pertama dengan IPK awal 0."""
        return cls(nama, nim, semester=1, ipk=0.0)

    # Class Method biasa: akses/ubah atribut kelas
    @classmethod
    def ganti_universitas(cls, nama_baru):
        cls.universitas = nama_baru

    def info(self):
        print(f"[{self.nim}] {self.nama} | Sem {self.semester} | IPK {self.ipk}")

# Cara normal
mhs1 = Mahasiswa("Andi", "2301001", 5, 3.80)

# Via factory method CSV
mhs2 = Mahasiswa.dari_csv("Budi,2301002,3,3.75")

# Via factory method baru
mhs3 = Mahasiswa.mahasiswa_baru("Citra", "2301003")

mhs1.info()   # [2301001] Andi | Sem 5 | IPK 3.8
mhs2.info()   # [2301002] Budi | Sem 3 | IPK 3.75
mhs3.info()   # [2301003] Citra | Sem 1 | IPK 0.0

# Ubah atribut kelas via class method
Mahasiswa.ganti_universitas("Universitas Indonesia")
print(Mahasiswa.universitas)  # Universitas Indonesia
```

---

## 7. Static Method (`@staticmethod`)

**Static method** adalah method yang *tidak terikat* ke objek maupun kelas — ia tidak menerima `self` ataupun `cls`. Gunakan static method untuk fungsi utilitas yang *secara logika berkaitan dengan kelas*, tapi tidak membutuhkan akses ke data kelas atau objek.

```python
class KonversiNilai:
    """Kelas utilitas untuk konversi nilai akademik."""

    @staticmethod
    def angka_ke_huruf(nilai):
        """Konversi nilai angka (0-100) ke nilai huruf."""
        if nilai >= 85:  return "A"
        if nilai >= 75:  return "B"
        if nilai >= 65:  return "C"
        if nilai >= 55:  return "D"
        return "E"

    @staticmethod
    def huruf_ke_bobot(huruf):
        """Konversi nilai huruf ke bobot angka."""
        bobot = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
        return bobot.get(huruf.upper(), 0.0)

    @staticmethod
    def hitung_ipk(daftar_nilai, daftar_sks):
        """Hitung IPK dari daftar nilai dan SKS."""
        total_bobot = sum(n * s for n, s in zip(daftar_nilai, daftar_sks))
        total_sks   = sum(daftar_sks)
        return round(total_bobot / total_sks, 2) if total_sks > 0 else 0.0

# Dipanggil via nama kelas (tidak perlu membuat objek)
print(KonversiNilai.angka_ke_huruf(87))         # A
print(KonversiNilai.huruf_ke_bobot("B"))         # 3.0

nilai = [4.0, 3.0, 4.0, 3.0]
sks   = [3, 2, 3, 2]
print(KonversiNilai.hitung_ipk(nilai, sks))      # 3.6
```

### Kapan Pakai Static Method?

Gunakan `@staticmethod` jika:
- Fungsinya *secara konseptual* berkaitan dengan kelas (misalnya validasi, konversi, kalkulasi)
- Fungsinya **tidak** membutuhkan `self` ataupun `cls`
- Kamu ingin mengelompokkan fungsi-fungsi utilitas dalam satu namespace kelas

---

## 8. Contoh Lengkap: Kelas `Karyawan`

Berikut contoh yang menggabungkan ketiga jenis atribut dan method:

```python
class Karyawan:
    # ── Atribut Kelas ──────────────────────────────────────
    perusahaan  = "PT Nusantara Digital"
    gaji_minimum = 3_000_000
    jumlah_karyawan = 0

    # ── Konstruktor ────────────────────────────────────────
    def __init__(self, nama, jabatan, gaji_pokok):
        # Atribut Instance
        self.nama       = nama
        self.jabatan    = jabatan
        self.gaji_pokok = gaji_pokok
        Karyawan.jumlah_karyawan += 1

    # ── Instance Methods ───────────────────────────────────
    def hitung_gaji_bersih(self, potongan_persen=10):
        """Hitung gaji bersih setelah potongan (default 10%)."""
        potongan = self.gaji_pokok * potongan_persen / 100
        return self.gaji_pokok - potongan

    def naik_jabatan(self, jabatan_baru, kenaikan_gaji):
        """Promosi karyawan."""
        self.jabatan    = jabatan_baru
        self.gaji_pokok += kenaikan_gaji
        print(f"{self.nama} dipromosikan ke {jabatan_baru}!")

    def info(self):
        print(f"{self.nama} | {self.jabatan} | Rp {self.gaji_pokok:,.0f}")

    # ── Class Methods ──────────────────────────────────────
    @classmethod
    def dari_dict(cls, data: dict):
        """Factory method: buat Karyawan dari dictionary."""
        return cls(data["nama"], data["jabatan"], data["gaji"])

    @classmethod
    def laporan_perusahaan(cls):
        """Tampilkan info tingkat kelas."""
        print(f"Perusahaan: {cls.perusahaan}")
        print(f"Total Karyawan: {cls.jumlah_karyawan}")

    # ── Static Methods ─────────────────────────────────────
    @staticmethod
    def format_rupiah(nominal):
        """Utilitas: format angka menjadi string Rupiah."""
        return f"Rp {nominal:,.0f}"

    @staticmethod
    def validasi_gaji(gaji):
        """Validasi apakah gaji di atas minimum."""
        return gaji >= Karyawan.gaji_minimum


# ── Penggunaan ─────────────────────────────────────────────
k1 = Karyawan("Anton",  "Junior Dev",    5_000_000)
k2 = Karyawan("Budi",   "Senior Dev",    9_000_000)
k3 = Karyawan.dari_dict({"nama": "Citra", "jabatan": "Designer", "gaji": 6_500_000})

k1.naik_jabatan("Mid Dev", 1_500_000)
# Anton dipromosikan ke Mid Dev!

k1.info()   # Anton | Mid Dev | Rp 6,500,000
k2.info()   # Budi | Senior Dev | Rp 9,000,000
k3.info()   # Citra | Designer | Rp 6,500,000

Karyawan.laporan_perusahaan()
# Perusahaan: PT Nusantara Digital
# Total Karyawan: 3

print(Karyawan.format_rupiah(6_500_000))    # Rp 6,500,000
print(Karyawan.validasi_gaji(2_500_000))    # False
```

---

## 9. Ringkasan Kapan Pakai Apa?

```
Pertanyaan yang perlu dijawab:
                           │
          ┌────────────────┼────────────────┐
          ▼                ▼                ▼
   "Butuh akses         "Butuh akses      "Tidak butuh
   data OBJEK           data KELAS        akses apapun"
   (self.xxx)?"         (cls.xxx)?"
          │                │                │
          ▼                ▼                ▼
   Instance Method     Class Method    Static Method
   def method(self):   @classmethod    @staticmethod
                        def method(cls): def method():
```

| Pertanyaan | Jawaban → Gunakan |
|---|---|
| Butuh baca/tulis data unik per objek? | **Instance Method** |
| Butuh factory method (cara alternatif buat objek)? | **Class Method** |
| Butuh baca/ubah atribut kelas? | **Class Method** |
| Cuma butuh fungsi utilitas terkait kelas? | **Static Method** |

---

## 📖 Bacaan Lanjutan

- 🔗 [Real Python: Class vs Instance Variables](https://realpython.com/instance-class-and-static-methods-demystified/)
- 🔗 [Python Docs: classmethod](https://docs.python.org/3/library/functions.html#classmethod)
- 🔗 [Python Docs: staticmethod](https://docs.python.org/3/library/functions.html#staticmethod)

---

*➡️ Lanjut ke: [Materi 04 — Enkapsulasi](../Materi_04_Enkapsulasi/materi.md)*
