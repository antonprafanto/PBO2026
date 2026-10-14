package kedaikita;

/*
 * File LayananKasir.java: kelas LayananKasir, "otak" alur kerja kasir.
 *
 * Aplikasi kita kini tersusun berlapis (layered):
 *     AplikasiKasir      TAMPILAN     -> hanya urusan tanya-jawab dengan pengguna
 *     LayananKasir       LAYANAN      -> alur kerja: pelanggan, pesanan, bayar, laporan
 *     model              DATA/ATURAN  -> Menu, Pesanan, Pembayaran, Diskon, dan lainnya
 *     RepositoriMenuCSV  PENYIMPANAN  -> membaca/menulis file CSV
 *
 * Lapisan tampilan boleh diganti (misalnya menjadi aplikasi web) tanpa
 * mengubah lapisan layanan dan model.
 */

import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;

/** Menjalankan alur kerja kasir di atas sebuah Kedai. */
public class LayananKasir {
    private Kedai kedai;
    private List<PengamatPesanan> daftarPengamat; // dipasang ke setiap pesanan
    private Map<String, Pelanggan> daftarPelanggan; // no HP -> Pelanggan

    public LayananKasir(Kedai kedai, List<PengamatPesanan> daftarPengamat) {
        this.kedai = kedai;
        this.daftarPengamat = daftarPengamat;
        this.daftarPelanggan = new LinkedHashMap<>();
    }

    public Kedai getKedai() {
        return kedai;
    }

    /** Mengambil pelanggan lama (berdasarkan no HP) atau mendaftarkan baru. */
    public Pelanggan pelanggan(String nama, String noHp) {
        if (!daftarPelanggan.containsKey(noHp)) {
            daftarPelanggan.put(noHp, new Pelanggan(nama, noHp));
        }
        return daftarPelanggan.get(noHp);
    }

    public Pesanan buatPesanan(Pelanggan pelanggan) {
        Pesanan pesanan = kedai.buatPesanan(pelanggan);
        for (PengamatPesanan pengamat : daftarPengamat) {
            pesanan.tambahPengamat(pengamat);
        }
        return pesanan;
    }

    /** Menambah item berdasarkan kode menu. Mengembalikan menu tersebut. */
    public Menu tambahItem(Pesanan pesanan, String kode, int jumlah) throws KedaiException {
        Menu menu = kedai.cariMenu(kode);
        pesanan.tambahItem(menu, jumlah);
        return menu;
    }

    /** Membayar memakai PembayaranFactory (pola Factory). */
    public void bayar(Pesanan pesanan, String jenis, int nominal, String bank)
            throws KedaiException {
        Pembayaran pembayaran = PembayaranFactory.buat(jenis, nominal, bank);
        pesanan.bayar(pembayaran);
    }

    public LaporanPenjualan laporan() {
        return new LaporanPenjualan(kedai.riwayatPesanan());
    }
}
