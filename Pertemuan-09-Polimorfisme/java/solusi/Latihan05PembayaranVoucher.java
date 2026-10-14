/*
 * Solusi Latihan 05 - KedaiKita: Bayar dengan Voucher
 * Pertemuan 09 - Polimorfisme
 *
 * Ide penyelesaian:
 * - PembayaranVoucher adalah anak kelas pembayaran (is-a), sama seperti
 *   PembayaranTunai, PembayaranQRIS, dan PembayaranKartu.
 * - Ia meng-override namaMetode() dan proses(). hitungBiayaLayanan() tidak
 *   ditulis ulang: voucher tidak dikenai biaya, jadi versi induk (0) dipakai.
 * - Voucher hanya bisa dipakai SEKALI. Sisa nilainya hangus.
 * - Method bayar() milik pesanan TIDAK DIUBAH (logikanya sama persis dengan
 *   Pesanan.bayar() di studi kasus), tetapi langsung bisa menerima voucher.
 *
 * Catatan nama kelas: folder java/ pertemuan ini sudah punya kelas Pelanggan,
 * Pembayaran, PembayaranTunai, dan Pesanan (di studi-kasus). Editor seperti
 * VS Code menganggap satu folder sebagai satu proyek dan akan protes "The type
 * Pembayaran is already defined". Karena itu, salinan RINGKAS kelas-kelas tadi
 * di file ini diberi akhiran "Kedai": PelangganKedai, PembayaranKedai,
 * PembayaranTunaiKedai, dan PesananKedai (pesanan langsung diberi total, tanpa
 * ItemPesanan). Di salinan studi kasus milikmu (di folder latihanmu, bukan di
 * folder materi), cukup buat file PembayaranVoucher.java berisi
 * "public class PembayaranVoucher extends Pembayaran", lalu pakai di Main.java.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan05PembayaranVoucher.java
 */
import java.util.List;
import java.util.Locale;

public class Latihan05PembayaranVoucher {

    public static void main(String[] args) {
        PelangganKedai budi = new PelangganKedai("Budi Santoso");
        PelangganKedai siti = new PelangganKedai("Siti Aminah");
        PembayaranVoucher voucher = new PembayaranVoucher("KEDAI50", 50000);

        System.out.println("=== VOUCHER TIDAK CUKUP, GANTI TUNAI ===");
        PesananKedai pesanan1 = new PesananKedai("P001", budi, 61000);
        if (!pesanan1.bayar(voucher)) {
            pesanan1.bayar(new PembayaranTunaiKedai(100000));
        }

        System.out.println();
        System.out.println("=== VOUCHER CUKUP ===");
        PesananKedai pesanan2 = new PesananKedai("P002", siti, 31000);
        pesanan2.bayar(voucher);

        System.out.println();
        System.out.println("=== VOUCHER YANG SAMA DIPAKAI LAGI ===");
        PesananKedai pesanan3 = new PesananKedai("P003", budi, 15000);
        pesanan3.bayar(voucher);

        System.out.println();
        System.out.println("=== STATUS AKHIR ===");
        for (PesananKedai pesanan : List.of(pesanan1, pesanan2, pesanan3)) {
            System.out.println(pesanan.getNomor() + ": " + pesanan.getStatus());
        }
        System.out.println("Poin " + budi.getNama() + ": " + budi.getPoin());
        System.out.println("Poin " + siti.getNama() + ": " + siti.getPoin());
    }
}

/** Salinan ringkas Pelanggan: nama dan poin saja. */
class PelangganKedai {
    private String nama;
    private int poin;

    public PelangganKedai(String nama) {
        this.nama = nama;
        this.poin = 0;
    }

    public String getNama() {
        return nama;
    }

    public int getPoin() {
        return poin;
    }

    public void tambahPoin(int jumlah) {
        poin += jumlah;
    }
}

/** Salinan kelas induk Pembayaran dari studi kasus. */
class PembayaranKedai {

    /** Pengganti kelas Rupiah: 18000 -> "Rp18.000". Dipakai juga oleh kelas anak. */
    public static String formatRupiah(int angka) {
        return "Rp" + String.format(Locale.US, "%,d", angka).replace(',', '.');
    }

    public String namaMetode() {
        return "Pembayaran umum";
    }

    public int hitungBiayaLayanan(int total) {
        return 0;
    }

    public boolean proses(int total) {
        System.out.println("  Memproses pembayaran " + formatRupiah(total));
        return true;
    }
}

/** Salinan PembayaranTunai dari studi kasus. */
class PembayaranTunaiKedai extends PembayaranKedai {
    private int uangDiterima;
    private int kembalian;

    public PembayaranTunaiKedai(int uangDiterima) {
        this.uangDiterima = uangDiterima;
        this.kembalian = 0;
    }

    public int getKembalian() {
        return kembalian;
    }

    @Override
    public String namaMetode() {
        return "Tunai";
    }

    @Override
    public boolean proses(int total) {
        if (uangDiterima < total) {
            int kurang = total - uangDiterima;
            System.out.println("  Uang kurang " + formatRupiah(kurang));
            return false;
        }
        kembalian = uangDiterima - total;
        System.out.println("  Uang diterima " + formatRupiah(uangDiterima)
                + ", kembalian " + formatRupiah(kembalian));
        return true;
    }
}

/** KELAS BARU: bayar dengan voucher bernilai tetap, sekali pakai. */
class PembayaranVoucher extends PembayaranKedai {
    private String kode;
    private int nilai;
    private boolean terpakai;

    public PembayaranVoucher(String kode, int nilai) {
        this.kode = kode;
        this.nilai = nilai;
        this.terpakai = false;
    }

    @Override
    public String namaMetode() {
        return "Voucher " + kode;
    }

    @Override
    public boolean proses(int total) {
        if (terpakai) {
            System.out.println("  Voucher " + kode + " sudah pernah dipakai");
            return false;
        }
        if (nilai < total) {
            System.out.println("  Nilai voucher " + formatRupiah(nilai)
                    + " tidak cukup");
            return false;
        }
        terpakai = true;
        int sisa = nilai - total;
        System.out.println("  Voucher " + kode + " dipakai, sisa "
                + formatRupiah(sisa) + " hangus");
        return true;
    }
}

/** Salinan ringkas Pesanan: total langsung diisi saat pesanan dibuat. */
class PesananKedai {
    private String nomor;
    private PelangganKedai pelanggan;
    private int totalPesanan;
    private String status;

    public PesananKedai(String nomor, PelangganKedai pelanggan, int total) {
        this.nomor = nomor;
        this.pelanggan = pelanggan;
        this.totalPesanan = total;
        this.status = "BARU";
    }

    public String getNomor() {
        return nomor;
    }

    public String getStatus() {
        return status;
    }

    public int hitungTotal() {
        return totalPesanan;
    }

    /** TIDAK DIUBAH: logikanya sama persis dengan Pesanan.bayar() di studi kasus. */
    public boolean bayar(PembayaranKedai pembayaran) {
        int total = hitungTotal();
        int biaya = pembayaran.hitungBiayaLayanan(total); // polimorfisme
        int totalBayar = total + biaya;
        System.out.println("Pembayaran pesanan " + nomor + " (" + pelanggan.getNama() + ")");
        System.out.println("  Metode       : " + pembayaran.namaMetode()); // polimorfisme
        if (biaya > 0) {
            System.out.println("  Biaya layanan: " + PembayaranKedai.formatRupiah(biaya));
        }
        System.out.println("  Total bayar  : " + PembayaranKedai.formatRupiah(totalBayar));
        boolean berhasil = pembayaran.proses(totalBayar); // polimorfisme
        if (berhasil) {
            status = "LUNAS";
            int poin = total / 10000;
            if (poin > 0) {
                pelanggan.tambahPoin(poin);
            }
            System.out.println("  Status       : LUNAS (+" + poin + " poin)");
        } else {
            System.out.println("  Status       : GAGAL, silakan pilih metode lain");
        }
        return berhasil;
    }
}
