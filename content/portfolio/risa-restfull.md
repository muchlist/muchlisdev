---
title: "Risa REST API (2021)"
date: 2021-02-28T21:38:25+08:00
draft: false
image: "/img/portfolio/risa-icon.jpg"
showonlyimage: false
weight: 13
tags: ["golang", "mongodb", "jwt", "fiber"]
categories: ["backend"]
---

Backend and scheduler for Risa, the IT asset and maintenance system used across Pelindo III's Kalimantan region. [Golang, MongoDB].
<!--more-->

Risa is what IT staff and vendors across seven Pelindo III branches in Kalimantan used to track equipment, maintenance history, daily checks, and stock. This is its backend: a Golang REST API on Fiber, MongoDB for storage, and a scheduler watching device health in the background. The [Flutter app](/portfolio/risa-flutter/) is the other half.

#### One search box across every device type
- Built `gen_unit`, a projection collection mirroring the fields every device has in common, so that a single search field could find anything in the estate regardless of its category.

![The gen_unit projection behind a single search box][genunit]

The request was easy to state and awkward to implement. Staff wanted to type a device name or an IP address into one box and find it, without first deciding whether they were looking for a CCTV camera, a computer, or an application. Each category has its own shape and its own collection, so no single query could reach across all of them.

`gen_unit` answers that by keeping one slim entry per device — name, IP, category, branch — written alongside every create, edit, and delete, and refreshed whenever a device's history changes. Nobody writes to it directly; it is maintained behind the scenes. The vocabulary I would use now is *read model*, and I would build it again. What I would not repeat is the search itself: it scans, so it slows as the estate grows. Moving it to Elasticsearch was already the plan on record.

#### Tracking work on a device
- Modeled `history` as a status lifecycle — info, in progress, awaiting approval, pending, complete — with nested entries, so one incident can be replayed and reported over a date range.

Every incomplete history entry increments a `cases` counter on that device's `gen_unit` entry, and completing it decrements the counter. Same trade as above: the write path does more work so a list of devices can show which ones need attention without a second query per row.

#### Daily checks that follow the shift
- Generated check lists from templates, matched to whichever shift is running at the moment the check is created.

An item flagged as a problem does not vanish when the check is submitted — it reappears on the next one, and keeps reappearing until somebody resolves it. `checklist_cctv` is deliberately separate: vendor maintenance runs on its own cadence and is done by different hands.

#### Stock as a single document
- Stored each stock item as one document, with usage and restock entries as children that adjust a `qty` field on write.

MongoDB makes this shape cheap and it suited the volume. A stock item and its movements are almost always read together and never read by anyone else, so there was nothing to gain by splitting them.

#### The scheduler
- Ran an hourly job to find CCTV cameras failing their ping and push a notification to the affected users through Firebase.

The ping results come from a separate small service called *pingers*. Keeping that out of the API meant the long-running network work never sat in the request path.

#### Structure

Handler → Service → Dao, with a separate client package for outside services.

- **Handler** extracts and validates input — params, query, JSON body, JWT claims — and normalizes case before anything downstream sees it.
- **Service** holds the business logic: composing two or more DAOs, converting strings to ObjectIDs, filling in what a DAO needs.
- **Dao** talks to the database. Case normalization matters again here, because an index on a case-sensitive field is only useful if the values going in are consistent.

This is the ancestor of the golden path repository I set up years later at [Hukumonline](/portfolio/hukumonline/) — the same instinct to keep business logic away from the database driver, arrived at before I had the vocabulary for it.

#### Tech stack
1. Golang, Fiber
2. MongoDB
3. gocron for scheduling, Maroto for PDF reports, Firebase for push notifications, ozzo-validation for request bodies
4. [erru_utils](https://github.com/muchlist/erru_utils_go) — a small library of my own giving every service the same error response and log format

One dependency has aged badly: JWT signing went through `dgrijalva/jwt-go`, which was later abandoned by its author and superseded by the maintained `golang-jwt/jwt` fork. Anything still building on it today should move.

#### Source code
- [risa_restfull](https://github.com/muchlist/risa_restfull) — the Golang backend
- [risa2](https://github.com/muchlist/risa2) — the Flutter app

[genunit]: /img/portfolio/risa-gen-unit.svg
