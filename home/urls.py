from django.urls import path
from . import views

urlpatterns = [
    # Added URLS
    path('home', views.home),
    path('authorized', views.authorized)
]