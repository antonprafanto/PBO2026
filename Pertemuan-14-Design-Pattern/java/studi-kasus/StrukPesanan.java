/*
 * File StrukPesanan.java: kelas StrukPesanan.
 *
 * SRP (Single Responsibility): satu-satunya alasan kelas ini berubah adalah
 * "format struk berubah". Aturan hitung harga tetap di Pesanan dan Diskon.
 *
 * buatTeks() MENGEMBALIKAN teks (bukan langsung mencetaknya), sehingga mudah
 * diuji dan bisa dipakai ulang, misalnya untuk disimpan ke file atau dikirim.
 *
 * Yang baru di Pertemuan 14: kepala struk memakai nama & alamat dari
 * PengaturanKedai (Singleton), dan ada baris pajak.
 */

import java.util.ArrayList;
import java.util.List;

/** Menyusun dan mencetak struk untuk satu pesanan. */
public class StrukPesanan implements DapatDicetak {
    private static final int LEBAR_STRUK = 40;

    private Pesanan pesanan;

    public StrukPesanan(Pesanan pesanan) {
        this.pesanan = pesanan;
    }

    /** Teks kiri rata kiri (30 kolom), teks kanan rata kanan (10 kolom). */
    private static String barisRapi(String kiri, String kanan) {
        return String.format("%-30s%10s", kiri, kanan);
    }

    public String buatTeks() {
        Pesanan p = pesanan;
        PengaturanKedai pengaturan = PengaturanKedai.getInstance();
        String garis = "=".repeat(LEBAR_STRUK);
        List<String> baris = new ArrayList<>();
        baris.add(garis);
        baris.add(pengaturan.getNamaKedai());
        baris.add(pengaturan.getAlamat());
        baris.add(garis);
        baris.add("No. Pesanan : " + p.getNomor());
        baris.add("Pelanggan   : " + p.getPelanggan().getNama());
        baris.add("Status      : " + p.getStatus());
        baris.add("-".repeat(LEBAR_STRUK));
        for (ItemPesanan item : p.getDaftarItem()) {
            String subtotal = Rupiah.format(item.hitungSubtotal());
            baris.add(barisRapi(item.toString(), subtotal));
        }
        baris.add("-".repeat(LEBAR_STRUK));
        baris.add(barisRapi("Subtotal", Rupiah.format(p.hitungSubtotal())));
        int potongan = p.hitungPotongan();
        if (potongan > 0) {
            baris.add(barisRapi("Diskon " + p.getDiskon().keterangan(),
                    "-" + Rupiah.format(potongan)));
        }
        String pajak = "Pajak " + pengaturan.getPajakPersen() + "%";
        baris.add(barisRapi(pajak, Rupiah.format(p.hitungPajak())));
        baris.add(barisRapi("TOTAL", Rupiah.format(p.hitungTotal())));
        baris.add(garis);
        return String.join("\n", baris);
    }

    @Override
    public void cetak() {
        System.out.println(buatTeks());
    }
}
