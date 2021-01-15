from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        db_table='genres'

class Movie(models.Model):
    title       = models.CharField(max_length=200)
    year        = models.IntegerField()
    genre       = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    country     = models.CharField(max_length=40)
    stars       = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)
    runtime     = models.IntegerField()
    description = models.TextField()
    image_url   = models.URLField(max_length=2000)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    class Meta:
        db_table='movies'