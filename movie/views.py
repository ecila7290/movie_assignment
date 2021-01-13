import json

from django.views import View
from django.http import JsonResponse

from .models import Movie

class AllMoviesView(View):
    def get(self, request):
        movies=Movie.objects.all()

        data={'movies':
            [{
                "movie_id":movie.id,
                "title":movie.title,
                "stars":movie.stars,
                "image":movie.image_url,
            } for movie in movies]
        }

        return JsonResponse(data, status=200)

class MovieView(View):
    def get(self, request, movie_id):
        movie=Movie.objects.get(id=movie_id)

        data={
            'movie':{
                'title':movie.title,
                'year':movie.year,
                'genre':movie.genre.name,
                'country':movie.country,
                'stars':movie.stars,
                'runtime':movie.runtime,
                'description':movie.description,
                'image':movie.image_url
            }
        }

        return JsonResponse(data, status=200)