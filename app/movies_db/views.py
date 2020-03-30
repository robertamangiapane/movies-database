from django.shortcuts import render
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
        form.save()

        # if form.is_valid():
    return render(request, 'movies_db/add.html')


def movie(request):
    return HttpResponse("View a selected movie")


def edit(request):
    return HttpResponse("Edit a selected movie")