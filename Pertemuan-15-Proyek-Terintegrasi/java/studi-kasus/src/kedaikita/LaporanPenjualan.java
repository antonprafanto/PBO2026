package kedaikita;

/*
 * File LaporanPenjualan.java: kelas LaporanPenjualan.
 *
 * Contoh nyata pemakaian koleksi:
 * - List   : daftar pesanan yang sudah lunas
 * - Map    : menghitung jumlah porsi per menu & pendapatan per kategori
 * - sort   : mengurutkan menu terlaris (porsi terbanyak dulu)
 * - generik: hasil menu terlaris berupa List<Pasangan<String, Integer>>
 */

import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

/** Ringkasan penjualan dari pesanan-pesanan yang sudah LUNAS. */
public class LaporanPenjualan implements DapatDicetak {
    private static final int LEBAR = 40;

    private List<Pesanan> pesananLunas;

    public LaporanPenjualan(List<Pesanan> daftarPesanan) {
        this.pesananLunas = new ArrayList<>();
        for (Pesanan p : daftarPesanan) {
            if (!p.getStatus().equals("BARU")) { // sudah dibayar
                pesananLunas.add(p);
            }
        }
    }

    public int jumlahPesanan() {
        return pesananLunas.size();
    }

    public int totalPendapatan() {
        int total = 0;
        for (Pesanan pesanan : pesananLunas) {
            total += pesanan.hitungTotal();
        }
        return total;
    }

    /** Nama menu -> total porsi terjual. */
    public Map<String, Integer> jumlahTerjual() {
        Map<String, Integer> hasil = new LinkedHashMap<>();
        for (Pesanan pesanan : pesananLunas) {
            for (ItemPesanan item : pesanan.getDaftarItem()) {
                String nama = item.getMenu().getNama();
                hasil.put(nama, hasil.getOrDefault(nama, 0) + item.getJumlah());
            }
        }
        return hasil;
    }

    /** n menu dengan porsi terbanyak. Jika seri, urut nama A-Z. */
    public List<Pasangan<String, Integer>> menuTerlaris(int n) {
        List<Pasangan<String, Integer>> daftar = new ArrayList<>();
        for (Map.Entry<String, Integer> entri : jumlahTerjual().entrySet()) {
            daftar.add(new Pasangan<>(entri.getKey(), entri.getValue()));
        }
        daftar.sort((a, b) -> {
            int banding = Integer.compare(b.getKedua(), a.getKedua()); // porsi terbanyak dulu
            if (banding != 0) {
                return banding;
            }
            return a.getPertama().compareTo(b.getPertama()); // jika seri: nama A-Z
        });
        return new ArrayList<>(daftar.subList(0, Math.min(n, daftar.size())));
    }

    /** Versi overload: tanpa n berarti 3 menu terlaris. */
    public List<Pasangan<String, Integer>> menuTerlaris() {
        return menuTerlaris(3);
    }

    /**
     * Kategori -> jumlah harga menu terjual (sebelum diskon & pajak).
     *
     * Hasilnya diurutkan berdasarkan nama kategori.
     */
    public Map<String, Integer> pendapatanPerKategori() {
        Map<String, Integer> hasil = new TreeMap<>(); // TreeMap: kunci selalu urut abjad
        for (Pesanan pesanan : pesananLunas) {
            for (ItemPesanan item : pesanan.getDaftarItem()) {
                String kategori = item.getMenu().getKategori();
                hasil.put(kategori, hasil.getOrDefault(kategori, 0) + item.hitungSubtotal());
            }
        }
        return hasil;
    }

    @Override
    public void cetak() {
        String garis = "=".repeat(LEBAR);
        System.out.println(garis);
        System.out.println("LAPORAN PENJUALAN KEDAIKITA");
        System.out.println(garis);
        System.out.println(String.format("%-30s%10d", "Pesanan lunas", jumlahPesanan()));
        String total = Rupiah.format(totalPendapatan());
        System.out.println(String.format("%-30s%10s", "Total pendapatan", total));
        System.out.println("-".repeat(LEBAR));
        System.out.println("Menu terlaris:");
        List<Pasangan<String, Integer>> terlaris = menuTerlaris();
        for (int nomor = 1; nomor <= terlaris.size(); nomor++) {
            Pasangan<String, Integer> pasangan = terlaris.get(nomor - 1);
            System.out.println(nomor + ". " + pasangan.getPertama() + " ("
                    + pasangan.getKedua() + " porsi)");
        }
        System.out.println("-".repeat(LEBAR));
        System.out.println("Penjualan per kategori (sebelum diskon & pajak):");
        for (Map.Entry<String, Integer> entri : pendapatanPerKategori().entrySet()) {
            System.out.println(String.format("%-30s%10s", entri.getKey(),
                    Rupiah.format(entri.getValue())));
        }
        System.out.println(garis);
    }
}
