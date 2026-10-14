/*
 * Solusi Latihan 04 - Kelas NilaiKuliah
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * - nilaiAkhir() = 30% tugas + 30% UTS + 40% UAS.
 *   Supaya hasilnya bilangan bulat, kalikan dulu baru bagi:
 *   (30 * tugas + 30 * uts + 40 * uas) / 100   (pembagian int membuang desimal)
 * - huruf() memakai nilaiAkhir() (method memanggil method lain milik objek yang sama).
 * - lulus(batas) mengembalikan boolean.
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan04NilaiKuliah.java
 */
public class Latihan04NilaiKuliah {

    public static void main(String[] args) {
        NilaiKuliah[] daftar = {
            new NilaiKuliah("Pemrograman Berorientasi Objek", 85, 78, 90),
            new NilaiKuliah("Basis Data", 70, 65, 72),
            new NilaiKuliah("Matematika Diskrit", 60, 55, 48)
        };
        System.out.println("=== KARTU HASIL STUDI (SEDERHANA) ===");
        for (NilaiKuliah mk : daftar) {
            String keterangan;
            if (mk.lulus(60)) {
                keterangan = "lulus";
            } else {
                keterangan = "belum lulus";
            }
            System.out.println(mk.namaMk + ": " + mk.nilaiAkhir() + " (" + mk.huruf() + ") - "
                    + keterangan);
        }
    }
}

/** Nilai satu mata kuliah. */
class NilaiKuliah {
    String namaMk;
    int tugas;
    int uts;
    int uas;

    NilaiKuliah(String namaMk, int tugas, int uts, int uas) {
        this.namaMk = namaMk;
        this.tugas = tugas;
        this.uts = uts;
        this.uas = uas;
    }

    int nilaiAkhir() {
        return (30 * tugas + 30 * uts + 40 * uas) / 100;
    }

    String huruf() {
        int nilai = nilaiAkhir();
        if (nilai >= 80) {
            return "A";
        } else if (nilai >= 70) {
            return "B";
        } else if (nilai >= 60) {
            return "C";
        } else if (nilai >= 50) {
            return "D";
        } else {
            return "E";
        }
    }

    boolean lulus(int batas) {
        return nilaiAkhir() >= batas;
    }
}
