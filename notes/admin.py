from django.contrib import admin

from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    pass

## register that the notes model is attached to this admin model 
admin.site.register(models.Notes, NotesAdmin)