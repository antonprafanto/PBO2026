"""
Latihan Mandiri - Materi 06: Pewarisan (Inheritance)
File: latihan.py

Petunjuk:
- Kerjakan setiap soal di bawah ini.
- Hapus perintah `pass` dan ganti dengan implementasi Anda.
- Jalankan file ini untuk menguji jawaban: python latihan.py
- Output yang diharapkan tersedia sebagai komentar di tiap soal.
"""

print("=" * 60)
print("LATIHAN MATERI 06 - PEWARISAN (INHERITANCE)")
print("=" * 60)


# ==================================================================
# SOAL 1 (* Mudah) - Hierarki Dasar: Bentuk Geometri
#
# Buat hierarki kelas berikut:
#   BentukDasar
#     |-- Persegi      (sisi)
#     |-- Lingkaran    (jari_jari)
#     `-- SegitigaSiku (alas, tinggi)
#
# Semua kelas anak harus mengimplementasikan:
#   - Method luas()  -> kembalikan luas bentuk
#   - Method keliling() -> kembalikan keliling bentuk
#   - Method __str__() -> format: "NamaBentuk | Luas: X | Keliling: Y"
#
# BentukDasar harus memiliki:
#   - Atribut 'warna' (default "putih")
#   - Method info() yang memanggil __str__ dan mencetak info warna
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 1: Hierarki Bentuk Geometri")
print("-" * 50)

import math

class BentukDasar:
    def __init__(self, warna="putih"):
        self.warna = warna

    def luas(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan luas()")

    def keliling(self):
        raise NotImplementedError("Subkelas harus mengimplementasikan keliling()")

    def info(self):
        print(f"  Bentuk: {self}")
        print(f"  Warna : {self.warna}")

    def __str__(self):
        return f"BentukDasar | Luas: {self.luas():.2f} | Keliling: {self.keliling():.2f}"


class Persegi(BentukDasar):
    def __init__(self, sisi, warna="putih"):
        pass   # TODO: Panggil super().__init__ dan simpan sisi

    def luas(self):
        pass   # TODO: Kembalikan sisi^2

    def keliling(self):
        pass   # TODO: Kembalikan 4 * sisi

    def __str__(self):
        pass   # TODO: "Persegi(sisi=X) | Luas: Y | Keliling: Z"


class Lingkaran(BentukDasar):
    def __init__(self, jari_jari, warna="putih"):
        pass   # TODO

    def luas(self):
        pass   # TODO: pi * r^2

    def keliling(self):
        pass   # TODO: 2 * pi * r

    def __str__(self):
        pass   # TODO: "Lingkaran(r=X) | Luas: Y | Keliling: Z"


class SegitigaSiku(BentukDasar):
    def __init__(self, alas, tinggi, warna="putih"):
        pass   # TODO

    def luas(self):
        pass   # TODO: 1/2 * alas * tinggi

    def sisi_miring(self):
        pass   # TODO: sqrt(alas^2 + tinggi^2) via math.sqrt

    def keliling(self):
        pass   # TODO: alas + tinggi + sisi_miring

    def __str__(self):
        pass   # TODO: "SegitigaSiku(alas=X, tinggi=Y) | Luas: Z | Keliling: W"


# Uji Soal 1
# Hapus tanda '#' di bawah setelah Anda mengimplementasikan kelas di atas
"""
p = Persegi(5, "merah")
l = Lingkaran(7)
s = SegitigaSiku(3, 4, "biru")

for bentuk in [p, l, s]:
    bentuk.info()
    print()

# Output yang diharapkan:
#   Bentuk: Persegi(sisi=5) | Luas: 25.00 | Keliling: 20.00
#   Warna : merah
#
#   Bentuk: Lingkaran(r=7) | Luas: 153.94 | Keliling: 43.98
#   Warna : putih
#
#   Bentuk: SegitigaSiku(alas=3, tinggi=4) | Luas: 6.00 | Keliling: 12.00
#   Warna : biru
"""
print("  [TODO] Soal 1 belum dikerjakan.")


# ==================================================================
# SOAL 2 (** Menengah) - Sistem Rekening Bank
#
# Buat hierarki kelas:
#   RekeningBank (induk)
#     |-- RekeningTabungan  (bunga_per_tahun, batas_tarik_per_hari)
#     `-- RekeningGiro      (limit_cerukan)  <- bisa "minus" sampai limit
#
# RekeningBank (induk) harus memiliki:
#   - Atribut: pemilik, nomor_rekening, saldo (awal = 0)
#   - Method setor(jumlah)    -> tambah saldo
#   - Method tarik(jumlah)    -> kurangi saldo, raise ValueError jika tidak cukup
#   - Property saldo          -> baca saldo (read-only dari luar)
#   - Method __str__()        -> format: "[no_rek] Pemilik | Saldo: Rp X"
#
# RekeningTabungan:
#   - Override tarik() -> periksa batas_tarik_per_hari
#   - Tambah method hitung_bunga() -> kembalikan bunga untuk periode tertentu
#   - Tambah method tambah_bunga_bulanan() -> setor bunga ke rekening
#
# RekeningGiro:
#   - Override tarik() -> boleh minus HINGGA limit_cerukan
#   - Tambah property cerukan_terpakai -> seberapa banyak limit cerukan terpakai
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 2: Sistem Rekening Bank")
print("-" * 50)

class RekeningBank:
    def __init__(self, pemilik, nomor_rekening, saldo_awal=0):
        pass   # TODO

    @property
    def saldo(self):
        pass   # TODO

    def setor(self, jumlah):
        pass   # TODO: Validasi positif, tambah saldo, cetak info

    def tarik(self, jumlah):
        pass   # TODO: Validasi cukup, kurangi saldo, cetak info

    def __str__(self):
        pass   # TODO


class RekeningTabungan(RekeningBank):
    def __init__(self, pemilik, nomor_rekening, bunga_per_tahun=3.5,
                 batas_tarik=5_000_000, saldo_awal=0):
        pass   # TODO

    def tarik(self, jumlah):
        pass   # TODO: Cek batas_tarik, lalu panggil super().tarik(jumlah)

    def hitung_bunga(self, bulan=1):
        pass   # TODO: saldo * (bunga_per_tahun/100) * (bulan/12)

    def tambah_bunga_bulanan(self):
        pass   # TODO: Setor hasil hitung_bunga(1) ke rekening


class RekeningGiro(RekeningBank):
    def __init__(self, pemilik, nomor_rekening, limit_cerukan=10_000_000,
                 saldo_awal=0):
        pass   # TODO

    def tarik(self, jumlah):
        pass   # TODO: Boleh minus tapi tidak melebihi limit_cerukan

    @property
    def cerukan_terpakai(self):
        pass   # TODO: Jika saldo negatif, kembalikan abs(saldo), else 0


# Uji Soal 2
"""
rt = RekeningTabungan("Budi", "TAB-001", bunga_per_tahun=3.5,
                      batas_tarik=5_000_000, saldo_awal=10_000_000)
rt.setor(2_000_000)
rt.tarik(4_000_000)     # OK
rt.tambah_bunga_bulanan()

try:
    rt.tarik(6_000_000)  # Gagal - melebihi batas tarik harian
except ValueError as e:
    print(f"  Error: {e}")

rg = RekeningGiro("Sari", "GIR-001", limit_cerukan=5_000_000)
rg.setor(3_000_000)
rg.tarik(7_000_000)     # OK karena ada cerukan
print(f"  Cerukan terpakai: Rp {rg.cerukan_terpakai:,.0f}")

try:
    rg.tarik(2_000_000)  # Gagal - melebihi limit cerukan
except ValueError as e:
    print(f"  Error: {e}")

print(rt)
print(rg)
"""
print("  [TODO] Soal 2 belum dikerjakan.")


# ==================================================================
# SOAL 3 (*** Menantang) - Sistem Notifikasi dengan Mixin
#
# Buat sistem notifikasi yang memanfaatkan Mixin:
#
# Kelas Mixin:
#   EmailMixin:   kirim_email(subjek, pesan) -> cetak format email
#   SMSMixin:     kirim_sms(nomor, pesan)    -> cetak format SMS
#   PushMixin:    kirim_push(judul, pesan)   -> cetak format push notif
#
# Kelas Utama:
#   Pengguna (induk)
#     |-- PenggunaPremium(EmailMixin, SMSMixin, PushMixin, Pengguna)
#     |     -> bisa kirim semua jenis notif
#     `-- PenggunaGratis(EmailMixin, Pengguna)
#           -> hanya bisa kirim email
#
# Pengguna harus memiliki nama dan email.
# Setiap Mixin harus menggunakan self.nama saat mencetak.
#
# Tambahkan method notifikasi_selamat_datang() di setiap kelas
# yang memanfaatkan notifikasi yang tersedia.
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 3: Sistem Notifikasi dengan Mixin")
print("-" * 50)

class EmailMixin:
    def kirim_email(self, subjek, pesan):
        pass   # TODO: cetak "[Email] ke {self.email}: [{subjek}] {pesan}"


class SMSMixin:
    def kirim_sms(self, nomor, pesan):
        pass   # TODO: cetak "[SMS] ke {nomor}: {pesan}"


class PushMixin:
    def kirim_push(self, judul, pesan):
        pass   # TODO: cetak "[Push] [{judul}]: {pesan} -> {self.nama}"


class Pengguna:
    def __init__(self, nama, email, nomor_hp=None):
        self.nama     = nama
        self.email    = email
        self.nomor_hp = nomor_hp


class PenggunaPremium(EmailMixin, SMSMixin, PushMixin, Pengguna):
    def __init__(self, nama, email, nomor_hp):
        super().__init__(nama, email, nomor_hp)

    def notifikasi_selamat_datang(self):
        pass   # TODO: Kirim semua jenis notifikasi


class PenggunaGratis(EmailMixin, Pengguna):
    def __init__(self, nama, email):
        super().__init__(nama, email)

    def notifikasi_selamat_datang(self):
        pass   # TODO: Kirim email saja


# Uji Soal 3
"""
premium = PenggunaPremium("Budi Santoso", "budi@email.com", "08123456789")
gratis  = PenggunaGratis("Sari Dewi",    "sari@email.com")

premium.notifikasi_selamat_datang()
print()
gratis.notifikasi_selamat_datang()

# Output yang diharapkan (premium):
#   [Email] ke budi@email.com: [Selamat Datang!] Halo Budi Santoso, ...
#   [SMS] ke 08123456789: Selamat datang, Budi Santoso!
#   [Push] [Selamat Datang!]: Akun premium aktif -> Budi Santoso

# Output yang diharapkan (gratis):
#   [Email] ke sari@email.com: [Selamat Datang!] Halo Sari Dewi, ...
"""
print("  [TODO] Soal 3 belum dikerjakan.")


print("\n" + "=" * 60)
print("Selesai! Kerjakan semua soal di atas.")
print("Hapus tanda # pada blok pengujian setelah implementasi selesai.")
print("=" * 60)
