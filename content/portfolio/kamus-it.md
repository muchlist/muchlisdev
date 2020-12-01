---
date: "2016-11-05T19:41:01+05:30"
title: "Kamus IT (2019)"
draft: false
image: "img/portfolio/kamus-it-front.webp"
showonlyimage: false
weight: 20
tags: ["kotlin", "retrofit", "mvvm", "django"]
categories: ["android"]
---

Aplikasi kamus yang berisi penjelasan istilah, tips dan tutorial dalam teknologi informasi.
<!--more-->

Sejak 2015, saya memiliki blog tentang IT. Karena terlalu mengoptimalkan SEO maka satu tulisan dalam blog dibuat minimal 800 kata. Disinilah masalahnya. Ada banyak istilah-istilah yang bisa dijelaskan dengan singkat yang ingin saya tulis juga namun berlawanan dengan aturan pada blog saya itu (artikel harus panjang). Maka saya membuat aplikasi ini.

![kamus it][gif]

{{< gplaybadge "https://play.google.com/store/apps/details?id=com.muchlis.kamusit&pcampaignid=pcampaignidMKT-Other-global-all-co-prtnr-py-PartBadge-Mar2515-1">}}

#### Fitur
- Pencarian istilah komputer dengan database online
- Penjelasan seringkas dan sepadat mungkin
- Navigasi antar artikel yang saling berhubungan melalui link
- Tombol menuju ke halaman web dimana penjelasan lanjutannya tersedia (fitur ini dihilangkan karena blog saya dianggap menulis artikel yang berbahaya, padahal tidak)
- Sorting hasil pencarian berdasarkan abjad atau update terakhir
- Data yang terus diperbaharui (heroku premium dihentikan karena saya keberatan dengan biaya servernya, hehe)



#### Teknologi yang digunakan
1. Android Native / Kotlin
2. Retrofit2
3. Jetpack Navigation
4. Backend Django
5. Postgresql
6. Heroku
  

#### Credits
- **Muchlis** sebagai Android dan Backend developer 


#### Masalah/solusi dalam development
* [Solusi pada Bug penerapan design pattern][bug]
* Heroku free akan membuat aplikasi ini lambat saat load data karena server akan tidur jika tidak diakses dalam 30 menit. Solusinya adalah dengan menerapkan offline first atau membayar server.

[gif]: /img/portfolio/kamus-it.gif
[bug]: {{< ref "problem/mvp-problem.md" >}}