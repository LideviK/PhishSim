# coding=utf-8
from .base import *  # noqa: F401,F403

# ========================= CONFIG VARIABLES ==========================

DEBUG = True
DOMAIN = 'http://localhost:8000'
SITE_ID = 1

INTERNAL_IPS = [
    '127.0.0.1', '172.18.0.1'
]

# =====================================================================


# =========================== DATABASES ===============================
# --------------------------- POSTGRES ---------------------------------
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'ph',
#         'USER': 'admin',
#         'PASSWORD': 'Better123',
#         'HOST': 'localhost',
#     }
# }
# ----------------------------------------------------------------------
# -------------------------- SQL LITE ----------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# ----------------------------------------------------------------------
# ======================================================================


# ================== INSTALLED APPS ==========================
# INSTALLED_APPS.append('django_extensions')
INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('drf_yasg')
# ============================================================


# ========================== MIDDLEWARES ===============================
MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware', )
# ======================================================================


# =========================== AUTENTICATION =========================
# AUTHENTICATION_BACKENDS = (
#     # default
#     'django.contrib.auth.backends.ModelBackend',
#     # email login
#     'allauth.account.auth_backends.AuthenticationBackend',
# )
# ===================================================================


# ========================== HOSTS ==================================
ALLOWED_HOSTS = ["*"]
# ===================================================================

# ========================== EMAIL CONFIG ===========================
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# ===================================================================

# ==================== DEBUG TOOLBAR CONFIG =========================

def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# ===================================================================


AUTHENTICATION_BACKENDS = (
    # default
    'django.contrib.auth.backends.ModelBackend',
    # email login
    'allauth.account.auth_backends.AuthenticationBackend',
)
