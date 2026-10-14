/*
 * Solusi Latihan 06 - Kelas Pecahan
 * Pertemuan 03 - Atribut dan Method Lebih Dalam
 *
 * Ide penyelesaian:
 * - Konstruktor langsung menyederhanakan pecahan: pembilang dan penyebut
 *   dibagi dengan FPB keduanya. Jadi new Pecahan(6, 8) tersimpan sebagai 3/4.
 * - fpb(a, b) adalah method static (algoritma Euclid). Ia tidak butuh data
 *   objek, hanya dua angka dari parameter.
 * - Konstruktor satu parameter meneruskan ke this(pembilang, 1), sehingga
 *   new Pecahan(3) berarti 3/1 = 3.
 * - tambah() dan kali() menerima objek Pecahan lain dan MENGEMBALIKAN objek
 *   Pecahan BARU (tipe kembaliannya Pecahan). Objek asalnya tidak diubah.
 *     a/b + c/d = (a*d + c*b) / (b*d)        a/b x c/d = (a*c) / (b*d)
 * - dariTeks("10/4") adalah method static yang membuat objek (konstruktor
 *   alternatif).
 * - samaDengan() membandingkan isi dua pecahan yang sudah disederhanakan.
 * - Pecahan di latihan ini selalu positif, agar semua pembagian int
 *   menghasilkan angka yang sama di Java maupun Python.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan06Pecahan.java
 */
public class Latihan06Pecahan {

    static String yaTidak(boolean nilai) {
        if (nilai) {
            return "ya";
        }
        return "tidak";
    }

    public static void main(String[] args) {
        System.out.println("=== PENYEDERHANAAN OTOMATIS ===");
        System.out.println("6/8 -> " + new Pecahan(6, 8));
        System.out.println("10/5 -> " + new Pecahan(10, 5));
        System.out.println("Dari teks \"10/4\" -> " + Pecahan.dariTeks("10/4"));

        System.out.println();
        System.out.println("=== OPERASI MENGHASILKAN OBJEK BARU ===");
        Pecahan setengah = new Pecahan(1, 2);
        Pecahan sepertiga = new Pecahan(1, 3);
        System.out.println(setengah + " + " + sepertiga + " = " + setengah.tambah(sepertiga));
        Pecahan duaPertiga = new Pecahan(2, 3);
        Pecahan tigaPerempat = Pecahan.dariTeks("3/4");
        System.out.println(duaPertiga + " x " + tigaPerempat + " = "
                + duaPertiga.kali(tigaPerempat));
        Pecahan seperempat = new Pecahan(1, 4);
        System.out.println(seperempat + " + " + tigaPerempat + " = "
                + seperempat.tambah(tigaPerempat));
        Pecahan tiga = new Pecahan(3); // konstruktor satu parameter: penyebut 1
        System.out.println(tiga + " + " + setengah + " = " + tiga.tambah(setengah));
        System.out.println("Setengah tetap " + setengah);

        System.out.println();
        System.out.println("=== MEMBANDINGKAN ISI ===");
        boolean hasil = new Pecahan(2, 4).samaDengan(setengah);
        System.out.println("2/4 sama dengan 1/2? " + yaTidak(hasil));
        hasil = sepertiga.samaDengan(new Pecahan(2, 5));
        System.out.println("1/3 sama dengan 2/5? " + yaTidak(hasil));
    }
}

/** Pecahan positif yang selalu disimpan dalam bentuk paling sederhana. */
class Pecahan {
    int pembilang;
    int penyebut;

    Pecahan(int pembilang, int penyebut) {
        int faktor = Pecahan.fpb(pembilang, penyebut);
        this.pembilang = pembilang / faktor;
        this.penyebut = penyebut / faktor;
    }

    Pecahan(int pembilang) {
        this(pembilang, 1);
    }

    /** Faktor persekutuan terbesar (FPB) dengan algoritma Euclid. */
    static int fpb(int a, int b) {
        while (b != 0) {
            int sisa = a % b;
            a = b;
            b = sisa;
        }
        return a;
    }

    /** Membuat Pecahan dari teks seperti "3/4". */
    static Pecahan dariTeks(String teks) {
        String[] bagian = teks.split("/");
        return new Pecahan(Integer.parseInt(bagian[0]), Integer.parseInt(bagian[1]));
    }

    Pecahan tambah(Pecahan lain) {
        int hasilPembilang = pembilang * lain.penyebut + lain.pembilang * penyebut;
        return new Pecahan(hasilPembilang, penyebut * lain.penyebut);
    }

    Pecahan kali(Pecahan lain) {
        return new Pecahan(pembilang * lain.pembilang, penyebut * lain.penyebut);
    }

    boolean samaDengan(Pecahan lain) {
        return pembilang == lain.pembilang && penyebut == lain.penyebut;
    }

    @Override
    public String toString() {
        if (penyebut == 1) {
            return "" + pembilang;
        }
        return pembilang + "/" + penyebut;
    }
}
