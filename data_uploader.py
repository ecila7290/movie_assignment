import os
import django
import csv
import sys

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie_assignment.settings')
django.setup()

from movie.models import Genre, Movie

# upload sample movie data
def upload_data():
    if not Genre.objects.filter().exists():
        Genre.objects.bulk_create([
            Genre(name='Drama'),
            Genre(name='Action'),
            Genre(name='Fantasy'),
        ])
    Movie.objects.bulk_create([
        Movie(title='School of rock', year=2003, genre_id=1, country='US', stars=3.8, runtime=108, description='Movie school of rock', image_url='rockimage.com'),
        Movie(title='Baby driver', year=2017, genre_id=2, country='US', stars=3.7, runtime=113, description='Movie baby driver', image_url='driverimage.com'),
        Movie(title='Kings speech', year=2010, genre_id=2, country='UK', stars=3.7, runtime=118, description='Movie kings speech', image_url='speechimage.com')  
    ])
    print('Uploaded successfully')

upload_data()