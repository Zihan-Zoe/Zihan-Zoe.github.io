# zihan-zoe.github.io

- **Contact card:** https://zihan-zoe.github.io/card/ (QR: `qr/card.png`, reuse it anywhere)
- **Papers:** one stable address and one QR code per paper: `https://zihan-zoe.github.io/p/<slug>/` → `qr/<slug>.png`

## Add a paper, or move one (e.g. OpenReview → arXiv)

1. Edit `papers.json`.
2. `pip install segno && python tools/build.py`
3. Commit and push.

The QR code encodes only the stable address, so changing a paper's `url` never changes its QR code.
To add a photo to the card, put a 4:5 portrait at `card/photo.jpg`.
