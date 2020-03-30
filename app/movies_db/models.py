from django.db.models import *

# Create your models here.


class Movie(Model):
    objects = Manager()
    title = CharField(max_length=200)
    link = CharField(max_length=200, blank=True)
    subtitle = CharField(max_length=200, blank=True)
    watched = CharField(max_length=3, default="No", blank=True)
    date = DateTimeField(null=True, blank=True)
    review = CharField(max_length=500, blank=True)
    other = CharField(max_length=200, blank=True)

