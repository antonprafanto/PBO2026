/*
 * Contoh 01 - Kelas dan Objek Pertamamu
 * Pertemuan 02 - Kelas dan Objek
 *
 * - Kelas Kucing adalah cetak biru (blueprint).
 * - oyen dan belang adalah dua objek (hasil cetakan) dari kelas Kucing.
 * - Atribut (field) diisi dari luar dengan notasi titik: objek.atribut = nilai
 *
 * Catatan: mengisi atribut dari luar seperti ini bisa dilakukan, tetapi bukan
 * kebiasaan yang baik. Di contoh 02 kita memakai konstruktor.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01KelasDanObjek.java
 */
public class Contoh01KelasDanObjek {

    public static void main(String[] args) {
        Kucing oyen = new Kucing(); // [2] membuat objek pertama dari kelas Kucing
        oyen.nama = "Oyen";         // [3] mengisi atribut milik objek oyen
        oyen.warna = "oranye";

        Kucing belang = new Kucing(); // objek kedua dari kelas yang SAMA
        belang.nama = "Belang";
        belang.warna = "hitam putih";

        System.out.println("=== DUA OBJEK DARI SATU KELAS ===");
        System.out.println("Kucing pertama: " + oyen.nama + ", warnanya " + oyen.warna); // [4]
        System.out.println("Kucing kedua  : " + belang.nama + ", warnanya " + belang.warna);
        System.out.println("oyen dibuat dari kelas  : " + oyen.getClass().getSimpleName()); // [5]
        System.out.println("belang dibuat dari kelas: " + belang.getClass().getSimpleName());
        if (oyen == belang) { // [6] apakah keduanya objek yang sama?
            System.out.println("oyen dan belang adalah objek yang sama");
        } else {
            System.out.println("oyen dan belang adalah dua objek yang berbeda");
        }
    }
}

/** Cetak biru untuk semua kucing. */
class Kucing { // [1] mendefinisikan kelas bernama Kucing
    String nama;  // atribut (field) dideklarasikan lengkap dengan tipenya
    String warna;
}
