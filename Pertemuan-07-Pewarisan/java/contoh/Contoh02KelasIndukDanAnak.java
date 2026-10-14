/*
 * Contoh 02 - Kelas Induk dan Kelas Anak
 * Pertemuan 07 - Pewarisan (Inheritance)
 *
 * Kode kembar dari contoh 01 kini dikumpulkan di SATU kelas induk, Kendaraan.
 * Motor dan Mobil menjadi kelas anak (kata kunci extends): mereka mewarisi
 * semua milik Kendaraan, lalu hanya menulis bagian yang khusus milik mereka.
 * Output program ini SAMA PERSIS dengan contoh 01.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02KelasIndukDanAnak.java
 */
public class Contoh02KelasIndukDanAnak {

    public static void main(String[] args) {
        Motor beat = new Motor("Honda Beat", "KT 1234 AB", 2020, "matic");
        Mobil avanza = new Mobil("Toyota Avanza", "KT 5678 CD", 2018, 7);

        System.out.println("=== DAFTAR KENDARAAN ===");
        System.out.println(beat.deskripsi());
        System.out.println(avanza.deskripsi());

        System.out.println();
        System.out.println("=== UMUR DI TAHUN 2026 ===");
        // [6] getMerek() dan umur() tidak ditulis di Motor/Mobil: keduanya warisan
        System.out.println(beat.getMerek() + ": " + beat.umur(2026) + " tahun");
        System.out.println(avanza.getMerek() + ": " + avanza.umur(2026) + " tahun");
    }
}

/** Kelas induk untuk semua kendaraan bermotor. */
class Kendaraan { // [1] kelas induk: semua bagian yang SAMA dikumpulkan di sini
    private String merek;
    private String platNomor;
    private int tahun;

    public Kendaraan(String merek, String platNomor, int tahun) {
        this.merek = merek;
        this.platNomor = platNomor;
        this.tahun = tahun;
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
}

/** Sepeda motor: semua milik Kendaraan, ditambah jenis transmisi. */
class Motor extends Kendaraan { // [2] Motor adalah Kendaraan
    private String transmisi; // [4] field tambahan khusus motor

    public Motor(String merek, String platNomor, int tahun, String transmisi) {
        super(merek, platNomor, tahun); // [3] bagian induk diisi induk, PALING AWAL
        this.transmisi = transmisi;
    }

    public String deskripsi() { // [5] method tambahan, memakai method warisan
        return "Motor: " + info() + ", transmisi " + transmisi;
    }
}

/** Mobil: semua milik Kendaraan, ditambah jumlah kursi. */
class Mobil extends Kendaraan {
    private int jumlahKursi;

    public Mobil(String merek, String platNomor, int tahun, int jumlahKursi) {
        super(merek, platNomor, tahun);
        this.jumlahKursi = jumlahKursi;
    }

    public String deskripsi() {
        return "Mobil: " + info() + ", " + jumlahKursi + " kursi";
    }
}
