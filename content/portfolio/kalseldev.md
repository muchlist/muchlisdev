---
title: "KalselDev — a free API for learning JWT (2021)"
date: 2021-01-21T21:38:25+08:00
draft: false
image: "/img/portfolio/kalseldev-front.webp"
showonlyimage: false
weight: 16
tags: ["golang", "mongodb", "jwt", "oauth2"]
categories: ["backend"]
---

A free REST API the Kalimantan programmer community could practice JWT against — a real server instead of a mock. Retired; kept here for what it taught. [Golang, MongoDB].
<!--more-->

KalselDev was a free REST API I ran so that beginner programmers could build against real server responses instead of fake ones. The service is retired and the domain now serves something else, so there is nothing left to sign up for. What is worth keeping is the thing it existed to teach.

#### Why it existed
- Built and self-hosted a free REST API with real login and JWT authorization, so that a practice app could exercise the whole authentication cycle rather than a mocked slice of it.

The free practice APIs available at the time mostly accepted `GET` and nothing else. That is enough to render a list and not enough to learn anything about authentication. Without `POST`, `PUT`, and `DELETE` sitting behind a real authorization check, a beginner's portfolio app stops exactly where the interesting questions start: where does the token come from, what happens when it expires, and what is the client supposed to do about it. It was also the first thing I built for other programmers rather than for an employer — the same conviction I had arrived at two years earlier building [Kamus IT](/portfolio/kamus-it/) against a server of my own instead of a tutorial's mock, only pointed outward this time.

#### The part most people still miss

![Fresh and non-fresh access tokens][fresh]

> **Fun fact:** in the flow most tutorials teach, you log in, receive an access token and a refresh token, and trade the refresh token for a new access token whenever the old one expires. What almost nobody is taught is that those two access tokens are not equivalent. The one from login was minted while the user was proving they knew the password. The one from refresh was minted from a credential sitting in device storage. The first is *fresh*; the second is not.

The distinction only matters for the handful of operations where you want the human actually present — changing a password, changing an email, deleting the account, moving money. A non-fresh token proves that this session was authenticated at *some* point in the past. A fresh token proves that someone knew the password a moment ago. Treat the two as interchangeable and a stolen refresh token carries exactly as much authority as the password itself.

Carrying it costs almost nothing: one claim in the token payload, and one check on the routes that deserve it. The naming comes from libraries like Flask-JWT-Extended, but the idea is not theirs — OpenID Connect records the same fact as the `auth_time` claim, and a relying party that needs recent proof sends `max_age` and forces re-authentication when too much time has passed since.

#### What I would build differently now

KalselDev minted its own tokens from its own login endpoint. For a first-party practice API that is still the right shape. What I did not understand in 2021 is what changes once the client is **public** — a mobile app or a single-page app that cannot keep a secret. Anything compiled into an app binary can be pulled back out of it.

OAuth2's authorization code flow was designed around confidential clients that could prove themselves with a client secret. **PKCE** (RFC 7636) closes the gap for everyone else: the client generates a random `code_verifier`, sends only its SHA-256 hash as the `code_challenge` when it starts the flow, and presents the original verifier when it redeems the authorization code. An attacker who intercepts the code — by registering the same custom URL scheme as the real app, for instance — cannot redeem it without the verifier, and the verifier never left the device.

That is no longer treated as a special case for public clients. The implicit flow is deprecated, and OAuth 2.1 folds PKCE into the authorization code flow for every client, confidential ones included.

#### Tech stack
1. Golang
2. MongoDB
3. A self-managed Linux server

#### Source code
- [KalselDevApi](https://github.com/muchlist/KalselDevApi) — the REST API
- [KalselDevDoc](https://github.com/muchlist/KalselDevDoc) — the documentation site

[fresh]: /img/portfolio/kalseldev-token-freshness.svg
