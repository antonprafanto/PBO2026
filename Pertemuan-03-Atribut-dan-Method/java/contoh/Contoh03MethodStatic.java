/*
 * Contoh 03 - Method static dan Konstruktor Alternatif
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Dua jenis method di dalam kelas Java:
 * - method objek : bekerja dengan data milik objek (punya this).
 * - method static: milik kelas, dipanggil lewat nama kelas, TIDAK punya this.
 *   Method static yang mengembalikan objek baru, seperti dariTeks(), sering
 *   disebut konstruktor alternatif (static factory method).
 *
 * Ingat: main juga method static. Saat program mulai, belum ada objek apa
 * pun, jadi JVM memanggil main lewat nama kelasnya.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03MethodStatic.java
 */
public class Contoh03MethodStatic {

    public static void main(String[] args) {
        System.out.println("=== METHOD OBJEK (butuh objek) ===");
        Tanggal proklamasi = new Tanggal(17, 8, 1945);
        System.out.println("Proklamasi kemerdekaan: " + proklamasi.teks());

        System.out.println();
        System.out.println("=== STATIC METHOD (tanpa objek) ===");
        int[] daftarTahun = {2024, 2026, 1900, 2000};
        for (int tahun : daftarTahun) {
            if (Tanggal.isKabisat(tahun)) { // [5] dipanggil lewat nama kelas
                System.out.println(tahun + ": tahun kabisat");
            } else {
                System.out.println(tahun + ": bukan tahun kabisat");
            }
        }

        System.out.println();
        System.out.println("=== KONSTRUKTOR ALTERNATIF (dari teks) ===");
        Tanggal sumpahPemuda = Tanggal.dariTeks("28-10-1928"); // [6] objek dibuat dari teks
        System.out.println("Sumpah Pemuda: " + sumpahPemuda.teks());
        Tanggal pertempuran = Tanggal.dariTeks("10-11-1945");
        System.out.println("Pertempuran Surabaya: " + pertempuran.teks());
    }
}

/** Tanggal sederhana: hari, bulan, dan tahun (semuanya bilangan bulat). */
class Tanggal {
    static final String[] NAMA_BULAN = {"Januari", "Februari", "Maret", "April", "Mei",
        "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"};

    int hari;
    int bulan;
    int tahun;

    Tanggal(int hari, int bulan, int tahun) {
        this.hari = hari;
        this.bulan = bulan;
        this.tahun = tahun;
    }

    String teks() { // [1] method objek: butuh data milik objek (this)
        return hari + " " + NAMA_BULAN[bulan - 1] + " " + tahun;
    }

    /** true jika tahun kabisat (bulan Februari punya 29 hari). */
    static boolean isKabisat(int tahun) { // [2] method static: tanpa this
        return (tahun % 4 == 0 && tahun % 100 != 0) || tahun % 400 == 0;
    }

    /** Konstruktor alternatif: membuat Tanggal dari teks "hari-bulan-tahun". */
    static Tanggal dariTeks(String teks) { // [3] method static yang mengembalikan objek
        String[] bagian = teks.split("-");
        int hari = Integer.parseInt(bagian[0]); // [4] Integer.parseInt juga method static
        int bulan = Integer.parseInt(bagian[1]);
        int tahun = Integer.parseInt(bagian[2]);
        return new Tanggal(hari, bulan, tahun);
    }
}
