#!/usr/bin/env python3
"""Create metadata-stripped public web copies for the exact site photo slots."""
from pathlib import Path
import argparse
from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
SLOTS = {
    "headshot": ("images/headshot.jpeg", 1800, "JPEG"),
    "about-archive": ("images/about-archive.webp", 1800, "WEBP"),
    "research-city": ("images/research-city.webp", 2200, "WEBP"),
    "city": ("images/photography/city-01.webp", 2200, "WEBP"),
    "landscape": ("images/photography/landscape-01.webp", 2200, "WEBP"),
    "camera": ("images/photography/camera-01.webp", 1800, "WEBP"),
    "archive": ("images/photography/archive-01.webp", 2200, "WEBP"),
}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("slot", choices=SLOTS)
    p.add_argument("source")
    p.add_argument("--quality", type=int, default=86)
    args=p.parse_args()
    rel,max_edge,fmt=SLOTS[args.slot]
    src=Path(args.source).expanduser()
    out=ROOT/rel
    out.parent.mkdir(parents=True,exist_ok=True)
    with Image.open(src) as im:
        im=ImageOps.exif_transpose(im).convert("RGB")
        im.thumbnail((max_edge,max_edge), Image.Resampling.LANCZOS)
        kwargs={"quality":args.quality,"optimize":True}
        if fmt=="WEBP": kwargs["method"]=6
        im.save(out,fmt,**kwargs)
    print(out.relative_to(ROOT))

if __name__=="__main__": main()
