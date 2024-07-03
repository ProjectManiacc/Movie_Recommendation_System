from django.shortcuts import render
from movie_app.models import Movies
from review_app.models import Reviews
from django.http import JsonResponse
from django import forms


def homepage(request):
    popular_movies = Movies.get_popular_movies()
    latest_reviews = Reviews.get_latest_review()
    context = {
        'popular_movies': popular_movies,
        'latest_reviews': latest_reviews,
        'range': range(1, 6)  # Dodajemy listę range do kontekstu
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')


def search_view(request):
    query = request.GET.get('q', '').strip()
    movies = Movies.objects.filter(title__icontains=query).distinct('title') if query else []
    return render(request, 'search_results.html', {'movies': movies})

def search_movies(request):
    query = request.GET.get('q', '').strip()
    if query:
        movies = Movies.objects.filter(title__icontains=query).distinct('title')[:8]
        results = [{'title': movie.title} for movie in movies]
        return JsonResponse(results, safe=False)
    return JsonResponse({'message': 'No results found'}, status=404)



