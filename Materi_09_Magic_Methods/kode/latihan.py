"""
Latihan Mandiri - Materi 09: Magic Methods (Metode Ajaib)
File: latihan.py

Kerjakan semua soal di bawah ini. Jangan hapus kode yang sudah ada.
Setiap soal memiliki instruksi, kode stub, dan test otomatis.

Jalankan: python latihan.py
"""

print("=" * 60)
print("LATIHAN MATERI 09 -- Magic Methods")
print("=" * 60)

# ======================================================================
# SOAL 1 (*Mudah) -- Kelas TimOlahraga
# ----------------------------------------------------------------------
# Buat kelas 'TimOlahraga' yang merepresentasikan tim olahraga kampus.
#
# Atribut:
#   - nama_tim  (str)   : nama tim, misal "Informatika FC"
#   - cabang    (str)   : cabang olahraga, misal "Sepak Bola"
#   - _anggota  (list)  : list nama anggota (awalnya kosong)
#
# Magic methods yang harus diimplementasikan:
#   1. __str__      -> "Tim Informatika FC (Sepak Bola) -- 11 anggota"
#   2. __repr__     -> "TimOlahraga('Informatika FC', 'Sepak Bola')"
#   3. __len__      -> jumlah anggota
#   4. __bool__     -> True jika ada anggota
#   5. __contains__ -> 'Budi' in tim  --> cek nama anggota
#   6. __iter__     -> for anggota in tim: print(anggota)
#   7. __iadd__     -> tim += "Nama Anggota"  (menambahkan anggota)
#
# Method biasa yang perlu dibuat:
#   - tambah(nama)  : alternatif untuk +=
# ======================================================================
print()
print("SOAL 1: Kelas TimOlahraga")
print("-" * 40)


class TimOlahraga:
    """Tim olahraga kampus Universitas Mulawarman."""

    def __init__(self, nama_tim, cabang):
        self.nama_tim = nama_tim
        self.cabang   = cabang
        self._anggota = []

    def tambah(self, nama):
        """Menambahkan seorang anggota ke tim."""
        # TODO: tambahkan 'nama' ke self._anggota
        pass

    def __str__(self):
        # TODO: kembalikan string seperti:
        #       "Tim Informatika FC (Sepak Bola) -- 11 anggota"
        pass

    def __repr__(self):
        # TODO: kembalikan string seperti:
        #       "TimOlahraga('Informatika FC', 'Sepak Bola')"
        pass

    def __len__(self):
        # TODO: kembalikan jumlah anggota
        pass

    def __bool__(self):
        # TODO: kembalikan True jika ada anggota (minimal 1)
        pass

    def __contains__(self, nama):
        # TODO: kembalikan True jika 'nama' ada di self._anggota
        pass

    def __iter__(self):
        # TODO: kembalikan iterator untuk self._anggota
        pass

    def __iadd__(self, nama):
        # TODO: tambahkan 'nama' ke anggota, kembalikan self
        pass


# -- Test Soal 1 --
tim_futsal = TimOlahraga("Informatika FC", "Futsal")

# Seharusnya belum ada anggota
assert len(tim_futsal) == 0,   "GAGAL: len() seharusnya 0"
assert not tim_futsal,         "GAGAL: bool() seharusnya False untuk tim kosong"

# Tambah anggota via +=
tim_futsal += "Budi Santoso"
tim_futsal += "Ahmad Fauzi"
tim_futsal += "Rizky Pratama"
tim_futsal += "Deni Kurniawan"
tim_futsal += "Sari Dewi"

assert len(tim_futsal) == 5,         "GAGAL: len() seharusnya 5"
assert bool(tim_futsal),             "GAGAL: bool() seharusnya True"
assert "Budi Santoso" in tim_futsal, "GAGAL: 'Budi Santoso' seharusnya ada"
assert "Fulan" not in tim_futsal,    "GAGAL: 'Fulan' seharusnya tidak ada"

print(f"  str : {tim_futsal}")
print(f"  repr: {repr(tim_futsal)}")
print(f"  Anggota:")
for anggota in tim_futsal:
    print(f"    - {anggota}")

print("  [OK] Soal 1 LULUS semua test!")


# ======================================================================
# SOAL 2 (**Sedang) -- Kelas Pecahan (Bilangan Pecahan)
# ----------------------------------------------------------------------
# Buat kelas 'Pecahan' yang merepresentasikan bilangan pecahan (a/b).
#
# Atribut:
#   - pembilang  (int)
#   - penyebut   (int)
#
# Aturan:
#   - Penyebut tidak boleh nol (raise ValueError jika penyebut == 0)
#   - Otomatis sederhanakan: 4/6 -> 2/3 menggunakan GCD (math.gcd)
#   - Penyebut selalu positif: -1/2 = -1/2, tapi 1/-2 = -1/2
#
# Magic methods yang harus diimplementasikan:
#   1. __str__      -> "2/3"  (atau "3" jika penyebut = 1)
#   2. __repr__     -> "Pecahan(2, 3)"
#   3. __add__      -> Pecahan(1,2) + Pecahan(1,3) = Pecahan(5,6)
#   4. __sub__      -> Pecahan(3,4) - Pecahan(1,4) = Pecahan(1,2)
#   5. __mul__      -> Pecahan(2,3) * Pecahan(3,4) = Pecahan(1,2)
#   6. __truediv__  -> Pecahan(1,2) / Pecahan(2,3) = Pecahan(3,4)
#   7. __eq__       -> Pecahan(1,2) == Pecahan(2,4)  -> True
#   8. __lt__       -> Pecahan(1,3) < Pecahan(1,2)   -> True
#   9. __float__    -> float(Pecahan(1,2)) -> 0.5
#   10. __abs__     -> abs(Pecahan(-3,4)) -> Pecahan(3,4)
#
# Hint: untuk penyederhanaan gunakan math.gcd()
#   from math import gcd
#   g = gcd(pembilang, penyebut)  -- kemudian bagi keduanya dengan g
# ======================================================================
print()
print("SOAL 2: Kelas Pecahan")
print("-" * 40)

import math
from functools import total_ordering


@total_ordering
class Pecahan:
    """Representasi bilangan pecahan sederhana."""

    def __init__(self, pembilang, penyebut=1):
        # TODO: validasi penyebut != 0
        # TODO: sederhanakan dengan math.gcd
        # TODO: pastikan penyebut selalu positif
        self.pembilang = pembilang
        self.penyebut  = penyebut

    def __str__(self):
        # TODO: kembalikan "a/b" atau "a" jika penyebut == 1
        pass

    def __repr__(self):
        # TODO: kembalikan "Pecahan(a, b)"
        pass

    def __add__(self, other):
        # TODO: hitung a/b + c/d = (a*d + c*b) / (b*d), lalu sederhanakan
        pass

    def __sub__(self, other):
        # TODO: hitung a/b - c/d = (a*d - c*b) / (b*d), lalu sederhanakan
        pass

    def __mul__(self, other):
        # TODO: hitung (a/b) * (c/d) = (a*c) / (b*d), lalu sederhanakan
        pass

    def __truediv__(self, other):
        # TODO: hitung (a/b) / (c/d) = (a*d) / (b*c), lalu sederhanakan
        pass

    def __eq__(self, other):
        # TODO: a/b == c/d jika a*d == b*c
        pass

    def __lt__(self, other):
        # TODO: a/b < c/d jika a*d < b*c
        pass

    def __float__(self):
        # TODO: kembalikan pembilang / penyebut sebagai float
        pass

    def __abs__(self):
        # TODO: kembalikan Pecahan dengan pembilang positif
        pass


# -- Test Soal 2 --
p1 = Pecahan(1, 2)
p2 = Pecahan(1, 3)
p3 = Pecahan(2, 4)   # harus disederhanakan menjadi 1/2

assert str(p1) == "1/2",          f"GAGAL: str(1/2) = '{str(p1)}', seharusnya '1/2'"
assert str(p3) == "1/2",          f"GAGAL: 2/4 harus disederhanakan ke '1/2', dapat '{str(p3)}'"
assert str(Pecahan(4)) == "4",    "GAGAL: Pecahan(4) seharusnya '4' (penyebut=1)"
assert repr(p1) == "Pecahan(1, 2)", f"GAGAL: repr salah: {repr(p1)}"

assert str(p1 + p2) == "5/6",    f"GAGAL: 1/2 + 1/3 = '{str(p1+p2)}', seharusnya '5/6'"
assert str(p1 - p2) == "1/6",    f"GAGAL: 1/2 - 1/3 = '{str(p1-p2)}', seharusnya '1/6'"
assert str(p1 * p2) == "1/6",    f"GAGAL: 1/2 * 1/3 = '{str(p1*p2)}', seharusnya '1/6'"
assert str(p1 / p2) == "3/2",    f"GAGAL: 1/2 / 1/3 = '{str(p1/p2)}', seharusnya '3/2'"

assert p1 == p3,                  "GAGAL: 1/2 == 2/4 seharusnya True"
assert p2 < p1,                   "GAGAL: 1/3 < 1/2 seharusnya True"
assert float(p1) == 0.5,          "GAGAL: float(1/2) seharusnya 0.5"
assert str(abs(Pecahan(-3, 4))) == "3/4", "GAGAL: abs(-3/4) seharusnya '3/4'"

print(f"  p1 = {p1}   repr: {repr(p1)}")
print(f"  p2 = {p2}")
print(f"  p1 + p2 = {p1 + p2}")
print(f"  p1 - p2 = {p1 - p2}")
print(f"  p1 * p2 = {p1 * p2}")
print(f"  p1 / p2 = {p1 / p2}")
print(f"  float(p1) = {float(p1)}")
print(f"  Diurutkan: {[str(p) for p in sorted([p1, Pecahan(3,4), p2, Pecahan(1,8)])]}")
print("  [OK] Soal 2 LULUS semua test!")


# ======================================================================
# SOAL 3 (***Sulit) -- Kelas DaftarTugas (Task List Mahasiswa)
# ----------------------------------------------------------------------
# Buat kelas 'DaftarTugas' dan 'Tugas' untuk sistem manajemen tugas
# mahasiswa yang sepenuhnya memanfaatkan magic methods.
#
# Kelas Tugas:
#   Atribut: judul (str), matkul (str), prioritas (int 1-5), selesai (bool)
#   Magic methods:
#     1. __str__      -> "[X] Kerjakan UTS PBO (prioritas: 5)"
#                        "[ ] Buat laporan Jarkom (prioritas: 3)"
#        Gunakan [X] jika selesai=True, [ ] jika selesai=False
#     2. __repr__     -> "Tugas('Kerjakan UTS PBO', 'PBO', 5, True)"
#     3. __eq__       -> sama jika judul dan matkul sama (abaikan prioritas/selesai)
#     4. __lt__       -> bandingkan berdasarkan prioritas (LEBIH TINGGI = lebih kecil
#                        saat diurutkan, agar prioritas 5 muncul pertama)
#                        Hint: return self.prioritas > other.prioritas  (dibalik)
#     5. __bool__     -> True jika tugas BELUM selesai (masih perlu dikerjakan)
#     6. __hash__     -> hash berdasarkan judul dan matkul
#
# Kelas DaftarTugas:
#   Atribut: _tugas (list Tugas)
#   Magic methods:
#     1. __len__      -> jumlah tugas
#     2. __bool__     -> True jika ada tugas yang belum selesai
#     3. __iter__     -> iterasi semua tugas, diurutkan berdasarkan prioritas
#     4. __contains__ -> 'judul_tugas' in daftar  (cek judul)
#     5. __iadd__     -> daftar += tugas  (menambahkan tugas)
#     6. __isub__     -> daftar -= tugas  (menghapus tugas berdasarkan judul+matkul)
#     7. __str__      -> "DaftarTugas: 5 tugas (3 pending, 2 selesai)"
#     8. __call__     -> daftar(matkul) -> list tugas untuk mata kuliah tertentu
#
# Metode biasa yang perlu dibuat di DaftarTugas:
#   - tandai_selesai(judul) : tandai tugas dengan judul tertentu sebagai selesai
# ======================================================================
print()
print("SOAL 3: DaftarTugas Mahasiswa")
print("-" * 40)


@total_ordering
class Tugas:
    """Representasi satu tugas mahasiswa."""

    def __init__(self, judul, matkul, prioritas, selesai=False):
        if not (1 <= prioritas <= 5):
            raise ValueError(f"Prioritas harus 1-5, bukan {prioritas}")
        self.judul     = judul
        self.matkul    = matkul
        self.prioritas = prioritas
        self.selesai   = selesai

    def __str__(self):
        # TODO: "[X] Kerjakan UTS PBO (prioritas: 5)"
        #        "[ ] Buat laporan (prioritas: 3)"
        pass

    def __repr__(self):
        # TODO: "Tugas('Kerjakan UTS PBO', 'PBO', 5, False)"
        pass

    def __eq__(self, other):
        # TODO: sama jika judul dan matkul sama
        pass

    def __lt__(self, other):
        # TODO: tugas dengan prioritas LEBIH TINGGI dianggap "lebih kecil"
        #       agar sorted() menempatkan prioritas tinggi di depan
        #       Hint: return self.prioritas > other.prioritas
        pass

    def __bool__(self):
        # TODO: True jika BELUM selesai (masih perlu dikerjakan)
        pass

    def __hash__(self):
        # TODO: hash berdasarkan judul dan matkul
        pass


class DaftarTugas:
    """Manajemen daftar tugas mahasiswa."""

    def __init__(self):
        self._tugas = []

    def tandai_selesai(self, judul):
        """Menandai tugas dengan judul tertentu sebagai selesai."""
        for t in self._tugas:
            if t.judul == judul:
                t.selesai = True
                return True
        return False

    def __len__(self):
        # TODO: jumlah total tugas
        pass

    def __bool__(self):
        # TODO: True jika ada tugas yang BELUM selesai
        pass

    def __iter__(self):
        # TODO: iterasi semua tugas, diurutkan berdasarkan prioritas
        #       Hint: return iter(sorted(self._tugas))
        pass

    def __contains__(self, judul):
        # TODO: True jika ada tugas dengan judul tersebut
        pass

    def __iadd__(self, tugas):
        # TODO: tambahkan tugas ke self._tugas, kembalikan self
        pass

    def __isub__(self, tugas):
        # TODO: hapus tugas dari self._tugas berdasarkan judul+matkul (__eq__)
        #       kembalikan self
        pass

    def __str__(self):
        # TODO: "DaftarTugas: 5 tugas (3 pending, 2 selesai)"
        pass

    def __call__(self, matkul):
        # TODO: kembalikan list tugas untuk mata kuliah 'matkul'
        pass


# -- Test Soal 3 --
daftar = DaftarTugas()

t1 = Tugas("Kerjakan UTS",            "PBO",             5)
t2 = Tugas("Buat laporan jaringan",   "Jarkom",          3)
t3 = Tugas("Latihan soal kalkulus",   "Kalkulus",        2)
t4 = Tugas("Implementasi Hash Table", "Struktur Data",   4)
t5 = Tugas("Presentasi kelompok",     "PBO",             4)

daftar += t1
daftar += t2
daftar += t3
daftar += t4
daftar += t5

assert len(daftar) == 5,              "GAGAL: len() seharusnya 5"
assert bool(daftar),                  "GAGAL: bool() seharusnya True (ada tugas pending)"
assert "Kerjakan UTS" in daftar,      "GAGAL: 'Kerjakan UTS' seharusnya ada"
assert "Tugas Fiktif" not in daftar,  "GAGAL: 'Tugas Fiktif' seharusnya tidak ada"

# Cek urutan iterasi (prioritas 5 harus muncul pertama)
urutan = list(daftar)
assert urutan[0].prioritas == 5, "GAGAL: tugas pertama seharusnya prioritas 5"

daftar.tandai_selesai("Kerjakan UTS")
daftar.tandai_selesai("Latihan soal kalkulus")

# Setelah tandai selesai, masih ada 3 pending
assert bool(daftar), "GAGAL: bool() seharusnya True (masih ada pending)"

# Test __call__: cari tugas untuk matkul PBO
tugas_pbo = daftar("PBO")
assert len(tugas_pbo) == 2, f"GAGAL: tugas PBO seharusnya 2, dapat {len(tugas_pbo)}"

# Test __isub__: hapus satu tugas
daftar -= t3   # hapus "Latihan soal kalkulus"
assert len(daftar) == 4, "GAGAL: setelah -= len() seharusnya 4"

print(f"  {daftar}")
print(f"  Daftar tugas (diurutkan prioritas):")
for t in daftar:
    print(f"    {t}")

print(f"  Tugas PBO ({len(daftar('PBO'))} tugas):")
for t in daftar("PBO"):
    print(f"    {t}")

print("  [OK] Soal 3 LULUS semua test!")

print()
print("=" * 60)
print("Semua soal selesai!")
print("=" * 60)
