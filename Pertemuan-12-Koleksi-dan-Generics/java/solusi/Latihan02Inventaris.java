/*
 * Solusi Latihan 02 - Inventaris Sekretariat Himpunan
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Stok disimpan dalam Map: nama barang -> jumlah. Dipakai LinkedHashMap
 *   agar urutan barang sesuai urutan saat pertama kali didaftarkan.
 * - tambah(): barang baru otomatis terdaftar (mulai dari 0 lewat getOrDefault).
 * - ambil(): melempar IllegalArgumentException jika barang tidak terdaftar
 *   atau stok kurang (materi exception Pertemuan 11).
 * - barangHabis(): List barang yang stoknya 0.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02Inventaris.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Latihan02Inventaris {

    static void ambilDanLapor(Inventaris inventaris, String nama, int jumlah) {
        try {
            inventaris.ambil(nama, jumlah);
            System.out.println("Ambil " + nama + " " + jumlah + " -> sisa " + inventaris.cek(nama));
        } catch (IllegalArgumentException e) {
            System.out.println("Ambil " + nama + " " + jumlah + " -> gagal: " + e.getMessage());
        }
    }

    public static void main(String[] args) {
        Inventaris inventaris = new Inventaris();
        inventaris.tambah("spidol", 12);
        inventaris.tambah("kertas HVS (rim)", 5);
        inventaris.tambah("lakban", 3);
        System.out.println("=== INVENTARIS AWAL ===");
        inventaris.tampilkan();

        System.out.println();
        System.out.println("=== TRANSAKSI ===");
        inventaris.tambah("spidol", 6);
        System.out.println("Tambah spidol 6 -> stok " + inventaris.cek("spidol"));
        ambilDanLapor(inventaris, "lakban", 3);
        ambilDanLapor(inventaris, "kertas HVS (rim)", 10);
        ambilDanLapor(inventaris, "stapler", 1);
        inventaris.tambah("stapler", 2);
        System.out.println("Tambah stapler 2 -> stok " + inventaris.cek("stapler"));

        System.out.println();
        System.out.println("=== INVENTARIS AKHIR ===");
        inventaris.tampilkan();
        System.out.println("Jumlah jenis barang: " + inventaris.jumlahJenis());
        System.out.println("Barang habis       : " + String.join(", ", inventaris.barangHabis()));
    }
}

/** Catatan stok barang: nama barang -> jumlah. */
class Inventaris {
    private Map<String, Integer> stok = new LinkedHashMap<>();

    public void tambah(String nama, int jumlah) {
        stok.put(nama, stok.getOrDefault(nama, 0) + jumlah);
    }

    public void ambil(String nama, int jumlah) {
        if (!stok.containsKey(nama)) {
            throw new IllegalArgumentException("barang tidak terdaftar");
        }
        int ada = stok.get(nama);
        if (jumlah > ada) {
            throw new IllegalArgumentException("stok hanya " + ada);
        }
        stok.put(nama, ada - jumlah);
    }

    public int cek(String nama) {
        return stok.getOrDefault(nama, 0);
    }

    public int jumlahJenis() {
        return stok.size();
    }

    public List<String> barangHabis() {
        List<String> hasil = new ArrayList<>();
        for (Map.Entry<String, Integer> entri : stok.entrySet()) {
            if (entri.getValue() == 0) { // Integer dibanding int: di-unboxing, aman
                hasil.add(entri.getKey());
            }
        }
        return hasil;
    }

    public void tampilkan() {
        for (Map.Entry<String, Integer> entri : stok.entrySet()) {
            System.out.println(String.format("  %-18s%4d", entri.getKey(), entri.getValue()));
        }
    }
}
