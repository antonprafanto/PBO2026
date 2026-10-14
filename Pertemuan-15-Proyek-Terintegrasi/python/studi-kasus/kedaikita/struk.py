"""
Modul struk: kelas StrukPesanan.

SRP (Single Responsibility): satu-satunya alasan kelas ini berubah adalah
"format struk berubah". Aturan hitung harga tetap di Pesanan dan Diskon.

buat_teks() MENGEMBALIKAN teks (bukan langsung print), sehingga mudah
diuji dan bisa dipakai ulang, misalnya untuk disimpan ke file atau dikirim.

Yang baru di Pertemuan 14: kepala struk memakai nama & alamat dari
PengaturanKedai (Singleton), dan ada baris pajak.
"""

from kedaikita.dapat_dicetak import DapatDicetak
from kedaikita.pengaturan import PengaturanKedai
from kedaikita.pesanan import Pesanan
from kedaikita.utilitas import format_rupiah

LEBAR_STRUK = 40


class StrukPesanan(DapatDicetak):
    """Menyusun dan mencetak struk untuk satu pesanan."""

    def __init__(self, pesanan: Pesanan):
        self._pesanan = pesanan

    @staticmethod
    def _baris_rapi(kiri: str, kanan: str) -> str:
        """Teks kiri rata kiri (30 kolom), teks kanan rata kanan (10 kolom)."""
        return f"{kiri:<30}{kanan:>10}"

    def buat_teks(self) -> str:
        p = self._pesanan
        pengaturan = PengaturanKedai.get_instance()
        garis = "=" * LEBAR_STRUK
        baris = [
            garis,
            pengaturan.nama_kedai,
            pengaturan.alamat,
            garis,
            f"No. Pesanan : {p.nomor}",
            f"Pelanggan   : {p.pelanggan.nama}",
            f"Status      : {p.status}",
            "-" * LEBAR_STRUK,
        ]
        for item in p.daftar_item:
            subtotal = format_rupiah(item.hitung_subtotal())
            baris.append(self._baris_rapi(str(item), subtotal))
        baris.append("-" * LEBAR_STRUK)
        baris.append(self._baris_rapi("Subtotal", format_rupiah(p.hitung_subtotal())))
        potongan = p.hitung_potongan()
        if potongan > 0:
            baris.append(self._baris_rapi(f"Diskon {p.diskon.keterangan()}",
                                          "-" + format_rupiah(potongan)))
        pajak = f"Pajak {pengaturan.pajak_persen}%"
        baris.append(self._baris_rapi(pajak, format_rupiah(p.hitung_pajak())))
        baris.append(self._baris_rapi("TOTAL", format_rupiah(p.hitung_total())))
        baris.append(garis)
        return "\n".join(baris)

    def cetak(self):
        print(self.buat_teks())
