---
title: "Electronic Container Damage Report (2020)"
date: 2020-08-22T23:55:25+08:00
draft: false
image: "/img/portfolio/ecdr-demo.webp"
showonlyimage: false
weight: 19
tags: ["kotlin", "retrofit", "mvvm", "flask", "mongodb"]
categories: ["android"]
---

Photographic evidence of container condition at every checkpoint in the port, replacing a paper form that carried no photos and needed a signature collected in person. [Kotlin, Flask, MongoDB].
<!--more-->

![ECDR][gif]

#### What the port was actually paying for

The port kept receiving claims from customers for container damage said to have occurred on its premises. Some of those claims were sound and some were not, and there was no reliable way to tell them apart, because the inspection document carried no photographs by default. Whoever held the better record won the argument, and the port did not hold the better record.

That is the entire business case. Everything about ECDR that looks like a productivity win — time saved, paper not printed — sits a long way behind the one thing that matters: when a claim arrives months later, there is a timestamped photograph of that container taken on its way in.

#### Four checkpoints, six sides

![How an inspection is recorded and approved][flow]

An inspection captures all six sides of a container along with the truck driver, and it happens at four points across the yard rather than once. Gate In and CY-Stack are the two visible in the screenshots.

Recording condition at each handoff is what turns *it arrived damaged* into something specific enough to act on: intact at the gate and damaged at the stack is the port's problem, and damaged at the gate is not. A single inspection can only ever establish the second. Four of them establish where in the chain the damage appeared.

A later checkpoint reopens the same container record instead of starting a new one, and photos can be copied forward from the previous step. Six sides across four checkpoints is a great many photographs, and most of them genuinely have not changed between two points in the same yard.

The photograph of the driver is the detail I would still defend. It stands in for a signature — you cannot reliably collect a written one from a driver at a gate, and a photograph of the person who brought the container is both harder to dispute and faster to capture than anything involving a pen.

#### The public IP that would not answer from inside the building

![The connection picker I shipped, and the Hairpin NAT that should have replaced it][hairpin]

This was a branch-level trial with no budget for infrastructure, so the Flask API ran on an Ubuntu box on site. Reaching it from outside the port meant a public IP — the branch ran Astinet, so one was available — together with port forwarding on the local network.

Then the part that cost me days. Requests to that public address from *inside* the same LAN never came back. The router saw a client on its own network rather than traffic arriving from outside, so the forwarding rule never applied, and the path was muddier still for the equipment already sitting in it, a Checkpoint proxy among other things.

What I shipped was a connection switch in the app: choose A on the office network, B everywhere else. It worked, and it was the wrong answer. It took a routing problem I had not solved and handed it to whoever was holding the phone, who now had to know which side of the firewall they were standing on in order to file a report.

The right answer has a name I did not know then: **Hairpin NAT**, also called NAT loopback or NAT reflection. The router recognises traffic aimed at its own public address from the inside and turns it back toward the local server. One address, correct from anywhere, and the picker stops needing to exist.

#### Tech stack
1. Android native, Kotlin, MVVM with Data Binding
2. Retrofit2
3. Flask and MongoDB
4. ReportLab for the *berita acara* and the range reports
5. An Ubuntu server on site

#### Recognition

ECDR was one of the two apps recognised at Pelindo III's Innoreactivation event in 2021; the other was [ITventory](/portfolio/inventaris/). The category was best *implemented* idea, and the case for this one was put by the branch that ran it — [the full story is here](/portfolio/penghargaaan/).

[gif]: /img/portfolio/ecdr.gif
[flow]: /img/portfolio/ecdr-inspection-flow.svg
[hairpin]: /img/portfolio/ecdr-hairpin-nat.svg
