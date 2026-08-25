"""
Contoh Kode: Break dan Continue
Demonstrasi penggunaan break dan continue untuk kontrol perulangan

Topik: BAB 6.5 - Kontrol Perulangan
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("PERINTAH BREAK - Menghentikan Perulangan")
print("="*60)

print("\nContoh 1: Break sederhana")
print("Mencari angka 7 dalam perulangan 1-10")
for i in range(1, 11):
    print(f"Memeriksa angka: {i}")
    if i == 7:
        print("  → Angka 7 ditemukan! Berhenti.")
        break  # Keluar dari loop
    print("  → Lanjut ke angka berikutnya...")

print("\n" + "-"*60)
print("Contoh 2: Break dengan kondisi")
print("Cari bilangan pertama yang habis dibagi 7 dan 3")
for i in range(1, 100):
    if i % 7 == 0 and i % 3 == 0:
        print(f"Ditemukan: {i}")
        break
else:
    print("Tidak ditemukan")  # Ini hanya dijalankan jika loop TIDAK di-break

print("\n" + "-"*60)
print("Contoh 3: Break dalam while loop")
print("Input password (maksimal 3 kali)")
percobaan = 0
password_benar = "python123"

while True:
    percobaan += 1
    print(f"\nPercobaan {percobaan}")
    
    # Simulasi input (dalam program nyata gunakan input())
    if percobaan == 1:
        password = "salah1"
    elif percobaan == 2:
        password = "python123"
    else:
        password = "salah3"
    
    print(f"Input: {password}")
    
    if password == password_benar:
        print("Login berhasil!")
        break
    else:
        print("Password salah!")
        if percobaan >= 3:
            print("Batas percobaan habis. Program berhenti.")
            break

print("\n" + "="*60)
print("PERINTAH CONTINUE - Lewati Satu Iterasi")
print("="*60)

print("\nContoh 1: Continue sederhana")
print("Cetak angka 1-10, KECUALI kelipatan 3")
for i in range(1, 11):
    if i % 3 == 0:
        continue  # Lewati iterasi ini, langsung ke iterasi berikutnya
    print(f"Angka: {i}")

print("\n" + "-"*60)
print("Contoh 2: Continue untuk filter")
print("Cetak bilangan ganjil antara 1-20")
for i in range(1, 21):
    if i % 2 == 0:
        continue  # Lewati bilangan genap
    print(f"Bilangan ganjil: {i}", end=" ")
print()

print("\n" + "-"*60)
print("Contoh 3: Continue dengan kondisi kompleks")
print("Proses data, skip jika tidak valid")
data = [10, -5, 0, 15, -3, 20, 8, 0, 12]
print(f"Data: {data}")
print("\nMemproses (skip nilai negatif dan nol):")

jumlah_valid = 0
total = 0

for angka in data:
    # Skip jika negatif atau nol
    if angka <= 0:
        print(f"  {angka} → SKIP (tidak valid)")
        continue
    
    # Kode di bawah ini hanya dijalankan untuk angka positif
    print(f"  {angka} → PROSES")
    total += angka
    jumlah_valid += 1

print(f"\nJumlah data valid: {jumlah_valid}")
print(f"Total: {total}")

print("\n" + "="*60)
print("PERBEDAAN BREAK VS CONTINUE")
print("="*60)

print("\nDengan BREAK (berhenti saat ketemu 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  {i} → BREAK! Berhenti total.")
        break
    print(f"  {i}")

print("\nDengan CONTINUE (lewati angka 5):")
for i in range(1, 11):
    if i == 5:
        print(f"  {i} → CONTINUE! Lewati saja.")
        continue
    print(f"  {i}")

print("\n" + "="*60)
print("VARIABEL AKUMULATOR DAN FLAG")
print("="*60)

print("\nContoh 1: Variabel Akumulator (penampung)")
print("Hitung total dan rata-rata")
data = [85, 90, 75, 88, 92]
total = 0  # Akumulator untuk menampung total

for nilai in data:
    total += nilai  # Tambahkan ke akumulator
    print(f"Nilai: {nilai}, Total sementara: {total}")

rata_rata = total / len(data)
print(f"\nHasil akhir:")
print(f"Total: {total}")
print(f"Rata-rata: {rata_rata}")

print("\n" + "-"*60)
print("Contoh 2: Variabel Flag (penanda)")
print("Cek apakah ada nilai negatif dalam list")
data = [10, 20, 30, -5, 40]
ada_negatif = False  # Flag untuk menandai

for angka in data:
    print(f"Cek {angka}...", end=" ")
    if angka < 0:
        ada_negatif = True  # Set flag
        print("NEGATIF ditemukan!")
        break
    print("OK")

if ada_negatif:
    print("\n⚠ Ada bilangan negatif dalam data")
else:
    print("\n✓ Semua bilangan positif")

print("\n" + "-"*60)
print("Contoh 3: Kombinasi Akumulator dan Flag")
print("Hitung jumlah bilangan prima di bawah 20")

jumlah_prima = 0  # Akumulator untuk hitung jumlah
print("Bilangan prima di bawah 20:")

for angka in range(2, 20):
    adalah_prima = True  # Flag untuk setiap angka
    
    # Cek apakah prima
    for pembagi in range(2, angka):
        if angka % pembagi == 0:
            adalah_prima = False
            break
    
    if adalah_prima:
        print(angka, end=" ")
        jumlah_prima += 1  # Tambah akumulator

print(f"\n\nTotal bilangan prima: {jumlah_prima}")

print("\n" + "="*60)
print("TIPS PENGGUNAAN")
print("="*60)
print("1. BREAK: Untuk keluar dari loop saat kondisi terpenuhi")
print("2. CONTINUE: Untuk skip iterasi tertentu tapi lanjutkan loop")
print("3. AKUMULATOR: Variabel untuk menampung hasil perhitungan")
print("4. FLAG: Variabel boolean untuk menandai kondisi tertentu")
print("="*60)
