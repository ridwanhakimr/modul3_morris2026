"""
Latihan 3 - Deret Aritmatika dan Perpangkatan
Program ini menghitung:
1. Jumlah deret aritmatika dari 1 sampai n
2. Hasil perpangkatan menggunakan perulangan (tanpa operator **)

Formula deret: 1 + 2 + 3 + ... + n
Formula perpangkatan: basis^pangkat = basis × basis × ... (sebanyak pangkat kali)

Nama File: latihan3_deret.py
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("PROGRAM PENGHITUNG DERET ARITMATIKA DAN PERPANGKATAN")
print("="*60)

# ============================================================
# BAGIAN 1: DERET ARITMATIKA
# ============================================================
print("\n" + "="*60)
print("BAGIAN 1: DERET ARITMATIKA")
print("="*60)

n = int(input("Masukkan nilai n (batas deret): "))

# Inisialisasi variabel penampung (akumulator)
jumlah_deret = 0

# Tampilkan proses perhitungan
print(f"\nProses perhitungan deret 1 sampai {n}:")
print("Deret: ", end="")

# Hitung jumlah deret dengan perulangan
for i in range(1, n + 1):
    jumlah_deret += i  # Sama dengan: jumlah_deret = jumlah_deret + i
    
    # Tampilkan angka
    if i < n:
        print(i, end=" + ")
    else:
        print(i, end=" ")

print(f"\n\nHasil penjumlahan: {jumlah_deret}")

# Verifikasi dengan rumus langsung: n(n+1)/2
rumus_langsung = n * (n + 1) // 2
print(f"Verifikasi rumus n(n+1)/2 = {n}({n}+1)/2 = {rumus_langsung}")

if jumlah_deret == rumus_langsung:
    print("✓ Hasil sesuai dengan rumus matematika")

# ============================================================
# BAGIAN 2: PERPANGKATAN
# ============================================================
print("\n" + "="*60)
print("BAGIAN 2: PERPANGKATAN MANUAL")
print("="*60)

basis = int(input("Masukkan bilangan basis: "))
pangkat = int(input("Masukkan pangkat: "))

# Inisialisasi hasil perpangkatan
hasil_pangkat = 1

# Tampilkan proses perhitungan
print(f"\nProses perhitungan {basis}^{pangkat}:")
print(f"{basis}^{pangkat} = ", end="")

# Hitung perpangkatan dengan perulangan
if pangkat == 0:
    print("1 (bilangan pangkat 0 = 1)")
elif pangkat > 0:
    # Tampilkan perkalian berulang
    for i in range(pangkat):
        if i < pangkat - 1:
            print(f"{basis} × ", end="")
        else:
            print(f"{basis}", end="")
        hasil_pangkat *= basis  # Sama dengan: hasil_pangkat = hasil_pangkat * basis
    
    print(f" = {hasil_pangkat}")
else:
    # Pangkat negatif
    print(f"1 / ({basis}^{abs(pangkat)})")
    for i in range(abs(pangkat)):
        hasil_pangkat *= basis
    hasil_pangkat = 1 / hasil_pangkat
    print(f"Hasil: {hasil_pangkat}")

# Verifikasi dengan operator ** bawaan Python
if pangkat >= 0:
    verifikasi = basis ** pangkat
    print(f"\nVerifikasi dengan operator **: {basis}**{pangkat} = {verifikasi}")
    if hasil_pangkat == verifikasi:
        print("✓ Hasil sesuai dengan operator bawaan Python")

# ============================================================
# RINGKASAN HASIL
# ============================================================
print("\n" + "="*60)
print("RINGKASAN HASIL")
print("="*60)
print(f"Jumlah deret 1 sampai {n}     : {jumlah_deret}")
print(f"Hasil {basis} pangkat {pangkat}        : {hasil_pangkat}")
print("="*60)
print("Terima kasih telah menggunakan program ini!")
print("="*60)
