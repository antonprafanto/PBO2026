/*
 * Contoh 09 - Kelas Pembungkus Integer, Autoboxing, dan Jebakannya
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Contoh ini KHUSUS Java (Python tidak punya tipe primitif seperti int Java).
 * - Generics hanya menerima KELAS: List<Integer>, bukan List<int>.
 * - Autoboxing : int -> Integer terjadi otomatis (misalnya saat add ke list).
 * - Unboxing   : Integer -> int terjadi otomatis (saat diambil ke variabel int).
 * - Jebakan 1  : == pada Integer membandingkan OBJEK, bukan angkanya.
 * - Jebakan 2  : list.remove(1) menghapus INDEKS 1, bukan angka 1.
 * - Jebakan 3  : unboxing null menghasilkan NullPointerException.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh09WrapperInteger.java
 */
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Contoh09WrapperInteger {

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        System.out.println("=== AUTOBOXING DAN UNBOXING ===");
        List<Integer> nilaiKuis = new ArrayList<>();
        nilaiKuis.add(85); // [1] int 85 dibungkus otomatis menjadi Integer
        nilaiKuis.add(70);
        int pertama = nilaiKuis.get(0); // [2] Integer dibuka otomatis menjadi int
        System.out.println("Nilai pertama + 5 = " + (pertama + 5));

        System.out.println();
        System.out.println("=== JEBAKAN 1: == PADA Integer ===");
        Integer a = 127;
        Integer b = 127;
        Integer c = 128;
        Integer d = 128;
        System.out.println("127 == 127      ? " + yaTidak(a == b)); // [3] kebetulan ya
        System.out.println("128 == 128      ? " + yaTidak(c == d)); // [4] TIDAK!
        System.out.println("128 equals 128  ? " + yaTidak(c.equals(d))); // [5] cara benar
        System.out.println("128 sebagai int ? " + yaTidak(c.intValue() == d.intValue()));

        System.out.println();
        System.out.println("=== JEBAKAN 2: remove(1) PADA List<Integer> ===");
        List<Integer> angka = new ArrayList<>(List.of(10, 20, 1, 30));
        System.out.println("Awal                     : " + angka);
        angka.remove(1); // [6] menghapus INDEKS 1, yaitu angka 20!
        System.out.println("Setelah remove(1)        : " + angka);
        angka.remove(Integer.valueOf(1)); // [7] menghapus ANGKA 1
        System.out.println("Setelah remove(Integer 1): " + angka);

        System.out.println();
        System.out.println("=== JEBAKAN 3: UNBOXING null ===");
        Map<String, Integer> stok = new HashMap<>();
        stok.put("pulpen", 12);
        Integer stokPensil = stok.get("pensil"); // [8] kunci tidak ada -> null
        if (stokPensil == null) {
            System.out.println("Stok pensil belum tercatat (null)");
        }
        int aman = stok.getOrDefault("pensil", 0); // [9] cara aman
        System.out.println("Stok pensil (getOrDefault): " + aman);
        // int bahaya = stok.get("pensil"); // NullPointerException saat dijalankan!
    }
}
