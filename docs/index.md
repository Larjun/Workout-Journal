# Workout Journal

My running and cycling journal: each session's numbers, what went wrong, and what to fix next. Strava and Runna are encouraging; this journal is meant to be honest.

Sessions are analysed with Claude (using my Strava data) and written up here as short entries. The focus files are living documents that change as I improve.

## Current focus

### Running: Runna "New To Running" plan, week 7 of 8
1. **Cadence:** hold 148 spm for the whole run (stuck at ~146 on 11-17 and 11-18). Set the metronome to 152 to land at 148–150.
2. **Effort cap:** keep easy-run HR under 160, and under 165 late in the run. Walk 20–30 s if over 165.
3. **Pacing:** never start faster than I finish. My default "own pace" is still too hard.

### Cycling: Zone 2 base on a restored 26" MTB
1. **Weekly long ride:** ~76 min in Zone 2 (125–154 bpm) and growing ~10 min/week, toward 90–120 min. Eat at 45–60 min on rides over ~75 min.
2. **Climb control:** keep flyover and bridge peaks under ~155 by shifting down early and spinning.
3. **Keep hard rides rare:** events are fine; don't let event effort (HR ~160+) become normal riding.

Details: [Running focus](focus/running.md) · [Cycling focus](focus/cycling.md) · [Browse by tag](tags.md)

## Session index

| Date | Type | Session | Verdict |
|---|---|---|---|
| 2026-11-28 | Run | [Continuous 4.25 km](sessions/2026/2026-11-28-run.md) | Longest continuous run: faster and lower HR than 3.75 km on 11-18; feet were the limiter |
| 2026-11-26 | Run | [2 × 2.5 km](sessions/2026/2026-11-26-run.md) | Longest session yet (5 km running); HR flat, legs faded in rep 2 |
| 2026-11-24 | Run | [Continuous 3.25 km (rain)](sessions/2026/2026-11-24-run.md) | Zone 2 held for ~2.3 km, then Zone 3 and a sprint home to 206 bpm |
| 2026-11-20 | Swim | [First swim test (pool)](sessions/2026/2026-11-20-swim.md) | Stroke fine; mostly single lengths with 1–3 min rests |
| 2026-11-19 | Ride | [25 km Zone 2](sessions/2026/2026-11-19-ride.md) | Event speed at HR 137, 98% Zone 2; but it was a rest day |
| 2026-11-18 | Run | [Continuous 3.75 km](sessions/2026/2026-11-18-run.md) | HR cap held (92% under 160, peak 166); cadence stuck at ~146 |
| 2026-11-17 | Run | [Continuous 3 km](sessions/2026/2026-11-17-run.md) | First continuous 3 km; HR drifted to 170, extra hard 640 m home |
| 2026-11-15 | Ride | [Race against Diabetes – Thooral 25](sessions/2026/2026-11-15-ride.md) | Event: 27 km hard (HR 162), very even pacing |
| 2026-11-14 | Ride | [First medium-distance ride in Chennai](sessions/2026/2026-11-14-ride.md) | 20 km in Zone 2, no fade. Best base ride yet |
| 2026-11-13 | Run | [2 × 2 km](sessions/2026/2026-11-13-run.md) | Faster at same/lower HR; cadence unchanged |
| 2026-11-12 | Ride | [First ride on Indian roads](sessions/2026/2026-11-12-ride.md) | 10.5 km, entirely Zone 2. Lost the bottle cage |
| 2026-11-11 | Run | [2 × 2 km](sessions/2026/2026-11-11-run.md) | Pacing fixed: HR 164 → 145. Rep 2 still drifted |
| 2026-11-07 | Ride | [Morning ride](sessions/2026/2026-11-07-ride.md) | First truly easy ride in my history |
| 2026-11-06 | Run | [2 × 1.75 km](sessions/2026/2026-11-06-run.md) | Easy run done hard: 21 min in Z4–5, faded badly |
| 2026-11-04 | Run | [2 × 1.5 km](sessions/2026/2026-11-04-run.md) | Rep 1 too fast, rep 2 at HR 176 |
| 2026-11-03 | Run | [Continuous 2 km](sessions/2026/2026-11-03-run.md) | 9:03/km at HR 162, too fast for conversational |

Weekly reviews: [2026-W46](weekly/2026-W46.md) · [2026-W45](weekly/2026-W45.md)

## Session entry template

```markdown
---
date: YYYY-MM-DD
type: run | ride
tags: [run, runna]
distance_km: 0.0
avg_hr: 0
max_hr: 0
---

# YYYY-MM-DD · Run/Ride · Session name

**Plan:** what the session was supposed to be

**Conditions:** temp, humidity, route/context tags

## Numbers
| Metric | Value |
|---|---|

## Verdict
One or two lines. Honest.

## What went wrong
- ...

## Fix for next time
- One main fix (plus at most two secondary)
```

## Rules of thumb

- Running calories ≈ 1 kcal per kg per km; walking ≈ half that. For rides, kJ of work ≈ kcal.
- Apple Watch/Strava running cadence can be per leg; steps per minute = value × 2.
- Ignore GPS max-pace spikes.
- Calorie estimates from Strava undercount on the MTB.

*Not medical advice.*
