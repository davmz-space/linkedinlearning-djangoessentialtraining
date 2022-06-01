from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    ## if user is deleted all notes related under that user is deleted
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")