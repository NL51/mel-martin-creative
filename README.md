# Mel Martin — A Life in Becoming

Personal creative home for Mel Martin. Built by RAIVYN.

## Source
- `src/index.html`: responsive design, content, gallery and client interactions.
- `src/server.js`: Worker routes, private R2 inquiry storage, privacy, robots and sitemap.
- `assets/`: supplied portrait mark and share card.
- `scripts/prepare.py`: embeds source and assets into the Worker.

## Build
Run `python scripts/prepare.py`, `bash scripts/build.sh`, then `node scripts/validate-artifact.mjs`.

## Contact handling
POST /api/contact validates fields and stores inquiries under `inquiries/YYYY-MM-DD/<uuid>.json` in the private R2 BUCKET. No public listing or read endpoint. Email notifications are not configured. Site administrators must review stored inquiries; visitors also have a direct mailto link. Configure an email provider and a retention process before a full business launch. Do not expose inquiry storage publicly.

## Content handoff
Replace labeled illustrative gallery studies with Mel's licensed photography/art. Replace concept book cover when available. Book and Human-AI program are in development; no checkout or unsupported availability claims. The planned book-inspired conversation series is separate from the existing Opportunity Now show. Domain MelMartin.me has not been connected. Canonical URLs currently point to the deployed Sites origin; update them with a custom-domain launch.

## GitHub
Mirror: https://github.com/NL51/mel-martin-creative
The Sites source repository remains the publishing source. Mirror changes to GitHub after Sites publication.
