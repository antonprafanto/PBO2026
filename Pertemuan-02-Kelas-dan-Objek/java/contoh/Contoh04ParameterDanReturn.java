/*
 * Contoh 04 - Method dengan Parameter dan Nilai Kembalian
 * Pertemuan 02 - Kelas dan Objek
 *
 * - Method boleh menerima parameter.
 * - Method boleh MENGEMBALIKAN nilai dengan return. Tipe nilai kembaliannya
 *   wajib ditulis di depan nama method (int, String, ...). Method yang tidak
 *   mengembalikan apa-apa memakai kata kunci void.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04ParameterDanReturn.java
 */
public class Contoh04ParameterDanReturn {

    public static void main(String[] args) {
        PersegiPanjang meja = new PersegiPanjang(120, 60);
        int luas = meja.hitungLuas(); // [3] hasil return disimpan ke variabel
        System.out.println("=== MEJA BELAJAR ===");
        System.out.println("Ukuran   : " + meja.panjang + " x " + meja.lebar + " cm");
        System.out.println("Luas     : " + luas + " cm2");
        System.out.println("Keliling : " + meja.hitungKeliling() + " cm"); // [4] langsung dipakai

        System.out.println();
        meja.perbesar(2); // [5] mengirim argumen ke parameter faktor
        System.out.println("=== SETELAH DIPERBESAR 2 KALI ===");
        System.out.println("Ukuran   : " + meja.panjang + " x " + meja.lebar + " cm");
        System.out.println("Luas     : " + meja.hitungLuas() + " cm2");
        System.out.println("Luas naik " + (meja.hitungLuas() / luas) + " kali lipat");
    }
}

/** Bangun datar persegi panjang dengan panjang dan lebar (cm). */
class PersegiPanjang {
    int panjang;
    int lebar;

    PersegiPanjang(int panjang, int lebar) {
        this.panjang = panjang;
        this.lebar = lebar;
    }

    int hitungLuas() { // [1] tipe kembalian int
        return panjang * lebar;
    }

    int hitungKeliling() {
        return 2 * (panjang + lebar);
    }

    void perbesar(int faktor) { // [2] menerima parameter dan mengubah atribut
        panjang = panjang * faktor;
        lebar = lebar * faktor;
    }
}
