---
title: "Electronic Container Damage Report (2019)"
date: 2020-08-22T23:55:25+08:00
draft: false
image: "img/portfolio/problem-mvp.jpg"
showonlyimage: false
weight: 1
---

Electronic Container Damage Report mempermudah membuat laporan kerusakan kontainer.
<!--more-->

![ecdr][image]

#### Latar belakang
1. Pada beberapa kasus, pihak pelabuhan menerima claim dari pengguna jasa atas kerusakan kontainer yang diduga terjadi di area pelabuhan.
2. Untuk membuat dokumen pemeriksaan kerusakan kontainer memerlukan banyak waktu karena petugas  harus menggunakan formulir kertas dan menuju foreman untuk mendapatkan tanda tangan.
3. Dokumen Pemeriksaan kerusakan kontainer tidak menyertakan foto sebagai bukti yang kuat secara default.

#### Benefit
1. Aplikasi Ecdr dapat menjadi bukti bahwa : kontainer yang masuk dalam keadaan baik atau sudah dalam keadaan rusak dengan hasil capture 6 sisi container dan foto sopir/pihak kapal melalui android. Sehingga di harapkan dapat mengurangi biaya penggantian kerusakan kontainer yang tidak seharusnya. 
2. Aplikasi ini akan menghemat waktu dan pengeluaran cetak kertas. 
3. Hasil laporan tersimpan pada server yang mana menjadi arsip yang lebih rapi daripada arsip dalam bentuk tumpukan kertas.

#### Fitur
- Pendataan kontainer
- Pengecekan fisik kontainer menggunakan foto di 4 titik lapangan
- Persetujuan Saksi
- Persetujuan Foreman/Manajer
- Copy foto dari pengecekan di step sebelumnya
- Export Berita acara pdf
- Reports pdf semua kontainer pada range ditentukan
- Reports pdf semua kontainer pengecekan


#### Teknologi yang digunakan
1. Android Native / Kotlin Mvvm arsitektur
2. Data Binding
2. Retrofit2
4. Backend Flask
5. MongoDB
6. ReportLab python
6. Lokal Ubuntu server di lokasi
  

#### Masalah & solusi
* [Solusi pada Bug penerapan design pattern][bug]
* Heroku free akan membuat aplikasi ini terlihat lemot saat load data karena server akan tidur jika tidak diakses dalam 30 menit. Solusinya adalah dengan menerapkan offline first atau membayar server.


#### Credits
- **Muchlis** sebagai android dan backend developer 
- **Muh Junaedhy** sebagai pemilik ide awal


[image]: /img/portfolio/ecdr.png
[bug]: {{< ref "problem/mvp-problem.md" >}}