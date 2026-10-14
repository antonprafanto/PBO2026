/*
 * Contoh 06 - Referensi dan Aliasing
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Variabel bertipe kelas TIDAK menyimpan objek, melainkan REFERENSI
 * (penunjuk) ke objek.
 * - b = a   -> b menunjuk objek yang SAMA dengan a (aliasing), tidak ada salinan
 * - a == b  -> true jika a dan b menunjuk objek yang sama
 * - null    -> nilai khusus untuk variabel yang tidak menunjuk objek apa pun
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06Referensi.java
 */
public class Contoh06Referensi {

    public static void main(String[] args) {
        System.out.println("=== DUA VARIABEL, SATU OBJEK ===");
        Ponsel ponselBudi = new Ponsel("Budi", 80);
        Ponsel ponselDipinjam = ponselBudi; // [1] TIDAK membuat ponsel baru
        ponselDipinjam.pakai(30);           // [2] Siti memakai ponsel yang ia pinjam
        System.out.println("Baterai dilihat lewat variabel peminjam: "
                + ponselDipinjam.baterai + "%");
        System.out.println("Baterai dilihat lewat variabel pemilik : "
                + ponselBudi.baterai + "%"); // [3] ikut berubah!
        if (ponselBudi == ponselDipinjam) { // [4] == pada objek: apakah objeknya sama?
            System.out.println("Keduanya menunjuk objek yang SAMA");
        } else {
            System.out.println("Keduanya menunjuk objek yang berbeda");
        }

        System.out.println();
        System.out.println("=== DUA OBJEK DENGAN DATA KEMBAR ===");
        Ponsel ponselA = new Ponsel("Rina", 50);
        Ponsel ponselB = new Ponsel("Rina", 50); // [5] objek baru, walaupun datanya kembar
        if (ponselA == ponselB) {
            System.out.println("Ponsel A dan ponsel B menunjuk objek yang SAMA");
        } else {
            System.out.println("Ponsel A dan ponsel B menunjuk objek yang berbeda");
        }
        ponselA.pakai(10);
        System.out.println("Baterai ponsel A: " + ponselA.baterai + "%, ponsel B: "
                + ponselB.baterai + "%");

        System.out.println();
        System.out.println("=== VARIABEL TANPA OBJEK ===");
        Ponsel ponselDimas = null; // [6] Dimas belum punya ponsel
        if (ponselDimas == null) { // [7] cara memeriksa null
            System.out.println("Dimas belum punya ponsel");
        }
        ponselDipinjam = null; // [8] Siti mengembalikan ponsel: "label"-nya dilepas
        System.out.println("Ponsel Budi tetap ada, baterainya " + ponselBudi.baterai + "%");
    }
}

/** Ponsel dengan persentase baterai. */
class Ponsel {
    String pemilik;
    int baterai;

    Ponsel(String pemilik, int baterai) {
        this.pemilik = pemilik;
        this.baterai = baterai;
    }

    void pakai(int persen) {
        baterai = baterai - persen;
    }
}
