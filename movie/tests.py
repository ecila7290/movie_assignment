import json

from django.test import TestCase, Client

from .models import Genre, Movie, MainSub, Cast, MovieCast

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
        MainSub.objects.bulk_create([
            MainSub(id=1,
            name='main'),
            MainSub(id=2,
            name='sub')
        ])
        Cast.objects.bulk_create([
            Cast(id=1,
            name='john',
            image_url='johnimage.com'),
            Cast(id=2,
            name='ann',
            image_url='annimage.com')
        ])
        MovieCast.objects.bulk_create([
            MovieCast(id=1,
            movie_id=1,
            cast_id=1,
            mainsub_id=1,
            role_name='johnson'),
            MovieCast(id=2,
            movie_id=1,
            cast_id=2,
            mainsub_id=1,
            role_name='annie')
        ])

    def tearDown(self):
        Genre.objects.all().delete()
        Movie.objects.all().delete()
        MainSub.objects.all().delete()
        Cast.objects.all().delete()
        MovieCast.objects.all().delete()

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
                },
                'casts':[{
                    'name'     : 'john',
                    'role_name': 'johnson',
                    'mainsub'  : 'main',
                    'image'    : 'johnimage.com'
                }, {
                    'name'     : 'ann',
                    'role_name': 'annie',
                    'mainsub'  : 'main',
                    'image'    : 'annimage.com'
                }]
            }
        )
    
    def test_movie_detail_get_not_found(self):
        client=Client()
        response=client.get('/movies/999')

        self.assertEqual(response.status_code,404)
        self.assertEqual(response.json(),
            {'message':'Movie does not exist.'}
        )