"""
Kode Praktik - Materi 13: OOP Modern Python
File: 02_type_hints_advanced.py
Topik: Comprehensive type hints untuk OOP

Jalankan: python 02_type_hints_advanced.py
"""

from dataclasses import dataclass
from typing import List, Dict, Optional, Union

# ======================================================================
# BAGIAN 1: Type Hints di @dataclass
#           Fokus: Comprehensive typing
# ======================================================================
print("=" * 60)
print("BAGIAN 1: Type Hints di @dataclass")
print("=" * 60)

@dataclass
class Mahasiswa:
    """Mahasiswa dengan comprehensive type hints."""
    nim: str
    nama: str
    angkatan: int
    nilai_dict: Optional[Dict[str, float]] = None  # Optional = bisa None
    
    def __post_init__(self):
        if self.nilai_dict is None:
            self.nilai_dict = {}
    
    def input_nilai(self, kode_mk: str, nilai: float) -> None:
        """Input nilai untuk matakuliah."""
        if not (0 <= nilai <= 100):
            raise ValueError(f"Nilai harus 0-100")
        self.nilai_dict[kode_mk] = nilai
    
    def hitung_rata_rata(self) -> float:
        """Hitung rata-rata nilai."""
        if not self.nilai_dict:
            return 0
        return sum(self.nilai_dict.values()) / len(self.nilai_dict)
    
    def get_nilai_list(self) -> List[float]:
        """Get list of all nilai."""
        return list(self.nilai_dict.values())
    
    def get_nilai_dict(self) -> Dict[str, float]:
        """Get dictionary of nilai."""
        return dict(self.nilai_dict)

print("\n-- Demo Type Hints di @dataclass --")
mhs = Mahasiswa("2301001", "Budi Santoso", 2023)
mhs.input_nilai("IF201", 85)
mhs.input_nilai("IF202", 90)

print(f"Mahasiswa: {mhs}")
print(f"Rata-rata: {mhs.hitung_rata_rata():.2f}")
print(f"Nilai list: {mhs.get_nilai_list()}")

# ======================================================================
# BAGIAN 2: Optional dan Union Types
#           Fokus: Nullable dan multiple types
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 2: Optional dan Union Types")
print("=" * 60)

@dataclass
class KRS:
    """KRS dengan Optional types."""
    nim: str
    semester: int
    total_sks: int
    catatan: Optional[str] = None

def find_krs(nim: str) -> Optional[KRS]:
    """Find KRS by NIM.
    
    Returns:
        KRS jika ditemukan, None jika tidak
    """
    data = {"2301001": KRS("2301001", 3, 18)}
    return data.get(nim)

def convert_nilai(value: Union[str, int, float]) -> float:
    """Convert value to float.
    
    Args:
        value: String, int, atau float
    
    Returns:
        float: Converted value
    """
    return float(value)

print("\n-- Optional Demo --")
krs = KRS("2301001", 3, 18, "Perlu pembimbing akademik")
print(f"KRS: {krs}")

print("\n-- Union Demo --")
print(f"Convert '85': {convert_nilai('85')}")
print(f"Convert 85: {convert_nilai(85)}")
print(f"Convert 85.5: {convert_nilai(85.5)}")

# ======================================================================
# BAGIAN 3: Complex Type Hints
#           Fokus: Advanced patterns
# ======================================================================
print("\n" + "=" * 60)
print("BAGIAN 3: Complex Type Hints")
print("=" * 60)

@dataclass
class Transaksi:
    """Transaksi dengan complex type hints."""
    id: str
    nim: str
    jenis: str
    items: List[Dict[str, Union[str, int, float]]]

print("\n-- Complex Type Hints Demo --")
transaksi = Transaksi(
    id="TXN001",
    nim="2301001",
    jenis="pembayaran",
    items=[
        {"kode": "SPP", "harga": 500000},
        {"kode": "PRAKTIK", "harga": 100000},
    ]
)

print(f"Transaksi: {transaksi.id}")
print(f"Total items: {len(transaksi.items)}")

print("\n" + "=" * 60)
print("Bagian selesai!")
print("=" * 60)
