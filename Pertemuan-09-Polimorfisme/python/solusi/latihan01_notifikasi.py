"""
Solusi Latihan 01 - Notifikasi Kampus
Pertemuan 09 - Polimorfisme

Ide penyelesaian:
- Kelas induk Notifikasi punya dua method: kirim(pesan) dan biaya().
- NotifEmail, NotifSMS, dan NotifWhatsApp meng-override kirim() dengan
  format masing-masing. Hanya NotifSMS yang meng-override biaya(); kelas
  lain memakai versi induk (biaya 0).
- Program utama cukup memanggil notif.kirim(pesan) dan notif.biaya() untuk
  SEMUA objek di list, tanpa if-elif berdasarkan jenis (polimorfisme).

Cara menjalankan:
    python latihan01_notifikasi.py
"""

PANJANG_MAKS_SMS = 20


class Notifikasi:
    """Kelas induk semua jenis notifikasi."""

    def __init__(self, tujuan: str):
        self._tujuan = tujuan

    @property
    def tujuan(self) -> str:
        return self._tujuan

    def kirim(self, pesan: str) -> str:
        return f"[UMUM] Kepada {self._tujuan}: {pesan}"

    def biaya(self) -> int:
        return 0  # bawaan: gratis


class NotifEmail(Notifikasi):
    def kirim(self, pesan: str) -> str:
        return f"[EMAIL] Kepada {self._tujuan}: {pesan}"


class NotifSMS(Notifikasi):
    def kirim(self, pesan: str) -> str:
        if len(pesan) > PANJANG_MAKS_SMS:
            pesan = pesan[:PANJANG_MAKS_SMS] + "..."  # potong pesan yang panjang
        return f"[SMS] Kepada {self._tujuan}: {pesan}"

    def biaya(self) -> int:  # satu-satunya kelas yang meng-override biaya()
        return 150


class NotifWhatsApp(Notifikasi):
    def kirim(self, pesan: str) -> str:
        return f"[WA] Kepada {self._tujuan}: *PENGUMUMAN* {pesan}"


def main():
    daftar_notif = [
        NotifEmail("ayu@kampus.ac.id"),
        NotifSMS("081234567890"),
        NotifWhatsApp("082198765432"),
    ]
    daftar_pesan = ["Kuliah PBO pindah ke Ruang D-201", "Kuis besok jam 8"]

    total_biaya = 0
    for pesan in daftar_pesan:
        print(f"=== KIRIM: {pesan} ===")
        for notif in daftar_notif:
            print(notif.kirim(pesan))  # versi kirim() milik objek sebenarnya
            total_biaya += notif.biaya()
        print()
    print(f"Total biaya pengiriman: Rp{total_biaya}")


if __name__ == "__main__":
    main()
