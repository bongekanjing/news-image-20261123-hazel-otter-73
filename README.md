# Front Page — Monday 23 November 2026

A single-page broadsheet front page summing up Monday, 23 November 2026.

## The lead

Ukraine's naval drones sank a Russian warship in Benghazi harbour, Libya — an
operation that puts Ukrainian unmanned surface vessels into the Mediterranean and
into a Russian naval footprint that had been considered out of reach.

## Also on this front page

Six further stories from that day, spread across five regions:

- **Europe** — the continent's response to the Benghazi strike and the winter
  energy picture.
- **Middle East** — the diplomatic fallout from an attack inside Libya.
- **East Asia** — the region's shipping and security read on the same event.
- **Caucasus** — the view from the states between the Black Sea and the Caspian.
- **Latin America** — a separate story from the western hemisphere.

## The artwork

`assets/entry.png` — 1024x1024, full front page in a dense broadsheet layout:
masthead and date, the lead story, second leads, and a grid of briefs with a
regional index.

## Running

Python 3.13, standard library only. No network, no third-party packages.

```sh
python3 main.py
```

`main.py` copies `assets/entry.png` to `entry.png` inside the output directory.
The output directory defaults to `/output` and can be overridden:

```sh
MAKEFUN_OUTPUT_DIR=out1 python3 main.py
```

The source is resolved relative to `main.py` itself, so the script works from any
working directory. If the source artwork is missing it exits with status 1 and a
clear message. The copy is byte-identical on every run.

## Layout

```
main.py            copy the artwork into the output directory
assets/entry.png   the front page, 1024x1024
README.md          this file
```

Bounty: https://make.fun/bounty/news-image-20261123
