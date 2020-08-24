---
title: "Restfull di jaringan lokal dan internet menggunakan IP Publik"
date: 2020-08-23T10:12:29+08:00
draft: false
showonlyimage: false
weight: 0
---

Masalah yang muncul ketika deploy restfull service di lokal network.
<!--more-->

Problem ini terjadi saat saya mengembangkan aplikasi ECDR, dimana situasinya saya rasa cukup menyulitkan proses pengembangan. Yaitu :
1. Karena aplikasi ini masih dalam percobaan perusahaan cabang, maka semua kebutuhan server tidak mengeluarkan biaya apapun, sehingga restfull service (Flask Python) harus di deploy di server lokal.
2. Membeli domainpun tidak diijinkan sehingga endpointnya masih menggunakan IP Address dan port.
3. Kebutuhan mengakses server melalui internet dapat dilakukan menggunakan IP Public, jadi ada mekanisme port forwarding yang harus saya lakukan pada jaringan lokal. Untungnya jaringan internet disana menggunakan Astinet sehingga ada IP Publik yang bisa digunakan.

#### Problem

Jika aplikasi diakses menggunakan IP Public saja apabila di akses melalui internet diluar kantor, atau IP Local saja jika melalui jaringan kantor tentu ini tidak menjadi masalah, namun bagaimana jika di android saya set IP Publik namun user menggunakan jaringan lokal? Android tidak dapat mengakses server karena routing jaringan menjadi kacau.

Menurut pengamatan saya jika menggunakan jaringan lokal maka ketika mengakses ip address public tidak dianggap sebagai pengakses dari luar sehingga tidak di forward ulang ke IP Lokal. Entahlah, yang jelas masalah jaringan tersebut terlalu kompleks karena melibatkan beberapa alat eksisting seperti Checkpoint proxy dan sebagainya.

#### Solusi
* Dalam hemat saya solusi yang paling efektif adalah dengan membeli domain, sehingga endpoint restfull service bisa diakses melalui domain yang sama (tidak perlu memodifikasi base url di android), tinggal router jaringan lokal saja yang di atur dns nya supaya jika diakses melalui jaringan dalam kantor diarahkan ke IP Lokal. Sayangnya membeli domain tidak diperbolehkan.
* Maka saya membagi jaringan di Android menjadi dua pilihan, user yang harus memilih ketika mengakses aplikasi, jika melalui jaringan kantor maka harus memilih koneksi A dan sebaliknya untuk koneksi B.