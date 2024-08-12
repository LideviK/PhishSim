"""PhishSim URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.contrib import admin
from django.conf.urls.static import static
from django.conf.urls import include, url

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .environment import ENVIRONMENT

# ---------------- SWAGGER API SCHEMA CONFIG --------------------
schema_view = get_schema_view(
    openapi.Info(
        title="PhishSim API",
        default_version='v1',
        description="PhishSim",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@phishsim.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
# ---------------------------------------------------------------

urlpatterns = [

    # core
    # url(r'^allauth/', include('allauth.urls')),
    # url(r'^admin/', admin.site.urls),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration', include('rest_auth.registration.urls')),
    url(r'^account/', include('allauth.urls')),
    url(r'^admin/', admin.site.urls),

    # API v1
    # url(r'^auth/', include("v1.accounts.urls")),
    # url(r'^', include("v1.accounts.urls")),
    # url(r'^company/', include("v1.company.urls")),
    # url(r'^user/', include("v1.user.urls")),

]

# add static dir path to the pattern
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if ENVIRONMENT == 'local' or ENVIRONMENT == 'dev':
    # ------------ IF LOCAL or DEV IMPORT THE DEBUG TOOLBAR --------------
    import debug_toolbar

    urlpatterns = [
                      url(r"^__debug__/", include(debug_toolbar.urls)),
                  ] + urlpatterns
    # -------------------------------------------------------------

    # ------------------- IF LOCAL or DEV ADD THE SWAGGER API DOC --------------------------------------
    urlpatterns += [

        url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    ]
    # ---------------------------------------------------------------------------------------------------
