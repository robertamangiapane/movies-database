from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Movie
from .movie_form import AddMovieForm


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies_db/index.html', context)


def add(request):
    if request.method == "POST":
        form = AddMovieForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            raise ValidationError("Movie must have a title")

    return render(request, 'movies_db/add.html')


def movie(request):
    return HttpResponse("View a selected movie")


def edit(request):
    return HttpResponse("Edit a selected movie")