/*
 * Contoh 02 - Set: Kumpulan Tanpa Data Kembar
 * Pertemuan 12 - Koleksi dan Generics
 *
 * - HashSet otomatis membuang data kembar (duplikat).
 * - Operasi himpunan: irisan (retainAll), gabungan (addAll), selisih (removeAll).
 *   Ketiganya MENGUBAH set yang memanggilnya, jadi kita kerjakan pada salinan.
 * - URUTAN isi HashSet TIDAK dijamin. Untuk dicetak, isinya dipindah dulu ke
 *   TreeSet, yaitu set yang isinya selalu urut.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02SetHimpunan.java
 */
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Contoh02SetHimpunan {

    /** Mencetak isi set dalam urutan abjad agar hasilnya selalu sama. */
    static void cetak(String judul, Set<String> isi) {
        Set<String> urut = new TreeSet<>(isi); // [5] TreeSet: isinya selalu urut
        System.out.println(String.format("%-14s: %s", judul, String.join(", ", urut)));
    }

    public static void main(String[] args) {
        List<String> pendaftar = List.of("Ayu", "Bima", "Citra", "Ayu", "Dimas", "Bima"); // [1]
        Set<String> pesertaPython = new HashSet<>(pendaftar); // [2] duplikat hilang
        Set<String> pesertaJava = new HashSet<>(List.of("Citra", "Eka", "Ayu", "Fajar")); // [3]

        System.out.println("=== PENDAFTARAN WORKSHOP PYTHON ===");
        System.out.println("Formulir masuk: " + pendaftar.size());
        System.out.println("Peserta unik  : " + pesertaPython.size());
        cetak("Peserta Python", pesertaPython);
        pesertaPython.add("Eka"); // [4] tambah anggota baru (add mengembalikan true)
        pesertaPython.add("Ayu"); // sudah ada: diabaikan (add mengembalikan false)
        System.out.println("Setelah tambah Eka dan Ayu: " + pesertaPython.size() + " peserta");

        System.out.println();
        System.out.println("=== OPERASI HIMPUNAN ===");
        cetak("Peserta Java", pesertaJava);
        Set<String> irisan = new HashSet<>(pesertaPython); // [6] salin dulu!
        irisan.retainAll(pesertaJava);
        cetak("Ikut keduanya", irisan);
        Set<String> gabungan = new HashSet<>(pesertaPython);
        gabungan.addAll(pesertaJava);
        cetak("Semua peserta", gabungan);
        Set<String> selisih = new HashSet<>(pesertaPython);
        selisih.removeAll(pesertaJava);
        cetak("Hanya Python", selisih);
        if (!pesertaPython.contains("Fajar")) { // [7] cek keanggotaan
            System.out.println("Fajar belum ikut workshop Python");
        }
    }
}
