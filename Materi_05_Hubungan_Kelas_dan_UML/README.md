# Materi 05 — Hubungan Kelas dan UML

## Tujuan Pembelajaran

Setelah mengikuti materi ini, mahasiswa mampu:
1. Menjelaskan tiga jenis hubungan antar kelas: **Asosiasi**, **Agregasi**, dan **Komposisi**
2. Membedakan kapan harus memakai masing-masing jenis hubungan
3. Mengimplementasikan hubungan antar kelas dalam kode Python
4. Membaca dan menulis **Diagram Kelas UML** sederhana
5. Merancang sistem yang terdiri dari beberapa kelas yang saling berinteraksi

---

## Baca Materi Terlebih Dahulu

**[Baca materi lengkap di sini: materi.md](./materi.md)**

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Asosiasi | Hubungan "menggunakan" — dua kelas saling kenal tapi independen |
| Agregasi | Hubungan "memiliki" — bagian bisa hidup tanpa induk |
| Komposisi | Hubungan "terdiri dari" — bagian tidak bisa hidup tanpa induk |
| Diagram UML | Notasi visual untuk merepresentasikan hubungan antar kelas |
| Implementasi Python | Cara mewujudkan ketiga hubungan dalam kode nyata |

---

## File Kode — Urutan Pengerjaan

> **Ikuti urutan ini agar mudah dipahami:**

| Urutan | File | Deskripsi |
|--------|------|-----------|
| 1 | `kode/01_asosiasi.py` | Hubungan "menggunakan" antar objek yang independen |
| 2 | `kode/02_agregasi.py` | Hubungan "memiliki" — bagian bisa eksis sendiri |
| 3 | `kode/03_komposisi.py` | Hubungan "terdiri dari" — bagian bergantung pada induk |
| 4 | `kode/latihan.py` | Soal latihan mandiri — kerjakan setelah memahami materi |

---

## Cara Menjalankan Kode

```bash
cd Materi_05_Hubungan_Kelas_dan_UML/kode

python 01_asosiasi.py
python 02_agregasi.py
python 03_komposisi.py
python latihan.py
```

---

## Kata Kunci Penting

| Istilah | Arti |
|---------|------|
| Asosiasi | Objek A "menggunakan" objek B sebagai parameter atau lokal variabel |
| Agregasi | Objek A "memiliki" objek B, tapi B bisa berdiri sendiri (has-a lemah) |
| Komposisi | Objek A "terdiri dari" objek B, B dibuat dan dihancurkan bersama A (has-a kuat) |
| UML | Unified Modeling Language — bahasa visual standar untuk desain OOP |
| Diagram Kelas | Representasi UML yang menunjukkan kelas, atribut, method, dan hubungannya |
| `---->` | Notasi asosiasi di UML |
| `o----` | Notasi agregasi (diamond kosong) di UML |
| `*----` | Notasi komposisi (diamond terisi) di UML |

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 06, pastikan Anda bisa:
- [ ] Menjelaskan perbedaan Asosiasi, Agregasi, dan Komposisi dengan kata-kata sendiri
- [ ] Menyebutkan contoh nyata dari masing-masing jenis hubungan
- [ ] Mengimplementasikan ketiga jenis hubungan dalam kode Python
- [ ] Membaca diagram kelas UML sederhana
- [ ] Menyelesaikan minimal Soal 1 dan 2 di `latihan.py`

---

## Navigasi

[<- Materi 04](../Materi_04_Enkapsulasi/) | [Beranda](../README.md) | [Materi 06 ->](../Materi_06_Pewarisan/)
