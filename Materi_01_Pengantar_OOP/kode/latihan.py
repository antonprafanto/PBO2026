"""
==========================================================
    MATERI 01 — Pengantar OOP
    File: latihan.py
    Topik: Soal Latihan Mandiri
==========================================================

📝 PETUNJUK PENGERJAAN:
    1. Baca soal dengan seksama
    2. Hapus tulisan 'pass' dan tulis jawaban Anda
    3. AKTIFKAN kode uji dengan hapus tanda '#' di depannya
    4. Jalankan: python latihan.py
    5. Bandingkan output Anda dengan "Contoh output yang diharapkan"

🎯 TUJUAN:
    Melatih kemampuan mendefinisikan kelas, atribut, dan method

💡 TIPS:
    - Jika error, baca pesan errornya dengan teliti
    - Coba satu soal dulu, baru lanjut ke berikutnya
==========================================================
"""

print("=" * 58)
print("         LATIHAN MANDIRI — MATERI 01")
print("=" * 58)


# ══════════════════════════════════════════════════════════
# SOAL 1 (Mudah) ⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 1: Kelas Buku")
print("-" * 45)
print("""
Buatlah sebuah kelas bernama 'Buku' dengan:

Atribut (di __init__):
  - judul   (str)   → judul buku
  - penulis (str)   → nama penulis
  - harga   (int)   → harga dalam rupiah

Method:
  - info()
      Menampilkan semua atribut dengan format rapi

  - diskon(persen)
      Hitung dan tampilkan harga setelah dikurangi diskon

Contoh output yang diharapkan:
  ========================
  Judul  : Pemrograman Python OOP
  Penulis: Anton Prafanto
  Harga  : Rp 150,000
  ========================
  Diskon 20% → Harga baru: Rp 120,000
""")


# ── Tulis jawaban Anda di sini ───────────────────────────
class Buku:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus tanda '#' di bawah ini untuk menguji jawaban ──
# buku1 = Buku("Pemrograman Python OOP", "Anton Prafanto", 150000)
# print("  [Uji Soal 1]")
# buku1.info()
# buku1.diskon(20)


# ══════════════════════════════════════════════════════════
# SOAL 2 (Sedang) ⭐⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 2: Kelas Rekening Bank")
print("-" * 45)
print("""
Buatlah kelas 'RekeningBank' dengan:

Atribut (di __init__):
  - pemilik     (str)   → nama pemilik rekening
  - no_rekening (str)   → nomor rekening
  - saldo       (float) → saldo awal, default = 0

Method:
  - setor(jumlah)
      Tambah saldo sejumlah 'jumlah', tampilkan saldo baru

  - tarik(jumlah)
      Kurangi saldo jika saldo mencukupi,
      jika tidak cukup tampilkan pesan peringatan

  - cek_saldo()
      Tampilkan informasi pemilik dan saldo saat ini

Contoh output yang diharapkan:
  ✅ Setor Rp 500,000 → Saldo: Rp 500,000
  ✅ Tarik Rp 200,000 → Saldo: Rp 300,000
  💰 Rekening [BRI-001] atas nama Budi → Saldo: Rp 300,000
  ❌ Saldo tidak cukup! Saldo Anda: Rp 300,000
""")


# ── Tulis jawaban Anda di sini ───────────────────────────
class RekeningBank:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus tanda '#' di bawah ini untuk menguji jawaban ──
# rek = RekeningBank("Budi Santoso", "BRI-001")
# print("  [Uji Soal 2]")
# rek.setor(500000)
# rek.tarik(200000)
# rek.cek_saldo()
# rek.tarik(400000)


# ══════════════════════════════════════════════════════════
# SOAL 3 (Menantang) ⭐⭐⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 3: Kelas Nilai Mahasiswa")
print("-" * 45)
print("""
Buatlah kelas 'NilaiMahasiswa' dengan:

Atribut (di __init__):
  - nama        (str)   → nama mahasiswa
  - nilai_tugas (float) → nilai tugas (0-100)
  - nilai_uts   (float) → nilai UTS (0-100)
  - nilai_uas   (float) → nilai UAS (0-100)

Method:
  - hitung_nilai_akhir()
      Rumus: (tugas × 30%) + (uts × 30%) + (uas × 40%)
      Kembalikan (return) nilai akhir sebagai float

  - get_grade()
      A  → nilai akhir ≥ 85
      B  → nilai akhir ≥ 75
      C  → nilai akhir ≥ 65
      D  → nilai akhir ≥ 55
      E  → di bawah 55
      Kembalikan (return) grade sebagai string

  - tampilkan_rapor()
      Tampilkan nama, ketiga nilai, nilai akhir, dan grade

Contoh output yang diharapkan:
  ========================================
  RAPOR MAHASISWA
  Nama    : Andi Rahman
  Tugas   : 85.0
  UTS     : 80.0
  UAS     : 90.0
  ----------------------------------------
  Nilai Akhir : 85.5
  Grade       : A
  ========================================

🏆 BONUS: Buat LIST yang berisi 3 objek NilaiMahasiswa,
   lalu tampilkan rapor semuanya dalam satu for loop!
""")


# ── Tulis jawaban Anda di sini ───────────────────────────
class NilaiMahasiswa:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus tanda '#' di bawah ini untuk menguji jawaban ──
# print("  [Uji Soal 3]")
# mhs1 = NilaiMahasiswa("Andi Rahman",  85, 80, 90)
# mhs2 = NilaiMahasiswa("Budi Santoso", 70, 65, 72)
# mhs3 = NilaiMahasiswa("Citra Dewi",   90, 95, 88)

# for mhs in [mhs1, mhs2, mhs3]:
#     mhs.tampilkan_rapor()


# ══════════════════════════════════════════════════════════
print()
print("=" * 58)
print("  🎯 Selamat mengerjakan! Semangat belajar! 💪")
print("  📌 Ingat: Error adalah bagian dari proses belajar!")
print("=" * 58)
