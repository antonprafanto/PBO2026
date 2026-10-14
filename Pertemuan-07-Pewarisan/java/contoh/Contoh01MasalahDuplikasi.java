/*
 * Contoh 01 - Masalah: Kode Kembar di Dua Kelas
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Kelas MotorLama dan MobilLama ditulis TERPISAH, tanpa pewarisan. Perhatikan
 * betapa banyak bagian yang sama persis: field merek, platNomor, tahun, serta
 * method getMerek(), info(), dan umur(). Di contoh 02, kita merapikannya
 * dengan pewarisan.
 *
 * Catatan nama kelas: diberi akhiran "Lama" (versi lama, sebelum pewarisan)
 * karena nama Motor dan Mobil dipakai di contoh 02. Nama kelas Java harus unik
 * di dalam satu folder java/, agar editor seperti VS Code tidak protes
 * "The type Motor is already defined".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01MasalahDuplikasi.java
 */
public class Contoh01MasalahDuplikasi {

    public static void main(String[] args) {
        MotorLama beat = new MotorLama("Honda Beat", "KT 1234 AB", 2020, "matic");
        MobilLama avanza = new MobilLama("Toyota Avanza", "KT 5678 CD", 2018, 7);

        System.out.println("=== DAFTAR KENDARAAN ===");
        System.out.println(beat.deskripsi());
        System.out.println(avanza.deskripsi());

        System.out.println();
        System.out.println("=== UMUR DI TAHUN 2026 ===");
        System.out.println(beat.getMerek() + ": " + beat.umur(2026) + " tahun");
        System.out.println(avanza.getMerek() + ": " + avanza.umur(2026) + " tahun");
    }
}

/** Sepeda motor, ditulis tanpa pewarisan. */
class MotorLama {
    private String merek; // [1] tiga field ini kembar dengan milik MobilLama
    private String platNomor;
    private int tahun;
    private String transmisi; // [2] khusus motor: "matic" atau "manual"

    public MotorLama(String merek, String platNomor, int tahun, String transmisi) {
        this.merek = merek;
        this.platNomor = platNomor;
        this.tahun = tahun;
        this.transmisi = transmisi;
    }

    public String getMerek() {
        return merek;
    }

    public String info() { // [3] method kembar
        return merek + " (" + platNomor + ") tahun " + tahun;
    }

    public int umur(int tahunSekarang) { // [3] method kembar
        return tahunSekarang - tahun;
    }

    public String deskripsi() {
        return "Motor: " + info() + ", transmisi " + transmisi;
    }
}

/** Mobil, ditulis tanpa pewarisan. Bandingkan baris demi baris dengan MotorLama! */
class MobilLama {
    private String merek;
    private String platNomor;
    private int tahun;
    private int jumlahKursi; // khusus mobil

    public MobilLama(String merek, String platNomor, int tahun, int jumlahKursi) {
        this.merek = merek;
        this.platNomor = platNomor;
        this.tahun = tahun;
        this.jumlahKursi = jumlahKursi;
    }

    public String getMerek() {
        return merek;
    }

    public String info() {
        return merek + " (" + platNomor + ") tahun " + tahun;
    }

    public int umur(int tahunSekarang) {
        return tahunSekarang - tahun;
    }

    public String deskripsi() {
        return "Mobil: " + info() + ", " + jumlahKursi + " kursi";
    }
}
