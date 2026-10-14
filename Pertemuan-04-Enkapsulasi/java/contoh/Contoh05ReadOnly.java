/*
 * Contoh 05 - Atribut Read-Only
 * Pertemuan 04 - Enkapsulasi
 *
 * Tidak semua data boleh diubah setelah objek dibuat. NIK di KTP tidak pernah
 * berubah, sedangkan alamat bisa berubah saat pemiliknya pindah rumah.
 *
 * - nik dan nama : hanya punya getter, TANPA setter -> read-only dari luar.
 *                  Ditambah final: kode di dalam kelas pun tidak bisa
 *                  mengubahnya lagi setelah konstruktor selesai.
 * - alamat       : punya getter DAN setter -> boleh diubah, tetapi diperiksa.
 *
 * Karena nik tidak punya setter, pemeriksaannya ditulis langsung di konstruktor.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh05ReadOnly.java
 */
public class Contoh05ReadOnly {

    public static void main(String[] args) {
        Penduduk warga = new Penduduk("1234567890123456", "Rina Wulandari",
                "Jl. Pramuka, Samarinda");
        System.out.println("=== DATA AWAL ===");
        System.out.println("NIK   : " + warga.getNik());
        System.out.println("Nama  : " + warga.getNama());
        System.out.println("Alamat: " + warga.getAlamat());

        System.out.println();
        System.out.println("=== PINDAH RUMAH ===");
        warga.setAlamat("Jl. Juanda, Samarinda"); // [4] diizinkan: alamat punya setter
        System.out.println("Alamat baru: " + warga.getAlamat());
        // warga.setNik("9999999999999999"); // [5] hapus tanda // untuk melihat error-nya

        System.out.println();
        System.out.println("=== DATA TIDAK VALID DITOLAK ===");
        try {
            warga.setAlamat("");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        try {
            new Penduduk("12345", "Doni Saputra", "Jl. Merdeka, Samarinda");
        } catch (IllegalArgumentException e) {
            System.out.println("Ditolak: " + e.getMessage());
        }
        System.out.println("Alamat " + warga.getNama() + " tetap: " + warga.getAlamat());
    }
}

/** Data kependudukan sederhana. */
class Penduduk {
    private final String nik; // [6] final: hanya boleh diisi satu kali, di konstruktor
    private final String nama;
    private String alamat;

    public Penduduk(String nik, String nama, String alamat) {
        if (nik.length() != 16) { // [1] satu-satunya kesempatan memeriksa NIK
            throw new IllegalArgumentException("NIK harus 16 digit");
        }
        this.nik = nik;
        this.nama = nama;
        setAlamat(alamat); // lewat setter alamat
    }

    public String getNik() { // [2] hanya getter, TANPA setter -> read-only
        return nik;
    }

    public String getNama() {
        return nama;
    }

    public String getAlamat() {
        return alamat;
    }

    public void setAlamat(String alamat) { // [3] alamat boleh berubah, asal tidak kosong
        if (alamat.isBlank()) {
            throw new IllegalArgumentException("Alamat tidak boleh kosong");
        }
        this.alamat = alamat;
    }
}
