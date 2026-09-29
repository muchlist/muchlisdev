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

A dictionary of IT terms, built because my own blog's SEO rules made short explanations impossible to publish. [Kotlin, Django, PostgreSQL].
<!--more-->

#### Why a blog needed an app

I had been writing an IT blog since 2015. Somewhere along the way I optimised it for search until every post had to run at least 800 words, and that rule quietly made a whole category of writing impossible.

Plenty of terms can be explained properly in three sentences. Padding those three sentences out to 800 words does not serve the person who came looking for the answer; it serves the ranking. So the short explanations needed somewhere else to live. Kamus IT is what the blog's own rules would not let it publish.

![Kamus IT][gif]

#### A glossary is only useful when the entries point at each other

The feature that matters here is not the search box. It is that an explanation can link to the other terms it leans on, so reading one entry leads into the next.

A term you do not understand, explained using four more terms you do not understand, is the failure mode of every glossary. Cross-links are the cheapest repair for it, and they are the reason this is a dictionary rather than a list. Results sort alphabetically or by what changed most recently.

#### The sleeping server

Django and PostgreSQL on Heroku's free tier, which puts a dyno to sleep after thirty minutes without traffic. For an app nobody opens continuously, that meant a good share of first searches paid a cold start before anything appeared on screen.

I wrote the options down at the time as *go offline-first, or pay for the server*. I paid, and later stopped paying because the cost was not worth it to me — at which point the updates stopped too.

Offline-first was the right answer, and not mainly because of the money. A dictionary is close to the ideal case for it: the dataset is small, it changes rarely, and it gets read constantly. Sync a local copy, answer every search from it, refresh in the background when there is a network. The cold start becomes invisible, search becomes instant in a way a round trip never can be, and the app keeps working while the server sleeps — or, as it turned out, after it is switched off for good.

That is the part I would change. The hosting decision and the architecture decision were tangled together, and offline-first would have pulled them apart: whether the app was useful would not have depended on whether I was still paying a monthly bill.

#### Tech stack
1. Android native, Kotlin
2. Retrofit2, Jetpack Navigation
3. Django and PostgreSQL
4. Heroku

#### The first one

Kamus IT is the oldest project on this site and the first of three Kotlin apps. [ITventory](/portfolio/inventaris/) and [ECDR](/portfolio/ecdr/) followed in 2020, and [Risa](/portfolio/risa-flutter/) replaced the whole approach a year after that. The app is no longer listed on the Play Store.

[gif]: /img/portfolio/kamus-it.gif
