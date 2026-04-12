"""
============================================================
    MATERI 03 - Atribut dan Method
    File: 01_atribut_instance_vs_kelas.py
    Topik: Perbedaan Atribut Instance dan Atribut Kelas
============================================================
"""

# ?????????????????????????????????????????????????????????
# BAGIAN 1: Atribut Instance
# Atribut yang didefinisikan via `self.xxx` di dalam __init__
# Setiap objek punya NILAI SENDIRI yang independen
# ?????????????????????????????????????????????????????????

print("=" * 55)
print("  1. ATRIBUT INSTANCE")
print("=" * 55)


class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        # Semua atribut di bawah adalah ATRIBUT INSTANCE
        self.nama = nama
        self.nim  = nim
        self.ipk  = ipk


budi  = Mahasiswa("Budi Santoso",  "2301001", 3.75)
sari  = Mahasiswa("Sari Dewi",     "2301002", 3.50)
andi  = Mahasiswa("Andi Wijaya",   "2301003", 3.20)

print(f"Nama Budi : {budi.nama}  | IPK: {budi.ipk}")
print(f"Nama Sari : {sari.nama}  | IPK: {sari.ipk}")
print(f"Nama Andi : {andi.nama} | IPK: {andi.ipk}")

# Ubah atribut instance satu objek -> tidak mempengaruhi yang lain
budi.ipk = 3.90
print(f"\nSetelah budi.ipk diubah ke 3.90:")
print(f"  budi.ipk  = {budi.ipk}")   # berubah
print(f"  sari.ipk  = {sari.ipk}")   # tetap
print(f"  andi.ipk  = {andi.ipk}")   # tetap


# ?????????????????????????????????????????????????????????
# BAGIAN 2: Atribut Kelas
# Didefinisikan di LUAR __init__, langsung di badan kelas
# Dibagi ke SEMUA objek; diubah via `NamaKelas.atribut`
# ?????????????????????????????????????????????????????????

print("\n" + "=" * 55)
print("  2. ATRIBUT KELAS")
print("=" * 55)


class MahasiswaV2:
    # ?? Atribut Kelas ?????????????????????????????
    universitas   = "Universitas Mulawarman"
    program_studi = "Informatika"
    jumlah_mhs    = 0    # counter objek yang dibuat

    def __init__(self, nama, nim, ipk):
        self.nama = nama
        self.nim  = nim
        self.ipk  = ipk
        MahasiswaV2.jumlah_mhs += 1  # update counter setiap ada objek baru


mhs1 = MahasiswaV2("Budi", "2301001", 3.75)
mhs2 = MahasiswaV2("Sari", "2301002", 3.50)
mhs3 = MahasiswaV2("Andi", "2301003", 3.20)

# Akses atribut kelas - via nama kelas (DIREKOMENDASIKAN)
print(f"Universitas   : {MahasiswaV2.universitas}")
print(f"Program Studi : {MahasiswaV2.program_studi}")
print(f"Total mahasiswa: {MahasiswaV2.jumlah_mhs}")

# Akses via objek - boleh untuk MEMBACA, tapi jangan untuk MENGUBAH
print(f"\nAkses via objek -> mhs1.universitas = '{mhs1.universitas}'")


# ?????????????????????????????????????????????????????????
# BAGIAN 3: Jebakan! Mengubah atribut kelas via objek
# ?????????????????????????????????????????????????????????

print("\n" + "=" * 55)
print("  3. JEBAKAN: Ubah Atribut Kelas via Objek")
print("=" * 55)

# [x] JANGAN lakukan ini jika maksudnya mengubah atribut KELAS
mhs1.universitas = "Universitas Lain"   # membuat atribut INSTANCE baru!

print(f"mhs1.universitas  = '{mhs1.universitas}'")       # "Universitas Lain" <- shadowed
print(f"mhs2.universitas  = '{mhs2.universitas}'")       # tetap "Universitas Mulawarman"
print(f"MahasiswaV2.universitas = '{MahasiswaV2.universitas}'")  # kelas tidak berubah!

# [OK] Cara BENAR mengubah atribut kelas:
MahasiswaV2.universitas = "Universitas Mulawarman (Updated)"
print(f"\nSetelah diubah via kelas:")
print(f"MahasiswaV2.universitas = '{MahasiswaV2.universitas}'")
# mhs1 tetap punya "shadow" instance attr-nya sendiri:
print(f"mhs1.universitas (masih shadow) = '{mhs1.universitas}'")
print(f"mhs2.universitas = '{mhs2.universitas}'")  # mengikuti perubahan kelas


# ?????????????????????????????????????????????????????????
# BAGIAN 4: Kasus Nyata - Menggunakan Atribut Kelas
# Contoh: tracking jumlah, konstanta bersama
# ?????????????????????????????????????????????????????????

print("\n" + "=" * 55)
print("  4. KASUS NYATA: Atribut Kelas")
print("=" * 55)


class Produk:
    # Konstanta yang berlaku untuk semua produk
    PAJAK_PERSEN  = 11     # PPN 11%
    DISKON_MEMBER = 10     # diskon anggota 10%
    _jumlah_produk = 0

    def __init__(self, nama, harga_dasar):
        self.nama        = nama
        self.harga_dasar = harga_dasar
        Produk._jumlah_produk += 1

    def harga_dengan_pajak(self):
        return self.harga_dasar * (1 + Produk.PAJAK_PERSEN / 100)

    def harga_member(self):
        harga = self.harga_dengan_pajak()
        return harga * (1 - Produk.DISKON_MEMBER / 100)

    @classmethod
    def total_produk(cls):
        return cls._jumlah_produk


laptop = Produk("Laptop ASUS",       8_500_000)
mouse  = Produk("Mouse Logitech",      150_000)
kboard = Produk("Keyboard Mechanical", 350_000)

print(f"Total produk terdaftar: {Produk.total_produk()}")
print(f"\n{'Produk':<25} {'Harga Dasar':>15} {'+ Pajak':>15} {'Harga Member':>15}")
print("-" * 72)
for p in [laptop, mouse, kboard]:
    print(f"{p.nama:<25} Rp {p.harga_dasar:>12,.0f} "
          f"Rp {p.harga_dengan_pajak():>12,.0f} "
          f"Rp {p.harga_member():>12,.0f}")


print("\n[OK] Selesai: 01_atribut_instance_vs_kelas.py")
