/*
 * Contoh 07 - Kapan Dua Objek Dianggap Sama? (equals dan hashCode)
 * Pertemuan 12 - Koleksi dan Generics
 *
 * - Tanpa override, equals() bawaan Object hanya bernilai true untuk objek
 *   yang sama persis (sama seperti ==).
 * - Dengan equals() + hashCode() berdasarkan NIK, dua objek yang NIK-nya sama
 *   dianggap sama. Akibatnya HashSet bisa membuang data ganda, dan HashMap
 *   bisa dicari memakai objek lain yang NIK-nya sama.
 * - Kontrak wajib: objek yang equals() harus punya hashCode() yang SAMA.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07EqualsHashCode.java
 */
import java.util.ArrayList;
import java.util.Comparator;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

public class Contoh07EqualsHashCode {

    static String yaTidak(boolean nilai) {
        return nilai ? "ya" : "tidak";
    }

    public static void main(String[] args) {
        System.out.println("=== VERSI A: TANPA ATURAN KESAMAAN ===");
        PemilihPolos a1 = new PemilihPolos("6472010000000001", "Budi Santoso");
        PemilihPolos a2 = new PemilihPolos("6472010000000001", "Budi Santoso"); // diinput ulang
        System.out.println("Dianggap sama     : " + yaTidak(a1.equals(a2))); // [3]
        Set<PemilihPolos> setA = new HashSet<>(List.of(a1, a2));
        System.out.println("Isi set           : " + setA.size() + " pemilih");

        System.out.println();
        System.out.println("=== VERSI B: SAMA JIKA NIK SAMA ===");
        Pemilih b1 = new Pemilih("6472010000000001", "Budi Santoso");
        Pemilih b2 = new Pemilih("6472010000000001", "Budi Santosa"); // salah ketik nama
        Pemilih b3 = new Pemilih("6472010000000002", "Siti Aminah");
        System.out.println("Dianggap sama     : " + yaTidak(b1.equals(b2))); // [4]
        System.out.println("Objek sama persis : " + yaTidak(b1 == b2));
        System.out.println("Kode hash sama    : " + yaTidak(b1.hashCode() == b2.hashCode()));
        Set<Pemilih> dpt = new HashSet<>(); // DPT = daftar pemilih tetap
        dpt.add(b1);
        dpt.add(b2); // [5] NIK sudah ada: diabaikan (add mengembalikan false)
        dpt.add(b3);
        System.out.println("Isi set           : " + dpt.size() + " pemilih");
        List<Pemilih> urut = new ArrayList<>(dpt); // urutkan dulu sebelum dicetak
        urut.sort(Comparator.comparing(Pemilih::getNik));
        for (Pemilih pemilih : urut) {
            System.out.println("  " + pemilih.getNik() + " " + pemilih.getNama());
        }

        System.out.println();
        System.out.println("=== MENCARI DENGAN OBJEK LAIN YANG NIK-NYA SAMA ===");
        Map<Pemilih, String> tps = new HashMap<>(); // [6] objek sebagai kunci
        tps.put(b1, "TPS 05");
        tps.put(b3, "TPS 12");
        Pemilih pencari = new Pemilih("6472010000000002", "Siti A."); // NIK milik Siti
        System.out.println("Terdaftar di DPT  : " + yaTidak(dpt.contains(pencari))); // [7]
        System.out.println("Lokasi TPS        : " + tps.get(pencari));
    }
}

/** Versi A: tanpa equals() dan hashCode() (memakai bawaan dari Object). */
class PemilihPolos {
    private String nik;
    private String nama;

    public PemilihPolos(String nik, String nama) {
        this.nik = nik;
        this.nama = nama;
    }
}

/** Versi B: dua pemilih dianggap sama jika NIK-nya sama. */
class Pemilih {
    private String nik;
    private String nama;

    public Pemilih(String nik, String nama) {
        this.nik = nik;
        this.nama = nama;
    }

    public String getNik() {
        return nik;
    }

    public String getNama() {
        return nama;
    }

    @Override
    public boolean equals(Object lain) { // [1] parameternya WAJIB bertipe Object
        if (!(lain instanceof Pemilih)) {
            return false; // bukan Pemilih (atau null): pasti tidak sama
        }
        Pemilih pemilihLain = (Pemilih) lain;
        return nik.equals(pemilihLain.nik);
    }

    @Override
    public int hashCode() { // [2] hash dari data yang SAMA dengan equals()
        return nik.hashCode();
    }
}
