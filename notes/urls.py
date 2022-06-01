from django.urls import URLPattern, path

from . import views

urlpatterns = [
    path('notes', views.NoteListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
]