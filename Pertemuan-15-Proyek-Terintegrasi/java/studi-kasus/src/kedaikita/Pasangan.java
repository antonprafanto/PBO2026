package kedaikita;

/*
 * File Pasangan.java: kelas GENERIK Pasangan<A, B>.
 *
 * "Generik" artinya tipe isi wadahnya ditentukan saat dipakai, bukan saat
 * kelasnya ditulis. Pasangan<String, Integer> berisi (teks, angka), sedangkan
 * Pasangan<String, Menu> berisi (teks, objek Menu). Satu kelas, banyak kegunaan.
 *
 * Catatan: berbeda dengan Python, Java MEMERIKSA tipe ini saat kompilasi.
 * Mengisi Pasangan<String, Integer> dengan dua teks akan langsung ditolak
 * compiler. Untuk angka, generics memakai kelas pembungkus Integer (bukan int).
 */

/** Wadah berisi dua nilai: pertama (tipe A) dan kedua (tipe B). */
public class Pasangan<A, B> {
    private A pertama;
    private B kedua;

    public Pasangan(A pertama, B kedua) {
        this.pertama = pertama;
        this.kedua = kedua;
    }

    public A getPertama() {
        return pertama;
    }

    public B getKedua() {
        return kedua;
    }

    @Override
    public String toString() {
        return "(" + pertama + ", " + kedua + ")";
    }
}
