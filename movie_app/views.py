from django.shortcuts import render
from .models import Movies
from review_app.models import Reviews
from django.http import JsonResponse
from django import forms


# Create your views here.

def display_movies(request):
    movies_details = Movies.get_movies_head()
    return render(request, 'movies.html', {'movies_details': movies_details})


def display_movie_details(request, movie_id):
    movie_details = Movies.get_movie_details(movie_id)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)
def display_sample_movie_details(request):
    movie_details = Movies.get_movie_details(1)
    reviews = Reviews.get_review_for_movie(movie_details['movie'])
    context = {
        'movie_details': movie_details,
        'reviews': reviews
    }
    return render(request, 'movie_details.html', context=context)



