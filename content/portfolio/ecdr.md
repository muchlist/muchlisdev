---
title: "Electronic Container Damage Report (2019)"
date: 2020-08-22T23:55:25+08:00
draft: false
image: "img/portfolio/ecdr-flow.webp"
showonlyimage: false
weight: 1
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
  

#### Masalah & solusi
* [Menggunakan Server Lokal untuk restfull api dan di onlinekan menggunakan IP Publik, tapi ada masalah.][problem]
* Pada awalnya saya mengembangkan aplikasi ini lengkap dengan fitur persetujuan oleh pengguna jasa (pengguna jasa  memiliki akun sehingga dapat memantau kontainer miliknya), namun fitur tersebut dihilangkan karena suatu hal. Bukan karena fiturnya salah.

#### Credits
- **Muchlis** sebagai android dan backend developer 
- **Muh Junaedhy** sebagai pemilik ide awal

[gif]: /img/portfolio/ecdr.gif
[problem]: {{< ref "problem/local-server-problem.md" >}}