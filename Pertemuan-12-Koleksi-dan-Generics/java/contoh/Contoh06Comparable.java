/*
 * Contoh 06 - Urutan Alami dengan Comparable
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Jika sebuah kelas mengimplementasikan Comparable<T> dan mengisi compareTo(),
 * objeknya punya URUTAN ALAMI. Collections.sort(), Collections.min(), dan
 * TreeSet langsung bisa dipakai tanpa Comparator.
 * Di sini pelari yang "lebih kecil" artinya "lebih cepat".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06Comparable.java
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Contoh06Comparable {

    public static void main(String[] args) {
        List<Pelari> hasil = List.of(
                new Pelari(105, "Rudi", 1290),
                new Pelari(112, "Maya", 1125),
                new Pelari(101, "Joko", 1198),
                new Pelari(108, "Lina", 1510),
                new Pelari(103, "Fikri", 1198));
        System.out.println("=== CATATAN PANITIA (urutan tiba di meja) ===");
        for (Pelari pelari : hasil) {
            System.out.println(pelari);
        }

        System.out.println();
        System.out.println("=== PERINGKAT (urutan alami: tercepat dulu) ===");
        List<Pelari> peringkat = new ArrayList<>(hasil);
        Collections.sort(peringkat); // [3] tanpa Comparator: memakai compareTo()
        for (int i = 0; i < peringkat.size(); i++) {
            System.out.println((i + 1) + ". " + peringkat.get(i));
        }
        System.out.println("Juara 1: " + Collections.min(hasil).getNama()); // [4]
        Pelari rudi = hasil.get(0);
        Pelari joko = hasil.get(2);
        String jawaban = joko.compareTo(rudi) < 0 ? "ya" : "tidak"; // [5]
        System.out.println("Joko lebih cepat dari Rudi? " + jawaban);

        System.out.println();
        System.out.println("=== DARI YANG TERLAMBAT ===");
        List<Pelari> terlambat = new ArrayList<>(hasil);
        terlambat.sort(Collections.reverseOrder()); // [6] urutan alami dibalik
        for (Pelari pelari : terlambat) {
            System.out.println(pelari);
        }

        System.out.println();
        System.out.println("=== ABSENSI (urutan khusus: nama A-Z) ===");
        List<Pelari> absensi = new ArrayList<>(hasil);
        absensi.sort(Comparator.comparing(Pelari::getNama)); // [7] Comparator mengalahkan urutan alami
        List<String> nama = new ArrayList<>();
        for (Pelari pelari : absensi) {
            nama.add(pelari.getNama());
        }
        System.out.println(String.join(", ", nama));
    }
}

/** Peserta lomba lari 5K. Urutan alaminya: waktu tercepat dulu. */
class Pelari implements Comparable<Pelari> { // [1] "Pelari bisa dibandingkan dengan Pelari"
    private int nomor;
    private String nama;
    private int waktuDetik;

    public Pelari(int nomor, String nama, int waktuDetik) {
        this.nomor = nomor;
        this.nama = nama;
        this.waktuDetik = waktuDetik;
    }

    public String getNama() {
        return nama;
    }

    public String waktuTeks() {
        return (waktuDetik / 60) + ":" + String.format("%02d", waktuDetik % 60);
    }

    @Override
    public String toString() {
        return String.format("#%d %-6s%s", nomor, nama, waktuTeks());
    }

    // [2] negatif: objek ini duluan; positif: objek lain duluan; 0: setara
    @Override
    public int compareTo(Pelari lain) {
        if (waktuDetik != lain.waktuDetik) {
            return Integer.compare(waktuDetik, lain.waktuDetik);
        }
        return Integer.compare(nomor, lain.nomor); // waktu sama: nomor dada kecil dulu
    }
}
