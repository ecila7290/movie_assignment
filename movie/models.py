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
    stars       = models.DecimalField(max_digits=2, decimal_places=1)
    runtime     = models.IntegerField()
    description = models.TextField()
    image_url   = models.URLField(max_length=2000)

    class Meta:
        db_table='movies'

class MainSub(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table='mainsub'

class Cast(models.Model):
    name      = models.CharField(max_length=45)
    image_url = models.URLField(max_length=2000, null=True)

    class Meta:
        db_table='casts'

class MovieCast(models.Model):
    movie     = models.ForeignKey(Movie, on_delete=models.CASCADE)
    cast      = models.ForeignKey(Cast, on_delete=models.CASCADE)
    mainsub   = models.ForeignKey(MainSub, on_delete=models.SET_NULL, null=True)
    role_name = models.CharField(max_length=45)
    
    class Meta:
        db_table='movie_casts'