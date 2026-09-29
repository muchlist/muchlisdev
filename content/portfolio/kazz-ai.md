---
title: "Kazz AI — an AI agent I pay for myself (2025 - Present)"
date: 2025-09-01T09:00:00+08:00
draft: false
image: "/img/portfolio/kazz-ai-front.webp"
showonlyimage: false
weight: 8
tags: ["golang", "genkit", "ai", "llm", "openrouter"]
categories: ["backend", "ai"]
---

The assistant inside [Kazz](/portfolio/kazz/): chat, receipt scanning, voice entry, and written monthly reviews — for 18,000 users, on one person's card. [Golang, Genkit].
<!--more-->

> An agent's cost is decided long before the model is chosen. It is decided by how much you hand it.

#### The constraint comes first

Kazz has a paid tier and it locks nothing. Every account gets the AI; the allowances are loose enough for ordinary daily use and they reset rather than lock. [The main article](/portfolio/kazz/) explains that decision.

The consequence lands here. An agent that must be genuinely useful *and* affordable is being pulled two ways, because the obvious way to improve an agent is to give it more — more tools, more history, more context, a stronger model — and all of that is billed per token. So this is mostly about giving it less without it noticing.

#### A cheap model decides what the expensive one sees

Before the real agent runs, a small classifier reads the message and answers one question: what kind of request is this? It sees at most the last four messages, each truncated to 200 characters — enough to resolve *what about last month?* and nothing more — and returns a route and a confidence at temperature zero.

That label picks the tool set:

- **data** — the full reading set: spending by period, pocket balances, budget status and history, loans, categories
- **knowledge** — two tools
- **record** — one tool
- **general** — none, and the whole data-gathering phase is skipped

Most of what an agent costs is the tools it was offered and did not need. Every definition is schema text in the prompt on every turn, and a model given twelve options reasons about twelve options. Someone asking how to split a bill does not need to be handed the loan ledger.

The part I am pleased with is what happens when the classifier is wrong. Below 0.7 confidence, or on any error, or past a five-second timeout, the result is discarded and the full tool set goes through — exactly what the system did before the classifier existed. The optimisation is allowed to fail. When it fails it costs me money, and never costs the user an answer.

#### Two phases, and a 200-character note between them

The agent proper is split in two. The first phase only gathers: it calls tools until it has enough, then stops and emits a short note — capped at 200 characters, never shown to anyone — for the second phase, which writes the reply. The note carries edge cases only: *no transactions in this period*, *this tool failed, mention it gracefully*.

Separating retrieval from voice is worth doing on its own. The handoff is the part that saves money: the second phase inherits a summary and the tool results, not the first phase's entire reasoning transcript.

#### Spending tokens the way you spend money

**Identifiers get shortened.** Records are ULIDs, 26 characters each; a hundred of them is 2,600 characters the model must read and echo back to refer to one. Tool results carry the last five characters instead, extended to six only on a collision inside the same result set. It costs less, and full record identifiers never enter the prompt — the same instinct as the [anonymity design](/portfolio/kazz/), arriving here for a different reason.

**Arithmetic stays in Go.** Kazz lets your financial month start on the day you are paid rather than on the first. Instead of explaining that to a model, the server computes the boundaries and writes them into the prompt as literal dates. Models are unreliable at date maths, Go is not, and a wrong month boundary is a wrong answer that looks entirely plausible.

**The provider has a price ceiling.** Every request carries a maximum acceptable price per completion token and a minimum throughput, and routing picks a provider within both — cost control as configuration rather than as a decision I have to remember to make.

#### Whatever the model returns is untrusted input

The monthly review asks the model for the notable changes between two periods, and what comes back is checked before it is stored. Any category it names that is absent from that period's actual aggregates is dropped. The remainder is sorted by size of change and capped at five, in code, even though the prompt already asks for at most five — a rule that lives only in a prompt is a request, not a constraint.

Every dropped entry is logged as a hallucinated category, with its value. That is the part worth copying: the log line turns hallucination into something countable. You watch it move when a model version changes, and you find out from a graph rather than from a user who believed a number I made up.

#### The cleverest thing here became unnecessary

To compare this month against something, you have to choose the something. The first version chose with a heuristic: score every previous report against the current period, penalise anything running forwards in time, weigh the durations, take the best match. It works, and I was pleased with it.

The third version does not use it. The client already knows which period the user was looking at, so it sends both and the scoring pass is skipped. The old path still serves old reports, and I would build the heuristic again, because it was the right answer while the client could not tell me. It is a good reminder of how often an elegant inference stands in for a question nobody asked.

#### What the server keeps, and for how long

A chat session is created with an expiry stamped on it, and the server stops serving it after that; what survives is whatever the phone kept. The window is deliberately short. It is cheaper, and it puts a retention promise in a column rather than in my intentions.

Reviews are not generated inside the request. They go onto a queue, a worker does the work carrying the user's locale and currency, and a push notification arrives when it is done. Nobody waits on a spinner for a language model, and the load spreads out instead of landing all at once on the first of the month.

Quotas are refundable:

```go
type Limiter interface {
	AllowGenerateReport(ctx context.Context, claims mjwt.CustomClaim) (bool, int, error)
	RefundGenerateReport(ctx context.Context, userID string)
	ResetLimitGenerateReport(ctx context.Context, userID string) error
}
```

`Refund` exists because an allowance is a promise. If generation fails on my side, that attempt must not come out of what the user was given.

#### Why Go, and not Python

Because the AI layer is a small part of a financial application, and the financial application was always going to be Go.

Genkit covers the ground the Python ecosystem is assumed to own — tool definitions, structured output, streaming, multiple providers — and generics give typed structured output directly, so the classifier returns a struct rather than a map to be picked apart. OpenAI, OpenRouter and Genkit itself sit behind ports, which is what let the provider change underneath without the domain noticing.

The friction is real and ordinary. The router once began returning truncated JSON, because the reasoning model was spending its output budget on hidden chain-of-thought before finishing a two-field object; the fix was an explicit token ceiling, and finding it meant knowing that the compatibility layer maps that setting by JSON tag in snake case rather than through the framework's own camel-cased config. That is a normal afternoon in any language.

#### Tech stack
1. Golang with Genkit — agent, tools, structured output, streaming
2. OpenRouter and OpenAI behind one port, with a per-request price ceiling
3. A job queue and worker for report generation, delivered by push
4. OpenTelemetry traces and metrics through every service call
5. Prompts and reports localised per user, in the user's own currency

#### Where it led

The reports do not run in the request path, which is the same trade I made in [ITventory](/portfolio/inventaris/) in 2020 with a scheduled CCTV ping, and again in [Risa](/portfolio/risa-restfull/) in 2021 with a precomputed read model. Pay on a schedule so the read is free. It was a ping job then and it is a language model now, and the shape of the answer has not changed in five years.
