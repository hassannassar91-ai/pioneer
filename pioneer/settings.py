"""
Django settings for Pioneer project.
"""

import os
from pathlib import Path
from urllib.parse import urlparse

import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get(
    "DJANGO_SECRET_KEY",
    "django-insecure-pioneer-dev-key-change-before-production",
)

DEBUG = os.environ.get("DJANGO_DEBUG", "true").lower() in ("1", "true", "yes")

DEFAULT_PROD_DOMAINS = [
    "pss-om.onrender.com",
    "pss-om.com",
    "www.pss-om.com",
]


def _dedupe(items):
    return list(dict.fromkeys(items))


def _build_allowed_hosts():
    hosts = []
    env_hosts = os.environ.get("DJANGO_ALLOWED_HOSTS", "").strip()
    if env_hosts:
        hosts.extend(h.strip() for h in env_hosts.split(",") if h.strip())

    render_url = os.environ.get("RENDER_EXTERNAL_URL", "").strip()
    if render_url:
        render_host = urlparse(render_url).hostname
        if render_host:
            hosts.append(render_host)

    if not hosts:
        hosts = ["localhost", "127.0.0.1", *DEFAULT_PROD_DOMAINS]

    # Any Render service URL (e.g. pioneer.onrender.com vs pioneer-web.onrender.com).
    hosts.append(".onrender.com")
    return _dedupe(hosts)


def _build_csrf_origins():
    origins = []
    env_origins = os.environ.get("DJANGO_CSRF_TRUSTED_ORIGINS", "").strip()
    if env_origins:
        origins.extend(x.strip() for x in env_origins.split(",") if x.strip())

    render_url = os.environ.get("RENDER_EXTERNAL_URL", "").strip()
    if render_url:
        origins.append(render_url.rstrip("/"))

    if not origins:
        origins = [f"https://{domain}" for domain in DEFAULT_PROD_DOMAINS]

    return _dedupe(origins)


ALLOWED_HOSTS = _build_allowed_hosts()
CSRF_TRUSTED_ORIGINS = _build_csrf_origins()

if not DEBUG:
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True

SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"
MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "website",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "pioneer.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "website.context_processors.company",
                "website.context_processors.language",
            ],
        },
    },
]

WSGI_APPLICATION = "pioneer.wsgi.application"

_database_url = os.environ.get("DATABASE_URL", "").strip()
if _database_url:
    DATABASES = {
        "default": dj_database_url.config(
            default=_database_url,
            conn_max_age=600,
            ssl_require=not DEBUG,
        )
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedStaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
