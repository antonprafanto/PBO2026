/*
 * Solusi Latihan 01 - Rata-rata Nilai dari Teks
 * Pertemuan 11 - Exception Handling
 *
 * Ide penyelesaian:
 * - Setiap teks diubah dengan Integer.parseInt() di dalam try. Jika gagal
 *   (NumberFormatException), cetak pesan, lalu perulangan lanjut.
 * - Penjumlahan ditulis di AKHIR blok try (Java tidak punya blok else),
 *   sehingga hanya dijalankan jika parseInt() berhasil.
 * - Rata-rata = total / jumlahValid. Jika TIDAK ADA nilai yang valid,
 *   jumlahValid = 0 sehingga pembagian melempar ArithmeticException.
 *   Exception itu sengaja tidak ditangkap di rataRataNilai(), tetapi
 *   merambat ke prosesKelas(), yang tahu harus menampilkan pesan apa.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01RataRataNilai.java
 */
public class Latihan01RataRataNilai {

    /** Rata-rata (sisa pembagian dibuang) dari teks yang berisi bilangan bulat. */
    static int rataRataNilai(String[] daftarTeks) {
        int total = 0;
        int jumlahValid = 0;
        for (String teks : daftarTeks) {
            try {
                int nilai = Integer.parseInt(teks);
                total += nilai;
                jumlahValid++;
            } catch (NumberFormatException e) {
                System.out.println("  '" + teks + "' bukan angka, dilewati");
            }
        }
        return total / jumlahValid; // ArithmeticException jika jumlahValid = 0
    }

    static void prosesKelas(String namaKelas, String[] daftarTeks) {
        System.out.println("=== " + namaKelas + " ===");
        try {
            int rata = rataRataNilai(daftarTeks);
            System.out.println("Rata-rata: " + rata);
        } catch (ArithmeticException e) {
            System.out.println("Tidak ada nilai yang valid, rata-rata tidak bisa dihitung");
        }
    }

    public static void main(String[] args) {
        prosesKelas("KELAS A", new String[] {"80", "75", "sembilan puluh", "92", ""});
        System.out.println();
        prosesKelas("KELAS B", new String[] {"-", "tidak hadir"});
    }
}
