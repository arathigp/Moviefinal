from django.contrib import auth
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):

    ACTIONSS = 'Actionss'
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=250)
    poster = models.ImageField(upload_to='gallery',blank=True, null=True)
    desc = models.TextField()
    release_date = models.DateField()
    actors = models.TextField()
    category = models.CharField(max_length=250,blank=True, null=True, choices=[
        ('Action', 'Action'),
        ('Drama', 'Drama'),
        ('Comedy', 'Comedy'),
        ('Others','Others')
        ])
    youtube_link = models.URLField(max_length=200)

    def __str__(self):
        return self.movie_title

class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField( validators=[MaxValueValidator(5), MinValueValidator(1)] ) # You can customize this based on your rating system

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}"