/*
 * File Pesanan.java: kelas Pesanan (dibantu kelas ItemPesanan).
 *
 * Relasi yang terlihat di sini:
 * - Pesanan --> Pelanggan   : ASOSIASI (pesanan "milik" seorang pelanggan,
 *                             tetapi pelanggan tetap ada walau pesanan selesai)
 * - Pesanan *-- ItemPesanan : KOMPOSISI (item dibuat di dalam pesanan dan
 *                             tidak punya arti tanpa pesanannya)
 * Tidak punya method main: yang dijalankan adalah kelas Main (Main.java).
 */

import java.util.ArrayList;
import java.util.List;

/** Satu pesanan milik seorang pelanggan, berisi beberapa ItemPesanan. */
public class Pesanan {
    private static final int LEBAR_STRUK = 40;
    private static int nomorTerakhir = 0; // atribut static untuk membuat nomor otomatis

    private String nomor;
    private Pelanggan pelanggan;
    private List<ItemPesanan> daftarItem;

    public Pesanan(Pelanggan pelanggan) {
        nomorTerakhir++;
        this.nomor = String.format("P%03d", nomorTerakhir); // P001, P002, ...
        this.pelanggan = pelanggan;
        this.daftarItem = new ArrayList<>();
    }

    public String getNomor() {
        return nomor;
    }

    public Pelanggan getPelanggan() {
        return pelanggan;
    }

    /** Mengembalikan SALINAN list, agar isi asli tidak diubah dari luar. */
    public List<ItemPesanan> getDaftarItem() {
        return new ArrayList<>(daftarItem);
    }

    public void tambahItem(Menu menu, int jumlah) {
        ItemPesanan item = new ItemPesanan(menu, jumlah); // objek item dibuat OLEH pesanan
        menu.kurangiStok(jumlah); // gagal (IllegalArgumentException) jika stok kurang
        daftarItem.add(item);
    }

    public int hitungTotal() {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }

    public void cetakStruk() {
        String garis = "=".repeat(LEBAR_STRUK);
        System.out.println(garis);
        System.out.println("KEDAIKITA - STRUK PESANAN");
        System.out.println(garis);
        System.out.println("No. Pesanan : " + nomor);
        System.out.println("Pelanggan   : " + pelanggan.getNama());
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
