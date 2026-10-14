"""
Contoh 05 - Representasi Teks Objek dengan __str__
Pertemuan 03 - Atribut dan Method Lebih Dalam

Tanpa __str__, print(objek) hanya menampilkan sesuatu seperti
<__main__.Motor object at 0x7f...> yang tidak berguna bagi pembaca.
Dengan __str__, kita sendiri yang menentukan teks yang tampil.

Cara menjalankan:
    python contoh05_str.py
"""


class Motor:
    """Motor mahasiswa yang terdaftar di parkiran kampus."""

    def __init__(self, plat, merek, warna):
        self.plat = plat
        self.merek = merek
        self.warna = warna

    def __str__(self):  # [1] dipanggil otomatis oleh print(), str(), dan f-string
        return f"{self.plat} - {self.merek} ({self.warna})"  # [2] return, bukan print


def main():
    motor_budi = Motor("KT 1234 AB", "Honda Beat", "merah")
    motor_siti = Motor("KT 5678 CD", "Yamaha NMAX", "hitam")

    print("=== MENCETAK OBJEK LANGSUNG ===")
    print(motor_budi)  # [3] print() memanggil motor_budi.__str__()
    print(motor_siti)

    print()
    print("=== DIPAKAI DI DALAM TEKS LAIN ===")
    print(f"Motor Budi: {motor_budi}")  # [4] f-string juga memanggil __str__
    teks = str(motor_siti)  # [5] str() menghasilkan teksnya untuk disimpan
    print(f"Teks motor Siti terdiri atas {len(teks)} karakter")

    print()
    print("=== SETELAH WARNA DIUBAH ===")
    motor_budi.warna = "biru"
    print(motor_budi)  # [6] teks selalu mengikuti nilai atribut terbaru


if __name__ == "__main__":
    main()
