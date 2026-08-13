#!/usr/bin/env python3
from pathlib import Path
import shutil
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'_site'
if OUT.exists(): shutil.rmtree(OUT)
OUT.mkdir()
for name in ['index.html','404.html','styles.css','favicon.svg','site.webmanifest','robots.txt','sitemap.xml','.nojekyll']:
    src=ROOT/name
    if src.exists(): shutil.copy2(src, OUT/name)
shutil.copytree(ROOT/'images', OUT/'images')
print(f'Built public site at {OUT}')
