/*
 * KedaiKita - versi BERORIENTASI OBJEK (sekilas)
 * Pertemuan 01 - Pengenalan PBO
 *
 * Masalah yang sama seperti KedaiKitaProsedural.java, tetapi kali ini setiap menu
 * adalah SATU OBJEK yang membawa nama, harga, dan stoknya sendiri.
 * Jangan khawatir bila ada sintaks yang belum kamu pahami (class, new, konstruktor,
 * this, ArrayList, lambda). Semuanya akan kita bahas pelan-pelan mulai Pertemuan 02.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java KedaiKitaOop.java
 *
 * Catatan: kelas yang memiliki main (KedaiKitaOop) sengaja ditulis PALING ATAS,
 * karena itu syarat menjalankan file dengan perintah "java NamaFile.java".
 */
import java.util.ArrayList;

public class KedaiKitaOop {

    static void tampilkanMenu(ArrayList<Menu> daftarMenu) {
        System.out.println("=== DAFTAR MENU KEDAIKITA ===");
        int nomor = 1;
        for (Menu menu : daftarMenu) {
            System.out.println(nomor + ". " + menu.nama + " - Rp" + menu.harga
                    + " (stok " + menu.stok + ")");
            nomor = nomor + 1;
        }
    }

    public static void main(String[] args) {
        Menu kopi = new Menu("Kopi Susu Gula Aren", 18000, 20);
        Menu nasiGoreng = new Menu("Nasi Goreng Kampung", 25000, 15);
        Menu esTeh = new Menu("Es Teh Manis", 8000, 30);
        // ArrayList = daftar yang isinya bisa bertambah (dibahas di Pertemuan 05).
        // ArrayList<Menu> dibaca "daftar berisi objek Menu".
        ArrayList<Menu> daftarMenu = new ArrayList<>();
        daftarMenu.add(kopi);
        daftarMenu.add(nasiGoreng);
        daftarMenu.add(esTeh);

        tampilkanMenu(daftarMenu);
        System.out.println();

        // Budi memesan 2 Kopi Susu Gula Aren dan 1 Es Teh Manis
        int total = kopi.harga * 2 + esTeh.harga * 1;
        kopi.kurangiStok(2);
        esTeh.kurangiStok(1);
        System.out.println("Pesanan Budi: 2 x Kopi Susu Gula Aren, 1 x Es Teh Manis");
        System.out.println("Total bayar : Rp" + total);
        System.out.println();

        // Mengurutkan daftar menu berdasarkan nama.
        // Yang dipindah adalah OBJEK-nya, jadi harga & stok ikut terbawa.
        // Bentuk (a, b) -> ... disebut lambda; sintaksnya dipelajari di Pertemuan 12.
        System.out.println("Mengurutkan menu sesuai abjad...");
        daftarMenu.sort((a, b) -> a.nama.compareTo(b.nama));
        tampilkanMenu(daftarMenu);
        System.out.println();
        System.out.println("Aman! Setiap menu membawa datanya sendiri, "
                + "jadi tidak ada yang tertukar.");
    }
}

/** Cetak biru untuk satu menu: punya nama, harga, dan stok. */
class Menu {
    String nama;
    int harga;
    int stok;

    Menu(String nama, int harga, int stok) {
        this.nama = nama;
        this.harga = harga;
        this.stok = stok;
    }

    void kurangiStok(int jumlah) {
        stok = stok - jumlah;
    }
}
