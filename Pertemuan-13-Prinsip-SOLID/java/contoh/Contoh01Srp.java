/*
 * Contoh 01 - SRP: Satu Kelas, Satu Alasan untuk Berubah
 * Pertemuan 13 - Prinsip SOLID
 *
 * Versi MELANGGAR: LaporanSerbaBisa menghitung nilai, menentukan predikat,
 * DAN mencetak laporan di dalam satu method. Hasil hitungannya "terkunci"
 * di dalam println, sehingga tidak bisa dipakai untuk keperluan lain.
 *
 * Versi SESUAI SRP:
 * - PenghitungNilai  -> hanya menghitung (rata-rata dan predikat)
 * - PencetakLaporan  -> hanya menyusun dan mencetak laporan
 * Laporannya SAMA PERSIS, tetapi hitungannya kini bisa dipakai ulang.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh01Srp.java
 */
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

public class Contoh01Srp {

    public static void main(String[] args) {
        Map<String, List<Integer>> dataNilai = new LinkedHashMap<>();
        dataNilai.put("Ayu", List.of(85, 90, 78));
        dataNilai.put("Bima", List.of(70, 65, 80));
        dataNilai.put("Citra", List.of(55, 60, 58));

        System.out.println("=== VERSI MELANGGAR SRP ===");
        new LaporanSerbaBisa(dataNilai).cetakLaporan();

        System.out.println();
        System.out.println("=== VERSI SESUAI SRP ===");
        PenghitungNilai penghitung = new PenghitungNilai();
        new PencetakLaporan(penghitung).cetak(dataNilai);

        System.out.println();
        System.out.println("=== BONUS SRP: HITUNGAN DIPAKAI ULANG ===");
        for (Map.Entry<String, List<Integer>> entri : dataNilai.entrySet()) {
            int rata = penghitung.rataRata(entri.getValue()); // [5] tanpa ikut mencetak laporan
            if (penghitung.predikat(rata).equals("D")) {
                System.out.println(entri.getKey() + " perlu remedial (rata-rata " + rata + ")");
            }
        }
    }
}

// ------------------------------------------------------------ MELANGGAR SRP
/** Menghitung DAN mencetak sekaligus (dua alasan untuk berubah). */
class LaporanSerbaBisa {
    private Map<String, List<Integer>> dataNilai; // nama -> daftar nilai

    public LaporanSerbaBisa(Map<String, List<Integer>> dataNilai) {
        this.dataNilai = dataNilai;
    }

    public void cetakLaporan() {
        System.out.println("LAPORAN NILAI KELAS PBO");
        for (Map.Entry<String, List<Integer>> entri : dataNilai.entrySet()) {
            int jumlah = 0;
            for (int nilai : entri.getValue()) {
                jumlah += nilai;
            }
            int rata = jumlah / entri.getValue().size(); // [1] aturan hitung...
            String predikat;
            if (rata >= 80) {
                predikat = "A";
            } else if (rata >= 70) {
                predikat = "B";
            } else if (rata >= 60) {
                predikat = "C";
            } else {
                predikat = "D";
            }
            System.out.println(String.format("  %-8s%4s  %s",
                    entri.getKey(), rata, predikat)); // [2] ...bercampur format
        }
    }
}

// -------------------------------------------------------------- SESUAI SRP
/** Hanya menghitung. Tidak pernah mencetak apa pun. */
class PenghitungNilai {

    public int rataRata(List<Integer> daftar) {
        int jumlah = 0;
        for (int nilai : daftar) {
            jumlah += nilai;
        }
        return jumlah / daftar.size();
    }

    public String predikat(int rata) { // [3] satu-satunya tempat aturan predikat
        if (rata >= 80) {
            return "A";
        }
        if (rata >= 70) {
            return "B";
        }
        if (rata >= 60) {
            return "C";
        }
        return "D";
    }
}

/** Hanya menyusun dan mencetak laporan. */
class PencetakLaporan {
    private PenghitungNilai penghitung;

    public PencetakLaporan(PenghitungNilai penghitung) {
        this.penghitung = penghitung; // [4] hitungan diminta dari ahlinya
    }

    public void cetak(Map<String, List<Integer>> dataNilai) {
        System.out.println("LAPORAN NILAI KELAS PBO");
        for (Map.Entry<String, List<Integer>> entri : dataNilai.entrySet()) {
            int rata = penghitung.rataRata(entri.getValue());
            String predikat = penghitung.predikat(rata);
            System.out.println(String.format("  %-8s%4s  %s", entri.getKey(), rata, predikat));
        }
    }
}
