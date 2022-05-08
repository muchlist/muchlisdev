---
title: "Restfull di jaringan lokal dan internet menggunakan IP Publik"
date: 2020-08-23T10:12:29+08:00
draft: false
showonlyimage: false
weight: 0
---

Masalah yang muncul ketika deploy restfull service di lokal network.
<!--more-->

Problem ini terjadi saat mengembangkan aplikasi ECDR dimana situasinya saya rasa cukup menyulitkan proses pengembangan, antara lain :
1. Karena aplikasi ini masih dalam percobaan perusahaan level cabang kecil, maka semua kebutuhan server tidak mengeluarkan biaya apapun, sehingga restfull service (Flask Python) harus di deploy di server lokal.
2. Kebutuhan mengakses server melalui internet dapat dilakukan menggunakan IP Public, jadi ada mekanisme port forwarding yang harus saya lakukan pada jaringan lokal. Untungnya jaringan internet disana menggunakan Astinet sehingga ada IP Publik yang bisa digunakan.

#### Problem

Akses public ip melalui jaringan local mengalami kendala.

Menurut pengamatan saya jika menggunakan jaringan lokal maka ketika mengakses ip address public tidak dianggap sebagai pengakses dari luar sehingga tidak di forward ulang ke IP Lokal pada rule ip & port forwarding. Masalah jaringan ini menjadi terlalu kompleks dengan adanya beberapa alat eksisting seperti Checkpoint proxy dan sebagainya.

#### Solusi
* Problem ini (akses public ip didalam jaringan local) tersolusikan dengan Hairpin NAT. Pada saat menemui problem ini saya belum mengetahui tentang Hairpin NAT ini. karena sudah tersolusikan maka dengan begitu solusi kedua menjadi tidak relevan.
* Membagi jaringan di Android menjadi dua pilihan, user yang harus memilih ketika mengakses aplikasi, jika melalui jaringan kantor maka harus memilih koneksi A dan sebaliknya untuk koneksi B.