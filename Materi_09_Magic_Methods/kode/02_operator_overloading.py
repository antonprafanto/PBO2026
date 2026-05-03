"""
Kode Praktik - Materi 09: Magic Methods (Metode Ajaib)
File: 02_operator_overloading.py
Topik: Operator aritmatika, perbandingan, container lanjutan, context manager

Jalankan: python 02_operator_overloading.py
"""

from functools import total_ordering

# ======================================================================
# BAGIAN 1: Operator Aritmatika -- Kelas Vektor2D dan Pecahan
#           Fokus: __add__, __sub__, __mul__, __truediv__, __neg__,
#                  __rmul__, __abs__, __str__, __repr__
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Operator Aritmatika -- Vektor2D")
print("=" * 60)


class Vektor2D:
    """
    Representasi vektor dua dimensi dengan operator matematika lengkap.
    Berguna untuk kalkulasi posisi, fisika, atau grafis.
    """

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    # -- Representasi --
    def __str__(self):
        return f"({self.x:.2f}, {self.y:.2f})"

    def __repr__(self):
        return f"Vektor2D({self.x}, {self.y})"

    # -- Aritmatika biner --
    def __add__(self, other):
        """v1 + v2"""
        if isinstance(other, Vektor2D):
            return Vektor2D(self.x + other.x, self.y + other.y)
        return NotImplemented   # biarkan Python coba __radd__ dari other

    def __sub__(self, other):
        """v1 - v2"""
        if isinstance(other, Vektor2D):
            return Vektor2D(self.x - other.x, self.y - other.y)
        return NotImplemented

    def __mul__(self, skalar):
        """v * 3  (perkalian dengan skalar)"""
        if isinstance(skalar, (int, float)):
            return Vektor2D(self.x * skalar, self.y * skalar)
        return NotImplemented

    def __rmul__(self, skalar):
        """3 * v  (reflected -- sisi kanan ekspresi)"""
        return self.__mul__(skalar)

    def __truediv__(self, skalar):
        """v / 2"""
        if isinstance(skalar, (int, float)):
            if skalar == 0:
                raise ZeroDivisionError("Tidak bisa membagi vektor dengan nol")
            return Vektor2D(self.x / skalar, self.y / skalar)
        return NotImplemented

    # -- Operator unary --
    def __neg__(self):
        """-v  (kebalikan arah)"""
        return Vektor2D(-self.x, -self.y)

    def __pos__(self):
        """+v  (salinan positif)"""
        return Vektor2D(self.x, self.y)

    def __abs__(self):
        """abs(v) -- panjang/magnitudo vektor"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # -- In-place operator --
    def __iadd__(self, other):
        """v += other"""
        if isinstance(other, Vektor2D):
            self.x += other.x
            self.y += other.y
            return self
        return NotImplemented

    # -- Perbandingan --
    def __eq__(self, other):
        if isinstance(other, Vektor2D):
            return self.x == other.x and self.y == other.y
        return NotImplemented


# --- Demo ---
v1 = Vektor2D(3, 4)
v2 = Vektor2D(1, 2)

print(f"  v1           = {v1}")
print(f"  v2           = {v2}")
print(f"  v1 + v2      = {v1 + v2}")
print(f"  v1 - v2      = {v1 - v2}")
print(f"  v1 * 2       = {v1 * 2}")
print(f"  3 * v1       = {3 * v1}       (menggunakan __rmul__)")
print(f"  v1 / 2       = {v1 / 2}")
print(f"  -v1          = {-v1}     (menggunakan __neg__)")
print(f"  abs(v1)      = {abs(v1):.2f}      (panjang vektor 3-4-5)")

v3 = Vektor2D(1, 0)
v3 += Vektor2D(2, 3)
print(f"  v3 setelah +=: {v3}  (menggunakan __iadd__)")

print(f"  v1 == v1?    {v1 == Vektor2D(3, 4)}")
print(f"  v1 == v2?    {v1 == v2}")

# ======================================================================
# BAGIAN 2: Operator Perbandingan -- @total_ordering
#           Fokus: __eq__, __lt__ + @total_ordering untuk NilaiMahasiswa
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Operator Perbandingan -- @total_ordering")
print("=" * 60)


@total_ordering
class NilaiMahasiswa:
    """
    Merepresentasikan nilai akhir seorang mahasiswa untuk satu mata kuliah.
    Menggunakan @total_ordering -- cukup definisikan __eq__ dan __lt__,
    sisanya (__le__, __gt__, __ge__) dibuat otomatis.
    """

    SKALA = {
        (85, 100): ("A",  4.0),
        (70,  84): ("B",  3.0),
        (55,  69): ("C",  2.0),
        (40,  54): ("D",  1.0),
        ( 0,  39): ("E",  0.0),
    }

    def __init__(self, nim, nama_matkul, angka):
        if not (0 <= angka <= 100):
            raise ValueError(f"Nilai harus antara 0-100, bukan {angka}")
        self.nim        = nim
        self.nama_matkul = nama_matkul
        self.angka      = angka
        self.huruf, self.bobot = self._hitung_huruf(angka)

    @staticmethod
    def _hitung_huruf(angka):
        for (bawah, atas), (huruf, bobot) in NilaiMahasiswa.SKALA.items():
            if bawah <= angka <= atas:
                return huruf, bobot
        return "E", 0.0

    def __str__(self):
        return f"{self.nim} | {self.nama_matkul:30s} | {self.angka:3d} ({self.huruf})"

    def __repr__(self):
        return f"NilaiMahasiswa('{self.nim}', '{self.nama_matkul}', {self.angka})"

    # -- Dua method wajib untuk @total_ordering --
    def __eq__(self, other):
        if isinstance(other, NilaiMahasiswa):
            return self.angka == other.angka
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, NilaiMahasiswa):
            return self.angka < other.angka
        return NotImplemented

    # -- __hash__ harus didefinisikan ulang karena __eq__ sudah didefinisikan --
    def __hash__(self):
        return hash((self.nim, self.nama_matkul, self.angka))


# --- Demo ---
nilai_list = [
    NilaiMahasiswa("2301001", "Pemrograman Berorientasi Objek", 88),
    NilaiMahasiswa("2301042", "Pemrograman Berorientasi Objek", 72),
    NilaiMahasiswa("2301087", "Pemrograman Berorientasi Objek", 95),
    NilaiMahasiswa("2301103", "Pemrograman Berorientasi Objek", 61),
    NilaiMahasiswa("2301115", "Pemrograman Berorientasi Objek", 45),
]

print("  -- Nilai sebelum diurutkan --")
for n in nilai_list:
    print(f"    {n}")

# sorted() bekerja karena ada __lt__
terurut = sorted(nilai_list, reverse=True)
print()
print("  -- Nilai setelah sorted(reverse=True) --")
for i, n in enumerate(terurut, 1):
    print(f"    {i}. {n}")

terbaik = max(nilai_list)
terburuk = min(nilai_list)
print()
print(f"  Nilai tertinggi: {terbaik.angka} ({terbaik.huruf})")
print(f"  Nilai terendah : {terburuk.angka} ({terburuk.huruf})")

n1 = NilaiMahasiswa("2301001", "PBO", 88)
n2 = NilaiMahasiswa("2301042", "PBO", 72)
print()
print(f"  n1(88) > n2(72)  : {n1 > n2}")   # __gt__ dari @total_ordering
print(f"  n1(88) <= n2(72) : {n1 <= n2}")   # __le__ dari @total_ordering
print(f"  n1(88) >= n1(88) : {n1 >= n1}")   # __ge__ dari @total_ordering

# ======================================================================
# BAGIAN 3: Container Lanjutan -- KartuRencanaStudi (KRS)
#           Fokus: __getitem__, __setitem__, __delitem__, __contains__,
#                  __iter__, __len__, __reversed__
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 3: Container -- Kartu Rencana Studi (KRS)")
print("=" * 60)


class MataKuliahKRS:
    """Satu entri mata kuliah dalam KRS."""

    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks  = sks

    def __str__(self):
        return f"{self.kode} | {self.nama:35s} | {self.sks} SKS"

    def __repr__(self):
        return f"MataKuliahKRS('{self.kode}', '{self.nama}', {self.sks})"


class KartuRencanaStudi:
    """
    KRS mahasiswa -- container untuk mata kuliah yang diambil.
    Mendukung akses via index, penghapusan, iterasi, dan lebih.
    """

    MAKS_SKS = 24

    def __init__(self, nim, nama, semester):
        self.nim      = nim
        self.nama     = nama
        self.semester = semester
        self._matkul  = []    # list MataKuliahKRS

    @property
    def total_sks(self):
        return sum(mk.sks for mk in self._matkul)

    def tambah(self, matkul):
        """Menambahkan mata kuliah ke KRS."""
        if self.total_sks + matkul.sks > self.MAKS_SKS:
            print(f"  [!] Gagal tambah '{matkul.nama}': "
                  f"melebihi batas {self.MAKS_SKS} SKS")
            return False
        self._matkul.append(matkul)
        return True

    # -- Container Protocol --
    def __len__(self):
        """len(krs) -- jumlah mata kuliah yang diambil."""
        return len(self._matkul)

    def __getitem__(self, index):
        """krs[0] -- akses mata kuliah via index."""
        return self._matkul[index]

    def __setitem__(self, index, matkul):
        """krs[0] = matkul_baru -- ganti mata kuliah."""
        self._matkul[index] = matkul

    def __delitem__(self, index):
        """del krs[0] -- hapus mata kuliah dari KRS."""
        dihapus = self._matkul[index]
        del self._matkul[index]
        print(f"  [OK] '{dihapus.nama}' dihapus dari KRS")

    def __contains__(self, kode_mk):
        """'IF204' in krs -- cek apakah kode matkul ada."""
        return any(mk.kode == kode_mk for mk in self._matkul)

    def __iter__(self):
        """for mk in krs -- iterasi seluruh mata kuliah."""
        return iter(self._matkul)

    def __reversed__(self):
        """reversed(krs) -- iterasi dari belakang."""
        return reversed(self._matkul)

    def __bool__(self):
        """if krs -- True jika ada mata kuliah yang diambil."""
        return len(self._matkul) > 0

    def __str__(self):
        return (f"KRS {self.nim} - {self.nama} "
                f"(Sem {self.semester}) | {len(self)} MK | {self.total_sks} SKS")


# --- Demo ---
krs = KartuRencanaStudi("2301001", "Budi Santoso", 4)

mk_list = [
    MataKuliahKRS("IF201", "Algoritma dan Struktur Data",         3),
    MataKuliahKRS("IF204", "Pemrograman Berorientasi Objek",      3),
    MataKuliahKRS("IF207", "Basis Data",                          3),
    MataKuliahKRS("IF210", "Jaringan Komputer",                   3),
    MataKuliahKRS("MK101", "Kalkulus II",                         3),
    MataKuliahKRS("MK102", "Aljabar Linear",                      3),
]

print(f"  {krs}")
print()
for mk in mk_list:
    krs.tambah(mk)

print(f"  {krs}")
print()
print(f"  len(krs)       = {len(krs)}")
print(f"  krs[0]         = {krs[0]}")
print(f"  'IF204' in krs = {'IF204' in krs}")
print(f"  'IF999' in krs = {'IF999' in krs}")

print()
print("  -- Iterasi dengan for --")
for mk in krs:
    print(f"    {mk}")

print()
print("  -- Iterasi terbalik dengan reversed() --")
for mk in reversed(krs):
    print(f"    {mk}")

print()
print("  -- Hapus mata kuliah (del krs[4]) --")
del krs[4]
print(f"  {krs}")

# ======================================================================
# BAGIAN 4: Context Manager -- __enter__ dan __exit__
#           Fokus: membuat objek yang aman digunakan dengan 'with'
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 4: Context Manager -- __enter__ dan __exit__")
print("=" * 60)


class SesiUjian:
    """
    Merepresentasikan sesi ujian online.
    Menggunakan context manager untuk memastikan sesi selalu ditutup.
    """

    def __init__(self, kode_mk, nama_mk, nim_mahasiswa):
        self.kode_mk        = kode_mk
        self.nama_mk        = nama_mk
        self.nim_mahasiswa  = nim_mahasiswa
        self.aktif          = False
        self.jawaban        = []

    def __enter__(self):
        """Dipanggil saat masuk blok 'with' -- membuka sesi."""
        print(f"  [Sesi Dimulai] {self.nama_mk} -- Mahasiswa: {self.nim_mahasiswa}")
        self.aktif = True
        return self   # nilai yang diterima oleh 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Dipanggil saat keluar blok 'with' -- menutup sesi.
        exc_type, exc_val, exc_tb berisi info exception (None jika tidak ada).
        Kembalikan True untuk menekan exception, False untuk membiarkannya.
        """
        self.aktif = False
        if exc_type is not None:
            print(f"  [!] Sesi berakhir DENGAN ERROR: {exc_type.__name__}: {exc_val}")
            print(f"  [!] Jawaban yang sudah masuk ({len(self.jawaban)}) tetap disimpan")
            return False   # biarkan exception menyebar (jangan ditekan)
        else:
            print(f"  [Sesi Selesai] {len(self.jawaban)} jawaban berhasil disimpan")
            return False

    def jawab(self, nomor, jawaban):
        """Menyimpan jawaban mahasiswa."""
        if not self.aktif:
            raise RuntimeError("Tidak bisa menjawab di luar sesi aktif")
        self.jawaban.append({"nomor": nomor, "jawaban": jawaban})
        print(f"    Soal {nomor}: jawaban '{jawaban}' disimpan")

    def __str__(self):
        status = "Aktif" if self.aktif else "Tidak Aktif"
        return f"SesiUjian({self.kode_mk}, {self.nim_mahasiswa}, {status})"


# --- Demo 1: Sesi normal (tanpa error) ---
print("  -- Demo 1: Sesi ujian normal --")
with SesiUjian("IF204", "PBO", "2301001") as sesi:
    sesi.jawab(1, "Enkapsulasi menyembunyikan data internal")
    sesi.jawab(2, "Pewarisan memungkinkan kelas turunan")
    sesi.jawab(3, "Polimorfisme: satu antarmuka, banyak implementasi")

print(f"  Status setelah with: {sesi}")

# --- Demo 2: Sesi dengan error (sesi tetap ditutup) ---
print()
print("  -- Demo 2: Sesi dengan error di tengah jalan --")
try:
    with SesiUjian("IF201", "Algoritma", "2301042") as sesi2:
        sesi2.jawab(1, "Bubble sort O(n^2)")
        raise ConnectionError("Koneksi internet terputus!")   # simulasi error jaringan
except ConnectionError as e:
    print(f"  [Tertangkap] {e}")
    print(f"  Sesi berhasil ditutup meski ada error: {sesi2}")

print()
print("Selesai! Semua bagian dijalankan tanpa error.")
