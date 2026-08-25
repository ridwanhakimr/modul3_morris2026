"""
Contoh Kode: Percabangan Bertingkat (Nested If)
Demonstrasi penggunaan nested if untuk kasus dengan multiple kondisi

Topik: BAB 6.2 - Percabangan Bertingkat
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("CONTOH 1: NESTED IF SEDERHANA")
print("="*60)

# Contoh sederhana: Cek umur dan status keanggotaan
umur = int(input("Masukkan umur Anda: "))

if umur >= 18:
    print("Anda sudah dewasa.")
    
    # Nested if - kondisi di dalam kondisi
    punya_kartu = input("Apakah Anda punya kartu member? (ya/tidak): ")
    
    if punya_kartu.lower() == "ya":
        print("Anda mendapat diskon 20%!")
    else:
        print("Anda mendapat diskon 10% (diskon standar)")
else:
    print("Anda masih di bawah umur.")
    print("Tidak ada diskon khusus.")

print("\n" + "="*60)
print("CONTOH 2: NESTED IF DENGAN MULTIPLE LEVEL")
print("="*60)

# Sistem kategorisasi cuaca dan aktivitas
suhu = float(input("Masukkan suhu (Celsius): "))

# Level 1: Cek rentang suhu utama
if suhu > 30:
    print("Cuaca: PANAS")
    
    # Level 2: Cek kelembaban
    kelembaban = float(input("Masukkan kelembaban (%): "))
    
    if kelembaban > 70:
        print("  → Kondisi: Panas dan lembab (gerah)")
        print("  → Saran: Gunakan AC, banyak minum air")
    else:
        print("  → Kondisi: Panas tapi kering")
        print("  → Saran: Pakai topi, gunakan sunscreen")

elif suhu >= 20:
    print("Cuaca: SEJUK")
    
    # Level 2: Cek angin
    angin = input("Apakah berangin? (ya/tidak): ")
    
    if angin.lower() == "ya":
        print("  → Kondisi: Sejuk berangin")
        print("  → Saran: Cuaca ideal untuk outdoor")
    else:
        print("  → Kondisi: Sejuk tenang")
        print("  → Saran: Cocok untuk jalan-jalan")

else:
    print("Cuaca: DINGIN")
    
    # Level 2: Cek hujan
    hujan = input("Apakah hujan? (ya/tidak): ")
    
    if hujan.lower() == "ya":
        print("  → Kondisi: Dingin dan hujan")
        print("  → Saran: Bawa jaket tebal dan payung")
    else:
        print("  → Kondisi: Dingin tapi cerah")
        print("  → Saran: Bawa jaket tipis")

print("\n" + "="*60)
print("CONTOH 3: NESTED IF VS ELIF")
print("="*60)

nilai = int(input("Masukkan nilai ujian (0-100): "))

print("\nDengan NESTED IF:")
# Cara 1: Nested if (bertingkat)
if nilai >= 60:
    if nilai >= 80:
        if nilai >= 90:
            print("Grade: A")
        else:
            print("Grade: B")
    else:
        print("Grade: C")
else:
    print("Grade: D (Tidak Lulus)")

print("\nDengan ELIF (lebih simpel):")
# Cara 2: Elif (rangkaian)
if nilai >= 90:
    print("Grade: A")
elif nilai >= 80:
    print("Grade: B")
elif nilai >= 60:
    print("Grade: C")
else:
    print("Grade: D (Tidak Lulus)")

print("\n" + "="*60)
print("KESIMPULAN:")
print("- Gunakan NESTED IF jika kondisi benar-benar bergantung satu sama lain")
print("- Gunakan ELIF jika kondisi saling eksklusif (pilihan bergantian)")
print("- Hindari nested if terlalu dalam (max 2-3 level)")
print("="*60)
