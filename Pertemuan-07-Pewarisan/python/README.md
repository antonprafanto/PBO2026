# 🐍 Praktik Python — Pertemuan 07: Pewarisan

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)

> **Prasyarat:** sudah membaca [Konsep Pertemuan 07](../README.md). Semua kode di halaman ini ada di folder `contoh/` dan `studi-kasus/`, dan bisa langsung dijalankan.

## Daftar Isi

- [Persiapan](#persiapan)
1. [Masalah: Kode Kembar di Dua Kelas](#1-masalah-kode-kembar-di-dua-kelas)
2. [Kelas Induk dan Kelas Anak](#2-kelas-induk-dan-kelas-anak)
3. [Override dan `super()`](#3-override-dan-super)
4. [Urutan Konstruktor dan Pewarisan Bertingkat](#4-urutan-konstruktor-dan-pewarisan-bertingkat)
5. [Atribut `_` untuk Kelas Anak](#5-atribut-_-untuk-kelas-anak)
6. [Kelas Akar `object`, `isinstance()`, dan `issubclass()`](#6-kelas-akar-object-isinstance-dan-issubclass)
7. [is-a atau has-a?](#7-is-a-atau-has-a)
8. [Pewarisan Ganda dan MRO](#8-pewarisan-ganda-dan-mro)
9. [Studi Kasus KedaiKita](#9-studi-kasus-kedaikita)
10. [Kesalahan Umum dan Cara Membaca Pesan Error](#10-kesalahan-umum-dan-cara-membaca-pesan-error)

## Persiapan

Struktur folder Python pertemuan ini:

```text
python/
├── contoh/          <- 8 contoh, dari masalah duplikasi sampai pewarisan ganda
├── studi-kasus/     <- KedaiKita versi Pertemuan 07 (6 file)
└── solusi/          <- solusi latihan (buka setelah mencoba sendiri!)
```

Cara menjalankan sebuah contoh dari terminal:

```bash
cd Pertemuan-07-Pewarisan/python/contoh
python contoh01_masalah_duplikasi.py
```

Studi kasus terdiri atas beberapa file, jadi jalankan `main.py` **dari dalam** folder `studi-kasus`:

```bash
cd Pertemuan-07-Pewarisan/python/studi-kasus
python main.py
```

> [!NOTE]
> Di macOS/Linux, gunakan `python3` sebagai ganti `python`. Di VS Code, kamu juga bisa membuka file lalu menekan tombol ▶ (*Run Python File*). Panduan instalasi ada di [00-Persiapan](../../00-Persiapan/README.md).

Seperti sejak Pertemuan 05, kode memakai *type hint* (`merek: str`, `-> int`) dan atribut bergaris bawah (`self._merek`).

## 1. Masalah: Kode Kembar di Dua Kelas

File: [`contoh/contoh01_masalah_duplikasi.py`](contoh/contoh01_masalah_duplikasi.py)

Sebelum belajar pewarisan, rasakan dulu masalahnya. File ini berisi dua kelas yang ditulis terpisah, `Motor` dan `Mobil`. Berikut kelas `Motor`:

```python
class Motor:
    """Sepeda motor, ditulis tanpa pewarisan."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, transmisi: str):
        self._merek = merek  # [1] tiga atribut ini kembar dengan milik Mobil
        self._plat_nomor = plat_nomor
        self._tahun = tahun
        self._transmisi = transmisi  # [2] khusus motor: "matic" atau "manual"

    @property
    def merek(self) -> str:
        return self._merek

    def info(self) -> str:  # [3] method kembar
        return f"{self._merek} ({self._plat_nomor}) tahun {self._tahun}"

    def umur(self, tahun_sekarang: int) -> int:  # [3] method kembar
        return tahun_sekarang - self._tahun

    def deskripsi(self) -> str:
        return f"Motor: {self.info()}, transmisi {self._transmisi}"

```

Kelas `Mobil` di file yang sama ditulis dengan pola yang **persis sama**. Bedanya hanya atribut `_jumlah_kursi` (pengganti `_transmisi`) dan isi method `deskripsi()`. Bukalah file-nya dan bandingkan baris demi baris.

Program utamanya membuat satu motor dan satu mobil, lalu menampilkan deskripsi dan umur keduanya.

**Output:**

```text
=== DAFTAR KENDARAAN ===
Motor: Honda Beat (KT 1234 AB) tahun 2020, transmisi matic
Mobil: Toyota Avanza (KT 5678 CD) tahun 2018, 7 kursi

=== UMUR DI TAHUN 2026 ===
Honda Beat: 6 tahun
Toyota Avanza: 8 tahun
```

Penjelasan:

- **[1]** Atribut `_merek`, `_plat_nomor`, dan `_tahun` ditulis dua kali, di `Motor` dan di `Mobil`. Property `merek` juga kembar.
- **[2]** Hanya satu atribut yang benar-benar khas: `_transmisi` untuk motor dan `_jumlah_kursi` untuk mobil.
- **[3]** Method `info()` dan `umur()` sama persis, huruf demi huruf.

Program ini berjalan benar, tetapi rapuh. Hampir seluruh isi kelas `Mobil` adalah salinan dari `Motor`. Yang benar-benar baru hanya satu atribut dan isi method `deskripsi()`.

> [!TIP]
> **Coba sendiri:** tambahkan atribut `warna` ke semua kendaraan, lalu tampilkan di `info()`. Hitung berapa tempat yang harus kamu ubah. Bayangkan jika jenis kendaraannya ada sepuluh!

## 2. Kelas Induk dan Kelas Anak

File: [`contoh/contoh02_kelas_induk_dan_anak.py`](contoh/contoh02_kelas_induk_dan_anak.py)

Sekarang kita kumpulkan semua bagian yang sama ke satu **kelas induk** bernama `Kendaraan`. `Motor` dan `Mobil` menjadi **kelas anak**.

```python
class Kendaraan:  # [1] kelas induk: semua bagian yang SAMA dikumpulkan di sini
    """Kelas induk untuk semua kendaraan bermotor."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int):
        self._merek = merek
        self._plat_nomor = plat_nomor
        self._tahun = tahun

    @property
    def merek(self) -> str:
        return self._merek

    def info(self) -> str:
        return f"{self._merek} ({self._plat_nomor}) tahun {self._tahun}"

    def umur(self, tahun_sekarang: int) -> int:
        return tahun_sekarang - self._tahun


class Motor(Kendaraan):  # [2] Motor adalah Kendaraan
    """Sepeda motor: semua milik Kendaraan, ditambah jenis transmisi."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, transmisi: str):
        super().__init__(merek, plat_nomor, tahun)  # [3] bagian induk diisi induk
        self._transmisi = transmisi  # [4] atribut tambahan khusus motor

    def deskripsi(self) -> str:  # [5] method tambahan, memakai method warisan
        return f"Motor: {self.info()}, transmisi {self._transmisi}"


class Mobil(Kendaraan):
    """Mobil: semua milik Kendaraan, ditambah jumlah kursi."""

    def __init__(self, merek: str, plat_nomor: str, tahun: int, jumlah_kursi: int):
        super().__init__(merek, plat_nomor, tahun)
        self._jumlah_kursi = jumlah_kursi

    def deskripsi(self) -> str:
        return f"Mobil: {self.info()}, {self._jumlah_kursi} kursi"
```

Program utamanya **sama persis** dengan contoh 01. Perhatikan dua baris terakhirnya:

```python
    print(f"{beat.merek}: {beat.umur(2026)} tahun")  # [6] merek dan umur() warisan
    print(f"{avanza.merek}: {avanza.umur(2026)} tahun")
```

Jalankan file ini, lalu bandingkan: output-nya **sama persis** dengan output contoh 01. Bedanya, kodenya jauh lebih rapi. Mengubah cara menghitung umur kini cukup dilakukan di **satu** tempat.

Penjelasan:

- **[1]** `Kendaraan` adalah kelas biasa. Ia menjadi "induk" karena ada kelas lain yang mewarisinya.
- **[2]** `class Motor(Kendaraan):` berarti "Motor mewarisi Kendaraan". Nama kelas induk ditulis di dalam tanda kurung.
- **[3]** `super()` merujuk ke kelas induk. `super().__init__(...)` menjalankan konstruktor `Kendaraan` untuk mengisi `_merek`, `_plat_nomor`, dan `_tahun` milik objek motor ini.
- **[4]** Setelah bagian induk terisi, kelas anak mengisi atribut tambahannya sendiri.
- **[5]** Method baru boleh memanggil method warisan. `self.info()` tidak ditulis di `Motor`, tetapi tersedia karena diwarisi dari `Kendaraan`.
- **[6]** Property `merek` dan method `umur()` juga tidak ditulis di `Motor` maupun `Mobil`. Keduanya warisan.

> [!TIP]
> **Coba sendiri:** di bawah kelas `Mobil`, tambahkan kelas anak ketiga yang **tidak** punya `__init__` sama sekali:
>
> ```python
> class Truk(Kendaraan):
>     pass
> ```
>
> Lalu cetak `Truk("Hino Dutro", "KT 9012 EF", 2015).info()` di `main()`. Apakah berhasil? Mengapa?

<details>
<summary>Lihat jawaban</summary>

Berhasil, dan tercetak `Hino Dutro (KT 9012 EF) tahun 2015`. Di Python, `__init__` adalah method biasa yang ikut diwariskan. Karena `Truk` tidak menulis `__init__` sendiri, Python memakai `__init__` milik `Kendaraan`. Hal ini **berbeda** di Java: konstruktor tidak pernah diwariskan (lihat [Jembatan](../jembatan-python-java.md)).

</details>

## 3. Override dan `super()`

File: [`contoh/contoh03_override.py`](contoh/contoh03_override.py)

Kelas anak bisa **menimpa** (*override*) method induk dengan menulis method bernama sama. Di dalam versi barunya, versi induk tetap bisa dipanggil lewat `super()`.

```python
BIAYA_LAYANAN_VIP = 25000  # biaya layanan VIP per orang, dalam Rupiah


class Tiket:
    """Tiket reguler sebuah acara."""

    def __init__(self, acara: str, harga: int):
        self._acara = acara
        self._harga = harga

    @property
    def acara(self) -> str:
        return self._acara

    def info(self) -> str:
        return f"Tiket {self._acara} - Rp{self._harga}"

    def hitung_bayar(self, jumlah: int) -> int:
        return self._harga * jumlah


class TiketVIP(Tiket):
    """Tiket VIP: punya fasilitas dan ada biaya layanan per orang."""

    def __init__(self, acara: str, harga: int, fasilitas: str):
        super().__init__(acara, harga)
        self._fasilitas = fasilitas

    def info(self) -> str:  # [1] override: nama dan parameter sama dengan induk
        return f"{super().info()} | VIP: {self._fasilitas}"  # [2] induk + tambahan

    def hitung_bayar(self, jumlah: int) -> int:  # [3] override kedua
        harga_dasar = super().hitung_bayar(jumlah)  # [4] hitungan versi induk
        return harga_dasar + BIAYA_LAYANAN_VIP * jumlah


def main():
    reguler = Tiket("Festival Musik Kampus", 50000)
    vip = TiketVIP("Festival Musik Kampus", 120000, "kursi depan dan kaus")

    print("=== INFO TIKET ===")
    print(reguler.info())  # [5] objek Tiket -> versi Tiket
    print(vip.info())  # [5] objek TiketVIP -> versi TiketVIP

    print()
    print("=== BAYAR UNTUK 3 ORANG ===")
    print(f"Reguler: Rp{reguler.hitung_bayar(3)}")
    print(f"VIP    : Rp{vip.hitung_bayar(3)}")
    print(f"Acara  : {vip.acara}")  # [6] property yang tidak di-override tetap warisan
```

**Output:**

```text
=== INFO TIKET ===
Tiket Festival Musik Kampus - Rp50000
Tiket Festival Musik Kampus - Rp120000 | VIP: kursi depan dan kaus

=== BAYAR UNTUK 3 ORANG ===
Reguler: Rp150000
VIP    : Rp435000
Acara  : Festival Musik Kampus
```

Penjelasan:

- **[1]** `TiketVIP` menulis method `info` dengan nama dan parameter yang sama dengan milik `Tiket`. Untuk objek `TiketVIP`, versi inilah yang dipakai.
- **[2]** `super().info()` menjalankan versi **induk**, yang menghasilkan `Tiket Festival Musik Kampus - Rp120000`. Versi anak tinggal menambahkan keterangan VIP. Rumus teks induk tidak perlu ditulis ulang.
- **[3]** Satu kelas boleh meng-*override* beberapa method sekaligus.
- **[4]** `super().hitung_bayar(3)` menghasilkan 3 x 120000 = 360000. Versi anak lalu menambah biaya layanan 3 x 25000 = 75000, sehingga totalnya 435000.
- **[5]** Versi yang dipakai ditentukan oleh **objeknya**. `reguler` adalah `Tiket`, jadi memakai versi `Tiket`. `vip` adalah `TiketVIP`, jadi memakai versi `TiketVIP`.
- **[6]** Method atau property yang tidak di-*override* tetap memakai versi warisan.

> [!TIP]
> **Coba sendiri:** hapus method `info()` dari kelas `TiketVIP`, lalu jalankan lagi. Baris kedua output menjadi `Tiket Festival Musik Kampus - Rp120000`. Tanpa *override*, objek VIP kembali memakai versi warisan dari `Tiket`.

> [!WARNING]
> Python **tidak memeriksa** apakah *override*-mu benar. Jika kamu salah ketik nama method, misalnya `hitung_byar`, Python diam saja dan menganggapnya method baru. Akibatnya, versi induk yang tetap berjalan. Lihat [Kesalahan 4](#kesalahan-4-salah-ketik-nama-method-saat-override).

## 4. Urutan Konstruktor dan Pewarisan Bertingkat

File: [`contoh/contoh04_urutan_konstruktor.py`](contoh/contoh04_urutan_konstruktor.py)

Contoh ini punya tiga tingkat: `Perangkat` → `Komputer` → `Laptop`. Setiap konstruktor mencetak pesan **setelah** memanggil konstruktor induknya.

```python
class Perangkat:
    """Tingkat 1: semua perangkat elektronik."""

    def __init__(self, merek: str):
        self._merek = merek
        print(f"  Bagian Perangkat selesai: merek {merek}")  # [1]

    def nyalakan(self) -> str:
        return f"{self._merek} dinyalakan"


class Komputer(Perangkat):
    """Tingkat 2: Komputer adalah Perangkat."""

    def __init__(self, merek: str, ram_gb: int):
        super().__init__(merek)  # [2] minta induk menyiapkan bagiannya dulu
        self._ram_gb = ram_gb
        print(f"  Bagian Komputer selesai: RAM {ram_gb} GB")

    def jalankan(self, program: str) -> str:
        return f"{program} berjalan dengan RAM {self._ram_gb} GB"


class Laptop(Komputer):
    """Tingkat 3: Laptop adalah Komputer, dan karena itu juga Perangkat."""

    def __init__(self, merek: str, ram_gb: int, baterai_jam: int):
        super().__init__(merek, ram_gb)  # [3] induk langsung Laptop adalah Komputer
        self._baterai_jam = baterai_jam
        print(f"  Bagian Laptop selesai: baterai {baterai_jam} jam")

    def cek_baterai(self) -> str:
        return f"Baterai tahan {self._baterai_jam} jam"


def main():
    print("=== MEMBUAT LAPTOP (3 TINGKAT) ===")
    laptop = Laptop("Lenovo", 16, 8)  # [4]

    print()
    print("=== MEMBUAT KOMPUTER (2 TINGKAT) ===")
    Komputer("Dell", 32)  # [5] hanya dua bagian yang disiapkan

    print()
    print("=== METHOD DARI SETIAP TINGKAT ===")
    print(laptop.nyalakan())  # [6] warisan dari "kakek" (Perangkat)
    print(laptop.jalankan("VS Code"))  # warisan dari induk (Komputer)
    print(laptop.cek_baterai())  # milik Laptop sendiri
```

**Output:**

```text
=== MEMBUAT LAPTOP (3 TINGKAT) ===
  Bagian Perangkat selesai: merek Lenovo
  Bagian Komputer selesai: RAM 16 GB
  Bagian Laptop selesai: baterai 8 jam

=== MEMBUAT KOMPUTER (2 TINGKAT) ===
  Bagian Perangkat selesai: merek Dell
  Bagian Komputer selesai: RAM 32 GB

=== METHOD DARI SETIAP TINGKAT ===
Lenovo dinyalakan
VS Code berjalan dengan RAM 16 GB
Baterai tahan 8 jam
```

Penjelasan:

- **[1]** `Perangkat` tidak menulis induk, jadi induknya adalah kelas akar `object` (bagian 6).
- **[2]** Baris pertama `__init__` milik `Komputer` langsung menyerahkan pekerjaan ke induk.
- **[3]** `super()` di `Laptop` merujuk ke **induk langsungnya**, yaitu `Komputer`, bukan `Perangkat`. `Komputer` yang nanti meneruskan ke `Perangkat`.
- **[4]** Walaupun yang dibuat adalah `Laptop`, pesan pertama yang tercetak berasal dari `Perangkat`. Lapis paling atas selesai lebih dulu.
- **[5]** Membuat `Komputer` hanya menjalankan dua konstruktor. `Laptop` tidak terlibat sama sekali.
- **[6]** Objek `Laptop` bisa memakai method dari **semua** tingkat di atasnya.

> [!TIP]
> **Coba sendiri:** di `Komputer.__init__`, pindahkan baris `super().__init__(merek)` ke **paling bawah**. Tebak dulu urutan tiga pesan saat membuat `Laptop`, baru jalankan.

<details>
<summary>Lihat jawaban</summary>

Urutannya menjadi `Bagian Komputer selesai`, lalu `Bagian Perangkat selesai`, lalu `Bagian Laptop selesai`. Python menjalankan baris demi baris, jadi cetakan `Komputer` terjadi sebelum `super()` dipanggil. Kode seperti ini berbahaya: jika `Komputer` memakai atribut induk sebelum `super()`, atribut itu belum ada. Java bahkan menolak kode semacam ini saat kompilasi. Biasakan `super().__init__(...)` di baris pertama.

</details>

## 5. Atribut `_` untuk Kelas Anak

File: [`contoh/contoh05_akses_kelas_anak.py`](contoh/contoh05_akses_kelas_anak.py)

Python tidak punya kata kunci `protected` seperti Java. Sebagai gantinya, programmer Python sepakat: atribut berawalan **satu** garis bawah adalah urusan "internal" kelas itu **dan kelas-kelas anaknya**.

```python
class RekeningBank:
    """Kelas induk rekening."""

    def __init__(self, pemilik: str, saldo_awal: int):
        self._pemilik = pemilik
        self._saldo = saldo_awal  # [1] satu garis bawah: internal kelas dan anaknya

    @property
    def saldo(self) -> int:  # [2] pintu resmi untuk membaca saldo dari luar
        return self._saldo

    def info(self) -> str:
        return f"Rekening {self._pemilik}: saldo Rp{self._saldo}"


class RekeningTabungan(RekeningBank):
    """Tabungan yang mendapat bunga bulanan (persen, bilangan bulat)."""

    def __init__(self, pemilik: str, saldo_awal: int, bunga_persen: int):
        super().__init__(pemilik, saldo_awal)
        self._bunga_persen = bunga_persen

    def tambah_bunga(self) -> int:
        bunga = self._saldo * self._bunga_persen // 100  # [3] membaca _saldo induk
        self._saldo += bunga  # [3] mengubah _saldo induk secara langsung
        return bunga
```

Bagian akhir program utamanya:

```python
    print(f"Lewat pintu resmi  : Rp{tabungan.saldo}")
    print(f"Langsung ke atribut: Rp{tabungan._saldo} (bisa, tetapi hindari)")  # [4]
```

**Output:**

```text
=== TABUNGAN SITI ===
Rekening Siti: saldo Rp1000000
Bunga bulan ini: Rp20000
Rekening Siti: saldo Rp1020000

=== DIBACA DARI LUAR KELAS ===
Lewat pintu resmi  : Rp1020000
Langsung ke atribut: Rp1020000 (bisa, tetapi hindari)
```

Penjelasan:

- **[1]** `_saldo` ditulis dengan satu garis bawah. Artinya: "jangan disentuh dari luar, tetapi kelas anak boleh".
- **[2]** Kode di luar kelas membaca saldo lewat property `saldo`.
- **[3]** `RekeningTabungan` adalah kelas anak, jadi ia wajar memakai dan mengubah `_saldo` secara langsung. Bunga 2% dari Rp1.000.000 adalah Rp20.000.
- **[4]** Secara teknis, kode di luar kelas pun **bisa** membaca `_saldo`. Python tidak menghalangi, karena garis bawah hanyalah kesepakatan. Programmer yang baik menghormati kesepakatan itu.

> [!WARNING]
> Jangan memakai **dua** garis bawah (`__saldo`) untuk atribut yang ingin dipakai kelas anak. *Name mangling* dari Pertemuan 04 mengubah namanya berdasarkan nama kelas, sehingga kelas anak gagal menemukannya. Lihat [Kesalahan 3](#kesalahan-3-memakai-__atribut-milik-induk).

## 6. Kelas Akar `object`, `isinstance()`, dan `issubclass()`

File: [`contoh/contoh06_kelas_akar_dan_cek_tipe.py`](contoh/contoh06_kelas_akar_dan_cek_tipe.py)

```python
class AlatMusik:  # [1] tidak menulis induk -> otomatis mewarisi object
    """Kelas induk semua alat musik."""

    def __init__(self, nama: str):
        self._nama = nama

    def __str__(self) -> str:  # [2] override __str__ bawaan object
        return f"Alat musik {self._nama}"


class Gitar(AlatMusik):
    """Gitar adalah AlatMusik. Tidak menambah apa pun."""


class Drum(AlatMusik):
    """Drum adalah AlatMusik. Tidak menambah apa pun."""


def ya_tidak(nilai: bool) -> str:
    return "ya" if nilai else "tidak"


def main():
    gitar = Gitar("gitar akustik")
    drum = Drum("drum elektrik")

    print("=== TEKS OBJEK ===")
    print(gitar)  # [3] memanggil __str__ warisan dari AlatMusik
    print(drum)

    print()
    print("=== CEK TIPE OBJEK ===")
    print(f"gitar adalah Gitar?        {ya_tidak(isinstance(gitar, Gitar))}")  # [4]
    print(f"gitar adalah AlatMusik?    {ya_tidak(isinstance(gitar, AlatMusik))}")
    print(f"gitar adalah Drum?         {ya_tidak(isinstance(gitar, Drum))}")
    print(f"gitar termasuk kelas akar? {ya_tidak(isinstance(gitar, object))}")
    print(f"Kelas persis gitar: {type(gitar).__name__}")  # [5]
    print(f"Kelas persis gitar = AlatMusik? {ya_tidak(type(gitar) is AlatMusik)}")

    print()
    print("=== CEK HUBUNGAN KELAS ===")
    print(f"Gitar turunan AlatMusik? {ya_tidak(issubclass(Gitar, AlatMusik))}")  # [6]
    print(f"AlatMusik turunan Gitar? {ya_tidak(issubclass(AlatMusik, Gitar))}")

    print()
    print("=== KESAMAAN BAWAAN DARI KELAS AKAR ===")
    kembaran = Gitar("gitar akustik")  # isi sama, tetapi objek berbeda
    print(f"gitar sama dengan kembarannya? {ya_tidak(gitar == kembaran)}")  # [7]
    print(f"gitar sama dengan dirinya?     {ya_tidak(gitar == gitar)}")
```

**Output:**

```text
=== TEKS OBJEK ===
Alat musik gitar akustik
Alat musik drum elektrik

=== CEK TIPE OBJEK ===
gitar adalah Gitar?        ya
gitar adalah AlatMusik?    ya
gitar adalah Drum?         tidak
gitar termasuk kelas akar? ya
Kelas persis gitar: Gitar
Kelas persis gitar = AlatMusik? tidak

=== CEK HUBUNGAN KELAS ===
Gitar turunan AlatMusik? ya
AlatMusik turunan Gitar? tidak

=== KESAMAAN BAWAAN DARI KELAS AKAR ===
gitar sama dengan kembarannya? tidak
gitar sama dengan dirinya?     ya
```

Penjelasan:

- **[1]** `class AlatMusik:` sama artinya dengan `class AlatMusik(object):`. Setiap kelas Python berakar pada `object`.
- **[2]** `object` sudah punya `__str__` bawaan. Menulis `__str__` di `AlatMusik` berarti meng-*override* versi bawaan itu. Tanpa *override*, `print(gitar)` mencetak teks seperti `<__main__.Gitar object at 0x7f3a2c1b9d90>`, dengan angka yang berubah setiap kali program dijalankan.
- **[3]** `Gitar` tidak menulis `__str__`, jadi memakai versi warisan dari `AlatMusik`.
- **[4]** `isinstance(objek, Kelas)` menjawab apakah objek termasuk kelas itu **atau turunannya**. Gitar termasuk `Gitar`, termasuk `AlatMusik`, dan termasuk `object`, tetapi bukan `Drum`.
- **[5]** `type(objek)` hanya melihat kelas **persisnya**. Karena itu, `type(gitar) is AlatMusik` bernilai salah, walaupun gitar adalah alat musik. Untuk memeriksa jenis objek, utamakan `isinstance()`.
- **[6]** `issubclass(A, B)` membandingkan dua **kelas**, bukan objek: "apakah A turunan B?". Arahnya hanya ke atas.
- **[7]** `==` bawaan dari `object` hanya bernilai benar untuk objek yang **sama persis**. Dua gitar dengan isi sama tetap dianggap berbeda. Cara mengubah aturan ini dibahas di Pertemuan 12.

## 7. is-a atau has-a?

File: [`contoh/contoh07_is_a_dan_has_a.py`](contoh/contoh07_is_a_dan_has_a.py)

Contoh ini membandingkan dua rancangan untuk "mobil dan mesinnya".

```python
class Mesin:
    """Mesin kendaraan dengan kapasitas tertentu (cc)."""

    def __init__(self, cc: int):
        self._cc = cc

    def hidupkan(self) -> str:
        return f"Mesin {self._cc} cc menyala"


class MobilKeliru(Mesin):  # [1] KELIRU: mobil dianggap "adalah" mesin
    """Rancangan keliru: mobil mewarisi mesin hanya demi memakai hidupkan()."""

    def __init__(self, nama: str, cc: int):
        super().__init__(cc)
        self._nama = nama

    def jalan(self) -> str:
        return f"{self._nama}: {self.hidupkan()}"


class MobilTepat:  # [2] TEPAT: mobil "punya" mesin
    """Rancangan tepat: mobil MENYIMPAN objek Mesin sebagai atribut."""

    def __init__(self, nama: str, mesin: Mesin):
        self._nama = nama
        self._mesin = mesin  # [3] has-a: atribut berisi objek lain

    def jalan(self) -> str:
        return f"{self._nama}: {self._mesin.hidupkan()}"  # [4] tugas diteruskan

    def ganti_mesin(self, mesin_baru: Mesin):  # [5] bagiannya bisa diganti
        self._mesin = mesin_baru
```

**Output:**

```text
=== RANCANGAN KELIRU: MOBIL MEWARISI MESIN ===
Avanza: Mesin 1300 cc menyala
Avanza adalah Mesin? ya (janggal!)

=== RANCANGAN TEPAT: MOBIL PUNYA MESIN ===
Xenia: Mesin 1300 cc menyala
Setelah ganti mesin -> Xenia: Mesin 1500 cc menyala
```

Penjelasan:

- **[1]** `MobilKeliru` mewarisi `Mesin` hanya agar bisa memakai `hidupkan()`. Programnya berjalan, tetapi `isinstance(avanza, Mesin)` menjawab "ya". Menurut program, Avanza **adalah** sebuah mesin. Janggal!
- **[2]** `MobilTepat` tidak mewarisi apa pun. Ia **menyimpan** objek `Mesin`.
- **[3]** Inilah hubungan *has-a*, wujudnya sama seperti relasi antarkelas di Pertemuan 05.
- **[4]** Saat mobil diminta jalan, ia **meneruskan** tugas menghidupkan mesin ke objek mesinnya. Teknik ini disebut **delegasi**.
- **[5]** Karena mesin hanyalah atribut, mesin bisa diganti kapan saja. `MobilKeliru` tidak bisa melakukannya, karena mesinnya adalah dirinya sendiri.

Sebelum menulis `class X(Y)`, ucapkan "X **adalah** Y". Jika kalimatnya janggal, gunakan atribut (*has-a*). Prinsip ini dikenal sebagai ***composition over inheritance***.

## 8. Pewarisan Ganda dan MRO

File: [`contoh/contoh08_pewarisan_ganda.py`](contoh/contoh08_pewarisan_ganda.py)

> [!NOTE]
> Contoh ini **khusus Python**. Java tidak mengizinkan satu kelas punya dua induk. Padanannya di Java dibahas di [Jembatan Python ↔ Java](../jembatan-python-java.md).

Python mengizinkan satu kelas punya **lebih dari satu** induk. Mobil amfibi, misalnya, adalah kendaraan darat sekaligus kendaraan air.

```python
class KendaraanDarat:
    """Kendaraan yang berjalan di jalan raya."""

    def jalan_di_darat(self) -> str:
        return "melaju di jalan raya"

    def info(self) -> str:
        return "Saya kendaraan darat"


class KendaraanAir:
    """Kendaraan yang berlayar di air."""

    def berlayar(self) -> str:
        return "berlayar di sungai"

    def info(self) -> str:
        return "Saya kendaraan air"


class MobilAmfibi(KendaraanDarat, KendaraanAir):  # [1] dua induk sekaligus
    """Mobil amfibi adalah kendaraan darat SEKALIGUS kendaraan air."""

    def __init__(self, nama: str):
        self._nama = nama

    def demo(self) -> str:
        return f"{self._nama} {self.jalan_di_darat()}, lalu {self.berlayar()}"


class PerahuBeroda(KendaraanAir, KendaraanDarat):  # [2] urutan induk dibalik
    """Sama-sama punya dua induk, tetapi KendaraanAir ditulis lebih dulu."""
```

**Output:**

```text
=== SATU OBJEK, DUA INDUK ===
Amfibi Mahakam melaju di jalan raya, lalu berlayar di sungai
Termasuk KendaraanDarat? ya
Termasuk KendaraanAir?   ya

=== METHOD BERNAMA SAMA: info() ===
MobilAmfibi  : Saya kendaraan darat
PerahuBeroda : Saya kendaraan air

=== URUTAN PENCARIAN METHOD (MRO) ===
MobilAmfibi  : MobilAmfibi -> KendaraanDarat -> KendaraanAir -> object
PerahuBeroda : PerahuBeroda -> KendaraanAir -> KendaraanDarat -> object
```

Penjelasan:

- **[1]** Induk-induknya ditulis berderet, dipisah koma. `MobilAmfibi` mewarisi `jalan_di_darat()` **dan** `berlayar()`.
- **[2]** `PerahuBeroda` punya dua induk yang sama, tetapi urutannya dibalik. `PerahuBeroda()` bisa dibuat tanpa argumen karena tidak ada kelas yang menulis `__init__`.
- **[3]** (di fungsi bantu `urutan_mro()`) Atribut `__mro__` berisi urutan kelas yang diperiksa Python saat mencari sebuah method. Cara lain melihatnya: `MobilAmfibi.mro()`.

Kedua induk punya `info()`. Python mencarinya mengikuti MRO: kelas itu sendiri dulu, lalu induk **paling kiri**, lalu induk berikutnya, dan terakhir `object`. Karena itu, `MobilAmfibi` memakai `info()` milik `KendaraanDarat`, sedangkan `PerahuBeroda` memakai milik `KendaraanAir`.

> [!WARNING]
> Pewarisan ganda mudah membingungkan, terutama jika kedua induk punya `__init__` sendiri. Cukup pahami konsep dan cara membaca MRO. Dalam praktik, pewarisan tunggal ditambah *has-a* biasanya lebih jelas.

## 9. Studi Kasus KedaiKita

File: [`studi-kasus/menu.py`](studi-kasus/menu.py) dan [`studi-kasus/main.py`](studi-kasus/main.py)

Rancangan dan diagramnya sudah dibahas di [halaman konsep](../README.md#10-studi-kasus-kedaikita-makanan-dan-minuman).

**Apa yang berubah dibanding Pertemuan 05/06?**

- `menu.py` kini berisi kelas induk `Menu` dan dua kelas anak: `Makanan` (dengan `level_pedas` 0 sampai 5) dan `Minuman` (dengan `dingin`).
- Kelas `Menu` sendiri tidak berubah, kecuali *docstring*-nya.
- `main.py` membuat semua menu sebagai `Makanan` atau `Minuman`, lalu menambah bagian "CEK PEWARISAN" dan "MENAMBAH MENU BARU".
- `pesanan.py`, `kedai.py`, `pelanggan.py`, dan `utilitas.py` **tidak berubah sama sekali**.

Berikut dua kelas anak di `menu.py`:

```python
class Makanan(Menu):
    """Menu kategori makanan. Tambahan: level pedas 0 sampai 5."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int = 0,
                 level_pedas: int = 0):
        # Panggil konstruktor induk. Kategori diisi otomatis "Makanan".
        super().__init__(kode, nama, harga, "Makanan", stok)
        self.level_pedas = level_pedas  # lewat setter, jadi ikut divalidasi

    @property
    def level_pedas(self) -> int:
        return self._level_pedas

    @level_pedas.setter
    def level_pedas(self, nilai: int):
        if nilai < 0 or nilai > 5:
            raise ValueError("Level pedas harus 0 sampai 5")
        self._level_pedas = nilai

    def __str__(self) -> str:
        # Override: pakai teks dari induk, lalu tambahkan info pedas
        return f"{super().__str__()} | pedas level {self._level_pedas}"


class Minuman(Menu):
    """Menu kategori minuman. Tambahan: disajikan dingin atau panas."""

    def __init__(self, kode: str, nama: str, harga: int, stok: int = 0,
                 dingin: bool = True):
        super().__init__(kode, nama, harga, "Minuman", stok)
        self._dingin = dingin

    @property
    def dingin(self) -> bool:
        return self._dingin

    def __str__(self) -> str:
        suhu = "dingin" if self._dingin else "panas"
        return f"{super().__str__()} | {suhu}"
```

- **Konstruktor anak** menerima data tanpa kategori. Kategori `"Makanan"`/`"Minuman"` dikirim otomatis ke `super().__init__(...)`. Semua validasi milik `Menu` (stok tidak negatif, harga lebih dari 0) tetap berjalan, karena dikerjakan oleh konstruktor induk.
- **`self.level_pedas = level_pedas`** sengaja memakai *setter*, bukan `self._level_pedas`, agar nilai 0 sampai 5 ikut diperiksa sejak objek dibuat.
- **`__str__` di-override** dengan gaya "memperluas": teks lengkap dari `Menu` diambil lewat `super().__str__()`, lalu ditambah keterangan pedas atau suhu.

Di `main.py`, fungsi `siapkan_kedai()` kini membuat lima menu sebagai objek kelas anak, misalnya `Minuman("M01", "Kopi Susu Gula Aren", 18000, 20, True)` dan `Makanan("M03", "Nasi Goreng Kampung", 25000, 15, 2)`. Bagian barunya:

```python
    print("=== CEK PEWARISAN ===")
    kopi = kedai.cari_menu("M01")
    nasi = kedai.cari_menu("M03")
    print(f"{kopi.nama} termasuk Minuman? {ya_tidak(isinstance(kopi, Minuman))}")
    print(f"{kopi.nama} termasuk Menu? {ya_tidak(isinstance(kopi, Menu))}")
    print(f"{nasi.nama} termasuk Minuman? {ya_tidak(isinstance(nasi, Minuman))}")
    print(f"Kategori {nasi.nama}: {nasi.kategori}")
    harga_promo = format_rupiah(kopi.harga_setelah_diskon(10))
    print(f"Diskon 10% untuk {kopi.nama} (method warisan Menu): {harga_promo}")
    print()

    print("=== MENAMBAH MENU BARU ===")
    kopi_tubruk = Minuman("M06", "Kopi Tubruk", 12000, 25, False)
    kedai.tambah_menu(kopi_tubruk)
    print(f"Ditambahkan: {kopi_tubruk}")
    try:
        Makanan("M07", "Seblak Super Pedas", 20000, 10, 9)
    except ValueError as e:
        print(f"Gagal menambah menu: {e}")
```

- **`kedai.tambah_menu(...)`** di `kedai.py` menerima parameter bertipe `Menu`. Kita mengirim `Minuman` dan `Makanan`, dan itu sah, karena keduanya **adalah** `Menu`. Hal yang sama berlaku untuk `Pesanan.tambah_item(menu, jumlah)`.
- **`isinstance(kopi, Menu)`** bernilai benar walaupun kopi dibuat dari kelas `Minuman`.
- **`kopi.harga_setelah_diskon(10)`** dan **`nasi.kategori`** tidak ditulis di kelas anak. Keduanya warisan dari `Menu`.
- **Seblak level 9** ditolak oleh *setter* `level_pedas`, lalu ditangkap dengan `try`/`except` seperti di Pertemuan 04.

Jalankan `python main.py` dari dalam folder `studi-kasus` (lihat [Persiapan](#persiapan)).

**Output:**

```text
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 20 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 15 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 12 | pedas level 0

=== CEK PEWARISAN ===
Kopi Susu Gula Aren termasuk Minuman? ya
Kopi Susu Gula Aren termasuk Menu? ya
Nasi Goreng Kampung termasuk Minuman? tidak
Kategori Nasi Goreng Kampung: Makanan
Diskon 10% untuk Kopi Susu Gula Aren (method warisan Menu): Rp16.200

=== MENAMBAH MENU BARU ===
Ditambahkan: [M06] Kopi Tubruk (Minuman) - Rp12.000 | stok 25 | panas
Gagal menambah menu: Level pedas harus 0 sampai 5

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P001
Pelanggan   : Budi Santoso
----------------------------------------
2 x Kopi Susu Gula Aren         Rp36.000
1 x Nasi Goreng Kampung         Rp25.000
----------------------------------------
TOTAL                           Rp61.000
========================================

========================================
KEDAIKITA - STRUK PESANAN
========================================
No. Pesanan : P002
Pelanggan   : Siti Aminah
----------------------------------------
1 x Kopi Tubruk                 Rp12.000
2 x Pisang Goreng Keju          Rp30.000
----------------------------------------
TOTAL                           Rp42.000
========================================

=== SETELAH TRANSAKSI ===
=== MENU KedaiKita ===
[M01] Kopi Susu Gula Aren (Minuman) - Rp18.000 | stok 18 | dingin
[M02] Es Teh Manis (Minuman) - Rp8.000 | stok 30 | dingin
[M03] Nasi Goreng Kampung (Makanan) - Rp25.000 | stok 14 | pedas level 2
[M04] Mie Goreng Jawa (Makanan) - Rp23.000 | stok 10 | pedas level 1
[M05] Pisang Goreng Keju (Makanan) - Rp15.000 | stok 10 | pedas level 0
[M06] Kopi Tubruk (Minuman) - Rp12.000 | stok 24 | panas
Jumlah pesanan tercatat: 2
```

Perhatikan daftar menu. Method `tampilkan_menu()` di `kedai.py` hanya menulis `print(menu)` untuk setiap menu, tanpa tahu jenisnya. Namun setiap baris tetap tampil dengan keterangan yang tepat: makanan dengan level pedas, minuman dengan suhu. Setiap objek memakai `__str__` miliknya sendiri (dibahas tuntas di Pertemuan 09). Di struk, `kurangi_stok()` warisan `Menu` juga bekerja sama baiknya untuk makanan maupun minuman.

> [!TIP]
> **Coba sendiri:**
> 1. Di `siapkan_kedai()`, tambahkan `kedai.tambah_menu(Minuman("M07", "Teh Tarik", 12000, 20, False))`. Tanpa mengubah kelas lain, apakah menu itu langsung tampil lengkap?
> 2. Ubah level pedas Mie Goreng Jawa dari 1 menjadi 6. Apa yang terjadi, dan mengapa programnya berhenti?

<details>
<summary>Lihat jawaban</summary>

1. Ya. Baris `[M07] Teh Tarik (Minuman) - Rp12.000 | stok 20 | panas` langsung muncul di daftar menu. `Kedai` tidak perlu diubah, karena Teh Tarik adalah `Menu`.
2. Program berhenti dengan `ValueError: Level pedas harus 0 sampai 5`. *Setter* `level_pedas` menolak nilai 6. Berbeda dengan Seblak, pembuatan Mie Goreng Jawa di `siapkan_kedai()` tidak dibungkus `try`/`except`, sehingga penolakannya menghentikan program.

</details>

## 10. Kesalahan Umum dan Cara Membaca Pesan Error

Ingat, pesan error Python dibaca **dari bawah ke atas**. Baris paling bawah menyebut jenis error dan penyebabnya. Baris di atasnya menunjukkan lokasinya.

### Kesalahan 1: Lupa memanggil `super().__init__()`

```python
class Kendaraan:
    def __init__(self, merek: str):
        self._merek = merek

    def info(self) -> str:
        return f"Kendaraan {self._merek}"


class Motor(Kendaraan):
    def __init__(self, merek: str, transmisi: str):
        self._transmisi = transmisi  # lupa super().__init__(merek)


beat = Motor("Honda Beat", "matic")
print(beat.info())
```

Pesan error-nya:

```text
Traceback (most recent call last):
  File "e1.py", line 15, in <module>
    print(beat.info())
  File "e1.py", line 6, in info
    return f"Kendaraan {self._merek}"
AttributeError: 'Motor' object has no attribute '_merek'
```

**Artinya:** objek motor berhasil dibuat, tetapi konstruktor `Kendaraan` tidak pernah dijalankan, sehingga atribut `_merek` tidak pernah ada. Error baru muncul belakangan, saat `info()` membaca `_merek`. Inilah yang membuat kesalahan ini licin. **Perbaikan:** tulis `super().__init__(merek)` di baris pertama `__init__` milik `Motor`.

### Kesalahan 2: Argumen untuk konstruktor induk tidak lengkap

Misalkan konstruktor `Kendaraan` menerima `merek` dan `plat_nomor`, tetapi `__init__` milik `Motor` hanya menulis `super().__init__(merek)`. Pesan error-nya:

```text
TypeError: Kendaraan.__init__() missing 1 required positional argument: 'plat_nomor'
```

**Artinya:** `super().__init__(...)` memanggil konstruktor `Kendaraan`, yang butuh `merek` **dan** `plat_nomor`. **Perbaikan:** `super().__init__(merek, plat_nomor)`. Kirim semua data yang dibutuhkan induk.

### Kesalahan 3: Memakai `__atribut` milik induk

```python
class RekeningBank:
    def __init__(self, pemilik: str, saldo_awal: int):
        self._pemilik = pemilik
        self.__saldo = saldo_awal  # dua garis bawah


class RekeningTabungan(RekeningBank):
    def tambah_bunga(self) -> int:
        bunga = self.__saldo * 2 // 100
        self.__saldo += bunga
        return bunga
```

```text
AttributeError: 'RekeningTabungan' object has no attribute '_RekeningTabungan__saldo'. Did you mean: '_RekeningBank__saldo'?
```

**Artinya:** karena *name mangling*, `self.__saldo` di kelas induk disimpan sebagai `_RekeningBank__saldo`. Di kelas anak, `self.__saldo` diubah menjadi `_RekeningTabungan__saldo`, yang tidak pernah ada. Python versi baru bahkan menebak maksudmu (*Did you mean*). **Perbaikan:** pakai **satu** garis bawah (`self._saldo`) untuk atribut yang boleh dipakai kelas anak.

### Kesalahan 4: Salah ketik nama method saat override

```python
class TiketVIP(Tiket):
    def hitung_byar(self, jumlah: int) -> int:  # salah ketik!
        return super().hitung_bayar(jumlah) + 25000 * jumlah


vip = TiketVIP("Festival Musik Kampus", 120000)
print(f"VIP: Rp{vip.hitung_bayar(3)}")
```

Tidak ada pesan error. Hasilnya:

```text
VIP: Rp360000
```

**Artinya:** `hitung_byar` dianggap method **baru**, bukan *override*. Saat `vip.hitung_bayar(3)` dipanggil, Python memakai versi warisan `Tiket`, sehingga biaya layanan tidak ikut dihitung. Seharusnya hasilnya Rp435000. Python tidak punya pemeriksa *override* seperti `@Override` di Java. **Perbaikan:** periksa ejaan nama method, dan uji hasilnya dengan angka yang kamu hitung sendiri.

### Kesalahan 5: Lupa tanda kurung pada `super`

```python
        super.__init__(merek)
```

```text
TypeError: descriptor '__init__' requires a 'super' object but received a 'str'
```

**Artinya:** untuk method biasa, misalnya `super.info()`, pesannya menjadi `AttributeError: type object 'super' has no attribute 'info'`. Di Python, `super` harus **dipanggil** dulu dengan `super()` agar menghasilkan "jembatan" ke kelas induk. **Perbaikan:** `super().__init__(merek)` dan `super().info()`. Di Java, kebiasaannya berbeda: `super(...)` untuk konstruktor dan `super.info()` tanpa kurung untuk method.

> [!NOTE]
> Bunyi dan tampilan pesan error bisa sedikit berbeda antarversi Python. Python 3.11 ke atas, misalnya, menambahkan tanda `^^^^` di bawah bagian yang bermasalah. Fokuslah pada **jenis error** (`AttributeError`, `TypeError`) dan kata kuncinya.

## 📝 Ringkasan Sintaks

| Konsep | Sintaks Python | Contoh |
|---|---|---|
| Kelas anak | `class Anak(Induk):` | `class Makanan(Menu):` |
| Memanggil konstruktor induk | `super().__init__(...)` | `super().__init__(kode, nama, harga, "Makanan", stok)` |
| Menambah atribut | `self._atribut = nilai` setelah `super()` | `self._dingin = dingin` |
| *Override* method | `def` dengan nama dan parameter sama | `def __str__(self) -> str:` |
| Memakai versi induk | `super().nama_method(...)` | `super().__str__()` |
| Atribut untuk kelas anak | satu garis bawah | `self._saldo` |
| Cek objek termasuk kelas | `isinstance(objek, Kelas)` | `isinstance(kopi, Menu)` |
| Cek kelas turunan | `issubclass(A, B)` | `issubclass(Gitar, AlatMusik)` |
| Kelas persis sebuah objek | `type(objek)` | `type(gitar).__name__` |
| Pewarisan ganda | `class Anak(Induk1, Induk2):` | `class MobilAmfibi(KendaraanDarat, KendaraanAir):` |
| Melihat MRO | `Kelas.__mro__` atau `Kelas.mro()` | `MobilAmfibi.__mro__` |

## ➡️ Langkah Berikutnya

- Bandingkan dengan Java: [Jembatan Python ↔ Java](../jembatan-python-java.md)
- Kerjakan [Latihan](../latihan.md), lalu uji pemahamanmu dengan [Kuis](../kuis.md).

---

[⬅️ Konsep](../README.md) · [☕ Praktik Java](../java/README.md) · [Jembatan Python ↔ Java ➡️](../jembatan-python-java.md)
