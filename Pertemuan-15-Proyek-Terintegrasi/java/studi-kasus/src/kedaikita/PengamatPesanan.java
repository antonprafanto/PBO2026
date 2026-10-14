package kedaikita;

/*
 * File PengamatPesanan.java: interface PengamatPesanan untuk pola OBSERVER.
 *
 * Pesanan (subjek) menyimpan daftar pengamat. Setiap kali status pesanan
 * berubah, Pesanan memanggil perbarui() milik SEMUA pengamatnya.
 * Pesanan tidak perlu tahu siapa saja pengamatnya: dapur, pelanggan,
 * layar antrean, atau apa pun yang ditambahkan kelak.
 */

/** Kontrak untuk objek yang ingin diberi tahu perubahan status pesanan. */
public interface PengamatPesanan {

    /**
     * Dipanggil oleh Pesanan setiap kali statusnya berubah.
     *
     * Parameternya langsung bertipe Pesanan, walaupun Pesanan sendiri juga
     * memakai PengamatPesanan. Di Java hal ini aman: tidak ada masalah
     * "circular import" seperti di Python.
     */
    void perbarui(Pesanan pesanan);
}
