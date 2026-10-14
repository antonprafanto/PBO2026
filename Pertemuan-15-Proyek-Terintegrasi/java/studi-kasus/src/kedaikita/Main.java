package kedaikita;

/*
 * KedaiKita - Pertemuan 15: Proyek Terintegrasi
 *
 * Titik masuk aplikasi kasir KedaiKita. Semua kelas kini berada di dalam
 * package kedaikita (folder src/kedaikita/, setiap file diawali baris
 * "package kedaikita;") dan data disimpan di folder data/.
 *
 * Cara menjalankan (dari dalam folder studi-kasus):
 *     Windows     : jalankan.bat          -> mode interaktif (kasir mengetik pilihan)
 *                   jalankan.bat --demo   -> mode demo (tanpa input, untuk dicoba cepat)
 *     macOS/Linux : ./jalankan.sh         -> mode interaktif
 *                   ./jalankan.sh --demo  -> mode demo
 * Kedua skrip itu menjalankan dua perintah berikut (tambahkan --demo di
 * perintah kedua untuk mode demo):
 *     javac -d out src/kedaikita/*.java
 *     java -cp out kedaikita.Main
 *
 * Cara menjalankan unit test:
 *     uji.bat (Windows)  atau  ./uji.sh (macOS/Linux)
 */

import java.io.IOException;
import java.io.UncheckedIOException;
import java.nio.file.Path;
import java.util.List;

public class Main {
    // Folder data dicari relatif terhadap folder kerja (working directory).
    // Skrip jalankan.bat/jalankan.sh selalu pindah dulu ke folder studi-kasus,
    // sehingga folder data/ pasti ditemukan.
    private static final Path FOLDER_DATA = Path.of("data");

    public static void main(String[] args) {
        AplikasiKasir aplikasi = new AplikasiKasir(FOLDER_DATA);
        try {
            if (List.of(args).contains("--demo")) {
                aplikasi.jalankanDemo();
            } else {
                aplikasi.jalankan();
            }
        } catch (KedaiException | IOException | UncheckedIOException e) {
            // Lapisan terluar: error tak terduga ditampilkan dengan sopan.
            // (UncheckedIOException = IOException yang dibungkus oleh
            // PencatatTransaksiCSV, lihat penjelasan di file itu.)
            System.out.println("Terjadi kesalahan: " + e.getMessage());
            System.exit(1);
        }
    }
}
