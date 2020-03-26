from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the movies database home.")


def add(request):
    return HttpResponse("Add a movie to your database")


def movie(request):
    return HttpResponse("View a selected movie")


def edit(request):
    return HttpResponse("Edit a selected movie")