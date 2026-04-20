"""
Kode Praktik - Materi 06: Pewarisan (Inheritance)
File: 03_studi_kasus.py
Topik: Studi kasus industri - Sistem Akademik & Sistem Kendaraan Rental

Jalankan: python 03_studi_kasus.py
"""

# ======================================================================
# STUDI KASUS 1: Sistem Akademik Lengkap
# Hierarki: Pengguna -> Mahasiswa / Dosen / Admin
# ======================================================================
print("=" * 60)
print("STUDI KASUS 1: Sistem Akademik")
print("=" * 60)

class Pengguna:
    """Kelas dasar semua akun di sistem akademik."""
    _total = 0

    def __init__(self, nama, email, password):
        Pengguna._total += 1
        self.id        = f"USR-{Pengguna._total:04d}"
        self.nama      = nama.strip().title()
        self.email     = email.lower().strip()
        self.__password = password
        self._aktif    = True
        self._log_aksi = []

    # -- Autentikasi ---------------------------------------------
    def login(self, password):
        if not self._aktif:
            print(f"  [X] Akun {self.nama} tidak aktif!")
            return False
        if password != self.__password:
            print(f"  [X] Password salah untuk akun {self.email}")
            return False
        self._catat("LOGIN")
        print(f"  [OK] {self.nama} berhasil login.")
        return True

    def logout(self):
        self._catat("LOGOUT")
        print(f"  [--] {self.nama} logout.")

    def ganti_password(self, lama, baru):
        if lama != self.__password:
            print("  [X] Password lama salah!")
            return
        self.__password = baru
        self._catat("GANTI_PASSWORD")
        print("  [OK] Password berhasil diubah.")

    def nonaktifkan(self):
        self._aktif = False
        self._catat("NONAKTIF")
        print(f"  [!] Akun {self.nama} dinonaktifkan.")

    def _catat(self, aksi):
        from datetime import datetime
        self._log_aksi.append(f"[{datetime.now().strftime('%H:%M:%S')}] {aksi}")

    @property
    def aktif(self):
        return self._aktif

    @property
    def log(self):
        return self._log_aksi.copy()

    def __str__(self):
        status = "[OK] Aktif" if self._aktif else "[X] Nonaktif"
        return f"[{self.id}] {self.nama} | {self.email} | {status}"


class Mahasiswa(Pengguna):
    def __init__(self, nama, email, password, nim, prodi):
        super().__init__(nama, email, password)
        self.nim       = nim
        self.prodi     = prodi
        self._ipk      = 0.0
        self._skripsi_selesai = False
        self._krs      = []
        self._transkrip = {}   # {matkul: nilai}

    @property
    def ipk(self):
        return self._ipk

    @ipk.setter
    def ipk(self, nilai):
        if not (0.0 <= nilai <= 4.0):
            raise ValueError(f"IPK harus 0.0-4.0, dapat: {nilai}")
        self._ipk = round(nilai, 2)

    @property
    def predikat(self):
        if self._ipk >= 3.51: return "Cum Laude"
        if self._ipk >= 3.01: return "Sangat Memuaskan"
        if self._ipk >= 2.76: return "Memuaskan"
        return "Cukup"

    def daftar_krs(self, matkul_list):
        self._krs = list(matkul_list)
        self._catat(f"DAFTAR_KRS: {', '.join(matkul_list)}")
        print(f"\n  [{self.nim}] KRS {self.nama} ({self.prodi}):")
        for mk in self._krs:
            print(f"    - {mk}")

    def input_nilai(self, matkul, nilai):
        if matkul not in self._krs:
            print(f"  [!] {matkul} tidak ada di KRS!")
            return
        self._transkrip[matkul] = nilai
        print(f"  [*] Nilai {matkul}: {nilai}")

    def tampilkan_transkrip(self):
        print(f"\n  === Transkrip {self.nama} ({self.nim}) ===")
        for mk, nilai in self._transkrip.items():
            print(f"    {mk:<25} : {nilai}")
        print(f"    {'IPK':<25} : {self._ipk:.2f} ({self.predikat})")

    def selesaikan_skripsi(self):
        self._skripsi_selesai = True
        self._catat("SKRIPSI_SELESAI")
        print(f"  [S] {self.nama} telah menyelesaikan skripsi!")

    def __str__(self):
        return (f"Mahasiswa | {super().__str__()} | "
                f"NIM: {self.nim} | IPK: {self._ipk:.2f} ({self.predikat})")


class Dosen(Pengguna):
    def __init__(self, nama, email, password, nip, jabatan="Asisten Ahli"):
        super().__init__(nama, email, password)
        self.nip      = nip
        self.jabatan  = jabatan
        self._matkul_diampu = []

    def tambah_matkul(self, matkul, sks):
        self._matkul_diampu.append({"nama": matkul, "sks": sks})
        print(f"  [+] {self.nama} ditugaskan: {matkul} ({sks} SKS)")

    def ajar(self, matkul, ruangan, jam):
        ada = any(m["nama"] == matkul for m in self._matkul_diampu)
        if not ada:
            print(f"  [!] {matkul} bukan matkul {self.nama}!")
            return
        print(f"  [~] [{self.nip}] {self.nama} mengajar '{matkul}' | {ruangan} | {jam}")

    def promosi(self, jabatan_baru):
        print(f"  [*] {self.nama}: {self.jabatan} -> {jabatan_baru}")
        self.jabatan = jabatan_baru

    @property
    def beban_sks(self):
        return sum(m["sks"] for m in self._matkul_diampu)

    def __str__(self):
        return (f"Dosen | {super().__str__()} | "
                f"NIP: {self.nip} | {self.jabatan} | "
                f"Beban: {self.beban_sks} SKS")


class Admin(Pengguna):
    def __init__(self, nama, email, password, level=1):
        super().__init__(nama, email, password)
        self.level = level

    def reset_password_pengguna(self, pengguna, password_baru):
        if self.level < 2:
            print("  [X] Level admin tidak cukup untuk reset password!")
            return
        pengguna._Pengguna__password = password_baru
        self._catat(f"RESET_PASSWORD: {pengguna.email}")
        print(f"  [OK] Password {pengguna.nama} berhasil direset oleh {self.nama}.")

    def __str__(self):
        return f"Admin (Level {self.level}) | {super().__str__()}"


# -- Demo Studi Kasus 1 -------------------------------------------
print("\n  -- Setup Pengguna --")
mhs1 = Mahasiswa("budi santoso", "budi@unmul.ac.id", "budi123",
                 "2301001", "Informatika")
mhs2 = Mahasiswa("sari dewi",   "sari@unmul.ac.id", "sari456",
                 "2301002", "Informatika")
dos1 = Dosen("dr. anton prafanto", "anton@unmul.ac.id", "anton789",
             "NIP001", "Lektor")
adm  = Admin("admin unmul", "admin@unmul.ac.id", "admin999", level=2)

print()
print("  -- Login & Aktivitas --")
mhs1.login("budi123")
mhs1.daftar_krs(["PBO", "Basis Data", "Kalkulus II", "Sistem Operasi"])
mhs1.input_nilai("PBO", "A")
mhs1.input_nilai("Basis Data", "B+")
mhs1.ipk = 3.78
mhs1.tampilkan_transkrip()

print()
dos1.login("anton789")
dos1.tambah_matkul("PBO", 3)
dos1.tambah_matkul("Basis Data", 3)
dos1.ajar("PBO", "Lab Pemrograman 2", "Senin 08:00")
dos1.promosi("Lektor Kepala")

print()
print("  -- Verifikasi isinstance / issubclass --")
print(f"  mhs1 adalah Mahasiswa? {isinstance(mhs1, Mahasiswa)}")
print(f"  mhs1 adalah Pengguna?  {isinstance(mhs1, Pengguna)}")
print(f"  dos1 adalah Mahasiswa? {isinstance(dos1, Mahasiswa)}")
print(f"  Mahasiswa subclass Pengguna? {issubclass(Mahasiswa, Pengguna)}")
print(f"  Admin subclass Dosen?        {issubclass(Admin, Dosen)}")

print()
print("  -- Informasi Semua Pengguna --")
for p in [mhs1, mhs2, dos1, adm]:
    print(f"  {p}")

print(f"\n  Total pengguna: {Pengguna._total}")


# ======================================================================
# STUDI KASUS 2: Sistem Rental Kendaraan
# Hierarki: Kendaraan -> Mobil / Motor / Truk
# ======================================================================
print("\n" + "=" * 60)
print("STUDI KASUS 2: Sistem Rental Kendaraan")
print("=" * 60)

class Kendaraan:
    """Kelas dasar kendaraan untuk sistem rental."""
    def __init__(self, plat, merk, model, tahun, tarif_per_hari):
        self.plat          = plat.upper()
        self.merk          = merk
        self.model         = model
        self.tahun         = tahun
        self.tarif_per_hari = tarif_per_hari
        self._tersedia     = True
        self._km           = 0

    @property
    def tersedia(self):
        return self._tersedia

    def hitung_biaya(self, hari):
        """Dapat di-override oleh subkelas untuk logika harga berbeda."""
        return self.tarif_per_hari * hari

    def sewa(self, nama_penyewa, hari):
        if not self._tersedia:
            print(f"  [X] {self.merk} {self.model} ({self.plat}) sudah disewa!")
            return None
        biaya = self.hitung_biaya(hari)
        self._tersedia  = False
        self._penyewa   = nama_penyewa
        self._hari_sewa = hari
        print(f"  [CAR] {self.merk} {self.model} ({self.plat}) disewa oleh {nama_penyewa}")
        print(f"     Durasi: {hari} hari | Biaya: Rp {biaya:,.0f}")
        return biaya

    def kembalikan(self, km_tempuh=0):
        if self._tersedia:
            print(f"  [!] Kendaraan ini belum disewa!")
            return
        self._km       += km_tempuh
        self._tersedia  = True
        print(f"  [OK] {self.merk} {self.model} dikembalikan oleh {self._penyewa}")
        print(f"     KM tempuh: {km_tempuh} km | Total KM: {self._km} km")

    def __str__(self):
        status = "[OK] Tersedia" if self._tersedia else "[X] Disewa"
        return f"[{self.plat}] {self.merk} {self.model} ({self.tahun}) | {status}"


class Mobil(Kendaraan):
    def __init__(self, plat, merk, model, tahun, tarif_per_hari,
                 kapasitas=5, bertransmisi_otomatis=False):
        super().__init__(plat, merk, model, tahun, tarif_per_hari)
        self.kapasitas             = kapasitas
        self.bertransmisi_otomatis = bertransmisi_otomatis


class Motor(Kendaraan):
    def __init__(self, plat, merk, model, tahun, tarif_per_hari,
                 cc=150, jenis="Matic"):
        super().__init__(plat, merk, model, tahun, tarif_per_hari)
        self.cc    = cc
        self.jenis = jenis


class Truk(Kendaraan):
    """Truk punya tarif berbeda: ada biaya tambahan per km."""
    def __init__(self, plat, merk, model, tahun, tarif_per_hari,
                 kapasitas_ton=5, tarif_per_km=500):
        super().__init__(plat, merk, model, tahun, tarif_per_hari)
        self.kapasitas_ton = kapasitas_ton
        self.tarif_per_km  = tarif_per_km
        self._km_kontrak   = 0

    def hitung_biaya(self, hari, km_estimasi=0):
        """Override: Truk punya biaya dasar + biaya per km."""
        biaya_dasar = self.tarif_per_hari * hari
        biaya_km    = self.tarif_per_km * km_estimasi
        self._km_kontrak = km_estimasi
        total = biaya_dasar + biaya_km
        print(f"     Biaya dasar: Rp {biaya_dasar:,.0f} | Biaya KM: Rp {biaya_km:,.0f}")
        return total

    def sewa(self, nama_penyewa, hari, km_estimasi=0):
        """Override untuk kirim km_estimasi ke hitung_biaya."""
        if not self._tersedia:
            print(f"  [X] {self.merk} {self.model} ({self.plat}) sudah disewa!")
            return None
        biaya = self.hitung_biaya(hari, km_estimasi)
        self._tersedia  = False
        self._penyewa   = nama_penyewa
        self._hari_sewa = hari
        print(f"  [TRK] {self.merk} {self.model} ({self.plat}) disewa oleh {nama_penyewa}")
        print(f"     Durasi: {hari} hari | Estimasi KM: {km_estimasi} km | Total: Rp {biaya:,.0f}")
        return biaya


# -- Demo Studi Kasus 2 -------------------------------------------
armada = [
    Mobil("KB 1234 AB", "Toyota",   "Avanza",  2022, 350_000, kapasitas=7),
    Mobil("KB 5678 CD", "Honda",    "Brio",    2023, 280_000, kapasitas=5),
    Motor("KB 9012 EF", "Yamaha",   "NMAX",    2023, 120_000, cc=155, jenis="Matic"),
    Motor("KB 3456 GH", "Honda",    "PCX",     2024, 130_000, cc=160, jenis="Matic"),
    Truk ("KB 7890 IJ", "Mitsubishi","Colt T",  2020, 800_000, kapasitas_ton=4, tarif_per_km=1000),
]

print("\n  -- Status Armada --")
for k in armada:
    print(f"  {k}")

print("\n  -- Transaksi Rental --")
avanza = armada[0]
avanza.sewa("Budi Santoso", 3)

truk = armada[4]
truk.sewa("Logistik Nusantara", 2, km_estimasi=500)

nmax = armada[2]
nmax.sewa("Sari Dewi", 1)

print("\n  -- Pengembalian --")
avanza.kembalikan(km_tempuh=280)
nmax.kembalikan(km_tempuh=45)

print("\n  -- Status Armada Setelah Transaksi --")
for k in armada:
    print(f"  {k}")

print()
