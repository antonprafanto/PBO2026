"""
Modul pengamat: "interface" PengamatPesanan untuk pola OBSERVER.

Pesanan (subjek) menyimpan daftar pengamat. Setiap kali status pesanan
berubah, Pesanan memanggil perbarui() milik SEMUA pengamatnya.
Pesanan tidak perlu tahu siapa saja pengamatnya: dapur, pelanggan,
layar antrean, atau apa pun yang ditambahkan kelak.
"""

from abc import ABC, abstractmethod


class PengamatPesanan(ABC):
    """Kontrak untuk objek yang ingin diberi tahu perubahan status pesanan."""

    @abstractmethod
    def perbarui(self, pesanan):
        """Dipanggil oleh Pesanan setiap kali statusnya berubah.

        Parameter pesanan sengaja tidak diberi type hint, agar modul ini
        tidak perlu meng-import pesanan.py (mencegah circular import).
        """
