/*
 * Solusi Latihan 02 - Jam Digital yang Menolak Waktu Mustahil
 * Pertemuan 11 - Exception Handling
 *
 * Ide penyelesaian:
 * - atur(jam, menit) MEMERIKSA dulu, baru mengubah field. Jika jam atau
 *   menit di luar batas, lempar IllegalArgumentException berisi pesan yang
 *   jelas. Karena pemeriksaan dilakukan sebelum perubahan, waktu lama utuh.
 * - Di main(), tampilan jam dicetak di blok finally sehingga SELALU muncul,
 *   baik pengaturan berhasil maupun ditolak.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02JamDigital.java
 */
public class Latihan02JamDigital {

    public static void main(String[] args) {
        JamDigital jamDinding = new JamDigital();
        System.out.println("=== JAM DIGITAL ===");
        System.out.println("Tampilan awal: " + jamDinding.tampilan());
        // Dua array sejajar: percobaan ke-i memakai daftarJam[i] dan daftarMenit[i].
        int[] daftarJam = {7, 25, 12, 23, -1};
        int[] daftarMenit = {30, 0, 75, 59, 10};
        for (int i = 0; i < daftarJam.length; i++) {
            int jam = daftarJam[i];
            int menit = daftarMenit[i];
            try {
                jamDinding.atur(jam, menit);
                System.out.println("Atur ke jam " + jam + " menit " + menit + " -> berhasil");
            } catch (IllegalArgumentException e) {
                System.out.println("Atur ke jam " + jam + " menit " + menit
                        + " -> ditolak: " + e.getMessage());
            } finally {
                System.out.println("  Tampilan jam: " + jamDinding.tampilan());
            }
        }
    }
}

/** Jam digital 24 jam. Waktu awal 00:00. */
class JamDigital {
    private int jam;
    private int menit;

    public JamDigital() {
        this.jam = 0;
        this.menit = 0;
    }

    public void atur(int jam, int menit) {
        if (jam < 0 || jam > 23) {
            throw new IllegalArgumentException("jam harus 0 sampai 23");
        }
        if (menit < 0 || menit > 59) {
            throw new IllegalArgumentException("menit harus 0 sampai 59");
        }
        this.jam = jam; // hanya sampai di sini jika keduanya valid
        this.menit = menit;
    }

    public String tampilan() {
        return String.format("%02d:%02d", jam, menit);
    }
}
