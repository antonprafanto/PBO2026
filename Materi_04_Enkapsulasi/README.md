# Materi 04 — Enkapsulasi

## 🎯 Tujuan Pembelajaran

Setelah mengikuti materi ini, mahasiswa mampu:
1. Memahami konsep **enkapsulasi** sebagai salah satu pilar OOP
2. Membedakan tingkat akses: **public**, **protected**, dan **private**
3. Menggunakan **`@property`** untuk membuat getter yang aman
4. Menggunakan **`@setter`** dan **`@deleter`** untuk mengontrol akses data
5. Menerapkan **validasi data** pada setter untuk menjaga integritas objek
6. Menerapkan enkapsulasi pada kasus nyata dunia kerja

---

## 📚 Baca Materi Terlebih Dahulu

👉 **[Baca materi lengkap di sini: materi.md](./materi.md)**

---

## 📋 Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Konsep Enkapsulasi | Membungkus data + perilaku, menyembunyikan detail internal |
| Konvensi Akses | `nama` (public), `_nama` (protected), `__nama` (private) |
| `@property` | Mengakses atribut private seperti atribut biasa, tapi via method |
| `@setter` | Mengubah atribut private dengan validasi |
| `@deleter` | Menghapus/mereset atribut private |
| Name Mangling | Bagaimana Python menyembunyikan atribut `__` |

---

## 📂 File Kode — Urutan Pengerjaan

> **Ikuti urutan ini agar mudah dipahami:**

| Urutan | File | Deskripsi |
|--------|------|-----------|
| 1️⃣ | `kode/01_akses_modifier.py` | Public, protected, private — perbedaan dan name mangling |
| 2️⃣ | `kode/02_property.py` | `@property`, `@setter`, `@deleter` secara lengkap |
| 3️⃣ | `kode/03_enkapsulasi_praktis.py` | Studi kasus nyata: RekeningBank & Mahasiswa |
| 4️⃣ | `kode/latihan.py` | Soal latihan mandiri — kerjakan setelah memahami materi |

---

## 🚀 Cara Menjalankan Kode

```bash
cd Materi_04_Enkapsulasi/kode

python 01_akses_modifier.py
python 02_property.py
python 03_enkapsulasi_praktis.py
python latihan.py
```

---

## 🔑 Kata Kunci Penting

| Istilah | Arti |
|---------|------|
| Enkapsulasi | Membungkus data + method, melindungi dari akses sembarangan |
| `nama` | **Public** — bisa diakses dari mana saja |
| `_nama` | **Protected** — konvensi "hanya untuk internal & subkelas" |
| `__nama` | **Private** — disembunyikan via name mangling |
| `@property` | Decorator untuk membuat getter yang tampak seperti atribut |
| `@nama.setter` | Decorator untuk mendefinisikan setter dengan validasi |
| `@nama.deleter` | Decorator untuk mendefinisikan deleter |
| Name Mangling | `__nama` diubah jadi `_NamaKelas__nama` oleh Python |

---

## ✅ Checklist Pemahaman

Sebelum lanjut ke Materi 05, pastikan Anda bisa:
- [ ] Menjelaskan perbedaan `nama`, `_nama`, dan `__nama`
- [ ] Membuat atribut private dan mengaksesnya dengan `@property`
- [ ] Menambahkan validasi pada `@setter`
- [ ] Menjelaskan apa itu *name mangling* dan kapan terjadi
- [ ] Menyelesaikan minimal Soal 1 dan 2 di `latihan.py`

---

## ⬅️ | ➡️ Navigasi

[← Materi 03](../Materi_03_Atribut_dan_Method/) | [🏠 Beranda](../README.md) | [Materi 05 →](../Materi_05_Hubungan_Kelas_dan_UML/)
