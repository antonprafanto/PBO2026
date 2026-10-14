/*
 * Contoh 02 - Asosiasi: Objek yang Mengenal Objek Lain
 * Pertemuan 05 - Relasi Antarkelas
 *
 * Setiap Mahasiswa MENGENAL dosen walinya lewat sebuah field yang berisi
 * referensi ke objek DosenWali. Beberapa mahasiswa bisa mengenal dosen yang
 * SAMA, dan mahasiswa baru boleh belum punya dosen wali (null).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh02Asosiasi.java
 */
public class Contoh02Asosiasi {

    public static void main(String[] args) {
        DosenWali buRina = new DosenWali("Bu Rina", "C-201");
        Mahasiswa ayu = new Mahasiswa("Ayu");
        Mahasiswa bima = new Mahasiswa("Bima");
        Mahasiswa citra = new Mahasiswa("Citra");

        System.out.println("=== SEBELUM PERWALIAN ===");
        System.out.println(ayu.infoPerwalian());

        ayu.aturDosenWali(buRina); // [5] dua mahasiswa mengenal objek yang SAMA
        bima.aturDosenWali(buRina);

        System.out.println();
        System.out.println("=== SETELAH PERWALIAN ===");
        Mahasiswa[] semua = {ayu, bima, citra};
        for (Mahasiswa mahasiswa : semua) {
            System.out.println(mahasiswa.infoPerwalian());
        }

        System.out.println();
        System.out.println("=== BU RINA PINDAH RUANGAN ===");
        buRina.pindahRuangan("D-105"); // [6] diubah di satu tempat saja
        System.out.println(ayu.infoPerwalian());
        System.out.println(bima.infoPerwalian());
    }
}

/** Dosen yang membimbing perwalian mahasiswa. */
class DosenWali {
    private String nama;
    private String ruangan;

    public DosenWali(String nama, String ruangan) {
        this.nama = nama;
        this.ruangan = ruangan;
    }

    public String getNama() {
        return nama;
    }

    public String getRuangan() {
        return ruangan;
    }

    public void pindahRuangan(String ruanganBaru) {
        this.ruangan = ruanganBaru;
    }
}

/** Mahasiswa yang mengenal dosen walinya. */
class Mahasiswa {
    private String nama;
    private DosenWali dosenWali; // [1] field bertipe kelas lain

    public Mahasiswa(String nama) {
        this.nama = nama;
        this.dosenWali = null; // awalnya belum ada
    }

    public void aturDosenWali(DosenWali dosen) {
        this.dosenWali = dosen; // [2] menyimpan REFERENSI, bukan salinan
    }

    public String infoPerwalian() {
        if (dosenWali == null) { // [3] periksa dulu sebelum dipakai
            return nama + ": belum punya dosen wali";
        }
        return nama + ": dosen wali " + dosenWali.getNama()
                + ", ruang " + dosenWali.getRuangan(); // [4]
    }
}
