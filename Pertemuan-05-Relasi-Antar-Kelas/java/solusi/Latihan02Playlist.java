/*
 * Solusi Latihan 02 - Playlist dan Lagu (Agregasi)
 * Pertemuan 05 - Relasi Antar Kelas
 *
 * Ide penyelesaian:
 * - Lagu dibuat di LUAR playlist, lalu dimasukkan dengan tambah(lagu).
 *   Karena itu, satu lagu yang sama boleh masuk ke dua playlist (agregasi).
 * - getDaftarLagu() mengembalikan SALINAN list, sehingga list asli di
 *   dalam playlist tidak bisa dikosongkan dari luar.
 * - Durasi disimpan dalam detik (int), lalu diubah menjadi teks m:ss.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02Playlist.java
 */
import java.util.ArrayList;
import java.util.List;

public class Latihan02Playlist {

    public static void main(String[] args) {
        Lagu pusaka = new Lagu("Indonesia Pusaka", "Ismail Marzuki", 215);
        Lagu ampar = new Lagu("Ampar-Ampar Pisang", "Lagu Daerah Kalimantan Selatan", 132);
        Lagu bengawan = new Lagu("Bengawan Solo", "Gesang", 187);

        Playlist belajar = new Playlist("Teman Belajar");
        Playlist mudik = new Playlist("Perjalanan Mudik");
        belajar.tambah(pusaka);
        belajar.tambah(bengawan);
        mudik.tambah(ampar);
        mudik.tambah(bengawan); // lagu yang sama ada di dua playlist

        System.out.println("=== DAFTAR PLAYLIST ===");
        belajar.tampilkan();
        mudik.tampilkan();

        System.out.println();
        System.out.println("=== MENGOSONGKAN SALINAN DARI LUAR ===");
        List<Lagu> salinan = belajar.getDaftarLagu();
        salinan.clear();
        System.out.println("Salinan di luar kini berisi " + salinan.size() + " lagu");
        belajar.tampilkan();
    }

    /** Mengubah 215 menjadi "3:35". */
    static String formatDurasi(int detik) {
        return String.format("%d:%02d", detik / 60, detik % 60);
    }
}

/** Sebuah lagu. Lagu bisa ada tanpa playlist mana pun. */
class Lagu {
    private String judul;
    private String penyanyi;
    private int durasiDetik;

    public Lagu(String judul, String penyanyi, int durasiDetik) {
        this.judul = judul;
        this.penyanyi = penyanyi;
        this.durasiDetik = durasiDetik;
    }

    public int getDurasiDetik() {
        return durasiDetik;
    }

    @Override
    public String toString() {
        String durasi = Latihan02Playlist.formatDurasi(durasiDetik);
        return judul + " - " + penyanyi + " (" + durasi + ")";
    }
}

/** Playlist yang mengumpulkan lagu-lagu yang sudah ada. */
class Playlist {
    private String nama;
    private List<Lagu> daftarLagu;

    public Playlist(String nama) {
        this.nama = nama;
        this.daftarLagu = new ArrayList<>();
    }

    public void tambah(Lagu lagu) {
        daftarLagu.add(lagu);
    }

    public List<Lagu> getDaftarLagu() {
        return new ArrayList<>(daftarLagu); // salinan, bukan list asli
    }

    public int totalDurasi() {
        int total = 0;
        for (Lagu lagu : daftarLagu) {
            total += lagu.getDurasiDetik();
        }
        return total;
    }

    public void tampilkan() {
        int jumlah = daftarLagu.size();
        String total = Latihan02Playlist.formatDurasi(totalDurasi());
        System.out.println(nama + " (" + jumlah + " lagu, total " + total + "):");
        for (int i = 0; i < daftarLagu.size(); i++) {
            System.out.println("  " + (i + 1) + ". " + daftarLagu.get(i));
        }
    }
}
