/*
 * Solusi Latihan 05 - KedaiKita: Laporan Stok (versi prosedural)
 * Pertemuan 01 - Pengenalan PBO
 *
 * Ide penyelesaian:
 * - Data menu tetap disimpan di tiga array paralel (static), seperti studi kasus.
 * - cariIndeksTermurah() mengembalikan INDEKS menu termurah (bukan namanya),
 *   sehingga pemanggil bisa membaca nama dan harga dari array yang berbeda.
 * - hitungNilaiStok() menjumlahkan harga x stok untuk setiap menu.
 * - tampilkanStokMenipis(batas) mencetak menu yang stoknya di bawah batas.
 *   Variabel ada (boolean) mencatat apakah minimal satu menu sudah tercetak.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05LaporanStok.java
 */
public class Latihan05LaporanStok {

    // Data menu: tiga array paralel. Indeks yang sama = menu yang sama.
    static String[] namaMenu = {
        "Kopi Susu Gula Aren",
        "Es Teh Manis",
        "Nasi Goreng Kampung",
        "Mie Goreng Jawa",
        "Pisang Goreng Keju"
    };
    static int[] hargaMenu = {18000, 8000, 25000, 23000, 15000};
    static int[] stokMenu = {20, 30, 15, 4, 3};

    static void tampilkanMenu() {
        System.out.println("=== DAFTAR MENU KEDAIKITA ===");
        for (int i = 0; i < namaMenu.length; i++) {
            System.out.println((i + 1) + ". " + namaMenu[i] + " - Rp" + hargaMenu[i]
                    + " (stok " + stokMenu[i] + ")");
        }
    }

    static int cariIndeksTermurah() {
        int indeksTermurah = 0;
        for (int i = 0; i < hargaMenu.length; i++) {
            if (hargaMenu[i] < hargaMenu[indeksTermurah]) {
                indeksTermurah = i;
            }
        }
        return indeksTermurah;
    }

    static int hitungNilaiStok() {
        int total = 0;
        for (int i = 0; i < hargaMenu.length; i++) {
            total = total + hargaMenu[i] * stokMenu[i];
        }
        return total;
    }

    static void tampilkanStokMenipis(int batas) {
        System.out.println("Stok menipis (kurang dari " + batas + "):");
        boolean ada = false;
        for (int i = 0; i < namaMenu.length; i++) {
            if (stokMenu[i] < batas) {
                System.out.println("- " + namaMenu[i] + " (sisa " + stokMenu[i] + ")");
                ada = true;
            }
        }
        if (!ada) {
            System.out.println("- (tidak ada)");
        }
    }

    public static void main(String[] args) {
        tampilkanMenu();
        System.out.println();

        System.out.println("=== LAPORAN STOK ===");
        int termurah = cariIndeksTermurah();
        System.out.println("Menu termurah : " + namaMenu[termurah] + " (Rp" + hargaMenu[termurah]
                + ")");
        System.out.println("Nilai stok    : Rp" + hitungNilaiStok());
        tampilkanStokMenipis(5);
        tampilkanStokMenipis(3);
    }
}
