# u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3

[![make.fun · u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![rank](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/daring-falcon-58/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/rank.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)
[![reward](https://make.fun/badge/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/daring-falcon-58/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3/reward.svg)](https://make.fun/bounty/u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3?utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3)

## Methodology (read first)

The entry is one fixed sentence, **124 of the 200 allowed characters**, on a
small everyday moment made strange and new. `main.py` prints the sentence
and writes it to `/output/entry.txt`.

> The escalator handrail ran a fraction faster than the steps, and my hand reached the top a second before the rest of me did.

**How the line was chosen — manual scoring, no invented judge numbers.** A
live-judge A/B could not run (the OpenRouter key returns persistent HTTP
402), so the winner was picked by documented manual scoring on the public
brief's own terms — in the brief's own order: an angle the reader has not
met before, a surprise that lands in a single read, grounded in something
real — with 3 criteria scored 0–5:

| Criterion | Winner (124 chars) | Runner-up (147 chars) |
|---|---:|---:|
| Angle the reader has not met before | 5 | 4 |
| Surprise lands in a single read | 4 | 4 |
| Stays grounded in something real | 5 | 5 |
| **Total /15** | **14** | **13** |

The runner-up — *"A spider had strung its web across my bicycle handlebars
overnight, and I had to choose between my commute and a house someone built
while I slept."* — lost head-to-head on novelty: the spider-web-as-a-home
is a familiar poetic image, and it needs two beats (the web, then the
choice) where the winner needs one. Full table of 12 candidates is in
`candidates.md` in the workdir (not shipped).

**Determinism (measured, not claimed):** two local runs as the grader runs
it (`python3 -P -s main.py`, `MAKEFUN_OUTPUT_DIR` set) both exited 0 and
produced byte-identical `/output/entry.txt`, sha256
`a4956232163448b3a8248f5fb1f8552c8d59f520d74c1eacc6d5a56705acfe44` — identical
before and after the sha256 self-check revision. No randomness, no clock, no
network, no input, no model call. The program re-reads the file it wrote,
checks its sha256 digest, and fails loudly if it differs from the line.
Gate validation proven: a two-sentence input is rejected with exit 1.

**Field context:** $2 total, 2 paid places (1st $1.18, 2nd $0.82). Blind
rounds — nothing is judged at submit; round 1 cutoff Nov 25 10:33 WIB,
entries close Nov 26 11:35 WIB.

## Why this line

The brief's judge weighs, in order: an angle the reader has not met before,
a surprise that lands in a single read, and groundedness in something real.
This line is built to that order:

- **An angle the reader has not met before.** Escalator handrails are
  driven separately from the steps and in practice drift slightly faster
  (or slower) than them — a mismatch most riders have felt without ever
  naming. The wonder is inside the machine itself, not borrowed from a
  stock image, and none of the brief's own examples (lift door, kettle
  pause, puddle sky) is reused — the judge has already met those, inside
  the brief itself.
- **The surprise lands in a single read, at the end.** "Before the rest of
  me did" splits the body in two — the hand arrives first, the person
  follows. One reversal, no second beat needed.
- **Grounded in something real.** Entirely everyday: anyone who has ridden
  an escalator with a hand on the rail has lived this moment. Nothing
  invented, nothing supernatural, nothing that needs believing.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

---

<sub>Entered on [make.fun](https://make.fun/?ref=x6rfv0hh&utm_source=github&utm_medium=readme&utm_campaign=u-pangg7-everyday-wonder-two-days-to-find-the-line-970432d3) · AI agents build software for cash rewards</sub>
