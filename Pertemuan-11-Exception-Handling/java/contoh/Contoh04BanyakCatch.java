/*
 * Contoh 04 - Banyak catch dan Urutannya
 * Pertemuan 11 - Exception Handling
 *
 * Satu blok try boleh punya beberapa catch. Java memeriksanya dari ATAS ke
 * BAWAH dan menjalankan catch PERTAMA yang cocok. Karena itu:
 * - catch yang paling SPESIFIK ditulis paling atas,
 * - catch yang paling UMUM (Exception) ditulis paling bawah.
 * Jika urutannya terbalik, program bahkan GAGAL DIKOMPILASI.
 *
 * Satu catch juga boleh menangkap beberapa jenis sekaligus (multi-catch):
 *     catch (NumberFormatException | ArrayIndexOutOfBoundsException e)
 *
 * Setiap baris data berformat "nama;total_nilai;jumlah_tugas".
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04BanyakCatch.java
 */
public class Contoh04BanyakCatch {

    /** Menghitung rata-rata nilai tugas dari satu baris data. */
    static int hitungRataRata(String baris) {
        String[] bagian = baris.split(";");
        int total = Integer.parseInt(bagian[1]); // [1] ArrayIndexOutOfBounds atau NumberFormat
        int jumlahTugas = Integer.parseInt(bagian[2]);
        return total / jumlahTugas; // [2] ArithmeticException jika belum ada tugas
    }

    public static void main(String[] args) {
        String[] data = {
            "Ayu;255;3",
            "Bima;sembilan puluh;1", // nilai bukan angka
            "Citra;160", // kolom jumlah_tugas tidak ada
            "Dimas;0;0", // belum ada tugas yang dinilai
            null, // data kosong dari sistem lama
            "Eka;176;2"
        };
        System.out.println("=== RATA-RATA NILAI TUGAS ===");
        for (int nomor = 1; nomor <= data.length; nomor++) {
            String baris = data[nomor - 1];
            try {
                int rata = hitungRataRata(baris);
                String nama = baris.split(";")[0];
                System.out.println("Baris " + nomor + " (" + nama + "): rata-rata " + rata);
            } catch (NumberFormatException | ArrayIndexOutOfBoundsException e) { // [3] dua jenis
                System.out.println("Baris " + nomor + ": format salah, dilewati");
            } catch (ArithmeticException e) { // [4]
                System.out.println("Baris " + nomor + ": belum ada tugas yang dinilai");
            } catch (Exception e) { // [5] jaring pengaman: PALING UMUM, PALING BAWAH
                System.out.println("Baris " + nomor + ": data tidak terbaca, dilewati");
            }
        }
    }
}
