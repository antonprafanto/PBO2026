"""
Kode Praktik - Materi 07: Polimorfisme (Polymorphism)
File: 03_studi_kasus.py
Topik: Dua skenario nyata — Sistem Penilaian Akademik & Sistem Notifikasi

Jalankan: python 03_studi_kasus.py
"""

from abc import ABC, abstractmethod

# ======================================================================
# SKENARIO 1: Sistem Penilaian Akademik
#
# Masalah: Ada banyak jenis komponen nilai (tugas, ujian, proyek,
# kuis). Setiap komponen dihitung berbeda tapi semuanya harus bisa
# digabungkan menjadi satu nilai akhir.
#
# Solusi Polimorfisme:
#   - KomponenNilai (ABC) mendefinisikan kontrak hitung_nilai()
#   - NilaiTugas, NilaiUjian, NilaiProyek, NilaiKuis mengimplementasikannya
#   - LembarNilai mengumpulkan semua komponen — tidak perlu tahu jenisnya
# ======================================================================
print("=" * 65)
print("SKENARIO 1: Sistem Penilaian Akademik")
print("=" * 65)


class KomponenNilai(ABC):
    """ABC — dasar semua komponen penilaian mata kuliah."""

    def __init__(self, nama, bobot):
        if not (0 < bobot <= 100):
            raise ValueError(f"Bobot harus 1-100, dapat: {bobot}")
        self.nama  = nama
        self.bobot = bobot

    @abstractmethod
    def hitung_nilai(self):
        """Kembalikan nilai komponen ini dalam skala 0-100."""
        pass

    def nilai_terbobot(self):
        return self.hitung_nilai() * (self.bobot / 100)

    def ringkasan(self):
        return (f"  {self.nama:<22} | Bobot: {self.bobot:>3}% | "
                f"Nilai: {self.hitung_nilai():>6.2f} | "
                f"Terbobot: {self.nilai_terbobot():>6.2f}")

    def __str__(self):
        return f"{self.nama} ({self.bobot}%): {self.hitung_nilai():.2f}"


class NilaiTugas(KomponenNilai):
    """Nilai rata-rata dari beberapa tugas yang dikumpulkan."""

    def __init__(self, nama, bobot, daftar_nilai):
        super().__init__(nama, bobot)
        if not daftar_nilai:
            raise ValueError("Daftar nilai tidak boleh kosong.")
        self._nilai = [float(n) for n in daftar_nilai]

    def hitung_nilai(self):
        return sum(self._nilai) / len(self._nilai)

    def detail(self):
        rata = self.hitung_nilai()
        print(f"    {self.nama}: {self._nilai} -> rata-rata {rata:.2f}")


class NilaiUjian(KomponenNilai):
    """Nilai ujian berdasarkan jumlah soal benar dari total soal."""

    def __init__(self, nama, bobot, jumlah_benar, total_soal):
        super().__init__(nama, bobot)
        if total_soal <= 0:
            raise ValueError("Total soal harus > 0.")
        self._benar = jumlah_benar
        self._total = total_soal

    def hitung_nilai(self):
        return (self._benar / self._total) * 100

    def detail(self):
        print(f"    {self.nama}: {self._benar}/{self._total} soal benar "
              f"= {self.hitung_nilai():.2f}")


class NilaiProyek(KomponenNilai):
    """Nilai proyek akhir dengan tiga aspek penilaian berbobot."""

    def __init__(self, nama, bobot, nilai_teknis, nilai_presentasi,
                 nilai_dokumentasi):
        super().__init__(nama, bobot)
        self._teknis       = nilai_teknis
        self._presentasi   = nilai_presentasi
        self._dokumentasi  = nilai_dokumentasi

    def hitung_nilai(self):
        return (self._teknis       * 0.50 +
                self._presentasi   * 0.30 +
                self._dokumentasi  * 0.20)

    def detail(self):
        print(f"    {self.nama}: teknis={self._teknis} "
              f"presentasi={self._presentasi} "
              f"dok={self._dokumentasi} "
              f"-> {self.hitung_nilai():.2f}")


class NilaiKuis(KomponenNilai):
    """Nilai kuis — ambil n nilai terbaik dari semua kuis."""

    def __init__(self, nama, bobot, daftar_nilai, ambil_terbaik=None):
        super().__init__(nama, bobot)
        self._nilai       = [float(n) for n in daftar_nilai]
        self._ambil       = ambil_terbaik or len(daftar_nilai)

    def hitung_nilai(self):
        terbaik = sorted(self._nilai, reverse=True)[:self._ambil]
        return sum(terbaik) / len(terbaik)

    def detail(self):
        terbaik = sorted(self._nilai, reverse=True)[:self._ambil]
        print(f"    {self.nama}: semua={self._nilai}, "
              f"ambil {self._ambil} terbaik={terbaik} "
              f"-> {self.hitung_nilai():.2f}")


class LembarNilai:
    """Mengumpulkan komponen nilai dan menghitung nilai akhir mahasiswa."""

    _PREDIKAT = [
        (87, "A",  4.00), (82, "A-", 3.75), (78, "B+", 3.50),
        (75, "B",  3.00), (71, "B-", 2.75), (67, "C+", 2.50),
        (64, "C",  2.00), (56, "D",  1.00), (0,  "E",  0.00),
    ]

    def __init__(self, mahasiswa, nim, matkul, sks):
        self.mahasiswa  = mahasiswa
        self.nim        = nim
        self.matkul     = matkul
        self.sks        = sks
        self._komponen  = []

    def tambah(self, komponen):
        """Tambah KomponenNilai apapun — polimorfisme bekerja di sini."""
        total_bobot = sum(k.bobot for k in self._komponen) + komponen.bobot
        if total_bobot > 100:
            raise ValueError(f"Total bobot melebihi 100%: {total_bobot}%")
        self._komponen.append(komponen)
        return self

    def nilai_akhir(self):
        return sum(k.nilai_terbobot() for k in self._komponen)

    def predikat_huruf(self):
        na = self.nilai_akhir()
        for batas, huruf, _ in self._PREDIKAT:
            if na >= batas:
                return huruf
        return "E"

    def bobot_mutu(self):
        na = self.nilai_akhir()
        for batas, _, mutu in self._PREDIKAT:
            if na >= batas:
                return mutu
        return 0.0

    def mutu(self):
        return self.sks * self.bobot_mutu()

    def cetak(self, tampilkan_detail=False):
        garis = "=" * 65
        print(f"\n  {garis}")
        print(f"  Mahasiswa : {self.mahasiswa} ({self.nim})")
        print(f"  Mata Kuliah: {self.matkul} ({self.sks} SKS)")
        print(f"  {'-' * 63}")
        if tampilkan_detail:
            print("  Detail Komponen:")
            for k in self._komponen:
                k.detail()
            print(f"  {'-' * 63}")
        print(f"  {'Komponen':<22}   {'Bobot':>5}   {'Nilai':>6}   "
              f"{'Terbobot':>8}")
        print(f"  {'-' * 63}")
        for k in self._komponen:
            print(k.ringkasan())
        print(f"  {'-' * 63}")
        na = self.nilai_akhir()
        print(f"  {'Nilai Akhir':<22}           {na:>6.2f}")
        print(f"  Predikat   : {self.predikat_huruf()}")
        print(f"  Bobot Mutu : {self.bobot_mutu():.2f}")
        print(f"  Mutu       : {self.mutu():.2f} (= {self.sks} SKS x "
              f"{self.bobot_mutu():.2f})")
        print(f"  {garis}")


# --- Demo Skenario 1 ---

# Mahasiswa 1 — nilai lengkap
lembar1 = LembarNilai("Budi Santoso", "2301001", "Pemrograman Berorientasi Objek", 3)
lembar1.tambah(NilaiKuis("Kuis",        15, [70, 85, 90, 65, 80], ambil_terbaik=4))
lembar1.tambah(NilaiTugas("Tugas Harian", 20, [85, 90, 78, 92, 88]))
lembar1.tambah(NilaiUjian("UTS",          25, 38, 50))
lembar1.tambah(NilaiProyek("Proyek Akhir",20, 88, 82, 90))
lembar1.tambah(NilaiUjian("UAS",          20, 44, 50))
lembar1.cetak(tampilkan_detail=True)

# Mahasiswa 2 — skenario nilai kurang
lembar2 = LembarNilai("Rudi Hartono", "2301003", "Pemrograman Berorientasi Objek", 3)
lembar2.tambah(NilaiKuis("Kuis",        15, [55, 60, 45, 70, 50], ambil_terbaik=4))
lembar2.tambah(NilaiTugas("Tugas Harian", 20, [70, 65, 60, 72, 68]))
lembar2.tambah(NilaiUjian("UTS",          25, 28, 50))
lembar2.tambah(NilaiProyek("Proyek Akhir",20, 72, 68, 75))
lembar2.tambah(NilaiUjian("UAS",          20, 32, 50))
lembar2.cetak()

# Rekap kelas
print("\n  REKAP NILAI KELAS:")
print(f"  {'Mahasiswa':<22} {'NA':>6}  {'Huruf':>6}  {'SKS':>4}  {'Mutu':>6}")
print("  " + "-" * 55)
for lembar in [lembar1, lembar2]:
    print(f"  {lembar.mahasiswa:<22} {lembar.nilai_akhir():>6.2f}  "
          f"{lembar.predikat_huruf():>6}  {lembar.sks:>4}  "
          f"{lembar.mutu():>6.2f}")


# ======================================================================
# SKENARIO 2: Sistem Notifikasi Multi-Kanal
#
# Masalah: Aplikasi akademik harus bisa mengirim notifikasi lewat
# berbagai kanal (email, SMS, push notification, webhook).
# Setiap kanal berbeda implementasinya tapi punya perilaku yang sama.
#
# Solusi Polimorfisme:
#   - KanalNotifikasi (ABC) — kontrak wajib kirim()
#   - Email, SMS, Push, Webhook mengimplementasikan kirim()
#   - ManajerNotifikasi mengirim ke semua kanal — tidak perlu tahu jenisnya
# ======================================================================
print("\n\n" + "=" * 65)
print("SKENARIO 2: Sistem Notifikasi Multi-Kanal")
print("=" * 65)


class KanalNotifikasi(ABC):
    """ABC — dasar semua kanal pengiriman notifikasi."""

    def __init__(self, nama_kanal):
        self.nama_kanal = nama_kanal
        self._terkirim  = 0
        self._gagal     = 0

    @abstractmethod
    def kirim(self, penerima, subjek, pesan):
        """Kirim notifikasi. Return True jika berhasil."""
        pass

    @property
    def statistik(self):
        total = self._terkirim + self._gagal
        persen = (self._terkirim / total * 100) if total > 0 else 0
        return f"{self.nama_kanal}: {self._terkirim}/{total} berhasil ({persen:.0f}%)"

    def __str__(self):
        return f"[{self.nama_kanal}]"


class KanalEmail(KanalNotifikasi):
    def __init__(self, smtp_server, pengirim):
        super().__init__("Email")
        self.smtp    = smtp_server
        self.pengirim = pengirim

    def kirim(self, penerima, subjek, pesan):
        if "@" not in penerima:
            print(f"  {self} Gagal: '{penerima}' bukan alamat email valid.")
            self._gagal += 1
            return False
        print(f"  {self} [{self.smtp}]")
        print(f"    Dari    : {self.pengirim}")
        print(f"    Kepada  : {penerima}")
        print(f"    Subjek  : {subjek}")
        print(f"    Pesan   : {pesan[:60]}{'...' if len(pesan) > 60 else ''}")
        self._terkirim += 1
        return True


class KanalSMS(KanalNotifikasi):
    def __init__(self, provider, nomor_pengirim):
        super().__init__("SMS")
        self.provider        = provider
        self.nomor_pengirim  = nomor_pengirim
        self._max_karakter   = 160

    def kirim(self, penerima, subjek, pesan):
        if not penerima.startswith("08") and not penerima.startswith("+62"):
            print(f"  {self} Gagal: '{penerima}' bukan nomor HP valid.")
            self._gagal += 1
            return False
        pesan_sms = f"[{subjek}] {pesan}"
        if len(pesan_sms) > self._max_karakter:
            pesan_sms = pesan_sms[:self._max_karakter - 3] + "..."
        print(f"  {self} [{self.provider}]")
        print(f"    Ke      : {penerima}")
        print(f"    Pesan   : {pesan_sms}")
        print(f"    ({len(pesan_sms)}/{self._max_karakter} karakter)")
        self._terkirim += 1
        return True


class KanalPushNotification(KanalNotifikasi):
    def __init__(self, app_id):
        super().__init__("Push Notif")
        self.app_id = app_id

    def kirim(self, penerima, subjek, pesan):
        print(f"  {self} [App: {self.app_id}]")
        print(f"    Device  : {penerima}")
        print(f"    Judul   : {subjek}")
        print(f"    Isi     : {pesan[:80]}{'...' if len(pesan) > 80 else ''}")
        self._terkirim += 1
        return True


class KanalWebhook(KanalNotifikasi):
    """Kirim notifikasi ke URL webhook (misal: Slack, Teams, Discord)."""

    def __init__(self, url, platform="Webhook"):
        super().__init__(platform)
        self.url = url

    def kirim(self, penerima, subjek, pesan):
        payload = {"channel": penerima, "title": subjek, "text": pesan}
        print(f"  {self} [{self.url}]")
        print(f"    Payload : {payload}")
        self._terkirim += 1
        return True


class ManajerNotifikasi:
    """Mengelola dan mendistribusikan notifikasi ke berbagai kanal."""

    def __init__(self, nama_sistem):
        self.nama_sistem = nama_sistem
        self._kanal      = []

    def daftarkan_kanal(self, kanal):
        self._kanal.append(kanal)
        return self

    def kirim_ke_semua(self, penerima_per_kanal, subjek, pesan):
        """
        penerima_per_kanal: dict {NamaKanal: alamat_penerima}
        Polimorfisme: kanal.kirim() dipanggil — Python tahu implementasi mana.
        """
        print(f"\n  [NOTIF] {self.nama_sistem}")
        print(f"  Subjek: {subjek}")
        print("  " + "-" * 50)
        berhasil = 0
        for kanal in self._kanal:
            penerima = penerima_per_kanal.get(kanal.nama_kanal)
            if penerima:
                if kanal.kirim(penerima, subjek, pesan):
                    berhasil += 1
        print(f"  [Hasil] {berhasil}/{len(self._kanal)} kanal berhasil.")

    def laporan_statistik(self):
        print(f"\n  Statistik Pengiriman — {self.nama_sistem}:")
        for kanal in self._kanal:
            print(f"    {kanal.statistik}")


# --- Demo Skenario 2 ---
manajer = ManajerNotifikasi("SIAKAD UNMUL")
manajer.daftarkan_kanal(KanalEmail("smtp.unmul.ac.id", "noreply@unmul.ac.id"))
manajer.daftarkan_kanal(KanalSMS("Telkomsel", "SIAKAD-UNMUL"))
manajer.daftarkan_kanal(KanalPushNotification("unmul.siakad.app"))
manajer.daftarkan_kanal(KanalWebhook("https://hooks.slack.com/xxx", "Slack"))

# Notifikasi 1: Pengumuman nilai keluar
print("\n  --- Notifikasi Nilai KRS ---")
manajer.kirim_ke_semua(
    penerima_per_kanal={
        "Email":      "budi@unmul.ac.id",
        "SMS":        "081234567890",
        "Push Notif": "device-token-budi-abc123",
        "Slack":      "#pengumuman-akademik",
    },
    subjek="Nilai PBO Telah Keluar",
    pesan=("Yth. Budi Santoso, nilai mata kuliah Pemrograman Berorientasi "
           "Objek Semester Genap 2024/2025 telah dipublikasikan. "
           "Silakan cek SIAKAD untuk detail nilai Anda."),
)

# Notifikasi 2: Pengingat batas KRS (beberapa kanal saja)
print("\n  --- Notifikasi Batas KRS ---")
manajer.kirim_ke_semua(
    penerima_per_kanal={
        "Email":      "nomor-salah-bukan-email",   # sengaja salah
        "SMS":        "08199887766",
        "Push Notif": "device-token-budi-abc123",
    },
    subjek="Pengingat: Batas Pengisian KRS 3 Hari Lagi",
    pesan="Segera lengkapi KRS Anda sebelum tanggal 20 Februari 2025.",
)

manajer.laporan_statistik()

print()
