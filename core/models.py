from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=100)
    poster = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    name = models.CharField(max_length=200)
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
