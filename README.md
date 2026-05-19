# 🎮 Cloud Reaction Game

[![Build](https://github.com/jpanderson91/reaction-game/actions/workflows/build.yml/badge.svg?branch=main)](https://github.com/jpanderson91/reaction-game/actions/workflows/build.yml)
[![Tests](https://github.com/jpanderson91/reaction-game/actions/workflows/tests.yml/badge.svg?branch=main)](https://github.com/jpanderson91/reaction-game/actions/workflows/tests.yml)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![Mode](https://img.shields.io/badge/mode-Terminal-black)
![Focus](https://img.shields.io/badge/focus-Learning%20by%20building-green)

> A terminal-based reaction-time game that simulates real-world cloud incidents (CPU spikes, PROD down, latency alerts) with console art and text effects.

---

## ✨ Demo

> **Add a short GIF once you have a playable loop.**

![Demo GIF](docs/images/demo.gif)

---

## 🖼️ Screenshots

> Drop screenshots into `docs/images/` and update the filenames below.

| Incident Alert | Results / Scoreboard |
|---|---|
| ![Alert Screen](docs/images/screen-alert.png) | ![Results Screen](docs/images/screen-results.png) |

---

## 🚀 Why this project exists

This is a *portfolio-quality* learning project that demonstrates:

- **Core Python fundamentals** (loops, conditionals, functions, timing, randomness)
- **Terminal UI polish** (ASCII art, colors, screen-clears/animations)
- **Game loop design** (rounds, streaks, difficulty scaling, fake-outs)
- **Professional hygiene** (tests + GitHub Actions CI with status badges)

---

## 🎯 Gameplay (concept)

1. The game arms itself: `WAIT…`
2. After a random delay, an incident fires: `🚨 PROD DOWN` / `🔥 CPU SPIKE` / `⏱️ LATENCY`
3. You respond as fast as possible.
4. Your reaction time, streak, and score are shown.

---

## ✅ Features (planned + in progress)

- [ ] One-round reaction timer (MVP)
- [ ] Multiple incidents + randomized prompts
- [ ] ANSI colors + ASCII banners
- [ ] Multi-round sessions, streaks, best times
- [ ] Fake-outs (penalize early reactions)
- [ ] Difficulty scaling
- [ ] Persist high scores (optional)

---

## 🧱 Roadmap (phased rubric)

### Phase 0 — Setup
- [ ] Create project & run `python main.py`
- [ ] Add dependencies (optional)

### Phase 1 — MVP (vertical slice)
- [ ] WAIT → random delay → GO → measure reaction time

### Phase 2 — Cloud theme
- [ ] Alerts: CPU spike / PROD down / latency

### Phase 3 — Visual polish
- [ ] Colors + ASCII art + screen clearing

### Phase 4 — Game loop
- [ ] Multi-round session + score tracking

### Phase 5 — Mechanics
- [ ] Fake-outs + penalties + streak system

### Phase 6 — Polish
- [ ] Log-style output, better UX pacing

### Phase 7 — Persistence (optional)
- [ ] Save/load highscores

---

## 🧩 Tech stack

- **Python 3.x**
- Optional terminal helpers:
  - `colorama` (cross-platform colors)
  - `pyfiglet` (ASCII banners)
- Testing:
  - `pytest`
- CI:
  - GitHub Actions workflows in `.github/workflows/`

---

## 📂 Project structure

```
cloud-reaction-game/
│
├── main.py
├── game/
│   ├── loop.py
│   ├── reaction.py
│   └── scoring.py
├── ui/
│   ├── display.py
│   ├── colors.py
│   └── ascii_art.py
├── events/
│   └── alerts.py
├── utils/
│   ├── timer.py
│   └── randomizer.py
├── tests/
│   └── test_smoke.py
├── docs/
│   └── images/
│       ├── demo.gif
│       ├── screen-alert.png
│       └── screen-results.png
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

---

## 🏁 Getting started

### Run locally

```bash
python main.py
```

### Install optional dependencies

```bash
pip install -r requirements.txt
```

### Install dev dependencies (tests)

```bash
pip install -r requirements-dev.txt
```

### Run tests

```bash
pytest -q
```

---

## 🤖 AI mentor workflow (recommended)

If you're using an AI agent, keep it in *mentor mode*:
- Ask questions first
- Share small hints
- Avoid big code dumps

(You can keep your Socratic system prompt in `docs/ai-system-prompt.md` if you want it versioned.)

---

## 🧷 CI badges (make them live)

These badges auto-update when the workflows run:

- `build.yml` → build/sanity checks
- `tests.yml` → unit tests

**Important:** Replace `jpanderson91` and `reaction-game` at the top of this README with your GitHub username/org and repository name.

---

## 📜 License

MIT (or choose your preferred license).
