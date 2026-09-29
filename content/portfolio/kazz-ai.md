---
title: "Kazz AI — an agent that has to pay for itself (2025 - Present)"
date: 2025-09-01T09:00:00+08:00
draft: false
image: "/img/portfolio/kazz-ai-front.webp"
showonlyimage: false
weight: 8
tags: ["golang", "genkit", "ai", "llm", "openrouter"]
categories: ["backend", "ai"]
---

The assistant inside [Kazz](/portfolio/kazz/): chat, receipt scanning, voice entry, and written monthly reviews, for 18,000 users — at a unit cost low enough that giving most of it away still works. [Golang, Genkit].
<!--more-->

> An agent's cost is decided long before the model is chosen. It is decided by how much you hand it.

#### The number this is all aimed at

Kazz rations its free tier rather than locking it: real limits, none of them permanent, all of them resetting. [The main article](/portfolio/kazz/) explains why.

That decision lands here as a single requirement. Most users are free users and always will be, so serving one has to be cheap enough that they are worth keeping. Not cheap as an ideal — cheap as a number, because the difference between a product that funds its own servers and one that quietly bleeds is decided by it.

Which puts the agent under two demands that pull against each other. The obvious way to make an agent better is to give it more: more tools, more history, more context, a stronger model. All of that is billed per token. So most of the work is giving it less without the user noticing.

#### The expensive part should not see everything

The naive shape of an agent is one model, every tool, the whole history, every turn. It works, and it is the most expensive thing you can build, because everything handed to a model is paid for whether it gets used or not. Tool definitions are the clearest case: they are prompt text, they are resent on every turn, and most of them have nothing to do with the question in front of you.

So something cheaper runs first and decides how much of the system the expensive part actually needs to see. Gathering the facts and writing the answer are separate jobs too, and the one that writes does not inherit the other's working out.

The property I care about most is what that cheap layer does when it is unsure. It gets out of the way, and the request proceeds exactly as it would have if the layer had never been built. That is the rule worth taking from this: an optimisation standing in front of a correctness-critical path needs a failure mode that costs money rather than accuracy. Mine can be wrong, time out, or fall over entirely, and the worst outcome is a more expensive answer — never a worse one.

#### Spending tokens the way you spend money

**Identifiers get shortened.** Records are ULIDs, 26 characters each; a result set of a hundred is 2,600 characters the model has to read and then quote back in order to refer to one of them. They are cut down before they ever reach the prompt. It costs less, and full record identifiers never enter the prompt at all — the same instinct as the [anonymity design](/portfolio/kazz/), arriving here for a different reason.

**Arithmetic stays in Go.** Kazz lets your financial month start on the day you are paid rather than on the first. Instead of explaining that to a model, the server works out the boundaries and writes them in as literal dates. Models are unreliable at date maths, Go is not, and a wrong month boundary produces a wrong answer that looks entirely plausible.

**The provider has a price ceiling.** Every request carries a maximum acceptable price per completion token and a minimum acceptable throughput, and routing picks a provider inside both — cost control as configuration rather than as a decision I have to remember to make.

#### Whatever the model returns is untrusted input

The monthly review asks the model for the notable changes between two periods, and what comes back is checked before any of it is stored. Any category it names that is absent from that period's real aggregates is dropped. What survives is sorted by size of change and capped in code, even though the prompt already asks for the same cap — a rule that lives only in a prompt is a request, not a constraint.

Every dropped entry is logged as a hallucinated category, with its value. That is the part worth copying. The log line turns hallucination into something countable: you can watch it move when a model version changes underneath you, and you find out from a graph rather than from a user who believed a number I made up.

#### The cleverest thing here became unnecessary

To compare this month against something, you have to choose the something. The first version chose with a heuristic — score the user's previous reports against the current period, rule out anything running forwards in time, weigh the durations, take the best match. It works, and I was pleased with it.

The third version does not use it. The client already knows which period the user was looking at, so it sends both, and the whole scoring pass is skipped. The old path still serves old reports, and I would build the heuristic again, because it was the right answer for as long as the client could not tell me. It is a good reminder of how often an elegant inference is standing in for a question nobody asked.

#### The user decides how long a conversation lives

A chat session carries an expiry, and the length is chosen in the app rather than by me — three hours unless you change it.

Putting that dial in the user's hands is the whole point. A conversation about your own money is not something anyone should have to extend good faith about, and a setting you can see is worth more than a paragraph in a privacy policy you cannot check.

Reviews are not generated inside the request either. They go onto a queue, a worker does the work carrying the user's locale and currency, and a push notification arrives when it is ready. Nobody waits on a spinner for a language model, and the load spreads out instead of landing all at once on the first of the month.

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

Genkit covers the ground the Python ecosystem is assumed to own — tool definitions, structured output, streaming, multiple providers — and generics give typed structured output directly, so a structured response arrives as a Go struct rather than a map to be picked apart. OpenAI, OpenRouter and Genkit itself sit behind ports, which is what let the provider change underneath without the domain noticing.

The friction is real and it is ordinary friction. One model started returning truncated JSON, because it was spending its output budget on hidden reasoning before finishing a two-field object; the fix was an explicit token ceiling, and finding it meant knowing that the compatibility layer maps that setting by JSON tag in snake case rather than through the framework's own camel-cased config. That is a normal afternoon in any language.

#### Tech stack
1. Golang with Genkit — agent, tools, structured output, streaming
2. OpenRouter and OpenAI behind one port, with a per-request price ceiling
3. PostgreSQL, with a job queue and worker for report generation, delivered by push
4. OpenTelemetry traces and metrics through every service call
5. Prompts and reports localised per user, in the user's own currency

#### Where it led

The reviews do not run in the request path, which is the same trade I made in [ITventory](/portfolio/inventaris/) in 2020 with a scheduled CCTV ping, and again in [Risa](/portfolio/risa-restfull/) in 2021 with a precomputed read model. Pay on a schedule so the read is free. It was a ping job then and it is a language model now, and the shape of the answer has not changed in five years.
