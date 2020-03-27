from django.db import models

# Create your models here.


class Movie(models.Model):
    movie = models.CharField(max_length=200)
    link = models.CharField(max_length=200)
    subtitle_link = models.CharField(max_length=200)
    watched = models.CharField(max_length=3, default="No")
    watched_on = models.DateTimeField()
    review = models.CharField(max_length=500)
    other = models.CharField(max_length=200)
