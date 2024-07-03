"""
URL configuration for movie_recommendation project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('admin/', admin.site.urls, name='admin'),
    path('movies/', include('movie_app.urls'), ),
    path('users/', include('user_app.urls')),
    path('reviews/', include('review_app.urls')),
    path('search/', views.search_view, name='search'),
    path('movies/', include(('movie_app.urls', 'movie_app'), namespace='movie_app')),
    path('movies/search/', views.search_movies, name='search_movies'),


]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
