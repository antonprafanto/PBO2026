/*
 * Contoh 01 - Exception Pertama: Pembagian dengan Nol
 * Pertemuan 11 - Exception Handling
 *
 * Membagi bilangan bulat (int) dengan nol tidak mungkin dilakukan. Java lalu
 * MELEMPAR exception bernama ArithmeticException. Jika tidak ditangkap,
 * program berhenti mendadak. Dengan try/catch, exception itu kita TANGKAP
 * sehingga program tetap berjalan sampai selesai.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01PembagianNol.java
 */
public class Contoh01PembagianNol {

    /** Membagi tagihan sama rata ke semua orang (sisa pembagian dibuang). */
    static int hitungPatungan(int total, int jumlahOrang) {
        return total / jumlahOrang; // [1] gagal jika jumlahOrang = 0
    }

    public static void main(String[] args) {
        System.out.println("=== PATUNGAN MAKAN DI WARUNG ===");
        int perOrang = hitungPatungan(120000, 4);
        System.out.println("Rp120000 dibagi 4 orang: Rp" + perOrang + " per orang");

        System.out.println();
        System.out.println("=== JIKA JUMLAH ORANG NOL ===");
        try { // [2] "coba jalankan blok ini"
            System.out.println("Menghitung patungan untuk 0 orang...");
            int hasil = hitungPatungan(120000, 0); // [3] exception dilempar di sini
            System.out.println("Hasil: Rp" + hasil + " per orang"); // [4] baris ini DILEWATI
        } catch (ArithmeticException e) { // [5] exception ditangkap di sini
            System.out.println("Gagal: jumlah orang tidak boleh nol");
        }
        System.out.println("Program tetap berjalan sampai baris terakhir"); // [6]
    }
}
