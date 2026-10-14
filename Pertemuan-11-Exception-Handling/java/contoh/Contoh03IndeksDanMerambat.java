/*
 * Contoh 03 - Indeks di Luar Batas dan Exception yang Merambat
 * Pertemuan 11 - Exception Handling
 *
 * Meminta elemen List di posisi yang tidak ada membuat Java melempar
 * IndexOutOfBoundsException. Perhatikan juga PERJALANAN exception-nya:
 *
 *     main() -> umumkan() -> ambilKelompok()   <- exception lahir di sini
 *
 * ambilKelompok() dan umumkan() tidak punya try/catch, jadi exception
 * "merambat" naik ke pemanggilnya, terus sampai ada yang menangkap (main).
 * Baris-baris yang tersisa di method yang dilewati tidak dijalankan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03IndeksDanMerambat.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh03IndeksDanMerambat {

    /** Mengembalikan nama kelompok pada giliran tertentu (mulai dari 1). */
    static String ambilKelompok(List<String> jadwal, int giliran) {
        System.out.println("    [ambil kelompok] mencari giliran " + giliran);
        return jadwal.get(giliran - 1); // [1] IndexOutOfBoundsException jika terlalu besar
    }

    static void umumkan(List<String> jadwal, int giliran) {
        System.out.println("  [umumkan] giliran " + giliran);
        String kelompok = ambilKelompok(jadwal, giliran); // [2] tidak ada try di sini
        System.out.println("  Giliran " + giliran + ": " + kelompok); // [3] dilewati jika ada error
    }

    public static void main(String[] args) {
        List<String> jadwal = new ArrayList<>();
        jadwal.add("Kelompok Pesut");
        jadwal.add("Kelompok Enggang");
        jadwal.add("Kelompok Bekantan");

        System.out.println("=== JADWAL PRESENTASI ===");
        int[] daftarGiliran = {1, 3, 5};
        for (int giliran : daftarGiliran) {
            try {
                umumkan(jadwal, giliran); // [4]
            } catch (IndexOutOfBoundsException e) { // [5] exception merambat sampai ke sini
                System.out.println("  -> Giliran " + giliran + " tidak ada. "
                        + "Hanya ada " + jadwal.size() + " kelompok.");
            }
        }
    }
}
