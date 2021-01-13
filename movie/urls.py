from django.urls import path

from .views import AllMoviesView, MovieView

urlpatterns = [
    path('movies', AllMoviesView.as_view()),
    path('movies/<int:movie_id>', MovieView.as_view())
]
