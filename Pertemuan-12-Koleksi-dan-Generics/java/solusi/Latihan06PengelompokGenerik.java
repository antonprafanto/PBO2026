/*
 * Solusi Latihan 06 - Pengelompok Generik
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Ide penyelesaian:
 * - Method generik <T, K> kelompokkan(daftar, kunci) bekerja untuk tipe isi
 *   APA PUN (T) dan tipe kunci APA PUN (K).
 * - kunci bertipe Function<T, K> (dari java.util.function): sebuah interface
 *   yang method-nya apply(T) mengembalikan K. Lambda atau method reference
 *   bisa langsung dipakai sebagai Function.
 * - Hasilnya Map<K, List<T>>. Jika kunci belum ada, buat ArrayList kosong dulu.
 *   LinkedHashMap menjaga urutan kunci sesuai kemunculan pertama.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06PengelompokGenerik.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.function.Function;

public class Latihan06PengelompokGenerik {

    static <T, K> Map<K, List<T>> kelompokkan(List<T> daftar, Function<T, K> kunci) {
        Map<K, List<T>> hasil = new LinkedHashMap<>();
        for (T isi : daftar) {
            K k = kunci.apply(isi);
            if (!hasil.containsKey(k)) {
                hasil.put(k, new ArrayList<>()); // kunci baru: siapkan list kosong
            }
            hasil.get(k).add(isi);
        }
        return hasil;
    }

    public static void main(String[] args) {
        List<String> buah = List.of("apel", "anggur", "belimbing", "ceri", "bisbul", "alpukat");

        System.out.println("=== BUAH PER HURUF AWAL ===");
        Map<String, List<String>> perHuruf = kelompokkan(buah, kata -> kata.substring(0, 1));
        for (Map.Entry<String, List<String>> entri : perHuruf.entrySet()) {
            System.out.println(entri.getKey() + ": " + String.join(", ", entri.getValue()));
        }

        System.out.println();
        System.out.println("=== BUAH PER PANJANG NAMA ===");
        Map<Integer, List<String>> perPanjang = kelompokkan(buah, String::length);
        for (Map.Entry<Integer, List<String>> entri : perPanjang.entrySet()) {
            System.out.println(entri.getKey() + " huruf: " + String.join(", ", entri.getValue()));
        }

        System.out.println();
        System.out.println("=== ANGGOTA UKM PER ANGKATAN ===");
        List<Anggota> anggota = List.of(
                new Anggota("Bima", 2023),
                new Anggota("Ayu", 2024),
                new Anggota("Eka", 2023),
                new Anggota("Citra", 2024),
                new Anggota("Dimas", 2025));
        Map<Integer, List<Anggota>> perAngkatan = kelompokkan(anggota, Anggota::getAngkatan);
        for (Map.Entry<Integer, List<Anggota>> entri : perAngkatan.entrySet()) {
            List<String> nama = new ArrayList<>();
            for (Anggota a : entri.getValue()) {
                nama.add(a.getNama());
            }
            System.out.println(entri.getKey() + ": " + String.join(", ", nama) + " ("
                    + entri.getValue().size() + " orang)");
        }
    }
}

/** Anggota UKM beserta angkatannya. */
class Anggota {
    private String nama;
    private int angkatan;

    public Anggota(String nama, int angkatan) {
        this.nama = nama;
        this.angkatan = angkatan;
    }

    public String getNama() {
        return nama;
    }

    public int getAngkatan() {
        return angkatan;
    }
}
