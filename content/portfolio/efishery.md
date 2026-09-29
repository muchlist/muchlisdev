---
title: "Backend Engineer at eFishery (2022 - 2025)"
date: 2025-02-28T09:00:00+08:00
draft: false
image: "/img/portfolio/efishery.webp"
showonlyimage: false
weight: 11
tags: ["golang", "postgresql", "kafka", "opentelemetry", "redis"]
categories: ["backend"]
---

Mid-level Backend Engineer at an aquaculture technology company, focused on performance optimization, service architecture, and observability. [Golang, PostgreSQL, Kafka].
<!--more-->

eFishery is an aquaculture technology company in Indonesia providing smart feeding systems, financing solutions, and market access for fish and shrimp farmers.

For almost three years I worked on internal services used across teams: customer, support, auth, and master data. Most of the work came down to three things — making slow things fast, making fragile things maintainable, and making problems visible before they turned into incidents.

#### Performance and reliability
- Optimized PostgreSQL queries, business logic, and the cache mechanism in the customer-service system, improving response times by **60%** while eliminating OOM issues.
- Reduced system bugs and improved service reliability by proactively addressing performance bottlenecks in Internal Core Services.

#### Architecture and code quality
- Refactored and modernized the Customer, Support, and Auth services to **Golang Hexagonal Architecture**, enabling **80%+** unit test coverage and making the codebase considerably easier to maintain.

Coverage that high is only reachable once the business logic stops depending on the database driver and the HTTP layer. Two decisions did most of the work — keeping transaction control in the service layer instead of the repository, and refusing to let one struct travel across every layer. I wrote both up in detail:

- [Teknik Implementasi Database Transaction pada Logic Layer di Backend Golang](https://blog.muchlis.dev/post/db-transaction/) — a `DBTX` abstraction and a `WithAtomic` wrapper that keep transactions atomic without coupling the service layer to pgx or GORM.
- [Memahami Pentingnya Memisahkan DTO, Entity dan Model](https://blog.muchlis.dev/post/struct-separation/) — why sharing one struct between database, domain, and API turns an external schema change into a codebase-wide edit.

#### Internal tooling and libraries
- Built **Flag Manager**, a feature flag caching library that cut network calls for flag retrieval by **90%**.

![Flag Manager caching flow][flag]

A feature flag gets read on the hot path, often several times in a single request. Fetching it remotely each time makes flag lookups scale with traffic. Flag Manager holds the flags in process memory and refreshes them on its own schedule, so a check costs a map lookup instead of a round trip.

- Built a **Context-Integrated Logging** system for Golang, carrying request context through the entire log trail.
- Built **Master-Validator**, a validation library for phone numbers, KTP, KK, and location data, eliminating **100%** of validation latency over the network.

#### Data and integration
- Developed a risk identification system to flag suspicious farmers using **Kafka Consumer**, **KSQLDB**, and AI models from the Data Engineering team.
- Implemented *fuzzy matching* for customer name and location similarity detection using **PostgreSQL trigrams (pg_trgm)** and **Levenshtein distance**, preventing **30%** of duplicate customer registrations.
- Led the data aggregation process for CRM using **Apache Airflow** and **Jenkins**, enabling near real-time insights and improving customer segmentation accuracy by **45%**.
- Enhanced the Master Data Service to enforce an approval process before any data modification, integrated with a Slack bot.

#### Security
- Strengthened OAuth2 by implementing **PKCE** and **revocable tokens**.

#### Observability
- Initiated the adoption of **OpenTelemetry** and custom metrics at eFishery, significantly reducing debugging time.

![OpenTelemetry tracing][otel]

Before tracing, locating a slow request meant guessing which service to suspect and then reading each one's logs separately. With every service emitting through one OpenTelemetry pipeline, a request carries a single trace across all of them — so the slow span is read off a waterfall rather than inferred.

#### Team contributions
- Authored technical handbooks on OpenTelemetry, Golang profiling, JWT claim standardization, *database transaction gameplay*, and project structure best practices.
- Conducted technical interviews, assessing candidates' technical knowledge.

#### Tech stack
1. Golang
2. PostgreSQL, Redis
3. Kafka, KSQLDB
4. OpenTelemetry, Prometheus
5. Apache Airflow, Jenkins
6. Docker

[flag]: /img/portfolio/efishery-flag-manager.svg
[otel]: /img/portfolio/efishery-otel.svg
