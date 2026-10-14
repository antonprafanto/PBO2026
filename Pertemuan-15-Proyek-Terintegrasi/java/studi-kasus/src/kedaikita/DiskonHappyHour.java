package kedaikita;

import java.util.List;

/** Happy hour: diskon 20% khusus untuk item minuman. */
public class DiskonHappyHour implements Diskon {
    private static final int PERSEN = 20;

    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        int totalMinuman = 0;
        for (ItemPesanan item : daftarItem) {
            if (item.getMenu().getKategori().equals("Minuman")) {
                totalMinuman += item.hitungSubtotal();
            }
        }
        return totalMinuman * PERSEN / 100;
    }

    @Override
    public String keterangan() {
        return "Happy Hour (minuman)";
    }
}
