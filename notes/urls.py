from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
]