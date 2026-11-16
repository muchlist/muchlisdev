# Drafts

Not built by Hugo — this directory sits outside `content/`, so nothing here
is published to muchlis.dev.

## kazz-essay.md, kazz-ai-essay.md

The first pass at the Kazz articles, written as arguments rather than as
portfolio entries. They read as blog posts, which is what they should be:
candidates for blog.muchlis.dev rather than for the portfolio grid.

Kept because the reporting behind them is real — the Kazz AI piece is
grounded in the money-magnet source, and both carry corrections from the
author about the business model, the free tier, and how much of the AI
internals may be described. Anything reused from here must keep those
corrections intact:

- the free tier rations, it does not unlock everything; Pro lifts ceilings
- Kazz is profitable; it is not underwritten out of pocket
- AI internals stay blurred: no thresholds, stage names, or tool mechanics
- no claim about how chat expiry is enforced
- streamed chart generation is never described

The frontmatter still carries portfolio weights. Rewrite it before
publishing anywhere.

## Corrections made after these drafts were written

- Kazz is offline-first for transactions, wallets (pockets), and categories
  since the sync rollout (money-magnet PR #256, October 2026): changes queue
  on the phone, push when online, and pull deltas back; home is computed on
  the phone. The earlier `304`-on-home detail no longer applies to the
  current app. Kazz AI still needs a connection, and so do voice and receipt
  capture.
- Auto-capture from bank and e-wallet notifications is a headline feature
  and was missing entirely. Capture happens on the device from
  notifications already delivered, not through a bank connection; the
  drafts are only turned into transactions once the user accepts them.
- The AI chat belongs in the main article too, not only in the AI one.
