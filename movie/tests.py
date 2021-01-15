import json

from django.test import TestCase, Client

from .models import Genre, Movie

class MoviesTest(TestCase):
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

    def tearDown(self):
        Genre.objects.all().delete()
        Movie.objects.all().delete()

    def test_movies_get_success(self):
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

    def test_movies_get_not_found(self):
        client=Client()
        response=client.get('/movie')

        self.assertEqual(response.status_code,404)

    def test_movies_post_success(self):
        client=Client()
        movie={
            'title'      : 'post movie',
            'year'       : '2000',
            'genre'      : '1',
            'country'    : 'KR',
            'runtime'    : '124',
            'description': 'this is description',
            'image_url'  : 'www.url.com'
        }
        response=client.post('/movies', json.dumps(movie), content_type='application/json')
        
        self.assertEqual(response.status_code,201)
        self.assertEqual(response.json(),
            {'message':'Created successfully'}
        )
    
    def test_movies_post_fail(self):
        client=Client()
        movie={
            'title'      : 'movie',
            'year'       : '2000',
            'genre'      : '1',
            'country'    : 'KR',
            'runtime'    : '124',
            'description': 'this is description',
            'image_url'  : 'www.url.com'
        }
        response=client.post('/movies', json.dumps(movie), content_type='application/json')
        
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(),
            {'message':'Movie already exists.'}
        )

    def test_movies_post_key_error(self):
        client=Client()
        movie={
            'title'      : 'post movie',
            'year'       : '2000',
            'genre'      : '1',
            'country'    : 'KR',
            'runtime'    : '124',
            'description': 'this is description',
        }
        response=client.post('/movies', json.dumps(movie), content_type='application/json')
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(),
            {'message':"'image_url', Key Error"}
        )

class MovieDetailTest(TestCase):
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

    def tearDown(self):
        Genre.objects.all().delete()
        Movie.objects.all().delete()

    def test_movie_detail_get_success(self):
        client=Client()
        response=client.get('/movies/1')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),
            {'movie': {
                'title'      : 'movie',
                'year'       : 2020,
                'genre'      : 'drama',
                'country'    : 'US',
                'stars'      : '3.3',
                'runtime'    : 123,
                'description': 'movie description',
                'image'      : 'image.com'
                }
            }
        )
    
    def test_movie_detail_get_not_found(self):
        client=Client()
        response=client.get('/movies/999')

        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),
            {'message':'Movie does not exist.'}
        )

    def test_movie_detail_put_success(self):
        client=Client()
        movie={
            'title' : 'put movie'
        }
        response=client.put('/movies/1', movie, content_type='application/json')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),
            {
                'movie': {
                'title'      : 'put movie',
                'year'       : 2020,
                'genre'      : 'drama',
                'country'    : 'US',
                'stars'      : '3.3',
                'runtime'    : 123,
                'description': 'movie description',
                'image'      : 'image.com'
                }
            }
        )

    def test_movie_detail_put_no_field(self):
        client=Client()
        movie={
            'titl' : 'put movie'
        }
        response=client.put('/movies/1', movie, content_type='application/json')

        self.assertEqual(response.status_code,400)
        self.assertEqual(response.json(),
            {'message':"Movie has no field named 'titl'"}
        )
    
    def test_movie_detail_put_not_found(self):
        client=Client()
        movie={
            'title' : 'put movie'
        }
        response=client.put('/movies/999', movie, content_type='application/json')

        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),
            {'message':'Movie does not exist.'}
        )

    def test_movie_detail_delete_success(self):
        client=Client()
        response=client.delete('/movies/1')

        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(),
            {'message':'Deleted successfully'}
        )

    def test_movie_detail_delete_not_found(self):
        client=Client()
        response=client.delete('/movies/999')

        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),
            {'message':'Movie does not exist.'}
        )