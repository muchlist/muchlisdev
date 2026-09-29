---
title: "Backend Engineer at Majoo Indonesia (2021 - 2022)"
date: 2022-08-31T09:00:00+08:00
draft: false
image: "/img/portfolio/majoo.webp"
showonlyimage: false
weight: 12
tags: ["golang", "kafka", "prometheus", "pprof"]
categories: ["backend"]
---

Mid-level Backend Engineer at a SaaS business management platform for MSMEs, focused on cost calculation systems and performance profiling. [Golang, Kafka].
<!--more-->

Majoo Indonesia is a SaaS-based business management platform offering POS (Point of Sale), accounting, inventory, CRM, and employee management solutions for MSMEs.

#### COGS calculation system
- Designed and developed an automated cost calculation system for **COGS** (*Cost of Goods Sold*) using a Golang API and **Kafka Pub/Sub**.

Cost of goods sold has to be recalculated on every transaction, purchase, or stock adjustment. Running that synchronously in the request path would be expensive, so the work was moved onto Kafka Pub/Sub to let the calculation run asynchronously without blocking user transactions.

![COGS calculation flow][flow]

The merchant's sale is recorded and answered straight away. The same API publishes an event, and the COGS worker picks it up on its own pace — so the cost figures catch up without the cashier ever waiting on them.

#### Performance and profiling
- Implemented **Golang Profiling** and **Prometheus** metrics to keep performance optimal and speed up issue resolution, eliminating memory leak issues.

Profiling with `pprof` is what made the memory leak findable in the first place: reading heap allocations with `top` and `list`, watching GC cycles through `GODEBUG=gctrace=1`, and confirming the fix with load testing before and after. I wrote up the full technique afterwards:

- [Teknik Profiling di Golang](https://blog.muchlis.dev/post/profiling/) — memory and CPU profiling, GC analysis, and verifying the result with load tests.

#### Team contributions
- Acted as a dedicated *code reviewer*, maintaining code quality standards across the team.

#### Tech stack
1. Golang
2. Kafka
3. Prometheus, pprof

[flow]: /img/portfolio/majoo-cogs-flow.svg
