from django.shortcuts import render
from .models import Movie

def homepage(request):
    movies = Movie.objects.all()
    return render(request, 'core/homepage.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    return render(request, 'core/movie_detail.html', {'movie': movie})


def rules(request):
    return render(request, 'core/rules.html')
