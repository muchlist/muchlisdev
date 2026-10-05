---
title: "ITventory (2020)"
date: 2020-08-24T21:38:25+08:00
draft: false
image: "/img/portfolio/inventaris-front.gif"
showonlyimage: false
weight: 18
tags: ["kotlin", "retrofit", "mvvm", "flask", "mongodb"]
categories: ["android"]
---

IT asset records, stock, maintenance history, and CCTV status for Pelindo III's branches across Kalimantan, built for staff working rolling shifts. [Kotlin, Flask, MongoDB].
<!--more-->

![ITventory][image]

#### The question at every shift change

IT at the Kalimantan branches worked rolling shifts, with coordination running through Banjarmasin. The recurring problem was never recording things. It was continuity: whoever came on next needed to know what had already been tried on a device, by whom, and whether it was finished, without phoning the person who had just gone home.

Reporting was Excel, and a spreadsheet is a snapshot somebody emails. It cannot answer *what has happened to this device*, because it has nowhere to put the answer.

So the app is built around a log rather than a table. Every entry names who opened it and who closed it, and those are routinely different people. That is the entire point. One in the screenshot reads *DER POSKO 3 / C066, dead, water got into the LAN cable*, opened by ITOPS and closed by somebody else with a note that the vendor had repaired it. The next person on shift reads that instead of asking.

The branch chips along the top carry an open-issue count each (Banjarmasin, Kumai, Sampit), so the regional picture and the local one are the same screen.

#### Pinging CCTV without freezing the screen

Camera status looks like a trivial feature until you implement it. A camera that is down does not refuse quickly; it goes quiet, and you wait out the full timeout. Ping every camera inside the request that draws the screen, and the screen is slowest exactly when the news is worst.

So the ping moved out of the request path. A scheduled job checks the cameras, writes down what it found, and the app reads what was written. The screen answers immediately, and it shows the last twelve hours of status rather than the state of the network at this instant. That is the more useful question anyway, because a camera that flickered six times overnight is a different problem from one that just went down.

Pay on a schedule so the read is free: the same trade I made again in [Risa](/portfolio/risa-restfull/) with `gen_unit`, and that ping job is the direct ancestor of the separate *pingers* service there.

#### QR codes on the hardware

A record is only worth keeping if you can get from the physical object back to it. A printed code per asset and a scanner in the app turn *which PC is this* into a non-question. Generating the codes in bulk is the part that makes it real. Nobody labels an estate one sticker at a time.

#### Replacement warnings

A monthly warning for equipment due for replacement. It is the only part of the app that speaks before it is spoken to; everything else answers a question somebody thought to ask.

#### Tech stack
1. Android native, Kotlin, MVVM with Data Binding
2. Retrofit2, MPAndroidChart
3. Flask and MongoDB
4. ReportLab for PDF, Pandas for the Excel exports

#### What it became

ITventory ran across Regional Kalimantan and was one of the two apps recognised at [Pelindo III's Innoreactivation event](/portfolio/penghargaaan/) in 2021. A year after building it I rebuilt the same problem from scratch as [Risa](/portfolio/risa-flutter/): Flutter instead of Kotlin, Golang instead of Flask, and a great deal more structure behind it. The problem statement barely changed. What changed was how much of it I already understood before starting.

[image]: /img/portfolio/inventaris2.gif
