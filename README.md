# Pioneer Smart Systems Website (Django)

Company website for **Pioneer Smart Systems** (شركة الرواد للأنظمة الذكية) — built with the same structure and content as the Visions Tech site, with Pioneer navy + gold branding and logo.

## Stack

- Python 3.12+
- Django 5
- Tailwind CSS v4
- WhiteNoise + Gunicorn (production)

## Pages

| Route | Page |
|-------|------|
| `/` | Home |
| `/about/` | About |
| `/solutions/` | Solutions |
| `/industries/` | Industries |
| `/products/` | Products |
| `/projects/` | Projects |
| `/contact/` | Contact |

English and Arabic (EN/AR) language toggle included.

## Local development

```powershell
cd c:\Users\Fujitsu\Pioneer
.\.venv\Scripts\activate
npm run build:css    # or: npm run watch:css
python manage.py runserver
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Brand theme

- **Navy:** `#002B5B` (primary)
- **Gold:** `#C59D5F` (accent)
- Logo: `website/static/website/images/pioneer-logo.png`

## Deploy to Render

1. Commit and push to GitHub.
2. Render → **New → Blueprint** → connect repo.
3. Update `render.yaml` with your custom domain when ready.
