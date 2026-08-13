#!/usr/bin/env python3
from pathlib import Path
from html.parser import HTMLParser
from PIL import Image
import sys
ROOT=Path(__file__).resolve().parents[1]
REQ=["index.html","styles.css","404.html","CNAME",".nojekyll","images/headshot.jpeg","images/about-archive.webp","images/research-city.webp","images/photography/city-01.webp","images/photography/landscape-01.webp","images/photography/camera-01.webp","images/photography/archive-01.webp"]
class P(HTMLParser):
    def __init__(self): super().__init__(); self.ids=set(); self.hrefs=[]; self.img=[]
    def handle_starttag(self,t,a):
        d=dict(a)
        if d.get("id"): self.ids.add(d["id"])
        if t=="a" and d.get("href"): self.hrefs.append(d["href"])
        if t=="img": self.img.append(d)
def main():
    errors=[]
    for rel in REQ:
        if not (ROOT/rel).exists(): errors.append(f"Missing {rel}")
    p=P(); p.feed((ROOT/"index.html").read_text())
    for anchor in ["about","research","media","cv","photography","contact"]:
        if anchor not in p.ids: errors.append(f"Missing section #{anchor}")
    for d in p.img:
        src=d.get("src","")
        if not d.get("alt"): errors.append(f"Missing alt text: {src}")
        if not d.get("width") or not d.get("height"): errors.append(f"Missing dimensions: {src}")
        path=ROOT/src
        if path.exists():
            try:
                with Image.open(path) as im:
                    if any(k.lower() in {"exif","xmp","iptc","photoshop","comment"} for k in im.info): errors.append(f"Metadata found: {src}")
            except Exception as e: errors.append(f"Unreadable image {src}: {e}")
    text=(ROOT/"index.html").read_text()
    if "Holly-Harris-CV.pdf" in text or "Download CV" in text or "Download full CV" in text: errors.append("CV download remains in HTML")
    if errors:
        print("FAILED")
        for e in errors: print("-",e)
        return 1
    print("PASSED: required files, six sections, images, and no CV download detected.")
    if "REPLACE CAPTION" in text: print("NOTE: replace temporary photo captions before publishing.")
    return 0
if __name__=="__main__": raise SystemExit(main())
