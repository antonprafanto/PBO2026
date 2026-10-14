/*
 * Contoh 03 - Map: Mencari Data Lewat Kunci
 * Pertemuan 12 - Koleksi dan Generics
 *
 * Map menyimpan pasangan KUNCI -> NILAI. Di sini kuncinya NIM (String) dan
 * nilainya objek Mahasiswa. Mencari lewat kunci tidak perlu memeriksa data
 * satu per satu seperti pada List.
 * Map<String, Mahasiswa> = interface; HashMap = wujud yang paling umum dipakai.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03MapPencarian.java
 */
import java.util.HashMap;
import java.util.List;
import java.util.Map;

public class Contoh03MapPencarian {

    /** Pencarian cara lama: periksa satu per satu dari depan. */
    static Mahasiswa cariDiList(List<Mahasiswa> daftar, String nim) {
        int langkah = 0;
        for (Mahasiswa mhs : daftar) {
            langkah++;
            if (mhs.getNim().equals(nim)) {
                System.out.println("  (list memeriksa " + langkah + " data sampai ketemu)");
                return mhs;
            }
        }
        return null;
    }

    public static void main(String[] args) {
        List<Mahasiswa> daftar = List.of(
                new Mahasiswa("2409106001", "Ayu Lestari", "Informatika"),
                new Mahasiswa("2409106002", "Bima Saputra", "Informatika"),
                new Mahasiswa("2409106003", "Citra Dewi", "Informatika"),
                new Mahasiswa("2409106004", "Dimas Pratama", "Informatika"));
        Map<String, Mahasiswa> data = new HashMap<>(); // [1] Map kosong: NIM -> Mahasiswa
        for (Mahasiswa mhs : daftar) {
            data.put(mhs.getNim(), mhs); // [2] simpan dengan kunci NIM
        }

        System.out.println("=== CARI MAHASISWA BERDASARKAN NIM ===");
        System.out.println("Lewat list : " + cariDiList(daftar, "2409106004"));
        System.out.println("Lewat kunci: " + data.get("2409106004")); // [3] langsung lewat kunci
        String nimAsing = "2409106099";
        if (data.containsKey(nimAsing)) { // [4] cek dulu apakah kuncinya ada
            System.out.println(data.get(nimAsing));
        } else {
            System.out.println("NIM " + nimAsing + " tidak terdaftar");
        }
        if (data.get(nimAsing) == null) { // [5] get(): null jika kunci tidak ada
            System.out.println("get() untuk NIM asing: tidak ada hasil");
        }

        System.out.println();
        System.out.println("=== MENGUBAH, MENGHAPUS, DAN NILAI CADANGAN ===");
        System.out.println("Jumlah data: " + data.size());
        Mahasiswa bimaBaru = new Mahasiswa("2409106002", "Bima Saputra", "Sistem Informasi");
        data.put("2409106002", bimaBaru); // [6] kunci sudah ada: nilai lama DITIMPA
        System.out.println("Bima pindah prodi: " + data.get("2409106002"));
        System.out.println("Jumlah data: " + data.size()); // tetap 4: kunci tidak bisa kembar
        data.remove("2409106001"); // [7] hapus berdasarkan kunci
        System.out.println("Setelah 2409106001 dihapus: " + data.size() + " data");
        Map<String, Integer> pinjaman = new HashMap<>(); // NIM -> jumlah buku dipinjam
        pinjaman.put("2409106003", 2);
        System.out.println("Buku dipinjam Citra: " + pinjaman.getOrDefault("2409106003", 0)); // [8]
        System.out.println("Buku dipinjam Dimas: " + pinjaman.getOrDefault("2409106004", 0));
    }
}

/** Data singkat seorang mahasiswa. */
class Mahasiswa {
    private String nim;
    private String nama;
    private String prodi;

    public Mahasiswa(String nim, String nama, String prodi) {
        this.nim = nim;
        this.nama = nama;
        this.prodi = prodi;
    }

    public String getNim() {
        return nim;
    }

    public String getNama() {
        return nama;
    }

    @Override
    public String toString() {
        return nim + " " + nama + " (" + prodi + ")";
    }
}
