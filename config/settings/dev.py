# coding=utf-8
import boto3
from dotenv import load_dotenv

from .base import INSTALLED_APPS, STATIC_URL
from .base import *  # noqa: F401,F403


# ============================= CONFIG VARS =========================
DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')

LOCAL = False
SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1',
]

PRODUCT_NAME = "PhishSim"
# ==================================================================


# ======================= DATABASE ===============================
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PW'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
        'CONN_MAX_AGE': 0,
        'OPTIONS': {'sslmode': 'prefer'},

    }
}
# =================================================================


# ======================== INSTALLED APPS =====================
INSTALLED_APPS.append('drf_yasg')
# =============================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


