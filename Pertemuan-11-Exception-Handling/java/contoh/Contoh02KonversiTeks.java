/*
 * Contoh 02 - Mengubah Teks Menjadi Angka
 * Pertemuan 11 - Exception Handling
 *
 * Data dari formulir, file, atau jaringan selalu datang sebagai TEKS. Saat
 * teks diubah menjadi angka dengan Integer.parseInt(), teks yang bukan
 * bilangan bulat membuat Java melempar NumberFormatException. Di contoh ini,
 * isian yang salah dilewati dengan pesan yang ramah, dan isian yang benar
 * tetap dijumlahkan.
 *
 * Data sengaja ditulis langsung di program (bukan dari input keyboard),
 * supaya hasilnya selalu sama setiap kali dijalankan.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02KonversiTeks.java
 */
public class Contoh02KonversiTeks {

    public static void main(String[] args) {
        // [1] isian jumlah porsi dari formulir pesanan online (semuanya teks)
        String[] isianFormulir = {"3", "dua", "5", "2.5", "", "4"};
        int total = 0;
        int jumlahSalah = 0;

        System.out.println("=== REKAP JUMLAH PORSI ===");
        for (String teks : isianFormulir) {
            try {
                int porsi = Integer.parseInt(teks); // [2] bisa melempar NumberFormatException
                total += porsi; // [3] hanya dijalankan jika parseInt() berhasil
                System.out.println("'" + teks + "' -> " + porsi + " porsi");
            } catch (NumberFormatException e) { // [4] isian ini dilewati, perulangan lanjut
                jumlahSalah++;
                System.out.println("'" + teks + "' -> bukan bilangan bulat, dilewati");
            }
        }

        System.out.println();
        System.out.println("Total porsi     : " + total);
        System.out.println("Isian yang salah: " + jumlahSalah);
    }
}
