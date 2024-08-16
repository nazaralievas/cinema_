from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=255)
    description = models.TextField()
    
    def __str__(self):
        return self.name
