"""
Kode Praktik - Materi 11: Prinsip SOLID
File: 01_srp_ocp_dasar.py
Topik: Single Responsibility Principle (SRP) dan Open/Closed Principle (OCP)

Jalankan: python 01_srp_ocp_dasar.py
"""

# ======================================================================
# BAGIAN 1: Single Responsibility Principle (SRP)
#           Fokus: satu kelas, satu tanggung jawab
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Single Responsibility Principle (SRP)")
print("=" * 60)

# --- Anti-pattern: Godly Class ---
print("\n-- Demo Anti-Pattern: Kelas yang melakukan segalanya --")

class MahasiswaJelek:
    """
    [JELEK] Mahasiswa yang handle data, email, PDF, database sekaligus.
    Terlalu banyak alasan untuk berubah!
    """
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk

    def hitung_uks(self):
        """Tanggung jawab 1: perhitungan akademik."""
        return self.ipk * 4

    def kirim_email_nilai(self, email, nilai):
        """Tanggung jawab 2: mengirim email (seharusnya di kelas lain!)."""
        print(f"  [Email] Mengirim nilai {nilai} ke {email}...")
        # Di aplikasi real, ada SMTP setup di sini
        return True

    def cetak_transkrip_pdf(self, filename):
        """Tanggung jawab 3: cetak dokumen (seharusnya di kelas lain!)."""
        print(f"  [PDF] Membuat transkrip ke {filename}...")
        # Di aplikasi real, ada PDF generation di sini
        return True

    def simpan_ke_database(self, connection):
        """Tanggung jawab 4: database (seharusnya di kelas lain!)."""
        print(f"  [DB] INSERT INTO mahasiswa VALUES ('{self.nim}', '{self.nama}', {self.ipk})...")
        # Di aplikasi real, ada cursor.execute(query) di sini
        return True


mhs_jelek = MahasiswaJelek("2301001", "Budi Santoso", 3.75)
print(f"  Mahasiswa: {mhs_jelek.nama} (NIM {mhs_jelek.nim}, IPK {mhs_jelek.ipk})")
print(f"  UKS: {mhs_jelek.hitung_uks()}")
mhs_jelek.kirim_email_nilai("budi@unmul.ac.id", "A")
mhs_jelek.cetak_transkrip_pdf("transkrip_2301001.pdf")
mhs_jelek.simpan_ke_database(None)

# --- Pattern: Separation of Concerns ---
print("\n-- Demo Pattern: Kelas terpisah, tanggung jawab jelas --")


class Mahasiswa:
    """
    [BAIK] Mahasiswa hanya menangani data akademik.
    Satu tanggung jawab: representasi data mahasiswa.
    """
    def __init__(self, nim, nama, ipk):
        self.nim = nim
        self.nama = nama
        self.ipk = ipk

    def hitung_uks(self):
        """Kalkulasi internal -- tetap di sini."""
        return self.ipk * 4

    def __str__(self):
        return f"{self.nim} | {self.nama} (IPK {self.ipk:.2f})"


class LayananEmail:
    """
    [BAIK] Tangani semua email akademik.
    Satu tanggung jawab: mengirim email.
    """
    @staticmethod
    def kirim_nilai(mahasiswa, nilai, email_tujuan):
        """Kirim notifikasi nilai."""
        print(f"  [Email] Mengirim nilai {nilai} ke {email_tujuan}...")
        print(f"          Mahasiswa: {mahasiswa.nama}")
        return True

    @staticmethod
    def kirim_pengumuman(daftar_email, judul, isi):
        """Kirim broadcast pengumuman."""
        print(f"  [Email Broadcast] Mengirim '{judul}' ke {len(daftar_email)} penerima...")
        return True


class LayananDokumen:
    """
    [BAIK] Tangani semua cetak/generate dokumen.
    Satu tanggung jawab: membuat dokumen.
    """
    @staticmethod
    def cetak_transkrip_pdf(mahasiswa, filename):
        """Generate transkrip PDF."""
        print(f"  [PDF] Membuat transkrip {mahasiswa.nim} -> {filename}...")
        return True

    @staticmethod
    def cetak_surat_lulus(mahasiswa, filename):
        """Generate surat kelulusan."""
        print(f"  [PDF] Membuat surat lulus {mahasiswa.nama} -> {filename}...")
        return True


class RepositoriMahasiswa:
    """
    [BAIK] Tangani semua database operations.
    Satu tanggung jawab: persistence (database).
    """
    def __init__(self):
        self._data = {}  # Simulasi database

    def simpan(self, mahasiswa):
        """Simpan mahasiswa ke database."""
        self._data[mahasiswa.nim] = mahasiswa
        print(f"  [DB] INSERT mahasiswa {mahasiswa.nim}...")
        return True

    def ambil(self, nim):
        """Ambil mahasiswa dari database."""
        return self._data.get(nim)

    def update(self, mahasiswa):
        """Update data mahasiswa."""
        if mahasiswa.nim in self._data:
            self._data[mahasiswa.nim] = mahasiswa
            print(f"  [DB] UPDATE mahasiswa {mahasiswa.nim}...")
            return True
        return False

    def hapus(self, nim):
        """Hapus mahasiswa dari database."""
        if nim in self._data:
            del self._data[nim]
            print(f"  [DB] DELETE mahasiswa {nim}...")
            return True
        return False


# --- Test dengan kelas-kelas terpisah ---
print()
mhs_baik = Mahasiswa("2301042", "Sari Dewi", 3.45)
print(f"  Mahasiswa: {mhs_baik}")
print(f"  UKS: {mhs_baik.hitung_uks()}")

layanan_email = LayananEmail()
layanan_email.kirim_nilai(mhs_baik, "B+", "sari@unmul.ac.id")

layanan_dokumen = LayananDokumen()
layanan_dokumen.cetak_transkrip_pdf(mhs_baik, "transkrip_2301042.pdf")

repo = RepositoriMahasiswa()
repo.simpan(mhs_baik)
ambil = repo.ambil("2301042")
print(f"  Verifikasi: mahasiswa di DB = {ambil}")

# ======================================================================
# BAGIAN 2: Open/Closed Principle (OCP)
#           Fokus: extend tanpa modify kode yang sudah ada
# ======================================================================
print()
print("=" * 60)
print("BAGIAN 2: Open/Closed Principle (OCP)")
print("=" * 60)

# --- Anti-pattern: Modification-Heavy ---
print("\n-- Demo Anti-Pattern: Ubah method setiap ada tipe baru --")


class KalkulatorNilaiJelek:
    """
    [JELEK] Setiap tipe mahasiswa baru = ubah method hitung().
    Violated OCP: tidak closed untuk modification.
    """
    def hitung(self, nilai, tipe_mahasiswa):
        """Besar-besaran if-elif untuk tiap tipe."""
        if tipe_mahasiswa == "reguler":
            return nilai * 1.0
        elif tipe_mahasiswa == "beasiswa_penuh":
            return nilai * 1.2   # Bonus 20%
        elif tipe_mahasiswa == "beasiswa_sebagian":
            return nilai * 1.1   # Bonus 10%
        elif tipe_mahasiswa == "afirmasi":
            return nilai * 1.15  # Bonus 15%
        elif tipe_mahasiswa == "bidikmisi":
            return nilai * 1.25  # Bonus 25%
        elif tipe_mahasiswa == "prestasi":
            return nilai * 1.3   # Bonus 30%
        # Setiap tipe baru = harus edit method ini!
        # Berisiko break kasus lama!


kalc_jelek = KalkulatorNilaiJelek()
print(f"  Reguler (85): {kalc_jelek.hitung(85, 'reguler')}")
print(f"  Beasiswa Penuh (85): {kalc_jelek.hitung(85, 'beasiswa_penuh')}")
print(f"  Afirmasi (85): {kalc_jelek.hitung(85, 'afirmasi')}")

# --- Pattern: Strategy Pattern ---
print("\n-- Demo Pattern: Strategy -- extend tanpa modify --")


class StrategiNilai:
    """
    [BAIK] Base class untuk semua strategi perhitungan.
    Ini adalah abstraksi.
    """
    def hitung(self, nilai):
        raise NotImplementedError


class StrategiReguler(StrategiNilai):
    """Strategi untuk mahasiswa reguler -- tanpa bonus."""
    def hitung(self, nilai):
        return nilai * 1.0


class StrategiBeasiswaPenuh(StrategiNilai):
    """Strategi untuk beasiswa penuh -- bonus 20%."""
    def hitung(self, nilai):
        return nilai * 1.2


class StrategiBeasiswaSebagian(StrategiNilai):
    """Strategi untuk beasiswa sebagian -- bonus 10%."""
    def hitung(self, nilai):
        return nilai * 1.1


class StrategiAfirmasi(StrategiNilai):
    """Strategi untuk afirmasi -- bonus 15%."""
    def hitung(self, nilai):
        return nilai * 1.15


class StrategyBidikmisi(StrategiNilai):
    """Strategi untuk bidikmisi -- bonus 25%."""
    def hitung(self, nilai):
        return nilai * 1.25


class StrategiPrestasi(StrategiNilai):
    """Strategi untuk prestasi -- bonus 30%."""
    def hitung(self, nilai):
        return nilai * 1.3


class KalkulatorNilaiAI:
    """
    [BAIK] Kalkulator menggunakan strategy.
    Tidak perlu ubah -- tinggal inject strategy baru!
    CLOSED untuk modification, OPEN untuk extension.
    """
    def __init__(self, strategi: StrategiNilai):
        self.strategi = strategi

    def hitung(self, nilai):
        """Method ini tidak perlu ubah lagi!"""
        return self.strategi.hitung(nilai)


print()
print("  Penggunaan dengan strategy pattern:")
print(f"  Reguler (85):           {KalkulatorNilaiAI(StrategiReguler()).hitung(85)}")
print(f"  Beasiswa Penuh (85):    {KalkulatorNilaiAI(StrategiBeasiswaPenuh()).hitung(85)}")
print(f"  Beasiswa Sebagian (85): {KalkulatorNilaiAI(StrategiBeasiswaSebagian()).hitung(85)}")
print(f"  Afirmasi (85):          {KalkulatorNilaiAI(StrategiAfirmasi()).hitung(85)}")
print(f"  Bidikmisi (85):         {KalkulatorNilaiAI(StrategyBidikmisi()).hitung(85)}")
print(f"  Prestasi (85):          {KalkulatorNilaiAI(StrategiPrestasi()).hitung(85)}")

print("\n  [POINT] Untuk tipe baru, tinggal buat class baru.")
print("          Tidak perlu ubah KalkulatorNilaiAI!")


# --- Pattern: Inheritance (Template Method) ---
print("\n-- Alternatif: Template Method dengan Inheritance --")


class MataKuliahBase:
    """
    [BAIK] Template method pattern.
    Subclass override hanya bagian yang berubah.
    """
    def __init__(self, kode, nama):
        self.kode = kode
        self.nama = nama

    def hitung_nilai_akhir(self, nilai_uts, nilai_uas):
        """Template -- subclass bisa override."""
        bobot_uts = self._get_bobot_uts()
        bobot_uas = self._get_bobot_uas()
        return nilai_uts * bobot_uts + nilai_uas * bobot_uas

    def _get_bobot_uts(self):
        """Override ini di subclass sesuai kebutuhan."""
        return 0.4

    def _get_bobot_uas(self):
        """Override ini di subclass sesuai kebutuhan."""
        return 0.6


class MataKuliahRegular(MataKuliahBase):
    """Regular -- 40% UTS, 60% UAS."""
    pass


class MataKuliahPraktik(MataKuliahBase):
    """Praktik -- 30% UTS, 70% UAS (praktek dominan)."""
    def _get_bobot_uts(self):
        return 0.3

    def _get_bobot_uas(self):
        return 0.7


class MataKuliahSeminar(MataKuliahBase):
    """Seminar -- 20% UTS, 80% UAS (presentasi dominan)."""
    def _get_bobot_uts(self):
        return 0.2

    def _get_bobot_uas(self):
        return 0.8


print()
print("  Template method pattern:")
regular = MataKuliahRegular("IF201", "Algoritma")
praktik = MataKuliahPraktik("IF301", "Lab Keamanan")
seminar = MataKuliahSeminar("IF491", "Seminar")

print(f"  {regular.nama}: 70 UTS, 80 UAS = {regular.hitung_nilai_akhir(70, 80):.1f}")
print(f"  {praktik.nama}: 70 UTS, 80 UAS = {praktik.hitung_nilai_akhir(70, 80):.1f}")
print(f"  {seminar.nama}: 70 UTS, 80 UAS = {seminar.hitung_nilai_akhir(70, 80):.1f}")

print()
print("Selesai! SRP & OCP dijalankan tanpa error.")
