/*
 * Contoh 01 - List: Interface dan Wujudnya
 * Pertemuan 12 - Koleksi dan Generics
 *
 * - List<String> belanja = new ArrayList<>(...);
 *     List      = interface, kontraknya "wadah berurutan"
 *     ArrayList = kelas yang mewujudkan kontrak itu; isinya BISA diubah.
 * - List.of(...) membuat list TETAP (immutable). Java tidak punya tuple,
 *   jadi List.of adalah padanan terdekat untuk "data yang tidak boleh diubah".
 * - Membuat list baru dari list lama memakai perulangan for biasa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01ListDanListTetap.java
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Contoh01ListDanListTetap {

    public static void main(String[] args) {
        List<String> belanja = new ArrayList<>(List.of("beras", "telur", "minyak")); // [1]
        System.out.println("=== LIST: DAFTAR BELANJA ANAK KOS ===");
        System.out.println("Isi awal      : " + String.join(", ", belanja));

        belanja.add("gula");      // [2] tambah di akhir
        belanja.add(0, "kopi");   // sisipkan di indeks 0 (paling depan)
        belanja.remove("minyak"); // [3] hapus berdasarkan ISI, bukan indeks
        belanja.add("telur");     // data kembar boleh
        System.out.println("Setelah diubah: " + String.join(", ", belanja));
        System.out.println("Jumlah item   : " + belanja.size());
        System.out.println("Item pertama  : " + belanja.get(0)); // [4] akses lewat indeks
        System.out.println("Item terakhir : " + belanja.get(belanja.size() - 1));
        if (belanja.contains("gula")) { // [5] cek keanggotaan
            System.out.println("Posisi gula   : indeks " + belanja.indexOf("gula"));
        }
        System.out.println("Telur dicatat : " + Collections.frequency(belanja, "telur") + " kali");

        System.out.println();
        System.out.println("=== DATA TETAP: HARI KULIAH PBO ===");
        List<String> hariKuliah = List.of("Senin", "Rabu"); // [6] list tetap (immutable)
        System.out.println("Hari kuliah   : " + String.join(", ", hariKuliah));
        try {
            hariKuliah.set(0, "Selasa"); // [7] mencoba mengubah isi list tetap
        } catch (UnsupportedOperationException e) {
            System.out.println("Gagal mengubah: isinya tetap (immutable)");
        }

        System.out.println();
        System.out.println("=== MEMBUAT LIST BARU DARI LIST LAMA ===");
        List<String> hurufBesar = new ArrayList<>();
        List<String> pendek = new ArrayList<>();
        for (String barang : belanja) { // [8] Java memakai perulangan biasa
            hurufBesar.add(barang.toUpperCase());
            if (barang.length() <= 4) { // [9] dengan syarat
                pendek.add(barang);
            }
        }
        System.out.println("Huruf besar   : " + String.join(", ", hurufBesar));
        System.out.println("Nama pendek   : " + String.join(", ", pendek));
        System.out.println("List asli     : " + String.join(", ", belanja));
    }
}
