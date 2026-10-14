/*
 * Contoh 05 - Representasi Teks Objek dengan toString()
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Tanpa toString(), System.out.println(objek) hanya menampilkan sesuatu
 * seperti Motor@1b6d3586 yang tidak berguna bagi pembaca.
 * Setiap kelas Java sudah punya toString() bawaan. Dengan @Override, kita
 * MENIMPA versi bawaan itu dengan teks buatan kita sendiri
 * (detail tentang override dibahas di Pertemuan 07).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05ToString.java
 */
public class Contoh05ToString {

    public static void main(String[] args) {
        Motor motorBudi = new Motor("KT 1234 AB", "Honda Beat", "merah");
        Motor motorSiti = new Motor("KT 5678 CD", "Yamaha NMAX", "hitam");

        System.out.println("=== MENCETAK OBJEK LANGSUNG ===");
        System.out.println(motorBudi); // [3] println memanggil motorBudi.toString()
        System.out.println(motorSiti);

        System.out.println();
        System.out.println("=== DIPAKAI DI DALAM TEKS LAIN ===");
        System.out.println("Motor Budi: " + motorBudi); // [4] penggabungan teks juga memanggilnya
        String teks = motorSiti.toString();             // [5] boleh juga dipanggil langsung
        System.out.println("Teks motor Siti terdiri atas " + teks.length() + " karakter");

        System.out.println();
        System.out.println("=== SETELAH WARNA DIUBAH ===");
        motorBudi.warna = "biru";
        System.out.println(motorBudi); // [6] teks selalu mengikuti nilai atribut terbaru
    }
}

/** Motor mahasiswa yang terdaftar di parkiran kampus. */
class Motor {
    String plat;
    String merek;
    String warna;

    Motor(String plat, String merek, String warna) {
        this.plat = plat;
        this.merek = merek;
        this.warna = warna;
    }

    @Override // [1] menandai bahwa kita menimpa toString() bawaan
    public String toString() { // [2] wajib public; mengembalikan teks, bukan mencetak
        return plat + " - " + merek + " (" + warna + ")";
    }
}
