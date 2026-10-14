/*
 * File KedaiException.java: exception khusus milik KedaiKita.
 * Setiap turunannya ada di file sendiri (StokTidakCukupException.java, dan seterusnya).
 *
 * Hierarki:
 *     Exception                          (bawaan Java)
 *     +-- KedaiException                 (induk semua error KedaiKita)
 *         +-- StokTidakCukupException
 *         +-- MenuTidakDitemukanException
 *         +-- PembayaranGagalException
 *
 * Karena semuanya turunan KedaiException, kita bisa menangkapnya satu per satu
 * ATAU sekaligus dengan "catch (KedaiException e)".
 *
 * Khusus Java: KedaiException adalah turunan Exception (bukan RuntimeException),
 * jadi termasuk CHECKED exception. Method yang bisa melemparnya wajib menulis
 * "throws ..." di kepalanya, dan pemanggilnya wajib menangkapnya (try/catch)
 * atau ikut meneruskannya (throws).
 */

/** Induk semua error khusus KedaiKita. */
public class KedaiException extends Exception {
    // serialVersionUID: "nomor versi" yang dianjurkan untuk setiap turunan
    // Exception (javac -Xlint memperingatkan jika tidak ada). Cukup diisi 1L.
    private static final long serialVersionUID = 1L;

    public KedaiException(String pesan) {
        super(pesan);
    }
}
