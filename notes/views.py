from doctest import DocFileSuite
from typing import List
from django.shortcuts import render

from .models import Notes
from django.http import Http404
from notes.forms import NotesForm
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from django.views.generic.edit import DeleteView

# Create your views here.
class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm

class NotesCreateView(CreateView):
    model = Notes
    success_url = '/smart/notes'
    form_class = NotesForm
        
class NoteListView(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html', {'notes': all_notes})

class NotesDetailView(DetailView):
    model = Notes
    context_object_name = "note"

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
        
#     return render(request, 'notes/notes_detail.html', {'note': note})