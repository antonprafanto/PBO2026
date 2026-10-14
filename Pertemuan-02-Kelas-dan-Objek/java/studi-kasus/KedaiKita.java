/*
 * KedaiKita - Pertemuan 02: Kelas dan Objek
 *
 * Versi pertama KedaiKita yang benar-benar memakai kelas.
 * - Kelas Menu adalah cetak biru (blueprint).
 * - kopi, esTeh, dan nasiGoreng adalah objek (hasil cetakan) dari kelas Menu.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KedaiKita.java
 *
 * Catatan: kelas yang memiliki main (KedaiKita) sengaja ditulis PALING ATAS,
 * karena itu syarat menjalankan file dengan perintah "java NamaFile.java".
 */
public class KedaiKita {

    public static void main(String[] args) {
        System.out.println("=== MENU KEDAIKITA ===");
        Menu kopi = new Menu("Kopi Susu Gula Aren", 18000); // [5] membuat objek
        Menu esTeh = new Menu("Es Teh Manis", 8000);
        Menu nasiGoreng = new Menu("Nasi Goreng Kampung", 25000);

        kopi.tampilkanInfo(); // [6] memanggil method milik objek
        esTeh.tampilkanInfo();
        nasiGoreng.tampilkanInfo();

        System.out.println();
        System.out.println("=== PESANAN BUDI ===");
        int totalKopi = kopi.hitungTotal(2);
        int totalNasi = nasiGoreng.hitungTotal(1);
        System.out.println("2 x " + kopi.nama + " = Rp" + totalKopi); // [7] membaca atribut objek
        System.out.println("1 x " + nasiGoreng.nama + " = Rp" + totalNasi);
        System.out.println("Total bayar: Rp" + (totalKopi + totalNasi));

        System.out.println();
        System.out.println("=== HARGA ES TEH NAIK ===");
        esTeh.harga = 10000; // [8] mengubah atribut satu objek
        esTeh.tampilkanInfo();
        kopi.tampilkanInfo(); // objek lain tidak ikut berubah
    }
}

/** Cetak biru untuk setiap menu di KedaiKita. */
class Menu {
    String nama; // [2] atribut (field) milik objek
    int harga;

    Menu(String nama, int harga) { // [1] konstruktor: dipanggil saat objek dibuat
        this.nama = nama;
        this.harga = harga;
    }

    void tampilkanInfo() { // [3] method: perilaku objek
        System.out.println(nama + " - Rp" + harga);
    }

    int hitungTotal(int jumlah) { // [4] method yang mengembalikan nilai
        return harga * jumlah;
    }
}
