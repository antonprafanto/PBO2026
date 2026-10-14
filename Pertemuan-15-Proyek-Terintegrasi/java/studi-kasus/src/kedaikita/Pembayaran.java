package kedaikita;

/*
 * File Pembayaran.java: kelas abstrak Pembayaran. Tiga kelas anaknya ada di
 * PembayaranTunai.java, PembayaranQRIS.java, dan PembayaranKartu.java.
 *
 * Sejak Pertemuan 11, proses() melempar PembayaranGagalException jika gagal.
 *
 * Yang baru di Pertemuan 14: PembayaranFactory (pola FACTORY, di file
 * PembayaranFactory.java) untuk membuat objek pembayaran dari pilihan berupa
 * teks, misalnya "tunai" atau "qris". Kode pemanggil tidak perlu tahu
 * nama-nama kelas konkretnya.
 */

/** Kelas abstrak: kerangka untuk semua metode pembayaran. */
public abstract class Pembayaran {

    /** Nama metode pembayaran, misalnya "Tunai". */
    public abstract String namaMetode();

    /** Memproses pembayaran. Melempar PembayaranGagalException jika gagal. */
    public abstract void proses(int total) throws PembayaranGagalException;

    /** Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override). */
    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    public String deskripsi(int total) {
        String biaya = Rupiah.format(hitungBiayaLayanan(total));
        return namaMetode() + " (biaya layanan " + biaya + ")";
    }
}
