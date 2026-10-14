/*
 * Contoh 03 - Percabangan dan Perulangan
 * Pertemuan 01 - Pengenalan PBO
 *
 * - if / else if / else memilih perintah mana yang dijalankan.
 * - for mengulang dengan penghitung (mulai; syarat; langkah).
 * - while mengulang SELAMA kondisinya masih benar.
 * - Blok perintah ditandai dengan kurung kurawal { }.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh03PercabanganPerulangan.java
 */
public class Contoh03PercabanganPerulangan {

    public static void main(String[] args) {
        System.out.println("=== PERCABANGAN: DISKON TOKO ALAT TULIS ===");
        int totalBelanja = 120000;
        boolean member = true; // [1] boolean: hanya bernilai true atau false

        int persenDiskon; // dideklarasikan dulu, nilainya diisi di percabangan
        if (totalBelanja >= 100000) { // [2] diperiksa dari atas; yang pertama benar dipilih
            persenDiskon = 10;
        } else if (totalBelanja >= 50000) {
            persenDiskon = 5;
        } else {
            persenDiskon = 0;
        }

        if (member) { // [3] kondisi berupa variabel boolean
            persenDiskon = persenDiskon + 5;
        }

        int potongan = totalBelanja * persenDiskon / 100;
        System.out.println("Total belanja : Rp" + totalBelanja);
        System.out.println("Diskon        : " + persenDiskon + "%");
        System.out.println("Potongan      : Rp" + potongan);
        System.out.println("Harus dibayar : Rp" + (totalBelanja - potongan));

        String hari = "Sabtu";
        if (hari.equals("Sabtu") || hari.equals("Minggu")) { // [4] ||: cukup salah satu benar
            System.out.println("Hari " + hari + ": toko tutup pukul 15.00");
        } else {
            System.out.println("Hari " + hari + ": toko tutup pukul 21.00");
        }

        System.out.println();
        System.out.println("=== PERULANGAN FOR: DAFTAR HARGA FOTOKOPI ===");
        int hargaPerLembar = 500;
        for (int lembar = 1; lembar <= 5; lembar++) { // [5] lembar = 1, 2, 3, 4, 5
            System.out.println(lembar + " lembar = Rp" + (lembar * hargaPerLembar));
        }

        System.out.println();
        System.out.println("=== PERULANGAN WHILE: MENABUNG UNTUK BUKU ===");
        int target = 100000;
        int tabungan = 0;
        int minggu = 0;
        while (tabungan < target) { // [6] diulang SELAMA kondisinya benar
            tabungan = tabungan + 30000;
            minggu = minggu + 1;
            System.out.println("Minggu ke-" + minggu + ": tabungan Rp" + tabungan);
        }
        System.out.println("Target Rp" + target + " tercapai dalam " + minggu + " minggu");
    }
}
