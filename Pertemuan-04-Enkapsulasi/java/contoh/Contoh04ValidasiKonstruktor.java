/*
 * Contoh 04 - Validasi di Konstruktor
 * Pertemuan 04 - Enkapsulasi
 *
 * Setter yang rajin memeriksa data belum cukup jika konstruktor menyimpan data
 * secara langsung. Objek bisa "lahir cacat" lewat pintu belakang itu.
 *
 * - MahasiswaBercelah: setter memeriksa, tetapi konstruktor menyimpan langsung.
 * - Mahasiswa: konstruktor mengisi field LEWAT setter, sehingga aturan yang
 *   sama berlaku sejak objek lahir. Aturannya cukup ditulis satu kali.
 *
 * (Batas semester 1-14 hanyalah aturan contoh di program ini.)
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh04ValidasiKonstruktor.java
 */
public class Contoh04ValidasiKonstruktor {

    public static void main(String[] args) {
        System.out.println("=== VERSI BERCELAH ===");
        MahasiswaBercelah ayu = new MahasiswaBercelah("Ayu", 20); // [5] semester 20 lolos!
        System.out.println(ayu.getNama() + " tercatat di semester " + ayu.getSemester());
        try {
            ayu.setSemester(21);
        } catch (IllegalArgumentException e) {
            System.out.println("Mengubah lewat setter ditolak: " + e.getMessage());
        }

        System.out.println();
        System.out.println("=== VERSI AMAN ===");
        Mahasiswa bima = new Mahasiswa("Bima", 3);
        System.out.println(bima.getNama() + " tercatat di semester " + bima.getSemester());
        try {
            Mahasiswa citra = new Mahasiswa("Citra", 20); // [6] ditolak sejak lahir
            System.out.println(citra.getNama() + " berhasil dibuat"); // tidak pernah dijalankan
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat mahasiswa: " + e.getMessage());
        }
        try {
            new Mahasiswa("   ", 2); // nama berisi spasi saja
        } catch (IllegalArgumentException e) {
            System.out.println("Gagal membuat mahasiswa: " + e.getMessage());
        }
    }
}

/** Setter-nya memeriksa data, tetapi konstruktornya tidak. */
class MahasiswaBercelah {
    private String nama;
    private int semester;

    public MahasiswaBercelah(String nama, int semester) {
        this.nama = nama;
        this.semester = semester; // [1] celah: disimpan langsung tanpa diperiksa
    }

    public String getNama() {
        return nama;
    }

    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        if (semester < 1 || semester > 14) {
            throw new IllegalArgumentException("Semester harus 1-14, bukan " + semester);
        }
        this.semester = semester;
    }
}

/** Konstruktor memakai setter, jadi data diperiksa sejak objek lahir. */
class Mahasiswa {
    private String nama;
    private int semester;

    public Mahasiswa(String nama, int semester) {
        setNama(nama); // [2] lewat setter: aturan nama ikut diperiksa
        setSemester(semester); // [3] lewat setter: aturan semester ikut diperiksa
    }

    public String getNama() {
        return nama;
    }

    public void setNama(String nama) {
        if (nama.isBlank()) { // [4] isBlank(): kosong atau hanya berisi spasi
            throw new IllegalArgumentException("Nama tidak boleh kosong");
        }
        this.nama = nama;
    }

    public int getSemester() {
        return semester;
    }

    public void setSemester(int semester) {
        if (semester < 1 || semester > 14) {
            throw new IllegalArgumentException("Semester harus 1-14, bukan " + semester);
        }
        this.semester = semester;
    }
}
