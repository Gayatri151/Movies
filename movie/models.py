from django.db import models

# Create your models here.



class Movie(models.Model):
    movie_name=models.CharField(max_length=100)
    ratings=models.FloatField(default=0)
    description=models.TextField()
    release_date=models.DateField()
    actor_name=models.CharField(max_length=100)
    director_name=models.CharField(max_length=100)


    def __str__(self):
        return self.movie_name
