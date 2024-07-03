from django.urls import path
from . import views

app_name = 'movie_app'

urlpatterns = [
    path('', views.display_movies, name='movies'),
    path('details/<int:movie_id>/', views.display_movie_details, name='movie_details'),
    path('details/', views.display_sample_movie_details, name='sample_movie_details'),
]
