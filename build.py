#!/usr/bin/env python3
"""Собирает фото для сайта.

Кладёшь фото в папки:
  photos/hero/     одно главное фото (первое по алфавиту)
  photos/fashion/  одежда, lookbook, e-commerce
  photos/body/     тело, спорт, бельё
  photos/image/    лицо, портрет, бьюти

Запуск:  python3 build.py
Скрипт уменьшает фото (до 1800 px), кладёт их в site/img/ и пишет site/photos.js.
Порядок в галерее = порядок имён файлов (01-..., 02-...).
"""
import json
import shutil
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "photos"
OUT = ROOT / "site" / "img"
CATS = ["fashion", "body", "image"]
EXT = {".jpg", ".jpeg", ".png", ".webp", ".heic"}
MAX = 1800


def convert(src: Path, dst: Path):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
    im.thumbnail((MAX, MAX))
    dst.parent.mkdir(parents=True, exist_ok=True)
    im.save(dst, "JPEG", quality=84, optimize=True, progressive=True)
    return im.size


def files(folder: Path):
    return sorted(p for p in folder.glob("*") if p.suffix.lower() in EXT)


def main():
    if OUT.exists():
        shutil.rmtree(OUT)
    data = {"hero": None, "items": []}

    hero = files(SRC / "hero")
    if hero:
        w, h = convert(hero[0], OUT / "hero.jpg")
        data["hero"] = {"src": "img/hero.jpg", "w": w, "h": h}

    for cat in CATS:
        for i, p in enumerate(files(SRC / cat), 1):
            name = f"{cat}-{i:02d}.jpg"
            w, h = convert(p, OUT / name)
            data["items"].append({"src": f"img/{name}", "cat": cat, "w": w, "h": h})

    js = "window.PHOTOS = " + json.dumps(data, indent=1) + ";\n"
    (ROOT / "site" / "photos.js").write_text(js)
    counts = {c: sum(1 for x in data["items"] if x["cat"] == c) for c in CATS}
    print("hero:", "yes" if data["hero"] else "no", "|", counts)


if __name__ == "__main__":
    main()
