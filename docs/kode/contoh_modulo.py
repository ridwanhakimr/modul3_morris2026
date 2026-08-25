"""
Contoh Kode: Operator Modulo dan Pengujian Bilangan
Demonstrasi penggunaan operator modulo (%) untuk berbagai pengujian bilangan

Topik: BAB 6.3 - Operator Modulo dan Pengujian Bilangan
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("PENGENALAN OPERATOR MODULO (%)")
print("="*60)

# Penjelasan konsep
print("Operator modulo (%) menghasilkan SISA BAGI dari pembagian.")
print("Contoh: 10 % 3 = 1 (karena 10 dibagi 3 = 3 sisa 1)")
print("\nBeberapa contoh:")
print(f"10 % 3 = {10 % 3}")
print(f"15 % 4 = {15 % 4}")
print(f"20 % 5 = {20 % 5}")
print(f"7 % 2 = {7 % 2}")

print("\n" + "="*60)
print("CONTOH 1: DETEKSI GANJIL DAN GENAP")
print("="*60)

# Konsep: Bilangan genap habis dibagi 2 (sisa 0)
#         Bilangan ganjil tidak habis dibagi 2 (sisa 1)

# Contoh dengan beberapa angka
angka_list = [10, 15, 22, 7]
print(f"Mengecek angka: {angka_list}")
print()

for angka in angka_list:
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan GENAP (karena {angka} % 2 = {angka % 2})")
    else:
        print(f"{angka} adalah bilangan GANJIL (karena {angka} % 2 = {angka % 2})")

print("\n" + "="*60)
print("CONTOH 2: DETEKSI KELIPATAN")
print("="*60)

# Contoh pengecekan kelipatan
bilangan = 24
pembagi = 6

print(f"Cek apakah {bilangan} kelipatan dari {pembagi}:")
if bilangan % pembagi == 0:
    print(f"[YA] {bilangan} adalah KELIPATAN dari {pembagi}")
    print(f"     Karena {bilangan} % {pembagi} = {bilangan % pembagi}")
else:
    print(f"[TIDAK] {bilangan} BUKAN kelipatan dari {pembagi}")
    print(f"        Karena {bilangan} % {pembagi} = {bilangan % pembagi} (ada sisa)")

# Contoh lain
print()
bilangan = 25
pembagi = 6
print(f"Cek apakah {bilangan} kelipatan dari {pembagi}:")
if bilangan % pembagi == 0:
    print(f"[YA] {bilangan} adalah KELIPATAN dari {pembagi}")
    print(f"     Karena {bilangan} % {pembagi} = {bilangan % pembagi}")
else:
    print(f"[TIDAK] {bilangan} BUKAN kelipatan dari {pembagi}")
    print(f"        Karena {bilangan} % {pembagi} = {bilangan % pembagi} (ada sisa)")

print("\n" + "="*60)
print("CONTOH 3: KLASIFIKASI BILANGAN LENGKAP")
print("="*60)

# Contoh analisis beberapa bilangan
angka_test = [15, -8, 0, 30]

for angka in angka_test:
    print(f"\nAnalisis bilangan {angka}:")
    print("-" * 40)
    
    # 1. Positif, Negatif, atau Nol
    if angka > 0:
        print("- Bilangan POSITIF")
    elif angka < 0:
        print("- Bilangan NEGATIF")
    else:
        print("- Bilangan NOL")
    
    # 2. Ganjil atau Genap (hanya untuk bilangan bukan nol)
    if angka != 0:
        if angka % 2 == 0:
            print("- Bilangan GENAP")
        else:
            print("- Bilangan GANJIL")
    
    # 3. Kelipatan 3
    if angka % 3 == 0 and angka != 0:
        print("- Kelipatan 3")
    
    # 4. Kelipatan 5
    if angka % 5 == 0 and angka != 0:
        print("- Kelipatan 5")
    
    # 5. Kelipatan 3 DAN 5 (kelipatan 15)
    if angka % 3 == 0 and angka % 5 == 0 and angka != 0:
        print("- Kelipatan 15 (kelipatan 3 DAN 5)")

print("\n" + "="*60)
print("CONTOH 4: APLIKASI FIZZBUZZ")
print("="*60)
print("Program klasik untuk belajar modulo!")
print("Aturan:")
print("- Jika kelipatan 3: cetak 'Fizz'")
print("- Jika kelipatan 5: cetak 'Buzz'")
print("- Jika kelipatan 3 DAN 5: cetak 'FizzBuzz'")
print("- Selain itu: cetak angkanya")
print("-" * 60)

batas = 20
print(f"FizzBuzz dari 1 sampai {batas}:")
print()

for i in range(1, batas + 1):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: FizzBuzz")
    elif i % 3 == 0:
        print(f"{i}: Fizz")
    elif i % 5 == 0:
        print(f"{i}: Buzz")
    else:
        print(f"{i}: {i}")

print("\n" + "="*60)
print("CONTOH 5: MENDAPATKAN DIGIT TERAKHIR")
print("="*60)

# Contoh pengambilan digit terakhir
angka_contoh = [1234, 567, 89, 4321]
print(f"Mengambil digit terakhir dari: {angka_contoh}")
print()

for angka in angka_contoh:
    digit_terakhir = angka % 10
    print(f"Digit terakhir dari {angka} adalah {digit_terakhir}")
    
    # Aplikasi: Cek apakah digit terakhir genap atau ganjil
    if digit_terakhir % 2 == 0:
        print(f"  -> Digit terakhir ({digit_terakhir}) adalah GENAP")
    else:
        print(f"  -> Digit terakhir ({digit_terakhir}) adalah GANJIL")
    print()

print("="*60)
print("RANGKUMAN OPERATOR MODULO")
print("="*60)
print("Kegunaan operator modulo (%):")
print("1. Cek ganjil/genap: angka % 2 == 0")
print("2. Cek kelipatan: angka % n == 0")
print("3. Ambil digit terakhir: angka % 10")
print("4. Siklus berulang: index % panjang_list")
print("5. Validasi input (misal: harus kelipatan tertentu)")
print("="*60)
