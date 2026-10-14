"""
Modul dapat_dicetak: "interface" DapatDicetak.

Python tidak punya kata kunci interface seperti Java. Cara yang lazim adalah
membuat kelas abstrak (turunan ABC) yang SEMUA method-nya abstrak.
Kelas apa pun yang mewarisinya WAJIB menyediakan method cetak().
"""

from abc import ABC, abstractmethod


class DapatDicetak(ABC):
    """Kontrak: objek ini bisa dicetak ke layar."""

    @abstractmethod
    def cetak(self):
        """Mencetak isi objek ke layar."""
