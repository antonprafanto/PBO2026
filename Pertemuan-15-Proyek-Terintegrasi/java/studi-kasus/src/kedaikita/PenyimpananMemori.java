package kedaikita;

import java.util.ArrayList;
import java.util.List;

/** Menyimpan pesanan di list (hilang saat program ditutup). */
public class PenyimpananMemori implements PenyimpananPesanan {
    private List<Pesanan> data;

    public PenyimpananMemori() {
        this.data = new ArrayList<>();
    }

    @Override
    public void simpan(Pesanan pesanan) {
        data.add(pesanan);
    }

    @Override
    public List<Pesanan> semua() {
        return new ArrayList<>(data);
    }
}
