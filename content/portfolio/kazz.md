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

A personal expense tracker on Android: record what you spend by typing, speaking, or photographing the receipt — or let the app lift it straight out of your bank notifications — then hold it to a budget and ask the app what the month looked like. [Flutter, Golang, PostgreSQL].
<!--more-->

Kazz is mine end to end — the Flutter app, the Go backend, and the landing page at [kalsel.dev](https://www.kalsel.dev/). It runs across Asia-Pacific with more than 18,000 active users and 410,000 transactions logged, rated 4.8 from 181 reviews on [Google Play](https://play.google.com/store/apps/details?id=dev.kalsel.kazz). Android today; iOS later in 2026.

![The home screen][home]

#### What it does
- record transactions by typing, by voice, or by scanning a receipt
- turn bank and e-wallet notifications into drafts on their own, confirmed in a batch
- ask Kazz AI about your own spending and have it draw the chart
- keep several wallets — cash flow, savings, a hidden-balance pocket, a gold pocket valued at the current price
- share a wallet with a partner or family, synced in real time
- budget by week, month, quarter, year, or a range you choose, with alerts
- classify spending as Need, Want, or Save, the Kakeibo way
- split a scanned bill evenly, per item, or by percentage
- track loans and recurring transactions
- read daily, weekly, and monthly reports, with a heatmap of the days the money left
- spend in one currency and read the totals in yours

#### Notifications become drafts

This is the feature that changes how the app is used.

Every expense tracker has the same real problem, and it is not data entry — it is memory. People do not abandon these apps because logging is hard; they abandon them because three days go by, four transactions are gone, and the totals are now fiction. Once the numbers are wrong, there is no reason to open it again.

So Kazz reads the notifications your bank and e-wallet apps already post to your phone, and saves them as drafts. They arrive on their own, at the moment the money moved. Later you open the list, tap once, and the AI turns the batch into transactions.

The drafts matter as much as the capture. Nothing is recorded until you accept it, which keeps the automation on the right side of the line: it does the remembering and the typing, and you keep the decision. And it does not involve your bank: these are notifications your phone has already been sent, read on the device rather than through an account you have to connect.

#### Three ways to enter one yourself

![Logging a transaction][inputs]

For everything that never produced a notification — cash, a market stall, splitting something with a friend — typing works and nobody enjoys it. Say the transaction instead and it comes back parsed into amount, category, and wallet.

![Receipt scan][scan]

Or photograph the receipt and get the line items back itemised.

#### Asking instead of reading

Every chart in an app answers a question somebody anticipated in advance. The chat answers the ones nobody did.

Ask where the money went last month, how much is left in the food budget, or how this month compares with February, and the answer is built from your own transactions — with the chart drawn alongside it when the shape matters more than the total. You can record a transaction by saying it in the chat, and ask about Kazz itself when you cannot find a feature.

It is not reserved for subscribers. Every account gets it; the free tier rations how often rather than locking it away. [Kazz AI](/portfolio/kazz-ai/) covers how it is built.

#### Wallets that behave differently

![Wallets and pockets][pockets]

A wallet is not one kind of thing. Cash flow is money you are spending this month. Savings is money you are not. The hidden-balance pocket exists because seeing a number makes it tempting — you can fund it and the balance stays out of sight. The gold pocket tracks weight rather than money and re-values itself as the price moves, so net worth stays honest without you maintaining it.

#### How a budget stays current

![How a budget is recalculated][budget]

A budget in Kazz is a set of pocket-and-category pairs with an amount and a period, so *groceries and eating out, from the household wallet, this month* is one budget rather than three.

Keeping its total current is the interesting part. Recalculating inside the request would make saving a transaction slower for everyone, including the overwhelming majority of transactions that no budget is watching. So the write path asks one cheap question first — does any budget care about this pocket and category? — and only then hands the work to a background worker. The screen reads a stored number and adds nothing up.

Crossing the alert threshold raises one notification per period rather than one per transaction, and on Pro a budget that reaches its end date is cloned into the next period automatically.

#### Seeing the shape of a month

![Spending heatmap][heatmap]

Reports run daily, weekly, and monthly, and compare against the period before. A heatmap marks the days money actually left, which is usually a more useful answer than a category total: most people are not overspending steadily, they are overspending on particular days.

Your financial month does not have to start on the 1st — set it to the day you are paid and every report follows.

#### Shared wallets and two currencies

A wallet can be shared with a partner or a parent, and everyone on it sees the same balances as they change. What stays private stays private: sharing is per wallet, not per account.

Amounts are stored in the currency they were spent in and displayed in yours, which matters for anyone earning in one place and spending in another.

#### Why the home screen opens quickly

Home is the screen people open most and usually the screen with the least news on it — you checked an hour ago and nothing has happened since.

So the app keeps its own copy and asks the server a conditional question rather than a fresh one. When nothing has changed the answer is a `304` with no body at all, and the screen redraws from what the phone is already holding. It is cheap on both sides: no payload to send, no payload to parse, and the common case costs almost nothing.

#### What Kazz does not keep

Sign-in is through Google, and that is all the identity there is — no name, no phone number, no profile. Accounts are addressed by a one-way hash of the email, which means the user list cannot be browsed, including by me.

#### Tech stack
1. Flutter — the Android app, with the home screen served from its local copy when nothing has changed
2. Golang — the API, hexagonal, with idempotent writes and cursor pagination
3. PostgreSQL — including trigram search across user-written notes
4. Redis and a job queue — budget recalculation, alerts, and scheduled work
5. Genkit — the AI layer, described in [Kazz AI](/portfolio/kazz-ai/)
6. OpenTelemetry — traces and metrics across every service call

[home]: /img/portfolio/kazz-home.webp
[inputs]: /img/portfolio/kazz-inputs.webp
[scan]: /img/portfolio/kazz-scan.webp
[pockets]: /img/portfolio/kazz-pockets.webp
[budget]: /img/portfolio/kazz-budget-flow.svg
[heatmap]: /img/portfolio/kazz-heatmap.webp
