# user urls

from django.conf.urls import include, url

from .views import TestRoute



urlpatterns = [

    url(r'^test/', view=TestRoute.as_view()),

]
