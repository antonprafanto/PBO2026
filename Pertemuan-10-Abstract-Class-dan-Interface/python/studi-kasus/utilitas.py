"""
Modul utilitas KedaiKita: fungsi-fungsi bantu yang dipakai banyak kelas.
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")
