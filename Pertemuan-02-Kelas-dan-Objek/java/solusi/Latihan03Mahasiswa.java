/*
 * Solusi Latihan 03 - Kelas Mahasiswa dan Predikat IPK
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * - predikat() memeriksa IPK dari yang tertinggi dulu (if - else if - else),
 *   lalu MENGEMBALIKAN teks predikat (tipe kembalian String).
 * - Aturan predikat mengikuti soal:
 *     IPK >= 3.51 -> Dengan Pujian
 *     IPK >= 3.01 -> Sangat Memuaskan
 *     IPK >= 2.76 -> Memuaskan
 *     lainnya     -> Cukup
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan03Mahasiswa.java
 */
public class Latihan03Mahasiswa {

    public static void main(String[] args) {
        Mahasiswa[] daftar = {
            new Mahasiswa("2409106001", "Ayu Lestari", 3.75),
            new Mahasiswa("2409106002", "Bima Saputra", 3.2),
            new Mahasiswa("2409106003", "Citra Dewi", 2.9),
            new Mahasiswa("2409106004", "Dimas Pratama", 2.5)
        };
        System.out.println("=== DAFTAR PREDIKAT ===");
        for (Mahasiswa mhs : daftar) {
            mhs.tampilkan();
        }
    }
}

/** Data mahasiswa beserta IPK-nya. */
class Mahasiswa {
    String nim;
    String nama;
    double ipk;

    Mahasiswa(String nim, String nama, double ipk) {
        this.nim = nim;
        this.nama = nama;
        this.ipk = ipk;
    }

    String predikat() {
        if (ipk >= 3.51) {
            return "Dengan Pujian";
        } else if (ipk >= 3.01) {
            return "Sangat Memuaskan";
        } else if (ipk >= 2.76) {
            return "Memuaskan";
        } else {
            return "Cukup";
        }
    }

    void tampilkan() {
        // Menggabungkan double dengan String (+) selalu memakai titik desimal,
        // jadi hasilnya sama di komputer berbahasa Indonesia maupun Inggris.
        System.out.println(nim + " " + nama + " - IPK " + ipk + " - " + predikat());
    }
}
