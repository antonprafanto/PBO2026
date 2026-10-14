import java.util.List;

/** Promo potongan sekian persen untuk semua item. */
public class DiskonPersen implements Diskon {
    private int persen;

    public DiskonPersen(int persen) {
        if (persen <= 0 || persen > 100) {
            throw new IllegalArgumentException("Persen diskon harus 1 sampai 100");
        }
        this.persen = persen;
    }

    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        return Diskon.subtotalDari(daftarItem) * persen / 100;
    }

    @Override
    public String keterangan() {
        return "Promo " + persen + "%";
    }
}
