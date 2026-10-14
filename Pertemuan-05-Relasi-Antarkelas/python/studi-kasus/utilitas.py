"""
Modul utilitas KedaiKita: fungsi-fungsi bantu yang dipakai banyak kelas.

File ini hanya berisi fungsi, jadi tidak mencetak apa-apa jika dijalankan
sendiri. Jalankan main.py dari folder studi-kasus.
"""


def format_rupiah(angka: int) -> str:
    """Mengubah 18000 menjadi 'Rp18.000'."""
    return f"Rp{angka:,}".replace(",", ".")
