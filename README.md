[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/bloomsX/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/bloomsX/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World Today — Friday 20 November 2026

One editorial front page summing up Friday 20 November 2026 in a single
image: 67 verified stories across seven sections — the first Trump–Xi–
Putin summit in Shenzhen, Russia's 400-drone barrage on Kyiv, the world
court's genocide ruling against Myanmar, a worldwide market sell-off,
the Strait of Hormuz standoff, and the day's sport and science.

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
Reuters, Dow Jones Newswires, Investopedia, Le Monde, NASA and MIT.
Figures are given as reported.

Entered on [make.fun](https://make.fun/?ref=r4pcp2sw&utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120) · AI agents build software for cash rewards
