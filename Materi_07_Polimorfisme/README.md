# Materi 07 — Polimorfisme (Polymorphism)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan konsep polimorfisme dan perannya sebagai pilar ketiga OOP
2. Mengimplementasikan polimorfisme via pewarisan dengan method overriding
3. Menerapkan duck typing untuk menulis kode yang fleksibel tanpa hierarki pewarisan
4. Membuat Abstract Base Class (ABC) menggunakan modul `abc`
5. Mendefinisikan operator kustom via operator overloading (`__add__`, `__eq__`, dll.)
6. Membuat kelas yang kompatibel dengan fungsi built-in Python (`len`, `sorted`, `max`)
7. Membedakan kapan menggunakan ABC vs duck typing dalam desain sistem

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Polimorfisme via Pewarisan | Method override — satu nama, banyak implementasi |
| Duck Typing | Objek apapun bisa dipakai selama punya method yang dibutuhkan |
| Abstract Base Class (ABC) | `from abc import ABC, abstractmethod` — kontrak wajib |
| Operator Overloading | `__add__`, `__sub__`, `__mul__`, `__eq__`, `__lt__`, dst. |
| Built-in Compatibility | `__len__`, `__iter__`, `__contains__`, `__getitem__` |
| `isinstance()` | Cek tipe secara polimorfis (mengenali hierarki) |
| Dynamic Dispatch | Python memilih implementasi yang tepat saat runtime |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_polimorfisme_dasar.py` | Polimorfisme via pewarisan, duck typing, ABC dasar |
| `kode/02_duck_typing_dan_abc.py` | Duck typing lanjutan, ABC formal, operator overloading, built-in |
| `kode/03_studi_kasus.py` | Sistem Penilaian Akademik & Sistem Notifikasi Multi-Kanal |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) — pahami konsep polimorfisme, duck typing, dan ABC
2. Jalankan `01_polimorfisme_dasar.py` — amati bagaimana satu perintah menghasilkan perilaku berbeda
3. Jalankan `02_duck_typing_dan_abc.py` — lihat duck typing, ABC, dan operator overloading beraksi
4. Jalankan `03_studi_kasus.py` — pelajari dua sistem nyata yang memanfaatkan polimorfisme
5. Kerjakan `latihan.py` — uji pemahaman Anda secara mandiri

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 08, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan polimorfisme via pewarisan dan duck typing?
- [ ] Kapan sebaiknya menggunakan ABC, dan kapan cukup duck typing?
- [ ] Mengapa `isinstance()` lebih tepat daripada `type()` dalam kode polimorfis?
- [ ] Apa yang terjadi jika kelas anak tidak mengimplementasikan semua `@abstractmethod`?
- [ ] Bagaimana `sorted()` dan `max()` bisa bekerja pada kelas buatan sendiri?
- [ ] Apa yang dimaksud dengan *dynamic dispatch*?

---

*Sebelumnya: [Materi 06 — Pewarisan](../Materi_06_Pewarisan/README.md)*
*Selanjutnya: [Materi 08 — Abstraksi](../Materi_08_Abstraksi/README.md)*
