from django.shortcuts import render, redirect
from .models import Movie
from .forms import ReviewForm


def homepage(request):
    context = {}
    q = request.GET.get('q')
    if q:
        context['movies'] = Movie.objects.filter(name__icontains=q)
    else:
        context['movies'] = Movie.objects.all()

    return render(request, 'core/homepage.html', context)


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


# регистрация, авторизация, logout -------------------
from .forms import RegistrationForm

def register(request):
    context = {}
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context['form'] = form
    else:
        context['form'] = RegistrationForm()

    return render(request, 'core/register.html', context)


from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
def login(request):
    if not request.user.is_authenticated:
        context = {}
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                user = form.get_user()
                auth.login(request, user)
                return redirect('homepage')
            context['form'] = form
        else:
            context['form'] = AuthenticationForm()
    else:
        return redirect('homepage')
    
    return render(request, 'core/login.html', context)


# from django.contrib.auth import logout
from django.contrib import auth
def logout(request):
    auth.logout(request)
    return redirect('homepage')