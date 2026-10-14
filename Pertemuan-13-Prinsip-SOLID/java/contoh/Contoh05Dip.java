/*
 * Contoh 05 - DIP: Bergantung pada Abstraksi, Bukan pada Kelas Konkret
 * Pertemuan 13 - Prinsip SOLID
 *
 * Versi MELANGGAR: PengingatKaku membuat sendiri objek SmsGateway di dalam
 * konstruktornya. Ia terkunci ke SMS selamanya.
 *
 * Versi SESUAI DIP: PengingatJadwal hanya mengenal interface Pengirim.
 * Objek pengirim yang konkret "disuntikkan" dari luar lewat konstruktor
 * (dependency injection). Kelas yang sama bisa memakai SMS, WhatsApp, atau
 * pengirim tiruan untuk pengujian, tanpa diubah sedikit pun.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05Dip.java
 */
import java.util.ArrayList;
import java.util.List;

public class Contoh05Dip {

    public static void main(String[] args) {
        System.out.println("=== VERSI MELANGGAR DIP ===");
        new PengingatKaku().ingatkan("081234567890", "PBO", "08.00");
        System.out.println("Mau pindah ke WhatsApp? Kelas PengingatKaku harus dibongkar.");

        System.out.println();
        System.out.println("=== VERSI SESUAI DIP ===");
        System.out.println("Disuntik PengirimSms:");
        new PengingatJadwal(new PengirimSms()).ingatkan("081234567890", "PBO", "08.00"); // [4]
        System.out.println("Disuntik PengirimWhatsApp:");
        new PengingatJadwal(new PengirimWhatsApp()).ingatkan("081234567890", "PBO", "08.00");

        System.out.println("Disuntik PengirimTiruan (untuk pengujian):");
        PengirimTiruan tiruan = new PengirimTiruan();
        PengingatJadwal pengingat = new PengingatJadwal(tiruan);
        pengingat.ingatkan("081234567890", "PBO", "08.00");
        pengingat.ingatkan("082198765432", "Basis Data", "10.00");
        List<String> catatan = tiruan.getCatatan(); // [5] memeriksa hasil tanpa mengirim pesan sungguhan
        System.out.println("  Pesan tercatat: " + catatan.size());
        System.out.println("  Pesan kedua   : " + catatan.get(1));
        boolean sesuai = catatan.get(1).equals("082198765432: Besok kuliah Basis Data jam 10.00");
        System.out.println("  Sesuai harapan? " + (sesuai ? "ya" : "tidak"));
    }
}

// ------------------------------------------------------------ MELANGGAR DIP
class SmsGateway {
    public void kirimSms(String nomor, String pesan) {
        System.out.println("  [SMS ke " + nomor + "] " + pesan);
    }
}

class PengingatKaku {
    private SmsGateway sms;

    public PengingatKaku() {
        this.sms = new SmsGateway(); // [1] membuat sendiri kelas konkret: terkunci
    }

    public void ingatkan(String nomor, String matkul, String jam) {
        sms.kirimSms(nomor, "Besok kuliah " + matkul + " jam " + jam);
    }
}

// -------------------------------------------------------------- SESUAI DIP
/** Abstraksi: apa pun yang bisa mengirim pesan. */
interface Pengirim {
    void kirim(String tujuan, String pesan);
}

class PengirimSms implements Pengirim {
    @Override
    public void kirim(String tujuan, String pesan) {
        System.out.println("  [SMS ke " + tujuan + "] " + pesan);
    }
}

class PengirimWhatsApp implements Pengirim {
    @Override
    public void kirim(String tujuan, String pesan) {
        System.out.println("  [WA ke " + tujuan + "] " + pesan);
    }
}

/** Pengirim pura-pura untuk pengujian: tidak mengirim, hanya mencatat. */
class PengirimTiruan implements Pengirim {
    private List<String> catatan = new ArrayList<>();

    public List<String> getCatatan() {
        return new ArrayList<>(catatan);
    }

    @Override
    public void kirim(String tujuan, String pesan) {
        catatan.add(tujuan + ": " + pesan);
    }
}

class PengingatJadwal {
    private Pengirim pengirim; // [3] tipenya abstraksi, bukan kelas konkret

    public PengingatJadwal(Pengirim pengirim) { // [2] disuntikkan dari luar
        this.pengirim = pengirim;
    }

    public void ingatkan(String nomor, String matkul, String jam) {
        pengirim.kirim(nomor, "Besok kuliah " + matkul + " jam " + jam);
    }
}
