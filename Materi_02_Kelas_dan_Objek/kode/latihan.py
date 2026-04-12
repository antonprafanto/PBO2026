"""
==========================================================
    MATERI 02 — Kelas dan Objek
    File: latihan.py
    Topik: Soal Latihan Mandiri
==========================================================

📝 PETUNJUK PENGERJAAN:
    1. Baca soal dengan seksama
    2. Hapus tulisan 'pass' dan tulis jawaban Anda di bawahnya
    3. AKTIFKAN kode uji: hapus tanda '#' di depan baris uji
    4. Jalankan: python latihan.py
    5. Bandingkan output dengan "Contoh output yang diharapkan"

💡 TIPS:
    - Kerjakan soal satu per satu, jangan langsung semua
    - Jika error, baca pesan error dengan teliti
    - Gunakan print() untuk debug nilai variabel Anda
==========================================================
"""

print("=" * 58)
print("         LATIHAN MANDIRI — MATERI 02")
print("=" * 58)


# ══════════════════════════════════════════════════════════
# SOAL 1 (Mudah) ⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 1: Kelas Lingkaran")
print("-" * 50)
print("""
Buatlah kelas 'Lingkaran' dengan:

Atribut (di __init__):
  - jari_jari (float) → jari-jari lingkaran

Method:
  - luas()
      Rumus: π × r²
      Kembalikan (return) hasilnya sebagai float

  - keliling()
      Rumus: 2 × π × r
      Kembalikan (return) hasilnya sebagai float

  - info()
      Tampilkan jari-jari, luas, dan keliling
      dengan format 2 angka desimal

Gunakan: import math  lalu gunakan math.pi (bukan 3.14)

Contoh output yang diharapkan:
  ================================
  Lingkaran
  Jari-jari : 7
  Luas      : 153.94
  Keliling  : 43.98
  ================================
""")

import math   # math.pi = 3.141592653589793

# ── Tulis jawaban Anda di sini ───────────────────────────
class Lingkaran:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus '#' berikut untuk menguji jawaban Anda ─────────
# print("  [Uji Soal 1]")
# l1 = Lingkaran(7)
# l1.info()
# l2 = Lingkaran(3.5)
# l2.info()


# ══════════════════════════════════════════════════════════
# SOAL 2 (Sedang) ⭐⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 2: Kelas Keranjang Belanja")
print("-" * 50)
print("""
Buatlah kelas 'KeranjangBelanja' dengan:

Atribut (di __init__):
  - nama_pembeli (str) → nama pembeli
  - items (list)       → daftar item, default = [] kosong
    PENTING: gunakan None sebagai default, lalu di dalam
    __init__ isi dengan: self.items = items if items else []

Method:
  - tambah_item(nama, harga, qty)
      Tambahkan dict {'nama': ..., 'harga': ..., 'qty': ...}
      ke dalam self.items

  - hapus_item(nama)
      Hapus item yang namanya cocok dari self.items
      Jika tidak ditemukan, tampilkan pesan

  - total_harga()
      Hitung dan kembalikan total = sum(harga × qty)

  - tampilkan_keranjang()
      Tampilkan daftar item dan total harga

Contoh output yang diharapkan:
  =========================================
  Keranjang Belanja: Budi
  -----------------------------------------
  1. Laptop           x1  → Rp  8,500,000
  2. Mouse            x2  → Rp    300,000
  -----------------------------------------
  TOTAL                   → Rp  8,800,000
  =========================================
""")

# ── Tulis jawaban Anda di sini ───────────────────────────
class KeranjangBelanja:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus '#' berikut untuk menguji jawaban Anda ─────────
# print("  [Uji Soal 2]")
# keranjang = KeranjangBelanja("Budi")
# keranjang.tambah_item("Laptop", 8_500_000, 1)
# keranjang.tambah_item("Mouse", 150_000, 2)
# keranjang.tambah_item("Keyboard", 350_000, 1)
# keranjang.tampilkan_keranjang()
# print()
# keranjang.hapus_item("Mouse")
# keranjang.tampilkan_keranjang()


# ══════════════════════════════════════════════════════════
# SOAL 3 (Menantang) ⭐⭐⭐
# ══════════════════════════════════════════════════════════
print("\n📝 SOAL 3: Sistem Antrian Bimbingan Skripsi")
print("-" * 50)
print("""
Buatlah kelas 'AntrianBimbingan' dengan:

Atribut (di __init__):
  - nama_dosen (str)  → nama dosen pembimbing
  - antrian    (list) → daftar nama mahasiswa, default kosong

Method:
  - daftar(nama_mahasiswa)
      Tambahkan nama ke antrian
      Tampilkan: "[nama] mendaftar. Posisi antrian: [nomor]"

  - panggil_berikutnya()
      Keluarkan mahasiswa PERTAMA dari antrian (FIFO)
      Tampilkan: "Memanggil: [nama]"
      Jika antrian kosong: tampilkan pesan sesuai

  - lihat_antrian()
      Tampilkan semua nama dalam antrian beserta nomornya
      Jika kosong: tampilkan "Antrian kosong"

  - sisa_antrian()
      Kembalikan (return) jumlah orang yang masih mengantri

Contoh output yang diharapkan:
  [Andi] mendaftar. Posisi antrian: 1
  [Budi] mendaftar. Posisi antrian: 2
  [Citra] mendaftar. Posisi antrian: 3
  [Dono] mendaftar. Posisi antrian: 4
  
  Antrian bimbingan Dr. Anton:
    1. Andi
    2. Budi
    3. Citra
    4. Dono
  
  Memanggil: Andi
  Memanggil: Budi
  
  Sisa antrian (2 orang):
    1. Citra
    2. Dono

🏆 BONUS: Tambahkan method batalkan(nama_mahasiswa) yang
   memungkinkan mahasiswa membatalkan antriannya!
""")

# ── Tulis jawaban Anda di sini ───────────────────────────
class AntrianBimbingan:
    pass  # ← Hapus 'pass', tulis jawaban Anda


# ── Hapus '#' berikut untuk menguji jawaban Anda ─────────
# print("  [Uji Soal 3]")
# antrian = AntrianBimbingan("Dr. Anton Prafanto")
# antrian.daftar("Andi Rahman")
# antrian.daftar("Budi Santoso")
# antrian.daftar("Citra Dewi")
# antrian.daftar("Dono Prasetyo")
# print()
# antrian.lihat_antrian()
# print()
# antrian.panggil_berikutnya()
# antrian.panggil_berikutnya()
# print()
# antrian.lihat_antrian()
# print(f"  Sisa: {antrian.sisa_antrian()} orang")


# ══════════════════════════════════════════════════════════
print()
print("=" * 58)
print("  🎯 Selamat mengerjakan! Semangat! 💪")
print("  📌 Ingat: Error adalah bagian dari proses belajar!")
print("=" * 58)
