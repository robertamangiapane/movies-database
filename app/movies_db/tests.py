import unittest
from django.test import Client


class FeatureTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_homepage(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b"You're at the movies database home.")

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

