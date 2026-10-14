/*
 * Solusi Latihan 01 - Notifikasi Kampus
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - Kelas induk Notifikasi punya dua method: kirim(pesan) dan biaya().
 * - NotifEmail, NotifSMS, dan NotifWhatsApp meng-override kirim() dengan
 *   format masing-masing. Hanya NotifSMS yang meng-override biaya(); kelas
 *   lain memakai versi induk (biaya 0).
 * - Program utama cukup memanggil notif.kirim(pesan) dan notif.biaya() untuk
 *   SEMUA objek di List, tanpa if-else berdasarkan jenis (polimorfisme).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01Notifikasi.java
 */
import java.util.List;

public class Latihan01Notifikasi {

    public static void main(String[] args) {
        List<Notifikasi> daftarNotif = List.of(
                new NotifEmail("ayu@kampus.ac.id"),
                new NotifSMS("081234567890"),
                new NotifWhatsApp("082198765432"));
        List<String> daftarPesan = List.of("Kuliah PBO pindah ke Ruang D-201", "Kuis besok jam 8");

        int totalBiaya = 0;
        for (String pesan : daftarPesan) {
            System.out.println("=== KIRIM: " + pesan + " ===");
            for (Notifikasi notif : daftarNotif) {
                System.out.println(notif.kirim(pesan)); // versi kirim() milik objek sebenarnya
                totalBiaya += notif.biaya();
            }
            System.out.println();
        }
        System.out.println("Total biaya pengiriman: Rp" + totalBiaya);
    }
}

/** Kelas induk semua jenis notifikasi. */
class Notifikasi {
    private String tujuan;

    public Notifikasi(String tujuan) {
        this.tujuan = tujuan;
    }

    public String getTujuan() {
        return tujuan;
    }

    public String kirim(String pesan) {
        return "[UMUM] Kepada " + tujuan + ": " + pesan;
    }

    public int biaya() {
        return 0; // bawaan: gratis
    }
}

class NotifEmail extends Notifikasi {
    public NotifEmail(String tujuan) {
        super(tujuan);
    }

    @Override
    public String kirim(String pesan) {
        return "[EMAIL] Kepada " + getTujuan() + ": " + pesan;
    }
}

class NotifSMS extends Notifikasi {
    private static final int PANJANG_MAKS_SMS = 20;

    public NotifSMS(String tujuan) {
        super(tujuan);
    }

    @Override
    public String kirim(String pesan) {
        String isi = pesan;
        if (isi.length() > PANJANG_MAKS_SMS) {
            isi = isi.substring(0, PANJANG_MAKS_SMS) + "..."; // potong pesan yang panjang
        }
        return "[SMS] Kepada " + getTujuan() + ": " + isi;
    }

    @Override // satu-satunya kelas yang meng-override biaya()
    public int biaya() {
        return 150;
    }
}

class NotifWhatsApp extends Notifikasi {
    public NotifWhatsApp(String tujuan) {
        super(tujuan);
    }

    @Override
    public String kirim(String pesan) {
        return "[WA] Kepada " + getTujuan() + ": *PENGUMUMAN* " + pesan;
    }
}
