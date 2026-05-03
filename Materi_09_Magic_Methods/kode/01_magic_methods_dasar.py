"""
Kode Praktik - Materi 09: Magic Methods (Metode Ajaib)
File: 01_magic_methods_dasar.py
Topik: __str__, __repr__, __len__, __bool__, __iter__, __call__, __format__

Jalankan: python 01_magic_methods_dasar.py
"""

# ======================================================================
# BAGIAN 1: __str__ dan __repr__ -- Representasi Objek
#           Fokus: membuat objek terlihat informatif saat dicetak
# ======================================================================
print("=" * 60)
print("BAGIAN 1: __str__ dan __repr__ -- Representasi Objek")
print("=" * 60)


class MahasiswaFTI:
    """Representasi data seorang mahasiswa Fakultas Teknik dan Informatika."""

    def __init__(self, nim, nama, prodi, ipk):
        self.nim   = nim
        self.nama  = nama
        self.prodi = prodi
        self.ipk   = ipk

    def __str__(self):
        """Dipanggil oleh print() dan str() -- untuk pengguna akhir."""
        return f"[{self.nim}] {self.nama} ({self.prodi}) -- IPK: {self.ipk:.2f}"

    def __repr__(self):
        """Dipanggil oleh repr() dan shell interaktif -- untuk developer."""
        return (
            f"MahasiswaFTI(nim='{self.nim}', nama='{self.nama}', "
            f"prodi='{self.prodi}', ipk={self.ipk})"
        )


# --- Demo ---
mhs1 = MahasiswaFTI("2301001", "Budi Santoso",   "Informatika",    3.75)
mhs2 = MahasiswaFTI("2301042", "Sari Dewi",      "Sistem Informasi", 3.60)
mhs3 = MahasiswaFTI("2301087", "Ahmad Fauzi",    "Informatika",    3.82)

print("-- print() menggunakan __str__ --")
print(mhs1)
print(mhs2)

print()
print("-- repr() menggunakan __repr__ --")
print(repr(mhs1))

print()
print("-- f-string menggunakan __str__ --")
print(f"Mahasiswa terbaik: {mhs3}")

print()
print("-- List berisi objek: masing-masing memanggil __repr__ --")
daftar = [mhs1, mhs2, mhs3]
print(daftar)   # list menggunakan repr() untuk tiap elemen

# ======================================================================
# BAGIAN 2: __len__, __bool__, __format__ -- Perilaku Numerik & Format
#           Fokus: kelas yang bisa diukur dan diformat secara kustom
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: __len__, __bool__, __format__ -- Numerik & Format")
print("=" * 60)


class KelasKuliah:
    """Sebuah kelas perkuliahan dengan daftar mahasiswa terdaftar."""

    KAPASITAS_MAKS = 40

    def __init__(self, kode_mk, nama_mk):
        self.kode_mk      = kode_mk
        self.nama_mk      = nama_mk
        self._mahasiswa   = []

    def daftarkan(self, mahasiswa):
        """Mendaftarkan satu mahasiswa ke kelas ini."""
        if len(self._mahasiswa) >= self.KAPASITAS_MAKS:
            print(f"  [!] Kelas {self.kode_mk} sudah penuh!")
            return
        self._mahasiswa.append(mahasiswa)

    def __len__(self):
        """Dipanggil oleh len() -- mengembalikan jumlah mahasiswa terdaftar."""
        return len(self._mahasiswa)

    def __bool__(self):
        """Dipanggil dalam konteks if -- True jika ada mahasiswa terdaftar."""
        return len(self._mahasiswa) > 0

    def __str__(self):
        return f"KelasKuliah({self.kode_mk}: {self.nama_mk}, {len(self)} mhs)"

    def __format__(self, spec):
        """Format kustom: 'ringkas', 'lengkap', atau default."""
        if spec == "ringkas":
            return f"{self.kode_mk} ({len(self)}/{self.KAPASITAS_MAKS})"
        if spec == "lengkap":
            status = "Penuh" if len(self) >= self.KAPASITAS_MAKS else "Tersedia"
            return (
                f"Mata Kuliah : {self.nama_mk}\n"
                f"  Kode      : {self.kode_mk}\n"
                f"  Terdaftar : {len(self)}/{self.KAPASITAS_MAKS}\n"
                f"  Status    : {status}"
            )
        return str(self)  # fallback ke __str__


# --- Demo ---
pbo_kelas = KelasKuliah("IF204", "Pemrograman Berorientasi Objek")
algos_kelas = KelasKuliah("IF201", "Algoritma dan Struktur Data")

print("-- Kelas kosong --")
print(f"  {pbo_kelas}")
print(f"  Jumlah: {len(pbo_kelas)}")
print(f"  Ada mahasiswa? {bool(pbo_kelas)}")

if not pbo_kelas:
    print("  [!] Belum ada mahasiswa yang mendaftar")

# Daftarkan beberapa mahasiswa
for mhs in [mhs1, mhs2, mhs3]:
    pbo_kelas.daftarkan(mhs)

print()
print("-- Setelah pendaftaran --")
print(f"  {pbo_kelas}")
print(f"  Jumlah: {len(pbo_kelas)}")
print(f"  Ada mahasiswa? {bool(pbo_kelas)}")

if pbo_kelas:
    print("  [OK] Kelas siap dibuka")

print()
print("-- Format kustom dengan __format__ --")
print(f"  Format ringkas : {pbo_kelas:ringkas}")
print()
print(f"  Format lengkap:\n{pbo_kelas:lengkap}")

# ======================================================================
# BAGIAN 3: __iter__ dan __contains__ -- Kelas sebagai Container
#           Fokus: iterasi 'for x in obj' dan 'item in obj'
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 3: __iter__ dan __contains__ -- Container Protocol")
print("=" * 60)


class DaftarNilai:
    """
    Daftar nilai mahasiswa untuk satu mata kuliah.
    Mendukung iterasi, pengecekan keanggotaan, dan slicing.
    """

    def __init__(self, nama_mk):
        self.nama_mk = nama_mk
        self._data   = {}   # {nim: nilai}

    def tambah(self, nim, nilai):
        """Menambahkan atau memperbarui nilai seorang mahasiswa."""
        self._data[nim] = nilai

    def __len__(self):
        return len(self._data)

    def __contains__(self, nim):
        """Dipanggil oleh 'nim in daftar_nilai'."""
        return nim in self._data

    def __iter__(self):
        """Dipanggil oleh 'for nim, nilai in daftar_nilai:' (menggunakan .items())."""
        return iter(self._data.items())

    def __getitem__(self, nim):
        """Dipanggil oleh 'daftar_nilai[nim]'."""
        if nim not in self._data:
            raise KeyError(f"NIM '{nim}' tidak ditemukan dalam daftar nilai")
        return self._data[nim]

    def __str__(self):
        return f"DaftarNilai({self.nama_mk}, {len(self)} entri)"


def konversi_ke_huruf(angka):
    """Mengkonversi nilai angka ke nilai huruf."""
    if angka >= 85: return "A"
    if angka >= 70: return "B"
    if angka >= 55: return "C"
    if angka >= 40: return "D"
    return "E"


# --- Demo ---
daftar_pbo = DaftarNilai("Pemrograman Berorientasi Objek")
daftar_pbo.tambah("2301001", 88)
daftar_pbo.tambah("2301042", 75)
daftar_pbo.tambah("2301087", 92)
daftar_pbo.tambah("2301103", 61)

print(f"  {daftar_pbo}")

print()
print("  -- Iterasi dengan 'for' (__iter__) --")
for nim, nilai in daftar_pbo:
    huruf = konversi_ke_huruf(nilai)
    print(f"    NIM {nim} : {nilai:3d} -> {huruf}")

print()
print("  -- Pengecekan keanggotaan (__contains__) --")
nim_cek = ["2301001", "2301999"]
for nim in nim_cek:
    ada = nim in daftar_pbo
    print(f"    NIM {nim} ada? {ada}")

print()
print("  -- Akses langsung (__getitem__) --")
nilai_budi = daftar_pbo["2301001"]
print(f"    Nilai Budi (2301001): {nilai_budi} -> {konversi_ke_huruf(nilai_budi)}")

# ======================================================================
# BAGIAN 4: __call__ -- Objek yang Bisa Dipanggil seperti Fungsi
#           Fokus: membuat objek callable untuk kalkulasi berulang
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 4: __call__ -- Objek Callable")
print("=" * 60)


class KalkulatorTagihanSKS:
    """
    Kalkulator tagihan SKS yang menyimpan konfigurasi tarif.
    Bisa dipanggil seperti fungsi setelah dibuat.
    """

    def __init__(self, tarif_per_sks, biaya_tetap=0):
        self.tarif_per_sks = tarif_per_sks
        self.biaya_tetap   = biaya_tetap
        self._riwayat      = []

    def __call__(self, jumlah_sks, nama_mahasiswa=""):
        """
        Dipanggil saat: hitung_tagihan(20)
        Menghitung tagihan dan menyimpan ke riwayat.
        """
        total = (jumlah_sks * self.tarif_per_sks) + self.biaya_tetap
        catatan = {
            "nama"      : nama_mahasiswa,
            "sks"       : jumlah_sks,
            "total"     : total
        }
        self._riwayat.append(catatan)
        return total

    def tampilkan_riwayat(self):
        """Menampilkan semua perhitungan yang sudah dilakukan."""
        print(f"  Riwayat Kalkulasi (tarif Rp {self.tarif_per_sks:,}/SKS):")
        for i, c in enumerate(self._riwayat, 1):
            print(f"    {i}. {c['nama']:20s} | {c['sks']:2d} SKS "
                  f"| Rp {c['total']:>12,.0f}")

    def __repr__(self):
        return (f"KalkulatorTagihanSKS(tarif={self.tarif_per_sks}, "
                f"biaya_tetap={self.biaya_tetap})")


# --- Demo ---
# Kalkulator untuk mahasiswa reguler (tarif UKT Kelompok III)
hitung_ukt = KalkulatorTagihanSKS(tarif_per_sks=850_000, biaya_tetap=500_000)

print(f"  Kalkulator: {repr(hitung_ukt)}")
print()

# Panggil seperti fungsi
tagihan_budi  = hitung_ukt(20, "Budi Santoso")
tagihan_sari  = hitung_ukt(18, "Sari Dewi")
tagihan_ahmad = hitung_ukt(22, "Ahmad Fauzi")

hitung_ukt.tampilkan_riwayat()

print()
print("  -- Pembuktian: callable() --")
print(f"    callable(hitung_ukt) = {callable(hitung_ukt)}")   # True karena ada __call__
print(f"    callable(str)        = {callable(str)}")            # True
print(f"    callable(3.14)       = {callable(3.14)}")          # False

print()
print("Selesai! Semua bagian dijalankan tanpa error.")
