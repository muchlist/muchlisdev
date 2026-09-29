---
title: "Kazz — a personal finance app with 18,000 users (2025 - Present)"
date: 2025-06-01T09:00:00+08:00
draft: false
image: "/img/portfolio/kazz-front.webp"
showonlyimage: false
weight: 7
tags: ["flutter", "golang", "genkit", "ai"]
categories: ["android", "backend"]
---

An expense tracker I designed, built, run, and pay for: 18,000 active users across Asia-Pacific, 410,000 transactions logged, and not one feature locked behind the subscription. [Flutter, Golang].
<!--more-->

> Having nobody to say no is not the same as having no constraints. It only means the constraints are yours now.

#### The first time nobody could say no

When eFishery wound down in 2025 I came out of it carrying a list.

Every engineer inside a company has one: the set of things you are reasonably sure are right and have never been allowed to do — not because anyone argued they were wrong, but because each arrived attached to a cost, or a deadline, or a quarter that was already planned. Hexagonal architecture. Idempotent writes. Telemetry across everything rather than across the three endpoints that broke last month. They all lose the same argument, and the argument is never *no*. It is *not now*.

Kazz is that list, built. It is a personal expense tracker: you record what you spend by typing it, saying it, or photographing the receipt, and it tells you where the money went.

The first thing it taught me is the line at the top of this article. The arguments did not stop when I became the only person in the room — they changed owner. Every conviction on that list now bills me personally, every month, which is a more rigorous reviewer than any planning meeting I have sat in.

#### The subscription gates the clock, not the features

There is a paid tier and it locks nothing. Chat, voice input, receipt scanning — a free account does all of it. What the subscription buys is volume: the free allowances are set loose enough for ordinary daily use, and they reset tomorrow or next week rather than locking anything permanently.

That inversion is the decision everything else bends around. The reflex is to put the expensive feature behind the wall, precisely because it is the one costing you money. I put the clock there instead. A feature wall tells someone they picked the wrong tier and leaves them looking at a padlock every day; a resetting allowance tells them to come back tomorrow, and most never reach it at all.

It also means I cannot forecast cost by counting subscribers, because subscribers are not who generates the load. Eighteen thousand people with working access to a language model, underwritten by one bank account, is not a business model — it is a budget. And a budget is a better design brief than a requirements document, because it answers questions a requirements document leaves open. Where should this data live? Whichever side is cheaper to read it from. How long should the server keep it? Exactly as long as it is needed and not one hour longer.

#### Anonymous by design

I started this from the wrong end. The first idea was to make the index itself unreadable — encrypt the data so that holding the database would not be the same as holding the users.

That is a tempting problem and mostly the wrong one, because it defends the data while leaving the *identities* sitting in plain sight beside it. What I settled on instead was making the user anonymous, including to me.

An account is reachable only through a one-way hash of its email address, and that hash is the single route in. No name, no phone number, no profile. Which means that as the administrator of my own system I cannot browse my users, list them, or search for one — I have to already know the address, hash it, and look up that exact value. It works the way the Google Play Console does: you can find a specific person if you already know who you are looking for, and you cannot go fishing.

The cost is real, and worth stating plainly, because a privacy claim with no cost attached usually has no mechanism behind it either. Support gets harder: the first thing I need from anyone who writes in is the address they signed in with, because there is no other route to their account. A system that cannot be browsed cannot be browsed by me either. That is the entire point, and it is also the bill.

#### Which of those convictions earned their keep

Most of the list held. The interesting part is *why* in each case, because the reason is never the one in the article that made you want the technique.

**Idempotency** earned it immediately. Phones on mobile data retry. Without an idempotency key a retry becomes a second transaction, and a duplicate row in a finance app is not a glitch to be cleaned up later — it is a wrong number in somebody's budget, which they will believe, act on, and blame themselves for.

**Cursor pagination** earned it on the same axis. 410,000 transactions across the user base, and every individual history only grows. Offset pagination degrades precisely where your best users live: a year deep in their own records.

**Trigram search** earned it because people name things themselves. Notes arrive in Indonesian and English, abbreviated, misspelled, full of shop names. Exact matching answers almost none of those queries, and a search box that usually returns nothing is abandoned within a week.

**Hexagonal architecture** is the honest one. It justified itself exactly once, when the AI layer underneath changed — and the swap never reached the domain, which is the whole promise, and it was kept. Once is a thin return on the discipline it demands. I would still do it, and I will not pretend the payoff arrived more often than that.

**Telemetry** stopped being a nice-to-have the moment I was the only one running this. There is no second engineer who happens to notice something is off. The instrumentation *is* the on-call rotation.

#### Tech stack
1. Flutter — the Android client, caching the most-opened screens on the device
2. Golang — the API, hexagonal, with idempotent writes and cursor pagination
3. Genkit — the AI layer, covered in [Kazz AI](/portfolio/kazz-ai/)
4. Internationalization and multi-currency, on both the server and the client
5. The landing page at [kalsel.dev](https://www.kalsel.dev/), also mine

#### Where the name came from

The domain is one I have used before.

In 2021 `kalsel.dev` served [KalselDev](/portfolio/kalseldev/), a free REST API I ran so that beginner programmers in Kalimantan could practise against a real server with real authorization instead of a mock. It was retired years ago, and that article on this site says the domain "now serves something else."

This is the something else. Same name, same person, still free — only now it is pointed at people who will never read a line of the code.

Kazz is on [Google Play](https://play.google.com/store/apps/details?id=dev.kalsel.kazz), rated 4.8 from 181 reviews.
