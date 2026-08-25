# AGENTS.md - Modul 3 Python Lanjutan (MORRIS IF 2026)

Modul pembelajaran Python berbasis LaTeX untuk mahasiswa baru. File utama: `modul3_python_lanjutan.tex`. Semua contoh kode Python sudah lengkap di `docs/kode/`.

## Perintah Penting

**Compile PDF:**
```bash
pdflatex modul3_python_lanjutan.tex
pdflatex modul3_python_lanjutan.tex  # jalankan 2x untuk update daftar isi
```

**Test kode Python:**
```bash
python "docs/kode/namafile.py"
```

## Struktur Proyek

- `modul3_python_lanjutan.tex` - file LaTeX utama (545 baris, struktur lengkap, konten masih kosong)
- `docs/CHECKLIST_PENGERJAAN_MODUL3.md` - breakdown tugas detail dengan estimasi waktu
- `docs/STRUKTUR_MODUL_3_PYTHON_LANJUTAN.txt` - referensi konten tiap bagian
- `docs/kode/*.py` - 12 file Python lengkap siap dipakai
- `docs/gambar/` - kosong, untuk screenshot (opsional)

## Aturan Style LaTeX

**Format yang tidak boleh diubah (sudah dikonfigurasi):**
- Font: Times New Roman via package `times`
- Warna: SEMUA HITAM - tidak ada hyperlink biru atau kotak berwarna
- Margin: 3cm kiri/kanan, 2.5cm atas/bawah
- Style: dokumen formal (seperti Word), bukan tutorial warna-warni
- Code listing: `pythonstyle` (background abu-abu, line numbers, tanpa warna)

**Saat menambah konten:**
- Gunakan `\lstinputlisting{docs/kode/namafile.py}` untuk embed file Python
- Gunakan `\begin{lstlisting}...\end{lstlisting}` hanya untuk snippet kecil inline
- Itemize/enumerate biasa, tanpa kotak fancy
- Bahasa Indonesia formal (target: mahasiswa baru)

## Pemetaan Konten (Krusial)

Setiap subsection BAB 6 dipetakan ke file Python tertentu:

| Bagian | File | Status |
|--------|------|--------|
| 6.1 | (skip - butuh Modul 1) | terblokir |
| 6.2 | contoh_nested_if.py | kosong |
| 6.3 | contoh_modulo.py | kosong |
| 6.4 | contoh_for_while.py | kosong |
| 6.5 | contoh_break_continue.py | kosong |
| 6.6 | contoh_nested_loop.py + contoh_pola_bintang.py | kosong |
| 6.7 | latihan3_prima.py | kosong |
| 6.8 | latihan3_deret.py | kosong |
| 6.9 | contoh_list.py | kosong |
| 6.10 | contoh_fungsi.py | kosong |
| 6.11 | tugas3_menu.py | kosong |

Semua file Python sudah ada dan lengkap. Bagian LaTeX sudah ada header tapi belum ada konten.

## Prioritas Pengerjaan (dari checklist)

1. **BAB 7** (Latihan dan Tugas) - prioritas tertinggi untuk mahasiswa
   - Tiap dari 4 latihan butuh: deskripsi, spesifikasi (input/proses/output), contoh output
   - Format sudah ada (modul3_python_lanjutan.tex:394-450)
   
2. **BAB 8-9** (cepat: 25 menit total)
   - BAB 8: Isi 3 bullet points di baris 516-518
   - BAB 9: Tambah referensi di baris 527-529

3. **BAB 6.2-6.11** (terbesar: ~7 jam)
   - Tiap subsection: penjelasan konsep (1-2 paragraf) + kode dari docs/kode + penjelasan output + tips

4. **Lampiran** (opsional, prioritas rendah)

## Kesalahan yang Harus Dihindari

- Jangan tambah warna/styling - semua sudah hitam/formal
- Jangan buat file Python baru - pakai yang sudah ada di docs/kode/
- Jangan skip konten BAB 6.1 (terblokir - butuh Modul 1)
- Jangan kerjakan beberapa BAB sekaligus - selesaikan satu bagian dulu sebelum lanjut
- Jangan compile tiap edit - compile hanya saat testing perubahan besar
- Jalankan pdflatex dua kali (bukan sekali) - diperlukan untuk update TOC

## File Referensi

Baca file ini sebelum menulis konten:
- `docs/STRUKTUR_MODUL_3_PYTHON_LANJUTAN.txt` - apa yang harus dicakup konten
- `docs/CHECKLIST_PENGERJAAN_MODUL3.md` - breakdown detail per subsection
- File Python terkait di `docs/kode/` - kode yang akan dijelaskan

## Referensi Struktur LaTeX

Nomor baris penting di modul3_python_lanjutan.tex:
- 103-189: BAB 1-5 (lengkap)
- 235-383: Struktur BAB 6 (header saja, konten kosong)
- 387-450: Struktur BAB 7 (format ada, konten kosong)
- 452-530: BAB 8-9 (sebagian, butuh bullet points)
- 535-544: Lampiran (kosong)

## Progress: 56% (19/34 tugas)

**Selesai:** Setup, BAB 1-5, semua 12 file Python
**Tersisa:** Konten BAB 6 (9 bagian), BAB 7 (4 latihan), poin BAB 8-9, Lampiran (opsional)
