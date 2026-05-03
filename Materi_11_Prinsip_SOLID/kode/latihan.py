"""
Latihan - Materi 11: Prinsip SOLID
File: latihan.py

Petunjuk:
- Lengkapi setiap bagian yang bertanda # TODO:
- Jalankan file ini untuk memverifikasi jawaban Anda
- Jangan ubah bagian yang tidak ditandai TODO
- Semua assert harus lulus tanpa AssertionError

Kaitan dengan Materi:
- SOAL 1 berkaitan dengan materi.md Bagian 2 (Single Responsibility Principle)
- SOAL 2 berkaitan dengan materi.md Bagian 3 (Open/Closed Principle)
- SOAL 3 berkaitan dengan materi.md Bagian 6 (Dependency Inversion Principle)
"""

from abc import ABC, abstractmethod

print("=" * 60)
print("LATIHAN MATERI 11: Prinsip SOLID")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah): Refactor SRP - Pisahkan Tanggung Jawab
# (Lihat materi.md Bagian 2 untuk teori SRP)
# ======================================================================
print()
print("SOAL 1: Refactor Single Responsibility Principle")
print("-" * 40)

# Diberikan:
class MahasiswaJelek:
    """
    [JELEK] Kelas ini melakukan terlalu banyak hal:
    1. Representasi data mahasiswa
    2. Mengirim email
    3. Cetak dokumen
    Anda harus pisahkan menjadi kelas-kelas terpisah!
    """
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk

    def kirim_email_nilai(self, email, nilai):
        """Email logic -- should be in separate class."""
        return f"Email: {nilai} dikirim ke {email}"

    def cetak_transkrip(self, filename):
        """Document logic -- should be in separate class."""
        return f"PDF: Transkrip dicetak ke {filename}"

    def hitung_beasiswa(self):
        """Academic logic -- this can stay."""
        return 500000 if self.ipk >= 3.5 else 0


# TODO: Buat class Mahasiswa (hanya handle data + hitung_beasiswa)
class Mahasiswa:
    pass  # TODO: implementasikan


# TODO: Buat class LayananEmail (handle semua email operations)
class LayananEmail:
    pass  # TODO: implementasikan


# TODO: Buat class LayananDokumen (handle semua cetak dokumen)
class LayananDokumen:
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 1
print("  Pengujian Soal 1...")

try:
    mhs = Mahasiswa("2301001", "Budi Santoso", 3.75)
    assert mhs.nim == "2301001"
    assert mhs.nama == "Budi Santoso"
    assert mhs.ipk == 3.75
    assert mhs.hitung_beasiswa() == 500000
    print("  [OK] Mahasiswa class OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  Mahasiswa: {err}")

try:
    email_svc = LayananEmail()
    hasil = email_svc.kirim_nilai("budi@unmul.ac.id", "A")
    assert isinstance(hasil, bool) and hasil is True
    print("  [OK] LayananEmail.kirim_nilai() OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  LayananEmail: {err}")

try:
    doc_svc = LayananDokumen()
    hasil = doc_svc.cetak_transkrip("transkrip.pdf")
    assert isinstance(hasil, bool) and hasil is True
    print("  [OK] LayananDokumen.cetak_transkrip() OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  LayananDokumen: {err}")


# ======================================================================
# SOAL 2 (**Sedang): Refactor OCP - Extend tanpa Modify
# (Lihat materi.md Bagian 3 untuk teori OCP)
# ======================================================================
print()
print("SOAL 2: Refactor Open/Closed Principle")
print("-" * 40)

# Diberikan:
class KalkulatorDiskonJelek:
    """
    [JELEK] Setiap tipe mahasiswa baru = ubah method ini!
    OCP violation: tidak closed untuk modification.
    Anda harus gunakan strategy pattern!
    """
    def hitung_diskon(self, harga, tipe_mahasiswa):
        if tipe_mahasiswa == "reguler":
            return harga * 0.0
        elif tipe_mahasiswa == "beasiswa":
            return harga * 0.2  # Diskon 20%
        elif tipe_mahasiswa == "bidikmisi":
            return harga * 0.5  # Diskon 50%
        # Tambah tipe baru = harus edit method ini!


# TODO: Buat abstract class StrategiDiskon dengan abstractmethod hitung_diskon
#       Method signature: hitung_diskon(self, harga: float) -> float
class StrategiDiskon(ABC):
    @abstractmethod
    def hitung_diskon(self, harga: float) -> float:
        """Hitung diskon untuk harga tertentu."""
        pass


# TODO: Buat class StrategiDiskonReguler (extend StrategiDiskon)
#       Implementasi: diskon = 0% dari harga
class StrategiDiskonReguler(StrategiDiskon):
    pass  # TODO: implementasikan


# TODO: Buat class StrategiDiskonBeasiswa (extend StrategiDiskon)
#       Implementasi: diskon = 20% dari harga
class StrategiDiskonBeasiswa(StrategiDiskon):
    pass  # TODO: implementasikan


# TODO: Buat class StrategiDiskonBidikmisi (extend StrategiDiskon)
#       Implementasi: diskon = 50% dari harga
class StrategiDiskonBidikmisi(StrategiDiskon):
    pass  # TODO: implementasikan


# TODO: Buat class KalkulatorDiskonBaik yang:
#       - __init__(self, strategi: StrategiDiskon)
#       - hitung(self, harga) -- gunakan strategi yang di-inject
class KalkulatorDiskonBaik:
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 2
print("  Pengujian Soal 2...")

try:
    strat_reguler = StrategiDiskonReguler()
    diskon = strat_reguler.hitung_diskon(100000)
    assert diskon == 0
    print("  [OK] StrategiDiskonReguler OK (diskon 0%)")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  StrategiDiskonReguler: {err}")

try:
    strat_beasiswa = StrategiDiskonBeasiswa()
    diskon = strat_beasiswa.hitung_diskon(100000)
    assert diskon == 20000
    print("  [OK] StrategiDiskonBeasiswa OK (diskon 20%)")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  StrategiDiskonBeasiswa: {err}")

try:
    strat_bidikmisi = StrategiDiskonBidikmisi()
    diskon = strat_bidikmisi.hitung_diskon(100000)
    assert diskon == 50000
    print("  [OK] StrategiDiskonBidikmisi OK (diskon 50%)")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  StrategiDiskonBidikmisi: {err}")

try:
    kalkulator = KalkulatorDiskonBaik(StrategiDiskonBeasiswa())
    hasil = kalkulator.hitung(100000)
    assert hasil == 20000, f"Harus return diskon 20000, bukan {hasil}"
    print("  [OK] KalkulatorDiskonBaik OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  KalkulatorDiskonBaik: {err}")


# ======================================================================
# SOAL 3 (***Sulit): Refactor DIP - Dependency Injection
# (Lihat materi.md Bagian 6 untuk teori DIP)
# ======================================================================
print()
print("SOAL 3: Refactor Dependency Inversion Principle")
print("-" * 40)

# Diberikan:
class DatabaseMahasiswaKonkret:
    """Database konkret -- hardcoded."""
    def ambil(self, nim):
        return {"nim": nim, "nama": "Dummy"}


class SistemAkademikJelek:
    """
    [JELEK] Hardcode depend pada DatabaseMahasiswaKonkret.
    Jika mau ganti database = ubah class ini!
    DIP violation: harus depend pada abstraksi.
    """
    def __init__(self):
        self.db = DatabaseMahasiswaKonkret()

    def cari_mahasiswa(self, nim):
        return self.db.ambil(nim)


# TODO: Buat abstract class RepositoriMahasiswa dengan abstractmethod ambil
#       Method signature: ambil(self, nim: str) -> dict
class RepositoriMahasiswa(ABC):
    @abstractmethod
    def ambil(self, nim: str) -> dict:
        """Ambil data mahasiswa berdasarkan NIM."""
        pass


# TODO: Buat class RepositoriMahasiswaMySQL (extend RepositoriMahasiswa)
#       Implementasi ambil: return {"nim": nim, "nama": "MySQL"}
class RepositoriMahasiswaMySQL(RepositoriMahasiswa):
    pass  # TODO: implementasikan


# TODO: Buat class RepositoriMahasiswaAPI (extend RepositoriMahasiswa)
#       Implementasi ambil: return {"nim": nim, "nama": "API"}
class RepositoriMahasiswaAPI(RepositoriMahasiswa):
    pass  # TODO: implementasikan


# TODO: Buat class SistemAkademikBaik yang:
#       - __init__(self, repo: RepositoriMahasiswa)
#       - cari_mahasiswa(self, nim) -- gunakan repo yang di-inject
#       - Jangan hardcode database!
class SistemAkademikBaik:
    pass  # TODO: implementasikan


# ==> PENGUJIAN SOAL 3
print("  Pengujian Soal 3...")

try:
    repo_mysql = RepositoriMahasiswaMySQL()
    mhs = repo_mysql.ambil("2301001")
    assert "2301001" in str(mhs)
    assert "MySQL" in str(mhs) or mhs.get("nama") == "MySQL"
    print("  [OK] RepositoriMahasiswaMySQL OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  RepositoriMahasiswaMySQL: {err}")

try:
    repo_api = RepositoriMahasiswaAPI()
    mhs = repo_api.ambil("2301042")
    assert "2301042" in str(mhs)
    assert "API" in str(mhs) or mhs.get("nama") == "API"
    print("  [OK] RepositoriMahasiswaAPI OK")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  RepositoriMahasiswaAPI: {err}")

try:
    # Test dengan MySQL
    sistem1 = SistemAkademikBaik(RepositoriMahasiswaMySQL())
    mhs1 = sistem1.cari_mahasiswa("2301001")
    assert mhs1 is not None
    
    # Test dengan API -- tanpa ubah SistemAkademikBaik!
    sistem2 = SistemAkademikBaik(RepositoriMahasiswaAPI())
    mhs2 = sistem2.cari_mahasiswa("2301042")
    assert mhs2 is not None
    
    print("  [OK] SistemAkademikBaik OK (flexible!)")
except (AssertionError, AttributeError, Exception) as err:
    print(f"  [X]  SistemAkademikBaik: {err}")

print()
print("Latihan selesai! Periksa output di atas untuk [OK]/[X].")
