"""
Contoh Kode: Perulangan Bersarang (Nested Loop)
Demonstrasi perulangan di dalam perulangan untuk kasus multi-dimensi

Topik: BAB 6.6 - Perulangan Bersarang (Nested Loop)
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("NESTED LOOP SEDERHANA")
print("="*60)

print("\nContoh 1: Loop di dalam loop")
print("Outer loop berjalan 3 kali, inner loop berjalan 2 kali")
print()

for i in range(1, 4):
    print(f"Outer loop: iterasi ke-{i}")
    for j in range(1, 3):
        print(f"  Inner loop: iterasi ke-{j}")
    print()

print("-"*60)
print("\nPenjelasan: Total iterasi = 3 × 2 = 6 kali")

print("\n" + "="*60)
print("TABEL PERKALIAN")
print("="*60)

print("\nContoh 2: Membuat tabel perkalian 1-5")
print()

# Header tabel
print("   ", end="")
for i in range(1, 6):
    print(f"{i:4}", end="")
print("\n" + "-"*30)

# Isi tabel
for i in range(1, 6):
    print(f"{i} |", end="")
    for j in range(1, 6):
        hasil = i * j
        print(f"{hasil:4}", end="")
    print()

print("\n" + "="*60)
print("POLA PERSEGI DAN SEGITIGA")
print("="*60)

print("\nContoh 3: Pola persegi bintang")
ukuran = 5
for i in range(ukuran):
    for j in range(ukuran):
        print("*", end=" ")
    print()

print("\n" + "-"*60)
print("Contoh 4: Pola segitiga siku-siku")
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "-"*60)
print("Contoh 5: Pola segitiga terbalik")
tinggi = 5
for i in range(tinggi, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n" + "="*60)
print("NESTED LOOP DENGAN ANGKA")
print("="*60)

print("\nContoh 6: Pola angka bertingkat")
tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n" + "-"*60)
print("Contoh 7: Koordinat matriks")
baris = 3
kolom = 4
print(f"Matriks {baris}x{kolom}:")
for i in range(baris):
    for j in range(kolom):
        print(f"({i},{j})", end=" ")
    print()

print("\n" + "="*60)
print("NESTED LOOP DENGAN KONDISI")
print("="*60)

print("\nContoh 8: Cetak hanya bilangan genap")
for i in range(1, 6):
    print(f"Baris {i}: ", end="")
    for j in range(1, 6):
        if j % 2 == 0:  # Hanya cetak genap
            print(j, end=" ")
    print()

print("\n" + "-"*60)
print("Contoh 9: Skip diagonal utama")
ukuran = 5
print("Matriks tanpa diagonal utama:")
for i in range(ukuran):
    for j in range(ukuran):
        if i == j:
            print("_", end=" ")  # Skip diagonal
        else:
            print("*", end=" ")
    print()

print("\n" + "="*60)
print("APLIKASI PRAKTIS")
print("="*60)

print("\nContoh 10: Cari semua pasangan yang jumlahnya 10")
target = 10
print(f"Pasangan angka (1-9) yang jumlahnya {target}:")
for i in range(1, 10):
    for j in range(i, 10):  # Mulai dari i agar tidak duplikat
        if i + j == target:
            print(f"  {i} + {j} = {target}")

print("\n" + "-"*60)
print("Contoh 11: Cek bilangan prima dalam rentang")
print("Bilangan prima dari 2-20:")
for angka in range(2, 21):
    adalah_prima = True
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            adalah_prima = False
            break
    if adalah_prima:
        print(angka, end=" ")
print()

print("\n" + "="*60)
print("NESTED LOOP 3 TINGKAT")
print("="*60)

print("\nContoh 12: Triple nested loop")
print("Kombinasi 3 angka yang jumlahnya 10:")
count = 0
for i in range(1, 9):
    for j in range(1, 9):
        for k in range(1, 9):
            if i + j + k == 10 and i <= j <= k:
                print(f"  {i} + {j} + {k} = 10")
                count += 1
print(f"Total kombinasi: {count}")

print("\n" + "="*60)
print("TIPS NESTED LOOP")
print("="*60)
print("1. Hati-hati dengan kompleksitas waktu (n × m × p...)")
print("2. Gunakan nama variabel yang jelas (i, j, k atau row, col)")
print("3. Hindari nested loop terlalu dalam (max 3 tingkat)")
print("4. Gunakan break untuk efisiensi jika perlu")
print("5. Perhatikan indentasi agar tidak salah tingkat")
print("="*60)
