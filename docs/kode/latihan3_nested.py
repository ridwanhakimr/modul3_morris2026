"""
Latihan 3 - Percabangan Bertingkat (Nested If)
Program ini menentukan kelulusan mahasiswa berdasarkan dua kriteria:
1. Nilai ujian (0-100)
2. Persentase kehadiran (0-100%)

Ketentuan kelulusan:
- Nilai >= 60 DAN Kehadiran >= 75% : LULUS dengan predikat
- Nilai >= 60 TAPI Kehadiran < 75% : TIDAK LULUS (kurang kehadiran)
- Nilai < 60 : TIDAK LULUS (nilai tidak memenuhi)

Nama File: latihan3_nested.py
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("SISTEM PENENTU KELULUSAN MAHASISWA")
print("="*60)

# Input data mahasiswa
nama = input("Masukkan nama mahasiswa: ")
nilai = float(input("Masukkan nilai ujian (0-100): "))
kehadiran = float(input("Masukkan persentase kehadiran (0-100): "))

print("\n" + "="*60)
print("HASIL PENILAIAN")
print("="*60)
print(f"Nama Mahasiswa  : {nama}")
print(f"Nilai Ujian     : {nilai}")
print(f"Kehadiran       : {kehadiran}%")
print("-"*60)

# Percabangan bertingkat (nested if)
# Lapis pertama: Cek nilai
if nilai >= 60:
    # Lapis kedua: Cek kehadiran (hanya jika nilai memenuhi)
    if kehadiran >= 75:
        # Keduanya memenuhi - tentukan predikat
        print("STATUS          : LULUS")
        
        # Lapis ketiga: Tentukan predikat berdasarkan nilai
        if nilai >= 85:
            predikat = "A (Sangat Baik)"
        elif nilai >= 75:
            predikat = "B (Baik)"
        elif nilai >= 65:
            predikat = "C (Cukup)"
        else:
            predikat = "D (Kurang)"
        
        print(f"Predikat        : {predikat}")
        print("\nSelamat! Anda dinyatakan LULUS.")
    else:
        # Nilai memenuhi tapi kehadiran tidak
        print("STATUS          : TIDAK LULUS")
        print("Alasan          : Kehadiran tidak memenuhi syarat (< 75%)")
        kekurangan = 75 - kehadiran
        print(f"                  Anda kekurangan {kekurangan}% kehadiran")
        print("\nMohon untuk lebih rajin hadir di perkuliahan.")
else:
    # Nilai tidak memenuhi (tidak perlu cek kehadiran)
    print("STATUS          : TIDAK LULUS")
    print("Alasan          : Nilai ujian tidak memenuhi syarat (< 60)")
    kekurangan = 60 - nilai
    print(f"                  Anda kekurangan {kekurangan} poin")
    
    # Tetap berikan info kehadiran sebagai informasi tambahan
    if kehadiran < 75:
        print(f"Info Tambahan   : Kehadiran juga tidak memenuhi ({kehadiran}%)")
    
    print("\nSilakan ikuti ujian remidi untuk memperbaiki nilai.")

print("="*60)
print("Terima kasih telah menggunakan sistem ini!")
print("="*60)
