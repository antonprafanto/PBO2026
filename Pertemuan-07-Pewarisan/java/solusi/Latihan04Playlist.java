/*
 * Solusi Latihan 04 - Playlist Bukan Lagu (is-a vs has-a)
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Ide penyelesaian:
 * - Rancangan lama "class Playlist extends Lagu" keliru: playlist BUKAN sebuah
 *   lagu. Uji kalimatnya: "Playlist adalah Lagu" terdengar janggal, sedangkan
 *   "Playlist punya banyak Lagu" terdengar wajar -> hubungannya has-a.
 * - Karena itu Playlist TIDAK mewarisi Lagu. Playlist menyimpan List berisi
 *   objek Lagu sebagai field (agregasi, seperti di Pertemuan 05).
 * - Method tambah() memasukkan lagu, totalDurasi() menjumlahkan durasi semua
 *   lagu, tampilkan() mencetak isinya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04Playlist.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan04Playlist {

    public static void main(String[] args) {
        Playlist playlist = new Playlist("Lagu Daerah Kalimantan");
        playlist.tambah(new Lagu("Ampar-Ampar Pisang", 132));
        playlist.tambah(new Lagu("Paris Barantai", 185));
        playlist.tambah(new Lagu("Indung-Indung", 170));
        playlist.tampilkan();
    }
}

/** Satu lagu dengan durasi dalam detik. */
class Lagu {
    private String judul;
    private int durasiDetik;

    public Lagu(String judul, int durasiDetik) {
        this.judul = judul;
        this.durasiDetik = durasiDetik;
    }

    public int getDurasiDetik() {
        return durasiDetik;
    }

    @Override
    public String toString() {
        int menit = durasiDetik / 60;
        int detik = durasiDetik % 60;
        return judul + " (" + menit + ":" + String.format("%02d", detik) + ")";
    }
}

/** Playlist PUNYA banyak lagu (has-a), bukan sebuah lagu (is-a). */
class Playlist { // TIDAK extends Lagu
    private String nama;
    private List<Lagu> daftarLagu; // has-a: list berisi objek Lagu

    public Playlist(String nama) {
        this.nama = nama;
        this.daftarLagu = new ArrayList<>();
    }

    public void tambah(Lagu lagu) {
        daftarLagu.add(lagu);
    }

    public int totalDurasi() {
        int total = 0;
        for (Lagu lagu : daftarLagu) {
            total += lagu.getDurasiDetik();
        }
        return total;
    }

    public void tampilkan() {
        System.out.println("=== PLAYLIST: " + nama + " ===");
        for (int i = 0; i < daftarLagu.size(); i++) {
            System.out.println((i + 1) + ". " + daftarLagu.get(i));
        }
        int total = totalDurasi();
        System.out.println("Jumlah lagu : " + daftarLagu.size());
        System.out.println("Total durasi: " + (total / 60) + " menit " + (total % 60) + " detik");
    }
}
