/*
 * Contoh 07 - Menyimpan Banyak Objek dalam Array
 * Pertemuan 02 - Kelas dan Objek
 *
 * Objek bisa disimpan di array seperti data biasa. Dengan perulangan for,
 * kita bisa memanggil method yang sama untuk setiap objek.
 * (Wadah yang ukurannya bisa bertambah, ArrayList, dibahas di Pertemuan 05.)
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07DaftarObjek.java
 */
public class Contoh07DaftarObjek {

    public static void main(String[] args) {
        Lagu[] playlist = { // [1] array berisi tiga objek Lagu
            new Lagu("Indonesia Pusaka", "Ismail Marzuki", 215),
            new Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132),
            new Lagu("Bengawan Solo", "Gesang", 187)
        };

        System.out.println("=== PLAYLIST BELAJAR ===");
        int total = 0;
        for (Lagu lagu : playlist) { // [2] variabel lagu bergantian menunjuk tiap objek
            lagu.tampilkan();
            total = total + lagu.durasiDetik;
        }
        System.out.println("Jumlah lagu : " + playlist.length);
        System.out.println("Total durasi: " + (total / 60) + " menit " + (total % 60) + " detik");
    }
}

/** Satu lagu di playlist. */
class Lagu {
    String judul;
    String penyanyi;
    int durasiDetik;

    Lagu(String judul, String penyanyi, int durasiDetik) {
        this.judul = judul;
        this.penyanyi = penyanyi;
        this.durasiDetik = durasiDetik;
    }

    String durasiTeks() {
        int menit = durasiDetik / 60;
        int detik = durasiDetik % 60;
        return menit + ":" + String.format("%02d", detik);
    }

    void tampilkan() {
        System.out.println("- " + judul + " (" + penyanyi + ") " + durasiTeks());
    }
}
