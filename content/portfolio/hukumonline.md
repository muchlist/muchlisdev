---
title: "Senior Backend & AI Engineer at Hukumonline (2025 - Present)"
date: 2026-09-29T09:00:00+08:00
draft: false
image: "/img/portfolio/hukumonline.webp"
showonlyimage: false
weight: 10
tags: ["golang", "aws", "lambda", "dynamodb", "rag", "langchain", "opentelemetry"]
categories: ["backend", "ai"]
---

Senior Backend Engineer and Senior AI Engineer at Indonesia's legal information platform, working on a serverless MVP, retrieval over case law, critical fixes, and observability. [Golang, Python, AWS].
<!--more-->

Hukumonline is Indonesia's legal information platform, publishing regulations, court decisions, and legal analysis, alongside services for legal professionals and businesses.

The work splits across both roles: a greenfield service on a serverless stack, retrieval over a corpus of court decisions, two critical bugs found early on, and the observability groundwork that makes all of it debuggable.

#### Serverless MVP for international expansion
- Built a new service — an international edition of the platform — on **AWS Lambda** and **DynamoDB**, written in **Golang** rather than a runtime with first-class Lambda support, by wrapping an ordinary Golang router so it could run as a Lambda handler.

![Golang router running on Lambda][lambda]

An adapter translates the API Gateway event into a standard `http.Request` and hands it to the router, which means the handlers are written exactly as they would be for any HTTP service. The same binary runs locally as a plain server, so the serverless deployment target never leaked into the application code — which is what let the MVP ship on a short timeline.

> **Fun fact:** cost was part of the brief — the MVP was meant to run at as close to zero infrastructure cost as possible, and on this stack that is more achievable than it sounds. Lambda's free allowance is 1 million requests and 400,000 GB-seconds of compute per month, and DynamoDB's is 25 GB of storage with 25 read and 25 write capacity units in provisioned mode — roughly 200 million requests a month, depending on item size. Neither allowance expires: these are the *always free* tiers, not the 12-month trial. The front door is the part that does run out, since API Gateway's free tier lasts only 12 months — which is what makes a Lambda Function URL the genuinely free entry point.

#### Retrieval over case law
- Built a **RAG chat** over the court decision corpus, answering legal questions from retrieved source documents rather than from model memory alone.

![Simplified retrieval flow over court decisions][rag]

The diagram above is a deliberate simplification — it shows the spine of the pipeline, not the system. The production version carries considerably more than a single retrieve-then-answer pass.

- Optimized retrieval queries and tuned the **HNSW** vector index, which is the step that decides whether retrieval is fast enough to sit inside a chat response.
- Authored a proposal for an **agent and tool** architecture, extending the system beyond single-shot retrieval.

Grounding matters more than usual in this domain: a legal answer that cannot be traced back to a specific decision is not useful, so the retrieved passages are the answer's evidence, not just its prompt.

#### Critical fixes
- Traced roughly **$1,000/month** of avoidable cloud spend to JWT verification keys being fetched from the managed AWS secret store on **every** request, and removed it by loading the keys once at startup and reusing them for the process lifetime.

The keys are an asymmetric pair, and the public half changes rarely — so paying a per-request API call to re-read something that had not changed made the bill scale with traffic rather than with need. The fix was less about caching than about moving the read to the place it belonged: process startup.

- Found and fixed a **memory leak** caused by module-level global state in a Python service retaining objects across requests instead of releasing them.

#### Observability
- Drove the initial effort to complete observability coverage with **OpenTelemetry** logging into **Loki**, custom metrics, and **RED metrics** (rate, errors, duration) for service-level visibility.
- Attached **trace IDs** to log lines so a single request can be stitched back together across services during debugging.

This is the same groundwork I introduced at [eFishery](/portfolio/efishery/) — it has turned out to be the highest-leverage thing to bring into a team that does not have it yet, because it changes debugging from reading separate logs and guessing into reading one trace.

#### Engineering standards
- Established a **golden path** Golang repository as a reference implementation for new services, applying **hexagonal architecture**, **interface segregation**, and a proper **unit of work** for transactions.

The transaction handling follows the approach I wrote up earlier: [Teknik Implementasi Database Transaction pada Logic Layer di Backend Golang](https://blog.muchlis.dev/post/db-transaction/) — keeping transaction control in the service layer so the business logic stays independent of the database driver.

#### Tech stack
1. Golang, Python
2. AWS Lambda, API Gateway, DynamoDB
3. LangChain, vector search (HNSW), RAG
4. OpenTelemetry, Loki, Prometheus-style RED metrics

[lambda]: /img/portfolio/hukumonline-lambda.svg
[rag]: /img/portfolio/hukumonline-rag.svg
