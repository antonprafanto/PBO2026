"""
Kode Praktik - Materi 09: Magic Methods (Metode Ajaib)
File: 03_studi_kasus.py
Topik: Penerapan magic methods pada dua sistem nyata

Jalankan: python 03_studi_kasus.py
"""

from functools import total_ordering

# ======================================================================
# SKENARIO 1: Sistem Nilai Akademik -- Kelas Transkrip
# ----------------------------------------------------------------------
# Mendemonstrasikan magic methods untuk membuat sistem transkrip
# yang "terasa" seperti tipe data bawaan Python.
#
# Magic methods yang digunakan:
#   __str__, __repr__, __len__, __bool__, __iter__,
#   __getitem__, __contains__, __iadd__, __add__
# ======================================================================
print("=" * 60)
print("SKENARIO 1: Sistem Nilai Akademik -- Transkrip")
print("=" * 60)


@total_ordering
class MataKuliahNilai:
    """Satu entri mata kuliah beserta nilai dalam transkrip."""

    def __init__(self, kode, nama, sks, nilai_angka):
        self.kode        = kode
        self.nama        = nama
        self.sks         = sks
        self.nilai_angka = nilai_angka
        self.nilai_huruf = self._hitung_huruf(nilai_angka)
        self.bobot_mutu  = self._hitung_bobot(nilai_angka)

    @staticmethod
    def _hitung_huruf(angka):
        if angka >= 85: return "A"
        if angka >= 70: return "B"
        if angka >= 55: return "C"
        if angka >= 40: return "D"
        return "E"

    @staticmethod
    def _hitung_bobot(angka):
        if angka >= 85: return 4.0
        if angka >= 70: return 3.0
        if angka >= 55: return 2.0
        if angka >= 40: return 1.0
        return 0.0

    def __str__(self):
        return (f"  {self.kode:7s} | {self.nama:35s} | "
                f"{self.sks} SKS | {self.nilai_angka:3d} ({self.nilai_huruf})")

    def __repr__(self):
        return (f"MataKuliahNilai('{self.kode}', '{self.nama}', "
                f"{self.sks}, {self.nilai_angka})")

    # Perbandingan berdasarkan nilai angka
    def __eq__(self, other):
        if isinstance(other, MataKuliahNilai):
            return self.nilai_angka == other.nilai_angka
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, MataKuliahNilai):
            return self.nilai_angka < other.nilai_angka
        return NotImplemented

    def __hash__(self):
        return hash((self.kode, self.nilai_angka))


class Transkrip:
    """
    Transkrip akademik mahasiswa -- kumpulan nilai semua mata kuliah.

    Mendukung:
    - len(transkrip)              -> jumlah mata kuliah
    - if transkrip:               -> True jika ada data
    - transkrip += mk_nilai       -> tambah mata kuliah
    - transkrip[0]                -> akses mata kuliah ke-0
    - 'IF204' in transkrip        -> cek kode matkul
    - for mk in transkrip:        -> iterasi semua mata kuliah
    - transkrip_a + transkrip_b   -> gabungkan dua transkrip
    """

    def __init__(self, nim, nama):
        self.nim      = nim
        self.nama     = nama
        self._entri   = []   # list MataKuliahNilai

    # ---- Properti kalkulasi ----
    @property
    def total_sks(self):
        return sum(mk.sks for mk in self._entri)

    @property
    def ips(self):
        """Indeks Prestasi Semester (semua entri yang ada)."""
        if not self._entri:
            return 0.0
        total_bobot = sum(mk.bobot_mutu * mk.sks for mk in self._entri)
        return total_bobot / self.total_sks

    # ---- Magic Methods: Representasi ----
    def __str__(self):
        predikat = self._predikat(self.ips)
        return (f"Transkrip [{self.nim}] {self.nama} | "
                f"{len(self)} MK | IPS: {self.ips:.2f} ({predikat})")

    def __repr__(self):
        return f"Transkrip(nim='{self.nim}', nama='{self.nama}', entri={len(self)})"

    @staticmethod
    def _predikat(ips):
        if ips >= 3.75: return "Cumlaude"
        if ips >= 3.00: return "Sangat Memuaskan"
        if ips >= 2.75: return "Memuaskan"
        if ips >= 2.00: return "Cukup"
        return "Kurang"

    # ---- Magic Methods: Ukuran & Boolean ----
    def __len__(self):
        """len(transkrip) -> jumlah mata kuliah."""
        return len(self._entri)

    def __bool__(self):
        """if transkrip -> True jika ada entri."""
        return len(self._entri) > 0

    # ---- Magic Methods: Container ----
    def __iter__(self):
        """for mk in transkrip"""
        return iter(self._entri)

    def __getitem__(self, index):
        """transkrip[0] atau transkrip[1:3]"""
        return self._entri[index]

    def __contains__(self, kode_mk):
        """'IF204' in transkrip"""
        return any(mk.kode == kode_mk for mk in self._entri)

    # ---- Magic Methods: Penambahan ----
    def __iadd__(self, mk_nilai):
        """transkrip += mk_nilai"""
        if not isinstance(mk_nilai, MataKuliahNilai):
            return NotImplemented
        # Cek duplikat
        if mk_nilai.kode in self:
            print(f"  [!] Kode '{mk_nilai.kode}' sudah ada, nilai diperbarui")
            for i, mk in enumerate(self._entri):
                if mk.kode == mk_nilai.kode:
                    self._entri[i] = mk_nilai
                    return self
        self._entri.append(mk_nilai)
        return self

    def __add__(self, other):
        """transkrip_a + transkrip_b -- gabungkan dua transkrip."""
        if not isinstance(other, Transkrip):
            return NotImplemented
        hasil = Transkrip(self.nim, self.nama)
        for mk in self:
            hasil += mk
        for mk in other:
            hasil += mk
        return hasil

    def cetak_detail(self):
        """Cetak transkrip lengkap."""
        print(f"  {'=' * 56}")
        print(f"  TRANSKRIP AKADEMIK")
        print(f"  NIM  : {self.nim}")
        print(f"  Nama : {self.nama}")
        print(f"  {'=' * 56}")
        print(f"  {'Kode':7s} | {'Mata Kuliah':35s} | SKS | Nilai")
        print(f"  {'-' * 56}")
        for mk in sorted(self, reverse=True):   # diurutkan dari nilai terbaik
            print(mk)
        print(f"  {'-' * 56}")
        print(f"  Total SKS : {self.total_sks}")
        print(f"  IPS       : {self.ips:.2f} -- {self._predikat(self.ips)}")
        print(f"  {'=' * 56}")


# --- Demo ---
print()
print("  Membuat transkrip Semester 4 -- Budi Santoso")
print()

t_budi = Transkrip("2301001", "Budi Santoso")

# Tambahkan mata kuliah dengan +=
t_budi += MataKuliahNilai("IF201", "Algoritma dan Struktur Data",       3, 88)
t_budi += MataKuliahNilai("IF204", "Pemrograman Berorientasi Objek",    3, 92)
t_budi += MataKuliahNilai("IF207", "Basis Data",                        3, 78)
t_budi += MataKuliahNilai("IF210", "Jaringan Komputer",                 3, 81)
t_budi += MataKuliahNilai("MK102", "Kalkulus II",                       4, 70)
t_budi += MataKuliahNilai("MK103", "Statistika",                        3, 85)

t_budi.cetak_detail()

print()
print("  -- Demo magic methods --")
print(f"  len(t_budi)        = {len(t_budi)}")
print(f"  bool(t_budi)       = {bool(t_budi)}")
print(f"  'IF204' in t_budi  = {'IF204' in t_budi}")
print(f"  'IF999' in t_budi  = {'IF999' in t_budi}")
print(f"  t_budi[0]          = {t_budi[0]}")

print()
print("  -- Slice: t_budi[0:2] --")
for mk in t_budi[0:2]:
    print(f"    {mk}")

print()
print("  -- Gabungkan dua transkrip (semester 3 + semester 4) --")
t_sem3 = Transkrip("2301001", "Budi Santoso")
t_sem3 += MataKuliahNilai("IF101", "Pemrograman Dasar",                 3, 90)
t_sem3 += MataKuliahNilai("IF104", "Struktur Diskrit",                  3, 82)

t_gabung = t_sem3 + t_budi
print(f"  Semester 3 : {t_sem3}")
print(f"  Semester 4 : {t_budi}")
print(f"  Gabungan   : {t_gabung}")

# ======================================================================
# SKENARIO 2: Sistem Jadwal Kuliah -- JadwalHarian
# ----------------------------------------------------------------------
# Sistem penjadwalan yang memanfaatkan magic methods untuk membuat
# kelas jadwal yang intuitif dan mudah dimanipulasi.
#
# Magic methods yang digunakan:
#   __str__, __repr__, __len__, __bool__, __iter__,
#   __getitem__, __contains__, __add__, __mul__,
#   __enter__, __exit__, __call__
# ======================================================================
print()
print("=" * 60)
print("SKENARIO 2: Sistem Jadwal Kuliah")
print("=" * 60)


class SlotWaktu:
    """Merepresentasikan satu slot waktu (jam mulai - jam selesai)."""

    def __init__(self, jam_mulai, jam_selesai):
        """Contoh: SlotWaktu(8, 10) = pukul 08.00--10.00"""
        self.jam_mulai   = jam_mulai
        self.jam_selesai = jam_selesai

    def __str__(self):
        return f"{self.jam_mulai:02d}.00--{self.jam_selesai:02d}.00"

    def __repr__(self):
        return f"SlotWaktu({self.jam_mulai}, {self.jam_selesai})"

    def __eq__(self, other):
        if isinstance(other, SlotWaktu):
            return (self.jam_mulai == other.jam_mulai and
                    self.jam_selesai == other.jam_selesai)
        return NotImplemented

    def __hash__(self):
        return hash((self.jam_mulai, self.jam_selesai))

    def bentrok_dengan(self, other):
        """Cek apakah dua slot waktu beririsan."""
        return not (self.jam_selesai <= other.jam_mulai or
                    other.jam_selesai <= self.jam_mulai)


class EntriJadwal:
    """Satu entri dalam jadwal: mata kuliah, ruang, dan waktu."""

    def __init__(self, kode_mk, nama_mk, ruang, slot):
        self.kode_mk = kode_mk
        self.nama_mk = nama_mk
        self.ruang   = ruang
        self.slot    = slot

    def __str__(self):
        return (f"{str(self.slot):14s} | {self.kode_mk:7s} | "
                f"{self.nama_mk:35s} | Ruang {self.ruang}")

    def __repr__(self):
        return (f"EntriJadwal('{self.kode_mk}', '{self.nama_mk}', "
                f"'{self.ruang}', {repr(self.slot)})")


class JadwalHarian:
    """
    Jadwal kuliah untuk satu hari.

    Magic Methods:
    - __len__       : len(jadwal) -> jumlah sesi
    - __bool__      : if jadwal -> ada kelas hari ini
    - __iter__      : for sesi in jadwal
    - __getitem__   : jadwal[0] atau jadwal[1:3]
    - __contains__  : 'IF204' in jadwal -> ada matkul ini?
    - __add__       : jadwal_pagi + jadwal_siang -> gabungkan
    - __mul__       : jadwal * 5 -> jadwal berlaku 5 minggu
    - __str__       : tampilan jadwal
    - __repr__      : representasi teknis
    - __enter__     : buka sesi hari ini
    - __exit__      : tutup sesi hari ini
    - __call__      : jadwal('IF204') -> cari entri matkul tertentu
    """

    def __init__(self, hari, tanggal=""):
        self.hari    = hari
        self.tanggal = tanggal
        self._entri  = []   # list EntriJadwal

    def tambah(self, entri):
        """Menambahkan entri ke jadwal, cek bentrok waktu."""
        for existing in self._entri:
            if existing.slot.bentrok_dengan(entri.slot):
                print(f"  [!] Bentrok waktu: '{entri.nama_mk}' "
                      f"dengan '{existing.nama_mk}' pada {entri.slot}")
                return False
        self._entri.append(entri)
        return True

    # -- Representasi --
    def __str__(self):
        tgl = f" ({self.tanggal})" if self.tanggal else ""
        return f"Jadwal {self.hari}{tgl} -- {len(self)} sesi"

    def __repr__(self):
        return f"JadwalHarian('{self.hari}', tanggal='{self.tanggal}', entri={len(self)})"

    # -- Ukuran & Boolean --
    def __len__(self):
        return len(self._entri)

    def __bool__(self):
        return len(self._entri) > 0

    # -- Container --
    def __iter__(self):
        return iter(sorted(self._entri, key=lambda e: e.slot.jam_mulai))

    def __getitem__(self, index):
        entri_urut = sorted(self._entri, key=lambda e: e.slot.jam_mulai)
        return entri_urut[index]

    def __contains__(self, kode_mk):
        return any(e.kode_mk == kode_mk for e in self._entri)

    # -- Aritmatika --
    def __add__(self, other):
        """Gabungkan dua jadwal menjadi satu."""
        if not isinstance(other, JadwalHarian):
            return NotImplemented
        gabung = JadwalHarian(f"{self.hari}+{other.hari}")
        for e in self._entri:
            gabung.tambah(e)
        for e in other._entri:
            gabung.tambah(e)
        return gabung

    def __mul__(self, minggu):
        """jadwal * 5 -- hitung total sesi dalam N minggu."""
        if isinstance(minggu, int):
            return len(self) * minggu
        return NotImplemented

    def __rmul__(self, minggu):
        return self.__mul__(minggu)

    # -- Context Manager --
    def __enter__(self):
        print(f"  [Mulai] Hari {self.hari} -- {len(self)} kelas terjadwal")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"  [Selesai] Hari {self.hari} berakhir")
        return False

    # -- Callable: cari entri berdasarkan kode matkul --
    def __call__(self, kode_mk):
        """jadwal('IF204') -> entri matkul IF204 atau None."""
        for e in self._entri:
            if e.kode_mk == kode_mk:
                return e
        return None


# --- Demo ---
print()
jadwal_senin = JadwalHarian("Senin", "5 Mei 2026")
jadwal_selasa = JadwalHarian("Selasa", "6 Mei 2026")

sesi_senin = [
    EntriJadwal("IF201", "Algoritma dan Struktur Data",      "Lab A",  SlotWaktu(8,  10)),
    EntriJadwal("IF204", "Pemrograman Berorientasi Objek",   "Lab B",  SlotWaktu(10, 12)),
    EntriJadwal("MK102", "Kalkulus II",                      "Gdg B",  SlotWaktu(13, 15)),
]

sesi_selasa = [
    EntriJadwal("IF207", "Basis Data",                       "Lab A",  SlotWaktu(8,  10)),
    EntriJadwal("IF210", "Jaringan Komputer",                "Lab C",  SlotWaktu(10, 12)),
]

for s in sesi_senin:
    jadwal_senin.tambah(s)
for s in sesi_selasa:
    jadwal_selasa.tambah(s)

print(f"  {jadwal_senin}")
print(f"  {jadwal_selasa}")

print()
print("  -- Context manager: jalankan hari Senin --")
with jadwal_senin as j:
    print(f"  Sesi hari ini:")
    for entri in j:
        print(f"    {entri}")

print()
print("  -- Magic methods lainnya --")
print(f"  len(jadwal_senin)       = {len(jadwal_senin)}")
print(f"  'IF204' in jadwal_senin = {'IF204' in jadwal_senin}")
print(f"  'IF999' in jadwal_senin = {'IF999' in jadwal_senin}")
print(f"  jadwal_senin[0]         = {jadwal_senin[0]}")
print(f"  jadwal_senin * 16       = {jadwal_senin * 16} sesi dalam 16 minggu")

print()
cari = jadwal_senin("IF204")    # menggunakan __call__
if cari:
    print(f"  jadwal_senin('IF204') -> {cari}")
else:
    print("  Tidak ditemukan")

print()
print("  -- Gabungkan jadwal dua hari (__add__) --")
jadwal_gabung = jadwal_senin + jadwal_selasa
print(f"  {jadwal_gabung}")
for entri in jadwal_gabung:
    print(f"    {entri}")

print()
print("  -- Coba tambah jadwal dengan waktu bentrok --")
bentrok = EntriJadwal("IF999", "Kuliah Bentrok",  "Lab A",  SlotWaktu(9, 11))
jadwal_senin.tambah(bentrok)   # harus ditolak karena 09.00--11.00 bentrok dengan 08.00--10.00

print()
print("Selesai! Semua skenario dijalankan tanpa error.")
