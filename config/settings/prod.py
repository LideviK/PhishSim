# coding=utf-8
import boto3

from .base import INSTALLED_APPS, STATIC_URL
from .base import *  # noqa: F401,F403




# ============================= CONFIG VARS =========================
DEBUG = False

LOCAL = False
SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1',
]


SECRET_KEY = os.getenv('SECRET_KEY')

# FRONTEND_BASE_URL = 'https://app.falconcloud.io'
# PRODUCT_NAME = "VistaSOC"


# ====================================================================


# ========================= DATABASES ==============================
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
# ===================================================================


# ======================== INSTALLED APPS =====================
INSTALLED_APPS.append('raven.contrib.django.raven_compat')
# =============================================================



# ========================= DJANGO RESET FRAMEWORK CONFIG ===================
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
}
# ===========================================================================
