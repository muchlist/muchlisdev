---
title: "ITventory (2020)"
date: 2020-08-24T21:38:25+08:00
draft: false
image: "img/portfolio/inventaris-front.gif"
showonlyimage: false
weight: 18
tags: ["kotlin", "retrofit", "mvvm", "flask"]
categories: ["android"]
---

Aplikasi untuk kebutuhan pendataan perangkat IT, stok, riwayat pemeliharaan, pekerjaan harian, status CCTV dll.
<!--more-->

![itventory][image]

#### Latar belakang
1. Koordinasi antar IT yang terpusat di Banjarmasin.
2. Pada cabang Banjarmasin IT bekerja secara rolling shift sehingga diperlukan suatu mekanisme agar satu sama lain mengerti riwayat suatu permasalahan.
3. Laporan dalam bentuk excel dirasa kurang efektif.

#### Benefit
* Menjadi tools IT Regional Kalimantan yang tepat dan serbaguna, mulai dari pencatatan pemakaian stok sampai dengan pemantauan status cctv.

#### Fitur
- Pencatatan barang-barang TIK
- Pencatatan penggunaan stok
- Riwayat tersentralisasi
- Status ping CCTV selama 12 jam terakhir
- Export excel
- Generate QR Code secara masal
- QR Code scanner
- Peringatan bulanan untuk barang inventaris yang perlu diganti
- Navigasi yang ringkas
- Pencatatan pekerjaan harian

#### Teknologi yang digunakan
1. Android Native / Kotlin Mvvm arsitektur
2. MPAndroid Chart
3. Data Binding
4. Retrofit2
5. Backend Flask
6. MongoDB
7. ReportLab python
8. Pandas python

#### Masalah/solusi dalam development
* Masih dalam tahap pengembangan
* Solusi menghindari blocking ping cctv

[image]: /img/portfolio/inventaris2.gif
[problem]: {{< ref "blog/local-server-problem.md" >}}