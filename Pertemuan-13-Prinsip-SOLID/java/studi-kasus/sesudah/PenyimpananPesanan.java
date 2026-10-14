/*
 * File PenyimpananPesanan.java: abstraksi tempat menyimpan pesanan (interface).
 *
 * DIP (Dependency Inversion): Kedai tidak bergantung pada "list di memori"
 * secara langsung, melainkan pada abstraksi PenyimpananPesanan.
 * Hari ini kita memakai PenyimpananMemori. Kelak kita bisa membuat
 * PenyimpananFile atau PenyimpananDatabase TANPA mengubah kelas Kedai
 * (coba di latihan!).
 *
 * ISP (Interface Segregation): kontraknya kecil, hanya simpan() dan semua().
 */

import java.util.List;

/** Kontrak penyimpanan pesanan. */
public interface PenyimpananPesanan {

    /** Menyimpan satu pesanan. */
    void simpan(Pesanan pesanan);

    /** Semua pesanan yang tersimpan, urut sesuai waktu disimpan. */
    List<Pesanan> semua();

    /**
     * Method default: sudah punya isi, jadi kelas yang meng-implements
     * interface ini tidak wajib menulisnya ulang.
     */
    default int jumlah() {
        return semua().size();
    }
}
