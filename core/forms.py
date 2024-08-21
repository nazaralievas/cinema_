from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['comment']


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name']