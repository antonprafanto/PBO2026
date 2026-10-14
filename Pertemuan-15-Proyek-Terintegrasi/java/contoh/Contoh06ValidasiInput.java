/*
 * Contoh 06 - Validasi Input: Periksa, Tanya Ulang, Tangani Akhir Input
 * Pertemuan 15 - Proyek Terintegrasi
 *
 * Program interaktif membaca input dengan Scanner.nextLine(). Di contoh ini
 * Scanner DIGANTIKAN oleh objek MasukanPalsu yang mengambil jawaban dari
 * daftar yang sudah disiapkan. Program bisa dijalankan tanpa mengetik apa
 * pun, dan output-nya selalu sama.
 *
 * Tiga kebiasaan aman saat membaca input:
 * 1. Validasi    : periksa jawaban (kosong? angka? dalam batas? pilihan dikenal?)
 * 2. Tanya ulang : jika tidak valid, beri pesan yang jelas lalu tanya lagi
 * 3. Akhir input : nextLine() melempar NoSuchElementException jika input habis;
 *                  tangani dengan rapi
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh06ValidasiInput.java
 */
import java.util.ArrayList;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Locale;
import java.util.Map;
import java.util.NoSuchElementException;

public class Contoh06ValidasiInput {
    private static final Map<String, Integer> HARGA_TIKET = Map.of("U", 50000, "M", 25000);
    // Map.of tidak menjamin urutan. Pilihan ini akan DICETAK, jadi pakai LinkedHashMap.
    private static final Map<String, String> NAMA_KATEGORI = buatPilihanKategori();

    private static Map<String, String> buatPilihanKategori() {
        Map<String, String> pilihan = new LinkedHashMap<>();
        pilihan.put("U", "Umum");
        pilihan.put("M", "Mahasiswa");
        return pilihan;
    }

    public static void main(String[] args) {
        System.out.println("=== SKENARIO 1: PENGGUNA SALAH KETIK BEBERAPA KALI ===");
        daftarSeminar(new MasukanPalsu(List.of("", "dua", "9", "2", "x", "m")));

        System.out.println();
        System.out.println("=== SKENARIO 2: INPUT BERAKHIR DI TENGAH JALAN ===");
        try {
            daftarSeminar(new MasukanPalsu(List.of("abc")));
        } catch (NoSuchElementException e) { // [6] tangani dengan rapi, jangan biarkan crash
            System.out.println("Input berakhir. Pendaftaran dibatalkan.");
        }
    }

    /** Bertanya terus sampai jawabannya angka bulat dari minimum..maksimum. */
    static int tanyaAngka(MasukanPalsu masukan, String pertanyaan, int minimum, int maksimum) {
        while (true) { // [2] ulangi sampai jawabannya valid
            String teks = masukan.baca(pertanyaan).trim();
            if (teks.isEmpty()) {
                System.out.println("  Jawaban tidak boleh kosong.");
                continue;
            }
            int angka;
            try {
                angka = Integer.parseInt(teks); // [3] melempar NumberFormatException
            } catch (NumberFormatException e) {
                System.out.println("  '" + teks + "' bukan angka bulat.");
                continue;
            }
            if (angka < minimum || angka > maksimum) { // [4] periksa batas
                System.out.println("  Harus di antara " + minimum + " dan " + maksimum + ".");
                continue;
            }
            return angka;
        }
    }

    /** Bertanya terus sampai jawabannya salah satu kunci di pilihan. */
    static String tanyaPilihan(MasukanPalsu masukan, String pertanyaan, Map<String, String> pilihan) {
        while (true) {
            String teks = masukan.baca(pertanyaan).trim().toUpperCase(Locale.ROOT); // [5]
            if (pilihan.containsKey(teks)) {
                return teks;
            }
            System.out.println("  Pilihan tersedia: " + String.join(", ", pilihan.keySet()) + ".");
        }
    }

    static void daftarSeminar(MasukanPalsu masukan) {
        int jumlah = tanyaAngka(masukan, "Jumlah tiket (1-5): ", 1, 5);
        String kategori = tanyaPilihan(masukan, "Kategori (U=Umum, M=Mahasiswa): ", NAMA_KATEGORI);
        int total = jumlah * HARGA_TIKET.get(kategori);
        System.out.println("Pendaftaran berhasil: " + jumlah + " tiket "
                + NAMA_KATEGORI.get(kategori) + ", total Rp" + total);
    }
}

/** Pengganti Scanner: jawaban diambil dari daftar yang sudah disiapkan. */
class MasukanPalsu {
    private List<String> sisa;

    MasukanPalsu(List<String> daftarJawaban) {
        this.sisa = new ArrayList<>(daftarJawaban);
    }

    String baca(String pertanyaan) {
        if (sisa.isEmpty()) { // [1] jawaban habis = input berakhir
            System.out.println(pertanyaan + "(input habis)");
            throw new NoSuchElementException("No line found"); // sama seperti Scanner.nextLine()
        }
        String jawaban = sisa.remove(0);
        // Tampilkan pertanyaan + jawaban seolah-olah diketik pengguna.
        // Jawaban kosong ditampilkan sebagai <Enter> agar terlihat.
        System.out.println(pertanyaan + (jawaban.isEmpty() ? "<Enter>" : jawaban));
        return jawaban;
    }
}
