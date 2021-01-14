import json

from django.views import View
from django.http import JsonResponse

from .models import Movie, MovieCast

class MoviesView(View):
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

    def post(self, request):
        try:
            data=json.loads(request.body)

            if Movie.objects.filter(title=data['title']).exists():
                return JsonResponse({'message':'Movie already exists.'}, status=400)
            
            Movie.objects.create(
                title       = data['title'],
                year        = data['year'],
                genre_id    = data['genre'],
                country     = data['country'],
                runtime     = data['runtime'],
                description = data['description'],
                image_url   = data['image_url']
            )

            return JsonResponse({'message':'Created successfully'}, status=201)

        except KeyError as e:
            return JsonResponse({'message':f"{e}, Key Error"}, status=400)

class MovieDetailView(View):
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
