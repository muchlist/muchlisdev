---
date: "2016-11-05T19:41:01+05:30"
title: "Kamus IT (2019)"
draft: false
image: "/img/portfolio/kamus-it-front.webp"
showonlyimage: false
weight: 20
tags: ["kotlin", "retrofit", "mvvm", "django"]
categories: ["android"]
---

My first Android app built against a backend I wrote, deployed, and paid for myself, instead of a tutorial's mock API. [Kotlin, Django, PostgreSQL].
<!--more-->

#### Why build it at all

By 2019 I could follow an Android tutorial to the end. What I could not do was point at a server and say I had put it there.

Every practice project I had built until then talked to somebody else's sample API, and a sample API quietly removes half of the work. It hands you endpoints that already exist, data somebody else modelled, and uptime somebody else is paying for. You never find out what you do not know, because the parts you do not know have been done for you.

So the point of this one was the whole loop: an Android client, a backend I designed, a database I modelled, on hosting I was answerable for.

#### Why a dictionary

The subject came from a problem I already had. I had been writing an IT blog since 2015, and somewhere along the way I optimised it for search until every post had to run at least 800 words.

That rule quietly made a whole category of writing impossible. Plenty of terms can be explained properly in three sentences, and padding those three sentences out to 800 words does not serve the person who came looking for the answer — it serves the ranking. So the short explanations needed somewhere to live, and I needed something real to build. Kamus IT is both at once.

![Kamus IT][gif]

#### A glossary is only useful when the entries point at each other

The feature that matters here is not the search box. It is that an explanation can link to the other terms it leans on, so reading one entry leads into the next.

A term you do not understand, explained using four more terms you do not understand, is the failure mode of every glossary. Cross-links are the cheapest repair for it, and they are the reason this is a dictionary rather than a list. Results sort alphabetically or by what changed most recently.

#### What owning the server actually taught me

Django and PostgreSQL on Heroku's free tier, which puts a dyno to sleep after thirty minutes without traffic. For an app nobody opens continuously, that meant a good share of first searches paid a cold start before anything appeared on screen.

This is precisely the class of problem a borrowed API never teaches you, because somebody else is keeping it awake. I wrote the options down at the time as *go offline-first, or pay for the server*. I paid, and later stopped paying because the cost was not worth it to me — at which point the updates stopped too.

Offline-first was the right answer, and not mainly because of the money. A dictionary is close to the ideal case for it: the dataset is small, it changes rarely, and it gets read constantly. Sync a local copy, answer every search from it, refresh in the background when there is a network. The cold start becomes invisible, search becomes instant in a way a round trip never can be, and the app keeps working while the server sleeps — or, as it turned out, after it is switched off for good.

The hosting decision and the architecture decision were tangled together, and offline-first would have pulled them apart. That is the thing I actually took away from this project, and I only got to learn it by owning the server rather than borrowing one.

#### Tech stack
1. Android native, Kotlin
2. Retrofit2, Jetpack Navigation
3. Django and PostgreSQL
4. Heroku

#### Where it led

Kamus IT is the oldest project on this site, and the conviction behind it outlasted the app. Two years later I built [KalselDev](/portfolio/kalseldev/) for the same reason turned outward: a free API with real login and real authorization, so that other beginners could practise against a genuine server instead of a mock. I knew the difference was worth the trouble because I had done it the hard way here.

[ITventory](/portfolio/inventaris/) and [ECDR](/portfolio/ecdr/) followed in 2020 — the same Kotlin, but built for people at work rather than for practice. The app itself is no longer listed on the Play Store.

[gif]: /img/portfolio/kamus-it.gif
