from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
]