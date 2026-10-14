/*
 * Contoh 02 - Konstruktor: Mengisi Data Saat Objek Dibuat
 * Pertemuan 02 - Kelas dan Objek
 *
 * Konstruktor adalah "method" khusus yang namanya SAMA dengan nama kelas dan
 * tidak punya tipe kembalian. Ia dipanggil OTOMATIS setiap kali objek dibuat
 * dengan new, sehingga setiap objek langsung lahir dengan data lengkap.
 *
 * Cara menjalankan dari folder java/contoh (Java 11 ke atas):
 *     java Contoh02Konstruktor.java
 */
public class Contoh02Konstruktor {

    public static void main(String[] args) {
        System.out.println("=== MEMBUAT TIGA OBJEK MOBIL ===");
        Mobil mobilBudi = new Mobil("Avanza", "hitam", 2019); // [4] argumen dikirim ke konstruktor
        Mobil mobilSiti = new Mobil("Brio", "merah", 2022);
        Mobil mobilRina = new Mobil("Xpander", "putih", 2021);

        System.out.println();
        System.out.println("=== DATA SETIAP MOBIL ===");
        System.out.println("Mobil Budi: " + mobilBudi.merek + " " + mobilBudi.warna
                + " (" + mobilBudi.tahun + ")");
        System.out.println("Mobil Siti: " + mobilSiti.merek + " " + mobilSiti.warna
                + " (" + mobilSiti.tahun + ")");
        System.out.println("Mobil Rina: " + mobilRina.merek + " " + mobilRina.warna
                + " (" + mobilRina.tahun + ")");
    }
}

/** Cetak biru mobil: setiap mobil punya merek, warna, dan tahun. */
class Mobil {
    String merek;
    String warna;
    int tahun;

    Mobil(String merek, String warna, int tahun) { // [1] konstruktor
        System.out.println("  (konstruktor dipanggil untuk mobil " + merek + ")"); // [2]
        this.merek = merek; // [3] simpan parameter ke atribut objek
        this.warna = warna;
        this.tahun = tahun;
    }
}
