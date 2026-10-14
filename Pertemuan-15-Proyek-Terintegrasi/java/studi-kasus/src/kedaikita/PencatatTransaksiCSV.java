package kedaikita;

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.StandardOpenOption;
import java.util.ArrayList;
import java.util.List;

/** Observer: mencatat setiap pesanan LUNAS ke file CSV. */
public class PencatatTransaksiCSV implements PengamatPesanan {
    private static final String PEMISAH = RepositoriMenuCSV.PEMISAH; // sama dengan file menu
    private static final List<String> KOLOM_TRANSAKSI =
            List.of("nomor", "pelanggan", "no_hp", "jumlah_porsi", "total");

    private Path path;

    public PencatatTransaksiCSV(Path path, boolean mulaiBaru) throws IOException {
        this.path = path;
        if (mulaiBaru || !Files.exists(path)) {
            Files.writeString(path, String.join(PEMISAH, KOLOM_TRANSAKSI) + "\n",
                    StandardCharsets.UTF_8);
        }
    }

    /** Versi overload: tanpa mulaiBaru berarti melanjutkan file yang sudah ada. */
    public PencatatTransaksiCSV(Path path) throws IOException {
        this(path, false);
    }

    @Override
    public void perbarui(Pesanan pesanan) {
        if (!pesanan.getStatus().equals("LUNAS")) {
            return;
        }
        int porsi = 0;
        for (ItemPesanan item : pesanan.getDaftarItem()) {
            porsi += item.getJumlah();
        }
        List<String> baris = List.of(pesanan.getNomor(), pesanan.getPelanggan().getNama(),
                pesanan.getPelanggan().getNoHp(), String.valueOf(porsi),
                String.valueOf(pesanan.hitungTotal()));
        try {
            Files.writeString(path, String.join(PEMISAH, baris) + "\n", StandardCharsets.UTF_8,
                    StandardOpenOption.CREATE, StandardOpenOption.APPEND);
        } catch (IOException e) {
            // perbarui() berasal dari interface PengamatPesanan yang tidak punya
            // "throws IOException". Karena itu IOException (checked) dibungkus
            // menjadi UncheckedIOException (unchecked) lalu dilempar lagi.
            throw new UncheckedIOException(e.getMessage(), e);
        }
    }

    /** Semua baris transaksi di file (tanpa baris judul). */
    public List<String[]> bacaSemua() throws IOException {
        List<String[]> hasil = new ArrayList<>();
        List<String> semuaBaris = Files.readAllLines(path, StandardCharsets.UTF_8);
        if (semuaBaris.isEmpty()) {
            return hasil; // file kosong: belum ada transaksi
        }
        for (int i = 1; i < semuaBaris.size(); i++) { // mulai dari 1: lewati baris judul kolom
            String baris = semuaBaris.get(i);
            if (!baris.isEmpty()) {
                hasil.add(baris.split(PEMISAH, -1));
            }
        }
        return hasil;
    }
}
