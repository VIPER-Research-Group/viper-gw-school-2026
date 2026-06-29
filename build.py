#!/usr/bin/env python3
"""
Static-site generator for the VIPER 2026 Summer School on PTA GW Astrophysics.

All pages share one HTML shell (nav + footer) defined here, so the site stays
consistent and is trivial to update. Run `python3 build.py` to regenerate every
*.html file in this directory. No third-party dependencies.
"""

import html

SITE = "VIPER 2026 Summer School"
EMAIL = "stephen.r.taylor@vanderbilt.edu"
DEMOS = "https://stevertaylor.github.io/viper-2026-summer-school-demos/"
MATERIALS = "https://github.com/stevertaylor/gw-school-2026-materials"
VIPER_URL = "https://as.vanderbilt.edu/viper/"
DATES = "July 20 – 31, 2026"

# --------------------------------------------------------------------------- #
# Inline SVG icons (stroke, currentColor). Keeps the site free of icon fonts.  #
# --------------------------------------------------------------------------- #
def svg(body, size=20):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" '
            f'stroke="currentColor" stroke-width="1.7" stroke-linecap="round" '
            f'stroke-linejoin="round">{body}</svg>')

I = {
    "calendar": svg('<rect x="3" y="4.5" width="18" height="16" rx="2"/><path d="M3 9h18M8 2.5v4M16 2.5v4"/>'),
    "pin":      svg('<path d="M12 21s7-5.6 7-11a7 7 0 1 0-14 0c0 5.4 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>'),
    "clock":    svg('<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>'),
    "users":    svg('<path d="M16 19v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="3.2"/><path d="M22 19v-2a4 4 0 0 0-3-3.8M16 3.3A4 4 0 0 1 16 11"/>'),
    "book":     svg('<path d="M4 4.5A2.5 2.5 0 0 1 6.5 2H20v16H6.5A2.5 2.5 0 0 0 4 20.5z"/><path d="M4 16.5A2.5 2.5 0 0 1 6.5 14H20"/>'),
    "code":     svg('<path d="M16 18l5-6-5-6M8 6l-5 6 5 6"/>'),
    "rocket":   svg('<path d="M5 13c-2 1-3 5-3 5s4-1 5-3M12 3c3.5 1.5 6 4 7.5 7.5L14 16l-5-5z"/><circle cx="14.5" cy="8.5" r="1.6"/>'),
    "gem":      svg('<path d="M6 3h12l3 6-9 12L3 9z"/><path d="M3 9h18M9 3 7 9l5 12 5-12-2-6"/>'),
    "signal":   svg('<path d="M4 20v-5M9 20v-9M14 20v-13M19 20V5"/>'),
    "mail":     svg('<rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3.5 6.5 12 13l8.5-6.5"/>'),
    "home":     svg('<path d="M4 11.5 12 4l8 7.5"/><path d="M6 10v10h12V10"/>'),
    "arrow":    svg('<path d="M5 12h14M13 6l6 6-6 6"/>'),
    "ext":      svg('<path d="M14 4h6v6M20 4l-9 9M18 14v5a1 1 0 0 1-1 1H5a1 1 0 0 1-1-1V7a1 1 0 0 1 1-1h5"/>', 16),
    "menu":     svg('<path d="M4 7h16M4 12h16M4 17h16"/>', 22),
    "wave":     svg('<path d="M2 12c2 0 2-6 4-6s2 12 4 12 2-12 4-12 2 6 4 6"/>'),
    "star":     svg('<path d="M12 3l2.6 5.6 6 .7-4.4 4 1.2 6-5.4-3-5.4 3 1.2-6-4.4-4 6-.7z"/>'),
    "link":     svg('<path d="M9 15l6-6M10 6l1-1a4 4 0 0 1 6 6l-1 1M14 18l-1 1a4 4 0 0 1-6-6l1-1"/>', 18),
    "download": svg('<path d="M12 3v12M7 11l5 5 5-5M5 21h14"/>'),
    "spark":    svg('<path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M18 6l-2.5 2.5M8.5 15.5 6 18"/>'),
    "globe":    svg('<circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 2.5 15.4 0 18M12 3c-2.5 2.6-2.5 15.4 0 18"/>'),
    "chat":     svg('<path d="M21 12a8 8 0 0 1-11.5 7.2L3 21l1.8-6.5A8 8 0 1 1 21 12z"/>'),
}

# --------------------------------------------------------------------------- #
# Navigation                                                                   #
# --------------------------------------------------------------------------- #
NAV_ITEMS = [
    ("index.html", "Home", "home"),
    ("schedule.html", "Schedule", "schedule"),
    ("syllabus.html", "Syllabus", "syllabus"),
    ("speakers.html", "Speakers", "speakers"),
    ("participants.html", "Participants", "participants"),
    ("travel.html", "Travel", "travel"),
]
SOFTWARE = [("installation.html", "Installation", "installation"),
            ("tutorials.html", "Tutorials &amp; demos", "tutorials")]
RESOURCES = [("imp_papers.html", "Key papers", "imp_papers"),
             ("useful_links.html", "Useful links", "useful_links")]


def nav(active):
    soft_active = active in [k for _, _, k in SOFTWARE]
    res_active = active in [k for _, _, k in RESOURCES]
    out = ['<header class="nav"><div class="nav-inner">']
    out.append(
        '<a class="brand" href="index.html">'
        f'<span class="mark">{I["wave"]}</span>'
        '<span>VIPER &rsquo;26<small>PTA GW Summer School</small></span></a>')
    out.append('<button class="nav-toggle" aria-label="Menu">' + I["menu"] + '</button>')
    out.append('<nav class="nav-links">')
    for href, label, key in NAV_ITEMS:
        cls = ' class="active"' if key == active else ''
        out.append(f'<a href="{href}"{cls}>{label}</a>')
    # Software dropdown
    out.append('<span class="has-menu"><a href="installation.html"'
               + (' class="active"' if soft_active else '') + '>Software &darr;</a>'
               '<span class="drop">'
               + ''.join(f'<a href="{h}">{l}</a>' for h, l, _ in SOFTWARE)
               + '</span></span>')
    # Resources dropdown
    out.append('<span class="has-menu"><a href="imp_papers.html"'
               + (' class="active"' if res_active else '') + '>Resources &darr;</a>'
               '<span class="drop">'
               + ''.join(f'<a href="{h}">{l}</a>' for h, l, _ in RESOURCES)
               + '</span></span>')
    out.append('</nav></div></header>')
    return ''.join(out)


def footer():
    return f'''<footer class="footer"><div class="wrap">
  <div class="footer-grid">
    <div>
      <a class="brand" href="index.html"><span class="mark">{I["wave"]}</span>
        <span>VIPER 2026<small>Summer School</small></span></a>
      <p class="muted" style="margin-top:1rem;max-width:34ch">
        The Vanderbilt Initiative in Probes of Extreme Relativity &mdash; training the next
        generation of nanohertz gravitational-wave astronomers.</p>
      <div class="contact-line">{I["mail"]}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
      <div class="contact-line">{I["home"]}<span>Stevenson Center, Vanderbilt University, Nashville, TN 37212</span></div>
    </div>
    <div>
      <h4>Program</h4>
      <a href="schedule.html">Schedule</a>
      <a href="syllabus.html">Syllabus</a>
      <a href="speakers.html">Speakers</a>
      <a href="participants.html">Participants</a>
    </div>
    <div>
      <h4>Get started</h4>
      <a href="installation.html">Software install</a>
      <a href="tutorials.html">Tutorials &amp; demos</a>
      <a href="imp_papers.html">Key papers</a>
      <a href="{VIPER_URL}">VIPER group {I["ext"]}</a>
    </div>
  </div>
  <div class="copyright">
    <span>&copy; 2026 VIPER &mdash; PTA GW Astrophysics Summer School.</span>
    <span>Vanderbilt University &middot; Nashville, TN</span>
  </div>
</div></footer>'''


FAVICON = ("data:image/svg+xml,"
           "%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E"
           "%3Cpath d='M2 12c2 0 2-6 4-6s2 12 4 12 2-12 4-12 2 6 4 6' "
           "fill='none' stroke='%235ec8e6' stroke-width='2' stroke-linecap='round'/%3E%3C/svg%3E")


def page(title, active, body, desc):
    full_title = f"{title} &middot; {SITE}" if title else SITE
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{full_title}</title>
<meta name="description" content="{html.escape(desc)}" />
<link rel="icon" href="{FAVICON}" />
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
<link rel="stylesheet" href="assets/css/site.css" />
</head>
<body>
<div class="cosmos"></div>
{nav(active)}
<main>
{body}
</main>
{footer()}
<script src="assets/js/site.js"></script>
</body>
</html>
'''


# --------------------------------------------------------------------------- #
# Schedule data (transcribed from the finalized 2026 program)                 #
# --------------------------------------------------------------------------- #
DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
W1_DATES = ["07/20", "07/21", "07/22", "07/23", "07/24"]
W2_DATES = ["07/27", "07/28", "07/29", "07/30", "07/31"]

# Rows are either a session row {"t": time, "cells": [(kind, title, who) x5]} or
# a banner row {"span": label, "time": t, "cls": class}. kind in
# {lecture, hands, hack, social, ""}.
COFFEE = {"span": "&#9749;&nbsp; Morning coffee, snacks &amp; lightning talks (10 min)", "time": "09:00", "cls": "coffee"}
PAUSE1 = {"span": "Pause &middot; 15 minutes", "time": "11:00", "cls": "pause"}
PAUSE2 = {"span": "Pause &middot; 15 minutes", "time": "15:15", "cls": "pause"}
LUNCH  = {"span": "&#127869;&#65039;&nbsp; Lunch (provided)", "time": "12:30", "cls": "lunch"}

WEEK1 = [
    COFFEE,
    {"t": "09:30", "cells": [
        ("lecture", "Introduction to GWs (theory)", "K. Schumacher"),
        ("lecture", "Pulsars &amp; pulsar timing", "T. Cromartie"),
        ("lecture", "Stochastic GW backgrounds (theory)", "S. Taylor"),
        ("lecture", "Introduction to Statistics", "A. Criswell"),
        ("lecture", "PTA likelihood", "N. Laal"),
    ]},
    PAUSE1,
    {"t": "11:15", "cells": [
        ("lecture", "Introduction to GWs (detectors across the spectrum)", "A. Criswell"),
        ("hands", "Timing a pulsar (tempo2, PINT, JUG)", "M. Miles"),
        ("lecture", "SMBHBs (astro theory)", "J. Runnoe"),
        ("hands", "Practical statistics &amp; foundational MCMC", "K. Gersbach"),
        ("hands", "Detecting a GWB (frequentist)", "K. Gersbach"),
    ]},
    LUNCH,
    {"t": "14:00", "cells": [
        ("hands", "Software Helpdesk", ""),
        ("lecture", "Pulsar timing response to GWs", "S. Taylor"),
        ("hands", "Holodeck", "K. G&uuml;ltekin"),
        ("hack", "Hack time", ""),
        ("hands", "Detecting a GWB (Bayesian)", "N. Laal"),
    ]},
    PAUSE2,
    {"t": "15:30", "cells": [
        ("social", "Introductions, networking &amp; EMIT DEI exercises", ""),
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("social", "Wrap-up + Ringdown (4pm)", ""),
    ]},
    {"t": "17:00", "cells": [
        ("social", "Welcome Reception", ""),
        ("", "", ""), ("", "", ""), ("", "", ""), ("", "", ""),
    ]},
]

WEEK2 = [
    COFFEE,
    {"t": "09:30", "cells": [
        ("lecture", "New Physics GW Signals", "A. Mitridate / K. Schumacher"),
        ("lecture", "Noise", "B. Larsen"),
        ("lecture", "EM SMBHBs", "M. Charisi"),
        ("lecture", "Advanced Sampling Methods", "T. Littenberg"),
        ("social", "Summary, student talks &amp; goodbyes", ""),
    ]},
    PAUSE1,
    {"t": "11:15", "cells": [
        ("hands", "PTArcade", "D. Wright"),
        ("lecture", "Continuous GW Signals", "C. Witt / M. Miles"),
        ("lecture", "GWB Population inference", "N. Laal"),
        ("hack", "Hack time", ""),
        ("", "", ""),
    ]},
    LUNCH,
    {"t": "14:00", "cells": [
        ("lecture", "ORFs, Anisotropy, Polarization &amp; Beyond-GR", "L. Schult"),
        ("hands", "Detecting a CW Signal", "M. Miles"),
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("", "", ""),
    ]},
    PAUSE2,
    {"t": "15:30", "cells": [
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("hack", "Hack time", ""),
        ("", "", ""),
    ]},
]


def render_week(rows, dates):
    out = ['<div class="sched-scroll"><table class="sched"><thead><tr>',
           '<th class="time">Time</th>']
    for day, d in zip(DAYS, dates):
        out.append(f'<th>{day}<span class="date">{d}/2026</span></th>')
    out.append('</tr></thead><tbody>')
    for row in rows:
        if "span" in row:
            out.append(f'<tr class="span-row {row["cls"]}"><td class="time">{row["time"]}</td>'
                       f'<td colspan="5">{row["span"]}</td></tr>')
            continue
        out.append(f'<tr><td class="time">{row["t"]}</td>')
        for kind, title, who in row["cells"]:
            if not kind and not title:
                out.append('<td class="empty"></td>')
                continue
            who_html = f'<span class="who">{who}</span>' if who else ''
            out.append(f'<td><div class="cell {kind}">{title}{who_html}</div></td>')
        out.append('</tr>')
    out.append('</tbody></table></div>')
    return ''.join(out)


def legend():
    return ('<div class="legend">'
            '<span><i class="lg-lecture"></i> Lecture</span>'
            '<span><i class="lg-hands"></i> Hands-on tutorial</span>'
            '<span><i class="lg-hack"></i> Hack time</span>'
            '<span><i class="lg-social"></i> Social / community</span>'
            '</div>')


# --------------------------------------------------------------------------- #
# Instructors (drawn from the program; affiliations intentionally omitted to   #
# avoid guessing — fill them in as confirmations arrive).                      #
# --------------------------------------------------------------------------- #
INSTRUCTORS = [
    ("Stephen Taylor", "ST", "Organizer &middot; Stochastic GW backgrounds; Pulsar timing response to GWs"),
    ("Maria Charisi", "MC", "Electromagnetic signatures of SMBH binaries"),
    ("Thankful Cromartie", "TC", "Pulsars &amp; pulsar timing"),
    ("Andrew Criswell", "AC", "Introduction to statistics; GWs across the spectrum"),
    ("Kyle Gersbach", "KG", "Practical statistics &amp; MCMC; Detecting a GWB (frequentist)"),
    ("Kayhan G&uuml;ltekin", "KG", "Holodeck"),
    ("Nima Laal", "NL", "PTA likelihood; Detecting a GWB (Bayesian); Population inference"),
    ("Bjorn Larsen", "BL", "Noise modeling"),
    ("Tyson Littenberg", "TL", "Advanced sampling methods"),
    ("Matthew Miles", "MM", "Timing a pulsar; Continuous GW signals; CW detection"),
    ("Andrea Mitridate", "AM", "New physics GW signals"),
    ("Jessie Runnoe", "JR", "Supermassive black-hole binaries (astrophysics)"),
    ("Kyle Schumacher", "KS", "Introduction to GWs (theory); New physics GW signals"),
    ("L. Schult", "LS", "ORFs, anisotropy, polarization &amp; beyond-GR"),
    ("Caitlin Witt", "CW", "Continuous GW signals"),
    ("David Wright", "DW", "PTArcade"),
]


def people_html(people):
    out = ['<div class="people">']
    for name, ini, topic in people:
        out.append(f'<div class="person"><span class="av">{ini}</span>'
                   f'<div><div class="nm">{name}</div><div class="tp">{topic}</div></div></div>')
    out.append('</div>')
    return ''.join(out)


# --------------------------------------------------------------------------- #
# Page bodies                                                                  #
# --------------------------------------------------------------------------- #

INDEX = f'''
<section class="hero"><div class="wrap">
  <span class="badge"><span class="dot"></span> {DATES} &middot; Vanderbilt University, Nashville TN</span>
  <h1>The <span class="gradient-text">nanohertz</span> gravitational-wave universe, in two weeks.</h1>
  <p class="lead">The 2026 VIPER Summer School on Pulsar Timing Array GW Astrophysics &mdash;
  your gateway into the theory, sources, statistics, and data analysis behind the
  nanohertz gravitational-wave sky.</p>
  <div class="hero-meta">
    <span class="item">{I["calendar"]} Two weeks &middot; Mon&ndash;Fri</span>
    <span class="item">{I["clock"]} 9:00 am &ndash; 4:00 pm daily</span>
    <span class="item">{I["pin"]} Vanderbilt University</span>
  </div>
  <div class="btn-row">
    <a class="btn btn-primary" href="schedule.html">View the schedule {I["arrow"]}</a>
    <a class="btn btn-ghost" href="{DEMOS}">Interactive demos {I["ext"]}</a>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <span class="eyebrow">{I["spark"]} What this is</span>
  <h2>Key points</h2>
  <div class="grid cols-4" style="margin-top:1.8rem">
    <article class="card"><div class="ico">{I["gem"]}</div><h3>Goals</h3>
      <p>Build a solid command of the fundamentals of gravitational-wave astrophysics &mdash;
      with an emphasis on the nanohertz band &mdash; and learn the methods used to hunt for
      nanohertz GWs with pulsar timing arrays.</p></article>
    <article class="card"><div class="ico">{I["rocket"]}</div><h3>Logistics</h3>
      <p>Two weeks, {DATES}. Mornings are lectures; afternoons mix hands-on software
      tutorials, hack time, and a software helpdesk. Held in person at Vanderbilt,
      running 9:00&nbsp;am&ndash;4:00&nbsp;pm each weekday.</p></article>
    <article class="card"><div class="ico">{I["pin"]}</div><h3>Around Vanderbilt</h3>
      <p>Vanderbilt sits minutes from downtown Nashville and the airport. Midtown and
      Downtown &mdash; both walkable &mdash; host a huge range of food, music, and nightlife.</p></article>
    <article class="card"><div class="ico">{I["signal"]}</div><h3>Funding</h3>
      <p>The VIPER summer-school series is supported in part by NSF CAREER award
      #2146016, &ldquo;Unveiling the Nanohertz GW Discovery Landscape by Broadening
      Participation in Multi-Messenger Astrophysics.&rdquo;</p></article>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="split">
    <div>
      <span class="eyebrow">{I["calendar"]} The arc</span>
      <h2>From first principles to real PTA data</h2>
      <p class="lead" style="margin-bottom:1.2rem">Week&nbsp;1 lays the foundations &mdash; GW theory,
      pulsars and timing, stochastic backgrounds, supermassive black-hole binaries, and
      the statistics that underpin every search. Week&nbsp;2 turns to frontier topics: new-physics
      signals, noise, electromagnetic counterparts, advanced sampling, population inference,
      anisotropy, and continuous waves.</p>
      <p>Throughout, afternoons are for getting your hands dirty &mdash; installing the stack,
      timing a pulsar, running Bayesian and frequentist GWB searches, and hacking on
      your own questions with instructors on hand.</p>
      <div class="btn-row">
        <a class="btn btn-ghost" href="syllabus.html">Read the syllabus {I["arrow"]}</a>
        <a class="btn btn-ghost" href="installation.html">Install the software {I["arrow"]}</a>
      </div>
    </div>
    <div class="framed"><img src="images/pta_TK.jpg" alt="A pulsar timing array probing passing gravitational waves" loading="lazy" /></div>
  </div>
</div></section>

<section class="section tight"><div class="wrap">
  <div class="card" style="display:flex;flex-wrap:wrap;align-items:center;gap:1.4rem;justify-content:space-between;border-color:rgba(155,123,255,.35)">
    <div style="max-width:60ch">
      <span class="eyebrow">{I["spark"]} Play with the physics</span>
      <h2 style="margin-bottom:.4rem">Interactive companion demos</h2>
      <p style="margin:0">A set of self-contained, browser-based demos &mdash; watch a binary radiate,
      stretch a ring of test masses, time a pulsar against a passing GW, and collapse pulsar
      pairs onto the Hellings &amp; Downs curve. No install required.</p>
    </div>
    <a class="btn btn-primary" href="{DEMOS}">Launch demos {I["ext"]}</a>
  </div>
</div></section>
'''

SCHEDULE = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["calendar"]} {DATES}</span>
  <h1>Schedule</h1>
  <p class="lead">Two weeks of lectures, hands-on tutorials, and hack time. Mornings open with
  coffee and 10-minute lightning talks at 9:00.</p>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="week-tabs" data-tab-group data-tab-scope="#sched">
    <button class="week-tab active" data-tab="w1">Week 1</button>
    <button class="week-tab" data-tab="w2">Week 2</button>
  </div>
  <div id="sched">
    <div class="week-panel active" data-panel="w1">
      <p class="week-meta">Week 1 &middot; July 20&ndash;24, 2026 &middot; foundations</p>
      {render_week(WEEK1, W1_DATES)}
    </div>
    <div class="week-panel" data-panel="w2">
      <p class="week-meta">Week 2 &middot; July 27&ndash;31, 2026 &middot; frontier topics &amp; methods</p>
      {render_week(WEEK2, W2_DATES)}
    </div>
  </div>
  {legend()}
  <p class="note" style="margin-top:1.6rem">Times and titles reflect the finalized program and may
  shift slightly. Speaker initials are listed in each block; see the
  <a href="speakers.html">Speakers</a> page for the full list.</p>
</div></section>
'''

SYLLABUS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["book"]} Program</span>
  <h1>Syllabus</h1>
  <p class="lead">What we cover, roughly in the order we cover it.</p>
</div></section>
<section class="section tight"><div class="wrap"><div class="prose">
  <h2>Week 1 &mdash; foundations</h2>
  <ul>
    <li><b>The GW landscape:</b> gravitational-wave theory and astrophysics across the spectrum;
      detectors from the ground-based band down to the nanohertz.</li>
    <li><b>Pulsars &amp; pulsar timing:</b> what pulsars are, how we time them
      (tempo2, PINT), and the timing response to gravitational waves.</li>
    <li><b>Stochastic GW backgrounds:</b> probing backgrounds through statistics; n-point
      correlations; the overlap reduction function and the Hellings &amp; Downs curve.</li>
    <li><b>Sources &amp; signals:</b> supermassive black-hole binaries as individual sources and
      as the origin of a GW background; the astrophysics behind the population.</li>
    <li><b>A tour of astro-statistics:</b> frequentist and Bayesian inference, parameter
      estimation, model selection, and foundational MCMC.</li>
    <li><b>The PTA likelihood &amp; first detections:</b> the structure of the PTA likelihood and
      practical recipes for detecting a GW background, both frequentist and Bayesian.</li>
  </ul>

  <hr />

  <h2>Week 2 &mdash; frontier topics &amp; methods</h2>
  <ul>
    <li><b>New-physics GW signals:</b> cosmological and beyond-Standard-Model sources of a
      nanohertz background, and how to model them (e.g. PTArcade).</li>
    <li><b>Noise:</b> the noise budget of a pulsar timing array and how it shapes inference.</li>
    <li><b>Electromagnetic SMBH binaries:</b> multi-messenger and EM signatures of inspiralling
      supermassive black holes.</li>
    <li><b>Advanced sampling:</b> modern samplers and techniques for high-dimensional,
      expensive PTA posteriors.</li>
    <li><b>Population inference:</b> inferring the SMBHB population from a measured background.</li>
    <li><b>Continuous waves:</b> searching for individual, resolvable SMBH binaries.</li>
    <li><b>Beyond the background:</b> overlap reduction functions, anisotropy, polarization,
      and tests of general relativity.</li>
  </ul>

  <hr />

  <p>Afternoons are dedicated to hands-on tutorials, a software helpdesk, and open
  <b>hack time</b> &mdash; bring your own questions and data. See the
  <a href="schedule.html">schedule</a> for the day-by-day breakdown and the
  <a href="tutorials.html">tutorials</a> page for the notebooks.</p>
</div></div></section>
'''

SPEAKERS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["users"]} Program</span>
  <h1>Speakers &amp; instructors</h1>
  <p class="lead">The people leading the lectures and tutorials, with the topics they teach.</p>
</div></section>
<section class="section tight"><div class="wrap">
  {people_html(INSTRUCTORS)}
  <p class="note" style="margin-top:1.6rem">Drawn from the finalized program. Affiliations and
  full bios will be added as they are confirmed.</p>
</div></section>
'''

PARTICIPANTS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["users"]} Program</span>
  <h1>Participants</h1>
</div></section>
<section class="section tight"><div class="wrap"><div class="prose">
  <p>The list of 2026 participants will be posted here ahead of the school. If you have been
  admitted and would like to coordinate lodging or travel with fellow attendees, the list will
  let you find one another &mdash; see the <a href="travel.html">travel</a> page for lodging options.</p>
  <div class="note"><b>Registered?</b> Your name will appear here closer to the start date.
  Questions about registration or logistics? Email
  <a href="mailto:{EMAIL}">{EMAIL}</a>.</div>
</div></div></section>
'''

TRAVEL = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["pin"]} Getting here</span>
  <h1>Traveling to Vanderbilt</h1>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="framed" style="margin-bottom:2rem"><img src="images/nashville.jpeg" alt="Nashville skyline along the river" loading="lazy" /></div>
  <div class="prose">
  <p>Vanderbilt University is a private university in Nashville, Tennessee. Nashville is
  sometimes called <i>Music City</i> &mdash; most famous for country music, but home to an endless
  variety of music and entertainment.</p>

  <h2>When</h2>
  <p>The school runs {DATES} (two weeks, Monday&ndash;Friday). Plan to arrive the weekend before
  July&nbsp;20 and depart on or after Friday July&nbsp;31.</p>

  <h2>Airport</h2>
  <p>Nashville International Airport (BNA) is roughly a 15&ndash;20 minute drive from Vanderbilt.
  An Uber or Lyft to or from campus costs about $20&ndash;$30.</p>

  <h2>Lodging</h2>
  <p>Nashville is a popular destination, so book early &mdash; especially for a two-week stay. Options include:</p>
  <ul>
    <li><b>Scarritt Bennett Center:</b> a conference center on the edge of campus with no-frills
      accommodation; suites with shared bathrooms are often available.</li>
    <li><b>Airbnb / short-term rentals:</b> entire apartments or houses close to campus, more
      affordable if shared. Use the <a href="participants.html">participants</a> list to find people to share with.</li>
  </ul>

  <h2>Getting around</h2>
  <p>Nashville has a limited bus network. E-scooters are easy to unlock by app and popular for
  short distances; for longer trips, Uber and Lyft are the most reliable option. Much of
  Midtown and Downtown is walkable from campus.</p>
  </div>
</div></section>
'''

INSTALLATION = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["download"]} Software</span>
  <h1>Installation</h1>
  <p class="lead">Get the PTA stack and its dependencies running before you arrive. Pick your platform.</p>
</div></section>
<section class="section tight"><div class="wrap"><div class="prose">
  <div class="os-tabs" data-tab-group data-tab-scope="#os">
    <button class="os-tab active" data-tab="linux">Linux</button>
    <button class="os-tab" data-tab="mac">macOS (Apple silicon)</button>
    <button class="os-tab" data-tab="win">Windows</button>
  </div>
  <div id="os">
    <div class="os-panel active" data-panel="linux">
      <p>First install <a href="https://docs.anaconda.com/anaconda/install/">Anaconda</a>, then:</p>
      <div class="codeblock"><span class="k">conda</span> create -n <span class="s">viper</span> -y -c conda-forge python=3.9
<span class="k">conda</span> activate <span class="s">viper</span>
<span class="k">conda</span> install -y -c conda-forge enterprise-pulsar enterprise_extensions
<span class="k">conda</span> install -y -c conda-forge nb_conda jupyterlab
<span class="k">pip</span> install la-forge
<span class="k">pip</span> install tqdm</div>
    </div>
    <div class="os-panel" data-panel="mac">
      <p>On Apple-silicon Macs, build the environment under the <code>osx-64</code> subdir.
      Install <a href="https://docs.anaconda.com/anaconda/install/">Anaconda</a> first, then:</p>
      <div class="codeblock"><span class="c"># build the env as osx-64 (runs under Rosetta)</span>
<span class="k">export</span> CONDA_SUBDIR=osx-64
<span class="k">conda</span> create -n <span class="s">viper</span> -y -c conda-forge python=3.9
<span class="k">conda</span> activate <span class="s">viper</span>
<span class="k">conda</span> config --env --set subdir osx-64
<span class="k">conda</span> install -y -c conda-forge enterprise-pulsar enterprise_extensions
<span class="k">conda</span> install -y -c conda-forge nb_conda jupyterlab
<span class="k">pip</span> install la-forge
<span class="k">pip</span> install tqdm</div>
    </div>
    <div class="os-panel" data-panel="win">
      <p>The PTA stack does <b>not</b> run natively on Windows. Install a Linux instance with
      <a href="https://learn.microsoft.com/en-us/windows/wsl/about">WSL</a>, then follow the Linux
      instructions inside it.</p>
    </div>
  </div>

  <hr />
  <h2>holodeck</h2>
  <p>The Week-1 holodeck tutorial needs a separate install. Follow the instructions at
  <a href="https://github.com/nanograv/holodeck">github.com/nanograv/holodeck</a>.</p>

  <h2>Course materials</h2>
  <p>Lecture slides and tutorial notebooks live in the materials repository:
  <a href="{MATERIALS}">{MATERIALS.split("//")[1]} {I["ext"]}</a>.
  Clone it and pull updates as the school approaches.</p>

  <div class="note">Stuck? There is a <b>Software Helpdesk</b> on the first afternoon (Mon, July 20)
  and instructors on hand throughout. Bring a laptop with the environment above already created.</div>
</div></div></section>
'''

TUTORIALS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["code"]} Software</span>
  <h1>Tutorials &amp; demos</h1>
  <p class="lead">Hands-on notebooks for the afternoons, plus browser-based demos you can open right now.</p>
</div></section>
<section class="section tight"><div class="wrap">
  <div class="grid cols-2">
    <a class="card" href="{MATERIALS}" style="text-decoration:none">
      <div class="ico">{I["code"]}</div>
      <h3>Course materials repository {I["ext"]}</h3>
      <p>Slides and Jupyter tutorials, organized by week and day &mdash; timing a pulsar, GWB
      searches (frequentist &amp; Bayesian), holodeck, continuous waves, and more. Clone it and
      <code>git pull</code> for updates.</p>
    </a>
    <a class="card" href="{DEMOS}" style="text-decoration:none">
      <div class="ico">{I["spark"]}</div>
      <h3>Interactive browser demos {I["ext"]}</h3>
      <p>Self-contained visual demos: GWs from compact binaries, pulse delays along the
      geodesic, pulsar timing vs. a passing GW, the Hellings &amp; Downs curve, and SMBH-binary
      light curves. No install needed.</p>
    </a>
  </div>

  <div class="prose" style="margin-top:2.4rem">
    <h2>What you&rsquo;ll work through</h2>
    <ul>
      <li><b>Timing a pulsar</b> with tempo2, PINT and JUG.</li>
      <li><b>Practical statistics &amp; foundational MCMC</b> &mdash; from priors to posteriors.</li>
      <li><b>Detecting a GW background</b> &mdash; both the optimal-statistic (frequentist) and
        full Bayesian (enterprise) routes.</li>
      <li><b>holodeck</b> &mdash; simulating the SMBHB population and its background.</li>
      <li><b>PTArcade</b> &mdash; new-physics interpretations of a nanohertz background.</li>
      <li><b>Continuous-wave</b> detection of individual binaries.</li>
    </ul>
    <p>Setup instructions are on the <a href="installation.html">installation</a> page. Come with
    the <code>viper</code> environment already built.</p>
  </div>
</div></section>
'''


def linkrow(href, name, desc, icon="link"):
    return (f'<a class="row" href="{href}"><span class="l"><span class="ic">{I[icon]}</span>'
            f'<span><span class="nm">{name}</span> <span class="ds">&mdash; {desc}</span></span></span>'
            f'<span class="arr">{I["arrow"]}</span></a>')


USEFUL_LINKS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["globe"]} Resources</span>
  <h1>Useful links</h1>
  <p class="lead">Software, collaborations, and pointers to dig deeper.</p>
</div></section>
<section class="section tight"><div class="wrap">
  <h3 style="margin-bottom:1rem">Software</h3>
  <div class="linklist">
    {linkrow("https://github.com/nanograv/enterprise", "enterprise", "the core PTA Bayesian inference library", "code")}
    {linkrow("https://github.com/nanograv/enterprise_extensions", "enterprise_extensions", "models &amp; helpers built on enterprise", "code")}
    {linkrow("https://github.com/nanograv/PINT", "PINT", "modern pulsar-timing package (Python)", "code")}
    {linkrow("https://github.com/nanograv/holodeck", "holodeck", "SMBHB population &amp; background simulator", "code")}
    {linkrow("https://github.com/nanograv/la_forge", "la_forge", "post-processing PTA MCMC chains", "code")}
    {linkrow("https://andrea-mitridate.github.io/PTArcade/", "PTArcade", "new-physics interpretations of a nanohertz GWB", "code")}
  </div>

  <h3 style="margin:2rem 0 1rem">Collaborations</h3>
  <div class="linklist">
    {linkrow("https://nanograv.org", "NANOGrav", "the North American Nanohertz Observatory for GWs", "globe")}
    {linkrow("https://www.ipta4gw.org", "IPTA", "the International Pulsar Timing Array", "globe")}
    {linkrow("https://www.epta.eu.org", "EPTA", "the European Pulsar Timing Array", "globe")}
    {linkrow("https://www.atnf.csiro.au/research/pulsar/ppta/", "PPTA", "the Parkes Pulsar Timing Array", "globe")}
  </div>

  <h3 style="margin:2rem 0 1rem">This school</h3>
  <div class="linklist">
    {linkrow(DEMOS, "Interactive demos", "browser-based visual companions", "spark")}
    {linkrow(MATERIALS, "Materials repository", "slides &amp; tutorial notebooks", "code")}
    {linkrow(VIPER_URL, "VIPER group", "the Taylor group at Vanderbilt", "users")}
  </div>
</div></section>
'''


def ref(title, authors, meta, href):
    return (f'<a class="ref" href="{href}" style="display:block;text-decoration:none">'
            f'<div class="t">{title}</div><div class="a">{authors}</div>'
            f'<div class="meta">{meta}</div></a>')


IMP_PAPERS = f'''
<section class="page-head"><div class="wrap">
  <span class="eyebrow">{I["book"]} Resources</span>
  <h1>Key papers</h1>
  <p class="lead">A starting reading list &mdash; foundational results and recent landmarks in
  nanohertz GW astrophysics. Not exhaustive; a springboard.</p>
</div></section>
<section class="section tight"><div class="wrap">
  <h3 style="margin-bottom:1rem">Foundations</h3>
  <div class="refs">
    {ref("Pulsar timing and an upper limit on a presumed gravitational-radiation background",
         "Detweiler, S. (1979)", "ApJ 234, 1100 &middot; doi:10.1086/157593",
         "https://doi.org/10.1086/157593")}
    {ref("Upper limits on the isotropic gravitational radiation background from pulsar timing analysis",
         "Hellings, R. W. &amp; Downs, G. S. (1983)", "ApJ 265, L39 &middot; doi:10.1086/183954",
         "https://doi.org/10.1086/183954")}
    {ref("A practical theorem on gravitational wave backgrounds",
         "Phinney, E. S. (2001)", "arXiv:astro-ph/0108028",
         "https://arxiv.org/abs/astro-ph/0108028")}
    {ref("Detection methods for stochastic gravitational-wave backgrounds: a unified treatment",
         "Romano, J. D. &amp; Cornish, N. J. (2017)", "Living Rev. Relativ. 20, 2 &middot; arXiv:1608.06889",
         "https://arxiv.org/abs/1608.06889")}
  </div>

  <h3 style="margin:2rem 0 1rem">Sources &amp; astrophysics</h3>
  <div class="refs">
    {ref("The astrophysics of nanohertz gravitational waves",
         "Burke-Spolaor, S. et al. (2019)", "A&amp;A Rev. 27, 5 &middot; arXiv:1811.08826",
         "https://arxiv.org/abs/1811.08826")}
    {ref("The Nanohertz Gravitational Wave Astronomer",
         "Taylor, S. R. (2021)", "CRC Press &middot; arXiv:2105.13270",
         "https://arxiv.org/abs/2105.13270")}
  </div>

  <h3 style="margin:2rem 0 1rem">The evidence (2023)</h3>
  <div class="refs">
    {ref("The NANOGrav 15 yr Data Set: Evidence for a Gravitational-wave Background",
         "Agazie, G. et al. (NANOGrav) (2023)", "ApJL 951, L8 &middot; arXiv:2306.16213",
         "https://arxiv.org/abs/2306.16213")}
    {ref("The second data release from the European Pulsar Timing Array III: Search for GW signals",
         "EPTA &amp; InPTA Collaborations (2023)", "A&amp;A 678, A50 &middot; arXiv:2306.16214",
         "https://arxiv.org/abs/2306.16214")}
  </div>

  <p class="note" style="margin-top:1.6rem">Lectures will point you to the most relevant papers for
  each topic. For software references, see <a href="useful_links.html">useful links</a>.</p>
</div></section>
'''


# --------------------------------------------------------------------------- #
# Assemble & write                                                             #
# --------------------------------------------------------------------------- #
PAGES = {
    "index.html":        ("", "home", INDEX,
                           "The 2026 VIPER Summer School on Pulsar Timing Array gravitational-wave astrophysics, "
                           f"{DATES}, Vanderbilt University, Nashville TN."),
    "schedule.html":     ("Schedule", "schedule", SCHEDULE,
                           "Two-week schedule for the 2026 VIPER PTA GW summer school."),
    "syllabus.html":     ("Syllabus", "syllabus", SYLLABUS,
                           "Topics covered at the 2026 VIPER PTA GW summer school."),
    "speakers.html":     ("Speakers", "speakers", SPEAKERS,
                           "Speakers and instructors at the 2026 VIPER PTA GW summer school."),
    "participants.html": ("Participants", "participants", PARTICIPANTS,
                           "Participants of the 2026 VIPER PTA GW summer school."),
    "travel.html":       ("Travel", "travel", TRAVEL,
                           "How to travel to Vanderbilt University in Nashville for the 2026 VIPER summer school."),
    "installation.html": ("Installation", "installation", INSTALLATION,
                           "Install the PTA software stack for the 2026 VIPER summer school."),
    "tutorials.html":    ("Tutorials &amp; demos", "tutorials", TUTORIALS,
                           "Hands-on tutorials and interactive demos for the 2026 VIPER summer school."),
    "imp_papers.html":   ("Key papers", "imp_papers", IMP_PAPERS,
                           "A reading list of key nanohertz gravitational-wave papers."),
    "useful_links.html": ("Useful links", "useful_links", USEFUL_LINKS,
                           "Software, collaborations and resources for nanohertz GW astrophysics."),
}


def main():
    for fname, (title, active, body, desc) in PAGES.items():
        with open(fname, "w", encoding="utf-8") as fh:
            fh.write(page(title, active, body, desc))
        print(f"wrote {fname}")


if __name__ == "__main__":
    main()
