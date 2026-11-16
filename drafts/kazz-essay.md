---
title: "Kazz — a personal finance app with 18,000 users (2025 - Present)"
date: 2025-06-01T09:00:00+08:00
draft: false
image: "/img/portfolio/kazz-front.webp"
showonlyimage: false
weight: 7
tags: ["flutter", "golang", "postgresql", "genkit", "ai"]
categories: ["android", "backend"]
---

An expense tracker I designed, built, and run: 18,000 active users across Asia-Pacific, 410,000 transactions logged, and a free tier whose limits reset instead of running out. [Flutter, Golang, PostgreSQL].
<!--more-->

> Having nobody to say no is not the same as having no constraints. It only means the constraints are yours now.

#### The first time nobody could say no

When eFishery wound down in 2025 I came out of it carrying a list.

Every engineer inside a company has one: the set of things you are reasonably sure are right and have never been allowed to do — not because anyone argued they were wrong, but because each arrived attached to a cost, or a deadline, or a quarter that was already planned. Hexagonal architecture. Idempotent writes. Telemetry across everything rather than across the three endpoints that broke last month. They all lose the same argument, and the argument is never *no*. It is *not now*.

Kazz is that list, built. It is a personal expense tracker: you record what you spend by typing it, saying it, or photographing the receipt, and it tells you where the money went.

The first thing it taught me is the line at the top of this article. The arguments did not stop when I became the only person in the room — they changed owner. Every conviction on that list now has to pay for itself out of the product's own margin, which is a more rigorous reviewer than any planning meeting I have sat in.

#### Rationing by the clock, not the padlock

There is a paid tier and I do want people to buy it. What it sells is headroom, not access.

A free account scans a receipt every couple of days, holds a handful of AI conversations a week, keeps a set number of wallets, and records up to a set number of transactions. Those are real limits and they are not loose by accident. What they never are is permanent: nothing is ever spent for good, and every allowance comes back tomorrow or next week. Pro lifts all the ceilings at once.

The distinction sounds small and it decides how the whole product feels. A padlock tells someone they bought the wrong tier, and it says so again every time they open the screen. A ration tells them to come back tomorrow. One reads as a shop that is closed to you; the other reads as a shop that has sold out of the thing you wanted, which is a far easier thing to forgive — and an easier thing to convert, because the person who keeps hitting a ration already knows exactly what they would be buying.

It also fixes the engineering target. Most users are free users and always will be, so the unit cost of serving one has to be low enough that they are cheap to keep rather than a loss to absorb. That single number is what every decision in [Kazz AI](/portfolio/kazz-ai/) is aimed at, and getting it low enough is why the app pays for its own servers rather than being subsidised by me.

#### Anonymous by design

I started this from the wrong end. The first idea was to make the index itself unreadable — encrypt the data so that holding the database would not be the same as holding the users.

That is a tempting problem and mostly the wrong one, because it defends the data while leaving the *identities* sitting in plain sight beside it. What I settled on instead was making the user anonymous, including to me.

An account is reachable only through a one-way hash of its email address, and that hash is the single route in. No name, no phone number, no profile. Which means that as the administrator of my own system I cannot browse my users, list them, or search for one — I have to already know the address, hash it, and look up that exact value. It works the way the Google Play Console does: you can find a specific person if you already know who you are looking for, and you cannot go fishing.

The cost is real, and worth stating plainly, because a privacy claim with no cost attached usually has no mechanism behind it either. Support gets harder: the first thing I need from anyone who writes in is the address they signed in with, because there is no other route to their account. A system that cannot be browsed cannot be browsed by me either. That is the entire point, and it is also the bill.

#### Which of those convictions earned their keep

Most of the list held. The interesting part is *why* in each case, because the reason is never the one in the article that made you want the technique.

**Idempotency** earned it immediately. Phones on mobile data retry. Without an idempotency key a retry becomes a second transaction, and a duplicate row in a finance app is not a glitch to be cleaned up later — it is a wrong number in somebody's budget, which they will believe, act on, and blame themselves for.

**Cursor pagination** earned it on the same axis. 410,000 transactions across the user base, and every individual history only grows. Offset pagination degrades precisely where your best users live: a year deep in their own records.

**Postgres trigram search** earned it because people name things themselves. Notes arrive in Indonesian and English, abbreviated, misspelled, full of shop names. Exact matching answers almost none of those queries, and a search box that usually returns nothing is abandoned within a week.

**Hexagonal architecture** is the honest one. It justified itself exactly once, when the AI layer underneath changed — and the swap never reached the domain, which is the whole promise, and it was kept. Once is a thin return on the discipline it demands. I would still do it, and I will not pretend the payoff arrived more often than that.

**Telemetry** stopped being a nice-to-have the moment I was the only one running this. There is no second engineer who happens to notice something is off. The instrumentation *is* the on-call rotation.

#### Tech stack
1. Flutter — the Android client, caching the most-opened screens on the device
2. Golang — the API, hexagonal, with idempotent writes and cursor pagination
3. PostgreSQL — including trigram search over user-written notes
4. Genkit — the AI layer, covered in [Kazz AI](/portfolio/kazz-ai/)
5. Internationalization and multi-currency, on both the server and the client
6. The landing page at [kalsel.dev](https://www.kalsel.dev/), also mine

Kazz is on [Google Play](https://play.google.com/store/apps/details?id=dev.kalsel.kazz), rated 4.8 from 181 reviews.
