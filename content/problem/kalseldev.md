---
title: "KalselDev (2021)"
date: 2021-01-22T21:38:25+08:00
draft: false
image: "/img/portfolio/business-card.jpg"
showonlyimage: false
weight: 16
tags: ["golang", "mongodb", "jwt"]
categories: ["backend"]
---

Restfull api bebas pakai untuk bahan ajaran di komunitas programmer kalimantan mengunakan Golang, Mongodb.
<!--more-->

![windows monitoring][image1]
![windows monitoring][image2]

#### Latar belakang
1. Kebutuhan untuk memonitoring perangkat server cctv yang sering hang karena kapasitas disk penuh.
2. Kebutuhan memantau kondisi semua server dan service-service yang dijalankan di cabang Banjarmasin baik perangkat ber sistem operasi Linux maupun Windows.
3. Belum adanya sistem alerting terhadap peralatan yang krusial apabila terjadi down.

#### Benefit
* IT mengetahui lebih dulu terhadap suatu insiden daripada user dengan sistem alerting.
* IT dapat menganalisa kinerja suatu alat/server.
* IT dapat melakukan tindak pencegahan sebelum terjadi masalah yang lebih besar pada server.

#### Fitur
1. Monitoring resource server seperti :
    - Uptime
    - Penggunaan ram dari waktu kewaktu
    - Penggunaan cpu
    - Jumlah thread yang aktif
    - Penggunaan koneksi/jaringan
    - Penggunaan disk, disk ctivity dan disk i/o
    - Jumlah exception error yang terjadi pada server
    - Jumlah request pada backend service
2. Pemberitahuan (alerting) via email jika :
    - Perangkat down
    - Penggunaan resource melibihi 90%
    - Jumlah error yang melebihi batas

#### Teknologi yang digunakan
1. Database time-series Prometheus
2. Grafana
3. Linux

#### Credits
- **Muchlis** instalasi, konfigurasi, query

[image1]: /img/portfolio/monitoring_win1.webp
[image2]: /img/portfolio/monitoring_win2.webp