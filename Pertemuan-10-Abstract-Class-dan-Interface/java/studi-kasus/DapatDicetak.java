/*
 * File DapatDicetak.java: interface DapatDicetak.
 *
 * Java punya kata kunci khusus interface untuk membuat "kontrak". Method di
 * dalam interface yang ditulis tanpa isi (hanya kepalanya) otomatis public
 * dan abstract. Kelas apa pun yang mengimplementasikan DapatDicetak WAJIB
 * menyediakan method cetak().
 */

/** Kontrak: objek ini bisa dicetak ke layar. */
public interface DapatDicetak {

    /** Mencetak isi objek ke layar. */
    void cetak();
}
