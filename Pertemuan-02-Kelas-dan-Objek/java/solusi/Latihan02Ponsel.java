/*
 * Solusi Latihan 02 - Kelas Ponsel
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * - Field baterai berubah lewat method pakai() dan isiDaya().
 * - pakai(menit): setiap menit memakai 2% baterai. Jika baterai tidak cukup,
 *   baterai menjadi 0 dan ponsel mati.
 * - isiDaya(persen): baterai bertambah, tetapi tidak boleh lebih dari 100.
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan02Ponsel.java
 */
public class Latihan02Ponsel {

    public static void main(String[] args) {
        Ponsel hp = new Ponsel("Samsung", 50);
        hp.tampilkanInfo();
        hp.pakai(10);
        hp.tampilkanInfo();
        hp.isiDaya(100);
        hp.tampilkanInfo();
        hp.pakai(60);
        hp.tampilkanInfo();
    }
}

/** Ponsel dengan baterai 0 sampai 100 persen. */
class Ponsel {
    String merek;
    int baterai;

    Ponsel(String merek, int baterai) {
        this.merek = merek;
        this.baterai = baterai;
    }

    void pakai(int menit) {
        int kebutuhan = menit * 2;
        if (kebutuhan >= baterai) {
            baterai = 0;
            System.out.println("Dipakai " + menit + " menit... Baterai habis! Ponsel mati.");
        } else {
            baterai = baterai - kebutuhan;
            System.out.println("Dipakai " + menit + " menit, baterai berkurang " + kebutuhan + "%");
        }
    }

    void isiDaya(int persen) {
        baterai = baterai + persen;
        if (baterai > 100) {
            baterai = 100;
        }
        System.out.println("Diisi daya " + persen + "%");
    }

    void tampilkanInfo() {
        System.out.println("  Ponsel " + merek + " - baterai " + baterai + "%");
    }
}
