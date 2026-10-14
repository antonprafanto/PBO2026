# Kuis — Pertemuan 04: Enkapsulasi

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 05 ➡️](../Pertemuan-05-Relasi-Antar-Kelas/README.md)

**Petunjuk:** ada 10 soal pilihan ganda. Kerjakan dulu semuanya **tanpa** membuka jawaban, catat pilihanmu, baru cocokkan. Target: minimal 8 benar.

---

### Soal 1

Manakah pernyataan yang paling tepat menggambarkan **enkapsulasi**?

- A. Membuat banyak objek dari satu kelas yang sama
- B. Menyatukan data dan method dalam satu kelas, lalu membatasi akses langsung ke data sehingga data hanya diubah lewat pintu resmi
- C. Mewariskan atribut dan method dari kelas induk ke kelas anak
- D. Menyembunyikan seluruh isi kelas sehingga objeknya sama sekali tidak bisa dipakai dari luar

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: enkapsulasi punya dua sisi, yaitu **membungkus** data bersama method yang mengolahnya dan **menyembunyikan** data dari akses langsung. Pilihan A adalah instansiasi (Pertemuan 02), sedangkan C adalah pewarisan (Pertemuan 07). Pilihan D berlebihan: enkapsulasi tetap menyediakan pintu resmi berupa method publik, karena objek yang sama sekali tidak bisa dipakai tentu tidak berguna.

</details>

### Soal 2

Di mesin ATM, kamu tidak bisa membuka brankas berisi uang. Kamu hanya bisa memakai menu "tarik tunai", yang memeriksa PIN, saldo, dan batas harian sebelum uang keluar. Dalam analogi enkapsulasi, menu "tarik tunai" setara dengan ...

- A. atribut privat
- B. nama kelas
- C. method publik yang menjaga aturan
- D. paket (*package*)

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: menu "tarik tunai" adalah pintu resmi yang boleh dipakai siapa saja, tetapi selalu memeriksa aturan sebelum mengubah data (saldo). Itulah peran method publik penjaga aturan. Uang di dalam brankas justru setara dengan **atribut privat** (pilihan A), yaitu data yang tidak boleh disentuh langsung.

</details>

### Soal 3

Di Java, sebuah field ditulis `private int saldo;` di dalam kelas `Rekening`. Kode mana yang boleh mengakses field `saldo` secara langsung?

- A. Hanya kode di dalam kelas `Rekening`
- B. Semua kelas di paket yang sama
- C. Kelas `Rekening` dan semua kelas anaknya
- D. Semua kelas, asalkan ditulis di file yang sama dengan `Rekening`

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: `private` adalah tingkat akses paling ketat, yaitu hanya untuk kode di dalam kelas itu sendiri. Pilihan B menggambarkan akses *default* (tanpa kata kunci). Pilihan C mendekati `protected` (yang sebenarnya juga terbuka untuk satu paket). Pilihan D adalah jebakan: di contoh-contoh kita, `main` berada di file yang sama dengan kelas pembantunya, tetapi tetap ditolak dengan pesan *has private access*, karena `main` ada di kelas yang **lain**.

</details>

### Soal 4

Di dalam kelas `Rekening` (Python), sebuah atribut ditulis `self.__saldo`. Pernyataan yang benar adalah ...

- A. Atribut itu benar-benar terkunci dan mustahil dibaca dari luar kelas
- B. Python menolak menjalankan program karena nama atribut tidak boleh diawali garis bawah
- C. Atribut itu otomatis menjadi atribut kelas, bukan atribut objek
- D. Python mengganti namanya menjadi `_Rekening__saldo`, dan nama itu tetap bisa diakses dari luar kelas

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: dua garis bawah di depan nama memicu *name mangling*. Python diam-diam menyimpan atribut itu dengan nama `_Rekening__saldo`. Membaca `rekening.__saldo` dari luar memang gagal (`AttributeError`), tetapi `rekening._Rekening__saldo` tetap berhasil. Jadi pilihan A keliru: *name mangling* bukan fitur keamanan. Pilihan B dan C juga tidak benar, karena nama bergaris bawah itu sah dan tetap menjadi milik objek.

</details>

### Soal 5

Perhatikan kode berikut.

**Python:**

```python
class Penduduk:
    def __init__(self, nik):
        self._nik = nik

    @property
    def nik(self):
        return self._nik


warga = Penduduk("1234567890123456")
warga.nik = "9999999999999999"
print(warga.nik)
```

**Java:**

```java
class Penduduk {
    private String nik;

    public Penduduk(String nik) {
        this.nik = nik;
    }

    public String getNik() {
        return nik;
    }
}

// di dalam main:
Penduduk warga = new Penduduk("1234567890123456");
warga.setNik("9999999999999999");
System.out.println(warga.getNik());
```

Apa yang terjadi?

- A. Tercetak `9999999999999999`
- B. Tercetak `1234567890123456`, karena perubahannya diabaikan diam-diam
- C. Terjadi error: Python menolak saat program berjalan (`AttributeError`), Java menolak saat kompilasi (`cannot find symbol`)
- D. Kedua program sama-sama ditolak saat kompilasi

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: `nik` hanya punya getter, tanpa setter, sehingga bersifat read-only. Di Python, `warga.nik = ...` berhenti dengan `AttributeError: property 'nik' of 'Penduduk' object has no setter` saat baris itu dijalankan. Di Java, method `setNik` tidak pernah dibuat, sehingga compiler menolak dengan `cannot find symbol`. Perubahan tidak diabaikan diam-diam (B), dan Python tidak memeriksa hal ini sebelum program berjalan (D).

</details>

### Soal 6

Perhatikan kode berikut.

**Python:**

```python
class Produk:
    def __init__(self, harga):
        self._harga = harga

    @property
    def harga(self):
        return self._harga

    @harga.setter
    def harga(self, nilai):
        if nilai <= 0:
            raise ValueError("Harga harus lebih dari 0")
        self._harga = nilai


p = Produk(-5000)
print(p.harga)
```

**Java:**

```java
class Produk {
    private int harga;

    public Produk(int harga) {
        this.harga = harga;
    }

    public int getHarga() {
        return harga;
    }

    public void setHarga(int harga) {
        if (harga <= 0) {
            throw new IllegalArgumentException("Harga harus lebih dari 0");
        }
        this.harga = harga;
    }
}

// di dalam main:
Produk p = new Produk(-5000);
System.out.println(p.getHarga());
```

Apa output-nya, dan mengapa?

- A. Error "Harga harus lebih dari 0", karena setter selalu dipanggil otomatis oleh konstruktor
- B. `-5000`, karena konstruktor menyimpan harga secara langsung tanpa melewati setter
- C. `0`, karena harga negatif otomatis diganti menjadi 0
- D. Error kompilasi, karena konstruktor tidak boleh mengisi field privat

<details>
<summary>Lihat jawaban</summary>

**Jawaban: B**

Pembahasan: setter memang memeriksa harga, tetapi konstruktor menulis langsung ke `self._harga` / `this.harga`. Setter tidak pernah dipanggil, sehingga harga -5000 lolos dan tercetak. Setter **tidak** dipanggil otomatis (A). Perbaikannya: di Python tulis `self.harga = harga`, di Java tulis `setHarga(harga);`. Pilihan D keliru, karena konstruktor adalah bagian dari kelas dan boleh mengisi field privatnya sendiri.

</details>

### Soal 7

Pada kelas `Menu` KedaiKita, stok **tidak** diberi setter. Stok hanya bisa berubah lewat `tambah_stok(jumlah)` / `tambahStok(jumlah)` dan `kurangi_stok(jumlah)` / `kurangiStok(jumlah)`. Apa alasan utamanya?

- A. Bahasa pemrograman tidak mengizinkan setter untuk bilangan bulat
- B. Setter selalu membuat program berjalan lebih lambat
- C. Stok tidak perlu dibaca dari luar kelas
- D. Method yang namanya bermakna tahu alasan perubahan (restok atau terjual), sehingga bisa menjaga aturan seperti "tidak boleh menjual melebihi stok"

<details>
<summary>Lihat jawaban</summary>

**Jawaban: D**

Pembahasan: setter hanya berbunyi "ubah stok menjadi X", sehingga kelas tidak tahu apakah stok berubah karena terjual, restok, atau salah ketik. Method penjaga aturan membawa makna dan bisa memeriksa aturannya masing-masing. Pilihan C keliru, karena stok tetap boleh **dibaca** lewat getter. Pilihan A dan B tidak benar.

</details>

### Soal 8

Ada dua cara mengurangi stok kopi sebanyak 2 porsi:

```text
Cara P: kopi.kurangi_stok(2)        (Java: kopi.kurangiStok(2))
Cara Q: jika stok kopi >= 2, ubah stok kopi menjadi stok - 2
```

Mana yang mengikuti prinsip ***tell, don't ask***?

- A. Cara P, karena objek kopi sendiri yang memeriksa aturan dan menolak jika stok tidak cukup
- B. Cara Q, karena pemanggil memeriksa aturan sendiri sebelum mengubah data
- C. Keduanya sama baiknya, asalkan hasil akhirnya benar
- D. Tidak ada, karena prinsip itu melarang memanggil method milik objek lain

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: *tell, don't ask* berarti **menyuruh** objek mengerjakan tugasnya, bukan **menanyakan** datanya lalu memutuskan di luar. Pada cara Q, aturan "stok tidak boleh minus" ditulis di luar kelas. Jika ada banyak tempat yang mengurangi stok, aturan itu harus ditulis berulang kali dan mudah terlupa. Selain itu, cara Q butuh setter stok yang justru membuka pintu bagi data rusak.

</details>

### Soal 9

Desain mana yang paling tepat untuk menyimpan **password** pada kelas `AkunPengguna`?

- A. Getter dan setter publik tanpa pemeriksaan, agar mudah dipakai
- B. Getter saja, agar password bisa ditampilkan di halaman profil
- C. Tanpa getter; password hanya bisa dicocokkan lewat method seperti `cek_password()` dan diganti lewat `ganti_password(lama, baru)`
- D. Atribut publik biasa, karena pemilik akun pasti merahasiakannya

<details>
<summary>Lihat jawaban</summary>

**Jawaban: C**

Pembahasan: tidak semua atribut perlu getter atau setter. Password tidak perlu (dan tidak boleh) dibaca dari luar, cukup **dicocokkan**. Penggantiannya pun harus lewat method penjaga aturan yang memeriksa password lama. Pilihan A dan D membuka data sepenuhnya, sedangkan pilihan B membocorkan password. Di aplikasi sungguhan, password bahkan disimpan dalam bentuk *hash*, bukan teks asli.

</details>

### Soal 10

Setter `volume` pada kelas `Televisi` menolak nilai di luar 0–100 dengan exception, seperti contoh 03. Perhatikan kode berikut.

**Python:**

```python
tv = Televisi("Polytron")   # volume awal 10
try:
    tv.volume = 50
    tv.volume = 150
    tv.volume = 30
except ValueError as e:
    print(f"Ditolak: {e}")
print(tv.volume)
```

**Java:**

```java
Televisi tv = new Televisi("Polytron"); // volume awal 10
try {
    tv.setVolume(50);
    tv.setVolume(150);
    tv.setVolume(30);
} catch (IllegalArgumentException e) {
    System.out.println("Ditolak: " + e.getMessage());
}
System.out.println(tv.getVolume());
```

Angka berapa yang tercetak di baris **terakhir**?

- A. 50
- B. 30
- C. 150
- D. 10

<details>
<summary>Lihat jawaban</summary>

**Jawaban: A**

Pembahasan: volume 50 berhasil disimpan. Saat 150 ditolak, exception dilempar dan **sisa** blok `try` dilewati, sehingga baris yang mengisi 30 tidak pernah dijalankan (B salah). Blok `except`/`catch` mencetak `Ditolak: Volume harus 0-100, bukan 150`, lalu baris terakhir mencetak 50. Nilai 150 tidak pernah tersimpan (C), dan perubahan ke 50 yang sudah berhasil tidak dibatalkan (D).

</details>

---

## Hitung Skormu

| Jumlah benar | Artinya | Saran |
|---|---|---|
| 8 – 10 | Mantap! Konsep enkapsulasi sudah kuat | Lanjut ke [Pertemuan 05](../Pertemuan-05-Relasi-Antar-Kelas/README.md) |
| 5 – 7 | Sudah paham sebagian | Baca ulang bagian konsep yang soalnya kamu jawab salah, lalu kerjakan Latihan 3 dan 5 |
| 0 – 4 | Perlu mengulang | Baca ulang [konsep](README.md) pelan-pelan dan jalankan semua contoh di halaman praktik sambil mencoba "Coba sendiri" |

---

[⬅️ Latihan](latihan.md) · [🏠 Beranda](../README.md) · [Pertemuan 05 ➡️](../Pertemuan-05-Relasi-Antar-Kelas/README.md)
