# Modul 3: Python Lanjutan - MORRIS IF 2026

[![Status](https://img.shields.io/badge/Progress-56%25-yellow)](https://github.com/ridwanhakimr/modul3_morris2026)
[![LaTeX](https://img.shields.io/badge/LaTeX-Document-green)](modul3_python_lanjutan.tex)

Modul pembelajaran Python Lanjutan untuk pelatihan MORRIS IF 2026, mencakup materi percabangan bertingkat, perulangan, list, fungsi, dan aplikasi konsol bermenu untuk mahasiswa baru Teknik Informatika.

## 📋 Informasi Modul

- **Judul**: Python Lanjutan: Struktur Logika Bertingkat, Perulangan, dan Pembangunan Alur Aplikasi Konsol
- **Program**: Pelatihan Dasar Pemrograman MORRIS IF
- **Penyusun**: Ridwan & Bunga
- **Target**: Mahasiswa Baru Teknik Informatika
- **Durasi**: 150 menit
- **Bobot Penilaian**: 20 poin

## 🎯 Status Pengerjaan

**Progress Keseluruhan: 56% (19/34 tugas selesai)**

### ✅ Selesai
- Setup LaTeX (Times New Roman, margin, header/footer, style code)
- BAB 1-5: Identitas, Deskripsi, Tujuan, Kompetensi, Pertanyaan Pemantik
- Semua 12 file Python lengkap di `docs/kode/`

### ❌ Belum Dikerjakan
- BAB 6: Materi Pembelajaran (9 subsection - skip 6.1)
- BAB 7: Latihan dan Tugas (4 latihan - **PRIORITAS TINGGI**)
- BAB 8-9: Catatan Penilaian & Referensi
- Lampiran (opsional)

## 📁 Struktur Folder

```
Modul 3/
├── modul3_python_lanjutan.tex          # File LaTeX utama (545 baris)
├── modul3_python_lanjutan.pdf          # Output PDF (hasil compile)
├── agents.md                           # Panduan untuk AI agent
├── README.md                           # File ini
└── docs/
    ├── STRUKTUR_MODUL_3_PYTHON_LANJUTAN.txt    # Referensi konten
    ├── CHECKLIST_PENGERJAAN_MODUL3.md          # Checklist detail
    ├── listkode.md                             # Daftar file kode
    ├── gambar/                                 # Folder screenshot (kosong)
    └── kode/                                   # 12 file Python lengkap
        ├── latihan3_prima.py                   # Deteksi bilangan prima
        ├── latihan3_nested.py                  # Nested if (kelulusan)
        ├── latihan3_deret.py                   # Deret aritmatika
        ├── tugas3_menu.py                      # Aplikasi menu
        ├── contoh_nested_if.py                 # Contoh BAB 6.2
        ├── contoh_modulo.py                    # Contoh BAB 6.3
        ├── contoh_for_while.py                 # Contoh BAB 6.4
        ├── contoh_break_continue.py            # Contoh BAB 6.5
        ├── contoh_nested_loop.py               # Contoh BAB 6.6
        ├── contoh_pola_bintang.py              # Contoh BAB 6.6
        ├── contoh_list.py                      # Contoh BAB 6.9
        └── contoh_fungsi.py                    # Contoh BAB 6.10
```

## 🚀 Quick Start

### Compile PDF
```bash
pdflatex modul3_python_lanjutan.tex
pdflatex modul3_python_lanjutan.tex  # jalankan 2x untuk update TOC
```

### Test Kode Python
```bash
python "docs/kode/namafile.py"
```

## 📝 Panduan Melanjutkan Pengerjaan

### Urutan Prioritas (Disarankan)

1. **BAB 7 - Latihan dan Tugas** (2 jam) - **PRIORITAS TERTINGGI**
   - Penting untuk mahasiswa
   - Format sudah ada (baris 394-450)
   - Isi: deskripsi, spesifikasi, contoh output

2. **BAB 8-9 - Penutup** (25 menit)
   - BAB 8: 3 bullet points catatan penilaian (baris 516-518)
   - BAB 9: Daftar referensi (baris 527-529)

3. **BAB 6 - Materi Pembelajaran** (7 jam)
   - **SKIP BAB 6.1** (butuh Modul 1)
   - Kerjakan BAB 6.2-6.11 satu per satu
   - Format: penjelasan konsep + kode dari docs/kode + penjelasan output + tips

4. **Lampiran** (1 jam) - Opsional

### Pemetaan Konten BAB 6

| Bagian | File Kode | Baris LaTeX |
|--------|-----------|-------------|
| 6.2 Nested If | contoh_nested_if.py | 251-260 |
| 6.3 Modulo | contoh_modulo.py | 264-273 |
| 6.4 Looping | contoh_for_while.py | 277-290 |
| 6.5 Kontrol | contoh_break_continue.py | 294-300 |
| 6.6 Nested Loop | contoh_nested_loop.py + contoh_pola_bintang.py | 305-312 |
| 6.7 Prima | latihan3_prima.py | 316-327 |
| 6.8 Deret | latihan3_deret.py | 331-340 |
| 6.9 List | contoh_list.py | 344-355 |
| 6.10 Fungsi | contoh_fungsi.py | 359-368 |
| 6.11 Menu | tugas3_menu.py | 372-383 |

## ⚠️ Aturan Penting

### Style LaTeX (JANGAN DIUBAH)
- Font: Times New Roman (package `times`)
- Warna: **SEMUA HITAM** - tidak ada hyperlink biru
- Margin: 3cm kiri/kanan, 2.5cm atas/bawah
- Style: formal seperti Word, bukan tutorial warna-warni
- Code listing: background abu-abu, line numbers, tanpa syntax highlighting warna

### Saat Menambah Konten
- Gunakan `\lstinputlisting{docs/kode/namafile.py}` untuk embed file Python
- Gunakan `\begin{lstlisting}...\end{lstlisting}` hanya untuk snippet inline
- Bahasa Indonesia formal
- Test kode Python dulu sebelum masukkan ke LaTeX

### Yang Harus Dihindari
- ❌ Jangan ubah style/warna yang sudah ada
- ❌ Jangan buat file Python baru (sudah lengkap semua)
- ❌ Jangan kerjakan BAB 6.1 (terblokir - butuh Modul 1)
- ❌ Jangan compile setiap edit kecil
- ✅ Compile hanya saat testing perubahan besar
- ✅ Jalankan pdflatex **DUA KALI** untuk update TOC

## 📚 File Referensi

Baca file ini sebelum mulai mengisi konten:

1. **`docs/STRUKTUR_MODUL_3_PYTHON_LANJUTAN.txt`**
   - Berisi outline lengkap konten yang harus ada
   - Referensi utama untuk apa yang harus ditulis

2. **`docs/CHECKLIST_PENGERJAAN_MODUL3.md`**
   - Breakdown detail per subsection
   - Estimasi waktu tiap tugas
   - Panduan pengisian bertahap

3. **`agents.md`**
   - Panduan ringkas untuk AI agent
   - Kesalahan umum yang harus dihindari
   - Nomor baris penting di file LaTeX

4. **File Python di `docs/kode/`**
   - Semua kode sudah lengkap dan bisa dijalankan
   - Tinggal dijelaskan di LaTeX

## 🛠️ Tools yang Dibutuhkan

- LaTeX distribution (MiKTeX/TeX Live)
- Python 3.8+
- Visual Studio Code (opsional, untuk edit LaTeX)
- Git (untuk version control)

## 📊 Estimasi Waktu

| Bagian | Estimasi |
|--------|----------|
| BAB 7 (Latihan) | 2 jam |
| BAB 8-9 (Penutup) | 25 menit |
| BAB 6 (Materi) | 7 jam |
| Lampiran | 1 jam |
| Review & Finalisasi | 30 menit |
| **TOTAL** | **~11 jam** |

## 🤝 Kontribusi

Proyek ini dikerjakan bersama oleh:
- **Ridwan** - Setup awal, struktur, kode Python
- **Bunga** - Konten LaTeX (lanjutan)

## 📞 Kontak

Untuk pertanyaan atau bantuan:
- Organisasi: Panitia MORRIS IF 2026 - Divisi Akademik
- Repository: https://github.com/ridwanhakimr/modul3_morris2026

## 📄 Lisensi

Modul ini dibuat untuk keperluan internal pelatihan MORRIS IF 2026.

---

**Terakhir diupdate:** 25 Agustus 2026  
**Status:** Work in Progress (56% selesai)
