import json

from django.test import TestCase, Client

from .models import Genre, Movie, MainSub, Cast, MovieCast

class AllMoviesTest(TestCase):
    def setUp(self):
        Genre.objects.create(
            id=1,
            name='drama'
        )
        Movie.objects.create(
            id=1,
            genre_id=1,
            title='movie',
            year=2020,
            country='US',
            stars=3.3,
            runtime=123,
            description='movie description',
            image_url='image.com'
        )
        MainSub.objects.create(
            id=1,
            name='main'
        )
        Cast.objects.create(
            id=1,
            name='john',
            image_url='johnimage.com'
        )
        MovieCast.objects.create(
            id=1,
            movie_id=1,
            cast_id=1,
            mainsub_id=1,
            role_name='johnson'
        )

    def tearDown(self):
        Genre.objects.all().delete()
        Movie.objects.all().delete()
        MainSub.objects.all().delete()
        Cast.objects.all().delete()
        MovieCast.objects.all().delete()

    def test_all_movies_get_success(self):
        client=Client()
        response=client.get('/movies')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),
            {'movies':
                [{
                    "movie_id": 1,
                    "title"   : 'movie',
                    "stars"   : '3.3',
                    "image"   : 'image.com',
                }]
            }
        )
        
    def test_all_movies_get_not_found(self):
        client=Client()
        response=client.get('/movie')

        self.assertEqual(response.status_code,404)