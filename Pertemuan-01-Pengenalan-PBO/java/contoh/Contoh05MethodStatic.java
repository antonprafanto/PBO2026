/*
 * Contoh 05 - Method static dengan Parameter dan Nilai Kembalian
 * Pertemuan 01 - Pengenalan PBO
 *
 * - Di Java, "fungsi" ditulis sebagai method di dalam kelas. Untuk program
 *   gaya prosedural seperti ini, method-nya kita beri kata kunci static agar
 *   bisa dipanggil langsung dari main (arti lengkap static: Pertemuan 03).
 * - Tipe nilai kembalian ditulis di depan nama method (int, String, ...).
 *   Method yang tidak mengembalikan apa pun memakai void.
 * - Setiap parameter ditulis lengkap dengan tipenya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05MethodStatic.java
 */
public class Contoh05MethodStatic {

    static final int TARIF_DASAR = 10000; // [1] konstanta: final = nilainya tidak bisa diubah
    static final int TARIF_PER_KM = 2500;

    /** Tarif dasar untuk 4 km pertama, ditambah tarif per km berikutnya. */
    static int hitungOngkos(int jarakKm) { // [2] mengembalikan int, parameter int jarakKm
        if (jarakKm <= 4) {
            return TARIF_DASAR; // [3] return langsung mengakhiri method
        }
        return TARIF_DASAR + (jarakKm - 4) * TARIF_PER_KM;
    }

    static String labelJarak(int jarakKm) { // method juga boleh mengembalikan String
        if (jarakKm <= 4) {
            return "dekat";
        } else if (jarakKm <= 10) {
            return "sedang";
        } else {
            return "jauh";
        }
    }

    static int hitungPotongan(int total, int persen) { // boleh lebih dari satu parameter
        return total * persen / 100; // persen dihitung dengan bilangan bulat
    }

    static void cetakGaris(int panjang) { // [4] void: tidak mengembalikan nilai
        System.out.println("-".repeat(panjang));
    }

    public static void main(String[] args) {
        System.out.println("=== TARIF OJEK ONLINE ===");
        cetakGaris(32);
        int jarakBudi = 3;
        int jarakSiti = 7;
        int jarakRina = 12;
        int ongkosBudi = hitungOngkos(jarakBudi); // [5] nilai kembalian disimpan ke variabel
        int ongkosSiti = hitungOngkos(jarakSiti);
        int ongkosRina = hitungOngkos(jarakRina);
        // [6] nilai kembalian juga bisa langsung dipakai saat menggabungkan teks
        System.out.println("Budi : " + jarakBudi + " km (" + labelJarak(jarakBudi) + ") -> Rp"
                + ongkosBudi);
        System.out.println("Siti : " + jarakSiti + " km (" + labelJarak(jarakSiti) + ") -> Rp"
                + ongkosSiti);
        System.out.println("Rina : " + jarakRina + " km (" + labelJarak(jarakRina) + ") -> Rp"
                + ongkosRina);
        cetakGaris(32);

        int total = ongkosBudi + ongkosSiti + ongkosRina;
        int potongan = hitungPotongan(total, 20);
        System.out.println("Total ongkos        : Rp" + total);
        System.out.println("Promo 20%           : -Rp" + potongan);
        System.out.println("Total setelah promo : Rp" + (total - potongan));
    }
}
