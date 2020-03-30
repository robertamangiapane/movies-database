from django import forms
from django.forms import ModelForm
from .models import Movie


class AddMovieForm(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'link', 'subtitle', 'watched', 'date', 'review', 'other']

