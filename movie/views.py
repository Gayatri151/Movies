from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializer import Movieserializer
from .models import Movie

# Create your views here.
class moviecreate(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):

        movieserializer = Movieserializer(data=request.data)
        if movieserializer.is_valid():
            movieserializer.save()
            return Response(movieserializer.data)
        return Response(movieserializer.errors)


class UpdateMovie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self, request,pk):
        try:
            movie = Movie.objects.get(id=pk)
            movieserializer = Movieserializer(movie,data=request.data)
            if movieserializer.is_valid():
                movieserializer.save()
                return Response(movieserializer.data)
            return Response(movieserializer.errors)
        except:
            return Http404

class DeleteMovie(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def delete(self, request,pk):
        try:
            movie = Movie.delete(pk=id)
            return Response("data deleted")
        except:
            return Http404

class MovieList(APIView):
    def get(self, request):
        movie = Movie.objects.all()
        serializer = Movieserializer(movie, many=True)
        return Response(serializer.data)


class MovieSearch(APIView):
    def get(self,request,name):
        movie = Movie.objects.filter(movie_name__icontains=name)
        serializer = Movieserializer(movie, many=True)
        return Response(serializer.data)


