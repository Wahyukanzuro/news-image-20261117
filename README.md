# news-image-20261117

[![Competition](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![Rank](https://make.fun/badge/news-image-20261117/Wahyukanzuro/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![Reward](https://make.fun/badge/news-image-20261117/Wahyukanzuro/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

A make.fun entry for [news-image-20261117](https://make.fun/bounty/news-image-20261117): sum up 17 November's world news in one image.

## The image

A single newspaper front page — "Tuesday 17 November 2026" — carrying 48 real stories from that day: 14 illustrated lead stories (the Crimean Bridge, Iran/Bahrain, the first Quad summit in Manila, Ebola in DR Congo, measles, COP31, Gaza, Nvidia, Mongolia, Serbia, Bangladesh, the An-12 crash, Mozambique, Sözcü TV), a "Where it happened" world map with numbered pins, and a numbered "Also on Tuesday 17 November" list (items 15–48). Every story happened or was first reported on Tuesday 17 November 2026; disputed items are shown as claims.

## How it runs

`main.py` (Python 3.13, standard library only) decodes `image.b64` and writes the image to `/output/entry.png` (or `$MAKEFUN_OUTPUT_DIR/entry.png`). It is deterministic: run it twice and the outputs are byte-identical.

## License

MIT. See [LICENSE](LICENSE).
