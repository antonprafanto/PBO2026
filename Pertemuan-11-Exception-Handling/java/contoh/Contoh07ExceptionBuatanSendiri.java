/*
 * Contoh 07 - Exception Buatan Sendiri dan Exception Chaining
 * Pertemuan 11 - Exception Handling
 *
 * Exception hanyalah KELAS. Kita bisa membuat jenis baru dengan PEWARISAN:
 *
 *     Exception                      (bawaan Java)
 *     +-- RekeningException          (induk semua error rekening)
 *         +-- SaldoTidakCukupException   (membawa data: saldo, diminta, kekurangan)
 *         +-- TransferGagalException
 *
 * - Penangkap boleh memilih: tangkap yang spesifik, atau tangkap induknya.
 * - Exception boleh membawa DATA TAMBAHAN, bukan hanya pesan.
 * - new TransferGagalException(pesan, e) (exception chaining) membuat
 *   exception baru sambil menyimpan exception lama sebagai PENYEBAB-nya
 *   (diambil kembali dengan getCause()).
 *
 * Karena RekeningException turunan Exception (bukan RuntimeException),
 * semuanya termasuk CHECKED exception: method yang melemparnya wajib menulis
 * "throws" (dibahas tuntas di Contoh 08).
 *
 * Cara menjalankan (Java 11 ke atas):
 *     java Contoh07ExceptionBuatanSendiri.java
 */
public class Contoh07ExceptionBuatanSendiri {

    static void transfer(Rekening asal, Rekening tujuan, int jumlah)
            throws TransferGagalException {
        try {
            asal.tarik(jumlah);
        } catch (SaldoTidakCukupException e) {
            String pesan = "Transfer " + asal.getPemilik() + " ke " + tujuan.getPemilik()
                    + " gagal";
            throw new TransferGagalException(pesan, e); // [6] simpan penyebab aslinya
        }
        tujuan.setor(jumlah);
        System.out.println("Transfer Rp" + jumlah + " dari " + asal.getPemilik()
                + " ke " + tujuan.getPemilik() + " berhasil");
    }

    public static void main(String[] args) {
        Rekening budi = new Rekening("Budi", 500000);
        Rekening siti = new Rekening("Siti", 100000);

        System.out.println("=== TARIK TUNAI ===");
        int[] daftarJumlah = {200000, 400000};
        for (int jumlah : daftarJumlah) {
            try {
                budi.tarik(jumlah);
                System.out.println("Tarik Rp" + jumlah + " berhasil, sisa saldo Rp"
                        + budi.getSaldo());
            } catch (SaldoTidakCukupException e) { // [7] tangkap yang spesifik
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Kurang Rp" + e.getKekurangan()
                        + ". Coba tarik paling banyak Rp" + e.getSaldo() + "."); // [8]
            }
        }

        System.out.println();
        System.out.println("=== TRANSFER ===");
        Rekening[] daftarAsal = {budi, siti};
        Rekening[] daftarTujuan = {siti, budi};
        int[] daftarNominal = {50000, 250000};
        for (int i = 0; i < daftarAsal.length; i++) {
            try {
                transfer(daftarAsal[i], daftarTujuan[i], daftarNominal[i]);
            } catch (RekeningException e) { // [9] tangkap induknya: semua error rekening
                System.out.println("Gagal: " + e.getMessage());
                System.out.println("  Penyebab: " + e.getCause().getMessage()); // [10]
            }
        }

        System.out.println();
        System.out.println("Saldo akhir: Budi Rp" + budi.getSaldo()
                + ", Siti Rp" + siti.getSaldo());
    }
}

/** Induk semua error yang berhubungan dengan rekening. */
class RekeningException extends Exception { // [1] turunan Exception
    // Nomor versi untuk serialisasi; dianjurkan ada di setiap kelas exception.
    private static final long serialVersionUID = 1L;

    public RekeningException(String pesan) {
        super(pesan);
    }

    public RekeningException(String pesan, Throwable penyebab) {
        super(pesan, penyebab); // pesan + exception lama yang menjadi penyebab
    }
}

/** Dilempar saat saldo tidak cukup untuk penarikan. */
class SaldoTidakCukupException extends RekeningException { // [2] turunan RekeningException
    private static final long serialVersionUID = 1L;

    private int saldo; // [4] data tambahan untuk penangkap
    private int diminta;

    public SaldoTidakCukupException(int saldo, int diminta) {
        super("Saldo tidak cukup: saldo Rp" + saldo + ", diminta Rp" + diminta); // [3]
        this.saldo = saldo;
        this.diminta = diminta;
    }

    public int getSaldo() {
        return saldo;
    }

    public int getDiminta() {
        return diminta;
    }

    public int getKekurangan() {
        return diminta - saldo;
    }
}

/** Dilempar saat transfer tidak bisa diselesaikan. */
class TransferGagalException extends RekeningException {
    private static final long serialVersionUID = 1L;

    public TransferGagalException(String pesan, Throwable penyebab) {
        super(pesan, penyebab);
    }
}

/** Rekening tabungan sederhana. */
class Rekening {
    private String pemilik;
    private int saldo;

    public Rekening(String pemilik, int saldo) {
        this.pemilik = pemilik;
        this.saldo = saldo;
    }

    public String getPemilik() {
        return pemilik;
    }

    public int getSaldo() {
        return saldo;
    }

    public void tarik(int jumlah) throws SaldoTidakCukupException {
        if (jumlah > saldo) {
            throw new SaldoTidakCukupException(saldo, jumlah); // [5]
        }
        saldo -= jumlah;
    }

    public void setor(int jumlah) {
        saldo += jumlah;
    }
}
