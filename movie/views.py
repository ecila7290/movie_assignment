import json

from django.views import View
from django.http import JsonResponse

from .models import Movie, MovieCast

class AllMoviesView(View):
    def get(self, request):
        movies=Movie.objects.all()

        data={'movies':
            [{
                "movie_id": movie.id,
                "title"   : movie.title,
                "stars"   : movie.stars,
                "image"   : movie.image_url,
            } for movie in movies]
        }

        return JsonResponse(data, status=200)

class MovieView(View):
    def get(self, request, movie_id):
        try:
            movie = Movie.objects.select_related('genre').get(id=movie_id)
            casts = MovieCast.objects.select_related('movie', 'cast','mainsub').filter(movie_id=movie_id).order_by('id')

            data  = {
                'movie':{
                    'title'      : movie.title,
                    'year'       : movie.year,
                    'genre'      : movie.genre.name,
                    'country'    : movie.country,
                    'stars'      : movie.stars,
                    'runtime'    : movie.runtime,
                    'description': movie.description,
                    'image'      : movie.image_url
                },
                'casts': 
                    [{
                        'name'     : cast.cast.name,
                        'role_name': cast.role_name,
                        'mainsub'  : cast.mainsub.name,
                        'image'    : cast.cast.image_url
                    } for cast in casts]
                
            }
            
            return JsonResponse(data, status=200)

        except Movie.DoesNotExist:
            return JsonResponse({'message':'Movie does not exist.'}, status=404)