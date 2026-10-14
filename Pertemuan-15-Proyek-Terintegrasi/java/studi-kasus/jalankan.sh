#!/bin/sh
# Menjalankan aplikasi kasir KedaiKita (versi Java) di macOS/Linux.
#
# Pemakaian:
#     ./jalankan.sh          -> mode interaktif (kasir mengetik pilihan)
#     ./jalankan.sh --demo   -> mode demo (tanpa input)
#
# Skrip ini pindah ke foldernya sendiri (agar folder data/ ditemukan),
# mengompilasi semua file di src/kedaikita ke folder out/, lalu menjalankan
# kelas kedaikita.Main dengan argumen yang sama.
cd "$(dirname "$0")" || exit 1
javac -d out src/kedaikita/*.java || exit 1
java -cp out kedaikita.Main "$@"
