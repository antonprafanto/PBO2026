# Materi 11 — Prinsip SOLID

## Tujuan Pembelajaran

Setelah mempelajari materi ini, mahasiswa mampu:

1. Menjelaskan lima prinsip SOLID dan mengapa penting untuk desain OOP
2. Menerapkan Single Responsibility Principle untuk pisahkan tanggung jawab
3. Menerapkan Open/Closed Principle dengan inheritance dan strategy pattern
4. Memahami Liskov Substitution Principle dan menghindari broken contracts
5. Menerapkan Interface Segregation Principle untuk interface yang focused
6. Menerapkan Dependency Inversion Principle dengan dependency injection
7. Mengenali anti-pattern dan refactor menuju kode yang SOLID

---

## Ringkasan Materi

| Topik | Deskripsi |
|-------|-----------|
| Single Responsibility Principle | Satu kelas, satu tanggung jawab → mudah test, mudah reuse |
| Open/Closed Principle | Extend tanpa modify → code lama aman, feature baru clean |
| Liskov Substitution Principle | Subclass tidak break kontrak parent → hierarchy sound |
| Interface Segregation Principle | Interface kecil dan focused → tidak ada dummy impl |
| Dependency Inversion Principle | Depend pada abstraksi, tidak konkret → flexible, testable |
| Anti-Pattern Recognition | Identifikasi dan refactor code yang melanggar SOLID |

---

## File Kode Praktik

| File | Topik |
|------|-------|
| `kode/01_srp_ocp_dasar.py` | SRP & OCP dengan contoh akademik |
| `kode/02_lsp_isp_dip.py` | LSP, ISP, DIP dengan implementasi lengkap |
| `kode/03_studi_kasus.py` | Sistem KRS yang menerapkan 5 prinsip SOLID |
| `kode/latihan.py` | Soal latihan mandiri (3 soal bertingkat) |

---

## Urutan Belajar yang Disarankan

1. Baca [materi.md](./materi.md) — pahami konsep setiap prinsip dan mengapa penting
2. Jalankan `01_srp_ocp_dasar.py` — lihat SRP & OCP beraksi dengan contoh sederhana
3. Jalankan `02_lsp_isp_dip.py` — pelajari tiga prinsip lanjutan dengan implementasi detail
4. Jalankan `03_studi_kasus.py` — lihat sistem akademik kompleks dengan SOLID diterapkan
5. Kerjakan `latihan.py` — refactor code yang melanggar SOLID menjadi SOLID-compliant

---

## Checklist Pemahaman

Sebelum lanjut ke Materi 12, pastikan Anda bisa menjawab:

- [ ] Apa perbedaan SRP dan ISP? Kapan gunakan masing-masing?
- [ ] Bagaimana menerapkan OCP dengan strategy pattern vs inheritance?
- [ ] Mengapa LSP penting? Apa yang terjadi jika dilanggar?
- [ ] Berikan contoh fat interface dan segregated interface dalam domain Anda.
- [ ] Apa manfaat dependency injection dalam testing?
- [ ] Bagaimana mendeteksi kode yang melanggar SOLID? Kapan refactor?
- [ ] Apakah SOLID selalu mutlak diterapkan? Ada exception-nya?
