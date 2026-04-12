"""
============================================================
    MATERI 05 - Hubungan Kelas dan UML
    File: 01_asosiasi.py
    Topik: Asosiasi - Hubungan "Menggunakan" antar Kelas
============================================================

Asosiasi adalah hubungan PALING LONGGAR antar kelas.
Objek A "menggunakan" objek B sebagai parameter method
atau variabel lokal. Keduanya hidup INDEPENDEN.

Diagram UML:
    Mahasiswa -----------> Printer
              "menggunakan"
============================================================
"""

print("=" * 58)
print("  MATERI 05 - Hubungan Kelas dan UML")
print("  01_asosiasi.py")
print("=" * 58)


# ============================================================
# CONTOH 1: Asosiasi Sederhana
# Mahasiswa menggunakan Printer untuk mencetak tugas
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 1: Mahasiswa -> Printer (Uses-A)")
print("=" * 58)


class Printer:
    """Printer berdiri sendiri - bisa dipakai siapa saja."""

    def __init__(self, merk, dpi=600):
        self.merk  = merk
        self.dpi   = dpi
        self._antrian = []

    def tambah_antrian(self, nama_file):
        self._antrian.append(nama_file)

    def cetak(self, nama_file):
        print(f"  [{self.merk}] Mencetak '{nama_file}' @ {self.dpi} DPI ... OK")

    def cetak_semua(self):
        if not self._antrian:
            print(f"  [{self.merk}] Antrian kosong.")
            return
        print(f"  [{self.merk}] Memproses {len(self._antrian)} dokumen:")
        for f in self._antrian:
            self.cetak(f)
        self._antrian.clear()

    def __str__(self):
        return f"Printer {self.merk} ({self.dpi} DPI)"


class Mahasiswa:
    """Mahasiswa menggunakan Printer sebagai parameter (Asosiasi)."""

    def __init__(self, nama, nim):
        self.nama = nama
        self.nim  = nim

    # Printer dikirim sebagai PARAMETER - bukan disimpan sebagai atribut
    def cetak_tugas(self, printer, nama_file):
        """Asosiasi: Printer diterima sebagai parameter, dipakai sementara."""
        print(f"  {self.nama} mengirim '{nama_file}' ke {printer.merk}...")
        printer.cetak(nama_file)

    def kirim_ke_antrian(self, printer, nama_file):
        """Asosiasi: menambahkan tugas ke antrian printer."""
        printer.tambah_antrian(nama_file)
        print(f"  {self.nama}: '{nama_file}' ditambahkan ke antrian {printer.merk}")

    def __str__(self):
        return f"Mahasiswa {self.nama} ({self.nim})"


# ---- Demo Contoh 1 ----
print("\nMembuat objek independen:")
printer_lab  = Printer("HP LaserJet Pro", 1200)
printer_dosen = Printer("Canon PIXMA", 600)

budi = Mahasiswa("Budi Santoso", "2301001")
sari = Mahasiswa("Sari Dewi",    "2301002")
andi = Mahasiswa("Andi Wijaya",  "2301003")

print(f"  {budi}")
print(f"  {sari}")
print(f"  {printer_lab}")

print("\nAsosiasi: cetak langsung")
budi.cetak_tugas(printer_lab,  "Laporan_PBO.pdf")
sari.cetak_tugas(printer_lab,  "UTS_Kalkulus.pdf")
andi.cetak_tugas(printer_dosen, "Tugas_Basis_Data.docx")

print("\nAsosiasi: cetak via antrian")
budi.kirim_ke_antrian(printer_lab, "Skripsi_Bab1.pdf")
sari.kirim_ke_antrian(printer_lab, "Skripsi_Bab2.pdf")
andi.kirim_ke_antrian(printer_lab, "Skripsi_Bab3.pdf")
printer_lab.cetak_semua()

# Bukti ketidaktergantungan: printer tetap ada setelah mahasiswa dihapus
del budi
print(f"\n  budi sudah dihapus, tapi printer masih ada: {printer_lab}")


# ============================================================
# CONTOH 2: Asosiasi Dua Arah (Bidirectional Association)
# Dokter memeriksa Pasien, dan Pasien punya Dokter yang memeriksa
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 2: Dokter <--> Pasien (Bidirectional)")
print("=" * 58)


class Dokter:
    def __init__(self, nama, spesialisasi):
        self.nama         = nama
        self.spesialisasi = spesialisasi
        self._riwayat     = []   # catatan pasien yang pernah diperiksa

    def periksa(self, pasien, diagnosis):
        """Asosiasi: pasien dikirim sebagai parameter."""
        catatan = {
            "pasien":    pasien.nama,
            "diagnosis": diagnosis
        }
        self._riwayat.append(catatan)
        pasien.catat_kunjungan(self, diagnosis)
        print(f"  Dr. {self.nama} memeriksa {pasien.nama}: {diagnosis}")

    def lihat_riwayat(self):
        print(f"\n  Riwayat Dr. {self.nama}:")
        for r in self._riwayat:
            print(f"    - {r['pasien']}: {r['diagnosis']}")

    def __str__(self):
        return f"Dr. {self.nama} (Sp. {self.spesialisasi})"


class Pasien:
    def __init__(self, nama, no_rm):
        self.nama    = nama
        self.no_rm   = no_rm
        self._kunjungan = []

    def catat_kunjungan(self, dokter, diagnosis):
        """Dicatat di pihak Pasien."""
        self._kunjungan.append({
            "dokter":    dokter.nama,
            "diagnosis": diagnosis
        })

    def lihat_kunjungan(self):
        print(f"\n  Riwayat Kunjungan {self.nama} (RM: {self.no_rm}):")
        for k in self._kunjungan:
            print(f"    - Dr. {k['dokter']}: {k['diagnosis']}")

    def __str__(self):
        return f"Pasien {self.nama} (RM: {self.no_rm})"


# ---- Demo Contoh 2 ----
dr_budi  = Dokter("Budi Hartono", "Penyakit Dalam")
dr_sari  = Dokter("Sari Utami",   "Kardiologi")

pasien1 = Pasien("Anton Prafanto", "RM-001")
pasien2 = Pasien("Dewi Rahayu",    "RM-002")

dr_budi.periksa(pasien1, "Demam tifoid, perlu rawat inap")
dr_budi.periksa(pasien2, "Hipertensi ringan")
dr_sari.periksa(pasien1, "Aritmia jantung, perlu monitoring")

dr_budi.lihat_riwayat()
dr_sari.lihat_riwayat()
pasien1.lihat_kunjungan()

# Bukti independensi:
del dr_budi
print(f"\n  dr_budi dihapus, tapi pasien1 masih ada: {pasien1}")


# ============================================================
# CONTOH 3: Asosiasi dengan Multiplisitas
# Seorang Dosen mengajar banyak MataKuliah
# ============================================================

print("\n" + "=" * 58)
print("  CONTOH 3: Dosen -> MataKuliah (1 to Many)")
print("=" * 58)


class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks  = sks

    def __str__(self):
        return f"[{self.kode}] {self.nama} ({self.sks} SKS)"


class Dosen:
    def __init__(self, nama, nip):
        self.nama = nama
        self.nip  = nip

    def mengajar(self, matakuliah, ruangan, jam):
        """Asosiasi: Dosen menggunakan MataKuliah sebagai parameter."""
        print(f"  {self.nama} mengajar {matakuliah.nama}")
        print(f"    Ruangan: {ruangan} | Jam: {jam}")

    def __str__(self):
        return f"Dosen: {self.nama} ({self.nip})"


# Objek berdiri sendiri
mk_pbo = MataKuliah("IF301", "Pemrograman Berorientasi Objek", 3)
mk_bd  = MataKuliah("IF302", "Basis Data", 3)
mk_kk  = MataKuliah("IF201", "Kalkulus", 2)

dosen_anton = Dosen("Dr. Anton Prafanto", "NIP19850101")

print("\nJadwal Mengajar:")
dosen_anton.mengajar(mk_pbo, "Lab Komputer A", "Senin 08:00")
dosen_anton.mengajar(mk_bd,  "Ruang 301",      "Rabu 10:00")


print("\n[OK] Selesai: 01_asosiasi.py")
print("     Lanjut ke: 02_agregasi.py")
