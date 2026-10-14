/*
 * Solusi Latihan 02 - Nilai Mata Kuliah
 * Pertemuan 04 - Enkapsulasi
 *
 * Ide penyelesaian:
 * - angka punya getter dan setter. Setter menolak angka di luar 0-100.
 * - getHuruf() dan isLulus() adalah getter TANPA setter yang DIHITUNG dari
 *   angka. Hasilnya tidak disimpan di field, sehingga selalu cocok dengan angka.
 *   (Kalau huruf disimpan terpisah, bisa saja angka berubah tetapi huruf lupa
 *   diperbarui. Data jadi tidak konsisten.)
 * - Getter boolean memakai awalan is: isLulus(), bukan getLulus().
 * - Konstruktor mengisi angka lewat setter.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan02NilaiMataKuliah.java
 */
public class Latihan02NilaiMataKuliah {

    public static void main(String[] args) {
        NilaiMataKuliah pbo = new NilaiMataKuliah("Pemrograman Berorientasi Objek", 85);
        NilaiMataKuliah basisData = new NilaiMataKuliah("Basis Data", 58);
        System.out.println("=== NILAI SEMESTER ===");
        System.out.println(pbo);
        System.out.println(basisData);

        System.out.println();
        System.out.println("=== SETELAH PERBAIKAN NILAI ===");
        basisData.setAngka(72);
        System.out.println(basisData);

        System.out.println();
        System.out.println("=== INPUT NILAI SALAH ===");
        try {
            basisData.setAngka(105);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            new NilaiMataKuliah("Statistika", -5);
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println(basisData);
    }
}

/** Nilai angka (0-100) satu mata kuliah. */
class NilaiMataKuliah {
    public static final int BATAS_LULUS = 60;

    private String mataKuliah;
    private int angka;

    public NilaiMataKuliah(String mataKuliah, int angka) {
        this.mataKuliah = mataKuliah;
        setAngka(angka); // lewat setter, jadi ikut diperiksa
    }

    public String getMataKuliah() {
        return mataKuliah;
    }

    public int getAngka() {
        return angka;
    }

    public void setAngka(int angka) {
        if (angka < 0 || angka > 100) {
            throw new IllegalArgumentException("Nilai harus 0-100, bukan " + angka);
        }
        this.angka = angka;
    }

    /** Huruf mutu, dihitung dari angka (read-only). */
    public String getHuruf() {
        if (angka >= 80) {
            return "A";
        } else if (angka >= 70) {
            return "B";
        } else if (angka >= 60) {
            return "C";
        } else if (angka >= 50) {
            return "D";
        } else {
            return "E";
        }
    }

    /** true jika angka mencapai batas lulus (read-only). */
    public boolean isLulus() {
        return angka >= BATAS_LULUS;
    }

    @Override
    public String toString() {
        String keterangan;
        if (isLulus()) {
            keterangan = "lulus";
        } else {
            keterangan = "belum lulus";
        }
        return mataKuliah + ": " + angka + " (" + getHuruf() + ") - " + keterangan;
    }
}
