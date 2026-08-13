# Holly Harris — Option 1 final website

Final **Foreign Affairs × Monocle** direction: restrained, photographic, sophisticated, and one continuous scrolling page.

Navigation: **About · Research · For Media · CV · Photography · Contact**.

## Identity
The hierarchy is **Holly Harris → Historian → U.S.–Russia Relations & American Foreign Policy**. The secondary descriptor is **Historian · Researcher · Writer**. “Academic” is intentionally not added because the Ph.D. affiliation, fellowships, publications, CV, and research sections already establish it.

## Replace photographs
Use these exact paths:
- `images/headshot.jpeg`
- `images/about-archive.webp`
- `images/research-city.webp`
- `images/photography/city-01.webp`
- `images/photography/landscape-01.webp`
- `images/photography/camera-01.webp`
- `images/photography/archive-01.webp`

Then search `index.html` for `REPLACE CAPTION`, enter the correct location/year, and update the nearby `alt` text. Keep original/private camera files outside the public repository.

## Install
1. Back up the current repository.
2. Copy the **contents** of this folder into the repository root; `index.html` must be at the root.
3. Replace placeholder photographs.
4. Run:

```bash
python -m pip install -r requirements.txt
python scripts/validate_site.py
python scripts/seo_check.py
```

5. Commit and push:

```bash
git add -A
git commit -m "Launch Option 1 editorial website"
git push origin main
```

## GitHub Pages
In GitHub: **Settings → Pages → Build and deployment → Source → GitHub Actions**. Confirm the custom domain is `hollyharrishistorian.com` and enable **Enforce HTTPS** when available.

## Google
After launch, add the domain to Google Search Console, submit `https://hollyharrishistorian.com/sitemap.xml`, inspect the homepage, and request indexing.
