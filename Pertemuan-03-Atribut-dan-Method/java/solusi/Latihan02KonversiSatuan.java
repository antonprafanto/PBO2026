/*
 * Solusi Latihan 02 - Kelas Utilitas Konversi Satuan
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - Semua method diberi kata kunci static karena tidak membutuhkan data objek.
 *   Kita cukup memanggilnya lewat nama kelas: KonversiSatuan.kmKeMeter(5).
 *   Polanya sama dengan kelas bawaan Java seperti Math (Math.max, Math.min).
 * - Semua perhitungan memakai int:
 *   * detik -> jam, menit, detik memakai / (pembagian int membuang desimal)
 *     dan % (sisa bagi).
 *   * Celsius -> Fahrenheit: celsius * 9 / 5 + 32 (kalikan dulu, baru bagi).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02KonversiSatuan.java
 */
public class Latihan02KonversiSatuan {

    public static void main(String[] args) {
        System.out.println("=== KONVERSI SATUAN (tanpa membuat objek) ===");
        int[] daftarKm = {5, 12};
        for (int km : daftarKm) {
            System.out.println(km + " km = " + KonversiSatuan.kmKeMeter(km) + " meter");
        }
        int[] daftarDetik = {3725, 1985};
        for (int detik : daftarDetik) {
            System.out.println(detik + " detik = " + KonversiSatuan.detikKeTeks(detik));
        }
        int[] daftarCelsius = {0, 25, 30, 100};
        for (int celsius : daftarCelsius) {
            System.out.println(celsius + " C = " + KonversiSatuan.celsiusKeFahrenheit(celsius)
                    + " F");
        }
    }
}

/** Kumpulan method konversi satuan. Tidak perlu dibuat objeknya. */
class KonversiSatuan {

    static int kmKeMeter(int km) {
        return km * 1000;
    }

    static String detikKeTeks(int detik) {
        int jam = detik / 3600;
        int menit = detik % 3600 / 60;
        int sisaDetik = detik % 60;
        return jam + " jam " + menit + " menit " + sisaDetik + " detik";
    }

    static int celsiusKeFahrenheit(int celsius) {
        return celsius * 9 / 5 + 32;
    }
}
