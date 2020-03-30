import unittest
from django.test import Client

from .models import Movie


class FeatureTestInfrastructure(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage_displays_all_movies(self):
        movie1 = Movie("First Movie", "html", "html", "yes", "02-04-2019", "good", "")
        movie2 = Movie("First Movie", "html", "html", "yes", "02-04-2019", "good", "")

        response = self.client.get('/')
        response_text = response.content.decode("utf-8")

        self.assertIn(movie1.title, response_text)
        self.assertIn(movie2.title, response_text)

    def test_add_movies(self):
        response = self.client.get('/add/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Add a movie to your database")

    def test_view_movies(self):
        response = self.client.get('/movie/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"View a selected movie")

    def test_edit_movies(self):
        response = self.client.get('/edit/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"Edit a selected movie")

