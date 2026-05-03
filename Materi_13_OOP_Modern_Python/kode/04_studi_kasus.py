"""
Sistem akademik dengan @dataclass, type hints, dan __slots__.

Studi kasus mengintegrasikan semua modern Python OOP features.

Jalankan: python 04_studi_kasus.py
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
from datetime import datetime

# ======================================================================
# STUDI KASUS: Sistem Akademik Modern Python OOP
# ======================================================================
print("=" * 60)
print("STUDI KASUS: Sistem Akademik Modern Python OOP")
print("=" * 60)

@dataclass
class MataKuliah:
    """Representasi matakuliah."""
    kode: str
    nama: str
    sks: int
    prerequisite: List[str] = field(default_factory=list)
    semester: int = 1
    
    def __post_init__(self):
        """Validate SKS dan semester."""
        if not (1 <= self.sks <= 6):
            raise ValueError(f"SKS harus 1-6")
        if not (1 <= self.semester <= 8):
            raise ValueError(f"Semester harus 1-8")
    
    def harga(self) -> float:
        """Calculate harga (SKS * 100,000)."""
        return self.sks * 100_000
    
    def info(self) -> Dict[str, object]:
        """Get info matakuliah."""
        return {
            "kode": self.kode,
            "nama": self.nama,
            "sks": self.sks,
            "harga": self.harga(),
            "prerequisite": self.prerequisite,
            "semester": self.semester,
        }

@dataclass
class Mahasiswa:
    """Representasi mahasiswa."""
    nim: str
    nama: str
    angkatan: int
    nilai_dict: Dict[str, float] = field(default_factory=dict)
    
    def __post_init__(self):
        """Validate NIM dan angkatan."""
        if len(self.nim) < 6:
            raise ValueError("NIM minimal 6 karakter")
        if not (2000 <= self.angkatan <= 2030):
            raise ValueError("Angkatan harus 2000-2030")
    
    def input_nilai(self, kode_mk: str, nilai: float) -> None:
        """Input nilai untuk matakuliah."""
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai harus 0-100")
        self.nilai_dict[kode_mk] = nilai
    
    def hitung_rata_rata(self) -> float:
        """Calculate rata-rata nilai."""
        if not self.nilai_dict:
            return 0
        return sum(self.nilai_dict.values()) / len(self.nilai_dict)
    
    def get_grade(self) -> str:
        """Get grade berdasarkan rata-rata."""
        rata = self.hitung_rata_rata()
        if rata >= 80:
            return "A"
        elif rata >= 70:
            return "B"
        elif rata >= 60:
            return "C"
        else:
            return "D"
    
    def info(self) -> Dict[str, object]:
        """Get info lengkap mahasiswa."""
        return {
            "nim": self.nim,
            "nama": self.nama,
            "angkatan": self.angkatan,
            "rata_rata": round(self.hitung_rata_rata(), 2),
            "grade": self.get_grade(),
            "total_mk": len(self.nilai_dict),
        }

@dataclass(frozen=True)
class Transaksi:
    """Immutable transaksi akademik.
    
    Menggunakan frozen=True (immutable) + __slots__ (memory efficient).
    Class ini aman untuk __slots__ karena tidak ada field default_factory.
    """
    __slots__ = ('id', 'nim', 'jenis', 'jumlah', 'timestamp')
    
    id: str
    nim: str
    jenis: str
    jumlah: float
    timestamp: str  # selalu diisi saat create, tidak ada default
    
    def __post_init__(self):
        """Validate transaksi."""
        if self.jumlah < 0:
            raise ValueError("Jumlah tidak boleh negative")

class SistemAkademik:
    """Sistem akademik utama."""
    
    def __init__(self):
        """Initialize sistem."""
        self.mahasiswa_dict: Dict[str, Mahasiswa] = {}
        self.matakuliah_dict: Dict[str, MataKuliah] = {}
        self.transaksi_list: List[Transaksi] = []
    
    def register_mahasiswa(self, nim: str, nama: str, angkatan: int) -> Optional[Mahasiswa]:
        """Register mahasiswa baru."""
        if nim in self.mahasiswa_dict:
            return None
        
        mahasiswa = Mahasiswa(nim, nama, angkatan)
        self.mahasiswa_dict[nim] = mahasiswa
        return mahasiswa
    
    def create_matakuliah(self, kode: str, nama: str, sks: int) -> Optional[MataKuliah]:
        """Create matakuliah baru."""
        if kode in self.matakuliah_dict:
            return None
        
        mk = MataKuliah(kode, nama, sks)
        self.matakuliah_dict[kode] = mk
        return mk
    
    def input_nilai(self, nim: str, kode_mk: str, nilai: float) -> bool:
        """Input nilai mahasiswa."""
        if nim not in self.mahasiswa_dict:
            return False
        
        mahasiswa = self.mahasiswa_dict[nim]
        mahasiswa.input_nilai(kode_mk, nilai)
        return True
    
    def record_transaksi(self, id: str, nim: str, jenis: str, jumlah: float) -> Transaksi:
        """Record transaksi akademik."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        transaksi = Transaksi(id, nim, jenis, jumlah, timestamp)
        self.transaksi_list.append(transaksi)
        return transaksi

# ===== Demo =====

print("\n-- Setup Sistem Akademik --")

sistem = SistemAkademik()

# Register mahasiswa
mhs1 = sistem.register_mahasiswa("2301001", "Budi Santoso", 2023)
mhs2 = sistem.register_mahasiswa("2301002", "Sari Dewi", 2023)

# Create matakuliah
sistem.create_matakuliah("IF201", "Database", 3)
sistem.create_matakuliah("IF202", "Algoritma", 3)

print("\n-- Input Nilai --")

sistem.input_nilai("2301001", "IF201", 85)
sistem.input_nilai("2301001", "IF202", 90)
sistem.input_nilai("2301002", "IF201", 78)
sistem.input_nilai("2301002", "IF202", 82)

print("\n-- Laporan Mahasiswa --")

for nim, mahasiswa in sistem.mahasiswa_dict.items():
    laporan = mahasiswa.info()
    print(f"\n{mahasiswa.nama} ({nim})")
    print(f"  Rata-rata: {laporan['rata_rata']}")
    print(f"  Grade: {laporan['grade']}")
    print(f"  Total MK: {laporan['total_mk']}")

print("\n-- Rekam Transaksi --")

sistem.record_transaksi("TXN001", "2301001", "pembayaran", 5000000)
sistem.record_transaksi("TXN002", "2301002", "pembayaran", 5000000)

print(f"\nTotal transaksi: {len(sistem.transaksi_list)}")

print("\n" + "=" * 60)
print("Studi kasus selesai!")
print("=" * 60)
