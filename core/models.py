from django.db import models


class Movie(models.Model):
    name = models.CharField(max_length=255)
    genre = models.CharField(max_length=200)
    poster = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


from django.contrib.auth.models import User

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    comment = models.TextField()
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Комментатор: {self.user.username} написал(а) отзыв на фильм {self.movie}"
