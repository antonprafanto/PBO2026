"""
Kode Praktik - Materi 08: Abstraksi (Abstraction)
File: 03_studi_kasus.py
Topik: Dua skenario nyata — Sistem Plugin Ekspor Data & Sistem Antrian Layanan Kampus

Jalankan: python 03_studi_kasus.py
"""

from abc import ABC, abstractmethod
import json
import math

# ======================================================================
# SKENARIO 1: Sistem Plugin Ekspor Data Akademik
#
# Masalah: Sistem akademik kampus perlu bisa mengekspor data ke
# berbagai format (CSV, JSON, teks laporan). Format baru bisa
# ditambahkan kapan saja tanpa mengubah kode inti.
#
# Solusi Abstraksi:
#   - EksporPluginABC mendefinisikan kontrak yang wajib dipenuhi
#   - Setiap plugin mengimplementasikan caranya sendiri
#   - SistemEkspor hanya berinteraksi melalui kontrak, tidak tahu
#     detail format — ini adalah kekuatan abstraksi!
# ======================================================================
print("=" * 65)
print("SKENARIO 1: Sistem Plugin Ekspor Data Akademik")
print("=" * 65)


class EksporPluginABC(ABC):
    """
    ABC — Kontrak yang wajib dipenuhi oleh semua plugin ekspor.
    Sistem inti hanya tahu interface ini, tidak peduli implementasinya.
    """

    @property
    @abstractmethod
    def format_nama(self):
        """Nama format, misalnya 'CSV', 'JSON', 'TXT'."""
        pass

    @property
    @abstractmethod
    def ekstensi_file(self):
        """Ekstensi file output, misalnya 'csv', 'json', 'txt'."""
        pass

    @abstractmethod
    def ekspor(self, data: list, nama_file: str):
        """
        Ekspor data ke file.
        data: list of dict
        nama_file: nama file tanpa ekstensi
        """
        pass

    # Method konkret — sudah ada, diwarisi langsung
    def nama_file_lengkap(self, nama):
        return f"{nama}.{self.ekstensi_file}"

    def pratinjau(self, data: list, maks_baris=3):
        """Tampilkan pratinjau data sebelum diekspor."""
        print(f"  Pratinjau ({min(maks_baris, len(data))} dari {len(data)} baris):")
        for baris in data[:maks_baris]:
            print(f"    {baris}")
        if len(data) > maks_baris:
            print(f"    ... ({len(data) - maks_baris} baris lagi)")


class EksporCSV(EksporPluginABC):
    """Plugin ekspor ke format CSV (Comma-Separated Values)."""

    def __init__(self, separator=","):
        self._sep = separator

    @property
    def format_nama(self):
        return "CSV"

    @property
    def ekstensi_file(self):
        return "csv"

    def ekspor(self, data: list, nama_file: str):
        if not data:
            print("  [CSV] Data kosong, tidak ada yang diekspor.")
            return

        path = self.nama_file_lengkap(nama_file)
        header = self._sep.join(data[0].keys())
        baris_list = [header]

        for row in data:
            baris = self._sep.join(str(v) for v in row.values())
            baris_list.append(baris)

        print(f"  [CSV] Menulis {len(data)} baris ke '{path}'")
        print(f"    Header : {header}")
        print(f"    Contoh : {baris_list[1] if len(baris_list) > 1 else '-'}")
        print(f"    Total  : {len(baris_list) - 1} baris data")


class EksporJSON(EksporPluginABC):
    """Plugin ekspor ke format JSON."""

    def __init__(self, indent=2):
        self._indent = indent

    @property
    def format_nama(self):
        return "JSON"

    @property
    def ekstensi_file(self):
        return "json"

    def ekspor(self, data: list, nama_file: str):
        if not data:
            print("  [JSON] Data kosong.")
            return

        path = self.nama_file_lengkap(nama_file)
        json_str = json.dumps(data, indent=self._indent, ensure_ascii=False)
        baris = json_str.count("\n") + 1

        print(f"  [JSON] Menulis ke '{path}'")
        print(f"    Jumlah objek : {len(data)}")
        print(f"    Jumlah baris : {baris}")
        print(f"    Pratinjau    : {json_str[:80]}{'...' if len(json_str) > 80 else ''}")


class EksporTeksLaporan(EksporPluginABC):
    """Plugin ekspor ke format laporan teks terformat."""

    def __init__(self, lebar=65):
        self._lebar = lebar

    @property
    def format_nama(self):
        return "Laporan Teks"

    @property
    def ekstensi_file(self):
        return "txt"

    def ekspor(self, data: list, nama_file: str):
        if not data:
            print("  [TXT] Data kosong.")
            return

        path = self.nama_file_lengkap(nama_file)
        kolom = list(data[0].keys())
        lebar_kolom = {k: max(len(k), max(len(str(r[k])) for r in data))
                       for k in kolom}

        header = "  ".join(k.upper().ljust(lebar_kolom[k]) for k in kolom)
        garis  = "-" * len(header)

        baris_teks = [garis, header, garis]
        for row in data:
            baris = "  ".join(str(row[k]).ljust(lebar_kolom[k]) for k in kolom)
            baris_teks.append(baris)
        baris_teks.append(garis)

        print(f"  [TXT] Menulis laporan ke '{path}'")
        print(f"    Kolom  : {', '.join(kolom)}")
        print(f"    Baris  : {len(data)}")
        print(f"    Contoh :")
        for b in baris_teks[:4]:
            print(f"      {b}")


class SistemEkspor:
    """
    Sistem inti ekspor — hanya berinteraksi dengan EksporPluginABC.
    Tidak tahu dan tidak peduli format apa yang sedang dipakai.
    """

    def __init__(self):
        self._plugins = {}   # format_nama -> plugin

    def daftarkan_plugin(self, plugin: EksporPluginABC):
        """Daftarkan plugin baru. Sistem langsung bisa menggunakannya."""
        if not isinstance(plugin, EksporPluginABC):
            raise TypeError("Plugin harus mengimplementasikan EksporPluginABC")
        self._plugins[plugin.format_nama] = plugin
        print(f"  Plugin '{plugin.format_nama}' (.{plugin.ekstensi_file}) terdaftar.")

    def ekspor(self, data: list, nama_file: str, format_nama: str):
        """Ekspor data menggunakan plugin yang sudah terdaftar."""
        if format_nama not in self._plugins:
            tersedia = list(self._plugins.keys())
            raise ValueError(f"Format '{format_nama}' tidak tersedia. "
                             f"Tersedia: {tersedia}")
        self._plugins[format_nama].ekspor(data, nama_file)

    def ekspor_semua(self, data: list, nama_file: str):
        """Ekspor ke semua format yang terdaftar sekaligus."""
        print(f"\n  Mengekspor '{nama_file}' ke {len(self._plugins)} format...")
        for plugin in self._plugins.values():
            plugin.ekspor(data, nama_file)

    def daftar_format(self):
        return list(self._plugins.keys())


# --- Demo Skenario 1 ---
data_mahasiswa = [
    {"nim": "2301001", "nama": "Budi Santoso",  "prodi": "Informatika", "ipk": 3.75},
    {"nim": "2301002", "nama": "Sari Dewi",      "prodi": "Informatika", "ipk": 3.20},
    {"nim": "2301003", "nama": "Eko Prasetyo",   "prodi": "Sistem Informasi", "ipk": 2.90},
    {"nim": "2301004", "nama": "Rini Wahyuni",   "prodi": "Informatika", "ipk": 3.85},
    {"nim": "2301005", "nama": "Dian Pratama",   "prodi": "Sistem Informasi", "ipk": 3.10},
]

sistem = SistemEkspor()
print("\n  Mendaftarkan plugin ekspor:")
sistem.daftarkan_plugin(EksporCSV())
sistem.daftarkan_plugin(EksporJSON(indent=2))
sistem.daftarkan_plugin(EksporTeksLaporan())

print(f"\n  Format tersedia: {sistem.daftar_format()}")
sistem.ekspor_semua(data_mahasiswa, "data_mahasiswa_2026")

# Ekspor format tertentu
print("\n  Ekspor hanya ke JSON:")
sistem.ekspor(data_mahasiswa, "backup_mahasiswa", "JSON")

# Coba format tidak ada
print("\n  Mencoba format tidak tersedia:")
try:
    sistem.ekspor(data_mahasiswa, "test", "Excel")
except ValueError as e:
    print(f"  ValueError: {e}")


# ======================================================================
# SKENARIO 2: Sistem Antrian Layanan Akademik Kampus
#
# Masalah: Bagian administrasi kampus punya beberapa jenis layanan
# (nilai, transkrip, surat keterangan, KRS). Setiap layanan punya
# prosedur berbeda tapi antrian dikelola dengan cara yang sama.
#
# Solusi Abstraksi + Template Method:
#   - LayananAkademikABC: kontrak dan template proses_layanan()
#   - Setiap subkelas mengisi detail validasi & proses
#   - AntrianLayanan mengelola semua jenis layanan secara seragam
# ======================================================================
print("\n" + "=" * 65)
print("SKENARIO 2: Sistem Antrian Layanan Akademik Kampus")
print("=" * 65)


class LayananAkademikABC(ABC):
    """
    ABC dengan Template Method untuk semua layanan akademik.
    Kontrak + urutan proses yang baku.
    """

    # -- Abstract properties ---------------------------------------------

    @property
    @abstractmethod
    def nama_layanan(self):
        pass

    @property
    @abstractmethod
    def estimasi_waktu_menit(self):
        pass

    @property
    @abstractmethod
    def biaya_admin(self):
        """Biaya administrasi layanan (0 jika gratis)."""
        pass

    # -- Abstract methods ------------------------------------------------

    @abstractmethod
    def validasi_syarat(self, data_pemohon: dict) -> bool:
        """Validasi apakah pemohon memenuhi syarat layanan ini."""
        pass

    @abstractmethod
    def proses_dokumen(self, data_pemohon: dict) -> str:
        """Proses inti layanan -- kembalikan deskripsi dokumen yang dihasilkan."""
        pass

    # -- Template Method (konkret) ---------------------------------------

    def layani(self, nomor_antrian: int, data_pemohon: dict):
        """
        TEMPLATE METHOD: urutan layanan selalu sama.
        1. Tampilkan info -> 2. Validasi -> 3. Proses -> 4. Selesai
        """
        print(f"\n  {'='*55}")
        print(f"  No. Antrian : {nomor_antrian:03d}")
        print(f"  Layanan     : {self.nama_layanan}")
        print(f"  Pemohon     : {data_pemohon.get('nama')} "
              f"({data_pemohon.get('nim')})")

        if not self.validasi_syarat(data_pemohon):
            print(f"  Status      : [X] DITOLAK")
            print(f"  {'='*55}")
            return False

        dokumen = self.proses_dokumen(data_pemohon)

        if self.biaya_admin > 0:
            print(f"  Biaya Admin : Rp {self.biaya_admin:,.0f}")

        print(f"  Estimasi    : {self.estimasi_waktu_menit} menit")
        print(f"  Dokumen     : {dokumen}")
        print(f"  Status      : [OK] SELESAI")
        print(f"  {'='*55}")
        return True


class LayananPerubahanNilai(LayananAkademikABC):
    """Layanan pengajuan perubahan/koreksi nilai mata kuliah."""

    @property
    def nama_layanan(self):
        return "Perubahan/Koreksi Nilai"

    @property
    def estimasi_waktu_menit(self):
        return 30

    @property
    def biaya_admin(self):
        return 0   # gratis

    def validasi_syarat(self, data: dict) -> bool:
        if not data.get("surat_dosen"):
            print("  [Validasi] Surat rekomendasi dosen belum ada")
            return False
        if not data.get("krs_semester"):
            print("  [Validasi] Fotokopi KRS semester tersebut belum ada")
            return False
        print("  [Validasi] Semua syarat terpenuhi OK")
        return True

    def proses_dokumen(self, data: dict) -> str:
        matkul = data.get("matakuliah", "Tidak Diketahui")
        return f"Formulir Perubahan Nilai MK: {matkul} (diteruskan ke dosen)"


class LayananTranskrip(LayananAkademikABC):
    """Layanan cetak transkrip nilai resmi."""

    @property
    def nama_layanan(self):
        return "Cetak Transkrip Nilai Resmi"

    @property
    def estimasi_waktu_menit(self):
        return 15

    @property
    def biaya_admin(self):
        return 25_000

    def validasi_syarat(self, data: dict) -> bool:
        tunggakan = data.get("tunggakan_spp", 0)
        if tunggakan > 0:
            print(f"  [Validasi] Ada tunggakan SPP Rp {tunggakan:,.0f}")
            return False
        rangkap = data.get("jumlah_rangkap", 1)
        if rangkap > 5:
            print(f"  [Validasi] Maksimal 5 rangkap per pengajuan (diminta: {rangkap})")
            return False
        print(f"  [Validasi] Tidak ada tunggakan, {rangkap} rangkap OK")
        return True

    def proses_dokumen(self, data: dict) -> str:
        rangkap = data.get("jumlah_rangkap", 1)
        tujuan  = data.get("tujuan", "Umum")
        return f"Transkrip resmi {rangkap} rangkap — keperluan: {tujuan}"


class LayananSuratKeterangan(LayananAkademikABC):
    """Layanan pembuatan surat keterangan aktif kuliah."""

    @property
    def nama_layanan(self):
        return "Surat Keterangan Mahasiswa Aktif"

    @property
    def estimasi_waktu_menit(self):
        return 10

    @property
    def biaya_admin(self):
        return 0

    def validasi_syarat(self, data: dict) -> bool:
        if not data.get("status_aktif", False):
            print("  [Validasi] Mahasiswa tidak berstatus aktif semester ini")
            return False
        print("  [Validasi] Status aktif terkonfirmasi OK")
        return True

    def proses_dokumen(self, data: dict) -> str:
        tujuan  = data.get("tujuan", "Keperluan Umum")
        bahasa  = data.get("bahasa", "Indonesia")
        return (f"Surat Keterangan Aktif — Tujuan: {tujuan}, "
                f"Bahasa: {bahasa}")


class LayananVerifikasiIjazah(LayananAkademikABC):
    """Layanan legalisir dan verifikasi ijazah."""

    @property
    def nama_layanan(self):
        return "Verifikasi & Legalisir Ijazah"

    @property
    def estimasi_waktu_menit(self):
        return 60

    @property
    def biaya_admin(self):
        return 50_000

    def validasi_syarat(self, data: dict) -> bool:
        if not data.get("ijazah_asli"):
            print("  [Validasi] Ijazah asli harus dibawa")
            return False
        if not data.get("ktp"):
            print("  [Validasi] KTP asli pemohon harus ada")
            return False
        print("  [Validasi] Ijazah asli & KTP ada OK")
        return True

    def proses_dokumen(self, data: dict) -> str:
        rangkap = data.get("rangkap_legalisir", 3)
        return f"Legalisir ijazah {rangkap} rangkap + surat pengantar verifikasi"


class AntrianLayanan:
    """
    Sistem antrian yang mengelola semua jenis LayananAkademikABC.
    Hanya tahu kontrak ABC — tidak tahu detail setiap layanan.
    """

    def __init__(self, nama_bagian):
        self.nama_bagian = nama_bagian
        self._antrian    = []   # list of (layanan, data_pemohon)
        self._counter    = 0
        self._sukses     = 0
        self._ditolak    = 0

    def tambah_antrian(self, layanan: LayananAkademikABC, data_pemohon: dict):
        """Tambah permintaan layanan ke antrian."""
        if not isinstance(layanan, LayananAkademikABC):
            raise TypeError("layanan harus berupa LayananAkademikABC")
        self._antrian.append((layanan, data_pemohon))
        nomor = len(self._antrian)
        print(f"  Antrian {nomor:03d}: {data_pemohon.get('nama')} — "
              f"{layanan.nama_layanan}")

    def proses_semua(self):
        """Proses semua antrian satu per satu."""
        if not self._antrian:
            print("  Antrian kosong.")
            return

        print(f"\n  {'='*55}")
        print(f"  PROSES ANTRIAN — {self.nama_bagian.upper()}")
        print(f"  Total: {len(self._antrian)} permintaan")
        print(f"  {'='*55}")

        for i, (layanan, data) in enumerate(self._antrian, 1):
            berhasil = layanan.layani(i, data)
            if berhasil:
                self._sukses += 1
            else:
                self._ditolak += 1

        self._antrian.clear()
        self._cetak_rekapitulasi()

    def _cetak_rekapitulasi(self):
        total = self._sukses + self._ditolak
        print(f"\n  REKAPITULASI:")
        print(f"  Total diproses : {total}")
        print(f"  Berhasil       : {self._sukses}")
        print(f"  Ditolak        : {self._ditolak}")


# --- Demo Skenario 2 ---
print()
antrian = AntrianLayanan("Bagian Akademik Universitas Mulawarman")

print("  Mendaftarkan permintaan layanan:\n")

antrian.tambah_antrian(
    LayananSuratKeterangan(),
    {"nama": "Budi Santoso", "nim": "2301001",
     "status_aktif": True, "tujuan": "Beasiswa KIP-K", "bahasa": "Indonesia"})

antrian.tambah_antrian(
    LayananTranskrip(),
    {"nama": "Sari Dewi", "nim": "2301002",
     "tunggakan_spp": 0, "jumlah_rangkap": 2, "tujuan": "Melamar Kerja"})

antrian.tambah_antrian(
    LayananPerubahanNilai(),
    {"nama": "Eko Prasetyo", "nim": "2301003",
     "surat_dosen": True, "krs_semester": False,   # satu syarat kurang
     "matakuliah": "Algoritma & Pemrograman"})

antrian.tambah_antrian(
    LayananTranskrip(),
    {"nama": "Rini Wahyuni", "nim": "2301004",
     "tunggakan_spp": 2_000_000,                    # ada tunggakan
     "jumlah_rangkap": 1, "tujuan": "Beasiswa"})

antrian.tambah_antrian(
    LayananVerifikasiIjazah(),
    {"nama": "Alumni: Dian Pratama", "nim": "1901001",
     "ijazah_asli": True, "ktp": True, "rangkap_legalisir": 5})

antrian.proses_semua()
