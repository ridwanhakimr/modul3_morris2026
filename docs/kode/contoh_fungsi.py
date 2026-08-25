"""
Contoh Kode: Fungsi (Def) untuk Merapikan Program
Demonstrasi pembuatan dan penggunaan fungsi untuk modularisasi kode

Topik: BAB 6.10 - Fungsi (Def) untuk Merapikan Program
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("FUNGSI SEDERHANA TANPA PARAMETER")
print("="*60)

# Definisi fungsi sederhana
def sapa():
    print("Halo, selamat datang!")
    print("Semoga hari Anda menyenangkan!")

# Memanggil fungsi
print("\nMemanggil fungsi sapa():")
sapa()

print("\nFungsi bisa dipanggil berkali-kali:")
sapa()
sapa()

print("\n" + "="*60)
print("FUNGSI DENGAN PARAMETER")
print("="*60)

# Fungsi dengan 1 parameter
def sapa_nama(nama):
    print(f"Halo {nama}, selamat datang!")

print("\nMemanggil fungsi dengan parameter:")
sapa_nama("Alice")
sapa_nama("Bob")
sapa_nama("Charlie")

# Fungsi dengan multiple parameter
def perkenalan(nama, umur, kota):
    print(f"Nama saya {nama}, umur {umur} tahun, tinggal di {kota}")

print("\nFungsi dengan 3 parameter:")
perkenalan("Diana", 20, "Jakarta")
perkenalan("Eko", 22, "Bandung")

print("\n" + "="*60)
print("FUNGSI DENGAN RETURN")
print("="*60)

# Fungsi yang mengembalikan nilai
def tambah(a, b):
    hasil = a + b
    return hasil

print("\nFungsi yang mengembalikan hasil:")
hasil1 = tambah(5, 3)
print(f"5 + 3 = {hasil1}")

hasil2 = tambah(10, 20)
print(f"10 + 20 = {hasil2}")

# Fungsi matematika lainnya
def kuadrat(angka):
    return angka ** 2

def pangkat(basis, eksponen):
    return basis ** eksponen

print(f"\nKuadrat dari 7: {kuadrat(7)}")
print(f"3 pangkat 4: {pangkat(3, 4)}")

print("\n" + "="*60)
print("FUNGSI UNTUK CEK BILANGAN")
print("="*60)

# Fungsi cek ganjil/genap
def adalah_genap(angka):
    if angka % 2 == 0:
        return True
    else:
        return False

# Cara lebih singkat (pythonic)
def adalah_ganjil(angka):
    return angka % 2 != 0

print("Menggunakan fungsi cek bilangan:")
for angka in [10, 15, 22, 33]:
    if adalah_genap(angka):
        print(f"{angka} adalah GENAP")
    else:
        print(f"{angka} adalah GANJIL")

# Fungsi cek prima
def adalah_prima(angka):
    if angka < 2:
        return False
    for i in range(2, angka):
        if angka % i == 0:
            return False
    return True

print("\nCek bilangan prima:")
for angka in [2, 4, 7, 10, 13, 15]:
    if adalah_prima(angka):
        print(f"{angka} adalah PRIMA")
    else:
        print(f"{angka} BUKAN prima")

print("\n" + "="*60)
print("FUNGSI UNTUK PENGOLAHAN LIST")
print("="*60)

# Fungsi hitung rata-rata
def hitung_rata_rata(data):
    total = sum(data)
    jumlah = len(data)
    return total / jumlah

# Fungsi cari nilai tertinggi dan terendah
def cari_min_max(data):
    nilai_min = min(data)
    nilai_max = max(data)
    return nilai_min, nilai_max  # Return multiple values

# Fungsi hitung jumlah lulus
def hitung_lulus(nilai_list, batas_lulus=75):
    jumlah = 0
    for nilai in nilai_list:
        if nilai >= batas_lulus:
            jumlah += 1
    return jumlah

# Test fungsi-fungsi
nilai = [85, 90, 75, 88, 92, 78, 95, 82]
print(f"Data nilai: {nilai}")

rata = hitung_rata_rata(nilai)
print(f"Rata-rata: {rata:.2f}")

min_val, max_val = cari_min_max(nilai)
print(f"Nilai terendah: {min_val}")
print(f"Nilai tertinggi: {max_val}")

lulus = hitung_lulus(nilai)
print(f"Jumlah yang lulus: {lulus}")

print("\n" + "="*60)
print("FUNGSI DENGAN DEFAULT PARAMETER")
print("="*60)

def sapa_lengkap(nama, sapaan="Halo"):
    print(f"{sapaan}, {nama}!")

print("Tanpa parameter sapaan (gunakan default):")
sapa_lengkap("Alice")

print("\nDengan parameter sapaan:")
sapa_lengkap("Bob", "Selamat pagi")
sapa_lengkap("Charlie", "Hi")

# Fungsi perhitungan dengan default
def hitung_diskon(harga, persen_diskon=10):
    diskon = harga * persen_diskon / 100
    harga_akhir = harga - diskon
    return harga_akhir

print(f"\nHarga Rp 100.000 (diskon default 10%): Rp {hitung_diskon(100000):.0f}")
print(f"Harga Rp 100.000 (diskon 20%): Rp {hitung_diskon(100000, 20):.0f}")

print("\n" + "="*60)
print("MEMECAH PROGRAM BESAR DENGAN FUNGSI")
print("="*60)

# Program analisis data dengan fungsi-fungsi

def input_data_nilai():
    """Input data nilai dari user"""
    print("Masukkan nilai mahasiswa (pisahkan dengan spasi):")
    print("Contoh: 85 90 75 88")
    # Simulasi input (dalam program asli gunakan input())
    input_string = "85 90 75 88 92"
    nilai_list = [int(x) for x in input_string.split()]
    return nilai_list

def analisis_statistik(data):
    """Hitung statistik dasar"""
    return {
        'jumlah': len(data),
        'total': sum(data),
        'rata_rata': sum(data) / len(data),
        'tertinggi': max(data),
        'terendah': min(data)
    }

def tampilkan_hasil(stats, data):
    """Tampilkan hasil analisis"""
    print("\n" + "="*60)
    print("HASIL ANALISIS")
    print("="*60)
    print(f"Jumlah data: {stats['jumlah']}")
    print(f"Total nilai: {stats['total']}")
    print(f"Rata-rata: {stats['rata_rata']:.2f}")
    print(f"Nilai tertinggi: {stats['tertinggi']}")
    print(f"Nilai terendah: {stats['terendah']}")

def main():
    """Fungsi utama program"""
    print("Program Analisis Nilai Mahasiswa")
    print("-"*60)
    
    # Gunakan fungsi-fungsi yang sudah dibuat
    data = input_data_nilai()
    print(f"Data yang diinput: {data}")
    
    statistik = analisis_statistik(data)
    tampilkan_hasil(statistik, data)

# Jalankan program utama
main()

print("\n" + "="*60)
print("KEUNTUNGAN MENGGUNAKAN FUNGSI")
print("="*60)
print("1. REUSABILITY: Kode bisa dipakai ulang tanpa copy-paste")
print("2. MODULARITAS: Program terbagi menjadi bagian-bagian kecil")
print("3. READABILITY: Kode lebih mudah dibaca dan dipahami")
print("4. MAINTAINABILITY: Mudah diperbaiki jika ada bug")
print("5. TESTING: Mudah ditest secara terpisah")

print("\n" + "="*60)
print("BEST PRACTICES FUNGSI")
print("="*60)
print("1. Nama fungsi harus deskriptif (hitung_rata_rata, bukan func1)")
print("2. Satu fungsi satu tugas (Single Responsibility)")
print("3. Gunakan docstring untuk dokumentasi")
print("4. Hindari fungsi terlalu panjang (max 20-30 baris)")
print("5. Return value daripada print (lebih fleksibel)")
print("="*60)
