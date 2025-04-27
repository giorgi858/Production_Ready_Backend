from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    
    def __str__(self) :
        return f'{self.content[0:50]} by {self.author.username}'
    
