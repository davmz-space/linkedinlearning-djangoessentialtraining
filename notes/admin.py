from django.contrib import admin

from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'created')

## register that the notes model is attached to this admin model 
admin.site.register(models.Notes, NotesAdmin)