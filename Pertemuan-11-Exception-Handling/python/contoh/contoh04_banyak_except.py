"""
Contoh 04 - Banyak except dan Urutannya
Pertemuan 11 - Exception Handling

Satu blok try boleh punya beberapa except. Python memeriksanya dari ATAS ke
BAWAH dan menjalankan except PERTAMA yang cocok. Karena itu:
- except yang paling SPESIFIK ditulis paling atas,
- except yang paling UMUM (Exception) ditulis paling bawah.

Satu except juga boleh menangkap beberapa jenis sekaligus dengan tuple:
    except (ValueError, IndexError):

Setiap baris data berformat "nama;total_nilai;jumlah_tugas".

Cara menjalankan:
    python contoh04_banyak_except.py
"""


def hitung_rata_rata(baris: str) -> int:
    """Menghitung rata-rata nilai tugas dari satu baris data."""
    bagian = baris.split(";")
    total = int(bagian[1])  # [1] IndexError atau ValueError
    jumlah_tugas = int(bagian[2])
    return total // jumlah_tugas  # [2] ZeroDivisionError jika belum ada tugas


def main():
    data = [
        "Ayu;255;3",
        "Bima;sembilan puluh;1",  # nilai bukan angka
        "Citra;160",  # kolom jumlah_tugas tidak ada
        "Dimas;0;0",  # belum ada tugas yang dinilai
        None,  # data kosong dari sistem lama
        "Eka;176;2",
    ]
    print("=== RATA-RATA NILAI TUGAS ===")
    for nomor, baris in enumerate(data, start=1):
        try:
            rata = hitung_rata_rata(baris)
            nama = baris.split(";")[0]
            print(f"Baris {nomor} ({nama}): rata-rata {rata}")
        except (ValueError, IndexError):  # [3] dua jenis, satu penanganan
            print(f"Baris {nomor}: format salah, dilewati")
        except ZeroDivisionError:  # [4]
            print(f"Baris {nomor}: belum ada tugas yang dinilai")
        except Exception:  # [5] jaring pengaman: PALING UMUM, PALING BAWAH
            print(f"Baris {nomor}: data tidak terbaca, dilewati")


if __name__ == "__main__":
    main()
