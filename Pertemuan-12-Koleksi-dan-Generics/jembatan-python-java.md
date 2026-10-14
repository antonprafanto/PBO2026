# 🌉 Jembatan Python ↔ Java Pertemuan 12: Koleksi dan *Generics*

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)

Konsep koleksi **sama** di kedua bahasa: *list*, set, dan map, aturan urutan, aturan kesamaan, serta *generics*. Yang berbeda adalah cara menuliskannya, dan beberapa perbedaan kecil yang justru sering menjebak. Halaman ini membantumu membaca kode di kedua bahasa dan menjelaskan **mengapa** perbedaan itu ada.

Kode di halaman ini berupa potongan untuk dibandingkan, bukan program untuk dijalankan sendiri. Versi lengkap yang bisa dijalankan ada di halaman praktik [🐍 Python](python/README.md) dan [☕ Java](java/README.md).

## Tabel Perbandingan Cepat

| Konsep | Python | Java |
|---|---|---|
| *List* | `[a, b]` (kelas `list`) | `List<T> x = new ArrayList<>();` |
| Data tetap | *tuple* `(a, b)` | `List.of(a, b)` |
| Set | `{a, b}`, set kosong `set()` | `Set<T> x = new HashSet<>();` atau `TreeSet` |
| Map | `{k: v}` (kelas `dict`) | `Map<K, V> x = new HashMap<>();`, `LinkedHashMap`, `TreeMap` |
| Jumlah isi | `len(x)` | `x.size()` |
| Cek isi | `x in koleksi` | `koleksi.contains(x)`, `map.containsKey(k)` |
| Ambil nilai map | `d[k]` (`KeyError` jika tidak ada) | `m.get(k)` (`null` jika tidak ada) |
| Nilai cadangan | `d.get(k, 0)` | `m.getOrDefault(k, 0)` |
| Hapus dari map | `del d[k]` | `m.remove(k)` |
| Jelajah map | `for k, v in d.items():` | `for (Map.Entry<K, V> e : m.entrySet())` |
| Urutan map saat dijelajahi | `dict`: urutan masuk | `HashMap`: tidak dijamin; `LinkedHashMap`: urutan masuk; `TreeMap`: urut kunci |
| Urutkan, hasil *list* baru | `sorted(xs, key=...)` | salin dulu: `new ArrayList<>(xs)`, lalu `sort(...)` |
| Urutkan *list* itu sendiri | `xs.sort(key=...)` | `xs.sort(cmp)` atau `Collections.sort(xs)` |
| *Lambda* | `lambda p: p.harga` | `p -> p.getHarga()` |
| Urutan khusus | `key=lambda p: p.harga` | `Comparator.comparing(Produk::getHarga)` |
| Urutan terbalik | `reverse=True` | `.reversed()` |
| Kriteria kedua | `key` berupa *tuple* `(-p.rating, p.harga)` | `.thenComparing(...)` |
| Urutan alami | *method* `__lt__` | `implements Comparable<T>` + `compareTo` |
| Kesamaan isi | `a == b` (memanggil `__eq__`) | `a.equals(b)` |
| Objek yang sama persis | `a is b` | `a == b` |
| Kode *hash* | `__hash__` | `hashCode()` |
| Kelas generik | `class Kotak(Generic[T]):` | `class Kotak<T> { ... }` |
| Pemeriksaan tipe *generics* | tidak diperiksa saat berjalan (VS Code, mypy) | diperiksa *compiler* saat kompilasi |
| Angka di dalam koleksi | `int` biasa | kelas pembungkus `Integer` (*autoboxing*) |
| *Comprehension* | `[x for x in xs if syarat]` | perulangan `for` (atau *Stream*, bonus) |

## 1. Arti `==` Justru Terbalik

Kedua potongan berikut mirip bagian KESAMAAN OBJEK di `main.py` dan `Main.java` studi kasus.

**Python:**

```python
kopi_a = kedai.cari_menu("M01")
kopi_b = Minuman("M01", "Kopi Susu Gula Aren", 18000, 20)
print(kopi_a == kopi_b)   # True  -> memanggil __eq__ (kode sama)
print(kopi_a is kopi_b)   # False -> bukan objek yang sama persis
```

**Java:**

```java
Menu kopiA = kedai.cariMenu("M01");
Menu kopiB = new Minuman("M01", "Kopi Susu Gula Aren", 18000, 20);
System.out.println(kopiA.equals(kopiB)); // true  -> equals() (kode sama)
System.out.println(kopiA == kopiB);      // false -> bukan objek yang sama persis
```

**Mengapa berbeda?** Di Python, operator seperti `==` dan `<` adalah "jalan pintas" untuk memanggil *method* khusus (`__eq__`, `__lt__`) sehingga kelas bebas menentukan artinya. Java tidak mengizinkan kelas mengubah arti operator. Untuk objek, `==` di Java selalu berarti "objek yang sama persis", dan kesamaan isi harus ditanyakan lewat *method* `equals()`. Inilah sebabnya teks (`String`) dan `Integer` di Java dibandingkan dengan `equals()`.

## 2. Kunci yang Tidak Ada: `KeyError` atau `null`

**Python:**

```python
stok = {"pulpen": 12}
print(stok.get("pensil", 0))   # 0
print(stok["pensil"])          # KeyError: 'pensil'
```

**Java:**

```java
Map<String, Integer> stok = new HashMap<>();
stok.put("pulpen", 12);
System.out.println(stok.getOrDefault("pensil", 0)); // 0
System.out.println(stok.get("pensil"));             // null (tanpa error)
int jumlah = stok.get("pensil");                    // NullPointerException!
```

**Mengapa berbeda?** Python memilih "gagal dengan suara keras": kunci yang tidak ada langsung menjadi *exception*. `Map.get()` di Java memilih mengembalikan `null`. Masalahnya baru muncul belakangan, misalnya saat `null` itu dibuka menjadi `int`. Di kedua bahasa, cara teraman sama: periksa dulu (`in` / `containsKey`) atau pakai nilai cadangan (`get(k, 0)` / `getOrDefault(k, 0)`).

## 3. *Lambda* dan Fungsi sebagai Argumen

| | Python | Java |
|---|---|---|
| Satu parameter | `lambda p: p.harga` | `p -> p.getHarga()` |
| Dua parameter | `lambda a, b: ...` | `(a, b) -> Integer.compare(a.getHarga(), b.getHarga())` |
| Isi beberapa baris | tidak bisa (*lambda* hanya satu ekspresi) | bisa, dengan `{ ... return ...; }` |
| Fungsi yang sudah ada | langsung ditulis namanya: `key=len`, `key=ambil_harga` | *method reference*: `String::length`, `Produk::getHarga` |
| Bentuk "aturan" urutan | fungsi kunci (`key=`) | objek `Comparator` |

**Mengapa berbeda?** Di Python, fungsi adalah objek biasa yang bisa dikirim ke mana saja. Java membutuhkan sebuah *interface* sebagai "wadah" *lambda*. Contohnya `Comparator<T>` untuk aturan urutan dan `Function<T, R>` untuk mengubah T menjadi R (dipakai di Latihan 6). Python cukup meminta **kunci** lalu membandingkannya sendiri, sedangkan pembanding Java bisa langsung membandingkan dua objek.

## 4. Urutan Alami: Satu *Method* atau Satu *Interface*

Kedua potongan berikut diringkas dari kelas `Menu` di studi kasus (`menu.py` dan `Menu.java`).

**Python:**

```python
def __lt__(self, lain: "Menu") -> bool:
    if self._harga != lain._harga:
        return self._harga < lain._harga
    return self._kode < lain._kode
```

**Java:**

```java
public int compareTo(Menu lain) {
    if (harga != lain.harga) {
        return Integer.compare(harga, lain.harga);
    }
    return kode.compareTo(lain.kode);
}
```

`__lt__` menjawab **ya/tidak** ("apakah aku di depanmu?"), sedangkan `compareTo` menjawab dengan **angka** negatif, nol, atau positif. Java juga mewajibkan `implements Comparable<Menu>`. Tanpa itu, `Collections.sort(daftar)` ditolak saat kompilasi. Python baru mengeluh saat program berjalan: `TypeError: '<' not supported between instances of ...`.

## 5. Lupa *Hash*: Python Melindungi, Java Diam

| Situasi | Python | Java |
|---|---|---|
| Menulis `__eq__`/`equals()` **tanpa** *hash* | kelas otomatis *unhashable*: `TypeError` saat masuk set/dict | dikompilasi tanpa masalah, tetapi set bisa berisi data kembar |
| Kapan ketahuan | begitu objek dimasukkan ke set/dict | bisa tidak pernah ketahuan |

Python sengaja mencabut kode *hash* bawaan begitu `__eq__` ditulis agar kontrak "sama berarti *hash* sama" tidak dilanggar diam-diam. Java mempercayakan kontrak itu sepenuhnya kepada pemrogram. Karena itu, di Java biasakan menulis `equals()` dan `hashCode()` **selalu bersamaan**.

## 6. *Generics*: Petunjuk atau Aturan?

```python
kotak: Kotak[int] = Kotak("bukan angka")   # Python: tetap berjalan
```

```java
Kotak<Integer> kotak = new Kotak<>("bukan angka"); // Java: ditolak compiler
```

Baris Python di atas tetap berjalan, dan masalahnya hanya dilaporkan oleh alat bantu seperti VS Code atau mypy (lihat [praktik Python bagian 8](python/README.md#8-kelas-generik-dan-petunjuk-tipe)). Baris Java langsung ditolak saat kompilasi dengan pesan yang diawali `error: incompatible types: cannot infer type arguments for Kotak<>`.

Petunjuk tipe Python ditujukan untuk manusia dan alat bantu. Java menjadikannya aturan yang diperiksa sebelum program berjalan. Akibatnya, Java juga butuh kelas pembungkus: isi `< >` harus kelas sehingga angka disimpan sebagai `Integer`. Dari sinilah muncul jebakan khusus Java yang tidak ada di Python, yaitu `==` pada dua `Integer` di atas 127 dan `list.remove(1)` pada `List<Integer>` ([contoh 09 di praktik Java bagian 8](java/README.md#8-generics-dan-kelas-pembungkus-integer)).

## Yang Sama di Kedua Bahasa

- Empat wadah utama (*list*, data tetap, set, map) dengan ciri yang sama.
- Set dan map berbasis *hash* membutuhkan kontrak kesamaan + *hash* yang benar.
- Urutan isi set berbasis *hash* **tidak dijamin**, bahkan bisa berubah setiap kali program dijalankan.
- Pengurutan **stabil**: data yang setara tetap mempertahankan urutan aslinya. Python `sorted()` dan Java `List.sort()` sama-sama menjamin hal ini.
- Pola menghitung kemunculan dengan map: ambil nilai lama (cadangan 0), tambah 1, simpan lagi.
- *Output* studi kasus KedaiKita versi Python dan Java **identik**.

## Jebakan saat Pindah Bahasa

| Jika kamu terbiasa... | Lalu menulis di... | Jebakannya |
|---|---|---|
| Python | Java | Membandingkan `String` atau `Integer` dengan `==`. Pakai `equals()` |
| Python | Java | Mencetak `HashMap`/`HashSet` dan berharap urutannya seperti `dict`. Pakai `LinkedHashMap`/`TreeMap`, atau urutkan dulu |
| Python | Java | Menulis `List<int>`. Yang benar `List<Integer>` |
| Python | Java | `remove(1)` pada `List<Integer>` menghapus **indeks** 1. Untuk angka 1, tulis `remove(Integer.valueOf(1))` |
| Python | Java | Mengurutkan `List.of(...)` langsung (`UnsupportedOperationException`). Salin dulu ke `ArrayList` |
| Java | Python | Menulis `{}` untuk set kosong, padahal itu dict. Pakai `set()` |
| Java | Python | Mengira `d[k]` mengembalikan `None` untuk kunci yang tidak ada. Hasilnya `KeyError` |
| Java | Python | `hasil = daftar.sort()` lalu heran mengapa `hasil` berisi `None`. Pakai `sorted()` |
| Java | Python | Mengira petunjuk tipe `list[int]` akan menolak teks saat program berjalan |

---

[⬅️ Konsep](README.md) · [🐍 Python](python/README.md) · [☕ Java](java/README.md) · [Latihan ➡️](latihan.md)
