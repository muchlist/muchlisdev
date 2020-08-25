---
title: "Electronic Container Damage Report (2020)"
date: 2020-08-22T23:55:25+08:00
draft: false
image: "img/portfolio/ecdr-flow.webp"
showonlyimage: false
weight: 2
---

Electronic Container Damage Report mempercepat, mempermudah dan memperkuat laporan kerusakan kontainer.
<!--more-->

![ecdr][gif]

#### Latar belakang
1. Pihak pelabuhan sering menerima claim dari pengguna jasa atas kerusakan kontainer yang diduga terjadi di area pelabuhan.
2. Untuk membuat dokumen pemeriksaan kerusakan kontainer memerlukan banyak waktu karena petugas harus menggunakan formulir kertas dan menuju foreman untuk mendapatkan tanda tangan.
3. Dokumen Pemeriksaan kerusakan kontainer tidak menyertakan foto sebagai bukti yang kuat secara default.

#### Benefit
1. Aplikasi Ecdr dapat menjadi bukti bahwa : kontainer yang masuk dalam keadaan baik atau sudah dalam keadaan rusak dengan hasil capture 6 sisi container dan foto sopir/pihak kapal melalui android. Sehingga di harapkan dapat mengurangi biaya penggantian kerusakan kontainer yang tidak seharusnya. 
2. Aplikasi ini akan menghemat waktu dan pengeluaran cetak kertas. 
3. Hasil laporan tersimpan pada server dan menjadi arsip yang lebih rapi daripada tumpukan kertas.

#### Fitur
- Pendataan kontainer
- Pengecekan fisik kontainer menggunakan foto di 4 titik lapangan
- Persetujuan Saksi
- Persetujuan Foreman/Manajer
- Copy foto dari pengecekan di step sebelumnya
- Export Berita acara pdf
- Reports pdf semua kontainer pada range ditentukan
- Reports pdf semua kontainer pengecekan pada range ditentukan


#### Teknologi yang digunakan
1. Android Native / Kotlin Mvvm arsitektur
2. Data Binding
2. Retrofit2
4. Backend Flask
5. MongoDB
6. ReportLab python
6. Lokal Ubuntu server di lokasi
  

#### Credits
- **Muchlis** sebagai Android dan Backend developer 
- **Muh Junaedhy** sebagai pemilik ide awal

#### Masalah/solusi dalam development
* [Masalah dalam menggunakan server Lokal untuk restfull api dan IP Publik.][problem]

[gif]: /img/portfolio/ecdr.gif
[problem]: {{< ref "problem/local-server-problem.md" >}}