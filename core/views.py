from django.shortcuts import render, redirect
from .models import Movie, Review
from .forms import ReviewForm


def homepage(request):
    q = request.GET.get('q')
    if q:
        movies = Movie.objects.filter(name__icontains=q)
    else:
        movies = Movie.objects.all()

    return render(request, 'core/homepage.html', {'movies': movies})


def movie_detail(request, id):
    movie = Movie.objects.get(id=id)
    reviews = movie.reviews.all().order_by('-date_created')

    if request.method == "POST":
        if request.user.is_authenticated:
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.movie = movie
                review.user = request.user
                review.save()
                return redirect('movie_detail', id = movie.id)
        else:
            return redirect('homepage')
    else:
        form = ReviewForm()

    return render(request, 'core/movie_detail.html', {'movie': movie, 'reviews': reviews, 'form': form})


def rules(request):
    return render(request, 'core/rules.html')
