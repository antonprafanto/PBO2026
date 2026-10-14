/*
 * Solusi Latihan 05 - KedaiKita: Riwayat Poin Pelanggan
 * Pertemuan 06 - UML Class Diagram
 *
 * Ide penyelesaian (dari diagram ke kode):
 * - Pelanggan "1" *-- "*" RiwayatPoin : riwayat
 *   KOMPOSISI: setiap kali poin berubah, objek pelanggan sendiri yang MEMBUAT
 *   objek RiwayatPoin lalu menyimpannya di List riwayat.
 * - tambahPoin() dan tukarPoin() tetap memakai parameter yang sama seperti
 *   di studi kasus. Isinya hanya ditambah satu baris untuk mencatat riwayat,
 *   sehingga kode lain yang memakai Pelanggan tidak perlu diubah.
 * - getRiwayat() mengembalikan SALINAN list (seperti getDaftarItem() di Pesanan).
 *
 * Catatan nama kelas: di solusi ini kelasnya diberi nama PelangganKedai, BUKAN
 * Pelanggan. Alasannya, folder java/ pertemuan ini sudah punya kelas Pelanggan
 * (di studi-kasus). Editor seperti VS Code menganggap satu folder sebagai satu
 * proyek dan akan protes "The type Pelanggan is already defined" jika ada dua
 * kelas bernama sama. Di proyekmu sendiri, cukup ubah kelas Pelanggan langsung.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05RiwayatPoin.java
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

public class Latihan05RiwayatPoin {

    public static void main(String[] args) {
        PelangganKedai budi = new PelangganKedai("Budi Santoso", "081234567890");

        System.out.println("=== TRANSAKSI POIN ===");
        budi.tambahPoin(6);
        budi.tambahPoin(3);
        int potongan = budi.tukarPoin(5);
        System.out.println("Tukar 5 poin -> potongan " + formatRupiah(potongan));
        try {
            budi.tukarPoin(10); // gagal: tidak tercatat di riwayat
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal tukar 10 poin: " + e.getMessage());
        }
        System.out.println(budi);

        System.out.println();
        budi.cetakRiwayat();

        System.out.println();
        System.out.println("=== MENCOBA MERUSAK RIWAYAT DARI LUAR ===");
        List<RiwayatPoin> salinan = budi.getRiwayat();
        salinan.clear();
        System.out.println("Isi salinan  : " + salinan.size() + " catatan");
        System.out.println("Riwayat asli : " + budi.getRiwayat().size() + " catatan");
    }

    /** Mengubah 5000 menjadi "Rp5.000" (sama seperti Rupiah.format di studi kasus). */
    static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }
}

/** Satu catatan perubahan poin: positif = bertambah, negatif = berkurang. */
class RiwayatPoin {
    private String keterangan;
    private int perubahan;

    public RiwayatPoin(String keterangan, int perubahan) {
        this.keterangan = keterangan;
        this.perubahan = perubahan;
    }

    public String getKeterangan() {
        return keterangan;
    }

    public int getPerubahan() {
        return perubahan;
    }

    @Override
    public String toString() {
        // Tanda + ditulis manual; angka negatif sudah membawa tanda - sendiri.
        String tanda = perubahan >= 0 ? "+" : "";
        return String.format("%-14s", keterangan) + tanda + perubahan;
    }
}

/** Pelanggan KedaiKita (versi Pertemuan 05) ditambah riwayat poin. */
class PelangganKedai {
    private String nama;
    private String noHp;
    private int poin;
    private List<RiwayatPoin> riwayat; // BARU: bagian milik pelanggan

    public PelangganKedai(String nama, String noHp) {
        this.nama = nama;
        this.noHp = noHp;
        this.poin = 0;
        this.riwayat = new ArrayList<>();
    }

    public String getNama() {
        return nama;
    }

    public String getNoHp() {
        return noHp;
    }

    public int getPoin() {
        return poin;
    }

    /** BARU: mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<RiwayatPoin> getRiwayat() {
        return new ArrayList<>(riwayat);
    }

    public void tambahPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditambahkan harus lebih dari 0");
        }
        poin += jumlah;
        riwayat.add(new RiwayatPoin("Tambah poin", jumlah)); // BARU
    }

    /** Menukar poin menjadi potongan harga. 1 poin = Rp1.000. */
    public int tukarPoin(int jumlah) {
        if (jumlah <= 0) {
            throw new IllegalArgumentException("Poin yang ditukar harus lebih dari 0");
        }
        if (jumlah > poin) {
            throw new IllegalArgumentException("Poin tidak cukup (sisa " + poin + ")");
        }
        poin -= jumlah;
        riwayat.add(new RiwayatPoin("Tukar poin", -jumlah)); // BARU
        return jumlah * 1000;
    }

    /** BARU: mencetak semua catatan poin secara berurutan. */
    public void cetakRiwayat() {
        System.out.println("=== RIWAYAT POIN: " + nama + " ===");
        int nomor = 1;
        for (RiwayatPoin catatan : riwayat) {
            System.out.println(nomor + ". " + catatan);
            nomor++;
        }
        System.out.println("Saldo poin akhir: " + poin);
    }

    @Override
    public String toString() {
        return nama + " (" + noHp + ") - " + poin + " poin";
    }
}
