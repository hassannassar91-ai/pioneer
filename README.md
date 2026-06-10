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

## Deploy to Render (same flow as Visions Tech)

Repo: [github.com/hassannassar91-ai/pioneer](https://github.com/hassannassar91-ai/pioneer)

1. Log in to [Render](https://dashboard.render.com).
2. **New → Blueprint** → connect the `pioneer` GitHub repo.
3. Render reads `render.yaml` and creates:
   - Web service: `pioneer-web` → `https://pioneer-web.onrender.com`
   - PostgreSQL: `pioneer-db`
4. Click **Apply** and wait for the first deploy to finish.
5. Optional custom domain: add `domains` under the web service in `render.yaml`, then point DNS at Render.

### Environment (set automatically by Blueprint)

- `DJANGO_DEBUG=false`
- `DJANGO_SECRET_KEY` (generated)
- `DATABASE_URL` (from `pioneer-db`)
- `DJANGO_ALLOWED_HOSTS` / `DJANGO_CSRF_TRUSTED_ORIGINS` for `pioneer-web.onrender.com`

### After first deploy

Create an admin user in the Render shell:

```bash
python manage.py createsuperuser
```
