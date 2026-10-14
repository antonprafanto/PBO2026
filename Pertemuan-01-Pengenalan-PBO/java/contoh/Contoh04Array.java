/*
 * Contoh 04 - Array: Menyimpan Banyak Data dalam Satu Variabel
 * Pertemuan 01 - Pengenalan PBO
 *
 * - Array ditulis dengan tipe elemen diikuti [ ], misalnya int[] atau String[].
 * - Isi awal array boleh ditulis di dalam kurung kurawal { }, dipisah koma.
 * - Indeks (nomor urut) elemen dimulai dari 0, bukan 1.
 * - nama.length memberi tahu banyaknya elemen. Ukuran array TETAP.
 * - Arrays.sort() mengurutkan isi array (angka dari kecil, teks sesuai abjad).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04Array.java
 */
import java.util.Arrays; // [1] Arrays: kelas bawaan Java berisi alat bantu untuk array

public class Contoh04Array {

    public static void main(String[] args) {
        int[] nilai = {78, 92, 65, 88, 70}; // [2] array int berisi lima nilai kuis

        System.out.println("=== NILAI KUIS ===");
        System.out.println("Banyak data    : " + nilai.length); // [3] length tanpa kurung
        System.out.println("Nilai pertama  : " + nilai[0]); // [4] indeks pertama adalah 0
        System.out.println("Nilai terakhir : " + nilai[nilai.length - 1]);

        System.out.println();
        System.out.println("=== SEMUA NILAI ===");
        for (int i = 0; i < nilai.length; i++) { // [5] perulangan dengan indeks: i = 0..4
            System.out.println("Mahasiswa ke-" + (i + 1) + ": " + nilai[i]);
        }

        int total = 0;
        int tertinggi = nilai[0];
        for (int n : nilai) { // [6] for-each: n berisi setiap elemen bergantian
            total = total + n;
            if (n > tertinggi) {
                tertinggi = n;
            }
        }
        System.out.println("Total          : " + total);
        System.out.println("Rata-rata      : " + (total / nilai.length)); // dibulatkan ke bawah
        System.out.println("Tertinggi      : " + tertinggi);

        System.out.println();
        System.out.println("=== MENGUBAH DAN MENGURUTKAN ===");
        nilai[2] = 75; // [7] mengganti elemen di indeks 2 (elemen ketiga)
        System.out.println("Setelah nilai ke-3 diperbaiki: " + Arrays.toString(nilai)); // [8]
        Arrays.sort(nilai); // [9] mengurutkan dari kecil ke besar
        System.out.println("Setelah diurutkan            : " + Arrays.toString(nilai));

        String[] kota = {"Samarinda", "Balikpapan", "Bontang"};
        Arrays.sort(kota); // teks diurutkan sesuai abjad
        String daftarKota = String.join(", ", kota); // [10] gabungkan isi array jadi satu teks
        System.out.println("Kota urut abjad: " + daftarKota);
    }
}
