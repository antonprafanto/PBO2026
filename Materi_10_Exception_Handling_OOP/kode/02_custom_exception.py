"""
Kode Praktik - Materi 10: Exception Handling OOP
File: 02_custom_exception.py
Topik: Custom exception dengan hierarki, atribut kontekstual, contextlib

Jalankan: python 02_custom_exception.py
"""

import warnings
from contextlib import contextmanager, suppress

# ======================================================================
# BAGIAN 1: Mendefinisikan Hierarki Custom Exception
#           Fokus: membangun pohon exception untuk domain sistem akademik
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Hierarki Custom Exception Sistem Akademik")
print("=" * 60)

# ------------------------------------------------------------------
# Layer 1: Exception dasar (base) untuk seluruh modul akademik
# ------------------------------------------------------------------

class SistemAkademikError(Exception):
    """
    Exception dasar untuk seluruh sistem akademik Unmul.
    Semua custom exception di sistem ini turunan dari kelas ini.
    """
    def __init__(self, pesan, kode_error=None):
        self.kode_error = kode_error
        super().__init__(pesan)

    def __str__(self):
        if self.kode_error:
            return f"[{self.kode_error}] {super().__str__()}"
        return super().__str__()


# ------------------------------------------------------------------
# Layer 2: Kelompok exception berdasarkan kategori
# ------------------------------------------------------------------

class DataTidakDitemukanError(SistemAkademikError):
    """Data yang dicari tidak ada dalam sistem."""
    pass

class ValidasiError(SistemAkademikError):
    """Data tidak memenuhi aturan validasi."""
    pass

class AturanBisnisError(SistemAkademikError):
    """Operasi melanggar aturan bisnis sistem akademik."""
    pass


# ------------------------------------------------------------------
# Layer 3: Exception spesifik dengan atribut kontekstual
# ------------------------------------------------------------------

class MahasiswaTidakDitemukanError(DataTidakDitemukanError):
    """Mahasiswa dengan NIM tertentu tidak ada dalam sistem."""

    def __init__(self, nim):
        self.nim = nim
        super().__init__(
            f"Mahasiswa dengan NIM '{nim}' tidak ditemukan dalam sistem",
            kode_error="DATA-001"
        )


class MataKuliahTidakDitemukanError(DataTidakDitemukanError):
    """Mata kuliah dengan kode tertentu tidak tersedia."""

    def __init__(self, kode_mk):
        self.kode_mk = kode_mk
        super().__init__(
            f"Mata kuliah dengan kode '{kode_mk}' tidak tersedia",
            kode_error="DATA-002"
        )


class NIMTidakValidError(ValidasiError):
    """Format NIM tidak sesuai standar."""

    def __init__(self, nim, alasan=""):
        self.nim    = nim
        self.alasan = alasan
        pesan = f"NIM '{nim}' tidak valid"
        if alasan:
            pesan += f": {alasan}"
        super().__init__(pesan, kode_error="VAL-001")


class IPKTidakValidError(ValidasiError):
    """Nilai IPK di luar rentang yang diizinkan."""

    def __init__(self, ipk, batas_bawah=0.0, batas_atas=4.0):
        self.ipk         = ipk
        self.batas_bawah = batas_bawah
        self.batas_atas  = batas_atas
        super().__init__(
            f"IPK {ipk} tidak valid (harus {batas_bawah:.1f}-{batas_atas:.1f})",
            kode_error="VAL-002"
        )


class TunggakanSPPError(AturanBisnisError):
    """Mahasiswa memiliki tunggakan SPP yang belum diselesaikan."""

    def __init__(self, nim, jumlah_tunggakan):
        self.nim              = nim
        self.jumlah_tunggakan = jumlah_tunggakan
        super().__init__(
            f"Mahasiswa {nim} memiliki tunggakan SPP "
            f"Rp {jumlah_tunggakan:,.0f} yang harus dilunasi",
            kode_error="BISNIS-001"
        )


class KapasitasPenuhError(AturanBisnisError):
    """Kelas sudah mencapai kapasitas maksimum."""

    def __init__(self, kode_mk, kapasitas_maks):
        self.kode_mk       = kode_mk
        self.kapasitas_maks = kapasitas_maks
        super().__init__(
            f"Kelas {kode_mk} sudah penuh (maks {kapasitas_maks} mahasiswa)",
            kode_error="BISNIS-002"
        )


class PrasyaratTidakTerpenuhiError(AturanBisnisError):
    """Mahasiswa belum memenuhi prasyarat untuk mata kuliah tertentu."""

    def __init__(self, kode_mk, prasyarat_kurang):
        self.kode_mk          = kode_mk
        self.prasyarat_kurang = prasyarat_kurang   # list kode MK prasyarat
        super().__init__(
            f"Prasyarat '{kode_mk}' belum terpenuhi: "
            f"perlu lulus {', '.join(prasyarat_kurang)} terlebih dahulu",
            kode_error="BISNIS-003"
        )


# --- Demo hierarki ---
print("\n  -- Demo str() setiap exception --")
exceptions_demo = [
    MahasiswaTidakDitemukanError("2301999"),
    MataKuliahTidakDitemukanError("IF999"),
    NIMTidakValidError("230", "terlalu pendek (harus 7 digit)"),
    IPKTidakValidError(4.5),
    TunggakanSPPError("2301042", 2_500_000),
    KapasitasPenuhError("IF204", 40),
    PrasyaratTidakTerpenuhiError("IF305", ["IF201", "IF204"]),
]

for e in exceptions_demo:
    print(f"  {e}")

print("\n  -- Demo isinstance dengan hierarki --")
err = TunggakanSPPError("2301042", 2_500_000)
print(f"  isinstance(err, TunggakanSPPError)  : {isinstance(err, TunggakanSPPError)}")
print(f"  isinstance(err, AturanBisnisError)  : {isinstance(err, AturanBisnisError)}")
print(f"  isinstance(err, SistemAkademikError): {isinstance(err, SistemAkademikError)}")
print(f"  isinstance(err, Exception)          : {isinstance(err, Exception)}")
print(f"  isinstance(err, ValidasiError)      : {isinstance(err, ValidasiError)}")

# ======================================================================
# BAGIAN 2: Menggunakan Custom Exception dalam Kelas
#           Fokus: integrasi exception ke dalam metode kelas
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Custom Exception dalam Kelas")
print("=" * 60)


class MataKuliah:
    """Representasi mata kuliah dengan validasi exception."""

    def __init__(self, kode, nama, sks, kapasitas=40, prasyarat=None):
        self.kode       = kode
        self.nama       = nama
        self.sks        = sks
        self.kapasitas  = kapasitas
        self.prasyarat  = prasyarat or []
        self._peserta   = []

    def daftarkan(self, mahasiswa):
        """
        Mendaftarkan mahasiswa ke mata kuliah ini.
        Raises:
            TunggakanSPPError: jika mahasiswa ada tunggakan
            KapasitasPenuhError: jika kelas sudah penuh
            PrasyaratTidakTerpenuhiError: jika prasyarat belum terpenuhi
        """
        # Guard clause: validasi berurutan sebelum proses utama
        if mahasiswa.tunggakan > 0:
            raise TunggakanSPPError(mahasiswa.nim, mahasiswa.tunggakan)

        if len(self._peserta) >= self.kapasitas:
            raise KapasitasPenuhError(self.kode, self.kapasitas)

        kurang = [p for p in self.prasyarat if p not in mahasiswa.mk_lulus]
        if kurang:
            raise PrasyaratTidakTerpenuhiError(self.kode, kurang)

        self._peserta.append(mahasiswa.nim)
        return True

    def __str__(self):
        return f"{self.kode} | {self.nama} ({self.sks} SKS) [{len(self._peserta)}/{self.kapasitas}]"


class Mahasiswa:
    """Representasi data mahasiswa."""

    def __init__(self, nim, nama, tunggakan=0, mk_lulus=None):
        self.nim       = nim
        self.nama      = nama
        self.tunggakan = tunggakan    # dalam rupiah
        self.mk_lulus  = mk_lulus or []

    def __str__(self):
        return f"[{self.nim}] {self.nama}"


def coba_daftarkan(mahasiswa, matkul):
    """Mendaftarkan dengan penanganan exception terstruktur."""
    print(f"\n  Mendaftarkan {mahasiswa} ke {matkul.kode}...")
    try:
        matkul.daftarkan(mahasiswa)
        print(f"  [OK] Berhasil terdaftar di '{matkul.nama}'")
    except TunggakanSPPError as e:
        print(f"  [GAGAL] {e}")
        print(f"          Silakan lunasi Rp {e.jumlah_tunggakan:,.0f} di Keuangan")
    except KapasitasPenuhError as e:
        print(f"  [GAGAL] {e}")
        print(f"          Coba pilih kelas paralel atau jadwal lain")
    except PrasyaratTidakTerpenuhiError as e:
        print(f"  [GAGAL] {e}")
        print(f"          Prasyarat belum: {', '.join(e.prasyarat_kurang)}")
    except AturanBisnisError as e:
        # Jaring pengaman untuk semua AturanBisnisError lainnya
        print(f"  [ATURAN] {e}")


# --- Demo ---
mk_pbo  = MataKuliah("IF204", "Pemrograman Berorientasi Objek", 3,
                     prasyarat=["IF101"])
mk_jarkom = MataKuliah("IF210", "Jaringan Komputer", 3, kapasitas=2)

mhs_budi  = Mahasiswa("2301001", "Budi Santoso",  tunggakan=0,
                       mk_lulus=["IF101", "IF201"])
mhs_sari  = Mahasiswa("2301042", "Sari Dewi",     tunggakan=2_500_000,
                       mk_lulus=["IF101"])
mhs_ahmad = Mahasiswa("2301087", "Ahmad Fauzi",   tunggakan=0,
                       mk_lulus=[])  # belum lulus IF101
mhs_deni  = Mahasiswa("2301103", "Deni Kurniawan", tunggakan=0,
                       mk_lulus=["IF101"])
mhs_reza  = Mahasiswa("2301115", "Reza Pratama",  tunggakan=0,
                       mk_lulus=["IF101"])

coba_daftarkan(mhs_budi, mk_pbo)     # harus berhasil
coba_daftarkan(mhs_sari, mk_pbo)     # TunggakanSPPError
coba_daftarkan(mhs_ahmad, mk_pbo)    # PrasyaratTidakTerpenuhiError

# Demo KapasitasPenuhError (kapasitas=2)
coba_daftarkan(mhs_deni, mk_jarkom)
coba_daftarkan(mhs_reza, mk_jarkom)
coba_daftarkan(mhs_budi, mk_jarkom)  # KapasitasPenuhError

# ======================================================================
# BAGIAN 3: contextlib -- @contextmanager dan suppress
#           Fokus: cara ringkas membuat context manager
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 3: contextlib -- @contextmanager dan suppress")
print("=" * 60)


@contextmanager
def transaksi_akademik(nim, operasi):
    """
    Context manager untuk operasi akademik yang harus atomic.
    Jika ada error, operasi dibatalkan (rollback).
    """
    print(f"\n  [Mulai Transaksi] {operasi} -- Mahasiswa: {nim}")
    log = []
    try:
        yield log   # beri kontrol ke blok 'with', log bisa diisi
        # Jika sampai sini, tidak ada exception -- commit
        print(f"  [Commit] {len(log)} operasi berhasil disimpan:")
        for item in log:
            print(f"    - {item}")
    except SistemAkademikError as e:
        # Rollback jika ada error sistem akademik
        print(f"  [Rollback] {operasi} dibatalkan karena: {e}")
        print(f"    {len(log)} operasi yang sudah masuk dibatalkan")
    except Exception as e:
        print(f"  [Rollback Darurat] Error tak terduga: {e}")
        raise   # teruskan exception non-akademik
    finally:
        print(f"  [Selesai Transaksi] {operasi}")


print("\n-- Demo @contextmanager: transaksi berhasil --")
with transaksi_akademik("2301001", "Pengisian KRS") as log:
    log.append("IF201 ditambahkan ke KRS")
    log.append("IF204 ditambahkan ke KRS")
    log.append("MK102 ditambahkan ke KRS")

print("\n-- Demo @contextmanager: transaksi gagal (exception) --")
with transaksi_akademik("2301042", "Pengisian KRS") as log:
    log.append("IF207 ditambahkan ke KRS")
    raise TunggakanSPPError("2301042", 1_500_000)   # simulasi error di tengah transaksi

# --- Demo contextlib.suppress ---
print("\n-- Demo suppress: abaikan exception tertentu --")

# Tanpa suppress (cara lama):
cache_file = "cache_nilai_2301001.tmp"
try:
    import os
    os.remove(cache_file)
except FileNotFoundError:
    pass  # tidak apa-apa jika file tidak ada
print(f"  [Cara lama] File cache dihapus (atau tidak ada -- tidak masalah)")

# Dengan suppress (cara modern):
with suppress(FileNotFoundError):
    import os
    os.remove(cache_file)
print(f"  [suppress]  Kode lebih bersih, hasil sama")

# ======================================================================
# BAGIAN 4: warnings -- Peringatan yang Bukan Error
#           Fokus: memberi tahu kondisi tidak ideal tanpa menghentikan program
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 4: warnings -- Peringatan (Bukan Error)")
print("=" * 60)


class IPKRendahWarning(UserWarning):
    """Peringatan IPK mendekati batas minimum akademik."""
    pass


class SKSBerlebihWarning(UserWarning):
    """Peringatan jumlah SKS melebihi rekomendasi."""
    pass


def evaluasi_beban_studi(nim, ipk, total_sks):
    """
    Mengevaluasi beban studi mahasiswa.
    Raises: IPKTidakValidError jika IPK di luar batas
    Warns: IPKRendahWarning atau SKSBerlebihWarning jika kondisi tidak ideal
    """
    # Validasi (exception jika di luar batas absolut)
    if not (0.0 <= ipk <= 4.0):
        raise IPKTidakValidError(ipk)

    # Peringatan (warning jika kondisi tidak ideal tapi masih valid)
    if ipk < 2.5:
        warnings.warn(
            f"IPK mahasiswa {nim} ({ipk:.2f}) mendekati batas minimum (2.0)",
            IPKRendahWarning,
            stacklevel=2
        )

    maks_sks = 24 if ipk >= 3.0 else 18
    if total_sks > maks_sks:
        warnings.warn(
            f"Mahasiswa {nim}: {total_sks} SKS melebihi rekomendasi "
            f"{maks_sks} SKS untuk IPK {ipk:.2f}",
            SKSBerlebihWarning,
            stacklevel=2
        )

    return f"Beban studi {nim}: {total_sks} SKS, IPK {ipk:.2f}"


# Tampilkan warnings ke output
warnings.simplefilter("always")

print("\n-- Mahasiswa IPK baik, SKS normal --")
print("  " + evaluasi_beban_studi("2301001", 3.75, 20))

print("\n-- Mahasiswa IPK rendah --")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    evaluasi_beban_studi("2301042", 2.3, 18)
    for warning in w:
        print(f"  [WARNING] {warning.category.__name__}: {warning.message}")

print("\n-- Mahasiswa SKS berlebih --")
with warnings.catch_warnings(record=True) as w:
    warnings.simplefilter("always")
    evaluasi_beban_studi("2301087", 2.8, 22)
    for warning in w:
        print(f"  [WARNING] {warning.category.__name__}: {warning.message}")

print()
print("Selesai! Semua bagian dijalankan tanpa error.")
