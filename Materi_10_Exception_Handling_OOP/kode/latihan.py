"""
Latihan - Materi 10: Exception Handling OOP
File: latihan.py

Petunjuk:
- Lengkapi setiap bagian yang bertanda # TODO:
- Jalankan file ini untuk memverifikasi jawaban Anda
- Jangan ubah bagian yang tidak ditandai TODO
- Semua assert harus lulus tanpa AssertionError
"""

from contextlib import contextmanager
import warnings

print("=" * 60)
print("LATIHAN MATERI 10: Exception Handling OOP")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah): Custom Exception Sistem Perpustakaan Kampus
# ----------------------------------------------------------------------
# Buat hierarki custom exception untuk perpustakaan kampus Unmul.
# Tingkat kesulitan: * (Mudah)
# ======================================================================
print()
print("SOAL 1: Custom Exception Sistem Perpustakaan")
print("-" * 40)

# TODO: Buat class PerpustakaanError(Exception) sebagai base exception.
#       Constructor menerima (pesan, kode=None).
#       __str__ harus menampilkan "[kode] pesan" jika kode ada, atau "pesan" saja.
class PerpustakaanError(Exception):
    pass  # TODO: implementasikan


# TODO: Buat class BukuTidakDitemukanError(PerpustakaanError).
#       Constructor menerima (isbn) dan menyimpannya sebagai self.isbn.
#       Pesan: "Buku dengan ISBN '{isbn}' tidak ditemukan di koleksi"
#       Kode error: "PERPU-001"
class BukuTidakDitemukanError(PerpustakaanError):
    pass  # TODO: implementasikan


# TODO: Buat class AnggotaTidakAktifError(PerpustakaanError).
#       Constructor menerima (nim, status) dan menyimpannya.
#       Pesan: "Anggota {nim} berstatus '{status}', bukan Aktif"
#       Kode error: "PERPU-002"
class AnggotaTidakAktifError(PerpustakaanError):
    pass  # TODO: implementasikan


# TODO: Buat class DendaKeterlambatanError(PerpustakaanError).
#       Constructor menerima (nim, judul_buku, hari_terlambat, total_denda).
#       Pesan: "Anggota {nim} terlambat {hari_terlambat} hari mengembalikan
#              '{judul_buku}', denda Rp {total_denda:,.0f}"
#       Kode error: "PERPU-003"
class DendaKeterlambatanError(PerpustakaanError):
    pass  # TODO: implementasikan


# TODO: Buat class BukuSudahDipinjamError(PerpustakaanError).
#       Constructor menerima (isbn, peminjam_nim).
#       Pesan: "Buku ISBN '{isbn}' sedang dipinjam oleh {peminjam_nim}"
#       Kode error: "PERPU-004"
class BukuSudahDipinjamError(PerpustakaanError):
    pass  # TODO: implementasikan


# TODO: Implementasikan fungsi pinjam_buku(nim, status_anggota, isbn,
#       koleksi_buku, sedang_dipinjam) yang:
#       1. Raise AnggotaTidakAktifError jika status_anggota != "Aktif"
#       2. Raise BukuTidakDitemukanError jika isbn tidak ada di koleksi_buku
#       3. Raise BukuSudahDipinjamError jika isbn ada di sedang_dipinjam
#       4. Kembalikan True jika semua validasi lolos
def pinjam_buku(nim, status_anggota, isbn, koleksi_buku, sedang_dipinjam):
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 1 (jangan ubah bagian ini)
print("  Pengujian Soal 1...")

try:
    e = PerpustakaanError("sistem error", "TEST")
    assert str(e) == "[TEST] sistem error", f"str() salah: {str(e)}"
    e2 = PerpustakaanError("tanpa kode")
    assert str(e2) == "tanpa kode"
    print("  [OK] PerpustakaanError OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  PerpustakaanError: {err}")

try:
    e = BukuTidakDitemukanError("978-602-111")
    assert e.isbn == "978-602-111"
    assert "978-602-111" in str(e)
    assert "[PERPU-001]" in str(e)
    assert isinstance(e, PerpustakaanError)
    print("  [OK] BukuTidakDitemukanError OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  BukuTidakDitemukanError: {err}")

try:
    e = AnggotaTidakAktifError("2301042", "Cuti")
    assert e.nim == "2301042"
    assert e.status == "Cuti"
    assert "[PERPU-002]" in str(e)
    print("  [OK] AnggotaTidakAktifError OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  AnggotaTidakAktifError: {err}")

try:
    e = DendaKeterlambatanError("2301001", "Algoritma Pemrograman", 5, 25000)
    assert e.nim == "2301001"
    assert e.hari_terlambat == 5
    assert e.total_denda == 25000
    assert "[PERPU-003]" in str(e)
    assert "25,000" in str(e) or "25000" in str(e)
    print("  [OK] DendaKeterlambatanError OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  DendaKeterlambatanError: {err}")

try:
    e = BukuSudahDipinjamError("978-602-111", "2301042")
    assert e.isbn == "978-602-111"
    assert e.peminjam_nim == "2301042"
    assert "[PERPU-004]" in str(e)
    print("  [OK] BukuSudahDipinjamError OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  BukuSudahDipinjamError: {err}")

try:
    koleksi   = {"978-602-111", "978-602-222", "978-602-333"}
    dipinjam  = {"978-602-222": "2301050"}

    hasil = pinjam_buku("2301001", "Aktif", "978-602-111", koleksi, dipinjam)
    assert hasil is True, "Peminjaman valid harus mengembalikan True"

    try:
        pinjam_buku("2301099", "Cuti", "978-602-111", koleksi, dipinjam)
        print("  [X]  pinjam_buku: seharusnya raise AnggotaTidakAktifError")
    except AnggotaTidakAktifError:
        pass

    try:
        pinjam_buku("2301001", "Aktif", "978-999-999", koleksi, dipinjam)
        print("  [X]  pinjam_buku: seharusnya raise BukuTidakDitemukanError")
    except BukuTidakDitemukanError:
        pass

    try:
        pinjam_buku("2301001", "Aktif", "978-602-222", koleksi, dipinjam)
        print("  [X]  pinjam_buku: seharusnya raise BukuSudahDipinjamError")
    except BukuSudahDipinjamError:
        pass

    print("  [OK] pinjam_buku() OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  pinjam_buku: {err}")


# ======================================================================
# SOAL 2 (**Sedang): Exception Handling dengan Guard Clause dalam Kelas
# ----------------------------------------------------------------------
# Buat kelas KantinKampus yang mengelola pemesanan makanan dengan
# exception handling yang lengkap menggunakan guard clauses.
# Tingkat kesulitan: ** (Sedang)
# ======================================================================
print()
print("SOAL 2: Kantin Kampus dengan Guard Clause")
print("-" * 40)

# TODO: Buat kelas-kelas exception berikut (semua turunan KantinError):
#       - KantinError(Exception): base, constructor(pesan, kode=None)
#       - MenuTidakAdaError(KantinError): constructor(nama_menu)
#         Pesan: "Menu '{nama_menu}' tidak tersedia", kode="KANTIN-001"
#       - StokHabisError(KantinError): constructor(nama_menu, stok_tersisa)
#         Pesan: "'{nama_menu}' stok habis (tersisa {stok_tersisa})",
#         kode="KANTIN-002", simpan stok_tersisa sebagai atribut
#       - SaldoKurangError(KantinError): constructor(nim, saldo, harga_total)
#         Pesan: "Saldo {nim} tidak cukup: Rp {saldo:,.0f} < Rp {harga_total:,.0f}"
#         kode="KANTIN-003", simpan semua sebagai atribut
class KantinError(Exception):
    pass  # TODO: implementasikan

class MenuTidakAdaError(KantinError):
    pass  # TODO: implementasikan

class StokHabisError(KantinError):
    pass  # TODO: implementasikan

class SaldoKurangError(KantinError):
    pass  # TODO: implementasikan


# TODO: Buat class KantinKampus dengan:
#   - __init__(self): self._menu = {} dan self._saldo_mahasiswa = {}
#   - tambah_menu(self, nama, harga, stok): tambah ke self._menu
#     self._menu[nama] = {"harga": harga, "stok": stok}
#   - isi_saldo(self, nim, jumlah): self._saldo_mahasiswa[nim] += jumlah
#     (jika nim belum ada, mulai dari 0)
#   - get_saldo(self, nim): return saldo mahasiswa nim, atau 0 jika tidak ada
#   - pesan(self, nim, nama_menu, jumlah=1):
#     Guard 1: raise MenuTidakAdaError jika nama_menu tidak ada di _menu
#     Guard 2: raise StokHabisError jika stok < jumlah
#     Guard 3: raise SaldoKurangError jika saldo < harga_total
#     Jika lolos: kurangi stok dan saldo, kembalikan True
class KantinKampus:
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 2 (jangan ubah bagian ini)
print("  Pengujian Soal 2...")

try:
    kantin = KantinKampus()
    kantin.tambah_menu("Nasi Goreng",   12000, 10)
    kantin.tambah_menu("Mie Ayam",      10000, 2)
    kantin.tambah_menu("Es Teh",         3000, 50)
    kantin.isi_saldo("2301001", 50000)
    kantin.isi_saldo("2301042", 8000)
    print("  [OK] KantinKampus.__init__, tambah_menu, isi_saldo OK")
except Exception as err:
    print(f"  [X]  KantinKampus setup: {err}")

try:
    hasil = kantin.pesan("2301001", "Nasi Goreng")
    assert hasil is True
    print("  [OK] pesan() normal OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  pesan() normal: {err}")

try:
    try:
        kantin.pesan("2301001", "Soto Lamongan")
        print("  [X]  seharusnya raise MenuTidakAdaError")
    except MenuTidakAdaError as e:
        assert "Soto Lamongan" in str(e)
        print("  [OK] MenuTidakAdaError OK")
except Exception as err:
    print(f"  [X]  MenuTidakAdaError: {err}")

try:
    # Habiskan stok Mie Ayam (stok=2)
    kantin.pesan("2301001", "Mie Ayam", 2)
    try:
        kantin.pesan("2301001", "Mie Ayam")   # stok sudah 0
        print("  [X]  seharusnya raise StokHabisError")
    except StokHabisError as e:
        assert e.stok_tersisa == 0
        print("  [OK] StokHabisError OK")
except Exception as err:
    print(f"  [X]  StokHabisError: {err}")

try:
    try:
        kantin.pesan("2301042", "Nasi Goreng")   # saldo 8000 < 12000
        print("  [X]  seharusnya raise SaldoKurangError")
    except SaldoKurangError as e:
        assert e.nim == "2301042"
        assert e.saldo == 8000
        assert e.harga_total == 12000
        print("  [OK] SaldoKurangError OK")
except Exception as err:
    print(f"  [X]  SaldoKurangError: {err}")


# ======================================================================
# SOAL 3 (***Sulit): Context Manager + Custom Warnings
# ----------------------------------------------------------------------
# Buat context manager untuk transaksi kantin dan tambahkan warnings
# untuk kondisi yang perlu perhatian.
# Tingkat kesulitan: *** (Sulit)
# ======================================================================
print()
print("SOAL 3: Context Manager dan Custom Warnings")
print("-" * 40)


# TODO: Buat class SaldoMenipisWarning(UserWarning).
#       Digunakan untuk memperingatkan saldo mahasiswa hampir habis.
class SaldoMenipisWarning(UserWarning):
    pass  # TODO: implementasikan


# TODO: Buat context manager menggunakan @contextmanager dengan nama
#       sesi_belanja(nim, nama_kantin).
#
#       Context manager ini harus:
#       1. Print "[Mulai Sesi] Belanja {nim} di {nama_kantin}" saat masuk
#       2. yield sebuah list kosong bernama 'keranjang'
#          (fungsi dalam blok 'with' bisa append ke keranjang)
#       3. Jika ada KantinError: print "[Dibatalkan] {error}" dan raise ulang
#       4. Jika tidak ada error: print "[Selesai] {len(keranjang)} item dibeli"
#       5. Di blok finally: print "[Keluar Sesi] {nim}"
#
#       Catatan: keranjang diisi oleh pengguna dari luar (blok with),
#       bukan oleh context manager sendiri.
@contextmanager
def sesi_belanja(nim, nama_kantin):
    pass  # TODO: implementasikan
    yield []  # TODO: ganti dengan implementasi yang benar


# TODO: Buat fungsi cek_saldo_dan_beli(kantin, nim, nama_menu, jumlah=1)
#       yang melakukan:
#       1. Panggil kantin.pesan(nim, nama_menu, jumlah) secara normal
#       2. Setelah berhasil beli: cek saldo sisa mahasiswa dengan kantin.get_saldo(nim)
#       3. Jika saldo sisa < 15000, keluarkan SaldoMenipisWarning:
#          "Saldo {nim} tersisa Rp {saldo_sisa:,.0f} -- segera isi ulang"
#          dengan stacklevel=2
#       4. Kembalikan True jika berhasil
#
#       Catatan: Gunakan kantin.get_saldo(nim) untuk akses saldo (method dari KantinKampus).
def cek_saldo_dan_beli(kantin, nim, nama_menu, jumlah=1):
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 3 (jangan ubah bagian ini)
print("  Pengujian Soal 3...")

try:
    assert issubclass(SaldoMenipisWarning, UserWarning)
    print("  [OK] SaldoMenipisWarning OK")
except Exception as err:
    print(f"  [X]  SaldoMenipisWarning: {err}")

# Siapkan kantin fresh untuk soal 3
try:
    kantin3 = KantinKampus()
    kantin3.tambah_menu("Nasi Goreng", 12000, 20)
    kantin3.tambah_menu("Es Teh",       3000, 50)
    kantin3.isi_saldo("2301001", 50000)
    kantin3.isi_saldo("2301200", 14000)   # saldo pas, akan memicu warning
except Exception as err:
    print(f"  [X]  Setup kantin3: {err}")

try:
    print("  -- sesi_belanja (berhasil) --")
    with sesi_belanja("2301001", "Kantin FT") as keranjang:
        kantin3.pesan("2301001", "Nasi Goreng")
        keranjang.append("Nasi Goreng")
        kantin3.pesan("2301001", "Es Teh")
        keranjang.append("Es Teh")
    print("  [OK] sesi_belanja (berhasil) OK")
except Exception as err:
    print(f"  [X]  sesi_belanja (berhasil): {err}")

try:
    print("  -- sesi_belanja (gagal) --")
    try:
        with sesi_belanja("2301200", "Kantin FT") as keranjang:
            kantin3.pesan("2301200", "Nasi Goreng")   # saldo 14000 < 12000? tidak
            keranjang.append("Nasi Goreng")            # ini mungkin berhasil
            kantin3.pesan("2301200", "Nasi Goreng")   # saldo kurang untuk kedua
            keranjang.append("Nasi Goreng")
    except KantinError:
        print("  [OK] sesi_belanja (gagal dengan exception) OK")
except Exception as err:
    print(f"  [X]  sesi_belanja (gagal): {err}")

try:
    kantin_w = KantinKampus()
    kantin_w.tambah_menu("Bakso",  10000, 20)
    kantin_w.isi_saldo("2301300", 22000)  # setelah beli 10000 -> sisa 12000 < 15000

    with warnings.catch_warnings(record=True) as w:
        warnings.simplefilter("always")
        hasil = cek_saldo_dan_beli(kantin_w, "2301300", "Bakso")
        assert hasil is True, "cek_saldo_dan_beli harus return True"
        assert len(w) >= 1, "Seharusnya ada SaldoMenipisWarning"
        assert issubclass(w[0].category, SaldoMenipisWarning), \
               f"Warning salah: {w[0].category}"
        # Verifikasi saldo sisa di warning message
        msg = str(w[0].message)
        assert ("12,000" in msg or "12000" in msg or "2301300" in msg), \
               f"Warning harus mention saldo/nim: {msg}"
        print("  [OK] cek_saldo_dan_beli + SaldoMenipisWarning OK")
except (AssertionError, Exception) as err:
    print(f"  [X]  cek_saldo_dan_beli: {err}")

print()
print("Latihan selesai! Periksa output di atas untuk [OK]/[X].")
