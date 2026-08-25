"""
Contoh Kode: Perulangan For dan While
Demonstrasi perbedaan dan penggunaan for dan while loop

Topik: BAB 6.4 - Perulangan (Looping)
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("PERULANGAN FOR - DASAR")
print("="*60)

# For loop paling sederhana
print("\nContoh 1: Cetak angka 1 sampai 5")
for i in range(1, 6):
    print(f"Angka: {i}")

print("\n" + "-"*60)
print("Contoh 2: Cetak angka 0 sampai 4 (default dari 0)")
for i in range(5):
    print(f"Index: {i}")

print("\n" + "-"*60)
print("Contoh 3: Dengan langkah (step) tertentu")
for i in range(0, 11, 2):  # Dari 0 sampai 10, loncat 2
    print(f"Bilangan genap: {i}")

print("\n" + "-"*60)
print("Contoh 4: Mundur dari 10 ke 1")
for i in range(10, 0, -1):
    print(f"Hitung mundur: {i}")
print("Liftoff!")

print("\n" + "="*60)
print("PERULANGAN WHILE - DASAR")
print("="*60)

# While loop paling sederhana
print("\nContoh 1: Cetak angka 1 sampai 5 dengan while")
i = 1
while i <= 5:
    print(f"Angka: {i}")
    i += 1  # Jangan lupa increment!

print("\n" + "-"*60)
print("Contoh 2: Hitung mundur dengan while")
i = 10
while i > 0:
    print(f"Hitung mundur: {i}")
    i -= 1
print("Liftoff!")

print("\n" + "="*60)
print("PERBANDINGAN FOR VS WHILE")
print("="*60)

print("\nTUGAS: Hitung jumlah 1 + 2 + 3 + 4 + 5")

# Cara 1: Menggunakan FOR
print("\nCara 1: Dengan FOR loop")
total_for = 0
for i in range(1, 6):
    total_for += i
    print(f"  Langkah {i}: total = {total_for}")
print(f"Hasil dengan FOR: {total_for}")

# Cara 2: Menggunakan WHILE
print("\nCara 2: Dengan WHILE loop")
total_while = 0
i = 1
while i <= 5:
    total_while += i
    print(f"  Langkah {i}: total = {total_while}")
    i += 1
print(f"Hasil dengan WHILE: {total_while}")

print("\n" + "="*60)
print("KAPAN MENGGUNAKAN FOR VS WHILE?")
print("="*60)

print("\nGUNAKAN FOR jika:")
print("✓ Tahu berapa kali akan berulang")
print("✓ Iterasi melalui range angka")
print("✓ Iterasi melalui list/string")
print("\nContoh: Cetak 10 angka pertama")
for i in range(1, 11):
    print(i, end=" ")

print("\n\nGUNAKAN WHILE jika:")
print("✓ Tidak tahu pasti berapa kali akan berulang")
print("✓ Berulang sampai kondisi tertentu terpenuhi")
print("✓ Butuh kontrol lebih fleksibel")

print("\nContoh: Input sampai benar")
print("(Simulasi - tanpa input sebenarnya)")
percobaan = 0
password_benar = False
while not password_benar and percobaan < 3:
    percobaan += 1
    print(f"Percobaan ke-{percobaan}: Meminta password...")
    # Simulasi: berhasil di percobaan ke-2
    if percobaan == 2:
        password_benar = True
        print("  → Password BENAR!")
    else:
        print("  → Password SALAH!")

print("\n" + "="*60)
print("BAHAYA: INFINITE LOOP (PERULANGAN TAK BERUJUNG)")
print("="*60)

print("\nContoh SALAH yang menyebabkan infinite loop:")
print("(Kode di bawah ini TIDAK dijalankan)")
print("""
i = 1
while i <= 5:
    print(i)
    # LUPA: i += 1  <-- Tanpa ini, loop tidak akan berhenti!
""")

print("\nCara menghindari infinite loop:")
print("✓ Pastikan variabel counter di-update")
print("✓ Pastikan kondisi bisa menjadi False")
print("✓ Gunakan break jika perlu keluar paksa")

print("\n" + "="*60)
print("CONTOH KASUS INTERAKTIF")
print("="*60)

print("\nProgram: Tebak angka (simulasi)")
angka_rahasia = 7
tebakan = 0
percobaan = 0

while tebakan != angka_rahasia and percobaan < 5:
    percobaan += 1
    # Simulasi input (dalam program asli, gunakan input())
    if percobaan == 1:
        tebakan = 5
    elif percobaan == 2:
        tebakan = 8
    elif percobaan == 3:
        tebakan = 7
    
    print(f"\nPercobaan {percobaan}: Tebakan = {tebakan}")
    
    if tebakan == angka_rahasia:
        print("BENAR! Anda menang!")
    elif tebakan < angka_rahasia:
        print("Terlalu kecil, coba lagi!")
    else:
        print("Terlalu besar, coba lagi!")

print("\n" + "="*60)
print("LATIHAN MANDIRI")
print("="*60)
print("Coba buat program dengan for/while untuk:")
print("1. Cetak tabel perkalian 1-10")
print("2. Hitung faktorial (n!)")
print("3. Cari bilangan terbesar dari input user")
print("4. Program kalkulator yang berulang sampai user ketik 'keluar'")
print("="*60)
