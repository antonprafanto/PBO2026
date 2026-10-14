/*
 * Solusi Latihan 03 - Frekuensi Kata
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Bersihkan teks: jadikan huruf kecil, buang titik dan koma, pecah per spasi.
 * - Hitung dengan Map: frekuensi.put(kata, frekuensi.getOrDefault(kata, 0) + 1)
 * - Salin entrySet() ke List, lalu urutkan dengan lambda pembanding:
 *   jumlah terbanyak dulu; jika seri, kata diurutkan A-Z.
 * - Kata yang muncul sekali dikumpulkan ke TreeSet agar langsung urut.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03FrekuensiKata.java
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.TreeSet;

public class Latihan03FrekuensiKata {

    static final String TEKS = "Kopi susu gula aren enak. Kopi hitam juga enak, "
            + "tapi kopi susu paling laris di kedai.";

    static Map<String, Integer> hitungFrekuensi(String teks) {
        String bersih = teks.toLowerCase().replace(".", "").replace(",", "");
        Map<String, Integer> frekuensi = new HashMap<>(); // tidak dicetak langsung
        for (String kata : bersih.split(" ")) {
            frekuensi.put(kata, frekuensi.getOrDefault(kata, 0) + 1);
        }
        return frekuensi;
    }

    public static void main(String[] args) {
        Map<String, Integer> frekuensi = hitungFrekuensi(TEKS);
        List<Map.Entry<String, Integer>> urut = new ArrayList<>(frekuensi.entrySet());
        urut.sort((a, b) -> {
            int banding = Integer.compare(b.getValue(), a.getValue()); // terbanyak dulu
            if (banding != 0) {
                return banding;
            }
            return a.getKey().compareTo(b.getKey()); // jika seri: A-Z
        });

        int jumlahKata = 0;
        for (int jumlah : frekuensi.values()) {
            jumlahKata += jumlah;
        }
        System.out.println("=== FREKUENSI KATA ===");
        System.out.println("Jumlah kata     : " + jumlahKata);
        System.out.println("Jumlah kata unik: " + frekuensi.size());
        System.out.println("3 kata terbanyak:");
        for (int i = 0; i < 3; i++) {
            Map.Entry<String, Integer> entri = urut.get(i);
            System.out.println("  " + (i + 1) + ". " + entri.getKey() + " (" + entri.getValue()
                    + " kali)");
        }
        Set<String> sekali = new TreeSet<>();
        for (Map.Entry<String, Integer> entri : frekuensi.entrySet()) {
            if (entri.getValue() == 1) {
                sekali.add(entri.getKey());
            }
        }
        System.out.println("Muncul sekali   : " + String.join(", ", sekali));
    }
}
