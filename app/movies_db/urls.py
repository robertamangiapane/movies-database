from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('add/movie', views.add, name='add_movie'),
    path('movie/', views.movie, name='movie'),
    path('edit/', views.edit, name='edit')
]