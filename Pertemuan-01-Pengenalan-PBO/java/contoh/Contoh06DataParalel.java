/*
 * Contoh 06 - Data Paralel: Rapi di Awal, Rapuh Saat Program Membesar
 * Pertemuan 01 - Pengenalan PBO
 *
 * Data satu mahasiswa disimpan di BEBERAPA array (nama, nim, nilai).
 * Indeks yang sama = mahasiswa yang sama. Agar data tidak tertukar, setiap
 * method yang memindahkan data wajib memindahkan SEMUA array bersama-sama.
 *
 * Ceritanya: method urutkanBerdasarkanNilai() ditulis ketika datanya baru
 * nama dan nilai. Belakangan, array nim ditambahkan, tetapi method itu lupa
 * diperbarui. Perhatikan apa yang terjadi pada NIM setelah pengurutan!
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06DataParalel.java
 */
public class Contoh06DataParalel {

    static void tampilkan(String[] nama, String[] nim, int[] nilai) {
        for (int i = 0; i < nama.length; i++) {
            System.out.println((i + 1) + ". " + nim[i] + " " + nama[i] + " - nilai " + nilai[i]);
        }
    }

    /** Bubble sort: bandingkan dua tetangga, tukar jika urutannya salah. */
    static void urutkanBerdasarkanNilai(String[] nama, int[] nilai) { // [1] hanya kenal 2 array
        int n = nilai.length;
        for (int putaran = 0; putaran < n - 1; putaran++) {
            for (int i = 0; i < n - 1 - putaran; i++) {
                if (nilai[i] > nilai[i + 1]) {
                    // [2] tukar nilai (pakai variabel sementara), lalu tukar nama juga
                    int sementaraNilai = nilai[i];
                    nilai[i] = nilai[i + 1];
                    nilai[i + 1] = sementaraNilai;

                    String sementaraNama = nama[i];
                    nama[i] = nama[i + 1];
                    nama[i + 1] = sementaraNama;
                }
            }
        }
    }

    public static void main(String[] args) {
        // [3] tiga array paralel: indeks yang sama = mahasiswa yang sama
        String[] nama = {"Ayu", "Bima", "Citra", "Dimas"};
        String[] nim = {"2409106001", "2409106002", "2409106003", "2409106004"};
        int[] nilai = {90, 55, 78, 62};

        System.out.println("=== DATA AWAL ===");
        tampilkan(nama, nim, nilai);

        System.out.println();
        System.out.println("=== DIURUTKAN DARI NILAI TERKECIL ===");
        urutkanBerdasarkanNilai(nama, nilai); // [4] array nim tidak ikut dikirim!
        tampilkan(nama, nim, nilai);

        System.out.println();
        System.out.println("Nama dan nilai pindah bersama, tetapi NIM tertinggal di tempatnya.");
        System.out.println("Sekarang NIM " + nim[0] + " milik Ayu tercatat bersama "
                + nama[0] + "!");
    }
}
