"""
Django settings for python_portfolio project.
"""

from pathlib import Path
import os
import dj_database_url

# ✅ Base directory of your project
BASE_DIR = Path(__file__).resolve().parent.parent

# ✅ Secret Key from Environment (or fallback)
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-insecure-fallback-key")

# ✅ Debug Mode (Turn off in production!)
DEBUG = os.getenv("DEBUG", "False") == "True"

# ✅ Hosts allowed to serve the app
ALLOWED_HOSTS = ['*']  # Change to specific domain in production

# ✅ Installed applications
INSTALLED_APPS = [
    "core",  # Your app
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
]

# ✅ Middleware (includes WhiteNoise for static files)
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

ROOT_URLCONF = "python_portfolio.urls"

# ✅ Template settings
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / 'core' / 'templates'],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "python_portfolio.wsgi.application"

# ✅ Default to SQLite, switch to Postgres if DATABASE_URL is found
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
if "DATABASE_URL" in os.environ:
    DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)

# ✅ Password validation
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ✅ Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ✅ Static files config for production (WhiteNoise compatible)
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'python_portfolio' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# ✅ Recommended settings for WhiteNoise
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ✅ Default auto field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
