import java.util.List;

/** Aturan diskon paling sederhana: tidak ada potongan sama sekali. */
public class TanpaDiskon implements Diskon {

    @Override
    public int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan) {
        return 0;
    }

    @Override
    public String keterangan() {
        return "Tanpa diskon";
    }
}
