import java.util.ArrayList;
import java.util.List;

/** Pengamat (observer) konkret: layar di dapur yang menampilkan pesanan masuk. */
public class LayarDapur implements PengamatPesanan {

    @Override
    public void perbarui(Pesanan pesanan) {
        if (pesanan.getStatus().equals("LUNAS")) {
            List<String> teksItem = new ArrayList<>();
            for (ItemPesanan item : pesanan.getDaftarItem()) {
                teksItem.add(item.toString());
            }
            String daftar = String.join(", ", teksItem);
            System.out.println("  [DAPUR] Pesanan baru " + pesanan.getNomor() + ": " + daftar);
        } else {
            System.out.println("  [DAPUR] " + pesanan.getNomor() + " -> " + pesanan.getStatus());
        }
    }
}
