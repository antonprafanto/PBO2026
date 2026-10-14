"""
Contoh 07 - Objek sebagai Parameter
Pertemuan 03 - Atribut dan Method Lebih Dalam

Saat sebuah objek dikirim ke method atau fungsi, yang dikirim adalah
REFERENSI-nya, bukan salinan objeknya. Karena itu method bisa MENGUBAH objek
tersebut, dan perubahannya tetap terlihat setelah method selesai.
Bandingkan dengan mengirim angka biasa.

Cara menjalankan:
    python contoh07_objek_sebagai_parameter.py
"""


class DompetDigital:
    """Dompet digital (e-wallet) dengan saldo dalam rupiah."""

    def __init__(self, pemilik, saldo):
        self.pemilik = pemilik
        self.saldo = saldo

    def saldo_cukup(self, jumlah):  # [1] method boolean: jawabannya ya atau tidak
        return self.saldo >= jumlah

    def transfer(self, tujuan, jumlah):  # [2] tujuan berisi objek DompetDigital lain
        if not self.saldo_cukup(jumlah):
            print(f"Transfer gagal: saldo {self.pemilik} tidak cukup")
            return
        self.saldo = self.saldo - jumlah
        tujuan.saldo = tujuan.saldo + jumlah  # [3] mengubah objek yang dikirim
        print(f"{self.pemilik} transfer Rp{jumlah} ke {tujuan.pemilik}")


def tambah_bonus_angka(saldo):  # [4] menerima ANGKA
    saldo = saldo + 5000  # hanya mengubah variabel milik fungsi ini
    print(f"  (di dalam: Rp{saldo})")


def tambah_bonus_dompet(dompet):  # [5] menerima OBJEK
    dompet.saldo = dompet.saldo + 5000  # mengubah objek milik pemanggil
    print(f"  (di dalam: Rp{dompet.saldo})")


def main():
    dompet_budi = DompetDigital("Budi", 100000)
    dompet_siti = DompetDigital("Siti", 20000)

    print("=== TRANSFER ANTARDOMPET ===")
    dompet_budi.transfer(dompet_siti, 30000)  # [6] objek dompet_siti dikirim
    dompet_siti.transfer(dompet_budi, 75000)
    print(f"Saldo Budi: Rp{dompet_budi.saldo}")
    print(f"Saldo Siti: Rp{dompet_siti.saldo}")

    print()
    print("=== MENGIRIM ANGKA vs MENGIRIM OBJEK ===")
    saldo_tunai = 10000
    tambah_bonus_angka(saldo_tunai)
    print(f"Saldo tunai sesudahnya      : Rp{saldo_tunai}")  # [7] tidak berubah
    tambah_bonus_dompet(dompet_siti)
    print(f"Saldo dompet Siti sesudahnya: Rp{dompet_siti.saldo}")  # [8] berubah


if __name__ == "__main__":
    main()
