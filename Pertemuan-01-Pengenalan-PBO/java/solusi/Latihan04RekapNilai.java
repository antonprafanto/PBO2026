/*
 * Solusi Latihan 04 - Rekap Nilai Kuis dengan Method static
 * Pertemuan 01 - Pengenalan PBO
 *
 * Ide penyelesaian:
 * - Setiap tugas dibuat menjadi satu method static kecil yang MENGEMBALIKAN
 *   hasilnya. main() cukup memanggil method-method itu lalu mencetak hasilnya.
 * - hitungRataRata: jumlahkan semua nilai, lalu bagi dengan banyak data
 *   (int / int otomatis membuang desimal).
 * - cariTertinggi: anggap elemen pertama yang tertinggi, lalu bandingkan satu per satu.
 * - hitungLulus: hitung berapa nilai yang >= batas.
 * - hurufMutu: periksa dari batas tertinggi dulu (if - else if - else).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04RekapNilai.java
 */
public class Latihan04RekapNilai {

    static int hitungRataRata(int[] daftarNilai) {
        int total = 0;
        for (int n : daftarNilai) {
            total = total + n;
        }
        return total / daftarNilai.length;
    }

    static int cariTertinggi(int[] daftarNilai) {
        int tertinggi = daftarNilai[0];
        for (int n : daftarNilai) {
            if (n > tertinggi) {
                tertinggi = n;
            }
        }
        return tertinggi;
    }

    static int hitungLulus(int[] daftarNilai, int batas) {
        int jumlah = 0;
        for (int n : daftarNilai) {
            if (n >= batas) {
                jumlah = jumlah + 1;
            }
        }
        return jumlah;
    }

    static String hurufMutu(int nilai) {
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

    public static void main(String[] args) {
        int[] nilaiKuis = {85, 72, 58, 91, 66, 47};

        System.out.println("=== NILAI KUIS PBO ===");
        for (int i = 0; i < nilaiKuis.length; i++) {
            int nilai = nilaiKuis[i];
            System.out.println("Mahasiswa " + (i + 1) + ": " + nilai + " (" + hurufMutu(nilai)
                    + ")");
        }

        System.out.println();
        System.out.println("=== REKAP ===");
        System.out.println("Rata-rata : " + hitungRataRata(nilaiKuis));
        System.out.println("Tertinggi : " + cariTertinggi(nilaiKuis));
        int jumlahLulus = hitungLulus(nilaiKuis, 60);
        System.out.println("Lulus     : " + jumlahLulus + " dari " + nilaiKuis.length
                + " mahasiswa");
    }
}
