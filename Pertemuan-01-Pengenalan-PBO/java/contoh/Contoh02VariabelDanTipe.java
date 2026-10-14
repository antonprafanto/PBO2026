/*
 * Contoh 02 - Variabel dan Tipe Data
 * Pertemuan 01 - Pengenalan PBO
 *
 * - Variabel adalah "kotak bernama" untuk menyimpan sebuah nilai.
 * - Di Java, setiap variabel WAJIB dideklarasikan beserta tipenya:
 *   String (teks), char (satu karakter), int (bilangan bulat),
 *   double (bilangan pecahan).
 * - Operator + menggabungkan teks dengan nilai lain.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02VariabelDanTipe.java
 */
public class Contoh02VariabelDanTipe {

    public static void main(String[] args) {
        // [1] format deklarasi: Tipe namaVariabel = nilai;
        String nama = "Ayu Lestari"; // String: teks, diapit tanda kutip GANDA
        char inisial = 'A';          // char: tepat satu karakter, diapit kutip TUNGGAL
        int semester = 3;            // int: bilangan bulat
        double ipk = 3.75;           // double: bilangan pecahan, memakai TITIK desimal

        System.out.println("=== DATA MAHASISWA ===");
        System.out.println("Nama     : " + nama); // [2] + menggabungkan teks dengan nilai
        System.out.println("Inisial  : " + inisial);
        System.out.println("Semester : " + semester);
        System.out.println("IPK      : " + ipk);

        System.out.println();
        System.out.println("=== HITUNG UANG JAJAN ===");
        int uangSaku = 50000;
        int hargaKopi = 18000;
        int jumlahCup = uangSaku / hargaKopi; // [3] int / int = pembagian bulat (sisa dibuang)
        int sisaUang = uangSaku % hargaKopi;  // [4] % sisa hasil bagi
        System.out.println("Uang saku     : Rp" + uangSaku);
        System.out.println("Harga kopi    : Rp" + hargaKopi);
        System.out.println("Bisa beli     : " + jumlahCup + " cup");
        System.out.println("Total belanja : Rp" + (jumlahCup * hargaKopi)); // [5] hitung dulu
        System.out.println("Sisa uang     : Rp" + sisaUang);

        System.out.println();
        System.out.println("=== MENGUBAH NILAI VARIABEL ===");
        semester = semester + 1; // [6] mengubah nilai: tipe TIDAK ditulis lagi
        System.out.println("Semester depan " + nama + " masuk semester " + semester);
    }
}
