from django.shortcuts import render
from django.http import HttpResponse
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies_db/index.html', context)


def add(request):
    return HttpResponse("Add a movie to your database")


def movie(request):
    return HttpResponse("View a selected movie")


def edit(request):
    return HttpResponse("Edit a selected movie")