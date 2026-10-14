/*
 * File Pembayaran.java: kelas ABSTRAK Pembayaran. Tiga kelas anaknya ada di
 * PembayaranTunai.java, PembayaranQRIS.java, dan PembayaranKartu.java.
 *
 * Yang baru di Pertemuan 10:
 * - Pembayaran kini kelas abstrak (abstract class). Objeknya TIDAK BISA dibuat
 *   langsung karena "pembayaran umum" memang tidak ada di dunia nyata.
 * - namaMetode() dan proses() menjadi method abstrak: setiap kelas anak
 *   WAJIB meng-override keduanya.
 * - hitungBiayaLayanan() tetap method biasa (konkret), dan deskripsi()
 *   adalah method konkret baru. Keduanya langsung diwarisi kelas anak.
 */

/** Kelas abstrak: kerangka untuk semua metode pembayaran. */
public abstract class Pembayaran {

    /** Nama metode pembayaran, misalnya "Tunai". */
    public abstract String namaMetode();

    /** Memproses pembayaran. Mengembalikan true jika berhasil. */
    public abstract boolean proses(int total);

    /** Biaya tambahan untuk pelanggan. Bawaannya 0 (boleh di-override). */
    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    /** Method konkret yang memanggil method abstrak. */
    public String deskripsi(int total) {
        String biaya = Rupiah.format(hitungBiayaLayanan(total));
        return namaMetode() + " (biaya layanan " + biaya + ")";
    }
}
