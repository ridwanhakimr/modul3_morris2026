"""
Tugas Mandiri - Aplikasi Konsol Bermenu
Program ini menggabungkan 3 latihan sebelumnya menjadi satu aplikasi konsol
yang berjalan berulang dengan menu pilihan:
1. Deteksi Bilangan Prima dan Ganjil/Genap
2. Sistem Penentu Kelulusan (Nested If)
3. Penghitung Deret Aritmatika dan Perpangkatan
4. Keluar dari Program

Nama File: tugas3_menu.py
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

def tampilkan_menu():
    """Menampilkan menu utama aplikasi"""
    print("\n" + "="*60)
    print(" "*15 + "APLIKASI KONSOL PYTHON")
    print("="*60)
    print("Menu Pilihan:")
    print("  1. Deteksi Bilangan Prima dan Ganjil/Genap")
    print("  2. Sistem Penentu Kelulusan Mahasiswa")
    print("  3. Penghitung Deret Aritmatika dan Perpangkatan")
    print("  4. Keluar dari Program")
    print("="*60)


def deteksi_prima():
    """Fitur 1: Deteksi bilangan prima dan ganjil/genap"""
    print("\n" + "="*60)
    print("FITUR 1: DETEKSI BILANGAN PRIMA DAN GANJIL/GENAP")
    print("="*60)
    
    bilangan = int(input("Masukkan sebuah bilangan bulat: "))
    
    print("\n" + "-"*60)
    
    # Cek ganjil atau genap
    if bilangan % 2 == 0:
        status_ganjil_genap = "GENAP"
    else:
        status_ganjil_genap = "GANJIL"
    
    print(f"Bilangan {bilangan} adalah bilangan {status_ganjil_genap}")
    
    # Deteksi bilangan prima
    print("-"*60)
    adalah_prima = True
    
    if bilangan < 2:
        adalah_prima = False
        if bilangan <= 0:
            alasan = "Bilangan prima harus lebih besar dari 1"
        else:
            alasan = "Bilangan 1 bukan bilangan prima"
    else:
        for i in range(2, bilangan):
            if bilangan % i == 0:
                adalah_prima = False
                alasan = f"Karena {bilangan} habis dibagi {i}"
                break
        
        if adalah_prima:
            alasan = f"Karena {bilangan} hanya habis dibagi 1 dan {bilangan}"
    
    print(f"\nBilangan {bilangan} adalah", end=" ")
    if adalah_prima:
        print("BILANGAN PRIMA")
    else:
        print("BUKAN BILANGAN PRIMA")
    print(alasan)
    print("="*60)


def penentu_kelulusan():
    """Fitur 2: Sistem penentu kelulusan mahasiswa"""
    print("\n" + "="*60)
    print("FITUR 2: SISTEM PENENTU KELULUSAN MAHASISWA")
    print("="*60)
    
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
    
    # Percabangan bertingkat
    if nilai >= 60:
        if kehadiran >= 75:
            print("STATUS          : LULUS")
            
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
            print("STATUS          : TIDAK LULUS")
            print("Alasan          : Kehadiran tidak memenuhi syarat (< 75%)")
            kekurangan = 75 - kehadiran
            print(f"                  Anda kekurangan {kekurangan}% kehadiran")
            print("\nMohon untuk lebih rajin hadir di perkuliahan.")
    else:
        print("STATUS          : TIDAK LULUS")
        print("Alasan          : Nilai ujian tidak memenuhi syarat (< 60)")
        kekurangan = 60 - nilai
        print(f"                  Anda kekurangan {kekurangan} poin")
        
        if kehadiran < 75:
            print(f"Info Tambahan   : Kehadiran juga tidak memenuhi ({kehadiran}%)")
        
        print("\nSilakan ikuti ujian remidi untuk memperbaiki nilai.")
    
    print("="*60)


def hitung_deret_pangkat():
    """Fitur 3: Penghitung deret aritmatika dan perpangkatan"""
    print("\n" + "="*60)
    print("FITUR 3: PENGHITUNG DERET ARITMATIKA DAN PERPANGKATAN")
    print("="*60)
    
    # Bagian 1: Deret Aritmatika
    print("\nBAGIAN 1: DERET ARITMATIKA")
    print("-"*60)
    n = int(input("Masukkan nilai n (batas deret): "))
    
    jumlah_deret = 0
    print(f"\nProses perhitungan deret 1 sampai {n}:")
    print("Deret: ", end="")
    
    for i in range(1, n + 1):
        jumlah_deret += i
        if i < n:
            print(i, end=" + ")
        else:
            print(i, end=" ")
    
    print(f"\n\nHasil penjumlahan: {jumlah_deret}")
    rumus_langsung = n * (n + 1) // 2
    print(f"Verifikasi rumus n(n+1)/2 = {rumus_langsung}")
    
    # Bagian 2: Perpangkatan
    print("\n" + "-"*60)
    print("BAGIAN 2: PERPANGKATAN MANUAL")
    print("-"*60)
    basis = int(input("Masukkan bilangan basis: "))
    pangkat = int(input("Masukkan pangkat: "))
    
    hasil_pangkat = 1
    print(f"\nProses perhitungan {basis}^{pangkat}:")
    print(f"{basis}^{pangkat} = ", end="")
    
    if pangkat == 0:
        print("1 (bilangan pangkat 0 = 1)")
    elif pangkat > 0:
        for i in range(pangkat):
            if i < pangkat - 1:
                print(f"{basis} × ", end="")
            else:
                print(f"{basis}", end="")
            hasil_pangkat *= basis
        print(f" = {hasil_pangkat}")
    else:
        print(f"1 / ({basis}^{abs(pangkat)})")
        for i in range(abs(pangkat)):
            hasil_pangkat *= basis
        hasil_pangkat = 1 / hasil_pangkat
        print(f"Hasil: {hasil_pangkat}")
    
    # Ringkasan
    print("\n" + "-"*60)
    print("RINGKASAN HASIL")
    print("-"*60)
    print(f"Jumlah deret 1 sampai {n}     : {jumlah_deret}")
    print(f"Hasil {basis} pangkat {pangkat}        : {hasil_pangkat}")
    print("="*60)


def main():
    """Fungsi utama - menjalankan aplikasi konsol"""
    print("\n" + "="*60)
    print(" "*10 + "SELAMAT DATANG DI APLIKASI KONSOL")
    print(" "*17 + "MODUL 3 - PYTHON LANJUTAN")
    print("="*60)
    
    # Loop utama aplikasi (berjalan terus sampai user pilih keluar)
    while True:
        tampilkan_menu()
        
        # Validasi input menu
        try:
            pilihan = input("\nPilih menu (1-4): ")
            
            if pilihan == "1":
                deteksi_prima()
            elif pilihan == "2":
                penentu_kelulusan()
            elif pilihan == "3":
                hitung_deret_pangkat()
            elif pilihan == "4":
                print("\n" + "="*60)
                print("Terima kasih telah menggunakan aplikasi ini!")
                print("Sampai jumpa lagi!")
                print("="*60)
                break  # Keluar dari loop
            else:
                print("\n[ERROR] Pilihan tidak valid! Silakan pilih menu 1-4.")
        
        except ValueError:
            print("\n[ERROR] Input tidak valid! Mohon masukkan angka yang benar.")
        except KeyboardInterrupt:
            print("\n\nProgram dihentikan oleh user.")
            break
        
        # Tanya apakah ingin kembali ke menu
        input("\nTekan Enter untuk kembali ke menu utama...")


# Jalankan program utama
if __name__ == "__main__":
    main()
