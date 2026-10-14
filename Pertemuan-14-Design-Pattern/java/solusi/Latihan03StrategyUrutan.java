/*
 * Solusi Latihan 03 - Strategy Pengurutan Daftar Mahasiswa
 * Pertemuan 14 - Design Pattern Dasar
 *
 * Ide penyelesaian:
 * - StrategiUrut adalah kontrak: nama() dan urutkan(daftar) -> list baru.
 * - Tiga strategi: UrutNim, UrutNama, UrutNilai (nilai tertinggi dulu; jika
 *   nilainya sama, urut nama A-Z).
 * - DaftarPeringkat (context) menyimpan SATU strategi dan bisa menukarnya
 *   kapan saja lewat aturStrategi().
 * - Perhatikan: Comparator (Pertemuan 12) sebenarnya juga sebuah "strategi
 *   kecil" yang kita kirim ke method sort().
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03StrategyUrutan.java
 */
import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

public class Latihan03StrategyUrutan {

    public static void main(String[] args) {
        List<Mahasiswa> kelasPbo = List.of(
                new Mahasiswa("2409106004", "Ayu Lestari", 85),
                new Mahasiswa("2409106002", "Bima Saputra", 92),
                new Mahasiswa("2409106001", "Citra Dewi", 85),
                new Mahasiswa("2409106003", "Dimas Pratama", 78));
        DaftarPeringkat peringkat = new DaftarPeringkat(kelasPbo, new UrutNim());
        peringkat.tampilkan();

        for (StrategiUrut strategi : List.of(new UrutNama(), new UrutNilai())) {
            System.out.println();
            peringkat.aturStrategi(strategi); // tukar strategi saat program berjalan
            peringkat.tampilkan();
        }
    }
}

class Mahasiswa {
    private String nim;
    private String nama;
    private int nilai;

    Mahasiswa(String nim, String nama, int nilai) {
        this.nim = nim;
        this.nama = nama;
        this.nilai = nilai;
    }

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }

    public int getNilai() {
        return nilai;
    }

    @Override
    public String toString() {
        return String.format("%s %-15s%4d", nim, nama, nilai);
    }
}

/** Strategy: kontrak semua cara mengurutkan mahasiswa. */
interface StrategiUrut {
    String nama();

    /** Mengembalikan list BARU yang sudah urut (list asli tidak diubah). */
    List<Mahasiswa> urutkan(List<Mahasiswa> daftar);
}

class UrutNim implements StrategiUrut {
    @Override
    public String nama() {
        return "NIM terkecil";
    }

    @Override
    public List<Mahasiswa> urutkan(List<Mahasiswa> daftar) {
        List<Mahasiswa> hasil = new ArrayList<>(daftar);
        hasil.sort(Comparator.comparing(Mahasiswa::getNim));
        return hasil;
    }
}

class UrutNama implements StrategiUrut {
    @Override
    public String nama() {
        return "Nama A-Z";
    }

    @Override
    public List<Mahasiswa> urutkan(List<Mahasiswa> daftar) {
        List<Mahasiswa> hasil = new ArrayList<>(daftar);
        hasil.sort(Comparator.comparing(Mahasiswa::getNama));
        return hasil;
    }
}

class UrutNilai implements StrategiUrut {
    @Override
    public String nama() {
        return "Nilai tertinggi";
    }

    @Override
    public List<Mahasiswa> urutkan(List<Mahasiswa> daftar) {
        List<Mahasiswa> hasil = new ArrayList<>(daftar);
        // nilai terbesar dulu; jika seri, nama A-Z
        hasil.sort(Comparator.comparing(Mahasiswa::getNilai).reversed()
                .thenComparing(Mahasiswa::getNama));
        return hasil;
    }
}

/** Context: menampilkan mahasiswa memakai strategi yang sedang dipasang. */
class DaftarPeringkat {
    private List<Mahasiswa> daftar;
    private StrategiUrut strategi;

    DaftarPeringkat(List<Mahasiswa> daftar, StrategiUrut strategi) {
        this.daftar = new ArrayList<>(daftar);
        this.strategi = strategi;
    }

    public void aturStrategi(StrategiUrut strategi) {
        this.strategi = strategi;
    }

    public void tampilkan() {
        System.out.println("=== URUT: " + strategi.nama().toUpperCase() + " ===");
        List<Mahasiswa> hasil = strategi.urutkan(daftar);
        for (int i = 0; i < hasil.size(); i++) {
            System.out.println((i + 1) + ". " + hasil.get(i));
        }
    }
}
