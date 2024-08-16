from django.urls import path
from .views import homepage, rules, movie_detail

urlpatterns = [
    path('', homepage, name='homepage'),
    path('movie_detail/<int:id>', movie_detail, name='movie_detail'),
    path('rules', rules, name='rules')
]