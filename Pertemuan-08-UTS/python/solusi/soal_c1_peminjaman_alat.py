"""
Solusi Soal C1 - Peminjaman Alat Laboratorium
Pertemuan 08 - UTS (latihan persiapan, BUKAN soal ujian asli)

Ide penyelesaian:
- Alat adalah kelas induk. AlatElektronik dan KitPraktikum mewarisinya,
  menambah atribut sendiri, dan meng-override __str__.
- Besar denda per hari dikirim kelas anak ke konstruktor induk, jadi
  hitung_denda() cukup ditulis SEKALI di kelas induk.
- Laboratorium menyimpan daftar alat (agregasi: alat dibuat di luar lalu
  didaftarkan). Peminjaman juga menyimpan alat yang dipinjam (agregasi:
  alat tetap ada setelah peminjaman selesai) dan mengenal Mahasiswa
  peminjamnya (asosiasi).
- Semua atribut berawalan _ dan dibaca lewat @property. Data yang tidak
  valid ditolak dengan raise ValueError(...).

Cara menjalankan (dari folder python/solusi; macOS/Linux: python3):
    python soal_c1_peminjaman_alat.py
"""

DENDA_ELEKTRONIK = 10000  # denda keterlambatan per hari, dalam Rupiah
DENDA_KIT = 5000
MAKS_HARI_PINJAM = 7
LEBAR_BUKTI = 40


def format_rupiah(angka: int) -> str:
    """Mengubah 30000 menjadi 'Rp30.000'."""
    return f"Rp{angka:,}".replace(",", ".")


class Mahasiswa:
    """Peminjam alat. Datanya hanya bisa dibaca dari luar (read-only)."""

    def __init__(self, nim: str, nama: str):
        self._nim = nim
        self._nama = nama

    @property
    def nim(self) -> str:
        return self._nim

    @property
    def nama(self) -> str:
        return self._nama

    def __str__(self) -> str:
        return f"{self._nama} ({self._nim})"


class Alat:
    """Kelas induk: data dan perilaku yang dimiliki SEMUA alat lab."""

    def __init__(self, kode: str, nama: str, denda_per_hari: int):
        if denda_per_hari <= 0:
            raise ValueError("Denda per hari harus lebih dari 0")
        self._kode = kode
        self._nama = nama
        self._denda_per_hari = denda_per_hari
        self._tersedia = True  # [1] alat baru selalu tersedia

    @property
    def kode(self) -> str:
        return self._kode

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def denda_per_hari(self) -> int:
        return self._denda_per_hari

    @property
    def tersedia(self) -> bool:
        return self._tersedia

    def pinjamkan(self):
        """Pintu resmi untuk mengubah status menjadi dipinjam."""
        if not self._tersedia:
            raise ValueError(f"{self._nama} sedang dipinjam")  # [2]
        self._tersedia = False

    def terima_kembali(self):
        self._tersedia = True

    def hitung_denda(self, hari_terlambat: int) -> int:
        return self._denda_per_hari * hari_terlambat

    def __str__(self) -> str:
        status = "tersedia" if self._tersedia else "dipinjam"
        return f"[{self._kode}] {self._nama} - {status}"


class AlatElektronik(Alat):
    """Alat yang memakai listrik. Tambahan: daya dalam watt."""

    def __init__(self, kode: str, nama: str, daya_watt: int):
        super().__init__(kode, nama, DENDA_ELEKTRONIK)  # [3] konstruktor induk
        if daya_watt <= 0:
            raise ValueError("Daya harus lebih dari 0 watt")
        self._daya_watt = daya_watt

    @property
    def daya_watt(self) -> int:
        return self._daya_watt

    def __str__(self) -> str:
        # [4] override: pakai teks dari induk, lalu tambahkan info daya
        return f"{super().__str__()} | {self._daya_watt} watt"


class KitPraktikum(Alat):
    """Satu kotak kit berisi banyak komponen. Tambahan: jumlah komponen."""

    def __init__(self, kode: str, nama: str, jumlah_komponen: int):
        super().__init__(kode, nama, DENDA_KIT)
        if jumlah_komponen < 1:
            raise ValueError("Jumlah komponen minimal 1")
        self._jumlah_komponen = jumlah_komponen

    @property
    def jumlah_komponen(self) -> int:
        return self._jumlah_komponen

    def __str__(self) -> str:
        return f"{super().__str__()} | {self._jumlah_komponen} komponen"


class Peminjaman:
    """Satu transaksi: siapa meminjam, alat apa saja, dan berapa lama."""

    _nomor_terakhir = 0  # [5] atribut kelas: penghitung nomor otomatis

    def __init__(self, peminjam: Mahasiswa, lama_hari: int):
        if lama_hari < 1 or lama_hari > MAKS_HARI_PINJAM:
            raise ValueError(f"Lama pinjam harus 1 sampai {MAKS_HARI_PINJAM} hari")
        Peminjaman._nomor_terakhir += 1  # [6] bertambah HANYA jika data valid
        self._nomor = f"PJ{Peminjaman._nomor_terakhir:03d}"  # PJ001, PJ002, ...
        self._peminjam = peminjam  # [7] asosiasi: menyimpan referensi Mahasiswa
        self._lama_hari = lama_hari
        self._daftar_alat: list[Alat] = []  # [8] agregasi: alat dibuat di luar
        self._selesai = False

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def peminjam(self) -> Mahasiswa:
        return self._peminjam

    @property
    def lama_hari(self) -> int:
        return self._lama_hari

    @property
    def selesai(self) -> bool:
        return self._selesai

    @property
    def daftar_alat(self) -> list[Alat]:
        """Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar."""
        return list(self._daftar_alat)

    def tambah_alat(self, alat: Alat):
        if self._selesai:
            raise ValueError(f"Peminjaman {self._nomor} sudah selesai")
        alat.pinjamkan()  # [9] gagal (ValueError) jika alat sedang dipinjam
        self._daftar_alat.append(alat)

    def kembalikan(self, hari_terlambat: int) -> int:
        """Menerima kembali semua alat lalu MENGEMBALIKAN total denda."""
        if self._selesai:
            raise ValueError(f"Peminjaman {self._nomor} sudah selesai")
        if hari_terlambat < 0:
            raise ValueError("Hari terlambat tidak boleh negatif")
        total_denda = 0
        for alat in self._daftar_alat:  # [10] mengirim pesan ke setiap alat
            alat.terima_kembali()
            total_denda += alat.hitung_denda(hari_terlambat)
        self._selesai = True
        return total_denda

    def cetak_bukti(self):
        garis = "=" * LEBAR_BUKTI
        print(garis)
        print(f"BUKTI PEMINJAMAN {self._nomor}")
        print(garis)
        print(f"Peminjam : {self._peminjam}")
        print(f"Lama     : {self._lama_hari} hari")
        print("-" * LEBAR_BUKTI)
        print(f"{'Alat':<30}{'Denda/hari':>10}")
        for alat in self._daftar_alat:
            label = f"[{alat.kode}] {alat.nama}"
            print(f"{label:<30}{format_rupiah(alat.denda_per_hari):>10}")
        print("-" * LEBAR_BUKTI)
        print(f"Jumlah alat: {len(self._daftar_alat)}")
        print(garis)


class Laboratorium:
    """Lab yang punya daftar alat dan catatan peminjaman."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_alat: list[Alat] = []  # agregasi
        self._daftar_peminjaman: list[Peminjaman] = []  # asosiasi (catatan)

    @property
    def nama(self) -> str:
        return self._nama

    def tambah_alat(self, alat: Alat):
        self._daftar_alat.append(alat)

    def cari_alat(self, kode: str) -> Alat | None:
        """Mengembalikan objek Alat dengan kode tertentu, atau None."""
        for alat in self._daftar_alat:
            if alat.kode == kode:
                return alat
        return None

    def buat_peminjaman(self, peminjam: Mahasiswa, lama_hari: int) -> Peminjaman:
        peminjaman = Peminjaman(peminjam, lama_hari)  # gagal jika lama_hari salah
        self._daftar_peminjaman.append(peminjaman)
        return peminjaman

    def jumlah_alat(self) -> int:
        return len(self._daftar_alat)

    def jumlah_alat_tersedia(self) -> int:
        jumlah = 0
        for alat in self._daftar_alat:
            if alat.tersedia:
                jumlah += 1
        return jumlah

    def jumlah_peminjaman(self) -> int:
        return len(self._daftar_peminjaman)

    def tampilkan_alat(self):
        print(f"=== ALAT {self._nama} ===")
        for alat in self._daftar_alat:
            print(alat)  # memanggil __str__ milik kelas anak


def siapkan_lab() -> Laboratorium:
    """Membuat laboratorium beserta empat alat awalnya."""
    lab = Laboratorium("Lab Pemrograman")
    lab.tambah_alat(AlatElektronik("A01", "Proyektor Portabel", 200))
    lab.tambah_alat(AlatElektronik("A02", "Laptop Cadangan", 65))
    lab.tambah_alat(KitPraktikum("K01", "Kit Mikrokontroler", 30))
    lab.tambah_alat(KitPraktikum("K02", "Kit Sensor IoT", 12))
    return lab


def proses_pengembalian(peminjaman: Peminjaman, hari_terlambat: int):
    """Mengembalikan semua alat sebuah peminjaman lalu mencetak dendanya."""
    denda = peminjaman.kembalikan(hari_terlambat)
    if hari_terlambat == 0:
        keterangan = "tepat waktu"
    else:
        keterangan = f"terlambat {hari_terlambat} hari"
    print(f"{peminjaman.nomor} kembali {keterangan}, denda {format_rupiah(denda)}")


def tampilkan_status(lab: Laboratorium):
    lab.tampilkan_alat()
    print(f"Alat tersedia: {lab.jumlah_alat_tersedia()} dari {lab.jumlah_alat()}")


def main():
    lab = siapkan_lab()
    lab.tampilkan_alat()
    print()

    print("=== DATA TIDAK VALID DITOLAK ===")
    try:
        lab.tambah_alat(AlatElektronik("A03", "Solder Listrik", 0))
    except ValueError as e:
        print(f"Gagal menambah alat: {e}")
    ayu = Mahasiswa("2409106001", "Ayu Lestari")
    bima = Mahasiswa("2409106002", "Bima Saputra")
    try:
        lab.buat_peminjaman(ayu, 10)
    except ValueError as e:
        print(f"Gagal membuat peminjaman: {e}")
    if lab.cari_alat("X99") is None:
        print("Cari X99: alat tidak ditemukan")
    print()

    print("=== PEMINJAMAN ===")
    pinjam_ayu = lab.buat_peminjaman(ayu, 3)
    pinjam_ayu.tambah_alat(lab.cari_alat("A01"))
    pinjam_ayu.tambah_alat(lab.cari_alat("K01"))
    pinjam_ayu.cetak_bukti()

    pinjam_bima = lab.buat_peminjaman(bima, 2)
    try:
        pinjam_bima.tambah_alat(lab.cari_alat("A01"))  # masih dipinjam Ayu
    except ValueError as e:
        print(f"Gagal meminjam: {e}")
    pinjam_bima.tambah_alat(lab.cari_alat("A02"))
    pinjam_bima.cetak_bukti()
    print()

    print("=== SETELAH PEMINJAMAN ===")
    tampilkan_status(lab)
    print()

    print("=== PENGEMBALIAN ===")
    proses_pengembalian(pinjam_ayu, 2)
    proses_pengembalian(pinjam_bima, 0)
    try:
        proses_pengembalian(pinjam_ayu, 1)  # sudah dikembalikan sebelumnya
    except ValueError as e:
        print(f"Gagal mengembalikan: {e}")
    print()

    print("=== STATUS AKHIR ===")
    tampilkan_status(lab)
    print(f"Peminjaman tercatat: {lab.jumlah_peminjaman()}")


if __name__ == "__main__":
    main()
