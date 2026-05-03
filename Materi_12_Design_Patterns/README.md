# Materi 12 -- Pola Desain (Design Patterns)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Memahami apa itu design patterns dan mengapa penting
2. Menerapkan Singleton Pattern untuk single-instance resources
3. Menerapkan Factory Pattern untuk flexible object creation
4. Menerapkan Observer Pattern untuk event-driven systems
5. Menerapkan Decorator Pattern untuk dynamic behavior composition
6. Mengenali kapan menggunakan pattern mana
7. Menghindari anti-patterns dalam design

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Singleton Pattern | Hanya satu instance di seluruh aplikasi (logger, config, DB) |
| Factory Pattern | Centralize object creation logic, decouple dari usage |
| Observer Pattern | Event-driven, loosely coupled communication antara objects |
| Decorator Pattern | Add behavior dynamis tanpa inheritance explosion |
| Anti-Patterns | God Object, Leaky Abstraction, Diamond Dependency |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_singleton_factory.py` | Singleton & Factory patterns dengan contoh akademik |
| `kode/02_observer.py` | Observer pattern untuk sistem notifikasi |
| `kode/03_decorator.py` | Decorator pattern untuk flexible composition |
| `kode/04_studi_kasus.py` | Sistem akademik kompleks dengan multiple patterns |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) -- pahami konsep setiap pattern dan kapan menggunakan
2. Jalankan `01_singleton_factory.py` -- lihat Singleton & Factory beraksi
3. Jalankan `02_observer.py` -- pelajari event-driven dengan Observer
4. Jalankan `03_decorator.py` -- pahami flexible composition dengan Decorator
5. Jalankan `04_studi_kasus.py` -- lihat patterns integrated dalam sistem kompleks
6. Kerjakan `latihan.py` -- implementasikan patterns di domain baru

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 13, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan Singleton vs Factory? Kapan gunakan masing-masing?
- [ ] Bagaimana Observer Pattern mengurangi coupling? Contoh di dunia real?
- [ ] Mengapa Decorator lebih baik daripada inheritance explosion?
- [ ] Apa problem dengan God Object? Bagaimana refactor?
- [ ] Berikan contoh pattern yang sudah Anda lihat di code/framework favorit?
- [ ] Apakah semua code perlu pattern? Ada kapan skip-nya?
- [ ] Bagaimana testing code dengan patterns? Lebih mudah atau lebih sulit?
