/*
 * Solusi Latihan 04 - Validasi Nomor HP dan Unit Test-nya
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Ide penyelesaian:
 * - validasiNoHp() membersihkan spasi dan tanda hubung, lalu memeriksa aturan
 *   satu per satu. Setiap pelanggaran melempar IllegalArgumentException dengan
 *   pesan jelas. Jika lolos semua aturan, nomor yang sudah bersih dikembalikan.
 * - Unit test memeriksa kasus normal, kasus gagal, dan kasus BATAS (tepat 10
 *   dan tepat 13 digit), karena bug paling sering bersembunyi di batas.
 * - Runner mini sama seperti contoh 05. harusMelempar() mengembalikan
 *   exception yang tertangkap (seperti assertThrows di JUnit), sehingga
 *   pesannya bisa diperiksa juga.
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Latihan04ValidasiNoHp.java
 */
import java.util.List;

public class Latihan04ValidasiNoHp {
    private static int jumlahLulus = 0;
    private static int jumlahGagal = 0;

    /** Mengembalikan nomor HP yang sudah bersih, atau melempar IllegalArgumentException. */
    static String validasiNoHp(String teks) {
        String bersih = teks.replace(" ", "").replace("-", "");
        if (bersih.isEmpty()) {
            throw new IllegalArgumentException("Nomor HP tidak boleh kosong");
        }
        for (char huruf : bersih.toCharArray()) {
            if (huruf < '0' || huruf > '9') {
                throw new IllegalArgumentException("Nomor HP hanya boleh berisi angka");
            }
        }
        if (!bersih.startsWith("08")) {
            throw new IllegalArgumentException("Nomor HP harus diawali 08");
        }
        if (bersih.length() < 10 || bersih.length() > 13) {
            throw new IllegalArgumentException("Nomor HP harus 10 sampai 13 digit");
        }
        return bersih;
    }

    public static void main(String[] args) {
        System.out.println("=== VALIDASI NOMOR HP ===");
        for (String teks : List.of("0812-3456-7890", "0812 3456 789", "08123", "0812abc4567",
                "6281234567890", "")) {
            try {
                System.out.println("'" + teks + "' -> " + validasiNoHp(teks));
            } catch (IllegalArgumentException e) {
                System.out.println("'" + teks + "' -> ditolak: " + e.getMessage());
            }
        }

        System.out.println();
        System.out.println("=== UNIT TEST ===");
        // Urutannya sama dengan versi Python (unittest mengurutkan nama test secara abjad).
        uji("Panjang tepat 10 dan tepat 13 digit diterima", () -> {
            samakan(validasiNoHp("0812345678"), "0812345678");
            samakan(validasiNoHp("0812345678901"), "0812345678901");
        });
        uji("Spasi dan tanda hubung dibersihkan",
                () -> samakan(validasiNoHp("0812-3456 7890"), "081234567890"));
        uji("Nomor berisi huruf ditolak dengan pesan yang tepat", () -> {
            IllegalArgumentException e = harusMelempar(() -> validasiNoHp("0812abc4567"));
            samakan(e.getMessage(), "Nomor HP hanya boleh berisi angka");
        });
        uji("Nomor kosong ditolak", () -> harusMelempar(() -> validasiNoHp("   ")));
        uji("Lebih dari 13 digit ditolak",
                () -> harusMelempar(() -> validasiNoHp("08123456789012")));
        uji("Kurang dari 10 digit ditolak", () -> harusMelempar(() -> validasiNoHp("08123")));
        uji("Nomor yang tidak diawali 08 ditolak",
                () -> harusMelempar(() -> validasiNoHp("6281234567890")));
        System.out.println("Hasil: " + jumlahLulus + " lulus, " + jumlahGagal + " gagal");
    }

    // ===================== alat bantu uji (runner mini) =====================

    static void uji(String nama, Runnable kasus) {
        try {
            kasus.run();
            jumlahLulus++;
            System.out.println("[LULUS] " + nama);
        } catch (AssertionError e) {
            jumlahGagal++;
            System.out.println("[GAGAL] " + nama);
            System.out.println("        -> " + e.getMessage());
        } catch (RuntimeException e) {
            jumlahGagal++;
            System.out.println("[ERROR] " + nama);
            System.out.println("        -> " + e);
        }
    }

    /** Seperti assertEqual untuk teks. */
    static void samakan(String hasil, String harapan) {
        if (!hasil.equals(harapan)) {
            throw new AssertionError("'" + hasil + "' != '" + harapan + "'");
        }
    }

    /** Seperti assertThrows di JUnit: mengembalikan exception yang tertangkap. */
    static IllegalArgumentException harusMelempar(Runnable kode) {
        try {
            kode.run();
        } catch (IllegalArgumentException e) {
            return e;
        }
        throw new AssertionError("IllegalArgumentException not raised");
    }
}
