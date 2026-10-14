package kedaikita;

/**
 * Pengamat (observer) konkret: mengirim kabar status pesanan ke nomor HP
 * pelanggan (simulasi SMS).
 */
public class NotifikasiPelanggan implements PengamatPesanan {

    @Override
    public void perbarui(Pesanan pesanan) {
        Pelanggan pelanggan = pesanan.getPelanggan();
        System.out.println("  [SMS ke " + pelanggan.getNoHp() + "] Halo " + pelanggan.getNama()
                + ", status pesanan " + pesanan.getNomor() + ": " + pesanan.getStatus());
    }
}
