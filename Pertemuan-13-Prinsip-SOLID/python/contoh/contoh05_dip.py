"""
Contoh 05 - DIP: Bergantung pada Abstraksi, Bukan pada Kelas Konkret
Pertemuan 13 - Prinsip SOLID

Versi MELANGGAR: PengingatKaku membuat sendiri objek SmsGateway di dalam
konstruktornya. Ia terkunci ke SMS selamanya.

Versi SESUAI DIP: PengingatJadwal hanya mengenal abstraksi Pengirim.
Objek pengirim yang konkret "disuntikkan" dari luar lewat konstruktor
(dependency injection). Kelas yang sama bisa memakai SMS, WhatsApp, atau
pengirim tiruan untuk pengujian, tanpa diubah sedikit pun.

Cara menjalankan:
    python contoh05_dip.py
"""

from abc import ABC, abstractmethod


# ------------------------------------------------------------ MELANGGAR DIP
class SmsGateway:
    def kirim_sms(self, nomor: str, pesan: str):
        print(f"  [SMS ke {nomor}] {pesan}")


class PengingatKaku:
    def __init__(self):
        self._sms = SmsGateway()  # [1] membuat sendiri kelas konkret: terkunci

    def ingatkan(self, nomor: str, matkul: str, jam: str):
        self._sms.kirim_sms(nomor, f"Besok kuliah {matkul} jam {jam}")


# -------------------------------------------------------------- SESUAI DIP
class Pengirim(ABC):
    """Abstraksi: apa pun yang bisa mengirim pesan."""

    @abstractmethod
    def kirim(self, tujuan: str, pesan: str):
        """Mengirim satu pesan ke tujuan."""


class PengirimSms(Pengirim):
    def kirim(self, tujuan: str, pesan: str):
        print(f"  [SMS ke {tujuan}] {pesan}")


class PengirimWhatsApp(Pengirim):
    def kirim(self, tujuan: str, pesan: str):
        print(f"  [WA ke {tujuan}] {pesan}")


class PengirimTiruan(Pengirim):
    """Pengirim pura-pura untuk pengujian: tidak mengirim, hanya mencatat."""

    def __init__(self):
        self._catatan: list[str] = []

    @property
    def catatan(self) -> list[str]:
        return list(self._catatan)

    def kirim(self, tujuan: str, pesan: str):
        self._catatan.append(f"{tujuan}: {pesan}")


class PengingatJadwal:
    def __init__(self, pengirim: Pengirim):  # [2] disuntikkan dari luar
        self._pengirim = pengirim  # [3] tipenya abstraksi, bukan kelas konkret

    def ingatkan(self, nomor: str, matkul: str, jam: str):
        self._pengirim.kirim(nomor, f"Besok kuliah {matkul} jam {jam}")


def main():
    print("=== VERSI MELANGGAR DIP ===")
    PengingatKaku().ingatkan("081234567890", "PBO", "08.00")
    print("Mau pindah ke WhatsApp? Kelas PengingatKaku harus dibongkar.")

    print()
    print("=== VERSI SESUAI DIP ===")
    print("Disuntik PengirimSms:")
    PengingatJadwal(PengirimSms()).ingatkan("081234567890", "PBO", "08.00")  # [4]
    print("Disuntik PengirimWhatsApp:")
    PengingatJadwal(PengirimWhatsApp()).ingatkan("081234567890", "PBO", "08.00")

    print("Disuntik PengirimTiruan (untuk pengujian):")
    tiruan = PengirimTiruan()
    pengingat = PengingatJadwal(tiruan)
    pengingat.ingatkan("081234567890", "PBO", "08.00")
    pengingat.ingatkan("082198765432", "Basis Data", "10.00")
    catatan = tiruan.catatan  # [5] memeriksa hasil tanpa mengirim pesan sungguhan
    print(f"  Pesan tercatat: {len(catatan)}")
    print(f"  Pesan kedua   : {catatan[1]}")
    sesuai = catatan[1] == "082198765432: Besok kuliah Basis Data jam 10.00"
    print(f"  Sesuai harapan? {'ya' if sesuai else 'tidak'}")


if __name__ == "__main__":
    main()
