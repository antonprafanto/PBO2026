"""
Kode Praktik - Materi 10: Exception Handling OOP
File: 03_studi_kasus.py
Topik: Penerapan exception handling pada dua sistem nyata

Jalankan: python 03_studi_kasus.py
"""

from contextlib import contextmanager

# ======================================================================
# SKENARIO 1: Sistem Pendaftaran KRS Online
# ----------------------------------------------------------------------
# Sistem pendaftaran KRS yang lengkap dengan hierarki exception,
# validasi berlapis, transaksi atomik, dan laporan hasil.
# ======================================================================
print("=" * 60)
print("SKENARIO 1: Sistem Pendaftaran KRS Online")
print("=" * 60)

# ------------------------------------------------------------------
# Definisi hierarki exception untuk sistem KRS
# ------------------------------------------------------------------

class KRSError(Exception):
    """Base exception untuk sistem KRS."""
    def __init__(self, pesan, kode=None):
        self.kode = kode
        super().__init__(pesan)

    def __str__(self):
        prefix = f"[{self.kode}] " if self.kode else ""
        return f"{prefix}{super().__str__()}"


class MahasiswaTidakAktifError(KRSError):
    def __init__(self, nim, status):
        self.nim    = nim
        self.status = status
        super().__init__(f"Mahasiswa {nim} berstatus '{status}', bukan Aktif", "KRS-001")


class TunggakanSPPError(KRSError):
    def __init__(self, nim, semester, jumlah):
        self.nim      = nim
        self.semester = semester
        self.jumlah   = jumlah
        super().__init__(
            f"Mahasiswa {nim} memiliki tunggakan SPP Semester {semester} "
            f"sebesar Rp {jumlah:,.0f}",
            "KRS-002"
        )


class KRSTerkunciError(KRSError):
    def __init__(self, nim, alasan):
        self.nim    = nim
        self.alasan = alasan
        super().__init__(f"KRS {nim} terkunci: {alasan}", "KRS-003")


class MataKuliahTidakAdaError(KRSError):
    def __init__(self, kode_mk):
        self.kode_mk = kode_mk
        super().__init__(f"Mata kuliah '{kode_mk}' tidak ditemukan", "KRS-004")


class KelasKapasitasPenuhError(KRSError):
    def __init__(self, kode_mk, kapasitas):
        self.kode_mk   = kode_mk
        self.kapasitas = kapasitas
        super().__init__(f"Kelas {kode_mk} sudah penuh ({kapasitas} mhs)", "KRS-005")


class PrasyaratBelumLulusError(KRSError):
    def __init__(self, kode_mk, kurang):
        self.kode_mk = kode_mk
        self.kurang  = kurang
        super().__init__(
            f"Prasyarat {kode_mk} belum terpenuhi: {', '.join(kurang)}",
            "KRS-006"
        )


class SKSMelebihiBatasError(KRSError):
    def __init__(self, nim, diminta, maks, sudah):
        self.nim      = nim
        self.diminta  = diminta
        self.maks     = maks
        self.sudah    = sudah
        super().__init__(
            f"Penambahan {diminta} SKS melebihi batas {maks} SKS "
            f"(sudah terdaftar {sudah} SKS)",
            "KRS-007"
        )


# ------------------------------------------------------------------
# Kelas-kelas sistem KRS
# ------------------------------------------------------------------

class MataKuliahKRS:
    def __init__(self, kode, nama, sks, kapasitas=40, prasyarat=None):
        self.kode      = kode
        self.nama      = nama
        self.sks       = sks
        self.kapasitas = kapasitas
        self.prasyarat = prasyarat or []
        self._peserta  = []

    @property
    def terisi(self):
        return len(self._peserta)

    def tambah_peserta(self, nim):
        self._peserta.append(nim)

    def __str__(self):
        return f"{self.kode} ({self.sks} SKS) [{self.terisi}/{self.kapasitas}]"


class DataMahasiswaKRS:
    def __init__(self, nim, nama, status, ipk, tunggakan=0, mk_lulus=None):
        self.nim       = nim
        self.nama      = nama
        self.status    = status    # "Aktif", "Cuti", "DO"
        self.ipk       = ipk
        self.tunggakan = tunggakan
        self.mk_lulus  = mk_lulus or []
        self.krs_aktif = []        # list kode MK yang sudah didaftarkan

    @property
    def total_sks_krs(self):
        return sum(mk.sks for mk in self.krs_aktif)

    @property
    def batas_sks(self):
        if self.ipk >= 3.0: return 24
        if self.ipk >= 2.5: return 21
        return 18

    def __str__(self):
        return f"[{self.nim}] {self.nama} (IPK {self.ipk:.2f})"


class SistemKRS:
    """Sistem pendaftaran KRS dengan validasi berlapis dan transaksi."""

    def __init__(self):
        self._katalog    = {}   # kode_mk -> MataKuliahKRS
        self._mahasiswa  = {}   # nim -> DataMahasiswaKRS
        self._log_error  = []

    def tambah_matkul(self, matkul):
        self._katalog[matkul.kode] = matkul

    def tambah_mahasiswa(self, mhs):
        self._mahasiswa[mhs.nim] = mhs

    @contextmanager
    def _transaksi(self, nim, kode_mk):
        """Context manager untuk atomisitas pendaftaran."""
        mhs = self._mahasiswa.get(nim)
        mk  = self._katalog.get(kode_mk)
        try:
            yield mhs, mk
        except KRSError as e:
            self._log_error.append({"nim": nim, "mk": kode_mk, "error": str(e)})
            raise

    def daftar(self, nim, kode_mk):
        """
        Mendaftarkan mahasiswa ke mata kuliah.
        Validasi berlapis dengan guard clauses.
        """
        with self._transaksi(nim, kode_mk) as (mhs, mk):
            # Guard 1: mahasiswa ada?
            if mhs is None:
                raise MataKuliahTidakAdaError(nim)

            # Guard 2: status aktif?
            if mhs.status != "Aktif":
                raise MahasiswaTidakAktifError(nim, mhs.status)

            # Guard 3: tunggakan?
            if mhs.tunggakan > 0:
                raise TunggakanSPPError(nim, "Ganjil 2025/2026", mhs.tunggakan)

            # Guard 4: mata kuliah ada?
            if mk is None:
                raise MataKuliahTidakAdaError(kode_mk)

            # Guard 5: kapasitas?
            if mk.terisi >= mk.kapasitas:
                raise KelasKapasitasPenuhError(kode_mk, mk.kapasitas)

            # Guard 6: prasyarat?
            kurang = [p for p in mk.prasyarat if p not in mhs.mk_lulus]
            if kurang:
                raise PrasyaratBelumLulusError(kode_mk, kurang)

            # Guard 7: batas SKS?
            if mhs.total_sks_krs + mk.sks > mhs.batas_sks:
                raise SKSMelebihiBatasError(
                    nim, mk.sks, mhs.batas_sks, mhs.total_sks_krs
                )

            # Semua valid -- daftarkan
            mk.tambah_peserta(nim)
            mhs.krs_aktif.append(mk)
            return True

    def cetak_ringkasan(self):
        """Cetak ringkasan hasil pendaftaran semua mahasiswa."""
        print("\n  -- Ringkasan KRS --")
        for nim, mhs in self._mahasiswa.items():
            print(f"  {mhs} | {mhs.total_sks_krs}/{mhs.batas_sks} SKS")
            for mk in mhs.krs_aktif:
                print(f"    + {mk.nama} ({mk.sks} SKS)")

        if self._log_error:
            print(f"\n  -- Log Error ({len(self._log_error)} gagal) --")
            for log in self._log_error:
                print(f"  NIM {log['nim']} -> {log['mk']}: {log['error']}")


# --- Setup sistem ---
sistem = SistemKRS()

# Katalog mata kuliah
for mk in [
    MataKuliahKRS("IF101", "Pemrograman Dasar",                   3),
    MataKuliahKRS("IF201", "Algoritma dan Struktur Data",          3, prasyarat=["IF101"]),
    MataKuliahKRS("IF204", "Pemrograman Berorientasi Objek",       3, prasyarat=["IF101"]),
    MataKuliahKRS("IF207", "Basis Data",                           3, prasyarat=["IF201"]),
    MataKuliahKRS("IF210", "Jaringan Komputer",                    3, kapasitas=2),
    MataKuliahKRS("MK102", "Kalkulus II",                          4),
]:
    sistem.tambah_matkul(mk)

# Data mahasiswa
for mhs in [
    DataMahasiswaKRS("2301001", "Budi Santoso",   "Aktif", 3.75, 0,
                     mk_lulus=["IF101", "IF201"]),
    DataMahasiswaKRS("2301042", "Sari Dewi",      "Aktif", 2.60, 2_000_000,
                     mk_lulus=["IF101"]),
    DataMahasiswaKRS("2301087", "Ahmad Fauzi",    "Cuti",  3.20, 0,
                     mk_lulus=["IF101", "IF201"]),
    DataMahasiswaKRS("2301103", "Deni Kurniawan", "Aktif", 3.50, 0,
                     mk_lulus=["IF101"]),
    DataMahasiswaKRS("2301115", "Reza Pratama",   "Aktif", 3.10, 0,
                     mk_lulus=["IF101"]),
]:
    sistem.tambah_mahasiswa(mhs)

# --- Proses pendaftaran ---
print()
pendaftaran = [
    ("2301001", "IF204"),   # harus berhasil
    ("2301001", "IF207"),   # harus berhasil (sudah lulus IF201)
    ("2301001", "MK102"),   # harus berhasil
    ("2301042", "IF204"),   # GAGAL: tunggakan SPP
    ("2301087", "IF204"),   # GAGAL: status Cuti
    ("2301103", "IF207"),   # GAGAL: prasyarat IF201 belum lulus
    ("2301103", "IF204"),   # berhasil
    ("2301115", "IF210"),   # berhasil (slot 1/2)
    ("2301001", "IF210"),   # berhasil (slot 2/2)
    ("2301103", "IF210"),   # GAGAL: kapasitas penuh
]

for nim, kode_mk in pendaftaran:
    nama = sistem._mahasiswa.get(nim, type("", (), {"nama": "?"})()).nama \
           if nim in sistem._mahasiswa else "?"
    mk_nama = sistem._katalog[kode_mk].nama if kode_mk in sistem._katalog else kode_mk
    try:
        sistem.daftar(nim, kode_mk)
        print(f"  [OK]    {nim} ({nama:15s}) -> {kode_mk} ({mk_nama})")
    except KRSError as e:
        print(f"  [GAGAL] {nim} ({nama:15s}) -> {kode_mk}: {e}")

sistem.cetak_ringkasan()

# ======================================================================
# SKENARIO 2: Sistem Input Nilai Mahasiswa
# ----------------------------------------------------------------------
# Sistem import nilai dari berbagai sumber (manual, CSV, API)
# dengan validasi dan pelaporan error terstruktur.
# ======================================================================
print()
print("=" * 60)
print("SKENARIO 2: Sistem Input Nilai Mahasiswa")
print("=" * 60)


class NilaiError(Exception):
    """Base exception sistem nilai."""
    pass

class FormatNilaiError(NilaiError):
    def __init__(self, baris, kolom, nilai, alasan):
        self.baris  = baris
        self.kolom  = kolom
        self.nilai  = nilai
        self.alasan = alasan
        super().__init__(
            f"Baris {baris}, Kolom '{kolom}': nilai '{nilai}' tidak valid -- {alasan}"
        )

class NIMTidakTerdaftarError(NilaiError):
    def __init__(self, nim, kode_mk):
        self.nim     = nim
        self.kode_mk = kode_mk
        super().__init__(f"NIM '{nim}' tidak terdaftar di kelas {kode_mk}")

class NilaiDuplikatError(NilaiError):
    def __init__(self, nim, kode_mk):
        self.nim     = nim
        self.kode_mk = kode_mk
        super().__init__(f"Nilai {nim} di {kode_mk} sudah pernah diinput sebelumnya")


class ProsesInputNilai:
    """Memproses batch input nilai dari berbagai sumber."""

    def __init__(self, kode_mk, peserta_terdaftar):
        self.kode_mk           = kode_mk
        self.peserta_terdaftar = set(peserta_terdaftar)
        self._nilai            = {}   # nim -> nilai
        self.laporan = {"berhasil": 0, "gagal": 0, "error_list": []}

    def _validasi_baris(self, baris_ke, nim, nilai_str):
        """Validasi satu baris data nilai."""
        # Validasi NIM
        if not isinstance(nim, str) or not nim.strip():
            raise FormatNilaiError(baris_ke, "nim", nim, "NIM tidak boleh kosong")

        nim = nim.strip()

        if not nim.isdigit() or len(nim) != 7:
            raise FormatNilaiError(baris_ke, "nim", nim, "Format NIM harus 7 digit angka")

        # Validasi nilai
        try:
            nilai = float(nilai_str)
        except (ValueError, TypeError):
            raise FormatNilaiError(baris_ke, "nilai", nilai_str,
                                   "Nilai harus berupa angka") from None

        if not (0.0 <= nilai <= 100.0):
            raise FormatNilaiError(baris_ke, "nilai", nilai_str,
                                   f"Nilai harus 0-100, bukan {nilai}")

        # Validasi keberadaan NIM di kelas
        if nim not in self.peserta_terdaftar:
            raise NIMTidakTerdaftarError(nim, self.kode_mk)

        # Validasi duplikat
        if nim in self._nilai:
            raise NilaiDuplikatError(nim, self.kode_mk)

        return nim, nilai

    def proses_batch(self, data_nilai):
        """
        Proses list data nilai. Setiap baris diproses independen --
        error di satu baris tidak menghentikan baris lainnya.
        data_nilai: list of dict {"nim": ..., "nilai": ...}
        """
        print(f"\n  Memproses {len(data_nilai)} baris nilai untuk {self.kode_mk}...")

        for i, baris in enumerate(data_nilai, 1):
            nim_raw   = baris.get("nim", "")
            nilai_raw = baris.get("nilai", "")
            try:
                nim, nilai = self._validasi_baris(i, nim_raw, nilai_raw)
                self._nilai[nim] = nilai
                self.laporan["berhasil"] += 1
            except (FormatNilaiError, NIMTidakTerdaftarError, NilaiDuplikatError) as e:
                self.laporan["gagal"] += 1
                self.laporan["error_list"].append(str(e))

    def cetak_laporan(self):
        """Cetak laporan hasil proses batch."""
        total = self.laporan["berhasil"] + self.laporan["gagal"]
        print(f"\n  -- Laporan Input Nilai {self.kode_mk} --")
        print(f"  Total data : {total}")
        print(f"  Berhasil   : {self.laporan['berhasil']}")
        print(f"  Gagal      : {self.laporan['gagal']}")

        if self.laporan["error_list"]:
            print(f"\n  Error detail:")
            for err in self.laporan["error_list"]:
                print(f"    - {err}")

        if self._nilai:
            print(f"\n  Nilai tersimpan:")
            for nim, nilai in sorted(self._nilai.items()):
                huruf = self._ke_huruf(nilai)
                print(f"    {nim}: {nilai:.1f} ({huruf})")

    @staticmethod
    def _ke_huruf(nilai):
        if nilai >= 85: return "A"
        if nilai >= 70: return "B"
        if nilai >= 55: return "C"
        if nilai >= 40: return "D"
        return "E"


# --- Demo ---
peserta_if204 = ["2301001", "2301042", "2301087", "2301103", "2301115"]
proses = ProsesInputNilai("IF204", peserta_if204)

data_input = [
    {"nim": "2301001", "nilai": "88"},      # valid
    {"nim": "2301042", "nilai": "75"},      # valid
    {"nim": "2301087", "nilai": "95"},      # valid
    {"nim": "2301103", "nilai": "tujuh"},   # FormatNilaiError: bukan angka
    {"nim": "2301115", "nilai": "110"},     # FormatNilaiError: di luar 0-100
    {"nim": "2301999", "nilai": "80"},      # NIMTidakTerdaftarError
    {"nim": "2301001", "nilai": "90"},      # NilaiDuplikatError
    {"nim": "",        "nilai": "70"},      # FormatNilaiError: NIM kosong
    {"nim": "2301103", "nilai": "61"},      # valid (setelah error sebelumnya)
]

proses.proses_batch(data_input)
proses.cetak_laporan()

print()
print("Selesai! Semua skenario dijalankan tanpa error.")
