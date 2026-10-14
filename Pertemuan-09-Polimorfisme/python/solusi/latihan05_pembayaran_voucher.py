"""
Solusi Latihan 05 - KedaiKita: Bayar dengan Voucher
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- PembayaranVoucher adalah anak Pembayaran (is-a), sama seperti
  PembayaranTunai, PembayaranQRIS, dan PembayaranKartu.
- Ia meng-override nama_metode() dan proses(). hitung_biaya_layanan() tidak
  ditulis ulang: voucher tidak dikenai biaya, jadi versi induk (0) dipakai.
- Voucher hanya bisa dipakai SEKALI. Sisa nilainya hangus.
- Method Pesanan.bayar() TIDAK DIUBAH SAMA SEKALI (disalin apa adanya dari
  studi kasus), tetapi langsung bisa menerima PembayaranVoucher.

Supaya file ini bisa dijalankan sendiri, Pelanggan, Pembayaran,
PembayaranTunai, dan Pesanan disalin dalam versi RINGKAS (Pesanan langsung
diberi total, tanpa ItemPesanan). Di salinan studi kasus milikmu (di folder
latihanmu, bukan di folder materi), cukup tambahkan kelas PembayaranVoucher
ke pembayaran.py, lalu pakai di main.py.

Cara menjalankan:
    python latihan05_pembayaran_voucher.py
"""


def format_rupiah(angka: int) -> str:
    return f"Rp{angka:,}".replace(",", ".")


class Pelanggan:
    """Versi ringkas Pelanggan: nama dan poin saja."""

    def __init__(self, nama: str):
        self._nama = nama
        self._poin = 0

    @property
    def nama(self) -> str:
        return self._nama

    @property
    def poin(self) -> int:
        return self._poin

    def tambah_poin(self, jumlah: int):
        self._poin += jumlah


class Pembayaran:
    """Kelas induk semua metode pembayaran (salinan dari studi kasus)."""

    def nama_metode(self) -> str:
        return "Pembayaran umum"

    def hitung_biaya_layanan(self, total: int) -> int:
        return 0

    def proses(self, total: int) -> bool:
        print(f"  Memproses pembayaran {format_rupiah(total)}")
        return True


class PembayaranTunai(Pembayaran):
    """Salinan dari studi kasus."""

    def __init__(self, uang_diterima: int):
        self._uang_diterima = uang_diterima
        self._kembalian = 0

    def nama_metode(self) -> str:
        return "Tunai"

    def proses(self, total: int) -> bool:
        if self._uang_diterima < total:
            kurang = total - self._uang_diterima
            print(f"  Uang kurang {format_rupiah(kurang)}")
            return False
        self._kembalian = self._uang_diterima - total
        print(f"  Uang diterima {format_rupiah(self._uang_diterima)}, "
              f"kembalian {format_rupiah(self._kembalian)}")
        return True


class PembayaranVoucher(Pembayaran):
    """KELAS BARU: bayar dengan voucher bernilai tetap, sekali pakai."""

    def __init__(self, kode: str, nilai: int):
        self._kode = kode
        self._nilai = nilai
        self._terpakai = False

    def nama_metode(self) -> str:
        return f"Voucher {self._kode}"

    def proses(self, total: int) -> bool:
        if self._terpakai:
            print(f"  Voucher {self._kode} sudah pernah dipakai")
            return False
        if self._nilai < total:
            print(f"  Nilai voucher {format_rupiah(self._nilai)} tidak cukup")
            return False
        self._terpakai = True
        sisa = self._nilai - total
        print(f"  Voucher {self._kode} dipakai, sisa {format_rupiah(sisa)} hangus")
        return True


class Pesanan:
    """Versi ringkas Pesanan: total langsung diisi saat pesanan dibuat."""

    def __init__(self, nomor: str, pelanggan: Pelanggan, total: int):
        self._nomor = nomor
        self._pelanggan = pelanggan
        self._total = total
        self._status = "BARU"

    @property
    def nomor(self) -> str:
        return self._nomor

    @property
    def status(self) -> str:
        return self._status

    def hitung_total(self) -> int:
        return self._total

    def bayar(self, pembayaran: Pembayaran) -> bool:
        """TIDAK DIUBAH: sama persis dengan Pesanan.bayar() di studi kasus."""
        total = self.hitung_total()
        biaya = pembayaran.hitung_biaya_layanan(total)  # polimorfisme
        total_bayar = total + biaya
        print(f"Pembayaran pesanan {self._nomor} ({self._pelanggan.nama})")
        print(f"  Metode       : {pembayaran.nama_metode()}")  # polimorfisme
        if biaya > 0:
            print(f"  Biaya layanan: {format_rupiah(biaya)}")
        print(f"  Total bayar  : {format_rupiah(total_bayar)}")
        berhasil = pembayaran.proses(total_bayar)  # polimorfisme
        if berhasil:
            self._status = "LUNAS"
            poin = total // 10000
            if poin > 0:
                self._pelanggan.tambah_poin(poin)
            print(f"  Status       : LUNAS (+{poin} poin)")
        else:
            print("  Status       : GAGAL, silakan pilih metode lain")
        return berhasil


def main():
    budi = Pelanggan("Budi Santoso")
    siti = Pelanggan("Siti Aminah")
    voucher = PembayaranVoucher("KEDAI50", 50000)

    print("=== VOUCHER TIDAK CUKUP, GANTI TUNAI ===")
    pesanan1 = Pesanan("P001", budi, 61000)
    if not pesanan1.bayar(voucher):
        pesanan1.bayar(PembayaranTunai(100000))

    print()
    print("=== VOUCHER CUKUP ===")
    pesanan2 = Pesanan("P002", siti, 31000)
    pesanan2.bayar(voucher)

    print()
    print("=== VOUCHER YANG SAMA DIPAKAI LAGI ===")
    pesanan3 = Pesanan("P003", budi, 15000)
    pesanan3.bayar(voucher)

    print()
    print("=== STATUS AKHIR ===")
    for pesanan in [pesanan1, pesanan2, pesanan3]:
        print(f"{pesanan.nomor}: {pesanan.status}")
    print(f"Poin {budi.nama}: {budi.poin}")
    print(f"Poin {siti.nama}: {siti.poin}")


if __name__ == "__main__":
    main()
