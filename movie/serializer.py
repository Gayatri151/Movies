from rest_framework import serializers
from .models import Movie

class Movieserializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ["movie_name","ratings","description","release_date",
                  "actor_name","director_name"]