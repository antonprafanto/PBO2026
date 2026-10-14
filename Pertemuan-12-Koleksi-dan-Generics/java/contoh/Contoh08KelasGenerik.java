/*
 * Contoh 08 - Kelas Generik Kotak<T> dan Method Generik
 * Pertemuan 12 - Koleksi dan Generics
 *
 * - class Kotak<T>: T adalah PARAMETER TIPE. Tipe isinya ditentukan saat
 *   dipakai, misalnya Kotak<Integer> atau Kotak<String>.
 * - static <T> T pertama(List<T> daftar): method generik.
 * - Java MEMERIKSA tipe ini saat kompilasi. Mengisi Kotak<Integer> dengan
 *   teks langsung ditolak compiler, dan tidak perlu cast saat mengambil isi.
 * - KotakLama (tanpa generics) memakai Object: boleh diisi apa saja, tetapi
 *   wajib cast saat mengambil isinya dan rawan error saat program berjalan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh08KelasGenerik.java
 */
import java.util.List;

public class Contoh08KelasGenerik {

    /** Mengembalikan isi pertama sebuah list, apa pun tipe isinya. */
    static <T> T pertama(List<T> daftar) { // [4] <T> sebelum tipe kembalian
        return daftar.get(0);
    }

    public static void main(String[] args) {
        Kotak<Integer> kotakAngka = new Kotak<>(42); // [5] di sini T = Integer
        Kotak<String> kotakTeks = new Kotak<>("bekal nasi kuning"); // di sini T = String
        System.out.println("=== KOTAK GENERIK ===");
        System.out.println(kotakAngka);
        System.out.println(kotakTeks);
        int angka = kotakAngka.getIsi(); // tanpa cast
        System.out.println("Isi kotak angka + 8   : " + (angka + 8));
        System.out.println("Isi kotak teks kapital: " + kotakTeks.getIsi().toUpperCase());
        kotakAngka.ganti(100);
        System.out.println("Setelah diganti       : " + kotakAngka);

        System.out.println();
        System.out.println("=== FUNGSI/METHOD GENERIK ===");
        System.out.println("Hari pertama : " + pertama(List.of("Senin", "Rabu", "Jumat")));
        System.out.println("Angka pertama: " + pertama(List.of(10, 20, 30)));

        System.out.println();
        System.out.println("=== KOTAK TANPA TIPE ===");
        KotakLama kotakLama = new KotakLama("pulpen");
        String teks = (String) kotakLama.getIsi(); // [6] wajib cast dari Object
        System.out.println("Isi kotak lama: " + teks.toUpperCase());
    }
}

/** Kotak yang berisi satu barang bertipe T. */
class Kotak<T> { // [1] T = parameter tipe
    private T isi; // [2] tipe field mengikuti T

    public Kotak(T isi) {
        this.isi = isi;
    }

    public T getIsi() { // [3] tipe kembalian mengikuti T
        return isi;
    }

    public void ganti(T isiBaru) {
        this.isi = isiBaru;
    }

    @Override
    public String toString() {
        return "Kotak berisi " + isi;
    }
}

/** Kotak gaya lama (sebelum ada generics): isinya bertipe Object. */
class KotakLama {
    private Object isi;

    public KotakLama(Object isi) {
        this.isi = isi;
    }

    public Object getIsi() {
        return isi;
    }
}
