/*
 * Contoh 04 - Menjelajahi Isi Map dan Menjaga Urutan
 * Pertemuan 12 - Koleksi dan Generics
 *
 * - Menghitung kemunculan: hitung.put(k, hitung.getOrDefault(k, 0) + 1)
 * - Tiga cara menjelajah: keySet() (kunci), values() (nilai),
 *   dan entrySet() (pasangan kunci-nilai).
 * - Memilih wujud Map sesuai kebutuhan urutan:
 *     HashMap       -> urutan TIDAK dijamin (jangan dicetak apa adanya)
 *     LinkedHashMap -> urutan saat kunci pertama kali dimasukkan
 *     TreeMap       -> kunci selalu urut (abjad / angka)
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04IterasiMap.java
 */
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.TreeMap;

public class Contoh04IterasiMap {

    public static void main(String[] args) {
        List<String> suara = List.of("Bima", "Ayu", "Bima", "Citra", "Ayu", "Bima"); // [1]
        Map<String, Integer> hitung = new LinkedHashMap<>(); // menjaga urutan masuk
        for (String nama : suara) {
            hitung.put(nama, hitung.getOrDefault(nama, 0) + 1); // [2] belum ada -> mulai dari 0
        }

        System.out.println("=== HASIL PEMILIHAN KETUA HIMPUNAN ===");
        System.out.println("Kandidat   : " + String.join(", ", hitung.keySet())); // [3] kunci saja
        int total = 0;
        for (int jumlah : hitung.values()) { // [4] nilai saja (unboxing Integer -> int)
            total += jumlah;
        }
        System.out.println("Total suara: " + total);
        for (Map.Entry<String, Integer> entri : hitung.entrySet()) { // [5] pasangan kunci-nilai
            System.out.println(entri.getKey() + ": " + entri.getValue() + " suara");
        }

        System.out.println();
        System.out.println("=== URUT NAMA KANDIDAT (A-Z) ===");
        Map<String, Integer> urut = new TreeMap<>(hitung); // [6] TreeMap: kunci selalu urut
        for (Map.Entry<String, Integer> entri : urut.entrySet()) {
            System.out.println(entri.getKey() + ": " + entri.getValue() + " suara");
        }

        System.out.println();
        System.out.println("=== PERSENTASE (dibulatkan ke bawah) ===");
        Map<String, Integer> persen = new LinkedHashMap<>(); // [7] Map baru dari Map lama
        for (Map.Entry<String, Integer> entri : hitung.entrySet()) {
            persen.put(entri.getKey(), entri.getValue() * 100 / total);
        }
        for (Map.Entry<String, Integer> entri : persen.entrySet()) {
            System.out.println(entri.getKey() + ": " + entri.getValue() + "%");
        }
    }
}
