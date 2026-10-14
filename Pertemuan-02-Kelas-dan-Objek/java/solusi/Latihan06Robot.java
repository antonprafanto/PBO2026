/*
 * Solusi Latihan 06 - Robot Penjelajah
 * Pertemuan 02 - Kelas dan Objek
 *
 * Ide penyelesaian:
 * - Simpan arah sebagai indeks ke array ARAH {"Utara", "Timur", "Selatan", "Barat"}.
 *   Belok kanan: (indeks + 1) % 4. Belok kiri: (indeks + 3) % 4, sama dengan
 *   mundur 1. Hindari (indeks - 1) % 4: di Java hasilnya -1 jika indeks 0.
 * - maju() mengubah x atau y sesuai arah saat ini.
 * - jalankan(perintah) membaca huruf satu per satu lalu memanggil method lain
 *   milik objek yang sama (maju(), belokKanan(), ...).
 *
 * Cara menjalankan dari folder java/solusi (Java 11 ke atas):
 *     java Latihan06Robot.java
 */
public class Latihan06Robot {

    public static void main(String[] args) {
        Robot robi = new Robot("Robi");
        System.out.println("Posisi awal: " + robi.posisi());
        robi.jalankan("MMRMM");
        robi.jalankan("LLMX");
    }
}

/** Robot di bidang koordinat. Mulai di (0, 0) menghadap Utara. */
class Robot {
    // static final = konstanta milik kelas, dipakai bersama oleh semua objek Robot
    // dan tidak diubah. Kata static dibahas tuntas di Pertemuan 03.
    static final String[] ARAH = {"Utara", "Timur", "Selatan", "Barat"};

    String nama;
    int x;
    int y;
    int indeksArah;

    Robot(String nama) {
        this.nama = nama;
        this.x = 0;
        this.y = 0;
        this.indeksArah = 0; // 0 = Utara
    }

    void belokKanan() {
        indeksArah = (indeksArah + 1) % 4;
    }

    void belokKiri() {
        indeksArah = (indeksArah + 3) % 4; // sama dengan mundur 1
    }

    void maju() {
        String arah = ARAH[indeksArah];
        // Teks (String) dibandingkan dengan equals(), bukan dengan ==.
        if (arah.equals("Utara")) {
            y = y + 1;
        } else if (arah.equals("Timur")) {
            x = x + 1;
        } else if (arah.equals("Selatan")) {
            y = y - 1;
        } else {
            x = x - 1;
        }
    }

    String posisi() {
        return "(" + x + ", " + y + ") menghadap " + ARAH[indeksArah];
    }

    void jalankan(String perintah) {
        System.out.println(nama + " menjalankan perintah '" + perintah + "'");
        // toCharArray() memecah teks menjadi huruf-huruf (tipe char).
        // Satu huruf ditulis dengan tanda kutip tunggal, misalnya 'M',
        // dan boleh dibandingkan dengan ==.
        for (char huruf : perintah.toCharArray()) {
            if (huruf == 'M') {
                maju();
            } else if (huruf == 'R') {
                belokKanan();
            } else if (huruf == 'L') {
                belokKiri();
            } else {
                System.out.println("  Perintah '" + huruf + "' tidak dikenal, dilewati");
            }
        }
        System.out.println("  Posisi sekarang: " + posisi());
    }
}
