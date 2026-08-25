"""
Contoh Kode: Pola Bintang dengan Nested Loop
Kumpulan pola bintang dan angka menggunakan perulangan bersarang

Topik: BAB 6.6 - Perulangan Bersarang (Nested Loop)
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("KOLEKSI POLA BINTANG DAN ANGKA")
print("="*60)

# ============================================================
# POLA 1: PERSEGI
# ============================================================
print("\nPOLA 1: PERSEGI")
print("-"*60)
ukuran = 5
for i in range(ukuran):
    for j in range(ukuran):
        print("*", end=" ")
    print()

# ============================================================
# POLA 2: SEGITIGA SIKU-SIKU
# ============================================================
print("\nPOLA 2: SEGITIGA SIKU-SIKU")
print("-"*60)
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 3: SEGITIGA TERBALIK
# ============================================================
print("\nPOLA 3: SEGITIGA TERBALIK")
print("-"*60)
tinggi = 5
for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 4: SEGITIGA SAMA KAKI
# ============================================================
print("\nPOLA 4: SEGITIGA SAMA KAKI (PIRAMIDA)")
print("-"*60)
tinggi = 5
for i in range(1, tinggi + 1):
    # Cetak spasi
    for j in range(tinggi - i):
        print(" ", end=" ")
    # Cetak bintang
    for k in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 5: PIRAMIDA TERBALIK
# ============================================================
print("\nPOLA 5: PIRAMIDA TERBALIK")
print("-"*60)
tinggi = 5
for i in range(tinggi, 0, -1):
    # Cetak spasi
    for j in range(tinggi - i):
        print(" ", end=" ")
    # Cetak bintang
    for k in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 6: BELAH KETUPAT
# ============================================================
print("\nPOLA 6: BELAH KETUPAT")
print("-"*60)
tinggi = 5

# Bagian atas (termasuk tengah)
for i in range(1, tinggi + 1):
    for j in range(tinggi - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

# Bagian bawah
for i in range(tinggi - 1, 0, -1):
    for j in range(tinggi - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 7: SEGITIGA ANGKA
# ============================================================
print("\nPOLA 7: SEGITIGA ANGKA BERURUTAN")
print("-"*60)
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# ============================================================
# POLA 8: SEGITIGA ANGKA SAMA
# ============================================================
print("\nPOLA 8: SEGITIGA ANGKA SAMA")
print("-"*60)
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(i):
        print(i, end=" ")
    print()

# ============================================================
# POLA 9: SEGITIGA ANGKA MENAIK
# ============================================================
print("\nPOLA 9: SEGITIGA ANGKA MENAIK TERUS")
print("-"*60)
tinggi = 5
angka = 1
for i in range(1, tinggi + 1):
    for j in range(i):
        print(angka, end=" ")
        angka += 1
    print()

# ============================================================
# POLA 10: KOTAK BERLUBANG
# ============================================================
print("\nPOLA 10: KOTAK BERLUBANG (BORDER SAJA)")
print("-"*60)
ukuran = 5
for i in range(ukuran):
    for j in range(ukuran):
        # Cetak bintang hanya di pinggir
        if i == 0 or i == ukuran - 1 or j == 0 or j == ukuran - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ============================================================
# POLA 11: POLA X
# ============================================================
print("\nPOLA 11: POLA X (DIAGONAL)")
print("-"*60)
ukuran = 7
for i in range(ukuran):
    for j in range(ukuran):
        # Cetak bintang di diagonal utama dan diagonal sekunder
        if i == j or i + j == ukuran - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

# ============================================================
# POLA 12: SETENGAH BELAH KETUPAT
# ============================================================
print("\nPOLA 12: SETENGAH BELAH KETUPAT (KANAN)")
print("-"*60)
tinggi = 5

# Bagian atas
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()

# Bagian bawah
for i in range(tinggi - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================================
# POLA 13: ANGKA GANJIL
# ============================================================
print("\nPOLA 13: PIRAMIDA ANGKA GANJIL")
print("-"*60)
tinggi = 5
for i in range(1, tinggi + 1):
    # Cetak spasi
    for j in range(tinggi - i):
        print(" ", end=" ")
    # Cetak angka ganjil
    angka = 1
    for k in range(i):
        print(angka, end=" ")
        angka += 2
    print()

# ============================================================
# POLA 14: SEGITIGA PASCAL (SEDERHANA)
# ============================================================
print("\nPOLA 14: SEGITIGA SEDERHANA DENGAN ANGKA 1")
print("-"*60)
tinggi = 5
for i in range(tinggi):
    # Cetak spasi
    for j in range(tinggi - i - 1):
        print(" ", end=" ")
    # Cetak angka 1
    for k in range(i + 1):
        print("1", end=" ")
    print()

# ============================================================
# BONUS: POLA INTERAKTIF
# ============================================================
print("\n" + "="*60)
print("BONUS: POLA CUSTOM")
print("="*60)
print("Buat pola segitiga dengan input user")
tinggi = int(input("Masukkan tinggi segitiga (1-10): "))
karakter = input("Masukkan karakter untuk pola: ")

print(f"\nHasil pola segitiga dengan '{karakter}':")
for i in range(1, tinggi + 1):
    for j in range(i):
        print(karakter, end=" ")
    print()

print("\n" + "="*60)
print("TIPS MEMBUAT POLA:")
print("="*60)
print("1. Pahami struktur: spasi + karakter")
print("2. Gambar dulu di kertas untuk visualisasi")
print("3. Outer loop = baris, Inner loop = kolom")
print("4. Gunakan rumus matematika untuk pola tertentu")
print("5. Test dengan ukuran kecil dulu (3-5 baris)")
print("="*60)
