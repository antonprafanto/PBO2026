/*
 * Contoh 04 - Polimorfisme dari Dalam Kelas
 * Pertemuan 09 - Polimorfisme
 *
 * Method tulis() hanya ditulis SEKALI, di kelas induk KartuUcapan. Di dalamnya,
 * tulis() memanggil salam() dan isi() (artinya this.salam() dan this.isi()).
 * Karena this selalu menunjuk objek yang sebenarnya, versi salam() dan isi()
 * yang berjalan adalah milik kelas anak (jika kelas anak meng-override-nya).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04PolimorfismeDariDalamKelas.java
 */
import java.util.List;

public class Contoh04PolimorfismeDariDalamKelas {

    public static void main(String[] args) {
        List<KartuUcapan> daftarKartu = List.of(
                new KartuUcapan("Siti", "Budi"),
                new KartuUlangTahun("Rina", "Ayu", 20),
                new KartuWisuda("Dimas", "Keluarga di Samarinda"));
        for (int i = 0; i < daftarKartu.size(); i++) {
            KartuUcapan kartu = daftarKartu.get(i);
            int nomor = i + 1;
            if (nomor > 1) {
                System.out.println();
            }
            String jenis = kartu.getClass().getSimpleName();
            System.out.println("=== Kartu " + nomor + ": " + jenis + " ===");
            kartu.tulis(); // [6] tulis() milik induk, hasilnya berbeda-beda
        }
    }
}

/** Kartu ucapan umum. Kerangka tulis() sama untuk semua jenis kartu. */
class KartuUcapan {
    private String penerima;
    private String pengirim;

    public KartuUcapan(String penerima, String pengirim) {
        this.penerima = penerima;
        this.pengirim = pengirim;
    }

    public String getPenerima() {
        return penerima;
    }

    public String salam() {
        return "Halo, " + penerima + "!";
    }

    public String isi() {
        return "Semoga harimu menyenangkan.";
    }

    public void tulis() { // [1] method induk yang memanggil method lain milik objek ini
        System.out.println("-".repeat(40));
        System.out.println(salam()); // [2] artinya this.salam(): versi siapa? tergantung objeknya
        System.out.println(isi());
        System.out.println("Salam hangat, " + pengirim);
        System.out.println("-".repeat(40));
    }
}

class KartuUlangTahun extends KartuUcapan {
    private int umur;

    public KartuUlangTahun(String penerima, String pengirim, int umur) {
        super(penerima, pengirim);
        this.umur = umur;
    }

    @Override // [3] hanya isi() yang di-override
    public String isi() {
        return "Selamat ulang tahun yang ke-" + umur + "!";
    }
}

class KartuWisuda extends KartuUcapan {
    public KartuWisuda(String penerima, String pengirim) {
        super(penerima, pengirim);
    }

    @Override // [4] salam() dan isi() sama-sama di-override
    public String salam() {
        return "Selamat, " + getPenerima() + ", S.Kom.!";
    }

    @Override
    public String isi() {
        return "Perjuanganmu terbayar lunas. " + super.isi(); // [5]
    }
}
