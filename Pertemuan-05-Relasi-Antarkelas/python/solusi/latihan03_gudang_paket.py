"""
Solusi Latihan 03 - Gudang Paket dan Kurir
Pertemuan 05 - Relasi Antarkelas

Relasi yang dipakai:
- Gudang o-- Paket  : agregasi (paket datang dari luar lalu diterima gudang)
- Paket --> Kurir   : asosiasi 0..1 (paket baru belum punya kurir = None)

Ide penyelesaian:
- cari_paket() mengembalikan objek Paket, atau None jika resi tidak ada.
  tugaskan_kurir() WAJIB memeriksa None sebelum memakai hasilnya.
- Menghitung paket milik seorang kurir: bandingkan referensinya dengan
  operator is (objek kurir yang SAMA, bukan sekadar nama yang sama).

Cara menjalankan:
    python latihan03_gudang_paket.py
"""


class Kurir:
    """Kurir pengantar paket."""

    def __init__(self, nama: str):
        self._nama = nama

    @property
    def nama(self) -> str:
        return self._nama


class Paket:
    """Paket kiriman. Kurirnya boleh belum ditentukan (0..1)."""

    def __init__(self, resi: str, tujuan: str, berat_kg: int):
        self._resi = resi
        self._tujuan = tujuan
        self._berat_kg = berat_kg
        self._kurir: Kurir | None = None  # belum ada kurir

    @property
    def resi(self) -> str:
        return self._resi

    @property
    def kurir(self) -> Kurir | None:
        return self._kurir

    def tugaskan(self, kurir: Kurir):
        self._kurir = kurir

    def __str__(self) -> str:
        if self._kurir is None:
            nama_kurir = "belum ada"
        else:
            nama_kurir = self._kurir.nama
        return (f"{self._resi} ke {self._tujuan}, {self._berat_kg} kg"
                f" - kurir: {nama_kurir}")


class Gudang:
    """Gudang yang menampung paket-paket sebelum diantar."""

    def __init__(self, nama: str):
        self._nama = nama
        self._daftar_paket: list[Paket] = []

    def terima(self, paket: Paket):
        self._daftar_paket.append(paket)

    def cari_paket(self, resi: str) -> Paket | None:
        for paket in self._daftar_paket:
            if paket.resi == resi:
                return paket
        return None

    def tugaskan_kurir(self, resi: str, kurir: Kurir):
        paket = self.cari_paket(resi)
        if paket is None:  # periksa dulu, jangan langsung dipakai
            print(f"Gagal: paket {resi} tidak ditemukan")
            return
        paket.tugaskan(kurir)
        print(f"{resi} diantar oleh {kurir.nama}")

    def jumlah_paket_kurir(self, kurir: Kurir) -> int:
        jumlah = 0
        for paket in self._daftar_paket:
            if paket.kurir is kurir:  # objek kurir yang sama
                jumlah += 1
        return jumlah

    def tampilkan(self):
        print(f"{self._nama} ({len(self._daftar_paket)} paket):")
        for paket in self._daftar_paket:
            print(f"- {paket}")


def main():
    gudang = Gudang("Gudang Samarinda")
    gudang.terima(Paket("SMD001", "Jl. Juanda", 2))
    gudang.terima(Paket("SMD002", "Jl. Pahlawan", 5))
    gudang.terima(Paket("SMD003", "Jl. Antasari", 1))
    joko = Kurir("Joko")
    wawan = Kurir("Wawan")

    print("=== PAKET MASUK ===")
    gudang.tampilkan()

    print()
    print("=== PENUGASAN KURIR ===")
    gudang.tugaskan_kurir("SMD001", joko)
    gudang.tugaskan_kurir("SMD003", joko)
    gudang.tugaskan_kurir("SMD009", wawan)
    gudang.tugaskan_kurir("SMD002", wawan)

    print()
    print("=== STATUS AKHIR ===")
    gudang.tampilkan()
    print(f"Paket yang dibawa {joko.nama}: {gudang.jumlah_paket_kurir(joko)}")
    print(f"Paket yang dibawa {wawan.nama}: {gudang.jumlah_paket_kurir(wawan)}")


if __name__ == "__main__":
    main()
