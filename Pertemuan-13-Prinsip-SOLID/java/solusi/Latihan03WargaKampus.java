/*
 * Solusi Latihan 03 - Interface Ramping untuk Warga Kampus (ISP)
 * Pertemuan 13 - Prinsip SOLID
 *
 * Ide penyelesaian:
 * - Interface gemuk WargaKampus (ikutKuliah, bayarUkt, mengajar, isiNilai)
 *   dipecah menjadi dua interface kecil:
 *     Pelajar  -> ikutKuliah(), bayarUkt()
 *     Pengajar -> mengajar(), isiNilai()
 * - Mahasiswa hanya Pelajar, Dosen hanya Pengajar. Tidak ada lagi method palsu
 *   seperti "Dosen.bayarUkt()" yang melempar exception.
 * - AsistenPraktikum meng-implements DUA interface sekaligus, sehingga ia boleh
 *   masuk ke daftar pelajar maupun daftar pengajar.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan03WargaKampus.java
 */
import java.util.List;

public class Latihan03WargaKampus {

    public static void main(String[] args) {
        Dosen hendra = new Dosen("Dr. Hendra");
        Mahasiswa ayu = new Mahasiswa("Ayu");
        AsistenPraktikum rizky = new AsistenPraktikum("Rizky");

        List<Pengajar> pengajar = List.of(hendra, rizky); // hanya yang meng-implements Pengajar
        List<Pelajar> pelajar = List.of(ayu, rizky); // hanya yang meng-implements Pelajar

        System.out.println("=== PARA PENGAJAR ===");
        for (Pengajar orang : pengajar) {
            System.out.println(orang.mengajar("PBO"));
            System.out.println(orang.isiNilai("Ayu", "A"));
        }

        System.out.println();
        System.out.println("=== PARA PELAJAR ===");
        for (Pelajar orang : pelajar) {
            System.out.println(orang.ikutKuliah("Basis Data"));
            System.out.println(orang.bayarUkt());
        }

        System.out.println();
        System.out.println("Jumlah pengajar: " + pengajar.size() + ", jumlah pelajar: " + pelajar.size());
        System.out.println("Rizky ada di kedua daftar karena ia mahasiswa sekaligus asisten.");
    }
}

/** Interface kecil untuk orang yang belajar. */
interface Pelajar {
    String ikutKuliah(String matkul);

    String bayarUkt();
}

/** Interface kecil untuk orang yang mengajar dan menilai. */
interface Pengajar {
    String mengajar(String matkul);

    String isiNilai(String namaMahasiswa, String nilai);
}

class Mahasiswa implements Pelajar {
    private String nama;

    public Mahasiswa(String nama) {
        this.nama = nama;
    }

    @Override
    public String ikutKuliah(String matkul) {
        return nama + " mengikuti kuliah " + matkul;
    }

    @Override
    public String bayarUkt() {
        return nama + " membayar UKT semester depan";
    }
}

class Dosen implements Pengajar {
    private String nama;

    public Dosen(String nama) {
        this.nama = nama;
    }

    @Override
    public String mengajar(String matkul) {
        return nama + " mengajar " + matkul;
    }

    @Override
    public String isiNilai(String namaMahasiswa, String nilai) {
        return nama + " mengisi nilai " + nilai + " untuk " + namaMahasiswa;
    }
}

class AsistenPraktikum implements Pelajar, Pengajar { // dua interface kecil sekaligus
    private String nama;

    public AsistenPraktikum(String nama) {
        this.nama = nama;
    }

    @Override
    public String ikutKuliah(String matkul) {
        return nama + " mengikuti kuliah " + matkul;
    }

    @Override
    public String bayarUkt() {
        return nama + " membayar UKT semester depan";
    }

    @Override
    public String mengajar(String matkul) {
        return nama + " membimbing praktikum " + matkul;
    }

    @Override
    public String isiNilai(String namaMahasiswa, String nilai) {
        return nama + " mengisi nilai praktikum " + nilai + " untuk " + namaMahasiswa;
    }
}
