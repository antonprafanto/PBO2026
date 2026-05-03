# Materi 09 — Magic Methods (Metode Ajaib)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan konsep magic methods (dunder methods) dan perannya dalam Python Data Model
2. Mengimplementasikan `__str__` dan `__repr__` untuk representasi objek yang informatif
3. Menggunakan `__len__`, `__bool__`, dan `__abs__` untuk perilaku numerik kustom
4. Membuat operator aritmatika kustom dengan `__add__`, `__sub__`, `__mul__`, dll.
5. Menerapkan operator perbandingan dengan `__eq__`, `__lt__`, dan `@total_ordering`
6. Membuat kelas yang berperilaku seperti container dengan `__getitem__`, `__iter__`, `__contains__`
7. Mengimplementasikan context manager dengan `__enter__` dan `__exit__`

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| `__str__` vs `__repr__` | Representasi string untuk pengguna vs developer |
| `__len__`, `__bool__`, `__abs__` | Magic methods numerik |
| Operator Aritmatika | `__add__`, `__sub__`, `__mul__`, `__truediv__`, dll. |
| Reflected Operators | `__radd__`, `__rmul__` — sisi kanan ekspresi |
| Operator Perbandingan | `__eq__`, `__lt__` + `@total_ordering` |
| `__hash__` | Hubungan dengan `__eq__` dan penggunaan di set/dict |
| Container Protocol | `__getitem__`, `__setitem__`, `__iter__`, `__contains__` |
| Context Manager | `__enter__`, `__exit__` untuk penggunaan `with` |
| `__call__` | Objek callable seperti fungsi |
| `__format__` | Format string kustom dalam f-string |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_magic_methods_dasar.py` | `__str__`, `__repr__`, `__len__`, `__bool__`, `__iter__`, `__call__` |
| `kode/02_operator_overloading.py` | Operator aritmatika, perbandingan, container, context manager |
| `kode/03_studi_kasus.py` | Sistem Nilai Akademik & Sistem Jadwal Kuliah |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) — pahami konsep magic methods dan Python Data Model
2. Jalankan `01_magic_methods_dasar.py` — amati bagaimana `print()`, `len()`, dan `for` bekerja pada objek kustom
3. Jalankan `02_operator_overloading.py` — lihat operator `+`, `>`, `in`, dan `with` pada objek buatan sendiri
4. Jalankan `03_studi_kasus.py` — pelajari dua sistem nyata yang memanfaatkan magic methods secara menyeluruh
5. Kerjakan `latihan.py` — uji pemahaman Anda secara mandiri

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 10, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan `__str__` dan `__repr__`? Kapan masing-masing dipanggil?
- [ ] Mengapa mendefinisikan `__eq__` menyebabkan `__hash__` menjadi `None`?
- [ ] Apa itu reflected operator (`__radd__`)? Kapan dipanggil?
- [ ] Bagaimana `@total_ordering` membantu menghemat penulisan kode?
- [ ] Apa yang harus dikembalikan `__exit__` agar exception tidak ditekan?
- [ ] Mengapa `__call__` berguna dibandingkan sekadar membuat fungsi biasa?
