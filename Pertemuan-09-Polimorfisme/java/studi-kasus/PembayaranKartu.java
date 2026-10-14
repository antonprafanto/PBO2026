/** Kartu kredit: pelanggan dikenai biaya layanan 2%. */
public class PembayaranKartu extends Pembayaran {
    private static final int PERSEN_BIAYA = 2;

    private String namaBank;

    public PembayaranKartu(String namaBank) {
        this.namaBank = namaBank;
    }

    @Override
    public String namaMetode() {
        return "Kartu Kredit " + namaBank;
    }

    @Override
    public int hitungBiayaLayanan(int total) {
        return total * PERSEN_BIAYA / 100;
    }

    @Override
    public boolean proses(int total) {
        System.out.println("  Transaksi kartu " + namaBank + " disetujui "
                + "sebesar " + Rupiah.format(total));
        return true;
    }
}
