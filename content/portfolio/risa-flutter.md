---
title: "Risa Android App (2021)"
date: 2021-02-28T21:38:25+08:00
draft: false
image: "/img/portfolio/risa-front.webp"
showonlyimage: false
weight: 14
tags: ["flutter", "dart", "provider", "firebase"]
categories: ["android"]
---

The Flutter app IT staff and vendors carried into the field across seven Pelindo III branches — inventory, daily checks, reports, and alerts. [Flutter, Dart].
<!--more-->

Risa is the mobile half of the IT asset and maintenance system whose [backend](/portfolio/risa-restfull/) I also built. It went to IT staff and vendors across seven Pelindo III branches in Kalimantan: Banjarmasin, Sampit, Bagendang, Kotabaru, Batulicin, Kumai, and Bumiharjo.

It shipped through the Play Store but was never open to the public — access was restricted to Pelindo staff, and the listing has since been taken down.

#### Screenshots
![screenshot 1][ss1]
![screenshot 2][ss2]
![screenshot 3][ss3]

#### What it does
- maintenance history
- report exports
- equipment inventory
- stock management
- speed test and CCTV monitoring
- daily check lists
- vendor CCTV maintenance checklists
- repair tasks and their progress
- alerts for devices in trouble

#### Written for people holding a phone in a machine room

The daily check is the screen that got the most use, and it is built around the shift the technician is actually working — the list they are handed is generated for that moment, and an item someone flagged as a problem keeps coming back on the next check until it is resolved.

Two details mattered more than they look. Photo evidence is captured and compressed on the device before upload, which is the difference between a report that sends and one that times out. And the search field is a single box: type a name or an IP and the device comes back whatever category it belongs to. That is the user-facing end of the `gen_unit` projection described in the [backend article](/portfolio/risa-restfull/) — the app is the reason that mechanism exists.

PDF reports are generated server-side and opened on the device. Alerts arrive through Firebase Messaging when the backend's hourly job finds a camera failing its ping.

#### My first Flutter app

The three Android apps before this one — [Kamus IT](/portfolio/kamus-it/), [ITventory](/portfolio/inventaris/), and [ECDR](/portfolio/ecdr/) — were Kotlin with Retrofit and MVVM. Risa is where I moved to Flutter, and it is still the stack I reach for when I need a mobile app.

#### Structure

`api` → `models` → `providers` → `screens`, which is the same separation the backend uses, one layer thinner. Dio handles HTTP, `json_serializable` generates the models through `build_runner`, and Provider holds the state each screen listens to.

#### Tech stack
1. Flutter, Dart
2. Provider for state, Dio for HTTP, json_serializable for models
3. Firebase Messaging with flutter_local_notifications
4. fl_chart, photo_view, image_picker with flutter_image_compress

#### Source code
- [risa2](https://github.com/muchlist/risa2) — the Flutter app
- [risa_restfull](https://github.com/muchlist/risa_restfull) — the Golang backend

[ss1]: /img/portfolio/risa-ss-1.webp
[ss2]: /img/portfolio/risa-ss-2.webp
[ss3]: /img/portfolio/risa-ss-3.webp
