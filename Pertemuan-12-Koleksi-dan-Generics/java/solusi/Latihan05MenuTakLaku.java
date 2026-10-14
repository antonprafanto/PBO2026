/*
 * Solusi Latihan 05 - KedaiKita: Porsi per Menu, Menu Tak Laku, Rata-rata Porsi
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Daftar menu disimpan di LinkedHashMap kode -> nama (urutan sesuai daftar).
 * - Setiap pesanan lunas = List<ItemBeli>. Datanya sama dengan 4 pesanan
 *   lunas di studi kasus, ditambah dua menu baru (M06, M07).
 * - porsiPerMenu(): semua kode diisi 0 dulu, supaya menu yang tidak pernah
 *   dipesan tetap muncul dengan angka 0.
 * - menuTakLaku(): selisih himpunan = semua kode - kode yang pernah terjual.
 *   Dipakai TreeSet agar hasilnya langsung urut kode.
 * - Rata-rata porsi = total porsi / jumlah pesanan. Agar tetap bilangan bulat,
 *   hitung "kali 100" dulu: 11 * 100 / 4 = 275, lalu dicetak sebagai 2.75.
 *
 * Catatan nama kelas: kelas di sini bernama ItemBeli dan AnalisisPenjualan,
 * BUKAN ItemPesanan atau LaporanPenjualan. Folder java/ pertemuan ini sudah
 * punya kelas-kelas itu (di studi-kasus), dan editor seperti VS Code akan
 * protes "The type ... is already defined" jika ada dua kelas bernama sama.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05MenuTakLaku.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Latihan05MenuTakLaku {

    public static void main(String[] args) {
        Map<String, String> daftarMenu = new LinkedHashMap<>();
        daftarMenu.put("M01", "Kopi Susu Gula Aren");
        daftarMenu.put("M02", "Es Teh Manis");
        daftarMenu.put("M03", "Nasi Goreng Kampung");
        daftarMenu.put("M04", "Mie Goreng Jawa");
        daftarMenu.put("M05", "Pisang Goreng Keju");
        daftarMenu.put("M06", "Teh Tarik");
        daftarMenu.put("M07", "Roti Bakar Cokelat");
        List<List<ItemBeli>> pesananLunas = List.of(
                List.of(new ItemBeli("M01", 2), new ItemBeli("M03", 1)),  // P001 Budi
                List.of(new ItemBeli("M02", 2), new ItemBeli("M05", 1)),  // P002 Siti
                List.of(new ItemBeli("M01", 1), new ItemBeli("M04", 1)),  // P003 Rina
                List.of(new ItemBeli("M01", 1), new ItemBeli("M02", 2))); // P004 Budi
        AnalisisPenjualan analisis = new AnalisisPenjualan(daftarMenu, pesananLunas);

        System.out.println("=== PORSI TERJUAL PER MENU ===");
        for (Map.Entry<String, Integer> entri : analisis.porsiPerMenu().entrySet()) {
            String kode = entri.getKey();
            System.out.println(String.format("%s %-24s%3d", kode, daftarMenu.get(kode),
                    entri.getValue()));
        }

        System.out.println();
        System.out.println("=== RINGKASAN ===");
        int rata = analisis.rataRataPorsiX100();
        System.out.println("Pesanan lunas  : " + pesananLunas.size());
        System.out.println("Total porsi    : " + analisis.totalPorsi());
        System.out.println("Rata-rata porsi: " + (rata / 100) + "."
                + String.format("%02d", rata % 100) + " porsi per pesanan");
        List<String> namaTakLaku = new ArrayList<>();
        for (String kode : analisis.menuTakLaku()) {
            namaTakLaku.add(daftarMenu.get(kode));
        }
        System.out.println("Menu tak laku  : " + String.join(", ", namaTakLaku));
    }
}

/** Satu baris pesanan: kode menu dan jumlah porsi. */
class ItemBeli {
    private String kode;
    private int jumlah;

    public ItemBeli(String kode, int jumlah) {
        this.kode = kode;
        this.jumlah = jumlah;
    }

    public String getKode() {
        return kode;
    }

    public int getJumlah() {
        return jumlah;
    }
}

/** Analisis tambahan untuk laporan penjualan KedaiKita. */
class AnalisisPenjualan {
    private Map<String, String> daftarMenu;
    private List<List<ItemBeli>> pesananLunas;

    public AnalisisPenjualan(Map<String, String> daftarMenu, List<List<ItemBeli>> pesananLunas) {
        this.daftarMenu = daftarMenu;
        this.pesananLunas = pesananLunas;
    }

    public Map<String, Integer> porsiPerMenu() {
        Map<String, Integer> hasil = new LinkedHashMap<>();
        for (String kode : daftarMenu.keySet()) {
            hasil.put(kode, 0); // semua mulai dari 0
        }
        for (List<ItemBeli> pesanan : pesananLunas) {
            for (ItemBeli item : pesanan) {
                hasil.put(item.getKode(), hasil.get(item.getKode()) + item.getJumlah());
            }
        }
        return hasil;
    }

    public Set<String> menuTakLaku() {
        Set<String> terjual = new TreeSet<>();
        for (List<ItemBeli> pesanan : pesananLunas) {
            for (ItemBeli item : pesanan) {
                terjual.add(item.getKode());
            }
        }
        Set<String> takLaku = new TreeSet<>(daftarMenu.keySet());
        takLaku.removeAll(terjual);
        return takLaku;
    }

    public int totalPorsi() {
        int total = 0;
        for (int porsi : porsiPerMenu().values()) {
            total += porsi;
        }
        return total;
    }

    public int rataRataPorsiX100() {
        return totalPorsi() * 100 / pesananLunas.size();
    }
}
