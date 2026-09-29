---
title: "Kazz AI — the assistant inside Kazz (2025 - Present)"
date: 2025-09-01T09:00:00+08:00
draft: false
image: "/img/portfolio/kazz-ai-front.webp"
showonlyimage: false
weight: 8
tags: ["golang", "genkit", "ai", "llm", "openrouter"]
categories: ["backend", "ai"]
---

The AI layer of [Kazz](/portfolio/kazz/): a chat that answers questions about your own spending, receipt and voice capture, automatic categorisation, split-bill maths, and a written review of the month. [Golang, Genkit].
<!--more-->

Every account gets this, not only paying ones. The free tier rations how often rather than locking anything away, and the allowances reset instead of running out.

![A written review of the month][insight]

#### What it does
- answer questions about your own transactions, in plain language
- generate a weekly or monthly review whenever you ask for one
- draw the chart that goes with an answer, rather than leaving you a paragraph of numbers
- record a transaction from a sentence you type or say
- read a photographed receipt into itemised expenses
- suggest a category for a transaction instead of asking you to pick one
- split a scanned bill evenly, per item, or by percentage
- answer questions about Kazz itself — where a feature lives, what it does

#### Asking about your own money

![Kazz AI chat][chat]

The chat is not a general assistant that happens to know about finance. It is scoped to one person's records: *where did the money go last month*, *how much is left in the food budget*, *compare this month to February*. Answers come from your actual transactions, not from the model's impression of what a month usually looks like.

When the answer involves a breakdown, a comparison, or a trend, the reply carries the chart with it. A written total tells you the number; the chart tells you the shape, and the shape is normally what the question was really about.

#### The monthly review

![The detailed report][report]

The review is written prose rather than a dashboard — what went up, what went down, which days did the damage, and what that suggests for next month. It compares against the previous period, so "high" means high for you rather than high in the abstract.

It is generated off the request path. You ask, the work is queued, a notification arrives when it is ready. Nobody waits on a spinner for a language model, and the load spreads out rather than landing all at once at the start of the month.

#### Capture, not typing

Receipt scanning and voice entry both end in the same place: a draft transaction with an amount, a category, and a wallet already filled in, waiting for you to confirm it. Categorisation runs on ordinary typed entries too.

![Split bill][splitbill]

Split bill is the same capability pointed at a shared receipt. Scan the bill, divide it evenly, by item, or by percentage, and the amounts each person owes come out the other side.

#### What the model is not trusted with

Anything the model returns about your figures is checked against the real aggregates before it is stored, and anything it invents is dropped and counted. A number that reaches you has been verified against your own records, because a plausible wrong figure in a finance app is worse than no figure at all.

Chat sessions carry an expiry, and the length is chosen in the app — three hours unless you change it.

#### Tech stack
1. Golang with Genkit — tools, structured output, and streaming
2. OpenRouter and OpenAI behind a single port, with a per-request price ceiling
3. A job queue and worker for report generation, delivered by push notification
4. PostgreSQL for the stored reviews and conversation state
5. Prompts and reports localised per user, in the user's own currency
6. OpenTelemetry traces and metrics through every call

#### Where it sits

The reviews do not run in the request path, which is the same trade I made in [ITventory](/portfolio/inventaris/) in 2020 with a scheduled CCTV ping, and again in [Risa](/portfolio/risa-restfull/) in 2021 with a precomputed read model. Pay on a schedule so the read is free. It was a ping job then and it is a language model now.

[insight]: /img/portfolio/kazz-ai-insight.webp
[chat]: /img/portfolio/kazz-ai-chat.webp
[report]: /img/portfolio/kazz-ai-report.webp
[splitbill]: /img/portfolio/kazz-splitbill.webp
