/** Simulasi QRIS: saldo e-wallet pelanggan disimpan di objek ini. */
public class PembayaranQRIS extends Pembayaran {
    private int saldo;

    public PembayaranQRIS(int saldoEwallet) {
        this.saldo = saldoEwallet;
    }

    public int getSaldo() {
        return saldo;
    }

    @Override
    public String namaMetode() {
        return "QRIS";
    }

    @Override
    public boolean proses(int total) {
        if (saldo < total) {
            System.out.println("  Saldo e-wallet tidak cukup "
                    + "(saldo " + Rupiah.format(saldo) + ")");
            return false;
        }
        saldo -= total;
        System.out.println("  Saldo e-wallet terpotong " + Rupiah.format(total)
                + ", sisa " + Rupiah.format(saldo));
        return true;
    }
}
