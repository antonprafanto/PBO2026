/*
 * Solusi Latihan 04 - Ranking Nilai Mahasiswa
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Urutan ALAMI mahasiswa = urut NIM, ditulis di compareTo()
 *   (kelas meng-implements Comparable<NilaiMahasiswa>).
 * - Ranking memakai Comparator tiga kriteria:
 *     Comparator.comparing(NilaiMahasiswa::getNilaiAkhir).reversed()      -> akhir terbesar
 *         .thenComparing(NilaiMahasiswa::getNilaiUas, Comparator.reverseOrder()) -> UAS terbesar
 *         .thenComparing(NilaiMahasiswa::getNama)                         -> nama A-Z
 *   Hati-hati: .reversed() di AKHIR rantai akan membalik SEMUA kriteria,
 *   termasuk nama. Karena itu kriteria kedua dibalik sendiri dengan
 *   Comparator.reverseOrder().
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04RankingNilai.java
 */
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class Latihan04RankingNilai {

    public static void main(String[] args) {
        List<NilaiMahasiswa> kelas = List.of(
                new NilaiMahasiswa("2409106003", "Citra Dewi", 88, 90),
                new NilaiMahasiswa("2409106001", "Ayu Lestari", 88, 85),
                new NilaiMahasiswa("2409106005", "Eka Putri", 75, 80),
                new NilaiMahasiswa("2409106002", "Bima Saputra", 75, 80),
                new NilaiMahasiswa("2409106004", "Dimas Pratama", 64, 60));

        System.out.println("=== URUT NIM (urutan alami) ===");
        List<NilaiMahasiswa> urutNim = new ArrayList<>(kelas);
        Collections.sort(urutNim);
        for (NilaiMahasiswa mhs : urutNim) {
            System.out.println(mhs);
        }

        System.out.println();
        System.out.println("=== RANKING KELAS ===");
        List<NilaiMahasiswa> ranking = new ArrayList<>(kelas);
        ranking.sort(Comparator.comparing(NilaiMahasiswa::getNilaiAkhir).reversed()
                .thenComparing(NilaiMahasiswa::getNilaiUas, Comparator.reverseOrder())
                .thenComparing(NilaiMahasiswa::getNama));
        for (int i = 0; i < ranking.size(); i++) {
            NilaiMahasiswa mhs = ranking.get(i);
            System.out.println(String.format("%d. %-15s%3d (UAS %d)", i + 1, mhs.getNama(),
                    mhs.getNilaiAkhir(), mhs.getNilaiUas()));
        }

        System.out.println();
        int lulus = 0;
        for (NilaiMahasiswa mhs : ranking) {
            if (mhs.getNilaiAkhir() >= 70) {
                lulus++;
            }
        }
        System.out.println("Lulus (nilai akhir >= 70): " + lulus + " orang");
        System.out.println("Peringkat 1: " + ranking.get(0).getNama());
    }
}

/** Nilai akhir dan nilai UAS seorang mahasiswa. */
class NilaiMahasiswa implements Comparable<NilaiMahasiswa> {
    private String nim;
    private String nama;
    private int nilaiAkhir;
    private int nilaiUas;

    public NilaiMahasiswa(String nim, String nama, int nilaiAkhir, int nilaiUas) {
        this.nim = nim;
        this.nama = nama;
        this.nilaiAkhir = nilaiAkhir;
        this.nilaiUas = nilaiUas;
    }

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }

    public int getNilaiAkhir() {
        return nilaiAkhir;
    }

    public int getNilaiUas() {
        return nilaiUas;
    }

    @Override
    public int compareTo(NilaiMahasiswa lain) {
        return nim.compareTo(lain.nim); // urutan alami: NIM terkecil dulu
    }

    @Override
    public String toString() {
        return nim + " " + nama;
    }
}
