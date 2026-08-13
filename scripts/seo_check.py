#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parents[1]
HTML = (ROOT / "index.html").read_text(encoding="utf-8")
errors=[]

def require(pattern, label, flags=0):
    if not re.search(pattern, HTML, flags): errors.append(f"Missing {label}")

require(r'<title>[^<]{20,65}</title>', 'descriptive <title>')
require(r'<meta name="description" content="[^\"]{70,170}">', 'meta description')
require(r'<meta name="robots" content="[^"]*index[^"]*follow', 'index/follow robots meta')
require(r'<link rel="canonical" href="https://hollyharrishistorian\.com/">', 'canonical URL')
require(r'<meta property="og:title"', 'Open Graph title')
require(r'<meta property="og:image" content="https://hollyharrishistorian\.com/', 'absolute Open Graph image')
require(r'<meta name="twitter:card" content="summary_large_image">', 'Twitter/X card')
require(r'<script type="application/ld\+json">', 'JSON-LD structured data')
require(r'<h1[^>]*>[^<]+</h1>', 'single visible H1')

if len(re.findall(r'<h1\b', HTML)) != 1:
    errors.append('Homepage must have exactly one H1')

# Parse JSON-LD strictly.
m=re.search(r'<script type="application/ld\+json">(.*?)</script>', HTML, re.S)
if m:
    try:
        data=json.loads(m.group(1))
        if data.get('@type')!='ProfilePage': errors.append('JSON-LD should describe a ProfilePage')
        if data.get('mainEntity',{}).get('@type')!='Person': errors.append('ProfilePage mainEntity should be Person')
    except Exception as exc: errors.append(f'Invalid JSON-LD: {exc}')

for required in ['robots.txt','sitemap.xml','favicon.svg','site.webmanifest','images/social/holly-harris-social-card.jpg']:
    if not (ROOT/required).exists(): errors.append(f'Missing {required}')

sitemap=(ROOT/'sitemap.xml').read_text(encoding='utf-8')
if 'https://hollyharrishistorian.com/' not in sitemap: errors.append('Canonical homepage missing from sitemap')
robots=(ROOT/'robots.txt').read_text(encoding='utf-8')
if 'Sitemap: https://hollyharrishistorian.com/sitemap.xml' not in robots: errors.append('robots.txt missing sitemap declaration')

if re.search(r'<meta\s+name=["\']keywords["\']', HTML, re.I):
    errors.append('Remove meta keywords; keyword stuffing is not used for Google ranking')

if errors:
    print('SEO CHECK FAILED')
    for e in errors: print(' -',e)
    sys.exit(1)
print('SEO CHECK PASSED')
