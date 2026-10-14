/*
 * Contoh 06 - Method sebagai Penjaga Aturan
 * Pertemuan 04 - Enkapsulasi
 *
 * Jumlah motor di parkiran TIDAK diberi setter. Jumlah itu hanya berubah
 * lewat method masuk() dan keluar(), yang menjaga aturan:
 * - jumlah motor yang masuk/keluar harus lebih dari 0,
 * - motor tidak boleh masuk melebihi sisa tempat,
 * - motor yang keluar tidak boleh lebih banyak dari motor yang ada.
 *
 * Prinsip "tell, don't ask": SURUH objek bekerja (parkiran.masuk(3)),
 * jangan TANYA datanya lalu mengubahnya sendiri dari luar kelas.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06MethodPenjagaAturan.java
 */
public class Contoh06MethodPenjagaAturan {

    public static void main(String[] args) {
        Parkiran parkiran = new Parkiran("Parkiran Gedung C", 5);

        System.out.println("=== PAGI: MOTOR BERDATANGAN ===");
        tampilkan(parkiran);
        parkiran.masuk(3); // [6] "tell": suruh parkiran mencatat motor yang masuk
        System.out.println("3 motor masuk");
        parkiran.masuk(2);
        System.out.println("2 motor masuk");
        tampilkan(parkiran);
        try {
            parkiran.masuk(1);
            System.out.println("1 motor masuk");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== SORE: MOTOR PULANG ===");
        parkiran.keluar(4);
        System.out.println("4 motor keluar");
        tampilkan(parkiran);
        try {
            parkiran.keluar(2);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            parkiran.masuk(-2); // [7] trik curang: "masuk" dengan angka negatif
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
    }

    /** Mengubah true/false menjadi teks "ya" atau "tidak". */
    private static String yaTidak(boolean kondisi) {
        if (kondisi) {
            return "ya";
        }
        return "tidak";
    }

    private static void tampilkan(Parkiran parkiran) {
        System.out.println("  " + parkiran.getNama() + ": terisi " + parkiran.getTerisi()
                + "/" + parkiran.getKapasitas() + ", sisa " + parkiran.getSisa()
                + ", penuh: " + yaTidak(parkiran.isPenuh()));
    }
}

/** Parkiran motor dengan kapasitas terbatas. */
class Parkiran {
    private String nama;
    private int kapasitas;
    private int terisi; // [1] tanpa setter: hanya berubah lewat masuk()/keluar()

    public Parkiran(String nama, int kapasitas) {
        if (kapasitas <= 0) {
            throw new IllegalArgumentException("Kapasitas harus lebih dari 0");
        }
        this.nama = nama;
        this.kapasitas = kapasitas;
        this.terisi = 0;
    }

    public String getNama() {
        return nama;
    }

    public int getKapasitas() {
        return kapasitas;
    }

    public int getTerisi() {
        return terisi;
    }

    public int getSisa() { // [2] dihitung saat diminta, tidak disimpan di field
        return kapasitas - terisi;
    }

    public boolean isPenuh() { // [3] getter boolean memakai awalan is, bukan get
        return terisi == kapasitas;
    }

    public void masuk(int jumlah) { // [4] pintu resmi untuk menambah jumlah motor
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah motor harus lebih dari 0");
        }
        if (jumlah > getSisa()) {
            throw new IllegalArgumentException("Tempat tidak cukup untuk " + jumlah
                    + " motor (sisa " + getSisa() + ")");
        }
        terisi += jumlah;
    }

    public void keluar(int jumlah) { // [5] pintu resmi untuk mengurangi jumlah motor
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Jumlah motor harus lebih dari 0");
        }
        if (jumlah > terisi) {
            throw new IllegalArgumentException("Hanya ada " + terisi + " motor di parkiran");
        }
        terisi -= jumlah;
    }
}
