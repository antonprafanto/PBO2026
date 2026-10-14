#!/bin/sh
# Menjalankan unit test KedaiKita (versi Java) di macOS/Linux.
#
# Pemakaian:
#     ./uji.sh
#
# Skrip ini pindah ke foldernya sendiri, mengompilasi semua file di
# src/kedaikita ke folder out/, lalu menjalankan kelas kedaikita.UjiKedaiKita.
cd "$(dirname "$0")" || exit 1
javac -d out src/kedaikita/*.java || exit 1
java -cp out kedaikita.UjiKedaiKita "$@"
