"""
Latihan Mandiri - Materi 08: Abstraksi (Abstraction)
File: latihan.py

Petunjuk:
- Kerjakan setiap soal di bawah ini.
- Hapus perintah `pass` dan ganti dengan implementasi Anda.
- Jalankan file ini untuk menguji jawaban: python latihan.py
- Output yang diharapkan tersedia sebagai komentar di tiap soal.
"""

from abc import ABC, abstractmethod
import math

print("=" * 60)
print("LATIHAN MATERI 08 - ABSTRAKSI (ABSTRACTION)")
print("=" * 60)


# ==================================================================
# SOAL 1 (* Mudah) — Kelas Abstrak Dasar: Hierarki Transportasi
#
# Buat hierarki kelas berikut menggunakan ABC:
#
#   TransportasiABC (abstrak)
#     |-- Sepeda       (tanpa mesin)
#     |-- Mobil        (berbahan bakar bensin)
#     `-- KapalFeri    (berbahan bakar solar)
#
# TransportasiABC harus punya:
#   - __init__(nama, kapasitas_penumpang)
#   - @abstractmethod: jenis_bahan_bakar() -> str
#   - @abstractmethod: kecepatan_maksimum() -> float  (km/jam)
#   - @abstractmethod: hitung_ongkos(jarak_km) -> float
#   - method KONKRET: info() yang mencetak semua informasi
#     (memanggil ketiga method abstrak di atas)
#
# Detail kelas konkret:
#   Sepeda(nama, kapasitas):
#     - jenis_bahan_bakar()    -> "Tenaga Manusia"
#     - kecepatan_maksimum()   -> 25.0 km/jam
#     - hitung_ongkos(jarak)   -> 0 (gratis)
#
#   Mobil(nama, kapasitas, harga_per_km):
#     - jenis_bahan_bakar()    -> "Bensin"
#     - kecepatan_maksimum()   -> 120.0 km/jam
#     - hitung_ongkos(jarak)   -> harga_per_km * jarak
#
#   KapalFeri(nama, kapasitas, tarif_dasar, tarif_per_km):
#     - jenis_bahan_bakar()    -> "Solar"
#     - kecepatan_maksimum()   -> 40.0 km/jam
#     - hitung_ongkos(jarak)   -> tarif_dasar + tarif_per_km * jarak
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 1: Hierarki Transportasi")
print("-" * 50)


class TransportasiABC(ABC):
    def __init__(self, nama, kapasitas_penumpang):
        self.nama               = nama
        self.kapasitas_penumpang = kapasitas_penumpang

    @abstractmethod
    def jenis_bahan_bakar(self):
        pass

    @abstractmethod
    def kecepatan_maksimum(self):
        pass

    @abstractmethod
    def hitung_ongkos(self, jarak_km):
        pass

    def info(self):
        ongkos = self.hitung_ongkos(100)
        print(f"  Nama              : {self.nama}")
        print(f"  Kapasitas         : {self.kapasitas_penumpang} penumpang")
        print(f"  Bahan Bakar       : {self.jenis_bahan_bakar()}")
        print(f"  Kecepatan Maks    : {self.kecepatan_maksimum()} km/jam")
        ongkos_str = f"Rp {ongkos:,.0f}" if ongkos > 0 else "Gratis"
        print(f"  Ongkos per 100 km : {ongkos_str}")


class Sepeda(TransportasiABC):
    def __init__(self, nama, kapasitas):
        pass   # TODO: panggil super().__init__

    def jenis_bahan_bakar(self):
        pass   # TODO: return "Tenaga Manusia"

    def kecepatan_maksimum(self):
        pass   # TODO: return 25.0

    def hitung_ongkos(self, jarak_km):
        pass   # TODO: return 0


class Mobil(TransportasiABC):
    def __init__(self, nama, kapasitas, harga_per_km):
        pass   # TODO

    def jenis_bahan_bakar(self):
        pass   # TODO: return "Bensin"

    def kecepatan_maksimum(self):
        pass   # TODO: return 120.0

    def hitung_ongkos(self, jarak_km):
        pass   # TODO: return harga_per_km * jarak_km


class KapalFeri(TransportasiABC):
    def __init__(self, nama, kapasitas, tarif_dasar, tarif_per_km):
        pass   # TODO

    def jenis_bahan_bakar(self):
        pass   # TODO: return "Solar"

    def kecepatan_maksimum(self):
        pass   # TODO: return 40.0

    def hitung_ongkos(self, jarak_km):
        pass   # TODO: return tarif_dasar + tarif_per_km * jarak_km


# --- Uji Soal 1 ---
# Jika implementasi benar, output berikut akan muncul:
#
# Kendaraan 1:
#   Nama              : Sepeda Gunung Polygon
#   Kapasitas         : 1 penumpang
#   Bahan Bakar       : Tenaga Manusia
#   Kecepatan Maks    : 25.0 km/jam
#   Ongkos per 100 km : Gratis
#
# Kendaraan 2:
#   Nama              : Toyota Avanza
#   Kapasitas         : 7 penumpang
#   Bahan Bakar       : Bensin
#   Kecepatan Maks    : 120.0 km/jam
#   Ongkos per 100 km : Rp 120,000
#
# Kendaraan 3:
#   Nama              : KMP Mahakam Jaya
#   Kapasitas         : 200 penumpang
#   Bahan Bakar       : Solar
#   Kecepatan Maks    : 40.0 km/jam
#   Ongkos per 100 km : Rp 600,000

kendaraan_list = [
    Sepeda("Sepeda Gunung Polygon", 1),
    Mobil("Toyota Avanza", 7, 1_200),
    KapalFeri("KMP Mahakam Jaya", 200, 100_000, 5_000),
]

for i, k in enumerate(kendaraan_list, 1):
    print(f"\n  Kendaraan {i}:")
    k.info()


# ==================================================================
# SOAL 2 (** Sedang) — Template Method: Proses Penilaian Karya
#
# Buat sistem penilaian karya menggunakan Template Method Pattern.
#
# PenilaianKaryaABC (abstrak):
#   - __init__(nama_juri, standar_nilai)  [standar_nilai: 0-100]
#   - @abstractproperty: nama_jenis_karya  (nama jenis lomba)
#   - @abstractmethod: kriteria_penilaian() -> list[str]
#     (kembalikan list nama kriteria, misal ["Orisinalitas", "Teknik"])
#   - @abstractmethod: nilai_per_kriteria(karya: dict) -> dict
#     (kembalikan dict {kriteria: nilai}, semua nilai 0-100)
#   - method KONKRET: nilai_final(karya) = rata-rata nilai_per_kriteria
#   - TEMPLATE METHOD: evaluasi(karya: dict):
#       1. Tampilkan judul evaluasi
#       2. Hitung nilai per kriteria
#       3. Hitung nilai final
#       4. Bandingkan dengan standar_nilai
#       5. Cetak hasil: LULUS / TIDAK LULUS
#
# Buat dua kelas konkret:
#
#   PenilaianEsai(nama_juri, standar_nilai):
#     - nama_jenis_karya: "Esai Ilmiah"
#     - kriteria: ["Relevansi Topik", "Kedalaman Analisis",
#                  "Struktur Penulisan", "Tata Bahasa"]
#     - nilai_per_kriteria(karya):
#         ambil dari karya["relevansi"], karya["analisis"],
#         karya["struktur"], karya["bahasa"]
#
#   PenilaianAplikasi(nama_juri, standar_nilai):
#     - nama_jenis_karya: "Aplikasi Informatika"
#     - kriteria: ["Fungsionalitas", "Antarmuka", "Inovasi", "Dokumentasi"]
#     - nilai_per_kriteria(karya):
#         ambil dari karya["fungsi"], karya["ui"],
#         karya["inovasi"], karya["dok"]
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 2: Template Method — Penilaian Karya")
print("-" * 50)


class PenilaianKaryaABC(ABC):
    def __init__(self, nama_juri, standar_nilai):
        self.nama_juri     = nama_juri
        self.standar_nilai = standar_nilai

    @property
    @abstractmethod
    def nama_jenis_karya(self):
        pass

    @abstractmethod
    def kriteria_penilaian(self):
        pass

    @abstractmethod
    def nilai_per_kriteria(self, karya: dict) -> dict:
        pass

    def nilai_final(self, karya: dict) -> float:
        pass   # TODO: rata-rata dari nilai_per_kriteria(karya).values()

    def evaluasi(self, karya: dict):
        pass   # TODO: Template Method
        # Contoh output yang diharapkan:
        # ------------------------------------------
        # Penilaian: Esai Ilmiah
        # Juri     : Dr. Ahmad
        # Karya    : "Implementasi AI di IKN"
        # ------------------------------------------
        # Relevansi Topik      : 88.0
        # Kedalaman Analisis   : 82.0
        # Struktur Penulisan   : 85.0
        # Tata Bahasa          : 90.0
        # ------------------------------------------
        # Nilai Final : 86.25
        # Standar     : 75.0
        # Hasil       : LULUS
        # ------------------------------------------


class PenilaianEsai(PenilaianKaryaABC):
    @property
    def nama_jenis_karya(self):
        pass   # TODO: return "Esai Ilmiah"

    def kriteria_penilaian(self):
        pass   # TODO: return list 4 kriteria

    def nilai_per_kriteria(self, karya: dict) -> dict:
        pass   # TODO: return dict dari karya["relevansi"], dll.


class PenilaianAplikasi(PenilaianKaryaABC):
    @property
    def nama_jenis_karya(self):
        pass   # TODO: return "Aplikasi Informatika"

    def kriteria_penilaian(self):
        pass   # TODO: return list 4 kriteria

    def nilai_per_kriteria(self, karya: dict) -> dict:
        pass   # TODO: return dict dari karya["fungsi"], dll.


# --- Uji Soal 2 ---
esai_juri = PenilaianEsai("Dr. Ahmad Fauzi", standar_nilai=75.0)
app_juri  = PenilaianAplikasi("Ir. Sri Rahayu", standar_nilai=80.0)

karya_esai = {
    "judul": "Implementasi AI di IKN",
    "relevansi": 88, "analisis": 82,
    "struktur": 85,  "bahasa":   90,
}
karya_app = {
    "judul": "SiKampus — Sistem Informasi Kampus Digital",
    "fungsi": 92, "ui": 78,
    "inovasi": 85, "dok": 70,
}
karya_app_gagal = {
    "judul": "App Absensi (versi alpha)",
    "fungsi": 65, "ui": 60,
    "inovasi": 55, "dok": 50,
}

print()
esai_juri.evaluasi(karya_esai)
app_juri.evaluasi(karya_app)
app_juri.evaluasi(karya_app_gagal)


# ==================================================================
# SOAL 3 (*** Sulit) — Multiple Interface: Sistem Perangkat Smart Campus
#
# Di era Smart Campus IKN, perangkat IoT di kampus bisa punya
# beberapa kemampuan. Buat sistem menggunakan multiple ABC.
#
# Buat 3 interface (ABC):
#
#   BisaTerhubung(ABC):
#     - @abstractmethod: hubungkan(alamat_ip) -> bool
#     - @abstractmethod: putuskan()
#     - @property @abstractmethod: status_koneksi -> str
#
#   BisaMemantau(ABC):
#     - @abstractmethod: baca_sensor() -> dict
#       (kembalikan dict berisi data sensor)
#     - @abstractmethod: nama_sensor -> str  (abstract property)
#
#   BisaMengirimData(ABC):
#     - @abstractmethod: kirim_ke_server(data: dict) -> bool
#     - @abstractmethod: url_server -> str  (abstract property)
#
# Buat 3 kelas perangkat konkret:
#
#   SensorSuhu(BisaTerhubung, BisaMemantau):
#     - Menghubungkan ke IP, membaca suhu & kelembaban
#     - baca_sensor() -> {"suhu_celsius": ..., "kelembaban_persen": ...}
#     - nama_sensor -> "Sensor Suhu & Kelembaban DHT22"
#     - status_koneksi: "Terhubung ke <ip>" atau "Tidak Terhubung"
#
#   KameraCCTV(BisaTerhubung, BisaMengirimData):
#     - Menghubungkan ke IP, mengirim snapshot ke server
#     - kirim_ke_server(data) -> True jika terhubung, False jika tidak
#     - url_server -> "https://cctv.unmul.ac.id/upload"
#
#   StasiunCuaca(BisaTerhubung, BisaMemantau, BisaMengirimData):
#     - Mengimplementasikan KETIGA interface sekaligus
#     - Baca cuaca (suhu, angin, hujan) DAN kirim ke server otomatis
#     - baca_dan_kirim(): panggil baca_sensor() lalu kirim_ke_server()
# ==================================================================
print("\n" + "-" * 50)
print("SOAL 3: Multiple Interface — Smart Campus IoT")
print("-" * 50)


class BisaTerhubung(ABC):
    @abstractmethod
    def hubungkan(self, alamat_ip: str) -> bool:
        pass

    @abstractmethod
    def putuskan(self):
        pass

    @property
    @abstractmethod
    def status_koneksi(self) -> str:
        pass


class BisaMemantau(ABC):
    @abstractmethod
    def baca_sensor(self) -> dict:
        pass

    @property
    @abstractmethod
    def nama_sensor(self) -> str:
        pass


class BisaMengirimData(ABC):
    @abstractmethod
    def kirim_ke_server(self, data: dict) -> bool:
        pass

    @property
    @abstractmethod
    def url_server(self) -> str:
        pass


class SensorSuhu(BisaTerhubung, BisaMemantau):
    def __init__(self, id_perangkat):
        self.id_perangkat = id_perangkat
        self._ip          = None
        # Tambahkan atribut yang diperlukan

    def hubungkan(self, alamat_ip: str) -> bool:
        pass   # TODO: simpan alamat_ip, return True

    def putuskan(self):
        pass   # TODO: reset IP ke None

    @property
    def status_koneksi(self) -> str:
        pass   # TODO: "Terhubung ke <ip>" atau "Tidak Terhubung"

    @property
    def nama_sensor(self) -> str:
        pass   # TODO: return "Sensor Suhu & Kelembaban DHT22"

    def baca_sensor(self) -> dict:
        pass   # TODO: return {"suhu_celsius": 28.5, "kelembaban_persen": 72}
               # (nilai boleh statis/hardcoded untuk latihan ini)


class KameraCCTV(BisaTerhubung, BisaMengirimData):
    def __init__(self, id_kamera, lokasi):
        self.id_kamera = id_kamera
        self.lokasi    = lokasi
        self._ip       = None

    def hubungkan(self, alamat_ip: str) -> bool:
        pass   # TODO

    def putuskan(self):
        pass   # TODO

    @property
    def status_koneksi(self) -> str:
        pass   # TODO

    @property
    def url_server(self) -> str:
        pass   # TODO: return "https://cctv.unmul.ac.id/upload"

    def kirim_ke_server(self, data: dict) -> bool:
        pass   # TODO: print info pengiriman, return True jika terhubung


class StasiunCuaca(BisaTerhubung, BisaMemantau, BisaMengirimData):
    def __init__(self, id_stasiun, lokasi):
        self.id_stasiun = id_stasiun
        self.lokasi     = lokasi
        self._ip        = None

    def hubungkan(self, alamat_ip: str) -> bool:
        pass   # TODO

    def putuskan(self):
        pass   # TODO

    @property
    def status_koneksi(self) -> str:
        pass   # TODO

    @property
    def nama_sensor(self) -> str:
        pass   # TODO: return "Stasiun Cuaca Lengkap"

    def baca_sensor(self) -> dict:
        pass   # TODO: return {"suhu": 31.2, "kecepatan_angin_kmh": 15,
               #              "curah_hujan_mm": 0.0, "tekanan_hpa": 1012}

    @property
    def url_server(self) -> str:
        pass   # TODO: return "https://bmkg.unmul.ac.id/cuaca"

    def kirim_ke_server(self, data: dict) -> bool:
        pass   # TODO

    def baca_dan_kirim(self):
        """Method khusus StasiunCuaca: baca sensor lalu langsung kirim."""
        pass   # TODO: panggil baca_sensor() dan kirim_ke_server()


# --- Uji Soal 3 ---
# Contoh output yang diharapkan:
#
#   [SensorSuhu S-001] Menghubungkan ke 192.168.1.10... Terhubung!
#   Status: Terhubung ke 192.168.1.10
#   Membaca Sensor Suhu & Kelembaban DHT22:
#     suhu_celsius     : 28.5
#     kelembaban_persen: 72
#
#   [CCTV CAM-GD-01] Menghubungkan ke 192.168.1.20... Terhubung!
#   Mengirim snapshot ke https://cctv.unmul.ac.id/upload ... OK
#
#   [StasiunCuaca SW-IKN] Menghubungkan ke 10.0.0.5... Terhubung!
#   Membaca & mengirim data cuaca...
#     Data: {'suhu': 31.2, 'kecepatan_angin_kmh': 15, ...}
#   Dikirim ke https://bmkg.unmul.ac.id/cuaca ... OK
#
#   Cek interface:
#   sensor  is BisaTerhubung : True
#   sensor  is BisaMemantau  : True
#   sensor  is BisaMengirimData: False
#   stasiun is BisaTerhubung : True
#   stasiun is BisaMemantau  : True
#   stasiun is BisaMengirimData: True

print()
sensor  = SensorSuhu("S-001")
kamera  = KameraCCTV("CAM-GD-01", "Gedung Dekanat")
stasiun = StasiunCuaca("SW-IKN", "Kampus IKN Nusantara")

sensor.hubungkan("192.168.1.10")
print(f"  Status: {sensor.status_koneksi}")
print(f"  Membaca {sensor.nama_sensor}:")
data_sensor = sensor.baca_sensor()
for k, v in data_sensor.items():
    print(f"    {k:<25}: {v}")

print()
kamera.hubungkan("192.168.1.20")
kamera.kirim_ke_server({"snapshot": "frame_001.jpg", "waktu": "08:00:00"})

print()
stasiun.hubungkan("10.0.0.5")
stasiun.baca_dan_kirim()

print()
print("  Cek interface:")
print(f"  sensor  is BisaTerhubung   : {isinstance(sensor,  BisaTerhubung)}")
print(f"  sensor  is BisaMemantau    : {isinstance(sensor,  BisaMemantau)}")
print(f"  sensor  is BisaMengirimData: {isinstance(sensor,  BisaMengirimData)}")
print(f"  stasiun is BisaTerhubung   : {isinstance(stasiun, BisaTerhubung)}")
print(f"  stasiun is BisaMemantau    : {isinstance(stasiun, BisaMemantau)}")
print(f"  stasiun is BisaMengirimData: {isinstance(stasiun, BisaMengirimData)}")
