# Materi 08 — Abstraksi (Abstraction)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan konsep abstraksi sebagai salah satu pilar OOP dan membedakannya dari enkapsulasi
2. Membuat kelas abstrak menggunakan `ABC` dan `@abstractmethod` dari modul `abc`
3. Mendefinisikan abstract property menggunakan kombinasi `@property` dan `@abstractmethod`
4. Menerapkan **Template Method Pattern** — kelas abstrak yang mendefinisikan kerangka algoritma
5. Mengimplementasikan multiple abstract interface pada satu kelas
6. Membangun hierarki kelas abstrak bertingkat
7. Memilih dengan tepat antara ABC, duck typing, dan `typing.Protocol`

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Konsep Abstraksi | Menyembunyikan detail, menampilkan antarmuka |
| Abstraksi vs Enkapsulasi | Perbedaan tujuan dan mekanisme keduanya |
| Kelas Abstrak (ABC) | `from abc import ABC, abstractmethod` |
| Abstract Property | `@property` + `@abstractmethod` |
| Template Method Pattern | Kerangka algoritma di kelas abstrak |
| Multiple Interface | Satu kelas mengimplementasikan banyak ABC |
| Hierarki Abstrak | Kelas abstrak mewarisi kelas abstrak |
| ABC vs Duck Typing vs Protocol | Panduan memilih pendekatan yang tepat |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_abstraksi_dasar.py` | Kelas abstrak, `@abstractmethod`, abstract property |
| `kode/02_abstract_property_dan_interface.py` | Template Method, multiple interface, hierarki abstrak |
| `kode/03_studi_kasus.py` | Sistem Plugin Ekspor Data Akademik & Sistem Antrian Layanan Kampus |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) — pahami abstraksi, bedakan dari enkapsulasi, dan pelajari ABC
2. Jalankan `01_abstraksi_dasar.py` — lihat cara kerja kelas abstrak dan abstract property
3. Jalankan `02_abstract_property_dan_interface.py` — eksplorasi Template Method dan multiple interface
4. Jalankan `03_studi_kasus.py` — pelajari dua sistem nyata yang memanfaatkan abstraksi
5. Kerjakan `latihan.py` — uji pemahaman Anda secara mandiri

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 09, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan antara abstraksi dan enkapsulasi?
- [ ] Mengapa kelas abstrak tidak bisa di-instansiasi langsung?
- [ ] Apa yang terjadi jika kelas anak lupa mengimplementasikan salah satu `@abstractmethod`?
- [ ] Bagaimana cara membuat abstract property di Python?
- [ ] Apa itu Template Method Pattern dan mengapa ia berguna?
- [ ] Kapan sebaiknya menggunakan ABC dibanding duck typing?
