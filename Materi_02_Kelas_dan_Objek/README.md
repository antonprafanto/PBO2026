# Materi 02 — Kelas dan Objek

## 🎯 Tujuan Pembelajaran

Setelah mengikuti materi ini, mahasiswa mampu:
1. Menuliskan **sintaks lengkap** definisi kelas Python dengan benar
2. Memahami peran **konstruktor `__init__`** dan berbagai polanya (wajib, default, validasi)
3. Membedakan **positional argument** dan **keyword argument** saat membuat objek
4. Membuat dan mengelola **banyak objek** dari satu kelas menggunakan list dan loop
5. Mengakses, mengubah, dan menghapus atribut objek

---

## 📚 Baca Materi Terlebih Dahulu

👉 **[Baca materi lengkap di sini: materi.md](./materi.md)**

---

## 📋 Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Sintaks Kelas | Konvensi PascalCase, docstring, `__init__`, method |
| Konstruktor `__init__` | Wajib, nilai default, validasi, perhitungan otomatis |
| Positional vs Keyword | Dua cara memberikan argumen saat buat objek |
| Banyak Objek | List of objects, filter, sort, aggregate |
| Modifikasi Atribut | Baca, ubah, tambah, dan hapus atribut |

---

## 📂 File Kode — Urutan Pengerjaan

> **Ikuti urutan ini agar mudah dipahami:**

| Urutan | File | Deskripsi |
|--------|------|-----------|
| 1️⃣ | `kode/01_definisi_kelas.py` | Sintaks kelas, nilai default, objek sebagai parameter/return |
| 2️⃣ | `kode/02_banyak_objek.py` | Membuat banyak objek, list, filter, sort, hitung total |
| 3️⃣ | `kode/03_konstruktor.py` | Pola konstruktor: dasar, validasi, perhitungan otomatis |
| 4️⃣ | `kode/latihan.py` | Soal latihan mandiri — kerjakan setelah memahami materi |

---

## 🚀 Cara Menjalankan Kode

```bash
cd Materi_02_Kelas_dan_Objek/kode

python 01_definisi_kelas.py
python 02_banyak_objek.py
python 03_konstruktor.py
python latihan.py
```

---

## 🔑 Kata Kunci Penting

| Istilah | Arti |
|---------|------|
| `__init__` | Konstruktor — method khusus yang otomatis dipanggil saat objek dibuat |
| `self.atribut = nilai` | Mendefinisikan atribut instance di konstruktor |
| Positional argument | `Kelas(nilai1, nilai2)` — urutan harus sesuai |
| Keyword argument | `Kelas(param=nilai)` — bisa urutan bebas |
| Default value | `def __init__(self, x=0)` — nilai yang dipakai jika argumen tidak diberikan |
| `del objek` | Menghapus referensi ke objek |
| List of objects | `daftar = [Kelas(...), Kelas(...)]` — menyimpan banyak objek dalam list |

---

## ✅ Checklist Pemahaman

Sebelum lanjut ke Materi 03, pastikan Anda bisa:
- [ ] Membuat kelas dengan konstruktor berparameter wajib dan default
- [ ] Membedakan cara `Kelas(a, b)` vs `Kelas(param=a, param2=b)`
- [ ] Membuat list berisi banyak objek dan melakukan loop
- [ ] Memfilter dan mengurutkan list objek berdasarkan atribut tertentu
- [ ] Menyelesaikan minimal Soal 1 dan 2 di `latihan.py`

---

## ⬅️ | ➡️ Navigasi

[← Materi 01](../Materi_01_Pengantar_OOP/) | [🏠 Beranda](../README.md) | [Materi 03 →](../Materi_03_Atribut_dan_Method/)
