/*
 * Contoh 08 - Objek sebagai Nilai Kembalian
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Method boleh mengembalikan OBJEK BARU. Tipe kembaliannya adalah nama
 * kelas, misalnya Durasi. tambah(lain) tidak mengubah durasi yang lama; ia
 * membuat lalu mengembalikan objek Durasi baru. Mirip 2 + 3 yang
 * menghasilkan 5 tanpa mengubah angka 2 maupun 3.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh08ObjekKembalian.java
 */
public class Contoh08ObjekKembalian {

    public static void main(String[] args) {
        Durasi kuliah = new Durasi(2, 30);
        Durasi praktikum = new Durasi(1, 40);

        System.out.println("=== MENJUMLAHKAN DUA DURASI ===");
        Durasi total = kuliah.tambah(praktikum); // [5] hasilnya objek baru
        System.out.println("Kuliah    : " + kuliah);
        System.out.println("Praktikum : " + praktikum);
        System.out.println("Total     : " + total);
        System.out.println("Durasi aneh 1 jam 75 menit dirapikan menjadi " + new Durasi(1, 75));

        System.out.println();
        System.out.println("=== MEMANGGIL SECARA BERANTAI ===");
        Durasi istirahat = new Durasi(0, 45);
        Durasi sehari = kuliah.tambah(istirahat).tambah(praktikum); // [6] hasil dipakai lagi
        System.out.println("Kuliah + istirahat + praktikum = " + sehari);
        System.out.println("Kuliah tetap " + kuliah); // [7] objek lama tidak berubah

        System.out.println();
        System.out.println("=== MEMBANDINGKAN DUA DURASI ===");
        Durasi batas = new Durasi(4, 30);
        if (total.lebihLamaDari(batas)) {
            System.out.println(total + " lebih lama dari " + batas);
        } else {
            System.out.println(total + " tidak lebih lama dari " + batas);
        }
    }
}

/** Lama waktu dalam jam dan menit (bilangan bulat). */
class Durasi {
    int jam;
    int menit;

    Durasi(int jam, int menit) {
        int total = jam * 60 + menit; // [1] dirapikan: 1 jam 75 menit -> 2 jam 15 menit
        this.jam = total / 60;
        this.menit = total % 60;
    }

    int totalMenit() {
        return jam * 60 + menit;
    }

    Durasi tambah(Durasi lain) { // [2] tipe kembaliannya Durasi: sebuah objek
        return new Durasi(0, totalMenit() + lain.totalMenit()); // [3] objek BARU
    }

    boolean lebihLamaDari(Durasi lain) { // [4] method boolean dengan parameter objek
        return totalMenit() > lain.totalMenit();
    }

    @Override
    public String toString() {
        return jam + " jam " + menit + " menit";
    }
}
