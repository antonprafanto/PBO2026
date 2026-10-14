import java.util.List;

/** Diskon 10% untuk pelanggan yang sudah punya minimal 10 poin. */
public class DiskonMember implements Diskon {
    private static final int PERSEN = 10;
    private static final int MINIMAL_POIN = 10;

    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        if (pelanggan.getPoin() < MINIMAL_POIN) {
            return 0;
        }
        return Diskon.subtotalDari(daftarItem) * PERSEN / 100;
    }

    @Override
    public String keterangan() {
        return "Member 10%";
    }
}
