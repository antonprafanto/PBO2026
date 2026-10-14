/*
 * Contoh 03 - Upcasting, Downcasting, dan instanceof
 * Pertemuan 09 - Polimorfisme
 *
 * Mahasiswa dan Dosen adalah Pengguna Sistem Informasi Akademik (SIA).
 * - UPCASTING (otomatis): objek Mahasiswa/Dosen disimpan di variabel bertipe
 *   Pengguna. Lewat variabel itu, hanya method milik Pengguna yang boleh
 *   dipanggil, dan versi yang berjalan selalu milik objek sebenarnya.
 * - DOWNCASTING (eksplisit): untuk memanggil method KHUSUS (isiKrs milik
 *   Mahasiswa, inputNilai milik Dosen), variabel harus di-cast ke tipe anak.
 *   Periksa dulu dengan instanceof agar tidak terjadi ClassCastException.
 *
 * Cara menjalankan (Java 16 ke atas, karena memakai pola instanceof):
 *     java Contoh03UpcastingDowncasting.java
 */
import java.util.List;

public class Contoh03UpcastingDowncasting {

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        List<Pengguna> daftar = List.of(
                new Mahasiswa("Ayu Lestari", "2409106001"), // [1] upcasting otomatis
                new Dosen("Rahmat Hidayat", "198003152005011002"),
                new Mahasiswa("Bima Saputra", "2409106002"));

        System.out.println("=== SEMUA PENGGUNA LOGIN ===");
        for (Pengguna pengguna : daftar) { // [2] method bersama: aman untuk semua pengguna
            System.out.println(pengguna.getNama() + " [" + pengguna.peran() + "] menu: "
                    + pengguna.menuUtama());
        }

        System.out.println();
        System.out.println("=== FITUR KHUSUS: CEK JENIS DULU ===");
        for (Pengguna pengguna : daftar) {
            if (pengguna instanceof Mahasiswa) { // [3] pastikan dulu jenisnya
                Mahasiswa mhs = (Mahasiswa) pengguna; // [4] downcasting (cara klasik)
                System.out.println(mhs.isiKrs(21));
            } else if (pengguna instanceof Dosen dosen) { // [5] cek + cast sekaligus (Java 16+)
                System.out.println(dosen.inputNilai("PBO", "A"));
            }
        }

        System.out.println();
        System.out.println("=== CEK JENIS IKUT MENGENAL INDUK ===");
        Pengguna ayu = daftar.get(0);
        System.out.println("Ayu termasuk Mahasiswa? " + yaTidak(ayu instanceof Mahasiswa));
        System.out.println("Ayu termasuk Pengguna?  " + yaTidak(ayu instanceof Pengguna)); // [6]
        System.out.println("Ayu termasuk Dosen?     " + yaTidak(ayu instanceof Dosen));
    }
}

/** Pengguna Sistem Informasi Akademik (SIA) kampus. */
class Pengguna {
    private String nama;

    public Pengguna(String nama) {
        this.nama = nama;
    }

    public String getNama() {
        return nama;
    }

    public String peran() {
        return "Pengguna";
    }

    public String menuUtama() {
        return "Profil";
    }
}

class Mahasiswa extends Pengguna {
    private String nim;

    public Mahasiswa(String nama, String nim) {
        super(nama);
        this.nim = nim;
    }

    @Override
    public String peran() {
        return "Mahasiswa";
    }

    @Override
    public String menuUtama() {
        return "Profil, KRS, KHS";
    }

    public String isiKrs(int sks) { // method KHUSUS mahasiswa
        return getNama() + " (" + nim + ") mengisi KRS " + sks + " SKS";
    }
}

class Dosen extends Pengguna {
    private String nip;

    public Dosen(String nama, String nip) {
        super(nama);
        this.nip = nip;
    }

    public String getNip() {
        return nip;
    }

    @Override
    public String peran() {
        return "Dosen";
    }

    @Override
    public String menuUtama() {
        return "Profil, Input Nilai, Jadwal Mengajar";
    }

    public String inputNilai(String mataKuliah, String nilai) { // method KHUSUS dosen
        return getNama() + " memasukkan nilai " + mataKuliah + ": " + nilai;
    }
}
