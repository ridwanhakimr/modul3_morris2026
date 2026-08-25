"""
Contoh Kode: List (Daftar) di Python
Demonstrasi penggunaan list untuk menyimpan dan mengolah banyak data

Topik: BAB 6.9 - Menyimpan Banyak Data dengan List
Penyusun: Ridwan & Bunga
Modul: Modul 3 - Python Lanjutan
"""

print("="*60)
print("PENGENALAN LIST")
print("="*60)

print("\nContoh 1: Membuat list")
# List kosong
list_kosong = []
print(f"List kosong: {list_kosong}")

# List berisi angka
angka = [10, 20, 30, 40, 50]
print(f"List angka: {angka}")

# List berisi string
nama = ["Alice", "Bob", "Charlie"]
print(f"List nama: {nama}")

# List campuran (boleh tapi tidak disarankan)
campuran = [1, "dua", 3.0, True]
print(f"List campuran: {campuran}")

print("\n" + "="*60)
print("MENGAKSES ELEMEN LIST")
print("="*60)

buah = ["Apel", "Jeruk", "Mangga", "Pisang", "Anggur"]
print(f"List buah: {buah}")
print(f"Jumlah elemen: {len(buah)}")

print("\nAkses dengan indeks (mulai dari 0):")
print(f"Elemen pertama (indeks 0): {buah[0]}")
print(f"Elemen kedua (indeks 1): {buah[1]}")
print(f"Elemen terakhir (indeks 4): {buah[4]}")

print("\nAkses dengan indeks negatif (dari belakang):")
print(f"Elemen terakhir (indeks -1): {buah[-1]}")
print(f"Elemen kedua dari belakang (indeks -2): {buah[-2]}")

print("\n" + "="*60)
print("MENAMBAH ELEMEN KE LIST")
print("="*60)

angka = [1, 2, 3]
print(f"List awal: {angka}")

# Menambah di akhir dengan append()
angka.append(4)
print(f"Setelah append(4): {angka}")

angka.append(5)
print(f"Setelah append(5): {angka}")

# Menambah di posisi tertentu dengan insert()
angka.insert(0, 0)  # Masukkan 0 di indeks 0
print(f"Setelah insert(0, 0): {angka}")

angka.insert(3, 2.5)  # Masukkan 2.5 di indeks 3
print(f"Setelah insert(3, 2.5): {angka}")

print("\n" + "="*60)
print("MENGHAPUS ELEMEN DARI LIST")
print("="*60)

warna = ["Merah", "Hijau", "Biru", "Kuning", "Hijau"]
print(f"List awal: {warna}")

# Hapus berdasarkan nilai dengan remove()
warna.remove("Hijau")  # Hapus "Hijau" pertama yang ditemukan
print(f"Setelah remove('Hijau'): {warna}")

# Hapus berdasarkan indeks dengan pop()
warna_terakhir = warna.pop()  # Hapus elemen terakhir
print(f"Setelah pop(): {warna}")
print(f"Elemen yang dihapus: {warna_terakhir}")

warna_kedua = warna.pop(1)  # Hapus elemen indeks 1
print(f"Setelah pop(1): {warna}")
print(f"Elemen yang dihapus: {warna_kedua}")

# Hapus berdasarkan indeks dengan del
del warna[0]  # Hapus elemen pertama
print(f"Setelah del warna[0]: {warna}")

print("\n" + "="*60)
print("MENELUSURI LIST DENGAN PERULANGAN")
print("="*60)

nilai = [85, 90, 75, 88, 92]
print(f"List nilai: {nilai}")

print("\nCara 1: Dengan for loop (akses nilai langsung)")
for n in nilai:
    print(f"Nilai: {n}")

print("\nCara 2: Dengan for loop (akses indeks dan nilai)")
for i in range(len(nilai)):
    print(f"Indeks {i}: Nilai {nilai[i]}")

print("\nCara 3: Dengan enumerate() (lebih pythonic)")
for i, n in enumerate(nilai):
    print(f"Indeks {i}: Nilai {n}")

print("\n" + "="*60)
print("OPERASI PADA LIST")
print("="*60)

data = [10, 25, 5, 30, 15, 20]
print(f"List data: {data}")

# Menghitung jumlah elemen
print(f"Jumlah elemen: {len(data)}")

# Mencari nilai maksimum dan minimum
print(f"Nilai tertinggi: {max(data)}")
print(f"Nilai terendah: {min(data)}")

# Menghitung total
print(f"Total: {sum(data)}")

# Menghitung rata-rata
rata_rata = sum(data) / len(data)
print(f"Rata-rata: {rata_rata}")

# Mengurutkan (sort)
data_sorted = sorted(data)  # Tidak mengubah list asli
print(f"Data terurut (sorted): {data_sorted}")
print(f"Data asli masih: {data}")

data.sort()  # Mengubah list asli
print(f"Data setelah sort(): {data}")

# Membalik urutan
data.reverse()
print(f"Data setelah reverse(): {data}")

print("\n" + "="*60)
print("STUDI KASUS: PENGOLAHAN DATA NILAI")
print("="*60)

print("Program: Analisis Nilai Mahasiswa")
print("-"*60)

# Data nilai mahasiswa
nilai_mahasiswa = [85, 90, 75, 88, 92, 78, 95, 82, 87, 91]
print(f"Data nilai: {nilai_mahasiswa}")

# Hitung total dan rata-rata
total = sum(nilai_mahasiswa)
rata_rata = total / len(nilai_mahasiswa)
nilai_tertinggi = max(nilai_mahasiswa)
nilai_terendah = min(nilai_mahasiswa)

print(f"\nHasil Analisis:")
print(f"Jumlah mahasiswa: {len(nilai_mahasiswa)}")
print(f"Total nilai: {total}")
print(f"Rata-rata: {rata_rata:.2f}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")

# Hitung jumlah yang lulus (>= 75)
jumlah_lulus = 0
for nilai in nilai_mahasiswa:
    if nilai >= 75:
        jumlah_lulus += 1

print(f"\nJumlah yang lulus (nilai >= 75): {jumlah_lulus}")
print(f"Persentase kelulusan: {jumlah_lulus / len(nilai_mahasiswa) * 100:.1f}%")

# Cari nilai di atas rata-rata
print(f"\nNilai di atas rata-rata ({rata_rata:.2f}):")
for i, nilai in enumerate(nilai_mahasiswa):
    if nilai > rata_rata:
        print(f"  Mahasiswa {i+1}: {nilai}")

print("\n" + "="*60)
print("STUDI KASUS: CARI ELEMEN TERTENTU")
print("="*60)

angka = [3, 7, 1, 9, 4, 7, 2, 7, 5]
print(f"List angka: {angka}")

# Cari apakah angka tertentu ada
cari = 7
if cari in angka:
    print(f"\nAngka {cari} DITEMUKAN dalam list")
    print(f"Jumlah kemunculan: {angka.count(cari)}")
    print(f"Indeks pertama kali muncul: {angka.index(cari)}")
else:
    print(f"\nAngka {cari} TIDAK ditemukan dalam list")

# Cari semua posisi angka tertentu
print(f"\nSemua posisi angka {cari}:")
for i, angka_item in enumerate(angka):
    if angka_item == cari:
        print(f"  Indeks {i}")

print("\n" + "="*60)
print("LIST COMPREHENSION (BONUS)")
print("="*60)

print("Cara singkat membuat list dengan pola tertentu")

# Buat list angka 1-10
angka = [i for i in range(1, 11)]
print(f"Angka 1-10: {angka}")

# Buat list kuadrat dari 1-10
kuadrat = [i**2 for i in range(1, 11)]
print(f"Kuadrat 1-10: {kuadrat}")

# Buat list bilangan genap 1-20
genap = [i for i in range(1, 21) if i % 2 == 0]
print(f"Bilangan genap 1-20: {genap}")

print("\n" + "="*60)
print("TIPS MENGGUNAKAN LIST")
print("="*60)
print("1. Indeks dimulai dari 0, bukan 1")
print("2. Gunakan append() untuk menambah di akhir")
print("3. Gunakan len() untuk mengetahui panjang list")
print("4. List bisa diubah (mutable)")
print("5. Gunakan in untuk cek keberadaan elemen")
print("6. Hati-hati dengan index out of range error")
print("="*60)
