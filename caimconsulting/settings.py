"""
Django settings for caimconsulting project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# To use local environment variables
from dotenv import load_dotenv

# https://devcenter.heroku.com/articles/django-app-configuration
import django_heroku

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    load_dotenv(dotenv_file)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.environ.get("DEBUG", "") != "False"

# https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/#https
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

ALLOWED_HOSTS = ["caim-consulting.herokuapp.com"]


# Application definition

INSTALLED_APPS = [
    "mainsite.apps.MainsiteConfig",
    "blog.apps.BlogConfig",
    "accounts.apps.AccountsConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "cloudinary_storage",  # https://pypi.org/project/django-cloudinary-storage/ (using only for media)
    "cloudinary",
    "tinymce",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # https://warehouse.python.org/project/whitenoise/
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


ROOT_URLCONF = "caimconsulting.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["caimconsulting/templates/"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "blog.context_processors.all_categories",
                "mainsite.context_processors.all_services",
                "mainsite.context_processors.all_advisors",
                "mainsite.context_processors.all_clients",
            ],
        },
    },
]

WSGI_APPLICATION = "caimconsulting.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
#     }
# }

# https://devcenter.heroku.com/articles/heroku-postgresql#connecting-with-django
# DATABASES = {}
# DATABASES["default"] = dj_database_url.config(conn_max_age=600, ssl_require=True)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, "static")

STATIC_URL = "/static/"

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = [
    # os.path.join(BASE_DIR, "static"),
    "caimconsulting/static/",
    "mainsite/static/",
    "accounts/static/",
    # "blog/static/",
]

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# https://docs.djangoproject.com/en/3.0/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# https://docs.djangoproject.com/en/3.0/ref/settings/#media-url
MEDIA_URL = "/media/"

# For storing user-uploaded media
# https://www.dothedev.com/blog/heroku-django-store-your-uploaded-media-files-for-free/
# https://pypi.org/project/django-cloudinary-storage/
CLOUDINARY_STORAGE = {
    "CLOUD_NAME": os.getenv("CLOUDINARY_CLOUD_NAME"),
    "API_KEY": os.getenv("CLOUDINARY_API_KEY"),
    "API_SECRET": os.getenv("CLOUDINARY_API_SECRET"),
}
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"

# Login redirect URL for accounts
LOGIN_REDIRECT_URL = "profile"

# Default User profile
AUTH_USER_MODEL = "accounts.User"

# Activate Django-Heroku.
# Refer: https://github.com/heroku/django-heroku/blob/master/django_heroku/core.py
# for full information on what settings are overwritten
django_heroku.settings(locals())

# Heroku Postgres requires SSL, but SQLite doesn’t need or expect it.
# Added for local development using SQLite
# https://blog.usejournal.com/deploying-django-to-heroku-connecting-heroku-postgres-fcc960d290d1
options = DATABASES["default"].get("OPTIONS", {})  # noqa: F821
options.pop("sslmode", None)
