from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
    path('notes/<int:pk>/edit', views.NotesUpdateView.as_view(), name="notes.update"),
    path('notes/new', views.NotesCreateView.as_view(), name="notes.new"),
]