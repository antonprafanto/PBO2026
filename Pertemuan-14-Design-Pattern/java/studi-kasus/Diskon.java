/*
 * File Diskon.java: abstraksi Diskon (sebuah interface). Setiap aturan diskon
 * (TanpaDiskon, DiskonPersen, dan seterusnya) ada di file sendiri.
 *
 * Prinsip yang diterapkan:
 * - OCP (Open/Closed): ingin promo baru? Buat kelas baru yang meng-implements
 *   Diskon. Kelas Pesanan TIDAK perlu diubah sama sekali.
 * - LSP (Liskov Substitution): semua kelas Diskon bisa dipakai di mana pun
 *   Diskon diharapkan, dan selalu mengembalikan potongan >= 0.
 *
 * Di Pertemuan 14 kita mengenali bahwa desain ini adalah pola STRATEGY:
 * setiap kelas diskon adalah satu "strategi" yang bisa ditukar saat program
 * berjalan. Strategi baru: DiskonHappyHour.
 */

import java.util.List;

/** Kontrak semua aturan diskon. */
public interface Diskon {

    /** Besar potongan dalam rupiah (tidak pernah negatif). */
    int hitungPotongan(List<ItemPesanan> daftarItem, Pelanggan pelanggan);

    /** Nama singkat diskon untuk ditampilkan di struk. */
    String keterangan();

    /** Method static milik interface: jumlah subtotal semua item. */
    static int subtotalDari(List<ItemPesanan> daftarItem) {
        int total = 0;
        for (ItemPesanan item : daftarItem) {
            total += item.hitungSubtotal();
        }
        return total;
    }
}
