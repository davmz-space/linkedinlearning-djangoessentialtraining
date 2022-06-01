from doctest import DocFileSuite
from typing import List
from django.shortcuts import render

from .models import Notes
from django.http import Http404
from notes.forms import NotesForm
from django.views.generic import CreateView, DetailView, ListView

# Create your views here.
class NotesCreateView(CreateView):
    model = Notes
    fields = ['title', 'text']
    # form_class = NotesForm
    success_url = '/smart/notes'
    
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