---
title: "Force Close dengan MVP Android"
date: 2020-08-22T11:40:43+08:00
draft: false
showonlyimage: false
weight: 0
---

Design patern MVP pertama kali saya terapkan saat mengikuti kelas beasiswa dari dicoding, ketika itu saya meniru apa yang diajarkan dan tidak ada yang kurang sama sekali. Walaupun saya tiru 100% contoh coding dari tutorial masalah ini masih muncul.

<!--more-->

#### Masalah
Dengan design pattern MVP (Model - View - Presenter) pada android ternyata setiap pergantian activity atau fragment ke activity lain dengan sangat cepat (kurang dari satu detik) bisa menyebabkan force close karena view yang diminta null. Misalnya dengan klik2 tombol navigasi dengan cepat.

Tentu saja ini bukan masalah pada design patternnya, namun pada cara implementasi yang saya gunakan.

#### Solusi
View yang null bukanlah view tujuan, namun view activity asal yang masih akan dipanggil oleh presenter ketika programnya masih berjalan. Jadi presenter masih jalan saat aktifitynya sudah berganti namun masih memanggil aktifity lama dalam prosesnya. Terjadilah forceclose karena dianggap viewnya masih aktifity lama.
Solusinya adalah dengan menggunakan null safety pada constructor view di presenter.

**Contoh class presenter**
{{< gist muchlist 7bd5cdd1e26309f205f987c6d6da6484 >}}

**Contoh interface View**
{{< gist muchlist 1112cba1872eb767bbfd4be57a33a90c >}}

**Contoh fragment yang mengimplementasi ContohView**
{{< gist muchlist 1f1d882eb3983908ebc0f93061eb550a >}}

Dengan menerapkan cara ini, masalah force close pada saat pergantian tampilan yang cepat di aplikasi Android dengan MVP Design Pattern akan teratasi.