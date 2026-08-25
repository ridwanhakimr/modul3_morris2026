"""
Latihan 3 - Deteksi Bilangan Prima
Program ini menerima satu bilangan dari pengguna dan menentukan:
1. Apakah bilangan tersebut prima atau bukan
2. Status ganjil atau genap dari bilangan tersebut

Nama File: latihan3_prima.py
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*50)
print("PROGRAM DETEKSI BILANGAN PRIMA DAN GANJIL/GENAP")
print("="*50)

# Input bilangan dari pengguna
bilangan = int(input("Masukkan sebuah bilangan bulat: "))

print("\n" + "-"*50)

# Cek ganjil atau genap menggunakan operator modulo
if bilangan % 2 == 0:
    status_ganjil_genap = "GENAP"
else:
    status_ganjil_genap = "GANJIL"

print(f"Bilangan {bilangan} adalah bilangan {status_ganjil_genap}")

# Deteksi bilangan prima
print("-"*50)

# Inisialisasi flag untuk menandai bilangan prima
adalah_prima = True

# Penanganan kasus khusus
if bilangan < 2:
    adalah_prima = False
    if bilangan <= 0:
        alasan = "Bilangan prima harus lebih besar dari 1"
    else:
        alasan = "Bilangan 1 bukan bilangan prima"
else:
    # Cek pembagi dari 2 sampai bilangan-1
    # Jika ada yang habis dibagi, maka bukan prima
    for i in range(2, bilangan):
        if bilangan % i == 0:
            adalah_prima = False
            alasan = f"Karena {bilangan} habis dibagi {i}"
            break
    
    # Jika loop selesai dan masih prima
    if adalah_prima:
        alasan = f"Karena {bilangan} hanya habis dibagi 1 dan {bilangan}"

# Tampilkan hasil
print(f"\nBilangan {bilangan} adalah", end=" ")
if adalah_prima:
    print("BILANGAN PRIMA")
else:
    print("BUKAN BILANGAN PRIMA")
print(alasan)

print("="*50)
print("Terima kasih telah menggunakan program ini!")
print("="*50)
