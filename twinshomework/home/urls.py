from django.urls import path
from . import views


app_name = 'home'  # done for namespacing URLs.

urlpatterns = [
    path("", views.homepage, name="homepage"),

]