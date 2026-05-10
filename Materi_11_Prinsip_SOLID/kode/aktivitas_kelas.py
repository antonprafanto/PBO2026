"""
============================================================
  AKTIVITAS KELAS - Materi 11: Prinsip SOLID
  Waktu     : 20 menit
  Kelompok  : 2-3 orang
  File      : aktivitas_kelas.py
============================================================

SKENARIO
--------
Anda diminta mereview kode backend dari aplikasi kampus sederhana.
Kode di bawah ini BEKERJA dengan benar, tapi desainnya buruk karena
melanggar beberapa prinsip SOLID.

TUGAS KELOMPOK (3 langkah)
---------------------------
  LANGKAH 1 - IDENTIFIKASI (5 menit)
    Baca kelas SistemNilaiKampus di bawah, lalu jawab:
    a) Prinsip SOLID mana saja yang dilanggar? Sebutkan minimal 2.
    b) Tulis jawaban sebagai komentar di bagian JAWABAN LANGKAH 1.

  LANGKAH 2 - REFACTOR (12 menit)
    Pecah SistemNilaiKampus menjadi kelas-kelas yang lebih baik.
    Tulis kode refactor Anda di bagian JAWABAN LANGKAH 2.
    Pastikan semua pengujian di bagian VERIFIKASI lulus ([OK]).

  LANGKAH 3 - SIAPKAN 1 KALIMAT (3 menit)
    Siapkan 1 kalimat untuk dipresentasikan:
    "Kami memisahkan [X] karena [alasan SOLID]."

------------------------------------------------------------
"""

from abc import ABC, abstractmethod

# ============================================================
# KODE "JELEK" - Jangan diubah, jadikan acuan saja
# ============================================================

class SistemNilaiKampus:
    """
    Sistem penilaian mahasiswa.
    Kode ini bekerja, tapi ada yang salah dari sisi desain!
    """

    def __init__(self):
        self.data_nilai = {}   # { nim: { matkul: nilai } }

    # --- Tanggung jawab 1: Simpan nilai ---
    def simpan_nilai(self, nim, matkul, nilai):
        if nim not in self.data_nilai:
            self.data_nilai[nim] = {}
        self.data_nilai[nim][matkul] = nilai

    # --- Tanggung jawab 2: Hitung statistik ---
    def hitung_ipk(self, nim):
        nilai_list = list(self.data_nilai.get(nim, {}).values())
        if not nilai_list:
            return 0.0
        return sum(nilai_list) / len(nilai_list) / 25   # skala 0-100 ke 0-4

    # --- Tanggung jawab 3: Kirim notifikasi ---
    def kirim_notifikasi(self, nim, pesan, via):
        if via == "email":
            print(f"  [Email] Ke {nim}@student.unmul.ac.id : {pesan}")
        elif via == "sms":
            print(f"  [SMS]   Ke 0812-xxxx ({nim}) : {pesan}")
        elif via == "whatsapp":
            print(f"  [WA]    Ke 0812-xxxx ({nim}) : {pesan}")
        # Kalau mau tambah telegram, LINE, dll → harus ubah method ini!

    # --- Tanggung jawab 4: Cetak laporan ---
    def cetak_laporan(self, nim, format_file):
        ipk = self.hitung_ipk(nim)
        if format_file == "pdf":
            print(f"  [PDF] Laporan {nim} | IPK: {ipk:.2f}")
        elif format_file == "excel":
            print(f"  [XLS] Laporan {nim} | IPK: {ipk:.2f}")
        # Kalau mau tambah format CSV, Word, dll → harus ubah method ini!


# ============================================================
# JAWABAN LANGKAH 1 - Tulis identifikasi pelanggaran SOLID
# ============================================================

# a) Prinsip yang dilanggar:
#    1. ...  (prinsip apa?) → karena ...
#    2. ...  (prinsip apa?) → karena ...
#    3. (opsional) ...

# ============================================================
# JAWABAN LANGKAH 2 - Tulis kode refactor di sini
# ============================================================

# Petunjuk: Anda boleh membuat kelas sebanyak yang diperlukan.
# PENTING: Gunakan nama kelas persis seperti yang dipakai di bagian
# VERIFIKASI di bawah (RepoNilai, HitungIPK, NotifikasiEmail, NotifikasiSMS)
# agar pengujian otomatis bisa berjalan.

# --- Tulis kelas-kelas baru di sini ---




# ============================================================
# VERIFIKASI - Jalankan file ini, semua baris harus [OK]
# ============================================================
print("=" * 50)
print("VERIFIKASI AKTIVITAS KELAS - SOLID")
print("=" * 50)

# Cek 1: Ada kelas terpisah untuk menyimpan/mengambil nilai
try:
    repo = RepoNilai()
    repo.simpan("2301001", "RPL", 85)
    repo.simpan("2301001", "PBO", 90)
    nilai = repo.ambil("2301001")
    assert isinstance(nilai, dict)
    assert nilai.get("RPL") == 85
    print("[OK] RepoNilai: simpan dan ambil nilai berfungsi")
except NameError:
    print("[--] RepoNilai belum dibuat")
except Exception as e:
    print(f"[X]  RepoNilai: {e}")

# Cek 2: Ada kelas terpisah untuk hitung IPK
try:
    hitung = HitungIPK()
    ipk = hitung.dari_nilai({"RPL": 85, "PBO": 90})
    assert 3.4 <= ipk <= 3.6, f"IPK tidak sesuai: {ipk}"
    print("[OK] HitungIPK: perhitungan IPK berfungsi")
except NameError:
    print("[--] HitungIPK belum dibuat")
except Exception as e:
    print(f"[X]  HitungIPK: {e}")

# Cek 3: Ada kelas terpisah untuk notifikasi (minimal 1 channel)
try:
    notif = NotifikasiEmail()
    hasil = notif.kirim("2301001", "Nilai sudah keluar")
    assert hasil is True
    print("[OK] NotifikasiEmail: pengiriman notifikasi berfungsi")
except NameError:
    print("[--] NotifikasiEmail belum dibuat")
except Exception as e:
    print(f"[X]  NotifikasiEmail: {e}")

# Cek 4: Menambah channel notifikasi BARU tidak mengubah kelas lama
try:
    # Jika OCP diterapkan, kelas baru ini bisa dibuat tanpa ubah yang lama
    notif2 = NotifikasiSMS()
    hasil2 = notif2.kirim("2301001", "Nilai sudah keluar")
    assert hasil2 is True
    print("[OK] NotifikasiSMS: channel baru bisa ditambah tanpa ubah kelas lama")
except NameError:
    print("[--] NotifikasiSMS belum dibuat (bonus)")
except Exception as e:
    print(f"[X]  NotifikasiSMS: {e}")

print("=" * 50)
print("Selesai! Diskusikan hasilnya bersama kelompok.")
