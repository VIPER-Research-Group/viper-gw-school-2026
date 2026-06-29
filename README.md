# VIPER 2026 Summer School on PTA GW Astrophysics

Website for the 2026 VIPER Summer School on Pulsar Timing Array gravitational-wave
astrophysics — **July 20–31, 2026**, Vanderbilt University, Nashville, TN.

**Live site:** https://viper-research-group.github.io/viper-gw-school-2026/

This is a complete redesign of the 2024 site
([`viper-gw-school-2024`](https://github.com/VIPER-Research-Group/viper-gw-school-2024)):
a self-contained dark "cosmic glass" static site with no framework, no jQuery, and no
icon fonts (icons are inline SVG). It is consistent in style with the
[2026 interactive demos](https://stevertaylor.github.io/viper-2026-summer-school-demos/).

## Structure

```
build.py                 ← generator: one HTML shell + per-page content + schedule data
assets/css/site.css      ← the whole design system
assets/js/site.js        ← nav toggle + tab switchers (vanilla JS)
images/                  ← hero + Nashville photos
*.html                   ← generated — do not hand-edit; edit build.py and regenerate
```

Pages: Home, Schedule (interactive Week 1 / Week 2 tabs), Syllabus, Speakers, Participants,
Travel, Installation, Tutorials & demos, Key papers, Useful links.

## Editing

All `*.html` files are generated. **Edit `build.py`**, then regenerate:

```bash
python3 build.py
```

The schedule is data near the top of `build.py` (the `WEEK1` / `WEEK2` lists) — change a
title, speaker, or session type there and rebuild. The shared nav/footer live in `build.py`
too, so they never drift between pages.

## Deploying

Served via GitHub Pages from `main` at the repository root. Push to `main` and the live
site updates in ~30 s.

## Credits

Course materials (slides + tutorial notebooks):
https://github.com/stevertaylor/gw-school-2026-materials
