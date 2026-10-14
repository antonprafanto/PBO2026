/*
 * Solusi Latihan 01 - Nomor Antrean Otomatis
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - jumlahPasien adalah atribut KELAS (static): satu penghitung untuk semua pasien.
 * - Setiap kali objek Pasien dibuat, penghitung dinaikkan LEWAT NAMA KELAS
 *   (Pasien.jumlahPasien += 1), lalu nilainya disalin menjadi atribut OBJEK
 *   nomor. Dengan begitu, setiap pasien menyimpan nomornya sendiri.
 * - kodeAntrean() menyusun teks "A001". Format %03d menambahkan angka 0 di
 *   depan sampai panjangnya 3 digit.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan01AntreanPasien.java
 */
public class Latihan01AntreanPasien {

    public static void main(String[] args) {
        System.out.println("=== ANTREAN PUSKESMAS ===");
        System.out.println("Jumlah pasien awal: " + Pasien.jumlahPasien);
        Pasien pasien1 = new Pasien("Andi Wijaya", "demam");
        Pasien pasien2 = new Pasien("Nurul Hidayah", "batuk");
        Pasien pasien3 = new Pasien("Yusuf Hamdani", "sakit gigi");
        System.out.println(pasien1);
        System.out.println(pasien2);
        System.out.println(pasien3);
        System.out.println("Jumlah pasien: " + Pasien.jumlahPasien);

        System.out.println();
        System.out.println("=== PASIEN BARU DATANG ===");
        Pasien pasien4 = new Pasien("Maya Sari", "pusing");
        System.out.println(pasien4);
        System.out.println("Jumlah pasien: " + Pasien.jumlahPasien);
        System.out.println("Nomor pasien pertama tetap " + pasien1.kodeAntrean());
    }
}

/** Pasien yang mendaftar di loket puskesmas. */
class Pasien {
    static int jumlahPasien = 0; // atribut kelas: penghitung bersama

    int nomor; // atribut objek: nomor milik pasien ini
    String nama;
    String keluhan;

    Pasien(String nama, String keluhan) {
        Pasien.jumlahPasien += 1; // lewat nama kelas
        this.nomor = Pasien.jumlahPasien;
        this.nama = nama;
        this.keluhan = keluhan;
    }

    String kodeAntrean() {
        return String.format("A%03d", nomor);
    }

    @Override
    public String toString() {
        return kodeAntrean() + " - " + nama + " (" + keluhan + ")";
    }
}
