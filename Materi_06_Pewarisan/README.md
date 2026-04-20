# Materi 06 — Pewarisan (Inheritance)

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan konsep pewarisan dan manfaatnya dalam OOP
2. Mengimplementasikan single, multilevel, dan multiple inheritance di Python
3. Menggunakan `super()` untuk memanggil konstruktor dan method kelas induk
4. Melakukan method overriding untuk menyesuaikan perilaku kelas anak
5. Memahami konsep Mixin sebagai pewarisan modular
6. Menggunakan `isinstance()` dan `issubclass()` secara tepat
7. Membedakan kapan menggunakan pewarisan vs komposisi

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Sintaks dasar | `class Anak(Induk):` |
| `super()` | Akses konstruktor/method kelas induk |
| Method overriding | Mendefinisikan ulang method milik induk |
| Single inheritance | Satu anak, satu induk |
| Multilevel inheritance | Rantai hierarki (A → B → C) |
| Multiple inheritance | Satu anak, dua atau lebih induk |
| Mixin | Kelas tambahan untuk fitur modular |
| MRO | Urutan pencarian method (`__mro__`) |
| `isinstance()` | Cek apakah objek adalah instance suatu kelas |
| `issubclass()` | Cek apakah kelas merupakan subclass dari kelas lain |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_pewarisan_dasar.py` | Sintaks dasar, `super()`, dan method overriding |
| `kode/02_pola_pewarisan.py` | Multilevel, Multiple inheritance, MRO, dan Mixin |
| `kode/03_studi_kasus.py` | Sistem Akademik dan Sistem Kendaraan lengkap |
| `kode/latihan.py` | Soal latihan mandiri |

---

*➡️ [Buka materi.md](./materi.md) untuk penjelasan lengkap*
