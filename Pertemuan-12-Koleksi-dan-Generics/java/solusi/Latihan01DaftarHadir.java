/*
 * Solusi Latihan 01 - Daftar Hadir Unik
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Hasil scan QR disimpan di List. Isinya bisa kembar, karena ada mahasiswa
 *   yang memindai dua kali.
 * - Pindahkan ke HashSet agar setiap mahasiswa hanya dihitung sekali.
 * - Operasi himpunan (selalu dikerjakan pada SALINAN, karena retainAll,
 *   addAll, dan removeAll mengubah set yang memanggilnya):
 *     hadir di keduanya  = irisan p1 dan p2           (retainAll)
 *     hadir sekali saja  = gabungan - irisan          (Java tidak punya ^)
 *     belum pernah hadir = kelas - gabungan           (removeAll)
 * - Untuk dicetak, set dipindah ke TreeSet agar urut abjad.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01DaftarHadir.java
 */
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.TreeSet;

public class Latihan01DaftarHadir {

    /** Isi set -> teks berurutan abjad, dipisah koma. */
    static String gabung(Set<String> isi) {
        return String.join(", ", new TreeSet<>(isi));
    }

    public static void main(String[] args) {
        List<String> kelas = List.of("Ayu", "Bima", "Citra", "Dimas", "Eka", "Fajar", "Gita",
                "Hadi");
        List<String> scanP1 = List.of("Ayu", "Bima", "Citra", "Ayu", "Eka", "Gita", "Bima");
        List<String> scanP2 = List.of("Bima", "Citra", "Dimas", "Gita", "Citra");

        Set<String> hadirP1 = new HashSet<>(scanP1);
        Set<String> hadirP2 = new HashSet<>(scanP2);

        Set<String> keduanya = new HashSet<>(hadirP1);
        keduanya.retainAll(hadirP2);
        Set<String> semuaHadir = new HashSet<>(hadirP1);
        semuaHadir.addAll(hadirP2);
        Set<String> sekali = new HashSet<>(semuaHadir);
        sekali.removeAll(keduanya);
        Set<String> belum = new HashSet<>(kelas);
        belum.removeAll(semuaHadir);

        System.out.println("=== REKAP DAFTAR HADIR KELAS PBO ===");
        System.out.println("Pertemuan 1: " + scanP1.size() + " kali scan, " + hadirP1.size()
                + " mahasiswa");
        System.out.println("Pertemuan 2: " + scanP2.size() + " kali scan, " + hadirP2.size()
                + " mahasiswa");
        System.out.println("Hadir di kedua pertemuan: " + gabung(keduanya));
        System.out.println("Hadir sekali saja       : " + gabung(sekali));
        System.out.println("Belum pernah hadir      : " + gabung(belum));
    }
}
