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
 * Yang baru di Pertemuan 11:
 * - Pesanan yang sudah LUNAS tidak boleh diubah atau dibayar lagi:
 *   method yang bersangkutan melempar KedaiException.
 * - bayar() tidak lagi mengembalikan true/false. Jika pembayaran gagal,
 *   PembayaranGagalException dari proses() "diteruskan" ke pemanggil, dan
 *   status pesanan tetap BARU.
 */

import java.util.ArrayList;
import java.util.List;

/** Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan. */
public class Pesanan implements DapatDicetak {
    private static final int LEBAR_STRUK = 40;
    private static int nomorTerakhir = 0; // atribut static untuk membuat nomor otomatis

    private String nomor;
    private Pelanggan pelanggan;
    private List<ItemPesanan> daftarItem;
    private String status;

    public Pesanan(Pelanggan pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir); // P001, P002, ...
        this.pelanggan = pelanggan;
        this.daftarItem = new ArrayList<>();
        this.status = "BARU";
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

    public int hitungTotal() {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
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
        status = "LUNAS";
        int poin = total / 10000;
        if (poin > 0) {
            pelanggan.tambahPoin(poin);
        }
        System.out.println("  Status       : LUNAS (+" + poin + " poin)");
    }

    /** Mencetak struk pesanan (memenuhi kontrak DapatDicetak). */
    @Override
    public void cetak() {
        String garis = "=".repeat(LEBAR_STRUK);
        System.out.println(garis);
        System.out.println("KEDAIKITA - STRUK PESANAN");
        System.out.println(garis);
        System.out.println("No. Pesanan : " + nomor);
        System.out.println("Pelanggan   : " + pelanggan.getNama());
        System.out.println("Status      : " + status);
        System.out.println("-".repeat(LEBAR_STRUK));
        for (ItemPesanan item : daftarItem) {
            String subtotal = Rupiah.format(item.hitungSubtotal());
            System.out.println(String.format("%-30s%10s", item.toString(), subtotal));
        }
        System.out.println("-".repeat(LEBAR_STRUK));
        System.out.println(String.format("%-30s%10s", "TOTAL", Rupiah.format(hitungTotal())));
        System.out.println(garis);
    }
}
