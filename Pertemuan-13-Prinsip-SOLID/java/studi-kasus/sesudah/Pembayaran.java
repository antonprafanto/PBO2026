/*
 * File Pembayaran.java: kelas abstrak Pembayaran. Tiga kelas anaknya ada di
 * PembayaranTunai.java, PembayaranQRIS.java, dan PembayaranKartu.java.
 *
 * Yang baru di Pertemuan 11:
 * - proses() tidak lagi mengembalikan true/false.
 *   Jika berhasil, ia selesai dengan tenang. Jika gagal, ia MELEMPAR
 *   PembayaranGagalException. Pemanggil tidak bisa "lupa" mengecek kegagalan
 *   (compiler Java bahkan mewajibkan pemanggil menangani checked exception ini).
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
