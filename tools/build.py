"""Build one redirect page and one QR code per paper, plus the contact-card QR.

Edit papers.json (add a paper, or change a paper's url), then run:
    pip install segno
    python tools/build.py
Each paper lives at https://zihan-zoe.github.io/p/<slug>/ and its QR code at qr/<slug>.png.
A QR code encodes only that stable address, so changing a paper's url never changes its QR code.
"""

import html
import json
from pathlib import Path

import segno

SITE = "https://zihan-zoe.github.io"
ROOT = Path(__file__).resolve().parent.parent

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta http-equiv="refresh" content="0; url={url}">
<link rel="canonical" href="{url}">
<style>body{{font-family:Arial,sans-serif;color:#1E1B3A;background:#fff;max-width:560px;margin:48px auto;padding:0 24px;line-height:1.5}}a{{color:#5A3FE0}}</style>
</head>
<body>
<p>{venue}</p>
<p>Redirecting to <a href="{url}">{title}</a></p>
</body>
</html>
"""


def qr(data: str, name: str) -> None:
    segno.make(data, error="m", micro=False).save(
        ROOT / "qr" / f"{name}.png", kind="png", scale=12, border=4, dark="#000000", light="#FFFFFF"
    )


def main() -> None:
    (ROOT / "qr").mkdir(exist_ok=True)
    qr(f"{SITE}/card/", "card")
    for p in json.loads((ROOT / "papers.json").read_text()):
        out = ROOT / "p" / p["slug"]
        out.mkdir(parents=True, exist_ok=True)
        esc = {k: html.escape(v, quote=True) for k, v in p.items()}
        (out / "index.html").write_text(PAGE.format(**esc))
        qr(f"{SITE}/p/{p['slug']}/", p["slug"])
        print(f"{SITE}/p/{p['slug']}/ -> {p['url']}")


if __name__ == "__main__":
    main()
