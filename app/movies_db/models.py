from django.db.models import *

# Create your models here.


class Movie(Model):
    objects = Manager()
    title = CharField(max_length=200)
    link = CharField(max_length=200)
    subtitle = CharField(max_length=200)
    watched = CharField(max_length=3, default="No")
    date = DateTimeField()
    review = CharField(max_length=500)
    other = CharField(max_length=200)

    # @classmethod
    # def create(cls, title, link, subtitle, watched, date, review, other):
    #     movie = cls(title=title, link=link, subtitle=subtitle, watched=watched, date=date, review=review, other=other)
    #     return movie
