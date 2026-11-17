#!/usr/bin/env python3
"""Download each supporter's logo from the supporter's own website and save a small copy.

python3 scripts/fetch_logos.py   (needs Pillow)

Each logo is scaled to the same height and put on a white rounded card, so it reads on light and
dark pages. Output: assets/supporters/<slug>.png. The GitHub org profile uses the same files.
"""
import io, urllib.request
from pathlib import Path
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parent.parent
H, PAD = 64, 12  # logo height and padding, in pixels (shown at half size)
SUPPORTERS = {
    # slug: list of image URLs on the supporter's own site, placed side by side
    'budaedu': ['https://www.budaedu.org/img/brand/wheel_logo.png',
                'https://www.budaedu.org/img/brand/word_logo.png'],
    'openpecha': ['https://openpecha.org/lovable-uploads/d40b99df-a81c-4b68-8c6c-84301d427a2b.png'],
    'ubi': ['https://unionebuddhistaitaliana.it/wp-content/uploads/2026/06/Logo-UBI.png'],
}


def load(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (BuddhistAI logo fetch)'})
    with urllib.request.urlopen(req, timeout=30) as r:
        im = Image.open(io.BytesIO(r.read())).convert('RGBA')
    box = im.getbbox()  # trim empty transparent edges
    return im.crop(box) if box else im


def build(urls):
    parts = []
    for u in urls:
        im = load(u)
        parts.append(im.resize((round(im.width * H / im.height), H), Image.LANCZOS))
    gap = PAD
    w = sum(p.width for p in parts) + gap * (len(parts) - 1) + 2 * PAD
    card = Image.new('RGBA', (w, H + 2 * PAD), (0, 0, 0, 0))
    ImageDraw.Draw(card).rounded_rectangle((0, 0, card.width - 1, card.height - 1), radius=14, fill='white')
    x = PAD
    for p in parts:
        card.alpha_composite(p, (x, PAD))
        x += p.width + gap
    return card


def main():
    out = ROOT / 'assets' / 'supporters'
    out.mkdir(parents=True, exist_ok=True)
    for slug, urls in SUPPORTERS.items():
        im = build(urls)
        im.save(out / f'{slug}.png', optimize=True)
        print(f'{slug}.png {im.width}x{im.height}')


if __name__ == '__main__':
    main()
