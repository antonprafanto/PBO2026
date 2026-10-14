/*
 * Contoh 04 - Overloading Konstruktor dan this(...)
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Java tidak punya nilai bawaan (default) untuk parameter. Sebagai gantinya,
 * kita menulis BEBERAPA konstruktor dengan daftar parameter yang berbeda
 * (overloading). Konstruktor yang pendek meneruskan pekerjaannya ke
 * konstruktor yang lengkap dengan this(...), sambil mengisi nilai bawaannya.
 * Method biasa juga bisa di-overload (dibahas lagi di Pertemuan 09).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04OverloadingKonstruktor.java
 */
public class Contoh04OverloadingKonstruktor {

    public static void main(String[] args) {
        System.out.println("=== MEMBUAT LAPTOP DENGAN JUMLAH ARGUMEN BERBEDA ===");
        Laptop laptopAyu = new Laptop("Asus");             // [5] konstruktor 1 parameter
        Laptop laptopBima = new Laptop("Lenovo", 16);      //     konstruktor 2 parameter
        Laptop laptopCitra = new Laptop("Acer", 16, 1024); //     konstruktor 3 parameter
        Laptop laptopDimas = new Laptop("HP", 8, 256);     // [6] semua nilai ditulis
        System.out.println(laptopAyu.info());
        System.out.println(laptopBima.info());
        System.out.println(laptopCitra.info());
        System.out.println(laptopDimas.info());

        System.out.println();
        System.out.println("=== MENAMBAH RAM ===");
        laptopAyu.tambahRam(); // [7] memakai versi tanpa parameter (tambah 8)
        laptopBima.tambahRam(16);
        System.out.println(laptopAyu.info());
        System.out.println(laptopBima.info());
    }
}

/** Laptop dengan kapasitas RAM dan penyimpanan (dalam GB). */
class Laptop {
    String merek;
    int ram;
    int penyimpanan;

    Laptop(String merek, int ram, int penyimpanan) { // [1] konstruktor lengkap
        this.merek = merek;
        this.ram = ram;
        this.penyimpanan = penyimpanan;
    }

    Laptop(String merek, int ram) { // [2] overloading: daftar parameter berbeda
        this(merek, ram, 512);      // [3] teruskan ke konstruktor lengkap
    }

    Laptop(String merek) {
        this(merek, 8, 512);
    }

    void tambahRam() { // [4] overloading method: nama sama, parameter berbeda
        tambahRam(8);
    }

    void tambahRam(int tambahan) {
        ram = ram + tambahan;
    }

    String info() {
        return merek + ": RAM " + ram + " GB, SSD " + penyimpanan + " GB";
    }
}
