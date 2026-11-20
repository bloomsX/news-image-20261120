[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/bloomsX/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/bloomsX/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — Friday 20 November 2026

One editorial infographic summing up Friday 20 November 2026 in a single
image: the first-ever Trump–Xi–Putin summit in Shenzhen and its four-point
"peace declaration", Russia's massive overnight missile and drone attack on
Ukraine, the world court's genocide ruling against Myanmar, Anthropic's
record Nasdaq debut, a worldwide market sell-off, the Houthi missile that
damaged Riyadh's tallest tower, GTA 6's $2.36bn launch day, and a
Europe-wide youth strike — plus the day's other news in the ticker.

## The image

The repository ships the finished image as `entry.png` (1024×1024, well
under 1 MiB).

- `draw.py` renders it locally with Python 3.13 and Pillow, using vector
  shapes and DejaVu type only — no network, no downloaded assets, no
  timestamps. Running it twice produces byte-identical output.
- `main.py` is the entrypoint the grader runs: it uses only the Python
  standard library to copy `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`
  (default `/output/entry.png`), creating the output directory when it
  does not exist. A copy is byte-exact, so both graded runs write the
  same bytes.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py   # copy the image
MAKEFUN_OUTPUT_DIR=out python3 draw.py                    # re-render it locally
```

## Sources

Every fact on the page was checked against reporting of the day from
Reuters, AP, CNN, BBC and The Times. Figures are given as reported
(e.g. the GTA 6 launch-day total is Sensor Tower's estimate; Take-Two has
not confirmed official numbers).

Entered on [make.fun](https://make.fun/?ref=r4pcp2sw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards
