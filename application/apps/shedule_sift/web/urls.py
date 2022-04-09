from django.urls import path

from . import views


# Register your urls here

urlpatterns = [path("", views.simple_view)]

# To register this URLS
# path("shedule_sift/", include("apps.shedule_sift.web.urls"))
