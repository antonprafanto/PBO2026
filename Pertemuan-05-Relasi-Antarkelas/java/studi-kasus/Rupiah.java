/*
 * File Rupiah.java: kelas utilitas KedaiKita, berisi method bantu yang dipakai
 * banyak kelas.
 *
 * Java tidak punya fungsi yang berdiri sendiri di luar kelas. Karena itu,
 * fungsi bantu ditulis sebagai method static dan dipanggil lewat nama
 * kelasnya, misalnya Rupiah.format(18000).
 *
 * Kelas ini tidak punya method main, jadi tidak bisa dijalankan sendiri.
 * Yang dijalankan adalah kelas Main (lihat Main.java).
 */

import java.util.Locale;

/** Kelas utilitas untuk menampilkan uang dalam format Rupiah. */
public class Rupiah {

    /** Mengubah 18000 menjadi "Rp18.000". */
    public static String format(int angka) {
        // Locale.US menjamin pemisah ribuan selalu koma (lalu diganti titik),
        // apa pun pengaturan bahasa di komputer yang menjalankan program.
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}
