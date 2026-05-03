# Materi 10 — Exception Handling OOP

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan konsep exception dan hierarki exception bawaan Python
2. Menggunakan `try`, `except`, `else`, dan `finally` dengan benar
3. Membuat custom exception dengan atribut kontekstual yang informatif
4. Merancang hierarki custom exception untuk suatu domain masalah
5. Menerapkan exception chaining (`raise ... from ...`) untuk debugging yang lebih baik
6. Membuat context manager menggunakan `@contextmanager` dari `contextlib`
7. Menerapkan best practices: tangkap spesifik, guard clause, jangan abaikan exception

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Hierarki Exception Python | `BaseException` -> `Exception` -> error spesifik |
| try / except / else / finally | Sintaks lengkap penanganan exception |
| `raise` dan re-raise | Melempar exception baru atau meneruskan yang ada |
| Exception chaining | `raise E from original` -- konteks debugging lengkap |
| Custom Exception | Turunan `Exception` dengan atribut kontekstual |
| Hierarki Custom Exception | Domain-specific exception tree |
| `@contextmanager` | Cara ringkas membuat context manager |
| `contextlib.suppress` | Abaikan exception tertentu secara elegan |
| Best Practices | Guard clause, logging, jangan `except: pass` |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_exception_dasar.py` | try/except/else/finally, raise, re-raise, exception chaining |
| `kode/02_custom_exception.py` | Custom exception, hierarki, atribut kontekstual, contextlib |
| `kode/03_studi_kasus.py` | Sistem Pendaftaran KRS & Sistem Nilai dengan exception lengkap |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) — pahami konsep exception, hierarki, dan best practices
2. Jalankan `01_exception_dasar.py` — amati alur try/except dan exception chaining
3. Jalankan `02_custom_exception.py` — lihat custom exception dan context manager beraksi
4. Jalankan `03_studi_kasus.py` — pelajari dua sistem nyata dengan exception handling lengkap
5. Kerjakan `latihan.py` — uji pemahaman Anda secara mandiri

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 11, pastikan Anda bisa menjawab:

- [ ] Kapan blok `else` dijalankan vs blok `except`?
- [ ] Mengapa `finally` lebih andal daripada menutup resource di luar blok `try`?
- [ ] Apa perbedaan `raise` (tanpa argumen) dan `raise E(...)` (dengan argumen)?
- [ ] Mengapa custom exception harus turunan `Exception`, bukan `BaseException`?
- [ ] Apa keuntungan menyimpan atribut (`self.nim`, `self.jumlah`) di custom exception?
- [ ] Kapan menggunakan `raise E from original` (exception chaining)?
