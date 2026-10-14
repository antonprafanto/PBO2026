package kedaikita;

/*
 * File Pesanan.java: kelas Pesanan (dibantu kelas ItemPesanan).
 *
 * Relasi yang terlihat di sini:
 * - Pesanan --> Pelanggan   : ASOSIASI (pesanan "milik" seorang pelanggan,
 *                             tetapi pelanggan tetap ada walau pesanan selesai)
 * - Pesanan *-- ItemPesanan : KOMPOSISI (item dibuat di dalam pesanan dan
 *                             tidak punya arti tanpa pesanannya)
 * - ItemPesanan --> Menu    : ASOSIASI (item menunjuk ke menu yang dipesan)
 *
 * Yang baru di Pertemuan 14 (design pattern):
 * - Pajak: persentasenya dibaca dari PengaturanKedai (Singleton).
 * - Observer: Pesanan menyimpan daftar pengamat (PengamatPesanan) dan memberi
 *   tahu mereka setiap kali status berubah lewat ubahStatus().
 * - Strategy: objek Diskon (sudah ada sejak Pertemuan 13) bisa ditukar kapan saja.
 */

import java.util.ArrayList;
import java.util.List;

/** Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan. */
public class Pesanan {
    private static final List<String> STATUS_VALID =
            List.of("BARU", "LUNAS", "DIPROSES", "SIAP", "SELESAI");
    private static int nomorTerakhir = 0; // atribut static untuk membuat nomor otomatis

    private String nomor;
    private Pelanggan pelanggan;
    private List<ItemPesanan> daftarItem;
    private String status;
    private Diskon diskon;
    private List<PengamatPesanan> daftarPengamat;

    public Pesanan(Pelanggan pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir); // P001, P002, ...
        this.pelanggan = pelanggan;
        this.daftarItem = new ArrayList<>();
        this.status = "BARU";
        this.diskon = new TanpaDiskon();
        this.daftarPengamat = new ArrayList<>();
    }

    public String getNomor() {
        return nomor;
    }

    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    public String getStatus() {
        return status;
    }

    public Diskon getDiskon() {
        return diskon;
    }

    /** Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<ItemPesanan> getDaftarItem() {
        return new ArrayList<>(daftarItem);
    }

    public void tambahItem(Menu menu, int jumlah) throws KedaiException {
        if (status.equals("LUNAS")) {
            throw new KedaiException("Pesanan " + nomor + " sudah lunas, tidak bisa diubah");
        }
        ItemPesanan item = new ItemPesanan(menu, jumlah); // objek item dibuat OLEH pesanan
        menu.kurangiStok(jumlah); // bisa melempar StokTidakCukupException
        daftarItem.add(item);
    }

    /** Versi overload: tanpa parameter jumlah berarti memesan 1 porsi. */
    public void tambahItem(Menu menu) throws KedaiException {
        tambahItem(menu, 1);
    }

    public void aturDiskon(Diskon diskon) throws KedaiException {
        if (status.equals("LUNAS")) {
            throw new KedaiException("Pesanan " + nomor + " sudah lunas, tidak bisa diubah");
        }
        this.diskon = diskon;
    }

    public int hitungSubtotal() {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }

    public int hitungPotongan() {
        return diskon.hitungPotongan(new ArrayList<>(daftarItem), pelanggan);
    }

    /** Pajak dihitung dari subtotal setelah dipotong diskon. */
    public int hitungPajak() {
        int persen = PengaturanKedai.getInstance().getPajakPersen();
        return (hitungSubtotal() - hitungPotongan()) * persen / 100;
    }

    public int hitungTotal() {
        return hitungSubtotal() - hitungPotongan() + hitungPajak();
    }

    // ----- pola Observer -----
    public void tambahPengamat(PengamatPesanan pengamat) {
        daftarPengamat.add(pengamat);
    }

    /** Mengubah status lalu memberi tahu SEMUA pengamat. */
    public void ubahStatus(String statusBaru) {
        if (!STATUS_VALID.contains(statusBaru)) {
            throw new IllegalArgumentException("Status tidak dikenal: " + statusBaru);
        }
        status = statusBaru;
        for (PengamatPesanan pengamat : daftarPengamat) {
            pengamat.perbarui(this);
        }
    }

    /** Membayar pesanan. Melempar KedaiException jika gagal. */
    public void bayar(Pembayaran pembayaran) throws KedaiException {
        if (status.equals("LUNAS")) {
            throw new KedaiException("Pesanan " + nomor + " sudah lunas");
        }
        int total = hitungTotal();
        int biaya = pembayaran.hitungBiayaLayanan(total);
        int totalBayar = total + biaya;
        System.out.println("Pembayaran pesanan " + nomor + " (" + pelanggan.getNama() + ")");
        System.out.println("  Metode       : " + pembayaran.namaMetode());
        if (biaya > 0) {
            System.out.println("  Biaya layanan: " + Rupiah.format(biaya));
        }
        System.out.println("  Total bayar  : " + Rupiah.format(totalBayar));
        pembayaran.proses(totalBayar); // jika gagal, baris di bawah tidak dijalankan
        int poin = total / 10000;
        if (poin > 0) {
            pelanggan.tambahPoin(poin);
        }
        System.out.println("  Status       : LUNAS (+" + poin + " poin)");
        ubahStatus("LUNAS"); // pengamat ikut diberi tahu
    }
}
