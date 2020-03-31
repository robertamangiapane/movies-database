from django.core.exceptions import ValidationError
from django.test import Client
from django.test import TestCase
from .models import Movie
from django import forms


class FeatureTestInfrastructure(TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_movies(self):
        movie1 = Movie("First Movie", "html", "html", "yes", "02-04-2019", "good", "")
        movie2 = Movie("Second Movie", "html", "html", "yes", "02-04-2019", "good", "")

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn(movie1.title, response_text)
        self.assertIn(movie2.title, response_text)

    def test_add_page_adds_movie(self):
        self.client.post('/add/', {'title': "Added Movie", 'link': "html", 'subtitle': "html", 'watched': "", "date": "", "review": "", "other": ""})

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn("Added Movie", response_text)

    def test_added_movie_redirect_to_home(self):
        response = self.client.post('/add/', {'title': "Added Movie", 'link': "html", 'subtitle': "html", 'watched': "", "date": "", "review": "", "other": ""})

        self.assertRedirects(response, '/')

    def test_cannot_add_page_adds_movie(self):

        with self.assertRaises(ValidationError):
            self.client.post('/add/',
                             {'title': "", 'link': "html", 'subtitle': "html", 'watched': "", "date": "", "review": "",
                              "other": ""})

    def test_view_movies(self):
        response = self.client.get('/movie/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"View a selected movie")

    def test_edit_movies(self):
        response = self.client.get('/edit/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Edit a selected movie")

