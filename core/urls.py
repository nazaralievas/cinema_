from django.urls import path
from .views import homepage, rules

urlpatterns = [
    path('', homepage, name='homepage'),
    path('rules', rules, name='rules')
]